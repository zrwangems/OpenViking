---
type: simulink-block
title: 'Proxy Task'
family: 'processor-task-execution'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Task Execution'
documentation_page: 'proxytask'
documentation_source_path: 'ref/proxytask.html'
language: zh-CN
chinese_source: worker-translation
---

# Proxy Task

## 端口

### 输入

### **Port\_1** — 来自 `Task Manager` 模块的 Function-call 标量

一种 function-call 信号，当作为 event-driven 任务运行时触发 Proxy Task 模块。

#### 依赖关系

要启用此端口，请将 `Type` 属性设置为 `Event-driven`。

**数据类型：** `function-call`

## 参数

### **Type** — 任务类型 `Timer-driven`（默认）| `Event-driven`

选择任务类型为 Timer-driven 或 Event-driven。

### **Sample Time** — 采样时间 1（默认）| 正标量

模块的采样时间。

**注意**

- Proxy Task 模块的 `Sample Time` 必须与 Task Manager 模块中对应 timer-driven 任务的采样时间匹配。
- Proxy Task 模块的 `Sample Time` 在模型中应是唯一的。当模型中的其他模块使用相同的采样时间时，由 Proxy Task 模块定义的任务持续时间在代码生成中无法得到保证。

#### 依赖关系

要启用此参数，请将 `Type` 属性设置为 `Timer-driven`。

## 所属库

SoC Blockset / Processor Task Execution

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

应用程序中任务的占位符

Proxy Task 模块可在没有显式实现的情况下模拟 SoC 应用程序中 timer-driven 任务的效果。此模块可用作将来开发或由另一位开发人员同时实现的 timer-driven 任务的占位符。

当添加到 processor reference Model 模块时，它会使处理器模型在设置为按端口调度速率时显示一个周期事件端口，其采样时间等于 `Sample Time` 参数。将该周期事件端口连接到 Task Manager 模块上的 timer-driven 任务输出端口。
