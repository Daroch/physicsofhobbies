---
title: "Fuentes reguladas: Tensión constante, corriente limitada"
pubDate: 2026-07-04
description: "Aprenda cómo una fuente de alimentación regulable protege sus proyectos electrónicos y el papel de tensión y corriente en su funcionamiento."
referenceUrl: "https://www.amazon.es/dp/B0CN6WRZFS"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Al desarrollar proyectos electrónicos, es común iniciar con fuentes de alimentación improvisadas, como cargadores de teléfono o baterías. Sin embargo, estos suministros suelen ofrecer un voltaje fijo y carecen de control sobre la corriente. Esta limitación puede llevar a voltajes inestables bajo carga, componentes sobrecalentados o incluso dañados, y dificultad para replicar resultados. La falta de un suministro de energía fiable y ajustable complica enormemente el proceso de depuración y desarrollo.

Una fuente de alimentación regulable de laboratorio se basa en principios de control de potencia y realimentación negativa. Su propósito principal es mantener una tensión de salida constante (modo CV o Constant Voltage) y, simultáneamente, limitar la corriente de salida a un valor preestablecido (modo CC o Constant Current). Esto es crucial para proteger el circuito bajo prueba. La Ley de Ohm, $V = I \cdot R$, explica la interdependencia entre tensión, corriente y resistencia. Si un componente en nuestro circuito presenta una baja resistencia (por ejemplo, un cortocircuito accidental), la corriente $I$ tendería a dispararse según la fórmula si la tensión $V$ se mantiene. Es aquí donde la función de limitación de corriente actúa, evitando que el exceso de corriente cause daños irreparables al componente o a la propia fuente. La fuente transiciona automáticamente entre el modo CV y CC para asegurar que ni la tensión ni la corriente superen los límites configurados.

Un error frecuente entre los makers es configurar únicamente la tensión de salida. Sin embargo, el ajuste del límite de corriente es igualmente vital y a menudo se ignora o se configura demasiado alto. Antes de conectar cualquier circuito a la fuente, establezca la tensión deseada, por ejemplo, 5V. Luego, ajuste el límite de corriente a un valor ligeramente superior al consumo máximo esperado por su proyecto; si no está seguro, comience con un valor conservador, como 0.1A, y aumente gradualmente si el circuito no funciona. Esta práctica crea una barrera de seguridad: si ocurre un cortocircuito o el circuito consume demasiada energía, la fuente limitará la corriente y protegerá los componentes, en lugar de entregar toda su potencia. Un límite de corriente excesivamente alto anula esta protección esencial.

Prueba rápida:
Para comprobar el funcionamiento correcto de su fuente regulable, puede realizar una prueba sencilla:
1.  Ajuste la tensión de la fuente a 5V y el límite de corriente a 0.5A. Desactive la salida.
2.  Conecte un multímetro en modo amperímetro directamente a las bornas de salida de la fuente (simulando un cortocircuito controlado).
3.  Active la salida. El multímetro debería indicar aproximadamente 0.5A, y la fuente debería mostrar que está operando en modo de corriente constante (CC).
4.  Ahora, ajuste la tensión a 12V y el límite de corriente a 1A. Conecte una resistencia de carga adecuada (por ejemplo, 12 ohmios, 5W) a la salida. El multímetro, configurado como voltímetro en paralelo, debería mostrar 12V, y la corriente medida en serie debería ser de 1A, indicando el modo de tensión constante (CV).

La fuente de alimentación WANPTEK 30V 5A es una elección práctica para un taller maker, ofreciendo un balance entre prestaciones y precio. Con su capacidad de 30 voltios y 5 amperios, cubre las necesidades de la mayoría de proyectos de electrónica doméstica, desde el desarrollo con microcontroladores ESP32 o Arduino hasta la alimentación de pequeños motores o tiras de LED. Sus displays digitales permiten un ajuste y monitoreo preciso de la tensión y la corriente, un aspecto fundamental para la experimentación segura y eficiente en el banco de trabajo, minimizando el riesgo de dañar componentes valiosos.