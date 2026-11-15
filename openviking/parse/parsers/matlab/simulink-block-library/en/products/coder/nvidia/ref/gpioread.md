---
type: simulink-block
title: 'GPIO Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Basic'
documentation_page: 'gpioread'
documentation_source_path: 'nvidia/ref/gpioread.html'
language: en
---

# GPIO Read

## Ports

### Output

### **output** — GPIO pin state 0 | 1

Logical state of an input pin at intervals that are determined by **Sample
time**.

**Data Types:** `Boolean`

## Parameters

### **Board** — Target board name `NVIDIA Jetson TX1` (default) | `NVIDIA Jetson TX2` | `NVIDIA Jetson Nano` | `NVIDIA Jetson AGX Xavier` | `NVIDIA Jetson Xavier NX`

Specify the name of the target board. This selection
affects the pins available for general purpose input
and output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Board` |
| **Type:** character vector, string |
| **Values:** `'NVIDIA Jetson TX1'`|`'NVIDIA Jetson TX2'`|`'NVIDIA Jetson Nano'`|`'NVIDIA Jetson AGX Xavier'`|`'NVIDIA Jetson Xavier NX'` |
| **Default:**  `'NVIDIA Jetson TX1'` |

### **GPIO number** — GPIO pin to read the logical status 0 (default) | scalar

Select a GPIO pin to read the logical status.

To open the pin mapping table, click **View pin map**. Make sure to
assign different pin numbers to the different blocks of your model.

### **Sample time (seconds)** — Time frequency at which block receives data `0.1` (default) | `scalar`

Specify how often the block should read the port buffer. Enter a value greater than
`0` or `-1` (for inherited sample time).

When you specify this parameter as-1, Simulink® determines the best sample time for the block based on the block context
within the model.

This value defaults to a sample time of `0.1` seconds. Smaller
values require the processor to complete the same number of instructions in less time
and this can cause task overruns.

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Read logical state of an input pin

Use this block to:

- Create a physical input from a GPIO pin.
- Read the logical value of the GPIO pin at intervals that are determined by
  **Sample time**.
- Send the logical value to other blocks in the model as a stream of boolean
  values.

**Warning**

You can damage your target hardware by:

- Shorting a GPIO pin to ground.
- Shorting a GPIO pin with high voltage to another GPIO pin with low voltage.
- Connecting a GPIO pin to a voltage source greater than the maximum voltage.
- Exceeding the maximum current by driving multiple GPIO pins high simultaneously.
