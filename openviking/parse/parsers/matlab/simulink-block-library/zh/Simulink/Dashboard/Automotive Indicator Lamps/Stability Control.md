---
type: simulink-block
title: 'Lamp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'lamp'
documentation_source_path: 'slref/lamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Lamp

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Connection
  summary: 要连接的信号及显示信号连接选项
  group: ''
  block_parameter: Binding
  type: Simulink.HMI.SignalSpecification
  default: '[]'
- name: States
  summary: 信号值与颜色对 标量和 RGB 向量
  group: ''
  block_parameter: ColorDefault
  type: '[r g b] vector'
  default: '[0.7529 0.7529 0.7529]'
- name: Icon
  summary: Lamp 模块外观 SVG 图像
  group: ''
  block_parameter: Icon
  type: string | character vector
  default: '''Default'''
- name: Label
  summary: 模块标签位置 Top（默认）| Bottom | Hide
  group: ''
  block_parameter: LabelPosition
  type: character vector
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
- name: Opacity
  summary: 模块不透明度 1（默认）| 标量
  group: ''
  block_parameter: Opacity
  type: scalar
  default: '1'
```

### **Connection** — 要连接的信号及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® 工具条或模块参数对话框中的 **Connection** 表。有关连接模式以及如何使用工具条进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **Connection** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **Parameters** 选项卡上点击 **Connect**。要更改该模块的连接，请改为点击 **Change**。
3. 选择要连接的信号线。
4. 在表中，选择要连接的信号。
5. 点击 **Apply**。

您还可以将 Dashboard 模块连接到 Stateflow 流程图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程使用

|  |
| --- |
| **模块参数**：`Binding` |
| **类型**：`Simulink.HMI.SignalSpecification` |
| **默认值**：`[]` |

### **States** — 信号值与颜色对 标量和 `RGB` 向量

状态将显示颜色与所连接信号的值进行匹配。每个状态由一个 **State** 和一个 **Color** 组成。

- **State** — 使 Lamp 模块显示指定颜色的所连接信号值。
- **Color** — 当所连接信号值与对应的 **State** 值匹配时的 Lamp 颜色。您可以从标准颜色调色板中选择，或使用 `RGB` 值指定自定义颜色。

`[undefined]` 状态指定当所连接信号值与 **States** 表中指定的任何值都不匹配时 Lamp 模块的颜色。点击 **+** 按钮添加另一个状态。

#### 编程使用

要以编程方式为 Lamp 模块指定 `State` 和 `Color` 参数值，请使用包含以下字段的结构体数组：

- `Value` — 使 Lamp 模块显示指定颜色指示的标量 `double` 信号值。
- `Color` — `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间，指定 Lamp 模块要显示的颜色。

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
| **类型**：structure array |
| **默认值**：structure |

`ColorDefault` 参数指定当所连接信号的值与任何指定的状态值都不匹配时 Lamp 模块的颜色。将 `ColorDefault` 参数指定为 `1`×`3` 的 `[r g b]` 向量，值介于 `0` 和 `1` 之间。

|  |
| --- |
| **模块参数**：`ColorDefault` |
| **类型**：`[r g b]` vector |
| **默认值**：`[0.7529 0.7529 0.7529]` |

### **Icon** — Lamp 模块外观 SVG 图像

使用图标来配置模型中 Lamp 模块的外观。您可以从内置形状、汽车和无线图标中选择，也可以上传自己的自定义 SVG 文件作为图标。

要查看图标选项，请在 **Icon** 选项卡上选择一个 **Icon Type**。要将自己的 SVG 文件用作模块图标，请选择 `Custom` 作为 **Icon Type** 并上传 SVG 文件。Lamp 模块的状态颜色可以应用于以下 SVG 元素：

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

| 图标 | Basic Shapes 库模块名称 | Programmatic Use 值 |
| --- | --- | --- |
| Lamp 图标：一个实心灰色圆形 | Lamp | `Default` |
| Circle 图标：一个实心黑色圆形 | Circle | `Circle` |
| Hexagon 图标：一个实心六边形 | Hexagon | `Hexagon` |
| Pentagon 图标：一个实心五边形 | Pentagon | `Pentagon` |
| Rectangle 图标：一个实心矩形 | Rectangle | `Rectangle` |
| Square 图标：一个实心正方形 | Square | `Square` |
| Triangle 图标：一个实心三角形 | Triangle | `Triangle` |
| Check1 图标：一个对勾 | Check1 | `Check1` |
| Check2 图标：一个线条略微弯曲的对勾 | Check2 | `Check2` |
| Check3 图标：一个对勾的轮廓 | Check3 | `Check3` |
| Check4 图标：一个轮廓上有凹痕的对勾 | Check4 | `Check4` |
| Ex1 图标：一个叉号 | Ex1 | `Ex1` |
| Ex2 图标：一个有一条曲线条的叉号 | Ex2 | `Ex2` |
| Ex3 图标：一个叉号的轮廓 | Ex3 | `Ex3` |
| Ex4 图标：一个轮廓上有凹痕的叉号 | Ex4 | `Ex4` |
| Face 图标：一张闭嘴呈直线的脸的轮廓 | Face | `Face` |
| Frown1 图标：一张张嘴向下弯的脸的轮廓 | Frown1 | `Frown1` |
| Frown2 图标：一张闭嘴向下弯的脸的轮廓 | Frown2 | `Frown2` |
| Smile1 图标：一张张嘴向上弯的脸的轮廓 | Smile1 | `Smile1` |
| Smile2 图标：一张闭嘴向上弯的脸的轮廓 | Smile2 | `Smile2` |
| Solid Face 图标：一张闭嘴呈直线的实心脸 | Solid Face | `SolidFace` |
| Solid Frown1 图标：一张张嘴向下弯的实心脸 | Solid Frown1 | `SolidFrown1` |
| Solid Frown2 图标：一张闭嘴向下弯的实心脸 | Solid Frown2 | `SolidFrown2` |
| Solid Smile1 图标：一张张嘴向上弯的实心脸 | Solid Smile1 | `SolidSmile1` |
| Solid Smile2 图标：一张闭嘴向上弯的实心脸 | Solid Smile2 | `SolidSmile2` |

**汽车图标**

| 图标 | Automotive Indicator Lamps 库模块名称 | Programmatic Use 值 |
| --- | --- | --- |
| Adaptive Cruise Control 图标：一个速度表，箭头指向一个刻度线，背景中有汽车轮廓 | Adaptive Cruise Control | `AdaptiveCruiseControl` |
| Adaptive Cruise Control Failure 图标：一个速度表，旁边有一个感叹号，背景中有汽车轮廓 | Adaptive Cruise Control Failure | `AdaptiveCruiseControlFailure` |
| Anti-Lock Brake System 图标：一个圆圈，在一对括号中标注有 "ABS" | Antilock Brake System | `AntilockBrakeSystem` |
| Battery 图标：一个电池的轮廓，正极上有加号，负极上有减号 | Battery | `Battery` |
| Check Engine 图标：一个发动机的轮廓，标注有 "Check Engine" | Check Engine | `CheckEngine` |
| Check Engine2 图标：一个发动机的轮廓，上面有避雷针的轮廓，下方有 "CHECK" 字样 | Check Engine2 | `CheckEngine2` |
| Cruise Control 图标：一个速度表，箭头指向其中一个刻度线 | Cruise Control | `CruiseControl` |
| Eco Mode 图标：一个实心叶子形状，标注有 "ECO" | Eco Mode | `EcoMode` |
| Electronic Stability 图标：一个圆圈，在一对括号中标注有 "ESP" | Electronic Stability | `ElectronicStability` |
| Engine 图标：一个发动机的轮廓 | Engine | `Engine` |
| Engine Coolant Temp 图标：一个温度计，背景中有波浪 | Engine Coolant Temp | `EngineCoolantTemp` |
| Engine Failure 图标：一个发动机的轮廓，上面有一个感叹号 | Engine Failure | `EngineFailure` |
| Engine Heating 图标：一个发动机的轮廓，上面有三个向上的波浪箭头 | Engine Heating | `EngineHeating` |
| Engine Oil 图标：一个油壶的轮廓 | Engine Oil | `EngineOil` |
| Exterior Bulb Failure 图标：一个发光的灯泡的轮廓，上面有一个感叹号 | Exterior Bulb Failure | `ExteriorBulbFailure` |
| Front Fog Light 图标：一个雾灯的轮廓，向左发出光线，光线表示为斜线，位于代表雾的波浪垂直线之上 | Front Fog Light | `FrontFogLight` |
| Fuel 图标：一个加油泵的轮廓，上面有一个向左的箭头 | Fuel | `Fuel` |
| Hazards 图标：一个警告三角形的轮廓 | Hazards | `Hazards` |
| Headlamp Leveling 图标：一个灯的轮廓，发出光线，上方有一个顺时针方向的箭头，下方有一个逆时针方向的箭头 | Headlamp Leveling | `HeadlampLeveling` |
| High Beams 图标：一个灯的轮廓，发出水平光线 | High Beams | `HighBeams` |
| Hill Descent Control 图标：一辆汽车下坡行驶的轮廓 | Hill Descent Control | `HillDescentControl` |
| Lighting Switch 图标：一个发光的灯泡的轮廓 | Lighting Switch | `LightingSwitch` |
| High Beams 图标：一个灯的轮廓，发出斜向下的光线 | Low Beams | `LowBeams` |
| Parking Assistance 图标：字母 "P" 旁边有一个实心三角形，"P" 发出表示为三条曲线的检测信号，指向三角形 | Parking Assistance | `ParkingAssistance` |
| Rear Fog Light 图标：一个雾灯的轮廓，向右发出光线，光线表示为水平线，位于代表雾的波浪垂直线之上 | Rear Fog Light | `RearFogLight` |
| Side Lights 图标：两个灯的轮廓，向左和向右发出光线 | Side Lights | `SideLights` |
| Stability Control 图标：一辆汽车后面有波浪线的轮廓 | Stability Control | `StabilityControl` |
| Stability Control Off 图标：一辆汽车后面有波浪线的轮廓，下方有 "OFF" 字样 | Stability Control Off | `StabilityControlOff` |
| Tire Monitor 图标：轮胎横截面的轮廓，上面有一个感叹号 | Tire Monitor | `TireMonitor` |
| Traction Control 图标：轮胎横截面的轮廓，标注有 "TC" | Traction Control | `TractionControl` |
| Traction Control Off 图标：轮胎横截面的轮廓，标注有 "TC"，整个图像上有一条斜线 | Traction Control Off | `TractionControlOff` |
| Traction Control Failure 图标：轮胎横截面的轮廓，标注有 "TC"，旁边有一个感叹号 | Traction Control Failure | `TractionControlFailure` |
| Turn Signal Left 图标：一个指向左侧的实心箭头 | Turn Signal Left | `TurnSignalLeft` |
| Turn Signal Right 图标：一个指向右侧的实心箭头 | Turn Signal Right | `TurnSignalRight` |

**无线图标**

| 图标 | 图标名称 | Programmatic Use 值 |
| --- | --- | --- |
| Network 图标：无线互联网连接图标 | Network | `Network` |
| Network No Signal 图标：无线互联网连接图标变灰，旁边有一个带叉的圆圈 | Network No Signal | `NetworkNoSignal` |
| Network Transmission 图标：一个无线互联网信号塔 | Network Transmission | `NetworkTransmission` |
| Network3G 图标：无线互联网连接图标，旁边有 "3G" | Network3G | `Network3G` |
| Network4G 图标：无线互联网连接图标，旁边有 "4G" | Network4G | `Network4G` |
| Network5G 图标：无线互联网连接图标，旁边有 "4G" | Network5G | `Network5G` |

#### 提示

- 您可以使用工具条中的模块选项卡更改 Lamp 模块的图标。
- Dashboard 库中包含为每个图标预配置了 Lamp 模块的库。
- 如果您想要在选择图标的能力之外自定义 Lamp 模块的外观，请考虑使用 Customizable Blocks 库中的 Lamp 模块设计您自己的指示灯。

#### 编程使用

|  |
| --- |
| **模块参数**：`Icon` |
| **类型**：string | character vector |
| **默认值**：`'Default'` |

### **Label** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：character vector |
| **值**：`'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**：`'Top'` |

### **Opacity** — 模块不透明度 `1`（默认）| 标量

模块不透明度，指定为介于 0 和 1 之间的标量值。

**示例：** `0.5`

#### 编程使用

|  |
| --- |
| **模块参数**：`Opacity` |
| **类型**：scalar |
| **默认值**：`1` |
## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时被忽略。

## 版本历史

**在 R2015a 中引入**

## 描述

在灯上显示反映信号值的颜色

Lamp 模块显示指示所连接信号值的颜色。要将 Lamp 模块配置为在仿真期间提供您需要的信息，请指定一个或多个状态，这些状态将信号值与 Lamp 模块要显示的颜色配对。您可以将 Lamp 模块与其他 Dashboard 模块一起使用，为您的模型构建交互式控件和指示器仪表板。

### Lamp 图标

您可以通过选择内置图标之一或上传自己的自定义图标来更改 Lamp 模块的外观。内置图标包括基本形状、汽车指示灯和无线图标。您可以使用 **Icon** 参数或使用工具条中的模块选项卡更改 Lamp 模块的图标。Dashboard 库还包含为每个图标预配置了 Lamp 模块版本的库。有关完整详细信息，请参阅 Icon。

Lamp 图标下拉菜单，显示基本形状图标、汽车指示灯、无线图标以及选择自定义图标的选项

如果您想要在选择图标的能力之外自定义 Lamp 模块的外观，请考虑使用 Customizable Blocks 库中的 Lamp 模块设计您自己的指示灯。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在该模块上并点击 Connect 按钮 。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中点击 Connect 按钮。

要将显示模块连接到模型中的信号或更改显示模块的连接，请进入连接模式。选择要连接的信号线。从出现的列表中，选择要连接的信号。然后，将鼠标悬停在 Dashboard 模块上并点击 Done Connecting 按钮 。要查看 Dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 流程图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画展示了如何将 Lamp 模块连接到您的模型。

一个未连接的 Lamp 模块连接到 Ramp 模块发送到 Terminator 模块的信号。
