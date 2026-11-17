---
type: simulink-block
title: 'Hough Lines'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'houghlines'
documentation_source_path: 'ref/houghlines.html'
language: zh-CN
chinese_source: worker-translation
---

# Hough Lines

## 端口

### 输入

### **Theta** — Theta 值 标量 | 向量

Theta 值，指定为标量或包含 *M* 个元素的向量。
*M* 是指定直线的数量。每个元素表示对应直线的
旋转角度，单位为 radians。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Rho** — Rho 值 标量 | 向量

Rho 值，指定为标量或包含 *M* 个元素的向量。
*M* 是指定直线的数量。每个元素表示对应直线在
**Theta** 的对应元素所指定的角度处，与图像左上角坐标原点之间的
距离。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Ref I** — 参考图像 矩阵

参考图像，指定为 *M*×*N*
矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **Pts** — 交点 矩阵

交点，以由坐标值组成的 *M*×4 矩阵形式返回，
其中 *M* 是输入直线的数量。

例如，假设一个 Hough Lines 模块的 theta 和 rho 输入均为
二元素向量，用于描述两条直线。

该模块输出一个 2×4 矩阵，其中每一行由两个
*xy* 坐标对组成，这些坐标对描述了对应直线与参考图像
边界线的交点。

`[x11 y11
x12 y12;`

`x21 y21
x22 y22]`

此图显示了由第一对 rho-theta 值描述的直线在 [`x11
y11 x12
y12`] 处与参考图像的边界相交，以及由第二对值
描述的直线在 [`x21
y21 x22
y22`] 处与边界相交。

**数据类型：** `int32`

## 参数

### **正弦值计算方法** — 正弦值计算方法 `Table lookup` (默认) | `Trigonometric function`

您可以指定以下选项之一。

- `Table lookup` — 在仿真开始之前，模块计算并存储确定直线交点所需的
  三角函数值。在这种情况下，模块需要额外的内存。
- `Trigonometric function` — 模块在仿真期间计算确定直线交点所需的正弦值和
  余弦值。

### **Theta 分辨率 (radians)** — Theta 分辨率 `pi/180` (默认) | 正标量

指定 theta 轴的间距。该值必须大于 0 且小于
`pi/2`。

#### 依存关系

要启用此参数，请将 **正弦值计算方法** 参数设置为 `Table lookup`。

## 所属库

Computer Vision Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `double` | `fixed pointb, c` | `integerd` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 此数据类型仅在输入端口 Ref1 上受支持。  b 当您将 FFT 实现参数设置为 FFTW，或者变换长度不是 2 的幂时，生成的代码将仅限于 MATLAB 主机计算机。  c 输入端口 Theta 和 Rho 支持字长小于或等于 32 的有符号定点数据类型，而 Ref1 支持有符号和无符号定点数据类型。  d 输出端口仅支持 32 位有符号整数。输入端口 Theta 和 Rho 支持有符号整数，而 Ref1 支持有符号和无符号整数。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

查找由 rho 和 theta 对描述的直线的笛卡尔坐标

Hough Lines 模块查找参考图像的边界线与由 rho-theta 对指定的直线之间的交点。该模块输出这些交点的笛卡尔坐标。边界线表示参考图像的左、右垂直边界以及上、下水平边界。

如果由 rho-theta 对指定的直线未与参考图像中的两条边界线相交，则该模块针对该直线输出值 [`0 0 0 0`]。此输出值使模型中的下一个模块能够忽略该直线的输出，因为 Hough Lines 模块通常位于一个在每个输出交点处绘制点或形状的模块之前。
