---
type: simulink-block
title: 'Deep Learning HDL Processing System'
family: 'deep-learning-hdl'
product_id: 'deep-learning-hdl'
product_name: 'Deep Learning HDL Toolbox'
documentation_release: R2025b
official_category: 'System Integration of Deep Learning Processor IP Core'
documentation_page: 'deeplearninghdlprocessingsystem'
documentation_source_path: 'ref/deeplearninghdlprocessingsystem.html'
language: en
---

# Deep Learning HDL Processing System

## Ports

### Input

### **RegisterWriteCtrlIn** — Input write data control bus bus

Input write data control bus, specified as a bus. The bus control signals are of
type `BusAXIWriteCtrlM2S` and includes these signals:

| Signal Name | Data Type |
| --- | --- |
| `wr_addr` | `uint32` scalar |
| `wr_len` | `uint32` scalar |
| `wr_valid` | `Boolean` scalar |

**Data Types:** `BusAXIWriteCtrlM2S`

### **RegisterWriteData** — Input data scalar | vector

Input data, specified as a scalar or vector.

**Data Types:** `uint32`

### **RegisterReadCtrlIn** — Input read data control bus bus

Input data read control bus, specified as a bus. The bus control signals are of
type `BusAXIReadCtrlM2S` and includes these signals:

| Signal Name | Data Type |
| --- | --- |
| `rd_addr` | `uint32` scalar |
| `rd_len` | `uint32` scalar |
| `rd_avalid` | `boolean` scalar |
| `rd_dready` | `boolean` scalar |

**Data Types:** `BusAXIReadCtrlM2S`

### **MemoryWriteCtrlIn** — Input DDR memory write data control bus bus

Input DDR memory write data control bus, specified as a bus. The bus control
signals are of type `BusAXIWriteCtrlM2S` and includes these
signals:

| Signal Name | Data Type |
| --- | --- |
| `wr_addr` | `uint32` scalar |
| `wr_len` | `uint32` scalar |
| `wr_valid` | `Boolean` scalar |

**Data Types:** `BusAXIWriteCtrlm2S`

### **MemoryWriteData** — Input DDR memory data scalar | vector

Input DDR memory data specified as a scalar or vector.

**Data Types:** `ufix128`

### **MemoryReadCtrlIn** — Input DDR memory read data control bus bus

Input DDR memory read data control bus, specified as a bus. The bus data type is
`BusAXIReadCtrlM2S` and includes these signals:

| Signal Name | Data Type |
| --- | --- |
| `rd_addr` | `uint32` scalar |
| `rd_len` | `uint32` scalar |
| `rd_avalid` | `boolean` scalar |
| `rd_dready` | `boolean` scalar |

**Data Types:** `BusAXIReadCtrlM2S`

### **InputStart** — Data processing start signal scalar

Data processing start signal, specified as a boolean.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `Boolean`

### **FrameCount** — Number of input data frames scalar

Number of input data frames, specified as a `int32`
scalar.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `int32`

### **InputStop** — Data streaming stop signal scalar

Data streaming stop signal, specified as a boolean.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `Boolean`

### **InputNext** — Next input frame ready signal scalar

Next input frame ready signal, specified as a boolean.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `Boolean`

### **OutputNext** — Current output data read complete signal scalar

Current output data read complete signal, specified as a boolean.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `Boolean`
### Output

### **RegisterWriteCtrlOut** — Output data write control bus bus

Output data write control bus, returned as a bus. The bus control signals are of
type `BusAXIWriteCtrlS2M` and includes these signals:

| Signal Name | Data Type |
| --- | --- |
| `wr_ready` | `boolean` scalar |
| `wr_complete` | `boolean` scalar |

**Data Types:** `BusAXIWriteCtrlS2M`

### **RegisterReadData** — Output data scalar | vector

Output data returned as a scalar or vector.

**Data Types:** `uint32`

### **RegisterReadCtrlOut** — Output data read control bus bus

Output data read control bus, returned as a bus. The bus control signals are of
type `BusAXIReadCtrlS2M` and includes these signals:

| Signal Name | Data Type |
| --- | --- |
| `rd_aready` | `boolean` scalar |
| `rd_dvalid` | `boolean` scalar |

**Data Types:** `BusAXIReadCtrlS2M`

### **MemoryWriteCtrlOut** — Output DDR memory data write control bus bus

Output DDR memory data write control bus, returned as a bus. The bus control
signals are of type `BusAXIWriteCtrlS2M` and includes these
signals:

| Signal Name | Data Type |
| --- | --- |
| `wr_ready` | `boolean` scalar |
| `wr_complete` | `boolean` scalar |

**Data Types:** `BusAXIWriteCtrlS2M`

### **MemoryReadData** — Output DDR memory data scalar | vector

Output DDR memory data returned as a scalar or vector.

**Data Types:** `ufix128`

### **MemoryReadCtrlOut** — Output DDR memory data read control bus bus

Output DDR memory data read control bus, returned as a bus. The bus control
signals are of type `BusAXIReadCtrlS2M` and includes these
signals:

| Signal Name | Data Type |
| --- | --- |
| `rd_aready` | `boolean` scalar |
| `rd_dvalid` | `boolean` scalar |

**Data Types:** `BusAXIReadCtrlS2M`

### **InputAddr** — Input data memory address signal scalar

Input data memory address signal returned, as a `uint32`
scalar.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `uint32`

### **InputSize** — Size of next input data frame scalar

Size of next input data frame, returned as a `uint32` scalar. The
input data frame size is measured in bytes.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `uint32`

### **InputValid** — Input data valid signal scalar

Input data valid signal, returned as a boolean.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `Boolean`

### **OutputAddr** — Processed output data memory address signal scalar

Processed output data memory address signal, returned as a
`uint32` scalar.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `uint32`

### **OutputSize** — Size of next output data frame signal scalar

Size of next output data frame signal, returned as a `uint32`
scalar. Use this signal when the `OutputValid` signal is on.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `uint32`

### **OutputValid** — Output data valid signal scalar

Output data valid signal, returned as a boolean scalar.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `Boolean`

### **Done** — Data processing complete signal scalar

Data processing complete signal, returned as a boolean scalar.

#### Dependencies

To enable this port, set the `RunTimeControl` property of the
`dlhdl.ProcessorConfig` object to `"port"`.

**Data Types:** `Boolean`

## Parameters

### **Network** — Name of network object `Network from MATLAB function` (default) | `Network from MAT-FILE`

Name of network object, specified as one of these options:

- `Network from MATLAB function` — Provide the name of
  the MATLAB function that returns a network object.
- `Network from MAT-file` — Provide the path to the
  MAT-file that stores the network object.

### **MATLAB Function** — Name of network MATLAB function `getDigitsNetwork` (default)

Name of the MATLAB function that returns a network object.

#### Dependencies

To enable this parameter, set **Network** to
`Network from MATLAB function`.

### **File Path** — Path to MAT-file `untitled.mat` (default)

Path to MAT-file that contains the network object.

#### Dependencies

To enable this parameter, set **Network** to
`Network from MAT-file`.

### **Activation Layer** — Name of network activation layer `pool10` (default)

Name of network activation layer to simulate. The default activation layer is the
last layer of the network object specified by the **Network**
parameter.

### **Maximum input frame number limit for memory access allocation** — Maximum input frame number limit 30 (default) | positive scalar

Maximum input frame number limit to calculate DDR memory access allocation.

### Processor Configuration Properties

### **Import Processor Configuration from MATLAB workspace** — Enable import of existing `dlhdl.ProcessorConfig` object `dlhdl.ProcessorConfig` (default) | `dlhdl.ProcessorConfig('Bitstream','zcu102_single')` | `dlhdl.ProcessorConfig('Bitstream','arria10soc_single')` | `dlhdl.ProcessorConfig('Bitstream','zc706_single')`

Import an existing `dlhdl.ProcessorConfig` object. if you specify
a function name, it must be a MATLAB function. For example, this MATLAB function returns a `dlhdl.ProcessorConfig` object called
`hPCinMATLAB`.

```
function hPCinMATLAB = hPCinMATLAB()
hPC = dlhdl.ProcessorConfig;
hPC.RunTimeControl = "port";
hPCinMATLAB = hPC;
end
```

After you add the MATLAB function name or `dlhdl.ProcessorConfig` object, click
**Apply** to import the processor configuration or MATLAB configuration into the block.

### **Export Processor Configuration to MATLAB workspace** — Enable export of `dlhdl.ProcessorConfig` object `hPCInSimulink` (default)

Export a `dlhdl.ProcessorConfig` object. The default object name
is `hPCInSimulink`.

#### Convolution Module

### **Module Generation** — Enable or disable convolution module generation on (default) | off

Enable or disable convolution module generation. Use this parameter to control
generation of the convolution module as a part of the deep learning processor
configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **LRN Block Generation** — Enable or disable local response normalization (LRN) block generation off (default) | on

Enable or disable LRN block generation. Use this parameter to control generation
of the LRN block as a part of the convolution module of the deep learning processor
configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Segmentation Block Generation** — Enable or disable segmentation block generation on (default) | off

Enable or disable segmentation block generation. Use this parameter to control
generation of the segmentation block as a part of the convolution module of the deep
learning processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Convolution Thread Number** — Number of parallel convolution processor kernel threads 16 (default) | 4 | 9 | 16 | 25 | 36 | 49 | 64

Number of parallel convolution processor kernel threads.

This parameter is the number of parallel 3-by-3 convolution kernel threads that
are a part of the `conv` module in the
`dlhdl.ProcessorConfig` object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Input Memory Size** — Input memory cache block RAM (BRAM) size Read-only: [227 227 3] (default) | 3-D positive integer array

This parameter is read-only.

Input memory cache BRAM size. This parameter is a 3-D matrix that represents the
maximum input image size permitted by the BRAM of the `conv` module
in the `dlhdl.ProcessorConfig` object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Output Memory Size** — Output memory cache block RAM (BRAM) sizes [227 227 3] (default) | 3-D positive integer array

Output memory cache BRAM size.

This parameter is a 3-D matrix that represents the maximum output image size
permitted by the BRAM of the `conv` module in the
`dlhdl.ProcessorConfig` object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Feature Size Limit** — Maximum input and output feature size 2048 (default) | positive integer

Maximum input and output feature size.

This parameter is a positive integer that represents the maximum input and output
feature size as a part of the `conv` module in the
`dlhdl.ProcessorConfig` object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

#### FC Module

### **Module Generation** — Enable or disable fully connected module generation on (default) | off

Enable or disable fully connected module generation. Use this parameter to control
generation of the fully connected module as a part of the deep learning processor
configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Softmax Block Generation** — Enable or disable Softmax block generation off (default) | on

Enable or disable Softmax block generation. Use this parameter to control
generation of the Softmax block as a part of the fully connected module of the deep
learning processor configuration. When you clear this parameter, the Softmax layer is
still implemented in software.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **FC Thread Number** — Number of parallel fully connected (fc) MAC threads 4 (default) | 4 | 8 | 16

Number of parallel fully connected (FC) MAC threads. This parameter is the number
of parallel FC MAC threads that are a part of the `fc` module in the
`dlhdl.ProcessorConfig` object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Input Memory Size** — Input memory cache block RAM (BRAM) sizes 25088 (default) | unsigned integer

Input memory cache BRAM size. This parameter is an unsigned integer that
represents the input cache memory size permitted by the BRAM of the
`fc` module in the `dlhdl.ProcessorConfig`
object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Output Memory Size** — Cache block RAM (BRAM) sizes 4096 (default) | unsigned integer

Output memory cache BRAM size. This parameter is an unsigned integer that
represents the output cache memory size permitted by the BRAM of the
`fc` module in the `dlhdl.ProcessorConfig`
object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

#### Custom Module

### **Module Generation** — Enable or disable custom module generation on (default) | off

Enable or disable custom module generation. Use this parameter to control
generation of the adder module as a part of the deep learning processor
configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Addition** — Enable or disable addition layer generation on (default) | off

Enable or disable addition layer generation. Use this parameter to control
generation of the addition layer as a part of the custom module of the deep learning
processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Multiplication** — Enable or disable multiplication layer generation on (default) | off

Enable or disable multiplication layer generation. Use this parameter to control
generation of the multiplication layer as a part of the custom module of the deep
learning processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Resize2D** — Enable or disable 2-D resize layer generation off (default) | on

Enable or disable 2-D resize layer generation. Use this parameter to control
generation of the 2-D resize layer as a part of the custom module of the deep learning
processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Sigmoid** — Enable or disable sigmoid layer generation off (default) | on

Enable or disable sigmoid layer generation. Use this parameter to control
generation of the sigmoid layer as a part of the custom module of the deep learning
processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **TanhLayer** — Enable or disable `tanh` layer generation off (default) | on

Enable or disable `tanh` layer generation. Use this parameter to
control generation of the `tanh` layer as a part of the custom module
of the deep learning processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **MishLayer** — Enable or disable `mish` layer generation off (default) | on

Enable or disable `mish` layer generation. Use this parameter to
control generation of the `mish` layer as a part of the custom module
of the deep learning processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **SwishLayer** — Enable or disable `swish` layer generation off (default) | on

Enable or disable `swish` layer generation. Use this parameter to
control generation of the `swish` layer as a part of the custom
module of the deep learning processor configuration.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Input Memory Size** — Input memory cache block RAM (BRAM) sizes 40 (default) | unsigned integer

Input memory cache BRAM size. This parameter is an unsigned integer that
represents the input cache memory size permitted by the BRAM of the
`custom` module in the `dlhdl.ProcessorConfig`
object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Output Memory Size** — Output memory cache block RAM (BRAM) sizes 120 (default) | unsigned integer

Output memory cache BRAM size. This parameter is an unsigned integer that
represents the input cache memory size permitted by the BRAM of the
`custom` module in the `dlhdl.ProcessorConfig`
object.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

#### Processor Top Level

### **Choose Processinf Mode of All Interface Signals** — Select the interface type for all deep learning processor IP core interface signals Read-only: `register` (default) | `port`

This parameter is read-only.

Select the interface type for all deep learning processor IP core interface
signals. Specify whether the run-time input signals, run-time feedback signals, input
interface control input signals, and input interface control feedback signals are
implemented as registers or ports.

#### Dependencies

To enable and edit this parameter, enable **Export Processor
Configuration to MATLAB Workspace**.

### **RunTimeControl** — Deep learning processor IP core mode setting Read-only: `register` (default) | `port`

This parameter is read-only.

Deep learning processor IP core mode setting. Specify whether the run-time input
signals to the deep learning processor IP core are implemented as registers or
ports.

### **RunTimeStatus** — Feedback signals from deep learning processor IP core control Read-only: `register` (default) | `port`

This parameter is read-only.

Feedback signals from deep learning processor IP core control. Specify whether the
run-time output signals from the deep learning processor IP core are implemented as
registers or ports.

### **InputStreamControl** — Deep learning processor IP core input interface control Read-only: `register` (default) | `port`

This parameter is read-only.

Deep learning processor IP core input interface control.

### **OutputStreamControl** — Deep learning processor IP core output interface control Read-only: `register` (default) | `port`

This parameter is read-only.

Deep learning processor IP core output interface control.

### **SetupControl** — Deep learning processor IP core user interface control Read-only: `register` (default) | `port`

This parameter is read-only.

Deep learning processor IP core user interface control.

### **ProcessorDataType** — Deep learning processor IP core module data type `single` (default)

Deep learning processor IP core module data type.

#### Dependencies

To edit this parameter, enable **Export Processor Configuration to
MATLAB Workspace**.

### **Export Deep Learning Processor IP Core Register addresses to MATLAB workspace** — Export register addresses Read-only: on (default) | off

This parameter is read-only.

Enable this option to export a structure containing address locations to the
MATLAB workspace.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Simulate deep learning processor IP core interface

The Deep Learning HDL Processing System block simulates the deep learning
processor IP core and models, simulates, and validates the hand-shaking logic between the pre-
and post-processing systems and the deep learning processor IP core. The block icon changes
depending on the `RunTimeControl` property setting of the
`dlhdl.ProcessorConfig` object. To access the block at the MATLAB® command line,
enter:

```
open_system('dlhdllib')
```

| `RunTimeControl` Setting | **Block Icon** |
| --- | --- |
| `Register` | Register Ports |
| `Port` | Port Inputs |
