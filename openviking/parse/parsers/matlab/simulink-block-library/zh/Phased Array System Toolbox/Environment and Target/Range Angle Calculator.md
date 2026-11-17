---
type: simulink-block
title: 'Range Angle Calculator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'rangeanglecalculator'
documentation_source_path: 'ref/rangeanglecalculator.html'
language: zh-CN
chinese_source: worker-translation
---

# Range Angle Calculator

## 端口

### 输入

### **Pos** — 源点位置 实值 3×1 向量 | 实值 3×*N* 矩阵

源点位置，指定为实值 3×1 向量或实值 3×*N* 矩阵，其中 *N* 是源点数量。每一列包含一个点的笛卡尔坐标，形式为 `[x;y;z]`。

当 `Pos` 是 3×*N* 矩阵时，您必须将 `RefPos` 指定为 *N* 个参考位置的 3×*N* 矩阵。如果所有参考点相同，您可以用单个 3×1 向量指定 `RefPos`。单位是米。

**示例：** [1000;2000;50]

**数据类型：** `double`

### **RefPos** — 参考点位置 `[0;0;0]`（默认）| 实值 3×1 向量 | 实值 3×*N* 矩阵

参考点位置，指定为实值 3×1 向量或实值 3×*N* 矩阵，其中 *N* 是参考点数量。每一列包含一个点的笛卡尔坐标，形式为 `[x;y;z]`。

当 `RefPos` 是 3×*N* 矩阵时，您必须将 `Pos` 指定为 *N* 个源位置的 3×*N* 矩阵。如果所有源点相同，您可以用单个 3×1 向量指定 `Pos`。参考位置单位是米。

**示例：** [100;100;10]

#### 依赖

要启用此端口，请将 **Reference position source** 下拉菜单设置为 `Input port`。

**数据类型：** `double`

### **RefAxes** — 局部坐标系轴 `[1 0 0;0 1 0;0 0 1]`（默认）| 实值 3×3 向量 | 实值 3×3×*N* 数组

局部坐标系轴，指定为实值 3×3 矩阵或 3×3×*N* 数组。对于数组，每一页对应每个参考点处的局部坐标轴。`RefAxes` 中的列指定局部坐标系坐标轴在笛卡尔坐标中的方向。当这些维度大于一时，*N* 必须与 `Pos` 或 `RefPos` 的列数匹配。

**示例：** [100;100;10]

#### 依赖

要启用此端口，请将 **Reference axes source** 下拉菜单设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Ang** — 方位角和仰角 实值 2×*N* 矩阵 | 实值 2×2*N* 矩阵

方位角和仰角，以度为单位，返回为 2×*N* 矩阵或 2×2*N* 矩阵。每一列表示一个方向角，形式为 [azimuth;elevation]。

当 **Propagation model** 设置为 **Free space** 时，`Ang` 是 2×*N* 矩阵，表示从源点到参考点的路径角度。

当 **Propagation model** 设置为 **Two-ray** 时，`Ang` 是 2×2*N* 矩阵。`Ang` 的交替列分别指视线路径和反射路径。

#### 依赖

要启用此端口，请将 **Output(s)** 下拉菜单设置为 `Angle` 或 `Range and Angle`。

**数据类型：** `double`

### **Range** — 传播距离 实值 1×*N* 向量 | 实值 1×2*N* 向量

传播距离，返回为实值 1×*N* 向量或实值 1×2*N* 向量。

当 **Propagation model** 设置为 **Free space** 时，**Range** 的大小为 1×*N*。传播距离是从 `Pos` 中定义的位置到 `RefPos` 中定义的对应参考位置的直接路径长度。

当 **Propagation model** 设置为 **Two-ray** 时，**Range** 包含直接路径和反射路径的距离。**Range** 的交替列分别指同一源-参考点对的视线路径和反射路径。

#### 依赖

要启用此端口，请将 **Output(s)** 下拉菜单设置为 `Range` 或 `Range and Angle`。

**数据类型：** `double`

## 参数

### **Propagation model** — 传播模型 `Free space`（默认）| `Two-ray`

通过将此参数设置为 `Free space` 或 `Two-ray` 来指定传播模型。

### **Reference position source** — 参考位置源 `Property`（默认）| `Input port`

通过将此参数设置为 `Property` 或 `Input port` 来指定参考位置源。如果 **Reference position source** 设置为 `Property`，则使用 **Reference position** 参数设置位置。如果 **Reference position source** 设置为 `Input port`，则使用标记为 `RefPos` 的输入端口。

### **Reference position** — 参考位置 `[0;0;0]`（默认）

以 `[x;y;z]` 形式的 3×1 直角坐标向量指定参考位置，单位为米。参考位置用作局部坐标系的原点。输入位置的距离和角度均相对于参考位置测量。此参数仅在 **Reference position source** 设置为 `Property` 时显示。

### **Reference axes source** — 参考坐标轴源 `Property`（默认）| `Input port`

通过将此参数设置为 `Property` 或 `Input port` 来指定参考坐标轴源。如果 **Reference axes source** 设置为 `Property`，则使用 **Reference axes** 参数设置坐标轴。如果 **Reference axes source** 设置为 `Input port`，则使用标记为 `RefAxes` 的输入端口。

### **Reference axes** — 参考坐标轴 `eye(3)`

以 3×3 正交矩阵的形式指定用于计算距离和角度的局部坐标系参考坐标轴。矩阵的每一列以 `[x; y; z]` 的形式指定局部坐标系中某一坐标轴的方向，原点位于参考位置。此参数仅在 **Reference axes source** 设置为 `Property` 时显示。

### **Output(s)** — 输出 `Angle`（默认）| `Range` | `Range and Angle`

指定模块的所需输出。每种输出类型根据参数值发送到不同的端口。

| 值 | 端口 |
| --- | --- |
| `Angle` | `Ang` |
| `Range` | `Range` |
| `Range and Angle` | `Ang` 和 `Range` |

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 | |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

距离和角度计算

Range Angle Calculator 模块计算若干位置相对于参考位置以及相对于参考坐标轴方向的距离和/或方位角和俯仰角。参考位置和参考坐标轴可以在模块对话框中指定，也可以通过输入端口传入。
