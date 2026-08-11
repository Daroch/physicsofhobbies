// Fuente única de la identidad del autor y del criterio editorial.
// La usan el JSON-LD de cada post, la caja de autor, /sobre-mi y /metodologia,
// para que la señal de autoría que ve Google y la que lee una persona no puedan
// divergir.

export const AUTHOR = {
  name: 'Álvaro',
  /** Titular corto. Solo credenciales reales y verificables. */
  role: 'Graduado en Física y desarrollador de software',
  bio: 'Analizo especificaciones técnicas de herramientas de taller y explico qué significan en la práctica.',
  avatar: '/images/avatar-physics-of-hobbies-512.png',
  /** Página de la entidad autor dentro del sitio. */
  page: '/sobre-mi',
  /**
   * Perfiles públicos que acreditan a la misma persona. Alimentan `sameAs` del
   * JSON-LD, que es lo que permite a Google enlazar el autor con una entidad
   * real fuera del sitio.
   * PENDIENTE: añadir la URL de LinkedIn. Mientras esté vacío no se emite
   * `sameAs` ni se pinta el enlace — es preferible no declarar nada a declarar
   * un perfil que no existe.
   */
  profiles: {
    linkedin: '',
    github: '',
  },
} as const;

export const SITE = {
  name: 'Physics of Hobbies',
  tagline: 'el porqué de las cosas',
  logo: '/images/favicon-32x32.png',
  contact: 'hola@physicsofhobbies.com',
} as const;

/** Criterio de selección de producto. Debe cuadrar con el filtro del workflow. */
export const CRITERIA = {
  minRating: 4,
  minReviews: 50,
} as const;

/** URLs de perfil declaradas, sin huecos. */
export const authorSameAs: string[] = Object.values(AUTHOR.profiles).filter(
  (url): url is string => typeof url === 'string' && url.length > 0
);

/** Bloque `author` reutilizable para el JSON-LD de cualquier página. */
export function authorSchema(siteUrl: URL | string | undefined) {
  return {
    '@type': 'Person',
    name: AUTHOR.name,
    description: AUTHOR.role,
    url: new URL(AUTHOR.page, siteUrl).toString(),
    ...(authorSameAs.length > 0 ? { sameAs: authorSameAs } : {}),
  };
}
