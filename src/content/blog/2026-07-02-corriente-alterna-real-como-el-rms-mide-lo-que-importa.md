---
title: "Corriente alterna real: Cómo el RMS mide lo que importa"
pubDate: 2026-07-02
description: "Aprenderá la importancia de True RMS en multímetros para mediciones precisas de corriente alterna en sus proyectos, sin importar la forma de onda."
referenceUrl: "https://www.amazon.es/dp/B07G1LQJ2P"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Construyes un controlador de motor o reparas una fuente de alimentación, y al medir tensiones alternas, los valores parecen inconsistentes. Sospechas de un componente defectuoso, pero la lectura de tu multímetro no concuerda con lo esperado. Esto puede deberse a que la señal no es una onda sinusoidal pura, y tu herramienta no interpreta correctamente estas formas de onda.

El valor RMS (Root Mean Square) de una tensión o corriente alterna representa su 'valor efectivo', es decir, la cantidad de energía que disiparía en una carga resistiva, equivalente a una señal de corriente continua. Muchos multímetros económicos, al medir AC, asumen que la señal es una onda senoidal pura y calculan el RMS escalando su valor promedio. Esto es una estimación válida solo para señales AC de red eléctrica limpias. Sin embargo, en proyectos de electrónica maker, las señales rara vez son senoidales perfectas. Piense en las salidas de controladores de motor PWM, fuentes de alimentación conmutadas o circuitos rectificadores. En estos casos, la forma de onda es compleja y un cálculo simple no representa la energía real. La fórmula para el RMS es $V_{\text{RMS}} = \sqrt{\frac{1}{T} \int_{0}^{T} V(t)^2 dt}$. Esta ecuación calcula la raíz cuadrada del promedio de los cuadrados de los valores instantáneos de la señal a lo largo de un período. Al realizar esta operación, el multímetro True RMS mide con precisión la tensión efectiva real de cualquier forma de onda, proporcionando un dato energéticamente relevante sin suposiciones sobre su geometría.

El error común entre los makers es confiar en mediciones AC de multímetros que no son True RMS cuando se trabaja con circuitos de potencia no senoidales. Si estás diagnosticando un motor controlado por PWM, verificando una fuente conmutada o analizando cualquier circuito que modifique la forma de onda de la corriente alterna, las lecturas de un multímetro estándar serán inconsistentes con la realidad energética. Un valor que parezca plausible puede no serlo. Un multímetro True RMS es esencial para obtener una medida fidedigna de la energía eléctrica efectiva. Al seleccionar un multímetro para tu taller, la especificación 'True RMS' no es un extra, sino una característica fundamental que asegura la precisión en la comprensión del comportamiento de la potencia, más allá de la simple indicación de dígitos.

**Prueba rápida**
1.  Enciende un aparato con fuente de alimentación conmutada (un PC o televisor) y enchúfalo a la red.
2.  Con el multímetro configurado en V AC, mide la tensión en el enchufe de pared. Anota la lectura; esto debe ser una onda senoidal.
3.  Ahora, si tienes un variador de velocidad, un dimmer de luz conectado a una bombilla incandescente, o la salida de un transformador con carga no lineal, mide su tensión AC.
4.  El valor que te da tu Richmeters RM409B es la tensión efectiva real de esa onda, clave para entender su comportamiento energético independientemente de su forma.

El Richmeters RM409B incorpora la funcionalidad True RMS, esencial para cualquier maker que trabaje con electrónica moderna y fuentes de alimentación conmutadas. Su capacidad NCV (Non-Contact Voltage) añade un nivel práctico de seguridad, permitiendo detectar tensión sin contacto físico. Es una herramienta robusta que proporciona lecturas fiables, adecuada para el banco de trabajo doméstico.