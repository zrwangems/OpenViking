---
type: simulink-block
title: 'Bicycle Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Mobile Robot Algorithms'
documentation_page: 'bicyclekinematicmodel'
documentation_source_path: 'ref/bicyclekinematicmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Bicycle Kinematic Model

## 端口
```yaml
ports:
- name: v
  summary: 车辆速度 数值标量
  direction: input
- name: psi
  summary: 转向角 数值标量
  direction: input
- name: omega
  summary: 转向角速度 数值标量
  direction: input
- name: state
  summary: 车辆位姿 三元素向量
  direction: output
- name: stateDot
  summary: state 输出的导数 三元素向量
  direction: output
```

### 输入

### **v** — 车辆速度 数值标量

车辆速度，以米每秒为单位指定。

### **psi** — 转向角 数值标量

车辆的转向角，以弧度为单位指定。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Vehicle Speed & Steering
Angle`。

### **omega** — 转向角速度 数值标量

车辆的角速度，以弧度每秒为单位指定。正值使车辆向左转向，负值使车辆向右转向。

#### 依赖关系

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Vehicle Speed & Heading Angular
Velocity`。
### 输出

### **state** — 车辆位姿 三元素向量

车辆当前的 *xy* 位置和朝向，以 *[x y theta]* 向量表示，单位为米和弧度。

### **stateDot** — `state` 输出的导数 三元素向量

车辆的线速度和角速度，以 *[xDot
yDot thetaDot]* 向量表示，单位为米每秒和弧度每秒。线速度和角速度通过对 `state`
输出求导计算得出。
## 参数
```yaml
parameters:
- name: Vehicle inputs
  summary: 车辆的速度和方向输入类型 Vehicle Speed & Steering Angle（默认）| Vehicle Speed & Heading Angular Velocity
  group: ''
- name: Wheel base
  summary: 前轴和后轴之间的距离 1（默认）| 正数值标量
  group: ''
- name: Vehicle speed range
  summary: 车辆速度的最小值和最大值 [-Inf Inf]（默认）| 二元素向量
  group: ''
- name: Maximum steering angle
  summary: 最大转弯半径 pi/4（默认）| 数值标量
  group: ''
- name: Initial state
  summary: 车辆的初始位姿 [0;0;0]（默认）| 三元素向量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Vehicle inputs** — 车辆的速度和方向输入类型 `Vehicle Speed & Steering Angle`（默认）| `Vehicle Speed & Heading Angular Velocity`

车辆的速度和方向输入类型，指定为以下选项之一：

- `Vehicle Speed & Steering Angle` — 车辆速度以米每秒为单位，转向角以弧度为单位。
- `Vehicle Speed & Heading Angular Velocity` — 车辆速度以米每秒为单位，航向角速度以弧度每秒为单位。

### **Wheel base** — 前轴和后轴之间的距离 `1`（默认）| 正数值标量

轴距是指车辆前轴和后轴之间的距离，以米为单位指定。

### **Vehicle speed range** — 车辆速度的最小值和最大值 `[-Inf Inf]`（默认）| 二元素向量

车轮速度范围是一个二元素向量，提供车辆车轮速度的最小值和最大值，[*MinSpeed MaxSpeed*]，以弧度每秒为单位指定。

### **Maximum steering angle** — 最大转弯半径 `pi/4`（默认）| 数值标量

最大转向角，是指车辆可以向右或向左转向的最大量，以弧度为单位指定。此属性用于验证用户提供的状态输入。

如果将 `Maximum steering angle` 设置为 `pi/2`，则最小转弯半径为零米。

### **Initial state** — 车辆的初始位姿 `[0;0;0]`（默认）| 三元素向量

车辆的初始 *x*、`y` 位置和朝向 *theta*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。

**可调：** 否
## 所属库

Robotics System Toolbox / Mobile Robot Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用自行车运动学模型计算类汽车车辆运动

自行车运动学模型模块创建一个自行车车辆模型，用于仿真简化的类汽车车辆动力学。该模型表示一辆具有两个车轴的车辆，由车轴之间的距离 `Wheel base` 定义。前轮可以通过转向角 `psi` 进行转动。车辆航向 `theta` 定义在后轴中心处。

带有 x、y、theta、psi、velocity、wheel base 和 turning radius 标注的自行车运动学模型示意图

自行车运动学模型模块创建一个自行车车辆模型，用于
模拟简化的类汽车车辆动力学。该模型表示一辆具有两个车轴的车辆
defined by the length between the axles, `Wheel base`. The
前轮可以通过转向角 `psi` 进行转动。
vehicle heading `theta` is defined at the center of the rear axle.

带有 x、y、theta、psi、velocity、wheel base 和 turning radius 标注的自行车运动学模型图
