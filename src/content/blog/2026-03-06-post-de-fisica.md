---
title: "Post de Física"
pubDate: 2026-03-06
description: "Resolver problemas de optimización, como encontrar la ruta más corta, es computacionalmente muy difícil. Aprende por qué y cómo abordarlo con pragmatismo en tu taller."
referenceUrl: "agua de lluvia"
category: "general (algoritmos y optimización)"
image: "/images/blog/2026-03-06-post-de-fisica.png"
tags: ["física", "maker", "divulgación"]
---

Cuando estás en el taller, ya sea con la impresora 3D, la CNC, o planificando cortes para un mueble, te pasas el día optimizando. Quieres que la pieza de la impresora use menos material y se haga rápido, que la CNC siga la ruta más corta para acabar antes, o que un panel de madera te dé todos los cortes con el mínimo desperdicio. Parece una tarea sencilla, ¿verdad? Es buscar "la mejor opción". Pues bien, la física y las matemáticas nos demuestran que, a menudo, encontrar esa "mejor opción absoluta" es un problema muchísimo más complejo de lo que parece.

**Contexto Práctico: ¿Por qué tus proyectos se atascan en la optimización?**

Imagina que tienes que cortar diez piezas distintas de un tablero de madera. Intuitivamente, empiezas a mover las plantillas, buscando la forma de encajarlo todo para que sobre el mínimo. Lo mismo pasa cuando configuras el slicer de tu impresora 3D: ¿qué infill uso? ¿dónde pongo los soportes? ¿cuál es la mejor orientación de la pieza para minimizar el tiempo o el material? Todas estas son decisiones de optimización. Estás buscando la "ruta" o la "configuración" que te lleva al resultado óptimo (menos tiempo, menos material, menos desperdicio).

Lo que los matemáticos y físicos hacemos con estos problemas es modelarlos usando algo llamado "polítopos". Piensa en un polítopo como un espacio de todas las combinaciones posibles de tus decisiones, limitado por tus restricciones. Por ejemplo, las restricciones de tu impresora 3D (tamaño máximo, velocidad del cabezal, temperatura del material) definen una "forma" en un espacio multidimensional. Cada "esquina" o "vértice" de esa forma representa una configuración válida. El "camino" entre esas esquinas son los cambios que haces en tus ajustes.

**Explicación Técnica: La paradoja de la ruta más corta**

El artículo "Finding Short Paths on Simple Polytopes" profundiza precisamente en esto. Suena abstracto, pero tiene implicaciones directas para tu trabajo. Básicamente, demuestra que **encontrar la ruta más corta entre una solución inicial y la solución óptima en un problema de optimización (como los de programación lineal) es NP-hard**.

¿Y qué significa "NP-hard"? Significa "computacionalmente muy difícil". No es que sea imposible de resolver, es que el tiempo que un ordenador necesitaría para encontrar la *solución absolutamente perfecta y más corta* crece de forma exponencial con el tamaño del problema. Para problemas pequeños, no hay problema. Para problemas grandes, significa que aunque tuvieras el superordenador más potente del mundo, podría tardar más tiempo que la edad del universo en encontrar la respuesta.

El método Simplex, que es uno de los algoritmos más comunes para resolver problemas de programación lineal (como el de la "mochila" o el de optimización de recursos), funciona moviéndose de vértice a vértice a lo largo de las aristas del polítopo. Cada "paso" o "pivote" es una mejora. El estudio de De Loera, Kafer y Sanità demuestra que encontrar la secuencia *más corta* de esos pasos para llegar al óptimo es NP-hard. Es como intentar encontrar el atajo definitivo en un laberinto con un número de habitaciones que se multiplica astronómicamente.

Además, el estudio también prueba que calcular el "diámetro" de un polítopo simple (que es la mayor distancia entre dos vértices cualesquiera, también en términos de número de pasos) es igualmente NP-hard. Esto es relevante para entender las "dimensiones" de la complejidad de un problema.

**¿Entonces no hay solución?**

Sí, la hay, y aquí viene la parte pragmática del estudio. Aunque encontrar la ruta *absolutamente más corta* sea NP-hard, el artículo también menciona un lado positivo: se pueden encontrar formulaciones "extendidas" para estos polítopos que, aunque más complejas, permiten encontrar un camino de longitud "lineal" (es decir, una solución buena, no necesariamente la *óptima absoluta*, pero sí eficiente de calcular) en un tiempo polinomial. Esto significa que podemos encontrar una solución *razonablemente buena* en un tiempo razonable, lo cual es suficiente para la mayoría de los casos prácticos en el taller.

**Prueba de Garaje: El problema del corte de madera**

Vamos a poner esto en práctica con un problema clásico: optimizar cortes.

**Materiales:**
*   Un metro o cinta métrica.
*   Un lápiz.
*   Un tablero de madera, o incluso un trozo de cartón grande.
*   Una lista de piezas que necesitas cortar:
    *   Dos piezas de 60 cm.
    *   Tres piezas de 30 cm.
    *   Una pieza de 45 cm.
*   Piezas de madera disponibles (puedes simular con tiras de cartón o papel):
    *   Una de 100 cm.
    *   Una de 80 cm.
    *   Una de 70 cm.
    *   Una de 50 cm.

**Procedimiento:**
1.  **Objetivo:** Cortar todas las piezas necesarias con el *mínimo desperdicio posible* de las piezas disponibles.
2.  **Intento "a ojo":** Sin pensar demasiado, empieza a asignar cortes. Por ejemplo, de la de 100cm cortas una de 60cm. ¿Qué te sobra? 40cm. ¿Puedes cortar algo más?
3.  **Intento "sistemático" (heurístico):**
    *   Una estrategia común es "corta primero las piezas más grandes que quepan en el listón más pequeño donde aún caben". O "corta primero las piezas grandes del listón más largo".
    *   Prueba varias configuraciones. Por ejemplo:
        *   ¿Corto las dos de 60cm de la de 100cm y la de 80cm? No caben.
        *   ¿Corto una de 60cm de la de 100cm? Sobran 40cm.
        *   ¿Corto una de 60cm de la de 80cm? Sobran 20cm.
        *   ¿Y si intento meter las de 30cm?
4.  **Observación:** Verás que, para este pequeño conjunto de piezas, puedes encontrar una solución razonablemente buena en poco tiempo. Pero, ¿estás *absolutamente seguro* de que es el desperdicio *mínimo posible*? Para saberlo, tendrías que probar *todas las combinaciones posibles*, lo cual, incluso con estos pocos elementos, se vuelve tedioso. Si añades más piezas de origen, más largos a cortar, y más restricciones, el problema escala muy rápidamente. Ahí es donde te encuentras con la NP-hardnes: la explosión combinatoria.

**Recursos Específicos:**

1.  [**Software de optimización de corte (ej: OptiCut o similar)**](https://www.amazon.es/s?k=software+optimizacion+corte&tag=myworkshoptag): Para automatizar la búsqueda de soluciones eficientes en tus proyectos de carpintería o mecanizado, sin preocuparte de la NP-hardnes.
2.  [**Libro: "Introduction to Operations Research" de Hillier y Lieberman**](https://www.amazon.es/s?k=Introduction+to+Operations+Research+Hillier+Lieberman&tag=myworkshoptag): Si quieres profundizar en los fundamentos matemáticos de la programación lineal y entender cómo se formulan estos problemas.
3.  [**Kit de desarrollo ESP32**](https://www.amazon.es/s?k=kit+desarrollo+esp32&tag=myworkshoptag): Para experimentar con la implementación de algoritmos heurísticos (aproximaciones que encuentran soluciones "buenas" rápidamente) en problemas de optimización pequeños que puedas encontrar en proyectos de automatización.

**PRO-TIP OPCIONAL:** Si un problema de optimización te está rompiendo la cabeza buscando el "óptimo absoluto", considera buscar una solución "suficientemente buena". Muchas veces, un algoritmo heurístico que te da el 95% del óptimo en segundos es infinitamente más útil que uno que te promete el 100% en siglos. El pragmatismo es clave.