---
type: simulink-block
title: 'VxWorks Task'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-A Processors / Modeling'
documentation_page: 'vxworkstask'
documentation_source_path: 'armcortexa/ref/vxworkstask.html'
language: zh-CN
chinese_source: worker-translation
---

# VxWorks Task

## 端口

### 输出

### **Port\_1** — 函数调用控制信号标量

一个函数调用控制信号，用于触发 Function-Call Subsystem 模块。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **任务函数名称** — VxWorks 上线程的名称 `'Task0'` (默认) | character vector

指定此任务的名称。最多可以输入 32 个字母、数字或字母和数字的组合。

#### 编程用法

|  |
| --- |
| **模块参数：** `taskName` |

### **线程优先级** — VxWorks 线程的优先级 `0` (默认) | `0 .. 255`

指定 VxWorks 线程的优先级，范围为 0 到 255（从低到高）。较高优先级的任务可以抢占较低优先级的任务。

#### 编程用法

|  |
| --- |
| **模块参数：** `taskPriority` |

## 所属库

Embedded Coder Support Package for ARM Cortex-A Processors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014a 中引入**

## 描述

将任务函数生成为单独的 VxWorks 线程

VxWorks Task 模块创建一个任务函数，该函数生成为单独的 VxWorks® 线程。该任务函数运行下游 Function-Call Subsystem 模块的代码。

VxWorks Task 模块使用先进先出 (FIFO) 调度算法，该算法执行实时进程时不进行时间分片。使用 FIFO 调度时，较高优先级的进程会抢占较低优先级的进程。当较高优先级进程运行时，较低优先级进程仍位于其优先级列表的顶部。当调度器阻塞较高优先级进程时，较低优先级进程会恢复运行。

VxWorks Task 模块使用 FIFO 调度。
