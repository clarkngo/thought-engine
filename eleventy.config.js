import { readdirSync, readFileSync, existsSync } from "node:fs";
import path from "node:path";
import { HtmlBasePlugin } from "@11ty/eleventy";

// Drafts are visible locally and left out of the production build (ELEVENTY_ENV=production).
const isProduction = process.env.ELEVENTY_ENV === "production";

// Posts and articles share one folder layout: content/<section>/<YYYY-MM-DD-slug>/index.md + visual files.
const SECTIONS = ["posts", "articles"];

const slugify = (text) =>
  text
    .toLowerCase()
    .replace(/<[^>]+>/g, "")
    .replace(/&[a-z]+;/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

const contentFolders = (section) => {
  const dir = path.join("content", section);
  return existsSync(dir) ? readdirSync(dir).filter((f) => existsSync(path.join(dir, f, "index.md"))) : [];
};

// True when the folder's index.md front matter says `draft: true`.
function isDraftFolder(section, folder) {
  const text = readFileSync(path.join("content", section, folder, "index.md"), "utf8");
  const frontMatter = text.match(/^---\n([\s\S]*?)\n---/);
  return Boolean(frontMatter && /^draft:\s*true\s*$/m.test(frontMatter[1]));
}

// Reads content/<section>/*/linkedin.md into { post, firstComment } blocks for the local Studio page.
function readLinkedInCopy() {
  const entries = [];
  for (const section of SECTIONS) {
    const dir = path.join("content", section);
    if (!existsSync(dir)) continue;
    for (const slug of readdirSync(dir)) {
      const file = path.join(dir, slug, "linkedin.md");
      if (!existsSync(file)) continue;
      const text = readFileSync(file, "utf8");
      const sections = {};
      for (const part of text.split(/^## /m).slice(1)) {
        const [heading, ...body] = part.split("\n");
        sections[heading.trim().toLowerCase()] = body.join("\n").trim();
      }
      const title = (text.match(/^# LinkedIn copy: (.+)$/m) || [])[1] || slug;
      const files = readdirSync(path.join(dir, slug));
      entries.push({
        slug,
        title,
        url: `/${section}/${slug}/`,
        post: sections["post"] || "",
        firstComment: sections["first comment"] || "",
        downloads: files.filter((f) => /\.(gif|mp4|pdf)$/.test(f)).sort(),
      });
    }
  }
  return entries.sort((a, b) => b.slug.localeCompare(a.slug));
}

export default function (eleventyConfig) {
  // Rewrites root-relative URLs ("/visuals/") to include pathPrefix.
  eleventyConfig.addPlugin(HtmlBasePlugin);

  for (const section of SECTIONS) {
    // Copy each folder's visuals, but in production skip drafts so unposted work isn't reachable by URL.
    for (const folder of contentFolders(section)) {
      if (isProduction && isDraftFolder(section, folder)) continue;
      eleventyConfig.addPassthroughCopy(`content/${section}/${folder}/*.{gif,png,jpg,jpeg,webp,svg,mp4,webm,pdf}`);
    }
    // linkedin.md holds the copy-paste LinkedIn text; it isn't a site page.
    eleventyConfig.ignores.add(`content/${section}/*/linkedin.md`);
  }
  eleventyConfig.addPassthroughCopy("content/assets");

  eleventyConfig.addPreprocessor("drafts", "md,njk", (data) => {
    if (data.draft && isProduction) return false;
  });

  eleventyConfig.addGlobalData("linkedinCopy", readLinkedInCopy);

  const byDate = (a, b) => b.date - a.date;
  eleventyConfig.addCollection("posts", (api) => api.getFilteredByGlob("content/posts/*/index.md").sort(byDate));
  eleventyConfig.addCollection("articles", (api) => api.getFilteredByGlob("content/articles/*/index.md").sort(byDate));
  eleventyConfig.addCollection("visuals", (api) =>
    api
      .getFilteredByGlob(SECTIONS.map((s) => `content/${s}/*/index.md`))
      .filter((item) => item.data.visual)
      .sort(byDate)
  );

  // Folder name of a post/article (fileSlug drops the date prefix, so it can't be used to match `related`).
  eleventyConfig.addFilter("folder", (inputPath) => path.basename(path.dirname(inputPath)));
  eleventyConfig.addFilter("head", (items, n) => items.slice(0, n));
  eleventyConfig.addFilter("isoDate", (date) => date.toISOString().slice(0, 10));
  eleventyConfig.addFilter("citationDate", (date) => date.toISOString().slice(0, 10).replaceAll("-", "/"));
  eleventyConfig.addFilter("year", (date) => date.getUTCFullYear());
  eleventyConfig.addFilter("monthAbbr", (date) =>
    date.toLocaleDateString("en-US", { month: "short", timeZone: "UTC" }).toLowerCase()
  );
  eleventyConfig.addFilter("apaDate", (date) =>
    `${date.getUTCFullYear()}, ${date.toLocaleDateString("en-US", { month: "long", day: "numeric", timeZone: "UTC" })}`
  );
  eleventyConfig.addFilter("readableDate", (date) =>
    date.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric", timeZone: "UTC" })
  );
  eleventyConfig.addFilter("readingMinutes", (html) => {
    const words = String(html).replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length;
    return Math.max(1, Math.round(words / 230));
  });

  // Articles: give every <h2> an id, and list them for the table of contents.
  eleventyConfig.addFilter("headingIds", (html) =>
    String(html).replace(/<h2>(.*?)<\/h2>/g, (_, inner) => `<h2 id="${slugify(inner)}">${inner}</h2>`)
  );
  eleventyConfig.addFilter("toc", (html) =>
    [...String(html).matchAll(/<h2>(.*?)<\/h2>/g)].map(([, inner]) => ({
      id: slugify(inner),
      text: inner.replace(/<[^>]+>/g, ""),
    }))
  );

  return {
    dir: { input: "content", includes: "_includes", data: "_data", output: "_site" },
    markdownTemplateEngine: "njk",
    // GitHub Pages project site: https://clarkngo.github.io/thought-engine/
    pathPrefix: "/thought-engine/",
  };
}
