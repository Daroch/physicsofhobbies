---
title: "Registrar ruido en el tiempo: del decibelio al voltaje CC"
pubDate: 2026-10-11
description: "Medir un pico de ruido no te dice nada sobre cómo vive ese ruido tu oído durante ocho horas de trabajo."
category: "acústica"
image: "/images/blog/2026-10-11-registrar-ruido-en-el-tiempo-del-decibelio-al-voltaje-cc.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0DJT42M9K?tag=physicshobbie-21"
productName: "Medidor de decibelios"
---

Imagina que te quejan del ruido de una máquina en el taller, o que necesitas justificar ante un cliente que el nivel sonoro de tu obra cumple la normativa en horario laboral. Un sonómetro básico te da un número en el momento en que lo miras, pero ese número cambia cada segundo: el compresor arranca, el torno acelera, alguien grita. Lo que necesitas no es una foto, sino una película: una serie de datos que muestre cómo evoluciona el ruido durante minutos, horas o un turno entero.

Aquí entra una distinción que mucha gente pasa por alto: el nivel de presión sonora en decibelios es una magnitud logarítmica, $L_p = 20 \log_{10}(p/p_0)$, donde $p_0$ es la referencia de 20 µPa. Para convertir ese valor en algo que un datalogger externo, un osciloscopio o un PLC puedan leer directamente, el equipo genera una salida de corriente continua (CC) proporcional al nivel en dB, normalmente a razón de unos milivoltios por decibelio. Esa linealización es lo que permite registrar la variable en el tiempo sin que tengas que estar tú delante leyendo la pantalla: el aparato muestrea a intervalos fijos (por ejemplo, una lectura por segundo) y guarda cada valor como un punto de una serie temporal. Con 43.000 puntos de memoria, a una muestra por segundo, tienes margen para casi doce horas continuas de registro antes de necesitar volcar los datos.

El error típico al usar este tipo de equipo es fijarse solo en el valor máximo (Lmax) y olvidar que lo que suele importar legal y prácticamente es el nivel equivalente continuo (Leq), un promedio energético del ruido a lo largo del periodo. Antes de lanzar un registro largo, decide qué intervalo de muestreo tiene sentido para el fenómeno que mides: un segundo es razonable para maquinaria con ciclos cortos, pero si quieres caracterizar el ruido ambiental de una calle durante todo el día, puedes permitirte muestras cada 10 o 30 segundos y así estirar la memoria disponible sin perder la forma general de la curva.

**Prueba rápida:**
1. Configura el equipo en ponderación A (la que se aproxima a la sensibilidad del oído humano) y en modo registro con intervalo de 1 segundo.
2. Déjalo grabando 5 minutos en una habitación con un electrodoméstico que se encienda y apague (nevera, extractor).
3. Exporta los datos a tu ordenador y represéntalos en una hoja de cálculo.
4. Compara el valor máximo puntual con el promedio de toda la serie: la diferencia te dirá cuánto se dispara el ruido respecto a lo que realmente te rodea de fondo.

Este modelo concreto no es solo un medidor instantáneo: guarda hasta 43.000 conjuntos de datos, permite exportarlos para analizarlos después y ofrece esa salida CC que lo convierte en un sensor que puedes integrar en un sistema de monitorización más amplio. Es recargable, lo que facilita dejarlo registrando sin depender de pilas, aunque como cualquier sonómetro de este rango de precio, su precisión de calibración de fábrica no sustituye a un certificado de laboratorio si necesitas datos con validez legal.

---

**¿Comparando modelos?** En [Mejor medidor de decibelios: 5 sonómetros comparados por ficha](/blog/2026-08-16-que-dato-de-la-ficha-decide-que-sonometro-comprar/) analizo varias fichas de este tipo de producto y qué dato de la ficha decide la compra.
