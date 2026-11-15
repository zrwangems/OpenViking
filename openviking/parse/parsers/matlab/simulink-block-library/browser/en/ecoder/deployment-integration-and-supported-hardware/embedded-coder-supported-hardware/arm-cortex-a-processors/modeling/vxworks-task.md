---
type: simulink-block
title: 'VxWorks Task'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-A Processors / Modeling'
documentation_page: 'vxworkstask'
documentation_source_path: 'armcortexa/ref/vxworkstask.html'
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

Specify a name for this task. You can enter at most 32 letters, numbers, or a
combination of letters and numbers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `taskName` |

### **Thread priority** — Priority of the VxWorks thread `0` (default) | `0 .. 255`

Specify the priority of the VxWorks thread from 0 to 255 (low-to-high). Higher-priority tasks can preempt
lower-priority tasks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `taskPriority` |

## Libraries

Embedded Coder Support Package for ARM Cortex-A Processors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Spawn task function as separate VxWorks thread

The VxWorks Task block creates a task function that spawns as a separate
VxWorks® thread. The task function runs the code of the downstream Function-Call Subsystem block.

The VxWorks Task block uses a first-in, first-out (FIFO) scheduling algorithm, which
executes real-time processes without time slicing. With FIFO scheduling, a higher-priority
process preempts a lower-priority process. While the higher-priority process runs, the
lower-priority process remains at the top of the list for its priority. When the scheduler
blocks the higher-priority processes, the lower-priority process resumes.

The VxWorks Task block uses FIFO scheduling.
