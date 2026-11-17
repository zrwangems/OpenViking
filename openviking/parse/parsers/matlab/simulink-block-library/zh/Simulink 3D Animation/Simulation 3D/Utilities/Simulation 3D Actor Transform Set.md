---
type: simulink-block
title: 'Simulation 3D Actor Transform Set'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Utilities'
documentation_page: 'simulation3dactortransformset'
documentation_source_path: 'simulation3dactortransformset.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Actor Transform Set

## 端口

### 输入

### **Translation** — Actor 平移 `array`

Actor 平移，单位为 m。数组维度为每个 actor 的部件数乘以 `3`。

- `Translation(1,1)`、`Translation(1,2)` 和
  `Translation(1,3)` — 车辆分别沿世界 *X*、*Y* 和 *Z* 轴的位移。
- `Translation(...,1)`、`Translation(...,2)` 和
  `Translation(...,3)` — Actor 相对于车辆的位移，位于最初与世界 *X*、*Y* 和 *Z* 轴对齐的车辆固定坐标系中。

例如，考虑一个具有车身和四个车轮的车辆 actor。`Translation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置相对于车辆的平移信息。

  Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

  | Translation | 数组元素 |
  | --- | --- |
  | 车辆，*Xv* | `Translation(1,1)` |
  | 车辆，*Yv* | `Translation(1,2)` |
  | 车辆，*Zv* | `Translation(1,3)` |
  | 左前轮，*XFL* | `Translation(2,1)` |
  | 左前轮，*YFL* | `Translation(2,2)` |
  | 左前轮，*ZFL* | `Translation(2,3)` |
  | 右前轮，*XFR* | `Translation(3,1)` |
  | 右前轮，*YFR* | `Translation(3,2)` |
  | 右前轮，*ZFR* | `Translation(3,3)` |
  | 左后轮，*XRL* | `Translation(4,1)` |
  | 左后轮，*YRL* | `Translation(4,2)` |
  | 左后轮，*ZRL* | `Translation(4,3)` |
  | 右后轮，*XRR* | `Translation(5,1)` |
  | 右后轮，*YRR* | `Translation(5,2)` |
  | 右后轮，*ZRR* | `Translation(5,3)` |

### **Rotation** — Actor 旋转 `array`

Actor 旋转，单位为 rad。数组维度为每个 actor 的部件数乘以 `3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和
  `Rotation(1,3)` — 车辆分别绕车辆固定俯仰、横滚和偏航 *Y*、*Z* 和 *X* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和
  `Rotation(...,3)` — Actor 分别绕车辆固定俯仰、横滚和偏航 *Y*、*X* 和 *Z* 轴的旋转。

例如，考虑一个具有车身和四个车轮的车辆 actor。`Rotation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置的旋转信息。

  Rotation=[PitchvRollvYawvPitchFLRollFLYawFLPitchFRRollFRYawFRPitchRLRollRLYawRLPitchRRRollRRYawRR]

  | Rotation | 数组元素 |
  | --- | --- |
  | 车辆，*Pitchv* | `Rotation(1,1)` |
  | 车辆，*Rollv* | `Rotation(1,2)` |
  | 车辆，*Yawv* | `Rotation(1,3)` |
  | 左前轮，*PitchFL* | `Rotation(2,1)` |
  | 左前轮，*RollFL* | `Rotation(2,2)` |
  | 左前轮，*YawFL* | `Rotation(2,3)` |
  | 右前轮，*PitchFR* | `Rotation(3,1)` |
  | 右前轮，*RollFR* | `Rotation(3,2)` |
  | 右前轮，*YawFR* | `Rotation(3,3)` |
  | 左后轮，*PitchRL* | `Rotation(4,1)` |
  | 左后轮，*RollRL* | `Rotation(4,2)` |
  | 左后轮，*YawRL* | `Rotation(4,3)` |
  | 右后轮，*PitchRR* | `Rotation(5,1)` |
  | 右后轮，*RollRR* | `Rotation(5,2)` |
  | 右后轮，*YawRR* | `Rotation(5,3)` |

### **Scale** — 角色缩放 `array`

角色缩放。数组维度为每个角色的部件数乘 `3`。

- `Scale(1,1)`、`Scale(1,2)` 和
  `Scale(1,3)` — 分别表示车辆沿世界 *X*、
  *Y* 和 *Z* 轴的缩放。
- `Scale(...,1)`、`Scale(...,2)` 和
  `Scale(...,3)` — 分别表示角色沿世界 *X*、
  *Y* 和 *Z* 轴的缩放。

例如，考虑一个带有车身和四个车轮的车辆角色。`Scale` 信号：

- 维度为 `[5x3]`。
- 根据车轴和车轮位置包含缩放信息。

  Scale=[XVscaleYVscaleZVscaleXFLscaleYFLscaleZFLscaleXFRscaleYFRscaleZFRscaleXRLscaleYRLscaleZRLscaleXRRscaleYRRscaleZRRscale]

  | Scale | 数组元素 |
  | --- | --- |
  | 车辆，*Xvscale* | `Scale(1,1)` |
  | 车辆，*Yvscale* | `Scale(1,2)` |
  | 车辆，*Zvscale* | `Scale(1,3)` |
  | 左前轮，*XFLscale* | `Scale(2,1)` |
  | 左前轮，*YFLscale* | `Scale(2,2)` |
  | 左前轮，*ZFLscale* | `Scale(2,3)` |
  | 右前轮，*XFRscale* | `Scale(3,1)` |
  | 右前轮，*YFRscale* | `Scale(3,2)` |
  | 右前轮，*ZFRscale* | `Scale(3,3)` |
  | 左后轮，*XRLscale* | `Scale(4,1)` |
  | 左后轮，*YRLscale* | `Scale(4,2)` |
  | 左后轮，*ZRLscale* | `Scale(4,3)` |
  | 右后轮，*XRRscale* | `Scale(5,1)` |
  | 右后轮，*YRRscale* | `Scale(5,2)` |
  | 右后轮，*ZRRscale* | `Scale(5,3)` |

## 参数

#### 角色设置

### **Tag for actor in 3D scene, ActorTag** — 名称 `SimulinkActor1`（默认）| 字符向量

角色名称。

角色是支持 3D
平移、旋转和缩放的场景对象。部件是角色的组件。组件不能独立存在；它们与某个角色关联。

该模块不支持同一角色标签的多个实例。当你使用 3D 模块对（例如 Simulation 3D Actor
Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景角色时，请指定相同的 **Tag for actor in 3D scene, ActorTag**
参数。

### **Number of parts per actor to set, NumberOfParts** — 名称 `1`（默认）| `scalar`

每个角色的部件数。角色是场景对象，
支持 3D 平移、旋转和缩放。部件是角色的组件。组件
不能独立存在；它们与某个角色关联。通常，一个带有车身和四个车轮的车辆
角色有 5 个部件。

该模块不支持同一角色标签的多个实例。当你使用 3D 模块对（例如 Simulation 3D Actor
Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景角色时，请指定相同的 **Tag for actor in 3D scene, ActorTag**
参数。

### **Coordinate system** — 用于角色变换的坐标系 `Default`（默认）| `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定角色在 3D 环境中用于
平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB® 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `MATLAB`

#### 初始值

### **Initial array values to translate actor per part, Translation** — 每个部件的 actor 初始平移 `[0 0 0]`（默认）| `array`

Actor 初始位置，沿世界 *X*、*Y* 和 *Z* 轴，单位为 m。

数组维度为每个 actor 的部件数乘 `3`。

- `Translation(1,1)`、`Translation(1,2)` 和
  `Translation(1,3)` — 车辆分别沿世界
  *X*、*Y* 和 *Z* 轴的位移。
- `Translation(...,1)`、`Translation(...,2)` 和
  `Translation(...,3)` — Actor 相对于车辆的位移，位于初始与世界 *X*、
  *Y* 和 *Z* 轴对齐的车辆固定坐标系中。

例如，考虑一个具有车身和四个车轮的车辆 actor。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置相对于车辆的平移信息。

  Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

  | Translation | 数组元素 |
  | --- | --- |
  | 车辆，*Xv* | `Translation(1,1)` |
  | 车辆，*Yv* | `Translation(1,2)` |
  | 车辆，*Zv* | `Translation(1,3)` |
  | 左前轮，*XFL* | `Translation(2,1)` |
  | 左前轮，*YFL* | `Translation(2,2)` |
  | 左前轮，*ZFL* | `Translation(2,3)` |
  | 右前轮，*XFR* | `Translation(3,1)` |
  | 右前轮，*YFR* | `Translation(3,2)` |
  | 右前轮，*ZFR* | `Translation(3,3)` |
  | 左后轮，*XRL* | `Translation(4,1)` |
  | 左后轮，*YRL* | `Translation(4,2)` |
  | 左后轮，*ZRL* | `Translation(4,3)` |
  | 右后轮，*XRR* | `Translation(5,1)` |
  | 右后轮，*YRR* | `Translation(5,2)` |
  | 右后轮，*ZRR* | `Translation(5,3)` |

### **Initial array values to rotate actor per part, Rotation** — 每个部件的 actor 初始旋转 `[0 0 0]`（默认）| `array`

Actor 初始旋转，绕世界 *X*、*Y* 和
*Z* 轴，范围为 [-pi/2, pi/2]，单位为 rad。

数组维度为每个 actor 的部件数乘 `3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和
  `Rotation(1,3)` — 车辆分别绕车辆固定俯仰、横滚
  和偏航 *Y*、*Z* 和 *X* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和
  `Rotation(...,3)` — Actor 分别绕车辆固定俯仰、横滚
  和偏航 *Y*、*Z* 和 *X* 轴的旋转。

例如，考虑一个具有车身和四个车轮的车辆 actor。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置的旋转信息。

  Rotation=[PitchvRollvYawvPitchFLRollFLYawFLPitchFRRollFRYawFRPitchRLRollRLYawRLPitchRRRollRRYawRR]

  | Rotation | 数组元素 |
  | --- | --- |
  | 车辆，*Pitchv* | `Rotation(1,1)` |
  | 车辆，*Rollv* | `Rotation(1,2)` |
  | 车辆，*Yawv* | `Rotation(1,3)` |
  | 左前轮，*PitchFL* | `Rotation(2,1)` |
  | 左前轮，*RollFL* | `Rotation(2,2)` |
  | 左前轮，*YawFL* | `Rotation(2,3)` |
  | 右前轮，*PitchFR* | `Rotation(3,1)` |
  | 右前轮，*RollFR* | `Rotation(3,2)` |
  | 右前轮，*YawFR* | `Rotation(3,3)` |
  | 左后轮，*PitchRL* | `Rotation(4,1)` |
  | 左后轮，*RollRL* | `Rotation(4,2)` |
  | 左后轮，*YawRL* | `Rotation(4,3)` |
  | 右后轮，*PitchRR* | `Rotation(5,1)` |
  | 右后轮，*RollRR* | `Rotation(5,2)` |
  | 右后轮，*YawRR* | `Rotation(5,3)` |

### **用于按部件缩放角色的初始数组值，Scale** — 角色初始缩放 `[1 1 1]`（默认）| `array`

Actor initial scale.

Array dimensions are number of parts per actor-by-`3`.

- `Scale(1,1)`, `Scale(1,2)`, and
  `Scale(1,3)` — Vehicle scale along world *X*-,
  *Y*, and *Z*- axes, respectively.
- `Scale(...,1)`, `Scale(...,2)`, and
  `Scale(...,3)` — Actor scale along world *X*-,
  *Y*, and *Z*- axes, respectively.

例如，考虑一个具有车身和四个车轮的车辆角色。该参数：

- Dimensions are `[5x3]`.
- 包含根据车轴和车轮位置的缩放信息。

  Scale=[XVscaleYVscaleZVscaleXFLscaleYFLscaleZFLscaleXFRscaleYFRscaleZFRscaleXRLscaleYRLscaleZRLscaleXRRscaleYRRscaleZRRscale]

  | Scale | Array Element | Scale Axis |
  | --- | --- | --- |
  | Vehicle, *Xvscale* | `Scale(1,1)` | World *X*-axis |
  | Vehicle, *Yvscale* | `Scale(1,2)` | World *Y*-axis |
  | Vehicle, *Zvscale* | `Scale(1,3)` | World *Z*-axis |
  | Front left wheel, *XFLscale* | `Scale(2,1)` | World *X*-axis |
  | Front left wheel, *YFLscale* | `Scale(2,2)` | World *Y*-axis |
  | Front left wheel, *ZFLscale* | `Scale(2,3)` | World *Z*-axis |
  | Front right wheel, *XFRscale* | `Scale(3,1)` | World *X*-axis |
  | Front right wheel, *YFRscale* | `Scale(3,2)` | World *Y*-axis |
  | Front right wheel, *ZFRscale* | `Scale(3,3)` | World *Z*-axis |
  | Rear left wheel, *XRLscale* | `Scale(4,1)` | World *X*-axis |
  | Rear left wheel, *YRLscale* | `Scale(4,2)` | World *Y*-axis |
  | Rear left wheel, *ZRLscale* | `Scale(4,3)` | World *Z*-axis |
  | Rear right wheel, *XRRscale* | `Scale(5,1)` | World *X*-axis |
  | Rear right wheel, *YRRscale* | `Scale(5,2)` | World *Y*-axis |
  | Rear right wheel, *ZRRscale* | `Scale(5,3)` | World *Z*-axis |

### **Sample time** — Sample time `-1` (default) | `scalar`

Sample time, *Ts*. The graphics frame rate
is the inverse of the sample time.

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

Not documented in R2025b.

## 扩展功能

Not documented in R2025b.

## 版本历史

**在 R2022b 中引入**

### R2025a: Set coordinate system parameter

在以下模块中设置 **Coordinate system** 参数：
Simulation 3D Actor Transform Set 模块，以表示用于角色变换的坐标系
in the 3D environment.

## 描述

设置角色平移、旋转、缩放

Simulation 3D Actor Transform Set 模块设置角色在 3D 可视化环境中的平移、
旋转和缩放。

The **Coordinate
该模块的 system** 参数指定角色变换如何
应用于 3D 环境。该模块的输出也遵循指定的坐标
system.

角色是支持 3D 平移、
旋转和缩放的场景对象。部件是角色组件。组件不能独立存在；它们
与角色相关联。

**Tip**

验证 Simulation 3D Actor Transform
Set 模块在 Simulation 3D Scene Configuration
模块之前执行。这样，Simulation 3D Actor Transform Set 会在 Unreal Engine® 3D 可视化环境接收信号数据之前
准备好这些数据。要检查模块执行顺序，
右键单击这些模块并选择 **Properties**。在
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Actor Transform Set — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order (Simulink)。
