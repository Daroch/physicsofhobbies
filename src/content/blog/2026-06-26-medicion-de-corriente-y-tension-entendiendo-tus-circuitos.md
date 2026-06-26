---
title: "Medición de Corriente y Tensión: Entendiendo tus Circuitos"
pubDate: 2026-06-26
description: "Aprenderás cómo la medición precisa de parámetros eléctricos con un multímetro True RMS es clave para diagnosticar y optimizar tus proyectos."
referenceUrl: "https://www.amazon.es/dp/B07B8TRBMP"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

¿Tu LED no enciende, el motor gira lento o un componente se calienta en exceso? A menudo, el problema reside en una tensión incorrecta, una corriente insuficiente o una resistencia inesperada en el circuito. Sin herramientas adecuadas, diagnosticar estas fallas es un proceso de adivinanzas.

Un multímetro mide propiedades eléctricas fundamentales como la tensión ($V$), la corriente ($I$) y la resistencia ($R$), interconectadas por la Ley de Ohm: $V = I \cdot R$. Para medir tensión, se conecta en paralelo con el componente; para corriente, se intercala en serie en el circuito; y para resistencia, aplica una pequeña corriente para calcular la tensión.
Un punto crítico es la precisión en corriente alterna (AC). Muchos dispositivos modernos no producen señales AC sinusoidales puras. Los multímetros básicos promedian estas señales, lo que resulta en lecturas erróneas. La función True RMS (Root Mean Square) mide el valor eficaz real, o potencia equivalente en calor, de la señal, independientemente de su forma. Esto asegura mediciones precisas incluso con ondas distorsionadas, algo vital en fuentes de alimentación conmutadas o circuitos de control de motores.

Un error frecuente es intentar medir corriente de una fuente conectando las puntas en paralelo, lo que causa un cortocircuito. Para medir corriente, el multímetro debe insertarse en serie en el circuito, interrumpiendo el flujo. Siempre selecciona la función y el rango adecuados antes de conectar las puntas; por ejemplo, si mides tensión DC, usa el modo DCV.
La categoría de seguridad (CAT III 600V) es crucial. Indica la capacidad del aparato para soportar picos de tensión sin riesgo para el usuario o el equipo. Para un maker, esto es una capa de protección extra al trabajar con circuitos conectados a la red eléctrica o fuentes de alimentación de mayor potencia. No seguir estas indicaciones puede comprometer la seguridad y la fiabilidad de las mediciones.

**Prueba rápida**
1. Con el multímetro en modo de continuidad, toca las puntas entre sí. Debería emitir un pitido y mostrar 0 ohmios.
2. En modo de tensión DC (VDC), mide una pila AA. Debería indicar alrededor de 1.5V.
3. Selecciona el modo de resistencia (Ohmios $\Omega$) y mide una resistencia conocida. Compara el valor con su código de colores o especificación.

El UNI-T UT139C es una buena elección para el maker que necesita mediciones fiables. Su función True RMS es fundamental para trabajar con electrónica moderna, donde las señales AC no siempre son ideales. La certificación CAT III 600V aporta una capa de seguridad importante, y características adicionales como la medición de capacitancia, frecuencia y temperatura amplían su utilidad en diversos proyectos.