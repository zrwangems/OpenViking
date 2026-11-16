---
type: simulink-block
title: 'Chart'
family: 'stateflow'
product_id: 'stateflow'
product_name: 'Stateflow'
documentation_release: R2025b
official_category: 'Chart Programming / Chart Programming Basics / Stateflow Charts'
documentation_page: 'chart'
documentation_source_path: 'ref/chart.html'
language: zh-CN
chinese_source: worker-translation
---

# Chart

## 端口

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

当您使用 **符号** 窗格在 Stateflow Chart 中创建输入数据时，Stateflow 会在 Chart 模块上创建对应的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

当您使用 **符号** 窗格在 Stateflow Chart 中创建输出数据时，Stateflow 会在 Chart 模块上创建对应的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

**注意**

Chart 还具有 Subsystem (Simulink) 模块参数，您可以通过右键单击 Chart 并单击 **模块参数 (Subsystem)** 来访问这些参数。但是，不建议更新这些参数。

### **更新方法** — 更新或唤醒 Stateflow Chart 的方法 `Inherited`（默认）| `Discrete` | `Continuous`

用于更新或唤醒 Stateflow Chart 的方法，指定为 `Inherited`、`Discrete` 或 `Continuous`。

`Inherited`
:   Simulink 模型的输入决定 Chart 在仿真期间何时唤醒。

    如果为 Chart 定义输入事件，则连接到触发端口的 Simulink 模块发出的信号会触发 Chart。Simulink 信号可以是 `Rising`、`Falling` 或 `Either`（上升沿和下降沿），也可以响应 `Function Call`。有关详细信息，请参阅通过发送输入事件激活 Stateflow Chart。

    如果未定义输入事件，则 Stateflow Chart 会隐式继承 Simulink 模型的触发。这些隐式事件是为 Chart 提供输入的 Simulink 信号的离散或连续采样时间。如果定义数据输入，则 Chart 以最快数据输入的速率唤醒。如果未为 Chart 定义任何数据输入，则 Chart 按其父级子系统的执行行为所定义的方式唤醒。

`Discrete`
:   当 Simulink 模型按您在 **采样时间** Chart 属性中指定的固定时间间隔生成隐式事件时，Stateflow Chart 唤醒。Simulink 模型中的其他模块可以具有不同的采样时间。

`Continuous`
:   Stateflow Chart 仅在主时间步中更新其状态，并在主时间步和次时间步中计算输出和局部连续变量。Chart 可以记录过零点，这允许 Simulink 模型在发生状态更改时对 Stateflow Chart 进行采样。Stateflow Chart 为局部连续变量计算导数。有关详细信息，请参阅 Stateflow 中的连续时间建模。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ChartUpdate` |
| **值：** | `"INHERITED"`（默认）| `"CONTINUOUS"` | `"DISCRETE"` |

### **采样时间** — Stateflow Chart 在仿真期间唤醒的时间间隔 `-1`（默认）| 标量 | 向量

指定 Chart 在仿真期间唤醒的时间间隔。默认值表示 Chart 从 Simulink 继承采样时间。有关指定采样时间的详细信息，请参阅指定采样时间 (Simulink)。

不要使用 Subsystem 模块参数中的 **采样时间** 参数。而应使用属性检查器。

#### 依赖关系

要启用此参数，请将 **更新方法** 设置为 `Discrete`。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认）| string scalar | character vector |
| **数据类型：** | `string` | `char` |

### **启用过零检测** — 是否在 Chart 中的状态转移上启用过零检测 `on`（默认）| `off`

是否在 Chart 中的状态转移上启用过零检测。有关详细信息，请参阅 Stateflow 中的连续时间建模。

#### 依赖关系

要启用此参数，请将 **更新方法** 设置为 `Continuous`。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnableZeroCrossings` |
| **值：** | `true` or `1`（默认）| `false` or `0` |
| **数据类型：** | `logical` |

### **启用 C 位操作** — 是否在 Chart 中启用 C 位操作 `off`（默认）| `on`

是否在 Chart 的状态和转移操作中使用位操作，指定为数值或逻辑值 1 (true) 或 0 (false)。

#### 依赖关系

要启用此参数，请将 **操作语言** 设置为 `C`。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnableBitOps` |
| **值：** | `false` or `0`（默认）| `true` or `1` |
| **数据类型：** | `logical` |

### **创建用于监视的输出** — 是否创建活动状态数据输出 `off`（默认）| `on`

是否为 Chart 创建活动状态数据输出端口。有关详细信息，请参阅通过活动状态数据监视状态活动。

#### 依赖关系

要启用此参数，请创建 Stateflow 状态、状态转移表或原子子图。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `HasOutputData` |
| **值：** | `false` or `0`（默认）| `true` or `1` |
| **数据类型：** | `logical` |

### **输出监视模式** — 活动状态输出的监视模式 `Child activity`（默认）| `Leaf state activity`

活动状态输出数据的监视模式。有关详细信息，请参阅通过活动状态数据监视状态活动。

#### 依赖关系

要启用此参数，请启用 **创建用于监视的输出**。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `OutputMonitoringMode` |
| **值：** | `"ChildActivity"`（默认）| `"LeafStateActivity"` |

### **数据名称** — 活动状态数据对象的名称 `ChartMode` | 标量

状态转移表的活动状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用 **创建用于监视的输出**。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `OutputPortName` |
| **值：** | `"ChartMode"`（默认）| string scalar | character vector |
| **数据类型：** | `string` | `char` |

### **枚举名称** — 活动状态数据对象的枚举数据类型名称 `ChartModeType` | 标量

状态转移表的活动状态数据对象的名称。

#### 依赖关系

要启用此参数，请启用 **创建用于监视的输出**。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnumTypeName` |
| **值：** | `"ChartModeType"`（默认）| string scalar | character vector |
| **数据类型：** | `string` | `char` |

### **手动定义枚举类型** — 是否手动定义枚举数据类型 `off`（默认）| `on`

是否手动为活动状态数据输出定义枚举数据类型。有关详细信息，请参阅定义状态活动枚举类型。

#### 依赖关系

要启用此参数，请启用 **创建用于监视的输出**。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `DoNotAutogenerateEnum` |
| **值：** | `false` or `0`（默认）| `true` or `1` |
| **数据类型：** | `logical` |

### 高级

### **在初始化时执行（进入）Chart** — 是否初始化状态配置 `off`（默认）| `on`

是否在时间零而不是在第一个输入事件时初始化 Chart 的状态配置。有关详细信息，请参阅初始化时 Chart 的执行。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ExecuteAtInitialization` |
| **值：** | `false` or `0`（默认）| `true` or `1` |
| **数据类型：** | `logical` |

### **整数溢出时饱和** — 数据在整数溢出时是否饱和 `on`（默认）| `off`

Chart 中的数据在整数溢出时是否饱和。清除此参数后，Chart 中的数据在整数溢出时回绕。有关详细信息，请参阅处理 Chart 数据的整数和枚举溢出。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `true` or `1`（默认）| `false` or `0` |
| **数据类型：** | `logical` |

### **每次 Chart 唤醒时初始化输出** — 是否初始化输出数据 `on`（默认）| `off`

是否在每次 Chart 唤醒时初始化输出数据。

选中此参数后，Chart 会在每次唤醒时重置其输出值，而不仅仅是在时间 0。只要函数调用、边沿触发或时钟节拍触发 Chart，Chart 就会重置输出值。如果为输出数据对象设置了初始值，则输出会重置为该值。否则，输出会重置为零。选择此参数可以：

- 确保在每次 Chart 执行中都定义所有输出。
- 防止输出锁存，即防止保留以前执行中计算的输出值。
- 为所有 Chart 输出提供有意义的初始值。

有关详细信息，请参阅初始值。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `InitializeOutput` |
| **值：** | `true` or `1`（默认）| `false` or `0` |
| **数据类型：** | `logical` |

### **支持可变大小数组** — Chart 是否支持可变大小数据 `on`（默认）| `off`

Chart 是否支持可变大小数据。有关详细信息，请参阅在 Stateflow Chart 中声明可变大小数据。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `SupportVariableSizing` |
| **值：** | `true` or `1`（默认）| `false` or `0` |
| **数据类型：** | `logical` |

### **导出 Chart 级函数** — 是否导出 Chart 级函数 `off`（默认）| `on`

是否将 Chart 级函数导出到 Simulink 模型中的其他模块。有关详细信息，请参阅导出 Stateflow 函数以供重用。

#### 依赖关系

要启用此参数，请向 Chart 中添加函数。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ExportChartFunctions` |
| **值：** | `false` or `0`（默认）| `true` or `1` |
| **数据类型：** | `logical` |

### **将导出的函数视为全局可见** — 导出的函数是否全局可见 `off`（默认）| `on`

从 Chart 导出的函数在 Simulink 模型中是否全局可见。启用此属性后，整个模型中的模块都可以调用从 Chart 导出的函数，而无需使用限定表示法。

#### 依赖关系

要启用此参数，请启用 **导出 Chart 级函数**。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `AllowGlobalAccessToExportedFunctions` |
| **值：** | `false` or `0`（默认）| `true` or `1` |
| **数据类型：** | `logical` |

### **启用超步语义** — 是否启用超步语义 `off`（默认）| `on`

是否为 Chart 启用超步语义。选择此参数可使 Chart 在每个时间步中执行多个转移，直到达到稳定状态。当您将 Chart 属性 **更新方法** 设置为 `Continuous` 时，此选项不可用。有关详细信息，请参阅超步语义。

#### 依赖关系

要启用此参数，请将 **更新方法** 设置为 `Discrete`。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EnableNonTerminalStates` |
| **值：** | `false` or `0`（默认）| `true` or `1` |
| **数据类型：** | `logical` |

### **超步中的最大迭代次数** — 最大转移数 `1000`（默认）| 正整数

在一个超步中可以完成的最大转移数。有关详细信息，请参阅超步语义。

#### 依赖关系

要启用此参数，请启用 **启用超步语义**。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `NonTerminalMaxCounts` |
| **值：** | `1000`（默认）| 正整数 |
| **数据类型：** | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` |

### **迭代次数过多后** — 超步超过最大转移数时的操作 `Proceed`（默认）| `Throw Error`

如果超步在一个超步中超过最大转移数，Stateflow 要执行的操作。有关详细信息，请参阅超步语义。

#### 依赖关系

要启用此参数，请启用 **启用超步语义**。

#### 编程用法

要以编程方式设置 Chart 参数值，请访问 Chart 的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `NonTerminalUnstableBehavior` |
| **值：** | `"Proceed"`（默认）| `"Throw Error"` |

### **将长度为 1 的维度视为固定大小** — 图是否将维度长度为 1 的非标量数据视为固定大小 `on`（默认）| `off`

*自 R2022b 起*

图是否将维度长度为 1 的非标量数据视为固定大小。选中此参数时，图将至少有一个维度长度为 1 的非标量数据视为固定大小，无论是否启用 **可变大小** 数据属性。清除此参数时，图将启用了 **可变大小** 属性的非标量数据视为可变大小。

#### 程序化使用

要以程序化方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatDimensionOfLengthOneAsFixedSize` |
| **值：** | `true` 或 `1`（默认） | `false` 或 `0` |
| **数据类型：** | `logical` |

### **变体激活时间** — 在仿真和代码生成工作流的不同阶段对变体模块或变体参数的活动选择 `update diagram analyze all choices`（默认）| `code compile`

指定 Stateflow 在仿真和代码生成期间分析哪些模块变体。根据您选择的选项，Stateflow 确定生成的代码必须只包含活动选择，还是同时包含活动和非活动选择。

- `update diagram analyze all choices` — 选中此选项时，Stateflow 分析活动和非活动选择中的信号属性不兼容性，并且仅为活动选择生成代码。
- `code compile` — 选中此选项时，Stateflow 分析变体转移的活动和非活动选择，并为活动和非活动选择生成代码。这些选择包含在 C 预处理器条件语句 #if 和 #endif 中，这些语句在编译生成的代码时进行条件编译。

#### 程序化使用

要以程序化方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `VariantActivationTime` |
| **值：** | `"update diagram analyze all choices"`（默认） | `"code compile"` |

### **操作语言** — 操作语言 `MATLAB`（默认）| `C`

用于编写图的操作语言，指定为 `MATLAB` 或 `C`。有关详细信息，请参阅 Differences Between MATLAB and C as Action Language Syntax。

#### 程序化使用

要以程序化方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `ActionLanguage` |
| **值：** | `"MATLAB"`（默认） | `"C"` |

### **状态机类型** — 状态机语义 `Classic`（默认）| `Mealy` | `Moore`

图实现的状态机语义，指定为 `Classic`、`Mealy` 或 `Moore`。有关详细信息，请参阅 Overview of Mealy and Moore Machines。

#### 程序化使用

要以程序化方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `StateMachineType` |
| **值：** | `"Classic"`（默认） | `"Mealy"` | `"Moore"` |

### 定点属性

### **将继承的 Simulink 信号类型视为 fi 对象** — 要视为 `fi` 对象的继承 Simulink 信号 `Fixed-point`（默认）| `Fixed-point & Integer`

要视为 Fixed-Point Designer™ `fi` 对象的继承 Simulink 信号，指定为以下值之一：

- `Fixed-point` — 图将所有定点输入视为 `fi` 对象。
- `Fixed-point & Integer` — 图将所有定点和整数输入视为 `fi` 对象。

#### 依赖项

要启用此参数，请将 **操作语言** 设置为 `MATLAB`。

#### 程序化使用

要以程序化方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `TreatAsFi` |
| **值：** | `"Fixed-point"`（默认） | `"Fixed-point & Integer"` |

### **MATLAB Chart fimath** — 默认 `fimath` 属性 `Same as MATLAB`（默认）| `Specify Other`

图的默认 `fimath` 属性，指定为以下值之一：

- `Same as MATLAB` — 图使用与当前默认 `fimath` 对象相同的 `fimath` 对象属性。文本框变暗，并以只读形式显示当前全局 `fimath` 对象。
- `Specify other` — 通过以下两种方式之一在文本框中指定您自己的 `fimath` 对象：

  - 在文本框中构造 `fimath` 对象。
  - 在 MATLAB 或模型工作区中构造 `fimath` 对象，然后在文本框中输入其变量名。如果使用此选项并计划与他人共享模型，请在模型工作区中定义该变量。

有关详细信息，请参阅 fimath Object Construction (Fixed-Point Designer)。

#### 依赖项

要启用此参数，请将 **操作语言** 设置为 `MATLAB`。

#### 程序化使用

要以程序化方式设置图参数值，请访问图的 `Stateflow.Chart` 对象，并使用点表示法更改对象属性。

|  |  |
| --- | --- |
| **参数：** | `EmlDefaultFimath` |
| **值：** | `"Same as MATLAB Default"`（默认） | `"Other:UserSpecified"` |

## 所属库

Stateflow

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一种默认 HDL 架构。

**活动状态输出**

要在 HDL 代码中生成显示活动状态的输出端口，请在图的属性窗口中选择 **Create output for monitoring**。输出是枚举数据类型。请参阅 Simplify Stateflow Charts by Incorporating Active State Output。

**寄存器输出**

要插入将图输出延迟一个仿真周期的输出寄存器，请使用 OutputPipeline (HDL Coder) 模块属性。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ClockDrivenOutput** | 启用时钟驱动输出，以防止组合逻辑驱动输出，并允许在时钟信号和状态变化时立即更新输出。默认值为 `off`。将 **ClockDrivenOutput** 设置为 `on` 时，HDL Coder 会添加一个在状态更新时更新的输出寄存器。然后，最终输出变量从时钟驱动寄存器赋值。此选项仅适用于 Moore 图。 |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **GuardIndexVariables** | 指定是否将数组索引提升到条件语句之外。启用某些优化（例如 RAM 映射、循环流式处理、共享等）时，表达式会移出数组索引。会为该表达式创建一个临时变量，这可能在仿真期间导致索引越界错误。默认值为 `off`。请参阅 GuardIndexVariables (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **InstantiateFunctions** | 为每个函数生成 VHDL® `entity` 或 Verilog® `module`。默认值为 `off`。另请参阅 InstantiateFunctions (HDL Coder)。 |
| **LoopOptimization** | 展开、流式处理或不优化循环。默认值为 `none`。另请参阅 LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 `off`。另请参阅 MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，这会生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

**优化**

此模块参与这些 HDL 优化，以优化速度和面积。

**速度和面积优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *分布式流水线*，或寄存器重定时，是一种速度优化，它移动设计中的现有延迟以减少关键路径，同时保持功能行为。 |
| Resource Sharing (HDL Coder) | *资源共享*是一种面积优化，HDL Coder 在其中识别多个功能等效资源，并将它们替换为单个资源。 |
| Understand Delay Balancing in HDL Coder (HDL Coder) | 当优化或模块实现选项在模型中沿关键路径引入延迟时，*延迟平衡*会检测沿一条路径引入的新延迟，然后在其他路径上插入匹配的延迟。 |
| Clock-Rate Pipelining (HDL Coder) | *时钟速率流水线*是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *自适应流水线*优化创建带寄存器的模块模式或组合，通过向设计中的模块插入流水线寄存器，可提高可实现的时钟频率并减少 FPGA 板上的面积使用。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中很可能的关键路径，请使用 *关键路径估计*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**限制**

要了解使用图的限制，请参阅 Introduction to Stateflow HDL Code Generation (HDL Coder)。

应用优化时，此模块有以下限制：

- **状态机类型** 属性设置为 `Moore` 的 Stateflow Chart 不支持 HDL 优化。
- 具有 **Trigger** 端口的 Stateflow Chart 不支持 HDL 优化。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

**PLC 模块属性**

|  |  |
| --- | --- |
| **UseExternalDefinition** | 禁止在生成的代码中定义模块。默认值为 `Off`。另请参阅 UseExternalDefinition (Simulink PLC Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**R2006a 之前引入**

### R2024a: 转移和并行状态的隐式排序将被移除

在未来的版本中，属性 **User-specified state/transition execution order** 将被移除。此属性仅适用于使用 C 作为操作语言的图。

- 启用此属性时，图按创建转移和并行状态的顺序执行它们。您也可以手动确定执行顺序。
- 禁用此属性时，图根据物理位置定义的隐式顺序执行转移和并行状态。

  转移按以下规则执行：

  1. 每个转移父级的层级。
  2. 转移的标签，按以下顺序：

     1. 带事件和条件的标签。
     2. 带事件的标签。
     3. 带条件的标签。
     4. 无标签。
  3. 转移源的角表面位置。时钟位置最小的转移具有最高优先级。例如，2 点钟位置的转移比 4 点钟位置的转移具有更高优先级。源位置为 12 点钟的转移具有最低优先级。

  并行状态按以下顺序执行：

  1. 从上到下。
  2. 从左到右。

为确保隐式排序的图保持兼容，请启用 **User-specified state/transition execution order** 属性。

### R2023b: 转换为状态转移表

要将图转换为状态转移表，请使用函数 `convertToSTT`。

### R2023a: 指定如何处理维度长度为 1 的非标量数据

使用新属性 **将长度为 1 的维度视为固定大小**，您可以指定当至少一个维度长度为 1 时图如何处理非标量数据。在 R2023a 之前，无论是否启用 **可变大小** 数据属性，图都会将至少有一个维度长度为 1 的非标量数据视为固定大小。

## 描述

使用有限状态机实现控制逻辑

Chart 模块以图形方式表示有限状态机。在 Stateflow® 图中，状态和转移构成顺序模态逻辑系统的基本构建块。状态对应于操作模式，转移表示系统从一种操作模式到另一种操作模式的转换。有关详细信息，请参阅 Model a Finite State Machine。

为实现控制逻辑，Stateflow 图可以使用 MATLAB® 或 C 作为操作语言。有关详细信息，请参阅 Differences Between MATLAB and C as Action Language Syntax。
