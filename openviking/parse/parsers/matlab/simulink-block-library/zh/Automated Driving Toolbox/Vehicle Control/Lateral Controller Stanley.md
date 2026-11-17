---
type: simulink-block
title: 'Lateral Controller Stanley'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Vehicle Control'
documentation_page: 'lateralcontrollerstanley'
documentation_source_path: 'ref/lateralcontrollerstanley.html'
language: zh-CN
chinese_source: worker-translation
---

# Lateral Controller Stanley

## 端口
```yaml
ports:
- name: RefPose
  summary: 参考位姿 [*x*, *y*, *Θ*] 向量
  direction: input
  data_types: single | double
- name: CurrPose
  summary: 当前位姿 [*x*, *y*, *Θ*] 向量
  direction: input
  data_types: single | double
- name: CurrVelocity
  summary: 当前纵向速度 实数标量
  direction: input
  data_types: single | double
- name: Direction
  summary: 车辆行驶方向 1（前向运动） | -1（倒车运动）
  direction: input
- name: Curvature
  summary: 路径曲率 实数标量
  direction: input
- name: CurrYawRate
  summary: 当前横摆角速度 实数标量
  direction: input
- name: CurrSteer
  summary: 当前转向角 实数标量
  direction: input
- name: SteerCmd
  summary: 转向角命令 实数标量
  direction: output
```

### 输入

### **RefPose** — 参考位姿 [*x*, *y*, *Θ*] 向量

参考位姿，指定为 [*x*, *y*, *Θ*] 向量。*x* 和 *y* 的单位为米，*Θ* 的单位为度。

*x* 和 *y* 指定用于将车辆转向的参考点。*Θ* 指定该参考点处路径的朝向角，逆时针方向为正。

- 对于前向运动的车辆，参考点是路径上距离车辆前轴中心最近的点。

  前向运动的车辆，路径上的参考点已标记。单位采用世界坐标系。
- 对于倒车运动的车辆，参考点是路径上距离车辆后轴中心最近的点。

  倒车运动的车辆，路径上的参考点已标记。单位采用世界坐标系。

**数据类型：** `single` | `double`

### **CurrPose** — 当前位姿 [*x*, *y*, *Θ*] 向量

车辆的当前位姿，指定为 [*x*, *y*, *Θ*] 向量。*x* 和 *y* 的单位为米，*Θ* 的单位为度。

*x* 和 *y* 指定车辆的位置，定义为车辆后轴的中心。

*Θ* 指定车辆在位置 (*x*,*y*) 处的朝向角，逆时针方向为正。

车辆位姿已标记。单位采用世界坐标系。

有关车辆位姿的更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems。

**数据类型：** `single` | `double`

### **CurrVelocity** — 当前纵向速度 实数标量

车辆的当前纵向速度，指定为实数标量。单位为米每秒。

- 如果车辆处于前向运动，则该值必须大于 0。
- 如果车辆处于倒车运动，则该值必须小于 0。
- 值为 0 表示车辆未处于运动状态。

**数据类型：** `single` | `double`

### **Direction** — 车辆行驶方向 `1`（前向运动） | `-1`（倒车运动）

车辆的行驶方向，指定为 `1` 表示前向运动，或 `-1` 表示倒车运动。行驶方向决定用于计算转向角命令的位置误差和角度误差。有关更多详细信息，请参阅算法。

### **Curvature** — 路径曲率 实数标量

参考点处路径的曲率，单位为弧度每米，指定为实数标量。

- 对于前向运动的车辆，参考点是路径上距离车辆前轴中心最近的点。

  前向运动的车辆，路径上的参考点已标记。单位采用世界坐标系。
- 对于倒车运动的车辆，参考点是路径上距离车辆后轴中心最近的点。

  倒车运动的车辆，路径上的参考点已标记。单位采用世界坐标系。

您可以从 Path Smoother Spline 模块的 **Curvatures** 输出端口获取路径的曲率。您还可以从 Scenario Reader 模块的输出车道边界结构体中获取车道边界的曲率。

#### 依赖关系

要启用此端口，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **CurrYawRate** — 当前横摆角速度 实数标量

车辆的当前横摆角速度，单位为度每秒，指定为实数标量。当前横摆角速度是车辆角速度的变化率。

#### 依赖关系

要启用此端口，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **CurrSteer** — 当前转向角 实数标量

车辆的当前转向角，单位为度，指定为实数标量。该值逆时针方向为正。

前轮转向的车辆，转向角已标记

有关更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems。

#### 依赖关系

要启用此端口，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。
### 输出

### **SteerCmd** — 转向角命令 实数标量

转向角命令，单位为度，以实数标量形式返回。该值逆时针方向为正。

前轮转向的车辆，转向角已标记

有关更多详细信息，请参阅 Automated Driving Toolbox 中的 Coordinate Systems。
## 参数
```yaml
parameters:
- name: Vehicle model
  summary: 车辆模型 Kinematic bicycle model（默认） | Dynamic bicycle model
  group: ''
- name: Position gain of forward motion
  summary: 前向运动时的车辆位置增益 2.5（默认） | 正实数标量
  group: ''
- name: Position gain of reverse motion
  summary: 倒车运动时的车辆位置增益 2.5（默认） | 正实数标量
  group: ''
- name: Yaw rate feedback gain
  summary: 横摆角速度反馈增益 2.5（默认） | 非负实数标量
  group: ''
- name: Steering angle feedback gain
  summary: 转向角反馈增益 2.5（默认） | 非负实数标量
  group: ''
- name: Wheelbase of vehicle (m)
  summary: 前后轴之间的距离 2.8（默认） | 实数标量
  group: ''
- name: Vehicle mass (kg)
  summary: 车辆质量 1575（默认） | 正实数标量
  group: ''
- name: Longitudinal distance from center of mass to front axle (m)
  summary: 到前轴的距离 1.2（默认） | 正实数标量
  group: ''
- name: Longitudinal distance from center of mass to rear axle (m)
  summary: 到后轴的距离 1.6（默认） | 正实数标量
  group: ''
- name: Front tire corner stiffness (N/rad)
  summary: 前轮胎侧偏刚度 19000（默认） | 正实数标量
  group: ''
- name: Maximum steering angle (deg)
  summary: 允许的最大转向角 35（默认） | 范围 (0, 180) 内的实数标量
  group: ''
```

### **Vehicle model** — 车辆模型 `Kinematic bicycle model`（默认） | `Dynamic bicycle model`

选择车辆模型的类型，以设置模块所使用的 Stanley 方法控制律。

- `Kinematic bicycle model` — 运动学自行车模型，适用于低速环境（如停车场）中的路径跟随，在这些环境中惯性效应最小
- `Dynamic bicycle model` — 动力学自行车模型，适用于高速环境（如高速公路）中的路径跟随，在这些环境中惯性效应更为显著

### **Position gain of forward motion** — 前向运动时的车辆位置增益 `2.5`（默认） | 正实数标量

车辆前向运动时的位置增益，指定为正标量。该值决定位置误差对转向角的影响程度。典型值范围为 [1, 5]。增大该值可增大转向角的幅值。

### **Position gain of reverse motion** — 倒车运动时的车辆位置增益 `2.5`（默认） | 正实数标量

车辆倒车运动时的位置增益，指定为正标量。该值决定位置误差对转向角的影响程度。典型值范围为 [1, 5]。增大该值可增大转向角的幅值。

### **Yaw rate feedback gain** — 横摆角速度反馈增益 `2.5`（默认） | 非负实数标量

横摆角速度反馈增益，指定为非负实数标量。该值决定模块在计算转向角命令时对车辆当前横摆角速度所赋予的权重。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Steering angle feedback gain** — 转向角反馈增益 `2.5`（默认） | 非负实数标量

转向角反馈增益，指定为非负实数标量。该值决定当前转向角命令 **SteerCmd** 与当前转向角 **CurrSteer** 之间的差值对下一个转向角命令的影响程度。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Wheelbase of vehicle (m)** — 前后轴之间的距离 `2.8`（默认） | 实数标量

车辆前轴与后轴之间的距离，单位为米，指定为实数标量。该值仅在车辆处于前向运动时适用，即当 **Direction** 输入端口为 `1` 时。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Kinematic bicycle model`。

### **Vehicle mass (kg)** — 车辆质量 `1575`（默认） | 正实数标量

车辆质量，单位为千克，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Longitudinal distance from center of mass to front axle (m)** — 到前轴的距离 `1.2`（默认） | 正实数标量

从车辆质心到前轮轴的纵向距离，单位为米，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Longitudinal distance from center of mass to rear axle (m)** — 到后轴的距离 `1.6`（默认） | 正实数标量

从车辆质心到后轮轴的纵向距离，单位为米，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Front tire corner stiffness (N/rad)** — 前轮胎侧偏刚度 `19000`（默认） | 正实数标量

前轮胎侧偏刚度，单位为牛顿每弧度，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Maximum steering angle (deg)** — 允许的最大转向角 `35`（默认） | 范围 (0, 180) 内的实数标量

车辆允许的最大转向角，单位为度，指定为范围 (0, 180) 内的实数标量。

**SteerCmd** 端口的输出被饱和限制在范围 [–*M*, *M*] 内，其中 *M* 是 **Maximum steering angle (deg)** 参数的值。

- 低于 –*M* 的值被设置为 –*M*。
- 高于 *M* 的值被设置为 *M*。
## 所属库

Automated Driving Toolbox / Vehicle Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

使用 Stanley 方法控制车辆转向角以实现路径跟随

Lateral Controller Stanley 模块计算转向角命令（单位为度），该命令在给定车辆当前速度和方向的情况下，调整车辆的当前位姿以匹配参考位姿。控制器使用 Stanley 方法 [1] 计算该命令，其控制律基于运动学和动力学自行车模型。要在模型之间切换，请使用 **Vehicle model** 参数。

- 运动学自行车模型适用于低速环境（如停车场）中的路径跟随，在这些环境中惯性效应最小。
- 动力学自行车模型适用于高速环境（如高速公路）中的路径跟随，在这些环境中惯性效应更为显著。该车辆模型提供描述车辆动力学的附加参数。
