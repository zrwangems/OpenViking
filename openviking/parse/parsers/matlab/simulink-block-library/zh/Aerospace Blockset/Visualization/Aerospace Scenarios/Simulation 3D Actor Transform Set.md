---
type: simulink-block
title: 'Simulation 3D Actor Transform Set'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Aerospace Scenarios'
documentation_page: 'simulation3dactortransformset'
documentation_source_path: 'simulation3dactortransformset.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Actor Transform Set

## 端口

### 输入

### **Translation** — 角色平移 `array`

角色平移，单位为 m。数组维度为每个角色的部件数 × `3`。

- `Translation(1,1)`、`Translation(1,2)` 和
  `Translation(1,3)` — 车辆沿世界
  *X*、*Y* 和 *Z* 轴的位移，
  分别对应。
- `Translation(...,1)`、`Translation(...,2)` 和
  `Translation(...,3)` — 角色相对于车辆的位移，位于
  最初与世界 *X*、
  *Y* 和 *Z* 轴对齐的车辆固定坐标系中，分别对应。

例如，考虑一个具有车身和四个车轮的车辆角色。`Translation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的、相对于车辆的平移信息。

  Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

  | Translation | 数组元素 |
  | --- | --- |
  | 车辆，*Xv* | `Translation(1,1)` |
  | 车辆，*Yv* | `Translation(1,2)` |
  | 车辆，*Zv* | `Translation(1,3)` |
  | 前左轮，*XFL* | `Translation(2,1)` |
  | 前左轮，*YFL* | `Translation(2,2)` |
  | 前左轮，*ZFL* | `Translation(2,3)` |
  | 前右轮，*XFR* | `Translation(3,1)` |
  | 前右轮，*YFR* | `Translation(3,2)` |
  | 前右轮，*ZFR* | `Translation(3,3)` |
  | 后左轮，*XRL* | `Translation(4,1)` |
  | 后左轮，*YRL* | `Translation(4,2)` |
  | 后左轮，*ZRL* | `Translation(4,3)` |
  | 后右轮，*XRR* | `Translation(5,1)` |
  | 后右轮，*YRR* | `Translation(5,2)` |
  | 后右轮，*ZRR* | `Translation(5,3)` |

### **Rotation** — 角色旋转 `array`

角色旋转，单位为 rad。数组维度为每个角色的部件数 × `3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和
  `Rotation(1,3)` — 车辆绕车辆固定俯仰、滚转和偏航 *Y*、*Z* 和 *X*
  轴的旋转，分别对应。
- `Rotation(...,1)`、`Rotation(...,2)` 和
  `Rotation(...,3)` — 角色绕车辆固定俯仰、滚转和偏航 *Y*、*Z* 和 *X*
  轴的旋转，分别对应。

例如，考虑一个具有车身和四个车轮的车辆角色。`Rotation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的旋转信息。

  Rotation=[PitchvRollvYawvPitchFLRollFLYawFLPitchFRRollFRYawFRPitchRLRollRLYawRLPitchRRRollRRYawRR]

  | Rotation | 数组元素 |
  | --- | --- |
  | 车辆，*Pitchv* | `Rotation(1,1)` |
  | 车辆，*Rollv* | `Rotation(1,2)` |
  | 车辆，*Yawv* | `Rotation(1,3)` |
  | 前左轮，*PitchFL* | `Rotation(2,1)` |
  | 前左轮，*RollFL* | `Rotation(2,2)` |
  | 前左轮，*YawFL* | `Rotation(2,3)` |
  | 前右轮，*PitchFR* | `Rotation(3,1)` |
  | 前右轮，*RollFR* | `Rotation(3,2)` |
  | 前右轮，*YawFR* | `Rotation(3,3)` |
  | 后左轮，*PitchRL* | `Rotation(4,1)` |
  | 后左轮，*RollRL* | `Rotation(4,2)` |
  | 后左轮，*YawRL* | `Rotation(4,3)` |
  | 后右轮，*PitchRR* | `Rotation(5,1)` |
  | 后右轮，*RollRR* | `Rotation(5,2)` |
  | 后右轮，*YawRR* | `Rotation(5,3)` |

### **Scale** — 角色缩放 `array`

角色缩放。数组维度为每个角色的部件数 × `3`。

- `Scale(1,1)`、`Scale(1,2)` 和
  `Scale(1,3)` — 车辆沿世界 *X*、
  *Y* 和 *Z* 轴的缩放，分别对应。
- `Scale(...,1)`、`Scale(...,2)` 和
  `Scale(...,3)` — 角色沿世界 *X*、
  *Y* 和 *Z* 轴的缩放，分别对应。

例如，考虑一个具有车身和四个车轮的车辆角色。`Scale` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的缩放信息。

  Scale=[XVscaleYVscaleZVscaleXFLscaleYFLscaleZFLscaleXFRscaleYFRscaleZFRscaleXRLscaleYRLscaleZRLscaleXRRscaleYRRscaleZRRscale]

  | Scale | 数组元素 |
  | --- | --- |
  | 车辆，*Xvscale* | `Scale(1,1)` |
  | 车辆，*Yvscale* | `Scale(1,2)` |
  | 车辆，*Zvscale* | `Scale(1,3)` |
  | 前左轮，*XFLscale* | `Scale(2,1)` |
  | 前左轮，*YFLscale* | `Scale(2,2)` |
  | 前左轮，*ZFLscale* | `Scale(2,3)` |
  | 前右轮，*XFRscale* | `Scale(3,1)` |
  | 前右轮，*YFRscale* | `Scale(3,2)` |
  | 前右轮，*ZFRscale* | `Scale(3,3)` |
  | 后左轮，*XRLscale* | `Scale(4,1)` |
  | 后左轮，*YRLscale* | `Scale(4,2)` |
  | 后左轮，*ZRLscale* | `Scale(4,3)` |
  | 后右轮，*XRRscale* | `Scale(5,1)` |
  | 后右轮，*YRRscale* | `Scale(5,2)` |
  | 后右轮，*ZRRscale* | `Scale(5,3)` |

## 参数

#### 角色设置

### **3D 场景中角色的标签，ActorTag** — 名称 `SimulinkActor1`（默认） | character vector

角色名称。

角色是支持 3D
平移、旋转和缩放的场景对象。部件是角色组件。组件本身不存在；
它们与角色关联。

该模块不支持同一角色标签的多个实例。使用 3D 模块对（例如 Simulation 3D Actor
Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景角色时，请指定
相同的 **3D 场景中角色的标签，ActorTag**
参数。

### **要设置的每个角色的部件数，NumberOfParts** — 名称 `1`（默认） | `scalar`

每个角色的部件数。角色是支持 3D 平移、旋转和缩放的场景对象。部件是角色组件。组件
本身不存在；它们与角色关联。通常，一个具有车身和四个车轮的车辆
角色有 5 个部件。

该模块不支持同一角色标签的多个实例。使用 3D 模块对（例如 Simulation 3D Actor
Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景角色时，请指定
相同的 **3D 场景中角色的标签，ActorTag**
参数。

#### 初始值

### **用于按部件平移角色的初始数组值，Translation** — 角色初始位置 `[0 0 0]`（默认） | `array`

角色初始位置，沿世界 *X*、*Y* 和
*Z* 轴，单位为 m。

数组维度为每个角色的部件数 × `3`。

- `Translation(1,1)`、`Translation(1,2)` 和
  `Translation(1,3)` — 车辆沿世界
  *X*、*Y* 和 *Z* 轴的位移，
  分别对应。
- `Translation(...,1)`、`Translation(...,2)` 和
  `Translation(...,3)` — 角色相对于车辆的位移，位于
  最初与世界 *X*、
  *Y* 和 *Z* 轴对齐的车辆固定坐标系中，分别对应。

例如，考虑一个具有车身和四个车轮的车辆角色。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的、相对于车辆的平移信息。

  Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

  | Translation | 数组元素 |
  | --- | --- |
  | 车辆，*Xv* | `Translation(1,1)` |
  | 车辆，*Yv* | `Translation(1,2)` |
  | 车辆，*Zv* | `Translation(1,3)` |
  | 前左轮，*XFL* | `Translation(2,1)` |
  | 前左轮，*YFL* | `Translation(2,2)` |
  | 前左轮，*ZFL* | `Translation(2,3)` |
  | 前右轮，*XFR* | `Translation(3,1)` |
  | 前右轮，*YFR* | `Translation(3,2)` |
  | 前右轮，*ZFR* | `Translation(3,3)` |
  | 后左轮，*XRL* | `Translation(4,1)` |
  | 后左轮，*YRL* | `Translation(4,2)` |
  | 后左轮，*ZRL* | `Translation(4,3)` |
  | 后右轮，*XRR* | `Translation(5,1)` |
  | 后右轮，*YRR* | `Translation(5,2)` |
  | 后右轮，*ZRR* | `Translation(5,3)` |

### **用于按部件旋转角色的初始数组值，Rotation** — 角色初始旋转 `[0 0 0]`（默认） | `array`

角色初始旋转，绕世界 *X*、*Y* 和
*Z* 轴，范围为 [-pi/2, pi/2]，单位为 rad。

数组维度为每个角色的部件数 × `3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和
  `Rotation(1,3)` — 车辆绕车辆固定俯仰、滚转和偏航 *Y*、*Z* 和 *X*
  轴的旋转，分别对应。
- `Rotation(...,1)`、`Rotation(...,2)` 和
  `Rotation(...,3)` — 角色绕车辆固定俯仰、滚转和偏航 *Y*、*Z* 和 *X*
  轴的旋转，分别对应。

例如，考虑一个具有车身和四个车轮的车辆角色。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的旋转信息。

  Rotation=[PitchvRollvYawvPitchFLRollFLYawFLPitchFRRollFRYawFRPitchRLRollRLYawRLPitchRRRollRRYawRR]

  | Rotation | 数组元素 |
  | --- | --- |
  | 车辆，*Pitchv* | `Rotation(1,1)` |
  | 车辆，*Rollv* | `Rotation(1,2)` |
  | 车辆，*Yawv* | `Rotation(1,3)` |
  | 前左轮，*PitchFL* | `Rotation(2,1)` |
  | 前左轮，*RollFL* | `Rotation(2,2)` |
  | 前左轮，*YawFL* | `Rotation(2,3)` |
  | 前右轮，*PitchFR* | `Rotation(3,1)` |
  | 前右轮，*RollFR* | `Rotation(3,2)` |
  | 前右轮，*YawFR* | `Rotation(3,3)` |
  | 后左轮，*PitchRL* | `Rotation(4,1)` |
  | 后左轮，*RollRL* | `Rotation(4,2)` |
  | 后左轮，*YawRL* | `Rotation(4,3)` |
  | 后右轮，*PitchRR* | `Rotation(5,1)` |
  | 后右轮，*RollRR* | `Rotation(5,2)` |
  | 后右轮，*YawRR* | `Rotation(5,3)` |

### **用于按部件缩放角色的初始数组值，Scale** — 角色初始缩放 `[1 1 1]`（默认） | `array`

角色初始缩放。

数组维度为每个角色的部件数 × `3`。

- `Scale(1,1)`、`Scale(1,2)` 和
  `Scale(1,3)` — 车辆沿世界 *X*、
  *Y* 和 *Z* 轴的缩放，分别对应。
- `Scale(...,1)`、`Scale(...,2)` 和
  `Scale(...,3)` — 角色沿世界 *X*、
  *Y* 和 *Z* 轴的缩放，分别对应。

例如，考虑一个具有车身和四个车轮的车辆角色。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的缩放信息。

  Scale=[XVscaleYVscaleZVscaleXFLscaleYFLscaleZFLscaleXFRscaleYFRscaleZFRscaleXRLscaleYRLscaleZRLscaleXRRscaleYRRscaleZRRscale]

  | Scale | 数组元素 | 缩放轴 |
  | --- | --- | --- |
  | 车辆，*Xvscale* | `Scale(1,1)` | 世界 *X* 轴 |
  | 车辆，*Yvscale* | `Scale(1,2)` | 世界 *Y* 轴 |
  | 车辆，*Zvscale* | `Scale(1,3)` | 世界 *Z* 轴 |
  | 前左轮，*XFLscale* | `Scale(2,1)` | 世界 *X* 轴 |
  | 前左轮，*YFLscale* | `Scale(2,2)` | 世界 *Y* 轴 |
  | 前左轮，*ZFLscale* | `Scale(2,3)` | 世界 *Z* 轴 |
  | 前右轮，*XFRscale* | `Scale(3,1)` | 世界 *X* 轴 |
  | 前右轮，*YFRscale* | `Scale(3,2)` | 世界 *Y* 轴 |
  | 前右轮，*ZFRscale* | `Scale(3,3)` | 世界 *Z* 轴 |
  | 后左轮，*XRLscale* | `Scale(4,1)` | 世界 *X* 轴 |
  | 后左轮，*YRLscale* | `Scale(4,2)` | 世界 *Y* 轴 |
  | 后左轮，*ZRLscale* | `Scale(4,3)` | 世界 *Z* 轴 |
  | 后右轮，*XRRscale* | `Scale(5,1)` | 世界 *X* 轴 |
  | 后右轮，*YRRscale* | `Scale(5,2)` | 世界 *Y* 轴 |
  | 后右轮，*ZRRscale* | `Scale(5,3)` | 世界 *Z* 轴 |

### **采样时间** — 采样时间 `-1`（默认） | `scalar`

采样时间，*Ts*。图形帧率
是采样时间的倒数。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Actor Transform Set 模块仿真模型需要
Simulink
3D Animation。

## 描述

设置角色平移、旋转、缩放

**注意**

使用 Simulation 3D Actor Transform Set 模块仿真模型需要
Simulink®
3D Animation™。

Simulation 3D Actor Transform Set 模块设置 3D 可视化环境中的角色平移、
旋转和缩放。

该模块使用
最初与惯性世界坐标系对齐的车辆固定坐标系。

坐标系图像，显示分别绕 x、y 和 z 轴的滚转、俯仰和偏航

| 轴 | 描述 |
| --- | --- |
| *X* | 车辆前进方向  滚转 — 绕 *X* 轴的右手旋转 |
| *Y* | 向车辆右侧延伸，最初平行于地面  俯仰 — 绕 *Y* 轴的右手旋转 |
| *Z* | 向上延伸  偏航 — 绕 *Z* 轴的左手旋转 |

角色是支持 3D 平移、
旋转和缩放的场景对象。部件是角色组件。组件本身不存在；
它们与角色关联。

**提示**

验证 Simulation 3D Actor Transform
Set 模块在 Simulation 3D Scene Configuration
模块之前执行。这样，Simulation 3D Actor Transform Set 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备好该信号数据。要检查模块执行顺序，
请右键单击这些模块并选择 **属性**。在
**常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Actor Transform Set — `-1`

有关执行顺序的详细信息，请参阅控制和显示执行顺序。
