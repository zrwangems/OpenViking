---
type: simulink-block
title: 'Binary Vector Conversion'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'binaryvectorconversion'
documentation_source_path: 'ref/binaryvectorconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Vector Conversion

## 端口

### 输入

### **in** — 输入信号 标量 | 逻辑向量

输入信号，指定为标量或逻辑向量。

- 编码时，输入信号为标量。
- 解码时，输入信号为逻辑（布尔）向量。

**注意**

当从位流转换为标量值时，任何大于 1 的输入被视为逻辑 '1'。类似地，任何小于 0 的输入位被视为逻辑 '0'。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixdt(0,16)`
### 输出

### **out** — 输出信号 标量 | 逻辑向量

输出信号，指定为标量或逻辑向量。

- 编码时，输出信号为逻辑（布尔）向量。
- 解码时，输出信号为标量。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixdt(0,16)`

## 参数

### **Convert** — 转换操作类型 `Scalar to binary-coded vector`（默认）| `Binary-coded vector to scalar` | `Resize binary-coded vector` | `Reverse binary-coded vector`

转换类型，指定为以下之一：

- `Scalar to binary-coded vector` — 将标量输入信号编码为逻辑向量。
- `Binary-coded vector to scalar` — 将逻辑向量信号解码为标量。
- `Resize binary-coded vector` — 使用二进制补码方法在保留符号的同时调整逻辑向量的大小。
- `Reverse binary-coded vector` — 反转逻辑向量的位索引排列。

**注意**

当从位流转换为标量值时，我们将任何大于 1 的输入视为逻辑 '1'。类似地，如果输入位小于 0（即任何负数），则将其视为逻辑 '0'。

#### 编程使用

|  |
| --- |
| **模块参数：** `Convert` |
| **类型：** 字符向量 |
| **值：** `Scalar to binary-coded vector`| `Binary-coded vector to scalar`| `Resize binary-coded vector`| `Reverse binary-coded vector` |
| **默认值：** `Scalar to binary-coded vector` |

### **Logical vector encoding** — 逻辑向量编码方法 `Unipolar (magnitude)`（默认）| `Bipolar (2's complement)`

逻辑向量的编码方法，指定为 `Unipolar (magnitude)` 或 `Bipolar (2's complement)`。

#### 依赖关系

要启用此参数，请将 **Convert** 设置为 `Scalar to binary-coded vector`、`Binary-coded vector to scalar` 或 `Resize binary-coded vector`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Encoding` |
| **类型：** 字符向量 |
| **值：** `Unipolar (magnitude)`| `Bipolar (2's complement)` |
| **默认值：** `Unipolar (magnitude)` |

### **Input vector length** — 输入向量中的向量元素数量 `8`（默认）| 正实数标量

输入向量中的向量元素数量，指定为正实数标量。

默认情况下，最低有效位（LSB）是向量的第一个元素（索引 1）。但您也可以将最高有效位（MSB）设置为向量的第一个元素。

#### 依赖关系

要启用此参数，请将 **Convert** 设置为 `Binary-coded vector to scalar`、`Resize binary-coded vector` 或 `Reverse binary-coded vector`。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputLength` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `8` |

### **Output vector length** — 输出向量中的向量元素数量 `8`（默认）| 正实数标量

输出向量中的向量元素数量，指定为正实数标量。

默认情况下，最低有效位（LSB）是向量的第一个元素（索引 1）。但您也可以将最高有效位（MSB）设置为向量的第一个元素。

#### 依赖关系

要启用此参数，请将 **Convert** 设置为 `Scalar to binary-coded vector` 或 `Resize binary-coded vector`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputLength` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `8` |

### **输出数据类型** — 输出标量的数据类型 `double`（默认）| `Inherit: Inherit via back propagation` | `single` | `uint8` | `uint16` | `uint32` | `fixdt(0,16)`

输出标量的数据类型。您可以选择继承数据类型、直接指定，或表示为数据类型对象。

#### 依赖关系

要启用此参数，请将 **Convert** 设置为
`Binary-coded vector to scalar`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataType` |
| **类型：** 字符向量 |
| **值：** `Inherit: Inherit via back propagation`| `double`| `single`| `uint8`| `uint16`| `uint32`| `fixdt(0,16)` |
| **默认值：** `double` |

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

将标量整数转换为二进制逻辑向量，反之亦然

Binary Vector Conversion 模块对二进制编码向量进行编码、解码和操作。您可以使用二进制幅值或二进制补码将标量输入转换为逻辑（布尔）向量信号，反之亦然。您还可以调整二进制逻辑向量的大小并反转位索引排列。
