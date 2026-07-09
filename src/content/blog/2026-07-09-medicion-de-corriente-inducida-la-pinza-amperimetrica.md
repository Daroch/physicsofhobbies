---
title: "Medición de Corriente Inducida: La Pinza Amperimétrica"
pubDate: 2026-07-09
description: "Aprenderás cómo la inducción magnética y el efecto Hall permiten medir corriente eléctrica sin contacto y cuándo usar una pinza amperimétrica."
referenceUrl: "https://www.amazon.es/dp/B07K2LB91V"
category: "electrónica"
image: "/images/default-physics.png"
tags: ["ciencia", "hobbies", "divulgación"]
---

Estás construyendo un controlador para tu CNC o una estación de carga personalizada, y sospechas que la fuente de alimentación no entrega la corriente esperada, o un motor no rinde y buscas consumos anómalos. La forma tradicional de verificar el amperaje implica cortar el circuito e insertar un amperímetro en serie. Este proceso es tedioso, consume tiempo y, en ocasiones, puede ser peligroso o impráctico si no quieres interrumpir el funcionamiento.

La corriente eléctrica que fluye por un conductor genera un campo magnético a su alrededor. Este fenómeno, descrito por la Ley de Ampère, es el pilar de las pinzas amperimétricas. Para medir corriente alterna (AC), la pinza como la UT210E utiliza una bobina interna que detecta la variación del campo magnético inducido por la corriente alterna. La magnitud de la tensión inducida en esta bobina es proporcional a la tasa de cambio del campo magnético y, por tanto, a la corriente que fluye. Para la corriente continua (DC), donde el campo magnético es constante, la pinza incorpora un sensor de efecto Hall. Este sensor produce un voltaje directamente proporcional a la intensidad del campo magnético constante, permitiendo así la lectura de DC sin interrupciones en el circuito.

El error más común al usar una pinza amperimétrica es intentar medir un cable que contiene tanto el conductor de fase como el neutro (o positivo y negativo en DC) juntos. En este caso, los campos magnéticos generados por las corrientes en direcciones opuestas se cancelan mutuamente, resultando en una lectura incorrecta o nula. Es imprescindible abrazar un único conductor. Otro aspecto crítico es la función 'True RMS'. Muchos dispositivos electrónicos, como fuentes de alimentación conmutadas, variadores de frecuencia o motores, no consumen corriente de forma sinusoidal perfecta. Una pinza que no sea True RMS mediría incorrectamente la corriente eficaz real, la que produce el calentamiento y es clave para el rendimiento y la seguridad. La UT210E, al ser True RMS, te proporciona el valor de corriente real, independientemente de la distorsión de la forma de onda, algo vital para el diagnóstico preciso en proyectos maker.

Prueba rápida:
1.  Enciende la pinza y selecciona el modo de medición de corriente (AC o DC) adecuado.
2.  Identifica un único conductor que alimenta la carga que deseas medir (por ejemplo, el cable de fase de un electrodoméstico o el positivo de una batería).
3.  Abre las mordazas de la pinza y rodea completamente ese único conductor.
4.  Lee el valor de corriente en la pantalla.

La UNI-T UT210E es una pinza amperimétrica compacta que ofrece mediciones True RMS tanto para corriente alterna como continua hasta 100 amperios. Su tamaño facilita el acceso en cuadros eléctricos o circuitos con espacio limitado, algo común en talleres maker. Es una herramienta adecuada para diagnosticar problemas de consumo o verificar el funcionamiento de componentes en impresoras 3D, fuentes de alimentación de CNC o sistemas de iluminación personalizados.