---
type: simulink-block
title: 'MATLAB Function'
family: 'libsb2sl'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'USR'
documentation_page: 'matlabfunction'
documentation_source_path: '../simulink/slref/matlabfunction.html'
language: zh-CN
chinese_source: official
---

# MATLAB Function

## 端口

### 输入

### **Port\_1** — 输入变量 标量 | 向量 | 矩阵

MATLAB 函数中的输入变量，指定为实数值标量、向量或矩阵。每个输入变量都有一个使用该变量名称的关联端口。

您不能在 Simulink 模型和 MATLAB Function 模块中的函数之间传递 MATLAB 支持但 Simulink 不支持的数据类型。您可以在 MATLAB Function 模块中使用这些数据类型。

有关此模块支持的定点数据类型的详细信息，请参阅Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer)和Data Type Override with MATLAB Function Block (Fixed-Point Designer)。

#### 依赖关系

要创建输入端口，请打开模块并在**符号**窗格中创建输入变量。请参阅Create and Define MATLAB Function Block Variables。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出变量 标量 | 向量 | 矩阵

MATLAB 函数中的输出变量，指定为实数值标量、向量或矩阵。每个输出变量都有一个使用该变量名称的关联端口。

#### 依赖关系

要创建输出端口，请打开模块并在**符号**窗格中创建输出变量。请参阅Create and Define MATLAB Function Block Variables。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

**注意**

MATLAB Function 模块也有 Subsystem 模块参数，您可以通过右键点击模块并点击**模块参数(子系统)** 来访问这些参数。但是，不推荐更新这些模块参数。

### **更新方法** — 用于激活模块的方法 **继承** (默认) | **离散** | **连续**

将激活 MATLAB Function 模块的方法指定为以下值之一：

- **继承** - 来自 Simulink 模型的输入激活 MATLAB Function 模块。

  如果您定义输入触发器，则 MATLAB Function 模块会执行，以响应触发端口上的 Simulink 信号或函数调用事件。如果您没有定义输入触发器，则 MATLAB Function 模块将从模型中隐式继承触发器。这些隐式事件是向模块提供输入的信号的离散或连续采样时间。

  如果您定义了数据输入，则 MATLAB Function 模块以最快的数据输入速率进行采样。如果未定义数据输入，则 MATLAB Function 模块以父级子系统的执行行为定义的速率进行采样。
- **离散** - MATLAB Function 模块使用您在模块的**采样时间**参数中指定的速率激活。该模块以对应于指定速率的固定时间间隔生成隐式事件。模型中的其他模块可以有不同采样时间。
- **连续** - MATLAB Function 模块仅在主时间步期间激活，在主时间步和子时间步内都会计算输出和局部连续变量。模块可以记录过零，这样，只要状态发生变化，Simulink 模型就可以对模块进行采样。模块计算局部连续变量的导数。

#### 编程用法

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

### **采样时间** — 仿真期间模块激活的时间间隔 `-1` (默认) | 标量 | 向量

指定在仿真期间 MATLAB Function 模块激活的时间间隔。默认值表示模块从 Simulink 继承采样时间。有关指定采样时间的详细信息，请参阅指定采样时间。

不要在 Subsystem 模块参数中使用**采样时间**参数。请改用属性检查器。

#### 依赖关系

要启用此参数，请将**更新方法**设置为**离散**。

#### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar | vector |
| **数据类型:** | `string` | `char` |

### 高级

### **对整数溢出进行饱和处理** — 数据是否对整数溢出进行饱和处理 `on` (默认) | `off`

将 MATLAB Function 模块中的数据在发生整数溢出时是否进行饱和指定为以下值之一：

- `on` - 模块通过将整数设置为字长允许的最大正值或负值对整数进行饱和处理。此设置匹配 MATLAB 行为。
- `off` - 当发生溢出情况时，模块在仿真模式下生成运行时错误。当您使用 Simulink Coder 生成代码时，行为取决于您的 C 语言编译器。

#### 提示

- 当此参数为 `on` 时，MATLAB 会在仿真期间添加额外的检查以检测整数上溢或下溢。如果 MATLAB Function 模块代码中没有发生整数溢出，则禁用此选项会更高效。
- 由 Simulink Coder 生成的代码不检查整数上溢或下溢，因此，当此参数为 `off` 时，可能会产生不可预测的结果。在这种情况下，请在生成代码之前仿真您的模型以测试上溢和下溢。
- 此参数设置仅与整数算术相关。它对定点或双精度算术不起作用。

#### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **支持可变大小数组** — 模块是否支持可变大小数据 `on` (默认) | `off`

指定 MATLAB Function 模块是否支持在仿真期间维度可变的输入和输出数据。当此参数为 `on` 时，您可以通过启用输出变量的**可变大小**属性来定义可变大小输出。有关详细信息，请参阅声明可变大小的 MATLAB Function 模块变量和Variable size。

#### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `SupportVariableSizing` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **允许直接馈通** — 模块是否支持直接馈通语义 `on` (默认) | `off`

指定 MATLAB Function 模块是否支持直接馈通语义，以便模块的输出由输入的值直接控制。当此参数为 `off` 时，模块输出仅依赖模块的当前状态。使用非直接馈通使您能够在反馈环中使用 MATLAB Function 模块并防止代数环。有关详细信息，请参阅 Use Nondirect Feedthrough in a MATLAB Function Block。

#### 依赖关系

要禁用此参数，您必须将**更新方法**设置为**继承**或**离散**。

#### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `AllowDirectFeedthrough` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### **将输出列向量解释为一维数据** — 模块是否将维度长度为 1 的输出变量视为固定大小 `off` (默认) | `on`

*自 R2021b 起*

将 MATLAB Function 模块是否将维度长度为 1 的输出变量视为固定大小指定为以下值之一：

- `off` - 无论您是否将变量指定为具有可变大小，模块都将至少一个维度的长度为 1 的输出变量视为固定大小。
- `on` - 如果您将变量指定为具有可变大小，则 MATLAB Function 模块将输出变量视为可变大小。

有关详细信息，请参阅Variable size。

**注意**

在 R2021b 及更早版本中，MATLAB Function 模块始终将输出列向量转换为一维信号。

#### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `VectorOutputs1D` |
| **值:** | `false` or `0` (默认) | `true` or `1` |
| **数据类型:** | `logical` |

### **将长度为 1 的维度视为固定大小** — 至少一个维度的长度为 1 的变量是否为固定大小 `on` (默认) | `off`

*自 R2023a 起*

将至少一个维度的长度为 1 的变量是否为固定大小指定为以下值之一：

- `on` - 一个维度的长度为 1 的可变大小变量是固定大小的变量。
- `off` - 模块中启用**可变大小**属性的变量始终为可变大小。

此参数仅影响启用**可变大小**属性的输出变量。请参阅Variable size。

#### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值:** | `true` or `1` (默认) | `false` or `0` |
| **数据类型:** | `logical` |

### 定点属性

### **将这些继承的 Simulink 信号类型视为 fi 对象** — 继承的 Simulink 信号被视为 `fi` 对象 `Fixed-point` (默认) | `Fixed-point & Integer`

将是否将继承的定点和整数信号视为 Fixed-Point Designer™ `fi` (Fixed-Point Designer) 对象指定为以下值之一：

- `Fixed-point` - MATLAB Function 模块将所有定点输入视为 Fixed-Point Designer `fi` 对象。
- `Fixed-point & Integer` - MATLAB Function 模块将所有定点和整数输入视为 Fixed-Point Designer `fi` 对象。

有关详细信息，请参阅Ways to Construct fi Objects (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用圆点表示法访问模块的 `MATLABFunctionConfiguration` 或 `Stateflow.EMChart` 对象和更改对象属性。

|  |  |
| --- | --- |
| **参数:** | `TreatAsFi` |
| **值:** | `"Fixed-point"` (默认) | `"Fixed-point & Integer"` |

### **MATLAB 函数 fimath** — 默认 `fimath` 属性 `Same as MATLAB` (默认) | `Specify Other`

将 MATLAB Function 模块的默认 `fimath` (Fixed-Point Designer) 对象属性指定为以下值之一：

- `Same as MATLAB` - 模块使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框灰显，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` - 以两种方式之一在文本框中指定您自己的 `fimath` 对象：

  - 在文本框内构造 `fimath` 对象。
  - 在 MATLAB 或模型工作区中构造 `fimath` 对象，然后在文本框中输入其变量名称。如果您使用此选项并计划与其他人共享您的模型，请在模型工作区中定义此变量。

有关详细信息，请参阅 fimath Object Construction (Fixed-Point Designer)和Fixed-Point Data Types with MATLAB Function Block (Fixed-Point Designer)。

#### 提示

- MATLAB Function 模块的 `fimath` 对象对于该模块的内容表现为 `globalfimath` (Fixed-Point Designer) 对象。该模块将此参数中的 `fimath` 对象属性与您选择视为 `fi` 对象的 MATLAB Function 模块的所有定点和整数输入信号相关联。在 MATLAB Function 模块中构造 `fi` 对象需要考虑其他注意事项。

  - 如果在构造 `fi` 对象时没有与之相关联的 `fimath` 对象，则 `fi` 构造函数使用默认 `fimath` 对象设置，而不考虑 **MATLAB 函数 fimath** 中的属性。如果在构造 `fi` 对象后对其执行操作，该对象将采用 **MATLAB 函数 fimath** 中的属性。
  - 如果您在 `fi` 构造函数中指定 `fimath` 对象，则 `fi` 构造函数在量化值时遵循该 `fimath` 对象。`fi` 构造函数中未指定的任何 `fimath` 对象设置都使用 **MATLAB 函数 fimath** 中的指定属性。

#### 编程用法

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

## 所属库

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

## 模块特性

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

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

如果您有 Embedded Coder® 许可证，您可以生成 Halide 代码。有关详细信息，请参阅Speed Up Generated Code Execution with Halide Code (Embedded Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

**PLC 模块属性**

|  |  |
| --- | --- |
| **UseExternalDefinition** | 在生成的代码中取消模块定义。默认值为 **Off**。另请参阅UseExternalDefinition (Simulink PLC Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2011a 中推出**

### R2023a: 指定如何处理维度长度为 1 的输出变量

使用新的**将长度为 1 的维度视为固定大小**参数，您可以指定当至少一个维度的长度为 1 时，MATLAB Function 模块如何处理输出变量。在 R2023a 之前，MATLAB Function 模块将一个维度长度为 1 的输出变量视为固定大小，无论您是否将变量指定为具有可变大小。

### R2021b: 将列向量输出为二维或一维数据

现在您可以使用**将输出列向量解释为一维数据**参数将 MATLAB Function 模块中的列向量输出为二维或一维数据。

### R2021a: 报告 MATLAB Function 模块在快速加速模式下的运行时错误

通过将**启用内存完整性检查**配置参数设置为**始终打开**，报告在快速加速模式下进行仿真时 MATLAB Function 模块的运行时错误。

### R2020a: 对 MATLAB Function 模块的 64 位整数类型支持

MATLAB Function 模块现在支持 64 位整数数据。该模块将 `int64` 和 `uint64` 数据类型实现为定点数，字长为 64 位，小数长度为 0。

### R2019b: 对 MATLAB Function 模块的字符串支持

现在，MATLAB Function 模块支持 Simulink 字符串。

## 描述

在 Simulink 模型中包含 MATLAB 代码

MATLAB Function 模块使您能够编写在 Simulink® 模型中执行的 MATLAB® 函数。MATLAB 函数在仿真期间的每个时间步执行。有关将 MATLAB 代码集成到 Simulink 模型中的详细信息，请参阅使用 MATLAB Function 模块在 Simulink 中实现 MATLAB 函数。如果您有 Simulink Coder™ 许可证，您还可以从 MATLAB Function 模块为 Simulink Coder 目标生成 C/C++ 代码。

双击 MATLAB Function 模块可打开 MATLAB Function 模块编辑器，您可以在其中编写 MATLAB 函数。您还可以使用模型资源管理器或**符号**窗格来定义变量、添加输入触发器以及创建函数调用输出。有关详细信息，请参阅Create and Define MATLAB Function Block Variables、Manage the Input Trigger of a MATLAB Function Block和Manage Function Call Outputs of a MATLAB Function Block。

在**符号**窗格中，您可以将模块输入声明为 Simulink 参数，而不是端口。MATLAB Function 模块还支持继承输入、输出和参数的类型及大小。您可以显式指定这些属性。请参阅定义和修改变量数据类型、指定 MATLAB Function 模块变量的大小和通过定义参数变量在多个 MATLAB Function 模块中使用数据。

当您仿真包含 MATLAB Function 模块的模型时，软件会从该模块生成二进制代码或 C/C++ 语言的 MATLAB 可执行文件 (MEX) 代码，并将此代码与模型集成。MATLAB Function 模块使用与 MATLAB Coder 相同的基础架构，您可使用该基础架构从 Simulink 之外的 MATLAB 代码生成 C/C++ 代码。因此，MATLAB Function 模块代码必须使用代码生成支持的 MATLAB 约定。请参阅Code and Integration Limitations for MATLAB Function Blocks。

为支持数据可视化，MATLAB Function 模块仅支持调用 MATLAB 函数进行仿真。请参阅使用 MATLAB 引擎在 MATLAB Function 模块中执行函数调用。如果使用 Simulink Coder 生成代码，并且函数调用不直接影响 Simulink 输入或输出，则调用不会出现在生成的代码中。
