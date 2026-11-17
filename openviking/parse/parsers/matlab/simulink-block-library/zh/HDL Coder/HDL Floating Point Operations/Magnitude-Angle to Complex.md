---
type: simulink-block
title: 'Magnitude-Angle to Complex'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'magnitudeangletocomplex'
documentation_source_path: '../fixedpoint/../simulink/slref/magnitudeangletocomplex.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnitude-Angle to Complex

## 端口
```yaml
ports:
- name: '|u|'
  summary: 幅值 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: ∠u
  summary: 弧度相位角 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 幅值或弧度相位角 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 复信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **|u|** — 幅值 标量 | 向量 | 矩阵

幅值，指定为实数值标量、向量或矩阵。

#### 依赖关系

- 要启用此端口，请将 **Input** 设置为
  `Magnitude and angle`。

#### 限制

- 如果一个输入具有浮点数据类型，则另一个
  输入必须使用相同的数据类型。例如，两个信号
  必须同为 `double` 或
  `single`。
- 仅当您将
  **Approximation method** 设置为
  `CORDIC` 时，才支持定点数据类型。当一个输入具有
  定点数据类型时，另一个输入也必须具有
  定点数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **∠u** — 弧度相位角 标量 | 向量 | 矩阵

弧度相位角，指定为实数值标量、向量或
矩阵。要计算 CORDIC 近似，输入角度必须介于：

- [–2π, 2π) rad，对于有符号定点类型
- [0, 2π) rad，对于无符号定点类型

有关详细信息，请参阅 Effect of Out-of-Range Input on CORDIC Approximations。

#### 依赖关系

- 要启用此端口，请将 **Input** 设置为
  `Magnitude and angle`。

#### 限制

- 如果一个输入具有浮点数据类型，则另一个
  输入必须使用相同的数据类型。例如，两个信号
  必须同为 `double` 或
  `single`。
- 仅当您将
  **Approximation method** 设置为
  `CORDIC` 时，才支持定点数据类型。如果一个输入具有
  定点数据类型，则另一个输入也必须具有
  定点数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_1** — 幅值或弧度相位角 标量 | 向量 | 矩阵

幅值或弧度相位角，指定为实数值标量、
向量或矩阵。

- 当您将 **Input** 设置为
  `Magnitude` 时，您在输入端口指定
  幅值，在对话框上指定角度。
- 当您将 **Input** 设置为
  `Angle` 时，您在输入端口指定
  角度，在对话框上指定幅值。

#### 依赖关系

要启用此端口，请将 **Input** 设置为
`Magnitude` 或
`Angle`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 复信号 标量 | 向量 | 矩阵

复信号，由您指定的幅值和相位角
构成。

如果模块输入为数组，则输出为复信号
数组。幅值输入向量的元素映射到相应复输出元素的幅值。类似地，
角度输入向量的元素映射到相应复输出元素的角度。如果一个输入为标量，则它映射到所有复输出信号的相应
分量（幅值或角度）。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Input
  summary: 输入类型 Magnitude（默认）| Angle | Magnitude and angle
  group: ''
  block_parameter: Input
  type: 字符向量
  values: '''Magnitude'' | ''Angle'' | ''Magnitude and angle'''
  default: '''Magnitude and angle'''
- name: Angle
  summary: 输出的相位角 0（默认）| 实数值标量、向量或矩阵
  group: ''
  block_parameter: ConstantPart
  type: 字符向量
  values: 常量标量
  default: '''0'''
- name: Magnitude
  summary: 输出的幅值 0（默认）| 实数值标量、向量或矩阵
  group: ''
  block_parameter: ConstantPart
  type: 字符向量
  values: 实数值标量、向量或矩阵
  default: '''0'''
- name: Approximation method
  summary: CORDIC 或无 None（默认）| CORDIC
  group: ''
  block_parameter: ApproximationMethod
  type: 字符向量
  values: '''None'' | ''CORDIC'''
  default: '''None'''
- name: Number of iterations
  summary: CORDIC 算法的迭代次数 11（默认）| 正整数，小于或等于定点输入的字长
  group: ''
  block_parameter: NumberOfIterations
  type: 字符向量
  values: 正整数，小于或等于定点输入的字长
  default: '''11'''
- name: Scale output by reciprocal of gain factor
  summary: 按增益因子的倒数缩放复输出的实部和虚部 on（默认）| off
  group: ''
  block_parameter: ScaleReciprocalGainFactor
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
```

### **Input** — 输入类型 `Magnitude`（默认）| `Angle` | `Magnitude and angle`

指定输入类型：幅值输入、角度输入或
两者。

#### 编程用法

|  |
| --- |
| **模块参数：** `Input` |
| **类型：** 字符向量 |
| **值：** `'Magnitude' | 'Angle' | 'Magnitude and angle'` |
| **默认值：** `'Magnitude and angle'` |

### **Angle** — 输出的相位角 `0`（默认）| 实数值标量、向量或矩阵

输出信号的恒定相位角，以 rad 为单位。要计算 CORDIC 近似，
输入角度必须介于：

- [–2π, 2π) rad，对于有符号定点类型
- [0, 2π) rad，对于无符号定点类型

有关详细信息，请参阅 Effect of Out-of-Range Input on CORDIC Approximations。

#### 依赖关系

要启用此参数，请将 **Input** 设置为
`Magnitude`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ConstantPart` |
| **类型：** 字符向量 |
| **值：** 常量标量 |
| **默认值：** `'0'` |

### **Magnitude** — 输出的幅值 `0`（默认）| 实数值标量、向量或矩阵

输出信号的恒定幅值，指定为实数值
标量、向量或矩阵。

#### 依赖关系

要启用此参数，请将 **Input** 设置为
`Angle`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ConstantPart` |
| **类型：** 字符向量 |
| **值：** 实数值标量、向量或矩阵 |
| **默认值：** `'0'` |

### **Approximation method** — CORDIC 或无 `None`（默认）| `CORDIC`

指定用于计算输出的近似类型。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 您希望使用默认的泰勒级数算法。 |
| `CORDIC` | 浮点和定点 | 您希望进行快速近似计算。 |

当您使用 CORDIC 近似时，请遵循以下关于输入角度的准则：

- 对于有符号定点类型，输入角度必须落在范围 [–2π, 2π) rad 内。
- 对于无符号定点类型，输入角度必须落在范围 [0, 2π) rad 内。

模块使用以下数据类型传播规则：

| 幅值输入的数据类型 | 近似方法 | 复输出的数据类型 |
| --- | --- | --- |
| 浮点 | `None` 或 `CORDIC` | 与输入相同 |
| 有符号定点 | `CORDIC` | `fixdt`(1, *`WL`* + 2, *`FL`*)  其中 *`WL`* 和 *`FL`* 是幅值的字长和小数长度 |
| 无符号定点 | `CORDIC` | `fixdt`(1, *`WL`* + 3, *`FL`*)  其中 *`WL`* 和 *`FL`* 是幅值的字长和小数长度 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** 字符向量 |
| **值：** `'None' | 'CORDIC'` |
| **默认值：** `'None'` |

### **Number of iterations** — CORDIC 算法的迭代次数 `11`（默认）| 正整数，小于或等于定点输入的字长

执行 CORDIC 算法的迭代次数。可能的
值范围取决于输入的数据类型：

| 模块输入的数据类型 | 您可以指定的值 |
| --- | --- |
| 浮点 | 正整数 |
| 定点 | 不超过幅值输入的字长或相位角输入的字长的正整数，取两者中较小的值 |

#### 依赖关系

要启用此参数，请将 **Approximation
method** 设置为 `CORDIC`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumberOfIterations` |
| **类型：** 字符向量 |
| **值：** 正整数，小于或等于定点输入的字长 |
| **默认值：** `'11'` |

### **Scale output by reciprocal of gain factor** — 按增益因子的倒数缩放复输出的实部和虚部 `on`（默认）| `off`

选中此复选框可按因子 `(1/CORDIC gain)` 缩放复输出的实部和虚部。此值取决于
您指定的迭代次数。随着迭代次数的增加，
该值趋近于 1.647。

默认情况下选中此复选框，这会为复输出 `X + iY` 带来数值上
更精确的结果。但是，
缩放输出会增加两次额外的乘法运算，一次用于
`X`，一次用于 `Y`。

#### 依赖关系

要启用此参数，请将 **Approximation
method** 设置为 `CORDIC`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ScaleReciprocalGainFactor` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认值：** `'on'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此
参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |
## 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有多周期实现，这会在生成的代码中引入额外的
延迟。要查看增加的延迟，请查看
生成的模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**HDL 模块属性**

**常规**

| HDL 属性 | 描述 |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射为定点类型和浮点类型的 `MAX`、`Min`、`CUSTOM` 或 `ZERO` 延迟。默认值为 `MAX`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅 LatencyStrategy (HDL Coder)。 |

**原生浮点**

| HDL 属性 | 描述 |
| --- | --- |
| **HandleDenormals** | 指定您是否希望 HDL Coder 插入额外逻辑来处理设计中的非规格化数。非规格化数是幅值小于可表示的最小浮点数的数，其尾数中没有前导零。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **InputRangeReduction** | 指定您的输入范围是有界还是无界。如果您的输入范围无界，请启用此属性，以便 HDL Coder 插入额外逻辑将输入范围缩减到 `[-pi, pi]`。默认值为 `on`。另请参阅 InputRangeReduction (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，您可以控制目标 FPGA 设备上的 DSP 使用情况。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**定点支持**

您可以为 Magnitude-Angle to Complex 模块生成以定点
数据类型作为输入的代码。要为该模块生成定点数据类型的
代码，请将 **Input** 设置为 `Magnitude and
angle`，并将 **Approximation method** 设置为
`CORDIC`。使用 CORDIC 近似
方法时，模块会增加额外的延迟周期，如下表
所示。

| 架构 | 参数 | 额外延迟周期 |
| --- | --- | --- |
| `Pol2CartCordic` | **Number of iterations**  **Scale output by reciprocal of gain factor** | 当 **Scale output by reciprocal of gain factor** 参数为 `off` 时， *Max Latency* = **Number of iterations** + 1。 当 **Scale output by reciprocal of gain factor** 参数为 `on` 时， *Max Latency* = **Number of iterations** + 6。 |

**限制**

当您将
**Input** 设置为 `Magnitude` 或
`Angle` 时，不支持定点数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

当您将 **Approximation method** 设置为
`CORDIC` 时，Magnitude-Angle to Complex 模块支持定点和基础整数数据
类型。

## 版本历史

**在 R2006a 之前引入**

### R2024a: 使用定点数据类型生成 HDL 代码

从 R2024a 开始，您可以为使用定点数据类型作为输入的 Magnitude-Angle to Complex 模块
生成 HDL 代码。要生成定点数据
类型的代码，请将 **Input** 模块参数设置为 `Magnitude
and angle`，并将 **Approximation method**
参数设置为 `CORDIC`。使用 CORDIC 近似
方法时，您还可以启用 **Scale output by reciprocal of gain
factor**，以按增益因子缩放复输出的实部和虚部。

## 描述

将幅值和/或相位角信号转换为复信号

### 支持的操作

Magnitude-Angle to Complex 模块将幅值和相位角
输入转换为复输出。角度输入必须以 rad 为单位。

当有两个模块输入时，模块支持以下输入
维度组合：

- 两个维度相等的输入
- 一个标量输入和另一个 n 维数组

如果模块输入为数组，则输出为复信号数组。幅值输入向量的元素映射到相应复输出元素的幅值。类似地，角度输入向量的元素映射到相应复输出元素的角度。如果一个输入为标量，则它映射到所有复输出信号的相应分量（幅值或角度）。

### 超出范围输入对 CORDIC 近似的影响

如果您使用 CORDIC 近似方法 [1]，
则模块的相位角输入具有以下限制：

- 对于有符号定点类型，输入角度必须落在范围
  [–2π, 2π) rad 内。
- 对于无符号定点类型，输入角度必须落在范围
  [0, 2π) rad 内。

此表总结了超出范围输入的影响：

| 模块用法 | 超出范围输入的影响 |
| --- | --- |
| 仿真模式 | 出现错误。 |
| 生成的代码 | 出现未定义行为。 |

当您使用 CORDIC 近似时，请确保为
Magnitude-Angle to Complex 模块使用范围内的输入。避免依赖生成的代码或加速器模式下的未定义
行为。
