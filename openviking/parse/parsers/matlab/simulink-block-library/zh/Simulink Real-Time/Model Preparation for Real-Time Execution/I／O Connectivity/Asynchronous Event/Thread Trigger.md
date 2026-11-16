---
type: simulink-block
title: 'Thread Trigger'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Asynchronous Event'
documentation_page: 'threadtrigger'
documentation_source_path: 'io_ref/threadtrigger.html'
language: zh-CN
chinese_source: official
---

# Thread Trigger

## 端口

### 输入

### **T** — 触发输入已针对所选转换进行测试 布尔值

检测边缘类型，通过将 **Trigger Edge** 参数设为 1 表示检测到边缘，设为 0 表示未检测到边缘。

**示例:**  `0`
### 输出

### **F** — 任务的函数调用输出 函数调用

输出对下游函数的调用，并为任务提供线程调度优先级

## 参数

### **Trigger Edge** — 选择触发沿类型 `Rising Edge` (默认) | `Falling Edge` | `Both Edges`

选择由模块输入检测到的触发沿类型。

#### 编程用法

|  |
| --- |
| **模块参数：**`edge` |

### **ISR Task Priority** — 为函数选择 ISR 任务优先级 `245`（高优先级） (默认) | `235`（中等优先级） | `225`（低优先级）

为函数调用选择中断服务例程 (ISR) 任务优先级。您可以从 254（最高优先级）到 193（最低优先级）之间选择任务优先级值。

Thread Trigger 块提供了调用独立模型线程中的 Function-Call Subsystem 块或 Triggered Subsystem 块的机制。该线程的运行优先级可高于或低于其他执行线程。模型中的每个利率组都作为不同的执行线程运行。有关详细信息，请参阅关于实时操作系统任务与优先级。

#### 编程用法

|  |
| --- |
| **模块参数：**`taskpri` |

## 所属库

Simulink Real-Time / Async

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

### R2022b: 已移除 Thread Trigger 模块采样时间参数

已移除 Thread Trigger 模块的采样时间参数。该模块从输入信号继承采样时间。

## 描述

当选定的输入边发生转换时，调用下游函数调用子系统

Thread Trigger 模块在选定输入沿发生变化时，调用下游的 Function-Call Subsystem 模块或 Triggered Subsystem 模块，并设置任务的中断优先级。该模块以模块采样率检测边缘转换。

若输入转换发生在任务运行期间，则会导致 Speedgoat® 目标计算机出现 CPU 过载。

如图所示，您可以将 Thread Trigger 块与位于引用模型内的 Function-Call Subsystem 块配合使用。此方法与 Simulink® Coder™ 兼容。由于 Thread Trigger 模块的输出信号为异步信号，且 Simulink Coder 不允许在引用的模型内部放置异步输出模块，因此请将 Thread Trigger 模块放置在模型的顶层。此方法不允许显式分区。请确保将异步任务规范优先级 (`P:245`) 与 Thread Trigger 模块中选定的优先级保持一致。有关详细信息，请参阅 About RTOS Tasks and Priorities。

This model shows Thread Trigger block usage with referenced model.
