// src/content.config.ts
import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders"; // Nuevo en Astro 5

const blog = defineCollection({
  // El loader le dice a Astro dónde buscar los archivos
  loader: glob({ pattern: "**/[^_]*.{md,mdx}", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.coerce.date(), // coerce asegura que el texto se convierta a objeto Date
    description: z.string().optional(),
    referenceUrl: z.string().url().optional(),
  }),
});

export const collections = { blog };
