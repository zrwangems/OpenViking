---
type: simulink-block
title: 'Combo Box'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'customcombobox'
documentation_source_path: 'slref/customcombobox.html'
language: zh-CN
chinese_source: worker-translation
---

# Combo Box

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Connection
  summary: 要连接的模块参数值 参数值连接选项
  group: 参数
  block_parameter: Binding
  type: Simulink.HMI.ParamSourceInfo
  default: '[]'
- name: Label
  summary: 显示已连接元素名称的标签位置 Hide（默认）| Bottom | Top
  group: 参数
  block_parameter: LabelPosition
  type: 字符向量
  values: '''Hide'' | ''Bottom'' | ''Top'''
  default: '''Hide'''
- name: Lock Aspect Ratio
  summary: 保持模块宽高比的选项 on（默认）| off
  group: 参数
- name: Enumerated Data Type
  summary: 使用枚举数据类型指定状态值和标签的选项 off（默认）| on
  group: 参数
- name: States
  summary: 状态的管理和配置 标量和字符向量
  group: 参数
- name: Lock Aspect Ratio
  summary: 保持模块宽高比的选项 on（默认）| off
  group: 设计
- name: Dropdown Background Color
  summary: 下拉列表的背景颜色 [r g b] 向量
  group: 设计
- name: Dropdown Border Color
  summary: 下拉列表边框的颜色 [r g b] 向量
  group: 设计
- name: Visible Entries
  summary: 下拉列表中可见选项的最大数量 标量
  group: 设计
- name: Highlight Background Color
  summary: 下拉列表中高亮选项的背景颜色 [r g b] 向量
  group: 设计
- name: Highlight Border Color
  summary: 下拉列表中高亮选项边框的颜色 [r g b] 向量
  group: 设计
- name: Highlight Font Color
  summary: 下拉列表中高亮选项的字体颜色 [r g b] 向量
  group: 设计
- name: Width
  summary: 尖角宽度 标量
  group: 设计
- name: Height
  summary: 尖角高度 标量
  group: 设计
- name: Lock Aspect Ratio
  summary: 保持尖角宽高比的选项 on（默认）| off
  group: 设计
- name: Select State
  summary: 状态标签和值 标量和字符向量
  group: 设计
- name: Value
  summary: 状态值 标量
  group: 设计
- name: Text
  summary: 状态标签文本 字符串 | 字符数组
  group: 设计
- name: Use Background Color
  summary: 指定纯色模块背景颜色的选项 off（默认）| on
  group: 设计
- name: Color
  summary: 模块背景颜色 [r g b] 向量
  group: 设计
  block_parameter: BackgroundColor
  type: 字符串 | 字符向量
  values: '[r g b] 向量'
- name: Opacity
  summary: 模块背景不透明度 1（默认）| 标量
  group: 设计
- name: Corner Radius
  summary: 模块背景颜色区域的圆角半径 标量
  group: 设计
- name: X Offset
  summary: 前景图像左边缘相对于模块左边缘的水平偏移 标量
  group: 设计
- name: Y Offset
  summary: 前景图像上边缘相对于模块上边缘的垂直偏移 标量
  group: 设计
- name: Width
  summary: 前景图像宽度 标量
  group: 设计
- name: Height
  summary: 前景图像高度 标量
  group: 设计
- name: Lock Aspect Ratio
  summary: 保持前景图像宽高比的选项 on（默认）| off
  group: 设计
```

使用属性检查器和模块参数对话框来指定模块参数的值。要设置仪表板模块的核心参数，请使用模块参数对话框或属性检查器中的 **Parameters** 选项卡。要自定义模块，请使用属性检查器中的 **Design** 选项卡。要打开模块的模块参数对话框，请双击该模块。要打开属性检查器，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

### 参数

要设置仪表板模块的核心参数，请打开属性检查器并点击 **Parameters** 选项卡。

#### 连接

### **Connection** — 要连接的模块参数值 参数值连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink 工具条或模块参数对话框中的 **Connection** 表。要从属性检查器打开模块参数对话框，请在 **Connected to** 右侧，点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将仪表板模块连接到 Stateflow 图表。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将仪表板模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将仪表板模块连接到由值定义的参数，某些属性适用于将仪表板模块连接到由变量定义的参数。并非所有字段都有连接的值，因为给定的仪表板模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

#### 主要

### **Label** — 显示已连接元素名称的标签位置 `Hide`（默认）| `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示仪表板模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当仪表板模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** 字符向量 |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认）| `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适应模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。当您释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。当您释放 **Shift** 键时，宽高比解锁。

### **Enumerated Data Type** — 使用枚举数据类型指定状态值和标签的选项 `off`（默认）| `on`

要配置模块的状态标签和值，您可以使用将每个枚举与数值配对的枚举数据类型。首先，选择 **Enumerated Data Type**。然后，在文本框中指定枚举数据类型的名称。指定的枚举数据类型的定义必须保存在 MATLAB 路径或基础工作区中。

**注意**

您可以使用 `Simulink.defineIntEnumType` 函数定义枚举数据类型。例如，要为从一到五的一组罗马数字定义枚举数据类型 `myEnumType`，请使用以下命令。

```
Simulink.defineIntEnumType('myEnumType',...
    {'I','II','III','IV','V'}, [1 2 3 4 5]);
```

然后，在属性检查器的 **Parameters** 选项卡上，在 **Enumerated Data Type** 文本框中，输入 `myEnumType`。

### **States** — 状态的管理和配置 标量和字符向量

组合框下拉列表中的每个选项对应于 Combo Box 模块的一个状态。状态具有标签和值。**State Label** 值是下拉列表中标识该选项的文本。当您选择某个选项时，Combo Box 模块进入关联的状态，并将 **State Value** 值赋给已连接的参数。

默认情况下，该模块具有三个组合框选项和三个对应的状态。

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

您可以设计具有任意数量大于或等于 1 的状态的 Combo Box 模块。要添加新状态，请点击 **+** 按钮。要删除状态，请点击 **State Label** 列中的标签文本或 **State Value** 列中的值，然后点击 **-** 按钮。

**注意**

当 **Enumerated Data Type** 打开时，您无法添加或删除状态。您可以在属性检查器的 **Parameters** 选项卡中关闭此选项。

要配置状态的标签文本或值，请点击 **State Label** 列中的标签文本或 **State Value** 列中的值，删除当前值，输入新值，然后按 **Enter**。

**提示**

您还可以在设计模式下配置状态的参数：

1. 选择 Combo Box 模块。
2. 进入设计模式。在属性检查器的 **Design** 选项卡上，点击 **Edit**。
3. 在 **Design** 选项卡上，打开 **States** 组件，展开 **Select State** 部分，然后从下拉菜单中，选择要配置的状态。
4. 在 **Text** 和 **Value** 文本框中配置所选状态的标签文本和值。

### 设计

要自定义仪表板模块，请打开属性检查器，点击 **Design** 选项卡，然后点击 **Edit**。您在此部分中对参数值所做的更改将应用于所有组合框选项。

#### Combo Box

### **Lock Aspect Ratio** — 保持模块宽高比的选项 `on`（默认）| `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适应模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。当您释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会锁定宽高比。当您释放 **Shift** 键时，宽高比解锁。

### **Dropdown Background Color** — 下拉列表的背景颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表选择背景颜色，或指定自定义颜色。

### **Dropdown Border Color** — 下拉列表边框的颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表的边框选择颜色，或指定自定义颜色。

### **Visible Entries** — 下拉列表中可见选项的最大数量 标量

默认情况下，当您展开下拉列表时，最多可见五个组合框选项。您可以通过滚动访问任何不可见的选项。指定展开下拉列表时可见选项的最大数量。

### **Highlight Background Color** — 下拉列表中高亮选项的背景颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表中高亮的选项选择背景颜色，或指定自定义颜色。

### **Highlight Border Color** — 下拉列表中高亮选项边框的颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表中高亮选项的边框选择颜色，或指定自定义颜色。

### **Highlight Font Color** — 下拉列表中高亮选项的字体颜色 `[r g b]` 向量

从标准颜色调色板中为下拉列表中高亮的选项选择字体颜色，或指定自定义颜色。

### **Width** — 尖角宽度 标量

将尖角的宽度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Height** — 尖角高度 标量

将尖角的高度指定为标签文本字体高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持尖角宽高比的选项 `on`（默认）| `off`

打开此选项可在使用属性检查器调整尖角大小时保持宽高比。

#### 状态

### **Select State** — 状态标签和值 标量和字符向量

组合框下拉列表中的每个选项对应于 Combo Box 模块的一个状态。状态具有标签和值。**State Label** 值是下拉列表中标识该选项的文本。当您选择某个选项时，Combo Box 模块进入关联的状态，并将 **State Value** 值赋给已连接的参数。

默认情况下，该模块具有三个组合框选项和三个对应的状态。

| State Value | State Label |
| --- | --- |
| `0` | `Label1` |
| `1` | `Label2` |
| `2` | `Label3` |

您可以设计具有任意数量大于或等于 1 的状态的 Combo Box 模块。要添加新状态，请点击 **+** 按钮。要删除状态，请在 **Select State** 部分中，选择该状态。然后，点击 **X** 按钮。

**注意**

当 **Enumerated Data Type** 启用时，您无法添加或删除状态。您可以在属性检查器的 **Parameters** 选项卡中禁用此选项。

要配置状态的标签文本或值，请在 **Select State** 部分中，选择该状态。然后，在 **Value** 和 **Text** 框中输入新值。

**提示**

您还可以使用属性检查器中的 **Parameters** 选项卡配置模块的状态。

### **Value** — 状态值 标量

指定在 **Select State** 部分中所选状态的 **State Value**。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改该值。您可以在属性检查器的 **Parameters** 选项卡中关闭此选项。

### **Text** — 状态标签文本 字符串 | 字符数组

指定在 **Select State** 部分中所选状态的 **State Label** 文本。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改该文本。您可以在属性检查器的 **Parameters** 选项卡中关闭此选项。

#### 背景图像

### **Use Background Color** — 指定纯色模块背景颜色的选项 `off`（默认）| `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink 工具条的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` 向量

要使用纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink 工具条的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间，格式为字符串或字符向量。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** 字符串 | 字符向量 |
| **值：** `[r g b]` 向量 |

### **Opacity** — 模块背景不透明度 `1`（默认）| 标量

将模块背景不透明度指定为 `0` 到 `1` 之间的标量值。

**示例：** `0.5`

### **Corner Radius** — 模块背景颜色区域的圆角半径 标量

将模块背景颜色所覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比例。

**示例：** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 标量

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 标量

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 标量

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 标量

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 保持前景图像宽高比的选项 `on`（默认）| `off`

选择此参数可在使用属性检查器调整图像大小时保持宽高比。
## 所属库

Simulink / Dashboard / Customizable Blocks

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

仪表板模块在代码生成时被忽略。

## 版本历史

**在 R2025a 中引入**

### R2025a：在仿真期间选择仪表板模块并打开模块参数对话框

当 Dashboard 或 Customizable Blocks 库中的 Simulink 模块处于*活动*状态时，您可以与该模块所代表的组件进行交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与该模块本身进行交互。例如，您可以移动或调整模块大小。默认情况下，Dashboard 和 Customizable Blocks 库中的所有模块在仿真期间均处于活动状态。提升到仪表板面板的模块在面板于其自身窗口中打开或停靠且未锁定时也处于活动状态。对于 Callback Button 模块，只要通过按下按钮触发的至少一个回调具有非空值，该模块就始终处于活动状态。要与非活动模块所代表的组件进行交互，您可以通过点击该模块来临时激活它。当您取消选择该模块时，该模块将再次变为非活动状态。

点击活动的 Callback Button 模块或连接到参数或变量值的 Dashboard 或 Customizable Blocks 库中的活动模块，既会选择该模块，也会与该模块所代表的组件进行交互。例如，点击未选中的活动已连接 Push Button 模块既会选择该模块，也会按下按钮。从 R2025a 开始，您可以通过按住 **Shift** 然后点击该模块来选择模块而不与组件进行交互。同样，您可以通过按住 **Shift** 然后双击该模块来打开模块参数对话框。

## 描述

使用具有可自定义外观的组合框在仿真期间更改参数或变量值

使用 Combo Box 模块在仿真之前或仿真期间更改所连接参数或变量的值。当您在 Customizable Blocks 库中使用 Combo Box 模块时，您可以自定义模块的外观，例如，使模块看起来像您正在设计的数字用户界面中的组合框。将 Combo Box 模块与其他仪表板模块一起使用，为您的模型构建由控件和指示器组成的交互式仪表板。

组合框下拉列表中的每个选项对应 Combo Box 模块的一个状态。该状态具有一个标签和一个值。状态标签是下拉列表中标识该选项的文本。当您选择一个选项时，Combo Box 模块进入关联状态，并将状态值赋给所连接的参数。要在仿真期间选择选项，请点击 Combo Box 模块以展开下拉列表，然后选择该选项。要在仿真未运行时选择选项，请点击 Combo Box 模块以选择该模块，再次点击该模块以展开下拉列表，然后选择该选项。

要自定义状态标签或值，请打开属性检查器的 **Parameters** 选项卡或模块参数对话框。

**注意**

- 在仿真期间或点击已连接的 Combo Box 模块后，双击该模块不会打开模块参数对话框。要打开模块参数对话框，请按住 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Combo Box 模块既会选择该模块，也会展开组合框下拉列表。要选择模块而不展开列表，请按住 **Shift**，然后点击该模块。

### 自定义 Combo Box 模块

当您将 Combo Box 模块添加到模型中时，该模块预配置了默认设计。您可以使用默认设计使用该模块，也可以自定义模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定的选项卡上，在 **Design** 下，点击 **Edit**。
- 在属性检查器中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式下，您可以使用模块上方的工具栏来自定义组合框。要访问其他自定义选项或为设计设置输入精确值，请使用属性检查器中的 **Design** 选项卡。

处于设计模式的可自定义 Combo Box 模块，工具栏和属性检查器中的 Design 选项卡可见。

**设计模式操作**

| 操作 | 工具栏中可用 | **Design** 选项卡中可用 |
| --- | --- | --- |
| 更改每个选项赋给所连接参数的值。 | 否 | 是 |
| 更改选项标签的文本。 | 否 | 是 |
| 添加或删除选项。 | 是 | 是 |
| 更改下拉列表的 V 形图标。 | 否 | 是 |
| 更改下拉列表中可见条目的数量。 | 否 | 是 |
| 更改下拉列表的背景色和边框颜色。 | 否 | 是 |
| 更改下拉列表中高亮条目的背景色、边框颜色和字体颜色。 | 否 | 是 |
| 上传背景图像。 | 否 | 是 |
| 设置纯色背景色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号（…）上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。在出现的列表中，选择要连接到的参数。然后，暂停在仪表板模块上，并点击 Done Connecting 按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Combo Box 模块连接到您的模型。

未连接的 Combo Box 模块连接到 Constant 模块。

### 参数记录

连接到仪表板模块的可调参数会记录到仿真数据检查器中，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的一个元素进行访问。
