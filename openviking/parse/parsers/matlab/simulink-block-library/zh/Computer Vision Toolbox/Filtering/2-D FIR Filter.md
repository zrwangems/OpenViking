---
type: simulink-block
title: '2-D FIR Filter'
family: 'filtering'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: '2dfirfilter'
documentation_source_path: 'ref/2dfirfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D FIR Filter

## 端口

### 输入

### **I** — 输入图像矩阵

输入图像，指定为数值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **H** — 滤波器系数矩阵

滤波器系数，指定为数值矩阵。**H** 端口的输入必须与 **I** 端口的输入具有相同的数据类型。

#### 依赖关系

要启用此端口，请将 **Coefficient source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **HV** — 垂直滤波器系数向量

垂直滤波器系数，指定为数值向量。**HV** 端口的输入必须与 **I** 端口的输入具有相同的数据类型。

#### 依赖关系

要启用此端口，请指定以下参数值。

- **Separable filter coefficients** — `on`
- **Coefficient source** — `Input port`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **HH** — 水平滤波器系数向量

水平滤波器系数，指定为数值向量。**HH** 端口的输入必须与 **I** 端口的输入具有相同的数据类型。

#### 依赖关系

要启用此端口，请指定以下参数值。

- **Separable filter coefficients** — `on`
- **Coefficient source** — `Input port`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **PVal** — 填充值标量

填充值，指定为数值标量。**PVal** 端口的输入必须与 **I** 端口的输入具有相同的数据类型。

#### 依赖关系

要启用此端口，请指定以下参数值。

- **Output size** — `Full` 或 `Same as input port I`
- **Padding options** — `Constant`
- **Pad value source** — `Input port`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### 输出

### **Output** — 滤波后的输出图像矩阵

滤波后的输出图像，返回为与输入图像具有相同数据类型的数值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **Separable filter coefficients** — 滤波器系数可分离 `off`（默认） | `on`

如果滤波器系数可分离，请选择此参数。使用可分离滤波器系数可减少模块计算输出时必须执行的计算量。您可以使用 `isfilterseparable` 检查滤波器是否可分离，并计算垂直和水平滤波器系数。

### **Coefficient source** — 滤波器系数的来源 `Specify via dialog`（默认） | `Input port`

将滤波器系数的来源指定为以下选项之一。

- `Specify via dialog` — 使用 **Coefficients** 参数指定滤波器系数；如果选择 **Separable filter coefficients** 参数，则使用 **Vertical coefficients (across height)** 和 **Horizontal coefficients (across width)** 参数指定。
- `Input port` — 使用 **H** 端口指定滤波器系数；如果选择 **Separable filter coefficients** 参数，则使用 **HV** 和 **HH** 端口指定。

### **Coefficients** — 滤波器系数 `[1 0; 0 -1]`（默认） | 数值矩阵

将滤波器系数指定为数值矩阵。

#### 依赖关系

要启用此参数，请指定以下参数值。

- **Separable filter coefficients** — `off`
- **Coefficient source** — `Specify via dialog`

### **Vertical coefficients (across height)** — 垂直滤波器系数 `[4 0]`（默认） | 数值向量

将垂直滤波器系数指定为数值向量。

#### 依赖关系

要启用此参数，请指定以下参数值。

- **Separable filter coefficients** — `on`
- **Coefficient source** — `Specify via dialog`

### **Horizontal coefficients (across height)** — 水平滤波器系数 `[4 0]`（默认） | 数值向量

将水平滤波器系数指定为数值向量。

#### 依赖关系

要启用此参数，请指定以下参数值。

- **Separable filter coefficients** — `on`
- **Coefficient source** — `Specify via dialog`

### **Output size** — 滤波后图像的尺寸 `Full`（默认） | `Same as input port I` | `Valid`

对于尺寸为 *M*×*N* 的输入图像和尺寸为 *P*×*Q* 的滤波器，将滤波后图像的尺寸指定为以下选项之一。

- `Full` — 模块使用填充返回具有完整尺寸 *(M+P–1)*×*(N+Q–1)* 的滤波后图像。
- `Same as input port I` — 模块使用填充返回尺寸为 *M*×*N* 的滤波后图像，与输入图像大小相同。
- `Valid` — 模块仅在系数矩阵无需填充即可完全位于输入图像内时对输入图像进行滤波，并返回尺寸为 *(M–P+1)*×*(N–Q+1)* 的滤波后图像。

### **Padding options** — 填充方法 `Constant`（默认） | `Replicate` | `Symmetric` | `Circular`

将填充方法指定为以下选项之一。

- `Constant` — 用常量值填充输入图像。
- `Replicate` — 通过重复其边界值填充输入图像。
- `Symmetric` — 通过沿边界镜像反射图像来填充输入图像。
- `Circular` — 通过假定图像是周期性的来填充输入图像。

#### 依赖关系

要启用此参数，请将 **Output size** 参数指定为 `Full` 或 `Same as input port I`。

### **Pad value source** — 填充值的来源 `Specify via dialog`（默认） | `Input port`

将填充值的来源指定为以下选项之一。

- `Specify via dialog` — 使用 **Pad value** 参数指定填充值。
- `Input port` — 使用 **PVal** 端口指定填充值。

#### 依赖关系

要启用此参数，请指定以下参数值。

- **Output size** — `Full` 或 `Same as input port I`
- **Padding options** — `Constant`

### **Pad value** — 填充值 `0`（默认） | 数值标量

将填充值指定为数值标量。

#### 依赖关系

要启用此参数，请指定以下参数值。

- **Output size** — `Full` 或 `Same as input port I`
- **Padding options** — `Constant`
- **Pad value source** — `Specify via dialog`

### **Filtering based on** — 滤波方法 `Convolution`（默认） | `Correlation`

将滤波方法指定为 `Convolution` 或 `Correlation`。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

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

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入矩阵进行 2-D FIR 滤波

2-D FIR Filter 模块使用表示为 2-D 系数矩阵或一对可分离滤波器系数向量的 2-D 有限脉冲响应 (FIR) 滤波器对 2-D 灰度图像进行滤波。
