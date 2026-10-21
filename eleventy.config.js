import { HtmlBasePlugin } from "@11ty/eleventy";

// Drafts are visible locally and left out of the production build (ELEVENTY_ENV=production).
const isProduction = process.env.ELEVENTY_ENV === "production";

export default function (eleventyConfig) {
  // Rewrites root-relative URLs ("/visuals/") to include pathPrefix.
  eleventyConfig.addPlugin(HtmlBasePlugin);

  // Post visuals live beside each post: content/posts/<slug>/visual.gif, carousel.pdf, ...
  eleventyConfig.addPassthroughCopy("content/posts/**/*.{gif,png,jpg,jpeg,webp,svg,mp4,webm,pdf}");
  eleventyConfig.addPassthroughCopy("content/assets");

  // linkedin.md holds the copy-paste LinkedIn text; it isn't a site page.
  eleventyConfig.ignores.add("content/posts/*/linkedin.md");

  eleventyConfig.addPreprocessor("drafts", "md,njk", (data) => {
    if (data.draft && isProduction) return false;
  });

  eleventyConfig.addCollection("posts", (collectionApi) =>
    collectionApi.getFilteredByGlob("content/posts/*/index.md").sort((a, b) => b.date - a.date)
  );

  eleventyConfig.addCollection("visuals", (collectionApi) =>
    collectionApi
      .getFilteredByGlob("content/posts/*/index.md")
      .filter((post) => post.data.visual)
      .sort((a, b) => b.date - a.date)
  );

  eleventyConfig.addFilter("isoDate", (date) => date.toISOString().slice(0, 10));
  eleventyConfig.addFilter("readableDate", (date) =>
    date.toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric", timeZone: "UTC" })
  );

  return {
    dir: { input: "content", includes: "_includes", data: "_data", output: "_site" },
    markdownTemplateEngine: "njk",
    // GitHub Pages project site: https://clarkngo.github.io/thought-engine/
    pathPrefix: "/thought-engine/",
  };
}
