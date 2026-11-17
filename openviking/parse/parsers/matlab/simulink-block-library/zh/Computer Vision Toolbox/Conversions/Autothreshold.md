---
type: simulink-block
title: 'Autothreshold'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'autothreshold'
documentation_source_path: 'ref/autothreshold.html'
language: zh-CN
chinese_source: worker-translation
---

# Autothreshold

## 端口
```yaml
ports:
- name: I
  summary: 输入图像矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: BW
  summary: 输出二值图像矩阵
  direction: output
  data_types: Boolean
- name: Th
  summary: 阈值标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: EMetric
  summary: 有效性度量值标量
  direction: output
  data_types: single | double
```

### 输入

### **I** — 输入图像矩阵

输入图像，指定为 *M*×*N* 矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **BW** — 输出二值图像矩阵

输出二值图像，以 *M*×*N* 矩阵形式返回。

**数据类型：** `Boolean`

### **Th** — 阈值标量

用于将强度图像转换为二值图像的阈值，以标量形式返回。

该模块使用 Otsu 方法计算阈值。该模块通过拆分输入图像的直方图来计算此值，使得每个像素组的方差最小化。

#### 依赖关系

要启用此端口，请选择 **Output threshold** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **EMetric** — 有效性度量值标量

有效性度量值，以范围 [0, 1] 内的标量形式返回。

如果输入图像的所有像素值相同，则有效性度量值为 `0`。如果图像有两个唯一像素，或者图像的直方图是对称的，则有效性度量值为 `1`。

#### 依赖关系

要启用此端口，请选择 **Output effectiveness metric** 参数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Thresholding operator
  summary: 指定阈值操作符 >（默认）| <=
  group: 主
- name: Output threshold
  summary: 输出阈值 off（默认）| on
  group: 主
- name: Output effectiveness metric
  summary: 输出有效性度量 off（默认）| on
  group: 主
- name: Specify data range
  summary: 指定输入像素值范围 off（默认）| on
  group: 主
- name: Minimum value of input
  summary: 最小输入像素值 0（默认）| 标量
  group: 主
- name: Maximum value of input
  summary: 最大输入像素值 255（默认）| 标量
  group: 主
- name: When data range is exceeded
  summary: 超出数据范围时执行的操作 Ignore（默认）| Saturate | Warn and saturate | Error
  group: 主
- name: Scale threshold
  summary: 指定缩放阈值 off（默认）| on
  group: 主
- name: Threshold scaling factor
  summary: 阈值操作的缩放因子 1（默认）| 标量
  group: 主
- name: Lock data type settings against change by the fixed-point tools
  summary: 数据类型覆盖 off（默认）| on
  group: 数据类型
```

**主**

**数据类型**

### 主

### **Thresholding operator** — 指定阈值操作符 `>`（默认）| `<=`

选择该模块是将强度图像中值低于阈值的像素还是值等于或大于阈值的像素包含在输出二值图像中。

- `>` — 对于输入图像中大于阈值的像素值，该模块在二值图像中输出 `1`。否则，该模块将像素赋值为 `0`。
- `<=` — 对于输入图像中小于或等于阈值的像素值，该模块输出 `1`。否则，该模块将像素赋值为 `0`。

### **Output threshold** — 输出阈值 `off`（默认）| `on`

选择 **Output threshold** 以返回该模块用于将强度图像转换为二值图像的阈值。选择此参数将启用 **Th** 输出端口。

### **Output effectiveness metric** — 输出有效性度量 `off`（默认）| `on`

选择 **Output effectiveness metric** 以返回有效性度量值。选择此参数将启用 **EMetric** 输出端口。

### **Specify data range** — 指定输入像素值范围 `off`（默认）| `on`

选择 **Specify data range** 以启用输入像素最小值和最大值的指定，用于确定阈值。选择此参数将启用 **Minimum value of input**、**Maximum value of input** 和 **When data range is exceeded** 参数。

### **Minimum value of input** — 最小输入像素值 `0`（默认）| 标量

指定用于确定阈值的输入像素最小值。

### **Maximum value of input** — 最大输入像素值 `255`（默认）| 标量

指定用于确定阈值的输入像素最大值。

### **When data range is exceeded** — 超出数据范围时执行的操作 `Ignore`（默认）| `Saturate` | `Warn and saturate` | `Error`

指定当输入图像像素值超出指定数据范围时该模块的行为。

- `Ignore` — 该模块忽略所有值超出指定数据范围的像素。
- `Saturate` — 该模块将低于数据范围的像素值饱和到指定的最小值，将高于数据范围的像素值饱和到指定的最大值。
- `Warn and saturate` — 该模块在 MATLAB® 命令窗口中显示警告消息，并按照 `Saturate` 选项的指定对像素值进行饱和处理。
- `Error` — 该模块显示错误消息并结束仿真。

### **Scale threshold** — 指定缩放阈值 `off`（默认）| `on`

选择 **Scale threshold** 以启用阈值操作的缩放因子指定。选择此参数将启用 **Threshold scaling factor** 参数。

### **Threshold scaling factor** — 阈值操作的缩放因子 `1`（默认）| 标量

以标量形式指定阈值操作的缩放因子。该模块通过将 Otsu 方法计算的阈值乘以指定的缩放因子来执行阈值操作。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。
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

**在 R2006a 之前引入**

## 描述

将强度图像转换为二值图像

Autothreshold 模块使用阈值将强度图像转换为二值图像。该模块使用 Otsu 方法确定阈值。
