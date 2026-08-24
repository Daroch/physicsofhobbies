---
title: "Kit Arduino: qué placa y accesorios incluye decide"
pubDate: 2026-08-24
description: "Los kits difieren en placa (UNO R3 o Mega 2560), fuente de alimentación y accesorios como relé, motor paso a paso o breadboard según su ficha."
category: "electrónica"
tags: ["comparativa", "ciencia", "hobbies"]
type: "roundup"
grupoBusqueda: "kit-arduino-sensores-completo-2026-08-09"
image: "/images/blog/2026-08-24-kit-arduino-que-placa-y-accesorios-incluye-decide-1.jpg"

audience: "Esto te sirve si vas a empezar con Arduino y necesitas decidir entre varios kits según qué placa y accesorios trae cada uno. No lo necesitas si ya tienes una placa Arduino y solo buscas un componente suelto, ni si tu proyecto exige especificaciones eléctricas exactas que estos anuncios no detallan."

specsThatMatter:
  - spec: "Tipo de placa (UNO R3 vs Mega 2560 R3)"
    why: "El Mega 2560 declara más pines digitales y analógicos y más memoria flash que el UNO R3, relevante si conectas muchos sensores o módulos a la vez. Si tu proyecto usa pocos sensores, el UNO R3 evita pagar por pines que no vas a usar."
  - spec: "Fuente de alimentación incluida"
    why: "Un módulo regulado con voltaje y corriente declarados (como el 9V 1A de Miuzei) evita alimentar motores o servos desde el USB del ordenador, que puede no dar corriente suficiente. Los kits que solo dicen 'módulo de fuente de alimentación' sin cifras no permiten calcular si cubre tu consumo."
  - spec: "Breadboard/protoboard incluida"
    why: "Sin ella no puedes montar ningún circuito con sensores sin soldar, así que su ausencia obliga a comprarla aparte antes de seguir cualquier tutorial del kit."
  - spec: "Servomotor o motor paso a paso incluido"
    why: "El servomotor da control de ángulo limitado (normalmente hasta 180°), útil para brazos o dirección. El motor paso a paso ofrece posicionamiento preciso en vueltas completas, más adecuado para robótica o mecanismos que necesitan giro continuo controlado."

chooseBy:
  - scenario: "vas a conectar muchos sensores o módulos a la vez"
    priority: "placa con más pines y memoria (Mega 2560 R3 según ficha)"
  - scenario: "quieres alimentar motores o servos sin depender del USB"
    priority: "fuente de alimentación con voltaje y corriente declarados"
  - scenario: "necesitas posicionamiento preciso en vueltas completas"
    priority: "kit que declare motor paso a paso incluido"
  - scenario: "empiezas de cero y quieres el gasto mínimo"
    priority: "kit básico con placa UNO R3 y protoboard, sin extras que no vas a usar"

comparison:
  columns: ["Placa base incluida", "Servomotor incluido", "Breadboard/protoboard incluida", "Fuente de alimentación incluida"]
  derivedNote: "No se incluye columna calculada: los datos disponibles son categóricos (sí/no/tipo de placa), no hay dos magnitudes numéricas de la ficha que combinar para obtener un criterio nuevo."

products:
  - name: "ELEGOO Conjunto Medio de Iniciación Compatible con Arduino IDE, Stem Kit | con Tutorial en Español, Relé de 5V, Modulo de Fuente de Alimentación, Servomotor, UNO R3 Placa de Desarrollo de Prototipos"
    shortName: "ELEGOO Kit Medio UNO R3"
    tier: "Kit intermedio con relé y servo"
    image: "/images/blog/2026-08-24-kit-arduino-que-placa-y-accesorios-incluye-decide-1.jpg"
    amazonUrl: "https://www.amazon.es/dp/B01MXGST4I?tag=physicshobbie-21"
    price: 39.07
    rating: 4.6
    reviews: 2867
    specs: ["UNO R3", "Sí", "no disponible", "Módulo genérico (sin V/A)"]
    highlight: "Según su ficha incluye relé de 5V, servomotor y un módulo de fuente de alimentación sin especificar voltaje o corriente. No se menciona breadboard, así que si no la tienes, cuenta con comprarla aparte."
  - name: "ELEGOO Conjunto Más Completo y Avanzado de Iniciación Mega 2560 | Compatible con Arduino IDE Stem Kit con Guías Tutorial en Español y Conjunto con Placa Controladora Mega 2560 R3, Servomotor"
    shortName: "ELEGOO Kit Mega 2560"
    tier: "Kit avanzado con placa Mega 2560"
    image: "/images/blog/2026-08-24-kit-arduino-que-placa-y-accesorios-incluye-decide-2.jpg"
    amazonUrl: "https://www.amazon.es/dp/B01MQPT9OD?tag=physicshobbie-21"
    price: 59.48
    rating: 4.6
    reviews: 1920
    specs: ["Mega 2560 R3", "Sí", "no disponible", "no disponible"]
    highlight: "Es el único de los cinco con placa Mega 2560 R3 según su título, útil si tu proyecto necesita más pines o memoria que un UNO R3. La ficha no detalla fuente de alimentación ni breadboard, y el título aparece truncado, así que el contenido completo no está claro."
  - name: "ELEGOO Conjunto Avanzado de Iniciación, Stem Kit Compatible con Arduino IDE | con Tutorial en Español y UNO R3 Placa, Relé, Modulo de Fuente de Alimentación, Motor Paso a Paso, Breadboard, etc"
    shortName: "ELEGOO Kit Avanzado UNO R3"
    tier: "Kit avanzado con motor paso a paso"
    image: "/images/blog/2026-08-24-kit-arduino-que-placa-y-accesorios-incluye-decide-3.jpg"
    amazonUrl: "https://www.amazon.es/dp/B01M9J4GCU?tag=physicshobbie-21"
    price: 56.51
    rating: 4.6
    reviews: 950
    specs: ["UNO R3", "no disponible", "Sí", "Módulo genérico (sin V/A)"]
    highlight: "Según su ficha incluye relé, motor paso a paso y breadboard, orientado a proyectos de robótica básica con posicionamiento preciso. El título termina en 'etc', así que puede traer más piezas no listadas; no hay confirmación de servomotor."
  - name: "ELEGOO UNO R3 Conjunto Básico de Iniciación Compatible con Arduino IDE | con Guías Tutorial en Español, Starter Kit para Arduino UNO, Stem Kit con Placa UNO R3 y Protoboard"
    shortName: "ELEGOO Kit Básico UNO R3"
    tier: "Kit básico de entrada"
    image: "/images/blog/2026-08-24-kit-arduino-que-placa-y-accesorios-incluye-decide-4.jpg"
    amazonUrl: "https://www.amazon.es/dp/B06W2KF3PJ?tag=physicshobbie-21"
    price: 24.01
    rating: 4.6
    reviews: 922
    specs: ["UNO R3", "no disponible", "Sí (protoboard)", "no disponible"]
    highlight: "Es el más barato de los cinco (24,01 €) y su ficha solo confirma placa UNO R3 y protoboard, sin relé, motor ni fuente de alimentación mencionados. Adecuado si buscas lo mínimo para empezar sin pagar por accesorios que no necesitas."
  - name: "Miuzei Starter Set Compatible con Arduino Kit con Tutoría en Español, Breadboard, Servo, 9V 1A Power Supply, sensors, Leds para R3 Electronica Kit"
    shortName: "Miuzei Kit Starter UNO"
    tier: "Kit alternativo con sensores variados"
    image: "/images/blog/2026-08-24-kit-arduino-que-placa-y-accesorios-incluye-decide-5.jpg"
    amazonUrl: "https://www.amazon.es/dp/B07CXKP3R3?tag=physicshobbie-21"
    price: 37.99
    rating: 4.5
    reviews: 843
    specs: ["UNO R3 (compatible)", "Sí", "Sí", "9V 1A regulada"]
    highlight: "Es el único que declara una fuente de alimentación con voltaje y corriente concretos (9V 1A), un dato que el resto no ofrece. Su ficha menciona 'sensors' y LEDs de forma genérica, sin especificar cuáles ni cuántos."

pitfalls:
  - claim: "Compatible con Arduino IDE"
    reality: "Significa que la placa es un clon que funciona con el software oficial de Arduino, no que sea una placa Arduino original. Funcionalmente similar, pero no es el mismo fabricante."
  - claim: "Conjunto más completo y avanzado"
    reality: "Es una valoración del vendedor en el título, no un dato verificable de la ficha. Compara el contenido real listado (placa, relé, motor, breadboard) antes de asumir que es superior a otro kit."
  - claim: "Tutorial en español incluido"
    reality: "Confirma el idioma del material, no su profundidad ni si cubre todos los componentes del kit. La ficha no detalla el número de lecciones ni proyectos incluidos."
  - claim: "Título termina en 'etc' tras listar componentes"
    reality: "Indica que el kit trae más piezas de las mencionadas, pero no dice cuáles. No asumas que incluye un componente concreto (como servomotor o sensor) si no aparece explícitamente listado."

verdicts:
  - profile: "Empiezas de cero con presupuesto ajustado"
    pick: "ELEGOO Kit Básico UNO R3 (B06W2KF3PJ)"
    why: "Es el más barato (24,01 €) y su ficha confirma lo mínimo necesario: placa UNO R3 y protoboard, sin pagar por accesorios que no vas a usar al principio."
  - profile: "Proyecto con muchos sensores o módulos simultáneos"
    pick: "ELEGOO Kit Mega 2560 (B01MQPT9OD)"
    why: "Es el único con placa Mega 2560 R3 según su título, con más pines y memoria que un UNO R3 para conectar más dispositivos a la vez."
  - profile: "Robótica con control de cargas y posicionamiento preciso"
    pick: "ELEGOO Kit Avanzado UNO R3 (B01M9J4GCU)"
    why: "Su ficha declara relé de 5V y motor paso a paso, componentes útiles para conmutar cargas externas y lograr giro controlado, algo que los demás no confirman juntos."
  - profile: "Necesitas saber la corriente exacta que entrega la fuente"
    pick: "no comprar ninguno de estos sin verificar antes"
    why: "Solo el kit Miuzei declara voltaje y corriente de su fuente (9V 1A); el resto dice 'módulo de fuente de alimentación' sin cifras, dato que no puedes calcular ni suponer."
---

Todos estos kits giran en torno a la misma placa de control (Arduino UNO R3 o Mega 2560 R3), un microcontrolador que ejecuta el código y gestiona las señales digitales y analógicas de los sensores y actuadores conectados. La diferencia real entre un kit y otro no está en la placa en sí, sino en qué se conecta a ella: un relé permite manejar cargas externas de mayor voltaje, un motor paso a paso da giro controlado en pasos discretos, y una fuente de alimentación regulada evita depender del USB del ordenador para alimentar esos componentes.

Como las fichas de estos productos son títulos de anuncio y no hojas técnicas detalladas, muchos datos concretos (voltaje/corriente de la fuente, número exacto de sensores, memoria de la placa) no están disponibles. Esto obliga a decidir por lo que sí se declara explícitamente en cada título: qué placa trae, qué actuador incluye y si menciona o no una protoboard, en lugar de por calificativos como 'completo' o 'avanzado' que no aportan una magnitud verificable.