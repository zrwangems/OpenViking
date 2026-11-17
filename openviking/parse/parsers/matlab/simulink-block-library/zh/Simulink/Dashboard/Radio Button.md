---
type: simulink-block
title: 'Radio Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'radiobutton'
documentation_source_path: 'slref/radiobutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Radio Button

## 端口
```yaml
ports: []
```

在 R2025b 中未提供文档。
## 参数
```yaml
parameters:
- name: Connection
  summary: 要连接的模块参数值 参数值连接选项
  group: Connection
  block_parameter: Binding
  type: Simulink.HMI.ParamSourceInfo
  default: '[]'
- name: 枚举数据类型
  summary: 使用枚举数据类型指定状态值和标签 off（默认） | on
  group: 主要
  block_parameter: EnumeratedDataType
  type: string or character array
  values: '''on'' | ''off'''
  default: ''''''
- name: Group Name
  summary: Radio Button 组的名称 RadioButtonGroup（默认值）| character vector
  group: 主要
  block_parameter: ButtonGroupName
  type: string 或 character array
  default: '''Group'''
- name: Label
  summary: 模块标签位置 Top（默认值）| Bottom | Hide
  group: 主要
  block_parameter: LabelPosition
  type: character vector
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
- name: States
  summary: 为连接的参数选择的状态集 scalar 和 character vector
  group: 主要
  block_parameter: States
  type: structure
  default: 3x1 结构体数组
- name: Opacity
  summary: 模块背景不透明度 1（默认值） | scalar
  group: 格式
  block_parameter: Opacity
  type: scalar
  default: '1'
- name: Foreground Color
  summary: 模块前景色 [r g b] 向量
  group: 格式
  block_parameter: ForegroundColor
  type: character vector | string
  values: '[r g b] 向量'
- name: Background Color
  summary: 模块背景色 [r g b] 向量
  group: 格式
  block_parameter: BackgroundColor
  type: character vector | string
  values: '[r g b] 向量'
```

### Connection

### **Connection** — 要连接的模块参数值 参数值连接选项

仪表盘模块不使用端口连接到模型元素。要将仪表盘模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或模块参数对话框中的 **Connection** 表。要从属性检查器打开模块参数对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的某个元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅《将仪表盘模块连接到 Simulink 模型》。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数之间的连接，请执行以下操作：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。
   要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改用于定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将仪表盘模块连接到 Stateflow 图。有关详细信息，请参阅《将仪表盘模块连接到 Stateflow》(Stateflow)。

#### 编程使用

要以编程方式将 Dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 Dashboard 模块连接到由值定义的参数，某些属性适用于将 Dashboard 模块连接到由变量定义的参数。对于某个连接，并非所有字段都有值，因为给定的 Dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

### 主要

### **枚举数据类型** — 使用枚举数据类型指定状态值和标签 `off`（默认） | `on`

可以使用枚举数据类型来配置模块的状态值和标签，该枚举数据类型将数值与每个枚举成员配对。要使用枚举数据类型指定模块的状态，请先选择**枚举数据类型**选项。然后，在文本框中指定枚举数据类型的名称。指定枚举数据类型的定义必须保存在 MATLAB 路径中或基础工作区中。

**示例：** `myEnumType`

#### 编程使用

要以编程方式使用枚举数据类型指定模块的状态标签和值，请为 `UseEnumeratedDataType` 参数指定 `'on'`，并为 `EnumeratedDataType` 参数指定枚举数据类型的名称。

|  |
| --- |
| **模块参数：** `UseEnumeratedDataType` |
| **类型：** string or character array |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

|  |
| --- |
| **模块参数：** `EnumeratedDataType` |
| **类型：** string or character array |
| **默认值：** `''` |

### **Group Name** — Radio Button 组的名称 `RadioButtonGroup`（默认值）| character vector

在 Radio Button 模块上显示的一组值的名称。与 **Block Name** 和
**Label** 不同，**Group Name**
始终显示在 Radio Button 模块上。

**示例：** `Input Amplitude`

#### 编程用法

|  |
| --- |
| **模块参数：** `ButtonGroupName` |
| **类型：** string 或 character array |
| **默认值：** `'Group'` |

### **Label** — 模块标签位置 `Top`（默认值）| `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Top'` | `'Bottom'` | `'Hide'` |
| **默认值：** `'Top'` |

### **States** — 为连接的参数选择的状态集 scalar 和 character vector

可从中为连接的参数选择值的状态集。每个
**State** 由一个 **State Value** 和一个
**State Label** 组成。

- **State Value** — 选择具有相应 **Label** 的状态时，分配给连接的
  变量或参数的值。
- **State Label** — 每个状态的标签。您可以使用 **Label** 显示开关
  位于底部时连接的参数所取的值，也可以输入描述性文本标签。

单击 **+** 按钮可添加更多
**States**。

模块的默认配置包含以下
**States**。

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

#### 编程用法

要以编程方式配置模块的 `States`，请使用包含 `Value` 和 `Label` 字段的结构体数组。对于要在模块中配置的每个状态，都应在数组中包含一个结构体。

```
state1.Value = 1;
state1.Label = 'State 1';
state2.Value = 2;
state2.Label = 'State 2';
radioStates = [state1 state2];
```

|  |
| --- |
| **模块参数：** `States` |
| **类型：** structure |
| **默认值：** `3x1` 结构体数组 |

### 格式

### **Opacity** — 模块背景不透明度 `1`（默认值） | scalar

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例：** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：** `Opacity` |
| **类型：** scalar |
| **默认值：** `1` |

### **Foreground Color** — 模块前景色 `[r g b]` 向量

模块前景色，包括文本颜色。您可以从标准颜色调色板中选择颜色，也可以指定自定义颜色。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为 string 或 character vector，用于定义一个 `1` 行 `3` 列的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` 向量 |

### **Background Color** — 模块背景色 `[r g b]` 向量

模块背景色。您可以从标准颜色调色板中选择颜色，也可以指定自定义颜色。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 string 或 character vector，用于定义一个 `1` 行 `3` 列的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` 向量 |
## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成时会忽略 Dashboard 模块。

## 版本历史

**在 R2017b 中引入**

### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 Dashboard 面板。为此，请选择该面板，并将鼠标指针悬停在出现的省略号上。在展开的操作菜单中，点击 **Open In New Window** 按钮。

包含该面板的新窗口可以独立于模型窗口进行最小化和还原。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑该面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击 **Open in canvas**。

有关在新窗口中打开面板的详细信息，请参阅“在新窗口中打开面板”。

### R2023a: Simulink 工具条中的 Panels 选项卡持续可见

当您向模型添加 Dashboard 面板时，**Panels** 选项卡会出现在 Simulink 工具条中，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，即使未选中任何面板，**Panels** 选项卡也会保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名选定的面板。
- 您可以隐藏选定的面板。

### R2022b: 支持撤销和重做对面板中可自定义 Dashboard 模块的更改

从 R2022b 开始，您可以撤销和重做对面板中可自定义 Dashboard 模块所做的更改。

要撤销或重做更改，请执行以下操作：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按
   **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是
**Ctrl**。

### R2022b: 面板的工具条支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其中包含的 Dashboard 模块。

当您点击面板中的 Dashboard 模块时，会显示该模块的工具条选项卡。例如，当您点击 Circular Gauge 模块时，工具条中会显示 **Gauge** 选项卡。

当您点击面板时，工具条中会显示 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏的面板适配到当前视图中。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2021a: 使用 Dashboard 模块调节矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到定义可调模块参数值的矩阵或结构体中的标量元素。将 Dashboard 模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中选择要连接到的参数。当您选择具有非标量值的参数时，请使用对话框中的文本框指定要调节的元素。

### R2020b：为多个 Dashboard 模块添加了 **Background Color**、**Foreground Color** 和 **Opacity** 属性

从 R2020b 开始，您可以为 Dashboard 库中的以下模块指定背景颜色、前景颜色和不透明度：

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b：Simulink 工具条支持 Dashboard 模块

从 R2020b 开始，当您在模型中选择一个模块，且该模块来自 Simulink 库中的 Dashboard 库，或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库时，Simulink 工具条中的 **Block** 选项卡会变为特定于该模块的选项卡。通过该工具条，您可以为所选模块建立连接、断开连接以及修改连接。您可以跳转到与所选模块相连的模型元素，还可以将所选模块添加到面板中。

### R2019a：以编程方式添加和配置 Dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

### R2019a：增强了对 Radio Button 模块的枚举数据类型支持

从 R2019a 开始，您可以使用枚举类来配置 Radio Button 模块各状态的值和标签。要使用枚举数据类型配置 Radio Button 模块的状态，请选择 **Enumerated Data Type** 参数。在文本框中，输入要使用的枚举类的名称。

使用枚举类配置模块的状态时，您无法手动编辑、添加或删除 **States** 表中的状态。

## 描述

选择参数值

Radio Button 模块允许您在仿真期间更改所连接参数的值。您可以指定值和标签的列表，然后从该列表中选择参数值。将 Radio Button 模块与其他 Dashboard 模块结合使用，可以为模型构建由控件和指示器组成的交互式仪表盘。

在仿真期间以及模块处于选中状态时，双击 Radio Button 模块不会打开其对话框。要编辑模块参数，可以使用**属性检查器**，也可以右键点击该模块，然后从上下文菜单中选择**模块参数**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将指针悬停在要连接的模块上，然后点击“连接”按钮。要在已连接的模块上进入连接模式，请选择该模块，将指针悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击“连接”按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择包含要连接参数的模块。从出现的列表中，选择要连接到的参数。然后，将指针悬停在 Dashboard 模块上，并点击“完成连接”按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或者在仿真未运行时修改用于定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

可以连接到具有标量值的参数，或连接到矩阵或结构体的一个元素。有关详细信息，请参阅“将 Dashboard 模块连接到 Simulink 模型”。

还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅“将 Dashboard 模块连接到 Stateflow (Stateflow)”。

此动画演示如何将 Radio Button 模块连接到模型。

未连接的 Radio Button 模块连接到 Gain 模块的 Gain 参数。

### 参数记录

连接到 Dashboard 模块的可调参数会记录到仿真数据检查器中，您可以在其中将参数值与记录的信号数据一起查看。通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，您可以在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅“将数据导出到工作区或文件”。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的一个元素进行访问。
