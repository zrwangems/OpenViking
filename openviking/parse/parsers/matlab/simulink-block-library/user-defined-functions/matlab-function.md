---
type: simulink-block
title: 'MATLAB Function'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'matlabfunction'
---

# MATLAB Function

Include MATLAB code in Simulink models

## 中文

在 Simulink 模型中包含 MATLAB 代码

### 所属库

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

### 描述

MATLAB Function 模块使您能够编写在 Simulink® 模型中执行的 MATLAB® 函数。MATLAB 函数在仿真期间的每个时间步执行。有关将 MATLAB 代码集成到 Simulink 模型中的详细信息，请参阅使用 MATLAB Function 模块在 Simulink 中实现 MATLAB 函数。如果您有 Simulink Coder™ 许可证，您还可以从 MATLAB Function 模块为 Simulink Coder 目标生成 C/C++ 代码。

双击 MATLAB Function 模块可打开 MATLAB Function 模块编辑器，您可以在其中编写 MATLAB 函数。您还可以使用模型资源管理器或**符号**窗格来定义变量、添加输入触发器以及创建函数调用输出。有关详细信息，请参阅Create and Define MATLAB Function Block Variables、Manage the Input Trigger of a MATLAB Function Block和Manage Function Call Outputs of a MATLAB Function Block。

在**符号**窗格中，您可以将模块输入声明为 Simulink 参数，而不是端口。MATLAB Function 模块还支持继承输入、输出和参数的类型及大小。您可以显式指定这些属性。请参阅定义和修改变量数据类型、指定 MATLAB Function 模块变量的大小和通过定义参数变量在多个 MATLAB Function 模块中使用数据。

当您仿真包含 MATLAB Function 模块的模型时，软件会从该模块生成二进制代码或 C/C++ 语言的 MATLAB 可执行文件 (MEX) 代码，并将此代码与模型集成。MATLAB Function 模块使用与 MATLAB Coder 相同的基础架构，您可使用该基础架构从 Simulink 之外的 MATLAB 代码生成 C/C++ 代码。因此，MATLAB Function 模块代码必须使用代码生成支持的 MATLAB 约定。请参阅Code and Integration Limitations for MATLAB Function Blocks。

为支持数据可视化，MATLAB Function 模块仅支持调用 MATLAB 函数进行仿真。请参阅使用 MATLAB 引擎在 MATLAB Function 模块中执行函数调用。如果使用 Simulink Coder 生成代码，并且函数调用不直接影响 Simulink 输入或输出，则调用不会出现在生成的代码中。

### 端口

#### 输入

#### **Port\_1** — 输入变量 标量 | 向量 | 矩阵

MATLAB 函数中的输入变量，指定为实数值标量、向量或矩阵。每个输入变量都有一个使用该变量名称的关联端口。

您不能在 Simulink 模型和 MATLAB Function 模块中的函数之间传递 MATLAB 支持但 Simulink 不支持的数据类型。您可以在 MATLAB Function 模块中使用这些数据类型。

有关此模块支持的定点数据类型的详细信息，请参阅Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer)和Data Type Override with MATLAB Function Block (Fixed-Point Designer)。

##### 依赖关系

要创建输入端口，请打开模块并在**符号**窗格中创建输入变量。请参阅Create and Define MATLAB Function Block Variables。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
#### 输出

#### **Port\_1** — 输出变量 标量 | 向量 | 矩阵

MATLAB 函数中的输出变量，指定为实数值标量、向量或矩阵。每个输出变量都有一个使用该变量名称的关联端口。

##### 依赖关系

要创建输出端口，请打开模块并在**符号**窗格中创建输出变量。请参阅Create and Define MATLAB Function Block Variables。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`

### 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

**注意**

MATLAB Function 模块也有 Subsystem 模块参数，您可以通过右键点击模块并点击**模块参数(子系统)** 来访问这些参数。但是，不推荐更新这些模块参数。

#### **更新方法** — 用于激活模块的方法 **继承** (默认) | **离散** | **连续**

将激活 MATLAB Function 模块的方法指定为以下值之一：

- **继承** - 来自 Simulink 模型的输入激活 MATLAB Function 模块。

  如果您定义输入触发器，则 MATLAB Function 模块会执行，以响应触发端口上的 Simulink 信号或函数调用事件。如果您没有定义输入触发器，则 MATLAB Function 模块将从模型中隐式继承触发器。这些隐式事件是向模块提供输入的信号的离散或连续采样时间。

  如果您定义了数据输入，则 MATLAB Function 模块以最快的数据输入速率进行采样。如果未定义数据输入，则 MATLAB Function 模块以父级子系统的执行行为定义的速率进行采样。
- **离散** - MATLAB Function 模块使用您在模块的**采样时间**参数中指定的速率激活。该模块以对应于指定速率的固定时间间隔生成隐式事件。模型中的其他模块可以有不同采样时间。
- **连续** - MATLAB Function 模块仅在主时间步期间激活，在主时间步和子时间步内都会计算输出和局部连续变量。模块可以记录过零，这样，只要状态发生变化，Simulink 模型就可以对模块进行采样。模块计算局部连续变量的导数。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

如果使用 `MATLABFunctionConfiguration` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数:** | `UpdateMethod` |
| **值:** | `"Inherited"` (默认) | `"Continuous"` | `"Discrete"` |

如果使用 `Stateflow.EMChart` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数:** | `ChartUpdate` |
| **值:** | `"INHERITED"` (默认) | `"CONTINUOUS"` | `"DISCRETE"` |

#### **采样时间** — 仿真期间模块激活的时间间隔 `-1` (默认) | 标量 | 向量

指定在仿真期间 MATLAB Function 模块激活的时间间隔。默认值表示模块从 Simulink 继承采样时间。有关指定采样时间的详细信息，请参阅指定采样时间。

不要在 Subsystem 模块参数中使用**采样时间**参数。请改用属性检查器。

##### 依赖关系

要启用此参数，请将**更新方法**设置为**离散**。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar | vector |
| **数据类型:** | `string` | `char` |

#### 高级

#### **对整数溢出进行饱和处理** — 数据是否对整数溢出进行饱和处理 `on` (默认) | `off`

将 MATLAB Function 模块中的数据在发生整数溢出时是否进行饱和指定为以下值之一：

- `on` - 模块通过将整数设置为字长允许的最大正值或负值对整数进行饱和处理。此设置匹配 MATLAB 行为。
- `off` - 当发生溢出情况时，模块在仿真模式下生成运行时错误。当您使用 Simulink Coder 生成代码时，行为取决于您的 C 语言编译器。

##### 提示

- 当此参数为 `on` 时，MATLAB 会在仿真期间添加额外的检查以检测整数上溢或下溢。如果 MATLAB Function 模块代码中没有发生整数溢出，则禁用此选项会更高效。
- 由 Simulink Coder 生成的代码不检查整数上溢或下溢，因此，当此参数为 `off` 时，可能会产生不可预测的结果。在这种情况下，请在生成代码之前仿真您的模型以测试上溢和下溢。
- 此参数设置仅与整数算术相关。它对定点或双精度算术不起作用。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

#### **支持可变大小数组** — 模块是否支持可变大小数据 `on` (默认) | `off`

指定 MATLAB Function 模块是否支持在仿真期间维度可变的输入和输出数据。当此参数为 `on` 时，您可以通过启用输出变量的**可变大小**属性来定义可变大小输出。有关详细信息，请参阅声明可变大小的 MATLAB Function 模块变量和Variable size。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SupportVariableSizing` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

#### **允许直接馈通** — 模块是否支持直接馈通语义 `on` (默认) | `off`

指定 MATLAB Function 模块是否支持直接馈通语义，以便模块的输出由输入的值直接控制。当此参数为 `off` 时，模块输出仅依赖模块的当前状态。使用非直接馈通使您能够在反馈环中使用 MATLAB Function 模块并防止代数环。有关详细信息，请参阅 Use Nondirect Feedthrough in a MATLAB Function Block。

##### 依赖关系

要禁用此参数，您必须将**更新方法**设置为**继承**或**离散**。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `AllowDirectFeedthrough` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

#### **将输出列向量解释为一维数据** — 模块是否将维度长度为 1 的输出变量视为固定大小 `off` (默认) | `on`

*自 R2021b 起*

将 MATLAB Function 模块是否将维度长度为 1 的输出变量视为固定大小指定为以下值之一：

- `off` - 无论您是否将变量指定为具有可变大小，模块都将至少一个维度的长度为 1 的输出变量视为固定大小。
- `on` - 如果您将变量指定为具有可变大小，则 MATLAB Function 模块将输出变量视为可变大小。

有关详细信息，请参阅Variable size。

**注意**

在 R2021b 及更早版本中，MATLAB Function 模块始终将输出列向量转换为一维信号。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `VectorOutputs1D` |
| **值:** | `false` or `0` (默认) | `true` or `1` |
| **数据类型:** | `logical` |

#### **将长度为 1 的维度视为固定大小** — 至少一个维度的长度为 1 的变量是否为固定大小 `on` (默认) | `off`

*自 R2023a 起*

将至少一个维度的长度为 1 的变量是否为固定大小指定为以下值之一：

- `on` - 一个维度的长度为 1 的可变大小变量是固定大小的变量。
- `off` - 模块中启用**可变大小**属性的变量始终为可变大小。

此参数仅影响启用**可变大小**属性的输出变量。请参阅Variable size。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

#### 定点属性

#### **将这些继承的 Simulink 信号类型视为 fi 对象** — 继承的 Simulink 信号被视为 `fi` 对象 `Fixed-point` (默认) | `Fixed-point & Integer`

将是否将继承的定点和整数信号视为 Fixed-Point Designer™ `fi` (Fixed-Point Designer) 对象指定为以下值之一：

- `Fixed-point` - MATLAB Function 模块将所有定点输入视为 Fixed-Point Designer `fi` 对象。
- `Fixed-point & Integer` - MATLAB Function 模块将所有定点和整数输入视为 Fixed-Point Designer `fi` 对象。

有关详细信息，请参阅Ways to Construct fi Objects (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatAsFi` |
| **值:** | `"Fixed-point"` (默认) | `"Fixed-point & Integer"` |

#### **MATLAB 函数 fimath** — 默认 `fimath` 属性 `Same as MATLAB` (默认) | `Specify Other`

将 MATLAB Function 模块的默认 `fimath` (Fixed-Point Designer) 对象属性指定为以下值之一：

- `Same as MATLAB` - 模块使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框灰显，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` - 以两种方式之一在文本框中指定您自己的 `fimath` 对象：

  - 在文本框内构造 `fimath` 对象。
  - 在 MATLAB 或模型工作区中构造 `fimath` 对象，然后在文本框中输入其变量名称。如果您使用此选项并计划与其他人共享您的模型，请在模型工作区中定义此变量。

有关详细信息，请参阅 fimath Object Construction (Fixed-Point Designer)和Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer)。

##### 提示

- MATLAB Function 模块的 `fimath` 对象对于该模块的内容表现为 `globalfimath` (Fixed-Point Designer) 对象。该模块将此参数中的 `fimath` 对象属性与您选择视为 `fi` 对象的 MATLAB Function 模块的所有定点和整数输入信号相关联。在 MATLAB Function 模块中构造 `fi` 对象需要考虑其他注意事项。

  - 如果在构造 `fi` 对象时没有与之相关联的 `fimath` 对象，则 `fi` 构造函数使用默认 `fimath` 对象设置，而不考虑 **MATLAB 函数 fimath** 中的属性。如果在构造 `fi` 对象后对其执行操作，该对象将采用 **MATLAB 函数 fimath** 中的属性。
  - 如果您在 `fi` 构造函数中指定 `fimath` 对象，则 `fi` 构造函数在量化值时遵循该 `fimath` 对象。`fi` 构造函数中未指定的任何 `fimath` 对象设置都使用 **MATLAB 函数 fimath** 中的指定属性。

##### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改关联的对象属性。

如果使用 `MATLABFunctionConfiguration` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数:** | `FimathMode` |
| **值:** | `"SameAsMATLAB"` (默认) | `"UserSpecified"` |

如果使用 `Stateflow.EMChart` 对象，请使用以下选项指定属性：

|  |  |
| --- | --- |
| **参数:** | `EmlDefaultFimath` |
| **值:** | `"Same as MATLAB Default"` (默认) | `"Other:UserSpecified"` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `是a` |
| **多维信号** | `是a` |
| **可变大小信号** | `是a` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

如果您有 Embedded Coder® 许可证，您可以生成 Halide 代码。有关详细信息，请参阅Speed Up Generated Code Execution with Halide Code (Embedded Coder)。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。实际数据类型或功能支持取决于模块实现。有关使用 MATLAB Function 模块的最佳做法，请参阅：

- Use hdlfimath Setting and Specify fi Objects inside MATLAB Function Block (HDL Coder)
- Design Guidelines for the MATLAB Function Block (HDL Coder)
- Generate Instantiable Code for Functions (HDL Coder)
- Optimize MATLAB Loops (HDL Coder)
- Pipeline MATLAB Expressions (HDL Coder)

**HDL 架构**

|  |  |
| --- | --- |
| **MATLAB 函数**（默认值） | 这是具有定点数据类型的 MATLAB Function 模块的默认架构。当您使用此架构时，您可以对 MATLAB Function 模块周围的模块使用速度和面积优化。MATLAB Function 模块中的代码不会优化。 |
| **MATLAB Datapath** | 这是具有浮点数据类型的 MATLAB Function 模块的默认架构。当您使用此架构时，代码生成器将 MATLAB Function 模块视为常规的 Subsystem 模块。通过为定点类型启用此架构，您可以对 MATLAB Function 模块内的模块以及与 MATLAB Function 模块一起工作的其他 Simulink 模块使用速度和面积优化。  通过此功能，您可以为 MATLAB Function 模块指定要为 Subsystem 模块指定的其他属性，例如 **ClockRatePipelining** 和 **FlattenHierarchy**。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 **inherit**。要指定此属性，请将**架构**设置为 `MATLAB Datapath`。另请参阅AdaptivePipelining (HDL Coder)。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 **inherit**。要指定此属性，请将**架构**设置为 `MATLAB Datapath`。另请参阅BalanceDelays (HDL Coder)。 |
| **ClockRatePipelining** | 以较快的时钟频率而不是较慢的数据速率插入流水线寄存器。默认值为 **inherit**。要指定此属性，请将**架构**设置为 `MATLAB Datapath`。另请参阅ClockRatePipelining (HDL Coder)。 |
| **ConstMultiplierOptimization** | 正则有符号数 (CSD) 或因子化 CSD 优化。默认值为**无**。另请参阅ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为**无**。要指定此属性，请将**架构**设置为 `MATLAB Datapath`。另请参阅DSPStyle (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除 MATLAB Function 模块层次结构。默认值为 **inherit**。要指定此属性，请将**架构**设置为 `MATLAB Datapath`。另请参阅FlattenHierarchy (HDL Coder)。 |
| **GuardIndexVariables** | 选择是否将矩阵访问提升到条件 MATLAB 语句外部。默认值为 **off**。要指定此属性，请将**架构**设置为 `MATLAB Function`。另请参阅GuardIndexVariables (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **InstantiateFunctions** | 为每个函数生成 VHDL® `entity` 或 Verilog® `module`。默认值为 **off**。另请参阅InstantiateFunctions (HDL Coder)。 |
| **LoopOptimization** | 展开、流化或不优化循环。默认值为**无**。如果您将**架构**设置为 `MATLAB Datapath`，您只能展开循环。如果您要在 `MATLAB Datapath` 架构中使用循环流，可以通过指定 **StreamingFactor** 来使用流式优化。另请参阅LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 **off**。另请参阅MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ResetType** | 隐藏重置逻辑生成。默认值为**默认**，它生成重置逻辑。另请参阅ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 并行数据路径或向量的数量，这些路径或向量通过时间多路复用的方式变换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。要指定此属性，请将**架构**设置为 `MATLAB Datapath`。另请参阅Streaming (HDL Coder)。 |
| **VariablesToPipeline** | **警告**  不推荐使用 `VariablesToPipeline`。请改用 `coder.hdl.pipeline` (HDL Coder)。  在一个或多个指定变量的输出端插入流水线寄存器。将变量列表指定为字符向量，变量之间用空格分隔。要指定此属性，请将**架构**设置为 `MATLAB Function`。 |

**数据类型支持**

对于 MATLAB Function 模块中的以下函数，HDL 代码生成支持半精度数据类型：

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

此模块支持复信号的代码生成。

另请参阅Complex Data Type Support (HDL Coder)。

**使用 `hdlfimath` 设置**

`hdlfimath` 函数是一种实用工具，用于定义针对 HDL 代码生成优化的 `fimath` 属性。有关详细信息，请参阅Use hdlfimath Setting and Specify fi Objects inside MATLAB Function Block (HDL Coder)。

**可调参数支持**

HDL Coder 支持以下数据类型的可调和不可调参数：

- 标量
- 向量
- 复数
- 结构体
- 枚举

有关详细信息，请参阅Generate DUT Ports for Tunable Parameters (HDL Coder)和Design Guidelines for the MATLAB Function Block (HDL Coder)。

**生成具有代数环的模块的 HDL 代码**

要为包含 Matlab Function 模块的模型生成 HDL 代码，请执行以下操作：

- 在“配置参数”对话框中，点击**诊断**，并将**代数环**参数设置为**无**或**警告**。
- 打开 Matlab Function 模块的模块封装，并选择**视为原子单元**和**尽量减少出现代数环**参数。

**限制**

- 如果模块包含 System object™，则模块输入不能包含非离散（常量或 `Inf`）采样时间。
- HDL Coder 不支持包含与函数的输入和输出相同的变量的 MATLAB Function。例如，不支持使用此 MATLAB 代码。

  ```
  function y = myFun(y)
  %#codegen

  y = 3 * y;
  ```
- 模块仅在原生浮点模式下支持浮点数据类型。

有关基于 MATLAB Function 模块的 HDL 代码生成支持的 MATLAB 语言子集，请参阅 Supported MATLAB Data Types, Operators, and Control Flow Statements (HDL Coder)。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

**PLC 模块属性**

|  |  |
| --- | --- |
| **UseExternalDefinition** | 在生成的代码中取消模块定义。默认值为 **Off**。另请参阅UseExternalDefinition (Simulink PLC Coder)。 |

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

### 版本历史记录

**在 R2011a 中推出**

#### R2023a: 指定如何处理维度长度为 1 的输出变量

使用新的**将长度为 1 的维度视为固定大小**参数，您可以指定当至少一个维度的长度为 1 时，MATLAB Function 模块如何处理输出变量。在 R2023a 之前，MATLAB Function 模块将一个维度长度为 1 的输出变量视为固定大小，无论您是否将变量指定为具有可变大小。

#### R2021b: 将列向量输出为二维或一维数据

现在您可以使用**将输出列向量解释为一维数据**参数将 MATLAB Function 模块中的列向量输出为二维或一维数据。

#### R2021a: 报告 MATLAB Function 模块在快速加速模式下的运行时错误

通过将**启用内存完整性检查**配置参数设置为**始终打开**，报告在快速加速模式下进行仿真时 MATLAB Function 模块的运行时错误。

#### R2020a: 对 MATLAB Function 模块的 64 位整数类型支持

MATLAB Function 模块现在支持 64 位整数数据。该模块将 `int64` 和 `uint64` 数据类型实现为定点数，字长为 64 位，小数长度为 0。

#### R2019b: 对 MATLAB Function 模块的字符串支持

现在，MATLAB Function 模块支持 Simulink 字符串。

## Libraries

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

## Description

The MATLAB Function block enables you to write MATLAB® functions that execute in Simulink® models. The MATLAB function executes during simulation at each time step. For more
information about integrating MATLAB code into your Simulink models, see Implement MATLAB Functions in Simulink with MATLAB Function Blocks. If you
have a Simulink
Coder™ license, you can also generate C/C++ code from a MATLAB
Function block for a Simulink
Coder target.

Double-click the MATLAB Function block to open the MATLAB Function Block Editor, where you write the MATLAB function. You can also define variables, add an input trigger, and create
function call outputs by using the Model Explorer or the **Symbols**
pane. For more information, see Create and Define MATLAB Function Block Variables, Manage the Input Trigger of a MATLAB Function Block,
and Manage Function Call Outputs of a MATLAB Function Block.

In the **Symbols** pane, you can declare a block input to be a
Simulink parameter instead of a port. The MATLAB Function block also
supports inheritance of types and size for inputs, outputs, and parameters. You can
specify these properties explicitly. See Define and Modify Variable Data Types, Specify Size of MATLAB Function Block Variables, and Use Data in Multiple MATLAB Function Blocks by Defining Parameter Variables.

When you simulate a model that contains a MATLAB Function block, the
software generates binary code or C/C++ MATLAB executable (MEX) code from the block and integrates this code with the
model. The MATLAB Function block uses the same infrastructure as
MATLAB
Coder, which you use to generate C/C++ code from MATLAB code outside of Simulink. Consequentially, the MATLAB Function block code must use
MATLAB conventions that are supported for code generation. See Code and Integration Limitations for MATLAB Function Blocks.

To support visualization of data, the MATLAB Function block supports
calls to MATLAB functions for simulation only. See Use MATLAB Engine to Execute a Function Call in MATLAB Function Blocks. If you generate code using Simulink
Coder, the calls do not appear in the generated code if the function calls do
not directly affect the Simulink inputs or outputs.

## Ports

### Input

### **Port\_1** — Input variable scalar | vector | matrix

Input variable in the MATLAB function, specified as a real-valued scalar, vector, or
matrix. Each input variable has an associated port that uses the name of
the variable.

You cannot pass data types supported by MATLAB but not supported by Simulink between the Simulink model and the function in the MATLAB
Function block. You can use these data types in the
MATLAB Function block.

For more information on fixed-point data type support for this block,
see Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer)
and Data Type Override with MATLAB Function Block (Fixed-Point Designer).

#### Dependencies

To create input ports, open the block and create input variables
in the **Symbols** pane. See Create and Define MATLAB Function Block Variables.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
### Output

### **Port\_1** — Output variable scalar | vector | matrix

Output variable in the MATLAB function, specified as a real-valued scalar, vector, or
matrix. Each output variable has an associated port that uses the name
of the variable.

#### Dependencies

To create output ports, open the block and create output variables
in the **Symbols** pane. See Create and Define MATLAB Function Block Variables.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

**Note**

MATLAB Function blocks also have Subsystem block parameters that you
can access by right-clicking the block and clicking **Block Parameters
(Subsystem)**. However, updating these block parameters is not
recommended.

### **Update method** — Method used for activating block `Inherited` (default) | `Discrete` | `Continuous`

Specify the method for activating the MATLAB Function block as one of
these values:

- `Inherited` — Input from the Simulink model activates the MATLAB Function
  block.

  If you define an input trigger, the MATLAB Function
  block executes in response to a Simulink signal or function-call event on the trigger port. If
  you do not define an input trigger, the MATLAB
  Function block implicitly inherits triggers from the
  model. These implicit events are the discrete or continuous sample
  times of the signals that provide inputs to the block.

  If you define data inputs, the MATLAB Function
  block samples at the rate of the fastest data input. If you do not
  define data inputs, the MATLAB Function block samples
  at the rate defined by the execution behavior of the parent
  subsystem.
- `Discrete` — The MATLAB
  Function block activates by using the rate you specify
  in the **Sample time** parameter of the block.
  The block generates an implicit event at regular time intervals that
  correspond to the specified rate. Other blocks in the model can have
  different sample times.
- `Continuous` — The MATLAB
  Function block activates during major time steps only,
  and computes outputs and local continuous variables during major and
  minor time steps. The block can register zero crossings, which
  allows Simulink models to sample the block whenever state changes
  occur. The block computes derivatives for local continuous
  variables.

#### Programmatic Use

To set the block parameter value programmatically, access the `MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

If you use the `MATLABFunctionConfiguration` object,
specify the property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `UpdateMethod` |
| **Values:** | `"Inherited"` (default) | `"Continuous"` | `"Discrete"` |

If you use the `Stateflow.EMChart` object, specify the
property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `ChartUpdate` |
| **Values:** | `"INHERITED"` (default) | `"CONTINUOUS"` | `"DISCRETE"` |

### **Sample time** — Time interval at which block activates up during simulation `-1` (default) | scalar | vector

Specify the time interval at which the MATLAB Function block activates
during simulation. The default value indicates that the block inherits the
sample time from Simulink. For more information on specifying sample time, see Specify Sample Time.

Do not use the **Sample Time** parameter in the
Subsystem block parameters. Instead, use the
Property Inspector.

#### Dependencies

To enable this parameter, set **Update method** to
`Discrete`.

#### Programmatic Use

To set the block parameter value programmatically, access the `MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar | vector |
| **Data Types:** | `string` | `char` |

### Advanced

### **Saturate on integer overflow** — Whether data saturates on integer overflow `on` (default) | `off`

Specify whether the data in the MATLAB Function block saturates on
integer overflow as one of these values:

- `on` — The block saturates an integer by
  setting it to the maximum positive or negative value allowed
  by the word size. This setting matches MATLAB behavior.
- `off` — The block generates a run-time
  error in simulation mode when a overflow condition occurs.
  When you use Simulink
  Coder to generate code, the behavior depends on your
  C language compiler.

#### Tips

- When this parameter is `on`, MATLAB adds additional checks during simulation to
  detect integer overflow or underflow. If integer overflow
  does not occur in the MATLAB Function block
  code, it is more efficient to disable this option.
- Code generated by Simulink
  Coder does not check for integer overflow or
  underflow and, therefore, may produce unpredictable results
  when this parameter is `off`. In this
  situation, simulate your model to test for overflow and
  underflow before generating code.
- This parameter setting is relevant only for integer
  arithmetic. It has no effect on fixed-point or
  double-precision arithmetic.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Support variable-size arrays** — Whether block supports variable-size data `on` (default) | `off`

Specify whether the MATLAB Function block supports input and output data
that varies in dimension during simulation. When this parameter is
`on`, you can define variable-size outputs by
enabling the **Variable size** property on output
variables. For more information, see Declare Variable-Size MATLAB Function Block Variables and Variable size.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `SupportVariableSizing` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Allow direct feedthrough** — Whether block supports direct feedthrough semantics `on` (default) | `off`

Specify whether the MATLAB Function block supports direct feedthrough
semantics, so that the output of the block is controlled directly by the
value of an input. When this parameter is `off`, the
block outputs rely only on the current state of the block. Using
nondirect feedthrough enables you to use MATLAB Function
blocks in a feedback loop and prevent algebraic loops. For more
information, see Use Nondirect Feedthrough in a MATLAB Function Block.

#### Dependencies

To disable this parameter, you must set **Update method** to
`Inherited` or
`Discrete`.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `AllowDirectFeedthrough` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### **Interpret output column vectors as one-dimensional data** — Whether block treats output variables with dimension of length 1 as fixed size `off` (default) | `on`

*Since R2021b*

Specify whether the MATLAB Function block treats output variables with a
dimension of length 1 as fixed size as one of these values:

- `off` — The block treats output variables
  that have at least one dimension of length 1 as fixed size,
  regardless of whether you specify the variables as having
  variable size.
- `on` — The MATLAB Function
  block treats output variables as variable size if you
  specify the variables as having variable size.

For more information, see Variable size.

**Note**

In release R2021b and earlier, MATLAB Function
blocks always convert output column vectors to one-dimensional
signals.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `VectorOutputs1D` |
| **Values:** | `false` or `0` (default) | `true` or `1` |
| **Data Types:** | `logical` |

### **Treat dimensions of length 1 as fixed size** — Whether variables with at least one dimension of length 1 are fixed size `on` (default) | `off`

*Since R2023a*

Specify whether variables with at least one dimension of length 1 are fixed size as one
of these values:

- `on` — Variables that are variable size
  with a dimension of 1 are fixed size.
- `off` — Variables in the block that have
  the **Variable size** property enabled are
  always variable size.

This parameter only affects output variables that have the
**Variable size** property enabled. See Variable size.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **Values:** | `true` or `1` (default) | `false` or `0` |
| **Data Types:** | `logical` |

### Fixed-point properties

### **Treat these inherited Simulink signal types as fi objects** — Inherited Simulink signals to treat as `fi` objects `Fixed-point` (default) | `Fixed-point & Integer`

Specify whether to treat inherited fixed-point and integer signals as Fixed-Point Designer™
`fi` (Fixed-Point Designer) objects as one of
these values:

- `Fixed-point` — The MATLAB
  Function block treats all fixed-point inputs as
  Fixed-Point Designer
  `fi` objects.
- `Fixed-point & Integer` — The
  MATLAB Function block treats all
  fixed-point and integer inputs as Fixed-Point Designer
  `fi` objects.

For more information, see Ways to Construct fi Objects (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or `Stateflow.EMChart` object of the block and change the
object property by using dot notation.

|  |  |
| --- | --- |
| **Parameter:** | `TreatAsFi` |
| **Values:** | `"Fixed-point"` (default) | `"Fixed-point & Integer"` |

### **MATLAB function fimath** — Default `fimath` properties `Same as MATLAB` (default) | `Specify Other`

Specify the default `fimath` (Fixed-Point Designer) object
properties for the MATLAB Function block as one of these
values:

- `Same as MATLAB` — The block uses the same
  `fimath` object properties as the current
  default `fimath` object. The text box is dimmed
  and displays the current global `fimath` object
  in read-only form.
- `Specify other` — Specify your own
  `fimath` object in the text box one of two
  ways:

  - Constructing the `fimath` object inside
    the text box.
  - Constructing the `fimath` object in the
    MATLAB or model workspace and then entering its
    variable name in the text box. If you use this option
    and plan to share your model with others, define the
    variable in the model workspace.

For more information, see fimath Object Construction (Fixed-Point Designer)
and Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer).

#### Tips

- The `fimath` object of a MATLAB Function block behaves
  as a `globalfimath` (Fixed-Point Designer) object for the contents of the
  block. The block associates the `fimath`
  object properties in this parameter with all fixed-point and
  integer input signals to the MATLAB Function
  block that you choose to treat as `fi`
  objects. Constructing `fi` objects in the
  MATLAB Function block introduces
  additional considerations.

  - If no `fimath` object is
    associated with a `fi` object when
    it is constructed, then the `fi`
    constructor uses the default
    `fimath` object settings regardless
    of the properties in **MATLAB function
    fimath**. If you perform operations on
    the `fi` object after it is
    constructed, the object adopts the properties in
    **MATLAB function
    fimath**.
  - If you specify a `fimath`
    object in the `fi` constructor,
    then the `fi` constructor obeys
    that `fimath` object when
    quantizing the value. Any `fimath`
    object settings not specified in the
    `fi` constructor use the
    specified properties in **MATLAB function
    fimath**.

#### Programmatic Use

To set the block parameter value programmatically, access the
`MATLABFunctionConfiguration` or the `Stateflow.EMChart` object of the block and change the
associated object property by using dot notation.

If you use the `MATLABFunctionConfiguration`
object, specify the property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `FimathMode` |
| **Values:** | `"SameAsMATLAB"` (default) | `"UserSpecified"` |

If you use the `Stateflow.EMChart` object, specify
the property using these options:

|  |  |
| --- | --- |
| **Parameter:** | `EmlDefaultFimath` |
| **Values:** | `"Same as MATLAB Default"` (default) | `"Other:UserSpecified"` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `yesa` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

You can generate Halide code if you have Embedded Coder® license. For more information, see Speed Up Generated Code Execution with Halide Code (Embedded Coder).

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. Actual data type or capability support depends
on block implementation. For best practices of using the MATLAB
Function block, see:

- Use hdlfimath Setting and Specify fi Objects inside MATLAB Function Block (HDL Coder)
- Design Guidelines for the MATLAB Function Block (HDL Coder)
- Generate Instantiable Code for Functions (HDL Coder)
- Optimize MATLAB Loops (HDL Coder)
- Pipeline MATLAB Expressions (HDL Coder)

**HDL Architecture**

|  |  |
| --- | --- |
| `MATLAB Function` (Default) | This is the default architecture for MATLAB Function blocks with fixed-point data types. When you use this architecture, you can use speed and area optimizations for blocks that surround the MATLAB Function block. The code inside the MATLAB Function block is not optimized. |
| `MATLAB Datapath` | This is the default architecture for MATLAB Function blocks with floating-point data types. When you use this architecture, the code generator treats the MATLAB Function block like a regular Subsystem block. By enabling this architecture for fixed-point types, you can use speed and area optimizations for blocks inside the MATLAB Function block and across the MATLAB Function block with other Simulink blocks.  This capability enables you to specify additional properties for the MATLAB Function block that you would specify for a Subsystem such as **ClockRatePipelining** and **FlattenHierarchy**. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **AdaptivePipelining** | Automatic pipeline insertion based on the synthesis tool, target frequency, and multiplier word-lengths. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also AdaptivePipelining (HDL Coder). |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also BalanceDelays (HDL Coder). |
| **ClockRatePipelining** | Insert pipeline registers at a faster clock rate instead of the slower data rate. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also ClockRatePipelining (HDL Coder). |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also DSPStyle (HDL Coder). |
| **FlattenHierarchy** | Remove MATLAB Function block hierarchy from generated HDL code. The default is `inherit`. To specify this property, set **Architecture** to `MATLAB Datapath`. See also FlattenHierarchy (HDL Coder). |
| **GuardIndexVariables** | Choose whether or not to lift matrix accesses out of conditional MATLAB statements. The default is `off`. To specify this property, set **Architecture** to `MATLAB Function`. See also GuardIndexVariables (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **InstantiateFunctions** | Generate a VHDL® `entity` or Verilog® `module` for each function. The default is `off`. See also InstantiateFunctions (HDL Coder). |
| **LoopOptimization** | Unroll, stream, or do not optimize loops. The default is `none`. If you set **Architecture** to `MATLAB Datapath`, you can only unroll loops. If you want to use loop streaming with the `MATLAB Datapath` architecture, you can use the streaming optimization by specifying a **StreamingFactor**. See also LoopOptimization (HDL Coder). |
| **MapPersistentVarsToRAM** | Map persistent arrays to RAM. The default is `off`. See also MapPersistentVarsToRAM (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. To specify this property, set **Architecture** to `MATLAB Datapath`. See also Streaming (HDL Coder). |
| **VariablesToPipeline** | **Warning**  `VariablesToPipeline` is not recommended. Use `coder.hdl.pipeline` (HDL Coder) instead.  Insert a pipeline register at the output of the specified variable or variables. Specify the list of variables as a character vector, with spaces separating the variables. To specify this property, set **Architecture** to `MATLAB Function`. |

**Data Type Support**

HDL code generation supports half-precision data types for these functions in
MATLAB Function block:

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

**Complex Data Support**

This block supports code generation for complex signals.

See also Complex Data Type Support (HDL Coder).

**Use `hdlfimath` Setting**

The `hdlfimath` function is a utility that defines
`fimath` properties optimized for HDL code generation. For
more information, see Use hdlfimath Setting and Specify fi Objects inside MATLAB Function Block (HDL Coder).

**Tunable Parameter Support**

HDL Coder supports both tunable and non-tunable parameters with the
following data types:

- Scalar
- Vector
- Complex
- Structure
- Enumeration

For details, see Generate DUT Ports for Tunable Parameters (HDL Coder) and Design Guidelines for the MATLAB Function Block (HDL Coder).

**Generate HDL Code with Algebraic Loops**

To generate HDL code for models that contain Matlab Function
blocks:

- In the Configuration Parameters dialog box, click
  **Diagnostics**, and set the
  **Algebraic loop** parameter to
  `none` or
  `warning`.
- Open the block mask for the Matlab Function block and
  select the **Treat as atomic unit** and
  **Minimize algebraic loop occurrences**
  parameters.

**Restrictions**

- If the block contains a System object™, block inputs cannot have non-discrete (constant or
  `Inf`) sample time.
- HDL Coder does not support a MATLAB Function that
  contains the same variable as the input and output of the function. For
  example, this MATLAB code is not
  supported.

  ```
  function y = myFun(y)
  %#codegen

  y = 3 * y;
  ```
- The block supports floating-point data types only in the Native
  Floating Point mode.

For the MATLAB language subset supported for HDL code generation from a
MATLAB Function block, see Supported MATLAB Data Types, Operators, and Control Flow Statements (HDL Coder).

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

**PLC Block Properties**

|  |  |
| --- | --- |
| **UseExternalDefinition** | Suppress block definition in generated code. The default is `Off`. See also UseExternalDefinition (Simulink PLC Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2011a**

### R2023a: Specify how to treat output variables with dimension of length 1

With the new **Treat dimensions of length 1 as fixed size** parameter,
you can specify how MATLAB Function blocks treat output variables
when at least one dimension has length 1. Prior to R2023a, MATLAB
Function blocks treat output variables with a dimension of length 1 as
fixed size, regardless of whether you specify the variables as having variable
size.

### R2021b: Output column vectors as two-dimensional or one-dimensional data

You can now output column vectors in MATLAB Function blocks as
two-dimensional or one-dimensional data with the **Interpret output column
vectors as one-dimensional data** parameter.

### R2021a: Report runtime errors for MATLAB Function blocks in rapid accelerator mode

Report runtime errors for MATLAB Function blocks when simulating in
rapid accelerator mode by setting the **Enable memory integrity checks**
configuration parameter to `Always on`.

### R2020a: 64-bit integer type support for MATLAB Function block

MATLAB Function blocks now support 64-bit integer data. The block
implements `int64` and `uint64` data types as
fixed-point numbers with a word length of 64 bits and a fraction length of 0.

### R2019b: String support for MATLAB Function block

Simulink strings are now supported in MATLAB Function
blocks.
