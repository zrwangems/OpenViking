---
type: simulink-block
title: 'Async Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Timers and Scheduling / Event-Based Scheduling'
documentation_page: 'asyncinterrupt'
documentation_source_path: 'ref/asyncinterrupt.html'
language: zh-CN
chinese_source: official
---

# Async Interrupt

## 端口

### 输入

### **Input** — 仿真的中断源 标量 | 向量

仿真的中断源，指定为标量或向量。
### 输出

### **Output** — 控制信号 标量 | 向量

这些模型元素的控制信号，指定为标量或向量：

- 函数调用子系统
- Task Sync 模块
- 为函数调用输入事件配置的 Stateflow 图

## 参数

### **VME 中断编号** — 要安装的中断的 VME 中断编号 [1 2] (默认) | 整数数组

要安装的中断的 VME 中断编号数组。有效范围是 `1..7`。

Async Interrupt 模块输出信号的宽度对应于指定的 VME 中断编号的数目。

**注意**

一个模型可以包含多个 Async Interrupt 模块。但是，如果您使用多个 Async Interrupt 模块，请不要重复使用在任一模块中指定的 VME 中断编号。

### **VME 中断向量偏移** — 对应于 VME 中断编号的中断向量偏移编号 [192 193] (默认) | 整数数组

对应于为参数 **VME 中断编号**输入的 VME 中断编号的唯一中断向量偏移编号的数组。Stateflow 软件将偏移传递给 RTOS (VxWorks) 调用 `intConnect``(INUM_TO_IVEC(offset),...)`。

### **Simulink 任务优先级** — 下游模块的优先级 [10 11] (默认) | 整数数组

下游模块的 Simulink® 优先级。Async Interrupt 模块的每个输出驱动一个下游模块（例如，一个函数调用子系统）。指定与您为参数 **VME 中断编号**指定的 VME 中断编号对应的优先级的数组。

生成速率转换代码需要参数 **Simulink 任务优先级**的值（请参阅 Asynchronous Rate Transitions）。当异步任务必须从其基本速率或调用方获得真实时间时，还需要 Simulink 任务优先级值来保持绝对时间完整性。分配的优先级通常高于分配给周期性任务的优先级。

**注意**

Simulink 软件不仿真异步任务行为。异步任务的任务优先级仅用于代码生成目的，在仿真期间不适用。

### **Preemption flag(s); preemptable-1; non-preemptable-0** — 选择抢占 [0 1] (默认) | 整数数组

如果 Async Interrupt 模块的输出信号驱动一个 Task Sync 模块，则将此选项设置为 1。

在示例 RTOS (VxWorks) 中，优先级较高的中断可以抢占优先级较低的中断。要在执行 ISR 期间锁定中断，请将抢占标志设置为 0。此设置会导致在 ISR 代码的开头和结尾生成 `intLock()` 和 `intUnlock()` 调用。请务必谨慎使用中断锁定，因为它会增大系统对 `intLockLevelSet()` 级别及以下级别的中断的中断响应时间。指定与为参数 **VME 终端编号**输入的 VME 中断编号对应的标志的数组。

**注意**

指定参数 **VME 中断向量偏移**和 **Simulink 任务优先级**的数组中的元素数必须与为参数 **VME 中断编号**指定的数组中的元素数匹配。

### **管理自己的计时器** — 选择计时器管理器 on (默认) | off

如果选中，由 Async Interrupt 模块生成的 ISR 通过从硬件计时器读取绝对时间来管理它自己的计时器。使用参数**计时器大小**指定硬件计时器的大小。

### **计时器分辨率(秒)** — ISR 计时器的分辨率 1/60 (默认)

ISR 计时器的分辨率。Async Interrupt 模块生成的 ISR 维护自己的绝对时间计数器。默认情况下，这些计时器通过使用 `tickGet` 调用从 RTOS (VxWorks) 核获取其值。参数**计时器分辨率**确定这些计数器的分辨率。默认分辨率为 `1/60` 秒。您的板支持包 (BSP) 的 `tickGet` 分辨率可能与之不同。请确定您的 BSP 的 `tickGet` 分辨率，并在参数**计时器分辨率**中输入该分辨率。

如果您的目标是 RTOS (VxWorks) 示例以外的 RTOS，请将 `tickGet` 调用替换为对目标 RTOS 的等效调用。或者，生成代码来读取目标硬件上的计时器寄存器。有关详细信息，请参阅Timers in Asynchronous Tasks和 Async Interrupt Block Implementation。

### **计时器大小** — 存储时钟计时单元的位数 **32 位** (默认) | **16 位** | **8 位** | **自动**

存储硬件计时器的时钟计时单元的位数。当您选择参数**管理自己的计时器**时，由 Async Interrupt 模块生成的 ISR 使用该计时器大小。大小可以是 **32 位**（默认值）、**16 位**、**8 位**或**自动**。如果选择**自动**，代码生成器将根据参数**应用程序生命周期(天)** 和**计时器分辨率**的设置来确定计时器大小。

默认情况下，计时器值存储为 32 位整数。当参数**计时器大小**设置为**自动**时，您可以通过设置参数**应用程序生命周期(天)** 来间接控制计数器的字长。如果您为**应用程序生命周期(天)** 设置的值对于代码生成器来说太大而无法作为指定分辨率的 32 位整数来处理，则代码生成器使用另一个 32 位整数来处理溢出。

有关详细信息，请参阅Optimize Memory Usage and Prevent Overflows for Time Counters。另请参阅Timers in Asynchronous Tasks。

### **启用仿真输入** — 选择添加仿真输入端口 on (默认) | off

如果选中，则 Simulink 软件会向 Async Interrupt 模块添加输入端口。此端口仅用于仿真。将一个或多个仿真的中断源连接到仿真输入。

**注意**

在生成代码之前，请考虑删除驱动仿真输入的模块，以防止这些模块对生成的代码产生影响。您也可以使用**变体控制项模式**参数设置为 **sim codegen 切换**的 Variant Source 模块。如果使用 Variant Source 模块，驱动模块的采样时间会影响生成的代码中支持的采样时间。

## 所属库

Simulink Coder / Asynchronous / Interrupt Templates

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2006a 中推出**

## 描述

生成执行下游子系统或 Task Sync 模块的 Versa Module Eurocard (VME) 中断服务例程 (ISR)

对于示例 RTOS (VxWorks®) 中的每个指定 VME 中断级别，Async Interrupt 模块都会生成一个中断服务例程 (ISR)，该例程调用以下项之一：

- 函数调用子系统
- Task Sync 模块
- 为函数调用输入事件配置的 Stateflow® 图

**注意**

使用 Interrupt Templates 模块库中的模块（Async Interrupt 和 Task Sync）进行仿真和代码生成。您可用使用这些模块提供的示例作为起点，帮助您为目标环境开发自定义模块。

### 假设和限制

- 该模块支持 VME 中断 1 到 7。
- 该模块使用这些 RTOS (VxWorks) 系统调用：

  |  |
  | --- |
  | `sysIntEnable` |
  | `sysIntDisable` |
  | `intConnect` |
  | `intLock` |
  | `intUnlock` |
  | `tickGet` |

### 性能方面的考虑

在中断级别执行大型子系统会对系统中同等优先级和更低优先级中断的中断响应时间产生重大影响。通常，最好使 ISR 尽可能短。仅将包含几个模块的函数调用子系统连接到 Async Interrupt 模块。

对于大型子系统，更好的解决方案是使用 Task Sync 模块将函数调用子系统的执行与 RTOS 任务同步。将 Task Sync 模块放在 Async Interrupt 模块和函数调用子系统之间。然后，Async Interrupt 模块使用 Task Sync 模块作为 ISR。ISR 向任务释放同步信号量（执行 `semGive`），并立即从中断级别返回。然后，示例 RTOS (VxWorks) 调度并运行该任务。请参阅 Task Sync 模块的说明。
