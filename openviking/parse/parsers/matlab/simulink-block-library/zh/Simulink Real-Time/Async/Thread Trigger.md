---
type: simulink-block
title: 'Thread Trigger'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Async'
documentation_page: 'threadtrigger'
documentation_source_path: 'io_ref/threadtrigger.html'
language: zh-CN
chinese_source: worker-translation
---

# Thread Trigger

## 端口
```yaml
ports:
- name: T
  summary: 针对所选跳变进行测试的触发输入 boolean
  direction: input
- name: F
  summary: 任务函数调用的函数调用输出
  direction: output
```

### 输入

### **T** — 针对所选跳变进行测试的触发输入 boolean

检测通过 **Trigger Edge** 参数选择的边沿类型，检测到为 1，未检测到为 0。

**示例：**
`0`
### 输出

### **F** — 任务函数调用的函数调用输出

输出对下游函数的调用，并提供该任务的线程调度优先级
## 参数
```yaml
parameters:
- name: Trigger Edge
  summary: 选择触发边沿类型 Rising Edge（默认）| Falling Edge | Both Edges
  group: ''
  block_parameter: edge
- name: ISR Task Priority
  summary: 选择函数的 ISR 任务优先级 245（高优先级）（默认）| 235（中优先级）| 225（低优先级）
  group: ''
  block_parameter: taskpri
```

### **Trigger Edge** — 选择触发边沿类型 `Rising Edge`（默认）| `Falling Edge` | `Both Edges`

选择由模块输入检测的触发边沿类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`edge` |

### **ISR Task Priority** — 选择函数的 ISR 任务优先级 `245`（高优先级）（默认）| `235`（中优先级）| `225`（低优先级）

选择函数调用的中断服务例程 (ISR) 任务优先级。您可以选择从 254（最高优先级）到 193（最低优先级）的任务优先级值。

Thread Trigger 模块提供了调用 Function-Call Subsystem 模块或 Triggered Subsystem 模块的方法，该模块是一个单独的模型线程。此线程可以以高于或低于其他执行线程的优先级运行。模型中的每个速率组作为不同的执行线程执行。有关详细信息，请参阅 About RTOS Tasks and Priorities。

#### 编程使用

|  |
| --- |
| **模块参数**：`taskpri` |
## 所属库

Simulink Real-Time / Async

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2022b: 移除了 Thread Trigger 模块采样时间参数

Thread Trigger 模块的 Sample Time 参数已移除。该模块从模块的输入信号继承采样时间。

## 描述

当所选输入边沿跳变发生时，调用下游函数调用子系统

当所选输入边沿跳变发生时，Thread Trigger 模块调用下游 Function-Call Subsystem 模块或 Triggered Subsystem 模块，并设置任务的中断优先级。该模块以模块采样率检查边沿跳变。

如果输入跳变在任务运行期间发生，则 Speedgoat® 目标计算机上会发生 CPU 过载。

您可以将 Thread Trigger 模块与位于引用模型内部的 Function-Call Subsystem 模块一起使用，如图所示。此方法兼容 Simulink® Coder™。由于 Thread Trigger 模块输出信号是异步的，并且 Simulink Coder 不允许在引用模型内部使用异步输出模块，因此请将 Thread Trigger 模块放在模型的顶层。此方法不允许显式分区。请记住将 Asynchronous Task Specification 优先级（`P:245`）与 Thread Trigger 模块中选择的优先级匹配。有关详细信息，请参阅 About RTOS Tasks and Priorities。

此模型展示了 Thread Trigger 模块与引用模型一起使用的情况。
