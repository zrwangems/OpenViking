---
type: simulink-block
title: 'Contrast Adjustment'
family: 'analysis-enhancement'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'contrastadjustment'
documentation_source_path: 'ref/contrastadjustment.html'
language: zh-CN
chinese_source: worker-translation
---

# Contrast Adjustment

## 端口

### 输入

### **I** — 输入图像矩阵 | 数组

输入图像，指定为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是输入图像中的颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出图像矩阵 | 数组

输出图像，返回为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

## 参数

### 主要

### **Adjust pixel values from** — 输入像素值范围定义 `Full input data range [min max]`（默认） | `User-defined range` | `Range determined by saturating outlier pixels`

指定模块如何确定输入图像的像素值范围，选项如下：

- `Full input data range [min max]` — 范围设置为输入图像中的最小和最大像素值。
- `User-defined range` — 选择此值可启用 **Range [low high]** 参数。将 **Range [low high]** 参数指定为二元素非负值向量，其中第一个元素是输入像素值范围的下限，第二个元素是输入像素值范围的上限。
- `Range determined by saturating outlier pixels` — 通过饱和离群像素指定的范围。模块基于 **Percentage of pixels to saturate [low high]**、**Specify number of histogram bins (used to calculate the range when outliers are eliminated)** 和 **Number of histogram bins** 参数确定范围。有关详细信息，请参阅通过饱和离群像素确定对比度调整范围。

### **Range [low high]** — 输入像素值范围 `[0 255]`（默认） | 二元素非负值向量

将输入像素值范围指定为二元素非负值向量。该向量的第一个和第二个元素分别指定输入像素值范围的下限和上限。

#### 依赖项

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `User-defined`。

### **Percentage of pixels to saturate [low high]** — 要饱和的像素最大百分比 `[1 1]`（默认） | 二元素非负值向量

将要饱和的像素最大百分比指定为二元素非负值向量。每个元素必须在 0 到 100 范围内。模块计算输入像素值范围的下限，使得输入图像中值小于该下限的像素百分比至多为第一个元素的值。类似地，模块计算输入像素值范围的上限，使得输入图像中值大于该上限的像素百分比至多为第二个元素的值。

#### 依赖项

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `Range determined by saturating outlier pixels`。

### **Specify number of histogram bins (used to calculate the range when outliers are eliminated)** — 自定义直方图 bin 数 `on`（默认） | `off`

选择此参数可启用 **Number of histogram bins** 参数，从而可以指定模块在消除离群值后用于计算输入像素值范围的自定义直方图 bin 数。

#### 依赖项

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `Range determined by saturating outlier pixels`。

### **Number of histogram bins** — 直方图 bin 数 `256`（默认） | 正整数

指定用于计算缩放输入像素值的范围的直方图 bin 数。

#### 依赖项

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `Range determined by saturating outlier pixels`，并选择 **Specify number of histogram bins (used to calculate the range when outliers are eliminated)** 参数。

### **Adjust pixel values to** — 输出像素值范围定义 `Full data type range`（默认） | `User-defined range`

指定模块如何确定输出图像的像素值范围，选项如下：

- `Full data type range` — 将输出像素值范围指定为从输入数据类型的最小值到最大值。
- `User-defined range` — 选择此值可启用 **Range [low high]** 参数。将 **Range [low high]** 参数指定为二元素非负值向量，其中第一个元素是输出像素值范围的下限，第二个元素是输出像素值范围的上限。

### **Range [low high]** — 输出像素值范围 `[0 255]`（默认） | 二元素非负值向量

将输出像素值范围指定为二元素非负值向量。该向量的第一个和第二个元素分别指定输出像素值范围的下限和上限。

#### 依赖项

要启用此参数，请将 **Adjust pixel values to** 参数设置为 `User-defined range`。

### 数据类型

有关定点模块参数的详细信息，请参阅为模块指定定点属性 (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006b 中引入**

## 描述

使用线性缩放调整图像对比度

Contrast Adjustment 模块通过在指定的上限和下限之间线性缩放像素值来调整图像的对比度。高于或低于指定范围的像素值分别饱和到上限或下限值。有关详细信息，请参阅调整图像对比度。
