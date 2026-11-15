---
type: simulink-block
title: 'Combo Box'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Dashboard'
documentation_page: 'combobox'
documentation_source_path: 'slref/combobox.html'
language: zh-CN
chinese_source: worker-translation
---

# Combo Box

## 端口

R2025b 中未记录。

## 参数

### 连接

### **Connection** — 用于将模块参数值连接到参数值的连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的 **Connection** 表。要从属性检查器打开“模块参数”对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的某个元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅将仪表板模块连接到 Simulink 模型。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **参数** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接到其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义所连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将仪表板模块连接到 Stateflow 图。有关详细信息，请参阅将仪表板模块连接到 Stateflow (Stateflow)。

#### 编程用法

要以编程方式将仪表板模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将仪表板模块连接到由值定义的参数，某些属性适用于将仪表板模块连接到由变量定义的参数。并非所有字段都具有连接值，因为给定的仪表板模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

### 主要

### **Enumerated Data Type** — 使用枚举数据类型指定状态值和标签 `off` (default) | `on`

您可以使用将数值与每个枚举配对的枚举数据类型，为模块配置状态值和标签。要使用枚举数据类型指定模块的状态，请先选择 **Enumerated Data Type** 选项。然后，在文本框中指定枚举数据类型的名称。指定的枚举数据类型的定义必须保存在 MATLAB 路径上或基础工作区中。

**示例：** `myEnumType`

#### 编程用法

要使用枚举数据类型以编程方式指定模块的状态标签和值，请为 `UseEnumeratedDataType` 参数指定 `'on'`，并为 `EnumeratedDataType` 参数指定枚举数据类型的名称。

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

### **Label** — 模块标签位置 `Hide` (default) | `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的某个元素时，标签为所连接元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **States** — 用于所连接参数 scalar and character vector 的状态集

用于为所连接参数选择值的状态集。每个 **状态** 由 **状态值** 和 **状态标签** 组成。

- **状态值** — 当您选择具有对应 **Label** 的状态时，分配给所连接变量或参数的值。
- **状态标签** — 每个状态的标签。您可以使用 **Label** 显示当开关位于底部时所连接参数采用的值，也可以输入描述性文本标签。

点击 **+** 按钮可添加其他 **States**。

模块的默认配置包括以下 **States**。

| 状态值 | 状态标签 |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

#### 编程用法

要以编程方式配置模块的 `States`，请使用包含字段 `Value` 和 `Label` 的结构体数组。对于要在模块上配置的每个状态，请在数组中包含一个结构体。

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
| **默认值：** `3x1` structure array |

### 格式

### **Opacity** — 模块背景不透明度 `1` (default) | scalar

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例：** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：** `Opacity` |
| **类型：** scalar |
| **默认值：** `1` |

### **Foreground Color** — 模块前景色 `[r g b]` vector

模块前景色，包括文本。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ForegroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Background Color** — 模块背景色 `[r g b]` vector

模块背景色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`-by-`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

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

代码生成时会忽略仪表板模块。

## 版本历史

**在 R2017b 中引入**

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。为此，请选择该面板，并将鼠标悬停在出现的省略号上。在展开的操作菜单中，点击 **Open In New Window** 按钮 。

您可以独立于模型窗口最小化和还原包含面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中点击 **Open in canvas** 。

有关在新窗口中打开面板的详细信息，请参阅在新窗口中打开面板。

### R2023a：Simulink 工具条中的持久面板选项卡

当您将仪表板面板添加到模型时，Simulink 工具条中会出现 **面板** 选项卡，并显示用于管理和编辑面板的选项。

以前，**面板** 选项卡仅在选中面板时可见。从 R2023a 开始，未选中面板时，**面板** 选项卡仍保持可见。

**面板** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：对面板中可自定义仪表板模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义仪表板模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink 工具条管理和编辑面板及其包含的仪表板模块。

当您点击面板中的仪表板模块时，会出现该模块的工具条选项卡。例如，当您点击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您点击面板时，工具条中会出现 **面板** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2021a：使用仪表板模块调整矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到矩阵或结构体的标量元素，该元素定义可调模块参数的值。当您将仪表板模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中选择要连接到的参数。当您选择具有非标量值的参数时，请使用对话框中的文本框指定要调整的元素。

### R2020b：为多个仪表板模块添加了 **Background Color**、**Foreground Color** 和 **Opacity** 属性

从 R2020b 开始，您可以为 Dashboard 库中的以下模块指定背景色、前景色和不透明度：

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b：对仪表板模块的 Simulink 工具条支持

从 R2020b 开始，当您在模型中选择的模块来自 Simulink 库中的 Dashboard 库或 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库时，Simulink 工具条中的 **Block** 选项卡会变为特定于该模块的选项卡。在工具条中，您可以连接、断开连接以及修改所选模块的连接。您可以跳转到连接到所选模块的模型元素，并且可以将所选模块添加到面板。

### R2019b：对 Rotary Switch 模块和 Combo Box 模块的增强枚举数据类型支持

从 R2019b 开始，您可以使用枚举类为 Rotary Switch 模块和 Combo Box 模块的状态配置值和标签。

要使用枚举数据类型配置 Rotary Switch 或 Combo Box 模块的 **States**，请选择 **Enumerated Data Type**。在文本框中，输入要使用的枚举类的名称。

当您使用枚举类配置模块的状态时，无法从 **States** 表中手动编辑、添加或删除状态。

### R2019a：以编程方式添加和配置仪表板模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

## 描述

从下拉菜单中选择参数值

Combo Box 模块允许您将参数值设置为多个值之一。您可以通过 Combo Box 模块参数定义每个可选值及其标签。将 Combo Box 模块与其他仪表板模块一起使用，为您的模型构建包含控件和指示器的交互式仪表板。

在仿真期间以及选中该模块时，双击 Combo Box 模块不会打开其对话框。要编辑该模块的参数，您可以使用 **属性检查器**，也可以右键点击该模块，并从上下文菜单中选择 **模块参数**。

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要连接到其参数的模块。从出现的列表中，选择要连接到的参数。然后，将鼠标悬停在仪表板模块上，并点击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义所连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的某个元素。有关详细信息，请参阅将仪表板模块连接到 Simulink 模型。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅将仪表板模块连接到 Stateflow (Stateflow)。

此动画展示了如何将 Combo Box 模块连接到您的模型。

未连接的 Combo Box 模块会连接到 Gain 模块的 Gain 参数。

### 参数记录

连接到仪表板模块的可调参数会记录到仿真数据检查器中，您可以在其中查看参数值以及记录的信号数据。您可以使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅将数据导出到工作区或文件。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。
