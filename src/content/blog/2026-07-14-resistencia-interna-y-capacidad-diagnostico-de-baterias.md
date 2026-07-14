---
title: "Resistencia interna y capacidad: Diagnóstico de baterías"
pubDate: 2026-07-14
description: "Comprenderá cómo medir la capacidad real de sus baterías y su resistencia interna para optimizar su rendimiento y vida útil en sus proyectos."
referenceUrl: "https://www.amazon.es/dp/B07XJR6J4Z"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Tienes un proyecto, quizás un dron o una herramienta portátil, y la batería no dura lo esperado. O peor, falla antes de tiempo en un momento crítico. A menudo, el problema no es la batería en sí, sino una lectura incorrecta de su estado real o un ciclo de vida agotado sin que seas consciente de ello.

Cuando una batería se descarga, libera energía eléctrica. Su capacidad se mide en amperios-hora (Ah) o miliamperios-hora (mAh), que es la cantidad total de carga que puede suministrar a una corriente determinada hasta un voltaje mínimo seguro. Esta capacidad no es un valor fijo, sino que depende de la corriente de descarga y de la temperatura de operación. Más importante aún es su resistencia interna equivalente (ESR), la oposición al flujo de corriente dentro de la propia batería. Se estima mediante la caída de voltaje que experimenta la batería bajo una carga conocida, siguiendo la Ley de Ohm: $\Delta V = I \times R_{interna}$. Una resistencia interna alta es un signo de deterioro. Significa que la batería disipa más energía como calor, su voltaje cae significativamente bajo carga, y su capacidad de entregar alta potencia a tu proyecto se reduce drásticamente. Entender este parámetro es crítico para la longevidad y el rendimiento.

La mayoría solo comprueba el voltaje de una batería con un multímetro. Sin embargo, su voltaje en vacío, sin carga, no revela su capacidad real ni su estado bajo condiciones de trabajo. Para una evaluación precisa, descarga la batería a una corriente constante y registra la energía entregada. El valor obtenido en mAh es su capacidad real, que puede ser inferior a la nominal, especialmente en baterías usadas o de menor calidad. Es crucial descargar la batería a una corriente representativa de tu aplicación final para obtener datos relevantes. Presta atención al incremento de la resistencia interna a medida que una batería envejece o sufre daños; es un indicador mucho más fiable de su salud que solo el voltaje. Una $R_{interna}$ elevada es una señal de advertencia, anticipando cuándo una batería ya no rendirá adecuadamente o incluso podría suponer un riesgo. Monitorear este valor te permite reemplazar celdas a tiempo y evitar fallos.

Prueba rápida:
1.  Conecta una batería Li-ion 18650 nueva al probador.
2.  Configura una descarga a 0.5A hasta 3.0V. Inicia la prueba y espera a que finalice.
3.  Anota la capacidad final (mAh) y la resistencia interna (mΩ) mostradas.
4.  Repite con una batería similar de uso intenso. Compara los valores: una batería sana mostrará mayor capacidad y menor resistencia interna.

El ZKETECH EBC-A20 permite realizar pruebas de descarga y carga para determinar la capacidad real de tus baterías, ideal para proyectos que exigen fiabilidad y conocer el estado exacto de cada celda. Su conectividad Bluetooth facilita el monitoreo y registro de datos en tiempo real, lo que es útil para analizar el comportamiento de la batería durante todo el ciclo de prueba, desde tu PC o móvil. Es una herramienta robusta para makers que necesitan caracterizar y emparejar celdas, o diagnosticar el estado de packs de baterías de todo tipo, desde LiPo hasta NiMH, mejorando la seguridad y eficiencia de sus diseños.