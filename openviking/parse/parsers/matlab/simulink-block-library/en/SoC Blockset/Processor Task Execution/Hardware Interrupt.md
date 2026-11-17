---
type: simulink-block
title: 'Hardware Interrupt'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'ref/hardwareinterrupt.html'
language: en
---

# Hardware Interrupt

## Ports
```yaml
ports:
- name: event1 Task
  summary: Simulate interrupt trigger scalar
  direction: input
- name: event1
  summary: Interrupt request scalar
  direction: output
```

### Input

### **event1 Task** — Simulate interrupt trigger `scalar`

The simulation-only message input acts as a pass-through and is reflected at the
output. The port receives input from a function call.

#### Dependencies

To enable this port, select the **Enable simulation port**
parameter.
### Output

### **event1** — Interrupt request `scalar`

This port ties the interrupt trigger to a software task. The output is a function
call.
## Parameters
```yaml
parameters:
- name: Task priority
  summary: Priority of selected interrupt 50 (default) | positive integer
  group: ''
- name: Processor core
  summary: core number 0 (default) | integer | -1
  group: ''
- name: Enable simulation port
  summary: Enable simulation port in block off (default) | on
  group: ''
- name: Hardware Mapping
  summary: Open Hardware Mapping tool button
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Task priority** — Priority of selected interrupt `50` (default) | positive integer

Specify the scheduling priority for the event-driven task between
`1` and `99`. Higher priority tasks preempt lower
priority tasks. The task priority range is limited by the hardware attributes. For more
information on task priority, see Task Priority and Preemption.

### **Processor core** — core number `0` (default) | integer | `-1`

Specify the number of the processor core where a task executes. For more information
on selecting cores and core execution visualizations, see Multicore Execution and Core Visualization.

To have the operating system dynamically assign a core to the task, set this value
to `-1`.

### **Enable simulation port** — Enable simulation port in block `off` (default) | `on`

Select this parameter to enable peripheral simulation. When selected, the block adds
an input port for simulation.

### **Hardware Mapping** — Open Hardware Mapping tool button

Click this parameter to open the Hardware Mapping
tool.
## Libraries

SoC Blockset / Processor Task Execution

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Trigger downstream function-call subsystem from interrupt service routine

The Hardware Interrupt block triggers a task when an event occurs. The task
must be associated with an event interrupt service routine. Once triggered, the task executes
the downstream subsystem. When using IP Core Generation Workflow, this block is configured and
placed in the generated software model.

**Tip**

To generate your software model, use the IP Core Generation Workflow instead of creating one
manually and configuring the Hardware Interrupt parameters. The workflow configures the
Hardware Interrupt block and places it in the generated model.

To associate the task with an interrupt event, use the Hardware Mapping app.
To start the app, click **Hardware Mapping** on the block mask.
