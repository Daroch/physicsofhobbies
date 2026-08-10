---
title: "La galga extensométrica: cómo una balanza pesa hasta 0.01g"
pubDate: 2026-08-10
description: "Pesar polvo de resina o gramos de plata sin margen de error empieza por entender qué hay dentro de la báscula, no solo qué número muestra."
category: "electronica"
image: "/images/blog/2026-08-10-la-galga-extensometrica-como-una-balanza-pesa-hasta-0-01g.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B083NQJJ3G?tag=physicshobbie-21"
---

Preparas una mezcla de resina epóxica con una proporción exacta 2:1, o pesas gemas y metal para una pieza de joyería, y la báscula de cocina que tienes te da el mismo número aunque muevas el objeto medio centímetro hacia la izquierda. Ese margen de error de un par de gramos puede arruinar una mezcla química, hacer que una pieza no calce en su molde o que factures mal un metal precioso. El problema no es tu técnica, es la resolución del instrumento.

Dentro de una balanza analítica como esta hay una celda de carga con galgas extensométricas: tiras metálicas cuya resistencia eléctrica cambia mínimamente cuando se deforman bajo peso. Ese cambio se mide mediante un puente de Wheatstone, un circuito que detecta variaciones diminutas de resistencia y las convierte en una señal eléctrica proporcional a la fuerza aplicada, que en la Tierra equivale al peso: $F = mg$. Cuanto más sensible es el puente y más estable es la electrónica que amplifica esa señal, menor es el incremento mínimo que la balanza puede detectar, en este caso 0.01g sobre un rango de 5000g. Es una relación de 1 a 500,000, que exige tanto una construcción mecánica rígida como un circuito de amplificación con bajo ruido.

La mayoría de la gente arruina la precisión de una balanza analítica antes de pesar nada, simplemente por dónde la coloca. Las corrientes de aire, las vibraciones de una mesa compartida con una impresora 3D o un torno, y las superficies no niveladas introducen fuerzas parásitas que la celda de carga interpreta como peso real. Antes de cada sesión de trabajo, comprueba el nivel con la burbuja integrada (si la tiene) o con un nivel de burbuja externo, y deja que la balanza se estabilice eléctricamente durante unos minutos tras encenderla, porque los componentes electrónicos cambian ligeramente su comportamiento con la temperatura de funcionamiento.

**Prueba rápida:**
1. Enciende la balanza y déjala en reposo 5 minutos sobre una superficie firme.
2. Tara a cero y coloca un objeto pequeño y conocido, como una moneda de 1 céntimo (2.3g).
3. Retira el objeto y repite la medición tres veces.
4. Si el valor varía más de 0.02g entre repeticiones, el problema está en la superficie o en vibraciones externas, no en la balanza.

Esta Bonvoisin de 5000g/0.01g viene calibrada de fábrica, lo cual ahorra el paso de calibración con pesas de referencia certificadas al sacarla de la caja, aunque conviene verificarla igualmente con una pesa patrón si el trabajo es crítico. El plato de acero inoxidable de 16x18cm da margen para recipientes pequeños de laboratorio o piezas de joyería sin comprometer la lectura, y las funciones de tara y conteo de piezas resultan prácticas para quien pesa componentes electrónicos o cuentas de bisutería en serie. Su límite real está en el entorno: sin una superficie estable y sin protección de corrientes de aire, ni la mejor celda de carga rinde lo que promete su hoja de especificaciones.