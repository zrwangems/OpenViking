---
type: simulink-block
title: 'MATLAB System'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'matlabsystem'
---

# MATLAB System

Include System object in model

## 中文

在模型中包含 System object

### 所属库

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

### 描述

MATLAB System 模块将现有的 System object（基于 `matlab.System`）添加到 Simulink® 中。它还允许您使用 System object API 为 Simulink 开发新模块。有关此模块的详细信息，请参阅使用 MATLAB System 模块和 System object 创建自定义模块。

对于解释执行，模型使用 MATLAB® 执行引擎进行模块仿真。

对于代码生成，模型使用代码生成进行模块仿真（使用代码生成支持的 MATLAB 代码子集）。MATLAB System 模块仅支持 MATLAB 中的部分可用函数。有关完整的函数列表，请参阅 C/C++ 代码生成支持的函数和对象。这些函数包括那些常见类别的函数，例如：

- 数组与矩阵运算，例如 `plus`、`minus` 和 `power`
- `size` 和 `length` 等矩阵运算
- `lu`、`inv`、`svd` 和 `chol` 等高级矩阵运算
- `sin`、`cos`、`sinh` 和 `cosh` 等三角函数

默认情况下，模块识别一维输入信号，并将一维输出信号作为二维信号进行传播。使用 `supports1DVectorsImpl` 方法使模块能够将一维输入和输出作为一维信号进行识别和传播。

从 R2025a 开始，该模块在其输入端口和输出端口支持无界可变大小信号。有关无界可变大小信号的详细信息，请参阅Unbounded Variable-Size Signals。

#### System object

要使用 MATLAB System 模块，您必须先创建新的 System object™，或者使用现有的 System object。有关详细信息，请参阅使用 MATLAB System object 创建模块。

### 端口

#### 输入

#### **In** — MATLAB System 模块的信号输入 标量 | 向量 | 矩阵

MATLAB System 模块接受模块特性表中所列类型的输入。有关详细信息，请参阅 Simulink 支持的数据类型。

有关此模块是否支持定点类型的详细信息，请参阅来自 MATLAB 的代码加速和代码生成 (Fixed-Point Designer)。

MATLAB System 模块支持 Simulink 帧。有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Out** — MATLAB System 模块的信号输出 标量 | 向量 | 矩阵

System object 返回的 MATLAB System  模块的信号输出。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **System object 名称** — System object 的名称 元胞数组 (默认)

指定用户定义的 System object 类的完整名称，不包含文件扩展名。此输入区分大小写。类名称必须存在于 MATLAB 路径中。

可以通过以下方式之一来指定 System object：

- 在文本框中输入名称。
- 点击文本框中的列表箭头。如果当前文件夹中存在有效的 System object，其名称将出现在列表中。从此列表中选择一个 System object。
- 浏览到包含有效 System object 的文件夹。如果该文件夹不在您的 MATLAB 路径中，本软件将提示您添加它。

如果您需要创建 System object，可以通过点击**新建**，使用模板进行创建。

当您保存 System object 之后，名称显示在 **System object 名称**文本框中。

使用用户定义的 System object 类名的完整名称。此模块不接受您已分配给 System object 类名的 MATLAB 变量。

##### 编程用法

|  |
| --- |
| **模块参数**：`System` |
| **类型：**字符向量 |
| **值:**System object 的名称 |
| **默认值：**`' '` |

#### **新建** — 从模板创建 System object **基本** (默认) | **高级** | **Simulink 扩展**

对 System object 模板选择下列选项之一。

**基本**
:   启动 MATLAB 编辑器并显示一个模板，用最少的 System object 方法创建一个简单的 System object。

**高级**
:   启动 MATLAB 编辑器并显示一个模板，用最多的 System object 方法创建一个更高级的 System object。

**Simulink 扩展**
:   启动 MATLAB 编辑器并显示一个文件，其中包含为 Simulink 自定义模块的实用工具。此文件与您在 MATLAB 中选择**新建** > **System object** > **Simulink 扩展**扩展时所看到的文件相同。

当您保存 System object 之后，可在 **System object 名称**文本框中输入其名称。

#### **仿真方式** — 选择仿真模式。 **代码生成** (默认) | **解释执行**

选择仿真模式。

**代码生成**
:   在第一次运行模型时，仅使用代码生成支持的 MATLAB 函数对 MATLAB System 模块进行仿真和生成代码。如果模块的结构未改变，后续模型运行将不会重新生成代码。

    如果仿真模式是**代码生成**，System object 最多接受 32 个输入。

**解释执行**
:   使用支持的所有 MATLAB 函数进行模型仿真。选择此选项可能会降低仿真性能。

#### **依赖关系** — MATLAB System 模块的依赖关系参数 auto (默认)

当您为模块分配有效的 System object 类名后，下次打开模块对话框时，即可看到此参数。每个 MATLAB System 模块都会出现此参数。您无法将其删除。

- 如果模块没有选项卡，此参数将出现在对话框的底部。
- 如果模块有多个选项卡，此参数将出现在对话框中第一个选项卡的底部。

#### **对整数溢出进行饱和处理** — 指定是否做溢出饱和处理。 `Off` (默认) | `On`

On
:   将溢出饱和处理为数据类型能够表示的最小值或最大值。例如，一个有符号的 8 位整数的溢出可以饱和处理为 -128 或 127。

Off
:   溢出将绕回到数据类型可以表示的合适值。例如，数字 130 不适合一个有符号的 8 位整数，因此绕回 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此复选框。
- 如果您希望优化生成的代码的效率，请考虑清除此复选框。清除此复选框还可以帮助您避免过度地指定信号超出范围时的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 依赖关系

当您在 System object 中使用 `showFiSettingsImpl` 方法时，将出现此复选框。

##### 编程用法

|  |
| --- |
| **模块参数：**`SaturateOnIntegerOverflow` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **将这些继承的 Simulink 信号类型视为 fi 对象** — 指定 `fi` 数据类型 **定点** (默认) | **定点和整数**

选择将哪些继承的数据类型视为 `fi` 数据类型，

**定点**
:   将定点数据类型视为 `fi` 数据类型。

**定点和整数**
:   将定点和整数数据类型视为 `fi` 数据类型。

##### 依赖关系

当您在 System object 中使用 `showFiSettingsImpl` 方法时，将出现此复选框。

#### **MATLAB System fimath** — 指定要使用的定点设置 `Same as MATLAB` (默认) | `Specify Other`

选择要使用哪些定点数学运算设置。

**与 MATLAB 相同**
:   使用当前 MATLAB 定点数学运算设置。

**指定其他**
:   启用编辑框，用于指定所需的定点数学运算设置。有关设置定点数学运算的信息，请参阅 `fimath` (Fixed-Point Designer)。

##### 依赖关系

当您在 System object 中使用 `showFiSettingsImpl` 方法时，将出现此复选框。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busba` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `否` |
| **多维信号** | `是a` |
| **可变大小信号** | `是ca` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。  b 有关详细信息，请参阅非虚拟总线和 MATLAB System 模块。  c 有关详细信息，请参阅 "可变大小信号"。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

您可以定义一个 System object 并在 MATLAB System 模块中使用它来进行 HDL 代码生成。

**可调参数支持**

HDL Coder 支持以下数据类型的可调参数：

- 数值
- 定点
- 字符
- 逻辑值

将可调参数用于 MATLAB System 模块时，可调参数应为 `StorageClass` 设置为 `ExportedGlobal` 的 `Simulink.Parameter` 对象。

```
x = Simulink.Parameter
x.Value = 1
x.CoderInfo.StorageClass = 'ExportedGlobal'
```

有关详细信息，请参阅Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

如果使用预定义的 System object，则可用的 HDL 模块属性与对应模块的可用属性相同。

默认情况下，以下 HDL 模块属性可用。

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 正则有符号数 (CSD) 或因子化 CSD 优化。默认值为**无**。另请参阅ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **LoopOptimization** | 展开、流化或不优化循环。默认值为 **none**。另请参阅LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 **off**。另请参阅MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ResetType** | 隐藏重置逻辑生成。默认值为**默认**，它生成重置逻辑。另请参阅ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |
| **VariablesToPipeline** | **警告**  不推荐使用 `VariablesToPipeline`。请改用 `coder.hdl.pipeline` (HDL Coder)。  在一个或多个指定的 MATLAB 变量的输出端插入流水线寄存器。将变量列表指定为字符向量，变量之间用空格分隔。 |

**限制**

- DUT 子系统必须为单速率。
- 输入不能包含非离散（常量或 `Inf`）采样时间。
- 要查找在 MATLAB System 模块中使用时支持 HDL 代码生成的预定义 System objects，请参阅Predefined System Objects Supported for HDL Code Generation (HDL Coder)。
- 如果您使用用户定义的 System object，则该 System object 必须支持 HDL 代码生成。有关用户定义的 System objects 和 HDL 代码生成要求的信息，请参阅 HDL Code Generation for System Objects (HDL Coder)。

另请参阅Generate Code for User-Defined System Objects (HDL Coder)和HDL Code Generation for System Objects (HDL Coder)。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

### 版本历史记录

**在 R2013b 中推出**

#### R2025a: MATLAB System 模块支持无界可变大小信号

现在，MATLAB System 模块在模块输入端口和输出端口支持无界可变大小信号。这使您能够使用在模型编译期间其维度未知的可变大小信号。有关无界可变大小信号的详细信息，请参阅Unbounded Variable-Size Signals。

#### R2024a: 报告 MATLAB System 模块在快速加速模式下的运行时错误

通过将**启用内存完整性检查**配置参数设置为**始终打开**，报告在快速加速模式下进行仿真时 MATLAB System 模块的运行时错误。

## Libraries

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

## Description

The MATLAB System block brings existing System objects (based on `matlab.System`) into Simulink®. It also enables you to use System object APIs to develop new blocks for
Simulink. For more information on this block, see Create Custom Blocks Using MATLAB System Block and System objects.

For interpreted execution, the model simulates the block using the MATLAB® execution engine.

For code generation, the model simulates the block using code generation (using the
subset of MATLAB code supported for code generation). The MATLAB System
block supports only a subset of the functions available in MATLAB. See Functions and Objects Supported for C/C++ Code Generation for a complete
list of functions. These functions include those in common categories, such as:

- Array vs. Matrix Operations,
  like `plus`, `minus`, and
  `power`
- Matrix operations, like `size` and `length`
- Advanced matrix operations, like `lu`, `inv`, `svd`, and `chol`
- Trigonometric functions, like `sin`, `cos`, `sinh`, and `cosh`

By default, the block recognizes 1-D input signals and propagates 1-D output signals
as 2-D. Use the `supports1DVectorsImpl` method to enable the block to recognize and
propagate 1-D inputs and outputs as 1-D signals.

Starting in R2025a, the block supports unbounded variable-size signals at its input
and output ports. For more information about unbounded variable-size signals, see Unbounded Variable-Size Signals.

### System Objects

To use the MATLAB System block, you must first have a new
System object™ or use an existing one. For more information, see Author Blocks Using MATLAB System Objects.

## Ports

### Input

### **In** — Signal input to a MATLAB System block scalar | vector | matrix

The MATLAB System block accepts inputs of the types
listed in the Block Characteristics table. For more information, see
Data Types Supported by Simulink.

For information on fixed-point support for this block, see Code Acceleration and Code Generation from MATLAB (Fixed-Point Designer).

The MATLAB System block supports Simulink frames. For more information, see Sample- and Frame-Based Concepts (DSP System Toolbox).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Out** — Signal output of a MATLAB System block scalar | vector | matrix

Signal output of a MATLAB System
block that the System object returns.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **System Object Name** — Name of the System object cell array (default)

Specify the full name of the user-defined System object class without the file extension. This entry is case
sensitive. The class name must exist on the MATLAB path.

You can specify a System object name in one of these ways:

- Enter the name in the text box.
- Click the list arrow attached to the text box. If valid System
  objects exist in the current folder, the names appear in the list.
  Select a System object from this list.
- Browse to a folder that contains a valid System object. If the folder is not on your MATLAB path, the software prompts you to add it.

If you need to create a System object, you can create one from a template by clicking
**New**.

After you save the System object, the name appears in the **System object
name** text box.

Use the full name of the user-defined System object class name. The block does not accept a MATLAB variable that you have assigned to a System object class name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `System` |
| **Type:** character vector |
| **Value:** name of the System object |
| **Default:** `' '` |

### **New** — Create a System object from a template `Basic` (default) | `Advanced` | `Simulink Extension`

Select one of the options for a System object template.

`Basic`
:   Starts MATLAB Editor and displays a template for a simple
    System object using the fewest System object methods.

`Advanced`
:   Starts MATLAB Editor and displays a template for a more
    advanced System object using most of the System object methods.

`Simulink Extension`
:   Starts MATLAB Editor and displays a file that contains
    utilities for customizing the block for Simulink. This is the same file available in MATLAB when you select **New** > **System Object** > **Simulink Extension**.

After you save the System object, you can enter the name in the **System object
name** text box.

### **Simulate using** — Select the simulation mode `Code generation` (default) | `Interpreted Execution`

Select the simulation mode.

`Code generation`
:   On the first model run, simulate and generate code for
    MATLAB System block using only MATLAB functions supported for code generation. If the
    structure of the block does not change, subsequent model runs do
    not regenerate the code.

    If the simulation mode is `Code
    generation`, System Objects accept a maximum of
    32 inputs.

`Interpreted execution`
:   Simulate model using all supported MATLAB functions. Choosing this option can slow
    simulation performance.

### **Dependency** — Dependency parameter for MATLAB System block auto (default)

After you assign a valid System object class name to the block, the next time you open the block
dialog box, the parameter is visible. This parameter appears for every
MATLAB System block. You cannot remove it.

- If the block has no tabs, this parameter appears at the bottom of
  the dialog box.
- If the block has multiple tabs, this parameter appears at the
  bottom of the first tab of the dialog box.

### **Saturate on integer overflow** — Specify whether overflows saturate `Off` (default) | `On`

On
:   Overflows saturate to either the minimum or maximum value
    that the data type can represent. For example, an overflow
    associated with a signed 8-bit integer can saturate to -128
    or 127.

Off
:   Overflows wrap to the appropriate value that the data type
    can represent. For example, the number 130 does not fit in a
    signed 8-bit integer and wraps to -126.

#### Tips

- Consider selecting this check box when your model has a
  possible overflow and you want explicit saturation protection in
  the generated code.
- Consider clearing this check box when you want to optimize
  efficiency of your generated code. Clearing this check box also
  helps you to avoid overspecifying how a block handles
  out-of-range signals. For more information, see Troubleshoot Signal Range Errors.
- When you select this check box, saturation applies to every
  internal operation on the block, not just the output or
  result.
- In general, the code generation process can detect when
  overflow is not possible. In this case, the code generator does
  not produce saturation code.

#### Dependency

This check box appears when you use the `showFiSettingsImpl`
method in the System object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Treat these inherited Simulink signal types as fi objects** — Specify `fi` data types `Fixed-point` (default) | `Fixed-point & Integer`

Select which inherited data types to treat `fi` data
types,

`Fixed-point`
:   Treat fixed-point data types as `fi` data
    types.

`Fixed-point & Integer`
:   Treat fixed-point and integer data types as
    `fi` data types.

#### Dependency

This check box appears when you use the `showFiSettingsImpl`
method in the System object.

### **MATLAB System fimath** — Specify fixed-point settings to use `Same as MATLAB` (default) | `Specify Other`

Select which fixed-point math settings to use.

**Same as MATLAB**
:   Use the current MATLAB fixed-point math settings.

**Specify Other**
:   Enable the edit box for specifying the desired fixed-point
    math settings. For information on setting fixed-point math, see
    `fimath` (Fixed-Point Designer).

#### Dependency

This check box appears when you use the `showFiSettingsImpl`
method in the System object.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busba` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesca` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation.  b See Nonvirtual Buses and MATLAB System Block for more information.  c See Variable-Size Signals for more information. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

You can define a System object and use it in a MATLAB System block for HDL code
generation.

**Tunable Parameter Support**

HDL Coder supports tunable parameters with the following data types:

- Numeric
- Fixed point
- Character
- Logical

When using tunable parameters with the MATLAB System block, the
tunable parameter should be a `Simulink.Parameter` object with
the `StorageClass` set to
`ExportedGlobal`.

```
x = Simulink.Parameter
x.Value = 1
x.CoderInfo.StorageClass = 'ExportedGlobal'
```

For details, see
Generate DUT Ports for Tunable Parameters (HDL Coder).

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

If you use a predefined System object, the HDL block properties available are the same as the properties
available for the corresponding block.

By default, the following HDL block properties are available.

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | Canonical signed digit (CSD) or factored CSD optimization. The default is `none`. See also ConstMultiplierOptimization (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **LoopOptimization** | Unroll, stream, or do not optimize loops. The default is `none`. See also LoopOptimization (HDL Coder). |
| **MapPersistentVarsToRAM** | Map persistent arrays to RAM. The default is `off`. See also MapPersistentVarsToRAM (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ResetType** | Suppress reset logic generation. The default is `default`, which generates reset logic. See also ResetType (HDL Coder). |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **VariablesToPipeline** | **Warning**  `VariablesToPipeline` is not recommended. Use `coder.hdl.pipeline` (HDL Coder) instead.  Insert a pipeline register at the output of the specified MATLAB variable or variables. Specify the list of variables as a character vector, with spaces separating the variables. |

**Restrictions**

- The DUT subsystem must be single-rate.
- Inputs cannot have non-discrete (constant or
  `Inf`) sample time.
- To find predefined System objects that are
  supported for HDL code generation when you use them in the
  MATLAB System block, see Predefined System Objects Supported for HDL Code Generation (HDL Coder).
- If you use a user-defined System object, it must support HDL code generation. For information
  about user-defined System objects and requirements
  for HDL code generation, see HDL Code Generation for System Objects (HDL Coder).

See also Generate Code for User-Defined System Objects (HDL Coder) and HDL Code Generation for System Objects (HDL Coder).

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2013b**

### R2025a: MATLAB System block supports unbounded variable-size signals

MATLAB System block now supports unbounded variable-size signals at
the block input and output ports. This enables you to use variable-size signals
whose dimensions are unknown during model compilation. For more information about
unbounded variable-size signals, see Unbounded Variable-Size Signals.

### R2024a: Report runtime errors for MATLAB System blocks in rapid accelerator mode

Report runtime errors for MATLAB System blocks when simulating in
rapid accelerator mode by setting the **Enable memory integrity checks**
configuration parameter to `Always on`.
