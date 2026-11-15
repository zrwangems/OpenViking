---
type: simulink-block
title: 'VxWorks Task'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'vxworkstask'
documentation_source_path: 'xilinxzynq7000ec/ref/vxworkstask.html'
language: en
---

# VxWorks Task

## Ports

### Output

### **Port\_1** — Function-call control signal scalar

A function-call control signal that triggers a Function-Call Subsystem block.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **Task function name** — Name of thread on VxWorks `'Task0'` (default) | character vector

Assign a name to this task. You can enter up to 32 letters and numbers. Do not use
standard `C` reserved characters, such as the `/` and
`:` characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `taskName` |

### **Thread priority** — Linux thread priority `1` (default) | `1 .. 99`

When you set **Thread scheduling policy** to
`SCHED_FIFO`, you can set the priority of the thread from 1
to 99 (low-to-high). Higher-priority tasks can preempt lower-priority tasks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `taskPriority` |

## Libraries

Embedded Coder Support Package for AMD SoC Devices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Spawn task function as separate VxWorks thread

Use this block to create a task function that spawns as a separate VxWorks® thread. The task function runs the code of the downstream Function-Call Subsystem block.

The VxWorks Task block uses a first-in, first-out (FIFO) scheduling algorithm, which
executes real-time processes without time slicing. With FIFO scheduling, a higher-priority
process preempts a lower-priority process. While the higher-priority process runs, the
lower-priority process remains at the top of the list for its priority. When the scheduler
blocks the higher-priority processes, the lower-priority process resumes.

The default thread scheduling policy is FIFO Scheduling.
