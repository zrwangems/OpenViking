---
type: simulink-block
title: 'Simulation 3D Motorcycle'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dmotorcycle'
documentation_source_path: 'ref/simulation3dmotorcycle.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Motorcycle

## 端口

### 输入

### **Translation** — 摩托车平移 `4`-by-`3` 数组

摩托车和部件平移，单位为 m。数组维度为 `4`-by-`3`。

- `Translation(1,1)`、`Translation(1,2)`,
  和 `Translation(1,3)` — 摩托车分别沿惯性车辆 Z-down *X*、*Y* 和
  *Z* 轴的平移。
- `Translation(...,1)`、
  `Translation(...,2)` 和 `Translation(...,3)`
  — 摩托车部件相对于车辆的平移，分别沿车辆 Z-down
  *X*、*Y* 和 *Z* 轴。

该信号包含与位置对应的平移信息。

Translation=[XvYvZvXHYHZHXFYFZFXRYRZR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 摩托车，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 摩托车，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 摩托车，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 车把，*XH* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 车把，*YH* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 车把，*ZH* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前轮，*XF* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 前轮，*YF* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前轮，*ZF* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后轮，*XR* | `Translation(4,1)` | 车辆 Z-down *X* 轴 |
| 后轮，*YR* | `Translation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后轮，*ZR* | `Translation(4,3)` | 车辆 Z-down *Z* 轴 |

### **Rotation** — 摩托车旋转 `4`-by-`3` 数组

车辆和部件旋转，单位为 rad。数组维度为
`4`-by-`3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和
  `Rotation(1,3)` — 摩托车分别绕惯性车辆 Z-down *X*、*Y* 和
  *Z* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和
  `Rotation(...,3)` — 摩托车部件相对于车辆绕车辆 Z-down
  *X*、*Y* 和 *Z* 轴的旋转。

该信号包含与位置对应的旋转信息。

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRPitchRYawR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 车把，*RollH* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 车把，*PitchH* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 车把，*YawH* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前轮，*RollF* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 前轮，*PitchF* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前轮，*YawF* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后轮，*RollR* | `Rotation(4,1)` | 车辆 Z-down *X* 轴 |
| 后轮，*PitchR* | `Rotation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后轮，*YawR* | `Rotation(4,3)` | 车辆 Z-down *Z* 轴 |

### **Light controls** — 车辆车灯 on 或 off 1-by-5 向量

Light controls 输入信号，指定为 1-by-5 Boolean 向量。该向量的每个元素按照下表将特定车辆车灯设为 on 或 off。值为 1 将车灯设为 on；值为 0 将车灯设为 off。

| 向量元素 | 车辆车灯 |
| --- | --- |
| (1,1) | 前照灯远光 |
| (1,2) | 前照灯近光 |
| (1,3) | 制动 |
| (1,4) | 左信号 |
| (1,5) | 右信号 |

#### 依赖关系

要创建此端口，请在 **Light Controls** 选项卡上选择
**Enable light controls**。

**数据类型：** `Boolean`

## 参数

### 车辆参数

### **Type** — 类型 `Sports bike`（默认） | `Motor bike` | `Scooter`

使用 **Type** 参数指定摩托车类型。此表提供了指向摩托车尺寸的链接。

| 设置 | 车辆尺寸 |
| --- | --- |
| `Sports bike` | 运动型摩托车 |
| `Motor bike` | 摩托车 |
| `Scooter` | 踏板车 |

### **Color** — 车辆颜色 `Red`（默认） | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver` | `Dazzle Camouflage`

选择车辆颜色。

### **Name** — 摩托车名称 `SimulinkVehicle1`（默认） | character vector

摩托车名称。默认情况下，当您在模型中使用该模块时，模块会将 **Name** 参数设置为
`SimulinkVehicleX`。`X` 的值取决于模型中 3D 仿真模块的数量。

### **Sample time** — 采样时间 `-1`（默认） | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

### 灯光控制

### **Enable light controls, VehLightsControl** — 控制车辆车灯 `off`（默认） | `on`

选择是否控制车辆前照灯。使用启用的参数设置灯光参数，包括前照灯强度。

#### 依赖关系

选择此参数会：

- 创建输入端口 `Light controls`
- 启用这些灯光参数。

  | 灯光 | 灯光参数 |
  | --- | --- |
  | **前照灯** | - **Headlight color** - **High beam intensity** - **Low beam intensity** - **High beam cone half angle** - **Low beam cone half angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **制动灯** | **Brake light intensity** |
  | **转向信号灯** | - **Turn signal light intensity** - **Period** - **Pulse width** |

#### 前照灯

### **Headlight color [R,G,B], HeadlightColor** — 前照灯颜色 `[1,1,1]`（默认） | RGB 三元组值的 1-by-3 向量

前照灯颜色，指定为归一化的 RGB 三元组值的 1-by-3 向量。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `int8` | `uint8`

### **High beam intensity, HighBeamIntensity** — 远光强度 `100000`（默认） | 正标量

远光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam intensity, LowBeamIntensity** — 近光强度 `60000`（默认） | 正标量

近光强度，单位为 cd。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **High beam cone half angle, HighBeamConeAngle** — 远光锥半角 `1.22`（默认） | 小于 pi/2 的正标量

远光锥半角，单位为 rad。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Low beam cone half angle, LowBeamConeAngle** — 近光锥半角 `1.22`（默认） | 小于 pi/2 的正标量

近光锥半角，单位为 rad。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Left headlight beam orientation [Pitch, Yaw], LeftHeadlightOrientation** — 左前照灯光束方向 `[0,0]`（默认） | 值介于 -pi 和 pi 之间的 1-by-2 向量

在 *Z*-down 坐标系中左前照灯光束方向的俯仰角和偏航角，指定为 1-by-2 向量，单位为 rad。
向量的第一个元素 `[1,1]` 是俯仰角。向量的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Right headlight beam orientation [Pitch, Yaw], RightHeadlightOrientation** — 右前照灯光束方向 `[0,0]`（默认） | 值介于 -pi 和 pi 之间的 1-by-2 向量

在 *Z*-down 坐标系中右前照灯光束方向的俯仰角和偏航角，指定为 1-by-2 向量，单位为 rad。
向量的第一个元素 `[1,1]` 是俯仰角。向量的第二个元素 `[1,2]` 是偏航角。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

#### 制动灯

### **Brake light intensity, BrakelightIntensity** — 强度 `500`（默认） | 正标量

制动灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

#### 转向信号灯

### **Turn signal light intensity, SignallightIntensity** — 强度 `500`（默认） | 正标量

转向信号灯强度，单位为 cd/m^2。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Period, SignallightPeriod** — 转向信号灯周期 `1`（默认） | 正标量

转向信号灯周期，单位为 s。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### **Pulse width, SignalPulseWidth** — 脉冲宽度 `50`（默认） | 小于 100 的正标量

转向信号灯脉冲宽度，以周期的百分比表示。

#### 依赖关系

要启用此参数，请选择 **Enable light controls**。

**数据类型：** `double`

### 初始值

### **Initial array values to translate vehicle per part, Translation** — 摩托车初始平移 zeros( 4, 3 )（默认） | `4`-by-`3` 数组

初始摩托车和部件平移，单位为 m。数组维度为
`5`-by-`3`。

- `Translation(1,1)`、`Translation(1,2)`
  和 `Translation(1,3)` — 初始车辆分别沿惯性车辆 Z-down
  坐标系 *X*、*Y* 和 *Z* 轴的平移。
- `Translation(...,1)`、
  `Translation(...,2)` 和 `Translation(...,3)`
  — 初始摩托车部件相对于车辆的平移，分别沿车辆 Z-down
  *X*、*Y* 和 *Z* 轴。

该参数包含与位置对应的平移信息。

Translation=[XvYvZvXHYHZHXFYFZFXRYRZR]

| Translation | 数组元素 | 平移轴 |
| --- | --- | --- |
| 摩托车，*Xv* | `Translation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 摩托车，*Yv* | `Translation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 摩托车，*Zv* | `Translation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 车把，*XH* | `Translation(2,1)` | 车辆 Z-down *X* 轴 |
| 车把，*YH* | `Translation(2,2)` | 车辆 Z-down *Y* 轴 |
| 车把，*ZH* | `Translation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前轮，*XF* | `Translation(3,1)` | 车辆 Z-down *X* 轴 |
| 前轮，*YF* | `Translation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前轮，*ZF* | `Translation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后轮，*XR* | `Translation(4,1)` | 车辆 Z-down *X* 轴 |
| 后轮，*YR* | `Translation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后轮，*ZR* | `Translation(4,3)` | 车辆 Z-down *Z* 轴 |

### **Initial array values to rotate vehicle per part, Rotation** — 摩托车初始旋转 zeros( 4, 3 )（默认） | `4`-by-`3` 数组

初始摩托车和部件绕车辆 Z-down
*X*、*Y* 和 *Z* 轴的旋转。

数组维度为 `5`-by-`3`。

- `Rotation(1,1)`、`Rotation(1,2)` 和
  `Rotation(1,3)` — 初始摩托车分别绕
  惯性车辆 Z-down 坐标系 *X*、*Y* 和 *Z* 轴的旋转。
- `Rotation(...,1)`、`Rotation(...,2)` 和
  `Rotation(...,3)` — 初始摩托车部件
  相对于车辆绕车辆 Z-down *X*、*Y* 和 *Z* 轴的旋转。

该参数包含与位置对应的旋转信息。

Rotation=[RollvPitchvYawvRollHPitchHYawHRollFPitchFYawFRollRPitchRYawR]

| Rotation | 数组元素 | 旋转轴 |
| --- | --- | --- |
| 车辆，*Rollv* | `Rotation(1,1)` | 惯性车辆 Z-down *X* 轴 |
| 车辆，*Pitchv* | `Rotation(1,2)` | 惯性车辆 Z-down *Y* 轴 |
| 车辆，*Yawv* | `Rotation(1,3)` | 惯性车辆 Z-down *Z* 轴 |
| 车把，*RollH* | `Rotation(2,1)` | 车辆 Z-down *X* 轴 |
| 车把，*PitchH* | `Rotation(2,2)` | 车辆 Z-down *Y* 轴 |
| 车把，*YawH* | `Rotation(2,3)` | 车辆 Z-down *Z* 轴 |
| 前轮，*RollF* | `Rotation(3,1)` | 车辆 Z-down *X* 轴 |
| 前轮，*PitchF* | `Rotation(3,2)` | 车辆 Z-down *Y* 轴 |
| 前轮，*YawF* | `Rotation(3,3)` | 车辆 Z-down *Z* 轴 |
| 后轮，*RollR* | `Rotation(4,1)` | 车辆 Z-down *X* 轴 |
| 后轮，*PitchR* | `Rotation(4,2)` | 车辆 Z-down *Y* 轴 |
| 后轮，*YawR* | `Rotation(4,3)` | 车辆 Z-down *Z* 轴 |

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024b：新的 Simulation 3D Motorcycle 模块颜色选项

从 R2024b 开始，您可以为 Simulation 3D Motorcycle 模块将 **Color, VehColor** 指定为
`Dazzle Camouflage`。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Motorcycle 模块对模型进行仿真需要
Simulink
3D Animation。

## 描述

在 3D 环境中实现摩托车

**注意**

使用 Simulation 3D Motorcycle 模块对模型进行仿真需要
Simulink®
3D Animation™。

Simulation 3D Motorcycle 模块在 3D 仿真环境中实现一辆具有两个车轮的摩托车。

要使用此模块，请确保模型中包含 Simulation 3D Scene Configuration 模块。
如果将此模块的 **Sample time** 参数设置为
`-1`，则该模块使用 Simulation 3D
Scene Configuration 模块中指定的采样时间。

该模块输入使用 SAE
J6701 中定义的车辆 Z-down *右手* (RH)
*笛卡尔* 坐标系。该坐标系是惯性的，并且初始与车辆几何中心对齐：

- *X* 轴 — 沿车辆纵轴，指向前方
- *Y* 轴 — 沿车辆横轴，指向右侧
- *Z* 轴 — 指向下方

**提示**

验证 Simulation 3D Motorcycle
模块在 Simulation 3D Scene Configuration 模块之前执行。这样，
Simulation 3D Motorcycle 会在 Unreal Engine® 3D 可视化环境接收信号数据之前准备信号数据。要检查模块执行顺序，
请右键单击每个模块并选择 **Properties**。在
**General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Motorcycle — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。
