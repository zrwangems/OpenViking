---
type: simulink-block
title: 'Unicycle Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Mobile Robot Modeling'
documentation_page: 'unicyclekinematicmodel'
documentation_source_path: 'ref/unicyclekinematicmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Unicycle Kinematic Model

## 端口

### 输入

### **dϕ/dt** — 车轮角速度 numeric scalar

车轮的角速度，单位为 radians per second。

#### 依赖关系

要启用此端口，请将 `Vehicle inputs` 参数设置为 `Wheel Speed & Heading Angular Velocity`。

### **v** — 车辆速度 numeric scalar

车辆速度，单位为 meters per second。

#### 依赖关系

要启用此端口，请将 `Vehicle inputs` 参数设置为 `Vehicle Speed & Heading Angular Velocity`。

### **ω** — 转向角速度 numeric scalar

车辆的角速度，单位为 radians per second。正值使车辆左转，负值使车辆右转。

### 输出

### **state** — 车辆位姿 three-element vector

车辆的当前 *xy* 位置和朝向，指定为 *[x y theta]* 向量，单位为 meters 和 radians。

### **stateDot** — `state` 输出的导数 three-element vector

车辆的线速度和角速度，指定为 *[xDot yDot thetaDot]* 向量，单位为 meters per second 和 radians per second。线速度和角速度通过求 `state` 输出的导数计算得到。

## 参数

### **Vehicle inputs** — 车辆的速度和方向输入类型 `Vehicle Speed & Heading Angular Velocity` (默认) | `Wheel Speed & Heading Angular Velocity`

用于控制车辆的速度和方向输入类型。选项包括：

- `Vehicle Speed & Heading Angular Velocity` — 车速，单位为 meters per second，以及航向角速度，单位为 radians per second。
- `Wheel Speed & Heading Angular Velocity` — 车轮速度，单位为 radians per second，以及航向角速度，单位为 radians per second。

### **Wheel radius** — 车辆的车轮半径 `0.1` (默认) | positive numeric scalar

车辆的车轮半径，单位为 meters。

### **Wheel speed range** — 车辆最小和最大速度 `[-Inf Inf]` (默认) | two-element vector

最小和最大车轮速度，单位为 radians per second。

### **Initial state** — 前轴和后轴之间的距离 `[0;0;0]` (默认) | three-element vector

车辆的初始 *x*-、`y`-位置和朝向 *theta*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不更改，后续仿真会重用该 C 代码。

**可调：** No

## 所属库

Robotics System Toolbox / Mobile Robot Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用单轮车运动学模型计算车辆运动

Unicycle Kinematic Model 模块创建一个单轮车车辆模型，以仿真简化的类汽车车辆动力学。此模型将车辆近似为具有给定车轮半径 `Wheel radius` 的单轮车，该单轮车可根据转向角速度 `ω` 原地旋转。

标注了 x、y、theta、velocity、steering velocity 和 wheel radius 的单轮车运动学模型图
