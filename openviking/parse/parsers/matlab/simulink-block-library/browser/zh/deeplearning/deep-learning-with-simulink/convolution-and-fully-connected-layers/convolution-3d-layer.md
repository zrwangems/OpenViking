---
type: simulink-block
title: 'Convolution 3D Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Convolution and Fully Connected Layers'
documentation_page: 'convolution3dlayer'
documentation_source_path: 'ref/convolution3dlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolution 3D Layer

## 端口

### 输入

### **Port\_1** — 输入数据 4 维数组

要对其执行卷积运算的输入数据。该数据必须具有四个维度，按顺序分别对应三个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 卷积输出数据 4 维数组

卷积输入数据的结果。输出数据具有四个维度，按顺序分别对应三个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认值） | `convolution3dLayer` 对象

指定包含来自训练网络的 `convolution3dLayer` 对象的工作区变量名称。Convolution 3D Layer 模块使用该对象的属性配置自身，并使用该对象的可学习参数计算模块输出。

#### 编程用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `convolution3dLayer` 对象 |
| **默认值：** `'layerObject'` |

### **数据格式** — 输入数据的格式 `SSSC`（默认值）

输入数据的格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch（`B`）维度，而是假定观测编号为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'SSSC'` |
| **默认值：** `'SSSC'` |

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认值） | 标量

软件检查的输出范围的最小值。

软件使用最小值执行以下操作：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最小值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认值） | 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认值） | 标量

软件检查的输出范围的最大值。

软件使用最大值执行以下操作：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最大值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认值） | 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认值） | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在数值精度、性能和生成代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认值） | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **锁定输出数据类型设置，防止定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off`（默认值） | `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **输出** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认值） | `'on'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认值） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认值） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **对整数溢出进行饱和** — 溢出操作的方法 `off`（默认值） | `on`

指定整数溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 –126。

#### 提示

- 当模型可能发生溢出且您希望在生成的代码中获得显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请为此参数保留默认 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选中此参数时，饱和将应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认值） | `'on'` |

### **权重** — 权重的数据类型 `Inherit: Inherit via back propagation`（默认值） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `Weights` 属性值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `WeightsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认值） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **偏置** — 偏置的数据类型 `Inherit: Inherit via back propagation`（默认值） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `Bias` 属性值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `BiasDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认值） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **累加器** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认值） | `Inherit: Same as first input` | `<data type expression>`

选择 Convolution 3D Layer 模块内每个 Convolution 模块的累加器数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在数值精度、性能和生成代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `AccumDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认值） | `'Inherit: Same as first input'` | `<data type expression>` |

### 执行

### **采样时间** — 指定采样时间的选项 `-1`（默认值） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认值） | 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Convolution and Fully Connected Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: **Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在之前的版本中，默认值为 `'layer'`。如果您的代码以编程方式创建 Simulink 并依赖名为 `'layer'` 的变量，请更新代码，使该变量名为 `'layerObject'`。

## 描述

3-D 卷积层

Convolution 3D Layer 模块将滑动长方体卷积滤波器应用于 3-D 输入。该层通过沿输入垂直和水平方向以及沿深度方向移动滤波器来对输入进行卷积，计算权重与输入的点积，然后加上偏置项。此模块接受 `SSSC` 格式的 3-D 图像数据（四个维度，按顺序分别对应三个空间维度和一个通道维度），并在空间维度上执行卷积。

`exportNetworkToSimulink` 函数生成此模块以表示 `convolution3dLayer` 对象。
