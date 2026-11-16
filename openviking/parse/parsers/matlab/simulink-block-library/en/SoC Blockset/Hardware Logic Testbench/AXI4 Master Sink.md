---
type: simulink-block
title: 'AXI4 Master Sink'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'axi4mastersink'
documentation_source_path: 'ref/axi4mastersink.html'
language: en
---

# AXI4 Master Sink

## Ports

### Input

### **rdData** — Input data scalar | vector

Input data from the data source. This value must be a scalar or vector.

Before reading the data, set the required data type. To set the data type, see the
**Data type** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdCtrlIn** — Input control bus bus

Input control bus from the data producer, specified as a bus. This control bus
comprises these control signals:

- `rd_aready` — Indicates the data source accepted the
  read request
- `rd_dvalid` — Indicates the data returned for the read
  request is valid

**Data Types:** `ReadControlS2MBusObj`
### Output

### **rdCtrlOut** — Output control bus bus

Output control bus to the data source indicating the block is ready to accept
data, returned as a scalar. This control bus comprises these control signals:

- `rd_addr` — Starting address for the read transaction
  that is sampled at the first cycle of the transaction
- `rd_len` — Number of data values you want to read,
  sampled at the first cycle of the transaction
- `rd_avalid` — Control signal that specifies whether
  the read request is valid
- `rd_dready` — Control signal that indicates when the
  block can read data

**Data Types:** `ReadControlM2SBusObj`

## Parameters

### **Data type** — Input data type `uint8` (default) | `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

Select the data type format for the input AXI data.

Click the  button to display the **Data Type Assistant**,
which helps you to set the data type for the **rdData** input port. For
details, see Specify Data Types Using Data Type Assistant.

### **Dimensions** — Input data dimensions `1` (default) | positive integer | array

Specify the dimensions of the input data as a positive scalar or an array. This
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

### **Number of transfers** — Number of read requests to send `1` (default) | positive integer

Specify the number of read requests for the block to send.

### **Initial address** — Start address `0` (default) | nonnegative scalar integer

Specify the address from which the block reads the data. This value must be a
nonnegative integer.

### **Initial delay** — Initial delay `0` (default) | nonnegative scalar

Specify the initial time after which the read operation starts.

### **Sample time** — Time interval of sampling 1 (default) | positive scalar | vector

Specify a time interval in seconds to define how often the block updates.

Specify the **Sample time** parameter as a scalar when you do not
want the output to have a time offset. To add a time offset to the output, specify the
**Sample time** parameter as a
`1`-by-`2` vector where the first element is the
sampling period and the second element is the offset. For more information about sample
times in Simulink®, see Specify Sample Time.

### **Save data in workspace** — Save to workspace `off` (default) | `on`

Select this parameter to save the input data to the MATLAB® workspace.

### **Variable name** — Workspace variable name `simOut` (default) | any MATLAB-supported variable name

Specify the workspace variable to which input data is saved. This parameter can be
any MATLAB-supported variable name.

#### Dependencies

To enable this parameter, select the **Save data in workspace**
parameter.

## Libraries

SoC Blockset / Hardware Logic Testbench

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Receive random access memory data

The AXI4 Master Sink block receives random access memory data from
AXI4-based data interface blocks. You can use this block as a test sink block for simulating
AXI4-based data applications.

The block accepts data along with a control bus and outputs a control bus.
