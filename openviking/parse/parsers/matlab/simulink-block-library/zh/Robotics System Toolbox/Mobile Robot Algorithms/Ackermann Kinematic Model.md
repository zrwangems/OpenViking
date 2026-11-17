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
```yaml
ports:
- name: v
  summary: 车辆速度 数值标量
  direction: input
- name: dψ/dt
  summary: 转向角速度 数值标量
  direction: input
- name: state
  summary: 车辆状态 四元向量
  direction: output
- name: stateDot
  summary: state 输出的导数 四元向量
  direction: output
```

### 输入

### **v** — 车辆速度 数值标量

车辆速度，以米每秒为单位指定。

### **dψ/dt** — 转向角速度 数值标量

车辆的转向角速度，以弧度每秒为单位指定。
### 输出

### **state** — 车辆状态 四元向量

当前 *xy* 位置、朝向和转向角，指定为 [*x y θ ψ*]，以米和弧度为单位。

### **stateDot** — `state` 输出的导数 四元向量

车辆的线速度和角速度，指定为 [*xDot yDot thetaDot psiDot*] 向量，以米每秒和弧度每秒为单位。
线速度和角速度通过对 `state`
输出求时间导数来计算。
## 参数
```yaml
parameters:
- name: Wheel base
  summary: 前后轴之间的距离 1（默认）| 正数值标量
  group: ''
- name: Vehicle speed range
  summary: 最小和最大车辆速度 [-Inf Inf]（默认）| 二元向量
  group: ''
- name: Maximum steering angle
  summary: 最大转向角 pi/4（默认）| 正数值标量
  group: ''
- name: Initial state
  summary: 车辆初始状态 [0;0;0;0]（默认）| 四元向量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Wheel base** — 前后轴之间的距离 `1`（默认）| 正数值标量

轴距是指车辆前轴和后轴之间的距离，
以米为单位指定。

### **Vehicle speed range** — 最小和最大车辆速度 `[-Inf Inf]`（默认）| 二元向量

车轮速度范围是一个二元向量，提供最小和最大
车辆车轮速度，[*MinSpeed MaxSpeed*]，以弧度每秒
为单位指定。

### **Maximum steering angle** — 最大转向角 `pi/4`（默认）| 正数值标量

最大转向角，指车辆可以向右或向左转向的最大量，
以弧度为单位指定。默认值为
`pi/4`。

### **Initial state** — 车辆初始状态 `[0;0;0;0]`（默认）| 四元向量

车辆的初始 *x*、`y` 位置、
航向角 *theta* 和转向角 *psi*。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用
  MATLAB® 解释器仿真模型。有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
- `Code generation` — 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续
  仿真中重用。

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

使用 Ackermann 运动学模型的类汽车车辆运动

Ackermann Kinematic Model 模块创建一个使用 Ackermann 转向的类汽车车辆模型。该模型表示一辆具有两个车轴的车辆，两轴之间由
距离 `Wheel base` 分隔。车辆
状态定义为四元向量 [*x y θ ψ*]，包含
全局 *xy* 位置、车辆航向 *θ* 和转向
角 *ψ*。车辆航向和 *xy* 位置
定义在后轴中心。角度以弧度为单位指定，全局
位置以米为单位指定。车辆的转向输入以 `dψ/dt` 给出，单位为
弧度每秒。

带有 x、y、theta、psi、速度、轴距和转弯半径标注的 Ackermann 运动学模型图
