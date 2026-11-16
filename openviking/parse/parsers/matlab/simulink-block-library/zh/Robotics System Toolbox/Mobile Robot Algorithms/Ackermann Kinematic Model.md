---
type: simulink-block
title: 'Ackermann Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Mobile Robot Algorithms'
documentation_page: 'ackermannkinematicmodel'
documentation_source_path: 'ref/ackermannkinematicmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Ackermann Kinematic Model

## 端口

### 输入

### **v** — 车辆速度 numeric scalar

车辆速度，以 meters per second 指定。

### **dψ/dt** — 转向角速度 numeric scalar

车辆的转向角速度，以 radians per second 指定。
### 输出

### **state** — 车辆状态 four-element vector

当前 *xy*-位置、朝向和转向角，指定为 [*x y θ ψ*]，单位为 meters and radians。

### **stateDot** — `state` 输出的导数 four-element vector

车辆的线速度和角速度，指定为 [*xDot
yDot thetaDot psiDot*] 向量，单位为 meters per second and radians per second。
线速度和角速度通过求 `state` 输出的时间导数计算得出。

## 参数

### **轴距** — 前轴和后轴之间的距离 `1` (默认) | positive numeric scalar

轴距指的是车辆前轴和后轴之间的距离，以 meters 指定。

### **车辆速度范围** — 最小和最大车辆速度 `[-Inf Inf]` (默认) | two-element vector

车轮速度范围是一个 two-element vector，提供车辆车轮的最小和最大速度，[*MinSpeed MaxSpeed*]，以 radians per second 指定。

### **最大转向角** — 最大转向角 `pi/4` (默认) | positive numeric scalar

最大转向角指的是车辆可以向右或向左转向的最大量，以 radians 指定。默认值为 `pi/4`。

### **初始状态** — 车辆初始状态 `[0;0;0;0]` (默认) | four-element vector

车辆的初始 *x*、`y` 位置、航向角 *theta* 和转向角 *psi*。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

- `Interpreted execution` — 使用
  MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码会在后续
  仿真中重用。

**可调：** No

## 所属库

Robotics System Toolbox / Mobile Robot Algorithms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2019b 中引入**

## 描述

使用 Ackermann 运动学模型的类汽车车辆运动

Ackermann Kinematic Model 模块创建一个使用 Ackermann 转向的类汽车车辆模型。该模型表示一辆具有两个轴的车辆，两轴之间的距离为 `Wheel base`。车辆状态定义为 four-element vector，[*x y θ ψ*]，其中包含全局 *xy-*位置、车辆航向 *θ* 和转向角 *ψ*。车辆航向和 *xy*-位置定义在后轴中心。角度以 radians 指定，全局位置以 meters 指定。车辆的转向输入以 `dψ/dt` 给出，单位为 radians per second。

标有 x、y、theta、psi、速度、轴距和转弯半径的 Ackermann 运动学模型示意图
