---
type: simulink-block
title: 'ReLU Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Activation Layers'
documentation_page: 'relulayer'
documentation_source_path: 'ref/relulayer.html'
language: zh-CN
chinese_source: worker-translation
---

# ReLU Layer

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入数据 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 输出数据 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入数据 标量 | 向量 | 矩阵

要执行非线性阈值操作的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

对输入矩阵执行非线性阈值操作的结果。
输入矩阵中小于零的值变为零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: 输出最小值
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: 输出最大值
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: 输出数据类型
  summary: '输出的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Keep MSB | Inherit: Keep LSB | Inherit: Inherit via back
    propagation | Inherit: Same as first input | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit via internal rule''（默认）| ''Inherit: Keep MSB'' | ''Inherit: Keep LSB'' | ''Inherit: Inherit
    via back propagation'' | ''Inherit: Same as first input'' | <data type expression>'
- name: 锁定输出数据类型设置以防止被定点工具更改
  summary: 防止定点工具覆盖输出数据类型的选项 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  values: '''off''（默认）| ''on'''
- name: 整数舍入模式
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  values: '''Floor''（默认）| ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: 整数溢出时饱和
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
- name: 采样时间
  summary: 指定采样时间的选项 -1（默认）| 标量
  group: 执行
  block_parameter: SampleTime
  values: '''-1''（默认）| 标量'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上，在**准备**库中，选择**属性检查器**。

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的最小值。

软件使用最小值来执行：

- 某些模块的参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

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

软件使用最大值来执行：

- 某些模块的参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最大值**不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型来平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定整数溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成的代码中显式提供饱和保护时，请将此参数设置为 `on`。
- 为了优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 当您选择此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### 执行

### **采样时间** — 指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

修正线性单元 (ReLU) 层

ReLU Layer 模块对层输入应用修正线性单元 (ReLU) 激活操作。ReLU 激活执行非线性阈值操作，其中任何小于零的输入值都设置为零。

此操作等效于：

ReLU(x)={x,x>00,x≤0

`exportNetworkToSimulink` 函数生成此模块以表示 `reluLayer` 对象。由于它应用逐元素操作，此模块支持任何格式的输入数据，并输出与输入具有相同维度和格式的数据。
