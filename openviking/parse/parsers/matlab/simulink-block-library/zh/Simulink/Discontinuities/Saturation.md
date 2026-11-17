---
type: simulink-block
title: 'Saturation'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'saturation'
documentation_source_path: 'slref/saturation.html'
language: zh-CN
chinese_source: worker-translation
---

# Saturation

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

饱和算法的输入信号。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，其值为输入信号、饱和上限或饱和下限。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **Upper limit** — 输入信号的饱和上限 `0.5`（默认）| 标量 | 向量

指定输入信号的上界。如果输入信号大于此边界，则输出信号被设置为该饱和值。**Upper limit** 参数使用舍入到最近值和饱和转换为输出数据类型。**Upper limit** 必须大于 **Output minimum** 参数且小于 **Output maximum** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperLimit` |
| **类型**：字符向量 |
| **Value**：实数标量或向量 |
| **默认值**：`'0.5'` |

### **Lower limit** — 输入信号的饱和下限 `-0.5`（默认）| 标量 | 向量

指定输入信号的下界。如果输入信号小于此边界，则输出信号被设置为该饱和值。**Lower limit** 参数使用舍入到最近值和饱和转换为输出数据类型。**Lower limit** 必须大于 **Output minimum** 参数且小于 **Output maximum** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerLimit` |
| **类型**：字符向量 |
| **Value**：实数标量或向量 |
| **默认值**：`'-0.5'` |

### **Treat as gain when linearizing** — 指定增益值 `on`（默认）| `off`

选择此参数可使命令将增益视为 1。Simulink® 软件中的线性化命令将此模块视为状态空间中的增益。清除此参数可使命令将增益视为 0。

#### 编程使用

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Enable zero-crossing detection** — 启用零穿越检测 `on`（默认）| `off`

选择以启用零穿越检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |

### 信号属性

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `OutMin` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `OutMax` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Same as input`（默认）| `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,2^0,0)` | `<data type expression>` | ...

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType` 对象）。有关详细信息，请参阅 Control Data Types of Signals。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Same as input'` | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `fixdt(1,16,2^0,0)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Same as input'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter：** | `LockScale` |
| **值**：| `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 指定定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

选择以下舍入模式之一。

`Ceiling`
:   将正数和负数均向正无穷方向舍入。等效于 MATLAB® 的 `ceil` 函数。

`Convergent`
:   将数字舍入到最接近的可表示值。如果出现平局，则舍入到最接近的偶数整数。等效于 Fixed-Point Designer™ 的 `convergent` 函数。

`Floor`
:   将正数和负数均向负无穷方向舍入。等效于 MATLAB 的 `floor` 函数。

`Nearest`
:   将数字舍入到最接近的可表示值。如果出现平局，则向正无穷方向舍入。等效于 Fixed-Point Designer 的 `nearest` 函数。

`Round`
:   将数字舍入到最接近的可表示值。如果出现平局，则将正数向正无穷方向舍入，将负数向负无穷方向舍入。等效于 Fixed-Point Designer 的 `round` 函数。

`Simplest`
:   自动在向 floor 舍入和向零舍入之间选择，以生成尽可能高效的舍入代码。

`Zero`
:   将数字向零方向舍入。等效于 MATLAB 的 `fix` 函数。

#### 编程使用

|  |
| --- |
| **模块参数**：`RndMeth` |
| **类型**：字符向量 |
| **值**：`'Ceiling'` | `'Convergent'` | `'Floor'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |
| **默认值**：`'Floor'` |

#### 另请参阅

有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

## 所属库

Simulink / Commonly Used Blocks Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL Architecture**

此模块具有一个默认 HDL 架构。

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入信号限制在饱和上限和下限值

Saturation 模块产生的输出信号是输入信号被限制在饱和上限和下限值之间的值。上限和下限由参数 **Upper limit** 和 **Lower limit** 指定。

| 输入 | 输出 |
| --- | --- |
| Lower limit ≤ 输入值 ≤ Upper limit | 输入值 |
| 输入值 < Lower limit | Lower limit |
| 输入值 > Upper limit | Upper limit |
