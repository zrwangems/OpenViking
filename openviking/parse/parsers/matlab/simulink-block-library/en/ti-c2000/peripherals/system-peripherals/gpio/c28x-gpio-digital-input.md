---
type: simulink-block
title: 'C28x GPIO Digital Input'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / GPIO'
documentation_page: 'gpiodigitalinput'
documentation_source_path: 'ref/gpiodigitalinput.html'
language: en
---

# C28x GPIO Digital Input

## Ports

### Output

### **Pin #** — GPIO pin status scalar | vector

The port outputs the status of the digital pin you select in the
**GPIO Group** parameter.

## Parameters

### **GPIO Group** — GPIO pins you want to configure `GPIO0-GPIO7` (default) | `GPIO8-GPIO15``GPIO16-GPIO23``…`

Select the group of GPIO pins you want to view or configure. For a
table of GPIO pins and peripherals, refer to the Texas Instruments
documentation for your specific target.

### **Sample time** — Frequency at which block reads input pin values `-1` (default) | `0.1`

Specify how often the block receives message, in seconds. When you
specify this parameter as -1, Simulink determines the best sample time
for the block based on the block context within the model.

For more information, refer to the section on Specify Sample Time.

### **Data type** — Data type of GPIO input `auto` (default) | `unit8` | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Specify the data type of the input. The input is read as 16-bit
integer, and then cast to the selected data type.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Configure general-purpose input/output pins as digital input

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
