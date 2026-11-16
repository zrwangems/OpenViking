---
type: simulink-block
title: 'Software Trigger CPU<->CLA'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / System Peripherals / CLA, Watchdog, Timer'
documentation_page: 'softwaretriggercpucla'
documentation_source_path: 'ref/softwaretriggercpucla.html'
language: en
---

# Software Trigger CPU<->CLA

## Ports

### Input

### **data** — Event trigger signal scalar

Specify an event signal to start the software interrupt in the CPU or CLA.

**Data Types:** `Boolean`
### Output

### **event** — Task event signal scalar

This port sends a message at whenever the trigger condition occurs. Specify the
trigger condition in the **Trigger condition** parameter. This output
connects to the input of the Task Manager (SoC Blockset)
block to execute the associated event-driven task.

**Note**

The Outport block, at the top-level of the
reference model that contains the Software Trigger CPU<->CLA
block, that connects to this **event** port must be configured as a
non-virtual bus.

**Data Types:** `rteEvent`

## Parameters

### **Task number** — Task identification number `1` (default) | integer from `1` to `8`

Specify the number of the CLA task to trigger.

### **Trigger condition** — Condition to trigger an event `Rising edge` (default) | `Input high`

Generate an event on the **event** port either on a rising edge of
the **data** port or whenever the input is high. To generate an event
when the input signal changes from zero to one, set this parameter to
`Rising edge`. To generate an event once per execution of the
task, set this parameter to `Input high`.

### **Trigger type** — Trigger type `Trig` (default) | `TrigAndWait(codegen)`

Specify the trigger type of on the CPU. To generate an event and continue running
the CPU, set this parameter to `Trig`. To generate an event and
instruct the CPU to wait for the interrupt to complete, set this parameter to
`TrigAndWait(codegen)`. The
`TrigAndWait(codegen)` option does not run in
simulation.

#### Dependencies

To enable this parameter, the block must be inside a reference model with the
**Processing Unit** set to one of the CPUs.

## Libraries

C2000 Microcontroller Blockset / Scheduling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Trigger software events between processor (CPU) and control law accelerator (CLA)

The Software Trigger CPU<->CLA block simulates the triggering of
software events between processor (CPU) and CLA in a supported Texas Instruments® hardware board. When you use this block as a task on a CPU, the block generates
an event to execute tasks on the connected CLA unit. When you use this block as a task on the
CLA, the block generates an event to execute tasks on the connected CPU. Use this block to
manage the communication and synchronization between the CPU and CLA.
