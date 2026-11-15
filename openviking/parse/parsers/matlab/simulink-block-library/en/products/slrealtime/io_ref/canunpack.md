---
type: simulink-block
title: 'CAN Unpack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / CAN'
documentation_page: 'canunpack'
documentation_source_path: 'io_ref/canunpack.html'
language: en
---

# CAN Unpack

## Ports

### Input

### **CAN Msg** — CAN message input `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

This block has one input port, **CAN Msg**. The block takes the
specified input CAN messages and unpacks their signal data to separate outputs.

The block supports the following signal data types: single, double, int8, int16,
int32, int64, uint8, uint16, uint32, uint64, and boolean. The block does not support
fixed-point data types.
### Output

### **Data** — CAN signal output single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

The block has one output port by default. The number of output ports is dynamic
and depends on the number of signals that you specify for the block to output. For
example, if your message has four signals, the block can have four output ports.

For signals specified manually or by a database, the default output data type for
CAN signals is double. To specify other types, use a Signal Specification block. This allows
the block to support the following output signal data types: single, double, int8,
int16, int32, int64, uint8, uint16, uint32, uint64, and boolean. The block does not
support fixed-point types.

Additional output ports can be added by selecting the options in the parameters
**Output ports** pane. For more information, see the parameters
`Output identifier`, `Output timestamp`,
`Output error`, `Output remote`, `Output
length`, and `Output status`.

## Parameters

### **Data to output as** — Select your data signal `raw data` (default) | `manually specify signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`: Output data as a uint8 vector array. If you select
  this option, you specify only the message fields. The other signal parameter fields
  are unavailable. This option opens only one output port on your block.

  The conversion formula
  is:

  ```
  physical_value = raw_value * Factor + Offset
  ```

  where `raw_value` is the unpacked signal value and
  `physical_value` is the scaled signal value.
- `manually specified signals`: You can specify data signals. If
  you select this option, use the `Signals` table to create your
  signals message manually. The number of output ports on your block depends on the
  number of signals that you specify. For example, if you specify four signals, your
  block has four output ports.
- `CANdb specified signals`: You can specify a CAN database file
  that contains data signals. If you select this option, select a CANdb file. The
  number of output ports on your block depends on the number of signals specified in
  the CANdb file. For example, if the selected message in the CANdb file has four
  signals, your block has four output ports.
- `ARXML specified signals`: Allows you to specify an ARXML file
  for signal definitions. This disables some remote options. After reading data from
  the ARXML file, you can switch to `manually specified signals` to
  further modify the table.

  For detailed information, see ARXML File Support for CAN in Simulink (Vehicle Network Toolbox).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataFormat` |
| **Type:** `string` | `character vector` |
| **Values:** `'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` | `'ARXML specified signals'` |
| **Default:** `'raw data'` |

### **Database file** — ARXML or CAN database file character vector

This option is available if you specify the **Data to output as**
parameter as `CANdb specified signals` or `ARXML specified
signals`. Click **Browse** to find the database
file on your system. The messages and signal definitions specified in the database file
populate the **Message** section of the dialog box. The signals
specified in the database file populate **Signals** table. File names
that contain non-alphanumeric characters such as equal signs, ampersands, and so forth
are not valid database file names. You can use periods in your database name. Rename
database files with non-alphanumeric characters before you use them.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CANdbFile` |
| **Type:** `string` | `character vector` |

### **Message list** — CAN message list array of character vectors

This option is available if you specify a database for the **Data is input
as** field, and you specify a database file in the **Database
file** field. You can select the message that you want to view. The
**Signals** table then displays the details of the selected message.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgList` |
| **Type:** `string` | `character vector` |

### **Name** — CAN message name `CAN Msg` (default) | character vector

Specify a name for your CAN message. The default is `CAN Msg`. This
option is available if you choose to output raw data or manually specify signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgName` |
| **Type:** `string` | `character vector` |

### **Identifier type** — CAN identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Specify whether your CAN message identifier is a `Standard` or an
`Extended` type. The default is `Standard`. A
standard identifier is an 11-bit identifier and an extended identifier is a 29-bit
identifier. This option is available if you choose to output raw data or manually
specify signals. For database specified signals, the **Identifier
type** inherits the type from the database.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgIDType` |
| **Type:** `string` | `character vector` |
| **Values:** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **Default:** `'Standard (11-bit identifier)'` |

### **CAN Identifier** — CAN message identifier `0` (default) | `0` to `536870911`

Specify your CAN message ID. This number must be an integer from 0 through 2047 for
a standard identifier and from 0 through 536870911 for an extended identifier. If you
specify `-1`, the block unpacks the messages that match the length
specified for the message. You can also specify hexadecimal values by using the
`hex2dec` function. This option is
available if you choose to output raw data or manually specify signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgIdentifier` |
| **Type:** `string` | `character vector` |
| **Values:** `'0'` to `'536870911'` |

### **Length (bytes)** — CAN message length `8` (default) | `0` to `8`

Specify the length of your CAN message from 0 to 8 bytes. If you are using database
specified signals for your output data, the database file defines the length of your
message. Otherwise, this field defaults to `8`. This option is
available if you choose to output raw data or manually specify signals.

Note: When a frame is received whose length is different from the value specified
in the mask or network description file, that frame is discarded.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgLength` |
| **Type:** `string` | `character vector` |
| **Values:** `'0'` to `'8'` |
| **Default:** `'8'` |

### **Add signal** — Add CAN signal

Add a signal to the signal table.

#### Programmatic Use

None

### **Delete signal** — Remove CAN signal

Remove the selected signal from the signal table.

#### Programmatic Use

None

### **Signals** — Signals table table

If you choose to specify signals manually or define signals by using a database
file, this table appears.

If you are using a database file, the data in the file populates this table and you
cannot edit the fields. To edit signal information, switch to specified signals.

If you have selected to specify signals manually, create your signals manually in
this table. Each signal that you create has these values:

**Name**
:   Specify a descriptive name for your signal. The Simulink block in your model displays this name. The default is
    `Signal [row number]`.

**Start bit**
:   Specify the start bit of the data. The start bit is the least significant bit
    counted from the start of the message. The start bit must be an integer from 0
    through 63.

**Length (bits)**
:   Specify the number of bits the signal occupies in the message. The length must
    be an integer from 1 through 64.

**Byte order**
:   Select either of these options:

    - `LE`: Where the byte order is in little-endian format
      (Intel®). In this format you count bits from the least-significant bit
      to the most-significant bit. For example, if you pack one byte of data in
      little-endian format, with the start bit at 20, the data bit table resembles
      this figure.

      **Little-Endian Byte Order Counted from the Least Significant Bit to
      the Highest Address**
    - `BE`: Where the byte order is in big-endian format
      (Motorola®). In this format you count bits from the least-significant bit
      to the most-significant bit. For example, if you pack one byte of data in
      big-endian format, with the start bit at 20, the data bit table resembles this
      figure.

      **Big-Endian Byte Order Counted from the Least Significant Bit to the
      Lowest Address**

**Data type**
:   Specify how the signal interprets the data in the allocated bits. Choose
    from:

    - `signed` (default)
    - `unsigned`
    - `single`
    - `double`

**Multiplex type**
:   Specify how the block unpacks the signals from the CAN message at each time
    step:

    - `Standard`: The
      signal
      is unpacked at each time step.
    - `Multiplexor`: The
      `Multiplexor` signal or the mode signal is
      unpacked. You can specify only one `Multiplexor`
      signal per message.
    - `Multiplexed`: The signal is unpacked if the
      value of the `Multiplexor` signal (mode signal) at
      run time matches the configured **Multiplex value** of this
      signal.

    For example, a message has four signals with these values.

    | Signal Name | Multiplex Type | Multiplex Value |
    | --- | --- | --- |
    | Signal-A | Standard | Not applicable |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | Not applicable |

    In this example:

    - The block unpacks Signal-A (Standard signal) and Signal-D (Multiplexor
      signal) in every time step.
    - If the value of Signal-D is 1 at a particular time step, then the block
      unpacks Signal-B along with Signal-A and Signal-D in that time step.
    - If the value of Signal-D is 0 at a particular time step, then the block
      unpacks Signal-C along with Signal-A and Signal-D in that time step.
    - If the value of Signal-D is not 1 or 0, the block does not unpack either
      of the Multiplexed signals in that time step.

**Multiplex value**
:   This option is available only if you have selected the **Multiplex
    type** to be `Multiplexed`. The value you provide must
    match the `Multiplexor` signal value at run time for the
    block to unpack the `Multiplexed` signal. The
    **Multiplex value** must be a positive integer or zero.

**Factor**
:   Specify the **Factor** value applied to convert the unpacked
    raw value to the physical value (signal value). For more information, see the
    **Data input as** parameter conversion formula.

**Offset**
:   Specify the **Offset** value applied to convert the physical
    value (signal value) to the unpacked raw value. For more information, see the
    **Data input as** parameter conversion formula.

**Min**, **Max**
:   Define a range of raw signal values. The default settings are
    `-Inf` (negative infinity) and `Inf`,
    respectively. For database specified signals, these settings are read from the
    database. For **manually specified signals**, you can specify the
    minimum and maximum physical value of the signal. By default, these settings do
    not clip signal values that exceed them.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignalInfo` |
| **Type:** `string` | `character vector` |

### **Output identifier** — Add CAN ID output port `off` (default)

Select this option to output a CAN message identifier. The data type of this port is
`uint32`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IDPort` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output timestamp** — Add Timestamp output port `off` (default) | `on`

Select this option to output the message timestamp. This value indicates when the
message was received, measured as the number of seconds elapsed since the model
simulation began. This option adds a new output port to the block. The data type of this
port is `double`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimestampPort` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output error** — Add Error output port `off` (default) | `on`

Select this option to output the message error status. This option adds a new output
port to the block. An output value of `1` on this port indicates that
the incoming message is an error frame. If the output value is `0`,
there is no error. The data type of this port is `uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ErrorPort` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output remote** — Add Remote output port `off` (default) | `on`

Select this option to output the message remote frame status. This option adds a new
output port to the block. The data type of this port is `uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemotePort` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output length** — Add Length output port `off` (default) | `on`

Select this option to output the length of the message in bytes. This option adds a
new output port to the block. The data type of this port is
`uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LengthPort` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output status** — Add Status output port `off` (default) | `on`

Select this option to output the message received status. The status is
`1` if the block receives a new message and `0` if
it does not. This option adds a new output port to the block. The data type of this port
is `uint8`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StatusPort` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

## Libraries

Vehicle Network Toolbox / CAN Communication C2000 Microcontroller Blockset / Target Communication Embedded Coder / Embedded Targets / Host Communication Simulink Real-Time / CAN / CAN MSG blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

### R2025a: Updated parameters: ARXML support

To support ARXML file definitions, the following parameters are updated:

- **Data to output as** — Has a new option `ARXML specified
  signals`.

- **CANdb file** — Has been renamed to **Database
  file** in the block mask. Its programmatic name remains
  `CANdbFile`.

## Description

Unpack individual signals from CAN messages

The CAN Unpack block unpacks a CAN message into signal data using the
specified output parameters at every time step. Data is output as individual signals.

To use this block, you also need a license for Simulink® software.

The CAN Unpack block supports:

- The use of Simulink accelerator and rapid accelerator modes. Using this feature, you can speed
  up the execution of Simulink models. For more information, see Acceleration.
- The use of model referencing. Using this feature, your model can include other
  Simulink models as modular components. For more information, see Model References.

**Tip**

- To process every message coming through a channel, do not use the CAN
  Unpack block in a function trigger subsystem. For more information, see
  Speedgoat® documentation.
- This block can be used to decode the signals of J1939 parameter groups up to 8
  bytes. However, to work with J1939 messages, it is preferable to use the blocks in the
  J1939 Communication block library instead of this block.
  See J1939.
