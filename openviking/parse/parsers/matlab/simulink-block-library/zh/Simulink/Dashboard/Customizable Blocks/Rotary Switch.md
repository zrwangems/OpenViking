---
type: simulink-block
title: 'Rotary Switch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard / Customizable Blocks'
documentation_page: 'customrotaryswitch'
documentation_source_path: 'slref/customrotaryswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotary Switch

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Connection
  summary: 用于连接参数值的模块参数值 连接选项
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
  summary: 用于保持模块宽高比的选项 on（默认）| off
  group: 参数
- name: Enumerated Data Type
  summary: 使用枚举数据类型指定状态值和标签 off（默认）| on
  group: 参数
  block_parameter: EnumeratedDataType
  type: 字符串或字符数组
  values: '''on'' | ''off'''
  default: ''''''
- name: States
  summary: 值与标签的配对 标量和字符向量
  group: 参数
  block_parameter: States
  type: 两个元素的结构体数组
- name: Lock Aspect Ratio
  summary: 用于保持模块宽高比的选项 on（默认）| off
  group: 设计
- name: Arc
  summary: 状态标签所跨越的弧长 300（默认）| 标量
  group: 设计
- name: Start Angle
  summary: State 1 的角度位置 120（默认）| 标量
  group: 设计
- name: Label Radius
  summary: 标签距模块中心的距离 标量
  group: 设计
- name: Select State
  summary: 状态的管理和配置 标量和字符向量
  group: 设计
  block_parameter: States
  type: 两个元素的结构体数组
- name: Value
  summary: 状态值 标量
  group: 设计
- name: Text
  summary: 状态标签文本 字符串 | 字符数组
  group: 设计
- name: Width
  summary: 手柄图像宽度 标量
  group: 设计
- name: Height
  summary: 手柄图像高度 标量
  group: 设计
- name: Lock Aspect Ratio
  summary: 用于保持图像宽高比的选项 on（默认）| off
  group: 设计
- name: Rotate Image
  summary: 手柄图像的旋转 0（默认）| 标量
  group: 设计
- name: Offset from Center
  summary: 手柄图像中心距模块中心的偏移 0（默认）| 标量
  group: 设计
- name: Use Background Color
  summary: 用于指定纯色模块背景色的选项 off（默认）| on
  group: 设计
- name: Color
  summary: 模块背景颜色 [r g b] 向量
  group: 设计
  block_parameter: BackgroundColor
  type: 字符向量 | 字符串
  values: '[r g b] 向量'
- name: Opacity
  summary: 模块背景不透明度 1（默认）| 标量
  group: 设计
- name: Corner Radius
  summary: 模块背景色覆盖区域外边缘距标签半径的偏移 标量
  group: 设计
- name: X Offset
  summary: 前景图像左边缘距模块左边缘的水平偏移 标量
  group: 设计
- name: Y Offset
  summary: 前景图像顶边相对于模块顶边的垂直偏移量 标量
  group: 设计
- name: Width
  summary: 前景图像宽度 标量
  group: 设计
- name: Height
  summary: 前景图像高度 标量
  group: 设计
- name: Lock Aspect Ratio
  summary: 用于保持前景图像宽高比的选项 on（默认）| off
  group: 设计
```

使用属性检查器和模块参数对话框指定模块参数的值。要设置仪表板模块的核心参数，请使用模块参数对话框或属性检查器中的**参数**选项卡。要自定义模块，请使用属性检查器中的**设计**选项卡。要打开模块的模块参数对话框，请双击该模块。要打开属性检查器，请在**建模**选项卡的**设计**下，选择**属性检查器**。

### 参数

要设置仪表板模块的核心参数，请打开属性检查器并点击**参数**选项卡。

#### 连接

### **Connection** — 用于连接参数值的模块参数值 连接选项

仪表板模块不使用端口连接到模型元素。要将仪表板模块连接到模型中的参数值，请使用连接模式、Simulink 工具条或模块参数对话框中的 **Connection** 表。要从属性检查器打开模块参数对话框，请在 **Connected to** 右侧，点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的**参数**选项卡中，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将仪表板模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将仪表板模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将仪表板模块连接到由值定义的参数，某些属性适用于将仪表板模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的仪表板模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认值：** `[]` |

#### 主要

### **Label** — 显示已连接元素名称的标签位置 `Hide`（默认）| `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示仪表板模块所连接元素的名称，也可以隐藏该标签。如果希望标签可见，请指定标签的位置。如果不希望标签可见，请选择 `Hide`。

**注意**

当仪表板模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** 字符向量 |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的宽高比，而是更改背景图像的宽高比以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。释放 **Shift** 键时，宽高比解锁。

### **Enumerated Data Type** — 使用枚举数据类型指定状态值和标签 `off`（默认）| `on`

您可以使用将数值与每个枚举配对的枚举数据类型来配置模块的状态值和标签。首先，选择 **Enumerated Data Type**。然后，在文本框中指定枚举数据类型的名称。指定的枚举数据类型的定义必须保存在 MATLAB 路径上或基础工作区中。

**注意**

您可以使用 `Simulink.defineIntEnumType` 函数定义枚举数据类型。例如，要为从一到五的一组罗马数字定义枚举数据类型 `myEnumType`，请使用以下命令。

```
Simulink.defineIntEnumType('myEnumType',...
    {'I','II','III','IV','V'}, [1 2 3 4 5]);
```

然后，在属性检查器的**参数**选项卡中，在 **Enumerated Data Type** 字段中，输入 `myEnumType`。

#### 编程用法

要使用枚举数据类型以编程方式指定模块的状态标签和值，请将 `UseEnumeratedDataType` 参数的值设置为 `'on'`，并将 `EnumeratedDataType` 参数的值设置为枚举数据类型的名称。

|  |
| --- |
| **模块参数：** `UseEnumeratedDataType` |
| **类型：** 字符串或字符数组 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

|  |
| --- |
| **模块参数：** `EnumeratedDataType` |
| **类型：** 字符串或字符数组 |
| **默认值：** `''` |

### **States** — 值与标签的配对 标量和字符向量

每个状态将一个 **State Value** 与一个 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 分配给已连接的变量或参数。您可以使用 **State Label** 在模块上显示分配给已连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关有五个状态，每个状态对应一个开关位置。

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

您可以使用可自定义的开关模块设计具有任意数量大于或等于 1 的状态的开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **-** 按钮。

**注意**

当 **Enumerated Data Type** 启用时，您无法添加或删除状态。

**提示**

您还可以在设计模式下配置状态的参数：

1. 选择开关模块。
2. 进入设计模式。在属性检查器的**设计**选项卡中，点击 **Edit**。
3. 在**设计**选项卡中，打开 **States** 组件，展开 **Select State** 部分，然后从下拉菜单中选择要配置的状态。
4. 使用模块上方的工具栏或属性检查器配置所选状态的参数值。

#### 编程用法

要以编程方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素的结构体数组，这些元素具有以下字段：

- `Value` — 状态的标量双精度值
- `Label` — 用作开关位置标签的字符串或字符数组

```
firstState.Value = 0;
firstState.Label = 'Off';
secondState.Value = 1;
secondState.Label = 'On';
switchStates = [firstState secondState];
```

|  |
| --- |
| **模块参数：** `States` |
| **类型：** 两个元素的结构体数组 |

### 设计

要自定义仪表板模块，请打开属性检查器，点击**设计**选项卡，然后点击 **Edit**。

#### Rotary Switch

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on`（默认）| `off`

选择此参数以在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块的大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。释放 **Shift** 键时，宽高比锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会锁定宽高比。释放 **Shift** 键时，宽高比解锁。

### **Arc** — 状态标签所跨越的弧长 `300`（默认）| 标量

将状态标签中心点所跨越的弧长指定为标量值，以度为单位。

**示例：** `90`

### **Start Angle** — `State 1` 的角度位置 `120`（默认）| 标量

将第一个状态的角度位置指定为标量值，以从指向右侧的水平轴顺时针测量的度数为单位。

**示例：** `0`

### **Label Radius** — 标签距模块中心的距离 标量

将标签距模块中心的距离指定为模块两个尺寸（宽度或高度）中较小者的比率。

**示例：** `0.5`

#### 状态

### **Select State** — 状态的管理和配置 标量和字符向量

每个状态将一个 **State Value** 与一个 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 分配给已连接的变量或参数。您可以使用 **State Label** 在模块上显示分配给已连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关有五个状态，每个状态对应一个开关位置。

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

您可以设计具有任意数量大于或等于 1 的状态的旋转开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **X** 按钮。

**注意**

当 **Enumerated Data Type** 打开时，您无法添加或删除状态。您可以在属性检查器的**参数**选项卡中禁用此选项。

要配置状态，请在 **States** 组件中，展开 **Select State** 部分并选择该状态。

在属性检查器**设计**选项卡的 **States** 组件中配置所选状态的值和标签文本。

您在 **States** 组件中对参数值所做的所有更改仅应用于所选状态。要配置不同的状态，请展开 **Select State** 部分并选择该状态。然后，在 **States** 组件中配置该状态的参数值。

**提示**

您还可以使用属性检查器中的**参数**选项卡配置模块的状态。

#### 编程用法

要以编程方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素的结构体数组，这些元素具有两个字段：

- `Value` — 状态的标量双精度值
- `Label` — 用作开关位置标签的字符串或字符数组

```
firstState.Value = 0;
firstState.Label = 'Off';
secondState.Value = 1;
secondState.Label = 'On';
switchStates = [firstState secondState];
```

|  |
| --- |
| **模块参数：** `States` |
| **类型：** 两个元素的结构体数组 |

### **Value** — 状态值 标量

每个状态将一个 **State Value** 与一个 **State Label** 配对。指定在**设计**选项卡中选择的状态的 **State Value**。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改该值。您可以在属性检查器的**参数**选项卡中关闭此选项。

### **Text** — 状态标签文本 字符串 | 字符数组

每个状态将一个 **State Value** 与一个 **State Label** 配对。指定在**设计**选项卡中选择的状态的 **State Label** 文本。

**注意**

当 **Enumerated Data Type** 打开时，您无法更改文本。您可以在属性检查器的**参数**选项卡中关闭此选项。

#### 手柄

### **Width** — 手柄图像宽度 标量

将手柄图像的宽度指定为模块两个尺寸（宽度或高度）中较小者的比率。

**示例：** `1`

### **Height** — 手柄图像高度 标量

将手柄图像的高度指定为模块两个尺寸（宽度或高度）中较小者的比率。

**示例：** `1`

### **Lock Aspect Ratio** — 用于保持图像宽高比的选项 `on`（默认）| `off`

选择此参数以在使用属性检查器调整图像大小时保持宽高比。

### **Rotate Image** — 手柄图像的旋转 `0`（默认）| 标量

以 90 度为增量绕其中心旋转手柄图像。

**示例：** `90`

### **Offset from Center** — 手柄图像中心距模块中心的偏移 `0`（默认）| 标量

将手柄图像中心到模块中心的距离指定为模块两个尺寸（宽度或高度）中较小者的比率。

**示例：** `1`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景色的选项 `off`（默认）| `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink 工具条的**格式**选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` 向量

要选择纯色背景，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink 工具条的**格式**选项卡中指定 **Background Color**。

要指定模块文本的颜色，请在 Simulink 工具条的**格式**选项卡中，指定 **Foreground Color**。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** 字符向量 | 字符串 |
| **值：** `[r g b]` 向量 |

### **Opacity** — 模块背景不透明度 `1`（默认）| 标量

将模块背景不透明度指定为 `0` 到 `1` 之间的标量值。

**示例：** `0.5`

### **Corner Radius** — 模块背景色覆盖区域外边缘距标签半径的偏移 标量

设置模块背景色覆盖区域外边缘距标签半径的偏移，指定为 `0` 到 `1` 之间的标量值。

**示例：** `0.1`

#### 前景图像

### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 标量

将图像左边缘距模块左边缘的水平偏移指定为模块宽度的比率。相对于偏移为 `0` 时图像的位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像顶边相对于模块顶边的垂直偏移量 标量

将图像顶边相对于模块顶边的垂直偏移量指定为模块高度的比例。相对于偏移量为 `0` 时的图像位置，负值偏移量将图像向上移动，正值将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 标量

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 标量

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on`（默认）| `off`

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

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2021b 中引入**

### R2025a：在仿真期间选择 dashboard 模块并打开模块参数对话框

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于*活动*状态时，您可以与该模块所代表的小工具进行交互。例如，您可以按下按钮或拨动开关。当模块处于非活动状态时，您只能与模块本身进行交互。例如，您可以移动或调整模块大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间均处于活动状态。提升到 dashboard 面板的模块在面板于其自身窗口中打开或停靠且未锁定时也处于活动状态。Callback Button 模块中，如果按下按钮触发的至少一个回调具有非空值，则该模块始终处于活动状态。要与非活动模块所代表的小工具进行交互，您可以通过点击该模块来临时激活它。当您取消选择该模块时，该模块将再次变为非活动状态。

点击活动的 Callback Button 模块或来自 Dashboard 或 Customizable Blocks 库且连接到参数或变量值的活动模块，会同时选择该模块并与该模块所代表的小工具进行交互。例如，点击未选中的活动已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，您可以通过按住 **Shift** 然后点击模块来选择模块而不与小工具进行交互。同样，您可以通过按住 **Shift** 然后双击模块来打开模块参数对话框。

### R2024b：使用键盘解锁 dashboard 模块宽高比

如果来自 Dashboard 库的模块的宽高比已锁定，您可以通过按住 **Shift** 临时解锁宽高比。当您释放 **Shift** 键时，宽高比将锁定。

如果宽高比已解锁，按住 **Shift** 会临时锁定宽高比。当您释放 **Shift** 键时，宽高比将解锁。

### R2024a：将 dashboard 面板部署为 Web 应用或独立桌面应用

拥有 Simulink Compiler™ 许可证后，您现在可以将 dashboard 面板与其所连接的模型一起打包，部署为独立桌面应用或 Web 应用。您可以使用该应用来操作控件并监视面板上的显示，而无需依赖 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window 。

您可以将包含面板的新窗口与模型窗口分开最小化和还原。从面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口的工具条中点击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink 工具条中的持久面板选项卡

当您将 dashboard 面板添加到模型时，Simulink 工具条中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，**Panels** 选项卡在未选中面板时也保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：对面板中可自定义 dashboard 模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command**（⌘）而不是 **Ctrl**。

### R2022b：工具条对面板的支持

从 R2022b 开始，您可以使用 Simulink 工具条来管理和编辑面板及其包含的 dashboard 模块。

当您点击面板中的 dashboard 模块时，该模块的工具条选项卡会出现。例如，当您点击 Circular Gauge 模块时，**Gauge** 选项卡会出现在工具条中。

当您点击面板时，**Panel** 选项卡会出现在工具条中。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适应当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 为所选面板添加新选项卡。

### R2022b：在 Raspberry Pi 板上对可自定义 Dashboard 模块的扩展支持

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持在您的 Raspberry Pi 板上部署来自 **Customizable Blocks** 库的以下模块：

- Horizontal Gauge
- Horizontal Slider
- Lamp
- Push Button
- Rocker Switch
- Rotary Switch
- Slider Switch
- Toggle Switch
- Vertical Gauge
- Vertical Slider

您可以在 Simulink 模型中自定义模块的视觉外观，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得（WYSIWYG）的可视化效果。

### R2022b：在 Android 设备上对可自定义 Dashboard 模块的扩展支持

从 R2022b 开始，Simulink Support Package for Android® Devices 支持在您的 Android 设备上部署来自 **Customizable Blocks** 库的以下模块：

- Horizontal Gauge
- Horizontal Slider
- Lamp
- Push Button
- Rocker Switch
- Rotary Switch
- Slider Switch
- Toggle Switch
- Vertical Gauge
- Vertical Slider

您可以在 Simulink 模型中自定义模块的视觉外观，并在您的 Android 设备以及 Web 浏览器上获得所见即所得（WYSIWYG）的可视化效果。

### R2022a：调整前景图像大小和位置

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整大小和重新定位前景图像。

## 描述

使用具有可自定义外观的旋转开关更改参数或变量值

使用 Rotary Switch 模块在仿真之前或仿真期间更改所连接变量或参数的值。当您在 Customizable Blocks 库中使用 Rotary Switch 模块时，您可以自定义模块的外观，使其看起来像您系统中的真实旋转开关。将 Rotary Switch 模块与其他 dashboard 模块一起使用，为您的模型创建交互式 dashboard。

真实的旋转开关具有多个设置。Rotary Switch 模块将这些设置视为不同的状态。一个状态将状态值与手柄方向、点击区域以及显示在点击区域上的状态标签配对。

要在仿真期间激活某个状态，请点击该状态的点击区域或将手柄拖动到指向该点击区域。要在仿真未运行时激活某个状态，请点击 Rotary Switch 模块以选择该模块，然后点击点击区域或将手柄拖动到指向该点击区域。当您激活该状态时，状态值将分配给 Rotary Switch 模块所连接的 Simulink® 模块图元素。

所有状态的点击区域共同覆盖模块中手柄从第一个状态移动到最后一个状态时所经过的角度范围内的区域。状态标签在该范围内均匀分布，第一个标签位于范围的起点，最后一个标签位于范围的终点。该范围被细分为点击区域，使得相邻点击区域的边界平分标签之间的角度距离。

该图像显示了一个具有四个状态的自定义旋转开关。第一个状态和最后一个状态的标签相距 150 度。状态标签（顺时针读取）为 A、B、C 和 D。点击区域以四种不同颜色显示。第一个和第四个状态的点击区域所跨越的角度距离是其他每个状态所跨越角度距离的一半。

**注意**

- 在仿真期间双击已连接的 Rotary Switch 模块或在点击该模块后双击，不会打开模块参数对话框。要打开模块参数对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Rotary Switch 模块会同时选择该模块并移动开关手柄。要选择模块而不移动开关手柄，请按 **Shift**，然后点击该模块。

### 自定义 Rotary Switch 模块

当您将 Rotary Switch 模块添加到模型时，该模块预配置有默认设计。您可以使用默认设计的模块，也可以自定义模块的外观。

要自定义模块的外观，请使用设计模式。选择模块后，您可以通过以下三种方式之一进入设计模式：

- 在 Simulink 工具条中，在模块特定选项卡的 **Design** 下，点击 **Edit**。
- 在属性检查器中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在设计模式中，您可以使用模块上方的工具栏来自定义旋转开关。要访问其他自定义选项或输入设计设置的精确值，请使用属性检查器中的 **Design** 选项卡。

处于设计模式的可自定义 Rotary Switch 模块，工具栏和属性检查器中的 Design 选项卡可见。

当您自定义 Rotary Switch 模块时，您为每个状态配置模块外观。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。要添加状态，请在工具栏中点击 Add State 按钮 。要删除状态，请点击 Remove State 按钮 。

**自定义所选状态的设计模式操作**

| 操作 | 工具栏中可用 | **Design** 选项卡中可用 |
| --- | --- | --- |
| 指定状态值。 | 否 | 是 |
| 指定状态标签文本。 | 否 | 是 |
| 添加或删除状态。 | 是 | 是 |
| 上传手柄图像。 | 是 | 是 |
| 更改手柄的大小。 | 否 | 是 |
| 更改手柄的位置。 | 否 | 是 |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件的大小和位置。手柄的移动被限制在通过模块中心且位于 **Start Angle** 的直线上。

要更改状态标签的颜色，请在 **Format** 选项卡的 **Style** 下，点击 **Foreground** 按钮上的箭头并选择一种颜色。您可以从标准颜色调色板中选择，或点击 Custom Colors 按钮 来指定自定义颜色。

**适用于所有状态的设计模式操作**

| 操作 | 工具栏中可用 | **Design** 选项卡中可用 |
| --- | --- | --- |
| 更改状态标签所跨越的弧长。 | 否 | 是，在 **Rotary Switch** 组件中 |
| 更改弧的起始角度。 | 否 | 是，在 **Rotary Switch** 组件中 |
| 更改标签半径。 | 否 | 是，在 **Rotary Switch** 组件中 |
| 上传背景图像。 | 是 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号（…）上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。从出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上，并点击 Done Connecting 按钮 。

在您更新模型图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义已连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，也可以连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示了如何将 Rotary Switch 模块连接到您的模型。

未连接的 Rotary Switch 模块连接到 Constant 模块。

### 参数记录

连接到 dashboard 模块的可调参数会记录到仿真数据检查器中，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。
