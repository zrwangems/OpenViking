---
type: simulink-block
title: 'Task Sync'
family: 'asynchronous'
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

### 输入

### **Input** — 来自中断模块调用的调用

来自 Async Interrupt 模块的调用。
### 输出参数

### **Output** — 对 function-call subsystem 调用的调用

对 function-call subsystem 的调用。

## 参数

### **任务名称（不超过 10 个字符）** — 任务函数名称 `Task0` (默认) | character vector

传递给 RTOS 中 `taskSpawn` 系统调用的第一个参数。RTOS (VxWorks) 将此名称用作任务函数名称。此名称还可用作调试辅助。例程使用任务名称来标识调用它们的任务。

### **Simulink 任务优先级 (0–255)** — RTOS 任务优先级 50 (默认) | integer

派生时为 function-call subsystem 任务分配的 RTOS 任务优先级。RTOS (VxWorks) 优先级的范围为 0 到 255，其中 0 表示最高优先级。

**注意**

Simulink® 软件不会仿真异步任务行为。异步任务的任务优先级仅用于代码生成目的，在仿真期间不会生效。

### **堆栈大小 (bytes)** — 任务堆栈的最大大小 1024 (默认) | integer

任务堆栈可以增长到的最大大小。堆栈大小在 RTOS (VxWorks) 派生任务时分配。根据任务中局部变量的数量选择堆栈大小。通过检查任务的生成代码（以及从生成代码调用的函数）来确定大小。

### **将此任务的数据传输与调用方任务同步** — 选择同步 off (默认) | on

如果未选择（默认），

- 该模块维护一个定时器，该定时器提供下游模块计算所需的绝对时间值。该定时器独立于调用 Task Sync 模块的 Async Interrupt 模块所维护的定时器。
- 出现 **定时器分辨率** 选项。
- **定时器大小** 选项指定时间计数器的字长。

如果选择，

- 该模块不维护独立定时器，也不显示 **定时器分辨率** 字段。
- 需要定时器的下游模块使用调用 Task Sync 模块的 Async Interrupt 模块所维护的定时器（请参阅 Timers in Asynchronous Tasks）。在异步中断被服务时读取定时器值。到 Task Sync 模块所调用模块的数据传输在与此 Async Interrupt 模块关联的任务内执行。因此，数据传输与调用方同步。

### **定时器分辨率 (seconds)** — 模块定时器的分辨率 1/60 (默认)

模块定时器的分辨率，以 seconds 为单位。仅当 **将此任务的数据传输与调用方任务同步** 被清除时，此参数才出现。默认情况下，该模块通过调用 RTOS (VxWorks) 中的 `tickGet` 函数获取定时器值。默认分辨率为 1/60 second。

### **定时器大小** — 用于存储时钟节拍的位数 `32bits` (默认) | `16bits` | `8bits` | `auto`

用于硬件定时器存储时钟节拍的位数。大小可以是 `32bits`（默认）、`16bits`、`8bits` 或 `auto`。如果选择 `auto`，代码生成器会根据模型配置参数 **应用程序寿命 (days)** 和模块参数**定时器分辨率**的设置确定定时器大小。

默认情况下，定时器值存储为 32-bit integers。当 **定时器大小** 为 `auto` 时，您可以通过设置 **应用程序寿命 (days)** 参数间接控制计数器的字长。如果将 **应用程序寿命 (days)** 设置为对于代码生成器而言太大、无法作为指定分辨率的 32-bit integer 处理的值，它将使用第二个 32-bit integer 来处理溢出。

有关详细信息，请参阅 Optimize Memory Usage and Prevent Overflows for Time Counters。另请参阅 Timers in Asynchronous Tasks。

## 所属库

Simulink Coder / Asynchronous / Interrupt Templates

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 中引入**

## 描述

通过派生一个示例 RTOS (VxWorks) 任务来运行下游 function-call subsystem 或 Stateflow chart 的代码

Task Sync 模块派生一个示例 RTOS (VxWorks) 任务，该任务调用 function-call subsystem 或 Stateflow® chart。通常，您将 Task Sync 模块放置在 Async Interrupt 模块和 function-call subsystem 模块或 Stateflow chart 之间。或者，您可以将 Task Sync 模块连接到 Stateflow 图的输出端口，该图具有配置为函数调用的事件 `Output to Simulink`。

Task Sync 模块：

- 使用 RTOS (VxWorks) 系统调用 `taskSpawn` 派生一个独立任务。当该任务被激活时，它调用下游 function-call subsystem 代码或 Stateflow chart。该模块调用 `taskDelete` 在模型终止期间删除该任务。
- 创建一个信号量，以使连接的子系统与该模块的执行同步。
- 将派生的任务包装在无限 `for` 循环中。在该循环中，派生任务通过使用 `semTake` 侦听信号量。对 `semTake` 的第一次调用指定 `NO_WAIT`。此设置让任务能够确定在 function-call subsystem 或 chart 完成之前是否发生了第二次 `semGive`。此序列表明中断速率过快或任务优先级过低。
- 生成同步代码（例如 `semGive()`）。此代码让派生的任务运行。该任务反过来调用连接的 function-call subsystem 代码。同步代码可在中断级运行。Async Interrupt 和 Task Sync 模块之间的连接实现此操作，并在 ISR 内触发 Task Sync 模块的执行。
- 如果下游算法代码中的模块需要绝对时间，则提供绝对时间。该时间来自 Async Interrupt 模块维护的定时器，或来自与 Task Sync 模块关联的任务维护的独立定时器。

设计应用程序时，请考虑何时可以为连接到 Task Sync 模块的下游 function-call subsystem 获取定时器和信号输入值。默认情况下，当 RTOS (VxWorks) 激活任务时读取时间和输入数据。对于这种情况，数据（输入和时间）与该任务本身同步。如果您选择 **将此任务的数据传输与调用方任务同步** 选项，并且 Task Sync 模块驱动是 Async Interrupt 模块，则在中断发生（即，在 ISR 内）时读取时间和输入数据。对于这种情况，数据与 Task Sync 模块的调用方同步。

**注意**

使用 Interrupt Templates 模块库中的模块（Async Interrupt 和 Task Sync）进行仿真和代码生成。这些模块提供起点示例，帮助您为目标环境开发自定义模块。
