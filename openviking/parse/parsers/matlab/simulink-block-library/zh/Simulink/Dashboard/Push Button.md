---
type: simulink-block
title: 'Push Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'pushbutton'
documentation_source_path: 'slref/pushbutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Push Button

## 端口

R2025b 中未记录。

## 参数

### 连接

### **Connection** — 用于连接参数值的模块参数值连接选项

仪表模块不使用端口连接到模型元素。要将仪表模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的 **Connection** 表。要从属性检查器打开“模块参数”对话框，请在 **Connected to** 右侧点击 **Connect** 或 **Change**。您可以连接到具有标量值的参数，或连接到矩阵的元素。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表将控制模块连接到具有标量值的参数，或更改控制模块与具有标量值的参数的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接其参数值的模块。
4. 在表中，选择要连接到的参数。
5. 点击 **Apply**。

在更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数，或修改定义已连接参数值的变量的值，请按 **Ctrl+D** 更新模型图。

您还可以将仪表模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程使用

要以编程方式将仪表模块连接到可调参数，请使用 `Simulink.HMI.ParamSourceInfo` 对象。`Simulink.HMI.ParamSourceInfo` 对象包含四个属性。某些属性适用于将仪表模块连接到由值定义的参数，某些属性适用于将仪表模块连接到由变量定义的参数。并非所有字段都有连接值，因为给定的仪表模块要么连接到由值定义的参数，要么连接到由变量定义的参数。

|  |
| --- |
| **模块参数**：`Binding` |
| **类型**：`Simulink.HMI.ParamSourceInfo` |
| **默认值**：`[]` |

### 主要

### **Button Text** — 按钮的文本标签 `Button`（默认）| 字符串 | 字符向量

在模型中 Push Button 模块上显示的文本。

#### 提示

要设计一个根据模块状态显示不同文本的按钮，请使用 Customizable Blocks 库中的 Push Button 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`ButtonText` |
| **类型**：string or character array |
| **默认值**：`'Button'` |

### **On Value** — 按下或锁存按钮时分配给已连接参数的值 `1`（默认）| 标量

按下或锁存按钮时分配给已连接模块参数的值。

#### 提示

使用 **Block Type** 参数配置模块如何响应点击：

- `Momentary` — 按钮仅在您按下它时应用 **On Value**。
- `Latch` — 按钮在您点击它时锁存状态变化并应用 **On value**，直到您再次点击它。

#### 编程使用

|  |
| --- |
| **模块参数**：`OnValue` |
| **类型**：string or character array |
| **默认值**：`'1'` |

### **Button Type** — 按钮对点击的响应 `Momentary`（默认）| `Latch`

指定按钮如何响应点击。

- `Momentary` — 按钮仅在您按下它时应用 **On Value**。
- `Latch` — 按钮在您点击它时锁存状态变化并应用 **On value**，直到您再次点击它。

#### 编程使用

|  |
| --- |
| **模块参数**：`ButtonType` |
| **类型**：string or character array |
| **Value:** `'Momentary'` | `'Latch'` |

### **Label** — 模块标签位置 `Hide`（默认）| `Bottom` | `Top`

模块标签的位置。当模块连接到模型中的元素时，标签为已连接元素的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：character vector |
| **值**：`'Hide'` | `'Bottom'` | `'Top'` |
| **默认值**：`'Hide'` |

### 格式

### **Opacity** — 模块背景不透明度 `1`（默认）| 标量

模块背景不透明度，指定为 0 到 1 之间的标量值。

**示例：** `0.5`

#### 编程使用

|  |
| --- |
| **模块参数**：`Opacity` |
| **类型**：scalar |
| **默认值**：`1` |

### **Foreground Color** — 模块前景色 `[r g b]` 向量

模块前景色，包括文本。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程使用

将模块的 `ForegroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ForegroundColor` |
| **类型**：character vector | string |
| **值**：`[r g b]` vector |

### **Background Color** — 模块背景色 `[r g b]` 向量

模块背景色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 编程使用

将模块的 `BackgroundColor` 参数指定为字符串或字符向量，该字符串或字符向量定义一个 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`BackgroundColor` |
| **类型**：character vector | string |
| **值**：`[r g b]` vector |

### 图标

### **Icon** — 在按钮上显示的图标 SVG 文件 | PNG 文件 | JPEG 文件

您可以向 Push Button 模块添加图标，以在按钮文本旁边或代替按钮文本显示。您可以从内置的形状、汽车和无线图标中选择，也可以上传自己的自定义 SVG、PNG 或 JPEG 文件作为图标使用。

要查看图标选项，请在模块对话框的 **Icon** 选项卡上选择一个 **Icon Type**。要使用自己的自定义图标，请选择 `Custom` 作为 **Icon Type** 并上传图像文件。

添加图标后，您可以使用以下参数配置图标外观：

- **Icon Alignment** — 图标相对于按钮文本的对齐方式
- **On Color** — 模块被按下或锁存并向已连接参数应用 **On value** 时的图标颜色
- **Off Color** — 模块未被按下或锁存且未向已连接参数应用 **On value** 时的图标颜色

要为图标指定 **On Color** 和 **Off Color**，您必须选择 **Customize Icon Color**。

**形状图标**

| 图标 | Basic Shapes Library 模块名称 | Programmatic Use 值 |
| --- | --- | --- |
| Check1 图标：一个对勾 | Check1 | `Check1` |
| Check2 图标：一个线条略微弯曲的对勾 | Check2 | `Check2` |
| Check3 图标：一个对勾的轮廓 | Check3 | `Check3` |
| Check4 图标：一个轮廓上有凹痕的对勾 | Check4 | `Check4` |
| Circle 图标：一个实心黑色圆形 | Circle | `Circle` |
| Ex1 图标：一个叉号 | Ex1 | `Ex1` |
| Ex2 图标：一个有一条曲线线条的叉号 | Ex2 | `Ex2` |
| Ex3 图标：一个叉号的轮廓 | Ex3 | `Ex3` |
| Ex4 图标：一个轮廓上有凹痕的叉号 | Ex4 | `Ex4` |
| Face 图标：一张闭嘴呈直线的脸的轮廓 | Face | `Face` |
| Frown1 图标：一张张嘴向下弯的脸的轮廓 | Frown1 | `Frown1` |
| Frown2 图标：一张闭嘴向下弯的脸的轮廓 | Frown2 | `Frown2` |
| Hexagon 图标：一个实心六边形 | Hexagon | `Hexagon` |
| Pentagon 图标：一个实心五边形 | Pentagon | `Pentagon` |
| Rectangle 图标：一个实心矩形 | Rectangle | `Rectangle` |
| Smile1 图标：一张张嘴向上弯的脸的轮廓 | Smile1 | `Smile1` |
| Smile2 图标：一张闭嘴向上弯的脸的轮廓 | Smile2 | `Smile2` |
| Solid Face 图标：一张闭嘴呈直线的实心脸 | Solid Face | `SolidFace` |
| Solid Frown1 图标：一张张嘴向下弯的实心脸 | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 图标：一张闭嘴向下弯的嘴 | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 图标：一张张嘴向上弯的实心脸 | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 图标：一张闭嘴向上弯的实心脸 | Solid Smile2 | `SolidSmile2` |
| Square 图标：一个实心正方形 | Square | `Square` |
| Triangle 图标：一个实心三角形 | Triangle | `Triangle` |

**汽车图标**

| 图标 | Automotive Indicator Lamps Library 模块名称 | Programmatic Use 值 |
| --- | --- | --- |
| Adaptive Cruise Control 图标：一个速度表，箭头指向一个刻度线，背景中有汽车的轮廓 | Adaptive Cruise Control | `AdaptiveCruiseControl` |
| Adaptive Cruise Control Failure 图标：一个速度表，旁边有一个感叹号，背景中有汽车的轮廓 | Adaptive Cruise Control Failure | `AdaptiveCruiseControlFailure` |
| Anti-Lock Brake System 图标：一个在一对括号中标有“ABS”的圆形 | Antilock Brake System | `AntilockBrakeSystem` |
| Battery 图标：一个电池的轮廓，正极上有加号符号，负极上有负号符号 | Battery | `Battery` |
| Check Engine 图标：一个标有“Check Engine”的发动机轮廓 | Check Engine | `CheckEngine` |
| Check Engine2 图标：一个发动机的轮廓，上面有避雷针的轮廓，下方有“CHECK”字样 | Check Engine2 | `CheckEngine2` |
| Cruise Control 图标：一个速度表，箭头指向其中一个刻度线 | Cruise Control | `CruiseControl` |
| Eco Mode 图标：一个标有“ECO”的实心叶子形状 | Eco Mode | `EcoMode` |
| Electronic Stability 图标：一个在一对括号中标有“ESP”的圆形 | Electronic Stability | `ElectronicStability` |
| Engine 图标：一个发动机的轮廓 | Engine | `Engine` |
| Engine Coolant Temp 图标：一个温度计，背景中有波浪 | Engine Coolant Temp | `EngineCoolantTemp` |
| Engine Failure 图标：一个发动机的轮廓，上面有一个感叹号 | Engine Failure | `EngineFailure` |
| Engine Heating 图标：一个发动机的轮廓，上面有三个向上的波浪形箭头 | Engine Heating | `EngineHeating` |
| Engine Oil 图标：一个油壶的轮廓 | Engine Oil | `EngineOil` |
| Exterior Bulb Failure 图标：一个发光的灯泡的轮廓，上面有一个感叹号 | Exterior Bulb Failure | `ExteriorBulbFailure` |
| Front Fog Light 图标：一个雾灯灯的轮廓，向左发出光线，光线表示为斜线，位于代表雾的波浪形垂直线之上 | Front Fog Light | `FrontFogLight` |
| Fuel 图标：一个加油泵的轮廓，上面有一个向左的箭头 | Fuel | `Fuel` |
| Hazards 图标：一个警告三角形的轮廓 | Hazards | `Hazards` |
| Headlamp Leveling 图标：一个灯的轮廓，发出光线，上方有一个顺时针方向的箭头，下方有一个逆时针方向的箭头 | Headlamp Leveling | `HeadlampLeveling` |
| High Beams 图标：一个灯的轮廓，发出水平光线 | High Beams | `HighBeams` |
| Hill Descent Control 图标：一辆汽车下坡行驶的轮廓 | Hill Descent Control | `HillDescentControl` |
| Lighting Switch 图标：一个发光的灯泡的轮廓 | Lighting Switch | `LightingSwitch` |
| High Beams 图标：一个灯的轮廓，发出斜向下延伸的光线 | Low Beams | `LowBeams` |
| Parking Assistance 图标：字母“P”旁边有一个实心三角形，“P”发出检测信号，表示为三条指向三角形的曲线 | Parking Assistance | `ParkingAssistance` |
| Rear Fog Light 图标：一个雾灯灯的轮廓，向右发出光线，光线表示为水平线，位于代表雾的波浪形垂直线之上 | Rear Fog Light | `RearFogLight` |
| Side Lights 图标：两个灯的轮廓，向左和向右发出光线 | Side Lights | `SideLights` |
| Stability Control 图标：一辆汽车后面有波浪线的轮廓 | Stability Control | `StabilityControl` |
| Stability Control Off 图标：一辆汽车后面有波浪线的轮廓，下方有“OFF”字样 | Stability Control Off | `StabilityControlOff` |
| Tire Monitor 图标：一个轮胎横截面的轮廓，上面有一个感叹号 | Tire Monitor | `TireMonitor` |
| Traction Control 图标：一个轮胎横截面的轮廓，标有“TC” | Traction Control | `TractionControl` |
| Traction Control Off 图标：一个轮胎横截面的轮廓，标有“TC”，整个图像上有一条对角斜线 | Traction Control Off | `TractionControlOff` |
| Traction Control Failure 图标：一个轮胎横截面的轮廓，标有“TC”，旁边有一个感叹号 | Traction Control Failure | `TractionControlFailure` |
| Turn Signal Left 图标：一个指向左侧的实心箭头 | Turn Signal Left | `TurnSignalLeft` |
| Turn Signal Right 图标：一个指向右侧的实心箭头 | Turn Signal Right | `TurnSignalRight` |

**无线图标**

| 图标 | 图标名称 | Programmatic Use 值 |
| --- | --- | --- |
| Network 图标：无线互联网连接图标 | Network | `Network` |
| Network No Signal 图标：无线互联网连接图标变灰，旁边有一个带叉的圆形 | Network No Signal | `NetworkNoSignal` |
| Network Transmission 图标：一个无线互联网信号塔 | Network Transmission | `NetworkTransmission` |
| Network3G 图标：无线互联网连接图标，旁边有“3G” | Network3G | `Network3G` |
| Network4G 图标：无线互联网连接图标，旁边有“4G” | Network4G | `Network4G` |
| Network5G 图标：无线互联网连接图标，旁边有“4G” | Network5G | `Network5G` |

#### 提示

- 您可以使用工具条中的 **Button** 选项卡更改 Push Button 模块的图标。
- 如果您想进一步自定义 Push Button 模块的外观，请考虑使用 Customizable Blocks 库中的 Push Button 模块设计自己的按钮。

  Customizable Blocks 库中的 Push Button 模块支持添加自定义图标，但不包含任何内置图标。
- 图标的开和关颜色可以应用于以下 SVG 元素：

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

#### 编程使用

|  |
| --- |
| **模块参数**：`Icon` |
| **类型**：string | character vector |
| **默认值**：`'Default'` |

### **Icon Alignment** — 图标相对于按钮文本的对齐方式 `Left`（默认）| `Right` | `Top` | `Bottom` | `Center`

图标相对于按钮文本的对齐方式。当您未指定按钮文本时，图标始终位于模块的中心。

#### 编程使用

|  |
| --- |
| **模块参数**：`IconAlignment` |
| **类型**：string | character vector |
| **Value:** `'Left'` | `'Right'` | `'Top'` | `'Bottom'` | `'Center'` |
| **默认值**：`'Left'` |

### **Customize Icon Color** — 是否使用图标开和关颜色 `Off`（默认）| `On`

当您向 Push Button 模块添加图标时，可以指定开和关颜色，使图标颜色变化以反映模块的状态。要使用并指定图标的 **On Color** 和 **Off Color**，请选择 **Customize Icon Color**。

#### 编程使用

|  |
| --- |
| **模块参数**：`IconColor` |
| **类型**：string | character vector |
| **Value:** `'On'` | `'Off'` |
| **默认值**：`'Off'` |

### **On Color** — 按下或锁存模块时的图标颜色 `[r g b]` 向量

当您为 Push Button 模块添加图标时，可以指定开启和关闭颜色，使图标颜色随模块状态变化。**On Color** 指定当模块被按下或锁存并向所连接的参数应用 **On value** 时图标的颜色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 依赖关系

要启用 **On Color** 参数，请选择 **Customize Icon Color**。

#### 编程使用

将模块的 `IconOnColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`IconOnColor` |
| **类型**：`[r g b]` vector |

### **Off Color** — 模块未按下或未锁存时的图标颜色 `[r g b]` 向量

当您为 Push Button 模块添加图标时，可以指定开启和关闭颜色，使图标颜色随模块状态变化。**Off Color** 指定当模块未被按下或未锁存且未向所连接的参数应用 **On value** 时图标的颜色。您可以从标准颜色调色板中选择颜色，或指定自定义颜色。

#### 依赖关系

要启用 **On Color** 参数，请选择 **Customize Icon Color**。

#### 编程使用

将模块的 `IconOffColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`IconOffColor` |
| **类型**：`[r g b]` vector |

## 所属库

Simulink / Dashboard

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

**在 R2015a 中引入**

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开仪表板面板。为此，请选择该面板并暂停在出现的省略号上。在展开的操作菜单中，点击 **Open In New Window** 按钮。

您可以独立于模型窗口最小化和恢复包含该面板的新窗口。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口的工具条中点击 **Open in canvas**。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink Toolstrip 中的持久面板选项卡

当您向模型添加仪表板面板时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选中面板时可见。从 R2023a 开始，当未选择任何面板时，**Panels** 选项卡保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：对面板中可自定义仪表板模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义仪表板模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的工具条支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的仪表板模块。

当您点击面板中的仪表板模块时，该模块的工具条选项卡会出现。例如，当您点击 Circular Gauge 模块时，工具条中会出现 **Gauge** 选项卡。

当您点击面板时，工具条中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适应当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2021b：Push Button 模块可在您释放点击后应用值

从 R2021b 开始，您可以配置 Push Button 模块的行为，使其在您点击模块时锁存或瞬时应用 **On Value**。

### R2021b：Push Button 模块可显示图标

从 R2021b 开始，您可以添加图标以显示在 Push Button 模块上，与按钮文本并排显示或替代按钮文本。您可以从预定义集合中为模块选择图标，或使用模块对话框或工具条的 **Button** 选项卡上传您自己的自定义图标。

您还可以指定开启颜色和关闭颜色，使图标颜色随模块状态变化，并指定图标相对于按钮文本的对齐方式。

### R2021a：使用仪表板模块调整矩阵和结构体元素

从 R2021a 开始，您可以将 Dashboard 库中的模块连接到矩阵或结构体的标量元素，该元素定义了可调模块参数的值。当您将仪表板模块连接到可调参数时，首先选择一个或多个模块。然后，在对话框中，选择要连接的参数。当您选择具有非标量值的参数时，使用对话框中的文本框指定要调整的元素。

### R2020b：为多个仪表板模块添加了 **Background Color**、**Foreground Color** 和 **Opacity** 属性

从 R2020b 开始，您可以为 Dashboard 库中的以下模块指定背景颜色、前景颜色和不透明度：

- Check Box
- Combo Box
- Edit
- Push Button
- Radio Button

### R2020b：Simulink Toolstrip 对仪表板模块的支持

从 R2020b 开始，当您在模型中选择来自 Simulink 库中的 Dashboard 库或来自 Aerospace Blockset™ Flight Control Analysis 库中的 Flight Instruments 库的模块时，Simulink Toolstrip 中的 **Block** 选项卡会变为特定于该模块的选项卡。您可以从工具条连接、断开连接和修改所选模块的连接。您可以跳转到连接到所选模块的模型元素，并且可以将所选模块添加到面板。

### R2019a：以编程方式添加和配置仪表板模块

从 R2019a 开始，您可以使用 `add_block` 和 `set_param` 等函数在模型中创建和配置 Dashboard 库中的模块。

## 描述

使用按钮更改参数或变量值

使用 Push Button 模块在仿真之前或期间更改所连接变量或参数的值。您可以将按钮配置为仅在按下按钮时更改值，或锁存值更改直到再次点击按钮。将 Push Button 模块与其他 Dashboard 模块一起使用，以创建交互式仪表板来控制您的模型。

在仿真期间或模块被选中时，双击 Push Button 模块不会打开其对话框。要编辑模块参数，您可以使用 **Property Inspector**，或通过以下方式打开模块对话框：

- 在模块未被选中且模型未进行仿真时双击模块。
- 右键点击模块，然后从上下文菜单中选择 **Block Parameters**。

### Push Button 图标

您可以向 Push Button 模块添加图标，该图标显示在按钮文本旁边。您可以从包含基本形状、汽车指示器和无线图标的预定义集合中选择图标，也可以上传您自己的自定义图标。有关更多信息，包括内置图标的完整列表，请参阅 Icon。

当您为 Push Button 模块添加图标时，您可以为图标配置开启颜色和关闭颜色，使其颜色随模块状态变化，并指定图标相对于按钮文本的对齐方式。例如，此 Push Button 模块配置为使用圆形图标，开启颜色指定为亮绿色，对齐到按钮文本的左侧。

按钮文本左侧带有绿色圆形图标的按钮模块。

Push Button 模块的图标设置允许您配置模块在模型中的外观。当您想要进一步自定义模块外观时，请考虑使用 Customizable Blocks 库中的 Push Button 模块。Customizable Blocks 库中的 Push Button 模块支持添加自定义图标，但不包含任何内置图标。

### 连接仪表板模块

仪表板模块不使用端口连接到模型元素。要连接仪表板模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后点击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将控制模块连接到模型中的参数或更改控制模块的连接，请进入连接模式。选择要将其参数连接到的模块。从出现的列表中，选择要连接到的参数。然后，暂停在仪表板模块上，并点击 Done Connecting 按钮。

在您更新模型图之前，控制模块无法连接到由变量定义的参数。要在仿真未运行时连接到由变量定义的参数或修改定义所连接参数值的变量值，请按 **Ctrl+D** 更新模型图。

您可以连接到具有标量值的参数，或连接到矩阵或结构体的元素。有关更多信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将仪表板模块连接到 Stateflow® 图。有关更多信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Push Button 模块连接到您的模型。

一个未连接的 Push Button 模块连接到 Constant 模块的 Value 参数。

### 参数记录

连接到仪表板模块的可调参数会记录到 Simulation Data Inspector，您可以在其中查看参数值以及记录的信号数据。您可以通过使用 UI 或 `Simulink.sdi.exportRun` 函数从 Simulation Data Inspector 导出参数数据，从而在 MATLAB® 工作区中访问记录的参数数据。有关使用 Simulation Data Inspector UI 导出数据的更多信息，请参阅 Export Data to Workspace or File。参数数据存储在 `Simulink.SimulationData.Parameter` 对象中，可作为导出的 `Simulink.SimulationData.Dataset` 中的元素进行访问。
