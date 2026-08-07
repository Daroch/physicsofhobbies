// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite"; // Usaremos solo esto
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  vite: {
    plugins: [tailwindcss()],
  },
  site: "https://physicshobbies.daroch.ovh",
  base: "/",
  integrations: [sitemap()],
});
