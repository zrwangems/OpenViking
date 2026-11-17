---
type: simulink-block
title: 'Proxy Task'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'proxytask'
documentation_source_path: 'ref/proxytask.html'
language: en
---

# Proxy Task

## Ports
```yaml
ports:
- name: Port_1
  summary: Function-call from Task Manager block scalar
  direction: input
  data_types: function-call
```

### Input

### **Port\_1** — Function-call from `Task Manager` block scalar

A function-call signal that triggers the Proxy Task block when
operating as an event-driven task.

#### Dependencies

To enable this port, set the `Type` property to
`Event-driven`.

**Data Types:** `function-call`
## Parameters
```yaml
parameters:
- name: Type
  summary: Type of task Timer-driven (default) | Event-driven
  group: ''
- name: Sample Time
  summary: Sample time 1 (default) | positive scalar
  group: ''
```

### **Type** — Type of task `Timer-driven` (default) | `Event-driven`

Select the type of task as either Timer-driven or Event-driven.

### **Sample Time** — Sample time 1 (default) | positive scalar

Sample time of the block.

**Note**

- The `Sample Time` of the Proxy Task block
  must match the sample time of the corresponding timer-driven task from the Task
  Manager block.
- The `Sample Time` of the Proxy Task block
  should be unique within the model. When other blocks in the model use the same
  sample time, the duration of the task defined by Proxy Task block
  cannot be guaranteed in code generation.

#### Dependencies

To enable this parameter, set the `Type` property to
`Timer-driven`.
## Libraries

SoC Blockset / Processor Task Execution

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

A placeholder for a task in your application

The Proxy Task block simulates the effect of a timer-driven task in your
SoC application without an explicit implementation. This block can be used as a placeholder
for timer-driven tasks to be developed in the future, or implemented simultaneously by another
developer.

When added to your processor reference Model block, it causes the processor model, when set to schedule rates by ports, to
display a periodic event port with a sample time equal to `Sample Time`
parameter. Connect the periodic event port to a timer-driven task output port on the Task Manager
block.
