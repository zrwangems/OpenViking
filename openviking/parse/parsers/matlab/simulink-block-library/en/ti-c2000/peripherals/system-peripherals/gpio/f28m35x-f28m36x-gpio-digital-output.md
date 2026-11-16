---
type: simulink-block
title: 'F28M35x/F28M36x GPIO Digital Output'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'f28m35xf28m36xgpiodigitaloutput'
documentation_source_path: 'ref/f28m35xf28m36xgpiodigitaloutput.html'
language: en
---

# F28M35x/F28M36x GPIO Digital Output

## Ports

### Input

### **Pin #** — Status of GPIO pin scalar | vector

Specify a value at this port to set the status of GPIO pin(s).

**Data Types:** `Boolean`

## Parameters

### **GPIO port** — Port to write GPIO pin status `GPIOA` (default) | `GPIOB``GPIOC``…`

Select one of GPIO ports to which you want to write the GPIO pin status.

### **Pin number** — GPIO pin to write status `Pin 0` (default) | `Pin 1` | `Pin 2` | `...`

Select the pin number of the GPIO pin whose status you want to write.

### **Initially set GPIO pin** — GPIO pin status during model initialization `on` (default) | `off`

Select this option to set the GPIO pin status during model initialization.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Set the logical value of a GPIO pin configured as output

Set the logical value of the configured GPIO pin.

Configure individual general-purpose input/output (GPIO) pins to operate as digital
outputs. When a pin is configured for digital output, it cannot operate as a digital input
or connect to peripheral I/O signals.
