---
title: "Ley de Ohm: Diagnóstico eléctrico con tu multímetro"
pubDate: 2026-07-10
description: "Comprenderás cómo un multímetro mide las propiedades eléctricas fundamentales y cómo usarlo para identificar fallos en tus circuitos maker."
referenceUrl: "https://www.amazon.es/dp/B098YR7R58"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Cuando un circuito electrónico deja de funcionar inesperadamente o un componente no responde como debería, la causa no siempre es visible. Una soldadura fría, un cable roto o una resistencia con un valor incorrecto pueden paralizar tu proyecto. Necesitas herramientas que te permitan "ver" lo que ocurre eléctricamente.

Un multímetro funciona midiendo las propiedades fundamentales de la electricidad: voltaje, corriente y resistencia. El voltaje (V) es la diferencia de potencial eléctrico entre dos puntos, la "presión" que empuja los electrones. La corriente (I) es el flujo de esos electrones a través de un conductor. La resistencia (R) es la oposición de un material al paso de la corriente. La relación entre estas tres magnitudes es descrita por la Ley de Ohm: $V = I \cdot R$.

Para medir voltaje, el multímetro se conecta en paralelo con el componente o la fuente, es decir, a ambos lados, para detectar esa diferencia de potencial. Para la corriente, se intercala en serie en el camino de los electrones, interrumpiendo el circuito para que toda la corriente pase a través del instrumento. Para la resistencia, el multímetro aplica una pequeña corriente conocida y mide la caída de voltaje resultante, calculando R mediante la Ley de Ohm.

El error más común es intentar medir corriente conectando el multímetro en paralelo, lo que puede causar un cortocircuito y dañar el aparato o la fuente de alimentación. Siempre conecta el multímetro en serie para medir corriente y en paralelo para medir voltaje. Al medir resistencia, asegúrate de que el componente esté desenergizado, sin corriente circulando. Para mediciones de voltaje o corriente desconocidas, selecciona siempre el rango más alto disponible y redúcelo gradualmente; esto protege el instrumento. Este multímetro es de auto-rango, lo que simplifica esta parte, pero entender el principio sigue siendo útil.

[Prueba rápida]
1.  **Medir voltaje de una pila:** Gira el selector a "V-" (voltaje DC), conecta el cable rojo al terminal positivo de una pila AA y el negro al negativo. Lee el valor. Debería ser alrededor de 1.5V.
2.  **Verificar continuidad de un cable:** Gira el selector a la posición de continuidad (símbolo de diodo/onda). Toca las puntas de prueba entre los dos extremos de un cable. Si suena un pitido y el valor es bajo (cercano a cero), el cable está bien.
3.  **Medir resistencia de un componente:** Con el selector en Ohmios ($\Omega$), toca las puntas de prueba a los extremos de una resistencia. El valor mostrado es su resistencia. Asegúrate de que no esté conectada a una fuente de energía.

[El producto]
El multímetro UNI-T UT131B es una herramienta compacta y sencilla, adecuada para iniciarse en la electrónica. Ofrece mediciones básicas de voltaje DC y AC, corriente DC, resistencia, continuidad y prueba de diodos. Su función de auto-rango facilita su uso para quienes no están familiarizados con la selección manual de escalas, minimizando errores. Es una opción práctica para diagnosticar problemas en proyectos maker o verificar componentes básicos. Ten en cuenta que solo mide corriente DC, no AC.