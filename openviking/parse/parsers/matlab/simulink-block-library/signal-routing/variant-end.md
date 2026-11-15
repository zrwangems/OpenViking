---
type: simulink-block
title: 'Variant End'
family: signal-routing
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'variantend'
---

# Variant End

Define end of bounded region

## 中文

定义有界区域的终点

### 库

Simulink / Signal Routing

### 描述

Variant End 模块定义有界区域的终点，使您能够限制变体条件传播，而无需引入层级。使用 Variant Start 模块定义有界区域的起点。对于每个 Variant Start 模块，都有一个唯一对应的 Variant End 模块。当您在 Variant Start 模块上指定变体条件时，对应的 Variant End 模块会在编译时基于唯一的 **Variant Start End Tag** 继承这些条件和其他参数。

### 端口

#### 输入

#### **Port\_1** — 输入分支 标量 | 向量 | 矩阵

与对应 Variant Start 模块一起定义有界区域终点的输入分支。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

#### **Port\_N** — 与第 *N* 个分支关联的输入端口 标量 | 向量 | 矩阵

与第 *N* 个分支关联的输入端口，该分支与对应 Variant Start 模块一起定义有界区域终点。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

来自活动变体的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

#### **Variant Start End Tag** — 有界区域的唯一标识符 `A`（默认） | 有效的 MATLAB® 标识符

用于标识组成有界区域的正确 Variant Start 和 Variant End 对的唯一标识符，指定为有效的 MATLAB 标识符。有效的 MATLAB 标识符是由字母数字（A–Z、a–z、0–9）和下划线组成的 character vector，其中第一个字符必须是字母，并且 character vector 的长度小于或等于 `namelengthmax`。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariantStartEndTag` |
| **类型：** character vector |
| **取值：** `'A'` | 有效的 MATLAB 标识符 |
| **默认值：** `'A'` |

#### **Variant Paired Block** — 用于高亮配对的 Variant Start 模块的选项 `off`（默认） | `on`

选择此参数可高亮显示与 Variant End 具有相同 **Variant Start End Tag** 的 Variant Start。如果存在多个具有相同 **Variant Start End Tag** 的 Variant Start 模块，则高亮显示找到的第一个模块。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariantPairedBlock` |
| **类型：** character vector |
| **取值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史

**在 R2024a 中引入**

## Libraries

Simulink / Signal Routing

## Description

The Variant End block defines the end of the bounded region that allows
you to limit variant condition propagation without introducing a level of hierarchy. Define
the start of the bounded region by using the Variant Start block. For every
Variant Start block, there is a single corresponding Variant
End block. When you specify the variant conditions on the Variant
Start block, the corresponding Variant End block inherits the
conditions and other parameters based on the unique **Variant Start End
Tag** on compile.

## Ports

### Input

### **Port\_1** — Input branch scalar | vector | matrix

Input branch that defines the end of the bounded region with the
corresponding Variant Start block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Port\_N** — Input port associated with *N*th branch scalar | vector | matrix

Input port associated with the *N*th branch that defines
the end of the bounded region with the corresponding Variant
Start block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Output signal from the active variant.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

### **Variant Start End Tag** — Unique identifier of bounded region `A` (default) | valid MATLAB® identifier

Unique identifier to identify the correct Variant Start and
Variant End pair that form the bounded region, specified as a
valid MATLAB identifier. A valid MATLAB identifier is a character vector of alphanumerics (A–Z, a–z, 0–9)
and underscores, such that the first character is a letter and the length of the
character vector is less than or equal to `namelengthmax`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantStartEndTag` |
| **Type:** character vector |
| **Values:** `'A'` | valid MATLAB identifier |
| **Default:** `'A'` |

### **Variant Paired Block** — Option to highlight paired Variant Start block `off` (default) | `on`

Select this parameter to highlight the Variant Start with the
same **Variant Start End Tag** as the Variant End.
If there are multiple Variant Start blocks with the same
**Variant Start End Tag**, then the first block found is
highlighted.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VariantPairedBlock` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024a**
