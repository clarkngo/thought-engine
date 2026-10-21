// Renders an animated SVG to GIF + MP4 beside it, frame by frame (deterministic, no screen recording).
//
//   npm run render -- content/posts/<slug>/visual.svg [--duration 6] [--fps 30]
//
// Needs Chrome (set CHROME_PATH if it isn't in the default macOS location) and ffmpeg on PATH.
import { execFileSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { pathToFileURL } from "node:url";
import puppeteer from "puppeteer-core";

const args = process.argv.slice(2);
const svgPath = args.find((a) => !a.startsWith("--"));
const opt = (name, fallback) => {
  const i = args.indexOf(`--${name}`);
  return i === -1 ? fallback : Number(args[i + 1]);
};
if (!svgPath) {
  console.error("Usage: npm run render -- <path/to/visual.svg> [--duration 6] [--fps 30]");
  process.exit(1);
}

const duration = opt("duration", 6); // seconds; must match the SVG's loop length
const fps = opt("fps", 30);
const size = 1080; // LinkedIn 1:1
const gifWidth = 720;
const gifFps = 15;

const outBase = svgPath.replace(/\.svg$/, "");
const frames = mkdtempSync(path.join(tmpdir(), "render-"));

const browser = await puppeteer.launch({
  executablePath: process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  headless: true,
});
try {
  const page = await browser.newPage();
  await page.setViewport({ width: size, height: size });
  await page.goto(pathToFileURL(path.resolve(svgPath)).href);
  await page.evaluate((s) => {
    const svg = document.documentElement;
    svg.setAttribute("width", s);
    svg.setAttribute("height", s);
    document.getAnimations().forEach((a) => a.pause());
  }, size);

  const total = Math.round(duration * fps);
  for (let i = 0; i < total; i++) {
    const ms = (i * 1000) / fps;
    await page.evaluate((t) => document.getAnimations().forEach((a) => (a.currentTime = t)), ms);
    await page.screenshot({ path: path.join(frames, `f${String(i).padStart(4, "0")}.png`) });
  }
  console.log(`Captured ${total} frames`);
} finally {
  await browser.close();
}

const input = ["-y", "-v", "error", "-framerate", String(fps), "-i", path.join(frames, "f%04d.png")];

execFileSync("ffmpeg", [
  ...input,
  "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart",
  `${outBase}.mp4`,
], { stdio: "inherit" });

execFileSync("ffmpeg", [
  ...input,
  "-vf",
  `fps=${gifFps},scale=${gifWidth}:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64[p];[b][p]paletteuse=dither=none`,
  "-loop", "0",
  `${outBase}.gif`,
], { stdio: "inherit" });

rmSync(frames, { recursive: true, force: true });
console.log(`Wrote ${outBase}.mp4 and ${outBase}.gif`);
