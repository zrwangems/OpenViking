---
type: simulink-block
title: 'Allpole Filter'
family: 'filtering'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'allpolefilter'
documentation_source_path: 'ref/allpolefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Allpole Filter

## 端口

### 输入

### **In** — 数据输入 向量 | 矩阵

将数据输入指定为向量或矩阵。该模块接受可变大小输入。在仿真期间，您可以更改每个输入通道的大小，但通道数必须保持不变。

数据输入和滤波器系数必须具有相同的数据类型。

如果输入为定点，则它必须是带符号整数或带符号定点值，且斜率为 2 的幂、偏置为零。

在将 **Coefficient source** 设置为 `Input port` 之前，此端口未命名。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持:** 是

### **Den** — 滤波器分母系数 标量 | 行向量

将滤波器传递函数的分母系数指定为标量或行向量。数据输入和滤波器系数必须具有相同的数据类型。

#### 依赖关系

要启用此端口，请将 **Coefficient source** 设置为 `Input port`。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持:** 是
### 输出

### **Out** — 滤波后的输出 向量 | 矩阵

滤波后的输出，以向量或矩阵形式返回。输出信号的大小、数据类型和复/实性与输入信号匹配。

在将 **Coefficient source** 设置为 `Input port` 之前，此端口未命名。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持:** 是

## 参数

### 主选项卡

### **Coefficient source** — 系数来源 `Dialog parameters` (默认) | `Input port`

选择是在模块掩码中指定滤波器系数，还是通过输入端口指定。

### **Filter structure** — 指定滤波器结构 `Direct form` (默认) | `Direct form transposed` | `Lattice AR`

将滤波器结构指定为以下之一：

- `Direct form`
- `Direct form transposed`
- `Lattice AR`

如果将结构指定为 `Direct form` 或 `Direct form transposed`，则该模块不支持定点处理的分析方法。

### **Coefficients** — 滤波器分母系数 [1 0.1] (默认) | 标量 | 行向量

将滤波器传递函数的分母系数指定为标量或行向量。

**可调:** 是

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 `Dialog parameters`。

### **Input processing** — 输入处理 `Columns as channels (frame based)` (默认) | `Elements as channels (sample based)`

指定该模块执行基于样本还是基于帧的处理。您可以选择以下选项之一：

- `Columns as channels (frame based)`
  — 将输入的每一列视为独立通道（基于帧的处理）。
- `Elements as channels (sample based)`
  — 将输入的每个元素视为独立通道（基于样本的处理）。

### **Initial states** — 滤波器状态的初始条件 `0` (默认) | 标量 | 向量 | 矩阵

将滤波器状态的初始条件指定为标量、向量或矩阵。

默认情况下，Allpole Filter 模块将内部滤波器状态初始化为零，这与假设过去的输入和输出为零的效果相同。您可以选择使用此参数为滤波器延迟指定非零初始条件。

要确定必须指定的初始状态数量以及如何指定它们，请参阅有关有效初始状态的表。**Initial states** 参数可以采用下表所述形式之一。

**有效的初始状态**

| 初始条件 | 描述 |
| --- | --- |
| 标量 | 该模块将滤波器中的所有延迟元素初始化为该标量值。 |
| 向量或矩阵（用于为每个通道应用不同的延迟元素） | 每个向量或矩阵元素为相应通道中的相应延迟元素指定唯一的初始条件：  - 向量长度等于输入通道数与滤波器中延迟元素数的乘积，`#_of_filter_coeffs-1`（对于 `Lattice AR`，为 `#_of_reflection_coeffs`）。 - 矩阵的行数必须与滤波器中延迟元素数相同，`#_of_filter_coeffs-1`（对于 `Lattice AR`，为 `#_of_reflection_coeffs`），并且必须为输入信号的每个通道包含一列。 |

### 数据类型选项卡

### **Coefficients** — 系数数据类型 `Inherit: Same word length as input` (默认) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)`

指定系数数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮（双大于号符号）以显示 **Data Type Assistant**，它可帮助您设置 **Coefficients** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Coefficients Minimum** — 滤波器系数的最小值 `[]` (默认) | 标量

指定滤波器系数的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）
- 定点数据类型的自动定标

### **Coefficients Maximum** — 滤波器系数的最大值 `[]` (默认) | 标量

指定滤波器系数的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）
- 定点数据类型的自动定标

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)`

指定乘积输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮（双大于号符号）以显示 **Data Type Assistant**，它可帮助您设置 **Product output** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)`

指定累加器数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮（双大于号符号）以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **State** — 状态数据类型 `Inherit: Same as accumulator` (默认) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)`

指定状态数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 内置整数，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮（双大于号符号）以显示 **Data Type Assistant**，它可帮助您设置 **State** 参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

要启用此参数，请将 **Filter structure** 设置为 `Lattice AR`。

### **Output** — 输出数据类型 `Inherit: Same as input` (默认) | `Inherit: Same as accumulator` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 内置数据类型，例如 `int8`
- 数据类型对象，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 输出最小值 `[]` (默认) | 标量

指定模块必须输出的最小值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]` (默认) | 标量

指定模块必须输出的最大值。默认值为 `[]`（未指定）。Simulink 软件使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

### **Integer rounding mode** — 整数舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。

### **Saturate on integer overflow** — 对整数溢出进行饱和处理 `off` (默认) | `on`

选中此复选框时，该模块会对每个内部运算应用饱和处理，而不仅仅是输出或结果。通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

| 操作 | 采取此操作的原因 | 发生溢出时的情况 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框。 | 您的模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护。 | 溢出会饱和到该数据类型可以表示的最小值或最大值。 | 与带符号 8 位整数相关的溢出可以饱和到 -128 或 127。 |
| 不选中此复选框。 | 您希望优化生成代码的效率。您希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。 | 溢出会回绕到该数据类型可表示的相应值。 | 数字 130 无法放入带符号 8 位整数，并回绕到 -126。 |

## 所属库

DSP System Toolbox / Filtering / Filter Implementations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `integera` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块仅支持带符号定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2011b 中引入**

## 描述

为全极点滤波器建模

Allpole Filter 模块使用指定的全极点滤波器对输入信号的每个通道独立进行滤波。该模块可以实现具有固定系数的静态滤波器和系数随时间变化的时变滤波器。您可以在仿真期间调整静态滤波器的系数。

该模块随时间独立地对输入信号的每个通道进行滤波。通过 **Input processing** 参数，您可以指定该模块是将输入的每个元素视为独立通道（基于样本的处理），还是将输入的每一列视为独立通道（基于帧的处理）。

该模块支持 Simulink® 状态记录功能。有关详细信息，请参阅 State (Simulink)。
