---
type: simulink-block
title: 'Task Trigger'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'tasktrigger'
documentation_source_path: 'ref/tasktrigger.html'
language: en
---

# Task Trigger

## Ports
```yaml
ports:
- name: Port_1
  summary: Output trigger scalar
  direction: output
  data_types: rteEvent
```

### Output

### **Port\_1** — Output trigger scalar

This port sends a task signal that triggers the Task Manager
block to execute the associated task.

**Data Types:** `rteEvent`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
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

Trigger task execution in your application

The Task Trigger block triggers execution of an event-driven task in your
application. Connect the output of this block to the event port of the respective task in the
Task Manager block.
Place this block in the appropriate task in the reference model.

You can place more than one of these blocks in the same task.

Use this block to enable efficient task schedules with explicit synchronization between
tasks.
