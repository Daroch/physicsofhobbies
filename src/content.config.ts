// src/content.config.ts
import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders"; // Nuevo en Astro 5

const roundupProduct = z.object({
  name: z.string(),
  tier: z.string().optional(),
  image: z.string(),
  amazonUrl: z.string().url(),
  price: z.number().optional(),
  rating: z.number().optional(),
  reviews: z.number().optional(),
  highlight: z.string(),
});

const blog = defineCollection({
  // El loader le dice a Astro dónde buscar los archivos
  loader: glob({ pattern: "**/[^_]*.{md,mdx}", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.coerce.date(),
    description: z.string(),
    category: z.string().default("General"),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
    amazonUrl: z.string().url().optional(),
    type: z.enum(["single", "roundup"]).default("single"),
    products: z.array(roundupProduct).optional(),
  }),
});

export const collections = { blog };
