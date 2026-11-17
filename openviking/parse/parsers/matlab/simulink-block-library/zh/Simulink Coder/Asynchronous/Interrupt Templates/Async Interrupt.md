---
type: simulink-block
title: 'Async Interrupt'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Asynchronous / Interrupt Templates'
documentation_page: 'asyncinterrupt'
documentation_source_path: 'ref/asyncinterrupt.html'
language: zh-CN
chinese_source: worker-translation
---

# Async Interrupt

## 端口

### 输入

### **Input** — 模拟中断源 标量 | 向量

模拟中断源，指定为标量或向量。
### 输出

### **Output** — 控制信号 标量 | 向量

用于这些模型元素的控制信号，指定为标量或向量：

- 函数调用子系统
- Task Sync 模块
- 配置为函数调用输入事件的 Stateflow 图

## 参数

### **VME interrupt number(s)** — 要安装的中断的 VME 中断号 [1 2]（默认）| 整数数组

要安装的中断的 VME 中断号数组。有效范围为
`1..7`。

Async Interrupt 模块输出信号的宽度对应于指定的 VME 中断号数量。

**注意**

一个模型可以包含多个 Async Interrupt 模块。但是，如果使用多个 Async Interrupt 模块，请勿在每个模块中指定重复的 VME 中断号。

### **VME interrupt vector offset(s)** — 对应于 VME 中断号的中断向量偏移号 [192 193]（默认）| 整数数组

对应于为参数 **VME interrupt number(s)** 输入的 VME 中断号的唯一中断向量偏移号数组。Stateflow 软件将这些偏移量传递给 RTOS（VxWorks）调用
`intConnect``(INUM_TO_IVEC(offset),...)`。

### **Simulink task priority(s)** — 下游模块的优先级 [10 11]（默认）| 整数数组

下游模块的 Simulink® 优先级。Async Interrupt 模块的每个输出驱动一个下游模块（例如，函数调用子系统）。指定与为参数 **VME interrupt number(s)** 指定的 VME 中断号相对应的优先级数组。

参数 **Simulink task priority** 的值是生成速率转换代码所必需的（请参阅 Asynchronous Rate Transitions）。当异步任务必须从其基本速率或其调用者获取实时时间时，Simulink 任务优先级值也是维护绝对时间完整性所必需的。分配的优先级通常高于分配给周期性任务的优先级。

**注意**

Simulink 软件不模拟异步任务行为。异步任务的任务优先级仅用于代码生成目的，在仿真期间不予遵循。

### **Preemption flag(s); preemptable-1; non-preemptable-0** — 选择抢占 [0 1]（默认）| 整数数组

如果 Async Interrupt 模块的输出信号驱动 Task Sync 模块，请将此选项设置为 1。

在示例 RTOS（VxWorks）中，较高优先级的中断可以抢占较低优先级的中断。要在 ISR 执行期间锁定中断，请将抢占标志设置为 0。此设置会导致在 ISR 代码的开头和结尾生成 `intLock()` 和 `intUnlock()` 调用。请谨慎使用中断锁定，因为它会增加系统在 `intLockLevelSet()` 级别及以下的中断响应时间。指定与为参数 **VME interrupt number(s)** 输入的 VME 中断号相对应的标志数组。

**注意**

指定参数 **VME interrupt vector offset(s)** 和 **Simulink task priority** 的数组中的元素数量必须与为参数 **VME interrupt number(s)** 指定的数组中的元素数量相匹配。

### **Manage own timer** — 选择定时器管理器 开（默认）| 关

如果选中，Async Interrupt 模块生成的 ISR 通过从硬件定时器读取绝对时间来管理自己的定时器。使用参数 **Timer size** 指定硬件定时器的大小。

### **Timer resolution (seconds)** — ISR 定时器 1/60 的分辨率（默认值）

ISR 定时器的分辨率。由 Async Interrupt 模块生成的 ISR 维护自己的绝对时间计数器。默认情况下，这些定时器通过使用 `tickGet` 调用从 RTOS（VxWorks）内核获取其值。参数 **Timer resolution** 决定这些计数器的分辨率。默认分辨率为 `1/60` 秒。您的板级支持包（BSP）的 `tickGet` 分辨率可能不同。确定您的 BSP 的 `tickGet` 分辨率，并将其输入到参数 **Timer resolution** 中。

如果您的目标 RTOS 不是示例 RTOS（VxWorks），请将 `tickGet` 调用替换为对目标 RTOS 的等效调用。或者，生成代码以读取目标硬件上的定时器寄存器。有关更多信息，请参阅 Timers in Asynchronous Tasks 和 Async Interrupt Block Implementation。

### **Timer size** — 用于存储时钟节拍的位数 `32bits`（默认值）| `16bits` | `8bits` | `auto`

用于存储硬件定时器时钟节拍的位数。当您选择参数 **Manage own timer** 时，由 Async Interrupt 模块生成的 ISR 使用该定时器大小。大小可以是 `32bits`（默认值）、`16bits`、`8bits` 或 `auto`。如果您选择 `auto`，代码生成器将根据参数 **Application lifespan (days)** 和 **Timer resolution** 的设置来确定定时器大小。

默认情况下，定时器值存储为 32 位整数。当参数 **Timer size** 设置为 `auto` 时，您可以通过设置参数 **Application lifespan (days)** 来间接控制计数器的字长。如果您将 **Application lifespan (days)** 设置为一个对于代码生成器来说过大的值，以至于无法作为指定分辨率的 32 位整数处理，代码生成器将使用第二个 32 位整数来处理溢出。

有关更多信息，请参阅 Optimize Memory Usage and Prevent Overflows for Time Counters。另请参阅 Timers in Asynchronous Tasks。

### **Enable simulation input** — 选择添加仿真输入端口 on（默认值）| off

如果选中，Simulink 软件将向 Async Interrupt 模块添加一个输入端口。此端口仅用于仿真。将一个或多个仿真中断源连接到仿真输入。

**注意**

在生成代码之前，请考虑移除驱动仿真输入的模块，以防止这些模块对生成的代码产生影响。或者，您可以使用 Variant Source 模块，并将 **Variant control mode** 参数设置为 `sim codegen switching`。如果使用 Variant Source 模块，驱动模块的采样时间将影响生成的代码中所支持的采样时间。

## 所属库

Simulink Coder / Asynchronous / Interrupt Templates

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 中引入**

## 描述

生成 Versa Module Eurocard（VME）中断服务例程（ISR），用于执行下游子系统或 Task Sync 模块

对于示例 RTOS（VxWorks®）中每个指定的 VME 中断级别，Async Interrupt 模块生成一个中断服务例程（ISR），该例程调用以下之一：

- 函数调用子系统
- Task Sync 模块
- 配置为函数调用输入事件的 Stateflow® 图

**注意**

使用 Interrupt Templates 模块库中的模块（Async Interrupt 和 Task Sync）进行仿真和代码生成。这些模块提供了起点示例，帮助您为目标环境开发自定义模块。

### 假设和限制

- 该模块支持 VME 中断 1 到 7。
- 该模块使用以下 RTOS（VxWorks）系统调用：

  |  |
  | --- |
  | `sysIntEnable` |
  | `sysIntDisable` |
  | `intConnect` |
  | `intLock` |
  | `intUnlock` |
  | `tickGet` |

### 性能注意事项

在中断级别执行大型子系统可能会对系统中同等和较低优先级中断的中断响应时间产生显著影响。通常，最好保持 ISR 尽可能短。仅将包含少量模块的函数调用子系统连接到 Async Interrupt 模块。

对于大型子系统，更好的解决方案是使用 Task Sync 模块将函数调用子系统的执行同步到 RTOS 任务。将 Task Sync 模块放在 Async Interrupt 模块和函数调用子系统之间。然后，Async Interrupt 模块将 Task Sync 模块用作 ISR。ISR 向任务释放一个同步信号量（执行 `semGive`），并立即从中断级别返回。然后示例 RTOS（VxWorks）调度并运行该任务。请参阅 Task Sync 模块的描述。
