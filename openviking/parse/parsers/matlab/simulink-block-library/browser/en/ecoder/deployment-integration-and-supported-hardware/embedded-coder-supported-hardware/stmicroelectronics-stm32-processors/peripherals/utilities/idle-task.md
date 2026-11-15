---
type: simulink-block
title: 'Idle Task'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Utilities'
documentation_page: 'idletask'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/idletask.html'
language: en
---

# Idle Task

## Ports

### Input

### **Port\_1** — Simulated interrupt scalar | vector

Optional simulated interrupt for testing asynchronous interrupt behavior
during Simulink® simulation.

#### Port Dependencies

To enable this port, select parameter **Enable simulation
input**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Port\_1** — Task identifiers and preemption flags vectors

Numbers that identify the background tasks and task preemption flags,
represented as vectors. A task identifier vector stores numbers that identify
the background tasks.

For each background task, the preemption flag vector stores a flag that
indicates whether the task can be preempted. Unless the preemption flag vector
contains one element, the number of elements in the preemption flag vector must
match the length of the task identifier vector. If the preemption flag vector
has the same number of elements as the task identifier vector, each task
represented in the task identifier vector has the preemption setting defined by
the value of the corresponding element in the preemption flag vector. When the
preemption flag vector contains one element, the flag setting applies to the
entire task identifier vector.

A higher-priority task cannot preempt a lower-priority task that cannot be
preempted.

**Data Types:** `uint8`

## Parameters

### **Task numbers** — Identifiers for tasks created [1 2] (default) | vector of integers in the range 0 to 15

Specify task identifiers for functions that are in the downstream subsystem as
a vector of integers in the range 0 to 15. The vector must contain the same number
of values as the number of functions in the downstream subsystem. For example, the
default vector `[1 2]` indicates that the downstream subsystem
contains two functions.

The number of values that you enter corresponds to the number of functions in
the downstream subsystem. The values that you specify determine the execution
order of the functions. For example, the vector `[2 3 1]`
indicates that:

- The subsystem contains three functions.
- The third function executes first.
- The first function executes second.
- The second function executes third.

After the functions execute, the Idle Task block cycles back and repeats the
execution of the functions in the same order.

### **Preemption flags** — Preemption flags for specified tasks [0 1] (default) | vector of 0 to 16 integers in the range [ 0, 1]

Specify preemption flags for the tasks specified by the **Task
numbers** parameter as a vector of up to 16 ones and zeros.
Higher-priority interrupts can preempt interrupts that have a lower priority. To
control preemption, use the preemption flags to specify whether an interrupt can
be preempted.

The value `1` indicates that the interrupt for the
corresponding task can be preempted. The value `0` indicates that
the interrupt cannot be preempted. You have the option of specifying:

- One preemption value that applies to the entire vector that you specify
  for **Task numbers**.
- A preemption value for each task identified in the vector that you
  specify for **Task numbers**. Specify the flag values in
  the order that corresponds to the order of the tasks in **Task
  numbers**.

For example, if you specify the vector `[2 3 1]` for
**Task numbers** and `[0]` for
**Preemption flags**, tasks `1`,
`2`, and `3` cannot be preempted. If you
specify `[1 1 0]` for **Preemption flags**,
tasks `2` and `3` can be preempted and task
`1` cannot be preempted.

### **Enable idle task block for profiling** — Enable profiling off (default) | on

Enabling this parameter allows measurement of the idle task execution time when
profiling is enabled.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Create free-running task

The Idle Task block and the subsystem connected to it specify functions in the
downstream subsystem to execute as background tasks. The tasks executed through the Idle
Task block are of the lowest priority, lower than that of the base rate task.

Enabling the parameter **Enable idle task block for profiling** allows
measurement of the idle task execution time when profiling is enabled.

### Vectorized Output

The block output comprises a set of vectors—the task numbers vector and the
preemption flag or flags vector. A preemption-flag vector must be the same length as the
number of tasks vector unless the preemption flag vector has only one element. The value
of the preemption flag determines whether a given interrupt (and task) is preemptable.
Preemption overrides prioritization. A lower-priority nonpreemptable task can preempt a
higher-priority preemptable task.

When the preemption flag vector has one element, that element value applies to the
functions in the downstream subsystem as defined by the task numbers in the task number
vector. If the preemption flag vector has the same number of elements as the task number
vector, each task defined in the task number vector has a preemption status defined by
the value of the corresponding element in the preemption flag vector.
