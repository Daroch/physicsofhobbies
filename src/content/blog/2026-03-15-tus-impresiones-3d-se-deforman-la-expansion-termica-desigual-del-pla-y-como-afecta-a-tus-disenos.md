---
title: "Tus Impresiones 3D se Deforman: La Expansión Térmica Desigual del PLA y Cómo Afecta a tus Diseños"
pubDate: 2026-03-15
description: "Las piezas 3D de PLA se expanden y contraen de forma diferente según la dirección de impresión al cambiar de temperatura. Entender esto te ayuda a evitar deformaciones y a mejorar el ajuste de tus componentes."
referenceUrl: "https://arxiv.org"
category: "materiales"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

¿Alguna vez has impreso una pieza con tolerancias muy ajustadas, o una pieza larga, y al final no encaja bien o se deforma al enfriarse o calentarse? No es solo "warping" por mala adhesión a la cama. El problema puede venir de algo más fundamental: cómo se comporta el material cuando cambia de temperatura, y en el caso de las impresiones 3D de PLA, la cosa se complica porque no se comporta igual en todas las direcciones.

Este estudio de Arxiv, "Investigating the Anisotropic Thermal Expansion Coefficients of 3D-Printed PLA Structures via Interferometric Dilatometry", no te va a dar la solución mágica, pero sí te explica por qué pasa esto. Lo que han hecho es usar un método súper preciso (dilatometría interferométrica láser) para medir cómo el PLA impreso se estira o encoge con la temperatura. Y la clave es esta: el coeficiente de expansión térmica (cuánto se deforma por grado Celsius) *no es el mismo* a lo largo de las capas de impresión que perpendicular a ellas. Han encontrado diferencias de hasta el 25% dependiendo de la dirección. Además, la densidad del relleno y la temperatura de impresión también influyen.

Piensa en una tabla de madera. Sabes que se hincha o contrae más a lo ancho de la veta que a lo largo. Aquí es parecido, pero con las capas de plástico. Al imprimir, el filamento se deposita y se enfría, creando una estructura donde las cadenas poliméricas se alinean de cierta manera. Esto hace que la pieza tenga propiedades diferentes en distintas direcciones (lo que llamamos anisotropía). Si tu pieza está caliente y se enfría, o viceversa, y tiene dimensiones críticas, este efecto anisotrópico puede ser la razón de que no encaje o se tuerza. Para un engranaje con un eje, o una carcasa donde un componente debe deslizarse con precisión, esto es crítico.

#### Explicación técnica:

La deformación térmica lineal de un material se describe con la fórmula $ \Delta L = \alpha L_0 \Delta T $, donde:
*   $ \Delta L $ es el cambio en la longitud.
*   $ \alpha $ es el coeficiente de expansión térmica (CTE).
*   $ L_0 $ es la longitud inicial.
*   $ \Delta T $ es el cambio de temperatura.

Lo que este estudio demuestra es que para el PLA impreso, este $ \alpha $ no es un valor único. Tienes un $ \alpha_{||} $ (paralelo a la dirección de las capas de impresión) y un $ \alpha_{\perp} $ (perpendicular a ellas) que son diferentes. Por ejemplo, si imprimes una varilla tumbada en la cama, se expandirá o contraerá de una manera a lo largo de su eje (paralelo a las capas) y de otra manera en su altura (perpendicular a las capas). Esta diferencia es la que causa tensiones internas y, eventualmente, deformaciones o fallos en el ajuste. Influye también el grado de entrecruzamiento entre capas y la orientación de los polímeros al solidificarse, algo que varía con la temperatura del extrusor y la velocidad de enfriamiento.

#### Prueba de garaje:

No tenemos un interferómetro láser, pero podemos ver el efecto.

1.  **Imprime dos muestras idénticas de PLA:**
    *   Una: un prisma rectangular largo y estrecho (por ejemplo, 100mm x 10mm x 5mm) impreso tumbado en la cama (capas a lo largo de los 100mm).
    *   Otra: el mismo prisma, pero impreso de pie (capas perpendiculares a los 100mm). Asegúrate de que ambas estén impresas con el mismo filamento, ajustes de densidad de relleno y temperatura de la boquilla y la cama.
2.  **Mide la longitud:** Una vez frías y a temperatura ambiente, usa un [calibre digital](https://www.amazon.es/s?k=calibre+digital&tag=TU_TAG) preciso para medir la longitud de 100mm de ambas muestras. Anota los valores.
3.  **Calienta las muestras:** Puedes usar una [pistola de calor](https://www.amazon.es/s?k=pistola+de+calor&tag=TU_TAG) con cuidado, o sumergirlas en agua tibia (por ejemplo, a 50-60°C) durante unos minutos. Mantén la temperatura lo más uniforme posible.
4.  **Mide de nuevo:** Rápidamente, saca las muestras y vuelve a medir la longitud de 100mm. Es crucial que midas cuando aún están calientes.
5.  **Compara:** Deberías notar que el cambio de longitud es diferente para ambas muestras, incluso si el cambio de temperatura fue similar. La muestra impresa tumbada (donde la longitud mayor es paralela a las capas) y la impresa de pie (donde la longitud mayor es perpendicular a las capas) se habrán expandido de forma ligeramente diferente.

Este experimento rudimentario no te dará los coeficientes exactos, pero te demostrará la anisotropía en la expansión térmica del PLA, que es la base del estudio.

#### Recursos específicos:

*   [Calibre Digital de Precisión](https://www.amazon.es/s?k=calibre+digital+electronico&tag=TU_TAG): Imprescindible para medir dimensiones con exactitud en el taller.
*   [Termómetro Infrarrojo](https://www.amazon.es/s?k=termometro+infrarrojo+pistola&tag=TU_TAG): Para medir la temperatura superficial de tus piezas sin contacto.
*   [Filamento PLA de marca conocida](https://www.amazon.es/s?k=filamento+PLA+prusa&tag=TU_TAG): La consistencia del filamento es clave para repetir experimentos y entender el material.

#### Consejo Práctico:
Para piezas con tolerancias críticas o que vayan a estar sometidas a cambios de temperatura, considera la orientación de impresión. Si una dimensión es crucial, intenta que las capas de impresión no la atraviesen perpendicularmente, si es posible. Un diseño inteligente de las paredes o la densidad de relleno también puede mitigar estas tensiones. A veces, la solución no es solo más temperatura de la cama, sino entender cómo el material se va a comportar *después* de imprimir.

---
**