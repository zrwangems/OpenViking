---
type: simulink-block
title: 'Simulation 3D Rotorcraft'
family: 'animation'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3drotorcraft'
documentation_source_path: 'simulation3drotorcraft.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Rotorcraft

## 端口

### 输入

### **Translation** — 旋翼机平移 `6`-by-`3` 数组 | `19`-by-`3` 数组 | `11`-by-`3` 数组

旋翼机平移，指定为：

- `6`-by-`3` 数组 — 旋翼机
  **类型** 为 `Light helicopter`。
- `19`-by-`3` 数组 — 旋翼机
  **类型** 为 `Helicopter`。
- `11`-by-`3` 数组 — 旋翼机
  **类型** 为 `Multirotor`。

该信号包含平移 [X, Y, Z]，以米为单位，数组的每一行对应旋翼机的一个骨骼。

该平移应用于 `Light helicopter` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ENGINE | 2 |
| ROTOR1 | 3 |
| ROTOR2 | 4 |
| SENSOR1 | 5 |
| SENSOR2 | 6 |

该平移应用于 `Helicopter` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ENGINE1 | 2 |
| ENGINE2 | 3 |
| ROTOR1 | 4 |
| ROTOR2 | 5 |
| NOSE\_GEAR | 6 |
| NOSE\_WHEEL | 7 |
| NOSE\_GEAR\_DOOR1 | 8 |
| NOSE\_GEAR\_DOOR2 | 9 |
| LEFT\_GEAR | 10 |
| LEFT\_WHEEL | 11 |
| LEFT\_GEAR\_DOOR1 | 12 |
| LEFT\_GEAR\_DOOR2 | 13 |
| RIGHT\_GEAR | 14 |
| RIGHT\_WHEEL | 15 |
| RIGHT\_GEAR\_DOOR1 | 16 |
| RIGHT\_GEAR\_DOOR2 | 17 |
| SENSOR1 | 18 |
| SENSOR2 | 19 |

该平移应用于 `Multirotor` 类型的以下骨骼。

| 骨骼 | 索引 |
| --- | --- |
| BODY | 1 |
| ROTOR1 | 2 |
| ROTOR2 | 3 |
| ROTOR3 | 4 |
| ROTOR4 | 5 |
| ROTOR5 | 6 |
| ROTOR6 | 7 |
| ROTOR7 | 8 |
| ROTOR8 | 9 |
| SENSOR1 | 10 |
| SENSOR2 | 11 |

**数据类型：** `single` | `double`

### **Rotation** — 旋翼机和机轮旋转 `6`-by-`3` 数组 | `19`-by-`3` 数组 | `11`-by-`3` 数组

旋翼机旋转，指定为：

- `6`-by-`3` 数组 — 旋翼机
  **类型** 为 `Light helicopter`。
- `19`-by-`3` 数组 — 旋翼机
  **类型** 为 `Helicopter`。
- `11`-by-`3` 数组 — 旋翼机
  **类型** 为 `Multirotor`。

该旋转应用于 Translation 端口列出的相同骨骼。

该信号包含旋转 [roll, pitch, yaw]，以弧度为单位，数组的每一行对应旋翼机的一个骨骼。

**数据类型：** `single` | `double`

### **LightStates** — 旋翼机灯光控制 1-by-7 double 值向量

旋翼机灯光控制，指定为 1-by-7 double 值向量。向量的每个元素开启（`1`）或关闭（`0`）特定的旋翼机灯光组。向量顺序如下：

- `LANDING_LIGHTS`
- `NOSE_LIGHTS`
- `ANTICOLLISION_BEACONS`
- N/A（忽略）
- `STROBE_LIGHTS`
- `NAVIGATION_LIGHTS`
- `POSITION_LIGHTS`

#### 依赖关系

要启用此端口，请将 **灯光配置** 参数设置为 `Configurable lights`。

**数据类型：** `single` | `double`

### **Scale** — 网格缩放 `[1 1 1]`（默认） | 1-by-3 数组

网格缩放，指定为 1-by-3 数组。

#### 依赖关系

要启用此端口，请将 **缩放源** 参数设置为 `Port`。
### 输出

### **Altitude** — 旋翼机姿态 1-by-5 向量

旋翼机姿态，返回为 1-by-5 向量。这些高度按顺序为：

| Light Helicopter | Helicopter | Multirotor |
| --- | --- | --- |
| `rotorcraft_body` | `rotorcraft_body` | `rotorcraft_body` |
| `rotorcraft_contact_location1` | `rotorcraft_front_tire` | `rotorcraft_contact_location1` |
| `rotorcraft_contact_location2` | `rotorcraft_left_tire` | `rotorcraft_contact_location2` |
| `rotorcraft_contact_location3` | `rotorcraft_right_tire` | `rotorcraft_contact_location3` |
| `rotorcraft_contact_location4` | N/A (`0`) | `rotorcraft_contact_location4` |

#### 依赖关系

要启用此端口，请选中 **启用高度和 WoW 传感器** 复选框。

**数据类型：** `double`

### **WoW** — 轮载 `true` | `false`

旋翼机轮载（weight on wheels，WoW）逻辑开关，如果任一接触位置或主起落架轮胎（左或右）在地面上，则返回 `true`。否则，输出为 `false`。

#### 依赖关系

要启用此端口，请选中 **启用高度和 WoW 传感器** 复选框。

**数据类型：** `Boolean`

## 参数

### **采样时间** — 采样时间 `-1`（默认） | 实数标量

采样时间，*Ts*。图形帧率是采样时间的倒数。

#### 编程使用

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: 字符向量 |
| **值**: 实数标量 |
| **默认值**: `'-1'` |

### 旋翼机

### **类型** — 旋翼机类型 `Light helicopter`（默认） | `Helicopter` | `Multirotor`

旋翼机类型，指定为 `Light helicopter`、`Helicopter` 或 `Multirotor`。

#### 依赖关系

要设置此参数，请将 **初始平移** 和 **初始旋转** 参数设置为匹配的数组大小。未能正确设置这些数组大小会导致错误。

#### 编程使用

|  |
| --- |
| **模块参数**: `Mesh` |
| **类型**: 字符向量 |
| **值**: `'Light helicopter'` | `'Helicopter'` | `'Multiroter'` |
| **默认值**: `'Light helicopter'` |

### **轻型直升机网格路径** — 轻型直升机网格路径 `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/LightHelicopter/Mesh/SK_LightHelicopter.SK_LightHelicopter'`（默认） | 字符向量

轻型直升机网格路径，指定为字符向量。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `Light helicopter`。

#### 编程使用

|  |
| --- |
| **模块参数**: `MeshPathLight` |
| **类型**: 字符向量 |
| **值**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/LightHelicopter/Mesh/SK_LightHelicopter.SK_LightHelicopter'` |
| **默认值**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/LightHelicopter/Mesh/SK_LightHelicopter.SK_LightHelicopter'` |

### **直升机网格路径** — 直升机网格路径 `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Helicopter/Mesh/SK_Helicopter.SK_Helicopter'`（默认） | 字符向量

直升机网格路径，指定为字符向量。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `Helicopter`。

#### 编程使用

|  |
| --- |
| **模块参数**: `MeshPath` |
| **类型**: 字符向量 |
| **值**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Helicopter/Mesh/SK_Helicopter.SK_Helicopter'` |
| **默认值**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Helicopter/Mesh/SK_Helicopter.SK_Helicopter'` |

### **多旋翼网格路径** — 多旋翼网格路径 `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_Quadcopter.SK_Quadcopter'`（默认） | `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_QuadcopterMini.SK_QuadcopterMini'` | 字符向量

多旋翼网格路径，指定为字符向量。要创建自定义航空航天网格，请参阅 Prepare Custom Aircraft Mesh for the Unreal Editor。

#### 依赖关系

要启用此参数，请将 **类型** 设置为 `Multirotor`。

#### 编程使用

|  |
| --- |
| **模块参数**: `MeshPathMulti` |
| **类型**: 字符向量 |
| **值**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_Quadcopter.SK_Quadcopter'` | `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_QuadcopterMini.SK_QuadcopterMini'` |
| **默认值**: `'/MathWorksAerospaceContent/Vehicles/Rotorcraft/Multirotor/Mesh/SK_Quadcopter.SK_Quadcopter'` |

### **颜色** — 旋翼机颜色 `Red`（默认） | `Orange` | `Yellow` | `Green` | `Cyan` | `Blue` | `Black` | `White` | `Silver` | `Metal`

旋翼机颜色，指定为 `Red`、`Orange`、`Yellow`、`Green`、`Cyan`、`Blue`、`Black`、`White`、`Silver` 或 `Metal`。

#### 编程使用

|  |
| --- |
| **模块参数**: `AircraftColor` |
| **类型**: 字符向量 |
| **值**: `'Red'` | `'Orange'` | `'Yellow'` | `'Green'` | `'Cyan'` | `'Blue'` | `'Black'` | `'White'` | `'Silver'` | `'Metal'` |
| **默认值**: `'Red'` |

### **名称** — 旋翼机名称 `SimulinkVehicle1`（默认） | 字符向量

旋翼机名称，指定为字符向量。默认情况下，当您在模型中使用该模块时，该模块会将 **名称** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中其他 simulation 3D 模块的数量。

#### 编程使用

|  |
| --- |
| **模块参数**: `ActorName` |
| **类型**: 字符向量 |
| **值**: 标量 |
| **默认值**: `'SimulinkVehicle1'` |

### **初始平移 (m)** — 旋翼机初始平移 `zeros(6,3)`（默认） | 19-by-3 数组 | 11-by-3 数组

旋翼机初始平移，指定为 6-by-3、19-by-3 或 11-by-3 数组。

#### 依赖关系

此参数必须与您在 **类型** 中设置的旋翼机类型匹配。未能正确设置这些数组大小会导致错误。

#### 编程使用

|  |
| --- |
| **模块参数**: `Translation` |
| **类型**: 字符向量 |
| **值**: 6-by-3 数组 | 19-by-3 数组 | 11-by-3 数组 |
| **默认值**: `'zeros(6,3)'` |

**数据类型：** `single` | `double`

### **初始旋转 (rad)** — 旋翼机旋转 `zeros(6,3)`（默认） | 19-by-3 数组 | 11-by-3 数组

旋翼机初始旋转，指定为 6-by-3、19-by-3 或 11-by-3 数组。

#### 依赖关系

此参数必须与您在 **类型** 中设置的旋翼机类型匹配。未能正确设置这些数组大小会导致错误。

#### 编程使用

|  |
| --- |
| **模块参数**: `Rotation` |
| **类型**: 字符向量 |
| **值**: 6-by-3 数组 | 19-by-3 数组 | 11-by-3 数组 |
| **默认值**: `'zeros(6,3)'` |

**数据类型：** `single` | `double`

### **缩放源** — 缩放源 `Dialog`（默认） | `Port`

缩放源，指定为 `Dialog` 或 `Port`。

#### 编程使用

|  |
| --- |
| **模块参数**: `ScaleInputPort` |
| **类型**: 字符向量 |
| **值**: `'Dialog'` | `'Port'` |
| **默认值**: `'Dialog'` |

### **初始缩放** — 初始网格缩放 `[1 1 1]`（默认） | 1-by-3 数组

初始网格缩放，指定为 1-by-3 数组。

#### 依赖关系

要启用此参数，请将 **缩放源** 设置为 `Port`。

#### 编程使用

|  |
| --- |
| **模块参数**: `InitialScale` |
| **类型**: 字符向量 |
| **值**: `1`-by-`3` 数组 |
| **默认值**: `'[1 1 1]'` |

**数据类型：** `single` | `double`

### **缩放** — 网格缩放 `[1 1 1]`（默认） | 1-by-3 数组

网格缩放，指定为 1-by-3 数组。

#### 依赖关系

要启用此参数，请将 **缩放源** 设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**: `Scale` |
| **类型**: 字符向量 |
| **值**: `1`-by-`3` 数组 |
| **默认值**: `'[1 1 1]'` |

**数据类型：** `single` | `double`

### 高度传感器

### **启用高度和 WoW 传感器** — 高度和 WoW 传感器 on（默认） | off

要启用高度和 WoW 传感器的输出端口，请选中此复选框。否则，请清除此复选框。有关高度和 WoW 传感器的详细信息，请参阅 Altitude Sensors and WoW Sensors。

#### 编程使用

|  |
| --- |
| **模块参数**: `IsGHSensorEnabled` |
| **类型**: 字符向量 |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **在查看器中显示传感器射线** — 在查看器中显示传感器射线的选项 off（默认） | on

要在查看器中显示传感器射线，请选中此复选框。否则，请清除此复选框。

#### 依赖关系

要启用此参数，请选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `AreGHRaysVisible` |
| **类型**: 字符向量 |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **将向量输出解释为 1-D** — 在传感器输出端口上控制重塑 off（默认） | on

控制是否在 **Altitude** 和 **WoW** 传感器输出端口上执行重塑：

- 选中此复选框以启用重塑。
- 清除此复选框以禁用重塑。

#### 编程使用

|  |
| --- |
| **模块参数**: `IsOutputReshapeEnabled` |
| **类型**: 字符向量 |
| **值**: `'on'` | `'off'` |
| **默认值**: `'off'` |

### **射线长度 (m)** — 射线长度 `1524`（默认） | 实数标量

射线长度，指定为实数标量，以米为单位。射线长度限制高度检测。例如，如果旋翼机原点下方到地面的垂直距离大于射线长度加上旋翼机机体 *Z* 偏移，则高度传感器会将第一个值返回为 `-1`。

#### 依赖关系

要启用此参数，请选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHRayLength` |
| **类型**: 字符向量 |
| **值**: 实数标量 |
| **默认值**: `'1524'` |

### **旋翼机机体 Z 偏移 (m)** — 旋翼机机体 *Z* 偏移 `1.169`（默认） | 实数标量

旋翼机机体 *Z* 偏移，指定为实数标量，以米为单位。

#### 依赖关系

要启用此参数，请选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHBodyOffset` |
| **类型**: 字符向量 |
| **值**: 实数标量 |
| **默认值**: `'1.169'` |

### **地面接触位置 1 (m)** — 第一个地面接触位置 `[1.47 -1.04 1.169]`（默认） | 3 元素向量

第一个地面接触位置，指定为 3 元素向量，以米为单位。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Light helicopter` 或 `Multirotor`。
- 选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHContactLocation1` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[1.47 -1.04 1.169]'` |

### **地面接触位置 2 (m)** — 第二个地面接触位置 `[-1.24 -1.04 1.169]`（默认） | 3 元素向量

第二个地面接触位置，指定为 3 元素向量，以米为单位。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Light helicopter` 或 `Multirotor`。
- 选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHContactLocation2` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[-1.24 -1.04 1.169]'` |

### **地面接触位置 3 (m)** — 第三个地面接触位置 `[-1.24 1.04 1.169]` | 3 元素向量

第三个地面接触位置，指定为 3 元素向量，以米为单位。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Light helicopter` 或 `Multirotor`。
- 选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHContactLocation3` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[-1.24 1.04 1.169]'` |

### **地面接触位置 4 (m)** — 第四个地面接触位置 `[1.47 1.04 1.169]` | 3 元素向量

第四个地面接触位置，指定为 3 元素向量，以米为单位。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Light helicopter` 或 `Multirotor`。
- 选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHContactLocation4` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[1.47 1.04 1.169]'` |

### **前轮胎半径 (m)** — 前起落架轮胎半径 `0.196`（默认） | 实数标量

前起落架轮胎半径，指定为实数标量，以米为单位。前起落架高度射线从前起落架轮轴中心加上前起落架轮胎半径 *Z* 偏移处发出。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Helicopter`。
- 选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHFrontTireRadius` |
| **类型**: 字符向量 |
| **值**: 实数标量 |
| **默认值**: `'0.196'` |

### **左轮胎半径 (m)** — 左起落架轮胎半径 `0.203`（默认） | 实数标量

左起落架轮胎半径，指定为实数标量，以米为单位。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Helicopter`。
- 选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHLeftTireRadius` |
| **类型**: 字符向量 |
| **值**: 实数标量 |
| **默认值**: `'0.203'` |

### **右轮胎半径 (m)** — 右起落架轮胎半径 `0.203`（默认） | 实数标量

右起落架轮胎半径，指定为实数标量，以米为单位。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Helicopter`。
- 选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `GHRightTireRadius` |
| **类型**: 字符向量 |
| **值**: 实数标量 |
| **默认值**: `'0.203'` |

### **WoW 传感器容差 (m)** — WoW 传感器容差 `0.05`（默认） | 实数标量

WoW 传感器容差，指定为实数标量。

#### 依赖关系

要启用此参数，请选中 **启用高度和 WoW 传感器** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `WoWSensorTolerance` |
| **类型**: 字符向量 |
| **值**: 实数标量 |
| **默认值**: `'0.05'` |

### 灯光配置

### **灯光配置** — 灯光配置选项 `Automatic lights`（默认） | `Configurable lights` | `Lights off`

灯光配置选项，指定为以下值之一：

- `Automatic lights` — 使用可提供真实模式循环的默认旋翼机灯光配置。
- `Configurable lights` — 配置旋翼机灯光参数。
- `Lights off` — 关闭所有旋翼机灯光。

#### 依赖关系

- 将此参数设置为 `Automatic lights` 会禁用所有其他 **灯光配置** 参数的可配置性。该模块使用旋翼机灯光值的默认参数值。
- 将此参数设置为 `Configurable lights` 会根据旋翼机类型启用 **灯光配置** 参数的可配置性。
- 将 **类型** 设置为给定的旋翼机类型，并将 **灯光配置** 设置为 `Configurable lights`，会启用每种旋翼机所用灯光参数的可配置性。
- 将此参数设置为 `Lights off` 会禁用所有其他 **灯光配置** 参数的可配置性。该模块会关闭所有旋翼机灯光。

#### 编程使用

|  |
| --- |
| **模块参数**: `LightsConfig` |
| **类型**: 字符向量 |
| **值**: `'Automatic lights'` | `'Configurable lights'` | `'Lights off'` |
| **默认值**: `'Automatic lights'` |

### **着陆灯强度 (cd)** — 着陆灯强度 `300000`（默认） | 正标量

着陆灯强度，指定为正标量，以 candela 为单位。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `LandingLightIntensity` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'300000'` |

### **着陆灯锥形半角 (deg)** — 着陆灯锥形半角 `15`（默认） | 正标量

着陆灯锥形半角，指定为正标量，以度为单位。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `LandingLightConeAngle` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'15'` |

### **着陆灯颜色 [r g b]** — 着陆灯颜色 `[1 1 1]`（默认） | 3 元素向量

着陆灯颜色，指定为 3 元素向量 [red green blue]。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 **Multirotor**。
- 将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `LandingLightColor` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[1 1 1]'` |

### **着陆灯位置** — 着陆灯位置 `[0 0 0]`（默认） | 3 元素向量

着陆灯位置，相对于骨骼网格的关联骨骼，指定为 3 元素向量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `HelicopterLeftLandingLightLocation` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[0 0 0]'` |

### **着陆灯方向 (deg)** — 着陆灯方向 `[0 0 0]`（默认） | 3 元素向量

着陆灯方向，相对于骨骼网格的关联骨骼，指定为 3 元素向量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `HelicopterLeftLandingLightOrientation` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[0 0 0]'` |

### **机头灯强度 (cd)** — 机头灯强度 `150000`（默认） | 正标量

机头灯强度，指定为正标量，以 candela 为单位。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `NoseLightIntensity` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'150000'` |

### **机头灯锥形半角 (deg)** — 机头灯锥形半角 `36`（默认） | 正标量

机头灯锥形半角，指定为正标量，以度为单位。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `NoseLightConeAngle` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'36'` |

### **机头灯位置** — 机头灯位置 `[0 0 0]`（默认） | 3 元素向量

机头灯位置，相对于骨骼网格的关联骨骼，指定为 3 元素向量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `HelicopterNoseLightLocation` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[0 0 0]'` |

### **机头灯方向 (deg)** — 机头灯方向 `[0 0 0]`（默认） | 3 元素向量

机头灯方向，相对于骨骼网格的关联骨骼，指定为 3 元素向量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `HelicopterNoseLightOrientation` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[0 0 0]'` |

### **航行灯强度** — 航行灯强度 `500`（默认） | 正标量

航行灯强度，指定为正标量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `NavLightIntensity` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'500'` |

### **位置灯强度** — 位置灯强度 `500`（默认） | 正标量

位置灯强度，指定为正标量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `PositionLightIntensity` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'500'` |

### **频闪灯强度** — 频闪灯强度 `5000`（默认） | 正标量

频闪灯强度，指定为正标量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `StrobeLightIntensity` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'5000'` |

### **频闪灯颜色 [r g b]** — 频闪灯颜色 `[1 1 1]`（默认） | 3 元素向量

频闪灯颜色，指定为 3 元素向量 [red green blue]。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 `Multirotor`。
- 将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `StrobeLightColor` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[1 1 1]'` |

### **频闪灯周期 (s)** — 频闪灯周期 `1.5`（默认） | 正标量

频闪灯周期，指定为正标量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `StrobePeriod` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'1.5'` |

### **频闪灯脉冲宽度 (% of period)** — 频闪灯脉冲宽度 `6`（默认） | 正标量

频闪灯脉冲宽度，指定为正标量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `StrobePulseWidth` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'6'` |

### **信标灯强度** — 信标灯强度 `4000`（默认） | 正标量

信标灯强度，指定为正标量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `BeaconLightIntensity` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'4000'` |

### **信标灯颜色 [r g b]** — 信标灯颜色 `[1 0 0]`（默认） | 3 元素向量

信标灯颜色，指定为 3 元素向量 [red green blue]。

#### 依赖关系

要启用此参数：

- 将 **类型** 设置为 **Multirotor**。
- 将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `BeaconLightColor` |
| **类型**: 字符向量 |
| **值**: 3 元素向量 |
| **默认值**: `'[1 0 0]'` |

### **信标灯周期 (s)** — 信标灯周期 `1.5`（默认） | 正标量

信标灯周期，指定为正标量，以秒为单位。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `BeaconPeriod` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'1.5'` |

### **信标灯脉冲宽度 (% of period)** — 信标灯脉冲宽度 `10`（默认） | 正标量

信标灯脉冲宽度，指定为正标量。

#### 依赖关系

要启用此参数，请将 **灯光配置** 设置为 `Configurable lights`。

#### 编程使用

|  |
| --- |
| **模块参数**: `BeaconPulseWidth` |
| **类型**: 字符向量 |
| **值**: 正标量 |
| **默认值**: `'10'` |

## 所属库

Aerospace Blockset / Animation / Simulation 3D

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2023a 中引入**

### R2024b: Simulation 3D Environment：为 Simulation 3D Rotorcraft 缩放网格

现在可以使用 **缩放** 参数或 **Scale** 端口更改 Simulation 3D Rotorcraft 模块的网格大小。默认缩放为 `[1 1 1]` 的 1-by-3 向量。

要启用这些参数或端口，请使用 **缩放源** 参数。

- `Dialog` — 启用 **缩放** 参数。
- `Port` — 启用 **Scale** 端口和 **初始缩放** 参数。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Rotorcraft 模块对模型进行仿真需要 Simulink 3D Animation。

### R2024a：Simulation 3D Rotorcraft 模块支持单精度输入

Simulation 3D Rotorcraft 模块现在支持 **Translation** 和 **Rotation** 输入端的单精度和双精度输入。在 R2024a 之前，此模块仅支持这些端口的双精度输入。

## 描述

实现 3D 旋翼机

**注意**

使用 Simulation 3D Rotorcraft 模块对模型进行仿真需要 Simulink® 3D Animation™。

Simulation 3D Rotorcraft 模块使用平移和旋转在 3D 可视化环境中实现旋翼机，以放置旋翼机。

要使用此模块，您的模型必须包含 Simulation 3D Scene Configuration 模块。如果将此模块的 **采样时间** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用旋翼机北-东-下 (NED) *右手* (RH) *笛卡尔* 坐标系。

- *X* 轴 — 沿旋翼机纵轴，指向机头
- *Y* 轴 — 沿旋翼机横轴，指向右侧
- *Z* 轴 — 指向下方

有关详细信息，请参阅 Fundamental Coordinate System Concepts。

**提示**

验证 Simulation 3D Rotorcraft 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Rotorcraft 会在 Unreal Engine® 3D 可视化环境接收数据之前准备好信号数据。要检查模块执行顺序，请右键单击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Rotorcraft — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。

### 骨架、骨骼和网格

Unreal® 使用*骨架*、*骨骼*和*网格*来定义 3D 模型。骨架由一组骨骼组成。网格是骨架的外覆层。旋翼机部件是网格的区段，例如旋翼叶片或机轮，它们链接到骨骼。有关详细信息，请参阅 https://docs.unrealengine.com/4.27/AnimatingObjects/SkeletalMeshAnimation/Skeleton/。

有关 Simulation 3D Rotorcraft 模块的平移输入数组如何连接到旋翼机类型的详细信息，请参阅 Algorithms。
