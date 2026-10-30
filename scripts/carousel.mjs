// Builds a LinkedIn carousel from a post's slides/slide-N.svg: carousel.pdf and cover.png beside them.
//
//   npm run carousel -- content/posts/<slug>
//
// Needs Chrome (set CHROME_PATH if it isn't in the default macOS location).
import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import puppeteer from "puppeteer-core";

const dir = process.argv[2];
if (!dir) {
  console.error("Usage: npm run carousel -- <path/to/post-folder>");
  process.exit(1);
}

const size = 1080; // LinkedIn 1:1
const slidesDir = path.join(dir, "slides");
const files = readdirSync(slidesDir)
  .filter((f) => /^slide-\d+\.svg$/.test(f))
  .sort((a, b) => parseInt(a.match(/\d+/)[0]) - parseInt(b.match(/\d+/)[0]));
const slides = files.map((f) => readFileSync(path.join(slidesDir, f), "utf8"));

// Each slide defines id="grid"; the first definition serves them all, and they're identical.
const html = `<!doctype html><meta charset="utf-8"><style>
  @page { size: ${size}px ${size}px; margin: 0; }
  html, body { margin: 0; }
  svg { display: block; break-after: page; }
  svg:last-child { break-after: auto; }
</style>${slides.join("\n")}`;

const browser = await puppeteer.launch({
  executablePath: process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  headless: true,
});
try {
  const page = await browser.newPage();
  await page.setViewport({ width: size, height: size });
  await page.setContent(html);
  await page.screenshot({ path: path.join(dir, "cover.png"), clip: { x: 0, y: 0, width: size, height: size } });
  await page.pdf({
    path: path.join(dir, "carousel.pdf"),
    width: `${size}px`,
    height: `${size}px`,
    printBackground: true,
  });
} finally {
  await browser.close();
}
console.log(`Wrote ${path.join(dir, "carousel.pdf")} (${slides.length} slides) and cover.png`);
