---
type: simulink-block
title: 'Weighted Sample Time Math'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'weightedsampletimemath'
language: zh-CN
chinese_source: worker-translation
---

# Weighted Sample Time Math



支持涉及采样时间的计算

## 库

Simulink / Math Operations

## 说明

Weighted Sample Time 模块根据 **Operation** 和 **Weight value** 参数的设置以及函数输出的执行上下文，输出加权采样时间、加权采样率或经过数学调整的加权采样时间。

通过 **Operation** 参数指定模块运算。

用于推导输出的采样时间取决于该模块是在周期还是非周期（或触发）执行上下文中使用。对于周期执行上下文，模块使用模型的采样时间。对于非周期或触发执行上下文，模块使用离散信号的采样时间。

使用 **Weight value** 参数指定采样时间权重因子。如果权重值 `w` 为 `1`，该值不会出现在模块图标上的方程中。

**提示**

可以使用 Weighted Sample Time 和 Weighted Sample Time Math 模块从 Simulink® 信号中提取采样时间。将 **Operation** 参数设置为 `Ts Only`，将 **Weight value** 参数设置为 `1.0`。使用此配置时，模块输出输入信号的采样时间。

该模块使用 MATLAB® 运算符的优先级规则计算其输出。例如，如果 **Operation** 参数设置为 `+`，则模块使用以下表达式计算输出：

    u + (Ts * w)

如果 **Operation** 参数设置为 `/`，则模块使用以下表达式计算输出：

    (u / Ts) / w)

有关详细信息，请参阅 Operator Precedence。

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

将输入信号指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

根据 **Operation** 和 **Weight value** 参数的设置以及包含该模块的函数的执行上下文，模块输出加权采样时间、加权采样率或经过数学调整的加权采样时间。

- 加权采样时间 – 在周期函数中使用时，加权采样时间是输入信号的采样时间乘以 **Weight value** 参数指定的值（`Ts * w`）。在非周期或触发函数中使用时，加权采样时间是自上次执行以来经过的时间乘以权重值。
- 加权采样率 – 在周期函数中使用时，加权采样率是加权采样时间的倒数（`1/(Ts * w)`）。当该模块用于非周期函数中时，加权采样率不相关。
- 经过数学调整的加权采样时间 – 模块将输入信号 `u` 的值加到加权采样时间上、从加权采样时间中减去 `u`，或者将 `u` 乘以或除以加权采样时间。

用于推导输出的采样时间以及输出的数据类型取决于该模块是在周期还是非周期（或触发）执行上下文中使用。

| 模块的执行上下文 | 用于推导输出的采样时间 | 输出信号的数据类型 |
| --- | --- | --- |
| 周期 | 模型的采样时间 | - 符号与输入信号值的符号相同。 - 字长是输入信号字长或 `long   long` 的一半中的较大值。 - 缩放为加权采样时间的最佳精度缩放。 |
| 非周期或触发 | 自上次执行以来经过的时间 | - 数据类型为无符号。 - 字长足够大，以考虑模型配置参数 **Application lifespan** 的设置。 - 缩放为模型配置参数 **Clock resolution** 的设置的最佳精度缩放。 |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Operation** — 数学运算 `+`（默认） | `-` | `*` | `/` | `Ts Only` | `1/Ts Only`

指定用于调整输入信号的运算。例如，如果指定 `+` 运算，模块会将加权采样时间加到输入信号的值上。当在非周期函数中使用该模块时，值 `1/Ts Only` 不相关。

#### 编程用法

|  |
| --- |
| **模块参数：** `TsampMathOp` |
| **类型：** character vector |
| **值：** `'+' | '-' | '*' | '/' | 'Ts Only' | '1/Ts Only'` |
| **默认：** `'+'` |

### **Weight value** — 采样时间的权重 `1.0`（默认） | real-valued scalar

以 real-valued scalar 形式输入采样时间的权重。模块将输入信号的采样时间乘以指定的值。例如，如果在采样时间为 `0.2` 的模型的周期函数中使用该模块，并将权重值指定为 `3`，则加权采样时间为 `0.6`。

#### 编程用法

|  |
| --- |
| **模块参数：** `weightValue` |
| **类型：** character vector |
| **值：** real-valued scalar |
| **默认：** `1.0` |

### **Implement using** — 调整采样时间的方法 `Online Calculations`（默认） | `Offline Scaling Adjustment`

选择是通过应用在线计算还是应用离线缩放来调整采样时间。此选项仅适用于定点运算和整数运算。对于浮点数据类型，模块会忽略此选项。

| `Ts * w` 的结果 | 两种模式的输出数据类型 | 模块执行 |
| --- | --- | --- |
| 2 的幂（正或负）或整数值 | 当 **Output data type** 设置为 `Inherit: Inherit via internal rule` 时相同 | 两种模式效率相同 |
| 不是 2 的幂且不是整数值 | 不同 | 离线缩放模式更高效 |

**注意**

当未启用 **Implement using** 参数时，运算默认使用在线计算。

#### 依赖关系

要启用此参数，请将 **Operation** 设置为 `*` 或 `/`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TsampMathImp` |
| **类型：** character vector |
| **值：** `'Online Calculations' | 'Offline Scaling Adjustment'` |
| **默认：** `'Online Calculations'` |

### 信号属性

### **Output data type** — 输出信号的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,20,0)` | `<data type expression>`

指定模块输出信号的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： character vector |
| **值**： `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,20,0)` | `'<data type expression>'` |
| **默认**： `'Inherit: Inherit via internal rule'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数会舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 依赖关系

要启用此参数，请将 **Operation** 参数设置为 `+`、`-`、`*` 或 `/`。如果将 **Operation** 设置为 `*` 或 `/`，还必须将 **Implement using** 参数设置为 `Online Calculations`。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认：** `'Floor'` |

### **Saturate on integer overflow** — 溢出操作方法 `off`（默认） | `on`

指定整数溢出是饱和还是回绕。

| 目标 | 操作 | 溢出行为 | 示例 |
| --- | --- | --- | --- |
| 模型存在可能的溢出情况，并且你希望在生成的代码中提供显式饱和保护。 | 选中复选框（`on`）。 | 饱和到该数据类型可以表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。大于此最大值的模块运算结果会导致 8 位整数溢出。选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小值 -128。 |
| 你希望优化生成的代码。你希望避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。 | 清除复选框（`off`）。 | 将溢出回绕为数据类型可表示的适当值。 | `int8`（有符号 8 位整数）数据类型可以表示的最大值是 127。大于此最大值的模块运算结果会导致 8 位整数溢出。清除此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。 |

选中 **Saturate on integer overflow** 时，饱和会应用于模块上的每个内部运算，而不仅仅是输出或结果。当代码生成器检测到不可能发生溢出时，它不会生成饱和代码。

#### 依赖关系

要启用此参数，请将 **Operation** 参数设置为 `+`、`-`、`*` 或 `/`。如果将 **Operation** 设置为 `*` 或 `/`，还必须将 **Implement using** 参数设置为 `Online Calculations`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SaturateOnIntegerOverflow` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |

### **Mode** — 数据类型模式 `Inherit`（默认） | `Built in` | `Fixed point` | `Expression`

选择希望如何指定 **Output data type** 的数据类型属性。你可以选择：

- `Inherit` — 指定用于继承数据类型的规则，例如 `Inherit: Same as input`。
- `Built in`— 指定内置数据类型，例如 `double`。
- `Fixed point` — 指定数据类型的定点属性。
- `Expression` — 指定一个求值为有效数据类型的表达式，例如 `fixdt(1,16)`。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Signedness** — 定点数据的有符号性 `Signed`（默认） | `Unsigned`

指定定点数据是有符号还是无符号。`Signed` 数据可以表示正值和负值，但 `Unsigned` 数据仅表示正值。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Scaling** — 缩放定点数据的方法 `Best precision`（默认） | `Binary point`

指定用于缩放定点数据以避免溢出情况并最小化量化误差的方法。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`

### **Word length** — 保存量化整数的字的位大小 `16`（默认） | 从 2 到 128 的整数

将保存量化整数的字的位大小指定为从 2 到 128 的正整数。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 定点数据类型的小数长度 `0`（默认） | 整数标量

将定点数据类型的小数长度指定为正或负整数标量。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`，并将 **Scaling** 设置为 `Binary point`。

### **Slope** — 指定定点数据类型的斜率 `2^0`（默认） | positive, real-valued scalar

指定定点数据类型的斜率。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。

### **Bias** — 指定定点数据类型的偏置 `0`（默认） | real-valued scalar

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。

### **Data type override** — 数据类型覆盖模式 `Inherit`（默认） | `Off`

选择此信号的数据类型覆盖模式。你可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用你指定的定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**R2006a 之前引入**

### R2023b：Weighted Sample Time Math 模块更新

Weighted Sample Time Math 模块现在支持：

- 其他输出类型

  - `double`
  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `int64`
  - `uint64`
  - `fixdt(1,16,0)`
  - `fixdt(1,16,20,0)`

- `Fixed point` 作为 **Mode** 参数的新选项，可启用以下定点参数：

  - **Signedness**
  - **Scaling**
  - **Word length**
  - **Slope**
  - **Bias**
  - **Data type override**
