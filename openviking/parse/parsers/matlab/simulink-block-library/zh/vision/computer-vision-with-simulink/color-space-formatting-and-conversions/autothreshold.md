---
type: simulink-block
title: 'Autothreshold'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Color Space Formatting and Conversions'
documentation_page: 'autothreshold'
documentation_source_path: 'ref/autothreshold.html'
language: zh-CN
chinese_source: worker-translation
---

# Autothreshold

## 端口

### 输入

### **I** — 输入图像矩阵

输入图像，指定为 *M*×*N* 矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **BW** — 输出二值图像矩阵

输出二值图像，返回为 *M*×*N* 矩阵。

**数据类型:** `Boolean`

### **Th** — 阈值标量

用于将强度图像转换为二值图像的阈值，返回为标量。

该模块使用 Otsu 方法计算阈值。该模块通过拆分输入图像的直方图来计算此值，使得每个像素组的方差最小化。

#### 依赖关系

要启用此端口，请选择 **Output threshold** 参数。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **EMetric** — 有效性度量值标量

有效性度量值，返回为范围 [0, 1] 中的标量。

如果输入图像的所有像素值都相同，则有效性度量值为 `0`。如果图像有两个唯一像素，或者如果图像的直方图是对称的，则有效性度量值为 `1`。

#### 依赖关系

要启用此端口，请选择 **Output effectiveness metric** 参数。

**数据类型:** `single` | `double`

## 参数

**主要**

**数据类型**

### 主要

### **Thresholding operator** — 指定阈值化运算符 `>` (default) | `<=`

选择模块在输出二值图像中是包含强度图像中值低于阈值的像素，还是包含值等于或大于阈值的像素。

- `>` — 对于输入图像中大于阈值的像素值，模块在二值图像中输出 `1`。否则，模块将该像素赋值为 `0`。
- `<=` — 对于输入图像中小于等于阈值的像素值，模块输出 `1`。否则，模块将该像素赋值为 `0`。

### **Output threshold** — 输出阈值 `off` (default) | `on`

选择 **Output threshold** 以返回模块用于将强度图像转换为二值图像的阈值。选择此参数会启用 **Th** 输出端口。

### **Output effectiveness metric** — 输出有效性度量 `off` (default) | `on`

选择 **Output effectiveness metric** 以返回有效性度量值。选择此参数会启用 **EMetric** 输出端口。

### **Specify data range** — 指定输入像素值范围 `off` (default) | `on`

选择 **Specify data range** 以启用对用于确定阈值的最小和最大输入像素值的指定。选择此参数会启用 **Minimum value of input**、**Maximum value of input** 和 **When data range is exceeded** 参数。

### **Minimum value of input** — 最小输入像素值 `0` (default) | 标量

指定用于确定阈值的最小输入像素值。

### **Maximum value of input** — 最大输入像素值 `255` (default) | 标量

指定用于确定阈值的最大输入像素值。

### **When data range is exceeded** — 当数据范围超出时要执行的操作 `Ignore` (default) | `Saturate` | `Warn and saturate` | `Error`

指定当输入图像像素的值超出指定数据范围时模块的行为。

- `Ignore` — 模块忽略所有值在指定数据范围之外的像素。
- `Saturate` — 模块将低于数据范围的像素值饱和到指定的最小值，并将高于数据范围的像素值饱和到指定的最大值。
- `Warn and saturate` — 模块在 MATLAB® 命令行窗口中显示警告消息，并按照 `Saturate` 选项的指定饱和像素值。
- `Error` — 模块显示错误消息并结束仿真。

### **Scale threshold** — 指定缩放阈值 `off` (default) | `on`

选择 **Scale threshold** 以启用对阈值化操作的缩放因子的指定。选择此参数会启用 **Threshold scaling factor** 参数。

### **Threshold scaling factor** — 用于阈值化的缩放因子 `1` (default) | 标量

将阈值化操作的缩放因子指定为标量。模块通过将 Otsu 方法计算出的阈值乘以指定的缩放因子来执行阈值化。

### 数据类型

有关定点模块参数的详细信息，请参阅为模块指定定点属性 (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 `off` (default) | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Conversions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

将强度图像转换为二值图像

Autothreshold 模块使用阈值将强度图像转换为二值图像。此模块使用 Otsu 方法确定阈值。
