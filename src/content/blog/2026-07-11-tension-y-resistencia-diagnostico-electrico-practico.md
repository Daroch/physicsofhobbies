---
title: "Tensión y Resistencia: Diagnóstico eléctrico práctico"
pubDate: 2026-07-11
description: "Este artículo explica cómo un multímetro mide propiedades eléctricas básicas y por qué la función True RMS es relevante para tus proyectos maker."
referenceUrl: "https://www.amazon.es/dp/B07FMJX5RL"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Estás trabajando en un proyecto electrónico y algo no funciona. Un LED no enciende, un motor no gira o una placa de desarrollo no arranca. La frustración surge cuando no sabes dónde está el fallo: ¿falta alimentación? ¿Hay un cortocircuito? ¿El componente está defectuoso? Sin visibilidad en el flujo eléctrico, el diagnóstico se convierte en una suposición.

Un multímetro mide propiedades eléctricas fundamentales. La resistencia se determina aplicando una pequeña tensión conocida y cuantificando la corriente resultante, una aplicación directa de la Ley de Ohm ($R = V/I$). La tensión es la diferencia de potencial eléctrico entre dos puntos, la 'presión' que impulsa los electrones. La corriente es el flujo de carga a través de un punto en el circuito por unidad de tiempo. Para corriente alterna (AC), la forma de onda no siempre es una sinusoide pura. Aquí, la función 'True RMS' es crucial. Un multímetro convencional asume una onda senoidal para calcular el valor efectivo. Un medidor True RMS, en cambio, calcula el valor cuadrático medio real de la señal, sin importar si su forma está distorsionada por armónicos o transitorios. Esto proporciona una medición precisa en circuitos con fuentes conmutadas, drivers LED o controladores de motor, donde las ondas pueden ser muy complejas y alejadas de una senoidal ideal.

Uno de los errores más comunes es la conexión incorrecta para medir corriente. Para tensión o resistencia, el multímetro se conecta en paralelo con la parte del circuito a medir. Para medir corriente, el multímetro debe insertarse en serie con el circuito, interrumpiéndolo. Esto significa que la corriente total del circuito debe fluir a través del multímetro. Si se conecta un amperímetro en paralelo, su muy baja resistencia interna actuará como un cortocircuito. Esto puede dañar los fusibles internos del multímetro, el propio dispositivo o incluso la fuente de alimentación. Al seleccionar un multímetro para tus proyectos maker, el soporte de True RMS no es una característica trivial. Ignorar esta especificación puede llevar a lecturas de voltaje y corriente alterna con errores significativos, del orden del 10% al 40%, en entornos donde abundan las formas de onda distorsionadas. Un diagnóstico basado en datos imprecisos es inútil.

**Prueba rápida**
1. Configura el multímetro en la escala de voltaje DC (V=).
2. Coloca la punta roja en el terminal positivo (+) de una pila AAA y la punta negra en el negativo (-).
3. Lee el valor mostrado. Una pila nueva o cargada debería marcar aproximadamente 1.5V.
4. Cambia a la función de continuidad (generalmente un símbolo de diodo o una campana) y toca ambas puntas del multímetro a los extremos de un cable. Debería sonar un pitido si el cable no está roto.

El ANENG AN8008 es un multímetro digital compacto que integra la funcionalidad True RMS. Su tamaño lo hace idóneo para el banco de trabajo doméstico y facilita su transporte a cualquier lugar. Es una elección práctica para el maker que necesita realizar mediciones fiables de tensión, corriente, resistencia y continuidad en proyectos de electrónica general, desde depuración de prototipos con microcontroladores hasta tareas de mantenimiento eléctrico en el hogar.