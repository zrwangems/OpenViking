---
type: simulink-block
title: 'Signal Editor'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'SNG'
documentation_page: 'signaleditorblock'
documentation_source_path: '../simulink/slref/signaleditorblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Editor

## 端口
```yaml
ports:
- name: Signal1
  summary: 场景中的信号 标量 | 向量 | 矩阵 | 数组
  direction: unspecified
  data_types: single | double | half | int | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | string | Boolean
    | fixed point | enumerated | bus
```

### 输出参数

### **Signal1** — 场景中的信号 标量 | 向量 | 矩阵 | 数组

一个或多个信号，以标量、向量、矩阵、数组、总线或总线数组 *(自 R2021a 起)* 形式返回。该模块为每个信号创建一个端口。

端口标签取决于数据集 MAT 文件中关联的变量。

在快速加速模式下，当选中 **Interpolate data** 参数时，Signal Editor 模块不支持 `int64` 和 `uint64` 数据类型。有关详细信息，请参阅 Array of buses support。

**数据类型：** `single` | `double` | `half` | `int` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: To create and edit scenarios, open Signal Editor user interface
  summary: 打开 Signal Editor 工具的选项 按钮
  group: ''
- name: File name
  summary: 数据集文件 untitled.mat（默认）| 字符向量
  group: ''
  block_parameter: Filename
  type: character vector
  values: character vector
  default: '''untitled.mat'''
- name: Active scenario
  summary: 活动场景 Scenario（默认）| 字符向量
  group: ''
  block_parameter: ActiveScenario
  type: character vector | numeric
  values: character vector | index value
  default: '''Scenario'''
- name: Use properties from
  summary: 信号属性来源 Dialog parameters（默认）| Signal data in MAT file
  group: ''
  block_parameter: '''SignalPropertySource'''
  type: character vector
  values: Dialog parameters | Signal data in MAT file
  default: '''SignalPropertySource'''
- name: Active signal
  summary: 要配置的信号 Signal 1（默认）| 字符向量
  group: ''
  block_parameter: ActiveSignal
  type: character vector | numeric
  values: character vector | index vector
  default: '''Signal 1'''
- name: Apply signal properties to all scenarios
  summary: 将指定信号属性应用于活动信号的选项 on（默认）| off
  group: ''
  block_parameter: ApplySigPropsToAllScenarios
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Apply signal properties to all signals
  summary: 将信号属性应用于所有信号的选项 off（默认）| on
  group: ''
  block_parameter: ApplySigPropsToAllSignals
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output a bus signal
  summary: 将信号配置为总线 off（默认）| on
  group: ''
  block_parameter: IsBus
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Select bus object
  summary: '总线对象 Bus: BusObject（默认）| 总线对象名称'
  group: ''
  block_parameter: OutputBusObjectStr
  type: character vector
  values: bus object name
  default: '''Bus: BusObject'''
- name: Mode
  summary: 总线对象模式 Bus object（默认）| 总线对象数据类型
  group: ''
- name: Unit
  summary: 物理单位 inherit（默认）| 支持的物理单位
  group: ''
  block_parameter: Unit
  type: character vector
  values: '''inherit'' | supported physical unit'
  default: '''inherit'''
- name: Sample time
  summary: 采样之间的时间间隔 0（默认）| -1 | 以秒为单位的采样时间
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: -1 | sample time in seconds
  default: '''0'''
- name: Interpolate data
  summary: 线性插值数据 on（默认）| off
  group: ''
  block_parameter: Interpolate
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Enable zero-crossing detection
  summary: 检测过零点 off（默认）| on
  group: ''
  block_parameter: ZeroCross
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Form output after final data value by
  summary: 最后一个有数据可用的时间命中点之后的模块输出 Setting to zero（默认）| Extrapolation | Holding final value
  group: ''
  block_parameter: OutputAfterFinalValue
  type: character vector
  values: '''Setting to zero'' | ''Extrapolation'' | ''Holding final value'''
  default: '''Setting to zero'''
```

### **To create and edit scenarios, open Signal Editor user interface** — 打开 Signal Editor 工具的选项 按钮

要打开 Signal Editor，请点击 **Open Signal Editor** ()。Signal Editor 将打开并绘制所有活动场景信号。

要查看来自 Signal Editor 工具的信号数据更改，请点击 Signal Editor 工具工具条中的 **Save** 按钮。

#### 编程使用

要打开 Signal Editor，请使用 `signalEditor` 函数。有关详细信息，请参阅 Signal Editor。

### **File name** — 数据集文件 `untitled.mat`（默认）| 字符向量

数据集文件，指定为字符向量，包含一个或多个标量 `Simulink.SimulationData.Dataset` 对象。不要在不同区域设置中使用来自某一区域设置的文件名。在多个平台上使用该模块时，请考虑仅指定 MAT 文件名，并将 MAT 文件放在 MATLAB 路径上。

要创建 MAT 文件，请点击 。此按钮将打开 Signal Editor，您可以使用它创建和编辑场景 MAT 文件。

#### 编程使用

|  |
| --- |
| **模块参数**：`Filename` |
| **类型**：character vector |
| **值**：character vector |
| **默认值**：`'untitled.mat'` |

### **Active scenario** — 活动场景 `Scenario`（默认）| 字符向量

活动场景，指定为字符向量。您可以根据需要切换活动场景。

如果您使用 `signalBuilderToSignalEditor` 函数或 Check model for Signal Builder blocks Upgrade Advisor 检查将 Signal Builder 模块转换为 Signal Editor 模块来创建此模块，则活动场景名称为 MAT 文件中的数据集变量名称。但是，如果您暂停在此参数上，将显示原始 Signal Builder 组名称。

#### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

#### 编程使用

|  |
| --- |
| **模块参数**：`ActiveScenario` |
| **类型**：character vector | numeric |
| **值**：character vector | index value |
| **默认值**：`'Scenario'` |

### **Use properties from** — 信号属性来源 `Dialog parameters`（默认）| `Signal data in MAT file`

信号属性来源，指定为：

- `Dialog parameters` — 使用模块对话框中的信号属性。
- `Signal data in MAT file` — 使用 **File name** 中指定的 MAT 文件中的信号属性。如果信号没有单位或插值属性，则信号属性默认为 Signal Editor 模块对话框设置。这些属性包括：

  - **Unit**
  - **Interpolate data**

#### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

#### 编程使用

|  |
| --- |
| **模块参数**：`'SignalPropertySource'` |
| **类型**：character vector |
| **值**：`Dialog parameters` | `Signal data in MAT file` |
| **默认值**：`'SignalPropertySource'` |

### **Active signal** — 要配置的信号 `Signal 1`（默认）| 字符向量

要配置的信号，指定为信号名称。此信号被视为活动信号。

#### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

当选中 **Apply signal properties to all signals** 参数时，此参数无效。

#### 编程使用

|  |
| --- |
| **模块参数**：`ActiveSignal` |
| **类型**：character vector | numeric |
| **值**：character vector | index vector |
| **默认值**：`'Signal 1'` |

不要将 `set_param` 函数与 Signal Editor 模块的其他名称-值参数组合使用来设置 `ActiveSignal`。

### **Apply signal properties to all scenarios** — 将指定信号属性应用于活动信号的选项 `on`（默认）| `off`

应用指定信号属性的选项。

- `on` — 将指定的信号属性应用于所有场景中的活动信号。
- `off` — 仅在当前活动场景中应用信号属性。

#### 依赖关系

- 要启用此参数，请将 **Use properties from** 参数设置为 `Dialog parameters`。
- 如果还选中了 **Apply signal properties to all signals** 参数，则该模块将信号属性应用于所有场景中的所有信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`ApplySigPropsToAllScenarios` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'on'` |

### **Apply signal properties to all signals** — 将信号属性应用于所有信号的选项 `off`（默认）| `on`

应用指定信号属性的选项。

- `on` — 将指定的信号属性应用于活动场景中的所有信号。不存在活动信号的概念。
- `off` — 不将信号属性应用于所有信号。

#### 依赖关系

- 要启用此参数，请将 **Use properties from** 参数设置为 `Dialog parameters`。
- 如果还选中了 **Apply signal properties to all scenarios** 参数，则该模块将信号属性应用于所有场景中的所有信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`ApplySigPropsToAllSignals` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Output a bus signal** — 将信号配置为总线 `off`（默认）| `on`

要将信号配置为总线，请选中此参数。

仅当活动信号是 MATLAB 结构体且其字段与现有总线对象相同时，才选中此参数，或创建一个匹配的新总线对象。如果为不是 MATLAB 结构体的活动信号选中此参数，仿真将返回错误。

#### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

#### 编程使用

|  |
| --- |
| **模块参数**：`IsBus` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Select bus object** — 总线对象 `Bus: BusObject`（默认）| 总线对象名称

选择或输入总线对象名称。要使用 Data Type Assistant 编辑总线对象或创建总线对象，请点击 **>>**。活动信号必须是 MATLAB 结构体，且其字段与此总线对象相同。

#### 依赖关系

要启用此参数，请选中 **Output a bus signal**。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputBusObjectStr` |
| **类型**：character vector |
| **值**：bus object name |
| **默认值**：`'Bus: BusObject'` |

### **Mode** — 总线对象模式 `Bus object`（默认）| 总线对象数据类型

指定总线对象名称。如果您没有总线对象，请点击 **Edit** 创建一个，这将打开 Type Editor。有关详细信息，请参阅 Create Simulink Bus Objects。

### **Unit** — 物理单位 `inherit`（默认）| 支持的物理单位

信号的物理单位，指定为允许的单位。要指定单位，请在文本框中开始输入。输入时，参数将显示可能的匹配单位。有关详细信息，请参阅 Unit Specification in Simulink Models。有关支持的单位列表，请参阅 Allowed Unit Systems。

要约束单位制，请点击参数右侧的链接：

- 如果组件中存在 Unit System Configuration 模块，将打开其对话框。使用该对话框指定组件允许和不允许的单位制。
- 如果组件中不存在 Unit System Configuration 模块，将显示模型配置参数对话框。使用该对话框指定模型允许和不允许的单位制。

#### 依赖关系

- 要启用此参数，请将 **Use properties from** 参数设置为 `Dialog parameters`。
- 如果还选中了 **Apply signal properties to all scenarios** 参数，则该模块将信号属性应用于所有场景中的所有信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`Unit` |
| **类型**：character vector |
| **值**：`'inherit'` | supported physical unit |
| **默认值**：`'inherit'` |

### **Sample time** — 采样之间的时间间隔 `0`（默认）| `-1` | 以秒为单位的采样时间

采样之间的时间间隔，以秒为单位指定。

#### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：`-1` | sample time in seconds |
| **默认值**：`'0'` |

### **Interpolate data** — 线性插值数据 `on`（默认）| `off`

对没有对应工作区数据的时间命中点进行线性插值。

- `on` — 对没有对应工作区数据的时间命中点进行线性插值。

  **注意**

  如果 Signal Editor 模块是新的 Simulink® Test™ 或 Simulink Design Verifier™ 测试框架模型的源，则 **Interpolate data** 参数默认关闭。
- `off` — 当前输出等于最近存在数据的时间点的输出。

Signal Editor 模块使用两个对应的工作区采样进行插值。

- 对于 `double` 数据，Signal Editor 模块使用两个对应的采样对值进行线性插值。
- 对于 `Boolean` 数据，Signal Editor 模块在两个时间值之间的前半段使用 `false`，后半段使用 `true`。
- 对于除 `double` 或 `Boolean` 之外的内置数据类型，Signal Editor 模块：

  - 将数据向上转型为 `double`
  - 执行线性插值（如 `double` 数据所述）
  - 将插值后的值向下转型为原始数据类型

当您加载枚举、定点、可变大小信号或字符串数据时，请清除 **Interpolate data** 参数。

该模块使用最后一个已知数据点的值作为最后一个已知数据点之后发生的时间命中点的值。

要确定最后一个有数据可用的时间命中点之后的模块输出，请组合以下参数的设置：

- **Interpolate data**
- **最终数据值之后输出形式**

有关详细信息，请参阅 **Form output after final data value by**。

在快速加速模式下，当选中 **Interpolate data** 参数时，Signal Editor 模块不支持 `int64` 和 `uint64` 数据类型。

#### 依赖关系

- 要启用此参数，请将 **Use properties from** 参数设置为 `Dialog parameters`。
- 如果还选中了 **Apply signal properties to all scenarios** 参数，则该模块将信号属性应用于所有场景中的所有信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`Interpolate` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'on'` |

### **Enable zero-crossing detection** — 检测过零点 `off`（默认）| `on`

如果选中 **Enable zero-crossing detection**，当输入数组包含同一时间值的多个条目时，Signal Editor 模块将检测到过零点。例如，假设该模块加载以下输入数据。

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

在时间 `2` 处，由于输入数据的不连续性，会发生过零点。有关详细信息，请参阅 Zero-Crossing Detection。

当您为总线加载输入数据时，Signal Editor 模块会检测所有叶总线元素的过零点。

此模块仅在使用可变步长求解器的仿真中支持过零点检测。当您使用固定步长求解器进行仿真时，软件不会为此模块检测或定位过零点。

#### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Form output after final data value by** — 最后一个有数据可用的时间命中点之后的模块输出 `Setting to zero`（默认）| `Extrapolation` | `Holding final value`

要确定最后一个有工作区数据可用的时间命中点之后的模块输出，请组合以下参数的设置：

- **Interpolate data**
- **最终数据值之后输出形式**

下表列出了基于这两个选项值的模块输出。

| 最终数据值之后输出形式的设置 | 插值数据设置 | 最终数据之后的模块输出 |
| --- | --- | --- |
| `Extrapolation` | 开 | 从最终数据值外推 |
| Off | Error |
| `Setting to zero` | On | Zero |
| Off | Zero |
| `Holding final value` | 开 | 工作区中的最终值 |
| 关 | 工作区中的最终值 |

例如，如果您执行以下操作，则该模块使用最后两个已知数据点来外推最后一个已知点之后发生的数据点：

- 选中 **Interpolate data**。
- 将 **Form output after final data value by** 设置为 `Extrapolation`。

#### 依赖关系

要启用此参数，请确保指定的 MAT 文件存在。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputAfterFinalValue` |
| **类型**：character vector |
| **值**：`'Setting to zero' | 'Extrapolation' | 'Holding final value'` |
| **默认值**：`'Setting to zero'` |
## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 具有影响 HDL 实现和综合逻辑的附加配置选项。

您可以从子系统生成具有多个测试平台的代码。要生成多个测试平台：

- 使用 Signal Editor 工具在多个数据集中创建和编辑多个信号。默认情况下，Signal Editor 创建 `timeseries` 数据。有关详细信息，请参阅 Create and Edit Signal Data。
- 通过在 Signal Editor 模块参数对话框中指定包含场景列表的 MAT 文件，并从下拉列表中选择 **Active scenario**，来设置场景。
- 使用 HDL Workflow Advisor 生成测试平台。在 **HDL Code Generation** > **Generate RTL Code and Testbench** 任务中，选中 **Generate RTL testbench** 并点击 **Apply**。

**限制**

- 代码生成不支持使用总线的设计。
- 代码生成不支持包含多个 Signal Editor 模块的设计。
- 多文件测试用例和仿真仅在您将所有输入信号连接到同一个 Signal Editor 模块时才支持设计。

**约束**

将 Signal Editor 模块连接到 DUT 端口以将其用作模型中的源模块，但确保它不放置在 DUT 子系统内部。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2017b 中引入**

### R2025a：Signal Editor 模块更新

从 R2025a 开始，Signal Editor 模块有以下更新：

- **Interpolate data** 参数现在默认启用。

  **注意**

  如果 Signal Editor 模块是新的 Simulink Test 或 Simulink Design Verifier 测试框架模型的源，则 **Interpolate data** 参数默认关闭。
- 新增的 **Use properties from** 允许您指定信号属性定义的来源。

### R2024b：Signal Editor 模块更新

Signal Editor 模块有以下更新：

- 当您从 Signal Editor 模块打开 Signal Editor 工具时，Signal Editor 工具现在会打开并已绘制所有活动场景信号。
- Signal Editor 模块支持加载具有 `int64` 或 `uint64` 数据类型的输入信号数据值。当您使用 Signal Editor 模块加载 `int64` 或 `uint64` 信号数据时：

  - 只有信号值可以具有 `int64` 或 `uint64` 数据类型。时间值必须具有 `double` 数据类型。
  - 使用数组以外的格式，例如 `timetable`、`timeseries` 或结构体。数组格式不支持 `double` 以外的任何数据类型。

  虽然所有仿真模式都支持加载 `int64` 和 `uint64` 信号数据，但快速加速仿真不支持 `int64` 和 `uint64` 数据的插值。要将 `int64` 或 `uint64` 数据加载到快速加速仿真中：

  1. 清除 **Interpolate data** 参数。
  2. 将 **Form output after final data value by** 参数设置为除 `Extrapolation` 以外的任意值。

### R2023b：Signal Editor 模块更新

Signal Editor 模块对话框有以下更新：

- 在 **Signal properties** 部分中，新增的 **Apply signal properties to all signals** 复选框允许您将指定的信号属性应用于所有信号。
- 当您将鼠标悬停在 **Active scenario** 参数上时，工具提示会显示数据集对象的 `Name` 属性。如果该模块是使用 `signalBuilderToSignalEditor` 函数从 Signal Builder 模块转换而来的，则 `Name` 属性与 Signal Builder 模块的 **Group** 名称相同。

### R2023a：Signal Editor 模块更新

Signal Editor 模块对话框有以下更新：

- **Launch Signal Editor** 按钮已移至模块参数对话框的顶部。
- **Signal properties** 部分已重新组织。
- 在 **Signal properties** 部分中，新增的 **Apply properties to active signal in all scenarios** 复选框允许您将指定的信号属性应用于所有场景中具有相同名称的活动信号。

### R2021a：总线数组支持

Signal Editor 模块支持为总线数组加载数据。顶层模型中的 Signal Editor 模块可以在普通或加速器模式仿真中为总线数组加载数据。仅在引用模型以普通模式执行时，才支持使用引用模型中的 Signal Editor 模块为总线数组加载数据。

## 描述

显示、创建、编辑和切换可互换场景

Signal Editor 模块显示、创建和编辑包含信号的可互换场景。信号可以是：

- MATLAB® `timeseries` 对象。`timeseries` 对象不能具有空的 `Data` 属性。
- `timetable` 对象。`timetable` 对象不能表示多个变量。
- MATLAB `timeseries` 或 `timetable` 对象的结构体。
- 二维矩阵。

该模块为每个信号创建一个端口。

要创建和编辑场景以及场景中包含的信号，请点击 **Open Signal Editor** ()。您还可以使用 Signal Editor 模块将场景切换进和切换出模型。

Signal Editor 模块支持包含信号作为一个或多个标量 `Simulink.SimulationData.Dataset` 对象的 MAT 文件。

### 创建和编辑场景与信号

要创建和编辑场景及其包含的信号，请通过点击 打开 Signal Editor 工具。Signal Editor 工具使您能够通过以下方式轻松操作信号：

- 在多个数据集中创建和编辑多个信号。默认情况下，Signal Editor 创建 timeseries 格式数据。
- 使用信号表示法通过 MATLAB 表达式创建更复杂的信号。您可以使用 Author and Insert 对话框，或在表格区域中手动输入简单的 MATLAB 表达式。
- 使用现有场景获取现有数据集，您可以为其编辑和创建信号。
- 创建和编辑多维信号。

有关 Signal Editor 工具的详细信息，请参阅 Create and Edit Signal Data。

### 编程交互

要以编程方式获取 Signal Editor 模块中场景和信号的总数，请分别使用 `get_param` 函数与 `NumberOfScenarios` 和 `NumberOfSignals` 参数。这些只读参数包含字符向量形式的值。要将这些值转换为 double，请使用 `str2double` 函数。

要以编程方式使 Signal Editor 模块能够标记输出信号线，请使用 `set_param` 函数将 `PreserveSignalName` 设置为 `'on'`（默认值）。

```
set_param(gcb,'PreserveSignalName','on')
```

有关编程交互的详细信息，请参阅 Parameters 和 Replace Programmatic Use of signalbuilder。

### 导入和导出

Signal Editor 通过以下方式支持自定义文件类型，例如 Microsoft® Excel®：

- 编辑从已注册的自定义文件类型导入的信号。有关详细信息，请参阅 Import Custom File Type。
- 将信号从 Signal Editor 导出到您已注册的自定义文件类型。有关详细信息，请参阅 Export Signals to Custom Registered File Types。

### 从 Signal Builder 模块迁移

您可以使用 `signalBuilderToSignalEditor` 函数将 Signal Builder 模块配置移植到 Signal Editor 模块。有关详细信息，请参阅 Replace Signal Builder Block with Signal Editor Block 和 Migrate from Signal Builder Block to Signal Editor Block。

### 快速重启

Signal Editor 模块支持快速重启。启用快速重启后，您仍然可以：

- 更改活动场景。
- 更改活动信号。

  虽然您可以更改活动信号，但不能编辑模块中的信号属性。
- 打开 Signal Editor 并编辑数据。
