// Fuente única de la identidad del autor y del criterio editorial.
// La usan el JSON-LD de cada post, la caja de autor, /sobre-mi y /metodologia,
// para que la señal de autoría que ve Google y la que lee una persona no puedan
// divergir.

export const AUTHOR = {
  /**
   * Solo el nombre de pila, por decisión del autor (2026-08-11): el apellido no
   * se publica en el sitio. La reconciliación de entidad con Google se apoya en
   * `sameAs` → LinkedIn, que es una declaración explícita y no depende de que
   * el nombre coincida literalmente.
   */
  name: "Álvaro",
  /**
   * Titular corto. Solo credenciales reales y verificables (ver notas/bio).
   * Lo consumen el JSON-LD (`description` del Person) y la cabecera de
   * /sobre-mi — deliberadamente NO la caja al pie de cada post: repetir las
   * titulaciones en los 14 artículos suena a currículum, y la señal de
   * autoridad ya viaja en los datos estructurados.
   */
  role: "Licenciado en Ciencias Físicas e Ingeniería Electrónica",
  /**
   * Una línea para la caja de autor. Dice de qué va el sitio, no quién es el
   * autor: para eso está el enlace a /sobre-mi.
   */
  shortBio:
    "Escribo sobre la física de los instrumentos de medida y sobre qué dicen —y qué callan— sus fichas técnicas.",
  avatar: "/images/avatar-physics-of-hobbies-512.png",
  /** Página de la entidad autor dentro del sitio. Con barra final: es la URL
   *  canónica, y el `url` del JSON-LD debe coincidir con ella exactamente. */
  page: "/sobre-mi/",
  /** Titulaciones, para `alumniOf` del JSON-LD. */
  degrees: [
    "Licenciado en Ciencias Físicas (Especialidad Electrónica y Automática), UPV/EHU",
    "Licenciado en Ingeniería Electrónica (Itinerario Automática), UPV/EHU",
  ],
  university: "Universidad del País Vasco (UPV/EHU)",
  knowsAbout: [
    "Física",
    "Ingeniería electrónica",
    "Instrumentación y medición",
    "Automática",
    "Electrónica de medida",
    "Desarrollo web fullstack",
  ],
  /**
   * Perfiles públicos que acreditan a la misma persona. Alimentan `sameAs` del
   * JSON-LD, que es lo que permite a Google enlazar el autor con una entidad
   * real fuera del sitio.
   */
  profiles: {
    linkedin:
      "https://www.linkedin.com/in/alvaro-larrinaga-jauregui-663512236/",
    github: "",
  },
} as const;

export const SITE = {
  name: "Physics of Hobbies",
  tagline: "el porqué de las cosas",
  logo: "/images/favicon-32x32.png",
  contact: "hola@physicsofhobbies.com",
} as const;

/**
 * Analítica autoalojada (Umami en el Oracle, ver notas/umami-despliegue.md).
 * Sin cookies y sin terceros: el script se sirve desde un subdominio propio.
 * `script` no es `/script.js` a propósito, para no chocar con las reglas de
 * bloqueo más genéricas.
 */
export const ANALYTICS = {
  host: "https://stats.physicsofhobbies.com",
  script: "/u.js",
  websiteId: "499441fe-5423-4c87-816e-f2a635470022",
} as const;

/** Criterio de selección de producto. Debe cuadrar con el filtro del workflow. */
export const CRITERIA = {
  minRating: 4,
  minReviews: 50,
} as const;

/** URLs de perfil declaradas, sin huecos. */
export const authorSameAs: string[] = Object.values(AUTHOR.profiles).filter(
  (url): url is string => typeof url === "string" && url.length > 0,
);

/** Bloque `author` reutilizable para el JSON-LD de cualquier página. */
export function authorSchema(siteUrl: URL | string | undefined) {
  return {
    "@type": "Person",
    name: AUTHOR.name,
    description: AUTHOR.role,
    url: new URL(AUTHOR.page, siteUrl).toString(),
    image: new URL(AUTHOR.avatar, siteUrl).toString(),
    alumniOf: {
      "@type": "CollegeOrUniversity",
      name: AUTHOR.university,
    },
    knowsAbout: [...AUTHOR.knowsAbout],
    ...(authorSameAs.length > 0 ? { sameAs: authorSameAs } : {}),
  };
}
