---
type: simulink-block
title: 'Task Sync'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Timers and Scheduling / Event-Based Scheduling'
documentation_page: 'tasksync'
documentation_source_path: 'ref/tasksync.html'
language: en
---

# Task Sync

## Ports

### Input

### **Input** — Call from interrupt block call

A call from an Async Interrupt block.
### Output Arguments

### **Output** — Call to function-call subsystem call

A call to a function-call subsystem.

## Parameters

### **Task name (10 characters or less)** — Task function name `Task0` (default) | character vector

The first argument passed to the `taskSpawn` system call in the
RTOS. The RTOS (VxWorks) uses this name as the task function name. This name also serves
as a debugging aid. Routines use the task name to identify the task from which they are
called.

### **Simulink task priority (0–255)** — RTOS task priority 50 (default) | integer

The RTOS task priority assigned to the function-call subsystem task when spawned.
RTOS (VxWorks) priorities range from 0 to 255, with 0 representing the highest
priority.

**Note**

The Simulink® software does not simulate asynchronous task behavior. The task priority
of an asynchronous task is for code generation purposes only and is not honored during
simulation.

### **Stack size (bytes)** — Maximum size for stack of the task 1024 (default) | integer

Maximum size to which the stack of the task can grow. The stack size is allocated
when the RTOS (VxWorks) spawns the task. Choose a stack size based on the number of
local variables in the task. Determine the size by examining the generated code for the
task (and functions that are called from the generated code).

### **Synchronize the data transfer of this task with the caller task** — Select synchronization off (default) | on

If not selected (the default),

- The block maintains a timer that provides absolute time values required by the
  computations of downstream blocks. The timer is independent of the timer maintained
  by the Async Interrupt block that calls the Task Sync
  block.
- A **Timer resolution** option appears.
- The **Timer size** option specifies the word size of the time
  counter.

If selected,

- The block does not maintain an independent timer and does not display the
  **Timer resolution** field.
- Downstream blocks that require timers use the timer maintained by the
  Async Interrupt block that calls the Task Sync block
  (see Timers in Asynchronous Tasks). The timer
  value is read at the time the asynchronous interrupt is serviced. Data transfers to
  blocks called by the Task Sync block execute within the task
  associated with the Async Interrupt block. Therefore, data transfers
  are synchronized with the caller.

### **Timer resolution (seconds)** — Resolution for timer of the block 1/60 (default)

The resolution of the timer of the block in seconds. This parameter appears only if
**Synchronize the data transfer of this task with the caller task**
is cleared. By default, the block gets the timer value by calling the
`tickGet` function in the RTOS (VxWorks). The default resolution is
1/60 second.

### **Timer size** — Number of bits to store clock tick `32bits` (default) | `16bits` | `8bits` | `auto`

The number of bits to store the clock tick for a hardware timer. The size can be
`32bits` (the default), `16bits`,
`8bits`, or `auto`. If you select
`auto`, the code generator determines the timer size based on
the settings of model configuration parameter **Application lifespan
(days)** and block parameter**Timer resolution**.

By default, timer values are stored as 32-bit integers. When **Timer
size** is `auto`, you can indirectly control the
word size of the counters by setting the **Application lifespan (days)** parameter. If you set **Application lifespan (days)**  to a
value that is too large for the code generator to handle as a 32-bit integer of the
specified resolution, it uses a second 32-bit integer to address overflows.

For more information, see Optimize Memory Usage and Prevent Overflows for Time Counters. See also Timers in Asynchronous Tasks.

## Libraries

Simulink Coder / Asynchronous / Interrupt Templates

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2006a**

## Description

Run code of downstream function-call subsystem or Stateflow chart by spawning an example RTOS ( VxWorks ) task

The Task Sync block spawns an example RTOS (VxWorks) task that
calls a function-call subsystem or Stateflow® chart. Typically, you place the Task Sync block between an
Async Interrupt block and a function-call subsystem block or Stateflow chart. Alternatively, you could connect the Task Sync block to
the output port of a Stateflow diagram that has an event, `Output to Simulink`, configured as
a function call.

The Task Sync block:

- Uses the RTOS (VxWorks) system call `taskSpawn` to spawn an
  independent task. When the task is activated, it calls the downstream function-call
  subsystem code or Stateflow chart. The block calls `taskDelete` to delete the task
  during model termination.
- Creates a semaphore to synchronize the connected subsystem with execution of the
  block.
- Wraps the spawned task in an infinite `for` loop. In the loop, the
  spawned task listens for the semaphore by using `semTake`. The first
  call to `semTake` specifies `NO_WAIT`. This setting
  lets the task determine whether a second `semGive` has occurred before
  the completion of the function-call subsystem or chart. This sequence indicates that the
  interrupt rate is too fast or the task priority is too low.
- Generates synchronization code (for example, `semGive()`). This
  code lets the spawned task run. The task in turn calls the connected function-call
  subsystem code. The synchronization code can run at interrupt level. The connection
  between the Async Interrupt and Task Sync blocks
  accomplishes this operation and triggers execution of the Task Sync block
  within an ISR.
- Supplies absolute time if blocks in the downstream algorithmic code require it. The
  time comes from the timer maintained by the Async Interrupt block or comes
  from an independent timer maintained by the task associated with the Task
  Sync block.

When you design your application, consider when timer and signal input values could be
taken for the downstream function-call subsystem that is connected to the Task
Sync block. By default, the time and input data are read when the RTOS (VxWorks)
activates the task. For this case, the data (input and time) are synchronized to the task
itself. If you select the **Synchronize the data transfer of this task with the caller
task** option and the Task Sync block driver is an Async
Interrupt block, the time and input data are read when the interrupt occurs (that
is, within the ISR). For this case, data is synchronized with the caller of the Task
Sync block.

**Note**

Use the blocks in the Interrupt Templates block library (Async
Interrupt and Task Sync) for simulation and code generation.
These blocks provide starting point examples to help you develop custom blocks for a target
environment.
