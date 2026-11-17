---
type: simulink-block
title: 'Find Local Maxima'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'findlocalmaxima'
documentation_source_path: 'ref/findlocalmaxima.html'
language: zh-CN
chinese_source: worker-translation
---

# Find Local Maxima

## 端口
```yaml
ports:
- name: I
  summary: 输入 *M*×*N* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Th
  summary: 用于检测局部最大值的阈值 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Idx
  summary: 局部最大值的坐标 *P*×2 矩阵
  direction: output
  data_types: single | double | uint8 | uint16 | uint32
- name: Count
  summary: 局部最大值的数量 标量
  direction: output
  data_types: single | double | uint8 | uint16 | uint32
```

### 输入

### **I** — 输入 *M*×*N* 矩阵

输入，指定为要在其中检测局部最大值的 *M*×*N* 矩阵。如果输入是来自 Hough Transform 模块的 Hough 矩阵输出，请选择 **Input is Hough matrix spanning full theta range** 参数，该参数会将此端口重命名为 **Hough**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Th** — 用于检测局部最大值的阈值 标量

用于检测局部最大值的阈值，指定为标量。

#### 依赖关系

要启用此端口，请将 **Source of threshold value** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Idx** — 局部最大值的坐标 *P*×2 矩阵

局部最大值的坐标，以基于 1 的 [*x*
*y*] 坐标的 *P*×2 矩阵形式返回。*P* 表示局部最大值的数量。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32`

### **Count** — 局部最大值的数量 标量

局部最大值的数量，以标量形式返回。

#### 依赖关系

要启用此端口，请清除 **Output variable size signal** 参数的复选框。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32`
## 参数
```yaml
parameters:
- name: Maximum number of local maxima
  summary: 要检测的局部最大值的最大数量 2 （默认） | 正整数
  group: ''
- name: Neighborhood size
  summary: 邻域区域的大小 [5 7] （默认） | 二元素向量
  group: ''
- name: Source of threshold value
  summary: 输入阈值值的来源 Specify via dialog （默认） | Input port
  group: ''
- name: Threshold
  summary: 用于检测局部最大值的阈值 10 （默认） | 标量
  group: ''
- name: Input is Hough matrix spanning full theta range
  summary: 输入是否为 Hough 矩阵 off （默认） | on
  group: ''
- name: Index output data type
  summary: 局部最大值坐标的数据类型 uint32 （默认） | double | single | uint8 | uint16
  group: ''
- name: Output variable size signal
  summary: 支持可变长度输入信号 on （默认） | off
  group: ''
- name: Count output data type
  summary: 局部最大值数量的数据类型 uint32 （默认） | double | single | uint8 | uint16
  group: ''
```

### **Maximum number of local maxima** — 要检测的局部最大值的最大数量 2 （默认） | 正整数

指定要在输入矩阵中检测的局部最大值的最大数量。该值必须是大于 0 的正整数。

### **Neighborhood size** — 邻域区域的大小 [`5 7`] （默认） | 二元素向量

以 `[r
c]` 形式的二元素向量指定邻域区域的大小。该向量指定窗口大小 *r*×*c*，模块在该窗口内确定局部最大值。窗口大小必须大于或等于 1×1。

### **Source of threshold value** — 输入阈值值的来源 `Specify via dialog` （默认） | `Input port`

指定输入阈值值的来源。当您选择 `Input port` 时，模块启用 **Th** 端口。当您选择 `Specify via dialog` 时，模块启用 **Threshold** 参数。

### **Threshold** — 用于检测局部最大值的阈值 10 （默认） | 标量

指定一个标量值，表示用于检测局部最大值的阈值。

#### 依赖关系

要启用此参数，请将 **Source of threshold value** 参数设置为 `Specify via dialog`。

### **Input is Hough matrix spanning full theta range** — 输入是否为 Hough 矩阵 off （默认） | on

如果此模块的输入是来自 Hough Transform 模块的 Hough 矩阵输出，请选择此参数。Find Local Maxima 模块假定输入是一个关于 rho 轴反对称的 Hough 矩阵，其 theta 值从 -pi/2 到 pi/2 弧度。因此，如果局部最大值靠近边界且其邻域区域在 Hough 矩阵之外，模块仅检测到一个局部最大值。模块会忽略相应的反对称最大值。

### **Index output data type** — 局部最大值坐标的数据类型 `uint32` （默认） | `double` | `single` | `uint8` | `uint16`

指定在输出端口 **Idx** 返回的局部最大值坐标的数据类型。

### **Output variable size signal** — 支持可变长度输入信号 on （默认） | off

指定模型是否支持可变长度的输入信号。

### **Count output data type** — 局部最大值数量的数据类型 `uint32` （默认） | `double` | `single` | `uint8` | `uint16`

指定在输出端口 **Count** 返回的局部最大值数量的数据类型。

#### 依赖关系

要启用此参数，请清除 **Output variable size signal** 参数。
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

## 版本历史

**在 R2006a 之前引入**

## 描述

在矩阵中查找局部最大值

Find Local Maxima 模块在给定的输入矩阵中查找局部最大值。该模块在由邻域大小指定的区域内查找值的局部最大值。模块将搜索区域中的值与用户指定的阈值进行比较，并将大于或等于阈值的值识别为局部最大值。找到局部最大值后，模块将邻域内的所有矩阵值（包括最大值）设置为零。此步骤确保后续搜索不会包含此最大值。该过程重复进行，直到模块找到所有有效最大值或达到指定的局部最大值数量。

必须选择阈值和邻域大小，使模块仅检测真正的局部最大值并消除虚假峰值。

此模块的输入也可以是由 Hough Transform 模块生成的 Hough 矩阵。Find Local Maxima 模块输出检测到的局部最大值的基于 1 的 [*x*
*y*] 坐标。发送到所有输入端口的數據必须具有相同的数据类型。
