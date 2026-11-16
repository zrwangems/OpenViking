---
type: simulink-block
title: 'DIP Switch'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Programmable Logic IO'
documentation_page: 'dipswitch'
documentation_source_path: 'ref/dipswitch.html'
language: en
---

# DIP Switch

## Ports

### Input

### **DSIn*`x`*** — Input signal `Boolean` scalar

Input signal to control the hardware logic. Using this port, you can dynamically
control the hardware logic during simulation at run time. Each DIP switch has a port,
named **DSIn1** to **DSIn***`x`*,
where *`x`* is **Number of DIP
switches**.

#### Dependencies

To enable this port, set the **Specify DIP switches via**
parameter to `InputPort`.

**Data Types:** `Boolean`
### Output

### **DS*`x`*** — Output signal `Boolean` scalar

Output signal that returns the state of the switch. Each DIP switch has a port,
named **DS1** to **DS***`x`*, where
*`x`* is **Number of DIP
switches**.

**Data Types:** `Boolean`

## Parameters

### **Hardware board** — View selected hardware `None` (default) | Supported Xilinx® or Intel ® boards | Custom boards

This parameter is read-only. To choose a hardware board and configure board
parameters, see Hardware Implementation Pane.

### **View DIP switches location** — View DIP switches button

To view a diagram with the location of the DIP switches on the selected hardware
board, click the **View DIP switches location** button.

This button is enabled only when you select specific Xilinx or Intel boards. For
more information about these boards, refer to Supported Third-Party Tools and Hardware.

### **IO logic** — IO logic indicator `None` (default) | `Active High` | `Active Low`

This parameter is read-only. Indicates the IO logic level on the selected hardware
board.

When the **IO logic** parameter is shown as **Active
Low**, the DIP Switch block accepts and outputs active low
signals when you set the **Specify DIP switches via** parameter to
`InputPort` and outputs active low signals when you set the
**Specify DIP switches via** parameter to
`Dialog`. The block represents these port names prefixed with
letter *n*. For example, **nDS1**.

### **Specify DIP switches via** — DIP switch source `Dialog` (default) | `InputPort`

To control the hardware logic by using the block parameters, select
`Dialog`. To control the hardware logic from the input port,
select `InputPort`.

### **Number of DIP switches** — DIP switch selection `1` (default) | list of integers in the range [1, n]

To specify the required number of DIP switch ports, select a value from the
**Number of DIP switches** list. *`n`*
represents the number of available DIP switches on the specified hardware board. For
example, if you select `3` from the list, the block shows three
DIP switch ports.

To use only the *`n`*th DIP switch, set the **Number
of DIP switches** parameter to *`n`* and terminate
the unused DIP switch ports.

### **DS*`n`*** — Selected DIP switches `Off` (default) | `On`

To enable the *`n`*th DIP switch port, select
`On` for the DS*`n`* parameter.
*`n`* represents the number of available DIP switches on the
specified hardware board.

#### Dependencies

To enable this parameter, set the **Specify push buttons via**
parameter to `Dialog`.

### **Sample time** — System sample time `-1` (default) | positive scalar

Specify the time interval a DIP switch toggles between `On` and
`Off`.

## Libraries

SoC Blockset / Hardware Logic I/O

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

Connect signals attached to DIP switches on hardware board

The DIP Switch block controls the hardware logic. The hardware logic
signals connected to a DIP Switch block are equivalent to the signals connected
to the dual inline package (DIP) switches on the hardware board.
