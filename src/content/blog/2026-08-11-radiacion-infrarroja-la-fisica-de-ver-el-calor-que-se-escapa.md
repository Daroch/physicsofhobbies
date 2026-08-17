---
title: "Radiación infrarroja: la física de ver el calor que se escapa"
pubDate: 2026-08-11
description: "Cada objeto emite radiación según su temperatura, y esta cámara te deja verla sin tocar nada ni desmontar un solo cable."
category: "óptica"
image: "/images/blog/2026-08-11-radiacion-infrarroja-la-fisica-de-ver-el-calor-que-se-escapa.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0DJQ91653?tag=physicshobbie-21"
productName: "TOPDON Camara Termica TC004 Mini"
---

Tienes un cuadro eléctrico que hace ruido raro, una pared que en invierno siempre está más fría de lo normal, o un motor que sospechas se calienta más de lo debido. El problema es que no puedes ver el calor a simple vista, y desmontar todo para buscar el punto caliente con un termómetro de contacto es lento y a veces peligroso. Necesitas una forma de mapear temperaturas en tiempo real, sin tocar lo que estás midiendo.

Todo objeto por encima del cero absoluto emite radiación electromagnética en el infrarrojo, y esa emisión depende de su temperatura según la ley de Stefan-Boltzmann: $P = \epsilon \sigma A T^4$. Aquí $\epsilon$ es la emisividad del material (cuánto emite comparado con un cuerpo negro ideal), $\sigma$ es la constante de Stefan-Boltzmann, $A$ el área y $T$ la temperatura absoluta. Una cámara térmica no mide temperatura directamente: mide la intensidad de esa radiación infrarroja y la traduce a un valor de temperatura asumiendo un coeficiente de emisividad, normalmente fijado en 0.95 para la mayoría de superficies orgánicas y pintadas.

Aquí está el error que comete casi todo el mundo: apuntar la cámara a metal pulido o vidrio y confiar en la lectura. Estas superficies tienen emisividad baja y reflejan la radiación del entorno en vez de emitir la propia, así que la cámara te da temperaturas falsas, normalmente más bajas de lo real. Si necesitas medir sobre metal brillante, cubre la zona con cinta aislante mate o pintura negra antes de medir, ambas con emisividad conocida cercana a 0.95, y así consigues una lectura fiable.

**Prueba rápida (5 minutos):**
1. Enciende una bombilla incandescente y déjala 2 minutos.
2. Apunta la cámara a la bombilla y anota la temperatura del cristal.
3. Coloca un trozo de papel de aluminio pegado a la superficie y vuelve a medir el mismo punto.
4. Compara: la lectura sobre el aluminio será notablemente distinta, aunque la temperatura real no haya cambiado. Eso es la emisividad jugándote una mala pasada.

Si estás dudando entre una cámara como esta y un termómetro infrarrojo de pistola, que cuesta ocho veces menos, la diferencia real no es la precisión sino cuántas veces mide cada uno: está desarrollada en [qué mide cada uno](/blog/2026-08-17-termometro-infrarrojo-o-camara-termica-que-mide-cada-uno/).

La TC004 Mini ofrece una resolución de 240x240 píxeles térmicos, modesta si la comparas con equipos profesionales de 640x480, pero suficiente para localizar puntos calientes en instalaciones domésticas o revisar placas electrónicas. Su rango de -20°C a 450°C cubre la mayoría de aplicaciones de bricolaje y mantenimiento, y los 25 Hz de refresco evitan el efecto de imagen entrecortada al mover la cámara. Ten en cuenta que es un accesorio para smartphone Android con USB-C, no un dispositivo autónomo con pantalla propia, así que necesitas tu móvil compatible para poder usarla.