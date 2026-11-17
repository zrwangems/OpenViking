---
type: simulink-block
title: 'Global Max Pooling 1D Layer'
family: 'deep-learning-layers'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Pooling Layers'
documentation_page: 'globalmaxpooling1dlayer'
documentation_source_path: 'ref/globalmaxpooling1dlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Global Max Pooling 1D Layer

## 端口

### 输入

### **Port\_1** — 输入数据二维数组

要下采样的输入数据。数据必须有两个维度，对应于
使用 **Data format** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1** — 下采样后的输出数据二维数组

对输入数据进行下采样后的结果。输出数据有两个维度，
对应于使用 **Data format** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条中，在 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认）| `globalMaxPooling1dLayer` 对象

指定包含来自训练网络的
`globalMaxPooling1dLayer` 对象的工作区变量的名称。
Global Max Pooling 1D Layer 模块使用该对象的属性自行配置。

#### 编程用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `globalMaxPooling1dLayer` 对象 |
| **默认值：** `'layerObject'` |

### **Data format** — 输入数据的格式 `CT`（默认）| `SC`

输入数据的数据格式。这些选项使用与
`dlarray` 对象的 `fmt` 参数相同的表示法，
但层模块不支持 Batch
(`B`) 维度，而是假定观测数为
`1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'CT'` | `'SC'` |
| **默认值：** `'CT'` |

### **Input size** — 输入数据的大小 `[10 10]`（默认）| 正标量数组

模块输入数据的大小，指定为正标量数组。要
确定先于
`globalMaxPooling1D` 对象的层的激活值，可以使用 `analyzeNetwork` 函数。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputSize` |
| **类型：** 数组 |
| **值：** `[10 10]` | `'<array>'` |
| **默认值：** `'[10 10]'` |

### 数据类型

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的最小值。

软件使用该最小值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和
  Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此
  优化可能会移除算法代码，并影响某些
  仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅
  Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的最大值。

软件使用该最大值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和
  Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动缩放。
- 优化从模型生成的代码。此
  优化可能会移除算法代码，并影响某些
  仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅
  Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **Output data type** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型来平衡数值精度、性能和生成代码
大小，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Lock output data type setting against changes by the fixed-point tools** — 用于防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖你在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认） | `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制
模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定整数溢出是饱和还是回绕。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以
表示的最大值是 127。任何大于该最大值的模块运算结果都会导致
8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。
  类似地，模块输出在最小输出值
  –128 处饱和。
- 清除此参数时，软件会将导致溢出的
  值解释为 `int8`，这可能会产生意外结果。
  例如，表示为
  `int8` 的模块结果 130（二进制 1000 0010）为 –126。

#### 提示

- 当你的模型可能发生
  溢出，并且你希望在生成
  代码中具有显式饱和保护时，将此参数设置为 `on`。
- 要优化生成代码的效率，请保留此参数的默认
  `off` 设置。使用默认
  设置还有助于避免过度指定模块如何处理
  超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选中此参数时，饱和适用于模块上的每个内部
  运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### 执行

### **Sample time** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定另一种类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在该模型中的上下文继承采样时间。

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

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果你有以编程方式创建 Simulink 并依赖于名为 `'layer'` 的变量的代码，请更新代码，使该变量名为 `'layerObject'`。

## 描述

1-D 全局最大池化层

Global Max Pooling 1D Layer 模块通过对输入的时间维度或空间维度取最大值来执行下采样。

该层进行池化的维度取决于层输入：

- 对于 `CT` 格式的时间序列和向量序列输入（两个
  维度分别按顺序对应通道和时间步），该层对时间维度进行池化。
- 对于 `SC` 格式的一维图像输入（两个维度
  分别按顺序对应空间像素和通道），该层对空间维度进行池化。

`exportNetworkToSimulink` 函数生成此模块来表示 `globalMaxPooling1dLayer` 对象。
