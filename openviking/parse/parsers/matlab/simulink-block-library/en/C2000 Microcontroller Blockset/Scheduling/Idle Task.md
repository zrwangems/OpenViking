---
type: simulink-block
title: 'Idle Task'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'idletaskblock'
documentation_source_path: 'ref/idletaskblock.html'
language: en
---

# Idle Task

## Ports

### Input

### **Port\_1** — Simulation only port scalar

Connect one or more simulated interrupt sources to the simulation
input.

#### Dependencies

This port appears only when **Enable simulation port**
parameter is enabled.

**Data Types:** `SoCData`
### Output

### **data** — Idle task data vector

The output of the Idle task is a vector of uint16 values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus`

## Parameters

### **Task numbers** — Identifies created tasks by numbers `double` (default) | `single` | `int8` | `int16` | `int32` | `int64` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `uint64` | `Boolean` | `bus`

Identifies the created tasks by number. Enter as many tasks as you need by
entering a vector of integers. The default values are [1,2] to indicate that the
downstream subsystem has two functions.

The values you enter determine the execution order of the functions in the
downstream subsystem, while the number of values you enter corresponds to the
number of functions in the downstream subsystem.

Enter a vector containing the same number of elements as the number of
functions in the downstream subsystem. This vector can contain up to 16 elements,
and the values must be from 0 to 15 inclusive.

The value of the first element in the vector determines the order in which the
first function in the subsystem is executed, the value of the second element
determines the order in which the second function in the subsystem is executed,
and so on.

For example, entering [2,3,1] in this field indicates that there are three
functions to be executed, and that the third function is executed first, the first
function is executed second, and the second function is executed third. After the
functions are executed, the Idle Task block cycles back and repeats the execution
of the functions in the same order.

### **Preemption flags** — Number of storage buffers `1` (default) | positive integer

Higher-priority interrupts can preempt interrupts that have lower priority. To
allow you to control preemption, use the preemption flags to specify whether an
interrupt can be preempted.

Entering `1` indicates that the interrupt can be preempted.
Entering `0` indicates the interrupt cannot be preempted. When
**Task numbers** contains more than one task, you
can assign different preemption flags to each task by entering a vector of flag
values, corresponding to the order of the tasks in **Task
numbers**. If **Task numbers** contains
more than one task, and you enter only one flag value here, that status applies to
the tasks.

In the default settings `[0 1]`, the task with priority
`1` in **Task numbers** is not
preemptable, and the priority `2` task can be preempted.

### **Enable simulation port** — Enable peripheral simulation port to block `off` (default) | `on`

When you select this option, Simulink software adds an input port to the Idle
Task block. This port is used in simulation only. Connect one or more simulated
interrupt sources to the simulation input.

**Note**

Select this check box to test asynchronous interrupt processing behavior
in Simulink software.

## Libraries

C2000 Microcontroller Blockset / Scheduling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Create free-running task

The Idle Task block, and the subsystem connected to it, specify one or more functions to
execute as background tasks. The tasks executed through the Idle Task block are of the
lowest priority, lower than that of the base rate task.

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
