---
title: "Ruido y señal: la física del apilado en astrofotografía"
pubDate: 2026-10-22
description: "Cada foto que tomas de una galaxia esconde más ruido que señal, y apilar cientos de exposiciones es la única forma de ganarle la partida."
category: "óptica"
image: "/images/blog/2026-10-22-ruido-y-senal-la-fisica-del-apilado-en-astrofotografia.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0GYX9GSVX?tag=physicshobbie-21"
productName: "ZWO Seestar - Telescopio inteligente S30 Pro"
---

Apuntas tu cámara a una nebulosa débil, disparas una exposición de 10 segundos y lo que ves en la pantalla es un borrón grisáceo con puntitos de colores que no se parecen a nada. Subes el tiempo de exposición y aparece el problema contrario: la Tierra gira, las estrellas se alargan en rayas y la imagen se vuelve inservible sin una montura que siga el cielo con precisión de segundos de arco. Este dilema —exposiciones cortas sin señal o exposiciones largas con rastro— es el que resuelve el apilado automático, y detrás de él hay una ley estadística muy simple.

La luz que llega de un objeto débil no fluye de forma continua: llega en fotones discretos, y su llegada sigue estadística de Poisson. Eso significa que el ruido de fondo de una imagen no es fijo, crece con la raíz cuadrada del número de fotones capturados. Si tomas $N$ exposiciones idénticas y las sumas, la señal útil crece de forma lineal ($N$ veces), pero el ruido aleatorio crece solo como $\sqrt{N}$. La relación señal-ruido mejora entonces según $SNR \propto \sqrt{N}$: apilar 100 fotos no te da 100 veces menos ruido, te da 10 veces menos. Es una ganancia real, pero con rendimientos decrecientes.

Aquí está el matiz que casi nadie calibra bien: no todo el ruido es fotónico. El sensor añade ruido de lectura cada vez que se descarga, y corriente oscura que se acumula con el tiempo y la temperatura. Por eso el software de apilado no suma exposiciones a lo bruto: resta primero fotogramas de oscuridad (dark frames) tomados con el objetivo tapado, aplica rechazo por sigma-clipping para eliminar rayos cósmicos o el paso de un satélite, y alinea cada subfotograma antes de sumarlo porque el objeto se ha movido unos píxeles entre disparo y disparo. Elegir exposiciones demasiado cortas te obliga a apilar miles de fotogramas con mucho ruido de lectura cada uno; elegir exposiciones demasiado largas satura el núcleo de las estrellas brillantes. El punto óptimo suele estar entre 10 y 30 segundos para telescopios de apertura pequeña, ajustado según la contaminación lumínica de tu cielo.

Puedes comprobarlo sin salir de casa en cinco minutos: 1) apunta cualquier cámara (o el propio Seestar) a una zona de cielo con poca luz, aunque sea con nubes finas. 2) Captura una sola exposición de 10 segundos y guárdala sin procesar. 3) Deja que el sistema acumule automáticamente 40 o 50 exposiciones apiladas. 4) Amplía ambas imágenes al 100% en la misma zona oscura del fondo: en la primera verás grano grueso y aleatorio, en la segunda un fondo mucho más uniforme, aunque el objeto en sí no haya cambiado de brillo real.

El ZWO Seestar S30 Pro automatiza justo este proceso: su app hace el seguimiento GoTo, dispara las subexposiciones, resta el ruido térmico y apila en vivo mientras observas la imagen mejorar en la pantalla del móvil. Su apertura de 30 mm sigue siendo una apertura pequeña —recoge menos fotones por segundo que un telescopio de 150 mm— así que el apilado compensa parte de esa limitación pero no la elimina: para objetos muy débiles seguirás necesitando más tiempo total de integración, no solo más fotogramas.

Conviene saber que el apilado no sustituye a la apertura: multiplicar exposiciones mejora la relación señal-ruido, pero el detalle que el objetivo no resuelve no aparece por acumular fotogramas. Qué apertura necesitas según lo que quieras mirar está en [telescopio astronómico: elige por apertura y montura](/blog/2026-10-11-telescopio-astronomico-elige-por-apertura-y-montura/).
