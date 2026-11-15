---
type: simulink-block
title: 'GPIO Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'gpioread'
documentation_source_path: 'beaglebone/ref/gpioread.html'
language: en
---

# GPIO Read

## Ports

### Output

### **Port\_1** — Output port containing logical value scalar

The block outputs the logical value of a digital pin.

**Data Types:** `Boolean`

## Parameters

### **GPIO number** — GPIO pin of BeagleBone® hardware board `P9_11` (default) | `P8_10` | `P8_11` | `P8_12` | `P8_13` | `P8_14` | `P8_15` | `P8_16` | `P8_17` | `P8_18` | `P8_19` | `P8_20` | `P8_21` | `P8_22` | `P8_23` | `P8_24` | `P8_25` | `P8_26` | `P8_27` | `P8_28` | `P8_29` | `P8_3` | `P8_30` | `P8_31` | `P8_32` | `P8_33` | `P8_34` | `P8_35` | `P8_36` | `P8_37` | `P8_38` | `P8_39` | `P8_4` | `P8_40` | `P8_41` | `P8_42` | `P8_43` | `P8_44` | `P8_45` | `P8_46` | `P8_5` | `P8_6` | `P8_7` | `P8_8` | `P8_9` | `P9_11` | `P9_12` | `P9_13` | `P9_14` | `P9_15` | `P9_16` | `P9_17` | `P9_18` | `P9_19` | `P9_20` | `P9_21` | `P9_22` | `P9_23` | `P9_24` | `P9_25` | `P9_26` | `P9_27` | `P9_28` | `P9_29` | `P9_30` | `P9_31` | `P9_41` | `P9_42`

Select a GPIO pin of the BeagleBone hardware board to read its logical status. Do not use the same GPIO pin in
multiple blocks within the Simulink® model. For more information on BeagleBone GPIO pins, click **View pin map**.

### **Sample time** — Time interval to read logical status on GPIO pin `0.1` (default) | scalar

Enter the sample time to reading the logical value of the GPIO pin. Smaller values
require the processor to complete the same number of instructions in less time, which
can cause task overruns. Enter a value greater than zero.

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Read logical value of GPIO pin configured as input

Use this block to:

- Create a physical input from a GPIO pin.
- Read the logical value of the GPIO pin at intervals that are determined by
  **Sample time**.
- Send the logical value to other blocks in the model as a stream of Boolean
  values.
- The maximum input voltage of the GPIO pin is 1.8 V.

**Caution**

You can damage your target hardware by:

- Shorting a GPIO pin to ground.
- Shorting a GPIO pin with high voltage to another GPIO pin with low voltage.
- Connecting a GPIO pin to a voltage source greater than the maximum voltage.
- Exceeding the maximum current by driving multiple GPIO pins high simultaneously.
