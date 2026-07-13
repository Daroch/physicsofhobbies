---
title: "Tiempo y Amplitud: Desentrañando Señales Eléctricas"
pubDate: 2026-07-13
description: "Descubre cómo un osciloscopio te permite ver y diagnosticar señales eléctricas, entendiendo su frecuencia, amplitud y comportamiento en tus proyectos."
referenceUrl: "https://www.amazon.es/dp/B07VGRJDFG"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Has montado un circuito, pero no funciona como esperas. El LED parpadea de forma errática, o la comunicación serie falla ocasionalmente sin razón aparente. Un multímetro solo te proporciona valores estáticos, sin mostrar qué ocurre realmente con el voltaje en el transcurso del tiempo.

Un osciloscopio digital convierte una señal eléctrica analógica en datos que puede mostrar en pantalla. Para ello, mide el voltaje en puntos discretos del tiempo, un proceso que llamamos muestreo. Para reconstruir una señal con fidelidad y sin distorsiones, la frecuencia de muestreo ($f_{muestra}$) debe ser al menos el doble de la frecuencia máxima ($f_{max}$) de la señal que se desea observar: $f_{muestra} \ge 2 f_{max}$. Esto es el teorema de muestreo de Nyquist-Shannon. Si se muestrea por debajo de este límite, el osciloscopio mostrará una versión alterada o 'alias' de la señal original, llevando a conclusiones erróneas sobre su comportamiento real. Comprender esto es clave para interpretar correctamente lo que se ve.

Cuando uses o compres un osciloscopio, no confundas su ancho de banda con la frecuencia máxima que puede mostrar. El ancho de banda (por ejemplo, 70MHz) indica hasta qué frecuencia puede medir el osciloscopio con una atenuación aceptable, típicamente del 30% (-3dB) de la amplitud real. Para señales digitales, un error común es subestimar el ancho de banda necesario. Una señal cuadrada de 10 MHz no es solo 10 MHz; contiene armónicos de mayor frecuencia esenciales para su forma. Para visualizar correctamente los flancos de subida y bajada de estas señales y analizar su integridad, el ancho de banda del osciloscopio debería ser, idealmente, de 3 a 5 veces la frecuencia fundamental de tu señal. Esto te permitirá ver sobreimpulsos o 'ringing' que un ancho de banda insuficiente ocultaría, afectando tus diagnósticos.

**Prueba rápida**
1.  Conecta la sonda del canal 1 al conector de calibración (CAL) de tu osciloscopio (normalmente 1kHz, 5V) y la pinza de masa a la masa.
2.  Ajusta la base de tiempo (horizontal) a 500 µs/división y la escala vertical a 1 V/división.
3.  Pulsa 'Auto' o ajusta manualmente el nivel de disparo (trigger) para estabilizar la imagen de la onda cuadrada en pantalla.
4.  Utiliza las funciones de medición (Measure) para verificar que la frecuencia es cercana a 1 kHz y el voltaje pico a pico es cercano a 5V, familiarizándote con la interfaz.

El Hantek DSO5072P ofrece 70 MHz de ancho de banda y 1 GSa/s de tasa de muestreo, lo que lo posiciona como una opción sólida para un maker avanzado. Sus dos canales permiten comparar señales simultáneamente, útil en proyectos de comunicaciones o control. Es adecuado para diagnosticar la mayoría de circuitos con microcontroladores, fuentes de alimentación conmutadas básicas y análisis de señales de audio o baja frecuencia RF.