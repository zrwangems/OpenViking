---
type: simulink-block
title: 'Push Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Dashboard'
documentation_page: 'pushbutton'
documentation_source_path: 'slref/pushbutton.html'
language: zh-CN
chinese_source: official
---

# Push Button

## 端口

R2025b 官方文档未提供。

## 参数

### 连接

### **连接** — 要连接的模块参数值 参数值连接选项

Dashboard 模块不使用端口来连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的**连接**表。要从属性检查器打开“模块参数”对话框，请在**连接到**的右侧，点击**连接**或**更改**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅Connect Dashboard Blocks to Simulink Model。

使用**连接**表将控制模块连接到带标量值的参数，或将控制模块连接更改为带标量值的参数：

1. 选择模块。
2. 要连接该模块，请在属性检查器的**参数**选项卡上点击**连接**。要更改模块的连接，请改为点击**更改**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接的参数。
5. 点击**应用**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数或修改定义所连接的参数值的变量值，请按 **Ctrl+D** 更新模型图。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

要以编程方式将 Dashboard 模块连接到可调参数或变量，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。有些属性适用于将 Dashboard 模块连接到由值定义的参数，有些属性适用于将 Dashboard 模块连接到由变量定义的参数。并非所有字段都有连接值，因为一个给定的 Dashboard 模块可以连接到由值定义的参数或由变量定义的参数。

|  |
| --- |
| **模块参数**：`Binding` |
| **类型：**`Simulink.HMI.ParamSourceInfo` |
| **默认值：**`[]` |

### 常设

### **按钮文本** — 按钮的文本标签 `Button` (默认) | 字符串 | 字符向量

模型中的 Push Button 模块上显示的文本。

#### 提示

要设计根据模块的状态显示不同文本的普通按钮，请使用 Customizable Blocks 库中的 Push Button 模块。

#### 编程用法

|  |
| --- |
| **模块参数**：`ButtonText` |
| **类型：**字符串或字符数组 |
| **默认值**：`'Button'` |

### **打开值** — 当按下或锁存按钮时赋给所连接的参数的值 `1` (默认) | 标量

当按下或锁存按钮时赋给所连接的模块参数的值。

#### 提示

使用**模块类型**参数配置模块如何响应点击：

- **瞬时** - 按钮仅在按下时应用**打开值**。
- **锁存** - 在点击按钮时按钮会锁存状态变化，并在您再次点击之前一直应用**打开值**。

#### 编程用法

|  |
| --- |
| **模块参数**：`OnValue` |
| **类型：**字符串或字符数组 |
| **默认值：**`'1'` |

### **按钮类型** — 按钮对点击的响应 **瞬时** (默认) | **锁存**

指定按钮如何响应点击。

- **瞬时** - 按钮仅在按下时应用**打开值**。
- **锁存** - 在点击按钮时按钮会锁存状态变化，并在您再次点击之前一直应用**打开值**。

#### 编程用法

|  |
| --- |
| **模块参数**：`ButtonType` |
| **类型：**字符串或字符数组 |
| **值**：`'Momentary'` | `'Latch'` |

### **标签** — 模块标签位置 `Hide` (默认) | `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接的元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型：**字符向量 |
| **值：**`'Hide'` | `'Bottom'` | `'Top'` |
| **默认值**：`'Hide'` |

### 格式

### **不透明度** — 模块背景不透明度 `1` (默认) | 标量

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例:** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：**`Opacity` |
| **类型：**标量 |
| **默认值：**`1` |

### **前景颜色** — 模块前景颜色 `[r g b]` 向量

模块前景颜色，包括文本。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

#### 编程用法

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型：**字符向量 | 字符串 |
| **值：**`[r g b]` 向量 |

### **背景颜色** — 模块的背景色。 `[r g b]` 向量

模块的背景色。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该向量定义 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型：**字符向量 | 字符串 |
| **值：**`[r g b]` 向量 |

### 图标

### **图标** — 按钮上显示的图标 SVG 文件 | PNG 文件 | JPEG 文件

您可以向 Push Button 模块添加显示在按钮文本旁边或代替按钮文本的图标。您可以从内置形状、汽车图标和无线图标中进行选择，也可以上传您自己的自定义 SVG、PNG 或 JPEG 文件用作图标。

要查看图标选项，请在模块对话框的**图标**选项卡上选择**图标类型**。要使用您自己的自定义图标，请选择**自定义**作为**图标类型**，并上传图像文件。

添加图标时，可以使用以下参数配置图标外观：

- **图标对齐方式** - 图标相对于按钮文本的对齐方式
- **打开颜色** - 按下或锁存模块并将**打开值**应用于所连接的参数时的图标颜色
- **关闭颜色** - 当未按下或锁存模块且未将**打开值**应用于所连接的参数时的图标颜色

要为图标指定**打开颜色**和**关闭颜色**，您必须选择**自定义图标颜色**。

**形状图标**

| 图标 | 基本形状库模块名称 | 编程使用的值 |
| --- | --- | --- |
| Check1 icon: a check mark | Check1 | `Check1` |
| Check2 icon: a check mark with slightly curved lines | Check2 | `Check2` |
| Check3 icon: the outline of a check mark | Check3 | `Check3` |
| Check4 icon: a check mark with a divot along its outline | Check4 | `Check4` |
| Circle icon: a solid black circle | Circle | `Circle` |
| Ex1 icon: a cross mark | Ex1 | `Ex1` |
| Ex2 icon: a cross mark with one curved line | Ex2 | `Ex2` |
| Ex3 icon: the outline of a cross mark | Ex3 | `Ex3` |
| Ex4 icon: a cross mark with a divot along the outline | Ex4 | `Ex4` |
| Face icon: the outline of a face with a closed mouth in a straight line | Face | `Face` |
| Frown1 icon: the outline of a face with an open downturned mouth | Frown1 | `Frown1` |
| Frown2 icon: the outline of a face with a closed downturned mouth | Frown2 | `Frown2` |
| Hexagon icon: a solid hexagon | Hexagon | `Hexagon` |
| Pentagon icon: a solid pentagon | Pentagon | `Pentagon` |
| Rectangle icon: a solid rectangle | Rectangle | `Rectangle` |
| Smile1 icon: the outline of a face with an open upturned mouth | Smile1 | `Smile1` |
| Smile2 icon: the outline of a face with a closed upturned mouth | Smile2 | `Smile2` |
| Solid Face icon: a solid face with a closed mouth in a straight line | Solid Face | `SolidFace` |
| Solid Frown1 icon: a solid face with an open downturned mouth | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 icon: a closed downturned mouth | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 icon: a solid face with an open upturned mouth | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 icon: a solid face with a closed upturned mouth | Solid Smile2 | `SolidSmile2` |
| Square icon: a solid square | Square | `Square` |
| Triangle icon: a solid triangle | Triangle | `Triangle` |

**汽车图标**

| 图标 | 汽车指示灯库模块名称 | 编程使用的值 |
| --- | --- | --- |
| Adaptive Cruise Control icon: a speedometer with an arrow pointing to a tick mark and the silhouette of a car in the background | Adaptive Cruise Control | `AdaptiveCruiseControl` |
| Adaptive Cruise Control Failure icon: a speedometer with an exclamation mark next to it and the silhouette of a car in the background | Adaptive Cruise Control Failure | `AdaptiveCruiseControlFailure` |
| Anti-Lock Brake System icon: a circle labeled "ABS" in a set of parentheses | Antilock Brake System | `AntilockBrakeSystem` |
| Battery icon: the outline of a battery with a plus symbol on the positive pole, and a negative symbol on the negative pole | Battery | `Battery` |
| Check Engine icon: the outline of an engine labeled "Check Engine" | Check Engine | `CheckEngine` |
| Check Engine2 icon: the outline of an engine with the silhouette of a lightning rod on it and the word "CHECK" underneath it | Check Engine2 | `CheckEngine2` |
| Cruise Control icon: a speedometer with an arrow pointing to one of the tick marks | Cruise Control | `CruiseControl` |
| Eco Mode icon: a solid leaf shape labeled "ECO" | Eco Mode | `EcoMode` |
| Electronic Stability icon: a circle labeled "ESP" in a set of parentheses | Electronic Stability | `ElectronicStability` |
| Engine icon: the silhouette of an engine | Engine | `Engine` |
| Engine Coolant Temp icon: a thermometer with waves in the background | Engine Coolant Temp | `EngineCoolantTemp` |
| Engine Failure icon: the silhouette of an engine with an exclamation mark on it | Engine Failure | `EngineFailure` |
| Engine Heating icon: the silhouette of an engine with three wavy arrows pointing upwards on it | Engine Heating | `EngineHeating` |
| Engine Oil icon: the silhouette of an oil can | Engine Oil | `EngineOil` |
| Exterior Bulb Failure icon: the silhouette of a glowing light bulb with an exclamation mark on it | Exterior Bulb Failure | `ExteriorBulbFailure` |
| Front Fog Light icon: the outline of a fog light lamp emitting rays of light to the left that are depicted as diagonal lines on top of a wavy vertical line that represents the fog | Front Fog Light | `FrontFogLight` |
| Fuel icon: the silhouette of a gas pump with an arrow pointing left on it | Fuel | `Fuel` |
| Hazards icon: the outline of a warning triangle | Hazards | `Hazards` |
| Headlamp Leveling icon: the outline of a lamp emitting rays of light with an arrow pointing clockwise above them and an arrow pointing counterclockwise below them | Headlamp Leveling | `HeadlampLeveling` |
| High Beams icon: the outline of a lamp emitting horizontal rays of light | High Beams | `HighBeams` |
| Hill Descent Control icon: the outline of a car driving down a slope | Hill Descent Control | `HillDescentControl` |
| Lighting Switch icon: the silhouette of a glowing light bulb | Lighting Switch | `LightingSwitch` |
| High Beams icon: the outline of a lamp emitting rays of light that run diagonally downward | Low Beams | `LowBeams` |
| Parking Assistance icon: the letter "P" next to a solid triangle, and the "P" emits a detection signal represented as three curved lines aimed at the triangle | Parking Assistance | `ParkingAssistance` |
| Rear Fog Light icon: the outline of a fog light lamp emitting rays of light to the right that are depicted as horizontal lines on top of a wavy vertical line that represents the fog | Rear Fog Light | `RearFogLight` |
| Side Lights icon: the outline two lamps emitting rays of light to the left and right | Side Lights | `SideLights` |
| Stability Control icon: the silhouette of a car with wavy lines behind it | Stability Control | `StabilityControl` |
| Stability Control Off icon: the silhouette of a car with wavy lines behind it and the word "OFF" underneath | Stability Control Off | `StabilityControlOff` |
| Tire Monitor icon: the outline of the cross-section of a tire with an exclamation mark on it | Tire Monitor | `TireMonitor` |
| Traction Control icon: the outline of the cross-section of a tire with the label "TC" | Traction Control | `TractionControl` |
| Traction Control Off icon: the outline of the cross-section of a tire with the label "TC" and a diagonal slash through the whole image | Traction Control Off | `TractionControlOff` |
| Traction Control Failure icon: the outline of the cross-section of a tire with the label "TC" and an exclamation mark next to it | Traction Control Failure | `TractionControlFailure` |
| Turn Signal Left icon: a solid arrow pointing left | Turn Signal Left | `TurnSignalLeft` |
| Turn Signal Right icon: a solid arrow pointing right | Turn Signal Right | `TurnSignalRight` |

**无线图标**

| 图标 | 图标名称 | 编程使用的值 |
| --- | --- | --- |
| Network icon: the wireless internet connection icon | Network | `Network` |
| Network No Signal icon: the wireless internet connection icon grayed out,with a crossed-out circle next to it | Network No Signal | `NetworkNoSignal` |
| Network Transmission icon: a wireless internet tower | Network Transmission | `NetworkTransmission` |
| Network3G icon: the wireless internet connection icon with "3G" next to it | Network3G | `Network3G` |
| Network4G icon: the wireless internet connection icon with "4G" next to it | Network4G | `Network4G` |
| Network5G icon: the wireless internet connection icon with "4G" next to it | Network5G | `Network5G` |

#### 提示

- 您可以使用工具条中的**按钮**选项卡更改 Push Button 模块的图标。
- 如果您要进一步自定义 Push Button 模块的外观，请考虑使用 Customizable Blocks 库中的 Push Button 模块设计您自己的按钮。

  Customizable Blocks 库中的 Push Button 模块支持添加自定义图标，但不包含任何内置图标。
- 图标的打开颜色和关闭颜色可以应用于以下 SVG 元素：

  - `altGlyph`
  - `circle`
  - `ellipse`
  - `path`
  - `polygon`
  - `rect`
  - `text`
  - `textPath`
  - `tref`
  - `tspan`

#### 编程用法

|  |
| --- |
| **模块参数**：`Icon` |
| **类型：**字符串 | 字符向量 |
| **默认值：**`'Default'` |

### **图标对齐方式** — 图标相对于按钮文本的对齐方式 **左侧** (默认) | **右侧** | **顶端** | **底端** | **居中**

图标相对于按钮文本的对齐方式。如果不指定按钮文本，图标将始终位于模块的中心。

#### 编程用法

|  |
| --- |
| **模块参数**：`IconAlignment` |
| **类型：**字符串 | 字符向量 |
| **值**：`'Left'` | `'Right'` | `'Top'` | `'Bottom'` | `'Center'` |
| **默认值**：`'Left'` |

### **自定义图标颜色** — 是否使用图标的打开颜色和关闭颜色 **off** (默认) | **on**

当您向 Push Button 模块添加图标时，您可以指定打开颜色和关闭颜色，以使图标颜色发生变化来反映模块的状态。要使用并指定图标的**打开颜色**和**关闭颜色**，请选择**自定义图标颜色**。

#### 编程用法

|  |
| --- |
| **模块参数**：`IconColor` |
| **类型：**字符串 | 字符向量 |
| **值**：`'On'` | `'Off'` |
| **默认值**：`'Off'` |

### **打开颜色** — 按下或锁存模块时的图标颜色 `[r g b]` 向量

当您向 Push Button 模块添加图标时，您可以指定打开颜色和关闭颜色，以使图标颜色发生变化来反映模块的状态。**打开颜色**指定按下或锁存模块并将**打开值**应用于所连接的参数时图标的颜色。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

#### 依赖关系

要启用**打开颜色**参数，请选择**自定义图标颜色**。

#### 编程用法

将模块的 `IconOnColor` 参数指定为 `1`×`3` `[r g b]` 向量，其值介于 `0` 到 `1` 之间。

|  |
| --- |
| **模块参数**：`IconOnColor` |
| **类型：**`[r g b]` 向量 |

### **关闭颜色** — 未按下或锁存模块时的图标颜色 `[r g b]` 向量

当您向 Push Button 模块添加图标时，您可以指定打开颜色和关闭颜色，以使图标颜色发生变化来反映模块的状态。**关闭颜色**指定未按下或锁存模块且未将**打开值**应用于所连接的参数时图标的颜色。您可以从标准颜色调色板中选择一种颜色，也可以指定自定义颜色。

#### 依赖关系

要启用**打开颜色**参数，请选择**自定义图标颜色**。

#### 编程用法

将模块的 `IconOffColor` 参数指定为 `1`×`3` `[r g b]` 向量，其值介于 `0` 到 `1` 之间。

|  |
| --- |
| **模块参数**：`IconOffColor` |
| **类型：**`[r g b]` 向量 |

## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

Dashboard 模块在代码生成中会被忽略。

## 版本历史

**在 R2015a 中推出**

### R2023b: 在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。要打开它，请先选择面板并将鼠标暂停在出现的省略号上。在展开的操作菜单中，点击**在新窗口中打开**按钮 。

您可以单独最小化和还原包含面板的新窗口，而不影响模型窗口。您可以通过面板窗口运行、暂停、停止和逐步运行仿真。在面板窗口中，您可以编辑面板及其中包含的模块。

要将面板返回到模型画布，请在面板窗口工具条中，点击**在画布中打开** 。

有关在新窗口中打开面板的详细信息，请参阅Open Panels in New Window。

### R2023a: Simulink 工具条中的持久面板选项卡

向模型添加仪表板面板时，**面板**选项卡会出现在 Simulink 工具条中，并显示用于管理和编辑面板的选项。

在之前的版本中，**面板**选项卡仅在面板选中时可见。从 R2023a 开始，即使没有选择面板时，**面板**选项卡仍保持可见。

**面板**选项卡也包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b: 面板中的可自定义 Dashboard 模块支持撤消和重做操作

从 R2022b 开始，您可以撤消和重做对面板中的可自定义 Dashboard 模块所做的更改。

要撤消或重做更改，请执行以下操作：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤消更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷方式基于 Windows®。在 Mac 上，按 **command** (⌘) 代替 **Ctrl**。

### R2022b: 对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink 工具条来管理和编辑面板及其中包含的 Dashboard 模块。

点击面板中的 Dashboard 模块时，将显示该模块的工具条选项卡。例如，当您点击 Circular Gauge 模块时，**仪表**选项卡会出现在工具条中。

当您点击某个面板时，工具条中会出现**面板**选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 调整所有未隐藏的面板以适应当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2021b: Push Button 模块可以在您点击后应用值

从 R2021b 开始，您可以配置 Push Button 模块的行为，以在点击该模块时锁存或立即应用**打开值**。

### R2021b: Push Button 模块可以显示图标

从 R2021b 开始，您可以在 Push Button 模块上添加图标，显示在按钮文本旁边或代替按钮文本。从预定义的图标集中为模块选择一个图标，或使用模块对话框或工具条的**按钮**选项卡上传您自己的自定义图标。

您还可以指定一种打开颜色和一种关闭颜色，以便其颜色随着模块的状态而变化，并指定图标相对于按钮文本的对齐方式。

### R2021a: 使用 Dashboard 模块调节矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到定义可调模块参数值的矩阵或结构体的标量元素。当您将 Dashboard 模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中选择要连接的参数。当选择具有非标量值的参数时，使用对话框中的文本框指定要调节的元素。

### R2020b: 为几个 Dashboard 模块添加**背景颜色**、**前景颜色**和**不透明度**属性

从 R2020b 开始，您可以从 Dashboard 库中为以下模块指定背景颜色、前景颜色和不透明度：

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b: Simulink 工具条对 Dashboard 模块的支持

从 R2020b 开始，当您从 Simulink 库中的 Dashboard 库中或从 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库中选择模型中的某个模块时，Simulink 工具条中的**模块**选项卡会变为特定于模块的选项卡。从工具条中，可以连接、断开连接和修改所选模块的连接。您可以跳转至连接到所选模块的模型元素，也可以将所选模块添加到面板中。

### R2019a: 以编程方式添加和配置 Dashboard 模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数从模型中的 Dashboard 库创建和配置模块。

## 描述

使用按钮更改参数或变量值

在仿真之前或仿真期间，使用 Push Button 模块更改所连接的变量或参数的值。您可以将按钮配置为仅在按下按钮时更改值，或在再次点击按钮前锁存值变化。将 Push Button 模块与其他 Dashboard 模块结合使用，可以创建交互式仪表板来控制您的模型。

在仿真期间或 Push Button 模块处于选中状态时，双击该模块不会打开其对话框。要编辑模块参数，您可以使用**属性检查器**或通过以下方式打开模块对话框：

- 当未选择模块且模型未仿真时，双击模块。
- 右键点击模块并从上下文菜单中选择**模块参数**。

### 普通按钮图标

您可以向 Push Button 模块添加图标，它会显示在普通按钮文本旁边。您可以从包括基本形状、汽车指示灯和无线图标的预定义集中选择一个图标，也可以上传自己的自定义图标。有关详细信息，包括内置图标的完整列表，请参阅图标。

当您向 Push Button 模块添加图标时，您可以为图标配置一种打开颜色和一种关闭颜色，以便其颜色随着模块的状态而变化，并指定图标相对于普通按钮文本的对齐方式。例如，下图中的 Push Button 模块配置为使用圆形图标，且将表示打开状态的颜色指定为亮绿色，图标与按钮文本的左侧对齐。

Push button block with a green circle icon to the left of the button text.

您可以使用 Push Button 模块的图标设置在模型中配置模块的外观。如果您要进一步自定义模块的外观，请考虑使用 Customizable Blocks 库中的 Push Button 模块。Customizable Blocks 库中的 Push Button 模块支持添加自定义图标，但不包含任何内置图标。

### 连接 Dashboard 模块

Dashboard 模块不使用端口来连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标在要连接的模块上暂停并点击连接按钮 。要在已连接的模块上进入连接模式，请选择该模块，在显示的省略号 (…) 上暂停，然后在展开的操作菜单中点击连接按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入连接模式。选择要连接到其参数的模块。从出现的列表中，选择要连接的参数。然后，请在 Dashboard 模块上悬停并点击完成连接按钮 。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数或修改定义所连接的参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关详细信息，请参阅Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画说明如何将 Push Button 模块连接到您的模型。

An unconnected Push Button block connects to the Value parameter of a constant block.

### 参数记录

连接到 Dashboard 模块的可调参数数据会记录到仿真数据检查器，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从仿真数据检查器导出参数数据来访问 MATLAB® 工作区中记录的参数数据。有关使用仿真数据检查器 UI 导出数据的详细信息，请参阅将数据导出到工作区或文件。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素来访问。
