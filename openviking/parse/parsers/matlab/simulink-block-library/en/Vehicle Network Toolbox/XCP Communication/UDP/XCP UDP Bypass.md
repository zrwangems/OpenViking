---
type: simulink-block
title: 'XCP UDP Bypass'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / UDP'
documentation_page: 'xcpudpbypass'
documentation_source_path: 'ug/xcpudpbypass.html'
language: en
---

# XCP UDP Bypass

## Ports
```yaml
ports:
- name: Function-call
  summary: Function call for bypass function call
  direction: output
```

### Output

### **Function-call** — Function call for bypass function call

Connects the function-call outport to a function-call subsystem containing one
data acquisition list.
## Parameters
```yaml
parameters:
- name: Task Priority
  summary: Task priority in QNX Neutrino scheduler 191 (default) | integer
  group: ''
- name: Sample Time
  summary: Sample time -1 (default) | double
  group: ''
```

### **Task Priority** — Task priority in QNX Neutrino scheduler 191 (default) | integer

Select the task priority for the QNX Neutrino scheduler.

### **Sample Time** — Sample time `-1` (default) | double

Select the sample time. For more information, see Sample Times in Subsystems (Simulink).
## Libraries

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The XCP communication blocks support code generation
with limited deployment portability that runs only on the host computer or Simulink
Real-Time targets.

Code generation requires a C++ compiler that is
compatible with the code generation target. For more information, see Supported and Compatible Compilers.

## Version History

**Introduced in R2020b**

## Description

Connect the function-call outport to a function-call subsystem

The XCP UDP Bypass block connects the function-call outport to a
function-call subsystem containing one data acquisition list. The block issues a function-call
when the downstream data acquisition list has new data available.

Consider the downstream function-call subsystem as a bypass task:

In Simulink®
Real-Time™, the bypass task is executed asynchronously with the assigned task
priority.

In Simulink, the block checks for data acquisition data periodically at the assigned sample
rate and executes the bypass task accordingly.
