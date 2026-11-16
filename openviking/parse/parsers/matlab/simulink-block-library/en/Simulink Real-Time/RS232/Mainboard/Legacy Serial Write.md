---
type: simulink-block
title: 'Legacy Serial Write'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232 / Mainboard'
documentation_page: 'legacyserialwrite'
documentation_source_path: 'io_ref/legacyserialwrite.html'
language: en
---

# Legacy Serial Write

## Ports

### Input

### **Input** — Data for serial port write serial data

The Input port contains the data to write for the serial port.

## Parameters

### **Serial port** — Port that is being accessed `Legacy Serial Port 1` (default) | .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

Specify the serial port for communications.

If using USB-to-serial adapters, the target computer
detects these adapters as `serusb1`, `serusb2`, and so
on in the order that the adapters are connected to the serial devices.

The order of port assignment is retained through the power cycle of the target
computer or serial device if there is no change in the connections to the ports.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `port` |

### **Output Datatype** — Select output data type `8 bit uint null terminated` (default) | `8 bit int null terminated` | `count+16 bit uint` | `count+16 bit int` | `count+32 bit uint` | `count+32 bit int`

Use this value to select the output data type.

#### Programmatic Use

```
dtype
```

### **SampleTime** — Select sample time in seconds `.01` (default) | double

Use this value to select the sample time in seconds.

#### Programmatic Use

```
sampletime
```

## Libraries

Simulink Real-Time / RS232 / Mainboard

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2021b: USB to Serial for RS232 Blocks

The RS232 mainboard blocks support connecting USB serial adapter ports. The
`Serial port` parameter of the Legacy Serial Read
block, Legacy Serial Write block, Legacy Serial Setup block,
Legacy Serial Port block, and Legacy Serial Port F block
means that you can select a `USB Serial Port` or a
`Legacy Serial Port`.

## Description

Write output data for baseboard serial communications

The Legacy Serial Write block writes output data for baseboard serial
communications on the Speedgoat® target computer.

For more information, see RS-232 Serial Communication and RS-232 Legacy Drivers.
