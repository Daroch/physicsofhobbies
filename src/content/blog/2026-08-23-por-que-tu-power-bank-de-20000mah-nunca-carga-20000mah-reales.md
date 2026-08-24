---
title: "Por qué tu power bank de 20000mAh nunca carga 20000mAh reales"
pubDate: 2026-08-23
description: "La capacidad que ves en la caja y la que realmente llega a tu móvil son dos números distintos, y la diferencia tiene explicación física."
category: "electrónica"
image: "/images/blog/2026-08-23-por-que-tu-power-bank-de-20000mah-nunca-carga-20000mah-reales.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0F84D5PRT?tag=physicshobbie-21"
productName: "Power Bank 22.5W 20000mAh Bateria Externa Carga Rapida"
---

Compras una batería externa de 20000mAh pensando que vas a cargar tu móvil de 4000mAh cinco veces. Al tercer ciclo ya está agotada y te preguntas si te han engañado. No te han engañado, pero sí te han contado solo la mitad de la historia.

Las celdas de litio dentro de este power bank trabajan a 3.7V nominales. Cuando el dispositivo convierte esa energía a los 5V, 9V o 12V que exige el USB-C de salida, pierde parte en el proceso. La energía real disponible se calcula como $E = V \times I \times t$, y al subir el voltaje de salida baja proporcionalmente la corriente si quieres mantener la misma potencia. Además, ningún convertidor DC-DC es perfecto: la eficiencia típica ronda el 80-85%, así que de esos 20000mAh anunciados (medidos a 3.7V) terminas recibiendo algo como 20000 × 3.7 × 0.82 / 5 ≈ 12300mAh útiles a 5V. Es física de conversión de energía, no publicidad engañosa, aunque pocas fichas técnicas lo explican con claridad.

Aquí es donde entra la carga rápida PD3.0 y QC4.0 que trae este modelo. Estos protocolos no aumentan la energía disponible, negocian con tu dispositivo el voltaje óptimo para transferir la misma potencia con menos pérdidas resistivas. La fórmula que manda es $P = V \times I$: si subes el voltaje a 9V o 12V, necesitas menos corriente para los mismos 22.5W, y como las pérdidas por calor en el cable dependen de $I^2 \times R$, menos corriente significa menos calentamiento y más eficiencia real. La pantalla LCD te sirve precisamente para esto: en vez de fiarte de una estimación por LEDs, ves el porcentaje real y muchas veces la potencia instantánea de carga, que te dice si el protocolo rápido está realmente funcionando o si tu cable se ha quedado corto.

**Prueba rápida (5 minutos):**
1. Carga el power bank al 100% y anota el dato en la pantalla LCD.
2. Conecta tu móvil con un cable USB-C certificado (no cualquiera) y déjalo cargar hasta que el power bank marque 0%.
3. Compara el porcentaje de batería ganado en tu móvil con el porcentaje teórico que debería dar la capacidad anunciada.
4. Si la diferencia ronda el 30-35%, tu power bank funciona dentro de lo normal para la física de conversión, no está defectuoso.

Este modelo entrega 22.5W combinando PD3.0 y QC4.0, lo que cubre la mayoría de smartphones actuales sin necesitar un cargador rápido aparte. La pantalla LCD es su punto útil real: te evita adivinar cuánta carga queda, algo que los power banks con solo LEDs no resuelven bien. Como limitación, 22.5W no es suficiente para cargar rápido portátiles o tablets grandes, así que si buscas eso necesitas revisar la potencia máxima antes de comprar.