---
type: simulink-block
title: 'External Interrupt'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'externalinterrupt'
documentation_source_path: 'nucleo/ref/externalinterrupt.html'
language: en
---

# External Interrupt

## Ports

### Input

### **SimIRQ** — Pin input for simulation purpose scalar

During simulations you can simulate an input to the block by
connecting a boolean signal from the Simulink library to the **SimIRQ** port. If the
input provided to the block is boolean true, the block triggers the
downstream function-call subsystem. If no input is provided, the block
triggers the downstream function-call subsystem until the simulation
continues to run. During code generation, any block that is connected to
this port is ignored and has no effect on the generated code.

#### Dependencies

To enable this port, select the **Enable simulation
input**.

**Data Types:** `Boolean`
### Output

### **IRQ** — Interrupt request scalar | vector

The **IRQ** port connects the downstream Function-Call Subsystem to
be triggered when the selected interrupt occurs.

## Parameters

### **Pin** — Pin name on hardware `5` (default) | `any pin number from pin map of board`

Specify the digital input pin name on the hardware to be used to generate
external interrupts. The pins that can be used for interrupts are different
for different STMicroelectronics® hardware boards.

Click **View pin map** to open the STMicroelectronics Pin Mapping table.

### **Pull mode** — Set hardware pin to logical high or low `Pull-up` (default) | `Pull-down` | `No pull-up or pull-down`

Select one of these modes.

- `Pull-up` – The selected hardware pin is
  set to logical high when no input is connected to the pin.
- `Pull-down` – The selected hardware pin
  is left floating when no input is connected to the pin.
- `No pull-up or pull-down` – The selected
  hardware pin is not set to either logical high or left floating when
  no input is connected to the pin.

### **Trigger type** — Transition on the digital pin that triggers the function call `Rising` (default) | `Falling` | `Either`

Select a **Trigger type** to specify which of these
transitions on the selected pin triggers the downstream function
call.

| Trigger type | Interrupt Trigger Condition |
| --- | --- |
| `Rising` | The digital pin value goes from low to high. |
| `Falling` | The digital pin value goes from high to low. |
| `Either` | The digital pin value goes from either low to high or high to low. |

This figure shows how the block executes the downstream function call as
the pin value changes in different interrupt modes.

### **Enable simulation input** — Option to provide input for simulation purpose `off` (default) | `on`

The parameter enables the **SimIRQ** input port.

### **Initial pin status** — Initial status of input pin `false` (default) | `true`

Select one of these pin status.

- `false` - Initial pin status is
  `0`.
- `true` - Initial pin status is
  `1`.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Trigger the downstream function-call subsystem from an Interrupt Service Routine

The External Interrupt block configures Simulink® to treat the downstream Function-Call Subsystem, connected to the output port of the block, as an
Interrupt Service Routine (ISR). ISR is a section of code that the CPU triggers when the
selected interrupt occurs at the selected pin of the hardware.

During simulations you can provide an input to the External Interrupt block by
connecting a boolean signal from the Simulink library to the input port of the External Interrupt block. If selected
`Trigger type` edge is detected in the boolean input, the block
triggers the downstream function-call subsystem. If you do not provide an input, the
block triggers the downstream function-call subsystem until the simulation continues to
run. During code generation, any simulation block that is connected to the input port of
the External Interrupt block is ignored and has no effect on the generated code.

**Note**

We recommend that you use the External Interrupt block only in the
parent model in a model hierarchy. For more information, refer to Model References.
