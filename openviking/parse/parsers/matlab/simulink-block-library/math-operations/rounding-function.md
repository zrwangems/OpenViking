---
type: simulink-block
title: 'Rounding Function'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'roundingfunction'
---

# Rounding Function

Apply rounding function to signal

## Libraries

Simulink / Math Operations

## Description

The Rounding Function block rounds each element of the input signal to
produce the output signal.

You select the type of rounding from the **Function** parameter list.
The name of the selected function appears on the block.

**Tip**

Use the Rounding Function block when you want vector or matrix
output.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Input signal to which the rounding function is applied.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal after the rounding function is applied to the input
signal. The output signal has the same dimensions and data type as the
input. Each element of the output signal is the result of applying the
selected rounding function to the corresponding element of the input
signal.

**Data Types:** `single` | `double`

## Parameters

### **Function** — Rounding function `floor` (default) | `ceil` | `round` | `fix`

Choose the rounding function applied to the input signal.

| Rounding function | Rounds each element of the input signal |
| --- | --- |
| `floor` | To the nearest integer value towards minus infinity |
| `ceil` | To the nearest integer towards positive infinity |
| `round` | To the nearest integer |
| `fix` | To the nearest integer towards zero |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Operator` |
| **Type**: character vector |
| **Values**: `'floor'` | `'ceil'` | `'round'` | `'fix'` |
| **Default**: `'floor'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Code Generation Requirements**

HDL code generation for the block requires that you use single data types as inputs to the
block, and enable the native floating point mode. In the Configuration
Parameters dialog box, on the **HDL Code Generation** > **Floating Point** pane, for **Library**, select `Native
Floating Point`. To learn more about using the native
floating-point mode, see Getting Started with HDL Coder Native Floating-Point Support (HDL Coder) and Generate Target-Independent HDL Code with Native Floating-Point (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, `Zero`, or `Custom` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **NFPCustomLatency** | To specify a value, set **LatencyStrategy** to `Custom`. HDL Coder adds latency equal to the value that you specify for the **NFPCustomLatency** setting. See also NFPCustomLatency (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**
