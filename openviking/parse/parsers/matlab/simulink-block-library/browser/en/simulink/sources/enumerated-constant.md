---
type: simulink-block
title: 'Enumerated Constant'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sources'
documentation_page: 'enumeratedconstant'
documentation_source_path: 'slref/enumeratedconstant.html'
language: en
---

# Enumerated Constant

## Ports

### Output

### **Port\_1** — Enumerated constant scalar | vector | matrix

Enumerated constant value, specified as a scalar, vector, or matrix.

**Data Types:** `enumerated`

## Parameters

### **Output data type** — Output data type `Enum: SlDemoSign` (default) | `Enum:<ClassName>`

Specify the enumerated type from which you want the block to output one or
more values. The initial value,
`Enum:``SlDemoSign`, is a dummy
enumerated type that prevents a newly cloned block from causing an error. To
specify the desired enumerated type, select it from the drop-down list or
enter
`Enum:``ClassName`
in the **Output data type** field, where
`ClassName` is the name
of the MATLAB® class that defines the type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Enum:<ClassName>'` |
| **Default**: `'Enum: SlDemoSign'` |

### **Mode** — Category of data to specify `Enumerated` (default)

Select the category of data to specify.

`Enumerated`
:   Enumerated data types. Selecting
    `Enumerated` enables a second
    menu/text box to the right, where you can enter the class
    name.

### **Value** — Enumerated value `SlDemoSign.Positive` (default) | `Enum:<ClassName.Value>`

Specify the value or values that the block outputs. The output of the
block has the same dimensions and elements as the **Value**
parameter. The initial value, `SlDemoSign.Positive`, is a
dummy enumerated value that prevents a newly cloned block from causing an
error.

To specify the desired enumerated values, select from the drop-down list
or enter any MATLAB expression that evaluates to the desired result, including an
expression that uses tunable parameters. All specified values must be of the
type indicated by the **Output data type**. To
specify an array that includes every value in the enumerated type, use the
`enumeration` function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Value` |
| **Type**: character vector |
| **Values**: `'SlDemoSign.Positive'` | `'SlDemoSign.Zero'` | `'SlDemoSign.Negative'` | `'Enum:<ClassName.Value>'` |
| **Default**: `'SlDemoSign.Positive'` |

### **Sample time** — Sample time `inf` (default) | scalar | vector

Specify the interval between times that the block output can change during
simulation (for example, due to tuning the **Value**
parameter). The default value of `inf` indicates that the
block output can never change. A sample time of `inf`
speeds the simulation and generated code by avoiding the need to recompute
the block output. For more information, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar | vector |
| **Default**: `'inf'` |

## Libraries

Simulink / Sources HDL Coder / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `enumerated` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2009b**

## Description

Generate enumerated constant value

The Enumerated Constant block outputs a scalar, array, or matrix of
enumerated values. You can also use the Constant block to output enumerated values, but it provides block
parameters that do not apply to enumerated types, such as **Output
minimum** and **Output maximum**. When you need a block
that outputs only constant enumerated values, use Enumerated Constant
rather than Constant. For more information, see Simulink Enumerations.
