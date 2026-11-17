---
type: simulink-block
title: 'Array-Vector Divide'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'arrayvectordivide'
documentation_source_path: 'ref/arrayvectordivide.html'
language: zh-CN
chinese_source: worker-translation
---

# Array-Vector Divide

## 端口

### 输入

### **A** — 输入数组 标量 | 向量 | 矩阵 | *N* 维数组

将输入数组指定为标量、向量、矩阵或 *N* 维数组。

如果输入为定点，则它必须是带符号整数，或具有 2 的幂斜率且零偏置的带符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **V** — 要用于相除的向量 向量

将用于相除的向量 *V* 指定为长度等于输入 *A* 中指定维度长度的向量。

#### 依赖关系

要启用此参数，请将 **向量 (V) 源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### 输出

### **Output** — 输出 标量 | 向量 | 矩阵 | *N* 维数组

Array-Vector Divide 模块的输出，返回为标量、向量、矩阵或 *N* 维数组。输出始终与输入信号具有相同的大小、数据类型和复数性。

有关模块如何计算输出的详细信息，请参阅算法。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

## 参数

### 主选项卡

### **沿维度相除** — 沿其进行除法的维度 `1` (默认) | 正整数

指定沿其将输入数组 *A* 除以向量 *V* 的元素的维度，取值为正整数。此参数的值必须小于或等于输入 *A* 的维度数。

### **向量 (V) 源** — 向量 *V* 的源 `Input port` (默认) | `Dialog parameter`

将向量 *V* 的源指定为以下项之一：

- `Input port` –– 使用输入端口 **V** 指定向量。
- `Dialog parameter` –– 使用 **向量 (V)** 对话框参数指定向量。

### **向量 (V)** — 要用于相除的向量 `[0.5 0.25]` (默认) | 向量

将用于相除的向量 *V* 指定为长度等于输入 *A* 中指定维度长度的向量。

#### 依赖关系

仅当您为 **向量 (V) 源** 参数选择 `Dialog parameter` 时，此参数才可见。

### 数据类型选项卡

**注意**

浮点继承优先于此选项卡上定义的数据类型设置。当输入为浮点时，模块会忽略这些设置，所有内部数据类型均为浮点。

### **舍入模式** — 舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下项之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 整数溢出时饱和 `off` (默认) | `on`

选中此参数时，模块会对其定点运算的结果进行饱和处理。清除此参数时，模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **向量 (V)** — 向量数据类型 `Inherit: Same word length as input` (默认) | `fixdt(1,16,0)`

使用此参数指定向量 *V* 元素的字长和小数长度。您可以将此参数设置为：

- 继承数据类型的规则，例如，`Inherit: Same word length as input`
- 计算结果为有效数据类型的表达式，例如，`fixdt(1,16,0)`

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **向量 (V)** 数据类型参数。

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

**注意**

当您通过模块的输入端口指定向量时，其元素的数据类型和定标继承自驱动模块。

#### 依赖关系

仅当您在模块掩码的 **主**选项卡上为 **向量 (V) 源** 参数选择 `Dialog parameter` 时，**数据类型**选项卡上的 **向量 (V)** 参数才可见。

### **输出** — 输出数据类型 `Inherit: Same as first input` (默认) | `fixdt([],16,0)`

指定输出数据类型。有关说明此模块中输出数据类型用法的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如，`Inherit: Same as first input`
- 计算结果为有效数据类型的表达式，例如，`fixdt([],16,0)`

点击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **输出** 参数。

有关详细信息，请参阅控制信号的数据类型 (Simulink)。

### **输出最小值** — 输出最小值 `[]` (默认) | 标量

指定模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

### **输出最大值** — 输出最大值 `[]` (默认) | 标量

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动定标

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2007b 中引入**

## 描述

沿指定维度将数组除以向量

Array-Vector Divide 模块将 *N* 维输入数组 *A* 的指定维度中的值除以输入向量 *V* 中的值。Array-Vector Divide 模块将 *V* 的每个元素除以 *A* 的该维度上的对应元素。

有关模块如何计算输出的详细信息，请参阅算法。
