---
type: simulink-block
title: 'Constant'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'MAT'
documentation_page: 'constant'
documentation_source_path: '../dsp/ref/constant.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant

## 端口
```yaml
ports:
- name: Port_1
  summary: 常量值 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### 输出

### **Port\_1** — 常量值 标量 | 向量 | 矩阵 | N 维数组

常量值，指定为实值或复值标量、向量、矩阵或 N 维数组。默认情况下，Constant 模块输出的信号的维度、数据类型和复数性与 **Constant value** 参数相同。但是，您可以将输出指定为 Simulink® 支持的任何数据类型，包括定点数据类型和枚举数据类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Constant value
  summary: 常量输出值 标量 | 向量 | 矩阵 | N 维数组
  group: 主要
  block_parameter: Value
  values: 带引号的标量 | 带引号的向量 | 带引号的矩阵 | 带引号的数组
- name: Interpret vector parameters as 1-D
  summary: 将向量视为一维 on (默认) | off
  group: 主要
  block_parameter: VectorParams1D
  values: '''on'' (默认) | ''off'''
- name: Sample time
  summary: 采样间隔 inf (默认) | 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  values: '''inf'' (默认) | 带引号的标量 | 带引号的向量'
- name: Output minimum
  summary: 用于范围检查的最小输出值 [] (默认) | 标量
  group: 信号属性
  block_parameter: OutMin
  values: '''[ ]'' (默认) | 带引号的标量'
- name: Output maximum
  summary: 用于范围检查的最大输出值 [] (默认) | 标量
  group: 信号属性
  block_parameter: OutMax
  values: '''[ ]'' (默认) | 带引号的标量'
- name: Output data type
  summary: '输出数据类型 Inherit: Inherit from ''Constant value'' (默认) | Inherit: Inherit via back propagation | double | single
    | half | int8 | int16 | ...'
  group: 信号属性
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit from ''Constant value'''' (默认) | ''Inherit: Inherit via back propagation'' | ''double'' | ''single''
    | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''boolean''
    | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''Enum: <class name>'' | ''Bus: <object name>'' | ''ValueType:
    <object name>'' | ''<data type expression>'''
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖 Output data type off (默认) | on
  group: 信号属性
  block_parameter: LockScale
  values: '''off'' (默认) | ''on'''
- name: Mode
  summary: 要指定的数据类别 Inherit (默认) | Built in | Fixed point | Enumerated | Bus object | Value type | Expression
  group: 信号属性
- name: Data type override
  summary: 为此信号指定数据类型覆盖模式 Inherit | Off
  group: 信号属性
- name: Signedness
  summary: 指定有符号或无符号 Signed (默认) | Unsigned
  group: 信号属性
- name: Scaling
  summary: 定点数据的定标方法 Best precision (默认) | Binary point | Slope and bias
  group: 信号属性
- name: Word length
  summary: 保存量化整数的字长位数 16 (默认) | 0 到 32 的整数
  group: 信号属性
- name: Fraction length
  summary: 指定定点数据类型的小数长度 0 (默认) | 标量整数
  group: 信号属性
- name: Slope
  summary: 指定定点数据类型的斜率 2^0 (默认) | 正实值标量
  group: 信号属性
- name: Bias
  summary: 指定定点数据类型的偏置 0 (默认) | 实值标量
  group: 信号属性
```

### 主要

### **Constant value** — 常量输出值 标量 | 向量 | 矩阵 | N 维数组

指定模块的常量值输出。

默认值取决于您添加的模块。

- `1` — Constant 或 One 模块
- `0` — Zero 模块
- `inf` — Inf 模块
- `-inf` — Negative Inf 模块
- `exp(1)` — Eulers Number 模块
- `pi` — Pi 模块
- `NaN` — NaN 模块

您可以输入 MATLAB 将其计算为矩阵的任何表达式，包括布尔关键字 `true` 和 `false`。

如果将 **Output data type** 设置为总线对象，则可以指定以下选项之一：

- 与总线对象对应的完整 MATLAB 结构体
- `0`，表示与总线对象的接地值对应的结构体

有关详细信息，请参阅 Using Bus Objects as the Output Data Type。

对于非总线数据类型，Simulink 会离线将此参数从其值数据类型转换为指定的输出数据类型，使用最近舍入方法和饱和溢出操作。

#### 依赖关系

当 **Output data type** 指定 `Simulink.ValueType` 对象时，软件会忽略常量值的数据类型。

当此参数指定 `Simulink.Parameter` 对象且 **Output data type** 指定 `Simulink.ValueType` 对象时：

- 模块使用 `Simulink.ValueType` 对象指定的最小值、最大值和数据类型。
- 模块使用 `Simulink.Parameter` 对象指定的单位。
- 两个对象指定的维度和复数性必须匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Value` |
| **值：** | 带引号的标量 | 带引号的向量 | 带引号的矩阵 | 带引号的数组 |
| **数据类型：** | `char` | `string` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on` (默认) | `off`

如果 **Constant value** 参数计算为 `N` 元素行向量或列向量，则选中此复选框以输出长度为 `N` 的向量。

- 选中此复选框时，如果 **Constant value** 参数计算为 `N` 元素行向量或列向量，则模块输出长度为 `N` 的向量。
- 清除此复选框时，如果 **Constant value** 参数计算为 `N` 元素行向量或列向量，则模块输出维度为 1×`N` 或 `N`×1 的矩阵。例如，模块输出维度为 1×`N` 或 `N`×1 的矩阵。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `VectorParams1D` |
| **值：** | `'on'` (默认) | `'off'` |

### **Sample time** — 采样间隔 `inf` (默认) | 标量 | 向量

指定 Constant 模块输出在仿真期间可以变化的时间间隔，例如由于调整 **Constant value** 参数。

`inf` 的默认值表示模块输出永远不会变化。此设置通过避免重新计算模块输出的需要来加速仿真和生成代码。

有关详细信息，请参阅 Specify Sample Time (Simulink)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `'inf'` (默认) | 带引号的标量 | 带引号的向量 |
| **数据类型：** | `char` | `string` |

### 信号属性

### **Output minimum** — 用于范围检查的最小输出值 `[]` (默认) | 标量

将软件检查的输出范围的下限值指定为有限、实数、双精度标量值。

软件使用最小值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 依赖关系

当 **Output data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最小值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[ ]'` (默认) | 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]` (默认) | 标量

将软件检查的输出范围的上限值指定为有限、实数、双精度标量值。

软件使用最大值来执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)）用于某些模块。
- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 依赖关系

当 **Output data type** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件会忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最大值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[ ]'` (默认) | 带引号的标量 |

### **Output data type** — 输出数据类型 `Inherit: Inherit from 'Constant value'` (默认) | `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `int16` | ...

指定输出数据类型。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

您可以指定以下任一选项：

- 继承的数据类型
- 内置 Simulink 数据类型 — 例如，指定 `single` 或 `uint8`。请参阅 Data Types Supported by Simulink (Simulink)。
- 定点数据类型 — 使用 `fixdt` (Simulink) 函数。例如，指定 `fixdt(1,16,0)`。
- 枚举数据类型 — 使用类型名称，前面加 `Enum:`。例如，指定 `Enum: myEnumType`。
- 总线数据类型 — 使用 `Simulink.Bus` (Simulink) 对象的名称，前面加 `Bus:`。例如，指定 `Bus: myBusObject`。
- 值类型 *(自 R2023b 起)* — 使用 `Simulink.ValueType` (Simulink) 对象的名称，前面加 `ValueType:`。例如，指定 `ValueType: windVelocity`。您指定的值类型必须将 `DimensionsMode` 设置为 `'Fixed'`。
- 自定义数据类型 — 使用指定类型的 MATLAB 表达式。例如，您可以指定一个 `Simulink.NumericType` (Simulink) 对象，其 `DataTypeMode` 属性设置为 `'Fixed-point: unspecified scaling'` 以外的值。

当您将 `Simulink.ValueType` 或 `Simulink.Bus` 对象指定为数据类型时，Constant 模块的 **Output minimum** 和 **Output maximum** 参数将被忽略。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象的相应属性。例如，假设某个模块将 **Output minimum** 设置为 `0`。当该模块的 **Output data type** 指定一个最小值为 `1` 的 `ValueType` 对象时，模块使用 `1` 而不是 `0` 作为其最小值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit from 'Constant value''` (默认) | `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'ValueType: <object name>'` | `'<data type expression>'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type `off` (默认) | `on`

选中此参数可防止定点工具覆盖您在模块上指定的 **Output data type**。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'` (默认) | `'on'` |

### **Mode** — 要指定的数据类别 `Inherit` (默认) | `Built in` | `Fixed point` | `Enumerated` | `Bus object` | `Value type` | `Expression`

选择要指定的数据类别。

- `Inherit` — 数据类型的继承规则。选择 `Inherit` 会启用右侧的第二个菜单。选择以下选项之一：

  - `Inherit from 'Constant value'` (默认)
  - `Inherit via back propagation`
- `Built in` — 内置数据类型。选择 `Built in` 会启用右侧的第二个菜单。选择以下选项之一：

  - `double` (默认)
  - `single`
  - `half`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `int64`
  - `uint64`
  - `boolean`
- `Fixed point` — 定点数据类型。
- `Enumerated` — 枚举数据类型。选择 `Enumerated` 会启用右侧的文本框，您可以在其中输入类名。
- `Bus object` — 总线对象。选择 `Bus object` 会启用右侧的文本框，您可以在其中输入要用于定义总线结构的总线对象名称。要创建或更改总线对象，请点击文本框右侧的 **Edit**。
- `Value type` *(自 R2023b 起)* — 值类型。选择 `Value type` 会启用右侧的文本框，您可以在其中输入要用于定义输出信号属性的值类型名称。要创建或更改值类型，请点击文本框右侧的 **Edit**。
- `Expression` — 计算为数据类型的表达式。选择 `Expression` 会启用右侧的文本框，您可以在其中输入表达式。

  不要将总线对象指定为表达式。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

为此信号选择数据类型覆盖模式。

- 当您选择 `Inherit` 时，软件从其上下文（即使用该信号的模块、`Simulink.Signal` 对象或 Stateflow® 图）继承数据类型覆盖设置。
- 当您选择 `Off` 时，软件忽略其上下文的数据类型覆盖设置，并使用为信号指定的定点数据类型。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

要启用此参数，请点击 **Show data type assistant** 按钮，并将 **Mode** 设置为 `Built in` 或 `Fixed point`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力在应用数据类型覆盖时提供了对模型中数据类型的更大控制。例如，您可以使用此选项确保数据类型满足下游模块的要求，而不管数据类型覆盖设置如何。

### **Signedness** — 指定有符号或无符号 `Signed` (默认) | `Unsigned`

指定定点数据是有符号还是无符号。有符号数据可以表示正值和负值，但无符号数据仅表示正值。

- `Signed`，将定点数据指定为有符号。
- `Unsigned`，将定点数据指定为无符号。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Scaling** — 定点数据的定标方法 `Best precision` (默认) | `Binary point` | `Slope and bias`

指定定点数据的定标方法，以避免溢出条件并最小化量化误差。有关详细信息，请参阅 Specifying a Fixed-Point Data Type (Simulink)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Word length** — 保存量化整数的字长位数 `16` (默认) | 0 到 32 的整数

指定保存量化整数的字长位数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type (Simulink)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 指定定点数据类型的小数长度 `0` (默认) | 标量整数

将定点数据类型的小数长度指定为正整数或负整数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type (Simulink)。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Binary point`。

### **Slope** — 指定定点数据类型的斜率 `2^0` (默认) | 正实值标量

指定定点数据类型的斜率。有关详细信息，请参阅 Specifying a Fixed-Point Data Type (Simulink)。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。

### **Bias** — 指定定点数据类型的偏置 `0` (默认) | 实值标量

将定点数据类型的偏置指定为任意实数。有关详细信息，请参阅 Specifying a Fixed-Point Data Type (Simulink)。

#### 依赖关系

要启用此参数，请将 **Scaling** 设置为 `Slope and bias`。
## 所属库

Simulink / Commonly Used Blocks Simulink / Sources DSP System Toolbox / Sources HDL Coder / Commonly Used Blocks HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**可调参数**

您可以在用于 HDL 代码生成的 Constant 模块中使用可调参数。有关详细信息，请参阅 Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

| 架构 | 参数 | 描述 |
| --- | --- | --- |
| `default`  `Constant` | 无 | 此实现输出 Constant 模块的值。 |
| `Logic Value` | 无 | 默认情况下，此实现为信号中的每一位输出字符 `'Z'`。例如，对于 4 位信号，该实现将输出 `'ZZZZ'`。 |
| `{'Value', 'Z'}` | 如果信号处于高阻态，请使用此参数值。此实现为信号中的每一位输出字符 `'Z'`。例如，对于 4 位信号，该实现将输出 `'ZZZZ'`。 |
| `{'Value', 'X'}` | 如果信号处于未知状态，请使用此参数值。此实现为信号中的每一位输出字符 `'X'`。例如，对于 4 位信号，该实现将输出 `'XXXX'`。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

- `Logic Value` 实现不支持 `double` 数据类型。如果您为 `double` 类型的常量值指定此实现，将发生代码生成错误。
- 当无限采样时间传播到被测设备（DUT）输出时，延迟平衡不支持 **Sample time** 设置为 `inf` 的 Constant 模块。如果在 HDL 代码生成期间出现无限采样率错误，请将 **Sample time** 设置为 `-1`。

**`Simulink.ValueType` 对象支持**

此模块支持 `Simulink.ValueType` 对象的代码生成。有关值类型的更多信息，请参阅 Specify Common Set of Signal Properties as Value Type (Simulink)。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2023b：将 **Output data type** 设置为 `Simulink.ValueType` 对象

**Output data type** 参数支持具有固定维度的 `Simulink.ValueType` (Simulink) 对象。

当您将值类型指定为 Constant 模块的数据类型时，值类型将覆盖模块指定的最小值和最大值以及常量值的数据类型。值类型会验证常量值的维度、复数和单位。当这些属性不匹配时，软件会发出警告或错误。

例如，假设一个 Constant 模块具有：

- **Constant value** 设置为单位为 `ft/s` 的 `Simulink.Parameter` 对象
- **Output data type** 设置为单位为 `m/s` 的 `Simulink.ValueType` 对象

在模型编译期间，软件会发出有关单位不匹配的警告。Constant 模块使用 `ft/s` 作为单位。

再举一个例子，假设一个 Constant 模块具有：

- **Constant value** 设置为 `[2 3]`
- **Output data type** 设置为维度为 `1` 的 `Simulink.ValueType` 对象

在模型编译期间，软件会发出有关维度不匹配的错误。复数不匹配也会导致错误。

Constant 模块不使用值类型的描述。

有关值类型的更多信息，请参阅 Specify Common Set of Signal Properties as Value Type (Simulink)。

## 描述

常量值

Constant 模块生成实数或复数常量值信号。使用此模块提供常量信号输入。该模块生成标量、向量或矩阵输出，具体取决于：

- **Constant value** 参数的维度
- **Interpret vector parameters as 1-D** 参数的设置

模块的输出具有与 **Constant value** 参数相同的维度和元素。如果您为此参数指定了一个希望模块将其解释为向量的向量，请选中 **Interpret vector parameters as 1-D** 复选框。否则，如果您为 **Constant value** 参数指定了一个向量，模块会将该向量视为矩阵。

**提示**

要输出常量枚举值，请考虑改用 Enumerated Constant (Simulink) 模块。Constant 模块提供了不适用于枚举类型的模块参数，例如 **Output minimum** 和 **Output maximum**。

### 使用总线对象作为输出数据类型

Constant 模块支持将非虚拟总线作为输出数据类型。使用总线对象作为输出数据类型可以帮助简化您的模型。如果您使用总线对象作为输出数据类型，请将 **Constant value** 设置为 `0` 或与总线对象匹配的 MATLAB® 结构体。

### 使用结构体作为总线的常量值

您指定的结构体必须包含总线对象所表示的总线的每个元素的值。模块输出是非虚拟总线信号。

您可以使用 `Simulink.Bus.createMATLABStruct` (Simulink) 创建与总线对应的完整结构体。

您可以使用 `Simulink.Bus.createObject` (Simulink) 从 MATLAB 结构体创建总线对象。

如果输出总线中的信号元素使用 `double` 以外的数值数据类型，您可以使用类型化表达式（如 `uint16(37)`）或非类型化表达式（如 `37`）来指定结构体字段。要控制字段数据类型，您可以将总线对象用作 `Simulink.Parameter` 对象的数据类型。要决定使用类型化还是非类型化表达式，请参阅 Control Data Types of Initial Condition Structure Fields (Simulink)。

### 设置配置参数以支持使用总线对象数据类型

要启用将总线对象用作输出数据类型，请在开始仿真之前，将 **Configuration Parameters** > **Diagnostics** > **Data Validity** > **Advanced parameters** > **Underspecified initialization detection** 设置为 `Simplified`。有关更多信息，请参阅 Underspecified initialization detection (Simulink)。
