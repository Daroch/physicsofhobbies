---
title: "Lúmenes, candelas y lux: por qué la caja no dice cuánto alumbra"
pubDate: 2026-08-21
description: "Mil lúmenes pueden alumbrar a 18 metros o a 400. La diferencia no está en la potencia, sino en cómo se reparte esa luz por el espacio."
category: "óptica"
tags: ["ciencia", "hobbies", "divulgación", "óptica"]
---

Dos frontales anuncian 1.000 lúmenes. Una alumbra un sendero hasta unos 18 metros; la otra, hasta 400. Las dos dicen la verdad.

El problema no es que mientan: es que el lumen no mide lo que tú quieres saber. Mide cuánta luz sale en total, no cuánta llega a donde apuntas. Y son cosas distintas hasta por un factor de 500.

## Cuatro palabras que no son sinónimos

La fotometría separa tres magnitudes que el marketing mezcla a propósito:

- **Lumen (lm)** — el **flujo luminoso**: toda la luz que emite la fuente, sumada en todas las direcciones. Es un total.
- **Candela (cd)** — la **intensidad luminosa**: cuánta luz sale *por unidad de dirección*. Es una densidad.
- **Lux (lx)** — la **iluminancia**: cuánta luz llega *por metro cuadrado* a la superficie que estás mirando. Es lo que de verdad determina si ves.

La palabra que conecta las tres es la que nadie usa fuera de un laboratorio: el **estereorradián** (sr), que mide ángulo sólido. Igual que un radián mide una porción de circunferencia, un estereorradián mide una porción de esfera. La esfera completa son $4\pi \approx 12{,}57$ sr.

Con eso, las definiciones se vuelven aritmética:

$$
1\ \text{cd} = \frac{1\ \text{lm}}{1\ \text{sr}}
\qquad\qquad
1\ \text{lx} = \frac{1\ \text{lm}}{1\ \text{m}^2}
$$

Los lúmenes son el presupuesto. Las candelas dicen en qué lo gastas.

## La misma luz, repartida de dos formas

Coge esos 1.000 lúmenes y espárcelos por igual en todas las direcciones, como una vela desnuda:

$$
I = \frac{1000\ \text{lm}}{4\pi\ \text{sr}} = 79{,}6\ \text{cd}
$$

Ahora concéntralos con un reflector en un cono estrecho de 10°. El ángulo sólido de un cono de semiángulo $\theta$ es $\Omega = 2\pi(1 - \cos\theta)$, así que para 10° completos:

$$
\Omega = 2\pi\,(1 - \cos 5^\circ) = 0{,}0239\ \text{sr}
$$

$$
I = \frac{1000\ \text{lm}}{0{,}0239\ \text{sr}} = 41.800\ \text{cd}
$$

**Los mismos 1.000 lúmenes dan 79,6 candelas o 41.800 candelas** —un factor de 525— según cómo los repartas. Ningún fabricante ha mentido en ninguno de los dos casos. Simplemente uno ha puesto una óptica y el otro no.

Esto es lo que hace que la cifra de la caja sea incomparable entre modelos: no distingue un haz que ilumina toda la habitación de uno que dibuja un círculo a cien metros.

## De candelas a metros

La iluminancia que recibe una superficie a distancia $d$ cae con el cuadrado de esa distancia, porque la misma luz se reparte sobre un área que crece como $d^2$:

$$
E = \frac{I}{d^2}
$$

La norma **ANSI/PLATO FL1**, que es el estándar de la industria de las linternas, define el **alcance** como la distancia a la que la iluminancia baja a **0,25 lux** — aproximadamente la claridad de una noche de luna llena. Despejando:

$$
d = \sqrt{\frac{I}{0{,}25}} = 2\sqrt{I}
$$

Aplicado a los dos casos de antes:

| Reparto | Intensidad | Alcance FL1 |
|---|---|---|
| Esférico (sin óptica) | 79,6 cd | 18 m |
| Cono de 10° | 41.800 cd | 409 m |

Ahí están los 18 metros y los 400 del principio, y salen de una sola cuenta a partir de un dato que casi ninguna ficha publica.

Conviene saber además qué significa ese umbral: 0,25 lux es **distinguir una silueta**, no ver con comodidad. Como la iluminancia crece al cuadrado según te acercas, a la mitad del alcance declarado tienes cuatro veces más luz. Una regla honesta es tratar el alcance FL1 como el límite de «ahí hay algo» y la mitad como el de «veo lo que hay».

## El número de la caja mide otra cosa, y encima en otro momento

Hay una segunda letra pequeña. La norma FL1 mide los lúmenes **a los 30 segundos** de encender, y no por capricho: un LED potente en un cuerpo pequeño se calienta en cuanto arranca, y el control térmico baja la corriente para no quemarlo. Ese escalón —el *step-down*— es física de disipación, no un defecto.

Así que una frontal puede dar sus lúmenes de portada durante un minuto y estabilizarse bastante por debajo el resto de la noche. Cuando una ficha anuncia el pico y calla el valor sostenido, la cifra describe el primer minuto de una batería llena.

De ahí que las cifras enormes deban leerse con la aritmética anterior en la mano: **18.000 lúmenes en un aparato de bolsillo** implican una potencia eléctrica y una superficie de disipación que ese tamaño no sostiene más que unos segundos, si es que los alcanza.

## Qué pedirle a una ficha

La FL1 no es obligatoria, pero define seis datos, y ahí está su utilidad como filtro: **una ficha que solo publica lúmenes no está siguiendo la norma**, y esa ausencia ya te dice algo.

- **Lúmenes**, medidos a 30 segundos, y a ser posible también el valor sostenido.
- **Candelas o alcance en metros**, que es el par que decide si ves lejos.
- **Autonomía** por modo, hasta que la luz cae al 10 % del valor inicial.
- **Resistencia al agua** con código IP concreto, no la palabra «impermeable».
- Resistencia a impactos, en metros de caída.

Y una decisión que no es de calidad sino de uso: **haz ancho o haz concentrado**. Para correr por un sendero quieres un cono amplio a pocos metros; para localizar algo lejos, lo contrario. Los lúmenes por sí solos no distinguen los dos casos, y por eso comprar por esa cifra es elegir a ciegas entre dos herramientas distintas.

Si quieres ver esto aplicado a fichas reales, en [lúmenes declarados vs reales](/blog/2026-08-20-lumenes-declarados-vs-reales-que-mirar-en-una-frontal/) comparo cinco frontales — y el hallazgo es que ninguna de las cinco declara candelas ni alcance.

## En casa pasa lo mismo

Esto no va solo de linternas. Una bombilla de 800 lm que reparte luz en todas direcciones da unas 64 cd, y sobre una mesa a 2 metros deja:

$$
E = \frac{64}{2^2} = 16\ \text{lux}
$$

Un foco dicroico de **400 lm** —la mitad de luz— con un haz de 36° concentra unas 1.300 cd, y sobre esa misma mesa:

$$
E = \frac{1300}{2^2} = 325\ \text{lux}
$$

**Veinte veces más luz sobre la mesa con la mitad de lúmenes.** Por eso comparar bombillas por lúmenes funciona solo mientras compares bombillas del mismo tipo de haz, y por eso una habitación puede quedarse oscura con la etiqueta llena de cifras grandes.

Es el mismo patrón que en [aumentos vacíos](/blog/2026-08-21-aumentos-vacios-por-que-525x-en-un-telescopio-de-60-mm-es-imposible/): el número que el fabricante escoge para la portada es el que puede hacer crecer sin coste —aumentos con un ocular más corto, lúmenes con un LED más grande— mientras el dato que decide el resultado, la apertura o las candelas, se queda fuera de la caja.
