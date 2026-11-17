---
type: simulink-block
title: 'Pilot Valve Actuator (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces'
documentation_page: 'pilotvalveactuatoril'
documentation_source_path: 'ref/pilotvalveactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Pilot Valve Actuator (IL)

## 端口

### 守恒

### **X** — 压力端口 *P*X 等温液体

端口 **X** 处的压力。没有质量流量通过该端口。

### **Y** — 压力端口 *P*Y 等温液体

端口 **Y** 处的压力。没有质量流量通过该端口。

#### 依赖关系

要启用此端口，请将 **执行器类型** 设置为 `Double-acting`。
### 输出

### **S** — 活塞位移，m physical signal

活塞位移，指定为 physical signal。位移符号对应于 **机械方向** 参数中指定的方向。

## 参数

### **执行器配置** — 所建模的执行器类型 `Single-acting`（默认） | `Double-acting`

所建模的执行器类型。

### **端口 X 处的活塞面积** — 端口 X 处活塞杆的横截面积 `1e-4 m^2`（默认） | positive scalar

端口 **X** 处活塞杆的横截面积。

### **端口 Y 处的活塞面积** — 端口 Y 处活塞杆的横截面积 `1e-4 m^2`（默认） | positive scalar

端口 **Y** 处活塞杆的横截面积。

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Double-acting`。

### **弹簧预紧力** — 中性位置处的力 `20 N`（默认） | scalar

在中性位置处作用在活塞上的力。

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Single-acting`。

### **端口 X 处的弹簧预紧力** — 中性位置处端口 X 的力 `20 N`（默认） | scalar

中性位置处端口 **X** 的力。

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Double-acting`。

### **端口 Y 处的弹簧预紧力** — 中性位置处端口 Y 的力 `20 N`（默认） | scalar

中性位置处端口 **Y** 的力。

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Double-acting`。

### **弹簧刚度** — 刚度系数 `15e3 N/m`（默认） | positive scalar

弹簧刚度系数。最大弹簧力由刚度 *K* 和 **弹簧预紧力** 确定：Fmax=Kxstroke+Fpre,

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Single-acting`。

### **端口 X 处的弹簧刚度** — 端口 X 处的刚度系数 `15e3 N/m`（默认） | positive scalar

端口 **X** 弹簧刚度。最大弹簧力由刚度 *K* 和 **端口 X 处的弹簧预紧力** 确定：Fmax=Kxstroke+Fpre,

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Double-acting`。

### **端口 Y 处的弹簧刚度** — 端口 Y 处的刚度系数 `15e3 N/m`（默认） | positive scalar

端口 **Y** 弹簧刚度。最大弹簧力由刚度 *K* 和 **端口 Y 处的弹簧预紧力** 确定：Fmax=Kxstroke+Fpre,

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Double-acting`。

### **活塞行程** — 最大活塞行进距离 `5e-3 m`（默认） | positive scalar

最大活塞行进距离。

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Single-acting`。

### **端口 X 处的活塞行程** — 端口 X 处的最大活塞行进距离 `5e-3 m`（默认） | positive scalar

端口 **X** 处的最大活塞行进距离。

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Double-acting`。

### **端口 Y 处的活塞行程** — 端口 Y 处的最大活塞行进距离 `5e-3 m`（默认） | positive scalar

端口 **Y** 处的最大活塞行进距离。

#### 依赖关系

要启用此参数，请将 **执行器类型** 设置为 `Double-acting`。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | positive scalar in the range [0,1]

连续平滑因子，当阀处于接近打开或接近关闭位置时，它为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **执行器动态** — 是否考虑致动过程中的瞬态 `Off`（默认） | `On`

是否考虑由致动引起的阀芯位置瞬态效应。将 **执行器动态** 设置为 `On` 会通过在阀芯位置中引入一阶滞后来近似执行器运动。**执行器时间常数** 也会影响所建模的动态。

### **执行器时间常数** — 活塞位移时间常数 `0.1 s`（默认） | positive scalar

该常数表示活塞从一个位置移动到另一个位置时达到稳态所需的时间。此参数会影响所建模的执行器动态。

#### 依赖关系

要启用此参数，请将 **执行器动态** 设置为 `On`。

### **机械方向** — 活塞位移方向 `Pilot pressure at port X causes positive piston displacement`（默认） | `Pilot pressure at port X causes negative piston displacement`

根据端口 **X** 处的配置设置活塞位移方向。如果 **执行器配置** 设置为 `Double-acting`，则端口 **Y** 处的位移力作用方向与端口 **X** 处的力相反。`Pilot pressure at port X causes positive piston displacement` 对应于当 **X** 处的压力将活塞推向端口 **Y** 时的正位移。`Pilot pressure at port X causes negative piston displacement` 对应于当 **X** 处的压力将活塞推向端口 **Y** 时的负位移。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

在等温液体网络中由先导压力控制的单作用或双作用执行器

Pilot Valve Actuator (IL) 模块对由先导压力控制的单作用或双作用执行器进行建模，用于控制等温液体网络中的连接阀或节流孔。

对于单作用执行器，当控制压力 *P*X – *P*atm 超过 **端口 X 处的弹簧预紧力** 时，活塞开始沿 **机械方向** 参数指定的方向运动。

对于双作用执行器，控制压力 *P*control 是 *P*X – *P*atm 与 *P*Y – *P*atm 之间的差值。活塞沿所施加压力差较大的方向运动，并抵抗对侧端口处的弹簧力。当活塞运动反向时，该弹簧不会伸展，也不会对活塞位置施加平衡力。

端口 **X** 和端口 **Y** 处的活塞连接到一个阀芯。当 *F*spool 降至对侧弹簧预紧力以下时，两个弹簧都将阀芯恢复到其中性位置。对于单作用执行器，中性位置位于端口 **X**。对于双作用执行器，中性位置位于执行器的中心。

### 单作用执行器

活塞上的力由端口 **X** 与大气压力之间的压力差产生：

Fspool=(pX−patm)AX,

其中 *A*X 是 **端口 X 处的活塞面积**。当 *F*spool 大于 **端口 X 处的弹簧预紧力** 时，活塞开始移动。

**单作用执行器示意图**

**活塞位移**

瞬时活塞位移计算为：

x˙dyn=xsteady−xdynτ,

其中稳态活塞位置 *x*steady 是在当前压力差下的活塞位置，与最大活塞行程处的弹簧力成比例：

xsteady=Fxstrokeε=Fspool−FpreFmax−Fprexstrokeε,

其中：

- *F*pre 是 **端口 X 处的弹簧预紧力**。
- *F*max 是抵抗活塞位移的最大弹簧力，Fmax=Kxstroke+Fpre，其中 *K* 是 **端口 X 处的弹簧刚度**。
- *x*stroke 是 **端口 X 处的活塞行程**。
- *ε* 是 **机械方向**，它表示活塞沿正方向（伸出）或负方向（缩回）运动。

如果活塞上的力小于 **X 处的弹簧预紧力**，则活塞保持在中性位置或移动到中性位置。如果活塞上的力达到或超过最大弹簧力，则活塞保持在行程处，直到所施加的压力发生变化。

### 双作用执行器

端口 **X** 和 **Y** 处力之间的差值决定活塞运动：

Fspool=(pX−patm)AX−(pY−patm)AY.

施加在端口 **X** 处的压力使阀芯远离 **X** 处的腔室，并抵抗端口 **Y** 处的弹簧。类似地，施加在端口 **Y** 处的压力使阀芯远离 **Y** 处的腔室，并抵抗端口 **X** 处的弹簧。当阀芯反向运动时，先前伸展的弹簧压缩，对阀芯施加力。先前压缩的弹簧，即运动方向所在端口处的弹簧，不会伸展，也不会影响阀芯位置。

**双作用执行器示意图**

**活塞位移**

活塞位移计算为：

x˙dyn=xsteady−xdynτ,

其中稳态活塞位置 *x*steady 是在当前压力差下的活塞位置，与最大活塞行程处的弹簧力成比例：

xsteady=(FYxstroke,Y−FXxstroke,X)ε=(Fspool−Fpre,YFmax,Y−Fpre,Yxstroke,Y−(−Fspool−Fpre,X)Fmax,X−Fpre,Xxstroke,X)ε,

其中：

- *F*pre,X 和 *F*pre,Y 分别是 **端口 X 处的弹簧预紧力** 和 **端口 Y 处的弹簧预紧力**。
- *F*max,X 和 *F*max,Y 分别是作用在端口 **X** 和 **Y** 处抵抗活塞位移的最大弹簧力，其中：

  Fmax=Kxstroke+Fpre,

  *K* 是每个端口的弹簧刚度。
- *x*stroke 是每个端口的活塞行程。
- *ε* 是 **机械方向**，它将活塞运动的信号指定为正（伸出）或负（缩回）。

如果活塞上的力小于相应端口的弹簧预紧力，则活塞保持在中性位置或返回到中性位置。如果活塞上的力达到或超过相应端口的最大弹簧力，则活塞保持在活塞行程处，直到所施加的压力发生变化。

### 数值平滑力

当执行器接近完全伸出或完全缩回时，可以通过调整模块 **平滑因子** 来保持仿真中的数值稳健性。当平滑因子非零时，会对所有计算得到的力应用平滑函数，但主要影响活塞运动极端位置处的仿真。

当 **执行器配置** 设置为 `Single-acting` 时，活塞上的归一化力计算为：

F^X=Fspool−FPreFmax−FPre.

当 **执行器配置** 设置为 `Double-acting` 时，**X** 处活塞上的归一化力计算为：

F^X=−Fspool−FPre,XFmax,X−FPre,X.

而 **Y** 处的归一化力计算为：

F^Y=Fspool−FPre,YFmax,Y−FPre,Y.

当 **平滑因子** 非零时，模块会在 `0` 和 `1` 之间对每个归一化力进行平滑。

有关更多信息，请参阅数值平滑。
