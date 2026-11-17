---
type: simulink-block
title: 'Pilot Valve Actuator (IL)'
family: 'hydro'
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
```yaml
ports:
- name: X
  summary: 压力端口 *P*X 等温液体
  direction: conserving
- name: Y
  summary: 压力端口 *P*Y 等温液体
  direction: conserving
- name: S
  summary: 活塞位移，m 物理信号
  direction: output
```

### 守恒端口

### **X** — 压力端口 *P*X 等温液体

端口 **X** 处的压力。没有质量流量通过该端口。

### **Y** — 压力端口 *P*Y 等温液体

端口 **Y** 处的压力。没有质量流量通过该端口。

#### 依赖关系

要启用此端口，请将 **Actuator type** 设置为 `Double-acting`。
### 输出

### **S** — 活塞位移，m 物理信号

活塞位移，指定为物理信号。位移符号对应于 **Mechanical orientation** 参数中指定的方向。
## 参数
```yaml
parameters:
- name: Actuator configuration
  summary: 建模的执行器类型 Single-acting（默认）| Double-acting
  group: ''
- name: Piston area at port X
  summary: 端口 X 处活塞杆的横截面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Piston area at port Y
  summary: 端口 Y 处活塞杆的横截面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Spring preload force
  summary: 中立位置处的力 20 N（默认）| 标量
  group: ''
- name: Spring preload force at port X
  summary: 中立位置处端口 X 的力 20 N（默认）| 标量
  group: ''
- name: Spring preload force at port Y
  summary: 中立位置处端口 Y 的力 20 N（默认）| 标量
  group: ''
- name: Spring stiffness
  summary: 刚度系数 15e3 N/m（默认）| 正标量
  group: ''
- name: Spring stiffness at port X
  summary: 端口 X 处的刚度系数 15e3 N/m（默认）| 正标量
  group: ''
- name: Spring stiffness at port Y
  summary: 端口 Y 处的刚度系数 15e3 N/m（默认）| 正标量
  group: ''
- name: Piston stroke
  summary: 最大活塞行程距离 5e-3 m（默认）| 正标量
  group: ''
- name: Piston stroke from port X
  summary: 端口 X 处的最大活塞行程距离 5e-3 m（默认）| 正标量
  group: ''
- name: Piston stroke from port Y
  summary: 端口 Y 处的最大活塞行程距离 5e-3 m（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Actuator dynamics
  summary: 是否考虑驱动过程中的瞬态 Off（默认）| On
  group: ''
- name: Actuator time constant
  summary: 活塞位移时间常数 0.1 s（默认）| 正标量
  group: ''
- name: Mechanical orientation
  summary: 活塞位移方向 Pilot pressure at port X causes positive piston displacement（默认）| Pilot pressure at port X causes negative
    piston displacement
  group: ''
```

### **Actuator configuration** — 建模的执行器类型 `Single-acting`（默认）| `Double-acting`

建模的执行器类型。

### **Piston area at port X** — 端口 X 处活塞杆的横截面积 `1e-4 m^2`（默认）| 正标量

端口 **X** 处活塞杆的横截面积。

### **Piston area at port Y** — 端口 Y 处活塞杆的横截面积 `1e-4 m^2`（默认）| 正标量

端口 **Y** 处活塞杆的横截面积。

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Double-acting`。

### **Spring preload force** — 中立位置处的力 `20 N`（默认）| 标量

在中立位置处作用于活塞的力。

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Single-acting`。

### **Spring preload force at port X** — 中立位置处端口 X 的力 `20 N`（默认）| 标量

中立位置处端口 **X** 的力。

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Double-acting`。

### **Spring preload force at port Y** — 中立位置处端口 Y 的力 `20 N`（默认）| 标量

中立位置处端口 **Y** 的力。

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Double-acting`。

### **Spring stiffness** — 刚度系数 `15e3 N/m`（默认）| 正标量

弹簧刚度系数。最大弹簧力由刚度 *K* 和 **Spring preload force** 确定：Fmax=Kxstroke+Fpre，

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Single-acting`。

### **Spring stiffness at port X** — 端口 X 处的刚度系数 `15e3 N/m`（默认）| 正标量

端口 **X** 弹簧刚度。最大弹簧力由刚度 *K* 和 **Spring preload force at port X** 确定：Fmax=Kxstroke+Fpre，

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Double-acting`。

### **Spring stiffness at port Y** — 端口 Y 处的刚度系数 `15e3 N/m`（默认）| 正标量

端口 **Y** 弹簧刚度。最大弹簧力由刚度 *K* 和 **Spring preload force at port Y** 确定：Fmax=Kxstroke+Fpre，

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Double-acting`。

### **Piston stroke** — 最大活塞行程距离 `5e-3 m`（默认）| 正标量

最大活塞行程距离。

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Single-acting`。

### **Piston stroke from port X** — 端口 X 处的最大活塞行程距离 `5e-3 m`（默认）| 正标量

端口 **X** 处的最大活塞行程距离。

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Double-acting`。

### **Piston stroke from port Y** — 端口 Y 处的最大活塞行程距离 `5e-3 m`（默认）| 正标量

端口 **Y** 处的最大活塞行程距离。

#### 依赖关系

要启用此参数，请将 **Actuator type** 设置为 `Double-acting`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

### **Actuator dynamics** — 是否考虑驱动过程中的瞬态 `Off`（默认）| `On`

是否考虑驱动引起的滑阀位置瞬态效应。将 **Actuator dynamics** 设置为 `On` 通过引入滑阀位置的一阶滞后来近似执行器运动。**Actuator time constant** 也会影响建模的动力学。

### **Actuator time constant** — 活塞位移时间常数 `0.1 s`（默认）| 正标量

描述活塞从一个位置移动到另一个位置时达到稳态所需时间的常数。此参数影响建模的执行器动力学。

#### 依赖关系

要启用此参数，请将 **Actuator dynamics** 设置为 `On`。

### **Mechanical orientation** — 活塞位移方向 `Pilot pressure at port X causes positive piston displacement`（默认）| `Pilot pressure at port X causes negative piston displacement`

根据端口 **X** 处的配置设置活塞位移方向。如果 **Actuator configuration** 设置为 `Double-acting`，则端口 **Y** 处的位移力方向与端口 **X** 处的力方向相反。`Pilot pressure at port X causes positive piston displacement` 对应于当 **X** 处的压力将活塞推向端口 **Y** 时的正位移。`Pilot pressure at port X causes negative piston displacement` 对应于当 **X** 处的压力将活塞推向端口 **Y** 时的负位移。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

由等温液体网络中的先导压力控制的单作用或双作用执行器

Pilot Valve Actuator (IL) 模块对等温液体网络中由先导压力控制的单作用或双作用执行器进行建模，用于控制连接的阀或节流孔。

对于单作用执行器，当控制压力 *P*X – *P*atm 超过 **Spring preload force at port X** 时，活塞开始沿 **Mechanical orientation** 参数指定的方向运动。

对于双作用执行器，控制压力 *P*control 是 *P*X – *P*atm 与 *P*Y – *P*atm 之间的差值。活塞沿较大施加压差的方向运动，抵抗对侧端口处的弹簧力。当活塞运动反向时，该弹簧不伸展，也不对活塞位置施加平衡力。

端口 **X** 和端口 **Y** 处的活塞连接到一个滑阀上。当 *F*spool 降至对侧弹簧预紧力以下时，两个弹簧将滑阀恢复到其中立位置。对于单作用执行器，中立位置位于端口 **X**。对于双作用执行器，中立位置位于执行器的中心。

### 单作用执行器

活塞上的力由端口 **X** 与大气压力之间的压差产生：

Fspool=(pX−patm)AX，

其中 *A*X 是 **Piston area at port X**。当 *F*spool 大于 **Spring preload force at port X** 时，活塞开始运动。

**单作用执行器示意图**

**活塞位移**

瞬时活塞位移计算如下：

x˙dyn=xsteady−xdynτ，

其中稳态活塞位置 *x*steady 是当前压差下的活塞位置，与最大活塞行程处的弹簧力成正比：

xsteady=Fxstrokeε=Fspool−FpreFmax−Fprexstrokeε，

其中：

- *F*pre 是 **Spring preload force at port X**。
- *F*max 是抵抗活塞位移的最大弹簧力，Fmax=Kxstroke+Fpre，其中 *K* 是 **Spring stiffness at port X**。
- *x*stroke 是 **Piston stroke from port X**。
- *ε* 是 **Mechanical orientation**，表示活塞沿正方向（伸出）或负方向（缩回）运动。

如果活塞上的力小于 **Spring preload force at X**，活塞保持在中立位置或移动到中立位置。如果活塞上的力达到或超过最大弹簧力，活塞保持在行程处，直到施加的压力发生变化。

### 双作用执行器

端口 **X** 和 **Y** 处的力之差决定活塞运动：

Fspool=(pX−patm)AX−(pY−patm)AY。

施加在端口 **X** 处的压力将滑阀推离 **X** 处的腔室，并抵抗端口 **Y** 处的弹簧。类似地，施加在端口 **Y** 处的压力将滑阀推离 **Y** 处的腔室，并抵抗端口 **X** 处的弹簧。当滑阀反向运动时，先前伸展的弹簧压缩，对滑阀施加力。先前压缩的弹簧，即运动方向上端口处的弹簧，不伸展，也不影响滑阀位置。

**双作用执行器示意图**

**活塞位移**

活塞位移计算如下：

x˙dyn=xsteady−xdynτ，

其中稳态活塞位置 *x*steady 是当前压差下的活塞位置，与最大活塞行程处的弹簧力成正比：

xsteady=(FYxstroke,Y−FXxstroke,X)ε=(Fspool−Fpre,YFmax,Y−Fpre,Yxstroke,Y−(−Fspool−Fpre,X)Fmax,X−Fpre,Xxstroke,X)ε，

其中：

- *F*pre,X 和 *F*pre,Y 分别是 **Spring preload force at port X** 和 **Spring preload force at port Y**。
- *F*max,X 和 *F*max,Y 分别是端口 **X** 和 **Y** 处抵抗活塞位移的最大弹簧力，其中：

  Fmax=Kxstroke+Fpre，

  *K* 是每个端口的弹簧刚度。
- *x*stroke 是每个端口的活塞行程。
- *ε* 是 **Mechanical orientation**，将活塞运动信号指定为正（伸出）或负（缩回）。

如果活塞上的力小于相应端口的弹簧预紧力，活塞保持在或返回到中立位置。如果活塞上的力达到或超过相应端口的最大弹簧力，活塞保持在活塞行程处，直到施加的压力发生变化。

### 数值平滑力

当执行器接近完全伸出或完全缩回时，可以通过调整模块的 **Smoothing factor** 来保持仿真的数值鲁棒性。当平滑因子非零时，平滑函数应用于所有计算得到的力，但主要影响活塞运动极限处的仿真。

当 **Actuator configuration** 设置为 `Single-acting` 时，活塞上的归一化力计算如下：

F^X=Fspool−FPreFmax−FPre。

当 **Actuator configuration** 设置为 `Double-acting` 时，**X** 处活塞上的归一化力计算如下：

F^X=−Fspool−FPre,XFmax,X−FPre,X。

**Y** 处的归一化力计算如下：

F^Y=Fspool−FPre,YFmax,Y−FPre,Y。

当 **Smoothing factor** 非零时，模块将每个归一化力平滑到 `0` 和 `1` 之间。

有关详细信息，请参阅数值平滑。
