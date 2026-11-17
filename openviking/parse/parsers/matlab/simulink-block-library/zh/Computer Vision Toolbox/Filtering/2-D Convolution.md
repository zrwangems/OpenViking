---
type: simulink-block
title: '2-D Convolution'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: '2dconvolution'
documentation_source_path: 'ref/2dconvolution.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Convolution

## 端口

### 输入

### **I1** — 输入矩阵 matrix

输入矩阵，指定为强度值矩阵或表示 RGB 视频流一个平面的矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I2** — 输入矩阵 matrix

输入矩阵，指定为强度值矩阵或表示 RGB 视频流一个平面的矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Output** — 卷积矩阵

输入矩阵的卷积，以矩阵形式返回。

#### 依赖关系

- 输出的维度由 **Output size** 参数决定。
- 如果输入的数据类型为浮点型，则模块的输出也为浮点型。
- 如果 `all(size(I1)<size(I2))`，模块将返回错误。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

**主选项卡**

### **Output size** — 输出大小 matrix

输出的维度。

下表描述了在给定以下输入维度时模块的输出：

- **I1** — (*Ma*,
  *Na*)
- **I2** — (*Mb*, *Nb*)

| **Output size** | 输出 | 输出维度 |
| --- | --- | --- |
| `Full` | 完整的二维卷积 | (*Ma*+*Mb*-1, *Na*+*Nb*-1)。 |
| `Same as input port I1` | 卷积的中心部分，其维度与端口 **I1** 处的输入相同 |  |
| `Valid` | 仅计算不包含任何输入零填充边缘的卷积部分。 | (*Ma*-*Mb*+1, *Na*-*Nb*+1) |

### **Normalized output** — 归一化输出 matrix

通过将输出除以
`sqrt(sum(dot(I1p,I1p))*sum(dot(I2,I2)))` 来归一化输出，其中
`I1p` 是与 **I2** 矩阵对齐的 **I1** 矩阵部分。

**注意**

当您选中 **Normalized output** 复选框时，模块输入不能为定点型。

**数据类型选项卡**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

## 所属库

Computer Vision Toolbox / Filtering

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

当您选中 **Normalized output** 复选框时，模块输入不能为定点型。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算两个输入矩阵的二维离散卷积

2-D Convolution 模块计算两个输入矩阵的二维卷积。
假设矩阵 A 的维度为 (*Ma*, *Na*)，矩阵
B 的维度为 (*Mb*, *Nb*)。当模块计算完整输出大小时，二维离散卷积的方程为：

C(i,j)=∑m=0(Ma−1)∑n=0(Na−1)A(m,n)\*B(i−m,j−n)

其中 0≤i<Ma+Mb−1 且 0≤j<Na+Nb−1。
