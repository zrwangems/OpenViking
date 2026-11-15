---
type: simulink-block
title: 'String Find'
family: string
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'String'
documentation_page: 'stringfind'
---

# String Find

Return index of first occurrence of pattern string

## 中文

返回模式字符串第一次出现的索引

### 所属库

Simulink / String

### 描述

String Find 模块返回模式字符串 **sub** 在文本字符串 **str** 中第一次出现的索引。

### 端口

#### 输入

#### **str** — 在其中查找模式的字符串 标量

要在其中查找模式 (`sub`) 的字符串，指定为标量。

**数据类型:** `string`

#### **sub** — 模式 标量

要在字符串(`str`)中找到的模式，指定为标量。

**数据类型:** `string`
#### 输出

#### **idx** — 找到的模式的位置索引 标量

找到的模式的位置索引，指定为正整数标量。

- 如果模块没有找到模式，它将返回 `-1`。
- 如果 **sub** 参数为空(`""`)，则该模块返回 `1`，表示它与搜索字符串的开头匹配。

**数据类型:** `int8` | `int16` | `int32`

### 参数

#### **输出数据类型** — 输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **int8** | **int16** | **int32** | `<data type expression>`

输出数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

当您选择继承的选项时，模块的行为如下所示：

- **继承: 从内部规则继承** - Simulink® 在考虑嵌入式目标硬件的属性的同时，会选择相应的数据类型来平衡数值准确性、性能和生成的代码大小。
- **继承: 通过反向传播继承** - 使用驱动模块的数据类型。

点击**显示数据类型助手**按钮  以显示**数据类型助手**，帮助您设置数据类型属性。有关详细信息，请参阅 。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'int16'` | `'int32'` | *`<data type expression>`* |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **模式** — 数据类型的类别 `Inherit` (默认) | `Built in` | `Expression`

数据类型的类别，指定为 `Inherit`、`Built in` 或 `Expression`。有关使用此参数的详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

点击**显示数据类型助手**按钮将启用此参数。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2018a 中推出**

## Libraries

Simulink / String

## Description

The String Find block returns the index of the first occurrence of the
pattern string **sub** in the text string **str**.

## Ports

### Input

### **str** — String in which to find pattern scalar

String in which to find pattern (`sub`), specified as
a scalar.

**Data Types:** `string`

### **sub** — Pattern scalar

Pattern to be found in string (`str`), specified as a
scalar.

**Data Types:** `string`
### Output

### **idx** — Position index of found pattern scalar

Position index of the found pattern, specified as a positive integer
scalar.

- If the block does not find the pattern, it returns
  `-1`.
- If the **sub** parameter is empty
  (`""`), the block returns
  `1`, indicating that it matched the
  beginning of the searched string.

**Data Types:** `int8` | `int16` | `int32`

## Parameters

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `int8` | `int16` | `int32` | `<data type expression>`

Output data type. The type can be inherited, specified directly, or
expressed as a data type object such as
`Simulink.NumericType`.

When you select an inherited option, the block exhibits these
behaviors:

- `Inherit: Inherit via internal rule` —
  Simulink® chooses a data type to balance numerical accuracy,
  performance, and generated code size, while taking into account the
  properties of the embedded target hardware.
- `Inherit: Inherit via back propagation` —
  Use data type of the driving block.

Click the **Show data type assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. See
Specify Data Types Using Data Type Assistant for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'int8'` | `'int16'` | `'int32'` | *`<data type expression>`* |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Mode** — Category of data type `Inherit` (default) | `Built in` | `Expression`

Category of data type, specified as `Inherit`,
`Built in`, or `Expression`. For more
information on using this parameter, see Specify Data Types Using Data Type Assistant.

#### Dependency

Clicking the **Show data type assistant** button
enables this parameter.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `integer` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**
