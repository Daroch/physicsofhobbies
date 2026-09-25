---
title: "Kit de iniciación Raspberry Pi: qué placa y RAM elegir"
pubDate: 2026-09-25
description: "La RAM, el tipo de almacenamiento y la potencia de la fuente cambian si el kit sirve para aprender o para domótica exigente."
category: "electrónica"
tags: ["comparativa", "ciencia", "hobbies"]
type: "roundup"
grupoBusqueda: "raspberry-pi-kit-iniciacion-2026-08-05"
image: "/images/blog/2026-09-25-kit-de-iniciacion-raspberry-pi-que-placa-y-ram-elegir-1.jpg"

audience: "Esto es para quien va a comprar su primer Raspberry Pi para aprender programación, montar un hub de domótica o un servidor casero ligero. No lo necesitas si ya tienes placa y solo buscas componentes sueltos, o si buscas potencia de escritorio: un SBC no compite en eso."

specsThatMatter:
  - spec: "Modelo de Raspberry Pi incluido (o si el kit no incluye placa)"
    why: "Un kit puede ser compatible con varios modelos sin incluir ninguno: es el caso del kit que solo trae accesorios y tutorial. Los demás sí incluyen una placa concreta (Pi 4 o Pi 5), con arquitecturas y rendimiento distintos. Decide si tu presupuesto real incluye la placa o hay que sumarla aparte."
  - spec: "RAM (2/4/8 GB)"
    why: "Determina cuántos servicios o contenedores puedes correr a la vez. Para Home Assistant con pocas integraciones, 2 GB puede bastar; para varias integraciones simultáneas o tareas de servidor, 4-8 GB evitan cuellos de memoria según el uso previsto."
  - spec: "Tipo de almacenamiento (microSD vs NVMe SSD)"
    why: "Una SSD NVMe por PCIe ofrece velocidades de lectura/escritura muy superiores a una tarjeta microSD, algo relevante para bases de datos (Home Assistant) o tiempos de arranque. Solo uno de estos kits especifica NVMe; en el resto no se aclara el formato exacto de los 64 GB."
  - spec: "Potencia de la fuente de alimentación (W)"
    why: "La Raspberry Pi 5 recomienda oficialmente 27 W (5V/5A) para funcionar sin recortes con periféricos o SSD conectados. Una fuente de 15 W, pensada para Pi 4, puede quedarse corta si se usa en Pi 5. Dos de las fichas ni siquiera declaran este dato."
  - spec: "Refrigeración (pasiva vs activa)"
    why: "Bajo carga sostenida, la Pi 5 genera más calor que la Pi 4. Disipadores pasivos pueden no evitar el throttling térmico en tareas largas, mientras que un ventilador activo sí lo previene según ficha. No es lo mismo aunque ambos se anuncien como 'refrigeración'."

chooseBy:
  - scenario: "quieres aprender programación y electrónica con proyectos guiados"
    priority: "prioriza el volumen de tutorial y lenguajes soportados, aunque tengas que comprar la placa aparte."
  - scenario: "buscas un hub de domótica básico con pocas integraciones"
    priority: "un Pi 4 de 2 GB con 15 W de fuente basta según ficha."
  - scenario: "vas a correr varias integraciones o contenedores en Home Assistant"
    priority: "sube a 4 GB u 8 GB de RAM para evitar cuellos de memoria."
  - scenario: "usarás el equipo como servidor casero o NAS ligero"
    priority: "prioriza almacenamiento NVMe y una fuente de 27 W, no microSD ni 15 W."

comparison:
  columns: ["Modelo de Raspberry Pi incluido", "RAM", "Almacenamiento incluido", "Potencia de la fuente (W)", "Refrigeración"]
  derivedNote: "No se incluye columna calculada: RAM, almacenamiento, potencia y refrigeración son magnitudes independientes en estas fichas, ninguna combinación entre ellas produce un dato nuevo relevante para la compra."

products:
  - name: "Freenove Kit de Arranque Completo para Raspberry Pi 5 4 B 3 B+ 500 Zero 2 W, Tutorial de 1170 Páginas, Python C Java Scratch Processing Code, 386 Artículos, 164 Proyectos, Altavoces Cámara"
    shortName: "Freenove Kit Accesorios"
    tier: "Kit sin placa, aprendizaje"
    image: "/images/blog/2026-09-25-kit-de-iniciacion-raspberry-pi-que-placa-y-ram-elegir-1.jpg"
    amazonUrl: "https://www.amazon.es/dp/B09ZXNL2WH?tag=physicshobbie-21"
    price: 64.95
    rating: 4.6
    reviews: 344
    specs: ["No incluye placa (compatible con Pi 5/4B/3B+/500/Zero 2W)", "no disponible", "no disponible", "no disponible", "no disponible"]
    highlight: "Según su ficha, este kit no incluye la placa Raspberry Pi: aporta tutorial de 1170 páginas, 386 artículos y 164 proyectos con altavoz y cámara. Útil si ya tienes o vas a comprar la placa por separado."
  - name: "db-tronic Raspberry Pi 4 2 GB Starter Kit | Edición 64 GB | Alimentación 15 W | Carcasa | HDMI 4K | Disipadores | Ideal para Home Assistant y el Smart Home"
    shortName: "db-tronic Pi4 2GB"
    tier: "Entrada, domótica básica"
    image: "/images/blog/2026-09-25-kit-de-iniciacion-raspberry-pi-que-placa-y-ram-elegir-2.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DDZGB6S5?tag=physicshobbie-21"
    price: 119.99
    rating: 4.2
    reviews: 69
    specs: ["Raspberry Pi 4 (2 GB RAM)", "2 GB", "64 GB", "15 W", "Disipadores (pasiva)"]
    highlight: "Kit completo con placa incluida y fuente de 15 W, suficiente para Pi 4 según ficha. Pensado para tareas ligeras de Home Assistant o smart home básico, no para cargas exigentes."
  - name: "db-tronic Raspberry Pi 4 4 GB Starter Kit | Edición 64 GB | Alimentación 15 W | Carcasa | HDMI 4K | Disipadores | Ideal para Home Assistant y el Smart Home"
    shortName: "db-tronic Pi4 4GB"
    tier: "Gama media, domótica"
    image: "/images/blog/2026-09-25-kit-de-iniciacion-raspberry-pi-que-placa-y-ram-elegir-3.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0D1N3V2FF?tag=physicshobbie-21"
    price: 154.99
    rating: 4.4
    reviews: 347
    specs: ["Raspberry Pi 4 (4 GB RAM)", "4 GB", "64 GB", "15 W", "Disipadores (pasiva)"]
    highlight: "Misma base que la variante de 2 GB pero con el doble de RAM, útil si vas a correr varias integraciones en Home Assistant. La fuente sigue siendo de 15 W, suficiente para Pi 4 según ficha."
  - name: "iRasptek Kit de inicio para Raspberry Pi 5 RAM 4 GB- 64 GB edición de OS-Bookworm precargado (funda roja y blanca)"
    shortName: "iRasptek Pi5 4GB"
    tier: "Pi 5 lista para usar"
    image: "/images/blog/2026-09-25-kit-de-iniciacion-raspberry-pi-que-placa-y-ram-elegir-4.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CZRJ238K?tag=physicshobbie-21"
    price: 203.21
    rating: 4.6
    reviews: 56
    specs: ["Raspberry Pi 5 (4 GB RAM)", "4 GB", "64 GB (OS Bookworm precargado)", "no disponible", "no disponible"]
    highlight: "Trae el sistema operativo precargado para arrancar directo, pero la ficha no declara la potencia de la fuente ni el tipo de refrigeración, dato relevante porque la Pi 5 recomienda 27 W."
  - name: "db-tronic Raspberry Pi 5 8 GB NVMe Kit | Edición 64 GB | Alimentación 27 W | Carcasa metálica | Refrigeración Activa | SSD M.2 NVMe PCIe | Ideal para Home Assistant y el Smart Home"
    shortName: "db-tronic Pi5 8GB NVMe"
    tier: "Gama alta, rendimiento"
    image: "/images/blog/2026-09-25-kit-de-iniciacion-raspberry-pi-que-placa-y-ram-elegir-5.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CRMQCYXH?tag=physicshobbie-21"
    price: 259.99
    rating: 4.2
    reviews: 351
    specs: ["Raspberry Pi 5 (8 GB RAM)", "8 GB", "64 GB NVMe SSD (M.2 PCIe)", "27 W", "Activa"]
    highlight: "El único con SSD NVMe, fuente de 27 W acorde a lo que pide la Pi 5 y refrigeración activa según ficha. Orientado a servidor casero o cargas sostenidas, con el precio más alto del grupo."

pitfalls:
  - claim: "Kit de iniciación completo para Raspberry Pi 5/4/3B+/500/Zero 2W"
    reality: "Compatibilidad con varios modelos no significa que la placa esté incluida; en este caso el kit son accesorios y tutorial, la Raspberry Pi se compra aparte."
  - claim: "Alimentación 15 W incluida"
    reality: "15 W es suficiente para Raspberry Pi 4, pero la Pi 5 recomienda oficialmente 27 W; no sirve para alimentarla con garantías según las especificaciones del fabricante."
  - claim: "Edición 64 GB"
    reality: "El dato de capacidad no aclara si es una tarjeta microSD o un SSD; la velocidad real de lectura/escritura cambia radicalmente entre ambos formatos."
  - claim: "Refrigeración incluida"
    reality: "Unos kits declaran solo disipadores pasivos y otros ventilador activo; bajo carga sostenida el resultado térmico no es equivalente aunque ambos se anuncien como 'refrigeración'."

verdicts:
  - profile: "Quiere aprender programación y electrónica con proyectos guiados"
    pick: "Freenove Kit Accesorios"
    why: "Aporta el tutorial más extenso del grupo (1170 páginas, 164 proyectos), pero recuerda sumar el coste de la placa que no incluye."
  - profile: "Domótica básica con pocas integraciones"
    pick: "db-tronic Pi4 2GB"
    why: "Placa, fuente de 15 W y carcasa incluidas a menor precio que el resto de kits con placa según ficha."
  - profile: "Hub de domótica con varias integraciones simultáneas"
    pick: "db-tronic Pi4 4GB"
    why: "Duplica la RAM frente al modelo de 2 GB para el mismo tipo de fuente, reduciendo el riesgo de cuellos de memoria."
  - profile: "Servidor casero o cargas sostenidas exigentes"
    pick: "db-tronic Pi5 8GB NVMe"
    why: "Único con SSD NVMe, 27 W de fuente y refrigeración activa, los tres datos que la ficha de Pi 5 exige para rendimiento estable."
---

Un kit de Raspberry Pi no es solo la placa: es un conjunto de piezas que tienen que funcionar juntas dentro de los límites físicos del propio SoC. La cantidad de RAM, el bus de almacenamiento y la potencia de la fuente no son accesorios intercambiables, son parámetros que determinan si el sistema arranca de forma estable o entra en throttling térmico o en cuellos de botella de memoria bajo carga.

La Raspberry Pi 5, por ejemplo, declara oficialmente una demanda de 27 W frente a los 15 W que suelen bastar para una Pi 4; usar una fuente pensada para el modelo anterior en el más reciente no es un simple ahorro, es un riesgo de inestabilidad documentado por el propio fabricante del SoC. Del mismo modo, el paso de una tarjeta microSD a un SSD por PCIe cambia el ancho de banda de E/S en un orden de magnitud, algo que pesa mucho si vas a correr una base de datos de Home Assistant o un servidor de archivos.

Por eso, antes de mirar el precio del kit, conviene identificar qué placa incluye realmente (si es que incluye alguna), cuánta RAM trae y qué tipo de almacenamiento y refrigeración declara su ficha. Son esos datos, y no el número de accesorios listados en el título, los que determinan si el kit sirve para lo que planeas hacer con él.