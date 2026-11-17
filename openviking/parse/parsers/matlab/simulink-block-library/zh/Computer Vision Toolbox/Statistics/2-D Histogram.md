---
type: simulink-block
title: '2-D Histogram'
family: 'statistics'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dhistogram'
documentation_source_path: 'ref/2dhistogram.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Histogram

## 端口

### 输入

### **Port\_1** — 输入图像 向量 | 矩阵 | 三维数组

输入图像，指定为向量、矩阵或三维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Rst** — 重置值 标量

输入序列的重置值，指定为标量。此值决定了导致模块重置运行直方图的事件。**Rst** 输入的采样时间必须为正整数，并且是输入采样时间的倍数。

#### 依赖关系

要启用此端口，请选择 **Running histogram** 参数，并将 **Trigger type** 参数设置为 `Rising edge`、`Falling edge`、`Either edge` 或 `Non-zero sample`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 直方图输出 向量 | 矩阵 | 三维数组

直方图输出，以向量、矩阵或三维数组形式返回。

如果 **Find the histogram over** 参数设置为 `Entire input`，则输出始终为向量。如果 **Find the histogram over** 参数设置为 `Each column`，则输出的维数与输入相同。

**数据类型：** `single` | `double` | `uint32`

## 参数

**主要**

### **Lower limit of histogram** — 最低值 bin 的下限 `0`（默认）| 实数值标量

为最低值 bin 的下边界 *Bm* 指定一个实数值标量。`NaN` 和 `inf` 不是 *Bm* 的有效值。

**可调：** Yes

### **Upper limit of histogram** — 最高值 bin 的上限 `1`（默认）| 实数值标量

为最高值 bin 的上边界 *Bm* 指定一个实数值标量。`NaN` 和 `inf` 不是 *BM* 的有效值。

**可调：** Yes

### **Number of bins** — 直方图中的 bin 数 `256`（默认）| 实数值标量

指定直方图中的 bin 数。

### **Find the histogram over** — 计算直方图所沿的维度 `Entire input`（默认）| `Each column`

指定模块计算直方图值时输入图像所沿的维度。对于 **Number of bins** 参数的任意给定值 *n*，此参数按如下方式影响模块的输出。

- `Entire input` — 模块在整个输入上计算直方图。它输出一个 *n* 元素列向量。
- `Each column` — 模块在输入的每一列上计算直方图。

  - 如果输入是 *M*×*N* 矩阵，模块输出 *n*×*N* 矩阵。输出矩阵的第 *j* 列包含 *M*×*N* 输入矩阵第 *j* 列中数据的直方图。
  - 如果输入是 *M*×*N*×*P* 数组，模块输出 *n*×*N*×*P* 数组。如果输入是三通道彩色图像，P 的值为 3，模块分别计算每个颜色通道的直方图。

### **Normalized** — 归一化直方图输出 `off`（默认）| `on`

选择 **Normalized** 参数以在 [0, 1] 范围内归一化输出直方图值。

**注意**

定点信号不支持使用此参数。

### **Running histogram** — 连续输入的频率分布 `off`（默认）| `on`

选择 **Running histogram** 参数以计算连续输入的过去和当前数据的频率分布。当模块在可选 **Rst** 端口检测到重置事件时，它会重置直方图（通过清空所有 bin）。输出大小会额外增加一个维度，该维度等于 ((*Tsim*/*Ts*)+1)，其中 *Tsim* 是仿真时间，*Ts* 是模块执行的采样时间。输出取决于 **Find the histogram over** 参数的值。

- `Entire input` — 模块对输入第一维中的数据计算运行直方图。模块输出 *n*×1×((*Tsim*/*Ts*)+1)，其中 *n* 是 **Number of bins** 参数的值。
- `Each column` — 模块对 *M*×*N* 矩阵的每一列计算运行直方图。模块输出 *n*×*N*×((*Tsim*/*Ts*)+1) 数组，其中 *n* 是 **Number of bins** 参数的值。

**注意**

当模块用于运行模式且输入数据类型为非浮点类型时，直方图的输出存储为 `uint32` 数据类型。此数据类型可以表示的最大数字是 `232–1`。如果超出 `uint32` 数据类型的范围，输出数据将回绕到 0。

### **Trigger type** — 运行直方图的重置条件 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

指定在可选 **Rst** 端口检测到时将重置运行直方图的事件。重置信号和输入数据信号必须具有相同的速率。

将重置事件指定为：

- `None` — 禁用 **Rst** 端口
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发重置事件：

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发重置事件：

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续
- `Either edge` — 当 **Rst** 输入是上升沿或下降沿时触发重置事件
- `Non-zero sample` — 在每个采样时间，当 **Rst** 输入不为零时触发重置事件

#### 依赖关系

要启用此参数，请选择 **Running histogram** 参数。

**数据类型**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（string.h）。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据输入生成直方图

2-D Histogram 模块计算输入图像中元素的频率。该模块针对整个输入或输入图像的每一列计算直方图值。它根据像素值将所有输入值归类到 bin 中。给定 bin 的直方图值表示该 bin 所包含的输入值的频率。该模块还能够跨输入序列计算运行直方图。该模块还能够跨输入序列计算运行直方图。
