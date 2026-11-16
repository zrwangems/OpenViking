---
type: simulink-block
title: 'CAN FD Pack'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN FD Communication'
documentation_page: 'canfdpack'
documentation_source_path: 'ug/canfdpack.html'
language: en
---

# CAN FD Pack

## Ports

### Input

### **Data** — CAN FD message signal input single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

The CAN FD Pack block has one input port by default. The number of
block inputs is dynamic and depends on the number of signals that you specify for the
block. For example, if your message has four signals, the block can have four input
ports.

The block supports the following input signal data types: single, double, int8,
int16, int32, int64, uint8, uint16, uint32, uint64, and boolean. The block does not
support fixed-point data types.

**Tip**

Even if you have a zero-length message with no signals, you still must provide
dummy data to the input port, for purposes of defining the sample time. In this
case, the data value itself is ignored.

### **CAN Msg ID** — CAN message identifier single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

The CAN Msg ID input port allows you to dynamically specify the CAN message
identifier. This port exists only when the **Specify CAN identifier from input port** parameter is
selected. For more information, see Dynamically Change CAN IDs by CAN Pack Block Input Ports.
### Output

### **Msg** — CAN FD message output `CAN_FD_MESSAGE_BUS`

This block has one output port, Msg. The CAN FD Pack block takes
the specified input signals and packs them into a CAN FD message, output as a
Simulink
`CAN_FD_MESSAGE_BUS` signal. For more information on Simulink bus objects, see Composite Interfaces (Simulink).

## Parameters

### **Data input as** — Select your data signal `raw data` (default) | `manually specified signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`: Input data as a uint8 vector array. If you select
  this option, you only specify the message fields. All other signal parameter fields
  are unavailable. This option opens only one input port on your block.

  The conversion formula is:

  ```
  raw_value = (physical_value - Offset) / Factor
  ```

  where `physical_value` is the original value of the signal and
  `raw_value` is the packed signal value.
- `manually specified signals`: Allows you to specify data signal
  definitions. If you select this option, use the **Signals** table
  to create your signals. The number of block inputs depends on the number of signals
  you specify.
- `CANdb specified signals`: Allows you to specify a CAN database
  file that contains message and signal definitions. If you select this option, select
  a CANdb file. The number of block inputs depends on the number of signals specified
  in the CANdb file for the selected message.
- `ARXML specified signals`: Allows you to specify an ARXML file
  for signal definitions. This disables some remote options. After reading data from
  the ARXML file, you can switch to `manually specified signals` to
  further modify the table.

  For detailed information, see ARXML File Support for CAN in Simulink.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataFormat` |
| **Type:** `string` | `character vector` |
| **Values:** `'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` `'ARXML specified signals'` |
| **Default:** `'raw data'` |

### **Database file** — ARXML or CAN database file character vector

This option is available if you specify the **Data is input as**
parameter as `CANdb specified signals` or `ARXML specified
signals`. Click **Browse** to find the database
file on your system. The message list specified in the database file populates the
**Message** section of the dialog box. The database file also
populates the **Signals** table for the selected message. File names
that contain non-alphanumeric characters such as equal signs, ampersands, and so on are
not valid database file names. You can use periods in your database name. Before you use
the database files, rename them with non-alphanumeric characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CANdbFile` |
| **Type:** `string` | `character vector` |

### **Message list** — CAN message list array of character vectors

This option is available if you specify a database in the **Data is input
as** field and you specify a database file in the **Database
file** field. Select the message to display signal details in the
**Signals** table.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgList` |
| **Type:** `string` | `character vector` |

### **Name** — CAN FD message name `CAN Msg` (default) | character vector

Specify a name for your CAN FD message. The default is `CAN Msg`.
This option is available if you choose to input raw data or manually specify signals.
This option is not available if you choose to use signals from a database file.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgName` |
| **Type:** `string` | `character vector` |

### **Protocol mode** — CAN FD message protocol `CAN FD` (default) | `CAN`

Specify the message protocol mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ProtocolMode` |
| **Type:** `string` | `character vector` |
| **Values:** `'CAN FD'` | `'CAN'` |
| **Default:** `'CAN FD'` |

### **Identifier type** — CAN identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Specify whether your CAN message identifier is a `Standard` or an
`Extended` type. The default is `Standard`. A
standard identifier is an 11-bit identifier and an extended identifier is a 29-bit
identifier. This option is available if you choose to input raw data or manually specify
signals. For database specified signals, the **Identifier type**
inherits the type from the database.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgIDType` |
| **Type:** `string` | `character vector` |
| **Values:** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **Default:** `'Standard (11-bit identifier)'` |

### **Identifier** — Message identifier `0` (default) | `0 .. 536870911`

Specify your message ID. This number must be a positive integer from 0 through 2047
for a standard identifier and from 0 through 536870911 for an extended identifier. You
can also specify hexadecimal values by using the `hex2dec` function. This option is available if you choose to input raw data
or manually specify signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgIdentifier` |
| **Type:** `string` | `character vector` |
| **Values:** `'0'` to `'536870911'` |

### **Specify CAN identifier from input port** — CAN message ID value `off` (default) | `on`

When selected, you can dynamically control the CAN identifier (CAN ID) by specifying
the value through an input port on the block. Selecting this option adds an input port
named CAN Msg ID.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CANIDInput` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Length (bytes)** — CAN FD message length `8` (default) | `0` to `64`

Specify the length of your message. For CAN messages the value can be 0 to 8 bytes;
for CAN FD the value can be 0 to 8, 12, 16, 20, 24, 32, 48, or 64 bytes. If you are
using database specified signals for your data input, the database file defines the
length of your message. This option is available if you choose to input raw data or
manually specify signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MsgLength` |
| **Type:** `string` | `character vector` |
| **Values:** `'0'` to `'8'`, `'12'`, `'16'`, `'20'`, `'24'`, `'32'`, `'48'`, `'64'` |
| **Default:** `'8'` |

### **Remote frame** — CAN message as remote frame `off` (default) | `on`

(Disabled for CAN FD protocol mode.) Specify the CAN message as a remote
frame.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Remote` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Bit Rate Switch (BRS)** — Enable bit rate switch `off` (default) | `on`

(Disabled for CAN protocol mode.) Enable bit rate switch.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BRSSwitch` |
| **Type:** `string` | `character vector` |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Add signal** — Add CAN FD signal

Add a signal to the signal table.

#### Programmatic Use

None

### **Delete signal** — Remove CAN FD signal

Remove the selected signal from the signal table.

#### Programmatic Use

None

### **Signals** — Signals table table

This table appears if you choose to specify signals manually or define signals by
using a database file.

If you are using a database file, the data in the file populates this table and you
cannot edit the fields. To edit signal information, switch to manually specified
signals.

If you have selected to specify signals manually, create your signals in this table.
Each signal that you create has these values:

**Name**
:   Specify a descriptive name for your signal. The Simulink block in your model displays this name. The default is
    `Signal [row number]`.

**Start bit**
:   Specify the start bit of the data. The start bit is the least significant bit
    counted from the start of the message data. For CAN the start bit must be an
    integer from 0 through 63, for CAN FD 0 through 511, within the number of bits in
    the message. (Note that message length is specified in bytes.)

**Length (bits)**
:   Specify the number of bits the signal occupies in the message. The length must
    be an integer from 1 through 64. The sum of all the signal lengths in a message is
    limited to the number of bits in the message length; that is, all signals must
    cumulatively fit within the length of the message. (Note that message length is
    specified in bytes and signal length in bits.)

**Byte order**
:   Select either of these options:

    - `LE`: Where the byte order is in little-endian format
      (Intel®). In this format you count bits from the least significant bit,
      to the most significant bit. For example, if you pack one byte of data in
      little-endian format, with the start bit at 20, the data bit table resembles
      this figure.

      **Little-Endian Byte Order Counted from the Least-Significant Bit to
      the Highest Address**
    - `BE`: Where byte order is in big-endian format
      (Motorola®). In this format you count bits from the least-significant bit
      to the most-significant bit. For example, if you pack one byte of data in
      big-endian format, with the start bit at 20, the data bit table resembles this
      figure.

      **Big-Endian Byte Order Counted from the Least Significant Bit to the
      Lowest Address**

    For more information, see CAN Frame Structure, Byte Order, and Bit Counting.

**Data type**
:   Specify how the signal interprets the data in the allocated bits. Choose
    from:

    - `signed` (default)
    - `unsigned`
    - `single`
    - `double`

      Note: If you have a `double` signal that does not align
      exactly to the message byte boundaries, to generate code with Embedded Coder® you must check **Support long long** under
      **Device Details** in the **Hardware
      Implementation** pane of the Configuration Parameters
      dialog.

**Multiplex type**
:   Specify how the block packs the signals into the message at each time
    step:

    - `Standard`: The signal is packed at each time
      step.
    - `Multiplexor`: The
      `Multiplexor` signal, or the mode signal is packed.
      You can specify only one `Multiplexor` signal per
      message.
    - `Multiplexed`: The signal is packed if the value
      of the `Multiplexor` signal (mode signal) at run time
      matches the configured **Multiplex value** of this
      signal.

    For example, a message has four signals with these types and values.

    | Signal Name | Multiplex Type | Multiplex Value |
    | --- | --- | --- |
    | Signal-A | Standard | Not applicable |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | Not applicable |

    In this example:

    - The block packs Signal-A (Standard signal) and Signal-D (Multiplexor
      signal) in every time step.
    - If the value of Signal-D is 1 at a particular time step, then the block
      packs Signal-B along with Signal-A and Signal-D in that time step.
    - If the value of Signal-D is 0 at a particular time step, then the block
      packs Signal-C along with Signal-A and Signal-D in that time step.
    - If the value of Signal-D is not 1 or 0, the block does not pack either of
      the Multiplexed signals in that time step.

**Multiplex value**
:   This option is available only if you have selected the **Multiplex
    type** to be `Multiplexed`. The value you provide here
    must match the `Multiplexor` signal value at run time for
    the block to pack the `Multiplexed` signal. The
    **Multiplex value** must be a positive integer or zero.

**Factor**
:   Specify the **Factor** value to apply to
    convert the physical value (signal value) to the raw value
    packed in the message. See the **Data input
    as** parameter conversion formula to understand how
    physical values are converted to raw values packed into a
    message.

**Offset**
:   Specify the **Offset** value to apply to
    convert the physical value (signal value) to the raw value
    packed in the message. See the **Data input
    as** parameter conversion formula to understand how
    physical values are converted to raw values packed into a
    message.

**Min**, **Max**
:   Define a range of signal values. The default settings are
    `-Inf` (negative infinity) and `Inf`,
    respectively. For database specified signals, these settings are read from the
    database file. For **manually specified signals**, you can
    specify the minimum and maximum physical value of the signal. By default, these
    settings do not clip signal values that exceed them.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SignalInfo` |
| **Type:** `string` | `character vector` |

## Libraries

Vehicle Network Toolbox / CAN FD Communication C2000 Microcontroller Blockset / Target Communication Simulink Real-Time / CAN / CAN-FD MSG blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2025a: Updated parameters: ARXML support

To support ARXML file definitions, the following parameters are updated:

- **Data input as** — Has a new option `ARXML specified
  signals`.

- **CANdb file** — Has been renamed to **Database
  file** in the block mask. Its programmatic name remains
  `CANdbFile`.

### R2024b: New parameter: Specify CAN identifier from input port

The parameter **Specify CAN identifier from input port** adds an
input port **CAN Msg ID**, to support dynamic specifying of CAN identifier.

## Description

Pack individual signals into message for CAN FD bus

The CAN FD Pack block loads signal data into a message at specified intervals during the
simulation.

To use this block, you also need a license for Simulink® software.

The CAN FD Pack block supports:

- The use of Simulink accelerator mode. Using this feature, you can speed up the execution of
  Simulink models. For more information, see Acceleration (Simulink).

**Tip**

- To work with J1939 messages, use the blocks in the J1939 Communication block library
  instead of this block. See J1939 Communication.
