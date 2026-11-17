---
type: simulink-block
title: 'Task Manager'
family: 'scheduling'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'taskmanager'
documentation_source_path: 'ref/taskmanager.html'
language: zh-CN
chinese_source: worker-translation
---

# Task Manager

## 端口

### 输出

### ***`Task1`*** — 来自 Task1 的函数调用标量

一个函数调用信号，可触发定时器驱动和事件驱动任务，分别在处理器 Model block 中表示为速率子系统或函数调用子系统。

对于来自定时器驱动子系统的速率端口，要在 Model block 上显示，请设置 **Block Parameters** > **Main** > **Schedule rates** 并选择端口。对于包含在 Function-Call Subsystem block 中的事件驱动子系统的函数调用端口，要在 Model block 上显示，请在处理器 Model block 中包含一个 Inport，并将其连接到该子系统的函数调用触发端口。在 Inport 中，选中 **Block Parameters** > **Signal Attributes** > **Output function call**。

**注意**

`Task1` 端口必须连接到 Model block 上的函数调用端口或已调度速率信号端口。

#### 依赖项

要为任务创建或移除控制信号端口，请通过点击模块对话框掩码中的 **添加** 或 **删除** 按钮，在 Task Manager 模块中添加或移除任务。

### 输入

### ***`Task1`*Event** — 消息事件通知标量

一个消息端口，用于触发关联的事件驱动任务。`Task1Event` 端口从 Event Source 模块接收消息。有关消息的更多信息，请参阅 Messages。

#### 依赖项

要显示 `Task1Event` 端口，则 `Task1` 的 **类型** 必须设置为 `Event-driven`。

**数据类型：** `rteEvent`

### ***`Task1`*Dur** — 任务持续时间 positive scalar

一个正值信号，用于指定任务在当前时间的执行持续时间。有关指定任务持续时间的更多信息，请参阅 Task Duration (SoC Blockset)。

#### 依赖项

要启用此端口，请将 **通过以下方式指定任务持续时间** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **启用任务仿真** — 启用任务持续时间的仿真 `on` (默认) | `off`

启用或禁用任务持续时间的仿真。如果清除此参数，任务将使用函数调用生成器进行仿真：对于事件驱动任务，其周期继承自模型的基本采样时间；对于定时器驱动任务，其周期来自对话框。

### **任务列表** — 任务列表 `Task1` (默认)

Task Manager 模块生成的任务列表。每个任务都有一组参数，列在模块对话框掩码的 **Main** 和 **Simulation** 选项卡中。

### **添加** — 添加任务按钮

向 Task Manager 模块添加任务。在部署期间，每个任务在生成的代码中封装为一个执行线程。线程的属性取自该任务的 **Main** 参数。在仿真期间，任务使用该任务的 **Main** 和 **Simulation** 参数的组合。

### **删除** — 删除现有任务按钮

从 Task Manager 中移除任务。

#### 依赖项

要启用此参数，请至少指定两个任务。

### **使用 Schedule Editor 排序** — 使用 Schedule Editor 工具指定任务优先级 `off` (默认) | `on`

使用 Schedule Editor 指定 SoC 模型中任务的顺序。使用 Schedule Editor 时，任务优先级会根据任务在编辑器中的顺序以及处理器模型的基本速率优先级自动分配给任务。

### Main

### **名称** — 任务名称 `Task1` (默认) | character vector

任务的唯一名称。任务名称只能包含字母数字字符和下划线。

### **类型** — 任务的触发类型 `Timer-driven` (默认) | `Event-driven`

将任务指定为定时器驱动或事件驱动。有关定时器驱动任务和事件驱动任务的更多信息，请分别参阅 Timer-Driven Task (SoC Blockset) 和 Event-Driven Tasks (SoC Blockset)。

#### 依赖项

要启用此参数，请将 `Type` 设置为 `Timer-driven`。

### **周期** — 定时器周期 `0.1` (默认) | positive scalar

指定定时器驱动任务的触发时间周期。

### **核心** — 执行任务的处理器核心 `0` (默认) | non-negative integer | `-1`

指定任务执行的处理器核心编号。

要让操作系统动态为任务分配核心，请将此值设置为 `-1`。

### **优先级** — 调度器中任务的优先级 `10` (默认) | positive integer

指定事件驱动任务在调度器中的优先级，介于 `1` 和 `99` 之间。较高优先级任务可以抢占较低优先级任务，反之亦然。任务优先级范围受硬件属性限制。有关任务优先级的更多信息，请参阅 Task Priority and Preemption (SoC Blockset)。

#### 依赖项

要启用此参数，请将 `Type` 设置为 `Event-driven`，并将 `Use Schedule Editor ordering` 设置为 `off`。

### **丢弃超限运行的任务** — 丢弃超限运行的任务 `off` (默认) | `on`

选择此参数可强制任务在发生超限运行后丢弃，而不是追赶。有关任务超限运行的更多信息，请参阅 Task Overruns and Countermeasures (SoC Blockset)。

**注意**

当 `Drop tasks that overrun` 设置为 `off` 时，任务的超限运行执行实例不能超过 2 个。任何额外的超限运行任务实例都会自动丢弃。

### Simulation

### **播放记录的任务执行序列** — 启用从文件回放 off (默认) | on

选择此参数，使 Task Manager 模块回放由指定 **文件名** 参数提供的记录执行数据。有关回放任务执行的更多信息，请参阅 Task Execution Playback Using Recorded Data (SoC Blockset)。

### **通过以下方式指定任务持续时间** — 任务执行时间的来源 `Dialog` (默认) | `Input port` | `Record task execution statistics`

指定任务执行计时的信息来源。

- `Dialog` - 使用在模块对话框掩码中定义的 **均值**、**偏差**、**最小值** 和 **最大值** 的正态分布概率模型。
- `Input port` – 当从 *Input port* 设置时，模块输入端口动态定义执行持续时间。
- `Record task execution statistics` – 使用由 **文件名** 指定的文件中提供的均值和偏差的正态分布概率模型。

有关配置任务持续时间的更多信息，请参阅 Task Duration (SoC Blockset)。

#### 任务持续时间设置

### **添加** — 添加分布按钮

将分布添加到生成执行持续时间的正态分布集合中。

**注意**

单个任务最多只能分配五个分布。

### **删除** — 移除分布按钮

从正态分布集合中移除一个分布。

### **百分比** — 分布的可能性 `100` (默认) | positive scalar

指定每个正态分布的可能性。正态分布的 **百分比** 加权和决定任务持续时间的可能性。

**注意**

单个任务中所有分布的 **百分比** 之和必须等于 `100`。

### **均值** — 仿真中的任务平均持续时间 `1e-06` (默认) | positive scalar

指定任务仿真期间任务的平均持续时间。仿真任务持续时间使用具有指定 **均值** 和 **标准差** 参数值的正态分布，作为任务行为的一阶近似。

### **标准差** — 仿真中的任务持续时间标准差 `0` (默认) | positive scalar

指定任务仿真期间任务的标准差持续时间。仿真任务持续时间使用具有指定 **均值** 和 **标准差** 的正态分布，作为任务行为的一阶近似。

### **最小值** — 任务持续时间下限 `1e-06` (默认) | positive scalar

任务持续时间分布的下限。

### **最大值** — 任务持续时间上限 `1e-06` (默认) | positive scalar

任务持续时间分布的上限。

### **文件名** — 包含诊断调度数据的文件 filepath

此文件中的数据指定 **均值** 和 **标准差** 参数值。当选择 **播放记录的任务执行序列** 参数时，指定的 CSV 文件提供显式的任务执行计时。该 CSV 文件包含先前从硬件板记录的任务调度器诊断数据。

#### 依赖项

要启用此参数，请将 **通过以下方式指定任务持续时间** 参数设置为 `Recorded task execution statistics`。

## 所属库

SoC Blockset / Processor Task Execution C2000 Microcontroller Blockset / Scheduling Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Scheduling Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Scheduling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要自动为您的设计生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的更多信息，请参阅 Use SoC Builder to Generate SoC Design (SoC Blockset)。

Task Manager 模块中的任务在生成的代码中作为线程执行。Task Manager 模块中的任务参数指定线程的优先级和执行核心。

## 版本历史

**在 R2019a 中引入**

## 描述

在 Simulink 模型中创建和管理任务执行

Task Manager 模块模拟软件任务的执行，如同它们在 SoC 处理器上的预期行为。使用 Task Manager，您可以在模型中添加和移除任务，这些任务可以是定时器驱动或事件驱动的。任务可以在模型中表示为速率（对于定时器驱动任务）或函数调用子系统（对于事件驱动任务），并包含在单个 Model block 中。Task Manager 根据任务的参数（例如周期、持续时间、触发、优先级或处理器核心）以及该任务与正在运行模型中其他任务状态及其优先级的组合，执行各个任务。

在仿真中，此模块使用代码生成来提高仿真速度。这会在首次仿真时带来一些开销，但如果模块设置保持不变，后续仿真会更快。有关更多信息，请参阅 Interpreted Execution vs. Code Generation。

**注意**

Task Manager 模块不能在引用模型中使用。有关引用模型的更多信息，请参阅 Model block。

Task Manager 模块提供三种在仿真中指定任务持续时间的方法：

- 在模块掩码中定义的任务持续时间概率模型。
- 来自先前任务仿真记录的数据文件，或来自 SoC 设备上任务的数据文件。
- 模块上的输入端口，您可以将其连接到更动态的任务持续时间模型。
