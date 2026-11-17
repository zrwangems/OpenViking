---
type: simulink-block
title: 'Task Sync'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Asynchronous / Interrupt Templates'
documentation_page: 'tasksync'
documentation_source_path: 'ref/tasksync.html'
language: zh-CN
chinese_source: worker-translation
---

# Task Sync

## 端口
```yaml
ports:
- name: Input
  summary: 来自中断模块调用的调用
  direction: input
- name: Output
  summary: 对函数调用子系统的调用
  direction: input
```

### 输入

### **Input** — 来自中断模块调用的调用

来自 Async Interrupt 模块的调用。
### 输出参数

### **Output** — 对函数调用子系统的调用

对函数调用子系统的调用。
## 参数
```yaml
parameters:
- name: Task name (10 characters or less)
  summary: 任务函数名称 Task0（默认）| 字符向量
  group: ''
- name: Simulink task priority (0–255)
  summary: RTOS 任务优先级 50（默认）| 整数
  group: ''
- name: Stack size (bytes)
  summary: 任务堆栈的最大大小 1024（默认）| 整数
  group: ''
- name: Synchronize the data transfer of this task with the caller task
  summary: 选择同步 off（默认）| on
  group: ''
- name: Timer resolution (seconds)
  summary: 模块定时器的分辨率 1/60（默认）
  group: ''
- name: Timer size
  summary: 存储时钟节拍的位数 32bits（默认）| 16bits | 8bits | auto
  group: ''
```

### **Task name (10 characters or less)** — 任务函数名称 `Task0`（默认）| 字符向量

传递给 RTOS 中 `taskSpawn` 系统调用的第一个参数。RTOS（VxWorks）将此名称用作任务函数名称。此名称也可作为调试辅助。例程使用任务名称来标识调用它们的任务。

### **Simulink task priority (0–255)** — RTOS 任务优先级 50（默认）| 整数

在生成时分配给函数调用子系统任务的 RTOS 任务优先级。RTOS（VxWorks）优先级范围为 0 到 255，其中 0 表示最高优先级。

**注意**

Simulink® 软件不模拟异步任务行为。异步任务的任务优先级仅用于代码生成目的，在仿真期间不予采用。

### **Stack size (bytes)** — 任务堆栈的最大大小 1024（默认）| 整数

任务堆栈可以增长到的最大大小。堆栈大小在 RTOS（VxWorks）生成任务时分配。根据任务中局部变量的数量选择堆栈大小。通过检查任务（以及从生成代码中调用的函数）的生成代码来确定大小。

### **Synchronize the data transfer of this task with the caller task** — 选择同步 off（默认）| on

如果未选择（默认），

- 该模块维护一个定时器，提供下游模块计算所需的绝对时间值。该定时器独立于调用 Task Sync 模块的 Async Interrupt 模块所维护的定时器。
- 出现 **Timer resolution** 选项。
- **Timer size** 选项指定时间计数器的字长。

如果选择，

- 该模块不维护独立的定时器，也不显示 **Timer resolution** 字段。
- 需要定时器的下游模块使用调用 Task Sync 模块的 Async Interrupt 模块所维护的定时器（参见 Timers in Asynchronous Tasks）。定时器值在服务异步中断时读取。向 Task Sync 模块所调用模块的数据传输在与 Async Interrupt 模块关联的任务内执行。因此，数据传输与调用方同步。

### **Timer resolution (seconds)** — 模块定时器的分辨率 1/60（默认）

模块定时器的分辨率，以秒为单位。此参数仅在 **Synchronize the data transfer of this task with the caller task** 被清除时出现。默认情况下，该模块通过调用 RTOS（VxWorks）中的 `tickGet` 函数获取定时器值。默认分辨率为 1/60 秒。

### **Timer size** — 存储时钟节拍的位数 `32bits`（默认）| `16bits` | `8bits` | `auto`

用于存储硬件定时器时钟节拍的位数。大小可以是 `32bits`（默认）、`16bits`、`8bits` 或 `auto`。如果选择 `auto`，代码生成器将根据模型配置参数 **Application lifespan (days)** 和模块参数 **Timer resolution** 的设置来确定定时器大小。

默认情况下，定时器值存储为 32 位整数。当 **Timer size** 为 `auto` 时，您可以通过设置 **Application lifespan (days)** 参数来间接控制计数器的字长。如果将 **Application lifespan (days)** 设置为对于代码生成器而言过大而无法作为指定分辨率的 32 位整数处理的值，它将使用第二个 32 位整数来处理溢出。

有关详细信息，请参见 Optimize Memory Usage and Prevent Overflows for Time Counters。另请参见 Timers in Asynchronous Tasks。
## 所属库

Simulink Coder / Asynchronous / Interrupt Templates

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 中引入**

## 描述

通过生成一个示例 RTOS（VxWorks）任务来运行下游函数调用子系统或 Stateflow 图表的代码

Task Sync 模块生成一个示例 RTOS（VxWorks）任务，该任务调用函数调用子系统或 Stateflow® 图表。通常，您将 Task Sync 模块放置在 Async Interrupt 模块和函数调用子系统模块或 Stateflow 图表之间。或者，您可以将 Task Sync 模块连接到 Stateflow 图的输出端口，该图具有配置为函数调用的事件 `Output to Simulink`。

Task Sync 模块：

- 使用 RTOS（VxWorks）系统调用 `taskSpawn` 生成一个独立任务。当任务被激活时，它调用下游函数调用子系统代码或 Stateflow 图表。该模块在模型终止期间调用 `taskDelete` 删除任务。
- 创建一个信号量，用于将所连接的子系统与模块的执行同步。
- 将生成的任务包裹在一个无限 `for` 循环中。在循环中，生成的任务通过使用 `semTake` 监听信号量。第一次调用 `semTake` 指定 `NO_WAIT`。此设置让任务确定在函数调用子系统或图表完成之前是否发生了第二次 `semGive`。此序列表明中断速率过快或任务优先级过低。
- 生成同步代码（例如 `semGive()`）。此代码让生成的任务运行。该任务进而调用所连接的函数调用子系统代码。同步代码可以在中断级别运行。Async Interrupt 和 Task Sync 模块之间的连接完成此操作，并在 ISR 内触发 Task Sync 模块的执行。
- 如果下游算法代码中的模块需要绝对时间，则提供绝对时间。该时间来自 Async Interrupt 模块维护的定时器，或来自与 Task Sync 模块关联的任务维护的独立定时器。

在设计应用程序时，请考虑何时为连接到 Task Sync 模块的下游函数调用子系统采集定时器和信号输入值。默认情况下，当 RTOS（VxWorks）激活任务时读取时间和输入数据。在这种情况下，数据（输入和时间）与任务本身同步。如果您选择 **Synchronize the data transfer of this task with the caller task** 选项，并且 Task Sync 模块的驱动程序是 Async Interrupt 模块，则在中断发生时（即在 ISR 内）读取时间和输入数据。在这种情况下，数据与 Task Sync 模块的调用方同步。

**注意**

使用 Interrupt Templates 模块库中的模块（Async Interrupt 和 Task Sync）进行仿真和代码生成。这些模块提供了起点示例，帮助您为目标环境开发自定义模块。
