---
type: simulink-block
title: 'AXI4 Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Intel SoC Devices / Modeling'
documentation_page: 'axi4read'
documentation_source_path: 'alterasoc/ref/axi4read.html'
language: en
---

# AXI4 Read

## Ports

### Output

### **Port\_1** — Output signal N-by-1 vector

The N-by-1 vector read from the registers on the IP core starting at
**Offset address** from the base address of the IP core.

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

### **Data type** — Data type used by IP core `'uint16'` (default) | `'single'` | `'double'` | `'int8'` | `'uint8'` | `'int16'` | `'int32'` | `'uint32'` | `'boolean'` | character vector

Enter the data type used by the IP core.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataType` |
| **Default:** `'uint16'` |

### **Output vector size** — Size of data vector from IP core `1` (default) | positive integer scalar

Enter the size of the data vector read from the IP core device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataLength` |
| **Default:** `1` |

### **Sample time** — Sample time `-1` (default)

Enter the sample time in seconds. This block polls the register on the IP core for
data. When  **Sample time** is set to `-1`, the base
rate of the subsystem that contains this block determines the polling frequency.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Default:** `-1` |

## Libraries

Embedded Coder Support Package for Intel SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Read data from IP core on target hardware through the AXI4-Lite interface

Use the AXI4-Lite interface to read a data vector from a contiguous group of registers on
the Programmable Logic IP Core into the embedded processor. The AXI4 Read block
supports only the AXI4-Lite protocol, allowing for simple, low-throughput memory-mapped
communication. Typical uses for this protocol include reading from control and status
registers.
