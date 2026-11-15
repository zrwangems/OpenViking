---
type: simulink-block
title: 'Rotary Switch'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customrotaryswitch'
language: zh-CN
chinese_source: worker-translation
---

# Rotary Switch

## 端口

R2025b 官方文档未提供。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上，于 **Design** 下，选择 **Property Inspector**。

要设置 dashboard 模块的核心参数，请打开 Property Inspector 并点击 **Parameters** 选项卡。

#### Connection

### **Connection** — 模块参数值连接到参数值的连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用 connect mode、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。要从 Property Inspector 打开 Block Parameters 对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。可以连接到具有标量值的参数，也可以连接到矩阵的元素。有关 connect mode 以及如何使用 toolstrip 连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在 Property Inspector 中，于 **Parameters** 选项卡上，点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模块图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模块图。

还可以将 dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### Programmatic Use

要以编程方式将 dashboard 模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将 dashboard 模块连接到由值定义的参数，某些属性适用于将 dashboard 模块连接到由变量定义的参数。并非所有字段都具有连接的值，因为给定 dashboard 模块连接到由值定义的参数或由变量定义的参数之一。

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.ParamSourceInfo` |
| **默认：** `[]` |

#### Main

### **Label** — 显示所连接元素名称的标签位置 `Hide`（默认） | `Bottom` | `Top`

可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏标签。如果希望标签可见，请指定标签位置。如果不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### Programmatic Use

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的纵横比，而是更改背景图像的纵横比以适合模块大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会临时解锁纵横比。释放 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会临时锁定纵横比。释放 **Shift** 键时，纵横比解锁。

### **Enumerated Data Type** — 使用 enumerated data type 指定状态值和标签 `off`（默认） | `on`

可以使用将数值与每个枚举配对的 enumerated data type 来配置模块的状态值和标签。首先，选择 **Enumerated Data Type**。然后，在文本框中指定 enumerated data type 的名称。指定 enumerated data type 的定义必须保存在 MATLAB path 上或 base workspace 中。

**注意**

可以使用 `Simulink.defineIntEnumType` 函数定义 enumerated data type。例如，要为从一到五的一组罗马数字定义 enumerated data type `myEnumType`，请使用以下命令。

```
Simulink.defineIntEnumType('myEnumType',...
    {'I','II','III','IV','V'}, [1 2 3 4 5]);
```

然后，在 Property Inspector 中，于 **Parameters** 选项卡上，在 **Enumerated Data Type** 字段中，输入 `myEnumType`。

#### Programmatic Use

要使用 enumerated data type 以编程方式指定模块的状态标签和值，请将 `UseEnumeratedDataType` 参数的值设置为 `'on'`，并将 `EnumeratedDataType` 参数的值设置为 enumerated data type 的名称。

|  |
| --- |
| **模块参数：** `UseEnumeratedDataType` |
| **类型：** string or character array |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

|  |
| --- |
| **模块参数：** `EnumeratedDataType` |
| **类型：** string or character array |
| **默认：** `''` |

### **States** — 值与标签的配对 scalar 和 character vector

每个状态将 **State Value** 与 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 赋给所连接的变量或参数。可以使用 **State Label** 在模块上显示赋给所连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关具有五个状态，每个开关位置对应一个状态。

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

可以使用可自定义开关模块设计具有任意数量状态且大于或等于 1 的开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **-** 按钮。

**注意**

当 **Enumerated Data Type** 启用时，不能添加或删除状态。

**提示**

也可以在 design mode 中配置状态参数：

1. 选择开关模块。
2. 进入 design mode。在 Property Inspector 中，于 **Design** 选项卡上，点击 **Edit**。
3. 在 **Design** 选项卡上，打开 **States** 组件，展开 **Select State** 部分，然后从下拉菜单中选择要配置的状态。
4. 使用模块上方的工具栏或 Property Inspector 配置所选状态的参数值。

#### Programmatic Use

要以编程方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素且具有以下字段的结构体数组：

- `Value` — 状态的 scalar double 值
- `Label` — 用作开关位置标签的 string 或 character array

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
| **类型：** two element array of structures |

### Design

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### Rotary Switch

### **Lock Aspect Ratio** — 用于保持模块纵横比的选项 `on`（默认） | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持纵横比。

当纵横比锁定时，添加新的背景图像会将模块的纵横比更改为与背景图像的纵横比匹配。当纵横比解锁时，添加新的背景图像不会更改模块的比例，而是拉伸或缩放背景图像以适合模块大小。

当纵横比锁定时，调整模块大小时按 **Shift** 键会解锁纵横比。释放 **Shift** 键时，纵横比锁定。当纵横比解锁时，调整模块大小时按 **Shift** 键会锁定纵横比。释放 **Shift** 键时，纵横比解锁。

### **Arc** — 状态标签跨过的弧长 `300`（默认） | scalar

将状态标签中心点跨过的弧长指定为 scalar 值，以 degrees 测量。

**示例：** `90`

### **Start Angle** — `State 1` 的角度位置 `120`（默认） | scalar

将第一个状态的角度位置指定为 scalar 值，以从指向右侧的水平轴顺时针方向的 degrees 测量。

**示例：** `0`

### **Label Radius** — 标签距模块中心的距离 scalar

将标签距模块中心的距离指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `0.5`

#### States

### **Select State** — 状态的管理和配置 scalar 和 character vector

每个状态将 **State Value** 与 **State Label** 配对。当模块处于给定状态时，它会将该状态的 **State Value** 赋给所连接的变量或参数。可以使用 **State Label** 在模块上显示赋给所连接变量或参数的值，或提供描述性文本标签。

默认情况下，开关具有五个状态，每个开关位置对应一个状态。

| State Value | State Label |
| --- | --- |
| `0` | `Off` |
| `1` | `Low` |
| `2` | `Medium` |
| `3` | `High` |
| `4` | `On` |

可以设计具有任意数量状态且大于或等于 1 的旋转开关。要添加新状态，请点击 **+** 按钮。要删除当前状态，请点击 **X** 按钮。

**注意**

当 **Enumerated Data Type** 打开时，不能添加或删除状态。可以在 Property Inspector 的 **Parameters** 选项卡中禁用此选项。

要配置状态，请在 **States** 组件中展开 **Select State** 部分并选择该状态。

在 Property Inspector 的 **Design** 选项卡上的 **States** 组件中配置所选状态的值和标签文本。

在 **States** 组件中对参数值所做的所有更改仅应用于所选状态。要配置其他状态，请展开 **Select State** 部分并选择该状态。然后，在 **States** 组件中配置该状态的参数值。

**提示**

还可以使用 Property Inspector 中的 **Parameters** 选项卡配置模块的状态。

#### Programmatic Use

要以编程方式配置模块的 **States**，请将 `States` 参数的值指定为包含两个元素且具有两个字段的结构体数组：

- `Value` — 状态的 scalar double 值
- `Label` — 用作开关位置标签的 string 或 character array

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
| **类型：** two element array of structures |

### **Value** — 状态值 scalar

每个状态将 **State Value** 与 **State Label** 配对。指定在 **Design** 选项卡中所选状态的状态值。

**注意**

当 **Enumerated Data Type** 打开时，不能更改该值。可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

### **Text** — 状态标签文本 string | character array

每个状态将 **State Value** 与 **State Label** 配对。指定在 **Design** 选项卡中所选状态 **State Label** 的文本。

**注意**

当 **Enumerated Data Type** 打开时，不能更改文本。可以在 Property Inspector 的 **Parameters** 选项卡中关闭此选项。

#### Handle

### **Width** — 手柄图像宽度 scalar

将手柄图像的宽度指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `1`

### **Height** — 手柄图像高度 scalar

将手柄图像的高度指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `1`

### **Lock Aspect Ratio** — 用于保持图像纵横比的选项 `on`（默认） | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

### **Rotate Image** — 手柄图像的旋转 `0`（默认） | scalar

以 90 degree 增量绕其中心旋转手柄图像。

**示例：** `90`

### **Offset from Center** — 手柄图像中心距模块中心的偏移 `0`（默认） | scalar

将手柄图像中心到模块中心的距离指定为两个模块尺寸（宽度或高度）中较小者的比例。

**示例：** `1`

#### Background Image

### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off`（默认） | `on`

对于模块背景，可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` vector

要选择纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准色调色板中选择背景颜色，或指定自定义颜色。

**提示**

还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Foreground Color**。

#### Programmatic Use

将模块的 `BackgroundColor` 参数指定为定义 `1`-by-`3` `[r g b]` vector 的 string 或 character vector，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** character vector | string |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1`（默认） | scalar

将模块背景不透明度指定为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景颜色的区域外边缘距标签半径的偏移 scalar

将模块背景颜色覆盖区域的外边缘距标签半径的偏移设置为从 `0` 到 `1` 的 scalar 值。

**示例：** `0.1`

#### Foreground Image

### **X Offset** — 前景图像左边缘距模块左边缘的水平偏移 scalar

将图像左边缘距模块左边缘的水平偏移指定为模块宽度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向左移动，正值偏移将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘距模块上边缘的垂直偏移 scalar

将图像上边缘距模块上边缘的垂直偏移指定为模块高度的比例。相对于偏移为 `0` 时图像的位置，负值偏移将图像向上移动，正值偏移将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 scalar

将前景图像的宽度指定为模块宽度的比例。

**示例：** `0.5`

### **Height** — 前景图像高度 scalar

将前景图像的高度指定为模块高度的比例。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像纵横比的选项 `on`（默认） | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持纵横比。

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

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2021b 中引入**

### R2025a: Select dashboard block and open Block Parameters dialog box during simulation

当来自 Dashboard 或 Customizable Blocks 库的 Simulink 模块处于 *active* 状态时，可以与模块所代表的 gadget 交互。例如，可以按下按钮或拨动开关。当模块处于 inactive 状态时，只能与模块交互。例如，可以移动或调整模块大小。默认情况下，来自 Dashboard 和 Customizable Blocks 库的所有模块在仿真期间均处于 active 状态。提升到 dashboard panel 的模块在面板于其自身窗口中打开或停靠且解锁时也处于 active 状态。如果 Callback Button 模块中至少一个由按下按钮触发的回调具有非空值，则该模块始终处于 active 状态。要与 inactive 模块所代表的 gadget 交互，可以通过点击该模块临时激活模块。取消选择模块后，模块再次变为 inactive。

点击 active 的 Callback Button 模块或点击连接到参数或变量值的 active Dashboard 或 Customizable Blocks 库模块，会同时选择该模块并与模块所代表的 gadget 交互。例如，点击未选中的 active 已连接 Push Button 模块会同时选择该模块并按下按钮。从 R2025a 开始，可以通过按 **Shift** 然后点击模块来选择模块而不与 gadget 交互。类似地，可以通过按 **Shift** 然后双击模块来打开 Block Parameters 对话框。

### R2024b: Unlock dashboard block aspect ratio with keyboard

如果来自 Dashboard 库的模块的纵横比已锁定，可以通过按 **Shift** 临时解锁纵横比。释放 **Shift** 键时，纵横比锁定。

如果纵横比已解锁，按 **Shift** 会临时锁定纵横比。释放 **Shift** 键时，纵横比解锁。

### R2024a: Deploy dashboard panel as web app or standalone desktop app

拥有 Simulink Compiler™ 许可证后，现在可以将 dashboard panel（连同其连接的模型一起打包）部署为独立桌面应用或 Web 应用。可以使用该应用操作控件并监视面板上的显示，而不依赖于 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a: Dock dashboard panels

从 R2024a 开始，可以将 dashboard panel 停靠到 Simulink Editor 窗口。可以使用停靠的面板在仿真期间监视信号并控制参数，而不会遮挡画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b: Open panel in new window

从 R2023b 开始，可以在新窗口中打开 dashboard panel。为此，请选择面板并暂停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window 。

可以独立于模型窗口最小化和还原包含面板的新窗口。在面板窗口中，可以运行、暂停、停止和单步执行仿真。在面板窗口中，可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中点击 Open in canvas 。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a: Persistent panels tab in Simulink Toolstrip

将 dashboard panel 添加到模型时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，未选择面板时 **Panels** 选项卡仍保持可见。

**Panels** 选项卡还包含以下新选项：

- 可以添加空面板。
- 可以重命名所选面板。
- 可以隐藏所选面板。

### R2022b: Undo and redo support for customizable dashboard blocks in panel

从 R2022b 开始，可以撤销和重做对面板中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b: Toolstrip support for panels

从 R2022b 开始，可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

点击面板中的 dashboard 模块时，会出现该模块的 toolstrip 选项卡。例如，点击 Circular Gauge 模块时，toolstrip 中会出现 **Gauge** 选项卡。

点击面板时，toolstrip 中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 将所有未隐藏面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2022b: Extended support for customizable Dashboard blocks on Raspberry Pi boards

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持将 **Customizable Blocks** 库中的以下模块部署到 Raspberry Pi 板上：

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

可以在 Simulink 模型中自定义模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022b: Extended support for customizable Dashboard blocks on Android devices

从 R2022b 开始，Simulink Support Package for Android® Devices 支持将 **Customizable Blocks** 库中的以下模块部署到 Android 设备上：

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

可以在 Simulink 模型中自定义模块的视觉方面，并在 Android 设备以及 Web 浏览器上获得所见即所得 (WYSIWYG) 可视化。

### R2022a: Resize and reposition foreground image

Customizable Blocks 库中的模块具有添加前景图像作为模块设计一部分的选项。从 R2022a 开始，可以在模块设计内旋转、调整大小并重新定位前景图像。

## 描述

使用具有可自定义外观的旋转开关更改参数或变量值

使用 Rotary Switch 模块在仿真前或仿真期间更改所连接变量或参数的值。在 Customizable Blocks 库中使用 Rotary Switch 模块时，可以自定义模块外观，使其看起来像系统中的真实旋转开关。将 Rotary Switch 模块与其他 dashboard 模块一起使用，为模型创建交互式 dashboard。

真实旋转开关具有多个设置。Rotary Switch 模块将这些设置视为不同状态。一个状态将状态值与手柄方向、点击区域以及显示在点击区域上的状态标签配对。

要在仿真期间激活某个状态，请点击该状态的点击区域，或将手柄拖动到指向该点击区域。要在仿真未运行时激活某个状态，请点击 Rotary Switch 模块以选择该模块，然后点击点击区域或将手柄拖动到指向该点击区域。激活状态时，状态值将赋给 Rotary Switch 模块所连接的 Simulink® 模块图元素。

所有状态点击区域合起来覆盖手柄从第一个状态移动到最后一个状态时所经过角度范围内的模块区域。状态标签在该范围内均匀分布，第一个标签位于范围起点，最后一个标签位于范围终点。该范围被细分为点击区域，使相邻点击区域的边界平分标签之间的角距离。

下图显示一个具有四个状态的自定义旋转开关。第一个状态和最后一个状态的标签相距 150 degrees。状态标签（顺时针读取）为 A、B、C 和 D。点击区域以四种不同颜色显示。第一个和第四个状态的点击区域跨过的角距离是其他每个状态跨过的角距离的一半。

**注意**

- 在仿真期间双击已连接的 Rotary Switch 模块，或在点击该模块后双击，不会打开 Block Parameters 对话框。要打开 Block Parameters 对话框，请按 **Shift**，然后双击该模块。
- 在仿真期间点击已连接的 Rotary Switch 模块会同时选择该模块并移动开关手柄。要选择该模块而不移动开关手柄，请按 **Shift**，然后点击该模块。

### Customize Rotary Switch Blocks

将 Rotary Switch 模块添加到模型时，该模块预配置有默认设计。可以使用默认设计使用该模块，也可以自定义模块外观。

要自定义模块外观，请使用 design mode。选择模块后，可以通过以下三种方式之一进入 design mode：

- 在 Simulink Toolstrip 中，在模块特定的选项卡上，于 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中，在 **Design** 选项卡上，点击 **Edit**。
- 暂停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮 。

在 design mode 中，可以使用模块上方的工具栏自定义旋转开关。要访问其他自定义选项或输入设计设置的精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于 design mode 的 Customizable Rotary Switch 模块，其中工具栏和 Property Inspector 中的 Design 选项卡可见。

自定义 Rotary Switch 模块时，需要为每个状态配置模块外观。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。要添加状态，请在工具栏中点击 Add State 按钮 。要删除状态，请点击 Remove State 按钮 。

**自定义所选状态的 Design Mode 操作**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Specify the state value. | No | Yes |
| Specify the state label text. | No | Yes |
| Add or remove states. | Yes | Yes |
| Upload a handle image. | Yes | Yes |
| Change the size of the handle. | No | Yes |
| Change the position the handle. | No | Yes |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，还可以在画布中以交互方式调整组件大小和位置。手柄的移动限制在穿过模块中心且沿 **Start Angle** 的直线上。

要更改状态标签的颜色，请在 **Format** 选项卡上，于 **Style** 下，点击 **Foreground** 按钮上的箭头并选择颜色。可以从标准色调色板中选择，或点击 Custom Colors 按钮 指定自定义颜色。

**适用于所有状态的 Design Mode 操作**

| Action | Available in Toolbar | Available in **Design** Tab |
| --- | --- | --- |
| Change the arc length spanned by the state labels. | No | Yes, in the **Rotary Switch** component |
| Change the start angle of the arc. | No | Yes, in the **Rotary Switch** component |
| Change the label radius. | No | Yes, in the **Rotary Switch** component |
| Upload a background image. | Yes | Yes |
| Set a solid background color. | No | Yes |
| Upload a foreground image. | No | Yes |

完成设计编辑后，要退出 design mode，请点击画布右上角的 **X**。

### Connect Dashboard Blocks

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用 connect mode。要在未连接的模块上进入 connect mode，请暂停在要连接的模块上并点击 Connect 按钮 。要在已连接的模块上进入 connect mode，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入 connect mode。选择要连接其参数的模块。在出现的列表中，选择要连接到的参数。然后，暂停在 dashboard 模块上并点击 Done Connecting 按钮 。

在更新模块图之前，控制模块无法连接到由变量定义的参数。要连接到由变量定义的参数，或在仿真未运行时修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模块图。

可以连接到具有标量值的参数，也可以连接到矩阵或结构的元素。有关详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

还可以将 dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Rotary Switch 模块连接到模型。

未连接的 Rotary Switch 模块连接到 Constant 模块。

### Parameter Logging

连接到 dashboard 模块的可调参数会记录到 Simulation Data Inspector，可以在其中查看参数值以及记录的信号数据。可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的详细信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素访问。
