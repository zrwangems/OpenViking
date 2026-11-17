---
type: simulink-block
title: 'Simulation 3D Actor Transform Set'
family: 'simulation-3d'
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

Actor 平移，单位为 m。数组维度为每个 Actor 的部件数 × `3`。

- `Translation(1,1)`、`Translation(1,2)` 和 `Translation(1,3)` — 车辆分别沿世界 *X*、*Y* 和 *Z* 轴的位移。
- `Translation(...,1)`、`Translation(...,2)` 和 `Translation(...,3)` — Actor 相对于车辆的位移，位于初始与世界 *X*、*Y* 和 *Z* 轴对齐的车辆固定坐标系中。

例如，考虑具有车身和四个车轮的车辆 Actor。`Translation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置相对于车辆的平移信息。

  Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

  | Translation | 数组元素 |
  | --- | --- |
  | 车辆, *Xv* | `Translation(1,1)` |
  | 车辆, *Yv* | `Translation(1,2)` |
  | 车辆, *Zv* | `Translation(1,3)` |
  | 左前轮, *XFL* | `Translation(2,1)` |
  | 左前轮, *YFL* | `Translation(2,2)` |
  | 左前轮, *ZFL* | `Translation(2,3)` |
  | 右前轮, *XFR* | `Translation(3,1)` |
  | 右前轮, *YFR* | `Translation(3,2)` |
  | 右前轮, *ZFR* | `Translation(3,3)` |
  | 左后轮, *XRL* | `Translation(4,1)` |
  | 左后轮, *YRL* | `Translation(4,2)` |
  | 左后轮, *ZRL* | `Translation(4,3)` |
  | 右后轮, *XRR* | `Translation(5,1)` |
  | 右后轮, *YRR* | `Translation(5,2)` |
  | 右后轮, *ZRR* | `Translation(5,3)` |

### **Rotation** — Actor 旋转 `array`

Actor 旋转，单位为 rad。数组维度为每个 Actor 的部件数 × `3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和 `Rotation(1,3)` — 车辆分别绕车辆固定的俯仰、侧倾和偏航 *Y*、*Z* 和 *X* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和 `Rotation(...,3)` — Actor 分别绕车辆固定的俯仰、侧倾和偏航 *Y*、*X* 和 *Z* 轴的旋转。

例如，考虑具有车身和四个车轮的车辆 Actor。`Rotation` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置的旋转信息。

  Rotation=[PitchvRollvYawvPitchFLRollFLYawFLPitchFRRollFRYawFRPitchRLRollRLYawRLPitchRRRollRRYawRR]

  | Rotation | 数组元素 |
  | --- | --- |
  | 车辆, *Pitchv* | `Rotation(1,1)` |
  | 车辆, *Rollv* | `Rotation(1,2)` |
  | 车辆, *Yawv* | `Rotation(1,3)` |
  | 左前轮, *PitchFL* | `Rotation(2,1)` |
  | 左前轮, *RollFL* | `Rotation(2,2)` |
  | 左前轮, *YawFL* | `Rotation(2,3)` |
  | 右前轮, *PitchFR* | `Rotation(3,1)` |
  | 右前轮, *RollFR* | `Rotation(3,2)` |
  | 右前轮, *YawFR* | `Rotation(3,3)` |
  | 左后轮, *PitchRL* | `Rotation(4,1)` |
  | 左后轮, *RollRL* | `Rotation(4,2)` |
  | 左后轮, *YawRL* | `Rotation(4,3)` |
  | 右后轮, *PitchRR* | `Rotation(5,1)` |
  | 右后轮, *RollRR* | `Rotation(5,2)` |
  | 右后轮, *YawRR* | `Rotation(5,3)` |

### **Scale** — Actor 缩放 `array`

Actor 缩放。数组维度为每个 Actor 的部件数 × `3`。

- `Scale(1,1)`、`Scale(1,2)` 和 `Scale(1,3)` — 车辆分别沿世界 *X*、*Y* 和 *Z* 轴的缩放。
- `Scale(...,1)`、`Scale(...,2)` 和 `Scale(...,3)` — Actor 分别沿世界 *X*、*Y* 和 *Z* 轴的缩放。

例如，考虑具有车身和四个车轮的车辆 Actor。`Scale` 信号：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置的缩放信息。

  Scale=[XVscaleYVscaleZVscaleXFLscaleYFLscaleZFLscaleXFRscaleYFRscaleZFRscaleXRLscaleYRLscaleZRLscaleXRRscaleYRRscaleZRRscale]

  | Scale | 数组元素 |
  | --- | --- |
  | 车辆, *Xvscale* | `Scale(1,1)` |
  | 车辆, *Yvscale* | `Scale(1,2)` |
  | 车辆, *Zvscale* | `Scale(1,3)` |
  | 左前轮, *XFLscale* | `Scale(2,1)` |
  | 左前轮, *YFLscale* | `Scale(2,2)` |
  | 左前轮, *ZFLscale* | `Scale(2,3)` |
  | 右前轮, *XFRscale* | `Scale(3,1)` |
  | 右前轮, *YFRscale* | `Scale(3,2)` |
  | 右前轮, *ZFRscale* | `Scale(3,3)` |
  | 左后轮, *XRLscale* | `Scale(4,1)` |
  | 左后轮, *YRLscale* | `Scale(4,2)` |
  | 左后轮, *ZRLscale* | `Scale(4,3)` |
  | 右后轮, *XRRscale* | `Scale(5,1)` |
  | 右后轮, *YRRscale* | `Scale(5,2)` |
  | 右后轮, *ZRRscale* | `Scale(5,3)` |

## 参数

#### Actor 设置

### **3D 场景中 Actor 的标签, ActorTag** — 名称 `SimulinkActor1`（默认） | character vector

Actor 名称。

Actor 是支持 3D 平移、旋转和缩放的场景对象。部件是 Actor 组件。组件本身不存在；它们与 Actor 关联。

该模块不支持同一 actor 标签的多个实例。当使用 3D 模块对（例如 Simulation 3D Actor Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景 actor 时，请指定相同的 **3D 场景中 Actor 的标签, ActorTag** 参数。

### **要设置的每个 Actor 的部件数量, NumberOfParts** — 名称 `1`（默认） | `scalar`

每个 Actor 的部件数量。Actor 是支持 3D 平移、旋转和缩放的场景对象。部件是 Actor 组件。组件本身不存在；它们与 Actor 关联。通常，具有车身和四个车轮的车辆 Actor 有 5 个部件。

该模块不支持同一 actor 标签的多个实例。当使用 3D 模块对（例如 Simulation 3D Actor Transform Get 和 Simulation 3D Actor Transform Set）引用同一场景 actor 时，请指定相同的 **3D 场景中 Actor 的标签, ActorTag** 参数。

### **坐标系** — 用于 Actor 变换的坐标系 `Default`（默认） | `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定 Actor 在 3D 环境中用于平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB® 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Simulink 3D Animation 中的坐标系。

**示例:** `MATLAB`

#### 初始值

### **用于逐部件平移 Actor 的初始数组值, Translation** — Actor 初始位置 `[0 0 0]`（默认） | `array`

Actor 初始位置，沿世界 *X*、*Y* 和 *Z* 轴，单位为 m。

数组维度为每个 Actor 的部件数 × `3`。

- `Translation(1,1)`、`Translation(1,2)` 和 `Translation(1,3)` — 车辆分别沿世界 *X*、*Y* 和 *Z* 轴的位移。
- `Translation(...,1)`、`Translation(...,2)` 和 `Translation(...,3)` — Actor 相对于车辆的位移，位于初始与世界 *X*、*Y* 和 *Z* 轴对齐的车辆固定坐标系中。

例如，考虑具有车身和四个车轮的车辆 Actor。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置相对于车辆的平移信息。

  Translation=[XvYvZvXFLYFLZFLXFRYFRZFRXRLYRLZRLXRRYRRZRR]

  | Translation | 数组元素 |
  | --- | --- |
  | 车辆, *Xv* | `Translation(1,1)` |
  | 车辆, *Yv* | `Translation(1,2)` |
  | 车辆, *Zv* | `Translation(1,3)` |
  | 左前轮, *XFL* | `Translation(2,1)` |
  | 左前轮, *YFL* | `Translation(2,2)` |
  | 左前轮, *ZFL* | `Translation(2,3)` |
  | 右前轮, *XFR* | `Translation(3,1)` |
  | 右前轮, *YFR* | `Translation(3,2)` |
  | 右前轮, *ZFR* | `Translation(3,3)` |
  | 左后轮, *XRL* | `Translation(4,1)` |
  | 左后轮, *YRL* | `Translation(4,2)` |
  | 左后轮, *ZRL* | `Translation(4,3)` |
  | 右后轮, *XRR* | `Translation(5,1)` |
  | 右后轮, *YRR* | `Translation(5,2)` |
  | 右后轮, *ZRR* | `Translation(5,3)` |

### **用于逐部件旋转 Actor 的初始数组值, Rotation** — Actor 初始旋转 `[0 0 0]`（默认） | `array`

Actor 初始旋转，绕世界 *X*、*Y* 和 *Z* 轴，范围为 [-pi/2, pi/2]，单位为 rad。

数组维度为每个 Actor 的部件数 × `3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和 `Rotation(1,3)` — 车辆分别绕车辆固定的俯仰、侧倾和偏航 *Y*、*Z* 和 *X* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和 `Rotation(...,3)` — Actor 分别绕车辆固定的俯仰、侧倾和偏航 *Y*、*X* 和 *Z* 轴的旋转。

例如，考虑具有车身和四个车轮的车辆 Actor。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置的旋转信息。

  Rotation=[PitchvRollvYawvPitchFLRollFLYawFLPitchFRRollFRYawFRPitchRLRollRLYawRLPitchRRRollRRYawRR]

  | Rotation | 数组元素 |
  | --- | --- |
  | 车辆, *Pitchv* | `Rotation(1,1)` |
  | 车辆, *Rollv* | `Rotation(1,2)` |
  | 车辆, *Yawv* | `Rotation(1,3)` |
  | 左前轮, *PitchFL* | `Rotation(2,1)` |
  | 左前轮, *RollFL* | `Rotation(2,2)` |
  | 左前轮, *YawFL* | `Rotation(2,3)` |
  | 右前轮, *PitchFR* | `Rotation(3,1)` |
  | 右前轮, *RollFR* | `Rotation(3,2)` |
  | 右前轮, *YawFR* | `Rotation(3,3)` |
  | 左后轮, *PitchRL* | `Rotation(4,1)` |
  | 左后轮, *RollRL* | `Rotation(4,2)` |
  | 左后轮, *YawRL* | `Rotation(4,3)` |
  | 右后轮, *PitchRR* | `Rotation(5,1)` |
  | 右后轮, *RollRR* | `Rotation(5,2)` |
  | 右后轮, *YawRR* | `Rotation(5,3)` |

### **用于逐部件缩放 Actor 的初始数组值, Scale** — Actor 初始缩放 `[1 1 1]`（默认） | `array`

Actor 初始缩放。

数组维度为每个 Actor 的部件数 × `3`。

- `Scale(1,1)`、`Scale(1,2)` 和 `Scale(1,3)` — 车辆分别沿世界 *X*、*Y* 和 *Z* 轴的缩放。
- `Scale(...,1)`、`Scale(...,2)` 和 `Scale(...,3)` — Actor 分别沿世界 *X*、*Y* 和 *Z* 轴的缩放。

例如，考虑具有车身和四个车轮的车辆 Actor。该参数：

- 维度为 `[5x3]`。
- 包含根据车轴和车轮位置的缩放信息。

  Scale=[XVscaleYVscaleZVscaleXFLscaleYFLscaleZFLscaleXFRscaleYFRscaleZFRscaleXRLscaleYRLscaleZRLscaleXRRscaleYRRscaleZRRscale]

  | Scale | 数组元素 | 缩放轴 |
  | --- | --- | --- |
  | 车辆, *Xvscale* | `Scale(1,1)` | 世界 *X* 轴 |
  | 车辆, *Yvscale* | `Scale(1,2)` | 世界 *Y* 轴 |
  | 车辆, *Zvscale* | `Scale(1,3)` | 世界 *Z* 轴 |
  | 左前轮, *XFLscale* | `Scale(2,1)` | 世界 *X* 轴 |
  | 左前轮, *YFLscale* | `Scale(2,2)` | 世界 *Y* 轴 |
  | 左前轮, *ZFLscale* | `Scale(2,3)` | 世界 *Z* 轴 |
  | 右前轮, *XFRscale* | `Scale(3,1)` | 世界 *X* 轴 |
  | 右前轮, *YFRscale* | `Scale(3,2)` | 世界 *Y* 轴 |
  | 右前轮, *ZFRscale* | `Scale(3,3)` | 世界 *Z* 轴 |
  | 左后轮, *XRLscale* | `Scale(4,1)` | 世界 *X* 轴 |
  | 左后轮, *YRLscale* | `Scale(4,2)` | 世界 *Y* 轴 |
  | 左后轮, *ZRLscale* | `Scale(4,3)` | 世界 *Z* 轴 |
  | 右后轮, *XRRscale* | `Scale(5,1)` | 世界 *X* 轴 |
  | 右后轮, *YRRscale* | `Scale(5,2)` | 世界 *Y* 轴 |
  | 右后轮, *ZRRscale* | `Scale(5,3)` | 世界 *Z* 轴 |

### **采样时间** — 采样时间 `-1`（默认） | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

### R2025a：设置坐标系参数

在 Simulation 3D Actor Transform Set 模块中设置 **坐标系** 参数，以表示 3D 环境中 Actor 变换的坐标系。

## 描述

设置 Actor 平移、旋转、缩放

Simulation 3D Actor Transform Set 模块在 3D 可视化环境中设置 Actor 平移、旋转和缩放。

该模块的 **坐标系** 参数指定 Actor 变换在 3D 环境中的应用方式。该模块的输出也遵循指定的坐标系。

Actor 是支持 3D 平移、旋转和缩放的场景对象。部件是 Actor 组件。组件本身不存在；它们与 Actor 关联。

**提示**

验证 Simulation 3D Actor Transform Set 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Actor Transform Set 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备好这些数据。要检查模块执行顺序，请右键点击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Actor Transform Set — `-1`

有关执行顺序的更多信息，请参阅 Control and Display Execution Order (Simulink)。
