---
type: simulink-block
title: 'AXI4 Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Intel SoC Devices / Modeling'
documentation_page: 'axi4write'
documentation_source_path: 'alterasoc/ref/axi4write.html'
language: en
---

# AXI4 Write

## Ports

### Input

### **Port\_1** — Input signal 1-D vector

The 1-D vector written to the registers on the IP core starting at
**Offset address** from the base address of the IP core.

**Data Types:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **Device name** — Path and filename of IP core device `/dev/mwipcore` (default) | character vector

Enter the path and filename of the IP core device.

**Note**

If you are using HDL Coder™ to generate the IP core, the IP core is mapped to
`/dev/mwipcore`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DeviceName` |
| **Default:** `/dev/mwipcore` |

### **Offset address** — Offset from base address of IP core to register `hex2dec( '0100' )` (default) | decimal number

Enter the offset from the base address of the IP core to the register. The block
reads data from this register. Use the `hex2dec` function when you specify the offset address using a hexadecimal
number expressed as a character vector.

**Note**

Using HDL Coder to generate the IP core, you can get the value of the offset address
from the Register Address Mapping portion of the Custom IP Report (HDL Coder). For more information, see
Register Address Mapping (HDL Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RegisterOffset` |
| **Default:** `hex2dec('0100')` |

## Libraries

Embedded Coder Support Package for Intel SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Write data to IP core on the target hardware through AXI4-Lite interface

Use the AXI4 interface to write vector data from the embedded processor to a contiguous
group of registers on the Programmable Logic IP Core. The AXI4 Write block
supports only the AXI4-Lite protocol, allowing for simple, low-throughput memory-mapped
communication. Typical uses for this protocol include writing to control and status
registers.

The sample rate of the block input signal controls how often this block writes data to the
register.
