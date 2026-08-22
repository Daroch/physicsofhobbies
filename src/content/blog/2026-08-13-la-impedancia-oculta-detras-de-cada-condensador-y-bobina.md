---
title: "La impedancia oculta detrás de cada condensador y bobina"
pubDate: 2026-08-13
description: "Un multímetro te dice si un condensador está muerto, pero no si sigue siendo bueno a la frecuencia en la que realmente trabaja."
category: "electrónica"
image: "/images/blog/2026-08-13-la-impedancia-oculta-detras-de-cada-condensador-y-bobina.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0FL7QG7MX?tag=physicshobbie-21"
productName: "FNIRSI LC1020E Medidor Digital LCR 100kHz"
---

Tienes un condensador electrolítico desmontado de una fuente que falló, y tu multímetro dice que mide los microfaradios correctos. Lo montas en el circuito nuevo y el aparato sigue sin funcionar bien. El problema es que un multímetro mide capacitancia con corriente continua o a una sola frecuencia fija, y eso no te dice nada sobre cómo se comporta ese componente cuando la corriente cambia de sentido miles o millones de veces por segundo, que es justo lo que le pasa en un circuito real.

Un condensador o una bobina no son componentes puramente ideales: tienen una resistencia parásita en serie (ESR, equivalent series resistance) que disipa energía como calor. La oposición total al paso de corriente alterna se llama impedancia, un número complejo $Z = R + jX$, donde $R$ es la parte resistiva y $X$ la reactancia (positiva si es inductiva, negativa si es capacitiva). De ahí se derivan dos indicadores clave: el factor de calidad $Q = X/R$, que te dice qué tan "limpio" es el componente, y el factor de disipación $D = 1/Q = \tan\theta$, que usan los fabricantes de condensadores para especificar pérdidas. Cuanto más bajo el $D$ (o más alto el $Q$), menos energía se pierde como calor.

La mayoría de gente que empieza con estos medidores comete un error simple: no calibra antes de medir. Un LCR-metro necesita anular la resistencia de sus propios cables y contactos (calibración de cortocircuito) y la capacitancia parásita del aire entre las puntas cuando no hay nada conectado (calibración de circuito abierto). Sin esos dos pasos, cualquier medición de componentes pequeños o de ESR bajo va a estar contaminada por el propio instrumento. También importa la frecuencia de test: un condensador electrolítico envejecido puede parecer normal a 100 Hz pero mostrar un ESR disparado a 100 kHz, que es la frecuencia real de conmutación en muchas fuentes.

**Prueba rápida:**
1. Calibra el equipo en abierto y en cortocircuito antes de nada.
2. Mide un condensador electrolítico nuevo y anota su ESR y su D.
3. Mide uno viejo de la misma capacitancia nominal, sacado de un aparato descartado.
4. Compara: si el ESR del viejo es varias veces mayor, ahí tienes la causa real de fallos intermitentes que un multímetro nunca detectaría.

El FNIRSI LC1020E hace exactamente esto: mide impedancia a 100 kHz fija, con detección automática del tipo de componente y pantalla dual que muestra a la vez el valor principal (capacitancia, inductancia o resistencia) y un secundario (ESR, Q, D o el ángulo de fase θ). Con 19999 cuentas de resolución te sirve para trabajo de banco serio, aunque su limitación real es que no permite elegir la frecuencia de test manualmente, algo que sí ofrecen LCR-metros de gama más alta y que resulta útil si necesitas caracterizar un componente en varios puntos del espectro. Para barrer esos puntos hace falta una fuente de señal con la frecuencia fijable con exactitud, que es justo lo que consigue [la síntesis digital directa](/blog/2026-08-14-dds-como-el-rigol-dg1022z-genera-senales-exactas-en-tu-banco/).