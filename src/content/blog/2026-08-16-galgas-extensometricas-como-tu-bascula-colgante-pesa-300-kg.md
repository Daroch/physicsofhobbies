---
title: "Galgas extensométricas: cómo tu báscula colgante pesa 300 kg"
pubDate: 2026-08-16
description: "Colgar un ciervo de 80 kg de una báscula de baño no funciona, pero un sensor del tamaño de tu dedo pulgar sí puede con 300 kg."
category: "mecánica"
image: "/images/blog/2026-08-16-galgas-extensometricas-como-tu-bascula-colgante-pesa-300-kg.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0DBZHDCZ5?tag=physicshobbie-21"
productName: "GRAM PRES Báscula Digital Colgante 660 lb/300 kg Con Gancho"
---

Vuelves de cazar o de pescar y necesitas saber cuánto pesa la pieza antes de despiezarla, o levantas un saco de pienso y no tienes ni idea de si son 20 o 40 kilos. Las básculas de plataforma no sirven para esto: no puedes poner un jabalí entero sobre un plato, y menos en el bosque sin corriente eléctrica. Necesitas algo que cuelgue del objeto y te dé el peso al instante, sin cables a la pared ni superficie plana donde apoyarlo.

El truco está dentro del gancho, en una pieza metálica llamada celda de carga con galgas extensométricas pegadas a su superficie. Cuando cuelgas el peso, esa pieza se deforma —muy poco, micras— y las galgas (resistencias eléctricas en zigzag) cambian su resistencia proporcionalmente a esa deformación. La relación es lineal según la ley de Hooke, $F = k \cdot x$, donde $x$ es la deformación y $k$ la rigidez del material. Cuatro galgas conectadas en configuración de puente de Wheatstone convierten ese cambio minúsculo de resistencia en una señal de voltaje que el microcontrolador traduce a kilogramos. El porqué de que sean cuatro y no una, y de dónde sale la cifra de 2 mV/V que verás en cualquier ficha de celda de carga, lo tienes en [cómo funciona una celda de carga](/blog/2026-08-16-de-micras-a-milivoltios-como-funciona-una-celda-de-carga/).

Aquí está el error que comete casi todo el mundo: tirar del gancho en ángulo en vez de dejar que la carga cuelgue perfectamente vertical. Si el peso tira en diagonal, estás metiendo una componente de fuerza lateral que la celda no está calibrada para medir, y el número que ves se aleja del real. La precisión que anuncia el fabricante (normalmente ±0.1% del fondo de escala) solo se cumple con tracción axial pura, es decir, colgando en línea recta desde el punto de suspensión hasta la carga.

Prueba rápida para verificar que tu báscula no miente:
1. Cuelga un objeto de peso conocido (una garrafa de agua de 5 litros pesa casi exactamente 5 kg).
2. Anota la lectura y compárala con el valor real.
3. Repite tirando ligeramente en ángulo, no en vertical.
4. Compara ambas lecturas: si difieren más del 2%, ya sabes por qué tus pesadas de campo no cuadran.

Esta báscula GRAM PRES cubre un rango de 0 a 300 kg con función de tara y bloqueo de lectura (hold), útil cuando el peso oscila porque cuelga de una cuerda con movimiento, como una pieza de caza recién colgada. El gancho de acero soporta cargas altas sin deformarse permanentemente, pero como cualquier celda de carga económica, pierde precisión relativa cerca del límite superior: para pesos de 250-300 kg el margen de error crece, así que si tu uso habitual ronda esas cifras, conviene contrastarla periódicamente con un peso patrón.