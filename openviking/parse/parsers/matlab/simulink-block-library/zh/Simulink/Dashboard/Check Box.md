---
type: simulink-block
title: 'Check Box'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'checkbox'
documentation_source_path: 'slref/checkbox.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Box

## 端口
```yaml
ports: []
```

R2025b 中未提供文档。
## 参数
```yaml
parameters:
- name: 连接
  summary: 要连接的模块参数值 参数值连接选项
  group: 连接
  block_parameter: Binding
  type: Simulink.HMI.ParamSourceInfo
  default: '[]'
- name: 复选框标签
  summary: 复选框操作的说明 Label (默认) | character vector
  group: 主要
  block_parameter: Label
  type: character vector
  default: '''Label'''
- name: 选中/未选中值
  summary: '为选中和未选中状态分配的值 Unchecked: 0 Checked: 1 (默认) | scalar'
  group: 主要
  block_parameter: Values
  type: 2x1 vector
  default: '[0 1]'
- name: 标签
  summary: 模块标签位置 Hide（默认）| Bottom | Top
  group: 主要
  block_parameter: LabelPosition
  type: 字符向量
  values: '''Hide'' | ''Bottom'' | ''Top'''
  default: '''Hide'''
- name: 不透明度
  summary: 模块背景不透明度 1（默认）| 标量
  group: 格式
  block_parameter: Opacity
  type: 标量
  default: '1'
- name: 前景色
  summary: 模块前景色 [r g b] 向量
  group: 格式
  block_parameter: ForegroundColor
  type: 字符向量 | 字符串
  values: '[r g b] 向量'
- name: 背景色
  summary: 模块背景色 [r g b] 向量
  group: 格式
  block_parameter: BackgroundColor
  type: 字符向量 | 字符串
  values: '[r g b] 向量'
```

### 连接

### **连接** — 要连接的模块参数值 参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或模块参数对话框中的**连接**表。要从属性检查器打开模块参数对话框，请在**连接到**右侧点击**连接**或**更改**。您可以连接到具有标量值的参数，也可以连接到矩阵的某个元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

要使用**连接**表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数之间的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的
   **参数**选项卡上，点击**连接**。
   要更改该模块的连接，请改为点击**更改**。
3. 选择您要连接到其参数值的模块。
4. 在表中，选择您要连接到的参数。
5. 点击**应用**。

在更新模型框图之前，控制模块无法连接到由变量定义的参数。当仿真未运行时，要连接到由变量定义的参数，或修改用于定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型框图。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

#### 以编程方式使用

要以编程方式将仪表盘模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。一些属性适用于将仪表盘模块连接到由值定义的参数，另一些属性适用于将仪表盘模块连接到由变量定义的参数。对于某个连接，并非所有字段都有值，因为给定的仪表盘模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

### 主要

### **复选框标签** — 复选框操作的说明 `Label` (默认) | character vector

显示在复选框旁边的标签。您可以使用 **复选框标签** 来描述在模型中选中该复选框时会发生的情况。

**示例：** `Enable sound`

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `Label` |
| **类型：** character vector |
| **默认值：** `'Label'` |

### **选中/未选中值** — 为选中和未选中状态分配的值 `Unchecked`: `0` `Checked`: `1` (默认) | scalar

在模块处于选中或未选中状态时，要分配给所连接变量或参数的值。

- `Unchecked` — 当 Check Box 模块未选中时，分配给所连接参数的值。
- `Checked` — 当 Check Box 模块处于选中状态时，分配给所连接参数的值。

#### 以编程方式使用

您可以使用一个 `2` 行 `1` 列的向量，以编程方式设置 **未选中** 和 **选中** 值，该向量按此顺序包含 **未选中** 和 **选中** 值。

|  |
| --- |
| **模块参数：** `Values` |
| **类型：** `2x1` vector |
| **默认值：** `[0 1]` |

### **标签** — 模块标签位置 `Hide`（默认）| `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程使用

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** 字符向量 |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### 格式

### **不透明度** — 模块背景不透明度 `1`（默认）| 标量

模块背景不透明度，指定为介于 0 和 1 之间的标量值。

**示例：** `0.5`

#### 编程使用

|  |
| --- |
| **模块参数：** `Opacity` |
| **类型：** 标量 |
| **默认值：** `1` |

### **前景色** — 模块前景色 `[r g b]` 向量

模块前景色，包括文本的颜色。您可以从标准颜色调色板中选择颜色，也可以指定自定义颜色。

#### 编程使用

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个
`1`×`3` 的
`[r g b]` 向量，其值介于 `0` 和
`1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** 字符向量 | 字符串 |
| **值：** `[r g b]` 向量 |

### **背景色** — 模块背景色 `[r g b]` 向量

模块背景色。您可以从标准颜色调色板中选择颜色，也可以指定自定义颜色。

#### 编程使用

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的
`[r g b]` 向量，其值介于 `0` 和
`1` 之间。

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

代码生成时会忽略 Dashboard 模块。

## 版本历史

**引入于 R2017b**

### R2023b：在新窗口中打开面板

从 R2023b 开始，可以在新窗口中打开 Dashboard 面板。为此，请选择该面板，并将鼠标指针悬停在出现的省略号上。在展开的操作菜单中，单击 **Open In New Window** 按钮。

可以独立于模型窗口，最小化和还原包含该面板的新窗口。在面板窗口中，可以运行、暂停、停止和逐步执行仿真。在面板窗口中，还可以编辑面板及其中包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中单击 **Open in canvas**。

有关在新窗口中打开面板的详细信息，请参阅“在新窗口中打开面板”。

### R2023a：Simulink 工具条中的 **Panels** 选项卡保持可见

向模型添加 Dashboard 面板时，Simulink 工具条中会出现 **Panels** 选项卡，其中显示用于管理和编辑面板的选项。

以前，只有选中面板时，**Panels** 选项卡才可见。从 R2023a 开始，即使未选中任何面板，**Panels** 选项卡也会保持可见。

**Panels** 选项卡还包含以下新选项：

- 可以添加空面板。
- 可以重命名所选面板。
- 可以隐藏所选面板。

### R2022b：支持撤消和重做对面板中可自定义 Dashboard 模块所做的更改

从 R2022b 开始，可以撤消和重做对面板中可自定义 Dashboard 模块所做的更改。

要撤消或重做更改，请执行以下操作：

1. 单击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤消更改，或按 **Ctrl+Y** 重做更改。

**注意**

这些键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘)，而不是 **Ctrl**。

### R2022b: 工具条对面板的支持

从 R2022b 开始，您可以使用 Simulink 工具条来管理和编辑面板以及其中包含的 Dashboard 模块。

当您点击面板中的 Dashboard 模块时，会出现该模块对应的工具条选项卡。例如，当您点击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您点击面板时，工具条中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏的面板适配到当前视图内。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2021a: 使用 Dashboard 模块调节矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到矩阵或结构体的标量元素，该矩阵或结构体定义了可调模块参数的值。将 Dashboard 模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中选择要连接到的参数。当您选择具有非标量值的参数时，请使用对话框中的文本框指定要调节的元素。

### R2020b: 为多个 Dashboard 模块添加了 **Background Color**、**Foreground Color** 和 **Opacity** 属性

从 R2020b 开始，您可以为 Dashboard 库中的以下模块指定背景颜色、前景颜色和不透明度：

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b：Simulink 工具条支持 Dashboard 模块

从 R2020b 开始，当您在模型中选择的模块来自 Simulink 库中的 Dashboard 库，或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库时，Simulink 工具条中的 **Block** 选项卡会变为特定于该模块的选项卡。通过工具条，您可以为所选模块建立连接、断开连接以及修改连接。您可以跳转到与所选模块连接的模型元素，还可以将所选模块添加到面板中。

### R2019a：以编程方式添加和配置 Dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数，在模型中创建和配置 Dashboard 库中的模块。

## 描述

选择参数或变量的值

Check Box 模块允许您通过选中或清除复选框，在仿真期间设置参数或变量的值。将 Check Box 模块与其他 Dashboard 模块结合使用，可为您的模型创建交互式仪表板。

在仿真期间以及选中该模块时，双击 Check Box 模块不会打开其对话框。要编辑模块参数，您可以使用 **Property Inspector**，也可以右键点击该模块，并从上下文菜单中选择 **Block Parameters**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口来连接模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标指针悬停在要连接的模块上，然后点击“连接”按钮。要在已连接的模块上进入连接模式，请选择该模块，将鼠标指针悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击“连接”按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择包含要连接的参数的模块。在出现的列表中，选择要连接到的参数。然后，将鼠标指针悬停在 Dashboard 模块上，并点击“完成连接”按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改用于定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关详细信息，请参阅“将 Dashboard 模块连接到 Simulink 模型”。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅“将 Dashboard 模块连接到 Stateflow (Stateflow)”。

此动画演示如何将 Check Box 模块连接到您的模型。

一个未连接的 Check Box 模块连接到 Gain 模块的 Gain 参数。

### 参数记录

连接到仪表盘模块的可调参数会记录到仿真数据检查器中，您可以在其中同时查看参数值和记录的信号数据。通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，您可以在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅“将数据导出到工作区或文件”。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的一个元素进行访问。
