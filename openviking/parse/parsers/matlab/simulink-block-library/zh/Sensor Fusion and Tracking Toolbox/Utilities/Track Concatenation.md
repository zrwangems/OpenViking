---
type: simulink-block
title: 'Track Concatenation'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'trackconcatenation'
documentation_source_path: 'ref/trackconcatenation.html'
language: zh-CN
chinese_source: worker-translation
---

# Track Concatenation

## 端口

### 输入

### **In1, In2, ..., InN** — 要合并的航迹，包含 MATLAB® 结构的 Simulink® 总线

要合并的航迹，其中每条航迹是包含 MATLAB 结构的 Simulink 总线。有关更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

您可以在跟踪器模块（例如 Global Nearest Neighbor Multi Object Tracker 模块）的 **Confirmed Tracks** 输出端口描述中找到航迹列表的定义。

默认情况下，该模块包含两个用于输入检测的端口。要添加更多端口，请使用 **Number of input sensors to combine** 参数。

### 输出

### **Out** — 合并后的航迹，包含 MATLAB 结构的 Simulink 总线

来自所有输入总线的合并航迹，以包含 MATLAB 结构的 Simulink 总线形式返回。请参阅 Create Nonvirtual Buses (Simulink)。您可以在跟踪器模块（例如 Global Nearest Neighbor Multi Object Tracker 模块）的 **Confirmed Tracks** 输出端口描述中找到航迹列表的定义。

## 参数

### **Number of input tracks to combine** — 输入航迹端口数量 `2`（默认）| 正整数

输入航迹端口数量，指定为正整数。输入端口标记为 **In1**、**In2**、…、**InN**，其中 *N* 是此参数设置的值。

**数据类型：** `double`

### **Source of output bus name** — 输出总线名称的来源 `Auto`（默认）| `Property`

输出总线名称的来源，指定为 `Auto` 或 `Property`。

- 如果选择 `Auto`，模块会自动生成总线名称。
- 如果选择 `Property`，请使用 **Specify an output bus name** 参数指定总线名称。

### **Specify an output bus name** — 输出总线名称 `BusTrackConcatenation`

为输出总线指定名称。

#### 依赖关系

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。

## 所属库

Sensor Fusion and Tracking Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2023a：Simulink 总线不再显示在工作区中

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

拼接航迹

Track Concatenation 模块将来自多个来源的航迹总线拼接为单个目标航迹列表。此模块的来源必须全部使用 `objectTrack` 格式，可以是传感器模块、跟踪器模块、Track-To-Track Fuser 模块或其他航迹拼接模块。使用此模块可以在将来自多个来源的航迹传入 Track-To-Track Fuser 模块之前对其进行拼接。
