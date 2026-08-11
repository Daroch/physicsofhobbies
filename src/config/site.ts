// Fuente única de la identidad del autor y del criterio editorial.
// La usan el JSON-LD de cada post, la caja de autor, /sobre-mi y /metodologia,
// para que la señal de autoría que ve Google y la que lee una persona no puedan
// divergir.

export const AUTHOR = {
  /** Nombre completo: tiene que coincidir con el perfil de LinkedIn para que
   *  Google pueda resolver autor y perfil como la misma entidad. */
  name: 'Álvaro Larrínaga Jáuregui',
  shortName: 'Álvaro',
  /** Titular corto. Solo credenciales reales y verificables (ver notas/bio). */
  role: 'Licenciado en Ciencias Físicas e Ingeniería Electrónica',
  bio: 'Dos licenciaturas por la UPV/EHU y veinte años desarrollando software. Analizo especificaciones técnicas de herramientas de taller y explico qué significan en la práctica.',
  avatar: '/images/avatar-physics-of-hobbies-512.png',
  /** Página de la entidad autor dentro del sitio. */
  page: '/sobre-mi',
  /** Titulaciones, para `alumniOf` del JSON-LD. */
  degrees: [
    'Licenciado en Ciencias Físicas (Especialidad Electrónica y Automática), UPV/EHU',
    'Licenciado en Ingeniería Electrónica (Itinerario Automática), UPV/EHU',
  ],
  university: 'Universidad del País Vasco (UPV/EHU)',
  knowsAbout: [
    'Física',
    'Ingeniería electrónica',
    'Instrumentación y metrología',
    'Automática',
    'Electrónica de medida',
  ],
  /**
   * Perfiles públicos que acreditan a la misma persona. Alimentan `sameAs` del
   * JSON-LD, que es lo que permite a Google enlazar el autor con una entidad
   * real fuera del sitio.
   */
  profiles: {
    linkedin: 'https://www.linkedin.com/in/alvaro-larrinaga-jauregui-663512236/',
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
    image: new URL(AUTHOR.avatar, siteUrl).toString(),
    alumniOf: {
      '@type': 'CollegeOrUniversity',
      name: AUTHOR.university,
    },
    knowsAbout: [...AUTHOR.knowsAbout],
    ...(authorSameAs.length > 0 ? { sameAs: authorSameAs } : {}),
  };
}
