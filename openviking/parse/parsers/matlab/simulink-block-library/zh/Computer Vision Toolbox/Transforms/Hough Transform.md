---
type: simulink-block
title: 'Hough Transform'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'houghtransform'
documentation_source_path: 'ref/houghtransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Hough Transform

## 端口
```yaml
ports:
- name: BW
  summary: 二值图像矩阵
  direction: input
  data_types: Boolean
- name: Hough
  summary: 参数空间矩阵
  direction: output
  data_types: single | double | fixed point
- name: Theta
  summary: Theta 值向量
  direction: output
  data_types: single | double | fixed point
- name: Rho
  summary: Rho 值向量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **BW** — 二值图像矩阵

二值图像，指定为 `Boolean` 值的矩阵。

**数据类型：** `Boolean`
### 输出

### **Hough** — 参数空间矩阵

参数空间矩阵，以数值矩阵形式返回。参数空间矩阵中的值位于 (*rho, theta*) 空间中。

**数据类型：** `single` | `double` | `fixed point`

### **Theta** — Theta 值向量

Theta 值，以数值向量形式返回。每个元素表示对应直线的旋转角度，以弧度为单位。

#### 依赖关系

要启用此端口，必须选择 **Output theta and rho values** 参数。

**数据类型：** `single` | `double` | `fixed point`

### **Rho** — Rho 值向量

Rho 值，以数值向量形式返回。每个元素表示对应直线距图像左上角点的距离。

#### 依赖关系

要启用此端口，必须选择 **Output theta and rho values** 参数。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Theta resolution (radians)
  summary: Theta 分辨率 pi/180（默认）| 正标量
  group: 主
- name: Rho resolution (pixels)
  summary: Rho 分辨率 1（默认）| 正标量
  group: 主
- name: Output theta and rho values
  summary: 启用 Theta 和 Rho 输出端口 off（默认）| on
  group: 主
- name: Output data type
  summary: 输出数据类型 double（默认）| single | Specify via Fixed-point tab
  group: 主
- name: Lock data type settings against change by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
```

### 主

### **Theta resolution (radians)** — Theta 分辨率 `pi/180`（默认）| 正标量

指定 Hough 变换 bin 沿 *theta* 轴的间距。此值必须小于 `pi/2`。

### **Rho resolution (pixels)** — Rho 分辨率 `1`（默认）| 正标量

指定 Hough 变换 bin 沿 *rho* 轴的间距。

### **Output theta and rho values** — 启用 Theta 和 Rho 输出端口 `off`（默认）| `on`

选择此参数以启用 **Theta** 和 **Rho** 输出端口。模块分别在这些端口输出 *theta* 轴和 *rho* 轴向量。

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `Specify via Fixed-point tab`

指定输出信号的数据类型。如果选择 `double` 或 `single`，所有输出均为指定的数据类型。如果选择 `Specify via Fixed-point tab`，可以在 **Data Types** 选项卡中指定每个输出的字长。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。
## 所属库

Computer Vision Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `doublea` | `fixed point` | `integer` | `singlea` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 输出端口支持此数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

在图像中查找直线

使用 Hough Transform 模块在图像中查找直线。该模块输出 Hough 空间矩阵，并可选输出 *rho* 轴和 *theta* 轴向量。矩阵中的峰值表示输入图像中潜在的直线。您可以使用 Hough Transform 模块的输出，通过 Hough Lines 模块在图像中查找直线。或者，您可以使用自定义算法，通过定位 Hough 空间矩阵中的峰值来识别潜在的直线。
