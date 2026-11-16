---
type: simulink-block
title: 'Linux Task'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-A Processors / Modeling'
documentation_page: 'linuxtask'
documentation_source_path: 'armcortexa/ref/linuxtask.html'
language: en
---

# Linux Task

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

### **Task name (32 characters or less)** — Name of thread on Linux `Task0` (default) | character vector

Specify a name for this task. You can enter at most 32 characters consisting of
letters, numbers, or a combination of letters and numbers.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `taskName` |

### **Thread scheduling policy** — Thread scheduling policy used by Linux `SCHED_FIFO` (default) | `SCHED_OTHER`

Select the scheduling policy that applies to this thread. You can choose from these
options:

- `SCHED_FIFO` — This option enables a first-in,
  first-out (FIFO) scheduling algorithm that executes real-time processes without time
  slicing. With FIFO scheduling, a higher-priority process preempts a lower-priority
  process. The lower-priority process remains at the top of the list for its priority
  and resumes execution when the scheduler blocks all higher-priority
  processes.

  For example, in the FIFO scheduling image, task2 preempts task1, and task3
  preempts task2. When task3 completes, task2 resumes. When task2 completes, task1
  resumes.

  The Linux Task block uses FIFO scheduling.

  `SCHED_FIFO` displays the **Thread
  priority** parameter on which you can set to a value from 1 to 99.
- `SCHED_OTHER` — This option enables the default
  Linux time-sharing scheduling algorithm. You can use this scheduling for all
  processes except those requiring special static priority real-time mechanisms. With
  this algorithm, the scheduler chooses processes based on their dynamic priority
  within the static priority 0 list. Each time the process is ready to run and the
  scheduler denies it, the operating system increases the dynamic priority of that
  process. Such prioritization helps the scheduler serve the
  `SCHED_OTHER` processes.

  Selecting `SCHED_OTHER` hides the **Thread
  priority** parameter and sets the thread priority to 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `taskPolicy` |

### **Threaded priority** — Linux thread priority `1` (default) | `1 .. 99`

Specify the priority of the Linux thread. A value of 1 indicates a low priority, and a value of 99 indicates
a high priority. Higher-priority tasks can preempt lower-priority tasks.

To enable this parameter, set **Thread scheduling policy** to
`SCHED_FIFO`.

To enable this parameter, set **Thread scheduling policy** to
`SCHED_FIFO`.

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

Spawn task function as separate Linux thread

Use this block to create a task function that spawns as a separate Linux® thread. The task function runs the code of the downstream Function-Call Subsystem block.
