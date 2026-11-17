---
type: simulink-block
title: 'Optical Flow'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'opticalflow'
documentation_source_path: 'ref/opticalflow.html'
language: zh-CN
chinese_source: worker-translation
---

# Optical Flow

## 端口
```yaml
ports:
- name: I/I1
  summary: 图像或视频帧 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: I2
  summary: 图像 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: '|V|^2'
  summary: 速度幅值 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: V
  summary: 复数形式的速度分量 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **I/I1** — 图像或视频帧 标量 | 向量 | 矩阵

图像或视频帧，指定为标量、向量或矩阵。如果 **Compute optical flow between** 参数设置为 `Two images`，此端口的名称将变为 **I1**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I2** — 图像 标量 | 向量 | 矩阵

图像或视频帧，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **|V|^2** — 速度幅值 标量 | 向量 | 矩阵

速度幅值，以标量、向量或矩阵形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **V** — 复数形式的速度分量 标量 | 向量 | 矩阵

复数形式的速度分量，指定为标量、向量或矩阵。

#### 依赖

要启用此端口，请将 **Velocity output** 参数设置为 `Horizontal and vertical components in complex form`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Method
  summary: 光流计算方法 Horn-Schunck（默认）| Lucas-Kanade
  group: ''
- name: Compute optical flow between
  summary: 计算光流 Current frame and N-th frame back（默认）| Two images
  group: ''
- name: N
  summary: 帧数 1（默认）| 标量
  group: ''
- name: Smoothness factor
  summary: 平滑因子 1（默认）| 正标量
  group: ''
- name: Stop iterative solution
  summary: 停止迭代求解 When maximum number of iterations is reached（默认）| When velocity difference falls below threshold | Whichever
    comes first
  group: ''
- name: Maximum number of iterations
  summary: 最大迭代次数 10（默认）| 标量
  group: ''
- name: Velocity output
  summary: 光流输出 Magnitude-squared（默认）| Horizontal and vertical components in complex form
  group: ''
- name: Temporal gradient filter
  summary: 用于时间梯度的滤波器 Difference filter [-1 1]（默认）| Derivative of Gaussian
  group: ''
- name: Number of input frames to buffer
  summary: 用于平滑的输入帧缓冲数量 3（默认）| 标量
  group: ''
- name: Standard deviation for image smoothing filter
  summary: 图像平滑滤波器的标准差 1.5（默认）| 标量
  group: ''
- name: Standard deviation for gradient smoothing filter
  summary: 梯度平滑滤波器的标准差 1（默认）| 标量
  group: ''
- name: Discard normal flow estimates when constraint equation is ill-conditioned
  summary: 当约束方程病态时丢弃法向流估计 off（默认）| on
  group: ''
- name: Output image corresponding to motion vectors (accounts for block delay)
  summary: 输出与运动向量对应的图像 off（默认）| on
  group: ''
- name: Threshold for noise reduction
  summary: 降噪阈值 0.0039（默认）| 标量
  group: ''
```

**主选项卡**

### **Method** — 光流计算方法 `Horn-Schunck`（默认）| `Lucas-Kanade`

选择用于计算光流的方法。选项包括 `Horn-Schunck` 或 `Lucas-Kanade`。

### **Compute optical flow between** — 计算光流 `Current frame and N-th frame back`（默认）| `Two images`

选择如何计算光流。选择 `Two images` 以计算两幅图像之间的光流。选择 `Current frame and N-th frame back` 以计算相隔 N 帧的两个视频帧之间的光流。

#### 依赖

要启用此参数，请将：

- **Method** 参数设置为 `Horn-Schunck`
- **Method** 参数设置为 `Lucas-Kanade`，并将 **Temporal gradient filter** 设置为 `Difference filter [-1 1]`

### **N** — 帧数 `1`（默认）| 标量

输入一个标量值，表示参考帧与当前帧之间的帧数。

#### 依赖

要启用此参数，请将 **Compute optical flow between** 参数设置为 `Current frame and N-th frame back`。

### **Smoothness factor** — 平滑因子 `1`（默认）| 正标量

指定平滑因子。对于两幅图像或视频帧之间较大的相对运动，输入较大的正标量值。对于较小的相对运动，输入较小的正标量值。

#### 依赖

要启用此参数，请将 **Method** 参数设置为 `Horn-Schunck`。

### **Stop iterative solution** — 停止迭代求解 `When maximum number of iterations is reached`（默认）| `When velocity difference falls below threshold` | `Whichever comes first`

指定控制模块迭代求解过程何时停止的方法。如果希望当速度差低于某个阈值时停止该过程，请选择 `When velocity difference falls below threshold`。如果希望在一定迭代次数后停止该过程，请选择 `When maximum number of iterations is reached`。您也可以选择 `Whichever comes first`。

#### 依赖

要启用此参数，请将 **Method** 参数设置为 `Horn-Schunck`。

### **Maximum number of iterations** — 最大迭代次数 `10`（默认）| 标量

指定模块执行的最大迭代次数。

#### 依赖

要启用此参数，请将 **Method** 参数设置为 `Horn-Schunck`，并将 **Stop iterative solution** 参数设置为 `When maximum number of iterations is reached` 或 `Whichever comes first`。

### **Velocity output** — 光流输出 `Magnitude-squared`（默认）| `Horizontal and vertical components in complex form`

指定如何输出光流。如果选择 `Magnitude-squared`，模块将输出一个光流矩阵，其中每个元素的形式为 u2+v2。如果选择 `Horizontal and vertical components in complex form`，模块将输出光流矩阵，其中每个元素的形式为 u+jv。

### **Temporal gradient filter** — 用于时间梯度的滤波器 `Difference filter [-1 1]`（默认）| `Derivative of Gaussian`

指定模块是使用差分滤波器还是高斯导数滤波器来求解 *u* 和 *v*。

#### 依赖

要启用此参数，请将 **Method** 参数设置为 `Lucas-Kanade`。

### **Number of input frames to buffer** — 用于平滑的输入帧缓冲数量 `3`（默认）| 标量

指定用于平滑的输入帧缓冲数量。将此参数用于时间滤波器特性，例如标准差和滤波器系数数量。

#### 依赖

要启用此参数，请将 **Temporal gradient filter** 参数设置为 `Derivative of Gaussian`。

### **Standard deviation for image smoothing filter** — 图像平滑滤波器的标准差 `1.5`（默认）| 标量

指定图像平滑滤波器的标准差。

#### 依赖

要启用此参数，请将 **Temporal gradient filter** 参数设置为 `Derivative of Gaussian`。

### **Standard deviation for gradient smoothing filter** — 梯度平滑滤波器的标准差 `1`（默认）| 标量

指定梯度平滑滤波器的标准差。

#### 依赖

要启用此参数，请将 **Temporal gradient filter** 参数设置为 `Derivative of Gaussian`。

### **Discard normal flow estimates when constraint equation is ill-conditioned** — 当约束方程病态时丢弃法向流估计 off（默认）| on

选择此参数可在光流约束方程病态时将运动向量设置为零。

#### 依赖

要启用此参数，请将 **Temporal gradient filter** 参数设置为 `Derivative of Gaussian`。

### **Output image corresponding to motion vectors (accounts for block delay)** — 输出与运动向量对应的图像 off（默认）| on

选择此参数可输出与模块输出的运动向量对应的图像。

#### 依赖

要启用此参数，请将 **Temporal gradient filter** 参数设置为 `Derivative of Gaussian`。

### **Threshold for noise reduction** — 降噪阈值 `0.0039`（默认）| 标量

指定一个标量值，用于确定每幅图像或视频帧之间的运动阈值。数值越高，微小运动对光流计算的影响越小。

#### 依赖

要启用此参数，请将 **Method** 参数设置为 `Lucas-Kanade`。

**数据类型选项卡**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。
## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

估计对象速度

Optical Flow 模块使用 Horn-Schunck 或 Lucas-Kanade 方法估计两幅图像之间或一个视频帧到另一个帧之间对象运动的方向和速度。
