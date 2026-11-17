---
type: simulink-block
title: 'Simulation 3D Aircraft'
family: 'aeroblks'
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

### **Translation** — 飞行器平移 `11`×`3` 数组 | `12`×`3` 数组 | `15`×`3` 数组 | `30`×`3` 数组 | `57`×`3` 数组

飞行器平移，指定为：

- `11`×`3` 数组 — 飞行器
  **Type** 为 `Sky Hogg`。
- `12`×`3` 数组 — 飞行器
  **Type** 为 `Airliner`。
- `15`×`3` 数组 — 飞行器
  **Type** 为 `General Aviation`。
- `30`×`3` 数组 — 飞行器
  **Type** 为 `Air Transport`。
- `57`×`3` 数组 — 飞行器
  **Type** 为 `Custom`。

该信号包含平移 [X, Y, Z]，单位为米，数组的每一行对应飞行器的一个骨骼。

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

**数据类型：** `single` | `double`

### **Rotation** — 飞行器和机轮旋转 `11`×`3` 数组 | `12`×`3` 数组 | `15`×`3` 数组 | `30`×`3` 数组 | `57`×`3` 数组

飞行器旋转，指定为：

- `11`×`3` 数组 — 飞行器
  **Type** 为 `Sky Hogg`。
- `12`×`3` 数组 — 飞行器
  **Type** 为 `Airliner`。
- `15`×`3` 数组 — 飞行器
  **Type** 为 `General Aviation`。
- `30`×`3` 数组 — 飞行器
  **Type** 为 `Air Transport`。
- `57`×`3` 数组 — 飞行器
  **Type** 为 `Custom`。

该旋转适用于 Translation 端口中列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，单位为弧度，数组的每一行对应飞行器的一个骨骼。

**数据类型：** `single` | `double`

### **LightStates** — 飞行器灯光控制 1×7 双精度值向量

飞行器灯光控制，指定为 1×7 双精度值向量。向量的每个元素打开（`1`）或关闭（`0`）特定的飞行器灯光组。该向量具有以下顺序：

- `LANDING_LIGHTS`
- `TAXI_LIGHTS`
- `ANTICOLLISION_BEACONS`
- `WINGTIP_STROBE_LIGHTS`
- `TAIL_STROBE_LIGHTS`
- `NAVIGATION_LIGHTS`
- `POSITION_LIGHTS`

#### 依赖关系

要启用此端口，请将 **Light Configuration** 参数设置为 `Configurable lights`。

**数据类型：** `single` | `double`

### **Scale** — 网格缩放 `[1 1 1]`（默认）| 1×3 数组

网格缩放，指定为 1×3 数组。

#### 依赖关系

要启用此端口，请将 **Scale source** 参数设置为 `Port`。
### 输出

### **Altitude** — 飞行器姿态 1×4 向量

飞行器高度，以 1×4 向量返回。四个高度按顺序为：

- `aircraft_body`
- `aircraft_front_tire`
- `aircraft_left_tire`
- `aircraft_right_tire`

#### 依赖关系

要启用此端口，请选中 **Enable altitude sensor** 复选框。

**数据类型：** `double`

### **WoW** — 机轮承重 `1` | `0`

飞行器机轮承重逻辑开关，如果任一接触位置或主起落架轮胎（左或右）在地面上，则返回 `1`（true）。否则，返回 `0`（false）。

#### 依赖关系

要启用此端口，请选中 **Enable altitude and Wow sensors** 复选框。

**数据类型：** `Boolean`

## 参数

### **Sample time** — 采样时间 `-1`（默认）| 实标量

采样时间，*Ts*。图形帧率是采样时间的倒数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'-1'` |

### Aircraft

### **Type** — 飞行器类型 `Sky Hogg`（默认）| `Airliner` | `General Aviation` | `Air Transport` | `Custom`

飞行器类型，指定为 `Sky Hogg`、`Airliner`、`General Aviation`、`Air Transport` 或 `Custom`。

#### 依赖关系

设置此参数要求您将 **Initial translation** 和 **Initial rotation** 参数设置为匹配的数组大小。未能适当设置这些数组大小会导致错误。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Mesh` |
| **类型**：字符向量 |
| **值**：`'Sky Hogg'` | `'Airliner'` | `'General Aviation'` | `'Air Transport'` | `'Custom'` |
| **默认值**：`'Sky Hogg'` |

### **Path to general aviation mesh** — 通用航空网格路径 `/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'`（默认）| 字符向量

通用航空网格路径，指定为字符向量。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

- 要启用此参数，请将 **Type** 设置为 `General Aviation`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MeshPathGA` |
| **类型**：字符向量 |
| **值**：`'/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'` |
| **默认值**：`'/MathWorksAerospaceContent/Vehicles/Aircraft/GeneralAviation/Mesh/SK_GeneralAviation.SK_GeneralAviation'` |

### **Path to air transport mesh** — 航空运输网格路径 `/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport`（默认）| 字符向量

航空运输网格路径，指定为字符向量。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

- 要启用此参数，请将 **Type** 设置为 `Air Transport`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MeshPathAT` |
| **类型**：字符向量 |
| **值**：`'/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport'` |
| **默认值**：`'/MathWorksAerospaceContent/Vehicles/Aircraft/AirTransport/Mesh/SK_AirTransport.SK_AirTransport'` |

### **Path to custom mesh** — 自定义网格路径 `/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20`（默认）| `/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_Aircraft.SK_Aircraft` | 字符向量

自定义网格路径，指定为字符向量。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

- 要启用此参数，请将 **Type** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`MeshPath` |
| **类型**：字符向量 |
| **值**：`'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20'` | `'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_Aircraft.SK_Aircraft'` |
| **默认值**：`'/MathWorksAerospaceContent/Vehicles/Aircraft/Custom/Mesh/SK_HL20.SK_HL20'` |

### **Color** — 飞行器颜色 `Red`（默认）| `Orange` | `Yellow` | `Green` | `Cyan` | `Blue` | `Black` | `White` | `Silver` | `Metal`

飞行器颜色，指定为 `Red`、`Orange`、`Yellow`、`Green`、`Cyan`、`Blue`、`Black`、`White`、`Silver` 或 `Metal`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AircraftColor` |
| **类型**：字符向量 |
| **值**：`'Red'` | `'Orange'` | `'Yellow'` | `'Green'` | `'Cyan'` | `'Blue'` | `'Black'` | `'White'` | `'Silver'` | `'Metal'` |
| **默认值**：`'Red'` |

### **Name** — 飞行器名称 `SimulinkVehicle1`（默认）| 字符向量

飞行器名称，指定为字符向量。默认情况下，当您在模型中使用该模块时，模块将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中其他 simulation 3D 模块的数量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ActorName` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'SimulinkVehicle1'` |

### **Initial translation (m)** — 飞行器初始平移 `zeros(11,3)`（默认）| `11`×`3` 数组 | `12`×`3` 数组 | `15`×`3` 数组 | `30`×`3` 数组 | `57`×`3` 数组

飞行器初始平移，指定为 `11`×`3`、`12`×`3`、`15`×`3`、`30`×`3` 或 `57`×`3` 数组。

#### 依赖关系

此参数必须与您在 **Type** 中设置的飞行器类型匹配。未能适当设置这些数组大小会导致错误。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Translation` |
| **类型**：字符向量 |
| **值**：`11`×`3` 数组 | `12`×`3` 数组 | `15`×`3` 数组 | `30`×`3` 数组 | `57`×`3` 数组 |
| **默认值**：`'zeros(11,3)'` |

**数据类型：** `single` | `double`

### **Initial rotation (rad)** — 飞行器旋转 `zeros(11,3)`（默认）| `11`×`3` 数组 | `12`×`3` 数组 | `15`×`3` 数组 | `30`×`3` 数组 | `57`×`3` 数组

飞行器初始旋转，指定为 `11`×`3`、`12`×`3`、`15`×`3`、`30`×`3` 或 `57`×`3` 数组。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Rotation` |
| **类型**：字符向量 |
| **值**：`11`×`3` 数组 | `12`×`3` 数组 | `15`×`3` 数组 | `30`×`3` 数组 | `57`×`3` 数组 |
| **默认值**：`'zeros(11,3)'` |

**数据类型：** `single` | `double`

### **Scale source** — 缩放来源 `Dialog`（默认）| `Port`

缩放来源，指定为 `Dialog` 或 `Port`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ScaleInputPort` |
| **类型**：字符向量 |
| **值**：`'Dialog'` | `'Port'` |
| **默认值**：`'Dialog'` |

### **Initial scale** — 初始网格缩放 `[1 1 1]`（默认）| 1×3 数组

初始网格缩放，指定为 1×3 数组。

#### 依赖关系

要启用此参数，请将 **Scale source** 设置为 `Port`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`InitialScale` |
| **类型**：字符向量 |
| **值**：`1`×`3` 数组 |
| **默认值**：`'[1 1 1]'` |

**数据类型：** `single` | `double`

### **Scale** — 网格缩放 `[1 1 1]`（默认）| 1×3 数组

网格缩放，指定为 1×3 数组。

#### 依赖关系

要启用此参数，请将 **Scale source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Scale` |
| **类型**：字符向量 |
| **值**：`1`×`3` 数组 |
| **默认值**：`'[1 1 1]'` |

**数据类型：** `single` | `double`

### Altitude Sensor

### **Enable altitude and WoW sensors** — 高度和 WoW 传感器开启（默认）| 关闭

要启用高度和 WoW（机轮承重）传感器，请选中此复选框。否则，请清除此复选框。

- 高度传感器返回飞行器原点下方到地面的垂直距离，模拟雷达高度计。有关详细信息，请参阅 Altitude Sensors。
- 如果任一主起落架机轮在地面上，WoW 传感器返回逻辑 true（`1`），否则返回 false（`0`）。有关详细信息，请参阅 WoW Sensors。

#### 程序化使用

|  |
| --- |
| **模块参数**：`IsGHSensorEnabled` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Show sensor rays in viewer** — 在查看器中显示传感器射线的选项 关闭（默认）| 开启

要在查看器中显示传感器射线，请选中此复选框。否则，请清除此复选框。

#### 依赖关系

要启用此参数，请选中 **Enable altitude and Wow sensors** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AreGHRaysVisible` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Interpret vector outputs as 1-D** — 控制传感器输出端口上的重塑 关闭（默认）| 开启

控制是否在 **Altitude** **WoW** 传感器输出端口上发生重塑：

- 选中此复选框以启用重塑。
- 清除此复选框以禁用重塑。

#### 程序化使用

|  |
| --- |
| **模块参数**：`IsOutputReshapeEnabled` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Length of rays (m)** — 射线长度 `1524`（默认）| 实标量

射线长度，指定为以米为单位的实标量。射线长度限制了高度检测。例如，如果飞行器原点下方到地面的垂直距离大于射线长度加上飞行器机体 *Z* 偏移量，则高度传感器对第一个值返回 `-1`。

#### 依赖关系

要启用此参数，请选中 **Enable altitude sensor** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`GHRayLength` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'1524'` |

### **Body Z offset (m)** — 飞行器机体 *Z* 偏移量 `0.90`（默认）| 实标量

飞行器机体 *Z* 偏移量，指定为以米为单位的实标量。

#### 依赖关系

要启用此参数，请选中 **Enable altitude sensor** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`GHBodyOffset` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'0.90'` |

### **Front tire radius (m)** — 前起落架轮胎半径 `0.21`（默认）| 实标量

前起落架轮胎半径，指定为以米为单位的实标量。前起落架高度射线从前起落架轴中心加上前起落架轮胎半径 *Z* 偏移量处发出。

#### 依赖关系

要启用此参数，请选中 **Enable altitude sensor** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`GHFrontTireRadius` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'0.21'` |

### **Left tire radius (m)** — Left gear tire radius 0.21 (default) | real scalar

Left gear tire radius, specified as a real scalar in meters.

#### 依赖关系

要启用此参数，请选择 **Enable altitude sensor**
check box.

#### 编程使用

|  |
| --- |
| **模块参数**：`GHLeftTireRadius` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'0.21'` |

### **Right tire radius (m)** — Right gear tire radius 0.21 (default) | real scalar

Right gear tire radius, specified as a real scalar in meters.

#### 依赖关系

要启用此参数，请选择 **Enable altitude sensor**
check box.

#### 编程使用

|  |
| --- |
| **模块参数**：`GHRightTireRadius` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'0.21'` |

### **WoW sensor tolerance (m)** — Wow sensor tolerance `0.05` (default) | real scalar

Wow sensor tolerance, specified as a real scalar.

#### 依赖关系

要启用此参数，请选择 **Enable altitude and Wow sensors**
check box.

#### 编程使用

|  |
| --- |
| **模块参数**：`WoWSensorTolerance` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'0.05'` |

### Light Configuration

### **Light configuration** — Light configurations options `Automatic lights` (default) | `Configurable lights` | `Lights off`

Light configuration options

- `Automatic lights` — 使用默认的飞机照明
  configuration that provides realistic pattern cycling.
- `Configurable lights` — Configure aircraft lighting
  parameters.
- `Lights off` — Turn off all aircraft lights.

#### 依赖关系

- 将此参数设置为 `Automatic lights`
  disables the configurability of all other **Light
  Configuration** 参数。该模块使用默认参数
  值作为飞机照明值。
- 将此参数设置为 `Configurable lights`
  enables the configurability of the **Light Configuration**
  根据飞机类型设置参数。
- 将 **Type** 设置为这些飞机类型，并
  **Light Configuration** to `Configurable
  lights` enables the configurability of the lighting parameters in
  用于每种飞机。

  | Type | Lights | Light Parameters |
  | --- | --- | --- |
  | `Airliner` | **Landing lights** | - **Landing lights intensity (cd)** - **Landing lights cone half angle   (deg)** |
  | **Taxi lights** | - **Taxi lights intensity (cd)** - **Taxi lights cone half angle   (deg)** |
  | **Red/green navigation lights** | **Navigation lights intensity** |
  | **White strobe lights** | - **Strobe lights intensity** - **Wingtip strobe period (s)** - **Wingtip strobe pulse width (% of   period)** - **Tail strobe period (s)** - **Tail strobe pulse width (% of   period)** |
  | **Red beacon lights** | - **Beacon lights intensity** - **Beacon period (s)** - **Beacon pulse width (% of period)** |
  | `Sky Hogg` | **Landing lights** | - **Landing lights intensity (cd)** - **Landing lights cone half angle   (deg)** |
  | **Red/green navigation lights** | **Navigation lights intensity** |
  | **White strobe lights** | - **Strobe lights intensity** - **Tail strobe period (s)** - **Tail strobe pulse width (% of   period)** |
  | **Red beacon lights** | - **Beacon lights intensity** - **Beacon period (s)** - **Beacon pulse width (% of period)** |
  | `General Aviation`, `Air Transport`, or `Custom` | **Landing lights** | - **Landing lights intensity (cd)** - **Landing lights cone half angle   (deg)** - **Left landing light location** - **Left landing light orientation** - **Right landing light location** - **Right landing light orientation** |
  | **Taxi lights** | - **Taxi lights intensity (cd)** - **Taxi lights cone half angle   (deg)** - **Taxi lights location** - **Taxi lights orientation (deg)** |
  | **Red/green navigation lights** | **Navigation lights intensity** |
  | **White navigation lights** | **Position light intensity** |
  | **White strobe lights** | - **Strobe lights intensity** - **Wingtip strobe period (s)** - **Wingtip strobe pulse width (% of   period)** - **Tail strobe period (s)** - **Tail strobe pulse width (% of   period)** |
  | **Red beacon lights** | - **Beacon lights intensity** - **Beacon period (s)** - **Beacon pulse width (% of period)** |
- 将此参数设置为 `Lights off` 会禁用
  configurability of all other **Light Configuration**
  参数。该模块会关闭所有飞机灯光。

#### 编程使用

|  |
| --- |
| **模块参数**：`LightsConfig` |
| **类型**：character vector |
| **值**：`'Automatic lights'` | `'Configurable lights'` | `'Lights off'` |
| **默认值**：`'Automatic lights'` |

### **Landing lights intensity (cd)** — Landing lights intensity 30000 (default) | positive scalar

Landing lights intensity, specified as a positive scalar, in candela.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`LandingLightIntensity` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'30000'` |

### **Landing lights cone half angle (deg)** — Landing lights cone half angle 15 (default) | positive scalar

Landing lights cone half angle, specified as a positive scalar, in degrees.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`LandingLightConeAngle` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'15'` |

### **Left landing light location** — Left landing light location `[0 0 0]` (default) | 3-element vector

左着陆灯相对于骨骼网格关联骨骼的位置，
mesh, specified as a 3-element vector.

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomLeftLandingLightLocation` |
| **类型**：character vector |
| **值**：3-element vector |
| **默认值**：`'[0 0 0]'` |

### **Left landing light orientation (deg)** — Left landing light orientation `[0 0 0]` (default) | 3-element vector

左着陆灯相对于骨骼网格关联骨骼的方向，
mesh, specified as a 3-element vector.

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomLeftLandingLightOrientation` |
| **类型**：character vector |
| **值**：3-element vector |
| **默认值**：`'[0 0 0]'` |

### **Right landing light location** — Right landing light location `[0 0 0]` (default) | 3-element vector

右着陆灯相对于骨骼网格关联骨骼的位置，
mesh, specified as a 3-element vector.

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomRightLandingLightLocation` |
| **类型**：character vector |
| **值**：3-element vector |
| **默认值**：`'[0 0 0]'` |

### **Right landing light orientation (deg)** — Right landing light orientation `[0 0 0]` (default) | 3-element vector

右着陆灯相对于骨骼网格关联骨骼的方向，
skeletal mesh, specified as a 3-element vector.

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomRightLandingLightOrientation` |
| **类型**：character vector |
| **值**：3-element vector |
| **默认值**：`'[0 0 0]'` |

### **Taxi lights intensity (cd)** — Taxi lights intensity `150000` (default) | positive scalar

Taxi lights intensity, specified as a positive scalar, in candela.

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`TaxiLightIntensity` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'150000'` |

### **Taxi lights cone half angle (deg)** — Taxi lights cone half angle `36` (default) | positive scalar

Taxi lights cone half angle, specified as a positive scalar, in degrees.

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`TaxiLightConeAngle` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'36'` |

### **Taxi lights location** — Taxi lights location `[0 0 0]` (default) | 3-element vector

滑行灯相对于骨骼网格关联骨骼的位置，
specified as a 3-element vector

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomTaxiLightLocation` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'[0 0 0]'` |

### **Taxi lights orientation (deg)** — Taxi lights orientation `[0 0 0]` (default) | 3-element vector

出租车灯光相对于骨骼网格关联骨骼的方向，
specified as a 3-element vector

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `General
Aviation`, `Air Transport`, or
`Custom` and **Light configuration** to
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`CustomTaxiLightOrientation` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'[0 0 0]'` |

### **Navigation lights intensity** — Navigation lights intensity `500` (default) | positive scalar

Navigation lights intensity, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`NavLightIntensity` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'500'` |

### **Position light intensity** — Position light intensity `500` (default) | positive scalar

Position light intensity, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`PositionLightIntensity` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'500'` |

### **Strobe lights intensity** — Strobe lights intensity `5000` (default) | positive scalar

Strobe lights intensity, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`StrobeLightIntensity` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'5000'` |

### **Wingtip strobe period (s)** — Wingtip strobe period `1.5` (default) | positive scalar

Wingtip strobe period, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`WingtipStrobePeriod` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'1.5'` |

### **Wingtip strobe pulse width (% of period)** — Wingtip strobe pulse width `6` (default) | positive scalar

Wingtip strobe pulse width, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Airliner`, `General Aviation`,
`Air Transport`, or `Custom` and
**Light configuration** to `Configurable
lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`WingtipStrobePulseWidth` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'6'` |

### **Tail strobe period (s)** — Tail strobe period `1.5` (default) | positive scalar

Tail strobe period, specified as a positive scalar, in seconds.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`TailStrobePeriod` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'1.5'` |

### **Tail strobe pulse width (% of period)** — Tail strobe pulse width `6` (default) | positive scalar

Tail strobe pulse width, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`TailStrobePulseWidth` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'6'` |

### **Beacon lights intensity** — Beacon lights intensity `4000` (default) | positive scalar

Beacon lights intensity, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`BeaconLightIntensity` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'4000'` |

### **Beacon period (s)** — Beacon period `1.5` (default) | positive scalar

Beacon period, specified as a positive scalar, in seconds.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`BeaconPeriod` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'1.5'` |

### **Beacon pulse width (% of period)** — Beacon pulse width `10` (default) | positive scalar

Beacon pulse width, specified as a positive scalar.

#### 依赖关系

要启用此参数，请将 **Light configuration** 设置为
`Configurable lights`.

#### 编程使用

|  |
| --- |
| **模块参数**：`BeaconPulseWidth` |
| **类型**：character vector |
| **值**：positive scalar |
| **默认值**：`'10'` |

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

Not documented in R2025b.

## 扩展功能

Not documented in R2025b.

## 版本历史

**在 R2021b 中引入**

### R2024b: Simulation 3D Environment: 为 Simulation 3D Aircraft 缩放网格

您现在可以使用以下方式更改 Simulation 3D Aircraft 模块的网格大小：
**Scale** 参数或 **Scale** 端口。默认缩放为
a 1-by-3 vector of `[1 1 1]`.

要启用参数或端口，请使用 **Scale source**
parameter.

- `Dialog` — 启用 **Scale** 参数。
- `Port` — 启用 **Scale** 端口并
  **Initial scale** parameter.

### R2024a: Requires Simulink 3D Animation

使用 Simulation 3D Aircraft 模块仿真模型需要
Simulink
3D Animation.

### R2024a: Simulation 3D Aircraft 模块支持单精度输入

Simulation 3D Aircraft 模块现在支持单精度和双精度输入，用于
**Translation** 和 **Rotation** 输入端口。在 R2024a 之前，该
模块对这些端口仅支持双精度输入。

### R2023a：Simulation 3D Aircraft 模块更新

Simulation 3D Aircraft 模块有以下变更：

- 模块 **Initial Values** 选项卡的内容已移至 **Aircraft** 选项卡下的 **Initial Values** 部分。
- **Altitude Sensor** 选项卡有以下变更：

  - **Enable altitude sensor** 已重命名为 **Enable Altitude and WoW sensors**。

    从 R2023a 开始，WoW（weight on wheels，轮载）传感器使用您在模块掩码中指定的高度传感器射线和偏移量来确定一个或多个机轮或地面接触位置是否接触地面。
  - **Enable visible sensor rays** 已重命名为 **Show sensor rays in viewer**。
  - **Aircraft body Z offset (in meters)** 已重命名为 **Body Z offset (m)**。
  - **Front gear tire radius (in meters)** 已重命名为 **Front tire radius (m)**。
  - **Left gear tire radius (in meters)** 已重命名为 **Left tire radius (m)**。
  - **Right gear tire radius (in meters)** 已重命名为 **Right tire radius (m)**。
  - **WoW sensor tolerance**，用于设置 WoW 传感器容差。
  - 新参数 **Interpret vector outputs as 1-D**，用于控制是否对 **Altitude** 和 **WoW** 传感器输出端口进行重塑。

### R2022a：支持自定义网格和飞机光照

该模块现在支持：

- 使用 **Path to custom mesh** 参数指定自定义飞机网格。要启用此参数，请将 **Type** 设置为 `Custom`。
- 使用新的 **Light Configuration** 选项卡配置飞机光照。
- **Color** 参数中为飞机机体提供更多颜色。

## 描述

在 3D 环境中实现飞机

**注意**

使用 Simulation 3D Aircraft 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Aircraft 模块使用平移和旋转在 3D 可视化环境中实现飞机，以放置飞机。

要使用此模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将此模块的 **Sample time** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用飞机北东地（NED）*右手*（RH）*笛卡尔*坐标系。

- *X* 轴 — 沿飞机纵轴，指向前方
- *Y* 轴 — 沿飞机横轴，指向右侧
- *Z* 轴 — 指向下方

有关详细信息，请参阅 Fundamental Coordinate System Concepts。

**提示**

验证 Simulation 3D Aircraft 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Aircraft 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备好信号数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Aircraft — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。

### 骨架、骨骼和网格

Unreal® 使用*骨架*、*骨骼*和*网格*来定义 3D 模型。骨架由一组骨骼组成。网格是骨架的外覆盖层。飞机部件是网格的各个部分，例如副翼或机轮，它们链接到骨骼。有关详细信息，请参阅 https://docs.unrealengine.com/4.27/AnimatingObjects/SkeletalMeshAnimation/Skeleton/。

有关 Simulation 3D Aircraft 模块平移输入数组如何连接到飞机类型的详细信息，请参阅 Algorithms。
