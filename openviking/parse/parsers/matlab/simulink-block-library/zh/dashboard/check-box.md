---
type: simulink-block
title: 'Check Box'
family: dashboard
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'checkbox'
language: zh-CN
chinese_source: worker-translation
---

# Check Box

## 端口

R2025b 官方文档未提供。

## 参数

### 连接

### **连接** — 要连接参数值的模块参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的 **连接** 表。要从属性检查器打开“模块参数”对话框，请在 **连接到** 右侧单击 **连接** 或 **更改**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **连接** 表将控制模块连接到具有标量值的参数，或更改控制模块到具有标量值的参数的连接，请执行以下操作：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **参数** 选项卡上单击 **连接**。要更改该模块的连接，请改为单击 **更改**。
3. 选择要将其参数值连接到目标的模块。
4. 在表中，选择要连接到的参数。
5. 单击 **应用**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将 Dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 Dashboard 模块连接到由值定义的参数，某些属性适用于将 Dashboard 模块连接到由变量定义的参数。并非所有字段都有用于连接的值，因为给定的 Dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

### 主要

### **复选框标签** — 复选框操作的描述 `Label` (default) | character vector

显示在复选框旁边的标签。您可以使用 **复选框标签** 来描述选中该复选框时模型中发生的情况。

**示例：** `Enable sound`

#### 编程用法

|  |
| --- |
| **模块参数：** `Label` |
| **类型：** character vector |
| **默认值：** `'Label'` |

### **选中/未选中值** — 要为选中和未选中状态分配的值 `Unchecked`：`0` `Checked`：`1`（默认值）| scalar

要为选中和未选中模块状态分配给已连接变量或参数的值。

- `Unchecked` — 当 Check Box 模块未选中时分配给已连接参数的值。
- `Checked` — 当 Check Box 模块选中时分配给已连接参数的值。

#### 编程用法

您可以使用一个 `2`-by-`1` 向量以编程方式设置 **Unchecked** 和 **Checked** 值，该向量按顺序包含 **Unchecked** 和 **Checked** 值。

|  |
| --- |
| **模块参数：** `Values` |
| **类型：** `2x1` vector |
| **默认值：** `[0 1]` |

### **标签** — 模块标签位置 `Hide`（默认值）| `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### 格式

### **不透明度** — 模块背景不透明度 `1`（默认值）| scalar

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例：** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：** `Opacity` |
| **类型：** scalar |
| **默认值：** `1` |

### **前景色** — 模块前景色 `[r g b]` vector

模块前景色，包括文本。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **背景色** — 模块背景色 `[r g b]` vector

模块背景色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

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

在代码生成中，Dashboard 模块会被忽略。

## 版本历史

**R2017b 中引入**

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 Dashboard 面板。为此，请选择该面板，并将鼠标悬停在出现的省略号上。在展开的操作菜单中，单击 **在新窗口中打开** 按钮。

您可以单独于模型窗口最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止仿真以及单步执行仿真。在面板窗口中，您可以编辑该面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中单击 **在画布中打开**。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink 工具条中的持久面板选项卡

当您向模型添加 Dashboard 面板时，Simulink 工具条中会显示 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，**Panels** 选项卡在未选中面板时仍保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：对面板中可自定义 Dashboard 模块的撤销和重做支持

从 R2022b 开始，您可以对面板中可自定义 Dashboard 模块所做的更改进行撤销和重做。

要撤销或重做更改：

1. 单击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink 工具条来管理和编辑面板以及面板中包含的 Dashboard 模块。

当您单击面板中的 Dashboard 模块时，会显示该模块的工具条选项卡。例如，当您单击 Circular Gauge 模块时，工具条中会显示 **Gauge** 选项卡。

当您单击面板时，工具条中会显示 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 为所选面板添加新选项卡。

### R2021a：使用 Dashboard 模块调整矩阵和结构元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到矩阵或结构的标量元素，该元素定义可调模块参数的值。当您将 Dashboard 模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中，选择要连接到的参数。当您选择具有非标量值的参数时，请使用对话框中的文本框指定要调整的元素。

### R2020b：为若干 Dashboard 模块添加了 **背景色**、**前景色** 和 **不透明度** 属性

从 R2020b 开始，您可以为 Dashboard 库中的以下模块指定背景色、前景色和不透明度：

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b：对 Dashboard 模块的 Simulink 工具条支持

从 R2020b 开始，当您选择模型中来自 Simulink 库中的 Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库的模块时，Simulink 工具条中的 **模块** 选项卡会变为特定于该模块的选项卡。在工具条中，您可以连接、断开连接以及修改所选模块的连接。您可以跳转到连接到所选模块的模型元素，并可以将所选模块添加到面板。

### R2019a：以编程方式添加和配置 Dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

## 描述

选择参数或变量值

Check Box 模块允许您在仿真期间通过选中或清除该复选框来设置参数或变量的值。将 Check Box 模块与其他 Dashboard 模块一起使用，可以为您的模型创建交互式仪表板。

在仿真期间以及模块处于选中状态时，双击 Check Box 模块不会打开其对话框。要编辑模块的参数，可以使用 **属性检查器**，或者右键单击该模块，然后从上下文菜单中选择 **模块参数**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后单击“连接”按钮。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中单击“连接”按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要将其参数连接到目标的模块。在出现的列表中，选择要连接到的参数。然后，将鼠标悬停在 Dashboard 模块上，并单击“完成连接”按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Check Box 模块连接到您的模型。

未连接的 Check Box 模块会连接到 Gain 模块的 Gain 参数。

### 参数记录

连接到 Dashboard 模块的可调参数会记录到 Simulation Data Inspector 中，您可以在其中查看参数值以及记录的信号数据。通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，您可以在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。
