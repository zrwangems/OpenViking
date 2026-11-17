---
type: simulink-block
title: 'Chain Drive'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'chaindrive'
documentation_source_path: 'ref/chaindrive.html'
language: zh-CN
chinese_source: worker-translation
---

# Chain Drive

## 端口
```yaml
ports:
- name: A
  summary: 链轮 A 机械旋转
  direction: unspecified
- name: B
  summary: 链轮 B 机械旋转
  direction: unspecified
```

### 守恒

### **A** — 链轮 A 机械旋转

与链轮 A 关联的守恒旋转端口。

### **B** — 链轮 B 机械旋转

与链轮 B 关联的守恒旋转端口。
## 参数
```yaml
parameters:
- name: Chain model
  summary: 链条柔性和间隙模型 Ideal - no chain compliance or backlash（默认）| 模型链合规性与 backlash
  group: 几何
- name: Sprocket A pitch radius
  summary: 链轮 *A* 节圆半径 80 mm（默认）| 标量
  group: 几何
- name: Sprocket B pitch radius
  summary: 链轮 *B* 节圆半径 40 mm（默认）| 标量
  group: 几何
- name: Chain slack length
  summary: 最大松弛长度 50 mm（默认）| 标量
  group: 几何
- name: Chain stiffness
  summary: 线性弹簧常数 1e5 N/m（默认）| 标量
  group: 动力学
- name: Chain damping
  summary: 线性阻尼系数 5 N/(m/s)（默认）| 标量
  group: 动力学
- name: Viscous friction coefficient of sprocket A
  summary: 链轮 *A* 摩擦 0.001 N*m/(rad/s)（默认）
  group: 动力学
- name: Viscous friction coefficient of sprocket B
  summary: 链轮 *B* 摩擦 0.001 N*m/(rad/s)（默认）
  group: 动力学
- name: Maximum tension
  summary: 张力限制模型 No maximum tension（默认）| Specify maximum tension
  group: 最大张力
- name: Chain maximum tension
  summary: 张力上限 1e6 N（默认）
  group: 最大张力
```

### 几何

### **Chain model** — 链条柔性和间隙模型 `Ideal - no chain compliance or backlash`（默认）| `模型链合规性与 backlash`

模块的柔性和间隙模型：

- `Ideal - no chain compliance or
  backlash` — 不对链条刚度、阻尼或间隙进行建模。
- `模型链合规性与
  backlash` — 对链条刚度、阻尼和间隙进行建模。

#### 依赖关系

如果此参数设置为 `Model
chain compliance and backlash`，
则相关参数和变量
启用。

### **Sprocket A pitch radius** — 链轮 *A* 节圆半径 `80` `mm`（默认）| 标量

链轮 A 的节圆半径。节圆是一个假想圆，在完全啮合时穿过链条滚子与链轮齿之间的接触点。

### **Sprocket B pitch radius** — 链轮 *B* 节圆半径 `40` `mm`（默认）| 标量

链轮 B 的节圆半径。节圆是一个假想圆，在完全啮合时穿过链条滚子与链轮齿之间的接触点。

### **Chain slack length** — 最大松弛长度 `50` `mm`（默认）| 标量

传动链条松边在绷紧之前可以移动的最大距离。该距离等于实际传动链条与完全绷紧传动链条之间的长度差。

如果一个链轮固定不动，同时上部链条分支绷紧，则松弛长度是第二个链轮在下部链条分支绷紧之前必须旋转的切向距离。

#### 依赖关系

当 **Chain model** 设置为
`模型链合规性与
backlash` 时，此参数启用。

### 动力学

### **Chain stiffness** — 线性弹簧常数 `1e5` `N/m`（默认）| 标量

链条柔性模型中的线性弹簧常数。该常数描述链条对拉伸应变的阻力。弹簧元件考虑了链条因变形而产生的弹性储能。

#### 依赖关系

当 **Chain model** 设置为
`模型链合规性与
backlash` 时，此参数启用。

### **Chain damping** — 线性阻尼系数 `5` `N/(m/s)`（默认）| 标量

链条柔性模型中的线性阻尼系数。该系数描述链条中相邻元件之间对拉伸运动的阻力。阻尼元件考虑了链条因变形而产生的功率损耗。

#### 依赖关系

当 **Chain model** 设置为
`模型链合规性与
backlash` 时，此参数启用。

### **Viscous friction coefficient of sprocket A** — 链轮 *A* 摩擦 `0.001` `N*m/(rad/s)`（默认）

在存在粘性润滑剂的情况下，链轮 *A* 关节轴承滚动作用引起的摩擦系数。

### **Viscous friction coefficient of sprocket B** — 链轮 *B* 摩擦 `0.001` `N*m/(rad/s)`（默认）

在存在粘性润滑剂的情况下，链轮 *B* 关节轴承滚动作用引起的摩擦系数。

### 最大张力

当 **Chain model** 设置为 `模型链合规性与
backlash` 时，这些设置启用。

### **Maximum tension** — 张力限制模型 `No maximum tension`（默认）| `Specify maximum tension`

选择是否约束传动链条中的最大拉伸力。

- `No maximum
  tension` — 仿真过程中链条张力可以任意大。
- `Specify maximum
  tension` — 链条张力必须保持低于最大值。如果张力超过此值，仿真将生成错误并停止。

#### 依赖关系

当此参数设置为
`Specify maximum
tension` 时，相关参数
启用。

当 **Chain model** 设置为
`模型链合规性与
backlash` 时，此参数启用。

### **Chain maximum tension** — 张力上限 `1e6` `N`（默认）

作用在链条中的拉伸力的最大允许值。

#### 依赖关系

当同时满足以下两个条件时，此参数启用：

- 在 **Geometry**
  设置中，**Chain model**
  参数设置为 `Model chain
  compliance and backlash`。
- 在 **Maximum tension**
  设置中，**Maximum tension**
  参数设置为 `Specify maximum
  tension`。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

带链条和两个链轮的功率传输系统

Chain Drive 模块表示一个带链条和两个链轮的功率传输系统。链条与链轮啮合，在两者之间传递旋转运动。由于外部负载，功率传输可以反向进行，即从从动链轮到主动链轮。这种情况称为反向驱动。

传动链条具有柔性。它可以在张力下拉伸，或者在松弛时变得松弛。柔性模型由并联布置的线性弹簧-阻尼器组构成。弹簧抵抗链条中的拉伸应变。阻尼器抵抗链条元件之间的拉伸运动。

弹簧力和阻尼力直接作用在链条所连接的链轮上。当其中一个链条分支绷紧时，弹簧力存在。阻尼力持续存在。为了表示并报告故障状态，如果链条中的净拉伸力超过指定的最大张力值，仿真将停止并生成错误。

该模块考虑了链轮关节轴承处的粘性摩擦。在运动过程中，粘性摩擦会导致功率传输损耗，从而降低链传动效率。这些损耗会因链条阻尼而加剧。为了消除链传动中的功率传输损耗，在 **Dynamic** 设置中，将粘性摩擦和链条阻尼的参数设置为零。

### 方程

链条中的拉伸应变率是链轮切向速度之差，而每个切向速度均为角速度与节圆半径的乘积。数学上，

x˙=ωARA−ωBRB，

其中：

- *x* 是拉伸
  应变。
- *ωA*、
  *ωB* 是
  链轮角速度。
- *RA*、
  *RB* 是
  链轮节圆半径。

图中显示了相关变量。

链条拉伸力是弹簧力和阻尼力的净和。弹簧力是拉伸应变与弹簧刚度常数的乘积。当拉伸应变小于链条松弛量时，该力为零。阻尼力是拉伸应变率与阻尼系数的乘积。数学上，

F={−(x−S2)k−x˙b,x>S2−x˙b,S2≥x≥−S2−(x+S2)k−x˙b,x<−S2，

其中：

- *S* 是链条
  松弛量。
- *k* 是弹簧刚度
  常数。
- *b* 是阻尼
  系数。

链条对每个链轮施加的扭矩等于拉伸力与链轮节圆半径的乘积。根据以下方程，这两个扭矩作用方向相反：

τA=−F·RA

τB=−F·RB

其中：

- *τA*
  是链条施加在链轮
  *A* 上的扭矩。
- *τB*
  是链条施加在链轮
  *B* 上的扭矩。

在速度方面并考虑摩擦时，适用以下方程：

ωA·RA=ωB·RB

(τA−μA·ωA)RB=−(τB−μB·ωB)RB

其中：

- *ωA*
  是链轮
  *A* 的旋转速度。
- *ωB*
  是链轮
  *B* 的旋转速度。
- *μA*
  是链轮 *A* 的粘性摩擦系数。
- *μB*
  是链轮 *B* 的粘性摩擦系数。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal
Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
