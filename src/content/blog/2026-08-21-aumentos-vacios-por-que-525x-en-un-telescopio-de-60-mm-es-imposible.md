---
title: "Aumentos vacíos: por qué 525x en un telescopio de 60 mm es imposible"
pubDate: 2026-08-21
description: "El aumento no lo pone el telescopio, lo pone el ocular que le enchufes. Lo que no puedes ampliar es la información que entra por la apertura."
category: "óptica"
tags: ["ciencia", "hobbies", "divulgación", "óptica"]
---

En la caja de un telescopio de iniciación, el número más grande casi siempre es el de los aumentos. «525x». Es también el único dato de la caja que no te dice absolutamente nada del instrumento.

No porque sea mentira —ese telescopio alcanza 525 aumentos si le pones los oculares adecuados— sino porque **el aumento no es una propiedad del telescopio**. Es una propiedad del par que formas al elegir un ocular, y puedes hacerlo tan grande como quieras.

## El aumento lo eliges tú, no el fabricante

El aumento sale de dividir dos distancias focales: la del objetivo, que es fija, entre la del ocular, que cambias metiendo la mano en la caja.

$$
M = \frac{F_{\text{objetivo}}}{f_{\text{ocular}}}
$$

Un tubo de 700 mm de focal con un ocular de 4 mm da 175 aumentos. Si además le enroscas una lente de Barlow que triplica, llegas a 525. De ahí sale el número de la caja, y de ahí sale que sea irrelevante: **con un ocular suficientemente corto, cualquier telescopio anuncia cualquier cifra**. Anunciar los aumentos es como vender un coche por la cifra más alta del velocímetro.

Lo que no puedes elegir es cuánta información entra en el tubo. Eso lo fija la apertura.

## La difracción pone el techo

La luz que atraviesa una abertura circular no converge en un punto, sino en un pequeño disco rodeado de anillos: el disco de Airy. Su radio angular depende de la longitud de onda y del diámetro de la abertura:

$$
\theta \approx 1{,}22 \frac{\lambda}{D}
$$

Pasado a segundos de arco y tomando luz verde ($\lambda \approx 550$ nm), que es donde el ojo es más sensible, queda una regla cómoda —el criterio de Rayleigh:

$$
\theta_{\text{arcsec}} \approx \frac{138}{D_{\text{mm}}}
$$

Para nuestro tubo de **60 mm de apertura**, eso son **2,3 segundos de arco**. Dos estrellas más juntas que eso llegan al ocular como una sola mancha, y ningún ocular del mundo las separa después. La información ya se perdió al entrar.

Ahí está la asimetría que explica todo el artículo: **el aumento es gratis y la resolución no**. Ampliar es fácil; capturar detalle exige diámetro.

## Cuánto se puede ampliar antes de que se acabe la información

Ampliar sí sirve, hasta un punto: el detalle que el telescopio *sí* ha capturado llega al ojo con un tamaño angular diminuto, y hay que agrandarlo para verlo. El ojo humano resuelve alrededor de 1 minuto de arco (60 segundos) en buenas condiciones, y necesita bastante más holgura cuando la imagen es tenue.

De ahí sale la regla clásica del **aumento máximo útil ≈ 2 × la apertura en milímetros**: 120 aumentos para nuestros 60 mm. Comprobemos qué margen deja, porque el cálculo es revelador:

$$
2{,}3'' \times 120 = 276'' \approx 4{,}6'
$$

O sea que a 120 aumentos el detalle más fino que el instrumento puede formar llega al ojo con casi 5 minutos de arco, unas cinco veces su límite. Ese margen generoso no es un lujo: a bajo brillo el ojo pierde agudeza, y por eso la regla es 2× y no 1×.

Pasado ese punto, cada aumento adicional agranda el disco de difracción exactamente igual que agranda el planeta. La proporción entre ambos no cambia nunca. Eso es un **aumento vacío**: más grande, misma información.

## Qué ocurre de verdad a 525 aumentos

Tres formas de ver el mismo desastre, todas con los números de arriba:

**El detalle se convierte en una mancha.** Ese disco de Airy de 2,3 segundos, ampliado 525 veces, ocupa 1.207 segundos de arco: **20 minutos**. Una estrella, que es un punto, se te presenta con dos tercios del tamaño aparente de la Luna llena.

**La imagen se queda a oscuras.** El haz que sale del ocular tiene un diámetro —la pupila de salida— que es la apertura dividida entre el aumento:

$$
P = \frac{D}{M}
$$

A 120 aumentos son 0,5 mm, ya justos. A 525 aumentos son **0,11 mm**: un hilo de luz más fino que las propias imperfecciones del ojo, que a ese tamaño empiezan a proyectarse sobre la imagen como sombras flotantes.

**El brillo por superficie se hunde.** Repartes la misma luz sobre una imagen cuya área aparente crece con el cuadrado del aumento. Entre 120x y 525x el factor es $(525/120)^2 \approx 19$: cada trocito de imagen llega **diecinueve veces más apagado**. Y el ojo, cuanto menos luz recibe, peor resuelve — lo que empeora el problema que el aumento pretendía resolver.

## Y encima está la atmósfera

Todo lo anterior supone una óptica perfecta mirando a través del vacío. En el suelo hay unos kilómetros de aire en movimiento, y ese *seeing* emborrona la imagen entre 1 y 4 segundos de arco según la noche.

Para el tubo de 60 mm, cuyo límite propio es 2,3 segundos, la difracción manda casi siempre. Pero en cuanto subes de apertura la cosa se invierte: un tubo de 200 mm tiene un límite teórico de 0,7 segundos que la atmósfera rara vez le deja aprovechar. Por eso los aumentos altísimos son inútiles **también** en instrumentos caros, y por eso vale más una noche estable que un ocular más corto.

## En prismáticos es la misma trampa con otro disfraz

Los prismáticos declaran el aumento en el propio nombre —10x50 son 10 aumentos y 50 mm de apertura— así que la pupila de salida sale de una división mental: 50/10 = **5 mm**, muy cerca de lo que abre la pupila humana adaptada a la oscuridad. Por eso ese formato es un clásico.

Ahora mira unos «zoom 10-30x60». En el extremo de 30 aumentos la pupila de salida cae a 2 mm y el campo de visión se estrecha, justo cuando el anuncio sugiere que estás sacando más partido. Y hay un límite todavía más terco: el aumento amplifica también el temblor de tus manos. Por encima de unos 10 o 12 aumentos a pulso, la imagen baila lo suficiente como para que el detalle extra no llegue a tu retina de forma utilizable. Necesitas trípode, y entonces el prismático deja de ser un prismático de mano.

## Qué mirar en la ficha

Cuando el número gordo de un anuncio se puede cambiar enroscando otra pieza, ese número describe el accesorio, no el aparato. Es el mismo patrón que las cámaras térmicas que anuncian una resolución mayor que la de su sensor: en [termómetro infrarrojo o cámara térmica](/blog/2026-08-17-termometro-infrarrojo-o-camara-termica-que-mide-cada-uno/) esa cifra inflada se llama interpolación y el mecanismo es idéntico —píxeles calculados, no medidos; aumentos aplicados, no capturados.

Así que la lista corta:

- **La apertura** ($D$), que fija el detalle máximo por $138/D$ y también cuánta luz recoges. Es el único número que no se puede compensar después con accesorios.
- **La distancia focal** del objetivo, que con tus oculares te dice qué aumentos vas a usar de verdad — que serán bastantes menos que el de la caja.
- **La pupila de salida** que te queda, $D/M$: por debajo de medio milímetro estás ampliando el vacío.
- En prismáticos, **el par aumento-apertura** y si vas a poder sostenerlos.

Y una regla que resume el artículo entero: si el aumento máximo anunciado supera el doble de la apertura en milímetros, lo que estás leyendo no es una especificación óptica. Es el catálogo de oculares que vienen en la caja.

Si lo tuyo son los prismáticos, en [qué pupila de salida necesitas](/blog/2026-08-20-que-pupila-de-salida-necesitas-segun-cuando-uses-los-prismaticos/) aplico esta misma cuenta a cinco modelos reales, con el resultado incómodo de que tres de ellos son indistinguibles según sus fichas.
