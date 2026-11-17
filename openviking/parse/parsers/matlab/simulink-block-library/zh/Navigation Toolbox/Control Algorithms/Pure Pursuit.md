---
type: simulink-block
title: 'Pure Pursuit'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Control Algorithms'
documentation_page: 'purepursuit'
documentation_source_path: 'ref/purepursuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Pure Pursuit

## 端口
```yaml
ports:
- name: Pose
  summary: 当前车辆位姿 [x y theta] 向量
  direction: input
- name: Waypoints
  summary: 航点 [ ]（默认）| *n*×2 数组
  direction: input
- name: Desired Linear Velocity
  summary: 线速度，单位为米每秒的标量
  direction: input
- name: Lookahead Distance
  summary: 前视距离，单位为米每秒的标量
  direction: input
- name: Linear Velocity
  summary: 线速度，单位为米每秒的标量
  direction: output
  data_types: double
- name: Angular Velocity
  summary: 角速度，单位为弧度每秒的标量
  direction: output
  data_types: double
- name: Target Direction
  summary: 车辆的目标方向，单位为弧度的标量
  direction: output
```

### 输入

### **Pose** — 当前车辆位姿 `[x y theta]` 向量

当前车辆位姿，指定为 `[x y theta]` 向量，对应于 *x-y* 位置和方向角 *theta*。正角度从正 *x* 轴逆时针测量。

### **Waypoints** — 航点 [ ]（默认）| *n*×2 数组

航点，指定为 `[x y]` 对的 *n*×2 数组，其中 *n* 是航点数量。您可以使用路径规划器（如 `mobileRobotPRM`（Robotics System Toolbox））生成航点，或在 Simulink® 中将其指定为数组。

### **Desired Linear Velocity** — 线速度，单位为米每秒的标量

期望线速度，指定为以米每秒为单位的标量。控制器假设车辆以恒定线速度行驶，且计算出的角速度与线速度无关。

#### 依赖

要启用此端口，请选择 **Specify desired linear velocity from input port** 参数。

### **Lookahead Distance** — 前视距离，单位为米每秒的标量

前视距离，指定为以米每秒为单位的标量。前视距离会改变控制器的响应。前视距离较大的车辆会生成平滑的路径，但在转弯处会进行较大的转向。前视距离较小的车辆会紧密跟随路径并进行急转弯，但会沿路径振荡。有关前视距离影响的更多信息，请参阅 Pure Pursuit Controller。

#### 依赖

要启用此端口，请选择 **Specify lookahead distance from input port** 参数。
### 输出

### **Linear Velocity** — 线速度，单位为米每秒的标量

线速度，以米每秒为单位的标量形式返回。

**数据类型：** `double`

### **Angular Velocity** — 角速度，单位为弧度每秒的标量

角速度，以弧度每秒为单位的标量形式返回。

**数据类型：** `double`

### **Target Direction** — 车辆的目标方向，单位为弧度的标量

车辆的目标方向，以弧度为单位的标量形式返回。车辆的前进方向被视为零弧度，正角度逆时针测量。此输出可用作 Vector Field Histogram 模块 **TargetDir** 端口的输入。

#### 依赖

要启用此端口，请选择 **Show Target Direction output port** 参数。
## 参数
```yaml
parameters:
- name: Specify desired linear velocity from input port
  summary: 启用期望线速度的输入端口 off（默认）| on
  group: ''
- name: Desired linear velocity (m/s)
  summary: 线速度 0.1（默认）| 标量
  group: ''
- name: Maximum angular velocity (rad/s)
  summary: 角速度 1.0（默认）| 标量
  group: ''
- name: Specify lookahead distance from input port
  summary: 启用前视距离的输入端口 off（默认）| on
  group: ''
- name: Lookahead distance (m)
  summary: 前视距离 1.0（默认）| 标量
  group: ''
- name: Show Target Direction output port
  summary: 目标方向指示 off（默认）| on
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

### **Specify desired linear velocity from input port** — 启用期望线速度的输入端口 `off`（默认）| `on`

选择此参数以启用 **Desired Linear Velocity** 输入端口处的期望线速度输入。

清除此参数以使用 **Desired linear velocity (m/s)** 参数指定期望线速度

### **Desired linear velocity (m/s)** — 线速度 `0.1`（默认）| 标量

期望线速度，指定为以米每秒为单位的标量。控制器假设车辆以恒定线速度行驶，且计算出的角速度与线速度无关。

#### 依赖

要启用此参数，请清除 **Specify desired linear velocity from input port** 参数。

### **Maximum angular velocity (rad/s)** — 角速度 `1.0`（默认）| 标量

最大角速度，指定为以弧度每秒为单位的标量。控制器将绝对角速度输出饱和在给定值。

### **Specify lookahead distance from input port** — 启用前视距离的输入端口 `off`（默认）| `on`

选择此参数以启用 **Lookahead Distance** 输入端口处的前视距离输入。

清除此参数以使用 **Lookahead distance (m)** 参数指定期望线速度

### **Lookahead distance (m)** — 前视距离 `1.0`（默认）| 标量

前视距离，指定为以米为单位的标量。前视距离会改变控制器的响应。前视距离较大的车辆会生成平滑的路径，但在转弯处会进行较大的转向。前视距离较小的车辆会紧密跟随路径并进行急转弯，但会沿路径振荡。有关前视距离影响的更多信息，请参阅 Pure Pursuit Controller。

#### 依赖关系

要启用此参数，请清除 **Specify lookahead distance from input port** 参数。

### **Show Target Direction output port** — 目标方向指示 `off`（默认）| `on`

选择此参数以启用 **Target Direction** 输出端口。此端口以弧度为单位给出目标方向，从前方位置起算，正角度按逆时针方向测量。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

**可调：** 否
## 所属库

Robotics System Toolbox / Mobile Robot Algorithms Navigation Toolbox / Control Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a：在输入端口指定线速度和前视距离，并重命名输出端口

Pure Pursuit 模块有两组更改：

1. 您现在可以通过选择 **Specify desired linear velocity from input port** 参数，在 **Desired Linear Velocity** 输入端口指定期望线速度。
2. 您现在可以通过选择 **Specify lookahead distance from input port** 参数，在 **Lookahead Distance** 输入端口指定期望线速度。
3. 输出端口和一个参数有了新名称。下表显示了 R2024a 之前的名称，以及 R2024a 及之后的名称。

   | R2024a 之前的名称 | R2024a 及之后的名称 |
   | --- | --- |
   | **LinVel** 输出端口 | **Linear Velocity** 输出端口 |
   | **AngVel** 输出端口 | **Angular Velocity** 输出端口 |
   | **TargetDir** 输出端口 | **Target Direction** 输出端口 |
   | **Show TargetDir output port** 参数 | **Show Target Direction output port** 参数 |

## 描述

线速度和角速度控制指令

Pure Pursuit 模块使用一组路点和类汽车或差速驱动车辆的当前位姿，计算用于跟随路径的线速度和角速度指令。该模块接收更新后的位姿，以更新车辆沿期望路点集合跟随路径的速度指令。使用 **Max angular velocity** 和 **Desired linear velocity** 参数，根据车辆的性能更新速度。

前视距离端口和参数计算路径上的前视点，该点是车辆的瞬时局部目标。角速度指令基于该点计算。改变前视距离对算法性能有显著影响。较高的前视距离会使车辆的轨迹更平滑，但可能导致车辆在路径上切角。前视距离过低可能导致路径跟踪出现振荡，从而引起不稳定行为。有关纯追踪算法的更多信息，请参阅 Pure Pursuit Controller。
