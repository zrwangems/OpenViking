---
type: simulink-block
title: 'AXI4-Interface Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4interfacewrite'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4interfacewrite.html'
language: en
---

# AXI4-Interface Write

## Ports

### Input

### **Port\_1** — Input signal to IP core registers *N*-by-1 vector

Specify the *N*-by-1 vector written to memory-mapped registers on
the IP core, starting at **Register offset**.

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

### **Device name** — Path and name of IP core device `/dev/mwipcore` (default) | character array

Enter the path and name of the IP core.

**Note**

If you use HDL Coder to generate the IP core, HDL Coder maps the IP core to `/dev/mwipcore`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DeviceName` |

### **Register offset** — Offset of register from base address of IP core `hex2dec( '010C' )` (default) | decimal number character array

Enter the offset of the register from the base address of the IP core. The block
writes data to this register. When you use a hexadecimal number character vector to
specify the address offset, represent the value as an argument inside the `hex2dec` function.

**Note**

If you use HDL Coder to generate the IP core, you can get the value of the address offset
from the “Register Address Mapping” section of the Custom IP Core Report (HDL Coder). For more information, see Register Address Mapping (HDL Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RegisterOffset` |

## Libraries

Embedded Coder Support Package for AMD SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Write data to IP core on AMD SoC Device

This block writes a data vector to a contiguous group of memory-mapped registers on an
HDL Coder™ generated IP core. The AXI4-Interface Write block, using the
central interconnect of the processing system, provides simple memory-mapped communication
with the IP core on the FPGA. This block is best suited for low-throughput communication, such
as setting status, state, or control registers. This diagram shows the path of the data after
it leaves this block.
