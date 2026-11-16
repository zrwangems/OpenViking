---
type: simulink-block
title: 'Simulation 3D Actor Transform Get'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dactortransformget'
documentation_source_path: 'ref/simulation3dactortransformget.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Actor Transform Get

## 端口

### 输出

### **Translation** — 角色平移 `array`

角色平移，单位为 m。数组维度为每个角色的部件数乘 `3`。

- `Translation(1,1)`、`Translation(1,2)` 和 `Translation(1,3)` — 车辆分别沿世界 *X*、*Y* 和 *Z* 轴的位移。
- `Translation(...,1)`、`Translation(...,2)` 和 `Translation(...,3)` — 角色相对于车辆的位移，在最初与世界 *X*、*Y* 和 *Z* 轴对齐的车辆固定坐标系中。

例如，考虑一个具有车身和四个车轮的车辆角色。`Translation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的、相对于车辆的平移信息。

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

### **Rotation** — 角色旋转 `array`

角色旋转，单位为 rad。数组维度为每个角色的部件数乘 `3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和 `Rotation(1,3)` — 车辆分别绕车辆固定的 pitch、roll 和 yaw *Y*、*Z* 和 *X* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和 `Rotation(...,3)` — 角色分别绕车辆固定的 pitch、roll 和 yaw *Y*、*X* 和 *Z* 轴的旋转。

例如，考虑一个具有车身和四个车轮的车辆角色。`Rotation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的旋转信息。

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

- `Scale(1,1)`、`Scale(1,2)` 和 `Scale(1,3)` — 车辆分别沿世界 *X*、*Y* 和 *Z* 轴的缩放。
- `Scale(...,1)`、`Scale(...,2)` 和 `Scale(...,3)` — 角色分别沿世界 *X*、*Y* 和 *Z* 轴的缩放。

例如，考虑一个具有车身和四个车轮的车辆角色。`Scale` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置确定的缩放信息。

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

### **Tag for actor in 3D scene, ActorTag** — 名称 `SimulinkActor1` (默认) | character vector

角色名称。

角色是支持 3D 平移、旋转和缩放的场景对象。部件是角色的组件。组件本身不存在；它们与角色关联。

该模块不支持同一角色标签的多个实例。当你使用 3D 模块对（例如 Simulation 3D Actor Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景角色时，请指定相同的 **Tag for actor in 3D scene, ActorTag** 参数。

### **Number of parts per actor to get, NumberOfParts** — 名称 `1` (默认) | `scalar`

每个角色的部件数。角色是支持 3D 平移、旋转和缩放的场景对象。部件是角色的组件。组件本身不存在；它们与角色关联。通常，一个具有车身和四个车轮的车辆角色有 5 个部件。

该模块不支持同一角色标签的多个实例。当你使用 3D 模块对（例如 Simulation 3D Actor Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景角色时，请指定相同的 **Tag for actor in 3D scene, ActorTag** 参数。

### **Sample time** — 采样时间 `-1` (默认) | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018a 中引入**

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Actor Transform Get 模块仿真模型需要 Simulink 3D Animation。

## 描述

获取角色平移、旋转、缩放

**注意**

使用 Simulation 3D Actor Transform Get 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Actor Transform Get 模块为 Simulink 仿真环境提供角色平移、旋转和缩放。

该模块使用车辆固定坐标系，该坐标系最初与惯性世界坐标系对齐。

坐标系图像，分别显示绕 x、y 和 z 轴的 roll、pitch 和 yaw

| 轴 | 描述 |
| --- | --- |
| *X* | 车辆前进方向  Roll — 绕 *X* 轴的右手旋转 |
| *Y* | 向车辆右侧延伸，最初平行于地平面  Pitch — 绕 *Y* 轴的右手旋转 |
| *Z* | 向上延伸  Yaw — 绕 *Z* 轴的左手旋转 |

角色是支持 3D 平移、旋转和缩放的场景对象。部件是角色的组件。组件本身不存在；它们与角色关联。

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Actor Transform Get 模块之前执行。这样，Unreal Engine® 3D 可视化环境会在 Simulation 3D Actor Transform Get 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Actor Transform Get — `1`

有关执行顺序的更多信息，请参阅 Control and Display Execution Order。
