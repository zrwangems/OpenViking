---
type: simulink-block
title: 'Edit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'edit'
documentation_source_path: 'slref/edit.html'
language: zh-CN
chinese_source: worker-translation
---

# Edit

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
  group: 连接
  block_parameter: Binding
  type: Simulink.HMI.ParamSourceInfo
  default: '[]'
- name: Align
  summary: 文本对齐方式 Center（默认）| Left | Right
  group: 主要
  block_parameter: Alignment
  type: 字符串或字符向量
  values: '''Center'' | ''Left'' | ''Right'''
  default: '''Center'''
- name: Label
  summary: 模块标签位置 Hide（默认）| Bottom | Top
  group: 主要
  block_parameter: LabelPosition
  type: 字符向量
  values: '''Hide'' | ''Bottom'' | ''Top'''
  default: '''Hide'''
- name: Opacity
  summary: 模块背景不透明度 1（默认）| 标量
  group: 格式
  block_parameter: Opacity
  type: 标量
  default: '1'
- name: Foreground Color
  summary: 模块前景色 [r g b] 向量
  group: 格式
  block_parameter: ForegroundColor
  type: 字符向量 | 字符串
  values: '[r g b] 向量'
- name: Background Color
  summary: 模块背景色 [r g b] 向量
  group: 格式
  block_parameter: BackgroundColor
  type: 字符向量 | 字符串
  values: '[r g b] 向量'
```

### 连接

### **Connection** — 用于连接参数值的模块参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的 **Connection** 表。要从属性检查器打开“模块参数”对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要将其参数值连接到的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将 Dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 Dashboard 模块连接到由值定义的参数，某些属性适用于将 Dashboard 模块连接到由变量定义的参数。并非所有字段都有连接的值，因为给定的 Dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

### 主要

### **Align** — 文本对齐方式 `Center`（默认）| `Left` | `Right`

Edit 模块中文本的对齐方式。

#### 编程用法

|  |
| --- |
| **模块参数：** `Alignment` |
| **类型：** 字符串或字符向量 |
| **值：** `'Center'` | `'Left'` | `'Right'` |
| **默认值：** `'Center'` |

### **Label** — 模块标签位置 `Hide`（默认）| `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** 字符向量 |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### 格式

### **Opacity** — 模块背景不透明度 `1`（默认）| 标量

模块背景不透明度，指定为介于 0 和 1 之间的标量值。

**示例：** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：** `Opacity` |
| **类型：** 标量 |
| **默认值：** `1` |

### **Foreground Color** — 模块前景色 `[r g b]` 向量

模块前景色，包括文本。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** 字符向量 | 字符串 |
| **值：** `[r g b]` 向量 |

### **Background Color** — 模块背景色 `[r g b]` 向量

模块背景色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** 字符向量 | 字符串 |
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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2017b 中引入**

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 Dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 **Open In New Window** 按钮。

您可以独立于模型窗口最小化和还原包含该面板的新窗口。从面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击 **Open in canvas**。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink 工具条中的持久面板选项卡

当您将 Dashboard 面板添加到模型时，Simulink 工具条中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选中任何面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：对面板中可自定义 Dashboard 模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义 Dashboard 模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：工具条对面板的支持

从 R2022b 开始，您可以使用 Simulink 工具条管理和编辑面板及其包含的 Dashboard 模块。

当您点击面板中的 Dashboard 模块时，该模块的工具条选项卡会出现。例如，当您点击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您点击面板时，工具条中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2021a：使用 Dashboard 模块调节矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到定义可调模块参数值的矩阵或结构体的标量元素。当您将 Dashboard 模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中，选择要连接到的参数。当您选择具有非标量值的参数时，使用对话框中的文本框指定要调节的元素。

### R2020b：为多个 Dashboard 模块添加了 **Background Color**、**Foreground Color** 和 **Opacity** 属性

从 R2020b 开始，您可以为 Dashboard 库中的以下模块指定背景色、前景色和不透明度：

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b：Simulink 工具条对 Dashboard 模块的支持

从 R2020b 开始，当您在模型中选择来自 Simulink 库中的 Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库的模块时，Simulink 工具条中的 **Block** 选项卡会变为特定于该模块的选项卡。从工具条中，您可以连接、断开连接和修改所选模块的连接。您可以跳转到连接到所选模块的模型元素，并且可以将所选模块添加到面板。

### R2019a：以编程方式添加和配置 Dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

## 描述

输入参数的新值

Edit 模块允许您在仿真期间为模块参数键入新值。将 Edit 模块与其他 Dashboard 模块一起使用，为您的模型构建交互式控件和指示器仪表板。

在仿真期间以及选中模块时，双击 Edit 模块不会打开其对话框。要编辑模块参数，您可以使用 **Property Inspector**，或者可以右键点击模块并从上下文菜单中选择 **Block Parameters**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上并点击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。从出现的列表中，选择要连接到的参数。然后，暂停在 Dashboard 模块上并点击 Done Connecting 按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Edit 模块连接到您的模型。

未连接的 Edit 模块连接到 Gain 模块的 Gain 参数。

### 参数记录

连接到 Dashboard 模块的可调参数会记录到仿真数据检查器中，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。
