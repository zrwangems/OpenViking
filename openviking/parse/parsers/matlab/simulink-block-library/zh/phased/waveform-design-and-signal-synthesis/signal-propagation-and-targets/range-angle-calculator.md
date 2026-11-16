---
type: simulink-block
title: 'Range Angle Calculator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveform Design and Signal Synthesis / Signal Propagation and Targets'
documentation_page: 'rangeanglecalculator'
documentation_source_path: 'ref/rangeanglecalculator.html'
language: zh-CN
chinese_source: worker-translation
---

# Range Angle Calculator

## 端口

### 输入

### **Pos** — 源点位置，实值 3×1 向量 | 实值 3×*N* 矩阵

源点位置，指定为实值 3×1 向量或实值 3×*N* 矩阵，其中 *N* 是源点数量。每列包含一个点的笛卡尔坐标，形式为 `[x;y;z]`。

当 `Pos` 是 3×*N* 矩阵时，必须将 `RefPos` 指定为用于 *N* 个参考位置的 3×*N* 矩阵。如果所有参考点都相同，可以用单个 3×1 向量指定 `RefPos`。单位是 meters。

**示例：** [1000;2000;50]

**数据类型：** `double`

### **RefPos** — 参考点位置 `[0;0;0]`（默认）| 实值 3×1 向量 | 实值 3×*N* 矩阵

参考点位置，指定为实值 3×1 向量或实值 3×*N* 矩阵，其中 *N* 是参考点数量。每列包含一个点的笛卡尔坐标，形式为 `[x;y;z]`。

当 `RefPos` 是 3×*N* 矩阵时，必须将 `Pos` 指定为用于 *N* 个源位置的 3×*N* 矩阵。如果所有源点都相同，可以用单个 3×1 向量指定 `Pos`。参考位置单位是 meters。

**示例：** [100;100;10]

#### 依赖关系

要启用此端口，请将 **参考位置源** 下拉菜单设置为 `Input port`。

**数据类型：** `double`

### **RefAxes** — 局部坐标系坐标轴 `[1 0 0;0 1 0;0 0 1]`（默认）| 实值 3×3 向量 | 实值 3×3×*N* 数组

局部坐标系坐标轴，指定为实值 3×3 矩阵或 3×3×*N* 数组。对于数组，每个页对应于每个参考点处的局部坐标轴。`RefAxes` 中的列指定局部坐标系中各坐标轴在笛卡尔坐标中的方向。当这些维度大于 1 时，*N* 必须与 `Pos` 或 `RefPos` 的列数匹配。

**示例：** [100;100;10]

#### 依赖关系

要启用此端口，请将 **参考坐标轴源** 下拉菜单设置为 `Input port`。

**数据类型：** `double`

### 输出

### **Ang** — 方位角和俯仰角，实值 2×*N* 矩阵 | 实值 2×2*N* 矩阵

方位角和俯仰角，以 degrees 为单位，返回为 2×*N* 矩阵或 2×2*N* 矩阵。每列表示一个方向角，形式为 [azimuth;elevation]。

当 **传播模型** 设置为 **Free space** 时，`Ang` 是 2×*N* 矩阵，表示从源点到参考点的路径角度。

当 **传播模型** 设置为 **Two-ray** 时，`Ang` 是 2×2*N* 矩阵。`Ang` 的交替列分别对应视距路径和反射路径。

#### 依赖关系

要启用此端口，请将 **输出** 下拉菜单设置为 `Angle` 或 `Range and Angle`。

**数据类型：** `double`

### **Range** — 传播距离，实值 1×*N* 向量 | 实值 1×2*N* 向量

传播距离，返回为实值 1×*N* 向量或实值 1×2*N* 向量。

当 **传播模型** 设置为 **Free space** 时，**Range** 的大小为 1×*N*。传播距离是从 `Pos` 中定义的位置到 `RefPos` 中定义的对应参考位置的直接路径长度。

当 **传播模型** 设置为 **Two-ray** 时，**Range** 包含直接路径和反射路径的距离。**Range** 的交替列分别对应同一源点-参考点对的视距路径和反射路径。

#### 依赖关系

要启用此端口，请将 **输出** 下拉菜单设置为 `Range` 或 `Range and Angle`。

**数据类型：** `double`

## 参数

### **传播模型** — 传播模型 `Free space`（默认）| `Two-ray`

通过将此参数设置为 `Free space` 或 `Two-ray` 来指定传播模型。

### **参考位置源** — 参考位置源 `Property`（默认）| `Input port`

通过将此参数设置为 `Property` 或 `Input port` 来指定参考位置源。如果 **参考位置源** 设置为 `Property`，则使用 **参考位置** 参数设置位置。如果 **参考位置源** 设置为 `Input port`，则使用标记为 `RefPos` 的输入端口。

### **参考位置** — 参考位置 `[0;0;0]`（默认）

将参考位置指定为以 meters 为单位的直角坐标 3×1 向量，形式为 `[x;y;z]`。参考位置用作局部坐标系的原点。输入位置的距离和角度相对于参考位置测量。仅当 **参考位置源** 设置为 `Property` 时，此参数才出现。

### **参考坐标轴源** — 参考坐标轴源 `Property`（默认）| `Input port`

通过将此参数设置为 `Property` 或 `Input port` 来指定参考坐标轴源。如果 **参考坐标轴源** 设置为 `Property`，则使用 **参考坐标轴** 参数设置坐标轴。如果 **参考坐标轴源** 设置为 `Input port`，则使用标记为 `RefAxes` 的输入端口。

### **参考坐标轴** — 参考坐标轴 `eye(3)`

以 3×3 标准正交矩阵的形式指定用于计算距离和角度的局部坐标系的参考坐标轴。矩阵的每列以 `[x; y; z]` 的形式指定局部坐标系中一个轴的方向，原点位于参考位置。仅当 **参考坐标轴源** 设置为 `Property` 时，此参数才出现。

### **输出** — 输出 `Angle`（默认）| `Range` | `Range and Angle`

指定模块所需的输出。根据参数值，每种类型的输出会发送到不同的端口。

| 值 | 端口 |
| --- | --- |
| `Angle` | `Ang` |
| `Range` | `Range` |
| `Range and Angle` | `Ang` 和 `Range` |

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

距离和角度计算

Range Angle Calculator 模块计算多个位置相对于参考位置以及相对于参考坐标轴方向的距离和/或方位角与俯仰角。参考位置和参考坐标轴可以在模块对话框中指定，也可以通过输入端口传入。
