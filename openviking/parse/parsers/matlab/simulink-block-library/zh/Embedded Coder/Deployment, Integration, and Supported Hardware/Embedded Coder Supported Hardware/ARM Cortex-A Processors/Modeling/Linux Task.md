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
language: zh-CN
chinese_source: worker-translation
---

# Linux Task

## 端口

### 输出

### **Port\_1** — 函数调用控制信号标量

一种函数调用控制信号，可触发 Function-Call Subsystem 模块。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条上，在 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **任务名称（不超过 32 个字符）** — Linux 上线程的名称 `Task0`（默认） | character vector

指定此任务的名称。最多可以输入 32 个字符，字符可以是字母、数字或字母和数字的组合。

#### 编程用法

|  |
| --- |
| **模块参数：** `taskName` |

### **线程调度策略** — Linux 使用的线程调度策略 `SCHED_FIFO`（默认） | `SCHED_OTHER`

选择适用于此线程的调度策略。你可以从以下选项中选择：

- `SCHED_FIFO` — 此选项启用先进先出（FIFO）调度算法，该算法在没有时间片的情况下执行实时进程。使用 FIFO 调度时，较高优先级的进程会抢占较低优先级的进程。较低优先级的进程仍处于其优先级的列表顶部，并当调度器阻塞所有更高优先级进程时恢复执行。

  例如，在 FIFO 调度图中，task2 抢占 task1，task3 抢占 task2。当 task3 完成时，task2 恢复。当 task2 完成时，task1 恢复。

  Linux Task 模块使用 FIFO 调度。

  `SCHED_FIFO` 会显示 **线程优先级** 参数，你可以将其设置为 1 到 99 之间的值。
- `SCHED_OTHER` — 此选项启用默认的 Linux 分时调度算法。你可以将此调度用于所有进程，但需要特殊静态优先级实时机制的进程除外。使用此算法时，调度器根据静态优先级 0 列表中的动态优先级选择进程。每次进程准备好运行但调度器拒绝其运行时，操作系统都会增加该进程的动态优先级。此类优先级排序有助于调度器服务 `SCHED_OTHER` 进程。

  选择 `SCHED_OTHER` 会隐藏 **线程优先级** 参数，并将线程优先级设置为 0。

#### 编程用法

|  |
| --- |
| **模块参数：** `taskPolicy` |

### **线程优先级** — Linux 线程优先级 `1`（默认） | `1 .. 99`

指定 Linux 线程的优先级。值 1 表示低优先级，值 99 表示高优先级。较高优先级的任务可以抢占较低优先级的任务。

要启用此参数，请将 **线程调度策略** 设置为 `SCHED_FIFO`。

要启用此参数，请将 **线程调度策略** 设置为 `SCHED_FIFO`。

#### 编程用法

|  |
| --- |
| **模块参数：** `taskPriority` |

## 所属库

Embedded Coder Support Package for ARM Cortex-A Processors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

将任务函数作为单独的 Linux 线程生成

使用此模块创建任务函数，该函数作为单独的 Linux® 线程生成。该任务函数运行下游 Function-Call Subsystem 模块的代码。
