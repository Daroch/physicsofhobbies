---
title: "Por qué tus impresiones 3D se deforman: la termodinámica del PLA"
pubDate: 2026-03-07
description: "La deformación de tus impresiones 3D no es magia; es termodinámica. Al enfriarse, los plásticos como PLA y ABS se encogen. Entender cómo y por qué sucede te ayuda a ajustar parámetros para minimizar el alabeo. Evita sorpresas en tu próximo proyecto."
referenceUrl: "dinosaurios"
category: "materiales"
image: "/images/blog/2026-03-07-por-que-tus-impresiones-3d-se-deforman-la-termodinamica-del-pla.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

**Contexto práctico: ¿por qué le importa esto a un hobbista?**

Seguro te ha pasado: empiezas una impresión 3D, todo va bien, y a mitad de la pieza, o justo al terminar, ves que los bordes se han levantado de la cama, o la pieza completa se ha retorcido como una patata frita. No solo es frustrante, sino que echa a perder material y tiempo. Esto que llamamos "alabeo" o "warping" es un dolor de cabeza común en la impresión FDM, y entender su causa te da el poder de controlarlo.

**Explicación técnica: traduce el paper a lenguaje de taller**

Mira, el problema principal es la **contracción térmica diferencial**. Piensa en cómo se comporta un material cuando se calienta y se enfría. Cuando fundes plástico, lo extruyes caliente sobre una superficie, y luego se enfría hasta la temperatura ambiente. Al enfriarse, el material se encoge. Esto es física básica. La relación es sencilla:

$\Delta L = \alpha L_0 \Delta T$

Donde:
*   $\Delta L$ es el cambio de longitud que sufre el material.
*   $\alpha$ es el **coeficiente de expansión térmica lineal** del material. Es una propiedad intrínseca y nos dice *cuánto* se encoge o dilata un material por cada grado Celsius. Los plásticos como el PLA o el ABS tienen un $\alpha$ relativamente alto comparado con metales, por ejemplo.
*   $L_0$ es la longitud original del material.
*   $\Delta T$ es el cambio de temperatura.

El problema real empieza porque el enfriamiento no es uniforme. La primera capa que pegas a la cama caliente se enfría desde arriba, mientras que la parte inferior se mantiene más caliente por la cama. Las capas superiores, una vez depositadas, también se enfrían al aire. Esta diferencia de temperatura entre las capas, y también dentro de la misma capa (los bordes expuestos se enfrían más rápido que el centro), hace que unas partes intenten contraerse más o más rápido que otras.

Imagina que estás construyendo una torre de ladrillos, pero cada capa de ladrillos se encoge un poco al secarse, y las de abajo se encogen menos porque están pegadas a una base que no se encoge, o que está caliente. Las capas superiores se encogen más libremente y tiran de las de abajo. Esa tensión acumulada es lo que hace que los bordes de tu pieza se levanten de la cama o que la pieza se tuerza una vez fría.

Además, los plásticos extruidos no son completamente "isotrópicos"; es decir, no se contraen igual en todas direcciones. La dirección en la que se extruye el filamento puede afectar ligeramente cómo se comportan las fibras de plástico, añadiendo otra capa de complejidad a esa contracción.

El estudio apunta a tres puntos clave para controlar esto:
1.  **Adhesión de la cama**: Si la primera capa no está bien pegada a la cama, las tensiones de contracción la arrancarán fácilmente.
2.  **Gradientes de temperatura**: Cuanto más uniforme sea el enfriamiento de la pieza, menos tensiones se acumularán. Una cama caliente ayuda a que las capas inferiores no se enfríen tan rápido. Un enclosure (cerramiento) para la impresora reduce las corrientes de aire y mantiene la temperatura ambiente alrededor de la pieza más estable.
3.  **Propiedades del material**: Cada plástico tiene su propio $\alpha$ y su propia **capacidad calorífica específica**. Materiales con un $\alpha$ muy alto (como el ABS) son más propensos a alabearse.

**Prueba de garaje: un experimento simple con herramientas comunes**

Vamos a ver esto en vivo.

1.  **Imprime una pieza de prueba:** Diseña un rectángulo delgado y largo, digamos 100mm x 20mm x 5mm de alto. Imprímelo en PLA.
2.  **Variación 1 (Adhesión):** Imprime uno sin brim/raft, con la cama limpia. Imprime otro igual con un brim de 5-10mm. Observa la diferencia en el levantamiento de las esquinas.
3.  **Variación 2 (Temperatura de cama):** Si tu impresora lo permite, imprime dos rectángulos más: uno con tu temperatura de cama normal para PLA (ej. 60°C) y otro con una temperatura un poco más baja (ej. 50°C), o si te atreves, sin cama caliente (solo si el PLA aguanta un poco, o para un material de bajo alabeo). Ten en cuenta que si es muy baja, es probable que no se pegue.
4.  **Medición:** Una vez que las piezas estén completamente frías y las hayas retirado de la cama, coloca cada pieza sobre una superficie plana y usa un **calibre digital** para medir la altura a la que se ha levantado cada esquina respecto a la base. Un **termómetro infrarrojo** también te puede servir para ver las diferencias de temperatura en la superficie de la pieza mientras se enfría.

Verás claramente cómo el brim ayuda a distribuir la tensión y cómo una temperatura de cama adecuada (ni muy fría que no pega, ni tan caliente que no ayuda al enfriamiento diferencial controlado) reduce el alabeo.

**Recursos específicos:**

*   **[Calibre digital](https://www.amazon.es/s?k=calibre+digital&tag=TU_TAG)**: Imprescindible para medir con precisión cualquier deformación o dimensión.
*   **[Termómetro infrarrojo](https://www.amazon.es/s?k=termometro+infrarrojo+impresion+3d&tag=TU_TAG)**: Útil para verificar temperaturas de cama, de la pieza durante el proceso o incluso de la boquilla si tienes dudas.
*   **[Spray adhesivo para cama de impresora 3D](https://www.amazon.es/s?k=spray+adhesivo+impresora+3d&tag=TU_TAG)** o láminas de PEI: Mejoran la adhesión de la primera capa, que es crítica para resistir las tensiones de contracción.

**Consejo Práctico:**
No olvides la importancia de la limpieza de la cama. Restos de grasa o huellas dactilares pueden crear puntos débiles en la adhesión, por muy buena que sea tu temperatura o tu adhesivo. Alcohol isopropílico y un paño limpio suelen ser suficientes.

Cada material y cada impresora es un mundo. Lo que funciona de maravilla para el PLA en tu máquina, puede no ser lo ideal para ABS en la de tu colega. La clave está en entender la física detrás del problema y luego experimentar con tus propios parámetros. No hay soluciones mágicas, solo ajustes bien pensados.