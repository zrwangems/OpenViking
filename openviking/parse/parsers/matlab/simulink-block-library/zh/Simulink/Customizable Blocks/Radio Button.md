---
type: simulink-block
title: 'Radio Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Customizable Blocks'
documentation_page: 'customradiobutton'
documentation_source_path: 'slref/customradiobutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Radio Button



使用具有可自定义外观的单选按钮在仿真期间更改参数或变量值

## 库

Simulink / Dashboard / Customizable Blocks

## 说明

使用 Radio Button 模块在仿真之前或仿真期间更改所连接参数或变量的值。当您在 Customizable Blocks 库中使用 Radio Button 模块时，您可以自定义模块外观，例如，使模块看起来像您正在设计的数字用户界面中的单选按钮。将 Radio Button 模块与其他 dashboard 模块一起使用，为您的模型构建由控件和指示器组成的交互式 dashboard。

每个单选按钮选项对应 Radio Button 模块的一个状态。状态包含标签和值。状态标签是模块上标识选项的文本。当您选择某个选项时，Radio Button 模块进入关联状态，并将状态值赋给所连接的参数。要在仿真期间选择 Radio Button 模块上的某个选项，请单击要选择的选项的单选按钮图标或标签文本。要在仿真未运行时选择选项，请单击 Radio Button 模块以选择该模块，然后单击选项图标或文本。

要自定义状态标签或值，请打开 Property Inspector 的 **Parameters** 选项卡或 Block Parameters 对话框。

**注意**

- 在仿真期间双击已连接的 Radio Button 模块，或在单击该模块后双击，不会打开 Block Parameters 对话框。要打开 Block Parameters 对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间单击已连接的 Radio Button 模块会同时选择该模块并选择一个单选按钮选项。要在不选择选项的情况下选择该模块，请按 **Shift**，然后单击该模块。

### 自定义 Radio Button 模块

当您将 Radio Button 模块添加到模型时，该模块已预配置为默认设计。您可以使用默认设计使用该模块，也可以自定义该模块的外观。

要自定义模块外观，请使用设计模式。选择该模块后，可通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定选项卡上的 **Design** 下，单击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，单击 **Edit**。
- 暂停在模块上方出现的省略号上，然后单击 Edit Custom Block 按钮。

在设计模式中，您可以使用模块上方的工具栏自定义单选按钮。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的可自定义 Radio Button 模块，其中工具栏和 Property Inspector 中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 更改每个选项赋给所连接参数的值。 | No | Yes |
| 更改选项标签的文本。 | No | Yes |
| 添加或删除选项。 | Yes | Yes |
| 上传表示已选中单选按钮的图标。 | No | Yes |
| 上传表示未选中单选按钮的图标。 | No | Yes |
| 更改单选按钮图标位于标签的哪一侧。 | No | Yes |
| 在选项列表周围添加边框，并在列表上方添加标题。 | No | Yes |
| 更改选项列表的标题。 | No | Yes |
| 更改边框粗细。 | No | Yes |
| 更改边框和标题的颜色。 | No | Yes |
| 上传背景图像。 | No | Yes |
| 设置纯色背景颜色。 | No | Yes |
| 上传前景图像。 | No | Yes |

要更改选项标签的字体颜色，请选择 Radio Button 模块，然后在 Simulink Toolstrip 的 **Format** 选项卡上更改前景色。

完成设计编辑后，要退出设计模式，请单击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将控制模块连接到模型中的参数，或更改控制模块的连接，请进入连接模式。选择要连接其参数的模块。从出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上，并单击 Done Connecting 按钮。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构体的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Radio Button 模块连接到您的模型。

未连接的 Radio Button 模块连接到 Constant 模块。

### 参数记录

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

## 参数

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后单击 **Parameters** 选项卡。

#### 连接

### **Connection** — 用于连接参数值的模块参数值连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧单击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用 toolstrip 进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 的 **Parameters** 选项卡上，单击 **Connect**。要更改该模块的连接，请改为单击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 单击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您还可以将 dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 dashboard 模块连接到由值定义的参数，某些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都具有连接的值，因为给定的 dashboard 模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数:** `Binding` |
| **类型:** `Simulink.HMI.ParamSourceInfo` |
| **默认:** `[]` |

#### 主要

### **Label** — 显示所连接元素名称的标签位置 `Hide`（默认） | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空。

#### 编程用法

|  |
| --- |
| **模块参数:** `LabelPosition` |
| **类型:** character vector |
| **值:** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认:** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认） | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新背景图像不会更改模块的宽高比，而是会更改背景图像的宽高比以适合模块大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。当您释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。当您释放 **Shift** 键时，宽高比解锁。

### **Enumerated Data Type** — 用于使用枚举数据类型指定状态值和标签的选项 `off`（默认） | `on`

要为模块配置状态标签和值，您可以使用将每个枚举与数值配对的枚举数据类型。首先，选择 **Enumerated Data Type**。然后，在文本框中指定枚举数据类型的名称。指定的枚举数据类型的定义必须保存在 MATLAB 路径或基础工作区中。

**注意**

您可以使用 `Simulink.defineIntEnumType` 函数定义枚举数据类型。例如，要为从一到五的一组罗马数字定义枚举数据类型 `myEnumType`，请使用此命令。

    Simulink.defineIntEnumType('myEnumType',...
        {'I','II','III','IV','V'}, [1 2 3 4 5]);

然后，在 Property Inspector 的 **Parameters** 选项卡上的 **Enumerated Data Type** 文本框中，输入 `myEnumType`。

### **States** — 状态的管理和配置 scalar 和 character vector

每个单选按钮选项对应 Radio Button 模块的一个状态。状态包含标签和值。**State Label** 值是模块上标识选项的文本。当您选择某个选项时，Radio Button 模块进入关联状态，并将 **State Value** 值赋给所连接的参数。

默认情况下，该模块有三个单选按钮选项和三个对应状态。

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

您可以设计具有任意数量状态（大于或等于 1）的 Radio Button 模块。要添加新状态，请单击 **+** 按钮。要删除状态，请单击 **State Label** 列中的标签文本或 **State Value** 列中的值，然后单击 **-** 按钮。

**注意**

当 **Enumerated Data Type** 打开时，您无法添加或删除状态。您可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

要配置状态的标签文本或值，请单击 **State Label** 列中的标签文本或 **State Value** 列中的值，删除当前值，输入新值，然后按 **Enter**。

**提示**

您还可以在设计模式中配置状态的参数：

1. 选择 Radio Button 模块。
2. 进入设计模式。在 Property Inspector 的 **Design** 选项卡上，单击 **Edit**。
3. 在 **Design** 选项卡上，打开 **States** 组件，展开 **Select State** 部分，然后从下拉菜单中选择要配置的状态。
4. 在 **Text** 和 **Value** 文本框中配置所选状态的标签文本和值。

### 设计

要自定义 dashboard 模块，请打开 Property Inspector，单击 **Design** 选项卡，然后单击 **Edit**。您在本节中所做参数值的更改将应用于所有单选按钮选项。

#### Radio Button

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认） | `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新背景图像不会更改模块的比例，而是会拉伸或缩放背景图像以适合模块大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。当您释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会锁定宽高比。当您释放 **Shift** 键时，宽高比解锁。

### **Show Group** — 用于显示单选按钮选项列表周围边框的选项 `on`（默认） | `off`

选择此参数以显示单选按钮选项列表周围的边框以及列表上方的标题。要更改标题，请在 **Group Title** 框中输入新标题。

### **Group Title** — 单选按钮选项列表上方的标题 string | character array

您可以显示单选按钮选项列表周围的边框以及列表上方的标题。要显示边框和默认标题，请选择 **Show Group** 选项。要更改标题，请在 **Group Title** 文本框中输入新标题。将标题指定为 string 或 character array。

### **Border Thickness** — 单选按钮选项列表周围边框的粗细 scalar

您可以显示单选按钮选项列表周围的边框以及列表上方的标题。要显示边框和标题，请选择 **Show Group** 选项。在 **Border Thickness** 文本框中，以 pixels 为单位指定边框粗细。输入大于或等于零的 scalar。

### **Border Color** — 单选按钮选项列表周围边框以及列表上方标题的颜色 `[r g b]` vector

您可以显示单选按钮选项列表周围的边框以及列表上方的标题。要显示边框和标题，请选择 **Show Group** 选项。要更改边框和标题的颜色，请展开 **Border Color** 菜单。从标准颜色调色板中选择一种颜色，或指定自定义颜色。

### **Placement** — 单选按钮图标相对于标签的位置 `Left`（默认） | `Top` | `Right` | `Bottom`

指定单选按钮图标相对于标签的位置。

**注意**

更改单选按钮图标位置不会更改偏移。

### **Offset** — 图标相对于标签的位置 scalar

以字体高度的比例指定图标相对于标签的位置，表示为大于或等于零的 scalar。

### **Width** — 图标宽度 scalar

以标签文本字体高度的比例指定图标宽度。

**示例:** `0.5`

### **Height** — 图标高度 scalar

以标签文本字体高度的比例指定图标高度。

**示例:** `0.5`

### **Lock Aspect Ratio** — 用于保持图标宽高比的选项 `on`（默认） | `off`

打开此选项以在调整单选按钮图标大小时保持宽高比。

#### 状态

### **Select State** — 状态标签和值 scalar 和 character vector

每个单选按钮选项对应 Radio Button 模块的一个状态。状态包含标签和值。**State Label** 值是模块上标识选项的文本。当您选择某个选项时，Radio Button 模块进入关联状态，并将 **State Value** 值赋给所连接的参数。

默认情况下，该模块有三个单选按钮选项和三个对应状态。

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

您可以设计具有任意数量状态（大于或等于 1）的 Radio Button 模块。要添加新状态，请单击 **+** 按钮。要删除状态，请在 **Select State** 部分中选择该状态。然后，单击 **X** 按钮。

**注意**

当 **Enumerated Data Type** 启用时，您无法添加或删除状态。您可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

要配置状态的标签文本或值，请在 **Select State** 部分中选择该状态。然后，在 **Value** 和 **Text** 框中输入新值。

**提示**

您还可以使用 Property Inspector 中的 **Parameters** 选项卡配置模块的状态。

### **Value** — 状态值 scalar

指定在 **Select State** 部分中选择的状态的 **State Value**。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改该值。您可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

### **Text** — 状态标签文本 string | character array

指定在 **Select State** 部分中选择的状态的 **State Label** 文本。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改该文本。您可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off`（默认） | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例:** `on`

### **Color** — 模块背景颜色 `[r g b]` vector

要使用纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`-by-`3` `[r g b]` vector，其值介于 `0` 和 `1` 之间，并格式化为 string 或 character vector。

|  |
| --- |
| **模块参数:** `BackgroundColor` |
| **类型:** string | character vector |
| **值:** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1`（默认） | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的 scalar 值。

**示例:** `0.5`

### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 scalar

将模块背景颜色覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例:** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 scalar

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例:** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 scalar

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时的图像位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例:** `1`

### **Width** — 前景图像宽度 scalar

将前景图像宽度指定为模块宽度的比例。

**示例:** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像高度指定为模块高度的比例。

**示例:** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on`（默认） | `off`

选择此参数以在使用 Property Inspector 调整图像大小时保持宽高比。

### 模块特征

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

**在 R2025a 中引入**

### R2025a: 在仿真期间选择 dashboard 模块并打开 Block Parameters 对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块所代表的小工具交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块交互。例如，您可以移动或调整模块大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间均处于活动状态。提升到 dashboard 面板的模块在面板于其自己的窗口中打开或停靠且未锁定时也处于活动状态。对于 Callback Button 模块，如果按下按钮触发的至少一个 callback 具有非空值，则该模块始终处于活动状态。要与非活动模块所代表的小工具交互，您可以通过单击模块临时激活该模块。当您取消选择该模块时，该模块会再次变为非活动状态。

单击活动的 Callback Button 模块，或单击连接到参数或变量值的来自 Dashboard 或 Customizable Blocks 库的活动模块，会同时选择该模块并与该模块所代表的小工具交互。例如，单击未选择的活动的已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按 **Shift** 然后单击模块来选择该模块而不与小工具交互。同样，您可以通过按 **Shift** 然后双击模块来打开 Block Parameters 对话框。

## 端口

R2025b 官方文档未提供。
