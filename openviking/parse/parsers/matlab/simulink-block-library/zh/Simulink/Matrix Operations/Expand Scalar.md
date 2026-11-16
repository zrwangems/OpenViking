---
type: simulink-block
title: 'Expand Scalar'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'expandscalar'
documentation_source_path: 'slref/expandscalar.html'
language: zh-CN
chinese_source: worker-translation
---

# Expand Scalar

## 端口

### 输出

### **Port\_1** — 标量扩展矩阵 标量 | 向量 | 矩阵

标量扩展矩阵，以标量、向量或矩阵形式返回。

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `bus` | `Boolean` | `fixed point`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上，在**准备**库中，选择**属性检查器**。

### **元素值** — 矩阵元素值 `1` (默认) | 标量

为扩展后的矩阵指定矩阵元素值，以标量表示。元素值可以是 `struct`。

**可调：** Yes

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ElementValue` |
| **值：** | 1 (默认) | 标量 |
| **数据类型：** | `char` |

### **输出维度** — 输出矩阵的维度 `5` (默认) | 标量 | 二元向量

以标量或向量形式指定输出矩阵的维度。

- 正整数标量会创建无方向向量。
- 二维向量会创建有方向向量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputDimensions` |
| **值：** | `'5'` (默认) | 标量 | 二元向量 |
| **数据类型：** | `char` |

### **输出数据类型** — 输出数据类型 `double` (默认) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

指定此模块的输出数据类型。您可以选择以下选项之一：

- 继承数据类型的规则，例如 `Inherit: Inherit via back propagation`。选择此选项时，输出数据类型和缩放与下一个下游模块匹配。
- 内置数据类型，例如 `double`。
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关设置数据类型参数的帮助，请通过点击 **显示数据类型助手** 按钮 来显示 **数据类型助手**。

有关详细信息，请参阅控制信号的数据类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'double'` (默认) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>` |
| **数据类型：** | `char` |

### **模式** — 数据类型模式 `Inherit` (默认) | `Built in` | `Fixed point` | `Expression`

选择希望如何指定 **输出数据类型** 的数据类型属性。

- `Inherit` — 指定用于继承数据类型的规则，例如 `Inherit: Same as input`。
- `Built in`— 指定内置数据类型，例如 `double`。
- `Fixed point` — 指定数据类型的定点属性。
- `Expression` — 指定计算结果为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关详细信息，请参阅使用数据类型助手指定数据类型。

### **符号性** — 定点数据的符号性 `Signed` (默认) | `Unsigned`

指定定点数据是有符号还是无符号。`Signed` 数据可以表示正值和负值。`Unsigned` 数据仅表示正值。有关详细信息，请参阅使用数据类型助手指定数据类型。

### **缩放** — 定点数据的缩放方法 `Best precision` (默认) | `Binary point`

指定定点数据的缩放方法，以避免溢出情况并最小化量化误差。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`。

### **字长** — 保存量化整数的字长（以位为单位） `16` (默认) | 2 到 65,535 的整数

以 2 到 65,535 之间的正整数指定用于保存量化整数的字长（以位为单位）。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`。

### **小数长度** — 定点数据类型的小数长度 `0` (默认) | 整数标量

以正整数或负整数标量指定定点数据类型的小数长度。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`，并将 **缩放** 设置为 `Binary point`。

### **数据类型覆盖** — 数据类型覆盖模式 `Inherit` (默认) | `Off`

选择此信号的数据类型覆盖模式。您可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Built in` 或 `Fixed point`。有关详细信息，请参阅使用数据类型助手指定数据类型。

### **采样时间** — 输出采样周期 `1` (默认) | 标量

以实数值标量指定输出的离散采样周期。

#### 依赖关系

要启用此参数，请清除 **从输入端口继承输出端口属性** 复选框。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `'1'` (默认) | 标量 |
| **数据类型：** | `char` |

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b: Expand Scalar 模块支持 `struct` 扩展

Expand Scalar 模块现在支持使用 Simulink 总线数据类型进行 MATLAB® `struct` 扩展。

## 描述

使用标量扩展从标量创建矩阵

Expand Scalar 模块输出标量扩展后的矩阵，其中矩阵的每个元素都具有相同的值。
