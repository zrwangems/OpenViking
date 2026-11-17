---
type: simulink-block
title: 'Task Trigger Merge'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'tasktriggermerge'
documentation_source_path: 'ref/tasktriggermerge.html'
language: en
---

# Task Trigger Merge

## Ports
```yaml
ports:
- name: Port_1
  summary: Input trigger scalar
  direction: input
  data_types: rteEvent
- name: Port_1
  summary: Output trigger scalar
  direction: output
  data_types: rteEvent
```

### Input

### **Port\_1** — Input trigger scalar

This port receives multiple task triggers and merges them into one.

You define the number of **Port\_*`N`***
input ports by specifying the **Number of input task
triggers** parameter.

**Data Types:** `rteEvent`
### Output

### **Port\_1** — Output trigger scalar

This port sends a task signal that triggers the Task Manager
block to execute the associated task.

**Data Types:** `rteEvent`
## Parameters
```yaml
parameters:
- name: Number of input task triggers
  summary: Number of triggers to merge 2 (default) | positive integer
  group: ''
```

### **Number of input task triggers** — Number of triggers to merge 2 (default) | positive integer

Number of task triggers to merge into one output trigger, specified as a positive
integer.
## Libraries

SoC Blockset / Processor Task Execution

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- To automatically generate C code for your design,
  and execute the code on an SoC device, use the SoC Builder tool.
  For more information on generating code for SoC designs, see Use SoC Builder to Generate SoC Design.
- To generate and execute C code for your SoC models, this block requires Embedded Coder® and one of these support packages:

  - SoC Blockset™ Support Package for AMD FPGA and SoC Devices
  - SoC Blockset Support Package for Intel® Devices
  - SoC Blockset Support Package for Embedded Linux® Devices
- To use this block, you must set **Hardware Board** in the
  configuration parameters to a supported board. You can then follow the instructions to
  configure the board. For more information, see Create an Embedded Linux Device Configuration.

When deployed to a supported hardware board, this block uses the POSIX semaphore API to
implement a task trigger.

## Version History

**Introduced in R2023b**

## Description

Merge multiple task triggers into one trigger

The Task Trigger Merge block creates a single task trigger from a set of
task triggers. Connect Task Trigger block
outputs to the input ports of this block, and connect the output of this block to the event
port of the respective event-driven task in the Task Manager block.

Place this block in the top model.
