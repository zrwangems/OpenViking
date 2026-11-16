---
type: simulink-block
title: 'LED'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Programmable Logic IO'
documentation_page: 'led'
documentation_source_path: 'ref/led.html'
language: en
---

# LED

## Ports

### Input

### **LED*`x`*** — Input signal `Boolean` scalar

Input signal from the hardware logic. Each LED has a port, named
**LED1** to **LED*`x`***,
where *`x`* is **Number of LEDs**.

**Data Types:** `Boolean`

## Parameters

### **Hardware board** — View selected hardware `None` (default) | Supported Xilinx® or Intel ® boards | Custom boards

This parameter is read-only. To choose a hardware board and configure board
parameters, see Hardware Implementation Pane.

### **View LEDs location** — View LEDs button

To view a diagram of the location of the LEDs on the selected hardware board, click
the **View LEDs location** button.

This button is enabled only when you select specific Xilinx or Intel boards. For
more information about these boards, refer to Supported Third-Party Tools and Hardware.

### **IO logic** — IO logic indicator `None` (default) | `Active High` | `Active Low`

This parameter is read-only. Indicates the IO logic level on the selected hardware
board.

When the **IO logic** parameter is shown as **Active
Low**, the LED block accepts active low signals and
represents the port names prefixed with letter *n*. For example,
**nLED1**.

### **Number of LEDs** — Number of LED ports `1` (default) | list of integers in the range [1, *n*]

Specify the required number of LED ports by specifying a value from this list.
*`n`* is the number of available LEDs on the specified hardware
board. For example, if you set this parameter to `4`, the block
shows four LED ports.

To use only the *`n`*th LED, set the **Number of
LEDs** parameter to *`n`* and leave the unused LED
ports unconnected.

For the Zynq®
UltraScale+™ RFSoC ZCU216 Evaluation Kit, the first three LED ports represent the first
set of red, green, and blue (RGB) LEDs out of the eight available sets, the next three
LED ports represent the second set of RGB LEDs, and so on. For example, if you set the
**Number of LEDs** parameter to `9`, the
**LED1**, **LED4**, and **LED7**
ports connect to the red LEDs, the **LED2**, **LED5**,
and **LED8** ports connect to the green LEDs, and the
**LED3**, **LED6**, and **LED9**
ports connect to the blue LEDs on the ZCU216 evaluation board.

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

Connect signals attached to LEDs on hardware board

The LED block indicates the status of a signal. The hardware logic signals
connected to an LED block are equivalent to the signals connected to the light
emitting diodes (LED) on the hardware board.
