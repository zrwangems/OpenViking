---
type: simulink-block
title: 'Task Manager'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'taskmanager'
documentation_source_path: 'ref/taskmanager.html'
language: en
---

# Task Manager

## Ports
```yaml
ports:
- name: '*Task1*'
  summary: Function-call from Task1 scalar
  direction: output
- name: '*Task1*Event'
  summary: Message event notification scalar
  direction: input
  data_types: rteEvent
- name: '*Task1*Dur'
  summary: Task duration positive scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
```

### Output

### ***`Task1`*** — Function-call from Task1 scalar

A function-call signal that can trigger timer-driven and event-driven
tasks, represented as rate or function-call subsystems in the processor
Model block, respectively.

For a rate port from a timer-driven subsystem, to show on the
Model block, set the **Block Parameters** > **Main** > **Schedule rates** and select ports. For a function-call port from an
event-driven subsystem contained in a Function-Call Subsystem
block to show on the Model block, include an Inport in the processor
Model block connected to the function-call trigger
port of the subsystem. In the Inport, check **Block Parameters** > **Signal Attributes** > **Output function call**.

**Note**

The `Task1` port must be connected to either a
function-call port or scheduled rate signal port on a
Model block.

#### Dependencies

To create or remove a control signal port for a task, add or
remove the task from the Task Manager block by clicking the
**Add** or **Delete**
buttons in the block dialog mask.
### Input

### ***`Task1`*Event** — Message event notification scalar

A message port that triggers the associated
event-driven task. The `Task1Event` port receives
the message from either a Memory Channel block or IO
Data Source block.
For more
information on messages, see Messages.

#### Dependencies

To show a `Task1Event`
port, then `Task1` must
have **Type** set to
`Event-driven`.

**Data Types:** `rteEvent`

### ***`Task1`*Dur** — Task duration positive scalar

A positive value signal that specifies the execution duration of a
task at the present time. For more information on specifying task
duration, see Task Duration.

#### Dependencies

To enable this port, set the **Specify task duration
via** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
## Parameters
```yaml
parameters:
- name: Enable task simulation
  summary: Enable simulation of task duration on (default) | off
  group: ''
- name: List of tasks
  summary: List of tasks Task1 (default)
  group: ''
- name: Add
  summary: Add task button
  group: ''
- name: Delete
  summary: Delete existing task button
  group: ''
- name: Use Schedule Editor ordering
  summary: Specify task priority using Schedule Editor tool off (default) | on
  group: ''
- name: Name
  summary: Name of task Task1 (default) | character vector
  group: Main
- name: Type
  summary: Trigger type of task Timer-driven (default) | Event-driven
  group: Main
- name: Period
  summary: Timer period 0.1 (default) | positive scalar
  group: Main
- name: Core
  summary: Processor core to execute task 0 (default) | non-negative integer | -1
  group: Main
- name: Priority
  summary: Priority of task in scheduler 10 (default) | positive integer
  group: Main
- name: Drop tasks that overrun
  summary: Drop tasks that overrun off (default) | on
  group: Main
- name: Play recorded task execution sequence
  summary: Enable playback from file off (default) | on
  group: Simulation
- name: Specify task duration via
  summary: Source of task execution time Dialog (default) | Input port | Record task execution statistics
  group: Simulation
- name: Add
  summary: Adds distribution button
  group: Simulation
- name: Delete
  summary: Remove distribution button
  group: Simulation
- name: Percent
  summary: Likelihood of distribution 100 (default) | positive scalar
  group: Simulation
- name: Mean
  summary: Mean task duration in simulation 1e-06 (default) | positive scalar
  group: Simulation
- name: SD
  summary: Standard deviation of task duration in simulation 0 (default) | positive scalar
  group: Simulation
- name: Min
  summary: Lower limit of task duration 1e-06 (default) | positive scalar
  group: Simulation
- name: Max
  summary: Upper limit of task duration 1e-06 (default) | positive scalar
  group: Simulation
- name: File name
  summary: File containing diagnostic scheduling data filepath
  group: Simulation
```

### **Enable task simulation** — Enable simulation of task duration `on` (default) | `off`

Enable or disable the simulation of task duration. If you clear this
parameter, tasks simulate using a function-call generator inheriting their
period from the fundamental sample time of the model for event-driven tasks
or from the dialog for timer-driven tasks.

### **List of tasks** — List of tasks `Task1` (default)

List of the tasks generated by the Task Manager block. Each task has a set
of parameters listed in the **Main** and
**Simulation** tabs of the block dialog mask.

### **Add** — Add task button

Add a task to the Task Manager block. During deployment, each task is
encapsulated as an execution thread in the generated code. The properties of
the thread are taken from the **Main** parameters for that
task. During simulation, the task uses a combination of the
**Main** and **Simulation** parameters
for that task.

### **Delete** — Delete existing task button

Remove a task from the Task Manager.

#### Dependencies

To enable this parameter, specify at least two tasks.

### **Use Schedule Editor ordering** — Specify task priority using Schedule Editor tool `off` (default) | `on`

Use the Schedule Editor to specify the ordering of the tasks in the SoC
model. When using the Schedule Editor, task priority is
automatically assigned to the tasks based on their order in the editor and
the base rate priority of the processor model. For more information on using Schedule Editor to specify task priority, see Task Management with Schedule Editor.

### Main

### **Name** — Name of task `Task1` (default) | character vector

Unique name of the task. The task name must only contain alphanumeric
characters and underscores.

### **Type** — Trigger type of task `Timer-driven` (default) | `Event-driven`

Specify the task as timer-driven or event-driven. For more information
on timer- and event-driven tasks, see Timer-Driven Task and
Event-Driven Tasks,
respectively.

#### Dependencies

To enable this parameter, set `Type` to
`Timer-driven`.

### **Period** — Timer period `0.1` (default) | positive scalar

Specify the trigger time period for timer-driven tasks.

### **Core** — Processor core to execute task `0` (default) | non-negative integer | `-1`

Specify the number of the processor core where a task executes.
For more information on selecting cores
and core execution visualizations, see Multicore Execution and Core Visualization.

To have the operating system dynamically assign a core to the task,
set this value to `-1`.

### **Priority** — Priority of task in scheduler `10` (default) | positive integer

Specify the schedulers priority for the event-driven task between
`1` and `99`. Higher priority
tasks can preempt lower priority tasks, and vice versa. The task
priority range is limited by the hardware attributes. For more
information on task priority, see Task Priority and Preemption.

#### Dependencies

To enable this parameter, set `Type` to
`Event-driven` and `Use
Schedule Editor ordering` to
`off`.

### **Drop tasks that overrun** — Drop tasks that overrun `off` (default) | `on`

Select this parameter to force tasks to drop, rather than catch up,
following an overrun instance. For more information on task overruns,
see Task Overruns and Countermeasures.

**Note**

No more than 2 instances of a task can overrun execution when
`Drop tasks that overrun` is set to
`off`. Any additional task instances that
overrun drop automatically.

### Simulation

### **Play recorded task execution sequence** — Enable playback from file off (default) | on

Select this parameter for the Task Manager block to
play back the recorded execution data provided from the specified
**File name** parameter. For more
information on replaying task execution, see Task Execution Playback Using Recorded Data.

### **Specify task duration via** — Source of task execution time `Dialog` (default) | `Input port` | `Record task execution statistics`

Specify the source of the timing information for the task
execution.

- `Dialog` - Use a normally distributed
  probabilistic model with **Mean**,
  **Deviation**, **Min**,
  and **Max** defined in the block dialog
  mask.
- `Input port` – When set from *Input port*, the block input port
  dynamically defines the execution duration.
- `Record task execution statistics` – Use a
  normally distributed probabilistic model with mean and deviation
  provided in file specified by **File
  name**.

For more information on configuring task duration, see Task Duration.

#### Task duration settings

### **Add** — Adds distribution button

Adds a distribution to the set of normal distributions that generates
an execution duration.

**Note**

Only a maximum five distributions can be assigned to a single
task.

### **Delete** — Remove distribution button

Remove a distribution from the set of normal distributions.

### **Percent** — Likelihood of distribution `100` (default) | positive scalar

Specify the likelihood of each normal distribution. The
**Percent** weighted sum of normal distributions
determines the task duration likelihood.

**Note**

The sum of **Percent** for all the distributions
in a single task must equal `100`.

### **Mean** — Mean task duration in simulation `1e-06` (default) | positive scalar

Specify the mean duration of the task during simulation of the task.
The simulated task duration uses a normal distribution with a specified
**Mean** and **SD** parameter values as a first-order approximation of
the task behavior.

### **SD** — Standard deviation of task duration in simulation `0` (default) | positive scalar

Specify the standard deviation duration of the task during simulation
of the task. The simulated task duration uses a normal distribution with
a specified **Mean** and **SD** as a first-order approximation of the task
behavior.

### **Min** — Lower limit of task duration `1e-06` (default) | positive scalar

Lower limit of a task duration distribution.

### **Max** — Upper limit of task duration `1e-06` (default) | positive scalar

Upper limit of a task duration distribution.

### **File name** — File containing diagnostic scheduling data filepath

The data in this file specifies the **Mean** and
**SD** parameter values. When the **Play recorded task execution sequence**
parameter is selected, the specified CSV file provides the explicit task
execution timing. The CSV file contains the diagnostic data of the task
scheduler previously recorded from the hardware board.

#### Dependencies

To enable this parameter, set the **Specify task duration
via** parameter to `Recorded task execution
statistics`.
## Libraries

SoC Blockset / Processor Task Execution C2000 Microcontroller Blockset / Scheduling Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Scheduling Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Scheduling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

To automatically generate C code for your design, and execute
on an SoC device, use the SoC Builder tool. To generate and execute C code for your SoC models,
Embedded Coder® features are required. For more information on generating code for SoC designs,
see Use SoC Builder to Generate SoC Design.

The tasks in the Task Manager block execute as threads in the generated code. The
task parameters in the Task Manager block specify the priority and execution core of
the thread.

## Version History

**Introduced in R2019a**

## Description

Create and manage task executions in Simulink model

The Task Manager block simulates the execution of software tasks as
they would be expected to behave on an SoC processor. With the Task Manager, you can add
and remove tasks from your model that can either be timer-driven or event-driven. Tasks
can be represented in a model as rates, for timer-driven tasks, or function-call
subsystems, for event-driven tasks, contained inside a single Model block. The Task Manager executes
individual tasks based on their parameters, such as period, duration, trigger, priority,
or processor core, and the combination of that task with the state of other tasks and
their priorities in the running model.

In simulation, this block uses code generation to improve simulation speed. This
entails some overhead when first simulating, but subsequent simulations are faster if
the block settings remain unchanged. For more information, see Interpreted Execution vs. Code Generation.

**Note**

The Task Manager block cannot be used in a referenced model. For
more information on referenced models, see Model block.

The Task Manager block provides three methods to specify the duration of a task in
simulation:

- A probability model of task duration defined in the block mask.
- From a data file recording of either a previous task simulation or from a task
  on an SoC device.
- Input ports on the block, which you can connect to more dynamic models of task
  duration.
