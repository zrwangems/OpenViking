---
type: simulink-block
title: 'Scenario To Platform'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Tracking Scenario and Sensor Models'
documentation_page: 'scenariotoplatform'
documentation_source_path: 'ref/scenariotoplatform.html'
language: zh-CN
chinese_source: worker-translation
---

# Scenario To Platform

## 端口

### 输入

### **Platforms (Scenario Frame)** — 场景坐标系中的平台位姿 包含 MATLAB® 结构的 Simulink® 总线

以场景坐标系表示的平台位姿，指定为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅
Create Nonvirtual Buses (Simulink)。该结构具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `NumPlatforms` | 平台数量，指定为非负整数。 |
| `Platforms` | 场景坐标系中的平台位姿，指定为平台位姿结构体数组。该模块仅读取 `NumPlatforms` 中指定的平台数量对应的平台位姿。 |

每个平台位姿结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `PlatformID` | 平台的唯一标识符，指定为正整数。 |
| `ClassID` | 用于对目标类型进行分类的用户定义整数，指定为非负整数。`0` 保留用于未分类的平台类型，为默认值。 |
| `Position` | 平台在场景坐标系中的位置，指定为实数值 1×3 向量。单位为米。 |
| `Velocity` | 平台在场景坐标系中的速度，指定为实数值 1×3 向量。单位为米每秒。 |
| `Acceleration` | 平台在场景坐标系中的加速度，指定为实数值 1×3 向量。单位为米每二次方秒。 |
| `Orientation` | 平台相对于场景坐标系的姿态，指定为 3×3 旋转矩阵。姿态定义了从场景坐标系到平台体坐标系的坐标系旋转。 |
| `AngularVelocity` | 平台在场景坐标系中的角速度，指定为实数值 1×3 向量。向量的大小定义了角速率。单位为度每秒。 |

除了直接指定目标平台位姿外，您还可以使用 Tracking Scenario
Reader 模块生成以场景坐标系表示的平台位姿。

### **Reference Platform Pose (Scenario Frame)** — 场景坐标系中的参考平台位姿 包含 MATLAB 结构的 Simulink 总线

以场景坐标系表示的参考平台位姿，指定为
包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅
Create Nonvirtual Buses (Simulink)。该结构具有以下字段：

| 字段 | 描述 |
| --- | --- |
| `PlatformID` | 平台的唯一标识符，指定为正整数。指定的 `PlatformID` 必须与 **Reference platform index** 参数中指定的值完全相同。 |
| `ClassID` | 用于对目标类型进行分类的用户定义整数，指定为非负整数。`0` 保留用于未分类的平台类型，为默认值。 |
| `Position` | 平台在场景坐标系中的位置，指定为实数值 1×3 向量。单位为米。这是必填字段，没有默认值。 |
| `Velocity` | 平台在场景坐标系中的速度，指定为实数值 1×3 向量。单位为米每秒。这是必填字段，没有默认值。 |
| `Acceleration` | 平台在场景坐标系中的加速度，指定为 1×3 向量。单位为米每二次方秒。这是必填字段，没有默认值。 |
| `Orientation` | 平台相对于场景坐标系的姿态，指定为 3×3 旋转矩阵。姿态定义了从场景坐标系到平台体坐标系的坐标系旋转。这是必填字段，没有默认值。 |
| `AngularVelocity` | 平台在场景坐标系中的角速度，指定为实数值 1×3 向量。向量的大小定义了角速率。单位为度每秒。这是必填字段，没有默认值。 |

#### 依赖项

要启用此端口，请选中 **Enable reference platform pose input** 复选框。

### 输出

### **Platforms (Platform Body Frame)** — 参考平台本体坐标系下的目标平台位姿 Simulink 总线，包含 MATLAB 结构体

以参考平台本体坐标系表示的目标平台位姿，指定为包含 MATLAB 结构体的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。参考平台是在 **Reference platform index** 参数中指定了 `PlatformID` 的平台。该结构体具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `NumPlatforms` | 平台数量，指定为非负整数。 |
| `Platforms` | 平台位姿，指定为平台位姿结构体数组。该模块仅读取 `NumPlatforms` 中指定的平台数量所对应的平台位姿。 |

每个平台位姿结构体包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `PlatformID` | 目标平台的唯一标识符，返回为正整数。 |
| `ClassID` | 用于对目标平台类型进行分类的用户定义整数，返回为非负整数。`0` 保留用于未分类的平台类型。 |
| `Position` | 目标平台在参考平台本体坐标系中的位置，返回为实值 1×3 向量。单位为米。 |
| `Velocity` | 目标平台在参考平台本体坐标系中的速度，返回为实值 1×3 向量。单位为米每秒。默认值为 `[0 0 0]`。 |
| `Acceleration` | 目标平台在参考平台本体坐标系中的加速度，返回为实值 1×3 向量。单位为米每二次方秒。默认值为 `[0 0 0]`。 |
| `Orientation` | 目标平台相对于参考平台本体坐标系的姿态，返回为 3×3 旋转矩阵。姿态定义了从参考平台本体坐标系到目标平台本体坐标系的坐标系旋转。 |
| `AngularVelocity` | 目标平台在参考平台本体坐标系中的角速度，指定为实值 1×3 向量。向量的大小定义了角速率。单位为度每秒。 |

您可以将此输出用作 Fusion Radar Sensor 模块的输入。

## 参数

### **Reference platform index** — 参考平台索引 `0`（默认）| 正整数

参考平台索引，指定为正整数。您必须通过 **Platforms (Scenario Frame)** 输入端口或 **Reference Platform Pose (Scenario Frame)** 输入端口指定与此索引对应的平台位姿。

**示例：** `1`

### **Enable reference platform pose input** — 启用参考平台位姿输入 `off`（默认）| `on`

选中此复选框以启用 **Reference Platform Pose (Scenario Frame)** 输入端口。

### **Source of output bus name** — 输出总线名称的来源 `Auto`（默认）| `Property`

输出总线名称的来源，指定为以下选项之一：

- `Auto` — 该模块自动创建总线名称。
- `Property` — 使用 **Specify an output bus name** 参数指定总线名称。

### **Specify an output bus name** — 输出端口总线名称 `BusPlatforms`（默认）| 有效总线名称

输出端口总线名称，指定为有效的总线名称。

#### 依赖项

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将复用该 C 代码。此选项需要额外的启动时间。

## 所属库

Sensor Fusion and Tracking Toolbox / Tracking Scenario and Sensor Models

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2023a：Simulink 总线不显示在工作区中

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

将平台位姿从场景坐标系变换到平台体坐标系

Scenario To Platform 模块将以场景坐标系表示的平台位姿变换为以平台体坐标系表示的平台位姿。
