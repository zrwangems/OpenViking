---
type: simulink-block
title: 'AXI4-Interface Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4interfaceread'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4interfaceread.html'
language: en
---

# AXI4-Interface Read

## Ports

### Output

### **Port\_1** — Data vector from IP core registers *N*-by-1 vector

The *N*-by-1 vector read from memory-mapped registers on the IP
core, starting from the **Register offset**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **Device name** — Path and name of IP core device `/dev/mwipcore` (default) | character array

Enter the path and name of the IP core.

**Note**

If you use HDL Coder to generate the IP core, HDL Coder maps the IP core to `/dev/mwipcore`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DeviceName` |

### **Register offset** — Offset of register from base address of IP core `hex2dec( '0104' )` (default) | decimal number

Enter the offset of the register from the base address of the IP core. The block
reads data from this register. Use the `hex2dec` function when you specify the address offset using a hexadecimal
number character vector.

**Note**

If you use HDL Coder to generate the IP core, you can get the value of the address offset
from the Register Address Mapping section of the Custom IP Core Report (HDL Coder). For more information, see Register Address Mapping (HDL Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RegisterOffset` |

### **Output vector size** — Size of data vector to be read from IP core `1` (default) | positive integer

Enter the size of the data vector to be read from the IP core device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataLength` |

### **Data type** — Data type of IP core `uint16` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32` | `boolean`

Select the data type used by the IP core.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |

### **Sample time** — Sample time in seconds `0.001` (default) | positive scalar

The signal data output by the AXI4-Interface Read block polls
directly from the IP core using the AXI4-Lite protocol. The **Sample
time** parameter value or the base rate of the subsystem specifies the
polling rate of the registers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |

## Libraries

Embedded Coder Support Package for AMD SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Read data from IP core on AMD SoC Device

This block reads a data vector from a contiguous group of memory-mapped registers on an
HDL Coder™ generated IP core. The AXI4-Interface Read block, using the
central interconnect of the processing system, provides simple memory-mapped communication
with the IP core on the FPGA. This block is best suited for low-throughput communication, such
as inspecting status, state, or control registers.
