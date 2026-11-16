---
type: simulink-block
title: 'Identity Matrix'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Matrix Operations'
documentation_page: 'identitymatrix'
documentation_source_path: 'slref/identitymatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Identity Matrix

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，用于确定输出矩阵的维度，指定为标量、向量或矩阵。当输入信号是 *M*×*N* 矩阵时，该模块生成 *M*×*N* 矩阵输出，其采样周期与输入相同。输入矩阵中的值将被忽略。

#### 依赖关系

要启用此端口，请选中 **从输入端口继承输出端口属性** 复选框。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **Port\_1** — 单位矩阵 标量 | 向量 | 矩阵

单位矩阵，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **从输入端口继承输出端口属性** — 输出端口从输入端口继承属性的选项 off（默认） | on

选中此复选框，使输出端口从输入端口继承其维度、采样周期和数据类型。否则，清除此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `InheritOutputPortAttributes` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

### **输出维度** — 输出矩阵的大小 `5`（默认） | 标量 | 二元素向量

输出矩阵中的行数和列数。您可以指定：

- 正整数标量 *M*，用于创建 *M*×*M* 方阵输出。
- 正整数向量 [*M* *N*]，用于创建 *M*×*N* 输出。

#### 依赖关系

要启用此参数，请清除 **从输入端口继承输出端口属性** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputDimensions` |
| **类型：** 字符向量 |
| **值：** 标量 | 二元素向量 |
| **默认值：** `'5'` |

### **输出数据类型** — 输出数据类型 `double`（默认） | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

指定此模块的输出数据类型。您可以选择以下选项之一：

- 继承数据类型的规则，例如 `Inherit: Inherit via back propagation`。当您选择此选项时，输出数据类型和定标与下一个下游模块匹配。
- 内置数据类型，例如 `double`。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关设置数据类型参数的帮助，请通过单击 **Show data type assistant** 按钮显示 **Data Type Assistant**。

有关详细信息，请参阅 Control Data Types of Signals。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | | `'fixdt(1,16,0)'` | `'<data type expression>'` |
| **默认值**：`'double'` |

### **模式** — 数据类型模式 `Inherit`（默认） | `Built in` | `Fixed point` | `Expression`

选择希望如何指定 **输出数据类型** 的数据类型属性。您可以选择：

- `Inherit` — 指定继承数据类型的规则，例如 `Inherit: Same as input`。
- `Built in` — 指定内置数据类型，例如 `double`。
- `Fixed point` — 指定数据类型的定点属性。
- `Expression` — 指定求值为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **符号性** — 定点数据的符号性 `Signed`（默认） | `Unsigned`

指定定点数据是有符号还是无符号。`Signed` 数据可以表示正值和负值，但 `Unsigned` 数据仅表示正值。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **定标** — 定点数据的定标方法 `Best precision`（默认） | `Binary point`

指定定点数据的定标方法，以避免溢出情况并最小化量化误差。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`

### **字长** — 保存量化整数的字长（以位为单位） `16`（默认） | 从 2 到 65,535 的整数

将保存量化整数的字长（以位为单位）指定为从 2 到 65,535 的正整数。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`。

### **小数长度** — 定点数据类型的小数长度 `0`（默认） | 整数标量

将定点数据类型的小数长度指定为正整数或负整数标量。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Fixed point`，并将 **定标** 设置为 `Binary point`。

### **数据类型覆盖** — 数据类型覆盖模式 `Inherit`（默认） | `Off`

选择此信号的数据类型覆盖模式。您可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型。

#### 依赖关系

要启用此参数，请将 **模式** 设置为 `Built in` 或 `Fixed point`。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **采样时间** — 输出采样周期 `1`（默认） | 标量

输出的离散采样周期，指定为实数值标量。

#### 依赖关系

要启用此参数，请清除 **从输入端口继承输出端口属性** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 标量或向量 |
| **默认值：** `'1'` |

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

**在 R2021b 中引入**

### R2022a：Identity Matrix 模块已添加到 Simulink Matrix Operations 库

Identity Matrix 模块已从 **DSP System Toolbox** > **Math Functions** > **Matrices and Linear** > **Matrix Operations** 库中移除。对于等效功能，请使用 **Simulink** > **Matrix Operations** 库中的 Identity Matrix 模块。所有现有模型继续正常工作。

## 描述

生成主对角线上为 1、其他位置为零值的矩阵

Identity Matrix 模块输出单位矩阵，类似于 MATLAB® `eye` 函数。该模块生成主对角线上为 1、其他位置为 0 的方阵或矩形矩阵。
