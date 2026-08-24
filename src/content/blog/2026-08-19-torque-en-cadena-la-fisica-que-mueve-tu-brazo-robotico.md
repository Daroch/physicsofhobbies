---
title: "Torque en cadena: la física que mueve tu brazo robótico"
pubDate: 2026-08-19
description: "Cada centímetro que alargas el brazo multiplica la carga sobre el servo de la base, y ahí es donde casi todos los proyectos fallan."
category: "robótica"
image: "/images/blog/2026-08-19-torque-en-cadena-la-fisica-que-mueve-tu-brazo-robotico.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B085C2S1N7?tag=physicshobbie-21"
productName: "Adeept Kit de brazo robótico 5-DOF compatible con Arduino IDE"
---

## El problema que el producto resuelve

Montas un brazo robótico, le pones una pinza en la punta, cargas un objeto pequeño y el servo de la base empieza a temblar o directamente se rinde. No es un problema de programación ni de cables sueltos: es que ese servo está peleando contra una palanca cada vez más larga y no tiene el torque para ganar esa pelea.

## La física detrás

Un brazo articulado es, en esencia, una cadena de palancas. Cada servo debe generar un torque suficiente para sostener no solo el peso que sujeta la pinza, sino el peso de todos los eslabones y servos que tiene por delante. El torque necesario es $\tau = F \cdot d$, donde $F$ es el peso que cuelga en el extremo y $d$ es la distancia horizontal desde el eje del servo hasta ese peso. Si duplicas la longitud del brazo, duplicas el torque exigido aunque el peso no cambie. Por eso el servo de la base de un brazo 5-DOF siempre necesita más torque que el de la muñeca: acumula el peso de todo lo que viene después.

## Cómo usarlo bien

La mayoría de la gente elige servos iguales para todas las articulaciones porque es más barato o más simple de programar, y luego se sorprende cuando el brazo se dobla solo bajo su propio peso. Antes de fijar una pieza, calcula el torque real que va a soportar cada eje sumando los brazos de palanca de las partes que tiene delante, y deja un margen de al menos un 30% sobre ese valor porque los servos pierden torque efectivo cuando trabajan cerca de su límite continuo, no solo en el pico.

## Prueba rápida

1. Extiende el brazo completamente en horizontal, sin carga en la pinza.
2. Observa si el servo de la base vibra o hace un ruido de esfuerzo constante (ya está cerca de su límite con el peso propio).
3. Añade un peso pequeño y conocido en la pinza (una moneda sirve).
4. Si el temblor aumenta notablemente o el brazo cede unos grados, ese servo está subdimensionado para esa configuración.

## El producto

Este kit de Adeept ofrece 5 grados de libertad controlados desde Arduino IDE, con pantalla OLED para feedback visual y un tutorial en PDF que cubre el montaje y el código básico. Es un punto de entrada razonable para entender cinemática directa e inversa sin programar los cálculos desde cero, aunque los servos incluidos son de gama económica y notarás sus límites de torque en cuanto trabajes con el brazo extendido o cargues objetos por encima de unos pocos gramos. Para experimentar con los conceptos de torque y palanca que mencionamos arriba es suficiente; para un brazo con carga útil seria, tocará mirar servos de mayor torque como upgrade.