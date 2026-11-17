---
type: simulink-block
title: 'CLA Task Manager'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'clataskmanager'
documentation_source_path: 'ref/clataskmanager.html'
language: zh-CN
chinese_source: worker-translation
---

# CLA Task Manager

## 端口
```yaml
ports:
- name: '*Task1*'
  summary: 来自 Task1 的函数调用 标量
  direction: output
- name: '*Task1*Event'
  summary: 消息事件通知 标量
  direction: input
  data_types: rteEvent
- name: '*Task1*Dur'
  summary: 任务持续时间 正标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
```

### 输出

### ***`Task1`*** — 来自 Task1 的函数调用 标量

一种可触发事件驱动任务的函数调用信号。CLA Model 模块将这些任务表示为函数调用子系统。

要显示 Model 模块上 Function-Call Subsystem 模块中包含的事件驱动子系统的函数调用端口，请在处理器 Model 模块中包含一个 Inport，并将其连接到该子系统的函数调用触发端口。在 Inport 中，选择 **Block Parameters** > **Signal Attributes** > **Output function call**。

**注意**

`Task1` 端口必须连接到 Model 模块上的函数调用端口。

#### 依赖关系

要为任务创建或移除控制信号端口，请通过点击模块对话框掩码中的 **Add** 或 **Delete** 按钮，在 CLA Task Manager 模块中添加或移除该任务。
### 输入

### ***`Task1`*Event** — 消息事件通知 标量

一种消息端口，用于触发关联的事件驱动任务。`Task1Event` 端口接收来自 Software Trigger CPU<->CLA、PWM Interface (SoC Blockset) 或 ADC Interface (SoC Blockset) 模块的消息。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

要显示 `Task1Event` 端口，请将 `Task1` 的 **Type** 参数设置为 `Event-driven`。

**数据类型：** `rteEvent`

### ***`Task1`*Dur** — 任务持续时间 正标量

一个正值信号，用于指定任务在当前时间的执行持续时间。有关指定任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

#### 依赖关系

要启用此端口，请将 **Specify task duration via** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
## 参数
```yaml
parameters:
- name: Enable task simulation
  summary: 启用任务持续时间仿真的选项 on（默认）| off
  group: ''
- name: List of tasks
  summary: 任务列表 Task1（默认）
  group: ''
- name: Add
  summary: 添加任务选项 按钮
  group: ''
- name: Delete
  summary: 删除现有任务选项 按钮
  group: ''
- name: Name
  summary: 任务名称 Task1（默认）| 字符向量
  group: 主要参数
- name: Priority
  summary: 任务在调度器中的优先级 10（默认）| [1, 99] 范围内的整数
  group: 主要参数
- name: Specify task duration via
  summary: 任务执行时间的来源 Dialog（默认）| Input port | Record task execution statistics
  group: 仿真
- name: Add
  summary: 添加分布选项 按钮
  group: 仿真
- name: Delete
  summary: 移除分布选项 按钮
  group: 仿真
- name: Percent
  summary: 分布的可能性 100（默认）| 正标量
  group: 仿真
- name: Mean
  summary: 仿真中的平均任务持续时间 1e-06（默认）| 正标量
  group: 仿真
- name: SD
  summary: 仿真中任务持续时间的标准差 0（默认）| 正标量
  group: 仿真
- name: Min
  summary: 任务持续时间下限 1e-06（默认）| 正标量
  group: 仿真
- name: Max
  summary: 任务持续时间上限 1e-06（默认）| 正标量
  group: 仿真
```

### **Enable task simulation** — 启用任务持续时间仿真的选项 `on`（默认）| `off`

启用或禁用任务持续时间的仿真。如果清除此参数，任务将使用函数调用生成器进行仿真。事件驱动任务从模型的基本采样时间继承其周期。定时器驱动任务从模块对话框掩码继承其周期。

### **List of tasks** — 任务列表 `Task1`（默认）

CLA Task Manager 模块生成的任务列表。每个任务都有一组参数，列在模块对话框掩码的 **Main** 和 **Simulation** 选项卡中。

### **Add** — 添加任务选项 按钮

向 CLA Task Manager 模块添加任务。在部署期间，生成的代码将每个任务封装为一个中断。每个任务的 **Main** 参数定义其中断的属性。在仿真期间，任务使用该任务的 **Main** 和 **Simulation** 参数的组合。

### **Delete** — 删除现有任务选项 按钮

从 Task Manager 中移除任务。

#### 依赖关系

要启用此参数，请指定至少两个任务。

### 主要参数

### **Name** — 任务名称 `Task1`（默认）| 字符向量

任务的唯一名称。任务名称只能包含字母数字字符和下划线。

### **Priority** — 任务在调度器中的优先级 `10`（默认）| [1, 99] 范围内的整数

将事件驱动任务在调度器中的优先级指定为 [1, 99] 范围内的整数。较高优先级的任务可以抢占较低优先级的任务。硬件属性限制了任务优先级范围。有关任务优先级的详细信息，请参阅 Task Priority and Preemption (SoC Blockset)。

#### 依赖关系

要启用此参数，请将 `Type` 设置为 `Event-driven`。

### 仿真

### **Specify task duration via** — 任务执行时间的来源 `Dialog`（默认）| `Input port` | `Record task execution statistics`

将任务执行的时序信息来源指定为以下选项之一。

- `Dialog` — 使用在模块对话框掩码中定义的 **Mean**、**Deviation**、**Min** 和 **Max** 的正态分布概率模型。
- `Input port` — 模块输入端口动态定义执行持续时间。
- `Record task execution statistics` — 使用在 **File name** 指定的文件中定义的均值和偏差的正态分布概率模型。

有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

#### 任务持续时间设置

### **Add** — 添加分布选项 按钮

向生成执行持续时间的正态分布集合中添加一个分布。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

**注意**

单个任务最多只能分配五个分布。

### **Delete** — 移除分布选项 按钮

从正态分布集合中移除一个分布。

### **Percent** — 分布的可能性 `100`（默认）| 正标量

指定每个正态分布的可能性。正态分布的 **Percent** 加权和决定任务持续时间的可能性。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

**注意**

单个任务中所有分布的 **Percent** 之和必须等于 100。

### **Mean** — 仿真中的平均任务持续时间 `1e-06`（默认）| 正标量

指定任务仿真期间的平均任务持续时间。仿真的任务持续时间使用具有指定 **Mean** 和 **SD** 参数值的正态分布，作为任务行为的一阶近似。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

### **SD** — 仿真中任务持续时间的标准差 `0`（默认）| 正标量

指定任务仿真期间任务持续时间的标准差。仿真的任务持续时间使用具有指定 **Mean** 和 **SD** 的正态分布，作为任务行为的一阶近似。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

### **Min** — 任务持续时间下限 `1e-06`（默认）| 正标量

任务持续时间分布的下限。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

### **Max** — 任务持续时间上限 `1e-06`（默认）| 正标量

任务持续时间分布的上限。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。
## 所属库

C2000 Microcontroller Blockset / Scheduling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

在 Control Law Accelerator (CLA) 模型中创建和管理任务执行

CLA Task Manager 模块仿真软件任务的执行，如同它们在 CLA 处理器上预期表现的那样。使用此模块，您可以在模型中添加和移除事件驱动任务。任务可以表示为包含在单个 Model 模块内的函数调用子系统。CLA Task Manager 模块根据其参数执行各个任务。任务参数包括持续时间、触发和优先级

**注意**

CLA Task Manager 模块不能在引用模型中使用。有关引用模型的详细信息，请参阅 Model 模块。

CLA Task Manager 模块提供三种在仿真中指定任务持续时间的方法：

- 在模块掩码中定义的任务持续时间概率模型。
- 记录先前任务仿真或 SoC 设备上任务的数据文件。
- 输入端口，您可以将其连接到更动态的任务持续时间模型。
