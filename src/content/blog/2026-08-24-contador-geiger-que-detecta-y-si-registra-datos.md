---
title: "Mejor contador Geiger: CPM, µSv/h y qué mide cada ficha"
pubDate: 2026-08-24
updatedDate: 2026-09-25
description: "Siete contadores Geiger comparados por su ficha: solo uno declara en qué unidades mide. Por qué CPM y µSv/h no son la misma medida y cuál te interesa."
category: "óptica"
tags: ["comparativa", "ciencia", "hobbies"]
type: "roundup"
grupoBusqueda: "contador-geiger-2026-08-05"
image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-1.jpg"

audience: "Esto es para quien quiere vigilar radiación ambiental, comprobar una pieza de cerámica vidriada o un mineral, o simplemente entender qué está midiendo el aparato antes de pagarlo. No es para radioprotección profesional: ninguna de estas fichas declara isótopo de calibración ni incertidumbre, y sin eso no hay medida defendible ante un organismo."

specsThatMatter:
  - spec: "En qué unidad muestra la lectura: CPM, µSv/h o µSv acumulados"
    why: "No son tres formas de decir lo mismo. Un tubo Geiger-Müller solo sabe hacer una cosa: contar pulsos, y eso son los CPM (cuentas por minuto), la medida cruda y honesta. Los µSv/h son una tasa de dosis, y para llegar a ellos el aparato multiplica los CPM por un factor de conversión fijo. Los µSv acumulados son la integral de esa tasa en el tiempo, que es lo que de verdad importa si te expones durante horas. Un aparato que solo enseña µSv/h te está dando el resultado de una cuenta cuyas suposiciones no puedes ver."
  - spec: "Isótopo contra el que está calibrado ese factor de conversión"
    why: "Aquí está la trampa de fondo. El factor CPM→µSv/h depende de la energía de los fotones que estés midiendo y de la geometría del tubo, y el convenio del sector es calibrar con cesio-137, cuyo gamma está en 661,7 keV. Apunta ese mismo aparato a una fuente de energía muy distinta y la cifra en µSv/h deja de ser correcta, mientras que los CPM siguen siendo un conteo real. Ninguna de las siete fichas dice con qué isótopo se calibró."
  - spec: "Tipo de tubo: cilíndrico de pared de vidrio o pancake con ventana de mica"
    why: "Es lo que decide qué puedes detectar de verdad, y no lo declara ninguno. Un tubo cilíndrico convencional tiene una pared que frena la radiación beta de baja energía antes de que llegue al gas: detecta gamma bien y beta solo a partir de cierta energía. Un tubo pancake con ventana fina de mica deja pasar beta blanda e incluso alfa. Por eso «detecta beta» en un título no significa que detecte cualquier beta."
  - spec: "Volcado de datos a un ordenador"
    why: "Una medida aislada de radiación ambiental no dice casi nada, porque el fondo natural varía con la altitud, la geología y hasta la presión atmosférica. Lo que informa es la serie temporal: saber cuál es tu fondo habitual para reconocer cuándo algo se sale de él. Sin volcado, esa serie la construyes copiando números a mano."

chooseBy:
  - scenario: "quieres entender qué mide el aparato y no solo ver un número"
    priority: "el que declare las unidades en la propia ficha, que aquí es solo el AEGTEST Radar-5633"
  - scenario: "vas a vigilar el fondo ambiental durante semanas o meses"
    priority: "volcado a ordenador: el GMC-800 lo declara como registrador, el FS5000 como software de PC"
  - scenario: "quieres medir beta de baja energía o comprobar contaminación superficial"
    priority: "ninguno de estos sin preguntar antes al vendedor si el tubo es pancake con ventana de mica"
  - scenario: "buscas el respaldo de una base de usuarios grande"
    priority: "la gama GQ, que reúne las cuatro fichas con más reseñas de este grupo"

comparison:
  columns: ["Unidades que declara la ficha", "Volcado a ordenador", "Tipos de radiación declarados"]
  derivedNote: "Esta tabla informa tanto por lo que varía como por lo que no. La primera columna está casi vacía a propósito: seis de las siete fichas no dicen en qué unidad muestran la lectura, y esa ausencia es el hallazgo principal, no un hueco que rellenar. La tercera es casi idéntica en todas las filas, y eso demuestra lo contrario: «beta, gamma y rayos X» lo declara casi todo el mundo, así que no sirve para elegir entre estos modelos por mucho que ocupe el título. No hay columna calculada porque no hay ninguna cifra numérica común que combinar: ninguna ficha del grupo declara sensibilidad, rango de dosis ni tipo de tubo."

products:
  - name: "Geiger AEGTEST Radar-5633 - Detector de radiación nuclear LCD, dosímetro recargable para β γ X, mediciones en CPM μSv/h μR/h μSv - Azul"
    shortName: "AEGTEST Radar-5633"
    tier: "el único que dice en qué mide"
    image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-6.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0DT5TKH6P?tag=physicshobbie-21"
    price: 69.99
    rating: 4.2
    reviews: 279
    specs: ["CPM, µSv/h, µR/h y µSv", "no disponible", "β, γ y X"]
    highlight: "Es el único de los siete cuya ficha enumera las magnitudes de la pantalla, y además incluye µSv a secas, es decir dosis acumulada y no solo tasa. Es también el más barato del grupo a 69,99€ y el de valoración más baja (4.2 sobre 279 reseñas). No declara con qué isótopo se calibró el paso de CPM a µSv/h."
  - name: "Detector de Radiación Nuclear GQ GMC-800 Diseño de EE.UU. Producto de Estándar Nacional de EE.UU. Dosímetro Registrador de Datos & Compartición Global Beta Gamma Rayos X Multifunción Contador Geiger."
    shortName: "GQ GMC-800"
    tier: "registro de datos declarado"
    image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-3.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0CKM8NML7?tag=physicshobbie-21"
    price: 99
    rating: 4.6
    reviews: 1211
    specs: ["no disponible", "Registrador de datos y compartición", "β, γ y X"]
    highlight: "A 99€ es el de la gama GQ que declara explícitamente «Registrador de Datos & Compartición Global», lo que apunta a serie temporal y no solo a lectura instantánea. La ficha no concreta el protocolo (USB, wifi o bluetooth) ni el formato de exportación, así que no se puede saber de antemano si encaja en tu flujo de trabajo."
  - name: "FS5000 Medidor Geiger, radiactividad, detector de radiación, medidor de radiación nuclear con software de PC, beta, gamma y rayos X, recargable, monitor, probador"
    shortName: "FS5000"
    tier: "software de PC declarado"
    image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-7.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0D3PX1W5B?tag=physicshobbie-21"
    price: 79
    rating: 4.5
    reviews: 215
    specs: ["no disponible", "Software de PC", "β, γ y X"]
    highlight: "La segunda vía de volcado del grupo, a 79€ y con 4.5 sobre 215 reseñas. Su ficha menciona software de PC, pero no dice para qué sistema operativo ni si el formato de salida es abierto, que es lo que decide si puedes tratar los datos con tus propias herramientas."
  - name: "GQ GMC-500+ Plus - Detector contador Geiger de radiación nuclear, para rayos X, beta y gamma"
    shortName: "GQ GMC-500+"
    tier: "el de más reseñas"
    image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-1.jpg"
    amazonUrl: "https://www.amazon.es/dp/B071JWB7TJ?tag=physicshobbie-21"
    price: 157
    rating: 4.6
    reviews: 1824
    specs: ["no disponible", "no disponible", "β, γ y X"]
    highlight: "El más caro del grupo (157€) y el que más reseñas acumula (1824, con 4.6). El «+» del nombre alude en la gama GQ a una segunda etapa de detección, pero la ficha de Amazon no lo desarrolla ni declara unidades, sensibilidad o tubo."
  - name: "GQ GMC de 320 Plus Geiger counter Nuclear Radiation Detector metros Beta Gamma X Blu-ray Europe"
    shortName: "GQ GMC-320 Plus"
    tier: "gama media GQ"
    image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-4.jpg"
    amazonUrl: "https://www.amazon.es/dp/B00ROHGWIQ?tag=physicshobbie-21"
    price: 125
    rating: 4.6
    reviews: 849
    specs: ["no disponible", "no disponible", "β, γ y X"]
    highlight: "A 125€ con 4.6 sobre 849 reseñas. Su título está claramente mal traducido («metros» por meters, «Blu-ray» por X-ray), lo que no dice nada del aparato pero sí de cuánta atención se le ha puesto a la ficha de la que vas a sacar tus datos."
  - name: "GQ GMC-300S Digital Detector de radiación nuclear Monitor Medidor Geiger Contador Dosímetro de radiación"
    shortName: "GQ GMC-300S"
    tier: "entrada de la gama GQ"
    image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-2.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0B541D433?tag=physicshobbie-21"
    price: 89
    rating: 4.6
    reviews: 1252
    specs: ["no disponible", "no disponible", "no disponible"]
    highlight: "La entrada de gama GQ a 89€, con 1252 reseñas y 4.6. Es el único de los siete cuyo título no menciona qué tipos de radiación detecta: dice «dosímetro», que sugiere dosis acumulada, pero no lo concreta en ninguna parte de la ficha."
  - name: "Detector de Radiación Nuclear Contador Geiger, Fellat Portátil Digital Dosimeter de Alta Sensibilidad Precisión Beta Gamma X-ray Monitor con Pantalla LCD Grande"
    shortName: "Fellat Dosímetro"
    tier: "pantalla grande"
    image: "/images/blog/2026-08-24-contador-geiger-que-detecta-y-si-registra-datos-5.jpg"
    amazonUrl: "https://www.amazon.es/dp/B0B3MH4G2T?tag=physicshobbie-21"
    price: 79.99
    rating: 4.3
    reviews: 331
    specs: ["no disponible", "no disponible", "β, γ y X"]
    highlight: "A 79,99€ con 4.3 sobre 331 reseñas, es el único del grupo fuera de las marcas GQ y AEGTEST. Su ficha presume de «Alta Sensibilidad Precisión» sin una sola cifra detrás, que es justo el patrón que conviene reconocer antes de comprar."

pitfalls:
  - claim: "«Alta sensibilidad» o «alta precisión»"
    reality: "Sensibilidad en un contador Geiger es una cifra concreta: CPM por µSv/h, o CPM por unidad de actividad para un isótopo dado. Sin ese número, «alta» no se puede comparar con nada, ni siquiera con otro aparato del mismo listado."
  - claim: "«Detecta beta, gamma y rayos X»"
    reality: "Es cierto y a la vez incompleto en las seis fichas que lo dicen. Lo que decide qué beta detectas es el espesor de la pared del tubo, y ninguna ficha declara el tipo de tubo. Un cilíndrico de vidrio frena la beta blanda antes de que entre al gas."
  - claim: "Una lectura en µSv/h es una medida de dosis"
    reality: "Es una tasa de dosis estimada a partir de un conteo, usando un factor de conversión que supone una energía de fotón concreta. Lo que recibes tú es la dosis acumulada, o sea esa tasa integrada en el tiempo, y solo una de las siete fichas menciona µSv acumulados."
  - claim: "«Producto de Estándar Nacional de EE.UU.»"
    reality: "La ficha no cita norma ni organismo. Un estándar sin número de norma no es verificable, y para radioprotección lo que valdría es un certificado de calibración trazable, que aquí no ofrece ninguno."
  - claim: "Los resultados de búsqueda de «contador Geiger» son todos contadores Geiger"
    reality: "No. En este mismo grupo de resultados aparece un módulo de tubo Miller para montar uno mismo, descrito como «kit ensamblado, módulo experimental». Es un componente para un proyecto de electrónica, no un instrumento listo para usar, y el precio bajo hace fácil confundirlo."

verdicts:
  - profile: "Quieres saber qué está midiendo el aparato, no solo ver un número en pantalla"
    pick: "AEGTEST Radar-5633 (B0DT5TKH6P)"
    why: "Es el único cuya ficha enumera las cuatro magnitudes de la pantalla, CPM incluido, y el único que menciona dosis acumulada en µSv. Es la ficha menos opaca del grupo, que no es lo mismo que decir que sea el mejor aparato."
  - profile: "Vas a vigilar el fondo ambiental a lo largo del tiempo"
    pick: "GQ GMC-800 (B0CKM8NML7) o FS5000 (B0D3PX1W5B)"
    why: "Son los dos únicos que declaran alguna forma de volcado a ordenador. El GMC-800 lo plantea como registrador con compartición y llega respaldado por 1211 reseñas; el FS5000 habla de software de PC y cuesta 20€ menos."
  - profile: "Necesitas una medida defendible ante un organismo o para radioprotección"
    pick: "ninguno de los siete tal cual"
    why: "Sin certificado de calibración trazable ni isótopo de referencia declarado, la cifra no es defendible. Si aun así compras aquí, pide al vendedor la hoja de calibración antes y no después."
  - profile: "Prefieres la opción con más usuarios detrás aunque la ficha diga poco"
    pick: "GQ GMC-500+ (B071JWB7TJ)"
    why: "1824 reseñas con 4.6 es el mayor respaldo del grupo, a cambio del precio más alto (157€) y de una ficha que no declara unidades, sensibilidad ni tubo."
---

Todos estos aparatos hacen físicamente lo mismo, y conviene tenerlo claro antes de mirar precios. Dentro hay un tubo lleno de gas a baja presión con un hilo central a varios cientos de voltios. Cuando una partícula o un fotón ionizante atraviesa el gas y arranca un electrón, el campo eléctrico acelera ese electrón hasta que ioniza a su vez, y en microsegundos se desencadena una avalancha que el circuito lee como un pulso. El tubo no sabe qué tipo de radiación ha entrado, ni con cuánta energía: solo sabe que ha entrado algo. Cuenta pulsos, y nada más.

De ahí sale la única medida cruda que existe en estos aparatos, las cuentas por minuto. Todo lo demás que aparezca en la pantalla es aritmética hecha sobre ese conteo. Los µSv/h salen de multiplicar los CPM por un factor de conversión, y ese factor no es una constante universal: depende de la energía de los fotones y de la geometría del tubo. El convenio del sector es calibrarlo con cesio-137, cuyo gamma está en 661,7 keV, de modo que la cifra es razonable cerca de esa energía y se va desviando conforme te alejas de ella. Los CPM, mientras tanto, siguen siendo un conteo real pase lo que pase.

Por eso la columna que importa de la tabla es la primera, y por eso está casi vacía. Seis de las siete fichas no dicen en qué unidad muestran la lectura, y ninguna de las siete dice contra qué isótopo se calibró la conversión. No es un descuido de Amazon: es que ese dato no vende, y el que sí vende («alta sensibilidad», «precisión», «estándar nacional») no se puede comprobar. La ficha menos opaca del grupo resulta ser también la más barata, lo cual dice bastante sobre la relación entre precio y transparencia en esta categoría.

Queda un segundo hueco igual de grande: el tipo de tubo. Un tubo cilíndrico con pared de vidrio detecta gamma con soltura, pero frena la radiación beta de baja energía antes de que llegue al gas. Un tubo pancake con ventana fina de mica deja pasar esa beta blanda e incluso alfa. Son dos instrumentos distintos para dos trabajos distintos, y los seis títulos que anuncian «beta, gamma y rayos X» no distinguen entre ellos. Si lo que quieres es comprobar contaminación superficial en una pieza concreta y no vigilar el fondo ambiental, esa es la pregunta que hay que hacerle al vendedor antes de pagar.

Y una advertencia sobre el propio listado de Amazon: entre los resultados de «contador Geiger» aparecen módulos de tubo para montar uno mismo, descritos como kit ensamblado o módulo experimental. Son componentes para un proyecto de electrónica, sin carcasa, sin pantalla calibrada y sin nada que convierta pulsos en una lectura interpretable. Como proyecto están muy bien y de hecho enseñan justo lo que cuenta este artículo. Como instrumento de medida, no lo son.
