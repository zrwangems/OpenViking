---
type: simulink-block
title: 'Toggle Switch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'toggleswitch'
documentation_source_path: 'slref/toggleswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Toggle Switch

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Connection
  summary: 用于连接参数值的模块参数值连接选项
  group: ''
  block_parameter: Binding
  type: Simulink.HMI.ParamSourceInfo
  default: '[]'
- name: States
  summary: 配对值和标签 标量和字符向量
  group: ''
  block_parameter: States
  type: 两个元素的结构体数组
- name: Label
  summary: 模块标签位置 Top（默认）| Bottom | Hide
  group: ''
  block_parameter: LabelPosition
  type: 字符向量
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
```

### **Connection** — 用于连接参数值的模块参数值连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或模块参数对话框中的 **Connection** 表。要从属性检查器打开模块参数对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，也可以连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将仪表板模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程使用

要以编程方式将仪表板模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将仪表板模块连接到由值定义的参数，某些属性适用于将仪表板模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的仪表板模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数**：`Binding` |
| **类型**：`Simulink.HMI.ParamSourceInfo` |
| **默认值**：`[]` |

### **States** — 配对值和标签 标量和字符向量

要分配给已连接变量或参数的值与要在模块上显示的文本的配对。开关有两个状态——**Top** 和 **Bottom**——分别对应每个开关位置。每个状态包含一个 **Value** 和一个 **Label**。

- **Value** — 当开关处于对应位置时要分配给已连接变量或参数的值。
- **Label** — 要在模块上为对应位置显示的文本。

下表描述了该模块的默认配置。

| 位置 | 状态值 | 状态标签 |
| --- | --- | --- |
| **Top** | `0` | `on` |
| **Bottom** | `1` | `off` |

#### 编程使用

要以编程方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素的结构体数组，其字段为：

- `Value` — 该状态的标量双精度值。
- `Label` — 用作开关位置标签的字符串或字符数组。

```
topState.Value = 0;
topState.Label = 'Off';
bottomState.Value = 1;
bottomState.Label = 'On';
switchStates = [topState bottomState];
```

|  |
| --- |
| **模块参数**：`States` |
| **类型**：两个元素的结构体数组 |

### **Label** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签为已连接元素的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：字符向量 |
| **值**：`'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**：`'Top'` |
## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

仪表板模块在代码生成时会被忽略。

## 版本历史

**在 R2015a 中引入**

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 **Open In New Window** 按钮。

您可以独立于模型窗口最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击 **Open in canvas**。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink 工具条中的持久面板选项卡

当您将仪表板面板添加到模型时，Simulink 工具条中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选中任何面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名选中的面板。
- 您可以隐藏选中的面板。

### R2022b：对面板中可自定义仪表板模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义仪表板模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：工具条对面板的支持

从 R2022b 开始，您可以使用 Simulink 工具条来管理和编辑面板及其包含的仪表板模块。

当您点击面板中的仪表板模块时，该模块的工具条选项卡会出现。例如，当您点击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您点击面板时，工具条中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适应当前视图。
- 折叠选中的面板。
- 自定义面板的大小和内容。
- 为选中的面板设置自定义背景图像。
- 为选中的面板添加新选项卡。

### R2021a：使用仪表板模块调整矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到定义可调模块参数值的矩阵或结构体的标量元素。当您将仪表板模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中，选择要连接到的参数。当您选择具有非标量值的参数时，请使用对话框中的文本框指定要调整的元素。

### R2020b：Simulink 工具条对仪表板模块的支持

从 R2020b 开始，当您在模型中选择来自 Simulink 库中的 Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库的模块时，Simulink 工具条中的 **Block** 选项卡会变为特定于该模块的选项卡。从工具条中，您可以连接、断开连接和修改所选模块的连接。您可以跳转到连接到所选模块的模型元素，并且可以将所选模块添加到面板。

### R2019a：以编程方式添加和配置仪表板模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

## 描述

在两个值之间切换参数

Toggle Switch 模块在仿真期间将已连接模块参数的值在两个值之间切换。例如，您可以将 Toggle Switch 模块连接到模型中的 Switch 模块，并在仿真期间更改其状态。将 Toggle Switch 模块与其他 Dashboard 模块一起使用，可以为您的模型创建交互式仪表板。

在仿真期间以及选中该模块时，双击 Toggle Switch 模块不会打开其对话框。要编辑模块的参数，您可以使用 **Property Inspector**，或者可以右键点击该模块并从上下文菜单中选择 **Block Parameters**。

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要连接其参数的模块。从出现的列表中，选择要连接到的参数。然后，暂停在仪表板模块上，并点击 Done Connecting 按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Toggle Switch 模块连接到您的模型。

未连接的 Toggle Switch 模块连接到 Constant 模块的 Value 参数。

### 参数记录

连接到仪表板模块的可调参数会记录到仿真数据检查器中，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。
