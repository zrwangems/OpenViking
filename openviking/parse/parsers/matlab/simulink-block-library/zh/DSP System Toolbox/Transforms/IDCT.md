---
type: simulink-block
title: 'IDCT'
family: 'transforms'
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

### 输入

### **Input 1** — 输入信号向量 | 矩阵 | *N*-D 数组

将输入信号指定为向量、矩阵或 *N*-D 数组。

对于所有 *N*-D 输入数组，该模块沿第一个维度计算 IDCT。第一个维度的大小（帧大小）必须是 2 的幂。要处理其他帧大小，请使用 Pad 模块将帧大小填充或截断为 2 的幂长度。

当输入是 *M*×*N* 矩阵时，该模块将每个输入列视为一个独立通道，其中包含 *M* 个连续样本。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point` | `bus`
**复数支持:** 是

### 输出

### **Output 1** — IDCT 输出向量 | 矩阵 | *N*-D 数组

该模块将输入信号的 IDCT 输出为向量、矩阵或 *N*-D 数组。

当该模块输出 *M*×*N* 矩阵时，第 *l* 列包含对应输入列的长度为 *M* 的 IDCT。

y(m,l)=∑k=1Mw(k)u(k,l)cosπ(2m−1)(k−1)2M,m=1,...,M

其中

w(k)={1M2M,,k=12≤k≤M

当输入为定点（有符号和无符号）时，输出为有符号定点。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point` | `bus`
**复数支持:** 是

## 参数

### 主选项卡

### **正弦和余弦计算** — 正弦和余弦计算 `Table lookup`（默认） | `Trigonometric fcn`

设置该模块通过以下方式计算正弦和余弦：在速度优化的表中查找正弦和余弦值（`Table lookup`），或进行正弦和余弦函数调用（`Trigonometric fcn`）。

要计算正弦和余弦，请将该参数设置为以下值之一：

- `Table lookup` –– 该模块
  在仿真开始前计算并存储三角函数值，并在仿真期间检索它们。当您从该模块生成代码时，运行生成代码的处理器将模块计算出的三角函数值存储在速度优化的表中，并在代码执行期间检索这些值。

  该模块运行速度快得多，但需要额外内存来存储预计算的三角函数值。
- `Trigonometric fcn` –– 该模块
  在仿真期间计算正弦和余弦值。当您从该模块生成代码时，运行生成代码的处理器在代码运行时计算正弦和余弦值。

  该模块运行速度较慢，但不需要额外的数据内存。对于代码生成，该模块需要一个支持库来仿真三角函数，从而增加生成代码的大小。

### 数据类型选项卡

### **舍入模式** — 舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择定点运算的舍入模式。正弦表值不遵循此参数；它们始终舍入到 `Nearest`。

### **整数溢出时饱和** — 整数溢出时饱和 `off`（默认） | `on`

选择此参数时，该模块对其定点运算结果进行饱和。清除此参数时，该模块对其定点运算结果进行绕回。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

**注意**

当满足以下条件时，**舍入模式**和**整数溢出时饱和**参数对数值结果没有影响：

- **乘积输出**数据类型为 `Inherit: Inherit via internal rule`。
- **累加器**数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置，该模块以全精度模式运行。

### **正弦表** — 正弦表 `Inherit: Same word length as input`（默认） | `fixdt(1,16)`

选择如何指定正弦表值的字长。正弦表值的小数长度始终等于字长减一。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16)`

正弦表值不遵循**舍入模式**和**整数溢出时饱和**参数。该模块始终将正弦表值饱和并舍入到 `Nearest`。

### **乘积输出** — 乘积输出 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as input` | `fixdt(1,16,0)`

指定乘积输出数据类型。有关描述此模块中乘积输出数据类型用法的图示，请参阅 Fixed-Point Data Types 和 Multiplication Data Types。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16,0)`

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **乘积输出** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **累加器** — 累加器 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt(1,16,0)`

指定累加器数据类型。有关描述此模块中累加器数据类型用法的图示，请参阅 Fixed-Point Data Types。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16,0)`

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **累加器** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **输出** — 输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as input` | `fixdt(1,16,0)`

指定输出数据类型。有关描述此模块中输出数据类型用法的图示，请参阅 Fixed-Point Data Types。您可以将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。

  当您选择 `Inherit: Inherit via internal rule` 时，该模块会自动计算输出字长和小数长度。内部规则首先使用以下公式计算理想的输出字长和小数长度：

  WLideal output=WLinput+floor(log2(DCT length−1))+1

  FLideal output=FLinput

  使用这些理想结果，内部规则随后选择适合您硬件的字长和小数长度。有关详细信息，请参阅 Inherit via Internal Rule。
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16,0)`

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **输出** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

### **输出最小值** — 输出最小值 `[]`（默认） | scalar

指定该模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **输出最大值** — 输出最大值 `[]`（默认） | scalar

指定该模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **锁定数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

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

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数（`string.h`）。

为符合嵌入式系统编码标准，生成的代码是非递归的。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

输入的逆离散余弦变换 (IDCT)

IDCT 模块计算输入信号 *u* 的逆离散余弦变换 (IDCT)。当输入是 *M*×*N* 矩阵时，该模块计算矩阵中每个通道的 IDCT。

以下是等效的 MATLAB® 代码。

    y = idct(u)
