// @ts-check
import fs from "node:fs";
import path from "node:path";
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite"; // Usaremos solo esto
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import sitemap from "@astrojs/sitemap";

// `lastmod` por post para el sitemap. No se puede usar `astro:content` desde
// aquí, así que se lee el `pubDate` del frontmatter a pelo. Sin esta señal
// Google no tiene forma de saber qué ha cambiado y difiere el rastreo — que es
// justo lo que Search Console reporta como "Descubierta: actualmente sin indexar".
const BLOG_DIR = "./src/content/blog";
const lastmodPorSlug = new Map(
  fs
    .readdirSync(BLOG_DIR)
    .filter((f) => /\.mdx?$/.test(f) && !f.startsWith("_"))
    .map((f) => {
      const frontmatter = fs.readFileSync(path.join(BLOG_DIR, f), "utf8");
      const fecha = frontmatter.match(/^pubDate:\s*['"]?(\d{4}-\d{2}-\d{2})/m);
      return [f.replace(/\.mdx?$/, ""), fecha?.[1]];
    })
    .filter(([, fecha]) => fecha)
);

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
  // El sitemap y los canonicals siempre han emitido barra final; los enlaces de
  // los componentes no, así que cada clic interno pasaba por un 301. Con esto
  // Astro avisa en dev si vuelve a colarse una URL sin barra.
  trailingSlash: "always",
  // /categoria/electronica/ existió hasta el 2026-08-11, cuando se unificó la
  // categoría duplicada por la tilde. Llegó a estar en el sitemap enviado a
  // Search Console, así que se redirige en vez de dejarla morir en un 404.
  // El destino lleva barra final: sin ella la cadena era 301 → meta-refresh →
  // 301, tres saltos para llegar al mismo sitio.
  redirects: {
    "/categoria/electronica": "/categoria/electrónica/",
  },
  integrations: [
    sitemap({
      serialize(item) {
        const slug = item.url.match(/\/blog\/([^/]+)\/$/)?.[1];
        const lastmod = slug && lastmodPorSlug.get(decodeURIComponent(slug));
        // Solo los posts llevan lastmod: en las páginas fijas y las de
        // categoría sería una fecha inventada, y una fecha falsa vale menos
        // que ninguna.
        return lastmod ? { ...item, lastmod } : item;
      },
    }),
  ],
});
