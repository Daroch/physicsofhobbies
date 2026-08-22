---
title: "PWM y microcontroladores: la lógica detrás del Mega 2560"
pubDate: 2026-08-18
description: "Un microcontrolador no entiende de continuo ni de analógico real, pero puede engañar a un servo o un LED con pura velocidad de conmutación."
category: "electrónica"
image: "/images/blog/2026-08-18-pwm-y-microcontroladores-la-logica-detras-del-mega-2560.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B01MQPT9OD?tag=physicshobbie-21"
productName: "ELEGOO Conjunto Más Completo y Avanzado de Iniciación Mega"
---

Tienes una idea clara en la cabeza: un brazo robótico que se mueva, un sensor que encienda una luz, una alarma que reaccione al movimiento. El problema aparece cuando intentas traducir esa idea a algo físico y te das cuenta de que necesitas controlar decenas de señales eléctricas distintas, sincronizadas, sin que se pisen entre sí. Ahí es donde entra un microcontrolador como el Mega 2560: no resuelve la idea, pero te da las manos para construirla.

El Mega 2560 funciona con lógica binaria pura, ceros y unos, voltajes de 0V o 5V sin términos medios. El truco para simular un valor "intermedio", como la posición de un servomotor o el brillo de un LED, es el PWM (modulación por ancho de pulso). En lugar de mandar un voltaje constante, el microcontrolador enciende y apaga la señal miles de veces por segundo, variando el tiempo que está en alto respecto al periodo total. Ese porcentaje se llama ciclo de trabajo, $D = \frac{t_{on}}{T} \times 100\%$, y es lo que tu servo interpreta como un ángulo concreto o tu LED como un nivel de brillo.

Aquí la mayoría de principiantes comete el mismo error: alimentar servomotores o motores directamente desde los pines digitales de la placa. El Mega 2560 puede entregar un máximo razonable de corriente por pin (unos 20-40 mA), y un servo bajo carga puede pedir varias veces eso en el arranque. Si no usas una fuente externa o al menos un capacitor de desacoplo cerca del servo, vas a ver reinicios aleatorios de la placa justo cuando el motor hace fuerza. Separar la alimentación de lógica y la de potencia no es opcional, es la diferencia entre un proyecto que funciona y uno que se reinicia solo. Y antes de elegir los servos conviene mirar la otra mitad del problema: [cuánto torque necesita cada articulación de un brazo](/blog/2026-08-19-torque-en-cadena-la-fisica-que-mueve-tu-brazo-robotico/).

**Prueba rápida:**
1. Conecta un LED con resistencia de 220Ω a un pin PWM (marcado con ~).
2. Sube un sketch que varíe el valor de `analogWrite()` de 0 a 255 en un bucle con `delay(10)`.
3. Observa cómo el LED pasa de apagado a máximo brillo de forma progresiva, no a saltos.
4. Repite el experimento con un multímetro en modo voltaje DC sobre el pin: verás una lectura promedio, no un salto brusco, porque el multímetro está integrando la señal PWM en el tiempo.

Este kit de ELEGOO te da el hardware para hacer justo ese tipo de pruebas sin tener que resolver antes el problema de las herramientas: trae la placa Mega 2560 (con más pines PWM y memoria que un Uno, útil si tu proyecto crece), un servomotor, y una colección de sensores y módulos básicos con guías en español. Las guías son un punto a favor real para quien empieza, aunque no esperes explicaciones profundas de la electrónica interna: te dicen qué cable va dónde, no por qué funciona. La parte de la física y los límites de corriente, como en cualquier kit genérico, la tienes que entender tú aparte.