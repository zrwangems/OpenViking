---
type: simulink-block
title: 'Push Button'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Programmable Logic IO'
documentation_page: 'pushbutton'
documentation_source_path: 'ref/pushbutton.html'
language: en
---

# Push Button

## Ports

### Input

### **PBIn*`x`*** — Input signal `Boolean` scalar

Input signal to control the hardware logic. Using these ports, you can dynamically
control the hardware logic during simulation at run time. Each push button has a port,
named **PBIn1** to **PBIn***`x`*,
where *`x`* is **Number of push
buttons**.

#### Dependencies

To enable this port, set the **Specify push buttons via**
parameter to `InputPort`.

**Data Types:** `Boolean`
### Output

### **PB*`x`*** — Output signal `Boolean` scalar

Output signal that returns the state of the push button. Each push button has a
port, named **PB1** to
**PB*`x`***, where
*`x`* is **Number of push buttons**.

**Data Types:** `Boolean`

## Parameters

### **Hardware board** — View selected hardware `None` (default) | Supported Xilinx® or Intel ® boards | Custom boards

This parameter is read-only. To choose a hardware board and configure board
parameters, see Hardware Implementation Pane.

### **View push buttons location** — View push buttons button

To view a diagram of the location of the push buttons on the selected hardware
board, click the **View push buttons location** button.

This button is enabled only when you select specific Xilinx or Intel boards. For
more information about these boards, refer to Supported Third-Party Tools and Hardware.

### **IO logic** — IO logic indicator `None` (default) | `Active High` | `Active Low`

This parameter is read-only. Indicates the IO logic level on the selected hardware
board.

When the **IO logic** parameter is shown as **Active
Low**, the Push Button block accepts and outputs active low
signals when you set the **Specify push buttons via** parameter to
`InputPort` and outputs active low signals when you set the
**Specify push buttons via** parameter to
`Dialog`. The block represents these port names prefixed with
letter *n*. For example, **nPB1**.

### **Specify push buttons via** — Push-button source `Dialog` (default) | `InputPort`

To control the hardware logic by using the block parameters, select
`Dialog`. To control the hardware logic from the input port,
select `InputPort`.

### **Number of push buttons** — Push-button selection `1` (default) | list of integers in the range [1, n]

To specify the required number of push-button ports, select a value from the
**Number of push buttons** list. *`n`*
represents the number of available push buttons on the specified hardware board. For
example, if you select `3` from the list, the block shows three
push-button ports.

To use only the *`n`*th push button, set the **Number
of push buttons** parameter to *`n`* and terminate the
unused push button ports.

### **PB*`n`*** — Selected push buttons `Off` (default) | `On`

To enable the *`n`*th push-button port, select
`On` for the PB*`n`* parameter.
*`n`* represents the number of available push buttons on the
specified hardware board.

#### Dependencies

To enable this parameter, set the **Specify push buttons via**
parameter to `Dialog`.

### **Sample time** — Sampling interval -1 (default) | positive scalar

Specify the time interval a push button toggles between `On` and
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

Connect signals attached to push buttons on hardware board

The Push Button block controls the hardware mechanism. The hardware logic
signals connected to a Push Button block are equivalent to the signals
connected to the push buttons on the hardware board.
