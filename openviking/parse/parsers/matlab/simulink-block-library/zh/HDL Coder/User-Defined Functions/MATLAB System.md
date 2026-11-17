---
type: simulink-block
title: 'MATLAB System'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'matlabsystem'
documentation_source_path: '../simulink/slref/matlabsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# MATLAB System

## 端口
```yaml
ports:
- name: In
  summary: MATLAB System 模块的信号输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Out
  summary: MATLAB System 模块的信号输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **In** — MATLAB System 模块的信号输入 标量 | 向量 | 矩阵

MATLAB System 模块接受模块特性表中列出的类型的输入。有关详细信息，请参阅 Data Types Supported by Simulink。

有关此模块的定点支持信息，请参阅 Code Acceleration and Code Generation from MATLAB (Fixed-Point Designer)。

MATLAB System 模块支持 Simulink 帧。有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — MATLAB System 模块的信号输出 标量 | 向量 | 矩阵

System object 返回的 MATLAB System 模块的信号输出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: System Object Name
  summary: System object 的名称 字符向量 (默认)
  group: ''
  block_parameter: System
  type: character vector
  values: System object 的名称
  default: ''' '''
- name: New
  summary: 从模板创建 System object Basic (默认) | Advanced | Simulink Extension
  group: ''
- name: Simulate using
  summary: 选择仿真模式 Code generation (默认) | Interpreted Execution
  group: ''
- name: Dependency
  summary: MATLAB System 模块的依赖参数 auto (默认)
  group: ''
- name: Saturate on integer overflow
  summary: 指定溢出是否饱和 Off (默认) | On
  group: ''
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Treat these inherited Simulink signal types as fi objects
  summary: 指定 fi 数据类型 Fixed-point (默认) | Fixed-point & Integer
  group: ''
- name: MATLAB System fimath
  summary: 指定要使用的定点设置 Same as MATLAB (默认) | Specify Other
  group: ''
```

### **System Object Name** — System object 的名称 字符向量 (默认)

指定用户定义 System object 类的完整名称，不带文件扩展名。此条目区分大小写。类名必须存在于 MATLAB 路径上。

您可以通过以下方式之一指定 System object 名称：

- 在文本框中输入名称。
- 单击文本框附带的列表箭头。如果当前文件夹中存在有效的 System object，其名称将出现在列表中。从此列表中选择一个 System object。
- 浏览到包含有效 System object 的文件夹。如果该文件夹不在您的 MATLAB 路径上，软件会提示您添加它。

如果您需要创建 System object，可以通过单击 **New** 从模板创建一个。

保存 System object 后，名称将出现在 **System object name** 文本框中。

使用用户定义 System object 类名的完整名称。该模块不接受您已分配给 System object 类名的 MATLAB 变量。

#### 编程使用

|  |
| --- |
| **模块参数**：`System` |
| **类型**：character vector |
| **值：** System object 的名称 |
| **默认值**：`' '` |

### **New** — 从模板创建 System object `Basic` (默认) | `Advanced` | `Simulink Extension`

选择 System object 模板的选项之一。

`Basic`
:   启动 MATLAB 编辑器并显示一个简单 System object 的模板，使用最少的 System object 方法。

`Advanced`
:   启动 MATLAB 编辑器并显示一个更高级的 System object 的模板，使用大多数 System object 方法。

`Simulink Extension`
:   启动 MATLAB 编辑器并显示一个包含用于为 Simulink 自定义模块的实用工具的文件。这与在 MATLAB 中选择 **New** > **System Object** > **Simulink Extension** 时可用的文件相同。

保存 System object 后，您可以在 **System object name** 文本框中输入名称。

### **Simulate using** — 选择仿真模式 `Code generation` (默认) | `Interpreted Execution`

选择仿真模式。

`Code generation`
:   在首次模型运行时，仅使用支持代码生成的 MATLAB 函数对 MATLAB System 模块进行仿真并生成代码。如果模块的结构不变，后续模型运行不会重新生成代码。

    如果仿真模式为 `Code generation`，System Object 最多接受 32 个输入。

`Interpreted execution`
:   使用所有支持的 MATLAB 函数对模型进行仿真。选择此选项可能会降低仿真性能。

### **Dependency** — MATLAB System 模块的依赖参数 auto (默认)

在为模块分配有效的 System object 类名后，下次打开模块对话框时，该参数将可见。此参数出现在每个 MATLAB System 模块中。您无法移除它。

- 如果模块没有选项卡，此参数出现在对话框底部。
- 如果模块有多个选项卡，此参数出现在对话框第一个选项卡的底部。

### **Saturate on integer overflow** — 指定溢出是否饱和 `Off` (默认) | `On`

On
:   溢出饱和到数据类型可以表示的最小值或最大值。例如，与有符号 8 位整数相关的溢出可以饱和到 -128 或 127。

Off
:   溢出回绕到数据类型可以表示的适当值。例如，数字 130 不适合有符号 8 位整数，会回绕到 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选中此复选框。
- 当您希望优化生成代码的效率时，请考虑清除此复选框。清除此复选框还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 当您选中此复选框时，饱和应用于模块上的每个内部操作，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 依赖关系

当您在 System object 中使用 `showFiSettingsImpl` 方法时，此复选框会出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Treat these inherited Simulink signal types as fi objects** — 指定 `fi` 数据类型 `Fixed-point` (默认) | `Fixed-point & Integer`

选择将哪些继承的数据类型视为 `fi` 数据类型，

`Fixed-point`
:   将定点数据类型视为 `fi` 数据类型。

`Fixed-point & Integer`
:   将定点和整数数据类型视为 `fi` 数据类型。

#### 依赖关系

当您在 System object 中使用 `showFiSettingsImpl` 方法时，此复选框会出现。

### **MATLAB System fimath** — 指定要使用的定点设置 `Same as MATLAB` (默认) | `Specify Other`

选择要使用的定点数学设置。

**Same as MATLAB**
:   使用当前的 MATLAB 定点数学设置。

**Specify Other**
:   启用编辑框以指定所需的定点数学设置。有关设置定点数学的信息，请参阅 `fimath` (Fixed-Point Designer)。

#### 依赖关系

当您在 System object 中使用 `showFiSettingsImpl` 方法时，此复选框会出现。
## 所属库

Simulink / User-Defined Functions HDL Coder / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busba` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesca` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。  b 有关详细信息，请参阅 Nonvirtual Buses and MATLAB System Block。  c 有关详细信息，请参阅 Variable-Size Signals。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

您可以定义 System object 并在 MATLAB System 模块中使用它进行 HDL 代码生成。

**可调参数支持**

HDL Coder 支持以下数据类型的可调参数：

- 数值
- 定点
- 字符
- 逻辑

在 MATLAB System 模块中使用可调参数时，可调参数应为 `Simulink.Parameter` 对象，并将 `StorageClass` 设置为 `ExportedGlobal`。

```
x = Simulink.Parameter
x.Value = 1
x.CoderInfo.StorageClass = 'ExportedGlobal'
```

有关详细信息，请参阅 Generate DUT Ports for Tunable Parameters (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

如果您使用预定义的 System object，可用的 HDL 模块属性与相应模块可用的属性相同。

默认情况下，以下 HDL 模块属性可用。

|  |  |
| --- | --- |
| **ConstMultiplierOptimization** | 规范符号数字 (CSD) 或因式分解 CSD 优化。默认值为 `none`。另请参阅 ConstMultiplierOptimization (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **LoopOptimization** | 展开、流式处理或不优化循环。默认值为 `none`。另请参阅 LoopOptimization (HDL Coder)。 |
| **MapPersistentVarsToRAM** | 将持久数组映射到 RAM。默认值为 `off`。另请参阅 MapPersistentVarsToRAM (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ResetType** | 抑制复位逻辑生成。默认值为 `default`，即生成复位逻辑。另请参阅 ResetType (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **VariablesToPipeline** | **警告** 不建议使用 `VariablesToPipeline`。请改用 `coder.hdl.pipeline` (HDL Coder)。  在指定的 MATLAB 变量的输出处插入流水线寄存器。将变量列表指定为字符向量，变量之间用空格分隔。 |

**限制**

- DUT 子系统必须是单速率。
- 输入不能具有非离散（常量或 `Inf`）采样时间。
- 要查找在 MATLAB System 模块中使用时支持 HDL 代码生成的预定义 System object，请参阅 Predefined System Objects Supported for HDL Code Generation (HDL Coder)。
- 如果您使用用户定义的 System object，它必须支持 HDL 代码生成。有关用户定义 System object 和 HDL 代码生成要求的信息，请参阅 HDL Code Generation for System Objects (HDL Coder)。

另请参阅 Generate Code for User-Defined System Objects (HDL Coder) 和 HDL Code Generation for System Objects (HDL Coder)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2013b 中引入**

### R2025a：MATLAB System 模块支持无界可变大小信号

MATLAB System 模块现在支持模块输入和输出端口处的无界可变大小信号。这使您能够使用在模型编译期间维度未知的可变大小信号。有关无界可变大小信号的更多信息，请参阅 Unbounded Variable-Size Signals。

### R2024a：在快速加速器模式下报告 MATLAB System 模块的运行时错误

通过将 **Enable memory integrity checks** 配置参数设置为 `Always on`，在快速加速器模式下仿真时报告 MATLAB System 模块的运行时错误。

## 描述

在模型中包含 System object

MATLAB System 模块将现有 System object（基于 `matlab.System`）引入 Simulink®。它还使您能够使用 System object API 为 Simulink 开发新模块。有关此模块的更多信息，请参阅 Create Custom Blocks Using MATLAB System Block and System objects。

对于解释执行，模型使用 MATLAB® 执行引擎对模块进行仿真。

对于代码生成，模型使用代码生成（使用支持代码生成的 MATLAB 代码子集）对模块进行仿真。MATLAB System 模块仅支持 MATLAB 中可用函数的一个子集。有关函数的完整列表，请参阅 Functions and Objects Supported for C/C++ Code Generation。这些函数包括常见类别中的函数，例如：

- 数组与矩阵运算，如 `plus`、`minus` 和 `power`
- 矩阵运算，如 `size` 和 `length`
- 高级矩阵运算，如 `lu`、`inv`、`svd` 和 `chol`
- 三角函数，如 `sin`、`cos`、`sinh` 和 `cosh`

默认情况下，模块将一维输入信号识别为一维，并将一维输出信号传播为二维。使用 `supports1DVectorsImpl` 方法使模块能够将一维输入和输出识别并传播为一维信号。

从 R2025a 开始，该模块在其输入和输出端口支持无界可变大小信号。有关无界可变大小信号的更多信息，请参阅 Unbounded Variable-Size Signals。

### System Object

要使用 MATLAB System 模块，您必须首先拥有一个新的 System object™ 或使用现有的 System object。有关更多信息，请参阅 Author Blocks Using MATLAB System Objects。
