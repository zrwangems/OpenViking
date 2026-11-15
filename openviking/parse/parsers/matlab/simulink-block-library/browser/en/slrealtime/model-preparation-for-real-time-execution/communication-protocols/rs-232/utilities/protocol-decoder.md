---
type: simulink-block
title: 'Protocol Decoder'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Utilities'
documentation_page: 'protocoldecoder'
documentation_source_path: 'io_ref/protocoldecoder.html'
language: en
---

# Protocol Decoder

## Ports

### Input

### **Data** — uint8 byte stream packet vector

The uint8 byte stream packet that contains the encoded data from multiple signals
as specified in the packet structure.

The input packet can be partially received over multiple sample times. The
Protocol Decoder block has the capability to buffer such partial data until the
complete packet is received.

**Data Types:** `uint8`

### **Length** — Length of data stream packet at Data input port numeric scalar

Optional input port to include the exact length of valid data stream. Use this
option when you know the exact length of the valid data in the input data
stream

This option is useful when you have a communication channel receive peripheral
that outputs partially received data that contains trailing zeros. Such peripherals
also output the length of the actual number of valid data bytes received. You can
connect the length output of the peripheral directly with the **Length** input port of Protocol Decoder block, so that trailing zeros in
the input byte stream do not affect the decoding logic.

#### Dependencies

This input port appears only if you select the **Is input data stream
length available** parameter.

**Data Types:** `uint16`
### Output

### **Field1** — First field decoded by the block scalar

Name of the first field decoded by the block. The name of the output port is
defined using the block parameter, `Field name`. Each subsequent
field that you create while defining the packet structure results in a new output
port, with the `Field name` value appearing as the name of output
port.

The block can have from 1 to `N` output ports.
`N` is the number of fields in the packet structure that you
specify in the **Specify packet fields sequentially** pane.

**Data Types:** `string`

### **IsNew** — New data indicator `0` | `1`

New data indicator returned as a logical. A value of 1 indicates that a new data
is available since the last sample was received by the block. This output can be used
to trigger subsystems to process new data received from the Protocol Decoder block.

If `IsNew` = 0, the block outputs decoded fields from the last
complete packet decoded by the block. If no last sample is available, the block
outputs zeros.

**Data Types:** `Boolean`

### **IsValid** — Checksum validation indicator `0` | `1`

Checksum validation indicator returned as a logical. A value of 1 indicates that
the input packet received by the block is valid when validated using the checksum
logic that you specified. If `IsValid` = 0, the block outputs
zeros.

#### Dependencies

This output port appears only if you select the **Specify logic for
checksum validation** parameter.

**Data Types:** `Boolean`

### **Variable field length** — Actual data length of the last field that is variable-sized numeric scalar

Actual data length of the last field that is variable-sized. The maximum size of
the variable size field can be specified using **Specify maximum length if
last field has variable size** parameter. The block outputs the
variable-sized data as a fixed size data with size that is equal to the maximum length
specified. The output contains actual data followed by trailing zeros. The size of
actual data can be determined using this **Variable Field Length**
output.

#### Dependencies

This output port appears only if you select the **Specify maximum length
if last field has variable size** parameter.

**Data Types:** `double`

### **Variable field lengths** — Actual data lengths of comma separated variables array

Actual data lengths of comma separated variables that are decoded from the input
stream.

This output value (1-by-`N` array) corresponds to the actual data
length of the fields in the packet, where N is the number of comma separated variables
in the packet.

When **Parse comma separated variables** is selected, the
`Output field length` parameter value corresponds to the maximum
size of the field. The actual size of the field is available as the **Variable
field lengths** output.

If the actual field length of nth field is less than
the specified `Output field length` parameter value on the block, the
output corresponding to the field is actual data followed by trailing zeros. The
nth element of the **Variable field
lengths** output provides the actual length corresponding to that variable
in that array.

If the actual field length of nth field is greater than
the specified `Output field length` parameter value on the block, the
output corresponding to the field is truncated and outputted, given the actual packet
size does not exceed maximum packet size. The nth element
of the **Variable field lengths** output provides the actual length
corresponding to that variable in that array.

#### Dependencies

This output port appears only if you select the **Parse comma separated
variables** parameter.

**Data Types:** `double`

## Parameters

### **Parse comma separated variables** — Parse input data that contains comma separated variables array

Specify that the input data to be parsed contains comma separated variables.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Header` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IsParseCSV` |

### **Header** — Header of the packet character array | array of numeric values less than 255

Specify the header that indicates the beginning of the data. The simulation
disregards data that occurs before the header. The header data is not sent to the output
port.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters.

Few examples of header values are: ‘START’, '$’, 36, [36,37].

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Header` |

#### Specify packet fields sequentially

### **Field name** — Name of the field in the packet structure `Field1` (default) | string

Specify the name of the field included in the packet structure. This name appears as
the name of the output port.

To add a new packet field and specify its properties, click
**Add**. After adding a field, click **Move Up** or
**Move Down** to change its sequence in the structure.

To delete a field and its properties, select the row and click
**Delete**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FieldNames` |

### **Output field length** — Length of the field in the packet structure as per the data type `1` (default) | numeric scalar

Length of the field in the packet structure as per the data type that you enter in
the next column (`Output field data type`). For example, if the
`Output field data type` of a field is `uint16` and
the length is 1, the decoder reads two bytes from the packet as per the packet structure
and combine these bytes to output a `uint16` value.

If you select **Parse comma separated variables** parameter, the
`Output field length` value corresponds to the maximum length that
the field can have.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FixedSizeFieldLength` |

### **Output field data type** — Data type of the field `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

Select the output data type of the field.

**Note**

`double` is considered as 8 bytes. If your hardware does not
support 8 bytes `double`, selecting this data type might give
incorrect results.

**Note**

If you select the **Parse comma separated variables** parameter,
you cannot edit this parameter (the **Output field data type** is set
to `uint8` always).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FixedFieldDataTypes` |

### **Byte order** — Endianess of the field in the packet `Little endian` (default) | `Big endian`

Select the endianess of the packet field to describe the order in which bytes are
transmitted.

**Note**

If you select the **Parse comma separated variables** parameter,
you cannot edit this parameter (the **Byte order** is set to
`Little endian` always).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IsLittleEndian` |

### **Specify maximum length if last field has variable size** — Enable last field to output variable-sized data and specify maximum length of the field numeric scalar

Enable last field of the packet to output variable-sized data and specify the
maximum length of the variable length field, which is present as the last field in the
packet.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxVariableSizeFieldLength` |

### **Specify logic for checksum validation** — Enable the logic for checksum validation and select the logic `XOR of bytes` | `2's complement of sum of bytes` | `Custom algorithm`

Specify the logic to generate checksum for validation using standard algorithms or a
custom algorithm.

If you select `Custom algorithm`, the additional parameters
– **Checksum size** and **File path** – are
enabled.

Checksum bytes are expected to be in the last in the packet (before terminator, if
terminator is available).

If you select the logic as `XOR of bytes`, checksum byte is
expected to be the last byte before terminator. The logic calculates the XOR of all
bytes excluding header, terminator and checksum byte, and compare it with the checksum
byte.

If you select the logic as `2's complement of sum of bytes`,
checksum byte is expected to be the last byte before terminator. The logic calculates
the 2's complement of sum off all bytes excluding header, terminator and checksum byte,
and compare it with the checksum byte.

If you select `Custom algorithm`, you can provide your own
custom logic to validate packet. In this case, checksum bytes are extracted as per the
size specified in the **Checksum size** field.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ChecksumAlgorithm` |

### **Checksum size** — Number of bytes of checksum data numeric scalar

Specify the number of bytes of checksum data. The blocks extracts the checksum bytes
as per the specified size and passes it to the function used for custom algorithm, for
validating the packet. Checksum bytes are expected to be in the last in the packet
(before terminator, if terminator is available).

#### Dependencies

This parameter is enabled only if you select `Custom
algorithm` option under **Specify logic for checksum
validation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ChecksumSize` |

### **File path** — Path of the function (.m) used for custom checksum logic MATLAB path

Specify the path of the function (.m) in which you defined the custom algorithm for
checksum logic. The file must be saved in a directory in the MATLAB path.

#### Dependencies

This parameter is enabled only if you select `Custom
algorithm` option under **Specify logic for checksum
validation** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ChecksumFilepath` |

### **Terminator** — Terminator of the packet `<none>` (default) | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

Specify the terminator that indicates the end of the data. The terminator data is
not sent to the output port.

If you select `Custom Terminator`, you can specify your own
terminator value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TerminatorOption` |

### **Custom terminator** — Custom terminator of the packet character array

Custom terminator that indicates the end of the data. The terminator data is not
sent to the output port.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters.

Few examples of custom terminator values are: ‘END’, '#’

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CustomTerminatorVal` |

### **Is input data stream length available** — Enable additional input for data stream length `off` (default) | `on`

Enable optional input port to include the exact length of valid data stream.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IsInputLengthAvailable` |

## Libraries

Simulink Real-Time / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Decode a uint8 byte stream by specifying the packet structure

The Protocol Decoder block decodes a uint8 byte stream as per the specified
packet structure based on the communication protocol. You can use this block to decode packet
into separate fields, by specifying the header, terminator, name of packet fields in sequence
and their size. You can also validate the packet using the checksum logic that you specify.
These figures show how the Protocol
Encoder and Protocol Decoder can simplify serial
communications.

**Simple Serial Communication without Encoder and Decoder Blocks**

Model slrt\_ex\_serialasciitest\_protocol\_e\_d showing simple serial communications.

**Simple Serial Communication with Encoder and Decoder Blocks**

Model slrt\_ex\_serialasciitest\_protocol\_e\_d modified to show encoder and decoder blocks for simple serial communications.
