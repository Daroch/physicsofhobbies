---
title: "Corriente alterna: la potencia real con True RMS"
pubDate: 2026-06-10
description: "Aprenderás cómo un multímetro mide la electricidad y por qué la función True RMS es fundamental para lecturas precisas en sistemas electrónicos."
referenceUrl: "undefined"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Estás montando un proyecto con un controlador de motor o una fuente de alimentación conmutada y necesitas verificar tensiones o corrientes. Conectas tu LED y no brilla como esperas, o el motor parece lento. Las mediciones te dan un valor, pero no cuadra con lo que ocurre en tu circuito.

Cuando medimos tensión o corriente continua, el valor es directo. En corriente alterna (AC), la cosa cambia. La mayoría de los multímetros económicos están calibrados para ondas sinusoidales perfectas, comunes en la red eléctrica, calculando su valor RMS (Root Mean Square) a partir del valor promedio o pico. Sin embargo, muchos dispositivos electrónicos actuales, como fuentes conmutadas, variadores de frecuencia o controladores de motor, generan ondas AC distorsionadas o pulsos modulados (PWM). Para estas señales no sinusoidales, la estimación del RMS tradicional es incorrecta. La función True RMS de un multímetro mide el verdadero valor efectivo de la señal, calculando la raíz cuadrada del promedio de los cuadrados de sus valores instantáneos. Matemáticamente, esto se expresa como $V_{RMS} = \sqrt{\frac{1}{T} \int_{0}^{T} V(t)^2 dt}$. En la práctica, esto significa que obtienes una lectura precisa de la potencia real que esa señal puede entregar o disipar, independientemente de su forma de onda compleja.

El error más común es confiar en mediciones AC de multímetros que no son True RMS cuando se trabaja con electrónica moderna. Si tu fuente de alimentación es conmutada, si estás usando un dimmer electrónico para LEDs o controlando un motor con PWM, las lecturas AC sin True RMS serán engañosas. Un multímetro sin esta función podría indicar 10V AC cuando el valor efectivo real es 7V o 12V. Al seleccionar un multímetro, prioriza siempre la función True RMS si tu trabajo implica cualquier tipo de electrónica que no sea alimentación de red pura y constante. Esto asegura que los cálculos de potencia (P = $V_{RMS} \times I_{RMS}$) sean correctos, evitando componentes subdimensionados o circuitos que no funcionan como deberían.

Prueba rápida
1.  Enciende el multímetro y selecciona la medición de tensión AC (V~).
2.  Conecta las puntas de prueba a un enchufe de pared. Anota la lectura.
3.  Conecta una lámpara con un dimmer a ese mismo enchufe, y a continuación, mide la tensión AC en los terminales de la lámpara con el dimmer a mitad de potencia.
4.  Compara la lectura del paso 2 (onda sinusoidal) con la del paso 3 (onda distorsionada). La precisión de la segunda lectura, especialmente si tu multímetro tiene True RMS, te dará el valor efectivo real, crucial para saber cuánta potencia llega a la bombilla.

Este multímetro digital profesional con True RMS y retroiluminación es una herramienta sólida para el maker. La función True RMS lo hace adecuado para diagnosticar y diseñar circuitos con fuentes de alimentación conmutadas, variadores de velocidad o sistemas de iluminación LED. Su retroiluminación mejora la visibilidad en entornos de taller con poca luz, facilitando lecturas claras.