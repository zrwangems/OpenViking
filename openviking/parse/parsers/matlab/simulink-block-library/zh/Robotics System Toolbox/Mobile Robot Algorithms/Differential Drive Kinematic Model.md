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
```yaml
ports:
- name: dϕL/dt
  summary: 左轮速度 数值标量
  direction: input
- name: dϕR/dt
  summary: 右轮速度 数值标量
  direction: input
- name: v
  summary: 车辆速度 数值标量
  direction: input
- name: ɷ
  summary: 车辆角速度 数值标量
  direction: input
- name: state
  summary: 车辆位姿 三元素向量
  direction: output
- name: stateDot
  summary: state 输出的导数 三元素向量
  direction: output
```

### 输入

### **dϕL/dt** — 左轮速度 数值标量

车辆的左轮速度，以弧度每秒为单位指定。

#### 依赖

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Wheel Speeds`。

### **dϕR/dt** — 右轮速度 数值标量

车辆的右轮速度，以弧度每秒为单位指定。

#### 依赖

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Wheel Speeds`。

### **v** — 车辆速度 数值标量

车辆速度，以米每秒为单位指定。

#### 依赖

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Vehicle Speed & Heading Angular
Velocity`。

### **ɷ** — 车辆角速度 数值标量

车辆的角速度，以弧度每秒为单位指定。正值使车辆左转，负值使车辆右转。

#### 依赖

要启用此端口，请将 `Vehicle
inputs` 参数设置为 `Vehicle Speed & Heading Angular
Velocity`。
### 输出

### **state** — 车辆位姿 三元素向量

车辆的当前位置和方向，以 [*x y
theta*] 向量形式指定，单位为米和弧度。

### **stateDot** — `state` 输出的导数 三元素向量

车辆当前的线速度和角速度，以
[*xDot yDot thetaDot*] 向量形式指定，单位为米每秒和弧度每
秒。线速度和角速度通过对 `state`
输出求导计算得出。
## 参数
```yaml
parameters:
- name: Vehicle inputs
  summary: 车辆速度和方向输入的类型 Wheel Speeds（默认）| Vehicle Speed & Heading Angular Velocity
  group: ''
- name: Wheel radius
  summary: 车辆的车轮半径 0.05（默认）| 正数值标量
  group: ''
- name: Wheel speed range
  summary: 车辆速度的最小值和最大值 [-Inf Inf]（默认）| 二元素向量
  group: ''
- name: Track width
  summary: 车辆从车轮到车轮的轮距长度 0.2（默认）| 数值标量
  group: ''
- name: Initial state
  summary: 车辆的初始位姿 [0;0;0]（默认）| 三元素向量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Vehicle inputs** — 车辆速度和方向输入的类型 `Wheel Speeds`（默认）| `Vehicle Speed & Heading Angular Velocity`

模型输入命令的格式

- `Wheel Speeds` — 两个车轮的角速度，以
  弧度每秒为单位。
- `Vehicle Speed & Heading Angular Velocity` —
  车辆速度，以米每秒为单位，以及航向角速度，以弧度每
  秒为单位。

### **Wheel radius** — 车辆的车轮半径 `0.05`（默认）| 正数值标量

车辆上车轮的半径，以米为单位指定。

### **Wheel speed range** — 车辆速度的最小值和最大值 `[-Inf Inf]`（默认）| 二元素向量

车轮速度范围是一个二元素向量，提供车辆车轮速度的最小值和最大值，
[*MinSpeed MaxSpeed*]，以弧度每
秒为单位指定。

### **Track width** — 车辆从车轮到车轮的轮距长度 `0.2`（默认）| 数值标量

从左轮到右轮的轮距长度，以米为单位指定。

### **Initial state** — 车辆的初始位姿 `[0;0;0]`（默认）| 三元素向量

车辆的初始 *xy* 位置和方向 *θ*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用
  MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码将在后续
  仿真中重用。

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

使用差速驱动运动学模型计算车辆运动

Differential Drive Kinematic Model 模块创建一个差速驱动
车辆模型，以仿真简化的车辆动力学。该模型近似表示具有
单个固定轴且车轮由指定轮距 `Track width` 分隔的车辆。
每个车轮可以使用速度输入 `dϕL/dt` 和 `dϕR/dt` 独立驱动，分别对应左轮和右轮。
车辆速度和航向由轴中心定义。

带有 x、y、theta、速度、轮距和车轮半径标注的差速驱动运动学模型图
