---
type: simulink-block
title: 'Idle Task'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Utilities'
documentation_page: 'idletask'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/idletask.html'
language: zh-CN
chinese_source: worker-translation
---

# Idle Task

## 端口

### 输入

### **Port\_1** — 仿真中断 标量 | 向量

用于在 Simulink® 仿真期间测试异步中断行为的可选仿真中断。

#### 端口依赖关系

要启用此端口，请选择参数 **Enable simulation input**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 输出

### **Port\_1** — 任务标识符和抢占标志向量

用于标识后台任务的编号和任务抢占标志，以向量形式表示。任务标识符向量存储用于标识后台任务的编号。

对于每个后台任务，抢占标志向量存储一个标志，用于指示该任务是否可被抢占。除非抢占标志向量包含一个元素，否则抢占标志向量中的元素数量必须与任务标识符向量的长度匹配。如果抢占标志向量与任务标识符向量具有相同数量的元素，则任务标识符向量中表示的每个任务具有由抢占标志向量中对应元素的值定义的抢占设置。当抢占标志向量包含一个元素时，该标志设置适用于整个任务标识符向量。

较高优先级任务不能抢占不可被抢占的较低优先级任务。

**数据类型：** `uint8`

## 参数

### **Task numbers** — 所创建任务的标识符 [1 2]（默认）| 0 到 15 范围内的整数向量

将下游子系统中的函数的任务标识符指定为 0 到 15 范围内的整数向量。该向量包含的值数量必须与下游子系统中的函数数量相同。例如，默认向量 `[1 2]` 表示下游子系统包含两个函数。

输入的值数量对应于下游子系统中的函数数量。指定的值决定函数的执行顺序。例如，向量 `[2 3 1]` 表示：

- 子系统包含三个函数。
- 第三个函数首先执行。
- 第一个函数第二个执行。
- 第二个函数第三个执行。

函数执行完后，Idle Task 模块会循环返回，并以相同顺序重复执行这些函数。

### **Preemption flags** — 指定任务的抢占标志 [0 1]（默认）| [ 0, 1] 范围内的 0 到 16 个整数的向量

为 **Task numbers** 参数指定的任务指定抢占标志，形式为最多包含 16 个 1 和 0 的向量。较高优先级中断可以抢占具有较低优先级的中断。要控制抢占，请使用抢占标志指定某个中断是否可被抢占。

值 `1` 表示对应任务的中断可被抢占。值 `0` 表示该中断不可被抢占。您可以选择指定：

- 一个抢占值，适用于为 **Task numbers** 指定的整个向量。
- 为 **Task numbers** 指定的向量中标识的每个任务指定一个抢占值。请按照与 **Task numbers** 中任务顺序对应的顺序指定标志值。

例如，如果为 **Task numbers** 指定向量 `[2 3 1]`，并为 **Preemption flags** 指定 `[0]`，则任务 `1`、`2` 和 `3` 不能被抢占。如果为 **Preemption flags** 指定 `[1 1 0]`，则任务 `2` 和 `3` 可被抢占，任务 `1` 不能被抢占。

### **Enable idle task block for profiling** — 启用 profiling off（默认）| on

启用此参数后，当启用 profiling 时，可以测量空闲任务执行时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

## 描述

创建自由运行任务

Idle Task 模块及其连接到的子系统指定下游子系统中的函数作为后台任务执行。通过 Idle Task 模块执行的任务具有最低优先级，低于基础速率任务的优先级。

启用参数 **Enable idle task block for profiling** 后，当启用 profiling 时，可以测量空闲任务执行时间。

### 向量化输出

模块输出由一组向量组成——任务编号向量和抢占标志向量（一个或多个）。抢占标志向量必须与任务数量向量长度相同，除非抢占标志向量只有一个元素。抢占标志的值决定给定中断（和任务）是否可被抢占。抢占会覆盖优先级排序。较低优先级的不可抢占任务可以抢占较高优先级的可抢占任务。

当抢占标志向量只有一个元素时，该元素值适用于下游子系统中的函数，这些函数由任务编号向量中的任务编号定义。如果抢占标志向量与任务编号向量具有相同数量的元素，则任务编号向量中定义的每个任务具有由抢占标志向量中对应元素的值定义的抢占状态。
