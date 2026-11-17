---
type: simulink-block
title: 'Simulation 3D Robot'
family: 'simulation-3d'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3drobot'
documentation_source_path: 'ref/simulation3drobot.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Robot

## 端口

### 输入

### **Config** — 机器人输入关节配置向量

机器人输入关节配置，指定为 *N* 元素向量。*N* 是刚体树中机器人关节配置的可动关节数，由 **Rigid body tree** 参数指定。

#### 依赖关系

要启用此端口，请选择 **Enable config input signal** 或 **Enable grasp settings input signals** 参数。

### **Translation** — 机器人基座平移向量

机器人基座平移，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移。单位为 meters。

#### 依赖关系

要启用此端口，请选择 **Enable translation and rotation input signals** 参数。

### **Rotation** — 机器人基座旋转向量

机器人基座旋转，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 *z*、*y* 和 *x* 轴的旋转。单位为 radians。

#### 依赖关系

要启用此端口，请选择 **Enable translation and rotation input signals** 参数。

### **TargetActor** — 要抓取的目标 actor 名称 fixed-sized string scalar | variable-sized uint8 array

要抓取的目标 actor 名称，指定为 fixed-sized string scalar 或 variable-sized uint8 array。

#### 依赖关系

要启用此端口，请选择 **Enable grasp settings input signals** 参数。

### **ActivateTargetGrasp** — 抓取目标 actor 布尔值

抓取目标 actor，指定为 boolean `1` (`true`) 以抓取目标 actor，或 boolean `0` (`false`) 以释放目标 actor。

#### 依赖关系

要启用此端口，请选择 **Enable grasp settings input signals** 参数。

### **GraspRegionTranslation** — 自动抓取目标 actor 所需的平移距离向量

在末端执行器自动抓取目标 actor 之前，末端执行器与目标 actor 之间允许的最大平移距离，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是末端执行器与目标 actor 之间沿 *x*、*y* 和 *z* 轴的平移差。单位为 meters。

#### 依赖关系

要启用此端口，请选择 **Enable target actor grasp region as an input signal** 参数。

### **GraspRegionRotation** — 自动抓取目标 actor 所需的旋转距离向量

在末端执行器自动抓取目标 actor 之前，末端执行器与目标 actor 之间允许的最大旋转距离，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是末端执行器与目标 actor 之间绕 *z*、*y* 和 *x* 轴的旋转差。单位为 radians。

#### 依赖关系

要启用此端口，请选择 **Enable target actor grasp region as an input signal** 参数。

### **TargetEETranslation** — 末端执行器与目标 actor 之间的平移差向量

末端执行器与目标 actor 之间的平移差，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是末端执行器与目标 actor 之间沿 *x*、*y* 和 *z* 轴的平移差。单位为 meters。

#### 依赖关系

要启用此端口，请选择 **End effector to target actor offset as an input signal** 参数。

### **TargetEERotation** — 末端执行器与目标 actor 之间的旋转差向量

末端执行器与目标 actor 之间的旋转差，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是末端执行器与目标 actor 之间绕 *z*、*y* 和 *x* 轴的旋转差。单位为 radians。

#### 依赖关系

要启用此端口，请选择 **End effector to target actor offset as an input signal** 参数。

### 输出

### **GroundTruthConfiguration** — 机器人配置的真值向量

机器人配置的真值，输出为 *N* 元素向量。*N* 是刚体树中机器人关节配置的可动关节数，由 **Rigid body tree** 参数指定。

#### 依赖关系

要启用此端口，请选择 **Enable ground truth config output signal** 参数。

### **IsTargetGrasped** — 目标 actor 已抓取状态布尔值

目标 actor 已抓取状态，如果末端执行器正在抓取目标 actor，则输出为 boolean `1` (`true`)；如果末端执行器未抓取目标 actor，则输出为 boolean `0` (`false`)。

#### 依赖关系

要启用此端口，请选择 **Enable target grasped status output signal** 参数。

### **GroundTruthTranslation** — 机器人输入关节配置向量

机器人基座的真值平移，输出为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移。单位为 meters。

#### 依赖关系

要启用此端口，请选择 **Enable ground truth translation and rotation output signal** 参数。

### **GroundTruthRotation** — 机器人输入关节配置向量

机器人基座的真值旋转，输出为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 *z*、*y* 和 *x* 轴的旋转。单位为 radians。

#### 依赖关系

要启用此端口，请选择 **Enable ground truth translation and rotation output signal** 参数。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。从 Simulink Toolstrip 中，在 **Simulation** 选项卡的 **Prepare** 库中，选择 Property Inspector。

### 参数

### **Input type** — 机器人模型源 `RigidBodyTree Object` (默认) | `Robot Library`

机器人模型源，指定为 `RigidBodyTree Object` 或 `Robot Library`：

- `RigidBodyTree Object` — 从 MATLAB® 工作区指定一个 `rigidBodyTree` object。
- `Robot Library` — 从 Robotics System Toolbox™ Robot Library Data 中选择机器人刚体树模型。有关详细信息，请参阅 Robotics System Toolbox Robot Library Data。

### **Rigid body tree** — 机器人刚体树模型 `twoJointRigidBodyTree` (默认) | `rigidBodyTree` object | Robot Library 中的机器人名称

机器人刚体树模型，根据 **Input type** 参数的值，指定为 `rigidBodyTree` object 或 Robotics System Toolbox Robot Library Data 中刚体树模型的名称：

- `RigidBodyTree Object` — 从 MATLAB 工作区指定一个 `rigidBodyTree` object。
- `Robot Library` — 从 Robotics System Toolbox Robot Library Data 中选择机器人刚体树模型。有关详细信息，请参阅 Robotics System Toolbox Robot Library Data。

### **Actor name** — 在 Unreal Engine 场景中表示机器人的 actor 名称 `SimulinkRobot1` (默认) | string scalar

在 Unreal Engine 场景中表示机器人的 actor 名称，指定为 string scalar。

### **Use existing Simulink 3D actor specified in the actor name prompt** — 使用 Unreal Engine 场景中的现有 actor 表示机器人 `off` (默认) | `on`

选择此参数可使用 Unreal Engine 场景中的现有 actor 来表示机器人。当您选择此参数时，Simulation 3D Robot 使用场景中由 **Actor name** 参数指定的名称的 actor。如果清除此参数，Simulation 3D Robot 将在场景中创建一个具有指定 actor 名称的新 actor 来表示机器人。

### **Sample time** — 采样时间 `-1` (默认) | 正标量

模块的采样时间，以 seconds 为单位，指定为正标量。3D 仿真环境帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 初始值

### **Initial base translation** — 机器人基座的初始平移 `[0 0 0]` (默认)

机器人基座的初始平移，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移。单位为 meters。

### **Initial base rotation** — 机器人基座的初始旋转 `[0 0 0]` (默认)

机器人基座的初始旋转，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 *z*、*y* 和 *x* 轴的旋转。单位为 radians。

### **Initial joint configuration** — 初始关节配置 `[0 0]` (默认) | *N* 元素行向量

初始关节配置，指定为 *N* 元素向量。*N* 等于刚体树中可动关节的数量。

### 抓取设置

### **End effector** — 末端执行器刚体名称 `tool` (默认)

使用 **Select body** 按钮从机器人刚体树中的某个刚体选择末端执行器刚体名称。

#### 依赖关系

要启用此参数，请选择 **Enable grasp settings input signals** 参数。

### **End effector to target actor offset as an input signal** — `off` (默认) | `on`

选择此参数可在 **TargetEETranslation** 和 **TargetEERotation** 输入端口分别输入末端执行器与目标 actor 之间的平移和旋转差。

清除此参数可使用 **End effector to target translation** 和 **End effector to target actor rotation** 参数指定平移和旋转差。

#### 依赖关系

要启用此参数，请选择 **Enable grasp settings input signals** 参数。

### **End effector to target actor translation** — `[0 0 0]` (默认) |

要抓取的末端执行器与目标 actor 之间的平移差，指定为三元素行向量，形式为 [*x*, *y*, *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移。单位为 meters。

#### 依赖关系

要启用此参数，请选择 **Enable grasp settings input signals** 参数。

### **End effector to target actor rotation** — `[0 0 0]` (默认) |

要抓取的末端执行器与目标 actor 之间的旋转差，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 *z*、*y* 和 *x* 轴的旋转。单位为 radians。

#### 依赖关系

要启用此参数，请选择 **Enable grasp settings input signals** 参数。

### **Enable region-based target actor grasp approach** — 当目标 actor 位于末端执行器的指定边界内时自动抓取目标 actor `off` (默认) | `on`

选择此参数可在目标 actor 位于末端执行器的指定区域内时，使用末端执行器自动抓取目标 actor。

#### 依赖关系

要启用此参数，请选择 **Enable grasp settings input signals** 参数。

### **Enable target actor grasp region as an input signal** — 在输入端口指定用于抓取目标 actor 的区域 `off` (默认) | `on`

选择此参数可在 **GraspRegionTranslation** 和 **GraspRegionRotation** 输入端口启用抓取区域的输入。

清除此参数可使用 **End effector to target actor grasp region translation difference** 和 **End effector to target actor grasp region rotation difference** 参数指定抓取区域。

#### 依赖关系

要启用此参数，请选择 **Enable region-based target actor grasp approach** 参数。

### **End effector to target actor grasp region translation difference** — 抓取区域的平移差 `[0.2 0.2 0.2]` (默认)

抓取区域的平移差，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移。单位为 meters。

#### 依赖关系

要启用此参数，请选择 **Enable region-based target actor grasp approach** 参数。

### **End effector to target actor grasp region rotation difference** — 抓取区域的旋转差 `[0 0 0]` (默认)

抓取区域的旋转差，指定为三元素行向量，形式为 [*yaw*, *pitch* , *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 z、y 和 x 轴的旋转。单位为 radians。

#### 依赖关系

要启用此参数，请选择 **Enable region-based target actor grasp approach** 参数。

### rigidBodyTree 几何设置

设置此选项卡中的参数，以在 3D 可视化环境中启用刚体树几何的可视化。

#### 可视几何可视化

### **Enable visual geometry visualization in 3D scene** — 在 3D 可视化环境中添加刚体树可视几何 `on` (默认) | `off`

选择此参数可在 3D 可视化环境中添加刚体树可视几何。

#### 碰撞几何可视化

### **Enable collision geometry visualization in 3D scene** — 在 3D 可视化环境中可视化刚体树碰撞几何 `off` (默认) | `on`

选择此参数可在 3D 可视化环境中可视化刚体树碰撞几何。

### **Collision geometry color** — 刚体树碰撞几何的颜色 `[0 1 0]` (默认) | 向量

在 3D 可视化环境中可视化的刚体树碰撞几何的颜色，指定为三元素行向量。

### **Collision geometry transparency** — 刚体树碰撞几何的透明度 `0.1` (默认) | 标量

在 3D 可视化环境中可视化的刚体树碰撞几何的透明度，指定为标量。

### 输入

### **Enable config input signal** — 在输入端口指定所需的机器人配置 `on` (默认) | `off`

选择此参数可在 **Config** 输入端口指定所需的机器人配置。

#### 依赖关系

要启用此参数，请清除 **Enable grasp settings input signals** 参数。

### **Enable grasp settings input signals** — `off` (默认) | `on`

选择此参数可启用 **Grasp Settings** 选项卡以控制机器人如何抓取目标 actor，以及 **TargetActor** 和 **ActivateTargetGrasp** 输入端口。

### **Enable translation and rotation input signals** — 在输入端口指定机器人基座的平移和旋转 `off` (默认) | `on`

选择此参数可在 **Translation** 和 **Rotation** 端口分别指定机器人基座的平移和旋转。对于移动机器人和移动机械臂机器人的刚体树模型，启用此端口。

### 输出

### **Enable ground truth config output signal** — 输出真值配置 `off` (默认) | `on`

选择此参数可在 **GroundTruthConfig** 输出端口输出真值配置。

### **Enable target grasped status output signal** — 输出抓取状态 `off` (默认) | `on`

选择此参数可在 **IsTargetGrasped** 输出端口输出末端执行器的抓取状态。

### **Enable ground truth translation and rotation output signal** — 输出机器人基座的真值位姿 `off` (默认) | `on`

选择此参数可在 **GroundTruthTranslation** 和 **GroundTruthRotation** 输出端口输出机器人基座的真值位姿。

## 所属库

Robotics System Toolbox / Simulation 3D

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

在 3D 环境中实现机器人

**注意**

使用 Simulation 3D Robot 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Robot 使用 Unreal Engine® 在 3D 仿真环境中实现机器人。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Robot 模块的 **Sample time** 参数设置为 `-1`，则该模块继承 Simulation 3D Scene Configuration 模块中指定的采样时间。
