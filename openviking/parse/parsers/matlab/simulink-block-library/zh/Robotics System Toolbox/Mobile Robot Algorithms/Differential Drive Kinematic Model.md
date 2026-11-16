---
type: simulink-block
title: 'Differential Drive Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Mobile Robot Algorithms'
documentation_page: 'differentialdrivekinematicmodel'
documentation_source_path: 'ref/differentialdrivekinematicmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Differential Drive Kinematic Model

## 端口

### 输入

### **dϕL/dt** — 左轮速度 numeric scalar

车辆的左轮速度，以 radians per second 为单位指定。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Wheel Speeds`。

### **dϕR/dt** — 右轮速度 numeric scalar

车辆的右轮速度，以 radians per second 为单位指定。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Wheel Speeds`。

### **v** — 车辆速度 numeric scalar

车辆速度，以 meters per second 为单位指定。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Vehicle Speed & Heading Angular
Velocity`。

### **ɷ** — 车辆的角速度 numeric scalar

车辆的角速度，以 radians per second 为单位指定。正值使车辆向左转向，负值使车辆向右转向。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Vehicle Speed & Heading Angular
Velocity`。

### 输出

### **state** — 车辆的位姿 three-element vector

车辆的当前位置和方向，指定为 [*x y theta*] 向量，单位为 meters 和 radians。

### **stateDot** — `state` 输出的导数 three-element vector

车辆当前的线速度和角速度，指定为 [*xDot yDot thetaDot*] 向量，单位为 meters per second 和 radians per second。线速度和角速度通过求 `state` 输出的导数来计算。

## 参数

### **Vehicle inputs** — 车辆的速度和方向输入类型 `Wheel Speeds`（默认） | `Vehicle Speed & Heading Angular Velocity`

模型输入命令的格式

- `Wheel Speeds` — 两个车轮的角速度，单位为 radians per second。
- `Vehicle Speed & Heading Angular Velocity` — 车辆速度，单位为 meters per second，以及航向角速度，单位为 radians per second。

### **Wheel radius** — 车辆的车轮半径 `0.05`（默认） | positive numeric scalar

车辆上车轮的半径，以 meters 为单位指定。

### **Wheel speed range** — 车辆的最小和最大速度 `[-Inf Inf]`（默认） | two-element vector

车轮速度范围是一个 two-element vector，它提供车辆车轮的最小和最大速度，[*MinSpeed MaxSpeed*]，以 radians per second 为单位指定。

### **Track width** — 车辆从车轮到车轮的轮距长度 `0.2`（默认） | numeric scalar

从左轮到右轮的轮距长度，以 meters 为单位指定。

### **Initial state** — 车辆的初始位姿 `[0;0;0]`（默认） | three-element vector

车辆的初始 *xy*-位置和方向 *θ*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。

**可调:** No

## 所属库

Robotics System Toolbox / Mobile Robot Algorithms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用差速驱动运动学模型计算车辆运动

Differential Drive Kinematic Model 模块创建一个差速驱动车辆模型，以仿真简化的车辆动力学。此模型近似表示具有单个固定车轴且车轮间隔为指定轮距 `Track width` 的车辆。每个车轮都可以分别使用左轮和右轮的速度输入 `dϕL/dt` 和 `dϕR/dt` 独立驱动。车辆速度和航向根据车轴中心定义。

差速驱动运动学模型示意图，标注了 x、y、theta、velocity、track width 和 wheel radius
