---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-M Processors / Modeling'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'armcortexm/ref/hardwareinterrupt.html'
language: en
---

# Hardware Interrupt

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

**Introduced in R2014b**

## Description

Trigger the downstream function-call subsystem from an interrupt service routine.

# Hardware Interrupt

Trigger the downstream function-call subsystem from an
interrupt service routine.

****Add-On Required:** This feature requires the Embedded Coder Support
Package for ARM Cortex-M Processors add-on.**

Create an Interrupt Service Routine (ISR) automatically in the
generated code in your model. The ISR executes the downstream function-call
subsystem associated with the block.

You can use this block for the following purposes:

- Use this block to build a processor specific, an ARM®
  Cortex®-M based core, hardware interrupt block.

  You can customize the block to processor specific interrupts by providing an
  XML based interrupt description file. See Create Hardware Interrupt Block for an ARM Cortex-M Based Processor Using an Interrupt Description File.

  Use this block as is, in code generation to respond to the Fault and NMI
  interrupt service routines and trigger a downstream function-call subsystem.
  Make sure the FaultISR and NmiISR are available in your interrupt vector
  table.

Using this block, you can:

- Create ISRs on ARM
  Cortex-M based processors.
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
