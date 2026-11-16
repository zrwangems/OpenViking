---
type: simulink-block
title: 'Task Manager'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / Task Management'
documentation_page: 'taskmanager'
documentation_source_path: 'ref/taskmanager.html'
language: zh-CN
chinese_source: worker-translation
---

# Task Manager

## 端口

### 输出

### ***`Task1`*** — 来自 Task1 的函数调用标量

一个函数调用信号，可触发计时器驱动和事件驱动任务，分别表示为处理器 Model block 中的速率子系统或函数调用子系统。

对于来自计时器驱动子系统的速率端口，要在 Model block 上显示，请设置 **Block Parameters** > **Main** > **Schedule rates** 并选择端口。对于来自 Function-Call Subsystem 模块中包含的事件驱动子系统的函数调用端口，要在 Model block 上显示，请在处理器 Model block 中包含一个 Inport，并将其连接到该子系统的函数调用触发端口。在 Inport 中，选中 **Block Parameters** > **Signal Attributes** > **Output function call**。

**注意**

`Task1` 端口必须连接到 Model block 上的函数调用端口或调度速率信号端口。

#### 依赖关系

要为任务创建或移除控制信号端口，请通过单击模块对话框掩码中的 **Add** 或 **Delete** 按钮，在 Task Manager 模块中添加或移除该任务。
### 输入

### ***`Task1`*Event** — 消息事件通知标量

一个消息端口，用于触发关联的事件驱动任务。`Task1Event` 端口从 Event Source 模块接收消息。有关消息的详细信息，请参阅消息。

#### 依赖关系

要显示 `Task1Event` 端口，`Task1` 必须将 **Type** 设置为 `Event-driven`。

**数据类型：** `rteEvent`

### ***`Task1`*Dur** — 任务持续时间正标量

一个正值信号，用于指定任务在当前时间的执行持续时间。有关指定任务持续时间的详细信息，请参阅任务持续时间。

#### 依赖关系

要启用此端口，请将 **Specify task duration via** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Enable task simulation** — 启用任务持续时间的仿真 `on`（默认） | `off`

启用或禁用任务持续时间的仿真。如果清除此参数，任务将使用函数调用生成器进行仿真，对于事件驱动任务，其周期继承自模型的基础采样时间；对于计时器驱动任务，其周期继承自对话框。

### **List of tasks** — 任务列表 `Task1`（默认）

Task Manager 模块生成的任务列表。每个任务都有一组参数，列在模块对话框掩码的 **Main** 和 **Simulation** 选项卡中。

### **Add** — 添加任务按钮

向 Task Manager 模块添加任务。在部署期间，每个任务在生成的代码中封装为一个执行线程。线程的属性取自该任务的 **Main** 参数。在仿真期间，任务使用该任务的 **Main** 和 **Simulation** 参数的组合。

### **Delete** — 删除现有任务按钮

从 Task Manager 中移除任务。

#### 依赖关系

要启用此参数，请指定至少两个任务。

### **Use Schedule Editor ordering** — 使用 Schedule Editor 工具指定任务优先级 `off`（默认） | `on`

使用 Schedule Editor 指定 SoC 模型中任务的顺序。使用 Schedule Editor 时，任务优先级会根据它们在编辑器中的顺序以及处理器模型的基础速率优先级自动分配给任务。

### Main

### **Name** — 任务名称 `Task1`（默认） | 字符向量

任务的唯一名称。任务名称只能包含字母数字字符和下划线。

### **Type** — 任务的触发类型 `Timer-driven`（默认） | `Event-driven`

将任务指定为计时器驱动或事件驱动。有关计时器驱动和事件驱动任务的详细信息，请分别参阅计时器驱动任务 (SoC Blockset) 和事件驱动任务 (SoC Blockset)。

#### 依赖关系

要启用此参数，请将 `Type` 设置为 `Timer-driven`。

### **Period** — 计时器周期 `0.1`（默认） | 正标量

指定计时器驱动任务的触发时间周期。

### **Core** — 执行任务的处理器核心 `0`（默认） | 非负整数 | `-1`

指定任务执行的处理器核心编号。
.

要让操作系统动态地为任务分配核心，请将此值设置为 `-1`。

### **Priority** — 任务在调度器中的优先级 `10`（默认） | 正整数

指定事件驱动任务在调度器中的优先级，范围为 `1` 到 `99`。较高优先级任务可以抢占较低优先级任务，反之亦然。任务优先级范围受硬件属性限制。有关任务优先级的详细信息，请参阅任务优先级和抢占 (SoC Blockset)。

#### 依赖关系

要启用此参数，请将 `Type` 设置为 `Event-driven`，并将 `Use Schedule Editor ordering` 设置为 `off`。

### **Drop tasks that overrun** — 丢弃超限运行的任务 `off`（默认） | `on`

选择此参数可强制任务在发生超限运行后丢弃，而不是追赶。有关任务超限运行的详细信息，请参阅任务超限与应对措施 (SoC Blockset)。

**注意**

当 `Drop tasks that overrun` 设置为 `off` 时，一个任务最多只能有 2 个实例超限运行执行。任何额外超限运行的任务实例都会自动丢弃。

### Simulation

### **Play recorded task execution sequence** — 启用从文件回放 off（默认） | on

选择此参数，使 Task Manager 模块回放由指定 **File name** 参数提供的记录执行数据。有关回放任务执行的详细信息，请参阅使用记录数据进行任务执行回放。

### **Specify task duration via** — 任务执行时间的来源 `Dialog`（默认） | `Input port` | `Record task execution statistics`

指定任务执行时序信息的来源。

- `Dialog` - 使用正态分布概率模型，其 **Mean**、**Deviation**、**Min** 和 **Max** 在模块对话框掩码中定义。
- `Input port` – 当从 *Input port* 设置时，模块输入端口动态定义执行持续时间。
- `Record task execution statistics` – 使用正态分布概率模型，其均值和偏差由 **File name** 指定的文件提供。

有关配置任务持续时间的详细信息，请参阅任务持续时间。

#### 任务持续时间设置

### **Add** — 添加分布按钮

向生成执行持续时间的正态分布集合中添加一个分布。

**注意**

单个任务最多只能分配五个分布。

### **Delete** — 删除分布按钮

从正态分布集合中移除一个分布。

### **Percent** — 分布的可能性 `100`（默认） | 正标量

指定每个正态分布的可能性。正态分布的 **Percent** 加权和确定任务持续时间的可能性。

**注意**

单个任务中所有分布的 **Percent** 之和必须等于 `100`。

### **Mean** — 仿真中的平均任务持续时间 `1e-06`（默认） | 正标量

指定任务仿真期间任务的平均持续时间。仿真的任务持续时间使用具有指定 **Mean** 和 **SD** 参数值的正态分布，作为任务行为的一阶近似。

### **SD** — 仿真中任务持续时间的标准差 `0`（默认） | 正标量

指定任务仿真期间任务持续时间的标准差。仿真的任务持续时间使用具有指定 **Mean** 和 **SD** 的正态分布，作为任务行为的一阶近似。

### **Min** — 任务持续时间下限 `1e-06`（默认） | 正标量

任务持续时间分布的下限。

### **Max** — 任务持续时间上限 `1e-06`（默认） | 正标量

任务持续时间分布的上限。

### **File name** — 包含诊断调度数据的文件 filepath

此文件中的数据指定 **Mean** 和 **SD** 参数值。选中 **Play recorded task execution sequence** 参数时，指定的 CSV 文件提供显式任务执行时序。该 CSV 文件包含先前从硬件板记录的任务调度器诊断数据。

#### 依赖关系

要启用此参数，请将 **Specify task duration via** 参数设置为 `Recorded task execution statistics`。

## 所属库

SoC Blockset / Processor Task Execution C2000 Microcontroller Blockset / Scheduling Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Scheduling Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Scheduling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅《使用 SoC Builder 为 Infineon® AURIX™ TC3x 生成代码并部署》和《使用 SoC Builder 为 Infineon AURIX TC4x 微控制器生成代码并部署》。

Task Manager 模块中的任务在生成的代码中作为线程执行。Task Manager 模块中的任务参数指定线程的优先级和执行核心。

## 版本历史

**在 R2019a 中引入**

## 描述

在 Simulink 模型中创建和管理任务执行

Task Manager 模块仿真软件任务的执行，就像它们在 SoC 处理器上预期表现的那样。使用 Task Manager，您可以在模型中添加和删除任务，这些任务可以是计时器驱动或事件驱动。任务可以在模型中表示为速率（对于计时器驱动任务）或函数调用子系统（对于事件驱动任务），并包含在单个 Model block 中。Task Manager 根据任务的参数（例如周期、持续时间、触发、优先级或处理器核心）以及该任务与运行模型中其他任务状态及其优先级的组合来执行各个任务。

在仿真中，此模块使用代码生成来提高仿真速度。这会在首次仿真时带来一些开销，但如果模块设置保持不变，后续仿真会更快。有关详细信息，请参阅解释执行与代码生成。

**注意**

Task Manager 模块不能在引用模型中使用。有关引用模型的详细信息，请参阅 Model block。

Task Manager 模块提供三种方法来指定仿真中任务的持续时间：

- 在模块掩码中定义的任务持续时间概率模型。
- 来自先前任务仿真或来自 SoC 设备上任务的数据文件记录。
- 模块上的输入端口，您可以将其连接到更动态的任务持续时间模型。
