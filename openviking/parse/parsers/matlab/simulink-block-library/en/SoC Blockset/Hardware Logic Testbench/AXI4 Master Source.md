---
type: simulink-block
title: 'AXI4 Master Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'axi4mastersource'
documentation_source_path: 'ref/axi4mastersource.html'
language: en
---

# AXI4 Master Source

## Ports
```yaml
ports:
- name: wrCtrlIn
  summary: Input control bus bus
  direction: input
  data_types: WriteControlS2MBusObj
- name: wrData
  summary: Output AXI data scalar | vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: wrCtrlOut
  summary: Output control bus bus
  direction: output
  data_types: WriteControlM2SBusObj
```

### Input

### **wrCtrlIn** — Input control bus bus

Control bus from the data consumer signaling that data consumer is ready to accept
data, specified as a scalar. This control bus comprises these control signals:

- `wr_ready` — Indicates the block can send data to the
  data consumer
- `wr_complete` — Indicates the write transaction has
  completed at the data consumer
- `wr_bvalid` — Indicates the data consumer has accepted
  the transaction

**Data Types:** `WriteControlS2MBusObj`
### Output

### **wrData** — Output AXI data scalar | vector

Output AXI data to the data consumer. This value is returned as a scalar or
vector.

You can change the data type of the output data. For more information, see the
**Data type**  parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrCtrlOut** — Output control bus bus

Control bus to the data consumer, returned as a bus. This control bus comprises
these control signals:

- `wr_addr` — Specifies the starting address that the
  block writes
- `wr_len` — Specifies the number of data elements in
  the write transaction
- `wr_valid` — Indicates the data sampled at the
  **wrData** output port is valid

**Data Types:** `WriteControlM2SBusObj`
## Parameters
```yaml
parameters:
- name: Data type
  summary: Output data type uint8 (default) | double | single | int8 | int16 | int32 | int64 | uint16 | uint32 | uint64 |
    fixed point
  group: ''
- name: Dimensions
  summary: Output data dimensions 1 | positive scalar | array
  group: ''
- name: Enable sample packing (last signal dimension as channel)
  summary: Pack data on the last dimension of the signal off (default) | on
  group: ''
- name: Number of transfers
  summary: Number of write requests to send 1 (default) | positive integer
  group: ''
- name: Initial address
  summary: Start address 0 (default) | nonnegative integer
  group: ''
- name: Initial delay
  summary: Initial delay 0 (default) | nonnegative scalar
  group: ''
- name: Data generation
  summary: Output generation type counter (default) | random | ones | workspace
  group: ''
- name: Counter init value
  summary: Initial counter value 0 (default) | scalar
  group: ''
- name: Variable name
  summary: Workspace variable name simOut (default) | any MATLAB-supported variable name
  group: ''
- name: Sample time
  summary: Time interval of sampling 1 (default) | positive scalar | vector
  group: ''
```

### **Data type** — Output data type `uint8` (default) | `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

Select the data type format for the output AXI data.

Click the  button to display the **Data Type Assistant**,
which helps you to set the data type for the **wrData** output port. For
details, see Specify Data Types Using Data Type Assistant.

### **Dimensions** — Output data dimensions `1` | positive scalar | array

Specify the dimensions of the output data as a positive scalar or an array. This
value defines the size of the data signal.

**Example:** `1` specifies a scalar sample.

**Example:** `[10 1]` specifies a vector of ten scalars.

### **Enable sample packing (last signal dimension as channel)** — Pack data on the last dimension of the signal `off` (default) | `on`

Select this parameter to enable data packing across the last dimension of the
signal. The Memory Channel block packs the data along the last dimension
of the signal. For example, if the channel data type is `uint32`, the
dimensions are `[1024 4]`, and if you select this parameter, then the
memory channel generates 1024 read or write transactions of 128 bits. For this example,
if you clear this sample packing parameter, the memory channel generates 4096
transactions of 32 bits each.

This figure shows how data is aligned for a signal with data type
`fixdt10[4x3]`. When the data is packed, three 10-bit words are
concatenated and extended by 2 bits to a 32-bit sample. When the data is not packed,
each 10-bit word is extended to a 16-bit sample.

The top row shows packed data aligned in samples of 10,10,10, and 2 to make 32 bits. The bottom row shows unpacked data aligned in samples of 10 and 6 to make 16 bits.

This figure shows how data is aligned for a signal with data type
`uint8[8x3]`. When the data is packed, three 8-bit words are
concatenated and extended by 8 bits to a 32-bit sample. When the data is not packed,
each 8-bit word is represented as an 8-bit sample.

The top row shows packed data aligned in samples of 8,8,8, and 8 to make 32 bits. The bottom row shows unpacked data aligned in samples of 8 bits.

The combined width of the flattened signal must not exceed 512 bits.

### **Number of transfers** — Number of write requests to send `1` (default) | positive integer

Specify the number of write requests for the block to send.

### **Initial address** — Start address `0` (default) | nonnegative integer

Specify the address to which the block writes the data. This value must be a
nonnegative integer.

### **Initial delay** — Initial delay `0` (default) | nonnegative scalar

Specify the initial time after which the write operation starts. This value must be
a nonnegative scalar.

### **Data generation** — Output generation type `counter` (default) | `random` | `ones` | `workspace`

Specify the generation type for the output as one of these values:

- `counter` — Generate data from a counter, based
  on the selected data type.
- `random` — Generate random data.
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

### **Variable name** — Workspace variable name `simOut` (default) | any MATLAB-supported variable name

Specify the workspace variable from which output data is generated. This parameter
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
## Libraries

SoC Blockset / Hardware Logic Testbench

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Generate random access memory data

The AXI4 Master Source block generates random access memory data to
AXI4-based data interface blocks. You can use this block as a test source block for simulating
AXI4-based data applications.

The block accepts a control bus and outputs data along with a control bus.
