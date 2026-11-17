---
type: simulink-block
title: 'Sort'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'sort'
documentation_source_path: 'ref/sort.html'
language: zh-CN
chinese_source: worker-translation
---

# Sort

## 端口

### 输入

### **Port\_1** — 数据输入 向量 | 矩阵

该模块接受实值或复值多通道输入。
输入数据类型必须为双精度、单精度、整数或定点，且具有 2 的幂斜率与零偏置。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
### 输出

### **Val** — 排序后的数据 向量 | 矩阵

该模块沿每个通道对数据进行排序，并通过此端口输出排序后的数据。排序后数据的大小、数据类型和复/实性与输入数据一致。该模块根据复数输入的幅值对其进行排序。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Value and index` 或 `Value`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **Idx** — 排序后数据的索引 向量 | 矩阵

此端口的输出包含排序后数据的索引。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Value and index` 或 `Index`。

**数据类型：** `uint32`

## 参数

### 主选项卡

### **Mode** — 指定模块返回数值、索引还是两者 `Value and Index`（默认）| `Value` | `Index`

当 **Mode** 参数设置为：

- `Value` — 该模块根据您在 **Sort order** 参数中指定的内容，按升序或降序对 *M*×*N* 输入矩阵的每个通道中的元素进行排序。每个采样时刻的输出 *Val* 是一个 *M*×*N* 矩阵，其中包含输入的各列排序后的结果。

  该模块根据复数输入的幅值对其进行排序。
- `Index` — 该模块对 *M*×*N* 输入矩阵的每个通道中的元素进行排序，并输出索引数组 *I*。*I* 中的每个元素都是 `uint32` 类型的整数，用于索引输入对应列中排序后的值。
- `Value and index` — 该模块输出输入数据的排序值 *Val*，以及索引数组 *I* 中对应的索引。

### **Sort order** — 排序顺序 `Ascending`（默认）| `Descending`

指定按升序或降序对输入数据进行排序。

### **Sort algorithm** — 排序方法 `Quick sort`（默认）| `Insertion sort`

快速排序算法使用递归排序方法，在对超过 32 个元素进行排序时更快。插入排序算法使用非递归方法，在对少于 32 个元素进行排序时更快。生成代码时，为避免递归函数调用，请使用插入排序算法。

### 数据类型选项卡

**注意**

要使用这些参数，数据输入必须为复数且为定点。对于所有其他输入，**Data Types** 选项卡上的参数将被忽略。复数输入按其幅值排序，幅值为输入的实部与虚部分量的平方和。实部和虚部平方的结果存储在 **Product output** 数据类型中。平方和的结果存储在 **Accumulator** 数据类型中。对于所有其他输入，**Data Types** 选项卡上的参数将被忽略。

### **Rounding mode** — 舍入运算的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 溢出操作的方法 关（默认）| 开

选中此参数时，模块将对其定点运算的结果进行饱和处理。清除此参数时，模块将对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — 乘积输出数据类型 `Inherit: Same as input`（默认）| `fixdt([],16,0)`

复数输入的实部和虚部的平方存储在 **Product output** 数据类型中。

您可以将此参数设置为：

- `Inherit: Same as input` — 乘积输出数据类型与输入数据类型相同。
- `fixdt([],16,0)` — 乘积输出数据类型为自动有符号、二进制点、定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

复数输入的实部和虚部的平方和的结果存储在 **Accumulator** 数据类型中。

您可以将此参数设置为：

- `Inherit: Same as product output` — 累加器数据类型与乘积输出数据类型相同。
- `Inherit: Same as input` — 累加器数据类型与输入数据类型相同。
- `fixdt([],16,0)` — 累加器数据类型为自动有符号、二进制点、定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 关（默认）| 开

选中此参数可防止定点工具覆盖您在模块上指定的数据类型。

## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前推出**

## 描述

按值对输入元素进行排序

Sort 模块根据您指定的 **Sort order**，按 `Ascending` 或 `Descending` 顺序对每个通道（列）中输入元素的值进行排序。复数输入按其幅值排序，幅值为输入的实部与虚部分量的平方和。您可以选择 **Sort algorithm** 为 `Quick sort` 或 `Insertion sort`。快速排序算法使用递归排序方法，在对超过 32 个元素进行排序时更快。插入排序算法使用非递归方法，在对少于 32 个元素进行排序时更快。生成代码时，请使用插入排序算法以避免递归函数调用。

**Mode** 参数指定模块的运行模式，您可以将其设置为 `Value`、`Index` 或 `Value and Index`。
