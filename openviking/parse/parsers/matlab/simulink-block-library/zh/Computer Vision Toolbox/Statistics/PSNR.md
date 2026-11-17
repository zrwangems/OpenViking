---
type: simulink-block
title: 'PSNR'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'psnr'
documentation_source_path: 'ref/psnr.html'
language: zh-CN
chinese_source: worker-translation
---

# PSNR

## 端口

### 输入

### **I1** — 输入图像 标量 | 向量 | 矩阵

输入图像，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **I2** — 输入图像 标量 | 向量 | 矩阵

输入图像，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Output** — 输出 标量

图像之间的峰值信噪比，以标量形式返回。

#### 依赖关系

如果输入为定点或整数数据类型，则模块输出为双精度浮点数。否则，模块输入和输出为相同的数据类型。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

仅针对 `double` 或 `single` 数据类型生成代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算图像之间的峰值信噪比 (PSNR)

PSNR 模块计算两幅图像之间的峰值信噪比，单位为分贝。该比值用作原始图像与压缩图像之间的质量度量。PSNR 越高，压缩或重建图像的质量越好。

均方误差 (MSE) 和峰值信噪比 (PSNR) 用于比较图像压缩质量。MSE 表示压缩图像与原始图像之间的累积平方误差，而 PSNR 表示峰值误差的度量。MSE 值越低，误差越低。

为计算 PSNR，该模块首先使用以下公式计算均方误差：

MSE=∑M,N[I1(m,n)−I2(m,n)]2M\*N

在上述公式中，*M* 和 *N* 分别是输入图像的行数和列数。然后该模块使用以下公式计算 PSNR：

PSNR=10log10(R2MSE)

在上述公式中，*R* 是输入图像数据类型中的最大波动值。例如，如果输入图像为双精度浮点数据类型，则 *R* 为 1。如果为 8 位无符号整数数据类型，则 *R* 为 255，依此类推。

### 计算彩色图像的 PSNR

计算彩色图像的 PSNR 存在不同的方法。由于人眼对亮度信息最为敏感，您可以通过将图像转换为分离强度（亮度）通道的颜色空间（如 YCbCr）来计算彩色图像的 PSNR。YCbCr 中的 Y（亮度）表示 R、G 和 B 的加权平均值。G 被赋予最大的权重，同样是因为人眼最容易感知它。仅在亮度通道上计算 PSNR。
