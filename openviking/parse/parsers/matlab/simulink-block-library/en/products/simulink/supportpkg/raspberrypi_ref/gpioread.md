---
type: simulink-block
title: 'GPIO Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'gpioread'
documentation_source_path: 'supportpkg/raspberrypi_ref/gpioread.html'
language: en
---

# GPIO Read

## Ports

### Output

### **Port\_1** — Output port containing logical value scalar

The block outputs the logical value of a digital pin.

**Data Types:** `Boolean`

## Parameters

### **Board** — Raspberry Pi hardware board `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

Select your Raspberry Pi hardware board. You can find this information on the target hardware,
product packaging, or product documentation.

### **GPIO number** — GPIO pin of Raspberry Pi hardware board `17` (default) | `4` | `27` | `22` | `10` | `9` | `11` | `14` | `15` | `18` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

Select a GPIO pin of the Raspberry Pi hardware board to read its logical status. Do not use the same GPIO pin in
multiple blocks within the Simulink® model. For more information on Raspberry Pi GPIO pins, click **View pin map**.

### **Sample time** — Time interval to read logical status on GPIO pin `0.1` (default) | scalar

Enter the sample time to reading the logical value of the GPIO pin. Smaller values
require the processor to complete the same number of instructions in less time, which
can cause task overruns. Enter a value greater than zero.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Read GPIO pin status

Use the GPIO Read block to read the logical value of a digital pin of your
Raspberry Pi® board.

**Warning**

You can damage your target hardware by:

- Exceeding the maximum voltage that can be applied to GPIO pins.
- Shorting a GPIO pin to ground.
- Shorting a GPIO pin with high voltage to another GPIO pin with low voltage.
- Connecting a GPIO pin to a voltage source greater than the maximum voltage.
- Exceeding the maximum current by driving multiple GPIO pins high simultaneously.
