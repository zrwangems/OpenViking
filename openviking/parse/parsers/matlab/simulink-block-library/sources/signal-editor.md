---
type: simulink-block
title: 'Signal Editor'
family: sources
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'signaleditorblock'
---

# Signal Editor

Display, create, edit, and switch interchangeable scenarios

## 中文

显示、创建、编辑和切换可互换场景。

### 所属库

Simulink / Sources

### 描述

可以使用 Signal Editor 模块显示、创建和编辑包含信号的可互换场景。信号可以是：

- MATLAB® `timeseries` 对象。`timeseries` 对象不能有空的 `Data` 属性。
- `timetable` 对象。`timetable` 对象不能表示多个变量。
- MATLAB `timeseries` 或 `timetable` 对象的结构体。
- 二维矩阵。

该模块为每个信号创建一个端口。

要创建和编辑场景以及场景中包含的信号，请点击**打开信号编辑器** ()。您也可以使用 Signal Editor 模块切换模型的场景。

Signal Editor 模块支持包含作为一个或多个标量 `Simulink.SimulationData.Dataset` 对象的信号的 MAT 文件。

#### 创建和编辑场景和信号

要创建和编辑场景及其中包含的信号，请点击  打开信号编辑器工具。信号编辑器工具使您能够以下列方式轻松操作信号：

- 创建和编辑多个数据集的多个信号。默认情况下，信号编辑器会创建时间序列格式数据。
- 使用信号符号通过 MATLAB 表达式创建更复杂的信号。您可以使用创建和插入对话框，或在表格区域中手动输入简单的 MATLAB 表达式。
- 使用现有场景获取现有数据集以便对其编辑和创建信号。
- 创建和编辑多维信号。

有关信号编辑器工具的详细信息，请参阅创建和编辑信号数据。

#### 编程交互

要以编程方式获取 Signal Editor 模块中的场景和信号的总数，请将 `get_param` 函数分别与 `NumberOfScenarios` 和 `NumberOfSignals` 参数结合使用。这些只读参数包含字符向量形式的值。要将这些值转换为双精度值，请使用 `str2double` 函数。

要以编程方式启用 Signal Editor 模块来标记输出信号线，请使用 `set_param` 函数将 `PreserveSignalName` 设置为 `'on'`（默认值）。

```
set_param(gcb,'PreserveSignalName','on')
```

有关编程交互的详细信息，请参阅参数和替换 signalbuilder 的程序化使用。

#### 导入和导出

信号编辑器通过允许您执行以下操作来支持自定义文件类型（如 Microsoft® Excel®）：

- 编辑从注册的自定义文件类型导入的信号。有关详细信息，请参阅Import Custom File Type。
- 将信号从信号编辑器导出为您注册的自定义文件类型。有关详细信息，请参阅Export Signals to Custom Registered File Types。

#### 从 Signal Builder 模块迁移

您可以使用 `signalBuilderToSignalEditor` 函数将 Signal Builder 模块配置移到 Signal Editor 模块。有关详细信息，请参阅用 Signal Editor 模块替换信号生成器模块和从信号生成器模块迁移到 Signal Editor 模块。

#### 快速重启

Signal Editor 模块支持快速重启。启用快速重启后，您仍可以：

- 更改激活场景。
- 更改活动信号。

  虽然您可以更改活动信号，但无法编辑模块中的信号属性。
- 打开信号编辑器并编辑数据。

### 端口

#### 输出参量

#### **Signal1** — 场景中的信号 标量 | 向量 | 矩阵 | 数组

一个或多个信号，以标量、向量、矩阵、数组、总线或总线数组 *(自 R2021a 起)*形式返回。该模块为每个信号创建一个端口。

端口标签取决于数据集 MAT 文件中相关联的变量。

在快速加速模式下，当**数据插值**参数处于选中状态时，Signal Editor 模块不支持 `int64` 和 `uint64` 数据类型。有关详细信息，请参阅总线数组支持。

**数据类型:** `single` | `double` | `half` | `int` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **要创建和编辑场景，请打开信号编辑器用户界面** — 打开信号编辑器工具的选项 按钮

要打开信号编辑器，请点击**打开信号编辑器** ()。信号编辑器会打开，且绘制了所有激活场景信号。

要查看信号编辑器工具中的信号数据更改，请点击信号编辑器工具工具条中的**保存**按钮。

##### 编程用法

要打开信号编辑器，请使用 `signalEditor` 函数。有关详细信息，请参阅信号编辑器。

#### **文件名** — 数据集文件 `untitled.mat` (默认) | 字符向量

数据集文件，指定为字符向量，包含一个或多个标量 `Simulink.SimulationData.Dataset` 对象。不要将一个区域设置中的文件名用于其他区域设置。当在多个平台上使用该模块时，考虑只指定 MAT 文件名并使 MAT 文件位于 MATLAB 路径中。

要创建 MAT 文件，请点击 。此按钮打开信号编辑器，让您可以创建和编辑场景 MAT 文件。

##### 编程用法

|  |
| --- |
| **模块参数**：`Filename` |
| **类型**：字符向量 |
| **值**：字符向量 |
| **默认值**：`'untitled.mat'` |

#### **激活场景** — 激活场景 `Scenario` (默认) | 字符向量

激活场景，指定为字符向量。您可以根据需要切换激活场景。

如果使用 `signalBuilderToSignalEditor` 函数或检查 Signal Builder 模块的模型升级顾问检查项来创建此模块以将 Signal Builder 模块转换为 Signal Editor 模块，则激活场景名称是 MAT 文件中的数据集变量名称。但是，如果您将鼠标在此参数上暂停，将显示原始的 Signal Builder 组名称。

##### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

##### 编程用法

|  |
| --- |
| **模块参数**：`ActiveScenario` |
| **类型**：字符向量 | 数值 |
| **值**：字符向量 | 索引值 |
| **默认值**：`'Scenario'` |

#### **使用来自以下源的属性** — 信号属性源 **对话框参数** (默认) | **MAT 文件中的信号数据**

信号属性源，指定为：

- **对话框参数** - 使用模块对话框中的信号属性。
- **MAT 文件中的信号数据** - 使用**文件名**中指定的 MAT 文件中的信号属性。如果信号没有单位或插值属性，信号属性将默认采用 信号编辑器 模块对话框设置。这些属性包括：

  - **单位**
  - **数据插值**

##### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

##### 编程用法

|  |
| --- |
| **模块参数**：`'SignalPropertySource'` |
| **类型**：字符向量 |
| **值**：`Dialog parameters` | `Signal data in MAT file` |
| **默认值**：`'SignalPropertySource'` |

#### **活动信号** — 要配置的信号 `Signal 1` (默认) | 字符向量

要配置的信号，指定为信号名称。此信号被视为活动信号。

##### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

当**将信号属性应用于所有信号**参数处于选中状态时，此参数不起作用。

##### 编程用法

|  |
| --- |
| **模块参数**：`ActiveSignal` |
| **类型**：字符向量 | 数值 |
| **值**：字符向量 | 索引向量 |
| **默认值**：`'Signal 1'` |

不要使用 `set_param` 函数将 `ActiveSignal` 与 Signal Editor 模块的另一个名称-值参量一起设置。

#### **将信号属性应用于所有场景** — 用于将指定的信号属性应用于活动信号的选项 `on` (默认) | `off`

用于应用指定的信号属性的选项。

- `on` - 将指定的信号属性应用于所有场景中的活动信号。
- `off` - 仅在当前激活场景中应用信号属性。

##### 依赖关系

- 要启用此参数，请将**使用来自以下源的属性**参数设置为**对话框参数**。
- 如果**将信号属性应用于所有信号**参数也处于选中状态，该模块会将信号属性应用于所有场景中的所有信号。

##### 编程用法

|  |
| --- |
| **模块参数**：`ApplySigPropsToAllScenarios` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'on'` |

#### **将信号属性应用于所有信号** — 用于将信号属性应用于所有信号的选项 `off` (默认) | `on`

用于应用指定的信号属性的选项。

- `on` - 将指定的信号属性应用于激活场景中的所有信号。没有活动信号的概念。
- `off` - 不要将信号属性应用于所有信号。

##### 依赖关系

- 要启用此参数，请将**使用来自以下源的属性**参数设置为**对话框参数**。
- 如果**将信号属性应用于所有场景**参数也处于选中状态，该模块会将信号属性应用于所有场景中的所有信号。

##### 编程用法

|  |
| --- |
| **模块参数**：`ApplySigPropsToAllSignals` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

#### **输出总线信号** — 将信号配置为总线 `off` (默认) | `on`

要将信号配置为总线，请选择此参数。

仅当活动信号是字段与现有总线对象相同的 MATLAB 结构体时，或在创建新的匹配总线对象时，才选中此参数。如果对不是 MATLAB 结构体的活动信号选中此参数，仿真将返回错误。

##### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

##### 编程用法

|  |
| --- |
| **模块参数**：`IsBus` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

#### **选择总线对象** — 总线对象 `Bus: BusObject` (默认) | 总线对象名称

选择或输入总线对象名称。要使用数据类型助手编辑或创建总线对象，请点击 **>>**。活动信号必须为 MATLAB 结构体，其字段与此总线对象相同。

##### 依赖关系

要启用此参数，请选择**输出总线信号**。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputBusObjectStr` |
| **类型**：字符向量 |
| **值**：总线对象名称 |
| **默认值**：`'Bus: BusObject'` |

#### **模式** — 总线对象模式 **总线对象** (默认) | 总线对象数据类型

指定总线对象名称。如果您没有总线对象，请点击**编辑**创建一个，这将打开类型编辑器。有关详细信息，请参阅 创建 Simulink 总线对象。

#### **单位** — 物理单位 `inherit` (默认) | 支持的物理单位

信号的物理单位，指定为允许的单位。要指定单位，请在文本框中键入需要的值。随着您的键入，参数将显示可能匹配的单位。有关详细信息，请参阅 Simulink 模型中的单位指定。有关支持的单位列表，请参阅允许使用的单位制。

要约束单位制，请点击参数右侧的链接：

- 如果组件中存在 Unit System Configuration 模块，将打开其对话框。使用该对话框为组件指定允许和不允许使用的单位制。
- 如果组件中不存在 Unit System Configuration 模块，将显示模型的“配置参数”对话框。使用该对话框为模型指定允许和不允许使用的单位制。

##### 依赖关系

- 要启用此参数，请将**使用来自以下源的属性**参数设置为**对话框参数**。
- 如果**将信号属性应用于所有场景**参数也处于选中状态，该模块会将信号属性应用于所有场景中的所有信号。

##### 编程用法

|  |
| --- |
| **模块参数**：`Unit` |
| **类型**：字符向量 |
| **值**：`'inherit'` | 支持的物理单位 |
| **默认值**：`'inherit'` |

#### **采样时间** — 采样时间间隔 `0` (默认) | `-1` | 采样时间（秒）

采样之间的时间间隔，以秒为单位指定。

##### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：`-1` | 采样时间（秒） |
| **默认值**：`'0'` |

#### **数据插值** — 数据线性插值 `on` (默认) | `off`

在不存在对应工作区数据的时间点对数据进行线性插值。

- `on` - 如果在不存在对应工作区数据的时间点进行线性插值，请选择此选项。

  **注意**

  如果 Signal Editor 模块是新的 Simulink® Test™ 或 Simulink Design Verifier™ 测试框架模型的源，则**数据插值**参数默认处于关闭状态。
- `off` - 当前输出等于存在数据的最近时间的输出。

Signal Editor 模块使用两个对应的工作区样本进行插值。

- 对于 `double` 数据，Signal Editor 模块使用两个对应样本进行线性插值。
- 对于 `Boolean` 数据，Signal Editor 模块对两个时间值之间的前半部分时间使用 `false`，对后半部分时间使用 `true`。
- 对于除 `double` 或 `Boolean` 之外的内置数据类型，Signal Editor 模块：

  - 将数据向上转换为 `double`
  - 执行线性内插（如针对 `double` 数据情形所述）
  - 将插入的值向下转换为原始数据类型

加载枚举、定点、可变大小信号或字符串数据时，请清除**数据插值**参数。

该模块使用最后一个已知数据点的值作为最后一个已知数据点之后出现的时间点的值。

要确定有可用数据的最后一个时间点之后的模块输出，请结合使用以下参数设置：

- **数据插值**
- **最终数据值之后的输出**

有关详细信息，请参阅**最终数据值之后的输出**。

在快速加速模式下，当**数据插值**参数处于选中状态时，Signal Editor 模块不支持 `int64` 和 `uint64` 数据类型。

##### 依赖关系

- 要启用此参数，请将**使用来自以下源的属性**参数设置为**对话框参数**。
- 如果**将信号属性应用于所有场景**参数也处于选中状态，该模块会将信号属性应用于所有场景中的所有信号。

##### 编程用法

|  |
| --- |
| **模块参数**：`Interpolate` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'on'` |

#### **启用过零检测** — 检测过零点 `off` (默认) | `on`

如果选择**启用过零检测**，Signal Editor 模块会在输入数组包含相同时间值的多个条目时检测过零。例如，假设模块加载以下输入数据。

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

在时间 `2` 处，由于输入数据的不连续性而导致发生过零情况。有关详细信息，请参阅过零检测。

加载总线的输入数据时，Signal Editor 模块会检测所有叶总线元素的过零点。

此模块仅在使用变步长求解器的仿真中支持过零检测。当使用定步长求解器进行仿真时，软件不会检测或定位此模块的过零点。

##### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

#### **最终数据值之后的输出** — 数据可用的最后一个时间点后的模块输出 **设置为零** (默认) | **外插** | **保持最终值**

要确定有可用工作区数据的最后一个时间点之后的模块输出，请结合使用以下参数设置：

- **数据插值**
- **最终数据值之后的输出**

下表列出了基于两个选项的值的模块输出。

| 最终数据值之后的输出的设置 | 数据插值的设置 | 最终数据之后的模块输出 |
| --- | --- | --- |
| **外插** | On | 根据最终数据值外插 |
| Off | 错误 |
| **设置为零** | On | 零 |
| Off | 零 |
| **保持最终值** | On | 工作区中的最终值 |
| Off | 工作区中的最终值 |

例如，如果您执行下列操作，模块将使用最后两个已知数据点对出现在最后一个已知点后的数据点进行外插：

- 选择**数据插值**。
- 将**最终数据值之后的输出**设置为**外插**。

##### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputAfterFinalValue` |
| **类型**：字符向量 |
| **值**：`'Setting to zero' | 'Extrapolation' | 'Holding final value'` |
| **默认值**：`'Setting to zero'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 具有影响 HDL 实现和综合逻辑的额外配置选项。

您可以从子系统中生成包含多个测试平台的代码。要生成多个测试平台，请执行以下操作：

- 使用信号编辑器工具在多个数据集中创建和编辑多个信号。默认情况下，信号编辑器创建 `timeseries` 数据。有关详细信息，请参阅创建和编辑信号数据。
- 通过指定包含场景列表的 MAT 文件并从下拉列表中选择**激活场景**，在 Signal Editor 模块参数对话框中设置一个场景。
- 使用 HDL 工作流顾问生成测试平台。在 **HDL 代码生成** > **生成 RTL 代码和测试平台**任务中，选择**生成 RTL 测试平台**，然后点击**应用**。

**限制**

- 代码生成不支持使用总线的设计。
- 代码生成不支持包含多个 Signal Editor 模块的设计。
- 仅当您将所有输入信号连接到同一个 Signal Editor 模块时，多文件测试用例和仿真才支持设计。

**限制**

将 Signal Editor block 连接到 DUT 端口以在模型中用作源模块，但确保它不放置在 DUT 子系统内。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2017b 中推出**

#### R2025a: Signal Editor 模块更新

从 R2025a 开始，Signal Editor 模块有以下更新：

- **数据插值**参数现在默认启用。

  **注意**

  如果 Signal Editor 模块是新的 Simulink Test 或 Simulink Design Verifier 测试框架模型的源，则**数据插值**参数默认处于关闭状态。
- 新的**使用来自以下源的属性**允许您指定信号属性定义的源。

#### R2024b: Signal Editor 模块更新

Signal Editor 模块具有这些更新：

- 当您从 信号编辑器 模块中打开信号编辑器工具时，信号编辑器工具现在会打开，并且已绘制所有激活场景信号。
- 信号编辑器 模块支持加载数据类型为 `int64` 或 `uint64` 的输入信号数据值。当使用 信号编辑器 模块加载 `int64` 或 `uint64` 信号数据时：

  - 只有信号值可以具有 `int64` 或 `uint64` 数据类型。时间值必须具有 `double` 数据类型。
  - 使用数组以外的格式，如 `timetable`、`timeseries` 或结构体。数组格式不支持除 `double` 以外的任何数据类型。

  虽然所有仿真模式都支持加载 `int64` 和 `uint64` 信号数据，但在快速加速仿真中不支持 `int64` 和 `uint64` 数据的插值。要将 `int64` 或 `uint64` 数据加载到快速加速仿真中，请执行以下操作：

  1. 清除**数据插值**参数。
  2. 将**最终数据值之后的输出**参数设置为除**外插**之外的任何值。

#### R2023b: Signal Editor 模块更新

Signal Editor 模块对话框有以下更新：

- 在**信号属性**部分，新的**将信号属性应用于所有信号**复选框可用于将指定的信号属性应用于所有信号。
- 当您将鼠标在**激活场景**参数上暂停时，工具提示会显示数据集对象的 `Name` 属性。如果模块是使用 `signalBuilderToSignalEditor` 函数从 Signal Builder 模块转换而来，则 `Name` 属性与 Signal Builder 模块**组**名称相同。

#### R2023a: Signal Editor 模块更新

Signal Editor 模块对话框有以下更新：

- **启动信号编辑器**按钮已移至模块参数对话框的顶部。
- **信号属性**部分经过重新组织。
- 在**信号属性**部分，新的**将属性应用于所有场景中的活动信号**复选框允许您将指定的信号属性应用于所有场景中具有相同名称的活动信号。

#### R2021a: 总线数组支持

信号编辑器 模块支持加载总线数组的数据。顶层模型中的 信号编辑器 模块可以在普通或加速模式仿真中加载总线数组的数据。仅当引用模型在普通模式下执行时，才支持使用引用模型中的 信号编辑器 模块加载总线数组的数据。

## Libraries

Simulink / Sources

## Description

The Signal Editor block displays, creates, and edits interchangeable
scenarios, which contain signals. Signals can be:

- MATLAB®
  `timeseries` objects.
  `timeseries` objects cannot have empty
  `Data` properties.
- `timetable` objects.
  `timetable` objects cannot represent multiple
  variables.
- Structure of MATLAB
  `timeseries` or `timetable` objects.
- Two-dimensional matrices.

The block creates one port for each signal.

To create and edit scenarios and the signals contained in the scenarios, click
**Open Signal Editor** (). You can also use the Signal Editor
block to switch scenarios in and out of models.

The Signal Editor block supports MAT files that contain signals as one
or more scalar `Simulink.SimulationData.Dataset` objects.

### Create and Edit Scenarios and Signals

To create and edit scenarios and the signals contained in them, open the Signal
Editor tool by clicking . The Signal Editor tool enables you to easily
manipulate signals in these ways:

- Create and edit multiple signals in multiple data sets. By default, the
  Signal Editor creates timeseries format data.
- Use signal notations to create more complicated signals using MATLAB expressions. You can use the Author and Insert dialog box or
  manually enter simple MATLAB expressions in the tabular area.
- Use existing scenarios to get existing data sets for which you can edit
  and create signals.
- Create and edit multidimensional signals.

For more information on the Signal Editor tool, see Create and Edit Signal Data.

### Programmatic Interactions

To programmatically get the total number of scenarios and signals in the
Signal Editor block, use the `get_param`
function with the `NumberOfScenarios` and
`NumberOfSignals` parameters, respectively. These read-only
parameters contain the values as character vectors. To convert these values to
doubles, use the `str2double` function.

To programmatically enable the Signal Editor block to label output
signal lines, set `PreserveSignalName` to `'on'`
(default) with the `set_param` function.

```
set_param(gcb,'PreserveSignalName','on')
```

For more information on programmatic interactions, see Parameters and Replace Programmatic Use of signalbuilder.

### Import and Export

The Signal Editor supports custom file types, such as Microsoft®
Excel®, by letting you:

- Edit signals imported from registered custom file types. For more
  information, see Import Custom File Type.
- Export signals from Signal Editor to your registered custom file types.
  For more information, see Export Signals to Custom Registered File Types.

### Migrating from Signal Builder Blocks

You can port Signal Builder block configurations to the
Signal Editor block using the
`signalBuilderToSignalEditor` function. For more information,
see Replace Signal Builder Block with Signal Editor Block and Migrate from Signal Builder Block to Signal Editor Block.

### Fast Restart

The Signal Editor block supports fast restart. With fast restart
enabled, you can still:

- Change the active scenario.
- Change the active signal.

  While you can change the active signal, you cannot edit the signal
  properties in the block.
- Open the Signal Editor and edit data.

## Ports

### Output Arguments

### **Signal1** — Signals in scenario scalar | vector | matrix | array

One or more signals, returned as a scalar, vector, matrix, array, a
bus, or an array of buses *(since R2021a)*. The
block creates one port per signal.

The port label depends on the associated variable in the data set MAT
file.

In rapid accelerator mode, the Signal Editor block does
not support `int64` and `uint64` data
types when the **Interpolate data** parameter is
selected. For more information, see Array of buses support.

**Data Types:** `single` | `double` | `half` | `int` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **To create and edit scenarios, open Signal Editor user interface** — Option to open Signal Editor tool button

To open the Signal Editor, click **Open Signal
Editor** (). The Signal Editor opens
with all the active scenario signals plotted.

To see the signal data changes from the Signal Editor tool,
click the **Save** button in the Signal Editor
tool toolstrip.

#### Programmatic Use

To open the Signal Editor, use the `signalEditor`
function. For more information. see Signal Editor.

### **File name** — Data set file `untitled.mat` (default) | character vector

Data set file, specified as character vector, containing one or more
scalar `Simulink.SimulationData.Dataset` objects. Do not use
a filename from one locale in a different locale. When using the block on
multiple platforms, consider specifying just the MAT filename and having the
MAT file be on the MATLAB path.

To create a MAT file, click . This button opens the Signal
Editor, which lets you create and edit scenario MAT files.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Filename` |
| **Type**: character vector |
| **Values**: character vector |
| **Default**: `'untitled.mat'` |

### **Active scenario** — Active scenario `Scenario` (default) | character vector

Active scenario, specified as a character vector. You can switch the
active scenario as necessary.

If you create this block by using the
`signalBuilderToSignalEditor` function or the
Check model for Signal Builder blocks Upgrade
Advisor check to convert a Signal Builder block to a
Signal Editor block, the active scenario name is the data
set variable name in the MAT file. However, if you pause on this parameter,
the original Signal Builder group name is displayed.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ActiveScenario` |
| **Type**: character vector | numeric |
| **Values**: character vector | index value |
| **Default**: `'Scenario'` |

### **Use properties from** — Signal property source `Dialog parameters` (default) | `Signal data in MAT file`

Signal property source, specified as:

- `Dialog parameters` — Use signal
  properties from the block dialog.
- `Signal data in MAT file` — Use signal
  properties from the MAT file specified in **File
  name**. If the signal does not have unit or
  interpolation properties, the signal property defaults to the
  Signal Editor block dialog setting. These
  properties include:

  - **Unit**
  - **Interpolate data**

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `'SignalPropertySource'` |
| **Type**: character vector |
| **Values**: `Dialog parameters` | `Signal data in MAT file` |
| **Default**: `'SignalPropertySource'` |

### **Active signal** — Signal to configure `Signal 1` (default) | character vector

Signal to configure, specified as a signal name. This signal is considered
the active signal.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

This parameter has no effect when the **Apply signal
properties to all signals** parameter is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ActiveSignal` |
| **Type**: character vector | numeric |
| **Values**: character vector | index vector |
| **Default**: `'Signal 1'` |

Do not use the `set_param` function to set
`ActiveSignal` in combination with another
name-value argument of the Signal Editor block.

### **Apply signal properties to all scenarios** — Option to apply specified signal properties to active signal `on` (default) | `off`

Option to apply the specified signal properties.

- `on` — Apply the specified signal properties to
  the active signal in all scenarios.
- `off` — Apply signal properties only in the
  current active scenario.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  signals** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ApplySigPropsToAllScenarios` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'on'` |

### **Apply signal properties to all signals** — Option to apply signal properties to all signals `off` (default) | `on`

Option to apply the specified signal properties.

- `on` — Apply the specified signal properties
  to all the signals in the active scenario. There is no concept
  of an active signal.
- `off` — Do not apply signal property to all
  signals.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  scenarios** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ApplySigPropsToAllSignals` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'off'` |

### **Output a bus signal** — Configure signal as bus `off` (default) | `on`

To configure a signal as a bus, select this parameter.

Select this parameter only if the active signal is a MATLAB structure whose fields are the same as an existing bus object,
or create a new matching bus object. If you select this parameter for an
active signal that is not a MATLAB structure, simulation returns an error.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IsBus` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'off'` |

### **Select bus object** — Bus object `Bus: BusObject` (default) | bus object name

Select or enter the bus object name. To edit the bus object or create a
bus object using the Data Type Assistant, click **>>**. The
active signal must be a MATLAB structure whose fields are the same as this bus object.

#### Dependencies

To enable this parameter, select **Output a bus
signal**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputBusObjectStr` |
| **Type**: character vector |
| **Values**: bus object name |
| **Default**: `'Bus: BusObject'` |

### **Mode** — Bus object mode `Bus object` (default) | bus object data type

Specify the bus object name. If you do not have a bus object, create one
by clicking **Edit**, which opens the Type Editor. For more
information, see Create Simulink Bus Objects.

### **Unit** — Physical unit `inherit` (default) | supported physical unit

Physical unit of the signal, specified as an allowed unit. To specify a
unit, begin typing in the text box. As you type, the parameter displays
potential matching units. For more information, see Unit Specification in Simulink Models. For a list of supported units, see
Allowed Unit
Systems.

To constrain the unit system, click the link to the right of the
parameter:

- If a Unit System
  Configuration block exists in the component, its dialog
  box opens. Use that dialog box to specify allowed and disallowed
  unit systems for the component.
- If a Unit System Configuration block does not exist
  in the component, the model Configuration Parameters dialog box
  displays. Use that dialog box to specify allowed and disallowed unit
  systems for the model.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  scenarios** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Unit` |
| **Type**: character vector |
| **Values**: `'inherit'` | supported physical unit |
| **Default**: `'inherit'` |

### **Sample time** — Time interval between samples `0` (default) | `-1` | sample time in seconds

Time interval between samples, specified in seconds.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: `-1` | sample time in seconds |
| **Default**: `'0'` |

### **Interpolate data** — Linearly interpolate data `on` (default) | `off`

Linearly interpolate data at time hits for which no corresponding
workspace data exist.

- `on` — Linearly interpolate at time hits for
  which no corresponding workspace data exist.

  **Note**

  If the Signal Editor block is the source for a
  new Simulink®
  Test™ or Simulink
  Design Verifier™ test harness model, the **Interpolate
  data** parameter is off by default.
- `off` — The current output equals the output at
  the most recent time for which data exists.

The Signal Editor block interpolates by using the two
corresponding workspace samples.

- For `double` data, the Signal
  Editor block linearly interpolates the value by using
  the two corresponding samples.
- For `Boolean` data, the Signal
  Editor block uses `false` for the first
  half of the time between two time values and `true`
  for the second half.
- For a built-in data type other than `double` or
  `Boolean`, the Signal Editor
  block:

  - Upcasts the data to `double`
  - Performs linear interpolation (as described for
    `double` data)
  - Downcasts the interpolated value to the original data
    type

When you load enumerated, fixed-point, variable-size signal, or string
data, clear the **Interpolate data**
parameter.

The block uses the value of the last known data point as the value of time
hits that occur after the last known data point.

To determine the block output after the last time hit for which data is
available, combine the settings of these parameters:

- **Interpolate data**
- **Form output after final data value by**

For details, see **Form
output after final data value by**.

In rapid accelerator mode, the Signal Editor block does not
support `int64` and `uint64` data types
when the **Interpolate data** parameter is
selected.

#### Dependencies

- To enable this parameter, set the **Use properties
  from** parameter to `Dialog
  parameters`.
- If the **Apply signal properties to all
  scenarios** parameter is also selected, the block
  applies the signal properties to all signals in all
  scenarios.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Interpolate` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'on'` |

### **Enable zero-crossing detection** — Detect zero-crossings `off` (default) | `on`

If you select **Enable zero-crossing detection**, the
Signal Editor block detects a zero crossing when the
input array contains multiple entries for the same time value. For example,
suppose that the block loads this input data.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

At time `2`, a zero crossing occurs because of the
discontinuity in the input data. For more information, see Zero-Crossing Detection.

When you load input data for a bus, the Signal Editor block
detects zero crossings for all leaf bus elements.

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off' | 'on'` |
| **Default**: `'off'` |

### **Form output after final data value by** — Block output after the last time hit for which data is available `Setting to zero` (default) | `Extrapolation` | `Holding final value`

To determine the block output after the last time hit for which workspace
data is available, combine the settings of these parameters:

- **Interpolate data**
- **Form output after final data value by**

This table lists the block output, based on the values of the two
options.

| Setting for Form Output After Final Data Value By | Setting for Interpolate Data | Block Output After Final Data |
| --- | --- | --- |
| `Extrapolation` | On | Extrapolated from final data value |
| Off | Error |
| `Setting to zero` | On | Zero |
| Off | Zero |
| `Holding final value` | On | Final value from workspace |
| Off | Final value from workspace |

For example, the block uses the last two known data points to extrapolate
data points that occur after the last known point if you:

- Select **Interpolate data**.
- Set **Form output after final data value by** to
  `Extrapolation`.

#### Dependencies

To enable this parameter, ensure that the specified MAT file
exists.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputAfterFinalValue` |
| **Type**: character vector |
| **Values**: `'Setting to zero' | 'Extrapolation' | 'Holding final value'` |
| **Default**: `'Setting to zero'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ has additional configuration options that affect HDL implementation
and synthesized logic.

You can generate code that has multiple test benches from your subsystem. To
generate multiple test benches:

- Create and edit multiple signals in multiple data sets by using the
  Signal Editor tool. By default, the Signal Editor creates `timeseries` data. For
  more information, see Create and Edit Signal Data.
- Set up a scenario in the Signal Editor block parameter
  dialog box by specifying the MAT file that contains the list of
  scenarios and selecting the **Active scenario** from
  the drop-down list.
- Generate the test bench by using the HDL Workflow Advisor. In the
  **HDL Code Generation** > **Generate RTL
  Code and Testbench** task, select **Generate RTL
  testbench** and click **Apply**.

**Limitations**

- Code generation does not support designs that use buses.
- Code generation does not support designs that include multiple
  Signal Editor blocks.
- Multi-file test cases and simulations support designs only if you
  connect all the input signals to the same Signal Editor
  block.

**Restrictions**

Connect the Signal Editor block to the DUT ports to use it as a
source block in your model, but ensure it is not placed inside the DUT
subsystem.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2017b**

### R2025a: Signal Editor block updates

Starting in R2025a, the Signal Editor block has these
updates:

- The **Interpolate data** parameter is now enabled by
  default.

  **Note**

  If the Signal Editor block is the source for a new
  Simulink
  Test or Simulink
  Design Verifier test harness model, the **Interpolate
  data** parameter is off by default.
- The new **Use properties from** lets you specify the
  source of signal property definitions.

### R2024b: Signal Editor block updates

The Signal
Editor block has these updates:

- When you open the Signal Editor tool from the Signal Editor
  block, the Signal Editor tool now opens with all the active
  scenario signals already plotted.
- The Signal Editor block supports loading input signal data values that have
  an `int64` or `uint64` data type. When you
  use the Signal Editor block to load `int64` or
  `uint64` signal data:

  - Only the signal values can have the `int64` or
    `uint64` data type. Time values must have
    `double` data type.
  - Use a format other than array, such as `timetable`,
    `timeseries`, or structure. Array format does not
    support any data type other than `double`.

  While loading `int64` and `uint64`
  signal data is supported in all simulation modes, interpolation of
  `int64` and `uint64` data is not
  supported in rapid accelerator simulations. To load `int64`
  or `uint64` data into a rapid accelerator
  simulation:

  1. Clear the **Interpolate data** parameter.
  2. Set the **Form output after final data value by**
     parameter to any value except
     `Extrapolation`.

### R2023b: Signal Editor block updates

The Signal Editor block dialog box has these updates:

- In the **Signal properties** section, the new
  **Apply signal properties to all signals** check box
  lets you apply the specified signal properties to all signals.
- When you pause on the **Active scenario** parameter, a
  tooltip displays the `Name` property of the data set
  object. If the block is converted from a Signal Builder block
  using the `signalBuilderToSignalEditor` function, the
  `Name` property is the same as the Signal
  Builder block **Group** name.

### R2023a: Signal Editor block updates

The Signal
Editor block dialog box has these updates:

- The **Launch Signal Editor** button has moved to the
  top of the block parameters dialog box.
- The **Signal properties** section is reorganized.
- In the **Signal properties** section, the new
  **Apply properties to active signal in all scenarios**
  check box lets you apply the specified signal properties to the active
  signal with the same name in all scenarios.

### R2021a: Array of buses support

The Signal Editor block supports loading data for an array of buses.
A Signal Editor block in the top model can load data for an array of
buses in normal or accelerator mode simulations. Loading data for an array of buses
using a Signal Editor block in a referenced model is supported only
when the referenced model executes in normal mode.
