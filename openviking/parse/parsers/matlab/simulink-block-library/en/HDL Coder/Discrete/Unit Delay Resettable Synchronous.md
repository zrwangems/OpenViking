---
type: simulink-block
title: 'Unit Delay Resettable Synchronous'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'unitdelayresettablesynchronous'
documentation_source_path: 'ref/unitdelayresettablesynchronous.html'
language: en
---

# Unit Delay Resettable Synchronous

## Ports

### Input

### **u** — Input signal `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

The Unit Delay Resettable Synchronous block accepts the
input signal of the data types listed below. For more information, see
Data Types Supported by Simulink.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **R** — Reset signal `Scalar`

The Unit Delay Resettable Synchronous block accepts the
Reset signal of the data types listed below. For more information, see
Data Types Supported by Simulink.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### Output

### **y** — Output signal `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

Output data type matches input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Initial condition** — Initial output of simulation 0.0 (default) | `Scalar` | `Vector` | `Matrix` | `Array` | `Bus`

The **Initial condition** can take a scalar input or use
the same data type as the input signal. You cannot run the simulation with
`NaN` or `Inf` as the
**Initial condition**.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `InitialCondition` |
| **Type:** character vector |
| **Value:** `'0'` | `'[n]'` | `'[m n]'` |
| **Default:** `'0'` |

### **Sample time** — Time interval between samples -1 (default) | `Scalar` | `Vector`

The **Sample time** must be a real double scalar that
specifies the period or a real double vector of length two that specifies
the period and offset. The period and offset must be finite and non-negative
with offset less than the period.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleTime` |
| **Type:** character vector |
| **Value:** `'-1'` | `'[n]'` | `'[m n]'` |
| **Default:** `'-1'` |

## Libraries

HDL Coder / Discrete

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder provides additional configuration options that
affect HDL implementation and synthesized
logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline. |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline. |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType. |

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

HDL code generation supports only boolean datatype at the Reset port.

## Version History

**Introduced in R2017b**

## Description

Delay input signal by one sample period when external Reset signal is false

The Unit Delay Resettable Synchronous block delays the input signal u
by one sample period when the external Reset signal is false. When the Reset signal is
true, the state and output signal take the value of the **Initial
condition** parameter after one sample period. The Reset signal is true
when R is not zero and false when R is zero.

The Unit Delay Resettable Synchronous block implementation consists of
a Synchronous Subsystem that contains a Resettable Delay
block with a **Delay length** of one and a State Control
block in `Synchronous` mode. When you use this block in your model and
have HDL Coder™ installed, your model generates cleaner HDL code and uses fewer hardware
resources due to the `Synchronous` behavior of the State
Control block.
