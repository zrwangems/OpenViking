---
type: simulink-block
title: 'Sigmoid Layer'
family: 'deep-learning-layers'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Activation Layers'
documentation_page: 'sigmoidlayer'
documentation_source_path: 'ref/sigmoidlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Sigmoid Layer

## 端口

### 输入

### **Port\_1** — 输入数据 标量 | 向量 | 矩阵

要应用 sigmoid 函数的矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

对输入矩阵应用 sigmoid 函数的结果。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在
**准备** 库中，选择 **属性检查器**。

### 数据类型

### **近似方法** — 用于计算层输出的近似方法 `None` (default) | `CORDIC` | `Lookup`

指定用于计算输出的近似类型。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None` (default) | Floating point | 您仅处理浮点数据时。 |
| `CORDIC` | Floating point（double 和 single）以及 **Bias** 值为 `0` 且 **Slope** 值为 2 的幂的 fixed point | 您处理定点数据并希望部署到 FPGA 硬件时。 |
| `Lookup` | Floating point 和 fixed point | 您处理定点数据并希望生成 C/C++ 代码时。 |

有关 CORDIC 近似方法的详细信息，请参阅 `cordictanh` (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** character vector |
| **取值：** `'none'` | `'CORDIC'` | `'Lookup'` |
| **默认：** `'none'` |

### **输出最小值** — 用于范围检查的最小输出值 `[]` (default) | 标量

软件检查的输出范围的下限值。

软件使用最小值来执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最小值** 不会使实际输出信号饱和或限幅。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **取值：** | `'[]'` (default) | 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]` (default) | 标量

软件检查的输出范围的上限值。

软件使用最大值来执行：

- 对某些模块进行参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最大值** 不会使实际输出信号饱和或限幅。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **取值：** | `'[]'` (default) | 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule` (default) | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型来平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **取值：** | `'Inherit: Inherit via internal rule'` (default) | `<data type expression>` |

### **锁定输出数据类型设置，防止定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off` (default) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **输出数据类型**。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **取值：** | `'off'` (default) | `'on'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **取值：** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **整数溢出时饱和** — 溢出操作的方法 `off` (default) | `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值为 127。任何大于此最大值的模块运算结果都会导致该 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 -128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当模型可能发生溢出，并且您希望在生成的代码中显式提供饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选中此参数时，饱和会应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **取值：** | `'off'` (default) | `'on'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1` (default) | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **取值：** `'-1'` (default) | 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Activation Layers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：更新了 **输出数据类型** 取值选项

**输出数据类型** 取值选项为 `'Inherit:
Inherit via internal rule'` 和 `<data type
expression>`。以前，**输出数据类型**
取值选项为 `'Inherit: Inherit via internal rule'`、
`'Inherit: Keep MSB'`、`'Inherit: Keep
LSB'`、`'Inherit: Inherit via back propagation'`、
`'Inherit: Same as first input'` 和 `<data type
expression>`。

### R2025a：移除了 **近似方法** 依赖关系

模块参数不依赖于 **近似方法** 的值。以前，**近似方法** 的值必须为 `'None'` 才能启用其他模块参数。

## 描述

Sigmoid 层

Sigmoid Layer 模块将 sigmoid 函数应用于层输入，使输出限制在区间 (0,1) 内。

`exportNetworkToSimulink` 函数生成此模块以表示 `sigmoidLayer` 对象。
由于它应用逐元素运算，此模块支持任意格式的输入数据，并输出与输入具有相同维度和格式的数据。
