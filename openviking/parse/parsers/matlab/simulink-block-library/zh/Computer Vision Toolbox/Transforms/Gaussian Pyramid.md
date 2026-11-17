---
type: simulink-block
title: 'Gaussian Pyramid'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'gaussianpyramid'
documentation_source_path: 'ref/gaussianpyramid.html'
language: zh-CN
chinese_source: worker-translation
---

# Gaussian Pyramid

## 端口
```yaml
ports:
- name: I
  summary: 输入图像 标量 | 向量 | 矩阵 | 数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: 输出图像 标量 | 向量 | 矩阵 | 数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **I** — 输入图像 标量 | 向量 | 矩阵 | 数组

输入图像，指定为标量、*M*×*N* 矩阵或 *M*×*N*×*C* 数组。*C* 是输入图像中的颜色通道数。要将此输入指定为标量或向量，必须将 **Operation** 参数设置为 `Expand`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Port\_1** — 输出图像 标量 | 向量 | 矩阵 | 数组

输出图像，返回为标量、向量、矩阵或数组。输出图像的维度由 **Operation** 和 **Pyramid level** 参数值决定。要使此端口返回标量或向量，必须将 **Operation** 参数设置为 `Reduce`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Operation
  summary: 选择操作 Reduce（默认） | Expand
  group: ''
- name: Pyramid level
  summary: 图像缩放因子 1（默认） | 正整数
  group: ''
- name: Coefficient source
  summary: 低通滤波器系数来源 Default separable filter [1/4-a/2 1/4 a 1/4 1/4-a/2]（默认） | Specify via dialog
  group: ''
- name: Coefficients for separable filter
  summary: 可分离滤波器系数 [0.0625 0.25 0.375 0.25 0.0625]（默认） | 向量
  group: ''
- name: Hidden coefficients
  summary: 隐藏的可分离滤波器系数 [1/4-0.375/2 1/4 0.375 1/4 1/4-0.375/2]（默认） | 向量
  group: ''
```

### **Operation** — 选择操作 `Reduce`（默认） | `Expand`

将高斯金字塔操作选择为以下方法之一：

- `Reduce` — 该模块应用低通滤波器，然后对输入图像进行下采样。
- `Expand` — 该模块对输入图像进行上采样，然后应用低通滤波器。

### **Pyramid level** — 图像缩放因子 `1`（默认） | 正整数

指定对图像每个维度进行上采样或下采样的 2 的因子。

对于 *M*×*N* 输入图像，如果将 **Operation** 参数设置为 `Reduce`，并将 **Pyramid level** 设置为 `1`，则输出图像的维度为 `ceil(M/2)`×`ceil(N/2)`。

对于 *M*×*N* 输入图像，如果将 **Operation** 参数设置为 `Expand`，则输出图像的维度为 [(M-1)2l+1]×[(N-1)2l+1]，其中 **Pyramid level** 参数 *l* 必须为正整数。

### **Coefficient source** — 低通滤波器系数来源 `Default separable filter [1/4-a/2 1/4 a 1/4 1/4-a/2]`（默认） | `Specify via dialog`

将低通滤波器系数来源指定为 `Default separable filter [1/4-a/2 1/4 a 1/4 1/4-a/2]` 或 `Specify via dialog`。

### **Coefficients for separable filter** — 可分离滤波器系数 `[0.0625 0.25 0.375 0.25 0.0625]`（默认） | 向量

将可分离滤波器系数指定为向量。

### **Hidden coefficients** — 隐藏的可分离滤波器系数 `[1/4-0.375/2 1/4 0.375 1/4 1/4-0.375/2]`（默认） | 向量

将隐藏的可分离滤波器系数指定为向量。
## 所属库

Computer Vision Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

执行高斯金字塔分解

Gaussian Pyramid 模块计算高斯金字塔缩减或扩展以调整图像大小。图像缩减过程包括低通滤波，然后对图像像素进行下采样。图像扩展过程包括上采样，然后对图像像素进行低通滤波。您还可以使用此模块构建拉普拉斯金字塔。
