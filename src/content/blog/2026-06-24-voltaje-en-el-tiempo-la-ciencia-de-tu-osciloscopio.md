---
title: "Voltaje en el tiempo: La ciencia de tu osciloscopio"
pubDate: 2026-06-24
description: "Aprenderá cómo un osciloscopio revela la forma de las señales eléctricas y qué características clave debe considerar para sus proyectos."
referenceUrl: "https://www.amazon.es/dp/B08B5X6L2K"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Estás montando un circuito con un microcontrolador y los sensores no responden como esperas. O quizá el motor paso a paso hace un ruido extraño y no sabes por qué. Un multímetro puede decirte si hay voltaje o corriente, pero no te muestra *cómo* cambia ese voltaje o corriente con el tiempo, lo cual es fundamental para diagnosticar fallos en sistemas dinámicos.

Un osciloscopio es un instrumento que grafica la tensión eléctrica (voltaje) en el eje vertical contra el tiempo en el eje horizontal. Esto te permite visualizar la forma de onda de una señal, su amplitud (pico a pico), frecuencia, período, y si presenta ruido, picos anómalos o distorsiones. Entender estas características es clave para verificar el correcto funcionamiento de un circuito o identificar problemas de temporización. La característica más importante a considerar en un osciloscopio es su ancho de banda, que define la frecuencia máxima de la señal que puede medir y mostrar con fidelidad sin atenuación significativa. Para observar una señal periódica sin distorsión significativa en su forma, el ancho de banda del osciloscopio ($f_{BW}$) debería ser al menos cinco veces la frecuencia de la señal que se desea analizar. Si solo se busca detectar la presencia de una señal, el límite teórico del teorema de Nyquist-Shannon es de dos veces la frecuencia, pero la forma de onda resultante será menos precisa.

El error común para muchos aficionados es subestimar la importancia del ancho de banda y asumir que cualquier osciloscopio servirá. Un dispositivo de 15 MHz como el FNIRSI DSO150 es muy útil para depurar proyectos con microcontroladores, donde se manejan señales de GPIO, I2C, SPI o PWM a frecuencias que suelen estar en el rango de los cientos de kHz a pocos MHz. También es apto para analizar señales de audio o rizado en fuentes de alimentación. Sin embargo, si tu proyecto implica comunicaciones USB 2.0 (480 Mbps, con componentes de señal de hasta 240 MHz), Ethernet (100 Mbps o 1 Gbps) o circuitos de radiofrecuencia más allá de unos pocos MHz, este osciloscopio no mostrará fielmente la forma de onda. Al seleccionar un osciloscopio, o al usar este, siempre compara su ancho de banda con la frecuencia fundamental más alta de la señal que quieres observar. Por ejemplo, para ver una señal cuadrada de 3 MHz con sus armónicos, un ancho de banda de 15 MHz ($3 \text{ MHz} \times 5 = 15 \text{ MHz}$) sería el mínimo recomendado para una visualización precisa de su forma. Ignorar esta regla te llevará a interpretaciones erróneas de tus circuitos.

**Prueba rápida**
1.  Conecta la sonda del osciloscopio a un pin digital de un Arduino configurado para generar una señal PWM (por ejemplo, `analogWrite(9, 128);`).
2.  Conecta la masa del osciloscopio a la masa del Arduino.
3.  Ajusta la escala de tiempo (horizontal) a unos 500 µs/div y la escala de voltaje (vertical) a 1 V/div.
4.  Observa la forma de onda cuadrada, su frecuencia y el ciclo de trabajo (duty cycle) de la señal PWM. Puedes variar `analogWrite` para ver el cambio en el ciclo de trabajo.

El FNIRSI DSO150 es un osciloscopio portátil de 15 MHz con un solo canal, diseñado para ser compacto y accesible, especialmente para el maker. Es una opción sólida para quienes se inician en la electrónica o necesitan una herramienta de diagnóstico básica para proyectos con señales de baja a media frecuencia, como la mayoría de los trabajos con Arduino, sensores y pequeños motores. Su naturaleza portátil y su alimentación por batería lo hacen especialmente útil para trabajos de campo, en espacios reducidos o simplemente para evitar tener un equipo voluminoso en tu banco de trabajo, permitiéndote ver las señales en situaciones donde un multímetro no ofrecería la información visual necesaria.