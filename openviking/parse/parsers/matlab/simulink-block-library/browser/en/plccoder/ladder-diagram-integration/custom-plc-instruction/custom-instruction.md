---
type: simulink-block
title: 'Custom Instruction'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Custom PLC Instruction'
documentation_page: 'custominstruction'
documentation_source_path: 'ref/custominstruction.html'
language: en
---

# Custom Instruction

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

The **EnableIn** port controls the execution of the block and
also reflects the rung state preceding the block. If the rung state preceding the
block is false, the **EnableIn** signal is set to false, the block
does not execute the custom logic, and the outputs are not updated.

### **src** — Input signal scalar

Input signal to the Custom Instruction block.

**Data Types:** `int8` | `int16` | `int32` | `single`
### Output

### **EnableOut** — Enable Output off (default) | on

If the **EnableIn** input to the block is false, the custom
logic implemented by the block is not executed and **EnableOut**
signal is set to false. If **EnableIn** is true and the custom
instruction executes, **EnableOut** signal is set to true.

## Parameters

### Inputs and Outputs

### **Instruction Name** — Name of user-defined ladder logic instruction sampleBlock (default) | character vector

Name of the ladder logic instruction that you want to create. The Rockwell Automation® Studio 5000 IDE must support the ladder logic instruction name.

### **Number of Inputs** — Number of input signals to block 1 (default) | scalar

The number of input signals to the block that are required for your custom ladder
logic instruction.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumInputs` |
| **Type**: scalar |
| **Value**: scalar |
| **Default**: `1` |

**Data Types:** `int8` | `int16` | `int32` | `single`

### **Input Types** — Data type of input signal `{{'SINT', 'INT','DINT','REAL'}}` (default) | character vector

The data type of the input signal specified as a cell array. For multiple inputs
signals, specify the data type as a comma-separated list of cell arrays for each
signal. For example, if you have two input signals with the same data type, then
specify the **Input Types** as
`{{'SINT','INT','DINT','REAL'},{'SINT','INT','DINT','REAL'}}`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InputTypeList` |
| **Type**: cell array |
| **Value**: cell array |
| **Default**: `{{'SINT','INT','DINT','REAL'}}` |

**Data Types:** `character vector`

### **Number of Outputs** — Number of output signals from block 1 (default) | scalar

The number of output signals from the user-defined Custom
Instruction block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumOutputs` |
| **Type**: scalar |
| **Value**: scalar |
| **Default**: `1` |

**Data Types:** `int8` | `int16` | `int32` | `single`

### **Output Types** — Data type of output signal `{{'SINT','INT','DINT','REAL'}}` (default) | character vector

The data type of the output signal specified as a cell array. If there is more
than one output signal, specify the data type as a comma-separated list of cell arrays
for each signal. For example, if you have two output signals with the same data type,
then specify the **Output Types** as
`{{'SINT','INT','DINT','REAL'},{'SINT','INT','DINT','REAL'}}`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputTypeList` |
| **Type**: cell array |
| **Value**: cell array |
| **Default**: `{{'SINT','INT','DINT','REAL'}}` |

**Data Types:** `character vector`

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Create custom ladder logic instruction

The Custom Instruction block implements user-defined instructions for a
ladder diagram model. When the rung conditions are true, the block executes the specified
custom logic. You can save these instructions in a user-defined library named
`plcuserlib.slx`. You can also import, simulate, and export your ladder
logic instructions by using your custom blocks saved in `plcuserlib.slx`
library.
