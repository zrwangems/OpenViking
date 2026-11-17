---
type: simulink-block
title: 'Normalization'
family: 'math-functions'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'normalization'
documentation_source_path: 'ref/normalization.html'
language: zh-CN
chinese_source: worker-translation
---

# Normalization

## 端口

### Input

### **Input** — 输入信号 标量 | 向量 | 矩阵 | *N* 维数组

将输入信号指定为标量、向量、矩阵或 *N* 维数组。在 `Squared 2-norm` 模式下，可以指定定点信号和浮点信号，但在 `2-norm` 模式下只能指定浮点信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes
### Output

### **Output** — 归一化输出 标量 | 向量 | 矩阵 | *N* 维数组

归一化输出，以标量、向量、矩阵或 *N* 维数组形式返回。输出始终与输入信号具有相同的大小、数据类型和复/实性。

有关模块如何对信号进行归一化的更多信息，请参阅算法。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Norm** — 归一化类型 `Squared 2-norm`（默认）| `2-norm`

将执行的归一化类型指定为以下之一：

- `Squared 2-norm` –– 支持浮点信号和定点信号。
- `2-norm` –– 仅支持浮点信号。

### **Normalization bias** — 归一化偏置 `1e-10`（默认）| 非负标量

将归一化偏置指定为非负标量。这是模块为避免除以零而在分母中加入的实数值 *b*。

**可调：** Yes

### **Normalize over** — 在其上执行归一化的维度 `Each column`（默认）| `Each row` | `Specified dimension`

将执行归一化的维度指定为以下之一：

- `Each column`
- `Each row`
- `Specified dimension` –– 使用 **Dimension** 参数指定维度。

### **Dimension** — 指定维度 `1`（默认）| 正整数

将执行归一化的维度的从 1 开始的值指定为正整数。此参数的值不能超过输入信号的维度数。

#### 依赖关系

要启用此参数，请将 **Normalize over** 参数设置为 `Specified dimension`。

### 数据类型选项卡

**注意**

仅当模块处于 squared 2-norm 模式时，此选项卡上的参数才适用于定点信号。有关在这种情况下如何使用乘积输出、累加器和输出数据类型的示意图，请参阅定点数据类型。

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

选中此参数时，模块将对其定点运算的结果进行饱和处理。清除此参数时，模块将对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — 乘积输出数据类型 `Inherit: Same as input`（默认）| `fixdt([],16,0)`

指定乘积输出数据类型。有关说明此模块中乘积输出数据类型用法的图示，请参阅定点数据类型和乘法数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **Product output** 参数。

有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

指定累加器数据类型。有关说明此模块中累加器数据类型用法的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as input` | `Inherit: Same as accumulator` | `fixdt([],16,0)`

指定输出数据类型。有关说明此模块中输出数据类型用法的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 继承数据类型的规则，例如 `Inherit: Same as input`
- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置 **Output** 参数。

有关更多信息，请参阅控制信号的数据类型 (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认）| 标量

指定模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动缩放

### **Output Maximum** — 输出最大值 `[]`（默认）| 标量

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅指定信号范围 (Simulink)）
- 定点数据类型的自动缩放

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Math Functions / Math Operations

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

**在 R2006a 之前引入**

## 描述

沿行、列或指定维度执行向量归一化

Normalization 模块使用 `Squared 2-norm` 或 `2-norm` 方法，独立地对输入的每一行、每一列或指定维度的每个向量进行归一化。

有关模块如何对信号进行归一化的更多信息，请参阅算法。
