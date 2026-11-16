---
type: simulink-block
title: 'Stream Data Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'streamdatasource'
documentation_source_path: 'ref/streamdatasource.html'
language: en
---

# Stream Data Source

## Ports

### Input

### **wrCtrlIn** — Input control bus bus

Control bus from the data consumer signaling that data consumer is ready to accept
stream data. This control bus comprises a ready signal.

**Data Types:** `StreamS2MBusObj`
### Output

### **wrData** — Output stream data scalar | vector

Output stream data to the data consumer. This value is returned as a scalar or
vector.

You can change the data type of the output stream data. For more information, see
the **Data type**  parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrCtrlOut** — Output control bus bus

Control bus to the data consumer, returned as a bus. This control bus comprises
these control signals:

- `valid` — Indicates the output data on the
  **wrData** output port is valid
- `tlast` — Indicates the end of the data
  transaction

**Data Types:** `StreamM2SBusObj`

## Parameters

### **Data type** — Output data type `uint8` (default) | `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixdt(1,16,0)`

Select the data type format for the output stream data.

Click the  button to display the **Data Type Assistant**,
which helps you to set the data type for the **wrData** output port. For
details, see Specify Data Types Using Data Type Assistant.

### **Dimensions** — Output data dimensions `10` (default) | positive integer | array

Specify the dimensions of the output stream data as a positive scalar or an
array.

**Example:** `1` specifies a scalar sample.

**Example:** `[10 1]` specifies a vector of ten scalars.

### **Burst length** — Length of single burst `20` (default) | positive integer

Length of the single burst, specified as a positive integer.

### **Total bursts** — Total number of bursts `4` (default) | positive integer

Total number of bursts generated from the block, specified as a positive
integer.

### **Data generation** — Output generation type `counter` (default) | `random` | `ones` | `workspace`

Specify the generation type for the output as one of these values:

- `counter` — Generate data from a counter, based
  on the selected data type.
- `random` — Generate a random data.
- `ones` — Generate data with all the bits as
  ones, based on the selected data type.
- `workspace` — Generate data from the MATLAB® workspace.

### **Counter init value** — Initial counter value `0` (default) | scalar

Specify the value from which the counter starts. The valid range of counter values
depends on the selected value for the **Data type** parameter. If
this value is out of the valid range, it is rounded off to the nearest valid
value.

For example, if **Data type** is `uint8`
and this value is `6.787`, this value is rounded to
`7`.

#### Dependencies

To enable this parameter, set the **Data generation** parameter
to `counter`.

### **Variable name** — Workspace variable name `simOut` (default) | any MATLAB supported variable name

Specify the variable name from which output stream data is generated. This parameter
can be any MATLAB-supported variable name.

**Note**

The workspace variable must be a numerical array.

#### Dependencies

To enable this parameter, set the **Data generation** parameter
to `workspace`.

### **Sample time** — Time interval of sampling 1 (default) | positive scalar | vector

Specify a time interval in seconds to define how often the block updates.

Specify the **Sample time** parameter as a scalar when you do not
want the output to have a time offset. To add a time offset to the output, specify the
**Sample time** parameter as a
`1`-by-`2` vector where the first element is the
sampling period and the second element is the offset. For more information about sample
times in Simulink®, see Specify Sample Time.

### **Transfer delay (in samples)** — Delay between bursts `0` (default) | nonnegative integer

Time after which the next burst occurs. This value must be a nonnegative
integer.

## Libraries

SoC Blockset / Hardware Logic Testbench

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

To automatically generate HDL code for your design, and execute
on an SoC device, use the **SoC Builder** tool. See Use SoC Builder to Generate SoC Design.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2019a**

## Description

Generate continuous stream data

The Stream Data Source block generates stream data to advanced extensible
interface AXI4-based stream data interface blocks. You can use this block as a test source
block for simulating AXI4-based stream data applications.

The block accepts a control bus and outputs stream data along with a control bus.
