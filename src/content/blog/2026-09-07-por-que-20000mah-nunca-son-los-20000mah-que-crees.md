---
title: "Por qué 20000mAh nunca son los 20000mAh que crees"
pubDate: 2026-09-07
description: "Esa batería externa promete 20000mAh, pero la energía real que le entrega a tu móvil es bastante menor de lo que marca la etiqueta."
category: "electrónica"
image: "/images/blog/2026-09-07-por-que-20000mah-nunca-son-los-20000mah-que-crees.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0DSPVDYQ9?tag=physicshobbie-21"
productName: "UGREEN Nexode 45W Power Bank 20000mAh Batería Externa Portátil"
---

Te ha pasado: compras una batería externa de 20000mAh esperando cargar tu móvil de 4000mAh cinco veces, y en la práctica te da para tres cargas y media. No es publicidad engañosa, es física de conversión de voltaje que casi nadie te explica en la caja del producto.

Los mAh miden carga eléctrica, no energía. La batería interna del power bank funciona a 3.7V (química de litio), pero tu móvil se carga a 5V, 9V o incluso más con Power Delivery. La energía real disponible es $E = V \times Q$, así que 20000mAh a 3.7V son unos 74Wh. Cuando esa energía pasa por el conversor DC-DC para subir el voltaje a 5V o 9V, pierdes entre un 15% y un 30% en forma de calor, según la eficiencia del circuito. Además, la potencia de carga rápida depende de $P = V \times I$: unos 45W reales requieren combinaciones como 9V a 5A o 20V a 2.25A, y el power bank tiene que negociar ese acuerdo con tu dispositivo mediante protocolos como PD o QC.

La mayoría de gente ignora dos cosas al elegir un power bank de carga rápida: la eficiencia real de conversión (raramente se anuncia, pero ronda el 80-85% en productos decentes) y si el cable y el puerto soportan realmente la potencia prometida. Un cable USB-C barato limita la corriente aunque el power bank pueda entregar 45W. Si te importa la velocidad de carga, fíjate en el protocolo compatible (PD3.0, PPS) más que en el número de vatios aislado, porque ese número solo se alcanza si tu dispositivo lo pide y lo acepta.

**Prueba rápida:**
1. Carga completamente tu móvil desde 0% usando el power bank y anota cuánto porcentaje de batería del power bank consumió el LED indicador.
2. Compara ese consumo con la capacidad teórica de tu móvil (por ejemplo, si tu móvil tiene 4000mAh y el power bank bajó un 25%, deberías esperar unas 4 cargas completas).
3. Si te da menos de 3 cargas completas con un power bank de 20000mAh, la eficiencia real ronda el 60-70%, dentro de lo normal para conversión de voltaje.
4. Repite la prueba usando un cable diferente y compara tiempos de carga: si cambia mucho, el cuello de botella era el cable, no la batería.

Este UGREEN Nexode integra un cable USB-C, lo que evita el problema típico de cables de baja calidad limitando la potencia, y sus tres puertos permiten repartir hasta 45W entre varios dispositivos simultáneamente. La limitación real está en que, como cualquier power bank de esta capacidad, la eficiencia de conversión hará que nunca veas los 20000mAh completos reflejados en tu dispositivo, algo inherente a la física del proceso y no un defecto específico de este producto.

---

**¿Comparando modelos?** En [Power bank 20000mAh: potencia (W) o cable USB-C](/blog/2026-08-24-power-bank-20000mah-potencia-w-o-cable-usb-c/) analizo varias fichas de este tipo de producto y qué dato de la ficha decide la compra.
