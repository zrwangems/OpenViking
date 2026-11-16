---
type: simulink-block
title: 'AXI4-Stream IIO Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4streamiioread'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4streamiioread.html'
language: en
---

# AXI4-Stream IIO Read

## Ports

### Output

### **Data** — Data frame from DMA buffer *N*-by-1 vector

This port outputs the *N*-by-1 vector received from the DMA
buffer transfer. Use the **Frame size** parameter to determine the
number of samples read for each DMA transfer. This port is unnamed until the
**Valid** port is enabled.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Valid** — Status of stream read from IP core `Boolean` value

This port outputs a validation flag indicating a successful read of the data from
the IP core, where `1` indicates a successful read.

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

### **IIO device name** — File name of IP core device `mwipcore0:s2mm0` (default) | character array

Enter the name and channel of the IP core on the FPGA as a colon separated list. If
you are using HDL Coder™ to generate the IP core, HDL Coder maps the IP core to `mwipcore0` and uses channel
`s2mm0`. For more information on getting IIO device names and
channels, see Tips.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `devName` |

### **Frame size** — Size of data vector to be read from IP core `1024` (default) | positive integer

Enter the size of the data vector to be read from the IP core device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SamplesPerFrame` |

### **Data type** — Data type of IP core `uint32` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32`

Select the data type used by the IP core.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `dataTypeStr` |

### **Sample time** — Sample time in seconds `0.1` (default) | positive scalar

The signal data output by the AXI4-Stream IIO Read blocks polls from the DMA buffer
using the AXI4-Stream protocol. The **Sample time** or base rate of the
subsystem specifies the polling rate of the DMA buffer.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |

### **Data timeout (seconds)** — Timeout for DMA stream read `Inf` (default) | positive scalar

Specify the maximum timeout delay for the DMA stream read.

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

Read AXI4-Stream Data using IIO

This block reads data from the direct-memory-access (DMA) buffer of the specified
AXI4-Stream IP core device by using the Industrial I/O (IIO) library drivers. The
AXI4-Stream IIO Read block enables you to achieve a low-latency,
high-throughput data transmission between your model deployed on the processor and the IP core
on the FPGA.
