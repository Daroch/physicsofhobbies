---
title: "Vatios, no grados: la física real de una punta que suelda bien"
pubDate: 2026-08-05
description: "Tocas un cable grueso con el soldador y la punta se enfría de golpe: eso no es un problema de temperatura, es un problema de potencia."
category: "electrónica"
image: "/images/blog/2026-08-05-vatios-no-grados-la-fisica-real-de-una-punta-que-suelda-bien.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B096X6SG13?tag=physicshobbie-21"
---

Sueldas un conector USB y la punta llega rápido a temperatura, pero en cuanto tocas un terminal grueso o un plano de tierra grande, el estaño no funde y tienes que esperar eternamente. Cambias el ajuste de temperatura pensando que el problema es ese, subes a 380°C, y sigue sin ir. El problema no está en los grados que marca la pantalla, está en cuánta energía puede entregar la punta por segundo mientras esa energía se escapa hacia la pieza que estás soldando.

Aquí entran en juego dos magnitudes distintas que se confunden todo el tiempo: temperatura y potencia. La temperatura te dice el estado térmico de la punta en reposo, pero cuando la pones en contacto con una masa metálica grande (un pad ancho, un cable grueso, un conector multipolo), esa masa actúa como un disipador que absorbe calor según $Q = m \cdot c \cdot \Delta T$, donde $m$ es la masa de la pieza y $c$ su calor específico. Si la potencia que entrega tu soldador ($P = V \cdot I$) no es suficiente para reponer ese calor tan rápido como se disipa, la punta se enfría por debajo del punto de fusión del estaño aunque el display siga marcando 380°C. La pantalla mide temperatura en un punto, no la capacidad de reposición térmica.

La mayoría de la gente sube la temperatura objetivo cuando debería estar preocupándose por la fuente de alimentación. Un soldador que recibe pocos vatios (por ejemplo, un cargador USB-C viejo limitado a 5V/2A, es decir 10W) tarda mucho más en recuperar temperatura tras cada contacto que uno alimentado con 20V/3A (60W). Si trabajas con piezas grandes o soldadura de componentes THT gruesos, revisa primero cuántos vatios reales te está dando tu fuente antes de tocar el ajuste de temperatura.

**Prueba rápida:**
1. Ajusta el soldador a 350°C y déjalo estabilizar 15 segundos.
2. Toca con la punta un trozo de cable de cobre grueso (2.5mm² o más) durante 3 segundos sin soldar nada.
3. Observa en pantalla cuánto tarda en volver a la temperatura objetivo tras retirar el cable.
4. Repite el mismo test alimentando el soldador con una fuente de menor potencia (un cargador de móvil básico, por ejemplo) y compara los tiempos de recuperación.

El Pinecil resuelve este problema de forma directa porque separa el control de temperatura (gestionado por su SoC RISC-V a 108 MHz, con precisión razonable gracias al IronOS) de la potencia disponible, que depende enteramente de lo que le conectes: con USB-C PD llega a 65W y con el conector de barril a 63W (21V, 3A), suficiente para la mayoría de trabajos de electrónica de consumo. Su limitación real es que sin una fuente PD/QC decente detrás, no vas a exprimir su rango de 100-400°C en piezas exigentes, así que la inversión en un buen cargador USB-C no es opcional, es parte del sistema.