---
title: "Kit Raspberry Pi: qué alimentación y refrigeración elegir"
pubDate: 2026-09-25
description: "Solo un kit declara SSD NVMe y refrigeración activa; el resto no especifica tipo de almacenamiento ni potencia de fuente."
category: "electrónica"
tags: ["comparativa", "ciencia", "hobbies"]
type: "roundup"
grupoBusqueda: "raspberry-pi-kit-iniciacion-2026-08-05"
image: "/images/blog/2026-09-25-kit-raspberry-pi-que-alimentacion-y-refrigeracion-elegir-1.jpg"

audience: "Esta comparativa sirve a quien va a montar un servidor doméstico, un proyecto de domótica o aprender con una Raspberry Pi 5 o 4. No es para quien busca un mini PC de escritorio con GPU dedicada, ni para quien ya tiene una Pi y solo necesita accesorios sueltos."

specsThatMatter:
  - spec: "RAM (GB)"
    why: "Determina cuántos procesos o contenedores puedes correr a la vez sin que el sistema empiece a usar swap en la tarjeta de almacenamiento, mucho más lenta que la RAM. Cuatro de las cinco fichas llevan 8GB (Pi 5); la quinta, con Pi 4, se queda en 4GB, la mitad de margen para Home Assistant con muchos add-ons o para Docker."
  - spec: "Alimentación (W)"
    why: "La Raspberry Pi 5 necesita una fuente de 27W (5V/5A) para no entrar en avisos de baja tensión cuando conectas periféricos USB o un HAT. Dos de los kits declaran 27W, uno declara 15W (pensado para Pi 4, insuficiente para una Pi 5) y en dos fichas no aparece el dato, así que hay que comprobarlo antes de comprar."
  - spec: "Almacenamiento incluido y tipo"
    why: "La capacidad (64GB o 128GB) define cuánto puedes instalar, pero el tipo de soporte decide la velocidad real de lectura/escritura. Solo un kit especifica SSD M.2 NVMe PCIe en su ficha; los demás no aclaran si es microSD, eMMC u otro medio, algo relevante si vas a escribir logs de forma continua."
  - spec: "Refrigeración incluida"
    why: "Bajo carga sostenida (compilación, contenedores, IA) la Pi 5 puede reducir su frecuencia por temperatura si el disipador es solo pasivo. Las fichas mencionan ventilador, refrigeración activa, caja de aluminio o disipadores sueltos, pero ninguna aporta temperaturas ni RPM que permitan comparar la eficacia real."
  - spec: "Versión de placa (Pi 5 / Pi 4)"
    why: "La Pi 5 usa CPU Cortex-A76 y añade PCIe para NVMe, mientras que la Pi 4 del grupo se queda en la generación anterior. Esto condiciona tanto el rendimiento bruto como la posibilidad de montar un SSD NVMe en el futuro."

chooseBy:
  - scenario: "montas un servidor Home Assistant que va a estar encendido 24/7"
    priority: "alimentación declarada de 27W y refrigeración activa, para evitar throttling continuo"
  - scenario: "necesitas escrituras rápidas para bases de datos o contenedores"
    priority: "el kit que declara SSD M.2 NVMe frente a los que no especifican el tipo de almacenamiento"
  - scenario: "es tu primer proyecto y el presupuesto manda"
    priority: "el kit Pi 4 4GB, más barato, aceptando menos RAM y una CPU de generación anterior"
  - scenario: "ya tienes fuente de alimentación, carcasa y tarjeta de otro proyecto"
    priority: "comprar solo la placa Raspberry Pi 5 8GB sin kit"

comparison:
  columns: ["Versión de placa", "RAM (GB)", "Almacenamiento incluido (GB)", "Alimentación (W)", "Refrigeración incluida"]
  derivedNote: "No se añade columna calculada: ninguna combinación de RAM, almacenamiento, alimentación o refrigeración de esta tabla produce una métrica física nueva; cada dato se lee de forma independiente."

products:
  - name: "Raspberry Pi 5 8GB"
    shortName: "Raspberry Pi 5 8GB"
    tier: "Solo placa, sin kit"
    image: "/images/blog/2026-09-25-kit-raspberry-pi-que-alimentacion-y-refrigeracion-elegir-1.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CK2FCG1K?tag=physicshobbie-21"
    price: 219.9
    rating: 4.7
    reviews: 2943
    specs: ["Raspberry Pi 5", "8", "no disponible", "no disponible", "no disponible"]
    highlight: "Es solo la placa base Raspberry Pi 5 con 8GB de RAM, sin fuente, carcasa ni almacenamiento incluidos según su ficha. Adecuada para quien ya dispone de estos accesorios de un proyecto anterior."
  - name: "db-tronic Raspberry Pi 5 8 GB Starter Kit | Edición 128 GB | Alimentación 27 W | Carcasa con Ventilador | Micro HDMI | Disipador Aluminio | Ideal para Home Assistant y el Smart Home"
    shortName: "db-tronic Pi 5 8GB Starter"
    tier: "Kit completo con ventilador"
    image: "/images/blog/2026-09-25-kit-raspberry-pi-que-alimentacion-y-refrigeracion-elegir-2.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CRPF47RG?tag=physicshobbie-21"
    price: 254.99
    rating: 4.5
    reviews: 762
    specs: ["Raspberry Pi 5", "8", "128", "27", "Carcasa con ventilador + disipador de aluminio"]
    highlight: "Kit db-tronic con 128GB, fuente de 27W y carcasa con ventilador según su ficha, orientado por el fabricante a Home Assistant. No se declara el tipo de almacenamiento (microSD, eMMC u otro)."
  - name: "iRasptek Starter Kit For Raspberry Pi 5 8GB RAM - Edición OS-Bookworm de 128GB preinstalada (Caja de Aluminio)"
    shortName: "iRasptek Pi 5 8GB Starter"
    tier: "Kit con OS preinstalado"
    image: "/images/blog/2026-09-25-kit-raspberry-pi-que-alimentacion-y-refrigeracion-elegir-3.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0D1D6RFNG?tag=physicshobbie-21"
    price: 258.99
    rating: 4.7
    reviews: 449
    specs: ["Raspberry Pi 5", "8", "128", "no disponible", "Caja de aluminio"]
    highlight: "Kit iRasptek con 128GB y sistema Bookworm preinstalado, en caja de aluminio según su ficha. No especifica la potencia del alimentador incluido ni si lleva ventilador."
  - name: "db-tronic Raspberry Pi 5 8 GB NVMe Kit | Edición 64 GB | Alimentación 27 W | Carcasa metálica | Refrigeración Activa | SSD M.2 NVMe PCIe | Ideal para Home Assistant y el Smart Home"
    shortName: "db-tronic Pi 5 8GB NVMe"
    tier: "Kit con SSD NVMe"
    image: "/images/blog/2026-09-25-kit-raspberry-pi-que-alimentacion-y-refrigeracion-elegir-4.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CRMQCYXH?tag=physicshobbie-21"
    price: 259.99
    rating: 4.2
    reviews: 351
    specs: ["Raspberry Pi 5", "8", "64", "27", "Refrigeración activa + carcasa metálica"]
    highlight: "Único kit del grupo que declara SSD M.2 NVMe PCIe como almacenamiento (64GB) y refrigeración activa con carcasa metálica, según su ficha. Pensado para cargas de escritura más intensas que una microSD."
  - name: "db-tronic Raspberry Pi 4 4 GB Starter Kit | Edición 64 GB | Alimentación 15 W | Carcasa | HDMI 4K | Disipadores | Ideal para Home Assistant y el Smart Home"
    shortName: "db-tronic Pi 4 4GB Starter"
    tier: "Kit básico, placa anterior"
    image: "/images/blog/2026-09-25-kit-raspberry-pi-que-alimentacion-y-refrigeracion-elegir-5.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0D1N3V2FF?tag=physicshobbie-21"
    price: 154.99
    rating: 4.4
    reviews: 347
    specs: ["Raspberry Pi 4", "4", "64", "15", "Disipadores"]
    highlight: "Kit db-tronic basado en Raspberry Pi 4 con 4GB de RAM y fuente de 15W según su ficha, la única placa de generación anterior del grupo. El más barato de los cinco comparados, pero con menos RAM y CPU más antigua."

pitfalls:
  - claim: "Comprar solo la placa sale más a cuenta"
    reality: "En este listado, no tanto como parece. La Raspberry Pi 5 de 8GB suelta está a 219,90€ y el kit db-tronic con la misma placa más 128GB, fuente de 27W y carcasa con ventilador está a 254,99€: 35€ de diferencia por todo el equipamiento. Es un cálculo directo sobre los precios de esta tabla, no un dato de ninguna ficha."
  - claim: "Kit completo listo para usar"
    reality: "No siempre incluye fuente de alimentación con potencia declarada: en uno de los kits la ficha no menciona los vatios del alimentador, un dato clave para que una Pi 5 arranque sin avisos de baja tensión."
  - claim: "Edición 128GB / 64GB"
    reality: "La ficha no aclara si esa capacidad es una tarjeta microSD, eMMC u otro soporte en tres de los cuatro kits que traen almacenamiento; solo el kit NVMe especifica el tipo de almacenamiento, que condiciona la velocidad real de lectura/escritura."
  - claim: "Ideal para Home Assistant y el Smart Home"
    reality: "Es una recomendación de marketing del vendedor; la ficha no aporta temperaturas de operación, IOPS ni tiempos de arranque que permitan verificar esa idoneidad."
  - claim: "Refrigeración activa / carcasa con ventilador"
    reality: "Ninguna ficha da RPM del ventilador ni temperatura bajo carga sostenida, así que no se puede comparar cuánto throttling evita cada solución en uso continuo."

verdicts:
  - profile: "servidor doméstico 24/7 (Home Assistant, contenedores)"
    pick: "db-tronic Raspberry Pi 5 8GB NVMe Kit (B0CRMQCYXH)"
    why: "Es el único con SSD NVMe y refrigeración activa declarados en ficha, relevante para escritura continua de logs."
  - profile: "aprendizaje con presupuesto ajustado"
    pick: "db-tronic Raspberry Pi 4 4GB Starter Kit (B0D1N3V2FF)"
    why: "Es el más barato de los cinco comparados (154,99€), aunque con la mitad de RAM y una CPU de generación anterior. El grupo de Airtable tiene kits más económicos que no entraron en esta selección."
  - profile: "ya tienes fuente, carcasa y tarjeta de otro proyecto"
    pick: "Raspberry Pi 5 8GB sola (B0CK2FCG1K)"
    why: "Evitas pagar de nuevo por fuente, carcasa y tarjeta. Ahora bien, echa la cuenta antes: la placa sola cuesta 219,90€ y el kit db-tronic de 128GB con fuente de 27W y carcasa con ventilador está en 254,99€, así que en este listado esos accesorios salen por 35€."
  - profile: "necesitas confirmar el tipo exacto de almacenamiento antes de comprar"
    pick: "no comprar ninguno de estos basándote solo en esta ficha"
    why: "Tres de los cuatro kits que incluyen almacenamiento no especifican si es microSD, eMMC u otro soporte, dato que afecta directamente a la velocidad y vida útil."
---

Todas las Raspberry Pi comparten el mismo principio: son ordenadores completos en una placa cuyo rendimiento real no depende solo del procesador, sino de tres factores que sí varían entre las cinco fichas de esta comparativa (cuatro kits y una placa suelta): cuánta corriente les llega (alimentación), cómo evacúan el calor bajo carga (refrigeración) y en qué soporte guardan el sistema (tipo de almacenamiento). Una Pi 5 mal alimentada o sin disipación adecuada rinde por debajo de su potencial aunque el chip sea el mismo en todos los kits.

Por eso, comparar estos kits no es solo mirar el precio de la placa: es ver qué decide incluir cada fabricante alrededor de ella, y qué deja sin especificar. En este grupo, ese es precisamente el punto débil de varias fichas: la potencia del alimentador y el tipo exacto de almacenamiento no siempre aparecen, y son justo los datos que determinan si el kit aguanta el uso que tienes en mente.