---
type: simulink-block
title: 'Rotary Switch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Dashboard'
documentation_page: 'rotaryswitch'
documentation_source_path: 'slref/rotaryswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotary Switch



切换旋钮开关所设置的参数值

## 库

Simulink / Dashboard

## 描述

Rotary Switch 在仿真期间将所连接模块参数的值更改为多个指定值。例如，您可以将 Rotary Switch 模块连接到模型中输入信号的 amplitude 或 frequency，并在仿真期间更改其特性。将 Rotary Switch 模块与其他 Dashboard 模块一起使用，以创建交互式 dashboard 来控制您的模型。

在仿真期间且选中该模块时，双击 Rotary Switch 模块不会打开其对话框。要编辑模块的参数，可以使用 **Property Inspector**，或者右键单击该模块，然后从上下文菜单中选择 **Block Parameters**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用 connect mode。要在未连接的模块上进入 connect mode，请将鼠标悬停在要连接的模块上，然后单击 Connect 按钮 。要在已连接的模块上进入 connect mode，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入 connect mode。选择要将其参数连接到的模块。在出现的列表中，选择要连接到的参数。然后，将鼠标悬停在 dashboard 模块上，并单击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。若要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Rotary Switch 模块连接到您的模型。

未连接的 Rotary Switch 模块连接到 Gain 模块的 Gain 参数。

### 参数记录

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。

## 参数

### **Connection** — 要连接的模块参数值 parameter value connection options

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用 connect mode、Simulink® Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧单击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关 connect mode 以及如何使用 toolstrip 进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块到具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的 **Parameters** 选项卡上单击 **Connect**。要更改该模块的连接，请改为单击 **Change**。
3. 选择要将其参数值连接到的模块。
4. 在该表中，选择要连接到的参数。
5. 单击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。若要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您还可以将 dashboard 模块连接到 Stateflow 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### Programmatic Use

要以编程方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。有些属性适用于将 dashboard 模块连接到由值定义的参数，有些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都有连接的值，因为给定 dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.ParamSourceInfo` |
| **Default:** `[]` |

### **States** — 位置标签和值 scalar and character vector

要分配给所连接变量或参数的数值对，并带有用于该模块的标签。一个 State 由一个 **State Value** 和一个 **State Label** 组成。

- **State Value** — 当 Rotary Switch 模块位于对应 **State Label** 时，分配给所连接变量或参数的值。
- **State Label** — 开关位置的标签。您可以使用 **State Label** 显示当 Rotary Switch 模块指向 **State Label** 时所连接变量或参数采用的值，也可以使用描述性文本标签。

单击 **+** 按钮以添加 **States**。

该模块的默认配置包含以下 **States**：

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |

#### Programmatic Use

要以编程方式配置该模块的 **States**，请将 `States` 参数的值指定为具有以下字段的结构体数组：

- `Value` — 该状态的标量 double 值。
- `Label` — 要用作开关位置标签的字符串或字符数组。

为要对该模块指定的每个状态在数组中包含一个结构体元素。

```
state1.Value = 1;
state1.Label = 'State 1';
state2.Value = 2;
state2.Label = 'State 2';
states = [state1 state2];
```

|  |
| --- |
| **Block Parameter:** `States` |
| **Type:** structure array |

### **Enumerated Data Type** — 使用枚举数据类型指定状态值和标签 `off` (default) | `on`

您可以使用枚举数据类型，该类型将数值与每个枚举配对，以配置该模块的状态值和标签。要使用枚举数据类型为该模块指定状态，请先选择 **Enumerated Data Type** 选项。然后，在文本框中指定枚举数据类型的名称。指定的枚举数据类型的定义必须保存在 MATLAB path 或 base workspace 中。

**Example:** `myEnumType`

#### Programmatic Use

要使用枚举数据类型以编程方式为该模块指定状态标签和值，请为 `UseEnumeratedDataType` 参数指定 `'on'`，并为 `EnumeratedDataType` 参数指定枚举数据类型的名称。

|  |
| --- |
| **Block Parameter:** `UseEnumeratedDataType` |
| **Type:** string or character array |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

|  |
| --- |
| **Block Parameter:** `EnumeratedDataType` |
| **Type:** string or character array |
| **Default:** `''` |

### **Label** — 模块标签位置 `Top` (default) | `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接元素的名称。

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Top'` | `'Bottom'` | `'Hide'` |
| **Default:** `'Top'` |

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

Dashboard 模块在代码生成时会被忽略。

### 版本历史记录

**Introduced in R2015a**

### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板，并将鼠标悬停在出现的省略号上。在展开的操作菜单中，单击 **Open In New Window** 按钮 。

您可以独立于模型窗口，最小化和还原包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和逐步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中，单击 **Open in canvas** 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a: Simulink Toolstrip 中的持久 Panels 选项卡

当您将 dashboard 面板添加到模型时，**Panels** 选项卡会出现在 Simulink Toolstrip 中，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，未选择面板时，**Panels** 选项卡仍保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b: 面板中可自定义 dashboard 模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 单击该面板或该面板中的某个模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷方式基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b: 面板的 Toolstrip 支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

当您单击面板中的 dashboard 模块时，该模块的 toolstrip 选项卡会出现。例如，当您单击 Circular Gauge 模块时，**Gauge** 选项卡会出现在 toolstrip 中。

当您单击面板时，**Panel** 选项卡会出现在 toolstrip 中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2021a: 使用 dashboard 模块调节矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到定义可调模块参数值的矩阵或结构体的标量元素。当您将 dashboard 模块连接到可调参数时，您首先选择一个或多个模块。然后，在对话框中，选择要连接到的参数。当您选择具有非标量值的参数时，请使用对话框中的文本框指定要调节的元素。

### R2020b: dashboard 模块的 Simulink Toolstrip 支持

从 R2020b 开始，当您在模型中选择来自 Simulink 库中的 Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库的模块时，Simulink Toolstrip 中的 **Block** 选项卡会变为特定于模块的选项卡。在 toolstrip 中，您可以连接、断开连接和修改所选模块的连接。您可以跳转到连接到所选模块的模型元素，并可以将所选模块添加到面板。

### R2019b: Rotary Switch 模块和 Combo Box 模块的增强枚举数据类型支持

从 R2019b 开始，您可以使用枚举类来配置 Rotary Switch 模块和 Combo Box 模块的状态值和标签。

要使用枚举数据类型配置 Rotary Switch 或 Combo Box 模块的 **States**，请选择 **Enumerated Data Type**。在文本框中，输入要使用的枚举类的名称。

当您使用枚举类配置模块的状态时，无法从 **States** 表中手动编辑、添加或移除状态。

### R2019a: 以编程方式添加和配置 dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

## 端口

R2025b 官方文档未提供。
