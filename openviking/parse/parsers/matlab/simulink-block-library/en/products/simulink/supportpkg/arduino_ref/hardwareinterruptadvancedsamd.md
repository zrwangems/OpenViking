---
type: simulink-block
title: 'Hardware Interrupt SAMD'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Event Scheduling and Interrupt Handling'
documentation_page: 'hardwareinterruptadvancedsamd'
documentation_source_path: 'supportpkg/arduino_ref/hardwareinterruptadvancedsamd.html'
language: en
---

# Hardware Interrupt SAMD

## Ports

### Output

### **Event name** — Generate interrupt request scalar

The block outputs a function call. The number of function call outputs depends on
the number of events you select to serve in an ISR. For example, if you select
**ADC RESRDY** and **Custom event** in the
**Events to serve** section, the block enables **ADC
RESRDY** and **Custom event** output ports.

## Parameters

### **Interrupt group** — Select peripheral ISR `Analog to digital converter (ADC)` (default) | `Timer/Counter for Control Applications (TCC)`

This parameter lists all the available ISRs for a particular type of peripheral in
an Arduino board. The values available in the **Interrupt name**
parameter change depending on the interrupt group you select in this parameter.

### **Interrupt name** — Select ISR `ADC_Handler` (default) | `TCC0_Handler` | `TCC1_Handler` | `TCC2_Handler`

The interrupt name specifies the ISR for the Hardware Interrupt
block. This parameter corresponds to the specific entry in the interrupt vector table of
the Arduino board. The available ISRs depend on the **Interrupt
group**.

#### Dependencies

- To enable the `TCC0_Handler`,
  `TCC1_Handler`, and
  `TCC2_Handler` interrupts, set **Interrupt
  group** to `Timer/Counter for Control Applications
  (TCC)`.
- To enable the `ADC_Handler` interrupt, set
  **Interrupt group** to `Analog to digital converter
  (ADC)`.

### **Interrupt number** — Position of ISR in interrupt vector table `23` (default) | `15` | `16` | `17`

This read-only parameter indicates the position of the ISR in the interrupt vector
table of the Arduino board.

### **Events to serve** — Select events and their execution order `ADC RESRDY` (default) | `ADC OVERRUN` | `Custom event` | `TCC0 overflow` | `TCC0 MCx0` | `TCC0 MCx1` | `TCC0 MCx2` | `TCC0 MCx3` | `TCC1 overflow` | `TCC1 MCx0` | `TCC1 MCx1` | `TCC2 overflow` | `TCC2 MCx0` | `TCC2 MCx1`

Select events or custom events and their respective execution order from the
**Events to serve** group to service events for the
**Interrupt name** that you select. You can select custom events to
execute along with the other events. You can also change the execution order of the
events.

#### Dependencies

- To enable the `TCC0 overflow`, `TCC0 MCx0`,
  `TCC0 MCx1`, `TCC0 MCx2`, `TCC0
  MCx3`, and `Custom event` events, set
  **Interrupt group** to `Timer/Counter for Control
  Applications (TCC)` and **Interrupt name** to
  `TCC0_Handler`.
- To enable the `TCC1 overflow`, `TCC1 MCx0`,
  `TCC1 MCx1`, and `Custom event` events, set
  **Interrupt group** to `Timer/Counter for Control
  Applications (TCC)` and **Interrupt name** to
  `TCC1_Handler`.
- To enable the `TCC2 overflow`, `TCC2 MCx0`,
  `TCC2 MCx1`, and `Custom event` events, set
  **Interrupt group** to `Timer/Counter for Control
  Applications (TCC)` and **Interrupt name** to
  `TCC2_Handler`.
- To enable the `ADC RESRDY`, `ADC OVERRUN`,
  and `Custom event` events, set **Interrupt
  group** to `Analog to digital converter (ADC)`
  and **Interrupt name** to
  `ADC_Handler`.

### **Simulink task priority** — Set priority of ISR `30` (default) | positive integer or non-negative integer

The value you specify in this parameter sets the priority of the downstream
function-call subsystem. The task priority in Simulink for the ISR is relative to the priority of the base rate that you set in
the Simulink model.

**Note**

The default priority of the base rate in the Simulink model is `40`, with a lower priority value indicating
a higher priority. To achieve this, in the Configuration Parameters dialog box,
select **Higher priority value indicates higher task
priority** in the **Solver** pane.

### **Run interrupt service routine as atomic unit** — Select to disable interrupt preemption `off` (default) | `on`

Select this parameter to block all other interrupts while executing the current
ISR(s).

### **Clear status after servicing each event** — Select to clear interrupt status flags `off` (default) | `on`

Select this option to clear all the interrupt status flags after servicing each
event.

## Libraries

Simulink Support Package for Arduino Hardware / Advanced / SAMD

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Trigger downstream function-call subsystems from interrupt service routine for Arduino SAMD21 core

Use the Hardware Interrupt block to create an interrupt service routine
(ISR) automatically in the generated code of your Simulink® model for the selected interrupts. The ISR executes the downstream function-call
subsystem associated with event ports of the block.

The function call subsystem associated with the event output port run at the same priority
as the ISR.

Using this block, you can:

- Create an ISR on the Arduino® board.
- Set priority for an ISR.
- Enable or disable interrupt preemption.

This block generates code only for the ISR and events that you select or specify. To
change the configuration, enable the interrupt, and specify triggering options, use the
settings of the selected peripherals. For example, to create an ISR for the ADC peripheral on
the Hardware Interrupt block:

- Your Simulink model must have an Analog Input
  block. In the block, select the **Enable end of conversion interrupt**
  parameter.
- In the Hardware Interrupt block, set these parameters:

  - **Interrupt group** to `Analog to digital
    converter`
  - **Interrupt name** to
    `ADC_Handler`
  - **Events to serve** to `ADC RESRDY`
    or `ADC OVERRUN`

Similarly, to create an ISR for the PWM peripheral on the Hardware
Interrupt block:

- Your Simulink model must have a PWM block. In
  the block, select the **Enable compare match (MCx) interrupt** or
  **Enable overflow/underflow (OVF) interrupt** parameter or both the
  parameters.
- In the Hardware Interrupt block, set these parameters:

  - **Interrupt group** to `Timer/Counter for Control
    Applications (TCC)`.
  - **Interrupt name** to either
    `TCC0_Handler`,
    `TCC1_Handler`, or
    `TCC2_Handler`.
  - **Events to serve** to `TCCx
    overflow`, `TCCx MCx`.

**Note**

The Hardware Interrupt block supports C/C++ code generation. This
feature allows you to generate C and C++ code using Embedded Coder®.

### Supported Arduino Boards

- Arduino MKR 1000
- Arduino MKR ZERO
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
