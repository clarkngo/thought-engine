// Print an article page to PDF for Zenodo, with the animated visual frozen on one frame.
//
//   node scripts/article-pdf.mjs <article-slug> <out.pdf> [freeze-seconds]
//
// Needs the local site running (npm start). BASE defaults to http://localhost:8080/thought-engine.
// freeze-seconds picks the moment in the 6s loop to show (default 5.4, near the end of the loop).
import puppeteer from "puppeteer-core";

const [slug, out, freeze = "5.4"] = process.argv.slice(2);
if (!slug || !out) {
  console.error("Usage: node scripts/article-pdf.mjs <article-slug> <out.pdf> [freeze-seconds]");
  process.exit(1);
}
const base = process.env.BASE || "http://localhost:8080/thought-engine";

const browser = await puppeteer.launch({
  executablePath: process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
});
const page = await browser.newPage();
await page.goto(`${base}/articles/${slug}/`, { waitUntil: "networkidle0" });

// Inline each SVG visual as a data URL with every animation paused at the chosen moment.
await page.evaluate(async (t) => {
  const svgs = [...document.querySelectorAll("img")].filter((i) => i.src.endsWith(".svg"));
  for (const [n, img] of svgs.entries()) {
    let svg = await (await fetch(img.src)).text();
    const freezeCss = `* { animation-play-state: paused !important; animation-delay: -${t}s !important; }`;
    svg = svg.replace("</style>", `${freezeCss}</style>`);
    img.loading = "eager"; // lazy images below the fold never decode in a headless print
    img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg);
    await Promise.race([img.decode().catch(() => {}), new Promise((r) => setTimeout(r, 3000))]);
    if (n === 0) Object.assign(img.style, { maxHeight: "5.2in", width: "auto", margin: "0 auto", display: "block" });
  }
}, freeze);

await page.addStyleTag({
  content: `h2, h3 { break-after: avoid; page-break-after: avoid; }
    img, pre, li { break-inside: avoid; }
    pre, code { white-space: pre-wrap !important; word-break: break-all; overflow: visible !important; }`,
});
await page.pdf({
  path: out,
  format: "Letter",
  printBackground: true,
  margin: { top: "0.75in", bottom: "0.75in", left: "0.75in", right: "0.75in" },
});
await browser.close();
console.log(`Wrote ${out}`);
