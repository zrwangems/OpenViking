---
type: simulink-block
title: 'AXI4-Stream IIO Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4streamiiowrite'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4streamiiowrite.html'
language: en
---

# AXI4-Stream IIO Write

## Ports

### Input

### **Data** — Data frame to DMA buffer *N*-by-1 array

This port outputs the *N*-by-1 vector written to memory in the
DMA buffer transfer. This port is unnamed until the **Valid** port is
enabled.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Valid** — Status of stream write to IP core scalar

This port outputs a validation flag indicating a successful write of the data to
the IP core, where `1` indicates a successful write.

#### Dependencies

To enable this port, set **Data timeout (seconds)** to a finite
value.

**Data Types:** `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **IIO device name** — File name of IP core device `mwipcore0:mm2s0` (default) | character array

Enter the name and channel of the IP core on the FPGA as a colon separated list. If
you are using HDL Coder™ to generate the IP core, HDL Coder maps the IP core to `mwipcore0` and uses channel
`mm2s0`. For more information on getting IIO device names and
channels, see Tips.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `devName` |

### **Data timeout (seconds)** — Timeout for DMA stream read `Inf` (default) | positive scalar

Specify the maximum timeout delay for the DMA stream write.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataTimeout` |

## Libraries

Embedded Coder Support Package for AMD SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Write AXI4-Stream Data using IIO

This block writes data to the direct-memory-access (DMA) buffer of the specified
AXI4-Stream IP core device by using the Industrial I/O (IIO) library drivers. The
AXI4-Stream IIO Write block enables low-latency, high-throughput data
transmission from your model on the processor to the IP core on the FPGA.
