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

### 输出

### ***`Task1`*** — 来自 Task1 的函数调用标量

一个函数调用信号，可触发事件驱动任务。CLA Model 模块将这些任务表示为函数调用子系统。

要显示来自 Model 模块上 Function-Call Subsystem 模块中包含的事件驱动子系统的函数调用端口，请在 processor Model 模块中包括一个 Inport，并将其连接到该子系统的函数调用触发端口。在该 Inport 中，选择 **模块参数** > **信号属性** > **输出函数调用**。

**注意**

`Task1` 端口必须连接到 Model 模块上的函数调用端口。

#### 依赖关系

要为任务创建或删除控制信号端口，请通过单击模块对话框掩码中的 **添加** 或 **删除** 按钮，从 CLA Task Manager 模块中添加或删除任务。

### 输入

### ***`Task1`*Event** — 消息事件通知标量

一个消息端口，用于触发关联的事件驱动任务。`Task1Event` 端口从 Software Trigger CPU<->CLA、PWM Interface (SoC Blockset) 或 ADC Interface (SoC Blockset) 模块接收消息。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

要显示 `Task1Event` 端口，请将 `Task1` 的 **类型** 参数设置为 `Event-driven`。

**数据类型：** `rteEvent`

### ***`Task1`*Dur** — 任务持续时间正标量

一个正值信号，用于指定任务在当前时间的执行持续时间。有关指定任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

#### 依赖关系

要启用此端口，请将 **通过以下方式指定任务持续时间** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **启用任务仿真** — 用于启用任务持续时间仿真的选项 `on`（默认） | `off`

启用或禁用任务持续时间的仿真。如果清除此参数，任务将使用函数调用生成器进行仿真。事件驱动任务从模型的基本采样时间继承其周期。定时器驱动任务从模块对话框掩码继承其周期。

### **任务列表** — 任务列表 `Task1`（默认）

由 CLA Task Manager 模块生成的任务列表。每个任务都有一组参数，列在模块对话框掩码的 **主要** 和 **仿真** 选项卡中。

### **添加** — 用于添加任务的按钮选项

向 CLA Task Manager 模块添加任务。在部署期间，生成的代码将每个任务封装为中断。每个任务的 **主要** 参数定义其中断的属性。在仿真期间，任务使用该任务的 **主要** 和 **仿真** 参数的组合。

### **删除** — 用于删除现有任务的按钮选项

从任务管理器中删除任务。

#### 依赖关系

要启用此参数，请指定至少两个任务。

### 主要

### **名称** — 任务名称 `Task1`（默认） | 字符向量

任务的唯一名称。任务名称只能包含字母数字字符和下划线。

### **优先级** — 任务在调度器中的优先级 `10`（默认） | [1, 99] 范围内的整数

将事件驱动任务的调度器优先级指定为 [1, 99] 范围内的整数。较高优先级任务可以抢占较低优先级任务。硬件属性会限制任务优先级范围。有关任务优先级的详细信息，请参阅 Task Priority and Preemption (SoC Blockset)。

#### 依赖关系

要启用此参数，请将 `Type` 设置为 `Event-driven`。

### 仿真

### **通过以下方式指定任务持续时间** — 任务执行时间的来源 `Dialog`（默认） | `Input port` | `Record task execution statistics`

将任务执行的时序信息来源指定为以下选项之一。

- `Dialog` — 使用正态分布概率模型，其 **均值**、**标准差**、**最小值** 和 **最大值** 在模块对话框掩码中定义。
- `Input port` — 模块输入端口动态定义执行持续时间。
- `Record task execution statistics` — 使用正态分布概率模型，其均值和标准差在 **文件名** 指定的文件中定义。

有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

#### 任务持续时间设置

### **添加** — 用于添加分布的按钮选项

向生成执行持续时间的正态分布集合中添加一个分布。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

**注意**

最多只能将五个分布分配给单个任务。

### **删除** — 用于删除分布的按钮选项

从正态分布集合中删除一个分布。

### **百分比** — 分布的可能性 `100`（默认） | 正标量

指定每个正态分布的可能性。正态分布的 **百分比** 加权和决定任务持续时间可能性。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

**注意**

单个任务中所有分布的 **百分比** 之和必须等于 100。

### **均值** — 仿真中的平均任务持续时间 `1e-06`（默认） | 正标量

指定任务仿真期间的平均任务持续时间。仿真的任务持续时间使用具有指定 **均值** 和 **标准差** 参数值的正态分布，作为任务行为的一阶近似。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

### **标准差** — 仿真中任务持续时间的标准差 `0`（默认） | 正标量

指定任务仿真期间的任务持续时间标准差。仿真的任务持续时间使用具有指定 **均值** 和 **标准差** 的正态分布，作为任务行为的一阶近似。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

### **最小值** — 任务持续时间的下限 `1e-06`（默认） | 正标量

任务持续时间分布的下限。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

### **最大值** — 任务持续时间的上限 `1e-06`（默认） | 正标量

任务持续时间分布的上限。有关配置任务持续时间的详细信息，请参阅 Task Duration (SoC Blockset)。

## 所属库

C2000 Microcontroller Blockset / Scheduling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

在 Control Law Accelerator (CLA) 模型中创建和管理任务执行

CLA Task Manager 模块仿真软件任务的执行，如同它们在 CLA 处理器上预期会表现的行为。使用此模块，您可以从模型中添加和删除事件驱动任务。任务可以表示为包含在单个 Model 模块内的函数调用子系统。CLA Task Manager 模块根据任务的参数执行各个任务。任务参数包括持续时间、触发和优先级

**注意**

CLA Task Manager 模块不能在引用模型中使用。有关引用模型的详细信息，请参阅 Model 模块。

CLA Task Manager 模块提供了三种在仿真中指定任务持续时间的方法：

- 在模块掩码中定义的任务持续时间概率模型。
- 记录先前任务仿真或 SoC 设备上任务的数据文件。
- 输入端口，您可以将其连接到更动态的任务持续时间模型。
