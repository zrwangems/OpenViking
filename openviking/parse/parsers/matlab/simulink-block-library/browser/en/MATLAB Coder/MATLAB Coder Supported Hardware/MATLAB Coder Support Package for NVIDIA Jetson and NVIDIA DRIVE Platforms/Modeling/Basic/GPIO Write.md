---
type: simulink-block
title: 'GPIO Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Basic'
documentation_page: 'gpiowrite'
documentation_source_path: 'nvidia/ref/gpiowrite.html'
language: en
---

# GPIO Write

## Ports

### Input

### **Port\_1** — Set the GPIO pin status scalar

The input port to set the GPIO pin status.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

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

### **GPIO number** — GPIO pin to write the logical status 0 (default) | scalar

Select a GPIO pin to write the logical status.

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

Set logical state of an output pin

Use this block to:

- Create a physical output to a GPIO pin.
- Receive the logical value from other blocks in the model as a stream of boolean
  values.
- Write the logical value to a GPIO pin at intervals that are determined by
  **Sample time**.

**Warning**

You can damage your target hardware by:

- Shorting a GPIO pin to ground.
- Shorting a GPIO pin with high voltage to another GPIO pin with low voltage.
- Connecting a GPIO pin to a voltage source greater than the maximum voltage.
- Exceeding the maximum current by driving multiple GPIO pins high simultaneously.
