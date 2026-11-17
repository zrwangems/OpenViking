---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'F2838x / M4'
documentation_page: 'hardwareinterruptblock'
documentation_source_path: 'ref/hardwareinterruptblock.html'
language: en
---

# Hardware Interrupt

## Ports
```yaml
ports:
- name: '*name* Event Task'
  summary: Function-call event input simulation scalar
  direction: input
- name: '*name* Event'
  summary: Generate interrupt request Scalar
  direction: output
```

### Input

### ***`name`* Event Task** — Function-call event input simulation scalar

The simulation-only message input port, when connected to an Function-Call Generator block, the block acts as
pass-through with the output emitted on the
***`name`* Event** port
in simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter.
### Output

### ***`name`* Event** — Generate interrupt request `Scalar`

The output of this block is a function-call. The number of function
call outputs will be same as events selected to serve in an ISR.
## Parameters
```yaml
parameters:
- name: Number of events to serve
  summary: Specify number of events to serve 1 (default) | 2 | 3 | <32
  group: ''
- name: Simulink task priority
  summary: Set priority of selected ISR 50 (default) | positive integer or nonnegative integer
  group: ''
- name: Disable interrupt pre-emption
  summary: Select to disable interrupt preemption off (default) | on
  group: ''
- name: Enable simulation port
  summary: Enable simulation ports to block off (default) | on
  group: ''
```

### **Number of events to serve** — Specify number of events to serve `1` (default) | `2` | `3` | `<32`

Specify the number of events to serve for the Hardware Interrupt block.
This parameter enables the specified number events as output port
`event#`

### **Simulink task priority** — Set priority of selected ISR `50` (default) | `positive integer or nonnegative integer`

The value you specify in this parameter sets the priority of the
downstream function-call subsystem. The simulink task priority of the
selected (ISR) is relative to the model base rate priority.

**Note**

The default model base sample rate priority is set to 40 with a
lower priority value indicating a higher priority task. To achieve
this the **Higher priority value indicates higher task
priority** option must be enabled in
**Configuration Parameters** >
**Solver** pane.

### **Disable interrupt pre-emption** — Select to disable interrupt preemption `off` (default) | `on`

By default, an interrupt can be preempted by a higher priority interrupt.
Selecting this option allows low priority interrupts to complete their
execution without being preempted by other interrupts.

### **Enable simulation port** — Enable simulation ports to block `off` (default) | `on`

Select this parameter to add an compatible simulation input port.
## Libraries

C2000 Microcontroller Blockset / F2838x / M4 C2000 Microcontroller Blockset / F28M35x / M3 C2000 Microcontroller Blockset / F28M36x / M3 C2000 Microcontroller Blockset / Scheduling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Trigger downstream function-call subsystems from interrupt service routine

Use the Hardware Interrupt block to create an interrupt service routine
(ISR) automatically in the generated code of your model. The ISR executes the downstream
function-call subsystem associated with event ports of the block.

The function call subsystem associated with the event output port run at same priority
as that of ISR priority.

Using this block you can:

- Create ISRs.
- Set ISR priority.
- Enable or disable interrupt preemption.
- Use the Hardware
  Mapping tool to configure the desired event or interrupt.

The **Hardware Mapping** tool allows you to configure the
hardware interrupts tasks for the selected hardware board. With this tool, you can map
the tasks in your software model to the available event sources and interrupts:

- Manually select the task in **Mapping Browser** >
  **Tasks** > **`CPU
  name`**. Select the desired event or interrupt source.
  For more, see Configure Interrupts and Events Using Hardware Mapping
