---
type: simulink-block
title: 'Deinterlacing'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'deinterlacing'
documentation_source_path: 'ref/deinterlacing.html'
language: zh-CN
chinese_source: worker-translation
---

# Deinterlacing

## 端口
```yaml
ports:
- name: Port_1
  summary: 隔行扫描输入 数值矩阵 | 三维数值数组 | 图像 | 视频
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 去隔行扫描输出 数值矩阵 | 三维数值数组 | 图像 | 视频
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 隔行扫描输入 数值矩阵 | 三维数值数组 | 图像 | 视频

隔行扫描输入，指定为数值矩阵、三维数值数组、图像或视频。

要输入隔行扫描图像，请使用 Image From File 或 Image From Workspace 模块读取图像文件。该图像也可以是视频帧。要输入隔行扫描视频，请使用 From Multimedia File 或 Video From Workspace 模块读取视频文件。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 去隔行扫描输出 数值矩阵 | 三维数值数组 | 图像 | 视频

去隔行扫描输出，返回为数值矩阵、三维数值数组、图像或视频。输出的尺寸和数据类型与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Method
  summary: 去隔行扫描方法 Line repetition（默认）| Linear interpolation | Vertical temporal median filtering
  group: ''
- name: Input image is transposed (data order is row major)
  summary: 指定数据顺序 off（默认）| on
  group: ''
- name: Rounding mode
  summary: 计算定点值时的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: ''
- name: Saturate on integer overflow
  summary: 指定溢出模式 on（默认）| off
  group: ''
- name: Accumulator
  summary: 累加器数据类型 Binary point scaling（默认）| Same as input
  group: ''
- name: Output
  summary: 输出的数据类型 Same as input（默认）| Binary point scaling
  group: ''
- name: Lock data type settings against change by the fixed-point tools
  summary: 数据类型覆盖 off（默认）| on
  group: ''
```

**主选项卡**

### **Method** — 去隔行扫描方法 `Line repetition`（默认）| `Linear interpolation` | `Vertical temporal median filtering`

使用此参数指定对输入数据进行去隔行扫描的方法。

- 如果将 **Method** 参数值设置为 `Line
  repetition`，则隔行扫描图像或视频帧底场的值将替换为前一场顶场的值。
- 如果将 **Method** 参数值设置为 `Line
  interpolation`，则底场的值计算为两个相邻顶场的值的平均值。
- 如果将 **Method** 参数值设置为
  `Vertical temporal median filtering`，则底场的值计算为底场及其两个相邻顶场的值的中位数。

### **Input image is transposed (data order is row major)** — 指定数据顺序 off（默认）| on

您可以使用此参数指定隔行扫描输入是否以行主序存储。当您选择此参数时，模块假定输入缓冲区包含按行顺序排列的数组连续数据元素。否则，模块假定缓冲区以列主序存储数据，使得元素按列顺序排列。

仅在以下情况下使用此参数：

- 您正在开发在采用行主序格式的嵌入式目标上运行的算法。
- 您希望限制在行主序和列主序系统接口处对信号进行转置所需的额外处理。

当您选中此复选框时，Deinterlacing 模块输入的前两个维度将交换。

**数据类型选项卡**

要启用 **Data Types** 选项卡上的选项，请将 **Main** 选项卡中的 **Method** 参数设置为 `Linear interpolation`。

#### **定点运算参数**

### **Rounding mode** — 计算定点值时的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定当指定的数据类型和定标无法精确表示定点计算结果时，模块使用的舍入模式。

有关可用选项的详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 指定溢出模式 on（默认）| off

当您选择此参数时，模块将对其定点运算的结果进行饱和处理。当您清除此参数时，模块将对其定点运算的结果进行回绕处理。

有关饱和和回绕的详细信息，请参阅定点运算的溢出处理。

#### **定点数据类型**

### **Accumulator** — 累加器数据类型 `Binary point scaling`（默认）| `Same as input`

使用此参数指定累加器（和）的数据类型和定标。

- 当您选择 `Binary point scaling` 时，可以输入累加器的字长和小数长度（以位为单位）。字长的默认值设置为 12，小数长度设置为 3。数据类型格式与输入数据格式相同，即有符号或无符号。
- 当您选择 `Same as input` 时，累加器的字长和小数长度与输入匹配。

### **Output** — 输出的数据类型 `Same as input`（默认）| `Binary point scaling`

使用此参数指定输出数据的数据类型和定标。

- 当您选择 `Same as input` 时，累加器的字长和小数长度与输入匹配。
- 当您选择 `Binary point scaling` 时，可以输入输出的字长和小数长度（以位为单位）。字长的默认值设置为 8，小数长度设置为 0。数据类型格式与输入数据类型格式相同，即有符号或无符号。

### **Lock data type settings against change by the fixed-point tools** — 数据类型覆盖 off（默认）| on

选择此参数可防止定点工具覆盖您在模块掩码上指定的数据类型。有关详细信息，请参阅 `fxptdlg`（Fixed-Point Designer），即 Fixed-Point Tool 的参考页。
## 所属库

Computer Vision Toolbox / Analysis & Enhancement

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

消除隔行扫描效应

`Deinterlacing` 模块从隔行扫描图像或视频中消除称为隔行扫描效应的运动伪影。隔行扫描图像或视频帧由顶场和底场组成，它们的采集时间略有不同。隔行扫描图像中的奇数行构成顶场，偶数行构成底场。

当您显示隔行扫描图像时，顶场和底场之间的时间差异会导致可见伪影，隔行扫描图像中的交替行看起来发生了位移。

此伪影称为隔行扫描效应，可以通过去隔行扫描技术进行校正。您可以使用 `Deinterlacing` 模块，通过以下方法之一将隔行扫描视频转换为去隔行扫描视频：

- 行重复
- 线性插值
- 垂直时间中值滤波

您可以使用此模块对强度图像和彩色图像进行去隔行扫描。
