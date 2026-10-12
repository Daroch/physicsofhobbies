# Physics of Hobbies

[physicsofhobbies.com](https://physicsofhobbies.com) — guías de compra de instrumentos de medida
escritas desde la ficha técnica, con criterio de ingeniero.

La premisa es que casi todas las reseñas de internet te cuentan qué tal va un aparato. Este sitio
hace otra cosa: coge las especificaciones que el fabricante publica y explica **qué significan
físicamente**, cuáles deciden la compra y, sobre todo, cuáles faltan. Que un fabricante no declare
la sensibilidad de un contador Geiger o el tipo de soporte de los «64 GB» de un kit de Raspberry Pi
es información útil, y aquí se dice.

De ahí salen dos reglas que condicionan todo lo demás:

- **No hay experiencia de uso.** Estos productos no se han probado. Todo se escribe desde la ficha
  («según su ficha», «el fabricante declara»), y la página [/metodologia](https://physicsofhobbies.com/metodologia)
  lo explica sin rodeos.
- **No hay números inventados.** Si un dato no está en la ficha, la tabla comparativa dice
  «no disponible» en vez de estimarlo. Rellenar ese hueco con algo verosímil destruiría lo único
  que diferencia al sitio.

El sitio lleva enlaces de afiliado de Amazon, declarados en cada página.

## Qué hay aquí

Este repositorio es **solo el frontend**: un sitio estático en Astro que se despliega en GitHub
Pages. El contenido llega desde fuera.

```
src/
  content/blog/     43 artículos en Markdown (14 comparativas, el resto explicativos)
  layouts/          dos plantillas: artículo normal y comparativa
  pages/            portada, categorías, /metodologia, /sobre-mi, /privacidad
  config/site.ts    configuración del sitio y analítica
```

**Astro 5** con Tailwind 4, KaTeX para las fórmulas (`remark-math` + `rehype-katex`) y sitemap
automático. Las fuentes y KaTeX están autoalojados: **cero peticiones a CDNs de terceros**.

Las comparativas no son texto libre. Van en el frontmatter con una estructura validada por Zod
—para quién es, qué specs importan y por qué, cómo elegir según tu caso, tabla, trampas de
marketing, veredicto por perfil— y la plantilla las renderiza. Eso obliga a que todas respondan a
las mismas preguntas y hace que una ficha incompleta se vea, en vez de disimularse en un párrafo.

```bash
npm install
npm run dev      # servidor local en :4321
npm run build    # genera dist/
```

## Cómo se publica

El contenido lo genera un pipeline que vive fuera de este repositorio:

1. Una base de **Airtable** guarda los productos, con su ficha tal y como la publica Amazon.
2. Un workflow de **n8n** autoalojado toma el siguiente producto pendiente, le pide a **Claude** un
   artículo a partir de esa ficha, y empuja el Markdown y la imagen a este repositorio.
3. El `push` dispara el workflow de **GitHub Actions** que compila y despliega.

Las comparativas siguen el mismo camino pero aterrizan en la rama `borradores` y pasan por revisión
humana antes de fusionarse. Los artículos de producto único van directos a `main`.

Dos detalles del pipeline que costaron más de lo previsto, por si a alguien le sirven:

- **La comprobación de «¿esto ya lo he publicado?» tiene que mirar el sitio publicado**, no la base
  de datos que lo alimenta. Consultando Airtable se escaparon tres artículos repetidos, porque
  Airtable no conoce ni las comparativas ni los textos escritos a mano. Ahora lee el listado de
  este repositorio.
- **Seleccionar qué productos comparar por número de reseñas es un filtro de popularidad**, y deja
  fuera justo lo caro y específico. La selección se hace buscando el mayor rango de precio posible.

## Licencia

El código es de libre consulta. Los textos y las imágenes de producto no: los primeros son obra
propia, las segundas pertenecen a sus fabricantes y se usan bajo el programa de afiliados de
Amazon.
