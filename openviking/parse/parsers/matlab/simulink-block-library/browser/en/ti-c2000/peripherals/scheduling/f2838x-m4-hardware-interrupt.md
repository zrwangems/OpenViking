---
type: simulink-block
title: 'F2838x-M4 Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / Arm Cortex - M3/M4'
documentation_page: 'f2838xm4hardwareinterrupt'
documentation_source_path: 'ref/f2838xm4hardwareinterrupt.html'
language: en
---

# F2838x-M4 Hardware Interrupt

## Ports

### Input

### **SimIRQ** — Simulation interrupt input port scalar

The interrupt block initiates a function call in simulation when you enable the
SimIRQ input port. However, **SimIRQ** is ignored in the generated
code.

#### Dependencies

To enable the **SimIRQ** port, select the **Add
simulation input port** parameter.

**Data Types:** `Boolean`
### Output

### **IRQ** — Generate interrupt request `Scalar`

The output of this block is a function call. The size of the function call line
equals the number of interrupts the block is set to handle.

## Parameters

### **Interrupt group** — Select an interrupt group `Cortex-M Exceptions` (default) | `MCANSS` | `ECAT` | `DCAN` | `EMAC` | `UART` | `SSI` | `I2C` | `USB` | `DMA` | `DMA` | `IPC` | `FMC` | `AES` | `Timer` | `Errors`

**Interrupt group** lists all the interrupt groups from your
interrupt description file. Selecting an interrupt group changes the list of values in
the **Interrupt name** parameter.

### **Interrupt name** — Select ISR `NMI_Handler` (default) | `HardFault_Handler` | `…`

The **Interrupt** name corresponds to the specific entry in the
processor's interrupt vector table. The available ISRs depend on the interrupt
group

### **Interrupt number** — Read only parameter `-14` (default) | `0` | `5` | `…`

This read-only parameter indicates the position of the selected ISR in the
interrupt vector table of your target hardware.

### **Simulink task priority** — Set priority of downstream function call `30` (default) | positive integer or nonnegative integer

The value you specify in this parameter sets the priority of the downstream
function-call subsystem. The simulink task priority of the selected (ISR) is relative
to the model base rate priority.

**Note**

The default model base sample rate priority is set to 40 with a lower priority
value indicating a higher priority task. To achieve this the **Higher
priority value indicates higher task priority** option is disabled in
the **Solver** pane in the **Configuration
Parameters**.

### **Disable interrupt pre-emption** — Select to disable interrupt preemption `off` (default) | `on`

By default, an interrupt can be preempted by a higher priority interrupt.
Selecting this option allows low priority interrupts to complete their execution
without being preempted by other interrupts.

### **Add simulation input port** — Select to enable input port off (default) | on

Select this option to enable the **SimIRQ** input. The Interrupt
block initiates a function call in simulation when you enable the SimIRQ input port.
However, **SimIRQ** is ignored in the generated code.

## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / Scheduling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Trigger downstream function-call subsystem from interrupt service routine

Use the F2838x-M4 Hardware Interrupt block to create an interrupt service routine (ISR)
automatically in the generated code of your model. The ISR executes the downstream
function-call subsystem associated with the block.

Using this block you can:

- Create ISRs on TI C2000 ARM Cortex-M4.
- Set ISR priority.
- Enable or disable interrupt preemption.
- Simulate the trigger of the interrupt and the downstream subsystem using a
  simulation input.

This block generates code only for the specified ISR. To change the configuration to
enable the interrupt and specific triggering options use the settings of the chosen
peripheral.

For example, to create an ISR for the UART peripheral on the Hardware Interrupt block,
select `UART` in the **Interrupt group** parameter and
`UART0INT_Handler` in the **Interrupt name** parameter.
To create an ISR on the UART Transmit and the UART Receive blocks, set the
**Interrupt name** parameter to
`UART0INT_Handler`.

To trigger an ISR from a UART Transmit block, select the **Enable Transmit
Interrupt** check box in **Configuration Parameters > Hardware
Implementation > Target Hardware Resources > UART**. Selecting this check box has
no effect if your model does not have a UART Transmit block.

An ISR from a UART Receive block is automatically triggered when you choose the
necessary Hardware Interrupt block settings because the **Enable Receive
Interrupt** check box is selected by default in **Configuration
Parameters > Hardware Implementation > Target Hardware Resources > UART**.

**Note**

Use MCAN Interrupt Status block inside the interrupt function call
subsystem to clear the source of interrupt.
