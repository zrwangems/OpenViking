---
type: simulink-block
title: 'Combo Box'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customcombobox'
language: zh-CN
chinese_source: worker-translation
---

# Combo Box

## 端口

R2025b 官方文档未提供。

## 参数

使用属性检查器和模块参数对话框指定模块参数的值。要设置 Dashboard 模块的核心参数，请使用模块参数对话框或属性检查器中的 **Parameters** 选项卡。要自定义模块，请使用属性检查器中的 **Design** 选项卡。要打开模块的模块参数对话框，请双击该模块。要打开属性检查器，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

要设置 Dashboard 模块的核心参数，请打开属性检查器，然后点击 **Parameters** 选项卡。

#### 连接

### **Connection** — 用于连接参数值的模块参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或模块参数对话框中的 **Connection** 表。要从属性检查器打开模块参数对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，也可以连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块到具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接到其参数值的模块。
4. 在该表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将 Dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 Dashboard 模块连接到由值定义的参数，某些属性适用于将 Dashboard 模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的 Dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **Block Parameter:** `Binding` |
| **Type:** `Simulink.HMI.ParamSourceInfo` |
| **Default:** `[]` |

#### 主要

### **Label** — 显示所连接元素名称的标签位置 `Hide` (默认) | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 Dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当 Dashboard 模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **Block Parameter:** `LabelPosition` |
| **Type:** character vector |
| **Values:** `'Hide'` | `'Bottom'` | `'Top'` |
| **Default:** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会更改模块的纵横比以匹配背景图像的纵横比。当纵横比未锁定时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块的大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会临时解锁纵横比。当您释放 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，调整模块大小时按 **Shift** 键会临时锁定纵横比。当您释放 **Shift** 键时，纵横比会解锁。

### **Enumerated Data Type** — 用于使用枚举数据类型指定状态值和标签的选项 `off` (默认) | `on`

要为模块配置状态标签和值，您可以使用将每个枚举与数值配对的枚举数据类型。首先，选择 **Enumerated Data Type**。然后，在文本框中指定枚举数据类型的名称。指定的枚举数据类型的定义必须保存在 MATLAB 路径上或基础工作区中。

**注意**

您可以使用 `Simulink.defineIntEnumType` 函数定义枚举数据类型。例如，要为从一到五的一组罗马数字定义枚举数据类型 `myEnumType`，请使用以下命令。

```
Simulink.defineIntEnumType('myEnumType',...
    {'I','II','III','IV','V'}, [1 2 3 4 5]);
```

然后，在属性检查器的 **Parameters** 选项卡上，在 **Enumerated Data Type** 文本框中输入 `myEnumType`。

### **States** — 状态的管理和配置 scalar and character vector

Combo Box 下拉列表中的每个选项都对应于 Combo Box 模块的一个状态。状态具有一个标签和一个值。**State Label** 值是下拉列表中标识该选项的文本。当您选择一个选项时，Combo Box 模块进入关联状态，并将 **State Value** 赋给所连接的参数。

默认情况下，该模块具有三个 Combo Box 选项和三个对应状态。

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

您可以将 Combo Box 模块设计为具有任意数量大于或等于 1 的状态。要添加新状态，请点击 **+** 按钮。要删除状态，请点击 **State Label** 列中的标签文本或 **State Value** 列中的值，然后点击 **-** 按钮。

**注意**

当 **Enumerated Data Type** 打开时，您无法添加或删除状态。您可以在属性检查器的 **Parameters** 选项卡中关闭此选项。

要配置状态的标签文本或值，请点击 **State Label** 列中的标签文本或 **State Value** 列中的值，删除当前值，输入新值，然后按 **Enter**。

**提示**

您还可以在设计模式中配置状态的参数：

1. 选择 Combo Box 模块。
2. 进入设计模式。在属性检查器中，在 **Design** 选项卡上，点击 **Edit**。
3. 在 **Design** 选项卡上，打开 **States** 组件，展开 **Select State** 部分，然后从下拉菜单中选择要配置的状态。
4. 在 **Text** 和 **Value** 文本框中配置所选状态的标签文本和值。

### 设计

要自定义 Dashboard 模块，请打开属性检查器，点击 **Design** 选项卡，然后点击 **Edit**。您在此部分中对参数值所做的更改将应用于所有 Combo Box 选项。

#### Combo Box

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会更改模块的纵横比以匹配背景图像的纵横比。当纵横比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会解锁纵横比。当您释放 **Shift** 键时，纵横比会锁定。当纵横比未锁定时，调整模块大小时按 **Shift** 键会锁定纵横比。当您释放 **Shift** 键时，纵横比会解锁。

### **Dropdown Background Color** — 下拉列表的背景色 `[r g b]` 向量

从标准颜色调色板中为下拉列表选择背景色，或指定自定义颜色。

### **Dropdown Border Color** — 下拉列表周围边框的颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表周围的边框选择颜色，或指定自定义颜色。

### **Visible Entries** — 下拉列表中可见选项的最大数量 scalar

默认情况下，当您展开下拉列表时，最多可见五个 Combo Box 选项。您可以通过滚动访问任何不可见的选项。指定展开下拉列表时可见选项的最大数量。

### **Highlight Background Color** — 下拉列表中高亮选项的背景色 `[r g b]` 向量

从标准颜色调色板中为下拉列表中的高亮选项选择背景色，或指定自定义颜色。

### **Highlight Border Color** — 下拉列表中高亮选项周围边框的颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表中的高亮选项周围的边框选择颜色，或指定自定义颜色。

### **Highlight Font Color** — 下拉列表中高亮选项的字体颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表中的高亮选项选择字体颜色，或指定自定义颜色。

### **Width** — V 形符号宽度 scalar

将 V 形符号的宽度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Height** — V 形符号高度 scalar

将 V 形符号的高度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持 V 形符号纵横比的选项 `on` (默认) | `off`

打开此选项可在使用属性检查器调整 V 形符号大小时保持纵横比。

#### 状态

### **Select State** — 状态标签和值 scalar and character vector

Combo Box 下拉列表中的每个选项都对应于 Combo Box 模块的一个状态。状态具有一个标签和一个值。**State Label** 值是下拉列表中标识该选项的文本。当您选择一个选项时，Combo Box 模块进入关联状态，并将 **State Value** 赋给所连接的参数。

默认情况下，该模块具有三个 Combo Box 选项和三个对应状态。

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

您可以将 Combo Box 模块设计为具有任意数量大于或等于 1 的状态。要添加新状态，请点击 **+** 按钮。要删除状态，请在 **Select State** 部分中选择该状态。然后，点击 **X** 按钮。

**注意**

当 **Enumerated Data Type** 启用时，您无法添加或删除状态。您可以在属性检查器的 **Parameters** 选项卡中禁用此选项。

要配置状态的标签文本或值，请在 **Select State** 部分中选择该状态。然后，在 **Value** 和 **Text** 框中输入新值。

**提示**

您还可以使用属性检查器中的 **Parameters** 选项卡配置模块的状态。

### **Value** — 状态值 scalar

指定在 **Select State** 部分中选择的状态的 **State Value**。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改该值。您可以在属性检查器的 **Parameters** 选项卡中关闭此选项。

### **Text** — 状态标签文本 string | character array

指定在 **Select State** 部分中选择的状态的 **State Label** 文本。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改该文本。您可以在属性检查器的 **Parameters** 选项卡中关闭此选项。

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景色的选项 `off` (默认) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景色 `[r g b]` 向量

要使用纯色背景色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间，格式为字符串或字符向量。

|  |
| --- |
| **Block Parameter:** `BackgroundColor` |
| **Type:** string | character vector |
| **Values:** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1` (默认) | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景色的区域的圆角半径 scalar

将模块背景色覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负偏移值将图像向左移动，正偏移值将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负偏移值将图像向上移动，正值将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像纵横比的选项 `on` (默认) | `off`

选择此参数可在使用属性检查器调整图像大小时保持纵横比。

## 所属库

Simulink / Dashboard / Customizable Blocks

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

## 版本历史

**在 R2025a 中引入**

### R2025a：在仿真期间选择 Dashboard 模块并打开模块参数对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于 *活动* 状态时，您可以与该模块所代表的小工具进行交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块进行交互。例如，您可以移动或调整模块大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间都处于活动状态。提升到 Dashboard 面板的模块在该面板在其自身窗口中打开或停靠且未锁定时也处于活动状态。对于 Callback Button 模块，如果按下按钮所触发的至少一个回调具有非空值，则该模块始终处于活动状态。要与非活动模块所代表的小工具进行交互，您可以通过点击该模块来临时激活它。当您取消选择该模块时，该模块会再次变为非活动状态。

点击活动的 Callback Button 模块或来自 Dashboard 或 Customizable Blocks 库且连接到参数或变量值的活动模块，会同时选择该模块并与该模块所代表的小工具进行交互。例如，点击未选中的活动已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后点击该模块来选择该模块，而无需与小工具交互。同样，您可以通过按 **Shift** 然后双击该模块来打开模块参数对话框。

## 描述

使用具有可自定义外观的 Combo Box 在仿真期间更改参数或变量值

使用 Combo Box 模块在仿真前或仿真期间更改所连接参数或变量的值。当您在 Customizable Blocks 库中使用 Combo Box 模块时，可以自定义该模块的外观，例如，使该模块看起来像您正在设计的数字用户界面中的组合框。将 Combo Box 模块与其他 Dashboard 模块一起使用，可为您的模型构建由控件和指示器组成的交互式仪表板。

Combo Box 下拉列表中的每个选项都对应于 Combo Box 模块的一个状态。状态具有一个标签和一个值。状态标签是下拉列表中标识该选项的文本。当您选择一个选项时，Combo Box 模块进入关联状态，并将状态值赋给所连接的参数。要在仿真期间选择选项，请点击 Combo Box 模块以展开下拉列表，然后选择该选项。要在仿真未运行时选择选项，请点击 Combo Box 模块以选择该模块，再次点击该模块以展开下拉列表，然后选择该选项。

要自定义状态标签或值，请打开属性检查器的 **Parameters** 选项卡或模块参数对话框。

**注意**

- 在仿真期间或点击已连接的 Combo Box 模块后双击该模块，不会打开模块参数对话框。要打开模块参数对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Combo Box 模块会同时选择该模块并展开 Combo Box 下拉列表。要在不展开列表的情况下选择该模块，请按 **Shift**，然后点击该模块。

### 自定义 Combo Box 模块

当您将 Combo Box 模块添加到模型时，该模块已预配置为默认设计。您可以使用默认设计的模块，也可以自定义该模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定选项卡上的 **Design** 下，点击 **Edit**。
- 在属性检查器中，在 **Design** 选项卡上，点击 **Edit**。
- 将鼠标悬停在模块上出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式中，您可以使用模块上方的工具栏自定义 Combo Box。要访问其他自定义选项或为设计设置输入精确值，请使用属性检查器中的 **Design** 选项卡。

处于设计模式的 Customizable Combo Box 模块，其中工具栏和属性检查器中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 更改每个选项赋给所连接参数的值。 | No | Yes |
| 更改选项标签的文本。 | No | Yes |
| 添加或删除选项。 | Yes | Yes |
| 更改下拉列表的 V 形图标。 | No | Yes |
| 更改下拉列表中可见条目的数量。 | No | Yes |
| 更改下拉列表的背景色和边框颜色。 | No | Yes |
| 更改下拉列表中高亮条目的背景色、边框色和字体颜色。 | No | Yes |
| 上传背景图像。 | No | Yes |
| 设置纯色背景色。 | No | Yes |
| 上传前景图像。 | No | Yes |

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入连接模式。选择要连接到其参数的模块。从出现的列表中，选择要连接到的参数。然后，将鼠标悬停在 Dashboard 模块上，并点击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Combo Box 模块连接到您的模型。

未连接的 Combo Box 模块会连接到 Constant 模块。

### 参数记录

连接到 Dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。
