---
title: "Por qué 45 W no es una cifra del power bank sino un acuerdo con tu móvil"
pubDate: 2026-09-07
description: "Los 45 W de la caja solo existen si tu móvil, el cable y la batería pactan un voltaje. Cuando no lo hacen, cargas a 15 W sin enterarte."
category: "electrónica"
image: "/images/blog/2026-09-07-por-que-45-w-no-es-una-cifra-del-power-bank-sino-un-acuerdo-con-tu-movil.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0DSPVDYQ9?tag=physicshobbie-21"
productName: "UGREEN Nexode 45W Power Bank 20000mAh Batería Externa Portátil"
---

Conectas el portátil a una batería externa que anuncia 45 W, aparece el icono de carga, y aun así el porcentaje sigue bajando mientras trabajas. No hay nada roto: lo más probable es que se hayan pactado 15 W, y 15 W no compensan lo que consumen pantalla y procesador juntos. El número de la caja no describe lo que sale por el puerto; describe el máximo que el power bank está dispuesto a ofrecer si el otro lado sabe pedirlo.

Un cargador USB-C no impone un voltaje: lo negocia. Al conectar, la fuente anuncia los perfiles que puede dar —5 V, 9 V, 15 V, 20 V— y el dispositivo elige el más alto que soporta. La potencia es $P = V \cdot I$, y ahí está la trampa: por un cable USB-C sin chip identificador la corriente se limita a 3 A. Con 3 A, 5 V dan 15 W, 9 V dan 27 W, y para llegar a 45 W hacen falta al menos 15 V. Si tu dispositivo solo acepta 9 V, los 45 W declarados son inalcanzables aunque la batería los tenga. La capacidad en mAh es otro asunto, y ya lo cuento en [por qué tu power bank de 20000 mAh nunca carga 20000 mAh reales](/blog/2026-08-23-por-que-tu-power-bank-de-20000mah-nunca-carga-20000mah-reales/): aquella es una historia de energía; esta es de potencia.

El error habitual es mirar solo los vatios del power bank. Lo que fija la velocidad es el perfil más alto que **los dos extremos** compartan, y el cable tiene voto: uno de 3 A limita a 45 W incluso a 15 V, y solo uno con chip e-marker para 5 A permite subir a 100 W. Antes de culpar a la batería, comprueba qué admite tu dispositivo: muchos móviles se quedan en 9 V y jamás pedirán más. Y si cargas dos aparatos a la vez, cómo se reparte la potencia entre puertos es una decisión del fabricante que casi nunca viene en la ficha.

**Prueba rápida:**
1. Carga tu dispositivo con el power bank y abre una app que muestre el voltaje y la corriente de carga (en Android hay varias; algunos móviles lo enseñan en los ajustes de batería).
2. Multiplica voltaje por corriente. Si salen 15 W de un cargador de 45, no se ha negociado el perfil alto.
3. Repite con otro cable USB-C. Si la cifra cambia, el cuello de botella era el cable.
4. Repite con otro dispositivo. Si solo uno alcanza los 45 W, el límite lo ponía el que se quedaba corto, no la batería.

Según su ficha, este UGREEN Nexode declara 45 W, un cable USB-C integrado y dos puertos más, uno USB-C y uno USB-A, y se anuncia como cargador de PC. Lo que la ficha no declara es justo lo que este artículo dice que importa: qué perfiles de voltaje ofrece, si esos 45 W son de un solo puerto o el total repartido, y si el cable integrado está preparado para 3 A o para 5 A. Con un cable fijo esa última duda ya no la resuelves cambiando de cable, así que conviene saberlo antes de comprar. Que el dato no esté no significa que falle; significa que no puedes contar con él.

---

**¿Comparando modelos?** En [Power bank 20000mAh: potencia (W) o cable USB-C](/blog/2026-08-24-power-bank-20000mah-potencia-w-o-cable-usb-c/) analizo varias fichas de este tipo de producto y qué dato de la ficha decide la compra.
