---
type: simulink-block
title: 'Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'referencegenerator'
documentation_source_path: 'ref/referencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Reference Generator

## 端口

### 输入

### **VehFdbk** — 车辆反馈 `Bus`

包含车辆反馈信号的总线，包括速度、加速度和方向盘扭矩。
### 输出

### **Vis** — 可视化参考信号 `Bus`

包含可视化参考信号的总线，包括纵向和横向位移以及转向。

### **Ref** — 车辆参考信号 `Bus`

包含车辆参考信号的总线，包括纵向和横向位移以及转向。

### **Fdbk** — 车辆位置反馈信号 `Bus`

包含车辆位置反馈信号的总线，包括位置。

## 参数

#### 配置

### **Maneuver** — 选择机动 `Constant Radius`（默认） | `Double Lane Change` | `Increasing Steer` | `Swept Sine` | `Sine with Dwell`

指定场景类型。

### **Maneuver start time** — 开始时间 `scalar`

机动开始时间，以 s 为单位。

### **Longitudinal velocity reference** — 目标速度 `scalar`

目标速度。

### **Longitudinal entrance velocity setpoint units** — 单位 `mph`（默认）

目标速度的单位。

### **Simulation time** — 仿真时间 `scalar`

时间，以 s 为单位。

#### Constant Radius

### **Radius value** — 半径 `scalar`

半径值，以 m 为单位。

### **Turn direction** — 转向方向 `Right`（默认） | `Left`

转向方向。

### **Lateral acceleration threshold** — 横向加速度 `scalar`

横向加速度阈值，以 g 为单位。

### **Stop simulation at lateral acceleration threshold** — 选择 `off`（默认） | `on`

如果车辆超过横向加速度阈值，则停止仿真。

#### Double Lane Change

### **Inertial longitudinal position of gate entrance** — 位置 `scalar`

门入口的惯性纵向位置，以 m 为单位。

### **Distance after target speed to begin reference** — 起始距离 `scalar`

达到目标速度后开始参考的距离，以 m 为单位。

### **Vehicle width** — 车辆宽度 `scalar`

车辆宽度，以 m 为单位。

左侧和右侧车道边界是 **Vehicle width** 参数的函数。

### **Lateral offset** — 横向偏移 `scalar`

横向偏移，以 m 为单位。

### **Lateral reference position breakpoints** — 断点 `scalar`

横向参考位置断点，以 m 为单位。

使用 **Lateral reference position breakpoints** 和 **Lateral reference data** 参数，将横向参考轨迹指定为纵向距离的函数。

### **Lateral reference data** — 横向数据 `scalar`

使用 **Lateral reference position breakpoints** 和 **Lateral reference data** 参数，将横向参考轨迹指定为纵向距离的函数。

#### Increasing Steer

### **Handwheel rate** — 方向盘速率 `scalar`

方向盘速率，以 deg/s 为单位。

### **Maximum handwheel angle** — 最大方向盘 `scalar`

最大方向盘转角，以 deg 为单位。

### **Steering hold time after max angle reached** — 转向保持 `scalar`

转向保持，以 s 为单位。

### **Lateral acceleration threshold** — 横向加速度 `scalar`

横向加速度阈值，以 g 为单位。

### **Stop simulation at lateral acceleration threshold** — 选择 `off`（默认） | `on`

如果车辆超过横向加速度阈值，则停止仿真。

#### Swept Sine

### **Swept time** — 扫频时间 `scalar`

扫频时间，以 s 为单位。

### **Steering amplitude** — 转向幅值 `scalar`

正弦转向幅值，以 deg 为单位。

### **Final frequency** — 最终频率 `scalar`

停止机动的截止频率，以 Hz 为单位。

#### Fishhook

### **Steer and countersteer speed, steerRate** — 转向和反向转向速度 `scalar`

转向和反向转向速度，以 deg/s 为单位。

### **Steer amplitude, steerAFH** — 转向幅值 `scalar`

转向幅值，以 deg 为单位。

### **Initial dwell time, tDwell1** — 初始驻留时间 `scalar`

初始驻留时间，以 s 为单位。

### **Countersteer dwell time, tDwell2** — 反向转向驻留时间 `scalar`

反向转向驻留时间，以 s 为单位。

### **Return to center time, tSteer3** — 回正时间 `scalar`

回正时间，以 s 为单位。

### **Roll rate countersteer initiation zero crossing threshold, pZero** — 过零阈值 `scalar`

侧倾角速度反向转向起始过零阈值，以 deg 为单位。

#### 3D Engine

### **3D Engine** — 启用 3D 可视化 `off`（默认） | `on`

启用 3D 可视化。

### **Scene** — 3D 场景 `Straight road` | `Curved road` | `Parking lot` | `Double lane change` | `Open surface` | `US city block` | `US highway` | `Virtual Mcity` | `Large parking lot`

指定 3D 场景的名称。

### **Engine frame rate, dt3D** — 图形 `.03`（默认）

图形帧率，以 s 为单位。图形帧率是采样时间的倒数。

### **Recommended for scene** — 初始车辆位置 `on`（默认） | `off`

使用针对场景推荐的车辆位置。

### **User-specified** — 初始车辆位置 `off`（默认） | `on`

指定以设置您自己的初始车辆位置值。

### **Initial longitudinal position, X\_o** — 初始纵向位置 `off`（默认） | `on`

沿地球固定 *X* 轴方向的车辆 CG 初始位置，以 m 为单位。

### **Initial lateral position, Y\_o** — 初始横向位置 `off`（默认） | `on`

沿地球固定 *Y* 轴方向的车辆 CG 初始位置，以 m 为单位。

### **Initial vertical position, Z\_o** — 初始垂直位置 `off`（默认） | `on`

沿地球固定 *Z* 轴方向的车辆 CG 初始位置，以 m 为单位。

### **Initial roll angle, phi\_o** — 侧倾 `off`（默认） | `on`

车辆固定坐标系绕地球固定 *X* 轴的旋转（侧倾），以 rad 为单位。

### **Initial pitch angle, theta\_o** — 俯仰 `off`（默认） | `on`

车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰），以 rad 为单位。

### **Initial yaw angle, psi\_o** — 横摆 `off`（默认） | `on`

车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆），以 rad 为单位。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

生成机动参考信号

Reference Generator 模块设置用于配置机动和 3D 仿真环境的参数。默认情况下，该模块设置为 Constant Radius 机动，且 3D 仿真引擎环境禁用。

### 模型

使用 **Maneuver** 参数指定机动类型。选择机动后，使用这些参数指定机动设置。默认情况下：

- **Use maneuver-specific driver, initial position, and scene** — 设置为 `on`
- **Maneuver start time** — 设置为 3s
- **Longitudinal velocity reference** — 设置为 30s
- **Longitudinal entrance velocity setpoint units** — 设置为 mph

| **Maneuver** 设置 | 实现 |
| --- | --- |
| `Double Lane Change` | 双车道变换机动    - **Vehicle width** — 用于 Visualization 子系统的车道信号；用于左侧和右侧车道边界 - **Lateral reference data** — 作为纵向距离函数的横向参考轨迹 - **Distance after target speed to begin reference** — 在车辆达到目标速度后，以指定距离开始机动 |
| `Increasing Steer` | 缓慢增加转向机动    - **Handwheel rate** — 增加方向盘转角的线性速率 - **Maximum handwheel angle** — 最大方向盘转角 |
| `Swept Sine` | 扫频正弦转向机动    - **Steering amplitude** — 正弦波幅值 - **Final frequency** — 停止机动的截止频率 |
| `Sine with Dwell` | 在测试中，车辆：  - 加速直到达到目标速度。 - 保持目标速度。 - 响应带驻留的正弦转向命令。      - **Steer frequency** — 正弦波频率 - **Steer amplitude** — 正弦波幅值 - **Dwell time** — 驻留时间 |
| `Constant Radius` | 恒定半径机动    - **Radius value** — 转弯半径 |
| `Fishhook` | 在测试中，车辆：  - 加速直到达到目标速度。 - 保持目标速度。 - 响应初始快速转向输入。 - 响应转向过度修正。      - **Steer and countersteer speed** — 转向速率 - **Initial dwell time** — 初始转向时间 - **Countersteer dwell time** — 反向转向时间 |

### 3D Engine

3D 引擎实现 3D 仿真环境。Vehicle Dynamics Blockset™ 将 3D 仿真环境与 Simulink® 集成，以便您可以查询车辆周围的世界，用于虚拟测试感知、控制和规划算法。有关 3D 引擎要求，请参阅 Unreal Engine Simulation Environment Requirements and Limitations。要启用 3D 引擎，请在 **3D Engine** 选项卡上，选择 **Enabled**。

要将车辆定位在场景中：

1. 选择位置初始化方法：

   - **Recommended for scene** — 将初始车辆位置设置为针对场景推荐的值
   - **User-specified** — 设置您自己的初始车辆位置
2. 点击 **Update the model workspaces with the initial values**，以使用应用的值覆盖模型工作区中的初始车辆位置。
