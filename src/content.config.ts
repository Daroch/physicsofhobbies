// src/content.config.ts
import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders"; // Nuevo en Astro 5

const blog = defineCollection({
  // El loader le dice a Astro dónde buscar los archivos
  loader: glob({ pattern: "**/[^_]*.{md,mdx}", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.coerce.date(),
    description: z.string(),
    referenceUrl: z.string().url().optional(),
    image: z.string().optional(),
  }),
});

export const collections = { blog };
