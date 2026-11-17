---
type: simulink-block
title: 'Corner Detection'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'cornerdetection'
documentation_source_path: 'ref/cornerdetection.html'
language: zh-CN
chinese_source: worker-translation
---

# Corner Detection

## 端口

### 输入

### **I** — 强度值输入图像矩阵

输入图像，指定为强度值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Loc** — 角点位置 *M*×2 矩阵

角点位置，以 [*x*
*y*] 坐标的 *M*×2 矩阵形式返回。*M* 表示角点的数量，且小于或等于 **Maximum number of
corners** 参数。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为以下之一：

- `Corner location`
- `Corner location and metric matrix`

**数据类型：** `uint32`

### **Count** — 检测到的角点数量 标量

检测到的角点数量，以标量形式返回。

#### 依赖关系

要启用此端口，请设置以下模块参数：

- **Output**：`Corner location` |
  `Corner location and metric matrix`
- **输出变量大小信号**：
  `off`

**数据类型：** `uint32`

### **Metric** — 角点度量值矩阵

角点度量值，以强度值矩阵形式返回。返回的矩阵与输入图像大小相同。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为以下之一：

- `Corner location and metric matrix`
- `Metric matrix`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主

### **Method** — 角点检测方法 `Harris corner detection (Harris & Stephens)`（默认）| `Minimum eigenvalue (Shi & Tomasi)` | `Local intensity comparison (Rosten & Drummond)`

将角点检测方法指定为 `Harris corner detection
(Harris & Stephens)`、`Minimum eigenvalue (Shi &
Tomasi)` 或 `Local intensity comparison (Rosten &
Drummond)`。

要获得最准确的结果，请使用 `Minimum eigenvalue (Shi &
Tomasi)`。要进行最快的计算，请使用 `Local intensity
comparison (Rosten & Drummond)`。要在准确性和计算速度之间取得平衡，请使用 `Harris corner detection (Harris &
Stephens)`。有关每种方法的详细信息，请参阅算法部分。

### **Sensitivity factor (0<k<0.25)** — 灵敏度因子 0.04（默认）| 标量

指定灵敏度因子 *k*。随着 *k*
减小，算法检测到尖锐角点的可能性增大。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为
`Harris corner detection (Harris & Stephens)`。

### **Coefficients for separable smoothing filter** — 滤波器系数 fspecial('gaussian', [1 5], 1.5)（默认）| 向量

指定平滑滤波器的滤波器系数向量。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为以下之一：

- `Harris corner detection (Harris &
  Stephens)`
- `Minimum eigenvalue (Shi & Tomasi)`

### **Intensity comparison threshold** — 强度阈值 0.1（默认）| 标量

指定用于查找有效周围像素的强度阈值。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为
`Local intensity comparison (Rosten &
Drummond)`。

### **Maximum angle to be considered a corner (in degrees)** — 最大角点角度 157.5（默认）| 标量

指定最大角点角度。

**可调：** 是

#### 依赖关系

- 要启用此参数，请将 **Method** 参数设置为
  `Local intensity comparison (Rosten &
  Drummond)`。
- 此参数仅可在仿真中调整。

### **Output** — 模块输出 `Corner location`（默认）| `Corner location and metric matrix` | `Metric matrix`

将模块输出指定为 `Corner location`、
`Corner location and metric matrix` 和
`Metric matrix`。

将此参数设置为 `Corner location` 或
`Corner location and metric matrix` 以显示
**最大角点数量**、**最小度量值，该值
indicates a corner** 和 **Neighborhood size (suppress region
around detected corners)** 参数。

### **Maximum number of corners** — 最大角点数量 200（默认）| 整数

指定希望模块查找的最大角点数量。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为以下之一：

- `Corner location`
- `Corner location and metric matrix`

### **Minimum metric value that indicates a corner** — 最小角点度量值 0.0005（默认）| 标量

指定最小角点度量值。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为以下之一：

- `Corner location`
- `Corner location and metric matrix`

### **Neighborhood size** — 邻域大小 [11 11]（默认）| 二元素向量

将邻域大小指定为正奇数的二元素向量
[*row*, *column*]。模块使用此参数
抑制具有最大角点度量值的有效角点周围的区域。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为以下之一：

- `Corner location`
- `Corner location and metric matrix`

### **Output variable size signal** — 可变大小信号 `on`（默认）| `off`

选择此参数以输出可变大小信号。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为以下之一：

- `Corner location`
- `Corner location and metric matrix`

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在此模块中指定的数据
类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 本地强度比较方法不支持此数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2007b 中引入**

## 描述

计算角点度量矩阵并查找图像中的角点

Corner Detection 模块使用 Harris
角点检测（由 Harris 和 Stephens 提出）、最小特征值（由 Shi 和 Tomasi 提出）或局部
强度比较（基于 Rosten 和 Drummond 提出的 *Accelerated Segment Test, (FAST)* 方法）方法查找图像中的角点。该模块基于具有最大角点度量值的像素
查找图像中的角点。
