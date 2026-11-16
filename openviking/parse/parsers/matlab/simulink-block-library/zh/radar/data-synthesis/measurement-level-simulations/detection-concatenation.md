---
type: simulink-block
title: 'Detection Concatenation'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Data Synthesis / Measurement-Level Simulations'
documentation_page: 'detectionconcatenation'
documentation_source_path: 'ref/detectionconcatenation.html'
language: zh-CN
chinese_source: worker-translation
---

# Detection Concatenation

## 端口

### 输入

### **In1, In2, ..., InN** — 要组合的传感器检测，为包含 MATLAB® 结构的 Simulink® 总线

要组合的传感器检测，其中每个检测是包含 MATLAB 结构的 Simulink 总线。有关更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

该结构具有以下形式：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | integer |
| `Detections` | 目标检测 | 目标检测结构体数组。这些检测中的前 `NumDetections` 个是实际检测。 |

`Detections` 的字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 测量时间 | `single` 或 `double` |
| `Measurement` | 目标测量值 | `single` 或 `double` |
| `MeasurementNoise` | 测量噪声协方差矩阵 | `single` 或 `double` |
| `SensorIndex` | 传感器的唯一 ID | `single` 或 `double` |
| `ObjectClassID` | 目标分类 ID | `single` 或 `double` |
| `MeasurementParameters` | 跟踪滤波器初始化函数使用的参数 | Simulink Bus |
| `ObjectAttributes` | 传递给跟踪器的附加信息 | Simulink Bus |

默认情况下，该模块包含两个用于输入检测的端口。要添加更多端口，请使用 **Number of input sensors to combine** 参数。

### 输出

### **Out** — 组合后的传感器检测，为包含 MATLAB 结构的 Simulink 总线

来自所有输入总线的组合传感器检测，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

该结构具有以下形式：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | integer |
| `Detections` | 目标检测 | 目标检测结构体数组。这些检测中的前 `NumDetections` 个是实际检测。 |

`Detections` 的字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 测量时间 | `single` 或 `double` |
| `Measurement` | 目标测量值 | `single` 或 `double` |
| `MeasurementNoise` | 测量噪声协方差矩阵 | `single` 或 `double` |
| `SensorIndex` | 传感器的唯一 ID | `single` 或 `double` |
| `ObjectClassID` | 目标分类 ID | `single` 或 `double` |
| `MeasurementParameters` | 跟踪滤波器初始化函数使用的参数 | Simulink Bus |
| `ObjectAttributes` | 传递给跟踪器的附加信息 | Simulink Bus |

**Maximum number of reported detections** 输出是所有输入端口的 **Maximum number of reported detections** 之和。实际检测数量是每个输入端口中实际检测数量之和。检测结构体中的 `ObjectAttributes` 字段是每个输入端口中 `ObjectAttributes` 字段的并集。

## 参数

### **Number of input sensors to combine** — 输入传感器端口数 2（默认）| 正整数

输入传感器端口数，指定为正整数。每个输入端口标记为 **In1**、**In2**、…、**InN**，其中 *N* 是此参数设置的值。

**数据类型：** `double`

### **Source of output bus name** — 输出总线名称来源 `Auto`（默认）| `Property`

输出总线名称来源，指定为 `Auto` 或 `Property`。

- 如果选择 `Auto`，该模块会自动生成总线名称。
- 如果选择 `Property`，请使用 **Specify an output bus name** 参数指定总线名称。

### **Specify an output bus name** — 输出总线名称 无默认值

#### 依赖关系

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox Sensor Fusion and Tracking Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

### R2023a: Simulink 总线不在工作区中显示

自 R2023a 起，此模块创建的 Simulink 总线不再在 MATLAB 工作区中显示。

## 描述

组合来自不同传感器的检测报告

Detection Concatenation 模块将来自多个传感器的检测报告组合到单个输出总线上。当来自多个传感器模块的检测被传递到跟踪器模块（例如该模块）时，拼接非常有用。您可以通过更改 **Number of input sensors to combine** 参数来增加输入端口数量，从而容纳更多传感器。
