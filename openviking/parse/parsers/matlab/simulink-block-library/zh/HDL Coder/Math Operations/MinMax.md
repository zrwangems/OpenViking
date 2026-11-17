---
type: simulink-block
title: 'MinMax'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'minmax'
documentation_source_path: '../simulink/slref/minmax.html'
language: zh-CN
chinese_source: worker-translation
---

# MinMax

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_N
  summary: 第 *N* 个输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输入的最小值或最大值 标量 | 向量 | 矩阵
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

提供输入信号，模块从中输出最大值或最小值。

- 当模块只有一个输入端口时，输入必须是标量或向量。模块输出一个标量，等于输入向量的最小或最大元素。
- 当模块有多个输入端口时，所有非标量输入必须具有相同的维度。模块将任何标量输入扩展为与非标量输入具有相同的维度。模块输出与输入具有相同维度的信号。每个输出元素等于对应输入元素的最小值或最大值。

#### 依赖关系

要支持矩阵输入，必须将 **Number of input ports** 参数设置为大于 1 的整数。所有非标量输入必须具有相同的维度。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — 第 *N* 个输入信号 标量 | 向量 | 矩阵

提供输入信号，模块从中输出最大值或最小值。

当模块有多个输入端口时，所有非标量输入必须具有相同的维度。模块将任何标量输入扩展为与非标量输入具有相同的维度。模块输出与输入具有相同维度的信号。每个输出元素等于对应输入元素的最小值或最大值。

#### 依赖关系

要提供多个输入信号，请将 **Number of input ports** 设置为大于 1 的整数。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输入的最小值或最大值 标量 | 向量 | 矩阵

当模块只有一个输入时，输出为标量值，等于输入元素的最小值或最大值。当模块有多个输入时，输出为与输入具有相同维度的信号。每个输出元素等于对应输入元素的最小值或最大值。如果模块输入具有不同的输入数据类型，则输出与输入大小相同，但精度可能较低。例如，如果一个输入为 `int8`，一个为 `uint8`，则输出数据类型仍为 8 位 `sfix8_E1`，但精度较低。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Function
  summary: 指定最小值或最大值 min（默认）| max
  group: 主要
  block_parameter: Function
  type: 字符向量
  values: '''min'' | ''max'''
  default: '''min'''
- name: Number of input ports
  summary: 指定输入端口数量 1（默认）| 正整数
  group: 主要
  block_parameter: Inputs
  type: 字符向量
  values: 正整数
  default: '''1'''
- name: Apply over
  summary: 如何沿指定维度应用函数 All dimensions（默认）| Specified dimension
  group: 主要
  block_parameter: CollapseMode
  type: 字符向量
  values: '''All dimensions'' | ''Specified dimension'''
  default: '''All dimensions'''
- name: Dimension
  summary: 指定沿其应用函数的维度 1（默认）| 正整数 | ... | N
  group: 主要
  block_parameter: CollapseDim
  type: 字符向量
  values: 正整数
  default: '''1'''
- name: Enable zero-crossing detection
  summary: 启用零交叉检测 on（默认）| off
  group: 主要
  block_parameter: ZeroCross
  type: 字符向量 | 字符串
  values: '''off'' | ''on'''
  default: '''on'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
- name: Require all inputs to have the same data type
  summary: 输入必须具有相同的数据类型 off（默认）| on
  group: 信号属性
  block_parameter: InputSameDT
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output minimum
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: Output maximum
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: 信号属性
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: Output data type
  summary: '指定输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Inherit via back propagation | Inherit: Same as first
    input | double | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16,0) | fixdt(1,16,2^0,0)
    | <data type expression>'
  group: 信号属性
  block_parameter: OutDataTypeStr
  type: 字符向量
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Inherit via back propagation'' | ''Inherit: Same as first input''
    | ''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64''
    | ''uint64'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖 Output data type 的选项 off（默认）| on
  group: 信号属性
  block_parameter: LockScale
  values: '''off''（默认）| ''on'''
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 信号属性
  block_parameter: RndMeth
  values: '''Floor''（默认）| ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 信号属性
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
```

### 主要

### **Function** — 指定最小值或最大值 `min`（默认）| `max`

指定是对输入应用函数 `min` 还是 `max`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Function` |
| **类型：** 字符向量 |
| **值：** `'min' | 'max'` |
| **默认值：** `'min'` |

### **Number of input ports** — 指定输入端口数量 `1`（默认）| `正整数`

指定模块的输入数量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Inputs` |
| **类型：** 字符向量 |
| **值：** `正整数` |
| **默认值：** `'1'` |

### **Apply over** — 如何沿指定维度应用函数 `All dimensions`（默认）| `Specified dimension`

指定如何沿指定维度应用函数。

- `All dimensions` — 对所有维度的所有输入值应用函数。
- `Specified dimension` — 对指定维度的所有输入值应用函数。

例如，在此模型中，**Function** 设置为 `max`，**Apply over** 设置为 `All dimensions`。模块返回所有维度中的最大输入值。

以 Constant 模块值 [1 3 5;3 6 7;9 10 1] 的 2D 矩阵作为 MinMax 模块输入，配置为所有维度

#### 依赖关系

要启用此参数，**Number of input ports** 必须为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CollapseMode` |
| **类型：** 字符向量 |
| **值：** `'All dimensions'` | `'Specified dimension'` |
| **默认值：** `'All dimensions'` |

### **Dimension** — 指定沿其应用函数的维度 `1`（默认）| 正整数 | `...` | `N`

将沿其应用函数的维度指定为正整数。例如，对于 2-D 矩阵，`1` 对每列应用函数，`2` 对每行应用函数。

例如，在此模型中，**Function** 设置为 `max`，**Apply over** 设置为 `Specified dimension`，**Dimension** 设置为 `2`。模块返回每行中的最大输入值。

以 Constant 模块值 [1 3 5;3 6 7;9 10 1] 的 2D 矩阵作为 MinMax 模块输入，配置为维度 2

#### 依赖关系

要启用此参数，请将 **Apply over** 设置为 `Specified dimension`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CollapseDim` |
| **类型：** 字符向量 |
| **值：** 正整数 |
| **默认值：** `'1'` |

### **Enable zero-crossing detection** — 启用零交叉检测 `on`（默认）| `off`

选择以启用零交叉检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程用法

|  |
| --- |
| **模块参数**： `ZeroCross` |
| **类型**： 字符向量 | 字符串 |
| **值**： `'off'` | `'on'` |
| **默认值**： `'on'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 带引号的标量或向量 |

### 信号属性

### **Require all inputs to have the same data type** — 输入必须具有相同的数据类型 `off`（默认）| `on`

选中此复选框以要求所有输入具有相同的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputSameDT` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

软件使用最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

软件使用最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 指定输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

当输入是小于单精度的浮点数据类型时，`Inherit: Inherit via internal rule` 输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当编码数据类型所需的位数小于编码单精度数据类型所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

#### 编程用法

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**： `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

指定溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的适当值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，表示为 `int8` 的模块结果 130（二进制 1000 0010）为 -126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成的代码中提供显式饱和保护时，请考虑选择此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和应用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |
## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 额外延迟周期 | 描述 |
| --- | --- | --- |
| `Tree` `(默认)` | 0 | 生成比较器的树结构。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射到浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2024a：MinMax 模块支持指定维度

MinMax 模块使您能够使用以下新参数查找指定维度上的最小值或最大值：

- **Apply over** — 对所有维度或指定维度应用函数。
- **Dimension** — 沿其应用函数的维度。

## 描述

输出输入的最小值或最大值

MinMax 模块输出输入的最小或最大元素。通过设置 **Function** 参数，您可以选择模块输出最小值还是最大值。

MinMax 模块忽略任何为 `NaN` 的输入值，除非所有输入值均为 `NaN`。当所有输入值均为 `NaN` 时，输出为 `NaN`，可以是标量或每个输出向量元素的值。
