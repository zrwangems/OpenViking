---
type: simulink-block
title: 'Hardware Interrupt SAM'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'hardwareinterruptadvancedsam'
documentation_source_path: 'supportpkg/arduino_ref/hardwareinterruptadvancedsam.html'
language: en
---

# Hardware Interrupt SAM

## Ports

### Output

### **Event name** — Generate interrupt request scalar

The block outputs a function call. The number of function call outputs depends on
the number of events you select to serve in an ISR. For example, if you select
**CAN rx** and **Custom event** in the
**Events to serve** section, the block enables **CAN
rx** and **Custom event** output ports.

## Parameters

### **Interrupt group** — Select peripheral ISR `Controller area network (CAN1)` (default) | `Controller area network (CAN0)`

This parameter lists all the available ISRs for a particular type of peripheral in
an Arduino board. The values available in the **Interrupt name**
parameter change depending on the interrupt group you select in this parameter.

### **Interrupt name** — Select ISR `CAN1_Handler` (default) | `CAN0_Handler`

The interrupt name specifies the ISR for the Hardware Interrupt
block. This parameter corresponds to the specific entry in the interrupt vector table of
the Arduino board. The available ISRs depend on the **Interrupt
group**.

#### Dependencies

- To enable the `CAN1_Handler`, set **Interrupt
  group** to `Controller area network
  (CAN1)`.
- To enable the `CAN0_Handler`, set **Interrupt
  group** to `Controller area network
  (CAN0)`.

### **Interrupt number** — Position of ISR in interrupt vector table `15` (default)

This read-only parameter indicates the position of the ISR in the interrupt vector
table of the Arduino board.

### **Event name** — Select events and their execution order `CAN rx` (default) | `Custom event`

Select events or custom events and their respective execution order from the
**Events to serve** group to service events for the
**Interrupt name** that you select. You can select custom events to
execute along with the other events. You can also change the execution order of the
events.

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

Simulink Support Package for Arduino Hardware / Advanced / SAM

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Trigger downstream function-call subsystems from interrupt service routine for Arduino SAM core

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
settings of the selected peripherals. For example, to create an ISR for the CAN communication
peripheral on the Hardware Interrupt block, your Simulink model must have an On-board CAN
Receive or On-board CAN
Transmit block.

**Note**

The Hardware Interrupt block supports C/C++ code generation. This feature
allows you to generate C and C++ code using Embedded Coder®.

### Supported Arduino Board

Arduino Due
