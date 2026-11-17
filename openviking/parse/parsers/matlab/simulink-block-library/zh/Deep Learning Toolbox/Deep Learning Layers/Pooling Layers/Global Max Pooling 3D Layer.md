---
type: simulink-block
title: 'Global Max Pooling 3D Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Pooling Layers'
documentation_page: 'globalmaxpooling3dlayer'
documentation_source_path: 'ref/globalmaxpooling3dlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Global Max Pooling 3D Layer

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入数据，4 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 下采样后的输出数据，4 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入数据，4 维数组

要进行下采样的输入数据。数据必须具有四个维度，按此顺序分别对应
三个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 下采样后的输出数据，4 维数组

对输入数据进行下采样的结果。输出数据具有四个维度，
按此顺序分别对应三个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: 层
  summary: 对应的层对象 layerObject（默认值） | globalMaxPooling3dLayer 对象
  group: 主要
  block_parameter: Layer
  type: 工作区变量
  values: globalMaxPooling3dLayer 对象
  default: '''layerObject'''
- name: 数据格式
  summary: 输入数据的格式 SSSC（默认值）
  group: 主要
  block_parameter: DataFormat
  type: 字符向量
  values: '''SSSC'''
  default: '''SSSC'''
- name: 输入大小
  summary: 输入数据的大小 [10 10 10 64]（默认）| 正标量数组
  group: 主要
  block_parameter: InputSize
  type: array
  values: '[10 10 10 64] | ''<array>'''
  default: '''[10 10 10 64]'''
- name: 输出最小值
  summary: 用于范围检查的最小输出值 []（默认）| scalar
  group: 数据类型
  block_parameter: OutMin
  values: '''[]''（默认） | 用引号括起来的标量'
- name: 输出最大值
  summary: 用于范围检查的最大输出值 []（默认值）| 标量
  group: 数据类型
  block_parameter: OutMax
  values: '''[]''（默认值） | 用引号括起来的标量'
- name: 输出数据类型
  summary: '输出的数据类型 Inherit: Inherit via internal rule（默认值）| Inherit: Inherit via back propagation | Inherit: Same as first
    input | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit via internal rule''（默认值） | ''Inherit: Inherit via back propagation'' | ''Inherit: Same as first
    input'' | <data type expression>'
- name: 锁定输出数据类型设置以防止定点工具更改
  summary: 防止定点工具覆盖输出数据类型的选项 off（默认值）| on
  group: 数据类型
  block_parameter: LockScale
  values: '''off''（默认值） | ''on'''
- name: 整数舍入模式
  summary: 定点运算的舍入模式 Floor（默认值）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  values: '''Floor''（默认值） | ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: 整数溢出时饱和
  summary: 溢出处理方式 off（默认） | on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认） | ''on'''
- name: 采样时间
  summary: 用于指定采样时间的选项 -1（默认值）| scalar
  group: 执行
  block_parameter: SampleTime
  values: '''-1''（默认值） | scalar'
```

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条上，在**仿真**选项卡的
**准备**库中，选择**属性检查器**。

### 主要

### **层** — 对应的层对象 `layerObject`（默认值） | `globalMaxPooling3dLayer` 对象

指定工作区变量的名称，该变量包含来自经过训练的网络的
`globalMaxPooling3dLayer` 对象。Global Max Pooling 3D Layer
模块使用该对象的属性对自身进行配置。

#### 编程使用

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `globalMaxPooling3dLayer` 对象 |
| **默认值：** `'layerObject'` |

### **数据格式** — 输入数据的格式 `SSSC`（默认值）

输入数据的数据格式。这些选项采用与
`dlarray` 对象的 `fmt` 参数相同的
表示法，但层模块不支持批量
(`B`) 维度，而是将观测数假定为
`1`。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'SSSC'` |
| **默认值：** `'SSSC'` |

### **输入大小** — 输入数据的大小 `[10 10 10 64]`（默认）| 正标量数组

输入到模块的数据的大小，指定为正标量数组。要确定位于 `globalMaxPooling3D` 对象之前的层的激活，可以使用 `analyzeNetwork` 函数。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputSize` |
| **类型：** array |
| **值：** `[10 10 10 64]` | `'<array>'` |
| **默认值：** `'[10 10 10 64]'` |

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| scalar

软件检查的输出范围的最小值。

软件使用该最小值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅指定模块参数的最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会删除算法代码，并影响某些仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最小值** 不会使实际输出信号饱和或截断。请改用 Saturation (Simulink) 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认） | 用引号括起来的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认值）| 标量

软件所检查的输出范围的最大值。

软件使用该最大值执行以下操作：

- 对某些模块进行参数范围检查。有关详细信息，请参阅为模块参数指定最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和
  启用仿真范围检查 (Simulink)。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以删除算法代码，并影响某些
  仿真模式（例如 SIL 或外部模式）的结果。有关详细信息，请参阅
  使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最大值**不会使实际输出信号饱和或对其限幅。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认值） | 用引号括起来的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认值）| `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为 `Simulink.NumericType` 之类的数据类型对象。当您选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型，在考虑嵌入式目标硬件属性的同时，权衡数值精度、性能和生成的代码大小。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认值） | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **锁定输出数据类型设置以防止定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off`（默认值）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认值） | `'on'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认值）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制
模块参数的舍入方式，请在封装字段中输入使用 MATLAB® 舍入函数的表达式。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认值） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **整数溢出时饱和** — 溢出处理方式 `off`（默认） | `on`

指定整数溢出时是进行饱和处理还是绕回。

- `on` — 溢出会饱和到该数据类型所能表示的最小值或最大值。
- `off` — 溢出会绕回到该数据类型所能表示的相应值。

例如，有符号 8 位整数 `int8` 所能表示的最大值为 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和至 127。
  同样，模块输出饱和至最小输出值 –128。
- 取消选中此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生非预期结果。
  例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 如果模型可能发生溢出，并且您希望在生成的代码中提供显式饱和保护，请将此参数设置为 `on`。
- 为优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅排查信号范围错误 (Simulink)。
- 选中此参数时，饱和处理将应用于模块的每个内部运算，而不仅仅应用于输出或结果。
- 通常，代码生成过程可以检测出不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认值）| scalar

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅采样时间的类型 (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程用法

要以编程方式设置模块参数的值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认值） | scalar |
## 所属库

Deep Learning Toolbox / Deep Learning Layers / Pooling Layers

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**Layer** 参数的默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在之前的版本中，默认值为 `'layer'`。如果您的代码以编程方式创建 Simulink，并且依赖于名为 `'layer'` 的变量，请更新代码，使该变量的名称改为 `'layerObject'`。

## 描述

三维全局最大池化层

Global Max Pooling 3D Layer 模块通过计算输入在高度、宽度和深度维度上的最大值来执行下采样。此模块接受采用 `SSSC` 格式的三维图像数据（四个维度按顺序分别对应三个空间维度和一个通道维度），并在空间维度上进行池化。

`exportNetworkToSimulink` 函数生成此模块，以表示 `globalMaxPooling3dLayer` 对象。
