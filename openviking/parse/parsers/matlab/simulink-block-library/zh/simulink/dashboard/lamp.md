---
type: simulink-block
title: 'Lamp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Dashboard'
documentation_page: 'lamp'
documentation_source_path: 'slref/lamp.html'
language: zh-CN
chinese_source: official
---

# Lamp

## 端口

R2025b 官方文档未提供。

## 参数

### **连接** — 要连接和显示的信号 信号连接选项

Dashboard 模块不使用端口来连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或“模块参数”对话框中的**连接**表。有关连接模式以及如何使用工具条进行连接的信息，请参阅Connect Dashboard Blocks to Simulink Model。

使用**连接**表连接 Display 模块或更改 Display 模块的连接：

1. 选择模块。
2. 要连接该模块，请在属性检查器的**参数**选项卡上点击**连接**。要更改模块的连接，请改为点击**更改**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击**应用**。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数**：`Binding` |
| **类型：**`Simulink.HMI.SignalSpecification` |
| **默认值：**`[]` |

### **状态** — 信号值和颜色对组 标量和 `RGB` 向量

状态将显示颜色与连接的信号值的相匹配。每个状态由**状态**和**颜色**组成。

- **状态** - 使 Lamp 模块显示指定颜色的已连接信号值。
- **颜色** - 当连接的信号值与对应的**状态**值匹配时信号灯的颜色。您可以从标准颜色调色板中选择，也可以使用 `RGB` 值指定自定义颜色。

`[undefined]` 状态指定当连接的信号值与**状态**表中指定的任何值都不匹配时，Lamp 模块的颜色。点击 **+** 按钮可添加另一个状态。

#### 编程用法

要以编程方式为 Lamp 模块指定 `State` 和 `Color` 参数值，请使用包含以下字段的结构体数组：

- `Value` - 导致 Lamp 模块显示指定颜色指示的标量 `double` 信号值。
- `Color` - `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间，指定要显示的 Lamp 模块的颜色。

```
lampState1.Value = 1;
lampState1.Color = [0 0 1];
lampState2.Value = 2;
lampState2.Color = [1 0 0];
lampStates = [lampState1 lampState2];
```

|  |
| --- |
| **模块参数**：`StateColors` |
| **类型：**结构体数组 |
| **默认值：**结构体 |

`ColorDefault` 参数指定当所连接信号的值与任何指定的状态值都不匹配时，Lamp 模块的颜色。将 `ColorDefault` 参数指定为 `1`×`3` `[r g b]` 向量，其值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ColorDefault` |
| **类型：**`[r g b]` 向量 |
| **默认值**：`[0.7529 0.7529 0.7529]` |

### **图标** — Lamp 模块外观 SVG 图像

使用一个图标来配置模型中 Lamp 模块的外观。您可以从内置形状、汽车图标和无线图标中进行选择，也可以上传您自己的自定义 SVG 文件作为图标。

要查看图标选项，请在**图标**选项卡上选择**图标类型**。要使用您自己的 SVG 文件作为模块图标，请选择**自定义**作为**图标类型**并上传 SVG 文件。Lamp 模块的状态颜色可以应用于下列 SVG 元素：

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

**形状图标**

| 图标 | 基本形状库模块名称 | 编程使用的值 |
| --- | --- | --- |
| Lamp icon: a solid gray circle | Lamp | `Default` |
| Circle icon: a solid black circle | Circle | `Circle` |
| Hexagon icon: a solid hexagon | Hexagon | `Hexagon` |
| Pentagon icon: a solid pentagon | Pentagon | `Pentagon` |
| Rectangle icon: a solid rectangle | Rectangle | `Rectangle` |
| Square icon: a solid square | Square | `Square` |
| Triangle icon: a solid triangle | Triangle | `Triangle` |
| Check1 icon: a check mark | Check1 | `Check1` |
| Check2 icon: a check mark with slightly curved lines | Check2 | `Check2` |
| Check3 icon: the outline of a check mark | Check3 | `Check3` |
| Check4 icon: a check mark with a divot along its outline | Check4 | `Check4` |
| Ex1 icon: a cross mark | Ex1 | `Ex1` |
| Ex2 icon: a cross mark with one curved line | Ex2 | `Ex2` |
| Ex3 icon: the outline of a cross mark | Ex3 | `Ex3` |
| Ex4 icon: a cross mark with a divot along the outline | Ex4 | `Ex4` |
| Face icon: the outline of a face with a closed mouth in a straight line | Face | `Face` |
| Frown1 icon: the outline of a face with an open downturned mouth | Frown1 | `Frown1` |
| Frown2 icon: the outline of a face with a closed downturned mouth | Frown2 | `Frown2` |
| Smile1 icon: the outline of a face with an open upturned mouth | Smile1 | `Smile1` |
| Smile2 icon: the outline of a face with a closed upturned mouth | Smile2 | `Smile2` |
| Solid Face icon: a solid face with a closed mouth in a straight line | Solid Face | `SolidFace` |
| Solid Frown1 icon: a solid face with an open downturned mouth | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 icon: a closed downturned mouth | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 icon: a solid face with an open upturned mouth | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 icon: a solid face with a closed upturned mouth | Solid Smile2 | `SolidSmile2` |

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

- 您可以使用工具条中的模块选项卡更改 Lamp 模块的图标。
- Dashboard 库包含为每个图标提供预配置 Lamp 模块的库。
- 如果您要自定义 Lamp 模块的外观（该外观无法通过选择图标来实现），请考虑使用 Customizable Blocks 库中的 Lamp 模块来设计您自己的指示灯。

#### 编程用法

|  |
| --- |
| **模块参数**：`Icon` |
| **类型：**字符串 | 字符向量 |
| **默认值：**`'Default'` |

### **标签** — 模块标签位置 `Top` (默认) | `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接的元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型：**字符向量 |
| **值**：`'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**：`'Top'` |

### **不透明度** — 模块不透明度 `1` (默认) | 标量

模块不透明度，指定为 0 到 1 之间的标量值。

**示例:** `0.5`

#### 编程用法

|  |
| --- |
| **模块参数：**`Opacity` |
| **类型：**标量 |
| **默认值：**`1` |

## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

Dashboard 模块在代码生成中会被忽略。

## 版本历史

**在 R2015a 中推出**

## 描述

显示反映信号灯上信号值的颜色

Lamp 模块会显示一种颜色，用来指示其所连接的信号的值。要配置 Lamp 模块以提供仿真期间所需的信息，请指定一个或多个状态，这些状态将信号值与要显示的 Lamp 模块的颜色配对。您可以将 Lamp 模块与其他 Dashboard 模块结合使用，为您的模型构建包含各种控件和指示器的交互式仪表板。

### 信号灯图标

您可以通过选择一个内置图标或上传您自己的自定义图标来更改 Lamp 模块的外观。内置图标包括基本形状、汽车指示灯和无线图标。您可以使用**图标**参数或使用工具条中的模块选项卡来更改 Lamp 模块的图标。Dashboard 库还包含为每个图标提供预配置的 Lamp 模块版本的库。有关完整的详细信息，请参阅图标。

Lamp Icon drop-down menu showing basic shape icons, automotive indicator lamps, wireless icons, and the option to choose a custom icon

如果您要自定义 Lamp 模块的外观（该外观无法通过选择图标来实现），请考虑使用 Customizable Blocks 库中的 Lamp 模块来设计您自己的指示灯。

### 连接 Dashboard 模块

Dashboard 模块不使用端口来连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标在要连接的模块上暂停并点击连接按钮 。要在已连接的模块上进入连接模式，请选择该模块，在显示的省略号 (…) 上暂停，然后在展开的操作菜单中点击连接按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择您要连接的信号。然后，请在 Dashboard 模块上悬停并点击完成连接按钮 。要查看 Dashboard 模块显示连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画说明如何将 Lamp 模块连接到您的模型。

An unconnected Lamp block connects to the signal that a Ramp block sends to a Terminator block.
