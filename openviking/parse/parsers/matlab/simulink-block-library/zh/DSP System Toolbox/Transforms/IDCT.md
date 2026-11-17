---
type: simulink-block
title: 'IDCT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'idct'
documentation_source_path: 'ref/idct.html'
language: zh-CN
chinese_source: worker-translation
---

# IDCT

## 端口
```yaml
ports:
- name: Input 1
  summary: 输入信号 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point | bus
- name: Output 1
  summary: IDCT 输出 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point | bus
```

### 输入

### **Input 1** — 输入信号 向量 | 矩阵 | *N* 维数组

将输入信号指定为向量、矩阵或 *N* 维数组。

对于所有 *N* 维输入数组，该模块沿第一个维度计算 IDCT。第一个维度的大小（帧大小）必须是 2 的幂。若要处理其他帧大小，请使用 Pad 模块将帧大小填充或截断为 2 的幂长度。

当输入为 *M*×*N* 矩阵时，该模块将每个输入列视为一个独立通道，其中包含 *M* 个连续采样。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point` | `bus`
**复数支持：** 是
### 输出

### **Output 1** — IDCT 输出 向量 | 矩阵 | *N* 维数组

该模块将输入信号的 IDCT 输出为向量、矩阵或 *N* 维数组。

当该模块输出 *M*×*N* 矩阵时，第 *l* 列包含对应输入列的长度为 *M* 的 IDCT。

y(m,l)=∑k=1Mw(k)u(k,l)cosπ(2m−1)(k−1)2M,m=1,...,M

其中

w(k)={1M2M,,k=12≤k≤M

当输入为定点（有符号和无符号）时，输出为有符号定点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point` | `bus`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Sine and cosine computation
  summary: 正弦和余弦计算 Table lookup（默认）| Trigonometric fcn
  group: 主选项卡
- name: Rounding mode
  summary: 舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 整数溢出时饱和 off（默认）| on
  group: 数据类型选项卡
- name: Sine table
  summary: '正弦表 Inherit: Same word length as input（默认）| fixdt(1,16)'
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt(1,16,0)'
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

### **Sine and cosine computation** — 正弦和余弦计算 `Table lookup`（默认）| `Trigonometric fcn`

将该模块设置为通过在速度优化的表中查找正弦和余弦值（`Table lookup`）来计算正弦和余弦，或通过调用正弦和余弦函数（`Trigonometric fcn`）来计算。

要计算正弦和余弦，请将该参数设置为以下值之一：

- `Table lookup` —— 该模块在仿真开始前计算并存储三角函数值，并在仿真期间检索这些值。当您从该模块生成代码时，运行生成代码的处理器会将模块计算的三角函数值存储在速度优化的表中，并在代码执行期间检索这些值。

  该模块运行速度要快得多，但需要额外的内存来存储预计算的三角函数值。
- `Trigonometric fcn` —— 该模块在仿真期间计算正弦和余弦值。当您从该模块生成代码时，运行生成代码的处理器会在代码运行时计算正弦和余弦值。

  该模块运行速度较慢，但不需要额外的数据内存。对于代码生成，该模块需要一个支持库来模拟三角函数，从而增加生成代码的大小。

### 数据类型选项卡

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。正弦表值不遵循此参数；它们始终舍入到 `Nearest`。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

当您选中此参数时，该模块对其定点运算的结果进行饱和处理。当您清除此参数时，该模块对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

**注意**

当满足以下条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **Sine table** — 正弦表 `Inherit: Same word length as input`（默认）| `fixdt(1,16)`

选择如何指定正弦表值的字长。正弦表值的小数长度始终等于字长减一。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16)`

正弦表值不遵循 **Rounding mode** 和 **Saturate on integer overflow** 参数。该模块始终将正弦表值饱和并舍入到 `Nearest`。

### **Product output** — 乘积输出 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出数据类型。有关说明此模块中乘积输出数据类型使用的图示，请参阅定点数据类型和乘法数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器数据类型。有关说明此模块中累加器数据类型使用的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt(1,16,0)`

指定输出数据类型。有关说明此模块中输出数据类型使用的图示，请参阅定点数据类型。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。

  当您选择 `Inherit: Inherit via internal rule` 时，该模块会自动计算输出字长和小数长度。内部规则首先使用以下公式计算理想的输出字长和小数长度：

  WLideal output=WLinput+floor(log2(DCT length−1))+1

  FLideal output=FLinput

  使用这些理想结果，内部规则随后选择适合您硬件的字长和小数长度。有关详细信息，请参阅 Inherit via Internal Rule。
- 求值为有效数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 输出最小值 `[]`（默认）| 标量

指定该模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]`（默认）| 标量

指定该模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
## 所属库

DSP System Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `bus` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

为符合嵌入式系统编码标准，生成的代码是非递归的。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

输入的逆离散余弦变换（IDCT）

IDCT 模块计算输入信号 *u* 的逆离散余弦变换（IDCT）。当输入为 *M*×*N* 矩阵时，该模块计算矩阵中每个通道的 IDCT。

以下是等效的 MATLAB® 代码。

```
y = idct(u)
```
