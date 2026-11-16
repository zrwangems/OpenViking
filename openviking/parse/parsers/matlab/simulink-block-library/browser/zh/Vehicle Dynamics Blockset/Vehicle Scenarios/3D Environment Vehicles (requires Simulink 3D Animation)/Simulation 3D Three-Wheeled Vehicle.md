---
type: simulink-block
title: 'Simulation 3D Three-Wheeled Vehicle'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dthreewheeledvehicle'
documentation_source_path: 'ref/simulation3dthreewheeledvehicle.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Three-Wheeled Vehicle

## 端口

### 输入

### **Translation** — 车辆平移 5-by-3 数组

车辆和车轮平移，单位为 m。数组维度为 5-by-3。

- `Translation(1,1)`、`Translation(1,2)` 和 `Translation(1,3)` — 车辆分别沿惯性车辆 *Z*-down *X*-、*Y*- 和 *Z*- 轴的平移。
- `Translation(...,1)`、`Translation(...,2)` 和 `Translation(...,3)` — 车轮相对于车辆的平移，分别沿车辆 *Z*-down *X*-、*Y*- 和 *Z*- 轴。

该信号包含根据车轴和车轮位置确定的平移信息。

Translation=[XvYvZvXHYHZHXFYFZFXRLYRLZRLXRRYRRZRR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆, *Xv* | `Translation(1,1)` | 惯性车辆 *Z*-down *X*-轴 |
| 车辆, *Yv* | `Translation(1,2)` | 惯性车辆 *Z*-down *Y*-轴 |
| 车辆, *Zv* | `Translation(1,3)` | 惯性车辆 *Z*-down *Z*-轴 |
| 车把, *XH* | `Translation(2,1)` | 惯性车辆 *Z*-down *X*-轴 |
| 车把, *YH* | `Translation(2,2)` | 惯性车辆 *Z*-down *Y*-轴 |
| 车把, *ZH* | `Translation(2,3)` | 惯性车辆 *Z*-down *Z*-轴 |
| 前轮, *XF* | `Translation(3,1)` | 车辆 *Z*-down *X*-轴 |
| 前轮, *YF* | `Translation(3,2)` | 车辆 *Z*-down *Y*-轴 |
| 前轮, *ZF* | `Translation(3,3)` | 车辆 *Z*-down *Z*-轴 |
| 后左轮, *XRL* | `Translation(4,1)` | 车辆 *Z*-down *X*-轴 |
| 后左轮, *YRL* | `Translation(4,2)` | 车辆 *Z*-down *Y*-轴 |
| 后左轮, *ZRL* | `Translation(4,3)` | 车辆 *Z*-down *Z*-轴 |
| 后右轮, *XRR* | `Translation(5,1)` | 车辆 *Z*-down *X*-轴 |
| 后右轮, *YRR* | `Translation(5,2)` | 车辆 *Z*-down *Y*-轴 |
| 后右轮, *ZRR* | `Translation(5,3)` | 车辆 *Z*-down *Z*-轴 |

### **Rotation** — 车辆旋转 5-by-3 数组

车辆和车轮旋转，单位为 rad。数组维度为 5-by-3。

- `Rotation(1,1)`、`Rotation(1,2)` 和 `Rotation(1,3)` — 车辆分别绕惯性车辆 *Z*-down *X*-、*Y*- 和 *Z*- 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和 `Rotation(...,3)` — 车轮相对于车辆的旋转，分别绕车辆 *Z*-down *X*-、*Y*- 和 *Z*- 轴。

**注意**

如果为前轮提供的 yaw 值与为车把提供的 yaw 值不同，则前轮使用车把的 yaw 值。车把和前轮的 yaw 值限制在 [-30, 30] degrees 范围内。

该信号包含根据车轴和车轮位置确定的旋转信息。

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆, *Rollv* | `Rotation(1,1)` | 惯性车辆 *Z*-down *X*-轴 |
| 车辆, *Pitchv* | `Rotation(1,2)` | 惯性车辆 *Z*-down *Y*-轴 |
| 车辆, *Yawv* | `Rotation(1,3)` | 惯性车辆 *Z*-down *Z*-轴 |
| 车把, *RollH* | `Rotation(2,1)` | 惯性车辆 *Z*-down *X*-轴 |
| 车把, *PitchH* | `Rotation(2,2)` | 惯性车辆 *Z*-down *Y*-轴 |
| 车把, *YawH* | `Rotation(2,3)` | 惯性车辆 *Z*-down *Z*-轴 |
| 前轮, *RollF* | `Rotation(3,1)` | 车辆 *Z*-down *X*-轴 |
| 前轮, *PitchF* | `Rotation(3,2)` | 车辆 *Z*-down *Y*-轴 |
| 前轮, *YawF* | `Rotation(3,3)` | 车辆 *Z*-down *Z*-轴 |
| 后左轮, *RollRL* | `Rotation(4,1)` | 车辆 *Z*-down *X*-轴 |
| 后左轮, *PitchRL* | `Rotation(4,2)` | 车辆 *Z*-down *Y*-轴 |
| 后左轮, *YawRL* | `Rotation(4,3)` | 车辆 *Z*-down *Z*-轴 |
| 后右轮, *RollRR* | `Rotation(5,1)` | 车辆 *Z*-down *X*-轴 |
| 后右轮, *PitchRR* | `Rotation(5,2)` | 车辆 *Z*-down *Y*-轴 |
| 后右轮, *YawRR* | `Rotation(5,3)` | 车辆 *Z*-down *Z*-轴 |

### **Light controls** — 车辆灯光控制 1-by-6 向量

灯光控制输入信号，指定为 1-by-6 Boolean 向量。向量的每个元素按照下表打开或关闭特定车辆灯光。值为 1 打开灯光；值为 0 关闭灯光。

| 向量元素 | 车辆灯光 |
| --- | --- |
| (1,1) | 前照灯远光 |
| (1,2) | 前照灯近光 |
| (1,3) | 制动 |
| (1,4) | 倒车 |
| (1,5) | 左信号 |
| (1,6) | 右信号 |

#### 依赖关系

要创建此端口，请在 **Light Controls** 选项卡上选择 **Enable light controls**。

**数据类型：** `Boolean`

## 参数

### 车辆参数

### **Type** — 车辆类型 `Tuk tuk`（默认）

车辆类型。默认情况下，**Type** 设置为 `Tuk tuk`。有关车辆尺寸，请参阅 Tuk tuk。

### **Name** — 车辆名称 `SimulinkVehicle1`（默认）| character vector

车辆名称。默认情况下，当您在模型中使用该模块时，该模块将 **Name** 参数设置为 `SimulinkVehicleX`。`X` 的值取决于模型中 Simulation 3D Vehicle with Ground Following 和 Simulation 3D Vehicle 模块的数量。

### **Sample time** — 采样时间 `-1`（默认）| `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

### 初始值

### **Initial array values to translate vehicle per part, Translation** — 车辆初始平移 zeros( 5, 3 )（默认）| 5-by-3 数组

初始车辆和车轮平移，单位为 m。数组维度为 5-by-3。

- `Translation(1,1)`、`Translation(1,2)` 和 `Translation(1,3)` — 初始车辆分别沿惯性车辆 *Z*-down 坐标系 *X*-、*Y*- 和 *Z*- 轴的平移。
- `Translation(...,1)`、`Translation(...,2)` 和 `Translation(...,3)` — 初始车轮相对于车辆的平移，分别沿车辆 *Z*-down *X*-、*Y*- 和 *Z*- 轴。

该参数包含根据车轴和车轮位置确定的平移信息。

Translation=[XvYvZvXHYHZHXFYFZFXRLYRLZRLXRRYRRZRR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 车辆, *Xv* | `Translation(1,1)` | 惯性车辆 *Z*-down *X*-轴 |
| 车辆, *Yv* | `Translation(1,2)` | 惯性车辆 *Z*-down *Y*-轴 |
| 车辆, *Zv* | `Translation(1,3)` | 惯性车辆 *Z*-down *Z*-轴 |
| 车把, *XH* | `Translation(2,1)` | 车辆 *Z*-down *X*-轴 |
| 车把, *YH* | `Translation(2,2)` | 车辆 *Z*-down *Y*-轴 |
| 车把, *ZH* | `Translation(2,3)` | 车辆 *Z*-down *Z*-轴 |
| 前轮, *XF* | `Translation(3,1)` | 车辆 *Z*-down *X*-轴 |
| 前轮, *YF* | `Translation(3,2)` | 车辆 *Z*-down *Y*-轴 |
| 前轮, *ZF* | `Translation(3,3)` | 车辆 *Z*-down *Z*-轴 |
| 后左轮, *XRL* | `Translation(4,1)` | 车辆 *Z*-down *X*-轴 |
| 后左轮, *YRL* | `Translation(4,2)` | 车辆 *Z*-down *Y*-轴 |
| 后左轮, *ZRL* | `Translation(4,3)` | 车辆 *Z*-down *Z*-轴 |
| 后右轮, *XRR* | `Translation(5,1)` | 车辆 *Z*-down *X*-轴 |
| 后右轮, *YRR* | `Translation(5,2)` | 车辆 *Z*-down *Y*-轴 |
| 后右轮, *ZRR* | `Translation(5,3)` | 车辆 *Z*-down *Z*-轴 |

### **Initial array values to rotate vehicle per part, Rotation** — 车辆初始旋转 zeros( 5, 3 )（默认）| 5-by-3 数组

初始车辆和车轮旋转，绕车辆 *Z*-down *X*-、*Y*- 和 *Z*- 轴。

数组维度为 5-by-3。

- `Rotation(1,1)`、`Rotation(1,2)` 和 `Rotation(1,3)` — 初始车辆分别绕惯性车辆 *Z*-down 坐标系 *X*-、*Y*- 和 *Z*- 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和 `Rotation(...,3)` — 初始车轮相对于车辆的旋转，分别绕车辆 *Z*-down *X*-、*Y*- 和 *Z*- 轴。

该参数包含根据车轴和车轮位置确定的旋转信息。

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRLPitchRLYawRLRollRRPitchRRYawRR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆, *Rollv* | `Rotation(1,1)` | 惯性车辆 *Z*-down *X*-轴 |
| 车辆, *Pitchv* | `Rotation(1,2)` | 惯性车辆 *Z*-down *Y*-轴 |
| 车辆, *Yawv* | `Rotation(1,3)` | 惯性车辆 *Z*-down *Z*-轴 |
| 车把, *RollH* | `Rotation(2,1)` | 车辆 *Z*-down *X*-轴 |
| 车把, *PitchH* | `Rotation(2,2)` | 车辆 *Z*-down *Y*-轴 |
| 车把, *YawH* | `Rotation(2,3)` | 车辆 *Z*-down *Z*-轴 |
| 前轮, *RollF* | `Rotation(3,1)` | 车辆 *Z*-down *X*-轴 |
| 前轮, *PitchF* | `Rotation(3,2)` | 车辆 *Z*-down *Y*-轴 |
| 前轮, *YawF* | `Rotation(3,3)` | 车辆 *Z*-down *Z*-轴 |
| 后左轮, *RollRL* | `Rotation(4,1)` | 车辆 *Z*-down *X*-轴 |
| 后左轮, *PitchRL* | `Rotation(4,2)` | 车辆 *Z*-down *Y*-轴 |
| 后左轮, *YawRL* | `Rotation(4,3)` | 车辆 *Z*-down *Z*-轴 |
| 后右轮, *RollRR* | `Rotation(5,1)` | 车辆 *Z*-down *X*-轴 |
| 后右轮, *PitchRR* | `Rotation(5,2)` | 车辆 *Z*-down *Y*-轴 |
| 后右轮, *YawRR* | `Rotation(5,3)` | 车辆 *Z*-down *Z*-轴 |

### 灯光控制

### **Enable light controls** — 控制车辆灯光的选项 `off`（默认）| `on`

选择是否控制车辆前照灯。使用已启用的参数设置灯光参数，包括前照灯强度。

#### 依赖关系

选择此参数：

- 创建输入端口 `Light controls`。
- 启用这些灯光参数。

  | 灯光 | 灯光参数 |
  | --- | --- |
  | **前照灯** | - **Headlight color** - **High beam   intensity** - **Low beam   intensity** - **High beam cone half   angle** - **Low beam cone half   angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **制动灯** | **Brake light intensity** |
  | **倒车灯** | **Reverse light intensity** |
  | **转向信号灯** | - **Turn signal light   intensity** - **Period** - **Pulse width** |

#### 前照灯

### **Headlight color [R,G,B], HeadlightColor** — 前照灯颜色 `[1,1,1]`（默认）| 1-by-3 向量，由 RGB 三元组值组成

前照灯颜色，指定为归一化的 1-by-3 向量，由 RGB 三元组值组成。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `int8` | `uint8`

### **High beam intensity, HighBeamIntensity** — 远光强度 `100000`（默认）| 正标量

远光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam intensity, LowBeamIntensity** — 近光强度 `60000`（默认）| 正标量

近光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **High beam cone half angle, HighBeamConeAngle** — 远光锥半角 `1.22`（默认）| 小于 pi/2 的正标量

远光锥半角，单位为 rad。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam cone half angle, LowBeamConeAngle** — 近光锥半角 `1.22`（默认）| 小于 pi/2 的正标量

近光锥半角，单位为 rad。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Left headlight beam orientation [Pitch, Yaw], LeftHeadlightOrientation** — 左前照灯光束方向 `[0,0]`（默认）| 1-by-2 向量，值介于 -pi 和 pi 之间

左前照灯光束在 *Z*-down 坐标系中的 pitch 和 yaw 方向，指定为 1-by-2 向量，单位为 rad。向量的第一个元素 `[1,1]` 是 pitch 角。向量的第二个元素 `[1,2]` 是 yaw 角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Right headlight beam orientation [Pitch, Yaw], RightHeadlightOrientation** — 右前照灯光束方向 `[0,0]`（默认）| 1-by-2 向量，值介于 -pi 和 pi 之间

右前照灯光束在 *Z*-down 坐标系中的 pitch 和 yaw 方向，指定为 1-by-2 向量，单位为 rad。向量的第一个元素 `[1,1]` 是 pitch 角。向量的第二个元素 `[1,2]` 是 yaw 角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

#### 制动灯

### **Brake light intensity, BrakelightIntensity** — 制动灯强度 `500`（默认）| 正标量

制动灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

#### 倒车灯

### **Reverse light intensity, ReverselightIntensity** — 倒车灯强度 `500`（默认）| 正标量

倒车灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

#### 转向信号灯

### **Turn signal light intensity, SignallightIntensity** — 转向信号灯强度 `500`（默认）| 正标量

转向信号灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Period, SignallightPeriod** — 转向信号灯周期 `1`（默认）| 正标量

转向信号灯周期，单位为 s。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Pulse width, SignalPulseWidth** — 脉冲宽度 `50`（默认）| 小于 100 的正标量

转向信号灯脉冲宽度，指定为周期的百分比。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Three-Wheeled Vehicle 模块仿真模型需要 Simulink 3D Animation。

## 描述

在 3D 环境中实现三轮车辆

**注意**

使用 Simulation 3D Three-Wheeled Vehicle 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Three-Wheeled Vehicle 模块在 3D 仿真环境中实现一个带三个车轮的车辆。

要使用此模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。如果将此模块的 **Sample time** 参数设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE J6701 中定义的车辆 Z-down right-handed (RH) Cartesian 坐标系。该坐标系为惯性坐标系，并且初始与车辆几何中心对齐：

- *X*-轴 — 沿车辆纵轴，指向前方
- *Y*-轴 — 沿车辆横轴，指向右侧
- *Z*-轴 — 指向下方

**提示**

验证 Simulation 3D Three-Wheeled Vehicle 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Three-Wheeled Vehicle 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备好信号数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Three-Wheeled Vehicle — `-1`

有关执行顺序的更多信息，请参阅 Control and Display Execution Order。
