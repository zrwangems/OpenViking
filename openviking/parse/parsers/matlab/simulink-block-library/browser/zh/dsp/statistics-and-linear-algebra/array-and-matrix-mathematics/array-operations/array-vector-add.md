---
type: simulink-block
title: 'Array-Vector Add'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Array Operations'
documentation_page: 'arrayvectoradd'
documentation_source_path: 'ref/arrayvectoradd.html'
language: zh-CN
chinese_source: worker-translation
---

# Array-Vector Add

## 端口

### 输入

### **A** — 输入数组 scalar | vector | matrix | *N*-D array

将输入数组指定为 scalar、vector、matrix 或 *N*-D array。

如果输入为 fixed point，则它必须是有符号整数或具有 power-of-two slope 和 zero bias 的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

### **V** — 要相加的向量 vector

将要相加的向量 *V* 指定为长度等于输入 *A* 中指定维度长度的向量。

#### 依赖关系

要启用此参数，请将 **Vector (V) source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes
### 输出

### **Output** — 输出 scalar | vector | matrix | *N*-D array

Array-Vector Add 模块的输出，返回为 scalar、vector、matrix 或 *N*-D array。输出始终与输入信号具有相同的大小、数据类型和复数性。

有关该模块如何计算输出的详细信息，请参阅 Algorithms。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Add along dimension** — 要沿其相加的维度 `1`（默认）| positive integer

将输入数组 *A* 与向量 *V* 的元素沿其相加的维度指定为正整数。此参数的值必须小于或等于输入 *A* 的维度数。

### **Vector (V) source** — 向量 *V* 的来源 `Input port`（默认）| `Dialog parameter`

将向量 *V* 的来源指定为以下之一：

- `Input port` –– 使用输入端口 **V** 来指定向量。
- `Dialog parameter` –– 使用 **Vector (V)** 对话框参数来指定向量。

### **Vector (V)** — 要相加的向量 `[0.5 0.25]`（默认）| vector

将要相加的向量 *V* 指定为长度等于输入 *A* 中指定维度长度的向量。

#### 依赖关系

要启用此参数，请将 **Vector (V) source** 参数设置为 `Dialog parameter`。

### 数据类型选项卡

**注意**

浮点继承优先于此选项卡上定义的数据类型设置。当输入为浮点时，该模块会忽略这些设置，并且所有内部数据类型均为浮点。

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅 Rounding Modes。

**注意**

当同时满足以下两个条件时，**Rounding mode** 和 **Saturate on integer overflow** 设置对数值结果没有影响：

- **Accumulator** 为
  `Inherit: Inherit via internal rule`
- **Output** 为 `Inherit: Same as accumulator`

使用这些数据类型设置时，该模块实际上以全精度模式运行。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

选中此参数时，该模块会对其定点运算的结果进行饱和处理。清除此参数时，该模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅 overflow mode for fixed-point operations。

### **Vector (V)** — 向量数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16,0)`

使用此参数指定向量 *V* 元素的字长和小数长度。您可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same word length as input`。
- 计算结果为有效数据类型的表达式，例如，
  `fixdt(1,16,0)`。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当在模块对话框的 **Main** 选项卡上为 **Vector (V) source** 参数选择 `Dialog parameter` 时，**Data Types** 选项卡上的 **Vector (V)** 参数才可见。
当向量通过模块的输入端口传入时，其元素的数据类型和定标继承自驱动模块。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `fixdt([],16,0)`

指定累加器数据类型。有关此模块中累加器数据类型用法的图示，请参阅 Fixed-Point Data Types。您可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 继承数据类型的规则，例如，
  `Inherit: Same as first input`。
- 计算结果为有效数据类型的表达式，例如，
  `fixdt(1,16,0)`。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Inherit same as accumulator`（默认）| `Inherit: Inherit same as first input` | `fixdt([],16,0)`

指定输出数据类型。有关此模块中输出数据类型用法的图示，请参阅 Fixed-Point Data Types。您可以将此参数设置为：

- 继承数据类型的规则，例如，
  `Inherit: Same as accumulator`
- 继承数据类型的规则，例如，
  `Inherit: Same as first input`
- 计算结果为有效数据类型的表达式，例如，
  `fixdt([],16,0)`。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认）| scalar

指定模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]`（默认）| scalar

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

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

沿指定维度将向量与数组相加

Array-Vector Add 模块将输入向量 *V* 中的值加到 *N* 维输入数组 *A* 的指定维度。Array-Vector Add 模块将 *V* 的每个元素加到 *A* 的指定维度上的对应元素。

有关该模块如何计算输出的详细信息，请参阅 Algorithms。
