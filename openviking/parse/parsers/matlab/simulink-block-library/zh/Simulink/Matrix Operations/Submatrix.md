---
type: simulink-block
title: 'Submatrix'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'submatrix'
documentation_source_path: 'slref/submatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Submatrix

## 端口

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵

输入信号，模块从中提取指定的子矩阵。

此模块支持 Simulink® 虚拟总线。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 选定的子矩阵 向量 | 矩阵

从输入信号中选定的子矩阵。输出的数据类型与输入相同。

此模块支持 Simulink 虚拟总线。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

## 参数

有关选择元素子集以构成子矩阵的详细信息，请参阅范围指定选项。

### **Row span** — 行范围 `All rows`（默认） | `One row` | `Range of rows`

输出中保留的输入行范围。

### **Row** — 输出的第一行 `First`（默认） | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

用作输出的第一行且唯一一行的输入行。

#### 依赖关系

要启用此参数，请将 **Row span** 设置为 `One row`。

### **Starting row** — 输出的第一行 `First`（默认） | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

用作输出的第一行的输入行。

#### 依赖关系

要启用此参数，请将 **Row span** 设置为 `Range of rows`。

### **Row index** — 第一行的索引 `1`（默认） | 正整数

用作输出的第一行且唯一一行的输入行的索引，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Row span** 设置为 `One row`，并将 **Row** 设置为 `Index`。

### **Starting row index** — 第一行的索引 `1`（默认） | 正整数

用作输出的第一行的输入行的索引，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Row span** 设置为 `Range of rows`，并将 **Starting row** 设置为 `Index`。

### **Row offset** — 第一行的偏移量 `1`（默认） | 正整数

用作输出的第一行且唯一一行的输入行的偏移量，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Row span** 设置为 `One row`，并将 **Row** 设置为 `Offset from last` 或 `Offset from middle`。

### **Starting row offset** — 第一行的偏移量 `1`（默认） | 正整数

用作输出的第一行的输入行的偏移量，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Row span** 设置为 `Range of rows`，并将 **Starting row** 设置为 `Offset from last` 或 `Offset from middle`。

### **Ending row** — 最后一行 `Last`（默认） | `Index` | `Offset from last` | `Offset from middle` | `Middle`

用作输出的最后一行的输入行。

#### 依赖关系

要启用此参数，请将 **Row span** 设置为 `Range of rows`，并将 **Starting row** 设置为除 `Last` 以外的任意值。

### **Ending row index** — 最后一行的索引 `1`（默认） | 正整数

用作输出的最后一行的输入行的索引，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Ending row** 设置为 `Index`。

### **Ending row offset** — 最后一行的偏移量 `1`（默认） | 正整数

用作输出的最后一行的输入行的偏移量。

#### 依赖关系

要启用此参数，请将 **Ending row** 设置为 `Offset from middle` 或 `Offset from last`。

### **Column span** — 输入列范围 `All columns`（默认） | `One column` | `Range of columns`

输出中保留的输入列范围。

### **Column** — 第一列 `First`（默认） | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

用作输出的第一列且唯一一列的输入列。

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `One column`。

### **Starting column** — 第一列 `First`（默认） | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

用作输出的第一列的输入列。

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `Range of columns`。

### **Starting column index** — 第一列的索引 `1`（默认） | 正整数

用作输出的第一列的输入列的索引，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `Range of columns`，并将 **Starting column** 设置为 `Index`。

### **Column index** — 第一列的索引 `1`（默认） | 正整数

用作输出的第一列且唯一一列的输入列的索引，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `One column`，并将 **Column** 设置为 `Index`。

### **Column offset** — 第一列的偏移量 `1`（默认） | 正整数

用作输出的第一列且唯一一列的输入列的偏移量，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `One column`，并将 **Column** 设置为 `Offset from last` 或 `Offset from middle`。

### **Starting column offset** — 第一列的偏移量 `1`（默认） | 正整数

用作输出的第一列的输入列的偏移量，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `Range of columns`，并将 **Starting column** 设置为 `Offset from last` 或 `Offset from middle`。

### **Ending column** — 最后一列 `Last`（默认） | `Index` | `Offset from last` | `Offset from middle` | `Middle`

用作输出的最后一列的输入列。

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `Range of columns`，并将 **Starting column** 设置为除 `Last` 以外的任意值。

### **Ending column index** — 最后一列的索引 `1`（默认） | 正整数

用作输出的最后一列的输入列的索引，指定为大于或等于 1 的整数。

#### 依赖关系

要启用此参数，请将 **Ending column** 设置为 `Index`。

### **Ending column offset** — 最后一列的偏移量 `1`（默认） | 正整数

用作输出的最后一列的输入列的偏移量。

#### 依赖关系

要启用此参数，请将 **Ending column** 设置为 `Offset from middle` 或 `Offset from last`。

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2021b：Create Submatrix 模块移至 Simulink Matrix Operations 库

Submatrix 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** 库移至 **Simulink** > **Matrix Operations** 库。所有现有模型继续正常工作。

## 描述

从矩阵输入中选择元素子集（子矩阵）

Submatrix 模块从 *M*×*N* 输入矩阵 `u` 中提取连续子矩阵 *y*。
有关选择要提取的行和列的详细信息，请参阅范围指定选项。
