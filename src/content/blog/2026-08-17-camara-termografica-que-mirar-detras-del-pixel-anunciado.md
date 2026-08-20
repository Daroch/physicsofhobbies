---
title: "Cámara termográfica: qué mirar detrás del pixel anunciado"
pubDate: 2026-08-17
description: "El pixel final que anuncian (SuperIR/TISR) no es el sensor real: qué declara cada ficha, y qué se calla, es lo que decide la compra."
category: "óptica"
tags: ["comparativa", "ciencia", "hobbies"]
type: "roundup"
image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-1.jpg"

audience: "Esto es para quien necesita localizar fugas térmicas, puntos calientes eléctricos o defectos de aislamiento en HVAC. No es para quien necesita medición de temperatura certificada o con trazabilidad, porque ninguna ficha de este grupo declara un error de precisión en °C o %."

specsThatMatter:
  - spec: "Resolución IR real vs. interpolada (SuperIR/TISR)"
    why: "El sensor microbolométrico tiene un número fijo de puntos de medida térmica. HIKMICRO es la única marca aquí que separa las dos cifras en su ficha: sensor de 96x96 y 240x240 por SuperIR. TOPDON anuncia 512x384 declarando TISR, y AMPBANK anuncia 240x240 declarando TISR, pero ninguna de las dos dice de qué sensor parte. Interpolar suaviza la imagen; no añade puntos que el sensor no midió."
  - spec: "Rango de temperatura medible"
    why: "El TC004 Mini y el AMPBANK declaran -20°C a 450°C; las otras tres fichas no dan rango. Para electricidad industrial o equipos calientes ese límite importa; para revisar fugas de aire en una vivienda sobra. Ninguna ficha da el error en °C o % dentro de ese rango, así que el número solo sirve para descartar equipos que no llegan, no para confiar en la lectura."
  - spec: "Frecuencia de actualización (Hz)"
    why: "Determina si la imagen se ve fluida al mover la cámara o al inspeccionar algo en movimiento (motor, correa). Los 25 Hz solo aparecen en las fichas del TC004 Mini y del AMPBANK; para las otras tres el dato no está disponible, y una tasa baja se nota como arrastre al barrer una pared."
  - spec: "Duración de batería y almacenamiento"
    why: "Va de 8h (HIKMICRO E02) a 24h (AMPBANK) según ficha. El almacenamiento solo lo declaran los HIKMICRO (4GB) y el TC004 grande (64GB, con WiFi y análisis por PC); el TC004 Mini y el AMPBANK no dicen nada, lo que importa si necesitas exportar informes en vez de solo mirar la pantalla in situ."
  - spec: "Protección IP"
    why: "Dos fichas la declaran y con distinto grado: IP65 (AMPBANK) e IP54 (HIKMICRO E01). En la norma IEC 60529 el primer dígito es polvo y el segundo agua: el 6 es estanco al polvo frente al 5, que solo lo limita, y el 5 aguanta chorros a baja presión frente al 4, que solo cubre salpicaduras. Ninguno de los dos cubre inmersión. Las otras tres fichas no dan dato."

chooseBy:
  - scenario: "trabajas con instalaciones eléctricas u hornos que superan los 100°C"
    priority: "rango de temperatura declarado (-20 a 450°C: TC004 Mini o AMPBANK)"
  - scenario: "necesitas documentar inspecciones con informes o exportar a PC"
    priority: "almacenamiento y WiFi (TC004 grande, 64GB)"
  - scenario: "trabajas en obra o exteriores con polvo y agua"
    priority: "el grado IP más alto declarado (AMPBANK, IP65)"
  - scenario: "inspeccionas piezas en movimiento (motores, correas)"
    priority: "frecuencia de actualización alta (25 Hz: TC004 Mini o AMPBANK)"

comparison:
  columns: ["Resolución IR (ficha)", "Rango temperatura", "Frecuencia actualización", "Duración batería", "Almacenamiento", "Precio (€)"]
  derivedNote: "No se incluye columna calculada: ninguna combinación de estas columnas produce un dato físico nuevo, y calcular «precio por resolución» solo mediría el marketing de cada ficha, no el aparato."

products:
  - name: "TOPDON Camara Termica TC004 Mini, Resolución IR de 240x240 Camara Termografica, -20℃ a 450℃, 15 Horas Duración de Batería, 25 Hz Frecuencia de Actualización, Alertas de Temperatura Alta/Baja"
    shortName: "TOPDON TC004 Mini"
    tier: "Rango y Hz declarados"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-1.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DJQ91653?tag=physicshobbie-21"
    price: 159.98
    rating: 4.5
    reviews: 1495
    specs: ["240x240 (la ficha no dice si es nativo o TISR)", "-20°C a 450°C", "25 Hz", "15 h", "no disponible", "159.98"]
    highlight: "Es la ficha más completa del grupo: rango, Hz y batería declarados, al precio más bajo de las que dan ese rango. Ojo con el catálogo: este mismo TC004 Mini está publicado también con otro ASIN (B0DJD2P3FF) y ficha idéntica a 193,62 €, así que no son dos opciones que comparar sino el mismo aparato dos veces."
  - name: "TOPDON Cámara Termografica TC004 con 512x384 Resolución TISR, 64GB Almacenamiento, 3,5″ Pantalla Camara Termica con Wifi, Grabación de Vídeo, Análisis de PC, para Inspección Eléctrica/Climatización"
    shortName: "TOPDON TC004 (512x384)"
    tier: "Almacenamiento y WiFi"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-2.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DZ2FZYQH?tag=physicshobbie-21"
    price: 303.99
    rating: 4.5
    reviews: 1495
    specs: ["512x384 (vía TISR; sin sensor nativo declarado)", "no disponible", "no disponible", "no disponible", "64GB + WiFi", "303.99"]
    highlight: "Es el único con pantalla de 3,5\", 64GB y análisis por PC según su ficha, pero no declara rango de temperatura, Hz ni batería. Es también el más caro del grupo, y lo que justifica ese precio en el anuncio es precisamente la cifra interpolada."
  - name: "Camara Termica HIKMICRO E01 con Puntero Láser, IR 96x96 | 240x240 SuperIR, 11h de duración, 4 GB, Video, 2m y IP54, Herramientas para el hogar, HVAC y eléctricas"
    shortName: "HIKMICRO E01"
    tier: "Sensor declarado, barato"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-4.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CF28BNNX?tag=physicshobbie-21"
    price: 159
    rating: 4.4
    reviews: 1270
    specs: ["96x96 nativo | 240x240 SuperIR", "no disponible", "no disponible", "11 h", "4GB", "159"]
    highlight: "Su ficha es de las dos únicas que declaran el sensor real (96x96), el más pequeño del grupo, y eso es una ventaja informativa aunque el número sea bajo: sabes lo que compras. Declara IP54, un grado por debajo del IP65 del AMPBANK, y no da rango de temperatura ni Hz."
  - name: "Camara Termica HIKMICRO E02 con Cámara Visual, 96x96 IR | Cámara dual, puntero láser, SuperIR 240x240, imagen por fusión, 8h de duración, 4GB, video"
    shortName: "HIKMICRO E02"
    tier: "Cámara dual, fusión"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-5.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CP99QBVJ?tag=physicshobbie-21"
    price: 179.99
    rating: 4.5
    reviews: 744
    specs: ["96x96 nativo | 240x240 SuperIR", "no disponible", "no disponible", "8 h", "4GB", "179.99"]
    highlight: "Añade cámara visual y fusión de imagen para ubicar el punto caliente sobre la foto real, según su ficha. Tiene la batería más corta del grupo (8h) y el mismo sensor de 96x96 que el E01, del que se diferencia por la óptica visible, no por la térmica."
  - name: "AMPBANK Camara Termica 240x240 TISR Resolución, Camara Termografica con 24 Horas Duración de Batería, 25 Hz, -20℃ a 450℃ Rango de Temperatura con Alarma de Temperatura, IP65"
    shortName: "AMPBANK 240x240 TISR"
    tier: "IP65 y 24 h"
    image: "/images/blog/2026-08-17-camara-termografica-que-mirar-detras-del-pixel-anunciado-6.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DFM69TPS?tag=physicshobbie-21"
    price: 179.99
    rating: 4.5
    reviews: 605
    specs: ["240x240 (declarado TISR; sin sensor nativo)", "-20°C a 450°C", "25 Hz", "24 h", "no disponible", "179.99"]
    highlight: "Anuncia exactamente la misma cifra que el TC004 Mini —240x240— pero es la única de las dos que aclara que ese número es TISR, o sea interpolado. Eso no la hace peor: la hace más explícita, y deja abierta la duda de qué hacen las que no lo dicen. Declara la batería más larga (24h) y el grado IP más alto (IP65), pero no dice de qué sensor parte ni si guarda imágenes."

pitfalls:
  - claim: "«240x240» en dos fichas distintas"
    reality: "El TC004 Mini y el AMPBANK anuncian la misma cifra, pero solo el AMPBANK declara que es TISR (interpolada). Cuando dos anuncios dan el mismo número y uno explica cómo lo obtiene, el que calla no es necesariamente mejor: es que no lo cuenta."
  - claim: "SuperIR 240x240 (HIKMICRO)"
    reality: "El sensor real declarado es de 96x96 puntos; SuperIR interpola por software hasta 240x240. El detalle térmico está limitado por los 96x96 puntos que efectivamente mide el sensor, y la ficha es de las pocas que te deja calcular esa diferencia."
  - claim: "-20°C a 450°C de rango"
    reality: "Es el rango de medición, no la precisión. Ninguna ficha de este grupo declara el error en °C o % dentro de ese rango, así que no sabes cuánto se puede desviar la lectura en el punto que te interesa."
  - claim: "IP65 / IP54"
    reality: "En la IEC 60529 el primer dígito es polvo y el segundo agua. IP65 es estanco al polvo y aguanta chorros a baja presión; IP54 solo limita la entrada de polvo y cubre salpicaduras. Ninguno de los dos protege frente a inmersión, y las otras tres fichas no declaran nada."

verdicts:
  - profile: "electricista o técnico HVAC que mide equipos calientes"
    pick: "TOPDON TC004 Mini (B0DJQ91653)"
    why: "Rango -20°C a 450°C y 25 Hz declarados, al precio más bajo de las dos fichas que dan ese rango."
  - profile: "inspector que necesita documentar y exportar informes"
    pick: "TOPDON TC004 (B0DZ2FZYQH)"
    why: "Único con 64GB, WiFi y análisis por PC según ficha, aunque le faltan datos de rango, Hz y batería."
  - profile: "trabajo en obra o exteriores, jornadas largas"
    pick: "AMPBANK (B0DFM69TPS)"
    why: "IP65 y 24h de batería, los dos valores más altos declarados del grupo, con el mismo rango y Hz que el TC004 Mini."
  - profile: "uso doméstico ocasional con presupuesto ajustado"
    pick: "HIKMICRO E01 (B0CF28BNNX)"
    why: "El más barato, y su ficha declara el sensor real (96x96) en vez de solo la cifra interpolada."
  - profile: "quiere ubicar visualmente el punto caliente sobre la escena real"
    pick: "HIKMICRO E02 (B0CP99QBVJ)"
    why: "Cámara dual con fusión de imagen según ficha, a cambio de la batería más corta del grupo (8h)."
  - profile: "necesita un valor de temperatura fiable, no un mapa relativo"
    pick: "Ninguna de estas cinco"
    why: "Ninguna ficha declara error de medición en °C o %. Sirven para ver dónde está el punto caliente, no para afirmar a cuántos grados está."
---

Toda cámara termográfica de este grupo funciona igual en el fondo: un sensor microbolométrico convierte radiación infrarroja en una matriz de temperaturas, punto por punto. El número de esos puntos —la resolución nativa del sensor— es lo que de verdad limita el detalle térmico que puedes ver, no el número de píxeles que aparece en la pantalla final.

Aquí está la trampa técnica de esta categoría: TOPDON (TISR), AMPBANK (también TISR) y HIKMICRO (SuperIR) usan interpolación por software para mostrar imágenes de 240x240 o 512x384 partiendo de sensores más pequeños. Ese proceso suaviza la imagen, pero no añade información térmica que el sensor no captó. Y la asimetría interesante está en quién lo dice: HIKMICRO publica las dos cifras por separado y AMPBANK nombra su TISR, mientras que la ficha del TC004 Mini anuncia 240x240 sin aclarar de dónde salen. Comparar solo el número anunciado te puede llevar a pagar de más sin ganar detalle real.

A partir de ahí, lo que separa a estas cámaras es el resto de la ficha: rango de temperatura medible, frecuencia de refresco, autonomía de batería, protección IP y si guardan o exportan datos. Ninguno de estos modelos declara un error de medición en °C o %, así que la decisión se reduce a qué rango y qué funciones necesitas, no a lo «preciso» que diga ser cada uno.
