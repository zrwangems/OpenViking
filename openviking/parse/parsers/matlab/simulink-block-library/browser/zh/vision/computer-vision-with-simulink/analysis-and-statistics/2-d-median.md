---
type: simulink-block
title: '2-D Median'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Analysis and Statistics'
documentation_page: '2dmedian'
documentation_source_path: 'ref/2dmedian.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Median

## 端口

### 输入

### **Port\_1** — 输入数组 标量 | 向量 | 矩阵 | *N* 维数组

将输入数组指定为向量、矩阵或 *N* 维数组。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出中位数值 标量 | 向量 | 矩阵 | *N* 维数组

中位数值以标量、向量、矩阵或 *N* 维数组形式返回。输出的大小以及中位数的计算方式取决于 **Find the median value over** 参数的设置。

- 对于 *M*×*N* 输入数组，**Find the median value over** 参数的值按以下方式确定输出形式。

  - `Entire input` — 输出为 *M*×*N* 输入数组所有元素的中位数值，作为标量
  - `Each row` — 输出为 *M*×1 列向量，其中向量中的每个元素是输入数组中对应行的中位数值。
  - `Each column` — 输出为 1×*N* 行向量，其中向量中的每个元素是输入数组中对应列的中位数值。
  - `Specified dimension` — 如果 **Dimension** 参数设置为 `1`，则输出与选择 `Each column` 时相同。如果 **Dimension** 参数设置为 `2`，则输出与选择 `Each row` 时相同。如果 **Dimension** 参数设置为 `3`，则每个采样时间的输出为 *M*×*N* 矩阵，其中包含输入第三维上每个向量的中位数值
- 对于 *N* 维数组，**Find the median value over** 参数的值按以下方式确定输出形式。

  - `Entire input` — 输出为 *M*×*N*×*P* 输入数组所有元素的中位数值，作为标量。
  - `Each row` — 输出为 *M*×1×*P* 数组，其中每个元素包含每个平面中每个行向量的中位数值。
  - `Each column` — 输出维度为 1×*N*×*P* 数组，其中每个元素包含每个平面中每个列向量的中位数值。
  - `Specified dimension` — 输出取决于 **Dimension**。如果 **Dimension** 设置为 `1`，则输出与选择 `Each column` 时相同。如果 **Dimension** 设置为 `2`，则输出与选择 `Each row` 时相同。如果 **Dimension** 设置为 `3`，则输出维度为 *M*×*N* 矩阵，其中包含输入第三维上每个向量的中位数值

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

**主要**

### **Sort algorithm** — 用于对输入数组排序的算法 `Quick sort` (default) | `Insertion sort`

指定对输入数组进行排序所用的算法。

- `Quick sort` — 此排序算法使用递归排序方法，在对超过 32 个元素进行排序时更快。
- `Insertion sort` — 此排序算法使用非递归方法，在对少于 32 个元素进行排序时更快。

生成代码时，为避免递归函数调用，请使用 `Insertion sort` 算法。

### **Find the median value over** — 计算中位数所沿的维度 `Entire input` (default) | `Each row` | `Each column` | `Specified dimension`

指定模块计算中位数所沿的输入维度。

- `Entire input` — 在整个输入上计算中位数。输出值为标量
- `Each row` — 在输入的每一行上计算中位数。输出为列向量
- `Each column` — 在输入的每一列上计算中位数。输出为行向量
- `Specified dimension` — 在 **Dimension** 参数所指定的输入维度上计算中位数。

  - 如果 **Dimension** 为 `1`，则输出与选择 `Each column` 时相同
  - 如果 **Dimension** 为 `2`，则输出与选择 `Each row` 时相同

### **Dimension** — 自定义维度 `1` (default) | positive scalar

指定输入数组的维度（从 1 开始的值），模块沿该维度计算中位数。此参数的值不得超过输入数组的维数。

#### 依赖关系

要启用此参数，请将 **Find the median value over** 参数设置为 `Specified dimension`。

**数据类型选项卡**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型的选项 `off` (default) | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

**注意**

浮点继承优先于此窗格中定义的数据类型设置。当输入为浮点时，模块会忽略这些设置，所有内部数据类型均为浮点。

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

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数 (string.h)。

## 版本历史

**在 R2006a 之前引入**

## 描述

输入数组的 2-D Median 值

2-D Median 模块计算输入数组的中位数。数组的中位数通过以下步骤计算。

1. 矩阵中的值按数值顺序排序。
2. 要查找数组 *A* 的中位数，该数组的元素总数为 *p*，其中 *p* 为：

   - 奇数 — 中位数 = *A*(`ceil`(*p* / 2))
   - 偶数 — 中位数 = (*A* (*p* / 2) + *A* (( *p* / 2) + 1)) / 2
