---
type: simulink-block
title: 'Pure Pursuit'
family: 'mobile-robot-algorithms'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Mobile Robot Algorithms'
documentation_page: 'purepursuit'
documentation_source_path: 'ref/purepursuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Pure Pursuit

## 端口

### 输入

### **Pose** — 当前车辆位姿 `[x y theta]` 向量

当前车辆位姿，指定为 `[x y theta]` 向量，对应于 *x-y* 位置和方向角 *theta*。正角度从正 *x* 轴逆时针测量。

### **Waypoints** — 路点 [ ]（默认）| *n*-by-2 数组

路点，指定为 `[x y]` 对的 *n*-by-2 数组，其中 *n* 是路点数量。您可以使用路径规划器（如 `mobileRobotPRM`）生成路点，或在 Simulink® 中将它们指定为数组。

### **Desired Linear Velocity** — 线速度标量，单位为 meters per second

期望线速度，指定为以 meters per second 为单位的标量。控制器假设车辆以恒定线速度行驶，并且计算得到的角速度与线速度无关。

#### 依赖关系

要启用此端口，请选择 **Specify desired linear velocity from input port** 参数。

### **Lookahead Distance** — 前视距离标量，单位为 meters per second

前视距离，指定为以 meters per second 为单位的标量。前视距离会改变控制器的响应。具有较大前视距离的车辆会生成平滑路径，但在转角处会进行更大的转向。具有较小前视距离的车辆会紧密跟随路径并进行急转弯，但会沿路径振荡。有关前视距离影响的详细信息，请参阅 Pure Pursuit Controller。

#### 依赖关系

要启用此端口，请选择 **Specify lookahead distance from input port** 参数。

### 输出

### **Linear Velocity** — 线速度标量，单位为 meters per second

线速度，以 meters per second 为单位的标量形式返回。

**数据类型：** `double`

### **Angular Velocity** — 角速度标量，单位为 radians per second

角速度，以 radians per second 为单位的标量形式返回。

**数据类型：** `double`

### **Target Direction** — 车辆目标方向标量，单位为 radians

车辆的目标方向，以 radians 为单位的标量形式返回。车辆的前进方向视为 zero radians，正角度按逆时针测量。此输出可用作 Vector Field Histogram (Navigation Toolbox) 模块的 **TargetDir** 端口的输入。

#### 依赖关系

要启用此端口，请选择 **Show Target Direction output port** 参数。

## 参数

### **Specify desired linear velocity from input port** — 启用期望线速度的输入端口 `off`（默认）| `on`

选择此参数可启用在 **Desired Linear Velocity** 输入端口输入期望线速度。

清除此参数可使用 **Desired linear velocity (m/s)** 参数指定期望线速度

### **Desired linear velocity (m/s)** — 线速度 `0.1`（默认）| 标量

期望线速度，指定为以 meters per second 为单位的标量。控制器假设车辆以恒定线速度行驶，并且计算得到的角速度与线速度无关。

#### 依赖关系

要启用此参数，请清除 **Specify desired linear velocity from input port** 参数。

### **Maximum angular velocity (rad/s)** — 角速度 `1.0`（默认）| 标量

最大角速度，指定为以 radians per second 为单位的标量。控制器将绝对角速度输出饱和在该给定值。

### **Specify lookahead distance from input port** — 启用前视距离的输入端口 `off`（默认）| `on`

选择此参数可启用在 **Lookahead Distance** 输入端口输入前视距离。

清除此参数可使用 **Lookahead distance (m)** 参数指定前视距离

### **Lookahead distance (m)** — 前视距离 `1.0`（默认）| 标量

前视距离，指定为以 meters 为单位的标量。前视距离会改变控制器的响应。具有较大前视距离的车辆会生成平滑路径，但在转角处会进行更大的转向。具有较小前视距离的车辆会紧密跟随路径并进行急转弯，但会沿路径振荡。有关前视距离影响的详细信息，请参阅 Pure Pursuit Controller。

#### 依赖关系

要启用此参数，请清除 **Specify lookahead distance from input port** 参数。

### **Show Target Direction output port** — 目标方向指示 `off`（默认）| `on`

选择此参数可启用 **Target Direction** 输出端口。此端口给出从前进位置算起的目标方向，以 radians 为单位的角度表示，正角度按逆时针测量。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度可与 `Interpreted execution` 相当。

**可调：** No

## 所属库

Robotics System Toolbox / Mobile Robot Algorithms Navigation Toolbox / Control Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a：在输入端口指定线速度和前视距离，并重命名输出端口

Pure Pursuit 模块有两组更改：

1. 现在，您可以通过选择 **Specify desired linear velocity from input port** 参数，在 **Desired Linear Velocity** 输入端口指定期望线速度。
2. 现在，您可以通过选择 **Specify lookahead distance from input port** 参数，在 **Lookahead Distance** 输入端口指定前视距离。
3. 输出端口和一个参数有了新名称。此表显示了 R2024a 之前的名称，以及 R2024a 及之后的名称。

   | R2024a 之前的名称 | R2024a 及之后的名称 |
   | --- | --- |
   | **LinVel** 输出端口 | **Linear Velocity** 输出端口 |
   | **AngVel** 输出端口 | **Angular Velocity** 输出端口 |
   | **TargetDir** 输出端口 | **Target Direction** 输出端口 |
   | **Show TargetDir output port** 参数 | **Show Target Direction output port** 参数 |

## 描述

线速度和角速度控制命令

Pure Pursuit 模块使用一组路点和类汽车或差速驱动车辆的当前位姿，计算用于跟随路径的线速度和角速度命令。该模块接收更新后的位姿，以更新速度命令，使车辆沿期望的一组路点跟随路径。使用 **Max angular velocity** 和 **Desired linear velocity** 参数，根据车辆性能更新速度。

前视距离端口和参数计算路径上的前视点，该点是车辆的瞬时局部目标。角速度命令基于该点计算。更改前视距离会对算法性能产生显著影响。较高的前视距离可使车辆轨迹更平滑，但可能导致车辆在路径转角处切角。前视距离过低可能导致路径跟踪振荡，从而引起不稳定行为。有关 pure pursuit 算法的详细信息，请参阅 Pure Pursuit Controller。
