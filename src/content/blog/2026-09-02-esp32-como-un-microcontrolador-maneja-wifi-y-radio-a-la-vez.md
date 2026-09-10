---
title: "ESP32: cómo un microcontrolador maneja WiFi y radio a la vez"
pubDate: 2026-09-02
description: "Un chip que hace de puente entre tus sensores y la nube, con dos núcleos y radio integrada por menos de lo que cuesta una placa Arduino con shield WiFi aparte."
category: "electrónica"
image: "/images/blog/2026-09-02-esp32-como-un-microcontrolador-maneja-wifi-y-radio-a-la-vez.jpg"
tags: ["ciencia", "hobbies", "divulgación"]
amazonUrl: "https://www.amazon.es/dp/B0CTMQQ1W4?tag=physicshobbie-21"
productName: "LAFVIN Kit básico de inicio para placa de desarrollo ESP32"
---

Tienes un Arduino Uno funcionando perfecto en el escritorio, pero en cuanto quieres que ese sensor de temperatura mande datos a tu móvil o a un servidor, te topas con el mismo muro: necesitas un módulo WiFi aparte, cableado extra y librerías que no siempre se llevan bien entre sí. Es el típico salto de complejidad que frena a mucha gente que empieza en IoT casero.

El ESP32 resuelve esto porque integra en un solo chip lo que antes eran piezas separadas: un microcontrolador de doble núcleo (normalmente a 240 MHz), radio WiFi 802.11 b/g/n y Bluetooth clásico y BLE. La clave física está en que la radio y el procesamiento comparten silicio, así que las señales digitales que generas en tu código se convierten directamente en ondas electromagnéticas moduladas a 2.4 GHz, la misma banda que usa tu router doméstico. La potencia de transmisión ronda los 20 dBm (unos 100 mW), suficiente para cubrir una casa pequeña pero no para atravesar varias paredes de hormigón sin perder señal, algo que conviene tener en cuenta si planeas colocar el módulo en un sótano o detrás de electrodomésticos metálicos.

Donde más se equivocan los principiantes es en la alimentación: el ESP32 consume picos de hasta 500 mA durante la transmisión WiFi, y si lo alimentas solo por el pin de 3.3V de un programador USB barato, vas a ver reinicios aleatorios que parecen fallos de código pero son caídas de tensión. Usa siempre una fuente capaz de entregar al menos 1A de forma estable, y si trabajas con baterías, añade un capacitor de al menos 100 µF cerca del regulador de la placa para amortiguar esos picos.

**Prueba rápida (5 minutos):**
1. Conecta el ESP32 al PC y abre el Arduino IDE con el core de ESP32 instalado.
2. Carga el ejemplo `WiFiScan` de la librería WiFi.h.
3. Abre el monitor serie a 115200 baudios.
4. Observa cuántas redes detecta y con qué intensidad de señal (RSSI); si tu propia red aparece por debajo de -70 dBm, sabrás que necesitas acercar el módulo o replantear la ubicación de tu proyecto final.

Este kit de LAFVIN incluye la placa ESP32-S junto con componentes básicos (resistencias, LEDs, algún sensor) y un tutorial en PDF, pensado para quien viene de Arduino y quiere dar el salto a proyectos conectados sin comprarse veinte piezas sueltas por separado. No esperes documentación tan pulida como la oficial de Espressif, pero cubre lo esencial para los primeros diez o quince proyectos de aprendizaje.

---

**¿Comparando modelos?** En [Kit Arduino: qué placa y accesorios incluye decide](/blog/2026-08-24-kit-arduino-que-placa-y-accesorios-incluye-decide/) analizo varias fichas de este tipo de producto y qué dato de la ficha decide la compra.
