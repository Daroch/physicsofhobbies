// src/content.config.ts
import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders"; // Nuevo en Astro 5

const roundupProduct = z.object({
  name: z.string(),
  /** Identificador corto para la tabla: el título largo de Amazon la vuelve
   *  ilegible. Si falta, se usa `name`. */
  shortName: z.string().optional(),
  tier: z.string().optional(),
  image: z.string(),
  amazonUrl: z.string().url(),
  price: z.number().optional(),
  rating: z.number().optional(),
  reviews: z.number().optional(),
  /** Apartado 5: "según ficha, para quién es". Nunca experiencia de uso. */
  highlight: z.string(),
  /**
   * Apartado 4: specs ya normalizadas a las mismas unidades, en el mismo orden
   * que `comparison.columns`. Un hueco se escribe "no disponible" — nunca se
   * infiere un número que no esté en la ficha.
   */
  specs: z.array(z.string()).optional(),
});

const blogBase = {
  title: z.string(),
  pubDate: z.coerce.date(),
  // Solo para revisiones de fondo, y se rellena a mano. Alimenta el `lastmod`
  // del sitemap y el `dateModified` del JSON-LD. Google ignora el `lastmod` de
  // un sitio entero si detecta que las fechas se mueven sin que cambie el
  // contenido, así que una fecha de más cuesta más que una de menos.
  updatedDate: z.coerce.date().optional(),
  description: z.string(),
  // Lista cerrada: antes era texto libre y n8n generó "electronica" y
  // "electrónica" como categorías distintas (dos páginas /categoria/, una 404).
  category: z
    .enum(["acústica", "materiales", "electrónica", "óptica", "mecánica", "robótica", "general"])
    .default("general"),
  tags: z.array(z.string()).default([]),
  image: z.string().optional(),
  amazonUrl: z.string().url().optional(),
  // Nombre corto del producto para el bloque "Ver en Amazon". Sin él, el CTA
  // repetía el titular del artículo y no decía qué se estaba comprando.
  productName: z.string().optional(),
};

const blog = defineCollection({
  // El loader le dice a Astro dónde buscar los archivos
  loader: glob({ pattern: "**/[^_]*.{md,mdx}", base: "./src/content/blog" }),
  schema: z.object({
    ...blogBase,
    type: z.enum(["single", "roundup"]).default("single"),

    // ── Plantilla de roundup experto (Semana 2 del plan) ──────────────────
    // El orden de los apartados es deliberado: primero para quién es, luego
    // qué mirar y por qué, después cómo decidir, y solo entonces los productos.
    // Así el criterio va por delante de la recomendación, que es lo que separa
    // esto de una lista de afiliados.

    /** 1. A quién va dirigido. */
    audience: z.string().optional(),

    /** 2. Qué specs importan y por qué (el diferencial: significado físico). */
    specsThatMatter: z
      .array(z.object({ spec: z.string(), why: z.string() }))
      .optional(),

    /** 3. Cómo elegir según tu caso: "si haces X → prioriza Y". */
    chooseBy: z
      .array(z.object({ scenario: z.string(), priority: z.string() }))
      .optional(),

    /** 4. Cabeceras de la tabla comparativa; casan con `products[].specs`. */
    comparison: z
      .object({
        columns: z.array(z.string()),
        /** Columna calculada por mí, no copiada de la ficha. */
        derivedNote: z.string().optional(),
      })
      .optional(),

    /** 5. Los productos (ver `roundupProduct`). */
    products: z.array(roundupProduct).optional(),

    /** 6. Trampas de marketing y errores comunes (el otro diferencial). */
    pitfalls: z
      .array(z.object({ claim: z.string(), reality: z.string() }))
      .optional(),

    /** 7. Veredicto por perfil de uso, nunca un "mejor" absoluto. */
    verdicts: z
      .array(
        z.object({
          profile: z.string(),
          pick: z.string(),
          why: z.string(),
        })
      )
      .optional(),
  }),
});

export const collections = { blog };
