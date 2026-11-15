---
type: simulink-block
title: 'External Interrupt'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'externalinterrupt'
documentation_source_path: 'supportpkg/raspberrypi_ref/externalinterrupt.html'
language: en
---

# External Interrupt

## Ports

### Input

### **SimIRQ** — Port to provide input for simulation `0` | `1`

During simulation, you can simulate an input to the External
Interrupt block by connecting a source block from the Simulink library to the **SimIRQ** port. If the input provided
to the block is boolean true, the block triggers the downstream function-call
subsystem. The External Interrupt block receives an input value of
`0` or `1` at each time step. When the input at
the block port is `1`, the block executes the Function-Call Subsystem. If you do not provide an input, the block triggers
the downstream function-call subsystem until the simulation continues to run. During
code generation, any Simulink block connected to the input port of the External
Interrupt block is ignored and has no effect on the generated code.

#### Dependencies

To enable this port, select the **Add simulation input port**
parameter.

**Data Types:** `Boolean`
### Output

### **IRQ** — Function-call event output scalar | vector

Sends function-call events to the function-call input port of a function-call
subsystem or model.

## Parameters

### **Board** — Raspberry Pi hardware board `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

Select the Raspberry Pi hardware board.

### **View pin map** — Open pin map button

Click **View pin map** to view the pin mapping diagram associated
with the Raspberry Pi hardware board that you select.

### **Pin** — Raspberry Pi hardware board pin to generate external interrupts `9` (default) | `4` | `17` | `27` | `27` | `22` | `10` | `11` | `14` | `15` | `18` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

Select the digital input pin on the Raspberry Pi hardware to generate external interrupts. When using multiple Raspberry Pi boards, you can select different pins for each of the boards.

### **Pull mode** — Set Raspberry Pi hardware pin to logic high or low `Pull-up` (default) | `Pull-down`

Select one of these modes.

- `Pull-up`: When you select this mode, the pin you set
  in the Pin parameter is pulled up to logic high when no input is connected
  to the pin.
- `Pull-down`: When you select this mode, the pin you
  set in the Pin parameter is pulled down to logic low when no input is connected
  to the pin.

### **Edge selection** — Transition on digital pin that triggers function call `Rising` (default) | `Falling` | `Either`

Select the edge selection mode to specify which signal transitions on the selected
Raspberry Pi hardware pin trigger the downstream function call.

- `Rising`: When the digital pin value goes from low to
  high
- `Falling`: When the digital pin value goes from high
  to low
- `Either`: When the digital pin value goes from either
  low to high or high to low

This figure shows how the block executes the downstream function call as the
hardware pin value changes in different interrupt modes.ISR triggered in different interrupt modes.

**Note**

For any **Edge selection** mode that you select, you can expect
a delay in the downstream function call that is close to the base rate of the
Simulink model.

### **Add simulation input port** — Option to provide input for simulation `off` (default) | `on`

This parameter enables the **SimIRQ** input port. To provide an
input to the block during simulation, connect a source block to the
**SimIRQ** input port. During code generation, any block connected to
the port is ignored and has no effect on the generated code.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Trigger downstream function-call subsystem from interrupt service routine

The External Interrupt block triggers a downstream Function-Call Subsystem from an interrupt service routine (ISR). The Function-Call Subsystem should be connected to the output port of the
External Interrupt block. An ISR is a section of code triggered by the
Raspberry Pi® kernel when the interrupt occurs at the hardware pin you specify.

During simulation, you can provide an input to the External Interrupt block
by connecting a source block from the Simulink® library to the input port of the External Interrupt block. The
External Interrupt block receives an input value of `0` or
`1` at each time step. When the input at the block port is
`1`, the block triggers the downstream function-call subsystem. When the input at the block port is
`0` or when no source of input is connected to the input port of the block,
the block does not trigger the downstream function-call subsystem. During code
generation, any Simulink block connected to the input port of the External Interrupt block
is ignored and has no effect on the generated code.

**Note**

We recommend that you use the External Interrupt block only in the parent
model in a model hierarchy. For more information, refer to Model References.
