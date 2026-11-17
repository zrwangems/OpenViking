---
type: simulink-block
title: 'Overwrite Values'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'overwritevalues'
documentation_source_path: 'ref/overwritevalues.html'
language: zh-CN
chinese_source: worker-translation
---

# Overwrite Values

## 端口

### 输入

### **A** — 输入数据 标量 | 向量 | 矩阵

将输入数据指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `bus`

### **V** — 覆盖值 标量 | 向量 | 矩阵

指定用于覆盖输入矩阵指定部分的值。此参数的维度必须与你要覆盖的矩阵部分的维度匹配，该部分由模块对话框中的行跨度和列跨度相关参数指定。

有关如何指定有效覆盖值的详细信息，请参阅 Valid Overwriting Values。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `bus`

### 输出

### **B** — 修改后的数据 标量 | 向量 | 矩阵

根据模块对话框中的行跨度和列跨度相关参数修改的数据，以标量、向量或矩阵形式返回。

输出的大小与原始输入信号相同。此模块的输入和输出必须具有相同的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `bus`

## 参数

### **Overwrite** — 覆盖子矩阵或对角线 `Submatrix`（默认） | `Diagonal`

指定是覆盖子矩阵还是覆盖对角线的指定部分。

### **Source of overwriting value(s)** — 覆盖值的来源 `Specify via dialog`（默认） | `Second input port`

将覆盖值的来源指定为以下选项之一：

- `Specify via dialog` — 必须在 **Overwrite with** 参数中提供覆盖值。模块在每个时间步使用相同的覆盖值来覆盖输入的指定部分。要了解如何指定有效的覆盖值，请参阅 Valid Overwriting Values。
- `Second input port` — 必须通过第二个模块输入端口 **V** 提供覆盖值。使用此设置可在每个时间步提供不同的覆盖值。输出的大小和速率继承自输入信号，而不是覆盖值。

  通过输入端口 **V** 提供覆盖值的速率必须与模块在输入端口 **A** 接收每个输入矩阵的速率匹配。换句话说，输入信号必须具有相同的 Simulink® 采样时间。

### **Overwrite with** — 用于覆盖的值 `0`（默认） | 标量 | 向量 | 矩阵

指定用于覆盖输入矩阵指定部分的值。此参数的维度必须与你要覆盖的矩阵部分的维度匹配，该部分由模块对话框中的行跨度和列跨度相关参数指定。

有关如何指定有效覆盖值的详细信息，请参阅 Valid Overwriting Values。

#### 依赖关系

要启用此参数，请将 **Source of overwriting value(s)** 设置为 `Specify via dialog`。

### **Row span** — 输入行的跨度 `Range of rows`（默认） | `All rows` | `One row`

指定要覆盖的输入行的跨度。可以将此参数设置为以下选项之一：

- `Range of rows` — 子矩阵包含输入的一行或多行，必须在 **Starting row** 和 **Ending row** 参数中指定。
- `All rows` — 子矩阵包含输入矩阵的所有行。
- `One row` — 子矩阵仅包含输入矩阵的一行，必须在 **Row** 参数中指定。

当将 **Row span** 设置为 `One row` 或 `Range of rows` 时，需要通过设置 **Row** 或 **Starting row** 和 **Ending row** 参数进一步指定子矩阵中包含的行。

### **Row/Starting row** — 行或起始行 `First`（默认） | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

指定作为模块覆盖的子矩阵第一行的输入行。可以将此参数设置为以下选项之一：

- `First` –– 输入的第一行
- `Index` –– 使用 **Row index** 和 **Starting row index** 参数指定第一个输入行
- `Offset from last` –– 索引为 *M* − *rowOffset* 的输入行，其中 *M* 是输入行数，*rowOffset* 是在 **Row offset** 和 **Starting row offset** 参数中指定的值
- `Last` –– 输入的最后一行
- `Offset from middle` –– 索引为 `floor`(*M*/2 + 1 − *rowOffset*) 的输入行，其中 *M* 是输入行数，*rowOffset* 是在 **Row offset** 和 **Starting row offset** 参数中指定的值
- `Middle` –– 索引为 `floor`(*M*/2 + 1) 的输入行，其中 *M* 是输入行数

#### 依赖关系

要启用 **Row** 参数，请将 **Row span** 设置为 `One row`。

要启用 **Starting row** 参数，请将 **Row span** 设置为 `Range of rows`。

### **Row index/Starting row index** — 行索引或起始行索引 `1`（默认） | 正整数

将作为模块覆盖的子矩阵第一行的输入行的索引指定为正整数。

#### 依赖关系

要启用 **Row index** 参数，请将 **Row** 设置为 `Index`。

要启用 **Starting row index** 参数，请将 **Starting row** 设置为 `Index`。

### **Row offset/Starting row offset** — 行偏移或起始行偏移 1 | 非负整数

指定作为模块覆盖的子矩阵第一行的输入行的偏移。当将 **Row/Starting row** 设置为以下选项之一时：

- `Offset from last` –– 索引为 *M* − *rowOffset* 的输入行，其中 *M* 是输入行数，*rowOffset* 是在此参数中指定的值
- `Offset from middle` –– 索引为 `floor`(*M*/2 + 1 − *rowOffset*) 的输入行，其中 *M* 是输入行数，*rowOffset* 是在此参数中指定的值

#### 依赖关系

要启用 **Row offset**，请将 **Row** 设置为 `Offset from middle` 或 `Offset from last`。

要启用 **Starting row offset**，请将 **Starting row** 设置为 `Offset from middle` 或 `Offset from last`。

### **Ending row** — 结束行 `Last`（默认） | `Index` | `Offset from last` | `Offset from middle` | `Middle`

指定作为模块覆盖的子矩阵最后一行的输入行。可以将此参数设置为以下选项之一：

- `Index` –– 使用 **Ending row index** 参数指定结束输入行
- `Offset from last` –– 索引为 *M* − *rowOffset* 的输入行，其中 *M* 是输入行数，*rowOffset* 是在 **Ending row offset** 参数中指定的值
- `Last` –– 输入的最后一行
- `Offset from middle` –– 索引为 `floor`(*M*/2 + 1 − *rowOffset*) 的输入行，其中 *M* 是输入行数，*rowOffset* 是在 **Ending row offset** 参数中指定的值
- `Middle` –– 索引为 `floor`(*M*/2 + 1) 的输入行，其中 *M* 是输入行数

#### 依赖关系

要启用 **Ending row** 参数，请将 **Row span** 设置为 `Range of rows`，并将 **Starting row** 设置为除 `Last` 以外的任意选项。

### **Ending row index** — 子矩阵最后一行的索引 `1`（默认） | 正整数

将作为模块覆盖的子矩阵最后一行的输入行的索引指定为正整数。

#### 依赖关系

要启用此参数，请将 **Ending row** 设置为 `Index`。

### **Ending row offset** — 结束行偏移 1 | 非负整数

指定作为模块覆盖的子矩阵最后一行的输入行的偏移。当将 **Ending row** 设置为以下选项之一时：

- `Offset from last` –– 索引为 *M* − *rowOffset* 的输入行，其中 *M* 是输入行数，*rowOffset* 是在 **Ending row offset** 参数中指定的值
- `Offset from middle` –– 索引为 `floor`(*M*/2 + 1 − *rowOffset*) 的输入行，其中 *M* 是输入行数，*rowOffset* 是在 **Ending row offset** 参数中指定的值

#### 依赖关系

要启用此参数，请将 **Ending row** 设置为 `Offset from middle` 或 `Offset from last`。

### **Column span** — 输入列的跨度 `Range of columns`（默认） | `All columns` | `One column`

指定要覆盖的输入列的跨度。可以将此参数设置为以下选项之一：

- `Range of columns` — 子矩阵包含输入的一列或多列，必须在 **Starting column** 和 **Ending column** 参数中指定。
- `All columns` — 子矩阵包含输入矩阵的所有列。
- `One column` — 子矩阵仅包含输入矩阵的一列，必须在 **Column** 参数中指定。

当将 **Column span** 设置为 `One column` 或 `Range of columns` 时，需要通过设置 **Column** 或 **Starting column** 和 **Ending column** 参数进一步指定子矩阵中包含的列。

### **Column/Starting column** — 列或起始列 `First`（默认） | `Index` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

指定作为模块覆盖的子矩阵第一列的输入列。可以将此参数设置为以下选项之一：

- `First` –– 输入的第一列
- `Index` –– 使用 **Column index** 和 **Starting column index** 参数指定第一个输入列
- `Offset from last` –– 索引为 *N* − *colOffset* 的输入列，其中 *N* 是输入列数，*colOffset* 是在 **Column offset** 和 **Starting column offset** 参数中指定的值
- `Last` –– 输入最后一列
- `Offset from middle` –– 索引为 `floor`(*N*/2 + 1 − *colOffset*) 的输入列，其中 *N* 是输入列数，*colOffset* 是在 **Column offset** 和 **Starting column offset** 参数中指定的值
- `Middle` –– 索引为 `floor`(*N*/2 + 1) 的输入列，其中 *N* 是输入列数

#### 依赖关系

要启用 **Column** 参数，请将 **Column span** 设置为 `One column`。

要启用 **Starting column** 参数，请将 **Column span** 设置为 `Range of columns`。

### **Column index/Starting column index** — 列索引或起始列索引 1 | 正整数

将作为模块覆盖的子矩阵第一列的输入列的索引指定为正整数。

#### 依赖关系

要启用 **Column index** 参数，请将 **Column** 设置为 `Index`。

要启用 **Starting column index** 参数，请将 **Starting column** 设置为 `Index`。

### **Column offset/Starting column offset** — 列偏移或起始列偏移 1 | 非负整数

指定作为模块覆盖的子矩阵第一列的输入列的偏移。当将 **Starting column** 设置为以下选项之一时：

- `Offset from last` –– 索引为 *N* − *colOffset* 的输入列，其中 *N* 是输入列数，*colOffset* 是在 **Column offset** 和 **Starting column offset** 参数中指定的值
- `Offset from middle` –– 索引为 `floor`(*N*/2 + 1 − *colOffset*) 的输入列，其中 *N* 是输入列数，*colOffset* 是在 **Column offset** 和 **Starting column offset** 参数中指定的值

#### 依赖关系

要启用 **Column offset** 参数，请将 **Column** 设置为 `Offset from middle` 或 `Offset from last`。

要启用 **Starting column offset** 参数，请将 **Starting column** 设置为 `Offset from middle` 或 `Offset from last`。

### **Ending column** — 结束列 `Last`（默认） | `Index` | `Offset from last` | `Offset from middle` | `Middle`

指定作为模块覆盖的子矩阵最后一列的输入列。可以将参数设置为以下选项之一：

- `Last` –– 输入最后一列
- `Index` –– 使用 **Ending column index** 参数指定输入列
- `Offset from last` –– 索引为 *N* − *colOffset* 的输入列，其中 *N* 是输入列数，*colOffset* 是在 **Ending column offset** 参数中指定的值
- `Offset from middle` –– 索引为 `floor`(*N*/2 + 1 − *colOffset*) 的输入列，其中 *N* 是输入列数，*colOffset* 是在 **Ending column offset** 参数中指定的值
- `Middle` –– 索引为 `floor`(*N*/2 + 1) 的输入列，其中 *N* 是输入列数

#### 依赖关系

要启用此参数，请将 **Column span** 设置为 `Range of columns`，并将 **Starting column** 设置为除 `Last` 以外的任意选项。

### **Ending column index** — 结束列索引 `1`（默认） | 正整数

将作为模块覆盖的子矩阵最后一列的输入列的索引指定为正整数。

#### 依赖关系

要启用此参数，请将 **Ending column** 设置为 `Index`。

### **Ending column offset** — 结束列偏移 `1` | 非负整数

指定作为模块覆盖的子矩阵最后一列的输入列的偏移。当将 **Ending column** 设置为以下选项之一时：

- `Offset from last` –– 索引为 *N* − *colOffset* 的输入列，其中 *N* 是输入列数，*colOffset* 是在此参数中指定的值
- `Offset from middle` –– 索引为 `floor`(*N*/2 + 1 − *colOffset*) 的输入列，其中 *N* 是输入列数，*colOffset* 是在此参数中指定的值

#### 依赖关系

要启用此参数，请将 **Ending column** 设置为 `Offset from middle` 或 `Offset from last`。

### **Diagonal span** — 对角线元素的跨度 `Range of elements`（默认） | `All elements` | `One element`

指定要覆盖的对角线元素的跨度。可以将参数设置为以下选项之一：

- `Range of elements` –– 覆盖输入对角线的一部分，必须在 **Starting element** 和 **Ending element** 参数中指定。
- `All elements` –– 覆盖整个输入对角线。
- `One element` –– 覆盖对角线中的一个元素，必须在 **Element** 参数中指定。

当将 **Diagonal span** 设置为 `One element` 或 `Range of elements` 时，需要通过设置 **Element** 或 **Starting element** 和 **Ending element** 参数进一步指定要覆盖的对角线元素。

#### 依赖关系

要启用此参数，请将 **Overwrite** 设置为 `Diagonal`。

### **Element/Starting element** — 元素或起始元素 `Index`（默认） | `First` | `Offset from last` | `Last` | `Offset from middle` | `Middle`

指定作为模块覆盖的子对角线中第一个元素的输入对角线元素。可以将此参数设置为以下选项之一：

- `Index` –– 第 *k* 个对角线元素，其中 *k* 是 **Element index** 或 **Starting element index** 参数的值
- `First` –– 输入第一行中的对角线元素
- `Offset from last` –– 索引为 *M* − *offset* 的行中的对角线元素，其中 *M* 是输入行数，*offset* 是在 **Element offset** 和 **Starting element offset** 参数中指定的值
- `Last` –– 输入最后一行中的对角线元素
- `Offset from middle` –– 索引为 `floor`(*M*/2 + 1 − *offset*) 的输入行中的对角线元素，其中 *M* 是输入行数，*offset* 是在 **Element offset** 和 **Starting element offset** 参数中指定的值
- `Middle` –– 索引为 `floor`(*M*/2 + 1) 的输入行中的对角线元素，其中 *M* 是输入行数

#### 依赖关系

要启用 **Element** 参数，请将 **Element span** 设置为 `One element`。

要启用 **Starting element** 参数，请将 **Element span** 设置为 `Range of elements`。

### **Element index/Starting element index** — 元素或起始元素索引 `2`（默认） | 正整数

将作为模块覆盖的子对角线第一个元素的输入对角线元素的索引指定为正整数。

#### 依赖关系

要启用 **Element index** 参数，请将 **Element** 设置为 `Index`。

要启用 **Starting element index** 参数，请将 **Starting element** 设置为 `Index`。

### **Ending element** — 结束元素 `Index`（默认） | `Offset from last` | `Last` | `Offset from middle` | `Middle`

指定作为模块覆盖的子对角线最后一个元素的输入对角线元素。可以将此参数设置为以下选项之一：

- `Index` –– 第 *k* 个对角线元素，其中 *k* 是 **Ending element index** 参数的值
- `Last` –– 输入最后一行中的对角线元素
- `Offset from last` –– 索引为 *M* − *offset* 的行中的对角线元素，其中 *M* 是输入行数，*offset* 是在 **Ending element offset** 参数中指定的值
- `Offset from middle` –– 索引为 `floor`(*M*/2 + 1 − *offset*) 的输入行中的对角线元素，其中 *M* 是输入行数，*offset* 是在 **Ending element offset** 参数中指定的值
- `Middle` –– 索引为 `floor`(*M*/2 + 1) 的输入行中的对角线元素，其中 *M* 是输入行数

#### 依赖关系

要启用此参数，请将 **Element span** 设置为 `Range of elements`，并将 **Starting element** 设置为除 `Last` 以外的任意选项。

### **Ending element index** — 结束元素索引 `4`（默认） | 正整数

将作为模块覆盖的子对角线最后一个元素的输入对角线元素的索引指定为正整数。

#### 依赖关系

要启用此参数，请将 **Ending element** 设置为 `Index`。

### **Element offset/Starting element offset** — 元素偏移或起始元素偏移 `2` | 整数（对于 offset from middle） | 非负整数（对于 offset from last）

指定作为模块覆盖的子对角线第一个元素的输入对角线元素的偏移。当将 **Starting element** 设置为：

- `Offset from middle` –– 将此参数的值指定为整数。
- `Offset from last` –– 将此参数的值指定为非负整数。

#### 依赖关系

要启用 **Element offset**，请将 **Element** 设置为 `Offset from middle` 或 `Offset from last`。

要启用 **Starting element offset**，请将 **Starting element** 设置为 `Offset from middle` 或 `Offset from last`。

### **Ending element offset** — 结束元素偏移 `4` | 非负整数

将作为模块覆盖的子对角线最后一个元素的输入对角线元素的偏移指定为非负整数。

#### 依赖关系

要启用此参数，请将 **Ending element** 设置为 `Offset from middle` 或 `Offset from last`。

## 所属库

DSP System Toolbox / Signal Management / Indexing / Matrix Operations DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

覆盖输入的子矩阵或子对角线

Overwrite Values 模块覆盖输入矩阵的连续子矩阵或子对角线。可以通过在模块参数中键入覆盖值，或通过附加输入端口提供覆盖值；这对于提供每个时间步都变化的覆盖值很有用。
