---
type: simulink-block
title: 'Magnitude-Angle to Complex'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Math Operations'
documentation_page: 'magnitudeangletocomplex'
documentation_source_path: 'slref/magnitudeangletocomplex.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnitude-Angle to Complex

## 端口

### 输入

### **|u|** — 幅值标量 | 向量 | 矩阵

幅值，指定为实值标量、向量或矩阵。

#### 依赖关系

- 要启用此端口，请将 **输入** 设置为 `Magnitude and angle`。

#### 限制

- 如果一个输入具有浮点数据类型，则另一个输入必须使用相同的数据类型。例如，两个信号都必须是 `double` 或 `single`。
- 仅当将 **近似方法** 设置为 `CORDIC` 时，才支持定点数据类型。当一个输入具有定点数据类型时，另一个输入也必须具有定点数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **∠u** — 弧度相位角标量 | 向量 | 矩阵

弧度相位角，指定为实值标量、向量或矩阵。要计算 CORDIC 近似，输入角度必须在以下范围内：

- [–2π, 2π) rad，对于有符号定点类型
- [0, 2π) rad，对于无符号定点类型

有关更多信息，请参阅越界输入对 CORDIC 近似的影响。

#### 依赖关系

- 要启用此端口，请将 **输入** 设置为 `Magnitude and angle`。

#### 限制

- 如果一个输入具有浮点数据类型，则另一个输入必须使用相同的数据类型。例如，两个信号都必须是 `double` 或 `single`。
- 仅当将 **近似方法** 设置为 `CORDIC` 时，才支持定点数据类型。当一个输入具有定点数据类型时，另一个输入也必须具有定点数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_1** — 幅值或弧度相位角标量 | 向量 | 矩阵

幅值，或弧度相位角，指定为实值标量、向量或矩阵。

- 当将 **输入** 设置为 `Magnitude` 时，在输入端口指定幅值，在对话框中指定角度。
- 当将 **输入** 设置为 `Angle` 时，在输入端口指定角度，在对话框中指定幅值。

#### 依赖关系

要启用此端口，请将 **输入** 设置为 `Magnitude` 或 `Angle`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 复信号标量 | 向量 | 矩阵

由指定的幅值和相位角形成的复信号。

如果模块输入是数组，则输出是复信号数组。幅值输入向量的元素映射到对应复输出元素的幅值。类似地，角度输入向量的元素映射到对应复输出元素的角度。如果一个输入是标量，则它映射到所有复输出信号的对应分量（幅值或角度）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **输入** — 输入类型 `Magnitude`（默认） | `Angle` | `Magnitude and angle`

指定输入类型：幅值输入、角度输入或两者。

#### 编程使用

|  |
| --- |
| **模块参数：** `Input` |
| **类型：** 字符向量 |
| **值：** `'Magnitude' | 'Angle' | 'Magnitude and angle'` |
| **默认：** `'Magnitude and angle'` |

### **角度** — 输出的相位角 `0`（默认） | 实值标量、向量或矩阵

输出信号的恒定相位角，以 rad 为单位。要计算 CORDIC 近似，输入角度必须在以下范围内：

- [–2π, 2π) rad，对于有符号定点类型
- [0, 2π) rad，对于无符号定点类型

有关更多信息，请参阅越界输入对 CORDIC 近似的影响。

#### 依赖关系

要启用此参数，请将 **输入** 设置为 `Magnitude`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ConstantPart` |
| **类型：** 字符向量 |
| **值：** 常量标量 |
| **默认：** `'0'` |

### **幅值** — 输出的幅值 `0`（默认） | 实值标量、向量或矩阵

输出信号的恒定幅值，指定为实值标量、向量或矩阵。

#### 依赖关系

要启用此参数，请将 **输入** 设置为 `Angle`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ConstantPart` |
| **类型：** 字符向量 |
| **值：** 实值标量、向量或矩阵 |
| **默认：** `'0'` |

### **近似方法** — CORDIC 或无 `None`（默认） | `CORDIC`

指定用于计算输出的近似类型。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 您想使用默认的泰勒级数算法。 |
| `CORDIC` | 浮点和定点 | 您想要快速、近似的计算。 |

使用 CORDIC 近似时，请遵循以下输入角度准则：

- 对于有符号定点类型，输入角度必须落在范围 [–2π, 2π) rad 内。
- 对于无符号定点类型，输入角度必须落在范围 [0, 2π) rad 内。

该模块使用以下数据类型传播规则：

| 幅值输入的数据类型 | 近似方法 | 复输出的数据类型 |
| --- | --- | --- |
| 浮点 | `None` 或 `CORDIC` | 与输入相同 |
| 有符号定点 | `CORDIC` | `fixdt`(1, *`WL`* + 2, *`FL`*) 其中 *`WL`* 和 *`FL`* 是幅值的字长和小数长度 |
| 无符号定点 | `CORDIC` | `fixdt`(1, *`WL`* + 3, *`FL`*) 其中 *`WL`* 和 *`FL`* 是幅值的字长和小数长度 |

#### 编程使用

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** 字符向量 |
| **值：** `'None' | 'CORDIC'` |
| **默认：** `'None'` |

### **迭代次数** — CORDIC 算法的迭代次数 `11`（默认） | 小于或等于定点输入字长的正整数

执行 CORDIC 算法的迭代次数。可能值的范围取决于输入的数据类型：

| 模块输入的数据类型 | 可指定的值 |
| --- | --- |
| 浮点 | 正整数 |
| 定点 | 不超过幅值输入字长或相位角输入字长的较小值的正整数 |

#### 依赖关系

要启用此参数，请将 **近似方法** 设置为 `CORDIC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumberOfIterations` |
| **类型：** 字符向量 |
| **值：** 小于或等于定点输入字长的正整数 |
| **默认：** `'11'` |

### **按增益因子倒数缩放输出** — 缩放复输出的实部和虚部 `on`（默认） | `off`

选中此复选框可按 `(1/CORDIC gain)` 因子缩放复输出的实部和虚部。此值取决于您指定的迭代次数。随着迭代次数增加，该值趋近于 1.647。

默认情况下会选中此复选框，这会使复输出 `X + iY` 在数值上更准确。但是，缩放输出会增加两次额外乘法运算，一次用于 `X`，一次用于 `Y`。

#### 依赖关系

要启用此参数，请将 **近似方法** 设置为 `CORDIC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ScaleReciprocalGainFactor` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认：** `'on'` |

### **采样时间（-1 表示继承）** — 采样之间的间隔 `-1`（默认） | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关更多信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的标量或向量 |

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

HDL Coder™ 提供了会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有多周期实现，会在生成代码中引入额外延迟。要查看增加的延迟，请查看生成模型或验证模型。请参阅 Generated Model and Validation Model (HDL Coder)。

**HDL 模块属性**

**常规**

| HDL 属性 | 描述 |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **LatencyStrategy** | 指定是否将设计中的模块映射为定点类型和浮点类型的 `MAX`、`Min`、`CUSTOM` 或 `ZERO` 延迟。默认值为 `MAX`。另请参阅 LatencyStrategy (HDL Coder)。 |
| **CustomLatency** | 当 **LatencyStrategy** 设置为 `CUSTOM` 时，使用此属性为定点类型指定介于 `ZERO` 和 `MAX` 之间的自定义延迟值。另请参阅 LatencyStrategy (HDL Coder)。 |

**本机浮点**

| HDL 属性 | 描述 |
| --- | --- |
| **HandleDenormals** | 指定是否希望 HDL Coder 插入附加逻辑来处理设计中的非规格化数。非规格化数是幅值小于最小浮点数的数，该浮点数可在尾数中没有前导零的情况下表示。默认值为 `inherit`。另请参阅 HandleDenormals (HDL Coder)。 |
| **InputRangeReduction** | 指定您的输入范围是有界还是无界。如果输入范围无界，请启用此属性，以便 HDL Coder 插入附加逻辑将输入范围缩减到 `[-pi, pi]`。默认值为 `on`。另请参阅 InputRangeReduction (HDL Coder)。 |
| **MantissaMultiplyStrategy** | 指定在代码生成期间如何实现尾数乘法运算。通过使用不同的设置，可以控制目标 FPGA 设备上的 DSP 使用情况。默认值为 `inherit`。另请参阅 MantissaMultiplyStrategy (HDL Coder)。 |

**定点支持**

您可以为具有定点数据类型输入的 Magnitude-Angle to Complex 模块生成代码。要为该模块生成具有定点数据类型的代码，请将 **输入** 设置为 `Magnitude and angle`，并将 **近似方法** 设置为 `CORDIC`。使用 CORDIC 近似方法时，该模块会按下表增加额外延迟周期。

| 架构 | 参数 | 附加延迟周期 |
| --- | --- | --- |
| `Pol2CartCordic` | **迭代次数**  **按增益因子倒数缩放输出** | 当 **按增益因子倒数缩放输出** 参数为 `off` 时，*Max Latency* = **迭代次数** + 1。当 **按增益因子倒数缩放输出** 参数为 `on` 时，*Max Latency* = **迭代次数** + 6。 |

**限制**

当将 **输入** 设置为 `Magnitude` 或 `Angle` 时，不支持定点数据类型。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

当将 **近似方法** 设置为 `CORDIC` 时，Magnitude-Angle to Complex 模块支持定点数据类型和基础整数数据类型。

## 版本历史

**在 R2006a 之前引入**

### R2024a: 使用定点数据类型生成 HDL 代码

从 R2024a 开始，您可以为使用定点数据类型作为输入的 Magnitude-Angle to Complex 模块生成 HDL 代码。要使用定点数据类型生成代码，请将 **输入** 模块参数设置为 `Magnitude and angle`，并将 **近似方法** 参数设置为 `CORDIC`。使用 CORDIC 近似方法时，您还可以启用 **按增益因子倒数缩放输出**，以按增益因子缩放复输出的实部和虚部。

## 描述

将幅值和/或相位角信号转换为复信号

### 支持的操作

Magnitude-Angle to Complex 模块将幅值和相位角输入转换为复输出。角度输入必须以 rad 为单位。

当模块有两个输入时，该模块支持以下输入维度组合：

- 两个维度相等的输入
- 一个标量输入，另一个为 n 维数组

如果模块输入是数组，则输出是复信号数组。幅值输入向量的元素映射到对应复输出元素的幅值。类似地，角度输入向量的元素映射到对应复输出元素的角度。如果一个输入是标量，则它映射到所有复输出信号的对应分量（幅值或角度）。

### 越界输入对 CORDIC 近似的影响

如果使用 CORDIC 近似方法 [1]，则相位角的模块输入具有以下限制：

- 对于有符号定点类型，输入角度必须落在范围 [–2π, 2π) rad 内。
- 对于无符号定点类型，输入角度必须落在范围 [0, 2π) rad 内。

下表总结了越界输入的影响：

| 模块使用 | 越界输入的影响 |
| --- | --- |
| 仿真模式 | 出现错误。 |
| 生成的代码 | 发生未定义行为。 |

使用 CORDIC 近似时，请确保为 Magnitude-Angle to Complex 模块使用范围内的输入。避免依赖生成代码或加速器模式下的未定义行为。
