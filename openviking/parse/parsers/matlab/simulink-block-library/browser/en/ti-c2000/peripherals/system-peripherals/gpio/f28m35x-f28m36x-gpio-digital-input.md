---
type: simulink-block
title: 'F28M35x/F28M36x GPIO Digital Input'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'f28m35xf28m36xgpiodigitalinput'
documentation_source_path: 'ref/f28m35xf28m36xgpiodigitalinput.html'
language: en
---

# F28M35x/F28M36x GPIO Digital Input

## Ports

### Output

### **Pin #** — GPIO pin status scalar | vector

The port outputs the status of the digital pin you select in the **Pin
number** parameter.

**Data Types:** `Boolean`

## Parameters

### **GPIO port** — Port to read GPIO pin status `GPIOA` (default) | `GPIOB``GPIOC``…`

Select one of GPIO ports to get the GPIO pin status.

### **Pin number** — GPIO pin whose status you want to read `Pin 0` (default) | `Pin 1` | `Pin 2` | `...`

Select the pin number of the GPIO pin whose status you want to read.

### **Sample time** — Frequency at which block reads input pin values `-1` (default) | `0.1`

Specify how often the block receives message, in seconds. When you specify this
parameter as -1, Simulink determines the best sample time for the block based on the
block context within the model.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Read the logical value of a GPIO pin configured as input

Read the logical value of a configured GPIO pin.

This block configures the general-purpose I/O (GPIO) MUX registers that control the
operation of GPIO shared pins for digital input. Each I/O port has one MUX register that
selects peripheral operation or digital I/O operation (the default). When a pin is
configured for digital input, you cannot use the same pin for digital output or peripheral
operation. You can configure the pull-up and the open-drain options for the individual
digital input pins. To configure, go to **Configuration Parameters > Hardware
Implementation > Target Hardware Resources** and select the appropriate GPIO
group.
