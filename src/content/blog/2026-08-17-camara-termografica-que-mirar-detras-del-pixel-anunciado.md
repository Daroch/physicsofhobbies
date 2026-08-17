---
title: "Cámara termográfica: qué mirar detrás del pixel anunciado"
pubDate: 2026-08-17
description: "El pixel final que anuncian (SuperIR/TISR) no es el sensor real: la resolución nativa y el rango de temperatura son los datos que deciden."
category: "electrónica"
tags: ["comparativa", "ciencia", "hobbies"]
type: "roundup"
image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-1.jpg"

audience: "Esto es para quien necesita localizar fugas térmicas, puntos calientes eléctricos o defectos de aislamiento en HVAC. No es para quien necesita medición de temperatura certificada o con trazabilidad, porque ninguna ficha de este grupo declara un error de precisión en °C o %."

specsThatMatter:
  - spec: "Resolución IR real vs. interpolada (SuperIR/TISR)"
    why: "El sensor microbolométrico tiene un número fijo de puntos de medida térmica. HIKMICRO declara sensor nativo de 96x96 y usa SuperIR por software para mostrar 240x240; TOPDON usa TISR para llegar a 512x384. Ese aumento no añade detalle térmico real, solo interpola entre los puntos que sí midió el sensor. La ficha no aclara el sensor nativo del TC004 grande."
  - spec: "Rango de temperatura medible"
    why: "Solo el TOPDON TC004 Mini declara -20°C a 450°C. Para electricidad industrial o hornos ese rango importa; para revisar fugas de aire en una vivienda sobra. Ninguna ficha da el error en °C o % en ese rango, así que el número solo sirve para descartar equipos que no llegan."
  - spec: "Frecuencia de actualización (Hz)"
    why: "Determina si la imagen se ve fluida al mover la cámara o al inspeccionar algo en movimiento (motor, correa). 25 Hz, declarado solo en los TC004 Mini, da vídeo más continuo que una tasa menor; para el resto del grupo el dato no está disponible."
  - spec: "Duración de batería y almacenamiento"
    why: "Va de 8h (HIKMICRO E02) a 15h (TOPDON TC004 Mini) según ficha. El almacenamiento (4GB o 64GB) y la conectividad WiFi solo aparecen en el TC004 grande, relevante si necesitas exportar informes en vez de solo ver la pantalla in situ."
  - spec: "Protección IP"
    why: "Solo HIKMICRO E01 declara IP54 (protección limitada contra polvo y salpicaduras). Los demás no dan dato de IP, así que si trabajas en obra o exteriores sin cubierta, es la única ficha con ese respaldo, aunque IP54 no cubre lluvia intensa ni inmersión."

chooseBy:
  - scenario: "trabajas con instalaciones eléctricas u hornos que superan los 100°C"
    priority: "rango de temperatura amplio (-20 a 450°C, TC004 Mini)"
  - scenario: "necesitas documentar inspecciones con informes o exportar a PC"
    priority: "almacenamiento y WiFi (TC004 grande, 64GB)"
  - scenario: "trabajas en obra o exteriores con polvo o salpicaduras"
    priority: "protección IP declarada (HIKMICRO E01, IP54)"
  - scenario: "inspeccionas piezas en movimiento (motores, correas)"
    priority: "frecuencia de actualización alta (25 Hz, TC004 Mini)"

comparison:
  columns: ["Resolución IR (ficha)", "Rango temperatura", "Frecuencia actualización", "Duración batería", "Almacenamiento", "Precio (€)"]
  derivedNote: "No se incluye columna calculada: ninguna combinación de estas columnas produce un dato físico nuevo, y calcular 'precio por resolución' solo mediría el marketing de cada ficha, no el aparato."

products:
  - name: "TOPDON Camara Termica TC004 Mini, Resolución IR de 240x240 Camara Termografica, -20℃ a 450℃, 15 Horas Duración de Batería, 25 Hz Frecuencia de Actualización, Alertas de Temperatura Alta/Baja"
    shortName: "TOPDON TC004 Mini"
    tier: "Rango amplio, más barato"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-1.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DJQ91653?tag=physicshobbie-21"
    price: 159.98
    rating: 4.5
    reviews: 1495
    specs: ["240x240 (nativo, según ficha)", "-20°C a 450°C", "25 Hz", "15 h", "no disponible", "159.98"]
    highlight: "Según su ficha es prácticamente el mismo aparato que el otro TC004 Mini de este listado (misma resolución, rango, Hz y batería), pero a menor precio: si vas a elegir uno de los dos, es este."
  - name: "TOPDON Cámara Termografica TC004 con 512x384 Resolución TISR, 64GB Almacenamiento, 3,5″ Pantalla Camara Termica con Wifi, Grabación de Vídeo, Análisis de PC, para Inspección Eléctrica/Climatización"
    shortName: "TOPDON TC004 (512x384)"
    tier: "Almacenamiento y WiFi"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-2.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DZ2FZYQH?tag=physicshobbie-21"
    price: 303.99
    rating: 4.5
    reviews: 1495
    specs: ["512x384 (vía TISR)", "no disponible", "no disponible", "no disponible", "64GB + WiFi", "303.99"]
    highlight: "Es el único con pantalla de 3,5\", 64GB y análisis por PC según su ficha, pero no declara rango de temperatura, Hz ni batería, así que para uso industrial extremo faltan datos para decidir."
  - name: "TOPDON Cámara Térmica TC004 Mini, 240x240 IR resolución, 15 h de duración de batería, -20°C - 450°C, 25 Hz, Termográficas para inspección de Sistemas de calefacción, ventilación y Aire Acondicionado"
    shortName: "TOPDON TC004 Mini"
    tier: "Rango amplio, mismo modelo"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-3.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DJD2P3FF?tag=physicshobbie-21"
    price: 193.62
    rating: 4.5
    reviews: 1477
    specs: ["240x240 (nativo, según ficha)", "-20°C a 450°C", "25 Hz", "15 h", "no disponible", "193.62"]
    highlight: "Ficha idéntica al otro TC004 Mini de esta lista (mismo rango, Hz, batería) pero a precio más alto; es el mismo aparato en otra publicación, no una variante distinta a comparar."
  - name: "Camara Termica HIKMICRO E01 con Puntero Láser, IR 96x96 | 240x240 SuperIR, 11h de duración, 4 GB, Video, 2m y IP54, Herramientas para el hogar, HVAC y eléctricas"
    shortName: "HIKMICRO E01"
    tier: "IP54, más económico"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-4.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CF28BNNX?tag=physicshobbie-21"
    price: 159
    rating: 4.4
    reviews: 1270
    specs: ["96x96 nativo | 240x240 SuperIR", "no disponible", "no disponible", "11 h", "4GB", "159"]
    highlight: "Es el único de la lista con IP54 declarada, útil para exteriores con polvo o salpicaduras. Su sensor nativo (96x96) es menor que el de los TC004 Mini, y no declara rango de temperatura ni Hz."
  - name: "Camara Termica HIKMICRO E02 con Cámara Visual, 96x96 IR | Cámara dual, puntero láser, SuperIR 240x240, imagen por fusión, 8h de duración, 4GB, video"
    shortName: "HIKMICRO E02"
    tier: "Cámara dual, fusión"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-5.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CP99QBVJ?tag=physicshobbie-21"
    price: 179.99
    rating: 4.5
    reviews: 744
    specs: ["96x96 nativo | 240x240 SuperIR", "no disponible", "no disponible", "8 h", "4GB", "179.99"]
    highlight: "Añade cámara visual y fusión de imagen para ubicar el punto caliente sobre la foto real, según su ficha. Tiene la batería más corta del grupo (8h) y el mismo sensor nativo pequeño que el E01."

pitfalls:
  - claim: "Resolución 512x384 (TISR)"
    reality: "TISR es una tecnología de interpolación de TOPDON que aumenta el número de píxeles mostrados; la ficha no indica el tamaño del sensor térmico nativo, así que no se puede confirmar cuánto detalle real hay detrás de ese número."
  - claim: "SuperIR 240x240 (HIKMICRO)"
    reality: "El sensor real declarado es de 96x96 puntos; SuperIR interpola por software hasta 240x240. El detalle térmico real está limitado por los 96x96 puntos que efectivamente mide el sensor."
  - claim: "-20°C a 450°C de rango"
    reality: "Es el rango de medición, no la precisión. Ninguna ficha de este grupo declara el error en °C o % dentro de ese rango, así que no sabes cuánto se puede desviar la lectura en el punto que te interesa."
  - claim: "IP54 (HIKMICRO E01)"
    reality: "Protege contra polvo limitado y salpicaduras leves de agua, no contra lluvia intensa ni inmersión. Es la única cámara del grupo con dato de protección, pero no es un grado alto."

verdicts:
  - profile: "electricista o técnico HVAC que mide equipos calientes"
    pick: "TOPDON TC004 Mini (B0DJQ91653)"
    why: "Único con rango -20°C a 450°C y 25Hz declarados, al precio más bajo de los dos TC004 Mini idénticos."
  - profile: "inspector que necesita documentar y exportar informes"
    pick: "TOPDON TC004 (B0DZ2FZYQH)"
    why: "Único con 64GB, WiFi y análisis por PC según ficha, aunque le faltan datos de rango y batería."
  - profile: "uso doméstico ocasional o exteriores con polvo"
    pick: "HIKMICRO E01 (B0CF28BNNX)"
    why: "Precio bajo y única IP54 declarada del grupo, aunque su sensor nativo (96x96) es el más pequeño."
  - profile: "quiere ubicar visualmente el punto caliente sobre la escena real"
    pick: "HIKMICRO E02 (B0CP99QBVJ)"
    why: "Cámara dual con fusión de imagen según ficha, a cambio de la batería más corta del grupo (8h)."
---

Toda cámara termográfica de este grupo funciona igual en el fondo: un sensor microbolométrico convierte radiación infrarroja en una matriz de temperaturas, punto por punto. El número de esos puntos —la resolución nativa del sensor— es lo que de verdad limita el detalle térmico que puedes ver, no el número de píxeles que aparece en la pantalla final.

Aquí está la trampa técnica de esta categoría: fabricantes como TOPDON (TISR) y HIKMICRO (SuperIR) usan interpolación por software para mostrar imágenes de 240x240 o 512x384 partiendo de sensores más pequeños. Ese proceso suaviza la imagen, pero no añade información térmica que el sensor no captó. Por eso, comparar solo el número de píxeles anunciado te puede llevar a pagar de más sin ganar detalle real.

A partir de ahí, lo que separa a estas cámaras es el resto de la ficha: rango de temperatura medible, frecuencia de refresco, autonomía de batería y si guardan o exportan datos. Ninguno de estos modelos declara un error de medición en °C o %, así que la decisión se reduce a qué rango y qué funciones necesitas, no a qué tan 'preciso' dice ser cada uno.