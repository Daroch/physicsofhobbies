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
  site: "https://physicsofhobbies.com",
  base: "/",
  // /categoria/electronica/ existió hasta el 2026-08-11, cuando se unificó la
  // categoría duplicada por la tilde. Llegó a estar en el sitemap enviado a
  // Search Console, así que se redirige en vez de dejarla morir en un 404.
  redirects: {
    "/categoria/electronica": "/categoria/electrónica",
  },
  integrations: [sitemap()],
});
