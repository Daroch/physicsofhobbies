---
title: "Termómetro infrarrojo o cámara térmica: qué mide cada uno"
pubDate: 2026-08-17
description: "Los dos leen la misma radiación. La diferencia es cuántas veces la miden: uno promedia una mancha, la otra reparte casi 50.000 lecturas."
category: "óptica"
tags: ["ciencia", "hobbies", "divulgación", "instrumentación"]
---

Un termómetro infrarrojo de pistola cuesta 25 € y una cámara térmica de aficionado unos 200 €. Los dos apuntan a una superficie, no la tocan, y devuelven grados centígrados. La pregunta razonable es si la cámara hace lo mismo ocho veces más caro.

No hace lo mismo. Pero la diferencia no está donde la gente supone, ni en la precisión ni en el rango: está en **cuántas veces mide cada uno**.

## El sensor es el mismo tipo de cosa

Ambos detectan la radiación infrarroja que emite cualquier cuerpo por estar a una temperatura dada, y ambos la convierten en grados asumiendo una emisividad. Esa física —la ley de Stefan-Boltzmann y por qué el metal pulido engaña a los dos por igual— está desarrollada en [la física de ver el calor que se escapa](/blog/2026-08-11-radiacion-infrarroja-la-fisica-de-ver-el-calor-que-se-escapa/). Aquí la damos por sabida.

La diferencia es geométrica. El termómetro de pistola tiene **un** detector. La cámara tiene una matriz de microbolómetros: 256 × 192 son 49.152 detectores midiendo a la vez.

## Lo que de verdad mide un termómetro de pistola

No mide un punto, por mucho que el láser dibuje uno. Mide el promedio de una **mancha circular** cuyo tamaño crece con la distancia. Eso es el ratio distancia:punto (D:S) de la ficha:

$$
d_{\text{mancha}} = \frac{\text{distancia}}{S}
$$

Con un D:S típico de 12:1, a un metro la mancha mide 83 mm de diámetro. El número que lees es el promedio de todo lo que cae dentro de esos **5.454 mm²**.

Ahí está la trampa práctica. Si buscas un terminal recalentado de 1 cm² dentro de un cuadro eléctrico y disparas desde un metro, ese terminal ocupa menos del 0,2 % de la mancha. Su calor queda diluido en el promedio con el plástico frío de alrededor, y **te devuelve un número tranquilizador que no es falso: es un promedio correcto de la superficie equivocada**.

Acercarse funciona —a 0,5 m la mancha baja a 1.364 mm²— pero en un cuadro con tensión acercarse es justo lo que quieres evitar.

## Lo que mide una cámara

Cada píxel cubre un ángulo fijo, así que su huella sobre la superficie también crece con la distancia:

$$
\text{mm por píxel} = \frac{2 \cdot d \cdot \tan(\text{FOV}/2)}{N_{\text{píxeles}}}
$$

Para una cámara de 256 píxeles de ancho con un campo de visión horizontal de unos 50°, a un metro cada píxel cubre 3,6 mm, es decir **13 mm²**.

La comparación a la misma distancia es contundente:

| A 1 metro | Termómetro D:S 12:1 | Cámara 256×192 |
|---|---|---|
| Lecturas | 1 | 49.152 |
| Superficie por lectura | 5.454 mm² | 13 mm² |

Cada lectura de la cámara es **411 veces más fina en área**. Ese es el factor que separa los dos instrumentos, y no aparece en ninguna ficha como tal: hay que calcularlo, porque lo que el fabricante anuncia es la resolución en píxeles y el campo de visión por separado.

## La regla de decisión

De ahí sale un criterio que no depende del presupuesto:

- **Si sabes dónde apuntar**, el termómetro de pistola es la herramienta correcta. Comprobar la sartén, el radiador, la salida de un conducto, el rodamiento que ya sabes cuál es. Es más barato, más rápido y cabe en un bolsillo.
- **Si necesitas encontrar dónde apuntar**, necesitas la cámara. Localizar la fuga térmica en una pared de tres metros, el terminal flojo entre cuarenta, el punto caliente de una placa con doscientos componentes. Buscar un máximo desconocido con un instrumento que promedia es un mal método: puedes barrer durante media hora y pasar por encima sin enterarte.

Dicho de otra forma: el termómetro responde «¿a qué temperatura está *esto*?». La cámara responde «¿*qué* está más caliente?». Son preguntas distintas.

## Sensibilidad no es exactitud

Aquí hay un malentendido que las fichas de cámaras alimentan, y conviene separarlo bien.

La **NETD** (típicamente 50 mK, o sea 0,05 °C) es la diferencia de temperatura más pequeña que la cámara distingue entre dos píxeles vecinos. Es una medida de *sensibilidad*.

La **exactitud** (típicamente ±2 °C o ±2 % de la lectura) es cuánto puede desviarse el valor absoluto respecto a la temperatura real.

Hay un factor **40** entre ambas cifras, y significan cosas opuestas: la cámara puede decirte con total fiabilidad que este tornillo está 0,05 °C más caliente que el de al lado, y a la vez equivocarse en 2 °C al decirte que está a 87 °C.

Una cámara térmica es, ante todo, un **comparador**. Excelente para «este punto está más caliente que su entorno», mediocre para «este punto está exactamente a tantos grados». Si lo que necesitas es el valor absoluto fiable, ni la cámara ni el termómetro barato te lo dan: eso pide contacto, y por eso algunos termómetros IR incluyen sonda tipo K.

Es el mismo patrón que separa resolución de precisión en una balanza: **el número de decimales que muestra un instrumento no dice nada sobre lo cerca que está del valor verdadero.**

## La trampa de la resolución anunciada

Muchas cámaras de gama baja anuncian una resolución mayor que la de su sensor: «640 × 480» cuando el microbolómetro real es de 256 × 192. La diferencia es **interpolación** — píxeles calculados a partir de los vecinos, no medidos.

Esos píxeles inventados suavizan la imagen y quedan bien en la pantalla, pero no añaden ni un dato térmico nuevo. Para el cálculo de mm por píxel de arriba hay que usar **la resolución del sensor**, no la de salida. Si una ficha da un solo número sin aclarar cuál es, asume que es el interpolado.

## Antes de comprar

Si ya has decidido que lo tuyo es el instrumento puntual, en [qué rango y qué emisividad necesitas](/blog/2026-08-13-termometro-infrarrojo-que-rango-y-que-emisividad-necesitas/) comparo cinco modelos — con el hallazgo incómodo de que ninguna de las cinco fichas declara ni precisión ni ratio D:S.

Y si te inclinas por la cámara, la pregunta que decide no es cuántos píxeles anuncia, sino **cuántos milímetros cubre cada píxel a la distancia a la que vas a trabajar de verdad**. Con la fórmula de arriba y dos datos de la ficha —resolución del sensor y campo de visión— lo tienes en una cuenta.
