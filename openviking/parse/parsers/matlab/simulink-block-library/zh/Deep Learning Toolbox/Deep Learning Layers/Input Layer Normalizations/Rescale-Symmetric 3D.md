---
type: simulink-block
title: 'Rescale-Symmetric 3D'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Input Layer Normalizations'
documentation_page: 'rescalesymmetric3d'
documentation_source_path: 'ref/rescalesymmetric3d.html'
language: zh-CN
chinese_source: worker-translation
---

# Rescale-Symmetric 3D

## 端口

### 输入

### **Port\_1** — 输入数据，4 维数组

要归一化的输入数据。数据必须具有四个维度，按顺序分别对应三个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 归一化后的输出数据，4 维数组

归一化后的输出数据。输出数据具有四个维度，按顺序分别对应三个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上，在**准备**库中，选择**属性检查器**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认值）| `image3dInputLayer` 对象

指定一个工作区变量的名称，该变量包含来自训练后的网络的 `image3dInputLayer` 对象，并且该对象的 `Normalization` 属性设置为 `"rescale-symmetric"`。Rescale-Symmetric 3D 模块使用该对象的属性配置自身，并使用该对象的 `Min` 和 `Max` 属性计算模块输出。

#### 编程使用

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `image3dInputLayer` 对象 |
| **默认值：** `'layerObject'` |

### **数据格式** — 输入数据的格式 `SSSC`（默认值）

输入数据的数据格式。这些选项采用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持批量（`B`）维度，而是假定观测数为 `1`。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** character vector |
| **值：** `'SSSC'` |
| **默认值：** `'SSSC'` |

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认值）| scalar

软件所检查的输出范围的最小值。

软件使用此最小值执行以下操作：

- 对某些模块进行参数范围检查。有关详细信息，请参阅为模块参数指定最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和
  启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些
  仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅
  使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最小值**不会使实际输出信号饱和或对其进行剪裁。请改用 Saturation (Simulink) 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认值）| 用引号括起来的 scalar |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认） | 标量

软件所检查的输出范围的最大值。

软件使用此最大值执行以下操作：

- 对某些模块执行参数范围检查。有关详细信息，请参阅为模块参数指定最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和
  启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可能会删除算法代码，并影响某些
  仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅
  使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最大值** 不会使实际输出信号饱和或将其截断。请改用 Saturation (Simulink) 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型来平衡数值精度、性能和生成代码大小，
同时考虑嵌入式目标硬件的属性。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'` (默认值) | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认值) | `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor` (默认值) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，
请在封装字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'` (默认值) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **整数溢出时饱和** — 溢出处理方式 `off`（默认） | `on`

指定整数溢出时是饱和还是回绕。

- `on` — 溢出饱和为数据类型可表示的最小值或最大值。
- `off` — 溢出回绕为数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值为 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。同样，模块输出在最小输出值 –128 处饱和。
- 取消选中此参数时，软件将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护时，请将此参数设置为 `on`。
- 要优化所生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅排查信号范围错误 (Simulink)。
- 选中此参数时，饱和将应用于模块的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### **Min** — 最小值的数据类型 `Inherit: Inherit via back propagation`（默认） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将通过 **Layer** 参数指定的对象的 `Min` 属性值转换为此数据类型。
该类型可以继承、直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MinDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Max** — 最大值的数据类型 `Inherit: Inherit via back propagation`（默认） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将通过 **Layer** 参数指定的对象的 `Max` 属性值转换为此数据类型。
该类型可以继承、直接指定，也可以表示为数据类型对象，例如 `Simulink.NumericType`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **除法输出** — 除法输出的数据类型 `Inherit: Inherit via internal rule`（默认值）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

为 Rescale-Symmetric 3D 模块内每个 Neighborhood Processing Subsystem (Simulink) 模块中的 Divide (Simulink) 模块的输出选择数据类型。该类型可以继承、直接指定，也可以表示为 `Simulink.NumericType` 之类的数据类型对象。选择 `Inherit: Inherit via internal rule` 时，Simulink 会在考虑嵌入式目标硬件属性的同时，选择一种数据类型，以在数值精度、性能和生成的代码大小之间取得平衡。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DivideOutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认值）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认值）| 标量

指定采样时间点之间的离散间隔，或指定其他采样时间类型，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅“采样时间的类型 (Simulink)”。

默认情况下，模块会根据其在模型中的上下文继承采样时间。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认值）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Input Layer Normalizations

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**Layer** 参数的默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您的代码以编程方式创建 Simulink，并依赖于名为 `'layer'` 的变量，请更新代码，使该变量的名称为 `'layerObject'`。

## 描述

采用 rescale-symmetric 归一化的三维输入层

Rescale-Symmetric 3D 模块将三维图像数据（具有四个维度的数据，按顺序分别对应三个空间维度和一个通道维度）输入神经网络，并将输入重新缩放到 [-1, 1] 范围内。

`exportNetworkToSimulink` 函数生成此模块，用于表示 `Normalization` 参数设置为 `"rescale-symmetric"` 的 `image3dInputLayer` 对象。
