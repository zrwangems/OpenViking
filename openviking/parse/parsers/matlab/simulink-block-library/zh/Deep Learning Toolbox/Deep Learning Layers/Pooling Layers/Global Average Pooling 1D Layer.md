---
type: simulink-block
title: 'Global Average Pooling 1D Layer'
family: 'deep-learning-layers'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Pooling Layers'
documentation_page: 'globalaveragepooling1dlayer'
documentation_source_path: 'ref/globalaveragepooling1dlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Global Average Pooling 1D Layer

## 端口

### 输入

### **Port\_1** — 输入数据二维数组

要进行下采样的输入数据。数据必须具有两个维度，对应于使用 **数据格式** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 下采样后的输出数据二维数组

对输入数据进行下采样的结果。输出数据具有两个维度，对应于使用 **数据格式** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **层** — 对应的层对象 `layerObject`（默认） | `globalAveragePooling1dLayer` 对象

指定一个工作区变量的名称，该变量包含来自已训练网络的 `globalAveragePooling1dLayer` 对象。Global Average Pooling 1D Layer 模块使用该对象的属性自行配置。

#### 编程用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `globalAveragePooling1dLayer` 对象 |
| **默认值：** `'layerObject` |

### **数据格式** — 输入数据的格式 `CT`（默认） | `SC`

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持批量 (`B`) 维度，而是假定观测数为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'CT'` | `'SC'` |
| **默认值：** `'CT'` |

### **输入大小** — 输入数据的大小 `[10 10]`（默认） | 正标量数组

模块输入数据的大小，指定为正标量数组。要确定某个 `globalAveragePooling1D` 对象之前那一层的激活值，可以使用 `analyzeNetwork` 函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputSize` |
| **类型：** 数组 |
| **值：** `[10 10]` | `'<array>'` |
| **默认值：** `'[10 10]'` |

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认） | 标量

软件检查的输出范围的最小值。

软件使用该最小值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅指定模块参数的最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最小值** 不会使实际输出信号饱和或对其进行裁剪。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认） | 标量

软件检查的输出范围的最大值。

软件使用该最大值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅指定模块参数的最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 对从模型生成的代码进行优化。此优化可以删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最大值** 不会使实际输出信号饱和或对其进行裁剪。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在数值精度、性能和生成代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **输出** 数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认） | `'on'` |

### **输出整数舍入模式** — 定点输出转换操作的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定模块输出值的舍入模式，该输出值由最终的定点转换操作生成。有关其他内部模块操作的舍入模式，请参阅 **内部整数舍入模式**。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **输出对整数溢出饱和** — 输出转换操作的溢出操作方式 `off`（默认） | `on`

指定模块输出值的整数溢出是饱和还是回绕，该输出值由最终的定点转换操作生成。有关内部模块操作的溢出操作方式，请参阅 **内部对整数溢出饱和**。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值为 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当模型可能发生溢出，并且您希望在生成代码中提供显式饱和保护时，请将此参数设置为 `on`。
- 为优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅排查信号范围错误 (Simulink)。
- 选择此参数后，饱和仅应用于输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### **累加器** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as first input` | `<data type expression>`

选择 Global Average Pooling 1D Layer 模块内 Sum of Elements 模块 `GlobalAvgPooling/Sum of Elements` 的累加器数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在数值精度、性能和生成代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `AccumDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Same as first input'` | `<data type expression>` |

### **池化元素数** — 标准差的数据类型 `Inherit: Inherit via back propagation`（默认） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

选择 Global Average Pooling 1D 模块内 Constant 模块 `GlobalAvgPooling/Sum of Elements` 的输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

`NumPoolingElements` Constant 模块通过计算使用 **层** 参数指定的对象的 `PoolSize` 属性元素的乘积，来计算池化元素数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `NumPoolingElementsDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **内部整数舍入模式** — 内部定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出操作之外的内部定点计算的舍入模式。有关输出操作的舍入模式，请参阅 **输出整数舍入模式**。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalRndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **内部对整数溢出饱和** — 内部模块操作的溢出操作方式 `off`（默认） | `on`

指定模块内部操作的整数溢出是饱和还是回绕。有关模块输出的溢出操作方式，请参阅 **输出对整数溢出饱和**。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值为 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当模型可能发生溢出，并且您希望在生成代码中提供显式饱和保护时，请将此参数设置为 `on`。
- 为优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅排查信号范围错误 (Simulink)。
- 选择此参数后，饱和仅应用于模块的内部操作。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalSaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### 执行

### **采样时间** — 指定采样时间的选项 `-1`（默认） | 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅采样时间类型 (Simulink)。

默认情况下，模块根据该模块在模型中的上下文继承其采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认） | 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Pooling Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: **层** 参数的默认值为 `'layerObject'`

从 R2025a 开始，**层** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您的代码以编程方式创建 Simulink 并依赖名称为 `'layer'` 的变量，请更新代码，使该变量的名称为 `'layerObject'`。

### R2025a: 更新了整数舍入模式和对整数溢出饱和参数

**整数舍入模式** 和 **对整数溢出饱和** 参数现在拆分为输出版本和内部版本的参数。**输出整数舍入模式** 和 **输出对整数溢出饱和** 控制模块输出的最终转换操作的行为。**内部整数舍入模式** 和 **内部对整数溢出饱和** 控制内部模块操作。

## 描述

一维全局平均池化层

Global Average Pooling 1D Layer 模块通过对输入的时间维度或空间维度求平均值来执行下采样。

该层进行池化的维度取决于层输入：

- 对于 `CT` 格式的时间序列和向量序列输入（两个维度按顺序分别对应通道和时间步），该层在时间维度上进行池化。
- 对于 `SC` 格式的一维图像输入（两个维度按顺序分别对应空间像素和通道），该层在空间维度上进行池化。

`exportNetworkToSimulink` 函数生成此模块以表示 `globalAveragePooling1dLayer` 对象。
