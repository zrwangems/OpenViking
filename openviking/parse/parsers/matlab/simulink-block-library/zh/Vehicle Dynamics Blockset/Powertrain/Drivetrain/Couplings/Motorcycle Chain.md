---
type: simulink-block
title: 'Motorcycle Chain'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Couplings'
documentation_page: 'motorcyclechain'
documentation_source_path: 'ref/motorcyclechain.html'
language: zh-CN
chinese_source: worker-translation
---

# Motorcycle Chain

## 端口
```yaml
ports:
- name: MDshft
  summary: 前链轮上的驱动轴力矩 scalar
  direction: input
- name: FCpR
  summary: 后轮接地点处的纵向力和垂向力 vector
  direction: input
- name: ThetaFrm
  summary: 主车架俯仰角 scalar
  direction: input
- name: ThetaArmR
  summary: 后摇臂俯仰角 scalar
  direction: input
- name: MBrkR
  summary: 后轮制动力矩 scalar
  direction: input
- name: AngAWhlR
  summary: 后轮角加速度 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: MDrvSprtR
  summary: 后链轮处的轮减振器力矩 scalar
  direction: output
- name: MDrvArmR
  summary: 后摇臂处的驱动链力矩 scalar
  direction: output
- name: MDrvFrm
  summary: 车架处的驱动链力矩 scalar
  direction: output
```

### 输入

### **MDshft** — 前链轮上的驱动轴力矩 `scalar`

前链轮上绕 *ym* 的驱动轴力矩，单位为 N·m。

### **FCpR** — 后轮接地点处的纵向力和垂向力 `vector`

后轮接地点 *OCpR* 处沿 *iCpR* 和 *kCpR* 的纵向力和垂向力，单位为 N。信号向量维度为 `[1x2]` 或 `[2x1]`。

### **ThetaFrm** — 主车架俯仰角 `scalar`

主车架俯仰角 *ϴfrm*，单位为 rad。

### **ThetaArmR** — 后摇臂俯仰角 `scalar`

后摇臂俯仰角 *ϴra*，单位为 rad。

### **MBrkR** — 后轮制动力矩 `scalar`

后轮 *GWhlRr* 上绕 *jWhlRr* 的制动力矩，单位为 N·m。

### **AngAWhlR** — 后轮角加速度 `scalar`

后轮角加速度，单位为 rad/s2。

### 输出

### **Info** — 总线信号 bus

包含以下模块计算结果的总线信号。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `FChn` | 施加到后摇臂的链条力 | N |
| `AngVSprtR` | 后链轮角速度 | rad/s |
| `MDrvSprtR` | 施加到后链轮的轮减振器力矩 | N·m |
| `WhlDmpAng` | 后链轮与后轮之间的角度 | rad |

### **MDrvSprtR** — 后链轮处的轮减振器力矩 `scalar`

施加到后链轮的轮减振器力矩，单位为 N·m。

### **MDrvArmR** — 后摇臂处的驱动链力矩 `scalar`

后摇臂 *OArmRr* 上绕 *jArmRr* 的驱动链力矩，单位为 N·m。

### **MDrvFrm** — 车架处的驱动链力矩 `scalar`

车架 *OFrm* 上绕 *jFrm* 的驱动链力矩，单位为 N·m。
## 参数
```yaml
parameters:
- name: Coordinates, SprktFrPxz
  summary: 前链轮位置 [0.05 -0.05]（默认）| vector
  group: ''
- name: Mass moment of inertia, SprktFrIyy
  summary: 前链轮转动惯量 0.005（默认）| scalar
  group: ''
- name: Radius, SprktFrR
  summary: 前链轮半径 0.04（默认）| scalar
  group: ''
- name: Mass moment of inertia, SprktRrIyy
  summary: 后链轮转动惯量 0.01（默认）| scalar
  group: ''
- name: Radius, SprktRrR
  summary: 后链轮半径 0.12（默认）| scalar
  group: ''
- name: Mass moment of inertia, WhlRrIyy
  summary: 后轮转动惯量 0.66（默认）| scalar
  group: ''
- name: Radius, WhlRrR
  summary: 后轮半径 0.33（默认）| scalar
  group: ''
- name: Arm length, ArmRrLen
  summary: 摇臂长度 0.535（默认）| scalar
  group: ''
- name: Stiffness, WhlDmpK
  summary: 轮减振器刚度 1e4（默认）| scalar
  group: ''
- name: Damping, WhlDmpC
  summary: 轮减振器阻尼 1e2（默认）| scalar
  group: ''
- name: Equilibrium angle
  summary: 轮减振器平衡角 -15e-3（默认）| scalar
  group: ''
- name: Rear sprocket angular velocity, SprktRrAngV0
  summary: 角速度 0（默认）| scalar
  group: ''
- name: Rear wheel angular velocity, WhlRrAngV0
  summary: 角速度 0（默认）| scalar
  group: ''
```

下图展示了链条与摩托车车架、后摇臂和后轮之间的几何关系。

摩托车链条示意图

#### 前链轮

### **Coordinates, SprktFrPxz** — 前链轮位置 `[0.05 -0.05]`（默认）| `vector`

前链轮位置 *SprktFrPxz*，分别沿 *xm*、*zm* 方向，单位为 m。

### **Mass moment of inertia, SprktFrIyy** — 前链轮转动惯量 `0.005`（默认）| `scalar`

前链轮质量转动惯量 *SprktFrIyy*，单位为 kg·m2。

### **Radius, SprktFrR** — 前链轮半径 `0.04`（默认）| `scalar`

前链轮半径 *SprktFrR*，单位为 m。

#### 后链轮

### **Mass moment of inertia, SprktRrIyy** — 后链轮转动惯量 `0.01`（默认）| `scalar`

后链轮质量转动惯量 *SprktRrIyy*，单位为 kg·m2。

### **Radius, SprktRrR** — 后链轮半径 `0.12`（默认）| `scalar`

后链轮半径 *SprktRrR*，单位为 m。

#### 后轮

### **Mass moment of inertia, WhlRrIyy** — 后轮转动惯量 `0.66`（默认）| `scalar`

后轮质量转动惯量 *WhlRrIyy*，单位为 kg·m2。

### **Radius, WhlRrR** — 后轮半径 `0.33`（默认）| `scalar`

后轮半径 *WhlRrR*，单位为 m。

#### 摇臂

### **Arm length, ArmRrLen** — 摇臂长度 `0.535`（默认）| `scalar`

摇臂长度 *ArmRrLen*，单位为 m。

#### 轮减振器

### **Stiffness, WhlDmpK** — 轮减振器刚度 `1e4`（默认）| `scalar`

轮减振器刚度 *WhlDmpK*，单位为 N/rad。

### **Damping, WhlDmpC** — 轮减振器阻尼 `1e2`（默认）| `scalar`

轮减振器阻尼 *WhlDmpC*，单位为 N·s/rad。

### **Equilibrium angle** — 轮减振器平衡角 `-15e-3`（默认）| `scalar`

平衡角 *WhlDmpAng0*，单位为 rad。

#### 初始条件

### **Rear sprocket angular velocity, SprktRrAngV0** — 角速度 `0`（默认）| `scalar`

后链轮角速度 *SprktRrAngV0*，单位为 rad/s。

### **Rear wheel angular velocity, WhlRrAngV0** — 角速度 `0`（默认）| `scalar`

后轮角速度 *WhlRrAngV0*，单位为 rad/s。
## 所属库

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

实现摩托车链条

Motorcycle Chain 模块实现摩托车链条对 Motorcycle Body Longitudinal In-Plane 模块的动态效应，包括动态张力和力矩驱动耦合。

下图展示了链条与摩托车车架、后摇臂和后轮之间的几何关系。

摩托车链条示意图

| 车架 | 图中变量 | 描述 |
| --- | --- | --- |
| 摩托车主车架  - *xm* – 沿指向前叉的向量向前 - *zm* – 向下 - *ym* – 垂直于摩托车平面 | *Om* | 主车架原点 |
