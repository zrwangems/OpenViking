---
type: simulink-block
title: 'Simulation 3D Aircraft'
family: 'animation'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3daircraft'
documentation_source_path: 'simulation3daircraft.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Aircraft

## 端口

### 输入

### **Translation** — 飞行器平移 `11`-by-`3` 数组 | `12`-by-`3` 数组 | `15`-by-`3` 数组 | `30`-by-`3` 数组 | `57`-by-`3` 数组

飞行器平移，指定为：

- `11`-by-`3` 数组 — 飞行器 **类型** 为 `Sky Hogg`。
- `12`-by-`3` 数组 — 飞行器 **类型** 为 `Airliner`。
- `15`-by-`3` 数组 — 飞行器 **类型** 为 `General Aviation`。
- `30`-by-`3` 数组 — 飞行器 **类型** 为 `Air Transport`。
- `57`-by-`3` 数组 — 飞行器 **类型** 为 `Custom`。

该信号包含以 meters 为单位的平移 [X, Y, Z]，数组的每一行对应飞行器的一个骨骼。

该平移适用于 `Airliner` 类型的以下骨骼：

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| LEFT\_ENGINE | 2 |
| RIGHT\_ENGINE | 3 |
| RUDDER | 4 |
| ELEVATOR | 5 |
| LEFT\_AILERON | 6 |
| RIGHT\_AILERON | 7 |
| FLAPS | 8 |
| NOSE\_WHEEL\_STRUT | 9 |
| NOSE\_WHEEL | 10 |
| LEFT\_WHEEL | 11 |
| RIGHT\_WHEEL | 12 |

该平移适用于 `Sky Hogg` 类型的以下骨骼：

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| PROPELLER | 2 |
| RUDDER | 3 |
| ELEVATOR | 4 |
| LEFT\_AILERON | 5 |
| RIGHT\_AILERON | 6 |
| FLAPS | 7 |
| NOSE\_WHEEL\_STRUT | 8 |
| NOSE\_WHEEL | 9 |
| LEFT\_WHEEL | 10 |
| RIGHT\_WHEEL | 11 |

该平移适用于 `General Aviation` 类型的以下骨骼：

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| RUDDER | 3 |
| ELEVATOR | 4 |
| LEFT\_AILERON | 5 |
| RIGHT\_AILERON | 6 |
| FLAPS | 7 |
| LEFT\_SPOILER | 8 |
| RIGHT\_SPOILER | 9 |
| NOSE\_GEAR | 10 |
| NOSE\_WHEEL | 11 |
| LEFT\_GEAR | 12 |
| LEFT\_WHEEL | 13 |
| RIGHT\_GEAR | 14 |
| RIGHT\_WHEEL | 15 |

该平移适用于 `Air Transport` 类型的以下骨骼：

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| ENGINE2 | 3 |
| ENGINE3 | 4 |
| ENGINE4 | 5 |
| RUDDER | 6 |
| ELEVATOR | 7 |
| HORIZONTAL\_STAB | 8 |
| LEFT\_AILERON | 9 |
| RIGHT\_AILERON | 10 |
| FLAPS1 | 11 |
| FLAPS2 | 12 |
| LEFT\_SPOILER | 13 |
| RIGHT\_SPOILER | 14 |
| NOSE\_GEAR | 15 |
| NOSE\_WHEEL | 16 |
| NOSE\_GEAR\_DOOR1 | 17 |
| NOSE\_GEAR\_DOOR2 | 18 |
| LEFT\_GEAR | 19 |
| LEFT\_WHEEL | 20 |
| LEFT\_GEAR\_LINK | 21 |
| LEFT\_GEAR\_DOOR1 | 22 |
| LEFT\_GEAR\_DOOR2 | 23 |
| LEFT\_GEAR\_DOOR2\_2 | 24 |
| RIGHT\_GEAR | 25 |
| RIGHT\_WHEEL | 26 |
| RIGHT\_GEAR\_LINK | 27 |
| RIGHT\_GEAR\_DOOR1 | 28 |
| RIGHT\_GEAR\_DOOR2 | 29 |
| RIGHT\_GEAR\_DOOR2\_2 | 30 |

该平移适用于 `Custom` 类型的以下骨骼：

| 骨骼 | 索引 |
| --- | --- |
| `BODY` | 1 |
| `ENGINE1` | 2 |
| `ENGINE1_PROP` | 3 |
| `ENGINE2` | 4 |
| `ENGINE2_PROP` | 5 |
| `ENGINE3` | 6 |
| `ENGINE3_PROP` | 7 |
| `ENGINE4` | 8 |
| `ENGINE4_PROP` | 9 |
| `ENGINE5` | 10 |
| `ENGINE5_PROP` | 11 |
| `ENGINE6` | 12 |
| `ENGINE6_PROP` | 13 |
| `ENGINE7` | 14 |
| `ENGINE7_PROP` | 15 |
| `ENGINE8` | 16 |
| `ENGINE8_PROP` | 17 |
| `ENGINE9` | 18 |
| `ENGINE9_PROP` | 19 |
| `ENGINE10` | 20 |
| `ENGINE10_PROP` | 21 |
| `ENGINE11` | 22 |
| `ENGINE11_PROP` | 23 |
| `ENGINE12` | 24 |
| `ENGINE12_PROP` | 25 |
| `ENGINE13` | 26 |
| `ENGINE13_PROP` | 27 |
| `ENGINE14` | 28 |
| `ENGINE14_PROP` | 29 |
| `ENGINE15` | 30 |
| `ENGINE15_PROP` | 31 |
| `ENGINE16` | 32 |
| `ENGINE16_PROP` | 33 |
| `WING1` | 34 |
| `WING1_LEFT_FLAP` | 35 |
| `WING1_RIGHT_FLAP` | 36 |
| `WING1_LEFT_AILERON` | 37 |
| `WING1_RIGHT_AILERON` | 38 |
| `WING1_LEFT_SPOILER` | 39 |
| `WING1_RIGHT_SPOILER` | 40 |
| `WING2` | 41 |
| `WING2_LEFT_FLAP` | 42 |
| `WING2_RIGHT_FLAP` | 43 |
| `HORIZONTAL_STABILIZER` | 44 |
| `LEFT_ELEVATOR` | 45 |
| `RIGHT_ELEVATOR` | 46 |
| `LEFT_RUDDER` | 47 |
| `RIGHT_RUDDER` | 48 |
| `NOSE_GEAR` | 49 |
| `NOSE_WHEEL` | 50 |
| `NOSE_GEAR_DOOR` | 51 |
| `LEFT_GEAR` | 52 |
| `LEFT_WHEEL` | 53 |
| `LEFT_GEAR_DOOR` | 54 |
| `RIGHT_GEAR` | 55 |
| `RIGHT_WHEEL` | 56 |
| `RIGHT_GEAR_DOOR` | 57 |

**Data Types:** `single` | `double`

### **Rotation** — 飞行器和机轮旋转 `11`-by-`3` 数组 | `12`-by-`3` 数组 | `15`-by-`3` 数组 | `30`-by-`3` 数组 | `57`-by-`3` 数组

飞行器旋转，指定为：

- `11`-by-`3` 数组 — 飞行器 **类型** 为 `Sky Hogg`。
- `12`-by-`3` 数组 — 飞行器 **类型** 为 `Airliner`。
- `15`-by-`3` 数组 — 飞行器 **类型** 为 `General Aviation`。
- `30`-by-`3` 数组 — 飞行器 **类型** 为 `Air Transport`。
- `57`-by-`3` 数组 — 飞行器 **类型** 为 `Custom`。

该旋转适用于 Translation 端口所列的相同骨骼。

该信号包含以 radians 为单位的旋转 [roll, pitch, yaw]，数组的每一行对应飞行器的一个骨骼。

**Data Types:** `single` | `double`

### **LightStates** — 飞行器灯光控制 1-by-7 的 double 值向量

飞行器灯光控制，指定为 1-by-7 的 double 值向量。向量的每个元素打开（`1`）或关闭（`0`）特定的飞行器灯光组。该向量的顺序如下：

- `LANDING_LIGHTS`
- `TAXI_LIGHTS`
- `ANTICOLLISION_BEACONS`
- `WINGTIP_STROBE_LIGHTS`
- `TAIL_STROBE_LIGHTS`
- `NAVIGATION_LIGHTS`
- `POSITION_LIGHTS`

#### 依赖关系

要启用此端口，请将 **灯光配置** 参数设置为 `Configurable lights`。

**Data Types:** `single` | `double`

### **Scale** — 网格缩放 `[1 1 1]`（默认）| 1-by-3 数组

网格缩放，指定为 1-by-3 数组。

#### 依赖关系

要启用此端口，请将 **缩放源** 参数设置为 `Port`。
### 输出

### **Altitude** — 飞行器高度 1-by-4 向量

飞行器高度，返回为 1-by-4 向量。四个高度按顺序为：

- `aircraft_body`
- `aircraft_front_tire`
- `aircraft_left_tire`
- `aircraft_right_tire`

#### 依赖关系

要启用此端口，请选中 **启用高度传感器** 复选框。

**Data Types:** `double`

### **WoW** — Weight on wheels `1` | `0`

飞行器 Weight on wheels 逻辑开关，如果任一接触位置或主起落架轮胎（左或右）在地面上，则返回 `1`（true）。否则，返回 `0`（false）。

#### 依赖关系

要启用此端口，请选中 **启用高度和 Wow 传感器** 复选框。

**Data Types:** `Boolean`

## 参数

### **采样时间** — 采样时间 `-1`（默认）| real scalar

采样时间，*Ts*。图形帧率是采样时间的倒数。

#### 程序化使用

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: character vector |
| **值**: real scalar |
| **默认**: `'-1'` |

### 飞行器

### **类型** — 飞行器类型 `Sky Hogg`（默认）| `Airliner` | `General Aviation` | `Air Transport` | `Custom`

飞行器类型，指定为 `Sky Hogg`、`Airliner`、`General Aviation`、`Air Transport` 或 `Custom`。

#### 依赖关系

设置此参数要求将 **初始平移** 和 **初始旋转** 参数设置为匹配的数组大小。未能正确设置这些数组大小会导致错误。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Mesh` |
| **类型**: character vector |
| **值**: `'Sky Hogg'` | `'Airliner'` | `'General Aviation'` | `'Air Transport'` | `'Custom'` |
| **默认**: `'Sky Hogg'` |

### **通用航空网格的路径** — 通用航空网格的路径 `/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'`（默认）| character vector

通用航空网格的路径，指定为 character vector。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

- 要启用此参数，请将 **类型** 设置为 `General Aviation`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `MeshPathGA` |
| **类型**: character vector |
| **值**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'` |
| **默认**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'` |

### **航空运输网格的路径** — 航空运输网格的路径 `/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport`（默认）| character vector

航空运输网格的路径，指定为 character vector。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

- 要启用此参数，请将 **类型** 设置为 `Air Transport`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `MeshPathAT` |
| **类型**: character vector |
| **值**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport'` |
| **默认**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport'` |

### **自定义网格的路径** — 自定义网格的路径 `/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20`（默认）| `/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_Aircraft.SK_Aircraft` | character vector

自定义网格的路径，指定为 character vector。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

- 要启用此参数，请将 **类型** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `MeshPath` |
| **类型**: character vector |
| **值**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20'` | `'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_Aircraft.SK_Aircraft'` |
| **默认**: `'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20'` |

### **颜色** — 飞行器颜色 `Red`（默认）| `Orange` | `Yellow` | `Green` | `Cyan` | `Blue` | `Black` | `White` | `Silver` | `Metal`

飞行器颜色，指定为 `Red`、`Orange`、`Yellow`、`Green`、`Cyan`、`Blue`、`Black`、`White`、`Silver` 或 `Metal`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AircraftColor` |
| **类型**: character vector |
| **值**: `'Red'` | `'Orange'` | `'Yellow'` | `'Green'` | `'Cyan'` | `'Blue'` | `'Black'` | `'White'` | `'Silver'` | `'Metal'` |
| **默认**: `'Red'` |

### **名称** — 飞行器名称 `SimulinkVehicle1`（默认）| character vector

飞行器名称，指定为 character vector。默认情况下，当您在模型中使用该模块时，模块会将 **名称** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中其他 simulation 3D 模块的数量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ActorName` |
| **类型**: character vector |
| **值**: scalar |
| **默认**: `'SimulinkVehicle1'` |

### **初始平移 (m)** — 飞行器的初始平移 `zeros(11,3)`（默认）| `11`-by-`3` 数组 | `12`-by-`3` 数组 | `15`-by-`3` 数组 | `30`-by-`3` 数组 | `57`-by-`3` 数组

飞行器的初始平移，指定为 `11`-by-`3`、`12`-by-`3`、`15`-by-`3`、`30`-by-`3` 或 `57`-by-`3` 数组。

#### 依赖关系

此参数必须与您在 **类型** 中设置的飞行器类型匹配。未能正确设置这些数组大小会导致错误。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Translation` |
| **类型**: character vector |
| **值**: `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array |
| **默认**: `'zeros(11,3)'` |

**Data Types:** `single` | `double`

### **初始旋转 (rad)** — 飞行器旋转 `zeros(11,3)`（默认）| `11`-by-`3` 数组 | `12`-by-`3` 数组 | `15`-by-`3` 数组 | `30`-by-`3` 数组 | `57`-by-`3` 数组

飞行器的初始旋转，指定为 `11`-by-`3`、`12`-by-`3`、`15`-by-`3`、`30`-by-`3` 或 `57`-by-`3` 数组。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Rotation` |
| **类型**: character vector |
| **值**: `11`-by-`3` array | `12`-by-`3` array | `15`-by-`3` array | `30`-by-`3` array | `57`-by-`3` array |
| **默认**: `'zeros(11,3)'` |

**Data Types:** `single` | `double`

### **缩放源** — 缩放源 `Dialog`（默认）| `Port`

缩放源，指定为 `Dialog` 或 `Port`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ScaleInputPort` |
| **类型**: character vector |
| **值**: `'Dialog'` | `'Port'` |
| **默认**: `'Dialog'` |

### **初始缩放** — 初始网格缩放 `[1 1 1]`（默认）| 1-by-3 数组

初始网格缩放，指定为 1-by-3 数组。

#### 依赖关系

要启用此参数，请将 **缩放源** 设置为 `Port`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InitialScale` |
| **类型**: character vector |
| **值**: `1`-by-`3` array |
| **默认**: `'[1 1 1]'` |

**Data Types:** `single` | `double`

### **缩放** — 网格缩放 `[1 1 1]`（默认）| 1-by-3 数组

网格缩放，指定为 1-by-3 数组。

#### 依赖关系

要启用此参数，请将 **缩放源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `Scale` |
| **类型**: character vector |
| **值**: `1`-by-`3` array |
| **默认**: `'[1 1 1]'` |

**Data Types:** `single` | `double`

### 高度传感器

### **启用高度和 WoW 传感器** — 高度和 WoW 传感器 on（默认）| off

要启用高度和 WoW（weight on wheels）传感器，请选中此复选框。否则，清除此复选框。

- 高度传感器返回飞行器原点下方到地面的垂直距离，模拟雷达高度计。有关详细信息，请参阅 Altitude Sensors。
- 如果任一主起落架机轮在地面上，则 WoW 传感器返回逻辑 true（`1`），否则返回 false（`0`）。有关详细信息，请参阅 WoW Sensors。

#### 程序化使用

|  |
| --- |
| **模块参数**: `IsGHSensorEnabled` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'on'` |

### **在查看器中显示传感器射线** — 显示传感器射线的选项 off（默认）| on

要在查看器中显示传感器射线，请选中此复选框。否则，清除此复选框。

#### 依赖关系

要启用此参数，请选中 **启用高度和 Wow 传感器** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AreGHRaysVisible` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **将向量输出解释为 1-D** — 控制传感器输出端口上的重塑 off（默认）| on

控制 **Altitude** **WoW** 传感器输出端口上是否发生重塑：

- 选中此复选框以启用重塑。
- 清除此复选框以禁用重塑。

#### 程序化使用

|  |
| --- |
| **模块参数**: `IsOutputReshapeEnabled` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **射线长度 (m)** — 射线长度 `1524`（默认）| real scalar

射线长度，指定为以 meters 为单位的 real scalar。射线长度限制高度检测。例如，如果飞行器原点下方到地面的垂直距离大于射线长度加上飞行器机体 *Z* 偏移，则高度传感器会将第一个值返回为 `-1`。

#### 依赖关系

要启用此参数，请选中 **启用高度传感器** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `GHRayLength` |
| **类型**: character vector |
| **值**: real scalar |
| **默认**: `'1524'` |

### **机体 Z 偏移 (m)** — 飞行器机体 *Z* 偏移 `0.90`（默认）| real scalar

飞行器机体 *Z* 偏移，指定为以 meters 为单位的 real scalar。

#### 依赖关系

要启用此参数，请选中 **启用高度传感器** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `GHBodyOffset` |
| **类型**: character vector |
| **值**: real scalar |
| **默认**: `'0.90'` |

### **前轮胎半径 (m)** — 前起落架轮胎半径 `0.21`（默认）| real scalar

前起落架轮胎半径，指定为以 meters 为单位的 real scalar。前起落架高度射线起始于前起落架轴中心加上前起落架轮胎半径 *Z* 偏移。

#### 依赖关系

要启用此参数，请选中 **启用高度传感器** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `GHFrontTireRadius` |
| **类型**: character vector |
| **值**: real scalar |
| **默认**: `'0.21'` |

### **左轮胎半径 (m)** — 左起落架轮胎半径 0.21（默认）| real scalar

左起落架轮胎半径，指定为以 meters 为单位的 real scalar。

#### 依赖关系

要启用此参数，请选中 **启用高度传感器** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `GHLeftTireRadius` |
| **类型**: character vector |
| **值**: real scalar |
| **默认**: `'0.21'` |

### **右轮胎半径 (m)** — 右起落架轮胎半径 0.21（默认）| real scalar

右起落架轮胎半径，指定为以 meters 为单位的 real scalar。

#### 依赖关系

要启用此参数，请选中 **启用高度传感器** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `GHRightTireRadius` |
| **类型**: character vector |
| **值**: real scalar |
| **默认**: `'0.21'` |

### **WoW 传感器容差 (m)** — Wow 传感器容差 `0.05`（默认）| real scalar

Wow 传感器容差，指定为 real scalar。

#### 依赖关系

要启用此参数，请选中 **启用高度和 Wow 传感器** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `WoWSensorTolerance` |
| **类型**: character vector |
| **值**: real scalar |
| **默认**: `'0.05'` |

### 灯光配置

### **灯光配置** — 灯光配置选项 `Automatic lights`（默认）| `Configurable lights` | `Lights off`

灯光配置选项

- `Automatic lights` — 使用默认飞行器灯光配置，该配置提供逼真的模式循环。
- `Configurable lights` — 配置飞行器灯光参数。
- `Lights off` — 关闭所有飞行器灯光。

#### 依赖关系

- 将此参数设置为 `Automatic lights` 会禁用所有其他 **灯光配置** 参数的可配置性。该模块使用飞行器灯光值的默认参数值。
- 将此参数设置为 `Configurable lights` 会根据飞行器类型启用 **灯光配置** 参数的可配置性。
- 将 **类型** 设置为这些飞行器类型，并将 **灯光配置** 设置为 `Configurable lights`，会启用每种飞行器所使用的灯光参数的可配置性。

  | 类型 | 灯光 | 灯光参数 |
  | --- | --- | --- |
  | `Airliner` | **着陆灯** | - **着陆灯强度 (cd)** - **着陆灯锥半角 (deg)** |
  | **滑行灯** | - **滑行灯强度 (cd)** - **滑行灯锥半角 (deg)** |
  | **红/绿导航灯** | **导航灯强度** |
  | **白色频闪灯** | - **频闪灯强度** - **翼尖频闪周期 (s)** - **翼尖频闪脉冲宽度 (% of period)** - **尾部频闪周期 (s)** - **尾部频闪脉冲宽度 (% of period)** |
  | **红色信标灯** | - **信标灯强度** - **信标周期 (s)** - **信标脉冲宽度 (% of period)** |
  | `Sky Hogg` | **着陆灯** | - **着陆灯强度 (cd)** - **着陆灯锥半角 (deg)** |
  | **红/绿导航灯** | **导航灯强度** |
  | **白色频闪灯** | - **频闪灯强度** - **尾部频闪周期 (s)** - **尾部频闪脉冲宽度 (% of period)** |
  | **红色信标灯** | - **信标灯强度** - **信标周期 (s)** - **信标脉冲宽度 (% of period)** |
  | `General Aviation`、`Air Transport` 或 `Custom` | **着陆灯** | - **着陆灯强度 (cd)** - **着陆灯锥半角 (deg)** - **左着陆灯位置** - **左着陆灯方向** - **右着陆灯位置** - **右着陆灯方向** |
  | **滑行灯** | - **滑行灯强度 (cd)** - **滑行灯锥半角 (deg)** - **滑行灯位置** - **滑行灯方向 (deg)** |
  | **红/绿导航灯** | **导航灯强度** |
  | **白色导航灯** | **位置灯强度** |
  | **白色频闪灯** | - **频闪灯强度** - **翼尖频闪周期 (s)** - **翼尖频闪脉冲宽度 (% of period)** - **尾部频闪周期 (s)** - **尾部频闪脉冲宽度 (% of period)** |
  | **红色信标灯** | - **信标灯强度** - **信标周期 (s)** - **信标脉冲宽度 (% of period)** |
- 将此参数设置为 `Lights off` 会禁用所有其他 **灯光配置** 参数的可配置性。该模块会关闭所有飞行器灯光。

#### 程序化使用

|  |
| --- |
| **模块参数**: `LightsConfig` |
| **类型**: character vector |
| **值**: `'Automatic lights'` | `'Configurable lights'` | `'Lights off'` |
| **默认**: `'Automatic lights'` |

### **着陆灯强度 (cd)** — 着陆灯强度 30000（默认）| positive scalar

着陆灯强度，指定为以 candela 为单位的 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `LandingLightIntensity` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'30000'` |

### **着陆灯锥半角 (deg)** — 着陆灯锥半角 15（默认）| positive scalar

着陆灯锥半角，指定为以 degrees 为单位的 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `LandingLightConeAngle` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'15'` |

### **左着陆灯位置** — 左着陆灯位置 `[0 0 0]`（默认）| 3-element vector

左着陆灯相对于骨骼网格关联骨骼的位置，指定为 3-element vector。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `CustomLeftLandingLightLocation` |
| **类型**: character vector |
| **值**: 3-element vector |
| **默认**: `'[0 0 0]'` |

### **左着陆灯方向 (deg)** — 左着陆灯方向 `[0 0 0]`（默认）| 3-element vector

左着陆灯相对于骨骼网格关联骨骼的方向，指定为 3-element vector。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `CustomLeftLandingLightOrientation` |
| **类型**: character vector |
| **值**: 3-element vector |
| **默认**: `'[0 0 0]'` |

### **右着陆灯位置** — 右着陆灯位置 `[0 0 0]`（默认）| 3-element vector

右着陆灯相对于骨骼网格关联骨骼的位置，指定为 3-element vector。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `CustomRightLandingLightLocation` |
| **类型**: character vector |
| **值**: 3-element vector |
| **默认**: `'[0 0 0]'` |

### **右着陆灯方向 (deg)** — 右着陆灯方向 `[0 0 0]`（默认）| 3-element vector

右着陆灯相对于骨骼网格关联骨骼的方向，指定为 3-element vector。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `CustomRightLandingLightOrientation` |
| **类型**: character vector |
| **值**: 3-element vector |
| **默认**: `'[0 0 0]'` |

### **滑行灯强度 (cd)** — 滑行灯强度 `150000`（默认）| positive scalar

滑行灯强度，指定为以 candela 为单位的 positive scalar。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `Airliner`、`General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `TaxiLightIntensity` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'150000'` |

### **滑行灯锥半角 (deg)** — 滑行灯锥半角 `36`（默认）| positive scalar

滑行灯锥半角，指定为以 degrees 为单位的 positive scalar。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `Airliner`、`General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `TaxiLightConeAngle` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'36'` |

### **滑行灯位置** — 滑行灯位置 `[0 0 0]`（默认）| 3-element vector

滑行灯相对于骨骼网格关联骨骼的位置，指定为 3-element vector

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `CustomTaxiLightLocation` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'[0 0 0]'` |

### **滑行灯方向 (deg)** — 滑行灯方向 `[0 0 0]`（默认）| 3-element vector

滑行灯相对于骨骼网格关联骨骼的方向，指定为 3-element vector

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `CustomTaxiLightOrientation` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'[0 0 0]'` |

### **导航灯强度** — 导航灯强度 `500`（默认）| positive scalar

导航灯强度，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `NavLightIntensity` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'500'` |

### **位置灯强度** — 位置灯强度 `500`（默认）| positive scalar

位置灯强度，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PositionLightIntensity` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'500'` |

### **频闪灯强度** — 频闪灯强度 `5000`（默认）| positive scalar

频闪灯强度，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `StrobeLightIntensity` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'5000'` |

### **翼尖频闪周期 (s)** — 翼尖频闪周期 `1.5`（默认）| positive scalar

翼尖频闪周期，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `Airliner`、`General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `WingtipStrobePeriod` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'1.5'` |

### **翼尖频闪脉冲宽度 (% of period)** — 翼尖频闪脉冲宽度 `6`（默认）| positive scalar

翼尖频闪脉冲宽度，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `Airliner`、`General Aviation`、`Air Transport` 或 `Custom`，并将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `WingtipStrobePulseWidth` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'6'` |

### **尾部频闪周期 (s)** — 尾部频闪周期 `1.5`（默认）| positive scalar

尾部频闪周期，指定为以 seconds 为单位的 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `TailStrobePeriod` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'1.5'` |

### **尾部频闪脉冲宽度 (% of period)** — 尾部频闪脉冲宽度 `6`（默认）| positive scalar

尾部频闪脉冲宽度，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `TailStrobePulseWidth` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'6'` |

### **信标灯强度** — 信标灯强度 `4000`（默认）| positive scalar

信标灯强度，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `BeaconLightIntensity` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'4000'` |

### **信标周期 (s)** — 信标周期 `1.5`（默认）| positive scalar

信标周期，指定为以 seconds 为单位的 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `BeaconPeriod` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'1.5'` |

### **信标脉冲宽度 (% of period)** — 信标脉冲宽度 `10`（默认）| positive scalar

信标脉冲宽度，指定为 positive scalar。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `BeaconPulseWidth` |
| **类型**: character vector |
| **值**: positive scalar |
| **默认**: `'10'` |

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024b：Simulation 3D Environment：为 Simulation 3D Aircraft 缩放网格

现在，您可以使用 **缩放** 参数或 **Scale** 端口更改 Simulation 3D Aircraft 模块网格的大小。默认缩放为 `[1 1 1]` 的 1-by-3 向量。

要启用这些参数或端口，请使用 **缩放源** 参数。

- `Dialog` — 启用 **缩放** 参数。
- `Port` — 启用 **Scale** 端口和 **初始缩放** 参数。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Aircraft 模块对模型进行仿真需要 Simulink 3D Animation。

### R2024a：Simulation 3D Aircraft 模块支持单精度输入

Simulation 3D Aircraft 模块现在支持 **Translation** 和 **Rotation** 输入端的单精度和双精度输入。在 R2024a 之前，该模块对这些端口仅支持双精度输入。

### R2023a：Simulation 3D Aircraft 模块更新

Simulation 3D Aircraft 模块有以下更改：

- 模块 **初始值** 选项卡的内容已移动到 **初始值** 部分下的 **飞行器** 选项卡。
- **高度传感器** 选项卡有以下更改：

  - **Enable altitude sensor** 已重命名为 **Enable Altitude and WoW sensors**。

    从 R2023a 开始，WoW（weight on wheels）传感器使用您在模块封装中指定的高度传感器射线和偏移来确定一个或多个机轮或地面接触位置是否接触地面。
  - **Enable visible sensor rays** 已重命名为 **Show sensor rays in viewer**。
  - **Aircraft body Z offset (in meters)** 已重命名为 **Body Z offset (m)**。
  - **Front gear tire radius (in meters)** 已重命名为 **Front tire radius (m)**。
  - **Left gear tire radius (in meters)** 已重命名为 **Left tire radius (m)**。
  - **Right gear tire radius (in meters)** 已重命名为 **Right tire radius (m)**。
  - **WoW sensor tolerance**，用于设置 WoW 传感器容差。
  - 新参数 **Interpret vector outputs as 1-D**，用于控制 **Altitude** 和 **WoW** 传感器输出端口上是否发生重塑。

### R2022a：支持自定义网格和飞行器灯光

该模块现在支持：

- 使用 **自定义网格路径** 参数指定自定义飞行器网格。要启用此参数，请将 **类型** 设置为 `Custom`。
- 使用新的 **灯光配置** 选项卡配置飞行器灯光。
- 在 **颜色** 参数中为飞行器机体提供更多颜色。

## 描述

在 3D 环境中实现飞行器

**注意**

使用 Simulation 3D Aircraft 模块对模型进行仿真需要 Simulink® 3D Animation™。

Simulation 3D Aircraft 模块使用平移和旋转在 3D 可视化环境中实现飞行器，以放置飞行器。

要使用此模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将此模块的 **采样时间** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

模块输入使用飞行器 north-east-down (NED) *right-handed* (RH) *Cartesian* 坐标系。

- *X* 轴 — 沿飞行器纵轴，指向前方
- *Y* 轴 — 沿飞行器横轴，指向右侧
- *Z* 轴 — 指向下方

有关详细信息，请参阅 Fundamental Coordinate System Concepts。

**提示**

验证 Simulation 3D Aircraft 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Aircraft 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备好这些数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Aircraft — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。

### 骨架、骨骼和网格

Unreal® 使用 *skeleton*、*bones* 和 *mesh* 定义 3D 模型。骨架由一组骨骼组成。网格是骨架的外覆盖层。飞行器部件是网格的各个部分，例如副翼或机轮，它们链接到骨骼。有关详细信息，请参阅 https://docs.unrealengine.com/4.27/AnimatingObjects/SkeletalMeshAnimation/Skeleton/。

有关 Simulation 3D Aircraft 模块平移输入数组如何连接到飞行器类型的详细信息，请参阅 Algorithms。
