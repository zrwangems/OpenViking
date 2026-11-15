---
type: simulink-block
title: 'To File'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sinks'
documentation_page: 'tofile'
documentation_source_path: 'slref/tofile.html'
language: en
---

# To File

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix | array

Signal to store in file. Each sample consists of a timestamp and an
associated data value. The data can be in array format or MATLAB
`timeseries` format. The To File block
accepts real or complex signal data of any data type that Simulink® software supports, except fixed-point data with a word
length greater than 32 bits.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **File name** — Path or file name `untitled.mat` (default) | MAT file path or name

Specify the path or file name of the MAT file in which to store the
output. On UNIX® systems, the path name can start with a tilde (~) character
signifying your home folder. If you specify a file name without path
information, Simulink software stores the file in the MATLAB working folder. (To determine the working folder, at the
MATLAB command line, enter `pwd`.) If the file
exists, Simulink software overwrites it.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `FileName` |
| **Type:** character vector |
| **Values:** MAT file path or name |
| **Default:**  `'untitled.mat'` |

### **Variable name** — Matrix name `ans` (default) | character vector

Specify the name of the matrix contained in the file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `MatrixName` |
| **Type:** character vector |
| **Values:** character vector |
| **Default:**  `'ans'` |

### **Save format** — Data format `Timeseries` (default) | `Array`

Specify the data format that the To File block uses for
writing data.

Use the `Array` format only for vector, double,
noncomplex signals.

For the `Timeseries` format, the To
File block:

- Writes data in a MATLAB
  `timeseries` object.
- Supports writing multidimensional, real, or complex output
  values.
- Supports writing output values that have any built-in data type,
  including `Boolean`, enumerated
  (`enum`), and fixed-point data with a word
  length of up to 32 bits.
- For virtual and nonvirtual bus input signals, creates a
  MATLAB structure that matches the bus hierarchy. Each leaf of
  the structure is a MATLAB
  `timeseries` object.

For the `Array` format, the To
File block:

- Writes data into a matrix containing two or more rows. The matrix
  has the following form:

  [t1t2…tfinalu11u12…u1final…un1un2…unfinal]

  Simulink software writes one column to the matrix for each data
  sample. The first element of the column contains the timestamp. The
  remainder of the column contains data for the corresponding output
  values.
- Supports writing data that is one-dimensional, double, and
  noncomplex.

The From File block can use data
written by a To File block in any format
(`Timeseries` or `Array`) without any
modifications to the data or other special provisions.

The From Workspace block can
read data that is in the `Array` format and is the
transposition of the data written by the To File block. To
provide the required format, use MATLAB commands to load and transpose the data from the MAT
file.

The following table shows how simulation mode support depends on the
**Save format** value.

| Simulation Mode | `Timeseries` | `Array` |
| --- | --- | --- |
| Normal | Supported | Supported |
| Accelerator | Supported | Supported |
| Rapid Accelerator | Supported | Supported |
| Software-in-the-loop (SIL) | Not supported | Supported if MAT file logging is enabled |
| Processor-in-the-loop (PIL) | Not supported | Supported if MAT file logging is available and enabled |
| External | Not supported | Supported if MAT file logging is enabled |
| RSim target | Supported | Supported if MAT file logging is enabled |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**  `SaveFormat` |
| **Type:** character vector |
| **Values:** `'Timeseries' | 'Array'` |
| **Default:**  `'Timeseries'` |

### **Decimation** — Decimation factor that determines when data writes 1 (default) | scalar | vector

Specify the decimation factor, *n*, that writes data at
every *n*th time that the block executes. The default value
has this block writing data at every time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Decimation` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'1'` |

### **Sample time** — Sample period and offset -1 (default) | scalar | vector

Specifies the sample period and offset at which to collect data points.
This parameter is useful when you are using a variable-step solver where the
interval between time steps is not constant. The default value causes the
block to inherit the sample time from the driving block. See Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'-1'` |

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Supports up to 32-bit fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions
on speed and memory often found in embedded systems. Generated code can contain
dynamic allocation and freeing of memory, recursion, additional memory overhead, and
widely-varying execution times. While the code is functionally valid and generally
acceptable in resource-rich environments, smaller embedded targets often cannot
support such code. Usually, blocks evolve toward being suitable for production code.
Thus, blocks suitable for production code remain suitable.

Code generation for RSim target provides identical support as Simulink; all other code generation targets support only double,
one-dimensional, real signals in array with time format.

To generate code for a To File block, on
the **Code Generation** > **Interface** pane, select the configuration parameter MAT-file logging (Simulink Coder).

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Supports up to 32-bit fixed-point data types.

## Version History

**Introduced before R2006a**

## Description

Write data to file

The To File block writes input signal data into a MAT file.
The block writes to the output file incrementally, with minimal memory overhead during
simulation. If the output file exists when the simulation starts, the block overwrites
the file. The file automatically closes when you pause the simulation or the simulation
completes. If simulation terminates abnormally, the To File block saves
the data it has logged up until the point of the abnormal termination.

The To File block icon shows the name of the output file.

### Control Amount of Data Saved

If you specify data logging intervals with the **Configuration Parameters** >  **Data Import/Export** >  **Logging intervals** parameter, the To File block logs only data inside of
the intervals. For example, the block logs no data if the intervals are empty
(`[]`). The block stores the logged data in the file associated
with the block instead of in the variable that you specify for the **Single
simulation output** parameter.

For variable-step solvers, to control the amount of data available to the
To File block, use the **Configuration Parameters** >  **Data Import/Export** >  **Additional parameters** >  **Output options** parameter. For example, to write data at identical time points over
multiple simulations, select the `Produce specified output only`
option.

Block parameters also control the amount of data saved. See Decimation and Sample time.

### Pause Simulation

After pausing a simulation, do not alter any file that a To File
block logs into. For example, do not save such a file with the MATLAB®
`save` command. Altering the file can cause an error when you
resume the simulation. If you want to alter the file after pausing, copy the file
and work with the copy of the file.

If you pause using the Simulation Stepper, the To File block
captures the simulation data up to the point of the pause. When you step back, the
To File data file no longer contains any simulation data past the
new reduced time of the last output.
