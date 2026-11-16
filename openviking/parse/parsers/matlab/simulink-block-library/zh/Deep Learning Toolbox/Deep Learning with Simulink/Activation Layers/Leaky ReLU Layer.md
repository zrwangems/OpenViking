---
type: simulink-block
title: 'Leaky ReLU Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Activation Layers'
documentation_page: 'leakyrelulayer'
documentation_source_path: 'ref/leakyrelulayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Leaky ReLU Layer

## 端口

### 输入

### **In** — 输入矩阵 标量 | 向量 | 矩阵

对其执行阈值操作的矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Out** — 输出矩阵 标量 | 向量 | 矩阵

对输入矩阵执行阈值操作的结果。输入矩阵中小于零的值乘以 **Scale** 参数的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Scale** — 负输入的缩放因子 `0.01`（默认）| 数值标量

负输入的缩放因子，指定为数值标量。

#### 编程用法

|  |
| --- |
| **模块参数：**  `Scale` |
| **类型：** character vector |
| **值：** 数值标量 |
| **默认值：**  `'0.01'` |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的最小值。

软件使用最小值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 指定模块参数的最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)。
- 定点数据类型的自动缩放。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最小值**不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的最大值。

软件使用最大值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 指定模块参数的最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)。
- 定点数据类型的自动缩放。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最大值**不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **锁定数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **输出整数舍入模式** — 定点输出转换操作的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定由最终定点转换操作生成的模块输出值的舍入模式。有关其他内部模块操作的舍入模式，请参阅 **内部整数舍入模式**。有关详细信息，请参阅 舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **输出整数溢出时饱和** — 输出转换操作的溢出操作方式 `off`（默认）| `on`

指定由最终定点转换操作生成的模块输出值在整数溢出时是饱和还是回绕。有关内部模块操作的溢出操作方式，请参阅 **内部整数溢出时饱和**。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生非预期结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成代码中获得显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 排查信号范围错误 (Simulink)。
- 选中此参数时，饱和仅应用于输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **Scale** — 缩放因子的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将 **Scale** 参数的值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ScaleDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **内部整数舍入模式** — 内部定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出操作之外的内部定点计算的舍入模式。有关输出操作的舍入模式，请参阅 **输出整数舍入模式**。有关详细信息，请参阅 舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalRndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **内部整数溢出时饱和** — 内部模块操作的溢出操作方式 `off`（默认）| `on`

指定模块的内部操作在整数溢出时是饱和还是回绕。有关模块输出的溢出操作方式，请参阅 **输出整数溢出时饱和**。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生非预期结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成代码中获得显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 排查信号范围错误 (Simulink)。
- 选中此参数时，饱和仅应用于模块的内部操作。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalSaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 采样时间的类型 (Simulink)。

默认情况下，模块根据模型内模块的上下文继承其采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Activation Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：更新了整数舍入模式和整数溢出时饱和参数

**整数舍入模式** 和 **整数溢出时饱和** 参数现在拆分为输出和内部版本的参数。**输出整数舍入模式** 和 **输出整数溢出时饱和** 控制模块输出的最终转换操作的行为。**内部整数舍入模式** 和 **内部整数溢出时饱和** 控制内部模块操作。

## 描述

Leaky 修正线性单元 (ReLU) 层

Leaky ReLU Layer 模块执行阈值操作，其中任何小于零的输入值都乘以一个固定标量。

此操作等效于：

f(x)={x,x≥0scale\*x,x<0.

由于它应用逐元素操作，此模块支持任何格式的输入数据，并输出与输入具有相同维度和格式的数据。

`exportNetworkToSimulink` 函数生成此模块来表示 `leakyReluLayer` 对象。
