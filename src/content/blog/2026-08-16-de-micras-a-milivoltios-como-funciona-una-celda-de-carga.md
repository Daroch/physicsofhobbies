---
title: "De micras a milivoltios: cómo funciona una celda de carga"
pubDate: 2026-08-16
description: "Una celda de carga se deforma unas micras y devuelve unos milivoltios. Entender esa cadena explica por qué el ±0,1% del fabricante no significa lo que crees."
category: "electrónica"
tags: ["ciencia", "hobbies", "divulgación", "metrología"]
---

Una balanza de laboratorio que resuelve 0,01 g y una báscula colgante que aguanta 300 kg no se parecen en nada por fuera. Por dentro llevan el mismo componente: una pieza metálica que se deforma bajo carga con cuatro galgas extensométricas pegadas a su superficie. Toda la diferencia entre ambas está en la rigidez de esa pieza y en la electrónica que lee la señal.

Merece la pena entender esa cadena completa, porque es la que decide qué número de la ficha te importa cuando vas a comprar. Y sobre todo, porque explica una trampa en la que cae casi todo el mundo al leer la precisión anunciada.

## Por qué la resistencia cambia al deformarse

Una galga es una tira metálica en zigzag pegada sobre la pieza que se deforma. La resistencia de cualquier conductor vale:

$$
R = \rho \frac{L}{A}
$$

Al estirarse, pasan tres cosas a la vez. La longitud $L$ aumenta. La sección $A$ disminuye, porque el material se estrecha al alargarse (efecto Poisson). Y la resistividad $\rho$ del metal cambia ligeramente por sí misma, que es el efecto piezorresistivo. Las tres empujan la resistencia en el mismo sentido, hacia arriba.

Si haces las cuentas con esos tres términos, la relación entre el cambio relativo de resistencia y la deformación queda:

$$
\frac{\Delta R}{R} = GF \cdot \varepsilon
$$

donde $\varepsilon = \Delta L / L$ es la deformación y $GF$ es el **factor de galga**. Para una galga metálica sale un número muy concreto: la parte geométrica aporta $1 + 2\nu \approx 1{,}6$ con un coeficiente de Poisson típico de $0{,}3$, y el término piezorresistivo añade alrededor de $0{,}4$. Total: **$GF \approx 2$**. Casi todas las galgas metálicas del mercado están entre 2,0 y 2,1, y no es casualidad — es física del material, no una decisión de diseño.

## El problema: la señal es diminuta

Una celda de carga bien diseñada trabaja a unas 1000 micro-deformaciones a fondo de escala, es decir $\varepsilon = 0{,}001$. Un 0,1% de deformación. Eso, en una pieza de acero de unos centímetros, son literalmente micras.

Con $GF = 2$, el cambio de resistencia es:

$$
\frac{\Delta R}{R} = 2 \times 0{,}001 = 0{,}002 = 0{,}2\%
$$

En una galga estándar de 350 Ω, eso son **0,7 Ω sobre 350 Ω**. Ahí está el problema real: medir 350,7 Ω frente a 350,0 Ω con un óhmetro exige una precisión absurda, y basta que la temperatura de la habitación suba un par de grados para que la propia galga cambie más que la señal que buscas.

## Por qué el puente de Wheatstone, y por qué cuatro galgas

El puente de Wheatstone resuelve exactamente eso: en lugar de medir la resistencia, mide la **diferencia** entre dos ramas. El pedestal de 350 Ω se cancela y solo queda lo que cambia, que es lo único que quieres amplificar.

Con las cuatro galgas activas —dos en tracción y dos en compresión, en caras opuestas de la pieza que flexa— la salida del puente es:

$$
\frac{V_{salida}}{V_{excitación}} = GF \cdot \varepsilon = 0{,}002 = 2\ \text{mV/V}
$$

Abre la ficha de cualquier celda de carga comercial y encontrarás justo ese número: **2 mV/V**. No es una convención arbitraria, es lo que sale de multiplicar el factor de galga por la deformación de diseño. Con 5 V de excitación, tu señal a fondo de escala es de 10 mV. Diez milivoltios para representar 300 kg.

Pero la razón de fondo para usar cuatro galgas no es la sensibilidad, es la temperatura. Si el conjunto se calienta, las cuatro resistencias suben a la vez y el puente sigue equilibrado: el efecto se cancela solo. Un puente completo es intrínsecamente compensado en temperatura, y eso importa mucho más que el factor 4 de ganancia.

De ahí la señal pasa a un amplificador de instrumentación y a un convertidor de alta resolución. En el mundo maker el habitual es el HX711, con 24 bits y ganancia interna de 128 justamente porque el fabricante sabe que la señal que va a llegarle son milivoltios.

## La trampa: «% del fondo de escala» no es «% de la lectura»

Aquí está lo que de verdad cambia una decisión de compra, y donde casi todas las fichas se aprovechan de la confusión.

Cuando un fabricante anuncia una precisión de **±0,1% FS** (*full scale*, fondo de escala), el error es una cantidad **absoluta y fija**, calculada sobre el máximo del aparato. No crece ni decrece con lo que pongas encima.

En una báscula de 300 kg, ese ±0,1% son **±300 g siempre**, midas lo que midas:

| Lo que pesas | Error absoluto | Error sobre tu lectura |
|---|---|---|
| 5 kg | ±300 g | **±6,0 %** |
| 20 kg | ±300 g | ±1,5 % |
| 80 kg | ±300 g | ±0,38 % |
| 250 kg | ±300 g | ±0,12 % |

La conclusión es incómoda pero clara: **un instrumento sobredimensionado mide mal**. Comprar una báscula de 300 kg «por si acaso» para pesar habitualmente 5 o 10 kg no es prudencia, es tirar la precisión a la basura. La regla práctica es trabajar en el tercio superior del rango siempre que puedas.

Y hay un segundo malentendido que conviene separar: **resolución no es precisión**. Una balanza de 5000 g que muestra 0,01 g tiene una resolución de 1 entre 500.000, un número impresionante. Pero eso solo dice cuántos decimales es capaz de mostrar, no cuánto se aproximan al valor real. La linealidad, la histéresis y la deriva térmica son errores independientes que la pantalla no te enseña. Un instrumento puede darte tres decimales estables y equivocados.

## Los errores que no salen en la ficha

Aunque la cadena sea perfecta, una celda de carga real arrastra tres efectos que rara vez aparecen destacados:

- **Deriva por fluencia (*creep*)**: bajo una carga sostenida, el adhesivo que sujeta la galga y el propio metal siguen deformándose lentamente. La lectura cambia sola a lo largo de los minutos. Por eso las básculas de precisión piden estabilizarse antes de dar el valor bueno.
- **Histéresis**: el valor que lees subiendo de peso no coincide exactamente con el que lees bajando.
- **Deriva térmica del cero**: el puente compensa bien los cambios de temperatura uniformes, pero no un gradiente — un lado del aparato al sol y el otro a la sombra sí desequilibra el puente.

Los tres empeoran cuanto más barata es la celda, y ninguno se corrige recalibrando una sola vez.

## Cómo se aplica esto

Dos artículos de este sitio analizan aparatos que llevan esta misma cadena dentro, cada uno en un extremo del rango:

- [La galga extensométrica: cómo una balanza pesa hasta 0.01g](/blog/2026-08-10-la-galga-extensometrica-como-una-balanza-pesa-hasta-0-01g/) — el caso de alta resolución, donde el entorno (vibraciones, corrientes de aire, nivelación) limita el resultado más que la propia electrónica.
- [Galgas extensométricas: cómo tu báscula colgante pesa 300 kg](/blog/2026-08-16-galgas-extensometricas-como-tu-bascula-colgante-pesa-300-kg/) — el caso de fondo de escala alto, donde la tabla de arriba decide si el aparato te sirve para lo que sueles pesar.

Si vas a comprar cualquiera de los dos, la pregunta útil no es cuántos decimales muestra la pantalla. Es qué peso vas a medir habitualmente, y qué fracción del fondo de escala representa.
