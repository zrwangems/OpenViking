---
type: simulink-block
title: 'Addition Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Combination Layers'
documentation_page: 'additionlayer'
documentation_source_path: 'ref/additionlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Addition Layer

## 端口

### 输入

### **Port\_1** — 第一个输入数据 标量 | 向量 | 矩阵

要相加的第一个输入，以数组形式提供，该数组遵循您使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 第二个输入数据 标量 | 向量 | 矩阵

要相加的第二个输入，以数组形式提供，该数组遵循您使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_N** — 第 *N* 个输入数据 标量 | 向量 | 矩阵

要相加的第 *N* 个输入，以数组形式提供，该数组遵循您使用 **数据格式** 参数指定的格式。该模块的输入端口数等于您使用 **输入数目** 模块参数指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

输入数据的逐元素和。输出数据使用您使用 **数据格式** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **输入数目** — 输入数目 `2` (默认) | `3` | `4` | `5`

指定模块的输入数目。该模块计算输入的求和。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumInputs` |
| **类型**：字符向量 |
| **取值**：`'2'` | `'3'` | `'4'` | `'5'` |
| **默认值**：`'2'` |

### **数据格式** — 输入数据的格式 `SSC` (默认) | `C` | `CT` | `SC` | `SSSC`

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch (`B`) 维度，而是假设观测数为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **取值：** `'SSC'` | `'C'` | `'CT'` | `'SC'` | `'SSSC'` |
| **默认值：** `'SSC'` |

### 数据类型

### **输出最小值** — 用于范围检查的输出最小值 `[]` (默认) | 标量

软件检查的输出范围的最小值。

软件使用最小值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 为模块参数指定最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。这种优化可能会删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最小值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **取值：** | `'[]'` (默认) | 带引号的标量 |

### **输出最大值** — 用于范围检查的输出最大值 `[]` (默认) | 标量

软件检查的输出范围的最大值。

软件使用最大值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 为模块参数指定最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 指定信号范围 (Simulink) 和 启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。这种优化可能会删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最大值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **取值：** | `'[]'` (默认) | 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成代码大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **取值：** | `'Inherit: Inherit via internal rule'` (默认) | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **锁定数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **取值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **输出整数舍入模式** — 定点输出转换操作的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定由最终定点转换操作生成的模块输出值的舍入模式。有关其他内部模块操作的舍入模式，请参阅 **内部整数舍入模式**。有关详细信息，请参阅 舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **取值：** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **输出整数溢出饱和** — 输出转换操作的溢出操作方法 `off` (默认) | `on`

指定由最终定点转换操作生成的模块输出值在整数溢出时是饱和还是回绕。有关内部模块操作的溢出操作方法，请参阅 **内部整数溢出饱和**。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块操作结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出饱和为 127。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 –126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成代码中显式提供饱和保护时，将此参数设置为 `on`。
- 为优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 排查信号范围错误 (Simulink)。
- 当您选择此参数时，饱和仅应用于输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **取值：** | `'off'` (默认) | `'on'` |

### **累加器** — 累加器的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as first input` | `<data type expression>`

选择累加器的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成代码大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `AccumDataTypeStr` |
| **取值：** | `'Inherit: Inherit via internal rule'` (默认) | `'Inherit: Same as first input'` | `<data type expression>` |

### **内部整数舍入模式** — 内部定点操作的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出操作之外的内部定点计算的舍入模式。有关输出操作的舍入模式，请参阅 **输出整数舍入模式**。有关详细信息，请参阅 舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalRndMeth` |
| **取值：** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **内部整数溢出饱和** — 内部模块操作的溢出操作方法 `off` (默认) | `on`

指定模块内部操作在整数溢出时是饱和还是回绕。有关模块输出的溢出操作方法，请参阅 **输出整数溢出饱和**。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块操作结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出饱和为 127。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 –126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成代码中显式提供饱和保护时，将此参数设置为 `on`。
- 为优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 排查信号范围错误 (Simulink)。
- 当您选择此参数时，饱和仅应用于模块的内部操作。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalSaturateOnIntegerOverflow` |
| **取值：** | `'off'` (默认) | `'on'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1` (默认) | 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 采样时间类型 (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **取值：** `'-1'` (默认) | 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Combination Layers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: 更新了整数舍入模式、整数溢出饱和和累加器参数

**整数舍入模式** 和 **整数溢出饱和** 参数现在拆分为输出和内部版本的参数。**输出整数舍入模式** 和 **输出整数溢出饱和** 控制模块输出的最终转换操作的行为。**内部整数舍入模式** 和 **内部整数溢出饱和** 控制模块内部操作。

**累加器数据类型** 参数现在命名为 **累加器**。

## 描述

加法层

Addition Layer 模块对来自多个神经网络层的输入进行逐元素相加。Addition Layer 模块的每个非标量输入必须具有相同的维度，并且必须遵循您使用 **数据格式** 模块参数指定的数据格式。该模块会扩展标量输入，使其具有与其他输入相同的维度。

`exportNetworkToSimulink` 函数生成此模块以表示 `additionLayer` 对象。
