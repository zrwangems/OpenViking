---
type: simulink-block
title: 'Lamp'
family: customizable-blocks
documentation_release: R2025b
official_category: 'Customizable Blocks'
documentation_page: 'customlamp'
language: zh-CN
chinese_source: worker-translation
---

# Lamp

## 端口

R2025b 官方文档未提供。

## 参数

使用 Property Inspector 和 Block Parameters 对话框指定模块参数的值。要设置 dashboard 模块的核心参数，请使用 Block Parameters 对话框或 Property Inspector 中的 **Parameters** 选项卡。要自定义模块，请使用 Property Inspector 中的 **Design** 选项卡。要打开模块的 Block Parameters 对话框，请双击该模块。要打开 Property Inspector，请在 **Modeling** 选项卡上的 **Design** 下，选择 **Property Inspector**。

要设置 dashboard 模块的核心参数，请打开 Property Inspector，然后点击 **Parameters** 选项卡。

#### 信号

### **Connection** — 要连接的信号以及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink Toolstrip 或 Block Parameters 对话框中的 **Connection** 表。有关连接模式以及如何使用 toolstrip 连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接模块，请在 Property Inspector 的 **Parameters** 选项卡上点击 **Connect**。要更改模块的连接，请改为点击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **Apply**。

您也可以将 dashboard 模块连接到 Stateflow chart。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认值：** `[]` |

#### 主要

### **Label** — 显示所连接元素名称的标签位置 `Hide` (默认) | `Bottom` | `Top`

您可以在位于模块顶部或底部的标签中显示 dashboard 模块所连接元素的名称，也可以隐藏该标签。如果您希望标签可见，请指定标签的位置。如果您不希望标签可见，请选择 `Hide`。

**注意**

当 dashboard 模块未连接到元素时，标签为空白。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Hide'` | `'Bottom'` | `'Top'` |
| **默认值：** `'Hide'` |

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的宽高比，而是会更改背景图像的宽高比以适合模块大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会临时解锁宽高比。当您松开 **Shift** 键时，宽高比会锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会临时锁定宽高比。当您松开 **Shift** 键时，宽高比会解锁。

#### 状态

### **Specify State Values as Ranges** — 用于指定激活状态的值的范围的选项 `off` (默认) | `on`

您可以指定激活 Lamp 模块状态的信号值范围。选择 **Specify State Values as Ranges**，并指定激活每个状态的值范围的最小值和最大值。

#### 编程用法

要以编程方式指定每个状态是由信号值激活还是由信号值范围激活，请将 `StateValueType` 参数指定为 string 或 character vector。要使用信号值激活每个状态，请将 `StateValueType` 设置为 `"Discrete"`。要使用信号值范围激活每个状态，请将 `StateValueType` 设置为 `"Range"`。

|  |
| --- |
| **模块参数：** `StateValueType` |
| **类型：** character vector | string |
| **值：** `"Discrete"` | `"Range"` |
| **默认值：** `"Discrete"` |

### **States** — Lamp 颜色与信号值的配对 标量和 `[r g b]` 向量

状态将 Lamp 颜色与所连接信号的值配对。每个状态由 **Value** 和 **Color** 组成。

- **Value** — 使 Lamp 模块显示指定颜色的所连接信号值或信号值范围。要指定值范围，请选择 **Specify State Values as Ranges**，并指定激活每个状态的值范围的最小值和最大值。
- **Color** — 当所连接信号值与对应的 **State** 值匹配时的 Lamp 颜色。您可以从标准颜色调色板中选择，也可以使用 `RGB` 值指定自定义颜色。

`[undefined]` 状态指定当所连接信号值与 **States** 表中指定的任何值都不匹配时 Lamp 模块的颜色。点击 **+** 按钮可添加另一个状态。

#### 编程用法

要以编程方式指定 Lamp 模块的 `Value` 和 `Color` 参数值，请使用包含以下字段的结构体数组：

- `Value` — 标量 `double` 信号值，或指定使 Lamp 模块显示指定颜色指示的 `double` 信号值范围的最小值和最大值的向量。

  **注意**

  指定向量会启用 **Specify State Values as Ranges** 选项。
- `Color` — `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间，指定 Lamp 模块要显示的颜色。

    lampState1.Value = [1 2];
    lampState1.Color = [0 0 1];
    lampState2.Value = [2 3];
    lampState2.Color = [1 0 0];
    lampStates = [lampState1 lampState2];

|  |
| --- |
| **模块参数：** `StateColors` |
| **类型：** structure array |
| **默认值：** structure |

`ColorDefault` 参数指定当所连接信号的值与任何指定的状态值都不匹配时 Lamp 模块的颜色。请将 `ColorDefault` 参数指定为 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ColorDefault` |
| **类型：** `[r g b]` vector |
| **默认值：** `[0.7529 0.7529 0.7529]` |

### Design

要自定义 dashboard 模块，请打开 Property Inspector，点击 **Design** 选项卡，然后点击 **Edit**。

#### Lamp

### **Lock Aspect Ratio** — 用于保持模块宽高比的选项 `on` (默认) | `off`

选择此参数可在 Simulink 画布中调整模块大小时保持宽高比。

当宽高比锁定时，添加新的背景图像会将模块的宽高比更改为与背景图像的宽高比匹配。当宽高比未锁定时，添加新的背景图像不会更改模块的比例，而是会拉伸或缩放背景图像以适合模块大小。

当宽高比锁定时，在调整模块大小时按 **Shift** 键会解锁宽高比。当您松开 **Shift** 键时，宽高比会锁定。当宽高比未锁定时，在调整模块大小时按 **Shift** 键会锁定宽高比。当您松开 **Shift** 键时，宽高比会解锁。

#### 状态

### **Select State** — 选择要配置的状态 标量和 `[r g b]` 向量

从 **States** 组件的 **Select State** 部分的下拉菜单中选择要配置的状态。您可以使用可自定义的 Lamp 模块设计具有任意数量状态（大于或等于 1）的灯。点击 **+** 可添加另一个状态。点击 **X** 可删除当前状态。

状态将显示颜色与所连接信号的值匹配。每个状态由 **State** 和 **Color** 组成。

- **State** — 使 Lamp 模块显示指定颜色的所连接信号值或信号值范围。要指定值范围，请选择 **Specify State Values as Ranges**，并指定激活每个状态的值范围的最小值和最大值。
- **Color** — 当所连接信号值与对应的 **State** 值匹配时的 Lamp 颜色。您可以从标准颜色调色板中选择，也可以使用 `RGB` 值指定自定义颜色。

`[default]` 状态指定当所连接信号值与 **States** 表中指定的任何值都不匹配时 Lamp 模块的颜色。

**注意**

您可以配置状态的不仅仅值和颜色：您可以为某个状态配置 **Design** 选项卡的 **States** 组件中的所有参数。例如，您可以选择当灯处于该状态时显示在灯上的图标。当您配置 **States** 组件中的任何参数时，更改会应用于在 **States** 组件的 **Select State** 部分中选择的状态。

#### 提示

您还可以使用 Property Inspector 中的 **Parameters** 选项卡配置模块状态的值和颜色。

#### 编程用法

要以编程方式指定 Lamp 模块的 `State` 和 `Color` 参数值，请使用包含以下字段的结构体数组：

- `Value` — 标量 `double` 信号值，或指定使 Lamp 模块显示指定颜色指示的 `double` 信号值范围的最小值和最大值的向量。

  **注意**

  指定向量会启用 **Specify State Values as Ranges** 选项。
- `Color` — `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间，指定 Lamp 模块要显示的颜色。

    lampState1.Value = [1 2];
    lampState1.Color = [0 0 1];
    lampState2.Value = [2 3];
    lampState2.Color = [1 0 0];
    lampStates = [lampState1 lampState2];

|  |
| --- |
| **模块参数：** `StateColors` |
| **类型：** structure array |
| **默认值：** structure |

`ColorDefault` 参数指定当所连接信号的值与任何指定的状态值都不匹配时 Lamp 模块的颜色。请将 `ColorDefault` 参数指定为 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数：** `ColorDefault` |
| **类型：** `[r g b]` vector |
| **默认值：** `[0.7529 0.7529 0.7529]` |

### **Apply Default Settings to All States** — 用于将默认状态的设置应用于所有其他状态的选项 `off` (默认) | `on`

将默认状态的设置应用于所有其他状态。此选项适用于 **States** 组件中的所有设置，但 **Value and Color** 部分中的设置除外。

### **Specify State Values as Ranges** — 用于指定激活状态的值的范围的选项 `off` (默认) | `on`

您可以指定激活状态的信号值范围。选择 **Specify State Values as Ranges**，并指定激活每个状态的值范围的最小值和最大值。

#### 编程用法

要以编程方式指定每个状态是由信号值激活还是由信号值范围激活，请将 `StateValueType` 参数指定为 string 或 character vector。要使用信号值激活每个状态，请将 `StateValueType` 设置为 `"Discrete"`。要使用信号值范围激活每个状态，请将 `StateValueType` 设置为 `"Range"`。

|  |
| --- |
| **模块参数：** `StateValueType` |
| **类型：** character vector | string |
| **值：** `"Discrete"` | `"Range"` |
| **默认值：** `"Discrete"` |

### **Value** — 状态值 标量

每个状态将一个 **Value** 与一个 **Color** 配对。指定激活在 **Design** 选项卡中选择的状态的 **Value**。

**注意**

当启用 **Specify State Values as Ranges** 选项时，**Value** 参数会变为参数 `Minimum` 和 `Maximum`，这允许您通过指定最小值和最大值来定义范围。

**示例：** `0`

### **Color** — 状态颜色 `[r g b]` 向量

每个状态将一个 **Value** 与一个 **Color** 配对。从标准颜色调色板中选择在 **Design** 选项卡中选择的状态的 **Color**，或指定自定义颜色。

**示例：** `[1 0 0]`

### **Opacity** — 状态颜色不透明度 `1` (默认) | 标量

将状态 **Color** 的不透明度指定为从 0 到 1 的标量值。

**示例：** `0.5`

### **Style** — 形状和图标组合样式 `Intersect` (默认) | `Simple` | `Subtract`

一个灯最多可以显示三种不同颜色：

- 状态 **Color**
- Property Inspector 中所选图标的颜色
- 背景颜色或背景图像，具体取决于激活的是哪一个

灯上显示的颜色取决于 Lamp 模块的形状层和图标层如何组合。选择如何组合这些层：

- 在 `Intersect` 样式中，形状和图标重叠的区域具有状态 **Color**。形状和图标不重叠的区域具有背景颜色或图像。
- 在 `Simple` 样式中，形状中未被图标覆盖的区域具有状态 **Color**。灯上的图标具有与其在 Property Inspector 中对应项相同的颜色。其余区域具有背景颜色或图像。
- 在 `Subtract` 样式中，形状中未被图标覆盖的区域具有状态 **Color**。其余区域具有背景颜色或图像。

三个 Lamp 模块，分别配置为组合形状和图标的三种方式之一：Simple、Intersect 或 Subtract。

**示例：** `'Simple'`

### **Shape** — 状态形状图像

选择一个形状，该形状与图标组合后确定灯上应用状态 **Color** 的区域。选择圆形、方形或三角形。

### **Icon** — Lamp 模块外观 SVG 图像

使用图标配置 Lamp 模块在模型中的外观。您可以从内置形状、汽车和无线图标中选择，也可以上传自己的自定义 SVG 文件作为图标。

要查看图标选项，请在 **Icon** 部分中选择 **Icon Type**。要将自己的 SVG 文件用作模块图标，请在 **Icon** 部分中选择 `Custom` 作为 **Icon Type**，然后在 **Custom Icon** 部分中点击加号按钮以上传 SVG 文件。

**形状图标**

| 图标 | 图标名称 | 编程用法值 |
| --- | --- | --- |
| Lamp icon: a solid gray circle | Lamp | `Default` |
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
| Frown1 icon: the outline of a face with an open frowning mouth | Frown1 | `Frown1` |
| Frown2 icon: the outline of a face with a closed frowning mouth | Frown2 | `Frown2` |
| Hexagon icon: a solid hexagon | Hexagon | `Hexagon` |
| L-shaped membrane icon: the silhouette of the L-shaped membrane | L-shaped Membrane | `Membrane` |
| Pentagon icon: a solid pentagon | Pentagon | `Pentagon` |
| Rectangle icon: a solid rectangle | Rectangle | `Rectangle` |
| Smile1 icon: the outline of a face with an open upturned mouth | Smile1 | `Smile1` |
| Smile2 icon: the outline of a face with a closed upturned mouth | Smile2 | `Smile2` |
| Solid Face icon: a solid face with a closed mouth in a straight line | Solid Face | `SolidFace` |
| Solid Frown1 icon: a solid face with an open frowning mouth | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 icon: a closed frowning mouth | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 icon: a solid face with an open upturned mouth | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 icon: a solid face with a closed upturned mouth | Solid Smile2 | `SolidSmile2` |
| Square icon: a solid square | Square | `Square` |
| Triangle icon: a solid triangle | Triangle | `Triangle` |

**汽车图标**

| 图标 | 图标名称 | 编程用法值 |
| --- | --- | --- |
| Adaptive Cruise Control 图标：一个速度表，带有指向刻度线的箭头，背景中有汽车轮廓 | Adaptive Cruise Control | `AdaptiveCruiseControl` |
| Adaptive Cruise Control Failure 图标：一个速度表，旁边有感叹号，背景中有汽车轮廓 | Adaptive Cruise Control Failure | `AdaptiveCruiseControlFailure` |
| ABS 图标：一个圆圈，在一组括号中标有 "ABS" | Antilock Brake System | `AntilockBrakeSystem` |
| Battery 图标：电池轮廓，正极上有 + 符号，负极上有 - 符号 | Battery | `Battery` |
| Check Engine 图标：发动机轮廓，标有 "Check Engine" | Check Engine | `CheckEngine` |
| Check Engine2 图标：发动机轮廓，上面有避雷针轮廓，下方有单词 "CHECK" | Check Engine2 | `CheckEngine2` |
| Cruise Control 图标：一个速度表，带有指向其中一个刻度线的箭头 | Cruise Control | `CruiseControl` |
| Eco Mode 图标：一个实心叶子形状，标有 "ECO" | Eco Mode | `EcoMode` |
| Electronic Stability 图标：一个圆圈，在一组括号中标有 "ESP" | Electronic Stability | `ElectronicStability` |
| Engine 图标：发动机轮廓 | Engine | `Engine` |
| Engine Coolant Temp 图标：一个温度计，背景中有波纹 | Engine Coolant Temp | `EngineCoolantTemp` |
| Engine Failure 图标：发动机轮廓，上面有感叹号 | Engine Failure | `EngineFailure` |
| Engine Heating 图标：发动机轮廓，上面有三个向上的波浪箭头 | Engine Heating | `EngineHeating` |
| Engine Oil 图标：油壶轮廓 | Engine Oil | `EngineOil` |
| Exterior Bulb Failure 图标：发光的灯泡轮廓，上面有感叹号 | Exterior Bulb Failure | `ExteriorBulbFailure` |
| Front Fog Light 图标：雾灯轮廓，向左发射光线，光线表示为斜线，位于表示雾的波浪垂直线之上 | Front Fog Light | `FrontFogLight` |
| Fuel 图标：加油泵轮廓，上面有向左的箭头 | Fuel | `Fuel` |
| Hazards 图标：警告三角形轮廓 | Hazards | `Hazards` |
| Headlamp Leveling 图标：灯轮廓，发射光线，上方有顺时针箭头，下方有逆时针箭头，表示可以转动灯来调平光线 | Headlamp Leveling | `HeadlampLeveling` |
| High Beams 图标：灯轮廓，发射水平光线 | High Beams | `HighBeams` |
| Hill Descent Control 图标：汽车下坡行驶的轮廓 | Hill Descent Control | `HillDescentControl` |
| Lighting Switch 图标：发光灯泡轮廓 | Lighting Switch | `LightingSwitch` |
| High Beams 图标：灯轮廓，发射向下倾斜的光线 | Low Beams | `LowBeams` |
| Parking Assistance 图标：字母 "P" 旁边有一个表示障碍物的实心三角形，"P" 发射表示为三条曲线的检测信号，指向三角形 | Parking Assistance | `ParkingAssistance` |
| Rear Fog Light 图标：雾灯轮廓，向右发射光线，光线表示为水平线，位于表示雾的波浪垂直线之上 | Rear Fog Light | `RearFogLight` |
| Side Lights 图标：两个灯轮廓，分别向左和向右发射光线 | Side Lights | `SideLights` |
| Stability Control 图标：汽车轮廓，后面有波浪线表示汽车打滑 | Stability Control | `StabilityControl` |
| Stability Control Off 图标：汽车轮廓，后面有波浪线表示汽车打滑，下方有单词 "OFF" | Stability Control Off | `StabilityControlOff` |
| Tire Monitor 图标：轮胎横截面轮廓，上面有感叹号 | Tire Monitor | `TireMonitor` |
| Traction Control 图标：轮胎横截面轮廓，标有 "TC" | Traction Control | `TractionControl` |
| Traction Control Off 图标：轮胎横截面轮廓，标有 "TC"，整个图像有一条斜线穿过 | Traction Control Off | `TractionControlOff` |
| Traction Control Failure 图标：轮胎横截面轮廓，标有 "TC"，旁边有感叹号 | Traction Control Failure | `TractionControlFailure` |
| Turn Signal Left 图标：指向左侧的实心箭头 | Turn Signal Left | `TurnSignalLeft` |
| Turn Signal Right 图标：指向右侧的实心箭头 | Turn Signal Right | `TurnSignalRight` |

**无线图标**

| 图标 | 图标名称 | 编程用法值 |
| --- | --- | --- |
| Network 图标：无线互联网连接图标 | Network | `Network` |
| Network No Signal 图标：灰显的无线互联网连接图标，旁边有一个带叉的圆圈 | Network No Signal | `NetworkNoSignal` |
| Network Transmission 图标：无线互联网塔 | Network Transmission | `NetworkTransmission` |
| Network3G 图标：无线互联网连接图标，旁边有 "3G" | Network3G | `Network3G` |
| Network4G 图标：无线互联网连接图标，旁边有 "4G" | Network4G | `Network4G` |
| Network5G 图标：无线互联网连接图标，旁边有 "4G" | Network5G | `Network5G` |

**提示**

Dashboard 库具有针对每个图标预配置 Lamp 模块的库。

#### 编程用法

|  |
| --- |
| **模块参数：** `Icon` |
| **类型：** string | character vector |
| **默认值：** `'Default'` |

### **X Offset** — 形状图标组合边界框左边缘相对于模块左边缘的水平偏移 标量

将形状和图标组合的边界框左边缘相对于模块左边缘的水平偏移指定为模块宽度的比率。相对于偏移为 `0` 时形状和图标组合的位置，负值偏移会将组合向左移动，正值偏移会将组合向右移动。

**示例：** `1`

### **Y Offset** — 形状图标组合边界框上边缘相对于模块上边缘的垂直偏移 标量

将形状和图标组合的边界框上边缘相对于模块上边缘的垂直偏移指定为模块高度的比率。相对于偏移为 `0` 时形状和图标组合的位置，负值偏移会将组合向上移动，正值偏移会将组合向下移动。

**示例：** `1`

### **Width** — 形状图标组合的宽度 标量

将形状和图标组合的边界框宽度指定为模块宽度的比率。

**示例：** `0.5`

### **Height** — 形状图标组合的高度 标量

将形状和图标组合的边界框高度指定为模块高度的比率。

**示例：** `0.5`

### **Icon Size** — 图标图像缩放级别 标量

您可以通过围绕图标中心放大或缩小来修改图标在灯上的显示方式。将缩放级别指定为从 `0` 到 `2` 的标量值。当 **Icon Size** 为 `1` 时，图标会缩放以在形状和图标组合的边界框限制内尽可能大地显示整个图像。当 **Icon Size** 大于 `1` 时，图像会在边界框的限制处被裁剪。

**示例：** `0.5`

#### 背景图像

### **Use Background Color** — 用于指定纯色模块背景颜色的选项 `off` (默认) | `on`

对于模块背景，您可以提供背景图像或选择纯色。要选择纯色背景颜色，请选择此参数。要提供背景图像，请清除此参数。

**注意**

使用 Simulink Toolstrip 的 **Format** 选项卡更改背景颜色会移除背景图像，并启用 **Use Background Color** 参数。

**示例：** `on`

### **Color** — 模块背景颜色 `[r g b]` 向量

要使用纯色背景颜色，请选择 **Use Background Color** 参数。然后，从标准颜色调色板中选择背景颜色，或指定自定义颜色。

**提示**

您还可以在 Simulink Toolstrip 的 **Format** 选项卡中指定 **Background Color**。

要指定模块文本的颜色，请使用 **Font Color** 参数。

#### 编程用法

将模块的 `BackgroundColor` 参数指定为 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间，格式为 string 或 character vector。

|  |
| --- |
| **模块参数：** `BackgroundColor` |
| **类型：** string | character vector |
| **值：** `[r g b]` vector |

### **Opacity** — 模块背景不透明度 `1` (默认) | 标量

将模块背景不透明度指定为从 `0` 到 `1` 的标量值。

**示例：** `0.5`

### **Corner Radius** — 具有模块背景颜色的区域的圆角半径 标量

将模块背景颜色所覆盖区域的圆角半径指定为模块两个尺寸（宽度或高度）中较小者的一半的比率。

**示例：** `0.25`

#### 前景图像

### **X Offset** — 前景图像左边缘相对于模块左边缘的水平偏移 标量

将图像左边缘相对于模块左边缘的水平偏移指定为模块宽度的比率。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向左移动，正值偏移会将图像向右移动。

**示例：** `1`

### **Y Offset** — 前景图像上边缘相对于模块上边缘的垂直偏移 标量

将图像上边缘相对于模块上边缘的垂直偏移指定为模块高度的比率。相对于偏移为 `0` 时图像的位置，负值偏移会将图像向上移动，正值偏移会将图像向下移动。

**示例：** `1`

### **Width** — 前景图像宽度 标量

将前景图像宽度指定为模块宽度的比率。

**示例：** `0.5`

### **Height** — 前景图像高度 标量

将前景图像高度指定为模块高度的比率。

**示例：** `0.5`

### **Lock Aspect Ratio** — 用于保持前景图像宽高比的选项 `on` (默认) | `off`

选择此参数可在使用 Property Inspector 调整图像大小时保持宽高比。

## 所属库

Simulink / Dashboard / Customizable Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成过程中会被忽略。

## 版本历史

**在 R2021b 中引入**

### R2024b：使用键盘解锁 dashboard 模块宽高比

如果 Dashboard 库中模块的宽高比已锁定，您可以通过按 **Shift** 临时解锁宽高比。当您松开 **Shift** 键时，宽高比会锁定。

如果宽高比未锁定，按 **Shift** 会临时锁定宽高比。当您松开 **Shift** 键时，宽高比会解锁。

### R2024a：将 dashboard 面板部署为 Web App 或独立桌面 App

借助 Simulink Compiler™ 许可证，您现在可以将与面板所连接模型一起打包的 dashboard 面板部署为独立桌面 App 或 Web App。您可以使用该 App 操作控件并监视面板上的显示，而独立于 Simulink。

要了解如何部署面板，请参阅 Deploy Dashboard Panel as App。

### R2024a：停靠 dashboard 面板

从 R2024a 开始，您可以将 dashboard 面板停靠到 Simulink Editor 窗口。您可以使用停靠的面板在仿真期间监视信号和控制参数，而不会遮盖画布中的模型图。

有关详细信息，请参阅 Dock Panels。

### R2023b：在新窗口中打开面板

从 R2023b 开始，您可以在新窗口中打开 dashboard 面板。为此，请选择该面板，并将鼠标悬停在出现的省略号上。在展开的操作菜单中，点击 Open In New Window。

您可以将包含该面板的新窗口与模型窗口分开最小化和还原。在面板窗口中，您可以运行、暂停、停止和单步执行仿真。在面板窗口中，您可以编辑面板及其包含的模块。

要将面板返回到模型画布，请在面板窗口 toolstrip 中点击 Open in canvas。

有关在新窗口中打开面板的详细信息，请参阅 Open Panels in New Window。

### R2023a：Simulink Toolstrip 中的持久 Panels 选项卡

当您将 dashboard 面板添加到模型时，Simulink Toolstrip 中会出现 **Panels** 选项卡，并显示用于管理和编辑面板的选项。

以前，**Panels** 选项卡仅在选择了面板时可见。从 R2023a 开始，当未选择面板时，**Panels** 选项卡会保持可见。

**Panels** 选项卡还包含以下新选项：

- 您可以添加空面板。
- 您可以重命名所选面板。
- 您可以隐藏所选面板。

### R2022b：对面板中的可自定义 dashboard 模块的撤销和重做支持

从 R2022b 开始，您可以撤销和重做对面板中可自定义 dashboard 模块所做的更改。

要撤销或重做更改：

1. 点击面板或面板中的模块。
2. 按 **Ctrl+Z** 撤销更改，或按 **Ctrl+Y** 重做更改。

**注意**

键盘快捷键基于 Windows®。在 Mac 上，请按 **command** (⌘) 而不是 **Ctrl**。

### R2022b：对面板的 Toolstrip 支持

从 R2022b 开始，您可以使用 Simulink Toolstrip 管理和编辑面板及其包含的 dashboard 模块。

当您点击面板中的 dashboard 模块时，会出现该模块的 toolstrip 选项卡。例如，当您点击 Circular Gauge 模块时，toolstrip 中会出现 **Gauge** 选项卡。

当您点击面板时，toolstrip 中会出现 **Panel** 选项卡。该选项卡提供以下选项：

- 管理模型中面板的可见性。
- 使所有未隐藏的面板适合当前视图。
- 折叠所选面板。
- 自定义面板的大小和内容。
- 为所选面板设置自定义背景图像。
- 向所选面板添加新选项卡。

### R2022b：扩展对 Raspberry Pi 板上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Raspberry Pi® Hardware 支持从 **Customizable Blocks** 库将这些模块部署到您的 Raspberry Pi 板上：

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

您可以在 Simulink 模型中自定义模块的视觉方面，并在从 Raspberry Pi 终端启动的 Web 浏览器中获得所见即所得 (WYSIWYG) 可视化。

### R2022b：扩展对 Android 设备上可自定义 Dashboard 模块的支持

从 R2022b 开始，Simulink Support Package for Android® Devices 支持从 **Customizable Blocks** 库将这些模块部署到您的 Android 设备上：

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

您可以在 Simulink 模型中自定义模块的视觉方面，并在 Android 设备以及 Web 浏览器中获得所见即所得 (WYSIWYG) 可视化。

### R2022a：在设计模式下查看和编辑每个状态

从 R2022a 开始，您可以在设计模式下查看和编辑可自定义 Lamp 模块的每个状态。您可以为每个状态修改模块外观的更多方面。例如，您现在可以设计一个为每个状态使用不同图标的灯。

### R2022a：Lamp 模块支持将状态值指定为范围

在以前的版本中，Lamp 模块仅在所连接信号具有您为该状态指定的单个唯一值时才进入状态。从 R2022a 开始，您可以指定激活每个状态的信号值范围。

### R2022a：更改状态颜色的不透明度

从 R2022a 开始，对于可自定义 Lamp 模块，您可以更改状态颜色的不透明度。

### R2022a：调整前景图像大小和重新定位前景图像

Customizable Blocks 库中的模块具有将前景图像添加为模块设计一部分的选项。从 R2022a 开始，您可以在模块设计中旋转、调整和重新定位前景图像。

## 描述

在具有可自定义外观的灯上显示反映信号值的颜色

Lamp 模块显示反映所连接信号值的颜色。当您在 Customizable Blocks 库中使用 Lamp 模块时，可以修改模块外观，使其看起来像您系统中的真实指示灯。将 Lamp 模块与其他 dashboard 模块配合使用，可为您的模型构建由控件和指示器组成的交互式 dashboard。

要配置 Lamp 模块，请指定一个或多个状态。状态将状态值与 Lamp 模块要显示的颜色配对。当所连接信号的值与状态值相同时，Lamp 模块显示该颜色。您也可以将状态值指定为范围，这样当所连接信号的值落入指定范围时，模块会显示该颜色。

### 自定义 Lamp 模块

当您将 Lamp 模块添加到模型时，该模块会预配置为默认设计。您可以使用默认设计使用该模块，也可以自定义模块外观。

要自定义模块外观，请使用设计模式。选择模块后，可以通过以下三种方式之一进入设计模式：

- 在 Simulink® Toolstrip 中，在模块特定选项卡上的 **Design** 下，点击 **Edit**。
- 在 Property Inspector 中的 **Design** 选项卡上，点击 **Edit**。
- 将鼠标悬停在模块上方出现的省略号上，然后点击 Edit Custom Block 按钮。

在设计模式下，您可以使用模块上方的工具栏自定义 Lamp。要访问其他自定义选项或为设计设置输入精确值，请使用 Property Inspector 中的 **Design** 选项卡。

处于设计模式的 Customizable Lamp 模块，可见工具栏和 Property Inspector 中的 Design 选项卡。

当您自定义 Lamp 模块时，您会为每个状态配置模块外观。要选择要自定义的状态，请使用工具栏中的下拉列表。或者，在 **Design** 选项卡上，选择 **States** 组件，然后从 **Select State** 列表中选择。要添加状态，请在工具栏中点击 Add State 按钮。要删除状态，请点击 Remove State 按钮。

**自定义所选状态的设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 将状态值指定为数字或范围。 | 否 | 是 |
| 添加或删除状态。 | 是 | 是 |
| 为颜色反映信号值的区域选择形状。 | 是 | 是 |
| 选择形状的颜色。 | 是 | 是 |
| 从包含无线图标和汽车指示灯的图标集中选择，或上传自定义图标。 | 是 | 是 |
| 指定如何组合形状和图标。 | 是 | 是 |
| 更改形状和图标的大小。 | 否 | 是 |
| 更改形状和图标的位置。 | 否 | 是 |

除了使用工具栏和 **Design** 选项卡自定义模块设计外，您还可以在画布中以交互方式调整组件大小和重新定位组件。要调整特定于某个状态的组件（例如图标）的大小，请在工具栏中选择该状态，然后调整组件大小或重新定位组件。

要组合形状和图标，请在工具栏从左数第三部分中，选择以下组合样式之一：

- Simple — 将图标叠加在形状上方。
- Intersect — 保留形状和图标的交集作为颜色反映信号值的区域。
- Subtract — 保留形状并从中挖去图标，作为改变颜色的区域。

三个 Lamp 模块，分别配置为组合形状和图标的三种方式之一：Simple、Intersect 或 Subtract。

**提示**

Intersect 和 Subtract 组合样式使用图标资源中的透明度来生成改变颜色的区域。对于自定义图标，请考虑使用支持透明度的图像格式，例如 SVG 或 PNG。

**应用于所有状态的设计模式操作**

| 操作 | 在工具栏中可用 | 在 **Design** 选项卡中可用 |
| --- | --- | --- |
| 上传背景图像。 | 否 | 是 |
| 设置纯色背景颜色。 | 否 | 是 |
| 上传前景图像。 | 否 | 是 |

完成设计编辑后，要退出设计模式，请点击画布右上角的 **X**。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，然后点击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号，或更改显示模块的连接，请进入连接模式。选择要连接的信号线。在出现的列表中，选择要连接的信号。然后，将鼠标悬停在 dashboard 模块上，并点击 Done Connecting 按钮。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您也可以将 dashboard 模块连接到 Stateflow® chart。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 Lamp 模块连接到您的模型。

未连接的 Lamp 模块连接到 Constant 模块发送到 Outport 模块的信号。
