---
type: simulink-block
title: 'Proxy Task'
family: 'soc'
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
```yaml
ports:
- name: Port_1
  summary: 来自 Task Manager 模块的函数调用 标量
  direction: input
  data_types: function-call
```

### 输入

### **Port\_1** — 来自 `Task Manager` 模块的函数调用 标量

当作为事件驱动任务运行时，触发 Proxy Task 模块的函数调用信号。

#### 依赖

要启用此端口，请将 `Type` 属性设置为
`Event-driven`。

**数据类型：** `function-call`
## 参数
```yaml
parameters:
- name: Type
  summary: 任务类型 Timer-driven（默认）| Event-driven
  group: ''
- name: Sample Time
  summary: 采样时间 1（默认）| 正标量
  group: ''
```

### **Type** — 任务类型 `Timer-driven`（默认）| `Event-driven`

将任务类型选择为 Timer-driven 或 Event-driven。

### **Sample Time** — 采样时间 1（默认）| 正标量

模块的采样时间。

**注意**

- Proxy Task 模块的 `Sample Time` 必须与 Task
  Manager 模块中对应定时器驱动任务的采样时间匹配。
- Proxy Task 模块的 `Sample Time` 在模型中应是唯一的。当模型中的其他模块使用相同的
  采样时间时，Proxy Task 模块所定义的任务持续时间在代码生成中
  无法得到保证。

#### 依赖

要启用此参数，请将 `Type` 属性设置为
`Timer-driven`。
## 所属库

SoC Blockset / Processor Task Execution

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

应用程序中任务的占位符

Proxy Task 模块在没有显式实现的情况下，模拟 SoC 应用程序中定时器驱动任务的效果。此模块可用作
将来开发或由另一位开发人员同时实现的定时器驱动任务的占位符。

当添加到处理器参考 Model 模块中时，它会使处理器模型在设置为按端口调度速率时，
显示一个周期事件端口，其采样时间等于 `Sample Time`
参数。将周期事件端口连接到 Task Manager
模块上的定时器驱动任务输出端口。
