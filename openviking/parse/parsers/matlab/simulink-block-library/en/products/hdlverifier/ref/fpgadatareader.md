---
type: simulink-block
title: 'FPGA Data Reader'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'HDL Verifier Supported Hardware / Intel FPGA Boards / FPGA Data Capture'
documentation_page: 'fpgadatareader'
documentation_source_path: 'ref/fpgadatareader.html'
language: en
---

# FPGA Data Reader

## Ports

### Output

### **Capture\_Window** — Current capture window scalar

This output port indicates the current capture window. The value of
this output port is an integer from 1 to the value of the
**Sample depth** parameter.

### **Trigger\_Position** — Position of trigger detection clock cycle within capture buffer Boolean scalar

This output port indicates the position of the trigger detection clock
cycle within a capture buffer.

## Parameters

#### Main

### **Sample time** — Rate of output signals `double`

The block returns one frame of data per time step, where the frame is the
entire capture buffer for each signal. Each frame contains **Sample
depth** values, as specified at generation time. The default
sample time provides for unbuffering each frame into single samples, which
results in a sample time of 1.

#### Trigger

### **Sample depth** — Number of samples captured for each signal integer

This parameter is read-only. It reflects the value you specified at
generation time.

### **Storage type** — Type of memory for storing captured data `Internal memory` | `External memory`

This parameter is read-only. It reflects the value you specified at
generation time.

### **Number of capture windows** — Number of data capture recurrences `1` (default) | integer power of two

Specify the number of recurrences to capture. This value must be a power
of two, up to **Sample depth**. A *window
depth* is defined as **Sample depth** /
**Number of capture windows**. Consider the
**Number of capture windows** when setting the
**Sample depth**, to allow for sufficient buffering.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **Storage type** to
`Internal memory`.

### **Number of trigger stages** — Number of trigger stages for providing trigger conditions *M* (default) | integer from 1 to *M*

Specify the number of trigger stages. This value must be an integer from 1
to *M*, where *M* is set by the **Max
trigger stages** parameter of the FPGA Data Capture Component
Generator tool. When you specify the **Max trigger
stages** parameter, consider the maximum number of trigger
stages in which you plan to configure the trigger conditions to capture
data.

### **Trigger position** — Position of trigger detection cycle within capture buffer `0` (default) | integer up to *window depth*–1

By default, the clock cycle when the trigger is detected is the first
sample of the capture buffer. You can change the relative position of the
trigger detection cycle within the capture buffer. A nondefault trigger
position means that some samples are captured before the trigger occurs. You
can set this parameter to any number between 0 and *window
depth*–1, inclusive. When the trigger position is equal to the
*window depth*–1, the last sample corresponds to the
cycle when the trigger occurs. If **Number of capture
windows** is greater than one, the same trigger position
applies to all windows. See Triggers.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **Storage type** to
`Internal memory`.

### **Signal** — Trigger component signal name character vector

This parameter is read-only. The signal names you specified at generation
time are listed in the drop-down menu at the bottom. Click the
**+** button to add a signal to the trigger
condition.

### **Operator** — Operator to compare signals within trigger condition `==` | `!=` | `<` | `>` | `<=` | `>=`

To compare signals, select one of these operators: `==`,
`!=`, `<`, `>`,
`<=`, or `>=`. To compare signals
containing `X` or `x` (don't-care value),
specify either `==` or `!=`
operator.

### **Value** — Value to compare signal to as part of overall trigger condition decimal | binary | hexadecimal | `Low` | `High` | `Rising edge` | `Falling edge` | `Both edges`

The trigger condition can be composed of value comparisons of one or more
signals. This parameter specifies the value to match for each signal.

For a multi-bit signal, specify a decimal, binary, or a hexadecimal value
within the range of the data type associated with the signal. While
providing hexadecimal or binary values, you can provide values with a
combination of `X` or `x` (don't care
value) to enable bit masking. While comparing the values, the trigger
condition discards place values with `X` or
`x` and provides the output.

To separate a group of bits for better readability, you can use
`_` between bits. For example, you can represent a
32-bit binary value as
`0b1010_XXXX_1011_XXXX_1110_XXXX_1111XXXX` and a 32-bit
hexadecimal value as `0xAB_CDEXFX`.

For `boolean` signals, select a level or edge condition.
See Triggers.

### **Trigger combination operator** — Logical operator to combine comparisons of individual signals into overall trigger condition `AND` (default) | `OR`

This parameter is indicated by the logic gate icon. Click the
**Change operator** button to toggle between
`AND` and `OR`.

Icon representing the AND logic gate operator

The trigger condition can be composed of value comparisons
of one or more signals. Combine these value comparisons with only one type
of logical operator. Suppose three signals, `A`,
`B`, and `C`, make up the trigger
condition. The options
are:

```
A == 10 AND B == 'Falling edge' AND C == 0
```

or

```
A == 10 OR B == 'Falling edge' OR C == 0
```

You
cannot mix and match the combination operators. See Triggers.

### **Trigger time out** — Maximum number of data capture IP core clock cycles within which trigger condition must occur in a trigger stage `1` (default) | integer from 1 to 65,536

Within this many data capture IP core clock cycles, the trigger condition
must occur in a trigger stage in which you are enabling this parameter. You
can specify any integer value from 1 to 65,536 according to your
requirements. Select this parameter to enable trigger time out in a trigger
stage. A trigger time out is not allowed in **Trigger Stage
1**.

### **Time out** — Number of seconds to wait before aborting data capture, if the trigger condition is not met `10` (default) | positive integer

If a trigger condition is enabled, but the HDL IP core does not detect the
condition, the data capture request times out after this many seconds. No
data is returned to Simulink.

#### Capture Condition

### **Enable capture condition logic** — Option to enable capture condition logic `off` (default) | `on`

Select this parameter to enable capture condition logic in the data
capture IP core. Enable capture condition logic to use a capture condition
to control which data to capture from the FPGA. The data capture IP core
evaluates the capture condition at each clock cycle and captures only the
data that satisfies the capture condition. For more information on capture
conditions, see Capture Conditions.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, select **Include capture condition
logic**.

### **Signal** — Capture component signal name character vector

This parameter is read-only. The signal names you specified as triggers at
generation time are listed in the drop-down menu at the bottom. Click the
**+** button to add a signal to the capture
condition.

#### Dependencies

To enable this parameter, select **Enable capture condition
logic**.

### **Operator** — Operator to compare signals within capture condition `==` | `!=` | `<` | `>` | `<=` | `>=`

To compare signals, select one of these operators: `==`,
`!=`, `<`, `>`,
`<=`, or `>=`. To compare signals
containing `X` or `x` (don't-care value),
specify either `==` or `!=`
operator.

#### Dependencies

To enable this parameter, select **Enable capture condition
logic**.

### **Value** — Value to compare signal to as part of overall capture condition decimal | binary | hexadecimal | `Low` | `High` | `Rising edge` | `Falling edge` | `Both edges`

The capture condition can be composed of value comparisons of one or more
signals. This parameter specifies the value to match for each signal.

For a multi-bit signal, specify a decimal, binary, or a hexadecimal value
within the range of the data type associated with the signal. While
providing hexadecimal or binary values, you can provide values with a
combination of `X` or `x` (don't care
value) to enable bit masking. While comparing the values, the capture
condition discards place values with `X` or
`x` and provides the output.

To separate a group of bits for better readability, you can use
`_` between bits. For example, you can represent a
32-bit binary value as
`0b1010_XXXX_1011_XXXX_1110_XXXX_1111XXXX` and a 32-bit
hexadecimal value as `0xAB_CDEXFX`.

For `boolean` signals, select a level or edge condition.
See Capture Conditions.

#### Dependencies

To enable this parameter, select **Enable capture condition
logic**.

### **Capture condition combination operator** — Logical operator to combine comparisons of individual signals into overall capture condition `AND` (default) | `OR`

This parameter is indicated by the logic gate icon. Click the
**Change operator** button to toggle between
`AND` and `OR`.

Icon representing the AND logic gate operator

The capture condition can be composed of value comparisons
of one or more signals. Combine these value comparisons with only one type
of logical operator. You cannot mix and match the combination operators. See
Capture Conditions.

#### Dependencies

To enable this parameter, select **Enable capture condition
logic**.

#### Data Types

### **Signal Name** — Name of output port character vector

This parameter is read-only. It reflects the name of the
**Capture\_Window** output port, the name of the
**Trigger\_Position** output port, and the signal names
you specify at generation time.

### **Bit Width** — Number of bits in signal positive integer

This parameter is read-only. It reflects the value you specified at
generation time.

### **Data Type** — Data type for captured data built-in type | `numerictype`

The **Data Type** menu provides data type suggestions
that match the bit width of the captured signal. This size is the width you
specified for the port on the generated IP. You can type in this field to
specify a custom data type. If the signal is 8, 16, or 32 bits, the default
is `uint`. If the signal has one bit, the default is
`boolean`. If the signal is a different width, the
default is `numerictype(0,bitWidth,0)`.

The block supports these data types, depending on the signal bit width:
`boolean`, `uint8`,
`int8`, `uint16`,
`int16`, `half`,
`uint32`, `int32`,
`single`, `uint64`,
`int64`, `double`, and
`numerictype`.

If your development board has multiple FPGAs or multiple JTAG
connections, the data capture software cannot detect the location
of your FPGA in the JTAG chain. Specify these advanced parameters
to locate the FPGA that contains the data capture IP core.

#### Advanced

### **JTAG cable name** — Name of JTAG cable used for data capture `auto` (default) | character vector

Name of the JTAG cable used for data capture, specified as a character
vector. Use this parameter when the board is connected to two JTAG cables of
the same type.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component Generator
tool, set the **Connection type** parameter to
`JTAG`.

### **JTAG cable type** — Type of JTAG cable used for communication with FPGA board (AMD® only) `auto` (default) | `FTDI`

Specify this parameter if more than one JTAG cable is connected to the
host computer. When not specified, the FPGA Data Reader block
will auto-detect the JTAG cable type, in the following order:

- The FPGA Data Reader block first searches for a
  Digilent® cable.
- If it does not find a Digilent JTAG cable, it searches for an FTDI cable.
- If it finds two cables of the same type, the object returns an
  error. Set this parameter to resolve it.
- If it finds two cables of different types, it will prioritize
  the Digilent cable. To use an FTDI cable, set this parameter to
  `FTDI`.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `JTAG`.

### **JTAG chain position** — Position of FPGA in JTAG scan chain (AMD only) `0` (default) | positive integer

Position of the FPGA in the JTAG scan chain, specified as a positive
integer.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `JTAG`.

### **Instruction registers before FPGA** — Instruction register lengths before FPGA (AMD only) `0` (default) | nonnegative integer

Number of instruction register lengths before the FPGA, specified as a
nonnegative integer.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `JTAG`.

### **Instruction registers after FPGA** — Instruction register lengths after FPGA (AMD only) `0` (default) | nonnegative integer

Number of instruction register lengths after the FPGA, specified as a
nonnegative integer.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `JTAG`.

### **JTAG clock frequency in MHz** — JTAG clock frequency (AMD only) `15` (default) | integer

Specify the JTAG clock frequency, in MHz. For AMD FPGAs, the JTAG clock frequency is 33 or 66 MHz. The JTAG
frequency depends on the type of cable and the maximum clock frequency
supported by the FPGA board.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `JTAG`.

### **External DDR memory base address** — Base address of external DDR memory (AMD only) `8000000` (default) | numeric value

Specify the base address of the external DDR memory as a numeric value.
Use this value to indicate where you want to store the captured data in the
DDR memory.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD`, **Connection type**
to `JTAG`, and **Storage
type** to `External
memory`.

### **Device IP address** — IP address of Ethernet port or USB Ethernet gadget on FPGA or SoC board (AMD only) dotted-quad value

Specify the internet protocol (IP) address of the Ethernet port or USB
Ethernet gadget on the FPGA or SoC board as a dotted-quad value. The device
IP address must be a set of four numbers consisting of integers in the range
from 0 to 255 that are separated by three dots. The default IP address for
the PL Ethernet or PS Ethernet interface is `192.168.0.2`.
The default IP address for the USB Ethernet interface is
`192.168.1.2`.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `PL Ethernet`,
`PS Ethernet`, or `USB
Ethernet`.

### **Device Port address** — UDP port number of FPGA board (AMD only) `50101` (default) | integer from 255 to 65,535

Specify the user datagram protocol (UDP) port number of the FPGA board as
an integer from 255 to 65,535.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `PL Ethernet`.

### **Data Capture IP core base address** — Base address of data capture HDL IP core (AMD only) `40000000` (default) | numeric value

Specify the base address of the data capture HDL IP core as a numeric
value.

#### Dependencies

To enable this parameter, in the FPGA Data Capture Component
Generator tool, set **FPGA vendor** to
`AMD` and **Connection
type** to `PS Ethernet` or
`USB Ethernet`.

## Libraries

Generated

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Capture data from live FPGA into Simulink model

The FPGA Data Reader block communicates with a generated IP core on an FPGA to
return captured data into Simulink®.

The data capture workflow consists of three key steps: generating the data capture IP, integrating it with the existing FPGA design, and capturing the data. Use this block during the data capture step to transfer the captured data into Simulink.

Before you run this block, you must generate the customized data capture components.
Integrate the generated HDL IP core into your project and deploy it to the FPGA. The
block communicates with the FPGA over a JTAG, Ethernet, or USB Ethernet cable. Make sure
that the required cable is connected between the board and the host computer.

For a workflow overview, see Data Capture Workflow.

By default, the FPGA Data Capture Component Generator tool
generates a data capture model that contains this block and a scope. The captured data
is streamed to the Logic Analyzer tool. The Scope block also
shows the captured data. You can add other blocks to the model for analysis,
verification, and display.

Generated data capture model
