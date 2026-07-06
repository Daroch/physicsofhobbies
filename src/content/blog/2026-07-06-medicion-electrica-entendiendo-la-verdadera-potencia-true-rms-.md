---
title: "Medición eléctrica: Entendiendo la verdadera potencia (True RMS)"
pubDate: 2026-07-06
description: "Aprenderá cómo un multímetro mide con precisión las señales eléctricas variables y la importancia de la función True RMS en sus proyectos."
referenceUrl: "https://www.amazon.es/dp/B0CB9SK4NF"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Al montar un circuito con un microcontrolador o conectar una tira de LEDs, a veces los componentes no responden como deberían, o los resultados son inconsistentes. Sospechamos un fallo eléctrico, pero sin las herramientas adecuadas, es difícil identificar si el problema radica en un voltaje insuficiente, una corriente excesiva o una señal de alimentación inestable. Medir con precisión es el primer paso para un diagnóstico correcto.

Un multímetro cuantifica magnitudes eléctricas como voltaje, corriente y resistencia. Para corriente alterna (CA), la complejidad aumenta, ya que la señal cambia constantemente. Los multímetros tradicionales, sin función True RMS, miden el valor promedio rectificado de una onda senoidal, escalándolo para aproximar su valor RMS. Esto funciona para ondas senoidales puras, pero muchas señales en el mundo maker (salidas de controladores PWM, fuentes conmutadas, dimmers) no lo son. Para estas, el valor efectivo real, o RMS (Root Mean Square), se calcula mediante: $V_{RMS} = \sqrt{\frac{1}{T}\int_{0}^{T} v^2(t) dt}$. Esta expresión matemática significa que el multímetro calcula el cuadrado de cada valor instantáneo del voltaje, promedia esos cuadrados durante un período, y luego toma la raíz cuadrada de ese promedio. El resultado es el valor de voltaje de CC equivalente que produciría la misma cantidad de calor en una resistencia. Esto es crucial porque la potencia disipada en una carga depende del cuadrado del voltaje o la corriente, independientemente de la forma de onda.

El error común es asumir que la medición de voltaje o corriente alterna es precisa con cualquier multímetro. Si su proyecto implica fuentes de alimentación conmutadas, variadores de velocidad para motores (PWM), dimmers LED o cualquier sistema que genere formas de onda no senoidales, un multímetro sin True RMS le dará lecturas erróneas. Al comprar, asegúrese de que el multímetro especifique 'True RMS'. Esto es crucial para obtener el valor de energía real y evitar diagnosticar un problema inexistente o pasar por alto uno real. La especificación de 'cuentas' (6000 en este caso) indica la resolución máxima que puede mostrar, permitiendo mediciones más finas.

Prueba rápida:
1.  Conecte una bombilla incandescente a un dimmer de pared.
2.  Encienda el multímetro en la función de medición de voltaje AC (V~).
3.  Conecte las puntas de prueba en paralelo a la bombilla (o a la salida del dimmer).
4.  Ajuste el dimmer a una posición intermedia. El valor medido por un multímetro True RMS le indicará el voltaje efectivo real que recibe la bombilla, que es el valor relevante para la potencia que consume.

El multímetro UNI-T UT890C, con sus 6000 cuentas y función True RMS, es una herramienta versátil para el taller maker. Permite diagnosticar problemas en fuentes de alimentación conmutadas, circuitos PWM y otros sistemas electrónicos modernos donde las formas de onda no son senoidales. Su capacidad True RMS asegura que las mediciones de voltaje y corriente alterna reflejen la potencia real, crucial para proyectos donde la precisión es un requisito.