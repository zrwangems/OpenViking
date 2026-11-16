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

### 输入

### **r** — 输入到输出轴速度比，无单位物理信号

与基座到从动件扭矩之比关联的物理信号端口，该比值等于从动件到基座角速度之比。

### 守恒

### **B** — 基座驱动轴机械旋转

与基座驱动轴关联的机械旋转守恒端口。

### **F** — 从动件驱动轴机械旋转

与从动件驱动轴关联的机械旋转守恒端口。

## 参数

### 主要

### **Output shaft rotates** — 输出轴方向相对于输入轴方向 `In same direction as input shaft`（默认） | `In opposite direction to input shaft`

输出驱动轴相对于输入驱动轴的旋转。

### 柔顺性

### **Transmission stiffness at base (B)** — 基座弹簧刚度系数 `5e5` `N*m/rad`（默认） | 正标量

在基座处测量的传动角度柔顺性 *kp* 的倒数。

### **Transmission damping at base (B)** — 基座阻尼系数 `5e3` `N*m/(rad/s)`（默认） | 正标量

在基座处测量的传动角度柔顺性阻尼 *kv* 的倒数。

### **Initial input torque at base (B)** — 基座启动扭矩 `0` `N*m`（默认） | 标量

仿真开始时施加在基座驱动轴上的扭矩。

### **Ratio threshold** — 零过渡平滑 `0.01`（默认） | 标量

传动比低于该值时，模块使用平滑处理。当比率介于零和 **Ratio threshold** 参数值之间时，模块对传动比进行平滑处理。

### 传动损失

### **Losses model** — 可选损失建模 `No losses — Suitable for HIL simulation`（默认） | `Constant efficiency`

非理想扭矩传递中摩擦损失的实现。

- `No losses — Suitable for HIL simulation` —
  扭矩传递是理想的。
- `Constant efficiency` — 模块以恒定效率
  *η* 降低齿轮箱扭矩传递，满足 0 < *η* ≤ 1。

### **Efficiency** — 基座到从动件扭矩传递效率 `0.8`（默认） | 正标量

基座与从动件驱动轴之间的有效扭矩传递效率 *η*。

#### 依赖关系

要启用此参数，请将 **Losses model** 设置为
`Constant efficiency`。

### **Follower power threshold** — 模块施加完整效率损失的功率点 `0.001` `W`（默认） | 正标量

从动轴功率的绝对值，高于该值时完整效率因子生效。低于该值时，双曲正切函数将效率因子平滑至 1，从而在没有功率传递时将效率损失降至 0。

作为指导原则，功率阈值应低于仿真期间预期的传递功率。较高的值可能导致模块低估效率损失。非常低的值往往会提高仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **Losses model** 设置为
`Constant efficiency`。

### 粘性损失

### **Viscous friction coefficients at base (B) and follower (F)** — 基座和从动件粘性摩擦向量 `[0, 0]` `N*m/(rad/s)`（默认） | 非负元素向量

分别施加在基座和从动件驱动轴上的粘性阻尼系数向量
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

### R2025a：指定零比率

现在可以在模块中指定零比率或可连续变化且会改变符号的比率。当比率为零时，模块不会在端口 **B** 和 **F** 之间传递功率。

## 描述

具有可变且可控传动比、传动柔顺性和摩擦损失的动态齿轮箱

Variable Ratio Transmission 模块表示一个齿轮箱，该齿轮箱在两个相连的驱动轴轴线（基座和从动件）之间动态传递运动和扭矩。

您可以选择从动轴是与基座轴同向旋转还是反向旋转。如果从动轴和基座轴同向旋转，则 *ωF* 和 *ωB* 具有相同符号。如果从动轴和基座轴反向旋转，则 *ωF* 和 *ωB* 具有相反符号。当输入比率为正时，输出轴的旋转方向为您指定的方向。当比率为负时，输出轴沿与输入轴相反的方向旋转。当比率为零时，两轴脱离，不传递扭矩。

传动柔顺性在轴运动之间引入内部时间延迟。与齿轮不同，可变传动比传动不会充当运动学约束。您还可以控制由传动损失和粘性损失引起的扭矩损失。

### 理想运动和扭矩传递

Variable Ratio Transmission 模块在基座轴和从动轴之间动态传递运动和扭矩。

如果轴之间的相对柔顺性 *ϕ* 不存在，则该模块等效于具有可变比率 *gFB(t)* 的齿轮。这样的齿轮对两个驱动轴的运动施加时间相关的运动学约束：

ωB=±gFB(t)ωF

τF=±gFB(t)τB

然而，Variable Ratio Transmission 确实包含轴之间的柔顺性。动态运动和扭矩传递取代了运动学约束，非零 *ϕ* 通过基座柔顺性参数 *k*p 和 *k*v* 动态响应：

dϕdt=(±gFB(t)ωF−ωB )α−kpkv ϕ(1−α)τB=(−kpϕ(t)−kv(±gFB(t)ωF−ωB))α±gFB(t)τB+τF−τloss=0

其中 *ɑ = 3u2-2u3*，且 u=|gFB(t)|gFB,thr。函数 *α* 可实现接合状态与分离状态之间的平滑过渡，比率阈值 *gFB,thr* 确定用于启动过渡的比率大小。当您将 **Losses model** 设置为 `No losses — Suitable for HIL simulation` 时，*τloss* = 0。

**估计柔顺性参数**

- 您可以根据传动时间常数 *tc* 和惯量 *J* 估计基座传动刚度 *kp*。

  kp=J(2πtc)2
- 您可以根据传动时间常数 *tc*、惯量 *J* 和阻尼系数 *C* 估计基座传动阻尼 *kv*。

  kv=2Ctc2π=2CJkp

### 非理想扭矩传递和损失

当您将 **Losses model** 设置为 `Constant efficiency` 时，*τloss* ≠ 0。模块以与非理想齿轮类似的方式对损失建模。有关非理想齿轮建模的一般信息，请参阅 Model Gears with Losses。

在非理想齿轮箱中，角速度和柔顺性动力学与理想情况相同。传递的扭矩和功率因以下因素而降低：

- 库仑摩擦，例如皮带与轮之间的摩擦，或由于拉伸造成的内部皮带损失，由效率 *η* 表征。
- 驱动轴与轴承的粘性耦合，由粘性摩擦系数 *μ1* 和 *μ2* 参数化。

扭矩平衡方程中的扭矩损失由库仑摩擦引起，因此

τloss=(1−η)(1+tanh4ppthr2(±gFB(t)τB)+1−tanh4ppthr2τF)

其中 *pthr* 是 **Follower power threshold** 参数。模块将粘性轴摩擦计算为连接到端口 **B** 和 **F** 的内部阻尼扭矩，因此

τdamper,B=μBωBτdamper,F=μFωF

其中总扭矩是 *τB* 或 *τF* 与其各自阻尼扭矩之和。
