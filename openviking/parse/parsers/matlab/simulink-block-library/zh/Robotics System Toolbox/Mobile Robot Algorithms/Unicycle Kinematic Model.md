---
type: simulink-block
title: 'Unicycle Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Mobile Robot Algorithms'
documentation_page: 'unicyclekinematicmodel'
documentation_source_path: 'ref/unicyclekinematicmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Unicycle Kinematic Model

## 端口

### 输入

### **dϕ/dt** — 车轮角速度 数值标量

车轮的角速度，以弧度每秒为单位。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Wheel Speed & Heading Angular
Velocity`。

### **v** — 车辆速度 数值标量

车辆速度，以米每秒为单位指定。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Vehicle Speed & Heading Angular
Velocity`。

### **ω** — 转向角速度 数值标量

车辆的角速度，以弧度每秒为单位指定。正值使车辆向左转向，负值使车辆向右转向。
### 输出

### **state** — 车辆位姿 三元素向量

车辆当前的 *xy* 位置和朝向，以 *[x y theta]* 向量形式指定，单位为米和弧度。

### **stateDot** — `state` 输出的导数 三元素向量

车辆的线速度和角速度，以 *[xDot
yDot thetaDot]* 向量形式指定，单位为米每秒和弧度每秒。线速度和角速度通过对 `state`
输出求导计算得出。

## 参数

### **Vehicle inputs** — 车辆的速度和方向输入类型 `Vehicle Speed & Heading Angular Velocity`（默认）| `Wheel Speed & Heading Angular Velocity`

用于控制车辆的速度和方向输入类型。选项包括：

- `Vehicle Speed & Heading Angular Velocity` —
  车辆速度，以米每秒为单位，以及航向角速度，以弧度每秒为单位。
- `Wheel Speed & Heading Angular Velocity` — 车轮
  速度，以弧度每秒为单位，以及航向角速度，以弧度每秒为单位。

### **Wheel radius** — 车辆的车轮半径 `0.1`（默认）| 正数值标量

车辆的车轮半径，以米为单位指定。

### **Wheel speed range** — 车辆速度的最小值和最大值 `[-Inf Inf]`（默认）| 二元素向量

车轮速度的最小值和最大值，以弧度每秒为单位指定。

### **Initial state** — 前后轴之间的距离 `[0;0;0]`（默认）| 三元素向量

车辆的初始 *x*、`y` 位置和朝向 *theta*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用
  MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码将在后续
  仿真中重复使用。

**Tunable:** No

## 所属库

Robotics System Toolbox / Mobile Robot Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用独轮车运动学模型计算车辆运动

Unicycle Kinematic Model 模块创建一个独轮车车辆模型，用于
仿真简化的类汽车车辆动力学。该模型将车辆近似为具有给定车轮半径 `Wheel radius`
的独轮车，该独轮车可以根据转向角速度 `ω` 原地旋转。

带有 x、y、theta、速度、转向速度和车轮半径标注的独轮车运动学模型图
