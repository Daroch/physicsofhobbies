---
title: "Radiación ionizante: mide su presencia y dosis"
pubDate: 2026-08-05
description: "Cómo un tubo Geiger-Müller convierte una partícula en un clic, por qué los CPM y los µSv/h no miden lo mismo y qué mirar antes de fiarte de la lectura."
category: "electrónica"
image: "/images/blog/2026-08-05-radiacion-ionizante-mide-su-presencia-y-dosis.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0B541D433?tag=physicshobbie-21"
productName: "GQ GMC-300S Contador Geiger"
---

Cuando trabajas con materiales antiguos, restauras un objeto vintage o simplemente tienes curiosidad por los niveles de energía que te rodean, es posible que te preguntes si hay radiación. Algunos componentes electrónicos viejos, esmaltes cerámicos o incluso ciertas rocas pueden emitir partículas ionizantes. Saber si un material es radiactivo y en qué medida es clave para operar con seguridad.

El corazón de un contador Geiger es el tubo Geiger-Müller (GM). Este tubo, sellado y lleno de un gas inerte a baja presión, contiene dos electrodos: un cátodo cilíndrico y un ánodo de hilo fino en el centro. Cuando la radiación ionizante (partículas alfa, beta o fotones gamma y X) atraviesa el tubo, choca con los átomos del gas, arrancando electrones de sus órbitas y creando iones. Estos electrones y iones se aceleran por el alto voltaje aplicado entre los electrodos. Los electrones ganan suficiente energía para ionizar a su vez otros átomos de gas, generando una "avalancha" de electrones y iones. Esta avalancha produce un pulso de corriente eléctrico detectable. El dispositivo cuenta estos pulsos. La tasa de pulsos, a menudo expresada en Cuentas Por Minuto (CPM), indica la intensidad de la radiación. Para entender el impacto biológico, los contadores Geiger modernos convierten estos pulsos a una tasa de dosis equivalente, comúnmente en microsieverts por hora ($\mu Sv/h$). Esta conversión no es trivial; depende de la energía y el tipo de radiación, así como de la calibración del detector.

Un error común es equiparar directamente el número de "clics" (CPM) con el riesgo de exposición. Aunque una mayor tasa de CPM indica más actividad radiactiva, el verdadero indicador de riesgo biológico es la tasa de dosis, medida en unidades como $\mu Sv/h$. Un buen dispositivo te mostrará ambas o permitirá la conversión. Recuerda la ley del inverso del cuadrado para fuentes puntuales: $I \propto 1/r^2$. Esto significa que la intensidad de la radiación (I) disminuye drásticamente con el cuadrado de la distancia (r) a la fuente. Mantener una distancia de seguridad es crucial. Además, siempre mide primero la radiación de fondo en tu entorno. Cualquier lectura significativamente por encima de este valor de referencia indica una fuente. La sensibilidad del tubo GM a diferentes tipos de radiación también varía: la mayoría detectan beta y gamma, pero para alfa se necesita una ventana especial muy fina, a menudo de mica. Asegúrate de que tu detector cubra el tipo de radiación que te interesa. Y conviene no confundir esto con lo que ocurre en el otro extremo del espectro electromagnético: [la radiación infrarroja no ioniza nada](/blog/2026-08-11-radiacion-infrarroja-la-fisica-de-ver-el-calor-que-se-escapa/), solo transporta calor.

Prueba rápida:
1.  Enciende el detector y déjalo estabilizar durante un minuto para obtener una lectura base de la radiación ambiental (fondo). Anota el valor en las unidades que muestre tu aparato, sean CPM o µSv/h.
2.  Toma una muestra de sal de potasio (sustituto de sal común) y colócala a 1-2 cm del sensor del dispositivo.
3.  Observa las lecturas. Deberías notar un aumento en los valores de µSv/h y/o CPM debido al isótopo radiactivo potasio-40.
4.  Retira la sal y confirma que las lecturas vuelven al nivel de fondo.

El GQ GMC-300S se anuncia como detector digital y dosímetro, con 1252 reseñas y 4.6 de valoración a 89€. Conviene saber qué es lo que su ficha **no** dice, porque es justo lo que este artículo explica que importa: no declara en qué unidades muestra la lectura, ni el tipo de tubo, ni contra qué isótopo está calibrada la conversión a µSv/h. Es incluso el único de su grupo cuyo título no enumera qué tipos de radiación detecta. Nada de eso lo descarta, pero son preguntas para el vendedor antes de pagar, no después.

Si estás comparando modelos, en [mejor contador Geiger: CPM, µSv/h y qué mide cada ficha](/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos/) contrasto siete fichas de este grupo y señalo cuál es la única que dice en qué unidades mide.