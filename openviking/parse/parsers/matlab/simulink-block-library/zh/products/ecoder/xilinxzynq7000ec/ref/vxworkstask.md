---
type: simulink-block
title: 'VxWorks Task'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'vxworkstask'
documentation_source_path: 'xilinxzynq7000ec/ref/vxworkstask.html'
language: zh-CN
chinese_source: worker-translation
---

# VxWorks Task

## 端口

### 输出

### **Port\_1** — 函数调用控制信号标量

用于触发 Function-Call Subsystem 模块的函数调用控制信号。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。从 Simulink® 工具条中，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **任务函数名称** — VxWorks 上的线程名称 `'Task0'`（默认）| character vector

为此任务分配名称。最多可以输入 32 个字母和数字。不要使用标准 `C` 保留字符，例如 `/` 和 `:` 字符。

#### 程序化使用

|  |
| --- |
| **模块参数：** `taskName` |

### **线程优先级** — Linux 线程优先级 `1`（默认）| `1 .. 99`

当将 **线程调度策略** 设置为 `SCHED_FIFO` 时，可以将线程的优先级设置为 1 到 99（从低到高）。较高优先级任务可以抢占较低优先级任务。

#### 程序化使用

|  |
| --- |
| **模块参数：** `taskPriority` |

## 所属库

Embedded Coder Support Package for AMD SoC Devices

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将任务函数派生为单独的 VxWorks 线程

使用此模块创建任务函数，该函数会派生为单独的 VxWorks® 线程。该任务函数运行下游 Function-Call Subsystem 模块的代码。

VxWorks Task 模块使用先进先出（FIFO）调度算法，该算法执行实时进程时不进行时间分片。使用 FIFO 调度时，较高优先级进程会抢占较低优先级进程。当较高优先级进程运行时，较低优先级进程仍留在其优先级列表的顶部。当调度器阻塞较高优先级进程时，较低优先级进程会恢复运行。

默认线程调度策略为 FIFO Scheduling。
