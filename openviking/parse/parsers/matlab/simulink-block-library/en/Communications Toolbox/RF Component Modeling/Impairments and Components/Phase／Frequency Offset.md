---
type: simulink-block
title: 'Phase/Frequency Offset'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Impairments and Components'
documentation_page: 'phasefrequencyoffset'
documentation_source_path: 'ref/phasefrequencyoffset.html'
language: en
---

# Phase/Frequency Offset

## Ports

### Input

### **In** — Complex signal scalar | vector | matrix

Complex signal, specified as a scalar, vector, or matrix.

This port is unnamed on the block until you enable the **Frequency offset from
port** parameter.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes

### **Frq** — Frequency offset scalar | vector | matrix

Frequency offset, specified as a scalar, a vector with the same number of rows or
columns as the input signal, or a matrix with the same dimensions as the input signal. For
more information, see Interdependent Offset-I/O Dimensions.

#### Dependencies

To enable this port, select the **Frequency offset from port**
parameter.

**Data Types:** `double` | `single`
### Output

### **Out** — Output signal scalar | vector | matrix

Output signal, returned as a scalar, vector, or matrix. This output is the same
dimension and data type as the input signal.

This port is unnamed on the block.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Phase offset (deg)** — Phase offset `0` (default) | scalar | vector | matrix

Phase offset in degrees, specified as a scalar, vector, or matrix.

If **Phase offset (deg)** and **Frequency offset (Hz)**
are both nonscalar, they must be the same size.

**Tunable:** Yes

### **Frequency offset from port** — Option to add port to set frequency offset `off` (default) | on

Select this parameter to add the **Frq** port.

- When you select this parameter, the **Frq** port specifies the
  frequency offset.
- When you clear this parameter, the **Frequency offset (Hz)**
  parameter specifies the frequency offset.

### **Frequency offset (Hz)** — Frequency offset `0` (default) | scalar | vector | matrix

Frequency offset in hertz, specified as a scalar, a vector with the same number of rows
or columns as the input signal, or a matrix with the same dimensions as the input signal. For
more information, see Interdependent Offset-I/O Dimensions.

If **Phase offset (deg)** and **Frequency offset (Hz)**
are both nonscalar, they must be the same size.

**Tunable:** Yes

#### Dependencies

To enable this port, clear the **Frequency offset from port**
parameter.

## Libraries

Communications Toolbox / RF Impairments Correction Communications Toolbox / RF Impairments and Components

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The **Frequency offset (Hz)** and **Phase offset (deg)**
parameters are tunable in Normal mode, Accelerator mode, and Rapid Accelerator mode. If you use
the Simulink
Coder™ rapid simulation (RSIM) target to build an RSIM executable, then you can tune
these parameters without recompiling the model. For more information, see Tunable Parameters (Simulink).

## Version History

**Introduced before R2006a**

## Description

Apply phase and frequency offsets to complex baseband signal

The Phase/Frequency Offset block applies phase and frequency offsets to a complex signal.

This icon shows the block with all ports enabled.Phase/Frequency Offset block with optional frequency offset input port
