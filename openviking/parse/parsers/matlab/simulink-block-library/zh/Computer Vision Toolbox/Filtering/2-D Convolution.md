---
type: simulink-block
title: '2-D Convolution'
family: 'filtering'
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

输入矩阵的卷积，返回为矩阵。

#### 依赖项

- 输出的维度由 **Output size** 参数决定。
- 如果输入的数据类型为 floating point，则模块的输出也为 floating point。
- 如果 `all(size(I1)<size(I2))`，则模块返回错误。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

**主选项卡**

### **Output size** — 输出大小 matrix

输出的维度。

下表描述在给定以下输入维度时模块的输出：

- **I1** — (*Ma*,
  *Na*)
- **I2** — (*Mb*, *Nb*)

| **Output size** | 输出 | 输出维度 |
| --- | --- | --- |
| `Full` | 完整的二维卷积 | (*Ma*+*Mb*-1, *Na*+*Nb*-1). |
| `Same as input port I1` | 与端口 **I1** 处输入具有相同维度的卷积中心部分 |  |
| `Valid` | 仅在没有任何输入的零填充边缘的情况下计算的卷积部分。 | (*Ma*-*Mb*+1, *Na*-*Nb*+1) |

### **Normalized output** — 归一化输出矩阵

通过将输出除以 `sqrt(sum(dot(I1p,I1p))*sum(dot(I2,I2)))` 来归一化输出，其中 `I1p` 是 **I1** 矩阵中与 **I2** 矩阵对齐的部分。

**注意**

当您选中 **Normalized output** 复选框时，模块输入不能为 fixed point。

**Data Types 选项卡**

有关 fixed-point 模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真 fixed-point 系统。

当您选中 **Normalized output** 复选框时，模块输入不能为 fixed point。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算两个输入矩阵的二维离散卷积

2-D Convolution 模块计算两个输入矩阵的二维卷积。假设矩阵 A 具有维度 (*Ma*, *Na*)，矩阵 B 具有维度 (*Mb*, *Nb*)。当模块计算完整输出大小时，二维离散卷积的方程为：

C(i,j)=∑m=0(Ma−1)∑n=0(Na−1)A(m,n)\*B(i−m,j−n)

其中 0≤i<Ma+Mb−1 且 0≤j<Na+Nb−1。
