---
type: simulink-block
title: 'C29x Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Scheduling'
documentation_page: 'c29xhardwareinterruptblock'
documentation_source_path: 'ref/c29xhardwareinterruptblock.html'
language: en
---

# C29x Hardware Interrupt

## Ports

### Output

### ***`name`* Event** — Generate interrupt request `Scalar`

The output of this block is a function-call. The number of function call
outputs will be same as events selected to serve in an ISR.

## Parameters

### **Interrupt group** — Select a peripheral ISR `External interrupts (EXTI)` (default) | `Analog to digital converter (ADC)` | `Pulse width modulation (PWM)` | `Direct memory access (DMA)`

Interrupt group lists all the ISR for a same type of peripherals. Selecting an
interrupt group changes the list of values in the **Interrupt name**parameter.

### **Interrupt name** — Select ISR `EXTI0_IRQHandler` (default) | `ADC_IRQHandler` | `TIM1_BRK_TIM9_IRQHandler` | `DMA0_Stream0_IRQHandler`

The interrupt name specifies the ISR to be generated for the hardware interrupt
block. The **Interrupt** name corresponds to the specific entry
in the processor's interrupt vector table. The available ISRs depend on the
interrupt group.

### **Interrupt number** — Position of ISR in interrupt table `21` (default) | `33` | `71` | `…`

This read-only parameter indicates the position of the selected ISR in the
interrupt vector table of your target hardware.

### **Events to serve** — Select events `EXTI0 Event` (default) | `ADC1 OVR` | `Stream0 TC` | `…`

Select events or custom event and there respective events execution order from
the **Events to serve** group to service events for the selected
**Interrupt name**. You can select custom events to execute
along with the other selected events. For more information, see Limitations (Embedded Coder).

Events to serve

### **Simulink task priority** — Set priority of selected ISR `30` (default) | `positive integer or nonnegative integer`

The value you specify in this parameter sets the priority of the downstream
function-call subsystem. The Simulink® task priority of the selected (ISR) is relative to the model base
rate priority.

**Note**

The default model base sample rate priority is set to 40 with a lower
priority value indicating a higher priority task. To achieve this the
**Higher priority value indicates higher task priority**
option must be enabled in **Configuration Parameters** >
**Solver** pane.

### **Run interrupt service routine as atomic unit** — Select to disable interrupt preemption `off` (default) | `on`

Enable Run interrupt service routine as atomic unit to block all other
interrupts while executing the selected interrupt service routine.

### **Clear status after servicing each event** — Select to clear interrupt status flags `off` (default) | `on`

Select this parameter to clear event status in interrupt service routine after
executing each event.

## Libraries

C2000 Microcontroller Blockset / F29H85x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Trigger downstream function-call subsystems from interrupt service routine

Use the Hardware Interrupt block to create an interrupt service routine (ISR)
automatically in the generated code of your model to react to the events selected. The ISR
executes the downstream function-call subsystem associated with event ports of the
block.

The function call subsystem associated with the event output port run at same priority
as that of ISR priority.

Using this block you can:

- Create ISRs.
- Set ISR priority.
- Enable or disable interrupt preemption.

This block generates code only for the specified ISR and selected events. To change the
configuration, enable the interrupt and specific triggering options use the settings of the
chosen peripheral.

For example, to create an ISR for the ADC peripheral on the Hardware Interrupt block:

- Model must have an **Analog to digital Converter** (ADC)
  block.
- Select `Analog to digital converter (ADC)` in the
  **Interrupt group** parameter and `ADCA#_INT`
  in the **Interrupt name** parameter from the hardware interrupt
  block.
- Select `EOC event` or `Overflow event` event
  name in the **Events to serve** parameter.

To know more about when not to use the custom event, refer to Limitations (Embedded Coder).
