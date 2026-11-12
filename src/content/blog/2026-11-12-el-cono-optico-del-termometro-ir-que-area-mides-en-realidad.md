---
title: "El cono óptico del termómetro IR: qué área mides en realidad"
pubDate: 2026-11-12
description: "Tu termómetro IR no mide un punto sino un círculo que crece con la distancia: así sabes qué superficie estás leyendo de verdad."
category: "óptica"
image: "/images/blog/2026-11-12-el-cono-optico-del-termometro-ir-que-area-mides-en-realidad.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0CFVZQFZ5?tag=physicsofhobbies-21"
productName: "Bosch termómetro de infrarrojos UniversalTemp"
---

Apuntas el termómetro infrarrojo a una resistencia que sospechas que se está calentando de más, lees 85 °C y decides que todo está bien. El problema es que ese número puede ser el promedio de la resistencia, del cableado de al lado y de un trozo de carcasa de plástico, todo mezclado en un solo valor sin que tú lo sepas. El láser que ves como un punto rojo no marca el área que realmente mide el sensor: marca solo el centro.

El termómetro IR no 've' un punto, ve un cono. La lente interna recoge la radiación que llega desde un círculo cuyo diámetro crece con la distancia, y esa relación se expresa como razón distancia:punto (D:S ratio). Un ratio de 12:1 significa que a 12 cm de distancia el área medida tiene 1 cm de diámetro; a 120 cm, ese círculo ya mide 10 cm. La fórmula es simple: $d_{spot} = \dfrac{D}{DS}$, donde $D$ es la distancia al objeto y $DS$ el ratio óptico del equipo. Cuanto más lejos apuntes, más grande es el área que se está promediando, y menor la probabilidad de que estés midiendo solo lo que te interesa.

La mayoría de la gente comete el mismo error: aleja el termómetro para evitar el calor o para alcanzar un punto incómodo, sin pensar que está ampliando el área de muestreo. Si quieres medir un componente electrónico de 3 mm de ancho, necesitas acercarte lo suficiente para que el spot sea menor que esos 3 mm, no solo centrar el láser sobre él. La ficha técnica de un termómetro IR suele declarar el ratio D:S, y ese dato importa tanto como el rango de temperatura anunciado, porque un rango de -30 °C a 500 °C no sirve de nada si el punto que lees mezcla tres superficies distintas.

**Prueba rápida**
1. Coloca una cinta aislante negra (alta emisividad conocida) sobre una superficie metálica brillante.
2. Mide la temperatura de la cinta apoyando el termómetro casi en contacto (distancia mínima recomendada por el fabricante).
3. Repite la medición alejándote 1 metro, apuntando al mismo punto con el láser.
4. Compara: si la lectura cambia de forma notable, estás viendo el efecto del cono óptico mezclando la cinta con el metal de alrededor.

El UniversalTemp de Bosch cubre un rango amplio (-30 °C a 500 °C) y resuelve parte del problema de la emisividad con tres grupos de materiales predefinidos, lo que evita que tengas que introducir un valor decimal cada vez que cambias de superficie. Es una simplificación razonable para uso general y bricolaje, aunque su ficha no declara el ratio D:S, así que para piezas pequeñas o electrónica delicada conviene acercarse físicamente en vez de confiar en la distancia cómoda. Para radiadores, tuberías o superficies de cocina, donde el área a medir es grande y uniforme, esa limitación apenas se nota.

---

**¿Comparando modelos?** En [Termómetro infrarrojo: cuál sirve para cocina y cuál no](/blog/2026-08-13-termometro-infrarrojo-que-rango-y-que-emisividad-necesitas/) analizo varias fichas de este tipo de producto y qué dato de la ficha decide la compra.
