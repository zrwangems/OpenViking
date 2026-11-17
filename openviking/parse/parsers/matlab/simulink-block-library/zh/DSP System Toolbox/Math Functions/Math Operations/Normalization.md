---
type: simulink-block
title: 'Normalization'
family: 'dsp'
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
```yaml
ports:
- name: Input
  summary: 输入信号 标量 | 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Output
  summary: 归一化输出 标量 | 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### 输入

### **Input** — 输入信号 标量 | 向量 | 矩阵 | *N* 维数组

将输入信号指定为标量、向量、矩阵或 *N* 维数组。在 `Squared 2-norm` 模式下可以指定定点信号和浮点信号，但在 `2-norm` 模式下只能指定浮点信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Output** — 归一化输出 标量 | 向量 | 矩阵 | *N* 维数组

归一化输出，以标量、向量、矩阵或 *N* 维数组形式返回。输出始终与输入信号具有相同的大小、数据类型和复数特性。

有关模块如何对信号进行归一化的详细信息，请参阅算法。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Norm
  summary: 归一化类型 Squared 2-norm（默认）| 2-norm
  group: 主选项卡
- name: Normalization bias
  summary: 归一化偏置 1e-10（默认）| 非负标量
  group: 主选项卡
- name: Normalize over
  summary: 归一化所沿的维度 Each column（默认）| Each row | Specified dimension
  group: 主选项卡
- name: Dimension
  summary: 指定维度 1（默认）| 正整数
  group: 主选项卡
- name: Rounding mode
  summary: 舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 整数溢出时饱和 off（默认）| on
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Same as input（默认）| fixdt([],16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Same as product output（默认）| Inherit: Same as input | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as product output（默认）| Inherit: Same as input | Inherit: Same as accumulator | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 输出最小值 []（默认）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 输出最大值 []（默认）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Norm** — 归一化类型 `Squared 2-norm`（默认）| `2-norm`

将执行的归一化类型指定为以下之一：

- `Squared 2-norm` —— 同时支持浮点信号和定点信号。
- `2-norm` —— 仅支持浮点信号。

### **Normalization bias** — 归一化偏置 `1e-10`（默认）| 非负标量

将归一化偏置指定为非负标量。这是模块在分母中添加的实数值 *b*，用于避免除以零。

**可调：** 是

### **Normalize over** — 归一化所沿的维度 `Each column`（默认）| `Each row` | `Specified dimension`

将归一化所沿的维度指定为以下之一：

- `Each column`
- `Each row`
- `Specified dimension` —— 使用 **Dimension** 参数指定维度。

### **Dimension** — 指定维度 `1`（默认）| 正整数

将归一化所沿维度的一基值指定为正整数。此参数的值不能超过输入信号的维度数。

#### 依赖关系

要启用此参数，请将 **Normalize over** 参数设置为 `Specified dimension`。

### 数据类型选项卡

**注意**

当模块处于 squared 2-norm 模式时，此选项卡上的参数仅适用于定点信号。有关此情况下乘积输出、累加器和输出数据类型的使用方式示意图，请参阅定点数据类型。

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

选中此参数时，模块对其定点运算的结果进行饱和处理。清除此参数时，模块对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — 乘积输出数据类型 `Inherit: Same as input`（默认）| `fixdt([],16,0)`

指定乘积输出数据类型。有关此模块中乘积输出数据类型的使用方式示意图，请参阅定点数据类型和乘法数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可以帮助您设置 **Product output** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

指定累加器数据类型。有关此模块中累加器数据类型的使用方式示意图，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 继承数据类型的规则，例如 `Inherit: Same as input`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可以帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as input` | `Inherit: Same as accumulator` | `fixdt([],16,0)`

指定输出数据类型。有关此模块中输出数据类型的使用方式示意图，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as product output`
- 继承数据类型的规则，例如 `Inherit: Same as input`
- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 求值为有效数据类型的表达式，例如 `fixdt([],16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可以帮助您设置 **Output** 参数。

有关更多信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认）| 标量

指定模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]`（默认）| 标量

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

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

**在 R2006a 之前推出**

## 描述

沿行、列或指定维度执行向量归一化

Normalization 模块使用 `Squared 2-norm` 或 `2-norm` 方法独立地对输入的每一行、每一列或指定维度的向量进行归一化。

有关模块如何对信号进行归一化的详细信息，请参阅算法。
