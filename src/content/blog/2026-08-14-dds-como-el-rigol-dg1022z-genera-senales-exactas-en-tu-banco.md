---
title: "DDS: cómo el RIGOL DG1022Z genera señales exactas en tu banco"
pubDate: 2026-08-14
description: "Cada onda que sale de un generador parte de un reloj digital preciso: así controlas frecuencia, fase y forma sin el ruido de un oscilador analógico."
category: "electrónica"
image: "/images/blog/2026-08-14-dds-como-el-rigol-dg1022z-genera-senales-exactas-en-tu-banco.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B01N3LBIU6?tag=physicshobbie-21"
productName: "RIGOL Generador de Funciones,DG1022Z Generador de"
---

Estás depurando un filtro activo y necesitas saber si atenúa correctamente a 3 kHz, o quieres comprobar si tu amplificador satura antes de lo esperado. Con un multímetro no llegas a ninguna parte, y una fuente casera con un 555 te da una señal cuadrada con jitter y armónicos impredecibles. Necesitas una referencia limpia, con frecuencia y amplitud que puedas fijar con exactitud y repetir mañana igual que hoy.

Un generador de funciones moderno como el DG1022Z no dibuja la onda con un oscilador analógico que deriva con la temperatura: la calcula. Usa síntesis digital directa (DDS), un método donde un acumulador de fase avanza a cada ciclo de reloj y ese valor se traduce, vía una tabla de conversión digital-analógica, en el voltaje instantáneo de la onda. La frecuencia de salida depende de tres parámetros según $f_{out} = \dfrac{M \cdot f_{clk}}{2^N}$, donde $M$ es el incremento de fase por ciclo, $f_{clk}$ el reloj interno y $N$ la resolución del acumulador. Cuantos más bits tenga $N$, más fina es la resolución en frecuencia y menor el error acumulado.

El fallo típico al usar estos equipos es ignorar la impedancia de salida. El DG1022Z entrega su amplitud especificada asumiendo una carga de 50 ohmios; si conectas la salida a la entrada de alta impedancia de un osciloscopio (1 MΩ) sin ajustar la configuración de carga en el menú, verás el doble de la amplitud programada. Ese error de factor 2 confunde a mucha gente que jura que el generador está mal calibrado cuando en realidad falta un ajuste de tres segundos en el propio equipo. La impedancia manda también dentro de los componentes que vas a medir con él, donde [es un número complejo y no una simple resistencia](/blog/2026-08-13-la-impedancia-oculta-detras-de-cada-condensador-y-bobina/).

**Prueba rápida (5 minutos):**
1. Configura el canal 1 en onda cuadrada, 1 kHz, 2 V pico a pico, salida a 50 ohmios.
2. Conecta el osciloscopio con una punta 1x directamente al conector BNC.
3. Ajusta en el menú del generador la carga a "alta impedancia" si tu punta no es 50 ohmios, y compara la amplitud leída con la programada.
4. Sube la frecuencia a 20 MHz y observa cómo se redondean los flancos: eso te da una idea directa del ancho de banda real del sistema, no solo del generador.

El DG1022Z cubre 25 MHz en dos canales independientes, con formas de onda estándar, arbitrarias y varios esquemas de modulación (AM, FM, PM, FSK, entre otros), suficiente para la mayoría de trabajo de banco en audio, control y electrónica digital de baja velocidad. No es un equipo para RF ni para señales de alta frecuencia con exigencias de pureza espectral estrictas, pero para diseñar, depurar y enseñar electrónica analógica y digital convencional cumple con precisión y estabilidad que un oscilador casero no te va a dar.