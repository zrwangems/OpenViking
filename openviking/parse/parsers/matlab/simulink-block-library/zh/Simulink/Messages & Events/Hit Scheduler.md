---
type: simulink-block
title: 'Hit Scheduler'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'hitscheduler'
documentation_source_path: 'slref/hitscheduler.html'
language: zh-CN
chinese_source: worker-translation
---

# Hit Scheduler

## 端口

### 输入

### **En** — 用于调度时间步的使能信号 标量 | 向量

当使能输入值为逻辑 `true` 时，该模块调度一个仿真时间步。

当你将 **Output type** 设置为 `Signal` 时，输入可以是标量或向量。当 **En** 输入为向量时，**Δt** 输入必须是具有相同维度的向量。

当你将 **Output type** 设置为 `Function call` 时，输入必须是标量。

**数据类型：** `Boolean`

### **Δt** — 当前仿真时间与要调度的时间步之间的间隔 标量 | 向量

该模块计算要调度的时间步，以 seconds 为单位，为当前仿真时间与时间间隔输入的当前值之和。

当你将 **Output type** 设置为 `Signal` 时，输入可以是标量或向量。当 **Δt** 输入为向量时，**En** 输入必须是具有相同维度的向量。

当你将 **Output type** 设置为 `Function call` 时，输入必须是标量。

**数据类型：** `double`

### 输出

### **Port\_1** — 已调度时间步的指示 标量 | 向量

该模块输出值指示仿真何时执行该模块所调度的时间步。你可以使用 **Output type** 参数配置该模块生成信号或函数调用事件。该模块输出值取决于输出类型以及输入信号的维度。

- 当你将 **Output type** 设置为 `Signal` 且输入信号为标量时，当仿真执行一个已调度时间步时，模块输出变为逻辑 `true`。
- 当你将 **Output type** 设置为 `Signal` 且输入信号为向量时，输出向量中与调度了该时间步的输入向量元素对应的元素从逻辑 `false` 变为逻辑 `true`。
- 当你将 **Output type** 设置为 `Function-Call` 时，输入必须是标量，并且当仿真执行一个已调度时间步时，该模块生成一个函数调用事件。

由于 Hit Scheduler 模块显式调度影响模块执行时机的求解器时间命中，因此对于两种输出类型，输出都具有可变采样时间。有关可变采样时间的详细信息，请参阅 Types of Sample Time。

**数据类型：** `Boolean`

## 参数

### **Output type** — 模块输出的类型 `Signal`（默认）| `Function Call`

该模块输出指示仿真何时执行该模块所调度的时间步。你可以配置该模块生成 Boolean 信号或函数调用事件。

- `Signal` — 当仿真执行一个已调度时间步时，模块输出变为逻辑 `true`。支持标量和向量输入与输出信号。
- `Function Call` — 当仿真执行一个已调度时间步时，模块生成一个函数调用事件。仅支持标量输入信号。

#### 编程使用

|  |
| --- |
| **模块参数：** `HitSchedulerOutputType` |
| **类型：** string | character vector |
| **值：** `'Signal'` | `'Function-Call'` |
| **默认：** `'Signal'` |

### **Initial buffer size** — 用于已调度时间步的缓冲区初始大小 `256`（默认）| integer

指定存储已调度时间步的缓冲区大小，为正的标量整数值。

默认情况下，缓冲区大小是动态的，因此软件可以在仿真期间缓冲区填满时增大大小。当你选择 **Use fixed buffer size** 时，**Initial buffer size** 参数值指定缓冲区的固定大小。如果仿真期间缓冲区溢出，Hit Scheduler 模块会以先进先出方式覆盖已调度时间命中。

#### 编程使用

|  |
| --- |
| **模块参数：** `InitialBufferSize` |
| **类型：** string | character vector |
| **值：** 正的、整数的数值标量 |
| **默认：** `'256'` |

### **Use fixed buffer size** — 使用固定大小缓冲区的选项 `off`（默认）| `on`

当你选择此选项时，该模块使用固定缓冲区大小，并且 **Initial buffer size** 参数指定缓冲区的大小。如果仿真期间缓冲区溢出，Hit Scheduler 模块会以先进先出方式覆盖已调度时间命中。默认情况下，缓冲区大小是动态的，因此软件可以在仿真期间根据需要调整大小。

#### 编程使用

|  |
| --- |
| **模块参数：** `FixedBuffer` |
| **类型：** string | character vector |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

## 所属库

Simulink / Messages & Events

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

为变步长求解器调度主时间步

使用 Hit Scheduler 模块在仿真期间为变步长求解器调度主时间步。借助 Hit Scheduler 模块，你可以基于模型在仿真期间的行为实现动态求解器命中事件调度。

要调度主时间步，你需要为该模块提供两个输入：

- **En** — 使能输入控制该模块何时调度时间步。当输入为逻辑 `true` 时，该模块调度一个时间步。
- **Δt** — 时间间隔输入指定已调度时间步何时发生。Hit Scheduler 模块计算要调度的时间命中，以 seconds 为单位，为当前仿真时间与时间间隔输入之和。

当仿真到达已调度时间命中时，仿真会执行主时间步，并且模块输出会更新。你可以使用 **Output type** 参数配置该模块生成信号输出或函数调用输出。

你可以使用 Hit Scheduler 模块调度多个未来时间步。该模块将未来时间步存储在一个队列中，你可以使用 **Initial buffer size** 和 **Use fixed buffer size** 参数配置该队列。

### 向量信号输入和输出

当你将该模块配置为生成信号输出时，你可以使用单个模块，通过向量输入基于模型中的多个信号调度时间命中。**En** 输入向量中的每个元素指示该模块何时应基于 **Δt** 向量中的相同元素调度时间命中。模块输出信号与输入信号具有相同维度。当仿真执行一个已调度步时，输出向量中与调度了该时间步的输入向量元素对应的元素从逻辑 `false` 变为逻辑 `true`。
