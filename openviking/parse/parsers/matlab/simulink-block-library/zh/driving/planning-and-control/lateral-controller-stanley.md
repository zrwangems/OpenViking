---
type: simulink-block
title: 'Lateral Controller Stanley'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Planning and Control'
documentation_page: 'lateralcontrollerstanley'
documentation_source_path: 'ref/lateralcontrollerstanley.html'
language: zh-CN
chinese_source: worker-translation
---

# Lateral Controller Stanley

## 端口

### 输入

### **RefPose** — 参考位姿 [*x*, *y*, *Θ*] 向量

参考位姿，指定为 [*x*, *y*, *Θ*] 向量。*x* 和 *y* 的单位为 meters，*Θ* 的单位为 degrees。

*x* 和 *y* 指定使车辆转向的目标参考点。*Θ* 指定该参考点处路径的朝向角，逆时针方向为正。

- 对于前向运动的车辆，参考点是路径上距离车辆前轴中心最近的点。

  前向运动车辆，且路径上的参考点已标记。坐标采用世界坐标。
- 对于倒车运动的车辆，参考点是路径上距离车辆后轴中心最近的点。

  倒车运动车辆，且路径上的参考点已标记。坐标采用世界坐标。

**Data Types:** `single` | `double`

### **CurrPose** — 当前位姿 [*x*, *y*, *Θ*] 向量

车辆的当前位姿，指定为 [*x*, *y*, *Θ*] 向量。*x* 和 *y* 的单位为 meters，*Θ* 的单位为 degrees。

*x* 和 *y* 指定车辆的位置，该位置定义为车辆后轴中心。

*Θ* 指定车辆在位置 (*x*,*y*) 处的朝向角，逆时针方向为正。

车辆已标记位姿。坐标采用世界坐标。

有关车辆位姿的更多详细信息，请参阅 Automated Driving Toolbox 中的“坐标系”。

**Data Types:** `single` | `double`

### **CurrVelocity** — 当前纵向速度 实数标量

车辆的当前纵向速度，指定为实数标量。单位为 meters per second。

- 如果车辆处于前向运动，则该值必须大于 0。
- 如果车辆处于倒车运动，则该值必须小于 0。
- 值为 0 表示车辆未运动。

**Data Types:** `single` | `double`

### **Direction** — 车辆行驶方向 `1`（前向运动）| `-1`（倒车运动）

车辆行驶方向，指定为 `1` 表示前向运动，或 `-1` 表示倒车运动。行驶方向决定用于计算转向角命令的位置误差和角度误差。更多详细信息，请参阅算法。

### **Curvature** — 路径曲率 实数标量

参考点处路径的曲率，以 radians per meter 为单位，指定为实数标量。

- 对于前向运动的车辆，参考点是路径上距离车辆前轴中心最近的点。

  前向运动车辆，且路径上的参考点已标记。坐标采用世界坐标。
- 对于倒车运动的车辆，参考点是路径上距离车辆后轴中心最近的点。

  倒车运动车辆，且路径上的参考点已标记。坐标采用世界坐标。

您可以从 Path Smoother Spline 模块的 **Curvatures** 输出端口获取路径的曲率。您还可以从 Scenario Reader 模块的输出车道边界结构体获取车道边界的曲率。

#### 依赖关系

要启用此端口，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **CurrYawRate** — 当前横摆角速度 实数标量

车辆的当前横摆角速度，以 degrees per second 为单位，指定为实数标量。当前横摆角速度是车辆角速度的变化率。

#### 依赖关系

要启用此端口，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **CurrSteer** — 当前转向角 实数标量

车辆的当前转向角，以 degrees 为单位，指定为实数标量。该值在逆时针方向为正。

前轮转动并标记了转向角的车辆

有关更多详细信息，请参阅 Automated Driving Toolbox 中的“坐标系”。

#### 依赖关系

要启用此端口，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### 输出

### **SteerCmd** — 转向角命令 实数标量

转向角命令，以 degrees 为单位，以实数标量形式返回。该值在逆时针方向为正。

前轮转动并标记了转向角的车辆

有关更多详细信息，请参阅 Automated Driving Toolbox 中的“坐标系”。

## 参数

### **Vehicle model** — 车辆模型 `Kinematic bicycle model`（默认）| `Dynamic bicycle model`

选择车辆模型类型，以设置模块使用的 Stanley 方法控制律。

- `Kinematic bicycle model` — 用于低速环境（如停车场，惯量影响极小）中路径跟随的运动学自行车模型
- `Dynamic bicycle model` — 用于高速环境（如高速公路，惯量影响更明显）中路径跟随的动力学自行车模型

### **Position gain of forward motion** — 车辆前向运动时的位置增益 `2.5`（默认）| 正实数标量

车辆前向运动时的位置增益，指定为正标量。该值决定位置误差对转向角的影响程度。典型值在范围 [1, 5] 内。增大该值会增加转向角的幅值。

### **Position gain of reverse motion** — 车辆倒车运动时的位置增益 `2.5`（默认）| 正实数标量

车辆倒车运动时的位置增益，指定为正标量。该值决定位置误差对转向角的影响程度。典型值在范围 [1, 5] 内。增大该值会增加转向角的幅值。

### **Yaw rate feedback gain** — 横摆角速度反馈增益 `2.5`（默认）| 非负实数标量

横摆角速度反馈增益，指定为非负实数标量。该值决定当模块计算转向角命令时，对车辆当前横摆角速度赋予的权重。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Steering angle feedback gain** — 转向角反馈增益 `2.5`（默认）| 非负实数标量

转向角反馈增益，指定为非负实数标量。该值决定当前转向角命令 **SteerCmd** 与当前转向角 **CurrSteer** 之间的差异对下一转向角命令的影响程度。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Wheelbase of vehicle (m)** — 前轴与后轴之间的距离 `2.8`（默认）| 实数标量

车辆前轴与后轴之间的距离，以 meters 为单位，指定为实数标量。该值仅在车辆前向运动时适用，即当 **Direction** 输入端口为 `1` 时。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Kinematic bicycle model`。

### **Vehicle mass (kg)** — 车辆质量 `1575`（默认）| 正实数标量

车辆质量，以 kilograms 为单位，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Longitudinal distance from center of mass to front axle (m)** — 到前轴的距离 `1.2`（默认）| 正实数标量

从车辆质心到其前轮轴的纵向距离，以 meters 为单位，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Longitudinal distance from center of mass to rear axle (m)** — 到后轴的距离 `1.6`（默认）| 正实数标量

从车辆质心到其后轮轴的纵向距离，以 meters 为单位，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Front tire corner stiffness (N/rad)** — 前轮胎侧偏刚度 `19000`（默认）| 正实数标量

前轮胎侧偏刚度，以 Newtons per radian 为单位，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Vehicle model** 设置为 `Dynamic bicycle model`。

### **Maximum steering angle (deg)** — 最大允许转向角 `35`（默认）| 范围 (0, 180) 内的实数标量

车辆的最大允许转向角，以 degrees 为单位，指定为范围 (0, 180) 内的实数标量。

**SteerCmd** 端口的输出被饱和到范围 [–*M*, *M*]，其中 *M* 是 **Maximum steering angle (deg)** 参数的值。

- 低于 –*M* 的值设置为 –*M*。
- 高于 *M* 的值设置为 *M*。

## 所属库

Automated Driving Toolbox / Vehicle Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

使用 Stanley 方法控制车辆转向角以进行路径跟随

Lateral Controller Stanley 模块计算转向角命令（单位为 degrees），该命令根据车辆的当前速度和方向，调整车辆的当前位姿以匹配参考位姿。控制器使用 Stanley 方法 [1] 计算此命令，该方法的控制律基于运动学自行车模型和动力学自行车模型。若要在模型之间切换，请使用 **Vehicle model** 参数。

- 运动学自行车模型适用于低速环境（如停车场，惯量影响极小）中的路径跟随。
- 动力学自行车模型适用于高速环境（如高速公路，惯量影响更明显）中的路径跟随。该车辆模型提供描述车辆动力学的附加参数。
