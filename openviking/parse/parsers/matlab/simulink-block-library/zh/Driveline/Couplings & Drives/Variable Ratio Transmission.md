---
type: simulink-block
title: 'Variable Ratio Transmission'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'variableratiotransmission'
documentation_source_path: 'ref/variableratiotransmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Ratio Transmission

## 端口
```yaml
ports:
- name: r
  summary: 输入轴与输出轴转速比，无量纲物理信号
  direction: input
- name: B
  summary: 基座驱动轴机械旋转
  direction: input
- name: F
  summary: 从动驱动轴机械旋转
  direction: input
```

### 输入

### **r** — 输入轴与输出轴转速比，无量纲物理信号

与基座扭矩与从动扭矩之比相关联的物理信号端口，该比值等于从动角速度与基座角速度之比。
### 守恒

### **B** — 基座驱动轴机械旋转

与基座驱动轴相关联的机械旋转守恒端口。

### **F** — 从动驱动轴机械旋转

与从动驱动轴相关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Output shaft rotates
  summary: 输出轴方向与输入轴方向的关系 In same direction as input shaft（默认）| In opposite direction to input shaft
  group: 主要
- name: Transmission stiffness at base (B)
  summary: 基座弹簧刚度系数 5e5 N*m/rad（默认）| 正标量
  group: 柔量
- name: Transmission damping at base (B)
  summary: 基座阻尼系数 5e3 N*m/(rad/s)（默认）| 正标量
  group: 柔量
- name: Initial input torque at base (B)
  summary: 基座处起始扭矩 0 N*m（默认）| 标量
  group: 柔量
- name: Ratio threshold
  summary: 零过渡平滑 0.01（默认）| 标量
  group: 柔量
- name: Losses model
  summary: 可选损耗建模 No losses — Suitable for HIL simulation（默认）| Constant efficiency
  group: 传动损耗
- name: Efficiency
  summary: 基座到从动扭矩传递效率 0.8（默认）| 正标量
  group: 传动损耗
- name: Follower power threshold
  summary: 模块施加满效率损耗的功率点 0.001 W（默认）| 正标量
  group: 传动损耗
- name: Viscous friction coefficients at base (B) and follower (F)
  summary: 基座和从动粘性摩擦向量 [0, 0] N*m/(rad/s)（默认）| 非负元素向量
  group: 粘性损耗
```

### 主要

### **Output shaft rotates** — 输出轴方向与输入轴方向的关系 `In same direction as input shaft`（默认）| `In opposite direction to input shaft`

输出驱动轴相对于输入驱动轴的旋转方向。

### 柔量

### **Transmission stiffness at base (B)** — 基座弹簧刚度系数 `5e5` `N*m/rad`（默认）| 正标量

在基座处测量的传动角柔量倒数
*kp*。

### **Transmission damping at base (B)** — 基座阻尼系数 `5e3` `N*m/(rad/s)`（默认）| 正标量

在基座处测量的传动角柔量阻尼倒数
*kv*。

### **Initial input torque at base (B)** — 基座处起始扭矩 `0` `N*m`（默认）| 标量

仿真开始时施加在基座驱动轴上的扭矩。

### **Ratio threshold** — 零过渡平滑 `0.01`（默认）| 标量

传动比低于此值时模块使用平滑处理。当传动比介于零与 **Ratio threshold** 参数值之间时，模块对传动比进行平滑处理。

### 传动损耗

### **Losses model** — 可选损耗建模 `No losses — Suitable for HIL simulation`（默认）| `Constant efficiency`

非理想扭矩传递中摩擦损耗的实现方式。

- `No losses — Suitable for HIL simulation` —
  扭矩传递为理想情况。
- `Constant efficiency` — 模块通过满足 0 < *η* ≤ 1 的恒定效率
  *η* 来降低齿轮箱扭矩传递。

### **Efficiency** — 基座到从动扭矩传递效率 `0.8`（默认）| 正标量

基座与从动驱动轴之间的有效扭矩传递效率 *η*。

#### 依赖关系

要启用此参数，请将 **Losses model** 设置为
`Constant efficiency`。

### **Follower power threshold** — 模块施加满效率损耗的功率点 `0.001` `W`（默认）| 正标量

从动轴功率的绝对值超过此值时，满效率因子生效。低于此值时，双曲正切函数将效率因子平滑至 1，在无功率传递时将效率损耗降至 0。

作为指导原则，功率阈值应低于仿真期间预期的传递功率。较高的值可能导致模块低估效率损耗。极低的值往往会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **Losses model** 设置为
`Constant efficiency`。

### 粘性损耗

### **Viscous friction coefficients at base (B) and follower (F)** — 基座和从动粘性摩擦向量 `[0, 0]` `N*m/(rad/s)`（默认）| 非负元素向量

分别施加在基座和从动驱动轴上的粘性阻尼系数向量
[*μB*,
*μF*]。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a: 指定零传动比

现在您可以在模块中指定零传动比或连续变化的变号传动比。当传动比为零时，模块不会在端口 **B** 和 **F** 之间传递功率。

## 描述

具有可变且可控传动比、传动柔量和摩擦损耗的动态齿轮箱

Variable Ratio Transmission 模块表示一个齿轮箱，它在两个相连的驱动轴轴线（基座和从动）之间动态传递运动和扭矩。

您可以选择从动轴与基座轴同向旋转还是反向旋转。如果从动轴与基座轴同向旋转，*ωF* 和 *ωB* 具有相同的符号。如果从动轴与基座轴反向旋转，*ωF* 和 *ωB* 具有相反的符号。当输入传动比为正时，输出轴的旋转方向为您指定的方向。当传动比为负时，输出轴沿与输入轴相反的方向旋转。当传动比为零时，两轴脱离啮合，不传递扭矩。

传动柔量在轴运动之间引入内部时间延迟。与齿轮不同，可变传动比变速器不充当运动学约束。您还可以控制由传动损耗和粘性损耗引起的扭矩损失。

### 理想运动和扭矩传递

Variable Ratio Transmission 模块在基座轴和从动轴之间动态传递运动和扭矩。

如果轴之间的相对柔量 *ϕ* 不存在，则该模块等效于具有可变传动比
*gFB(t)* 的齿轮。这种齿轮对两个驱动轴的运动施加时间相关的运动学约束：

ωB=±gFB(t)ωF

τF=±gFB(t)τB

然而，Variable Ratio Transmission 确实包含轴之间的柔量。动态运动和扭矩传递取代了运动学约束，非零的 *ϕ* 通过基座柔量参数 *k*p 和 *k*v 动态响应：

dϕdt=(±gFB(t)ωF−ωB )α−kpkv ϕ(1−α)τB=(−kpϕ(t)−kv(±gFB(t)ωF−ωB))α±gFB(t)τB+τF−τloss=0

其中 *ɑ = 3u2-2u3*，且 u=|gFB(t)|gFB,thr。函数 *α* 实现啮合与脱离状态之间的平滑过渡，传动比阈值 *gFB,thr* 决定启动过渡的传动比幅值。当您将 **Losses model** 设置为 `No losses — Suitable for HIL simulation` 时，*τloss* = 0。

**估算柔量参数**

- 您可以根据传动时间常数 *tc* 和惯量 *J* 估算基座传动刚度 *kp*。

  kp=J(2πtc)2
- 您可以根据传动时间常数 *tc*、惯量 *J* 和阻尼系数 *C* 估算基座传动阻尼 *kv*。

  kv=2Ctc2π=2CJkp

### 非理想扭矩传递和损耗

当您将 **Losses model** 设置为 `Constant efficiency` 时，*τloss* ≠ 0。该模块以类似于非理想齿轮的方式对损耗进行建模。有关非理想齿轮建模的一般信息，请参阅 Model Gears with Losses。

在非理想齿轮箱中，角速度和柔量动力学与理想情况相同。传递的扭矩和功率因以下因素而降低：

- 库仑摩擦，例如皮带与轮之间的摩擦，或由拉伸引起的内部皮带损耗，由效率 *η* 表征。
- 驱动轴与轴承的粘性耦合，由粘性摩擦系数 *μ1* 和 *μ2* 参数化。

扭矩平衡方程中的扭矩损失由库仑摩擦引起，因此

τloss=(1−η)(1+tanh4ppthr2(±gFB(t)τB)+1−tanh4ppthr2τF)

其中 *pthr* 是 **Follower power threshold** 参数。模块将粘性轴摩擦计算为附加到端口 **B** 和 **F** 的内部阻尼扭矩，因此

τdamper,B=μBωBτdamper,F=μFωF

其中总扭矩是 *τB* 或 *τF* 与其各自阻尼扭矩之和。
