---
type: simulink-block
title: 'Contrast Adjustment'
family: 'vision'
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
```yaml
ports:
- name: I
  summary: 输入图像矩阵 | 数组
  direction: input
  data_types: single | double | int8 | int16 | uint8 | uint16 | Boolean | fixed point
- name: Port_1
  summary: 输出图像矩阵 | 数组
  direction: output
  data_types: single | double | int8 | int16 | uint8 | uint16 | Boolean | fixed point
```

### 输入

### **I** — 输入图像矩阵 | 数组

输入图像，指定为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是输入图像中的颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出图像矩阵 | 数组

输出图像，返回为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Adjust pixel values from
  summary: 输入像素值范围定义 Full input data range [min max]（默认）| User-defined range | Range determined by saturating outlier pixels
  group: 主
- name: Range [low high]
  summary: 输入像素值范围 [0 255]（默认）| 非负数的二元素向量
  group: 主
- name: Percentage of pixels to saturate [low high]
  summary: 要饱和的像素最大百分比 [1 1]（默认）| 非负数的二元素向量
  group: 主
- name: Specify number of histogram bins (used to calculate the range when outliers are eliminated)
  summary: 自定义直方图箱数 on（默认）| off
  group: 主
- name: Number of histogram bins
  summary: 直方图箱数 256（默认）| 正整数
  group: 主
- name: Adjust pixel values to
  summary: 输出像素值范围定义 Full data type range（默认）| User-defined range
  group: 主
- name: Range [low high]
  summary: 输出像素值范围 [0 255]（默认）| 非负数的二元素向量
  group: 主
- name: Lock data type settings against change by the fixed-point tools
  summary: 数据类型覆盖 off（默认）| on
  group: 数据类型
```

### 主

### **Adjust pixel values from** — 输入像素值范围定义 `Full input data range [min max]`（默认）| `User-defined range` | `Range determined by saturating outlier pixels`

指定模块如何确定输入图像的像素值范围，选项如下：

- `Full input data range [min max]` — 范围设置为输入图像中的最小和最大像素值。
- `User-defined range` — 选择此值以启用 **Range [low high]** 参数。将 **Range [low high]** 参数指定为非负值的二元素向量，其中第一个元素是输入像素值范围的下限，第二个元素是输入像素值范围的上限。
- `Range determined by saturating outlier pixels` — 通过饱和离群像素指定的范围。模块根据 **Percentage of pixels to saturate [low high]**、**Specify number of histogram bins (used to calculate the range when outliers are eliminated)** 和 **Number of histogram bins** 参数确定范围。有关详细信息，请参阅 Determine Contrast Adjustment Range by Saturating Outlier Pixels。

### **Range [low high]** — 输入像素值范围 `[0 255]`（默认）| 非负数的二元素向量

将输入像素值范围指定为非负数的二元素向量。向量的第一个和第二个元素分别指定输入像素值范围的下限和上限。

#### 依赖关系

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `User-defined`。

### **Percentage of pixels to saturate [low high]** — 要饱和的像素最大百分比 `[1 1]`（默认）| 非负数的二元素向量

将要饱和的像素最大百分比指定为非负数的二元素向量。每个元素必须在 0 到 100 的范围内。模块计算输入像素值范围的下限，使得输入图像中值小于下限的像素百分比至多为第一个元素的值。类似地，模块计算输入像素值范围的上限，使得输入图像中值大于上限的像素百分比至多为第二个元素的值。

#### 依赖关系

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `Range determined by saturating outlier pixels`。

### **Specify number of histogram bins (used to calculate the range when outliers are eliminated)** — 自定义直方图箱数 `on`（默认）| `off`

选择此参数以启用 **Number of histogram bins** 参数，该参数允许您指定模块在消除离群值后用于计算输入像素值范围的自定义直方图箱数。

#### 依赖关系

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `Range determined by saturating outlier pixels`。

### **Number of histogram bins** — 直方图箱数 `256`（默认）| 正整数

指定用于计算缩放输入像素值范围的直方图箱数。

#### 依赖关系

要启用此参数，请将 **Adjust pixel values from** 参数设置为 `Range determined by saturating outlier pixels`，并选择 **Specify number of histogram bins (used to calculate the range when outliers are eliminated)** 参数。

### **Adjust pixel values to** — 输出像素值范围定义 `Full data type range`（默认）| `User-defined range`

指定模块如何确定输出图像的像素值范围，选项如下：

- `Full data type range` — 将输出像素值范围指定为从输入数据类型的最小值到最大值。
- `User-defined range` — 选择此值以启用 **Range [low high]** 参数。将 **Range [low high]** 参数指定为非负值的二元素向量，其中第一个元素是输出像素值范围的下限，第二个元素是输出像素值范围的上限。

### **Range [low high]** — 输出像素值范围 `[0 255]`（默认）| 非负数的二元素向量

将输出像素值范围指定为非负数的二元素向量。向量的第一个和第二个元素分别指定输出像素值范围的下限和上限。

#### 依赖关系

要启用此参数，请将 **Adjust pixel values to** 参数设置为 `User-defined range`。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。
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

**在 R2006b 中引入**

## 描述

使用线性缩放调整图像对比度

Contrast Adjustment 模块通过在指定的上限和下限之间线性缩放像素值来调整图像的对比度。高于或低于指定范围的像素值分别被饱和到上限或下限值。有关详细信息，请参阅 Adjust Contrast of Image。
