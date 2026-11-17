---
type: simulink-block
title: 'MATLAB Function'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'USR'
documentation_page: 'matlabfunction'
documentation_source_path: '../simulink/slref/matlabfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# MATLAB Function

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入变量 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | string | fixed
    point | enumerated | bus
- name: Port_1
  summary: 输出变量 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | string | fixed
    point | enumerated | bus
```

### 输入

### **Port\_1** — 输入变量 标量 | 向量 | 矩阵

MATLAB 函数中的输入变量，指定为实值标量、向量或矩阵。每个输入变量都有一个关联的端口，该端口使用变量的名称。

不能在 Simulink 模型和 MATLAB Function 模块中的函数之间传递 MATLAB 支持但 Simulink 不支持的数据类型。可以在 MATLAB Function 模块中使用这些数据类型。

有关此模块的定点数据类型支持的详细信息，请参阅 Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer) 和 Data Type Override with MATLAB Function Block (Fixed-Point Designer)。

#### 依赖关系

要创建输入端口，请打开模块并在 **Symbols** 窗格中创建输入变量。请参阅 Create and Define MATLAB Function Block Variables。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出变量 标量 | 向量 | 矩阵

MATLAB 函数中的输出变量，指定为实值标量、向量或矩阵。每个输出变量都有一个关联的端口，该端口使用变量的名称。

#### 依赖关系

要创建输出端口，请打开模块并在 **Symbols** 窗格中创建输出变量。请参阅 Create and Define MATLAB Function Block Variables。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Update method
  summary: 用于激活模块的方法 Inherited（默认）| Discrete | Continuous
  group: ''
  block_parameter: ChartUpdate
  values: '"INHERITED"（默认）| "CONTINUOUS" | "DISCRETE"'
- name: Sample time
  summary: 模块在仿真期间激活的时间间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 标量 | 向量'
- name: Saturate on integer overflow
  summary: 数据在整数溢出时是否饱和 on（默认）| off
  group: 高级
  block_parameter: SaturateOnIntegerOverflow
  values: true 或 1（默认）| false 或 0
- name: Support variable-size arrays
  summary: 模块是否支持可变大小数据 on（默认）| off
  group: 高级
  block_parameter: SupportVariableSizing
  values: true 或 1（默认）| false 或 0
- name: Allow direct feedthrough
  summary: 模块是否支持直接馈通语义 on（默认）| off
  group: 高级
  block_parameter: AllowDirectFeedthrough
  values: true 或 1（默认）| false 或 0
- name: Interpret output column vectors as one-dimensional data
  summary: 模块是否将长度为 1 的维度的输出变量视为固定大小 off（默认）| on
  group: 高级
  block_parameter: VectorOutputs1D
  values: false 或 0（默认）| true 或 1
- name: Treat dimensions of length 1 as fixed size
  summary: 至少有一个长度为 1 的维度的变量是否为固定大小 on（默认）| off
  group: 高级
  block_parameter: TreatDimensionOfLengthOneAsFixedSize
  values: true 或 1（默认）| false 或 0
- name: Treat these inherited Simulink signal types as fi objects
  summary: 要视为 fi 对象的继承 Simulink 信号 Fixed-point（默认）| Fixed-point & Integer
  group: 定点属性
  block_parameter: TreatAsFi
  values: '"Fixed-point"（默认）| "Fixed-point & Integer"'
- name: MATLAB function fimath
  summary: 默认 fimath 属性 Same as MATLAB（默认）| Specify Other
  group: 定点属性
  block_parameter: EmlDefaultFimath
  values: '"Same as MATLAB Default"（默认）| "Other:UserSpecified"'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

**注意**

MATLAB Function 模块还具有子系统模块参数，您可以通过右键单击模块并单击 **Block Parameters (Subsystem)** 来访问这些参数。但是，不建议更新这些模块参数。

### **Update method** — 用于激活模块的方法 `Inherited`（默认）| `Discrete` | `Continuous`

将激活 MATLAB Function 模块的方法指定为以下值之一：

- `Inherited` — 来自 Simulink 模型的输入激活 MATLAB Function 模块。

  如果定义输入触发器，MATLAB Function 模块将响应触发器端口上的 Simulink 信号或函数调用事件而执行。如果未定义输入触发器，MATLAB Function 模块将隐式继承来自模型的触发器。这些隐式事件是为模块提供输入的信号的离散或连续采样时间。

  如果定义数据输入，MATLAB Function 模块以最快数据输入的速率进行采样。如果未定义数据输入，MATLAB Function 模块以父子系统执行行为定义的速率进行采样。
- `Discrete` — MATLAB Function 模块使用在模块的 **Sample time** 参数中指定的速率激活。模块以与指定速率对应的固定时间间隔生成隐式事件。模型中的其他模块可以具有不同的采样时间。
- `Continuous` — MATLAB Function 模块仅在主时间步期间激活，并在主时间步和次时间步期间计算输出和局部连续变量。模块可以注册零交叉，这允许 Simulink 模型在状态变化发生时对模块进行采样。模块计算局部连续变量的导数。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

如果使用 `MATLABFunctionConfiguration` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数：** | `UpdateMethod` |
| **值：** | `"Inherited"`（默认）| `"Continuous"` | `"Discrete"` |

如果使用 `Stateflow.EMChart` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数：** | `ChartUpdate` |
| **值：** | `"INHERITED"`（默认）| `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample time** — 模块在仿真期间激活的时间间隔 `-1`（默认）| 标量 | 向量

指定 MATLAB Function 模块在仿真期间激活的时间间隔。默认值表示模块从 Simulink 继承采样时间。有关指定采样时间的详细信息，请参阅 Specify Sample Time。

不要使用子系统模块参数中的 **Sample Time** 参数。而应使用属性检查器。

#### 依赖关系

要启用此参数，请将 **Update method** 设置为 `Discrete`。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| 标量 | 向量 |
| **数据类型：** | `string` | `char` |

### 高级

### **Saturate on integer overflow** — 数据在整数溢出时是否饱和 `on`（默认）| `off`

将 MATLAB Function 模块中的数据在整数溢出时是否饱和指定为以下值之一：

- `on` — 模块通过将整数设置为字长允许的最大正值或负值来使其饱和。此设置与 MATLAB 行为一致。
- `off` — 在仿真模式下发生溢出条件时，模块生成运行时错误。使用 Simulink Coder 生成代码时，行为取决于您的 C 语言编译器。

#### 提示

- 当此参数为 `on` 时，MATLAB 在仿真期间添加额外检查以检测整数溢出或下溢。如果 MATLAB Function 模块代码中未发生整数溢出，则禁用此选项更高效。
- Simulink Coder 生成的代码不检查整数溢出或下溢，因此当此参数为 `off` 时可能产生不可预测的结果。在这种情况下，请在生成代码之前对模型进行仿真以测试溢出和下溢。
- 此参数设置仅与整数运算相关。它对定点或双精度运算没有影响。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `true` 或 `1`（默认）| `false` 或 `0` |
| **数据类型：** | `logical` |

### **Support variable-size arrays** — 模块是否支持可变大小数据 `on`（默认）| `off`

指定 MATLAB Function 模块是否支持在仿真期间维度变化的输入和输出数据。当此参数为 `on` 时，您可以通过在输出变量上启用 **Variable size** 属性来定义可变大小输出。有关详细信息，请参阅 Declare Variable-Size MATLAB Function Block Variables 和 Variable size。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SupportVariableSizing` |
| **值：** | `true` 或 `1`（默认）| `false` 或 `0` |
| **数据类型：** | `logical` |

### **Allow direct feedthrough** — 模块是否支持直接馈通语义 `on`（默认）| `off`

指定 MATLAB Function 模块是否支持直接馈通语义，以便模块的输出直接由输入值控制。当此参数为 `off` 时，模块输出仅依赖于模块的当前状态。使用非直接馈通使您能够在反馈环路中使用 MATLAB Function 模块并防止代数环。有关详细信息，请参阅 Use Nondirect Feedthrough in a MATLAB Function Block。

#### 依赖关系

要禁用此参数，必须将 **Update method** 设置为 `Inherited` 或 `Discrete`。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `AllowDirectFeedthrough` |
| **值：** | `true` 或 `1`（默认）| `false` 或 `0` |
| **数据类型：** | `logical` |

### **Interpret output column vectors as one-dimensional data** — 模块是否将长度为 1 的维度的输出变量视为固定大小 `off`（默认）| `on`

*自 R2021b 起*

将 MATLAB Function 模块是否将长度为 1 的维度的输出变量视为固定大小指定为以下值之一：

- `off` — 模块将至少有一个长度为 1 的维度的输出变量视为固定大小，无论您是否将这些变量指定为可变大小。
- `on` — 如果您将输出变量指定为可变大小，MATLAB Function 模块将这些输出变量视为可变大小。

有关详细信息，请参阅 Variable size。

**注意**

在 R2021b 及更早版本中，MATLAB Function 模块始终将输出列向量转换为一维信号。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `VectorOutputs1D` |
| **值：** | `false` 或 `0`（默认）| `true` 或 `1` |
| **数据类型：** | `logical` |

### **Treat dimensions of length 1 as fixed size** — 至少有一个长度为 1 的维度的变量是否为固定大小 `on`（默认）| `off`

*自 R2023a 起*

将至少有一个长度为 1 的维度的变量是否为固定大小指定为以下值之一：

- `on` — 具有长度为 1 的维度的可变大小变量为固定大小。
- `off` — 模块中启用了 **Variable size** 属性的变量始终为可变大小。

此参数仅影响启用了 **Variable size** 属性的输出变量。请参阅 Variable size。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值：** | `true` 或 `1`（默认）| `false` 或 `0` |
| **数据类型：** | `logical` |

### 定点属性

### **Treat these inherited Simulink signal types as fi objects** — 要视为 `fi` 对象的继承 Simulink 信号 `Fixed-point`（默认）| `Fixed-point & Integer`

将是否将继承的定点和整数信号视为 Fixed-Point Designer™ `fi` (Fixed-Point Designer) 对象指定为以下值之一：

- `Fixed-point` — MATLAB Function 模块将所有定点输入视为 Fixed-Point Designer `fi` 对象。
- `Fixed-point & Integer` — MATLAB Function 模块将所有定点和整数输入视为 Fixed-Point Designer `fi` 对象。

有关详细信息，请参阅 Ways to Construct fi Objects (Fixed-Point Designer)。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatAsFi` |
| **值：** | `"Fixed-point"`（默认）| `"Fixed-point & Integer"` |

### **MATLAB function fimath** — 默认 `fimath` 属性 `Same as MATLAB`（默认）| `Specify Other`

将 MATLAB Function 模块的默认 `fimath` (Fixed-Point Designer) 对象属性指定为以下值之一：

- `Same as MATLAB` — 模块使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框变暗并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` — 通过以下两种方式之一在文本框中指定您自己的 `fimath` 对象：

  - 在文本框内构造 `fimath` 对象。
  - 在 MATLAB 或模型工作区中构造 `fimath` 对象，然后在文本框中输入其变量名。如果使用此选项并计划与他人共享模型，请在模型工作区中定义变量。

有关详细信息，请参阅 fimath Object Construction (Fixed-Point Designer) 和 Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer)。

#### 提示

- MATLAB Function 模块的 `fimath` 对象对于模块的内容而言行为类似于 `globalfimath` (Fixed-Point Designer) 对象。模块将此参数中的 `fimath` 对象属性与您选择视为 `fi` 对象的 MATLAB Function 模块的所有定点和整数输入信号相关联。在 MATLAB Function 模块中构造 `fi` 对象会引入额外的注意事项。

  - 如果在构造 `fi` 对象时没有 `fimath` 对象与其关联，则 `fi` 构造函数使用默认 `fimath` 对象设置，而不管 **MATLAB function fimath** 中的属性如何。如果在 `fi` 对象构造后对其执行操作，则该对象采用 **MATLAB function fimath** 中的属性。
  - 如果在 `fi` 构造函数中指定 `fimath` 对象，则 `fi` 构造函数在量化值时遵循该 `fimath` 对象。`fi` 构造函数中未指定的任何 `fimath` 对象设置使用 **MATLAB function fimath** 中指定的属性。

#### 程序化使用

要以编程方式设置模块参数值，请访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象，并使用点表示法更改关联的对象属性。

如果使用 `MATLABFunctionConfiguration` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数：** | `FimathMode` |
| **值：** | `"SameAsMATLAB"`（默认）| `"UserSpecified"` |

如果使用 `Stateflow.EMChart` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数：** | `EmlDefaultFimath` |
| **值：** | `"Same as MATLAB Default"`（默认）| `"Other:UserSpecified"` |
## 所属库

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `yesa` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **零交叉检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

如果您拥有 Embedded Coder® 许可证，则可以生成 Halide 代码。有关详细信息，请参阅 Speed Up Generated Code Execution with Halide Code (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。实际数据类型或能力支持取决于模块实现。有关使用 MATLAB Function 模块的最佳实践，请参阅：

- 在 MATLAB Function 模块内使用 hdlfimath 设置并指定 fi 对象 (HDL Coder)
- MATLAB Function 模块的设计指南 (HDL Coder)
- 为函数生成可实例化代码 (HDL Coder)
- 优化 MATLAB 循环 (HDL Coder)
- 流水线化 MATLAB 表达式 (HDL Coder)

**HDL 架构**

|  |  |
| --- | --- |
| `MATLAB Function`（默认） | 这是具有定点数据类型的 MATLAB Function 模块的默认架构。使用此架构时，可以对围绕 MATLAB Function 模块的模块使用速度和面积优化。MATLAB Function 模块内部的代码不会被优化。 |
| `MATLAB Datapath` | 这是具有浮点数据类型的 MATLAB Function 模块的默认架构。使用此架构时，代码生成器将 MATLAB Function 模块视为常规 Subsystem 模块。通过为定点类型启用此架构，可以对 MATLAB Function 模块内部的模块以及跨 MATLAB Function 模块与其他 Simulink 模块使用速度和面积优化。此能力使您能够为 MATLAB Function 模块指定您会为 Subsystem 指定的附加属性，例如 **ClockRatePipelining** 和 **FlattenHierarchy**。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 `inherit`。要指定此属性，请将 **Architecture** 设置为 `MATLAB Datapath`。另请参阅 AdaptivePipelining (HDL Coder)。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。要指定此属性，请将 **Architecture** 设置为 `MATLAB Datapath`。另请参阅 BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。要指定此属性，请将 **Architecture** 设置为 `MATLAB Datapath`。另请参阅 ClockRatePipelining (HDL Coder)。 |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。要指定此属性，请将 **Architecture** 设置为 `MATLAB Datapath`。另请参阅 DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除 MATLAB Function 模块层级。默认值为 `inherit`。要指定此属性，请将 **Architecture** 设置为 `MATLAB Datapath`。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **GuardIndexVariables** | 选择是否将矩阵访问提升到条件 MATLAB 语句之外。默认值为 `off`。要指定此属性，请将 **Architecture** 设置为 `MATLAB Function`。另请参阅 GuardIndexVariables (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **InstantiateFunctions** | 为每个函数生成 VHDL® `entity` 或 Verilog® `module`。默认值为 `off`。另请参阅 InstantiateFunctions (HDL Coder)。 |
| **LoopOptimization** | 展开、流式化或不优化循环。默认值为 `none`。如果将 **Architecture** 设置为 `MATLAB Datapath`，则只能展开循环。如果要将循环流式化与 `MATLAB Datapath` 架构一起使用，可以通过指定 **StreamingFactor** 来使用流式化优化。另请参阅 LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 `off`。另请参阅 MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅资源共享 (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行、标量数据路径的并行数据路径或向量数量。默认值为 0，即实现完全并行的数据路径。要指定此属性，请将 **Architecture** 设置为 `MATLAB Datapath`。另请参阅流式化 (HDL Coder)。 |
| **VariablesToPipeline** | **警告** 不建议使用 `VariablesToPipeline`。请改用 `coder.hdl.pipeline` (HDL Coder)。在指定变量的输出端插入流水线寄存器。将变量列表指定为字符向量，变量之间用空格分隔。要指定此属性，请将 **Architecture** 设置为 `MATLAB Function`。 |

**数据类型支持**

HDL 代码生成支持 MATLAB Function 模块中以下函数的半精度数据类型：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| `all` | `and, &` | `any` | `cast` | `conj` | `ctranspose` |
| `end` | `=` | `eq` | `==` | `ge, >=` | `gt, >` |
| `half` | `inf` | `int8` | `int16` | `int32` | `int64` |
| `isa` | `iscolumn` | `isempty` | `isequal` | `isfinite` | `isfloat` |
| `isinf` | `isinteger` | `islogical` | `isnan` | `isnumeric` | `isreal` |
| `isrow` | `isscalar` | `isvector` | `le, <=` | `length` | `logical` |
| `lt, <` | `max` | `min` | `minus, -` | `NaN` | `ndims` |
| `ne, ~=` | `not` | `numel` | `or, |` | `plus, +` | `prod` |
| `reshape` | `single` | `size` | `sqrt` | `sum` | `times, .*` |
| `transpose` | `uint8` | `uint16` | `uint32` | `uint64` | `uminus` |
| `uplus` | `vertconcat` | - | - | - | - |

**复数数据支持**

此模块支持复数信号的代码生成。

另请参阅复数数据类型支持 (HDL Coder)。

**使用 `hdlfimath` 设置**

`hdlfimath` 函数是一个实用工具，用于定义针对 HDL 代码生成优化的 `fimath` 属性。有关更多信息，请参阅在 MATLAB Function 模块内使用 hdlfimath 设置并指定 fi 对象 (HDL Coder)。

**可调参数支持**

HDL Coder 支持具有以下数据类型的可调和不可调参数：

- 标量
- 向量
- 复数
- 结构体
- 枚举

有关详细信息，请参阅为可调参数生成 DUT 端口 (HDL Coder) 和 MATLAB Function 模块的设计指南 (HDL Coder)。

**为包含代数环的模型生成 HDL 代码**

要为包含 Matlab Function 模块的模型生成 HDL 代码：

- 在“配置参数”对话框中，点击 **Diagnostics**，并将 **Algebraic loop** 参数设置为 `none` 或 `warning`。
- 打开 Matlab Function 模块的模块封装，并选择 **Treat as atomic unit** 和 **Minimize algebraic loop occurrences** 参数。

**限制**

- 如果模块包含 System object™，则模块输入不能具有非离散（常量或 `Inf`）采样时间。
- HDL Coder 不支持包含与函数输入和输出相同变量的 MATLAB Function。例如，不支持以下 MATLAB 代码。

  ```
  function y = myFun(y)
  %#codegen

  y = 3 * y;
  ```
- 该模块仅在 Native Floating Point 模式下支持浮点数据类型。

有关从 MATLAB Function 模块生成 HDL 代码所支持的 MATLAB 语言子集，请参阅支持的 MATLAB 数据类型、运算符和控制流语句 (HDL Coder)。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

**PLC 模块属性**

|  |  |
| --- | --- |
| **UseExternalDefinition** | 在生成代码中抑制模块定义。默认值为 `Off`。另请参阅 UseExternalDefinition (Simulink PLC Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或能力支持取决于模块实现。

## 版本历史

**在 R2011a 中引入**

### R2023a：指定如何处理长度为 1 维度的输出变量

通过新的 **Treat dimensions of length 1 as fixed size** 参数，您可以指定当至少一个维度长度为 1 时，MATLAB Function 模块如何处理输出变量。在 R2023a 之前，无论您是否将这些变量指定为可变大小，MATLAB Function 模块都会将长度为 1 维度的输出变量视为固定大小。

### R2021b：将输出列向量输出为二维或一维数据

现在，您可以使用 **Interpret output column vectors as one-dimensional data** 参数，将 MATLAB Function 模块中的列向量输出为二维或一维数据。

### R2021a：在快速加速器模式下报告 MATLAB Function 模块的运行时错误

通过将 **Enable memory integrity checks** 配置参数设置为 `Always on`，在快速加速器模式下仿真时报告 MATLAB Function 模块的运行时错误。

### R2020a：MATLAB Function 模块支持 64 位整数类型

MATLAB Function 模块现在支持 64 位整数数据。该模块将 `int64` 和 `uint64` 数据类型实现为字长为 64 位、小数长度为 0 的定点数。

### R2019b：MATLAB Function 模块支持字符串

MATLAB Function 模块现在支持 Simulink 字符串。

## 描述

在 Simulink 模型中包含 MATLAB 代码

MATLAB Function 模块使您能够编写在 Simulink® 模型中执行的 MATLAB® 函数。MATLAB 函数在每个时间步的仿真期间执行。有关将 MATLAB 代码集成到 Simulink 模型中的更多信息，请参阅使用 MATLAB Function 模块在 Simulink 中实现 MATLAB 函数。如果您拥有 Simulink Coder™ 许可证，还可以从 MATLAB Function 模块为 Simulink Coder 目标生成 C/C++ 代码。

双击 MATLAB Function 模块以打开 MATLAB Function Block Editor，您可以在其中编写 MATLAB 函数。您还可以使用 Model Explorer 或 **Symbols** 窗格定义变量、添加输入触发并创建函数调用输出。有关更多信息，请参阅创建和定义 MATLAB Function 模块变量、管理 MATLAB Function 模块的输入触发以及管理 MATLAB Function 模块的函数调用输出。

在 **Symbols** 窗格中，您可以将模块输入声明为 Simulink 参数而不是端口。MATLAB Function 模块还支持输入、输出和参数的类型和大小继承。您可以显式指定这些属性。请参阅定义和修改变量数据类型、指定 MATLAB Function 模块变量的大小以及通过定义参数变量在多个 MATLAB Function 模块中使用数据。

当您仿真包含 MATLAB Function 模块的模型时，软件会从该模块生成二进制代码或 C/C++ MATLAB 可执行文件 (MEX) 代码，并将此代码与模型集成。MATLAB Function 模块使用与 MATLAB Coder 相同的基础设施，您可以使用该基础设施从 Simulink 外部的 MATLAB 代码生成 C/C++ 代码。因此，MATLAB Function 模块代码必须使用支持代码生成的 MATLAB 约定。请参阅 MATLAB Function 模块的代码和集成限制。

为支持数据可视化，MATLAB Function 模块支持仅用于仿真的 MATLAB 函数调用。请参阅使用 MATLAB Engine 在 MATLAB Function 模块中执行函数调用。如果您使用 Simulink Coder 生成代码，则如果函数调用不直接影响 Simulink 输入或输出，这些调用不会出现在生成的代码中。
