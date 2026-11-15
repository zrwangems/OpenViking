---
type: simulink-block
title: 'Interval Test'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Logic and Bit Operations'
documentation_page: 'intervaltest'
documentation_source_path: 'slref/intervaltest.html'
language: en
---

# Interval Test

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | N-D array

Input signal, specified as a scalar, vector, matrix, or N-D
array.

#### Limitations

When the input signal is an enumerated type, the **Upper
limit** and **Lower limit** values
must be of the same enumerated type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **Port\_1** — Output signal scalar | vector | matrix | N-D array

Output signal indicating whether the input values fall within the
specified interval. You can specify the **Output data
type** as `boolean` or
`uint8`.

**Data Types:** `uint8` | `Boolean`

## Parameters

### **Interval closed on right** — Include upper limit value `on` (default) | `off`

When you select this check box, the **Upper limit** is
included in the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `IntervalClosedRight` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Upper limit** — Upper limit of interval `0.5` (default) | scalar | vector | matrix | N-D array

The upper limit of the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `uplimit` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'0.5'` |

### **Interval closed on left** — Include lower limit value `on` (default) | `off`

When you select this check box, the **Lower limit** is
included in the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `IntervalClosedLeft` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |

### **Lower limit** — Lower limit of interval `-0.5` (default) | scalar | vector | matrix | N-D array

The lower limit of the interval for which the block outputs true
(`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `lowlimit` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'-0.5'` |

### **Output data type** — Output data type `boolean` (default) | `uint8`

Specify the output data type as `boolean` or
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'boolean' | 'uint8'` |
| **Default:** `'boolean'` |

## Libraries

Simulink / Logic and Bit Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `Module` (default) | Generate code for the subsystem and the blocks within the subsystem. |
| `BlackBox` | Generate a black box interface. The generated HDL code includes only the input/output port definitions for the subsystem. Therefore, you can use a subsystem in your model to generate an interface to existing, manually written HDL code.  The black-box interface generation for subsystems is similar to the Model block interface generation without the clock signals. |
| `No HDL` | Remove the subsystem from the generated code. You can use the subsystem in simulation, however, treat it as a “no-op” in the HDL code. |

**Black Box Interface Customization**

For the `BlackBox` architecture, you
can customize port names and set attributes of the external component
interface. See Customize Black Box or HDL Cosimulation Interface (HDL Coder).

**HDL Block Properties**

| General | |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. See also AdaptivePipelining (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. See also ClockRatePipelining (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **FlattenHierarchy** | Remove subsystem hierarchy from generated HDL code. The default is `inherit`. See also FlattenHierarchy (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |

If this block is not the DUT, the block property settings in the **Target
Specification** tab are ignored. In the HDL Workflow Advisor, if you use the
**IP Core Generation** workflow, these target specification block
property values are saved with the model. If you specify these target specification block
property values using `hdlset_param`, when you open HDL Workflow Advisor,
the fields are populated with the corresponding values.

| Target Specification | |
| --- | --- |
| **AdditionalTargetInterfaces** | Additional target interfaces, specified as a character vector.  To save this block property on the model, in the **Set Target Interface** task of the **IP Core Generation** workflow, corresponding to the DUT ports that you want to add more interfaces, select **Add more...**. You can then add more interfaces in the Add New Target Interfaces dialog box. Specify the type of interface, number of additional interfaces, and a unique name for each additional interface.  Values: `''` (default) | cell array of character vectors  Example: `'{{'AXI4-Stream','InterfaceID','AXI4-Stream1'}}'` |
| **ProcessorFPGASynchronization** | Processor/FPGA synchronization mode, specified as a character vector.  To save this block property on the model, specify the **Processor/FPGA Synchronization** in the **Set Target Interface** task of the **IP Core Generation** workflow.  Values: `Free running` (default) | `Coprocessing - blocking`  Example: `'Free running'` |
| **TestPointMapping** | To save this block property on the model, specify the mapping of test point ports to target platform interfaces in the **Set Target Interface** task of the **IP Core Generation** workflow.  Values: `''` (default) | cell array of character vectors  Example: `'{{'TestPoint','AXI4-Lite','x"108"'}}'` |
| **TunableParameterMapping** | To save this block property on the model, specify the mapping of tunable parameter ports to target platform interfaces in the **Set Target Interface** task of the **IP Core Generation** workflow.  Values: `''` (default) | cell array of character vectors  Example: `'{{'myParam','AXI4-Lite','x"108"'}}'` |
| **AXI4RegisterReadback** | To save this block property on the model, specify whether you want to enable readback on AXI4 subordinate write registers in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow. To learn more, see Model Design for AXI4 Slave Interface Generation (HDL Coder).  Values: `'off'` (default) | `'on'` |
| **AXI4SlaveIDWidth** | To save this block property on the model, specify the number of AXI manager interfaces that you want to connect the DUT IP core to by using the **AXI4 Slave ID Width** setting in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow. To learn more, see Define Multiple AXI Master Interfaces in Reference Designs to Access DUT AXI4 Slave Interface (HDL Coder).  Values: `'off'` (default) | `'on'` |
| **RegisterInterfaceReadPipeline** | To save this block property on the model, Specify the number of pipeline stages to insert in the read address decoder path by using the **Register interface read pipeline** setting in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow. To learn more, see Model Design for AXI4 Slave Interface Generation (HDL Coder).  Values: `0` (default) | character vector |
| **GenerateDefaultAXI4Slave** | To save this block property on the model, specify whether you want to disable generation of default AXI4 subordinate interfaces in the **Generate RTL Code and IP Core** task of the **IP Core Generation** workflow.  Values: `'on'` (default) | `'off'` |
| **IPCoreAdditionalFiles** | Verilog®, SystemVerilog, or VHDL® files for black boxes in your design. Specify the full path to each file, and separate file names with a semicolon (;).  You can set this property in the HDL Workflow Advisor, in the **Additional source files** field.  Values: `''` (default) | character vector  Example: `'C:\myprojfiles\led_blinking_file1.vhd;C:\myprojfiles\led_blinking_file2.vhd;'` |
| **IPCoreName** | IP core name, specified as a character vector.  You can set this property in the HDL Workflow Advisor, in the **IP core name** field. If this property is set to the default value, the HDL Workflow Advisor constructs the IP core name based on the name of the DUT.  Values: `''` (default) | character vector  Example: `'my_model_name'` |
| **IPCoreVersion** | IP core version number, specified as a character vector.  You can set this property in the HDL Workflow Advisor, in the **IP core version** field. If this property is set to the default value, the HDL Workflow Advisor sets the IP core version.  Values: `''` (default) | character vector  Example: `'1.3'` |
| **IPDataCaptureBufferSize** | FPGA Data Capture buffer size, specified as a character vector. Use FPGA Data Capture to observe signals in a design when running on an FPGA.  The buffer size uses values that are 128\*2^n, where n is an integer. By default, the buffer size is 128 (n=0). The maximum value of n is 13, which means that the maximum value for buffer size is 1048576 (=128\*2^13).  Values: `''` (default) | character vector  Example: `'1.3'` |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Determine if signal is in specified interval

The Interval Test block outputs true (`1`) if the
input is between the values specified by the **Lower limit** and
**Upper limit** parameters. The block outputs false
(`0`) if the input is outside those values. The output of the block
when the input is equal to the **Lower limit** or the **Upper
limit** is determined by whether you select the **Interval closed
on left** and **Interval closed on right** check
boxes.
