---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/hardwareinterrupt.html'
language: en
---

# Hardware Interrupt

## Ports

Not documented in R2025b.

## Parameters

**Interrupt group**
:   Select an interrupt group.

    **Interrupt group** lists all the interrupt
    groups from your interrupt description file. Selecting an interrupt
    group changes the list of values in the **Interrupt name**  parameter.

**Interrupt name**
:   Select an interrupt service routine (ISR) to be generated.

    The **Interrupt name** corresponds to the specific
    entry in the processor interrupt vector table.

**Interrupt number**
:   This read-only parameter indicates the position of the selected
    ISR in the interrupt vector table of your target hardware.

**Simulink task priority**
:   To set the priority of the downstream function-call subsystem,
    use this parameter. The default model base sample rate priority is
    set to 40 with a lower priority value indicating a higher priority
    task. These settings can be adjusted in the Solver pane of Configuration
    Parameter. The Simulink task priority of the selected interrupt is
    relative to the model base rate priority. Check the **Disable
    interrupt pre-emption** parameter to block all other interrupts
    while executing the selected interrupt service routine.

**Disable interrupt pre-emption**
:   By default, an interrupt can be pre-empted by a higher priority
    interrupt. Selecting this option allows low priority interrupts to
    complete their execution without being pre-empted by other interrupts.

**Add simulation input port**
:   Select this option to enable the SimIRQ block input. The interrupt
    block initiates a function-call in simulation when the SimIRQ input
    is true. However, SimIRQ is ignored in the generated code.

**Interrupt group**
:   Select an interrupt group.

    **Interrupt group** lists all the interrupt
    groups from your interrupt description file. Selecting an interrupt
    group changes the list of values in the **Interrupt name**  parameter.

**Interrupt name**
:   Select an interrupt service routine (ISR) to be generated.

    The **Interrupt name** corresponds to the specific
    entry in the processor interrupt vector table.

**Interrupt number**
:   This read-only parameter indicates the position of the selected
    ISR in the interrupt vector table of your target hardware.

**Simulink task priority**
:   To set the priority of the downstream function-call subsystem,
    use this parameter. The default model base sample rate priority is
    set to 40 with a lower priority value indicating a higher priority
    task. These settings can be adjusted in the Solver pane of Configuration
    Parameter. The Simulink task priority of the selected interrupt is
    relative to the model base rate priority. Check the **Disable
    interrupt pre-emption** parameter to block all other interrupts
    while executing the selected interrupt service routine.

**Disable interrupt pre-emption**
:   By default, an interrupt can be pre-empted by a higher priority
    interrupt. Selecting this option allows low priority interrupts to
    complete their execution without being pre-empted by other interrupts.

**Add simulation input port**
:   Select this option to enable the SimIRQ block input. The interrupt
    block initiates a function-call in simulation when the SimIRQ input
    is true. However, SimIRQ is ignored in the generated code.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Trigger the downstream function-call subsystem from an interrupt service routine.

# Hardware Interrupt

Trigger the downstream function-call subsystem from an
interrupt service routine.

Create an Interrupt Service Routine (ISR) automatically in the
generated code in your model. The ISR executes the downstream function-call
subsystem associated with the block.

You can use this block for the following purposes:

- Use this block to build a processor specific, an ARM
  Cortex-M based core, hardware interrupt block.

  You can customize the block to processor specific interrupts
  by providing an XML based interrupt description file. See Create Hardware Interrupt Block for an ARM Cortex-M Based Processor using an Interrupt Description File.
- Use this block as is, in code generation to respond
  to the Fault and NMI interrupt service routines and trigger a downstream
  function-call subsystem. Make sure the FaultISR and NmiISR are available
  in your interrupt vector table.

Using this block, you can:

- Create ISRs on ARM Cortex-M based processors.
- Set ISR priority.
- Enable or disable interrupt pre-emption.
- Simulate the trigger of the interrupt and the downstream
  subsystem using a simulation input.

For hardware support packages, processor specific blocks are
provided with interrupt description files. In the interrupt description
file, the mask parameters are updated with interrupt groups, names,
and interrupt numbers that match the processor characteristics.

This block only generates code for the specified ISR. The configuration
to enable the interrupt and specific triggering options should be
done in the peripheral settings.

- Hardware Interrupt block
