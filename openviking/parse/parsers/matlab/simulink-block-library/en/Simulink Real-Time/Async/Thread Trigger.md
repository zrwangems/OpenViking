---
type: simulink-block
title: 'Thread Trigger'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Async'
documentation_page: 'threadtrigger'
documentation_source_path: 'io_ref/threadtrigger.html'
language: en
---

# Thread Trigger

## Ports
```yaml
ports:
- name: T
  summary: Trigger input tested for selected transition boolean
  direction: input
- name: F
  summary: Function call output for task function call
  direction: output
```

### Input

### **T** — Trigger input tested for selected transition boolean

Detects the edge type that is selected by using the **Trigger
Edge** parameter as 1 for detected and 0 for not detected..

**Example:**
`0`
### Output

### **F** — Function call output for task function call

Outputs the call to the downstream function and provides the thread scheduling
priority for the task
## Parameters
```yaml
parameters:
- name: Trigger Edge
  summary: Selects trigger edge type Rising Edge (default) | Falling Edge | Both Edges
  group: ''
  block_parameter: edge
- name: ISR Task Priority
  summary: Selects the ISR task priority for function 245 (high priority) (default) | 235 (medium priority) | 225 (low priority)
  group: ''
  block_parameter: taskpri
```

### **Trigger Edge** — Selects trigger edge type `Rising Edge` (default) | `Falling Edge` | `Both Edges`

Selects the trigger edge type that is detected by the block input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `edge` |

### **ISR Task Priority** — Selects the ISR task priority for function `245` (high priority) (default) | `235` (medium priority) | `225` (low priority)

Selects the interrupt service routine (ISR) task priority for the function call. You
can select task priority values from 254 (highest priority) to 193 (lowest
priority).

The Thread Trigger block provides means to call a Function-Call Subsystem block or Triggered Subsystem block that is a separate model thread. This thread can
run with higher or lower priority than other execution threads. Each rate group in the
model executes as a different execution thread. For more information, see About RTOS Tasks and Priorities.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `taskpri` |
## Libraries

Simulink Real-Time / Async

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2022b: Removed Thread Trigger Block Sample Time Parameter

The Sample Time parameter for the Thread Trigger block is removed. The
block inherits sample time from the input signal to the block.

## Description

Call downstream function-call subsystem when selected input edge transition occurs

The Thread Trigger block calls the downstream Function-Call Subsystem block or Triggered Subsystem block and sets the interrupt priority of the task when the
selected input edge transition occurs. The block checks for the edge transition at the block
sample rate.

If the input transition occurs while the task is running, a CPU overload occurs on the
Speedgoat® target computer.

You can use a Thread Trigger block with a Function-Call Subsystem block that resides inside a referenced model as shown in
the figure. This approach is compatible with Simulink®
Coder™. Because the Thread Trigger block output signal is asynchronous
and Simulink
Coder does not permit an asynchronous output block inside a referenced model, place
the Thread Trigger block at the top level of the model. This approach does not
permit explicit partitioning. Remember to match the Asynchronous Task Specification priority
(`P:245`) to the priority selected in the Thread Trigger
block. For more information, see About RTOS Tasks and
Priorities.

This model shows Thread Trigger block usage with referenced model.
