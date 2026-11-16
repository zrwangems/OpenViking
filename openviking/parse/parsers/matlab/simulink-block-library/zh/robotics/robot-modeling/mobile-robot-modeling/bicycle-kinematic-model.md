---
type: simulink-block
title: 'Bicycle Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Mobile Robot Modeling'
documentation_page: 'bicyclekinematicmodel'
documentation_source_path: 'ref/bicyclekinematicmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Bicycle Kinematic Model

## 端口

### 输入

### **v** — 车辆速度 numeric scalar

车辆速度，以 meters per second 为单位。

### **psi** — 转向角 numeric scalar

车辆转向角，以 radians 为单位。

#### 依赖关系

要启用此端口，将 `Vehicle inputs` 参数设置为 `Vehicle Speed & Steering Angle`。

### **omega** — 转向角速度 numeric scalar

车辆的角速度，以 radians per second 为单位。正值使车辆左转，负值使车辆右转。

#### 依赖关系

要启用此端口，将 `Vehicle inputs` 参数设置为 `Vehicle Speed & Heading Angular Velocity`。

### 输出

### **state** — 车辆位姿 three-element vector

车辆的当前 *xy*-位置和朝向，指定为 *[x y theta]* 向量，以 meters 和 radians 为单位。

### **stateDot** — `state` 输出的导数 three-element vector

车辆的线速度和角速度，指定为 *[xDot yDot thetaDot]* 向量，以 meters per second 和 radians per second 为单位。线速度和角速度通过求 `state` 输出的导数计算。

## 参数

### **Vehicle inputs** — 车辆的速度和方向输入类型 `Vehicle Speed & Steering Angle`（默认） | `Vehicle Speed & Heading Angular Velocity`

车辆的速度和方向输入类型，指定为以下选项之一：

- `Vehicle Speed & Steering Angle` — 车辆速度，以 meters per second 为单位，并带有转向角，以 radians 为单位。
- `Vehicle Speed & Heading Angular Velocity` — 车辆速度，以 meters per second 为单位，并带有航向角速度，以 radians per second 为单位。

### **Wheel base** — 前后轴之间的距离 `1`（默认） | positive numeric scalar

Wheel base 指前后车辆轴之间的距离，以 meters 为单位。

### **Vehicle speed range** — 最小和最大车辆速度 `[-Inf Inf]`（默认） | two-element vector

车轮速度范围是 two-element vector，提供最小和最大车辆车轮速度，[*MinSpeed MaxSpeed*]，以 radians per second 为单位。

### **Maximum steering angle** — 最大转向半径 `pi/4`（默认） | numeric scalar

最大转向角，指车辆可以向右或向左转向的最大量，以 radians 为单位。此属性用于验证用户提供的 state 输入。

如果 `Maximum steering angle` 设置为 `pi/2`，则会导致最小转向半径为 zero meters。

### **Initial state** — 车辆初始位姿 `[0;0;0]`（默认） | three-element vector

车辆的初始 *x*-、`y`-位置和朝向 *theta*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。

**Tunable:** No

## 所属库

Robotics System Toolbox / Mobile Robot Algorithms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用自行车运动学模型计算类汽车车辆运动

Bicycle Kinematic Model 模块创建一个自行车车辆模型，以仿真简化的类汽车车辆动力学。此模型表示具有两个车轴的车辆，两个车轴由轴间距离 `Wheel base` 定义。前轮可通过转向角 `psi` 转动。车辆航向 `theta` 在后轴中心处定义。

带有 x、y、theta、psi、velocity、wheel base 和 turning radius 标注的自行车运动学模型图
