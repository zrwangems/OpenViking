---
type: simulink-block
title: 'C28x GPIO Digital Output'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'gpiodigitaloutput'
documentation_source_path: 'ref/gpiodigitaloutput.html'
language: en
---

# C28x GPIO Digital Output

## Ports

### Input

### **Input** — Set the GPIO pin status scalar | vector

The input port to set the GPIO pin status.

## Parameters

### **GPIO Group** — GPIO pins you want to configure `GPIO0-GPIO7` (default) | `GPIO8-GPIO15``GPIO16-GPIO23``…`

Select the group of GPIO pins you want to view or configure. For a
table of GPIO pins and peripherals, refer to the Texas Instruments
documentation for your specific target.

### **GPIO pins for output** — GPIO pins you want to configure `GPIO0` (default) | `GPIO8``GPIO16``…`

To configure a GPIO pin for digital output, select the check box next
to it. Refer to the block for a table of all available peripherals for
each pin.

A value of True at the input of the block drives the selected GPIO pin
high. A value of False at the input of the block grounds the selected
GPIO pin.

### **Toggle GPIO#** — GPIO pins you want to configure `Toggle GPIO0` (default) | `Toggle GPIO1``…`

For each pin selected for output, you can elect to toggle the signal
of that pin. In **Toggle** mode, a value of
`True` at the input of the block switches the GPIO
pin output level. Thus, if the GPIO pin was driven high, in
**Toggle** mode, with the value of
`True` at the input, the pin output level is driven
low. If the GPIO pin was driven low, in **Toggle**
mode, with the value of `True` at the input of the
block, the same pin output level is driven high. If the input of the
block is `False`, the GPIO pin output level is
unaffected.

**Note**

The outputs of this block can be vectorized.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Configure general-purpose input/output pins as digital output

This block configures the general-purpose I/O (GPIO) MUX registers that control
the operation of GPIO shared pins for digital input. Each I/O port has one MUX
register that selects peripheral operation or digital I/O operation (the default).
When a pin is configured for digital input, it becomes unavailable for digital
output or peripheral operation. You can configure the **Input qualification
type** for individual digital input pins. To configure, go to
**Configuration Parameters > Hardware Implementation > Target
Hardware Resources** and select the appropriate GPIO group.

Each processor has a different number of available GPIO pins.

**Note**

To avoid losing new settings, click **Apply** before
changing the **GPIO Group** parameter.
