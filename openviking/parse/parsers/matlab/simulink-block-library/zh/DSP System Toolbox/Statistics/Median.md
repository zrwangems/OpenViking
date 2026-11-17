---
type: simulink-block
title: 'Median'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'median'
documentation_source_path: 'ref/median.html'
language: zh-CN
chinese_source: worker-translation
---

# Median

## 端口
```yaml
ports:
- name: Port_1
  summary: 数据输入 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 沿指定维度的中值 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 数据输入 向量 | 矩阵 | *N* 维数组

该模块接受实值或复值多通道和多维输入。输入数据类型必须为双精度、单精度、整数或定点，且具有 2 的幂斜率与零偏置。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 沿指定维度的中值 向量 | 矩阵 | *N* 维数组

该模块计算输入每一行或每一列的中值，或沿输入指定维度的向量计算中值。它还可以计算整个输入的中值。输出数组 `y` 中的每个元素是对应列、行或整个输入的中值。输出数组 `y` 取决于 **Find the median value over** 参数的设置。

考虑一个大小为 *M*×*N*×*P* 的三维输入信号。
当您将 **Find the median value over** 设置为：

- `Entire input` — 每个采样时刻的输出是一个标量，包含 *M*×*N*×*P* 输入矩阵的中值。
- `Each row` — 每个采样时刻的输出由 *M*×1×*P* 数组组成，其中每个元素包含输入第二维上每个向量的中值。对于 *M*×*N* 矩阵输入，输出为 *M*×1 列向量。
- `Each column` — 每个采样时刻的输出由 1×*N*×*P* 数组组成，其中每个元素包含输入第一维上每个向量的中值。对于 *M*×*N* 矩阵输入，每个采样时刻的输出为 1×*N* 行向量。

  在此模式下，该模块将长度为 *M* 的无向向量输入视为 *M*×1 列向量。
- `Specified dimension` — 每个采样时刻的输出取决于 **Dimension** 参数的值。如果将 **Dimension** 设置为 `1`，则输出与选择 `Each column` 时相同。如果将 **Dimension** 设置为 `2`，则输出与选择 `Each row` 时相同。如果将 **Dimension** 设置为 `3`，则每个采样时刻的输出为 *M*×*N* 矩阵，其中包含输入第三维上每个向量的中值。

  输出的数据类型与输入的数据类型一致。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Sort algorithm
  summary: 排序方法 Quick sort（默认）| Insertion sort
  group: 主选项卡
- name: Find the median value over
  summary: 计算中值所沿的维度 Each column（默认）| Entire input | Each row | Specified dimension
  group: 主选项卡
- name: Dimension
  summary: 自定义维度 1（默认）| 标量
  group: 主选项卡
- name: Rounding mode
  summary: 舍入操作的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Same as input（默认）| fixdt([],16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Same as product output（默认）| Inherit: Same as input | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as accumulator（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 输出最小值 []（默认）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 输出最大值 []（默认）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Sort algorithm** — 排序方法 `Quick sort`（默认）| `Insertion sort`

将排序算法指定为 `Quick sort` 或 `Insertion sort`。

### **Find the median value over** — 计算中值所沿的维度 `Each column`（默认）| `Entire input` | `Each row` | `Specified dimension`

- `Each column` — 该模块输出每一列的中值。
- `Each row` — 该模块输出每一行的中值。
- `Entire input` — 该模块输出整个输入的中值。
- `Specified dimension` — 该模块输出 **Dimension** 参数中所指定维度上的中值。

### **Dimension** — 自定义维度 `1`（默认）| 标量

指定该模块计算中值所沿的输入信号维度（从 1 开始的值）。此参数的值必须大于 0 且小于或等于输入信号的维度数。

#### 依赖关系

要启用此参数，请将 **Find the median value over** 设置为 `Specified dimension`。

### 数据类型选项卡

**注意**

要使用这些参数，数据输入必须为定点。对于所有其他输入，**Data Types** 选项卡上的参数将被忽略。

### **Rounding mode** — 舍入操作的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多详细信息，请参阅 rounding mode。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认）| on

当您选中此参数时，该模块将对其定点运算的结果进行饱和处理。当您清除此参数时，该模块将对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅 overflow mode for fixed-point operations。

### **Product output** — 乘积输出数据类型 `Inherit: Same as input`（默认）| `fixdt([],16,0)`

指定 Median 模块中乘积运算输出的数据类型。有关更多信息，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。

您可以将此参数设置为：

- `Inherit: Same as input` — 乘积输出数据类型与输入数据类型相同。
- `fixdt([],16,0)` — 乘积输出数据类型为自动有符号、二进制点、缩放定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

指定 Median 模块中累加运算输出的数据类型。有关更多详细信息，请参阅 Fixed-Point Data Types。

您可以将此参数设置为：

- `Inherit: Same as product output` — 累加器数据类型与乘积输出数据类型相同。
- `Inherit: Same as input` — 累加器数据类型与输入数据类型相同。
- `fixdt([],16,0)` — 累加器数据类型为自动有符号、二进制点、缩放定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Output** 指定 Median 模块输出的数据类型。有关更多详细信息，请参阅 Fixed-Point Data Types。

您可以将此参数设置为：

- `Inherit: Same as accumulator` — 输出数据类型与累加器数据类型相同。
- `Inherit: Same as input` — 输出数据类型与输入数据类型相同。
- `Inherit: Same as product output` — 输出数据类型与乘积输出数据类型相同。
- `fixdt([],16,0)` — 输出数据类型为自动有符号、二进制点、缩放定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认）| 标量

指定该模块可以输出的最小值。默认值为 `[]`（未指定）。Simulink® 使用此值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Output Maximum** — 输出最大值 `[]`（默认）| 标量

指定该模块可以输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动缩放。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 off（默认）| on

选中此参数可防止定点工具覆盖您在模块上指定的数据类型。
## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

输入的中值

Median 模块计算输入每一行或每一列的中值，或沿输入指定维度的向量计算中值。它还可以计算整个输入的中值。您可以使用 **Find the median value over** 参数指定维度。在计算中值时，该模块首先对输入值进行排序。如果值的数量为奇数，则中值为中间值。如果值的数量为偶数，则中值为两个中间值的平均值。要对数据进行排序，您可以将 **Sort algorithm** 参数指定为 `Quick sort` 或 `Insertion sort`。该模块根据复数的幅值对其进行排序。
