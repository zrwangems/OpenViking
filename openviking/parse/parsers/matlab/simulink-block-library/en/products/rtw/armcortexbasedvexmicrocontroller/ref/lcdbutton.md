---
type: simulink-block
title: 'LCD Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / LCD'
documentation_page: 'lcdbutton'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/lcdbutton.html'
language: en
---

# LCD Button

## Ports

### Input

### **Port\_1** — State of the selected button for simulation purpose scalar

When you select the **Add input port for simulation**
parameter, an input port becomes available.

For simulation behavior, provide the state of the button from this
port via a source block.

Any nonzero value at this port indicates that the button is pressed. A
value of `0` at this port indicates that the button is
released.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Port\_1** — State of the selected button:`1` while pressed and `0` while released scalar

The block outputs the state of the selected button on the LCD Display
Module: `1` while pressed and `0`
while released.

**Data Types:** `double`

## Parameters

### **UART port** — UART port number `UART1` (default) | `UART2`

Select the UART port number on the microcontroller to which the LCD
Display Module is connected.

### **Button** — Button to read the logical state `Left` (default) | `Center` | `Right`

Select the button whose logical state (pressed or released) is to be
read.

### **Add input port for simulation** — Specify if you want to run a normal mode simulation off (default) | on

If you want the normal mode simulation with a source block providing the
input value, select this parameter.

### **Sample time** — Specify how often to read the state of a button `0.2` (default)

Specify how often the block reads the state of the button, in
seconds.

#### Dependencies

If you select the **Add input port for simulation**
parameter, the **Sample time** parameter is hidden and
the value is inherited (Sample time = -1).

## Libraries

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller/LCD

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Read logical state of selected push button on LCD Display Module

The LCD Button block reads the logical state of the selected push
button on the LCD Display Module. To select a push button, use the
**Button** parameter.

The block output is 1 while the button is pressed. The block output is 0 while the
button is released.

There are three buttons on the LCD Display Module: Left, Center, and Right. To control
the peripherals, such as a servo motor that is connected to the VEX microcontroller, use
the values from these buttons.

During simulations, without the hardware, this block emits zeros if there is no source
block connected to the simulation input port. See Block Produces Zeros or Does Nothing in Simulation. To achieve simulation,
connect a source block from the Utilities library in VEX microcontroller library.

During code generation, any simulation block that is connected to the input port of
the LCD Button block is ignored and has no effect on the generated
code.
