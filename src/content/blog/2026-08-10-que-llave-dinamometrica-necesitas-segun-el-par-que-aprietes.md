---
title: "Qué llave dinamométrica comprar según el par que aprietes"
pubDate: 2026-08-10
description: "El error se mide en porcentaje de la lectura, así que la misma precisión declarada significa cosas distintas según el par. Tres cuadradillos comparados por ficha."
category: "mecánica"
tags: ["mecánica", "par de apriete", "herramientas", "torque"]
type: "roundup"
image: "/images/blog/roundup-llave-38.jpg"

audience: "Vas a apretar tornillería con un par especificado — bicicleta, moto, coche o impresora 3D — y no sabes si comprar una llave de 1/4\", 3/8\" o 1/2\". Si solo necesitas aflojar, no necesitas una llave dinamométrica."

specsThatMatter:
  - spec: "Rango de par (Nm)"
    why: "Es la spec que decide la compra, y no por el máximo sino por el mínimo. Una llave de 20-220 Nm no sirve para los 6 Nm de una potencia de bicicleta: el resorte no llega a comprimirse lo suficiente para que el mecanismo de clic sea fiable. Comprueba siempre que tu par objetivo cae holgadamente dentro del rango, no en el borde."
  - spec: "Precisión (±%)"
    why: "Casi siempre es porcentaje de la lectura, no del fondo de escala. Con ±3%, apretar a 10 Nm da un error de ±0,3 Nm, y a 200 Nm da ±6 Nm. El mismo número en la ficha significa un error veinte veces mayor en un caso que en otro — por eso importa elegir el rango donde vas a trabajar, no el más amplio."
  - spec: "Cuadradillo (1/4\", 3/8\", 1/2\")"
    why: "No es solo el tamaño del encaje: marca el par que el mecanismo puede transmitir sin deformarse. Un cuadradillo de 1/4\" con 200 Nm se redondea. Y como la longitud del brazo crece con el cuadradillo, también determina la fuerza que tienes que hacer tú: τ = F × r, así que con un brazo corto necesitas mucha más fuerza para el mismo par."
  - spec: "Dientes del trinquete"
    why: "72 dientes significa que puedes recuperar el ángulo cada 5°, frente a los 15° de uno de 24. Solo importa si trabajas en huecos donde no puedes dar recorrido a la llave; no tiene nada que ver con la precisión del par."

chooseBy:
  - scenario: "aprietas tornillería de bicicleta o electrónica (2-25 Nm)"
    priority: "1/4\", por resolución en pares bajos"
  - scenario: "haces mantenimiento de moto o bici de gama alta (5-60 Nm)"
    priority: "3/8\", el término medio"
  - scenario: "cambias ruedas de coche (90-130 Nm)"
    priority: "1/2\", es el único que llega"
  - scenario: "necesitas cubrir rangos muy separados"
    priority: "dos llaves, no una de rango amplio"

comparison:
  columns: ["Cuadradillo", "Rango", "Precisión", "Error a 1/4 del rango", "Dientes", "Precio"]
  derivedNote: "La columna «Error a 1/4 del rango» la he calculado yo aplicando la precisión declarada a un par situado en el primer cuarto del rango de cada llave — el punto donde la mayoría de la gente trabaja y donde el error absoluto empieza a doler. No es un dato de la ficha."

products:
  - name: "Amazon Basics Llave de trinquete dinamométrica de 1/4 pulgadas, 3.95-22.5 Nm"
    shortName: "Amazon Basics 1/4\""
    tier: "1/4\" · par bajo"
    image: "/images/blog/roundup-llave-14.jpg"
    amazonUrl: "https://www.amazon.es/dp/B07SZVW98Z?tag=physicshobbie-21"
    price: 15.49
    rating: 4.2
    reviews: 4060
    specs: ["1/4\"", "3,95-22,5 Nm", "no disponible", "no disponible", "no disponible", "15,49 €"]
    highlight: "Según su ficha es la única de las tres que baja de 4 Nm, así que es la que cubre la tornillería fina. No declara precisión ni número de dientes, lo cual en una llave dinamométrica es una omisión importante: sin ese dato no puedes saber cuánto te desvías."
  - name: "VANPO Llave Dinamométrica 3/8'', 5-60 Nm"
    shortName: "VANPO 3/8\""
    tier: "3/8\" · uso general"
    image: "/images/blog/roundup-llave-38.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CXDNQYT2?tag=physicshobbie-21"
    price: 30.38
    rating: 4.5
    reviews: 1161
    specs: ["3/8\"", "5-60 Nm", "±3%", "±0,6 Nm a 20 Nm", "72", "30,38 €"]
    highlight: "El rango 5-60 Nm cubre la mayoría del mantenimiento de moto y bicicleta de gama alta. Con ±3% sobre 20 Nm el error es de ±0,6 Nm, holgado para bujías y tornillería de suspensión."
  - name: "Llave Dinamometrica 1/2\", 20-220Nm"
    shortName: "Genérica 1/2\""
    tier: "1/2\" · par alto"
    image: "/images/blog/roundup-llave-12.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DNQ8CJ3H?tag=physicshobbie-21"
    price: 28.29
    rating: 4.5
    reviews: 270
    specs: ["1/2\"", "20-220 Nm", "±3%", "±2,1 Nm a 70 Nm", "72", "28,29 €"]
    highlight: "Es la única de las tres que alcanza los 90-130 Nm de una tuerca de rueda. El mismo ±3% que la de 3/8\" produce aquí un error absoluto unas 3,5 veces mayor, que sigue siendo irrelevante para una rueda pero la descarta para tornillería fina."

pitfalls:
  - claim: "«Precisión ±3%», sin especificar respecto a qué."
    reality: "Si es porcentaje de la lectura (lo habitual), el error crece con el par y la llave es peor en la parte baja de su rango. Si fuera porcentaje del fondo de escala, sería un error fijo y catastrófico en pares bajos. Cuando la ficha no lo aclara, asume lo primero y no trabajes en el primer 20% del rango."
  - claim: "«Rango 20-220 Nm», vendido como versatilidad."
    reality: "Un rango amplio no es una ventaja, es un compromiso. La precisión se mantiene en la zona central; en los extremos el mecanismo trabaja fuera de su punto óptimo. Dos llaves de rango estrecho miden mejor que una de rango amplio, y suelen costar lo mismo juntas."
  - claim: "«72 dientes» como reclamo de calidad."
    reality: "Los dientes son comodidad en espacios estrechos, no precisión. Una llave de 72 dientes con mal resorte mide peor que una de 24 bien calibrada. Es una spec de conveniencia disfrazada de spec de rendimiento."
  - claim: "El silencio sobre la calibración."
    reality: "Ninguna de las tres indica cada cuánto hay que recalibrar ni si viene con certificado. Una llave de clic se descalibra con el uso y con guardarla tensada. Si nadie menciona la calibración, asume que no viene certificada y que tendrás que fiarte del fabricante."

verdicts:
  - profile: "Bicicleta y tornillería fina"
    pick: "Amazon Basics 1/4\" (3,95-22,5 Nm)"
    why: "Es la única que baja lo suficiente. Su punto débil es que no publica precisión: si necesitas garantía sobre el error, busca una de 1/4\" que sí la declare."
  - profile: "Moto y mantenimiento general"
    pick: "VANPO 3/8\" (5-60 Nm)"
    why: "El rango más útil si solo vas a tener una llave, y el error absoluto se mantiene por debajo de 1 Nm en casi todo su recorrido."
  - profile: "Ruedas de coche"
    pick: "Llave 1/2\" (20-220 Nm)"
    why: "Es la única que llega al par que pide una tuerca de rueda. No la compres esperando usarla también para la bicicleta."
---

El par de apriete es fuerza por distancia al eje de giro: $\tau = F \times r$. Es la razón por la que aflojas una tuerca agarrotada con una barra larga en vez de con los dedos, y también la razón por la que no existe una sola llave dinamométrica que sirva para todo.

Dentro de una llave de clic hay un resorte precargado que cede cuando el par alcanza el valor que has fijado. Ese mecanismo tiene un punto de trabajo óptimo, y su error se especifica casi siempre como **porcentaje de la lectura**. Ahí está la consecuencia que casi nadie explica: con la misma precisión declarada del ±3%, apretar a 10 Nm te da un margen de ±0,3 Nm, mientras que apretar a 200 Nm te da ±6 Nm. Veinte veces más.

Por eso la pregunta correcta no es «cuál es la más precisa», sino «en qué rango voy a trabajar». Una tuerca de rueda de coche pide entre 90 y 130 Nm; un tornillo de potencia de bicicleta, entre 5 y 6 Nm. Ninguna llave cubre bien ambos extremos, y la que lo intenta lo hace peor en los dos.
