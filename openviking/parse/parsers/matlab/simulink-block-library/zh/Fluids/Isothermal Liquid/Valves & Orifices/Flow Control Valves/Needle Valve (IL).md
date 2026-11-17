---
type: simulink-block
title: 'Needle Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'needlevalveil'
documentation_source_path: 'ref/needlevalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Needle Valve (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口，等温液体
  direction: conserving
- name: B
  summary: 液体端口，等温液体
  direction: conserving
- name: S
  summary: 针阀位移，m，物理信号
  direction: input
```

### 守恒端口

### **A** — 液体端口，等温液体

阀的液体入口或出口端口。

### **B** — 液体端口，等温液体

阀的液体入口或出口端口。
### 输入

### **S** — 针阀位移，m，物理信号

控制构件位移，单位为 m，指定为物理信号。正信号使针阀缩回并打开阀门。
## 参数
```yaml
parameters:
- name: Seat orifice diameter
  summary: 阀座孔径 5e-3 m（默认）| 正标量
  group: ''
- name: Needle cone angle
  summary: 控制构件几何角度 90 deg（默认）| 正标量
  group: ''
- name: Needle position when in the seat
  summary: 针阀偏移 0 m（默认）| 标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的面积 inf m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的正标量
  group: ''
- name: Pressure recovery
  summary: 是否考虑面积扩大时的压力增加 off（默认）| on
  group: ''
```

### **Seat orifice diameter** — 阀座孔径 `5e-3 m`（默认）| 正标量

阀座孔口的直径。

### **Needle cone angle** — 控制构件几何角度 `90 deg`（默认）| 正标量

控制构件几何角度。请参阅阀门描述中的针阀示意图。

### **Needle position when in the seat** — 针阀偏移 `0 m`（默认）| 标量

阀门关闭时的针阀偏移。正的、非零值表示阀门部分打开。负的、非零值表示重叠阀，该阀在由端口 **S** 处的物理信号设定的初始位移范围内保持关闭。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会被饱和到指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过阀门的质量流率的压力-流率方程中。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流动响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高在这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的针阀

Needle Valve (IL) 模块对针阀的流动减少进行建模。该阀包括一个锥形针阀和一个圆形、锐边阀座。针阀根据端口 **S** 处的位移信号打开或关闭。正信号使针阀缩回并打开阀门。

### 开口面积

**针阀示意图**

**针阀俯视图**

阀的开口面积计算如下：

Aopen=πhsin(θ2)[d0−h2sin(θ)]+Aleak，

其中：

- *h* 是针阀外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是阀座锥角，始终与 **Needle cone angle** 匹配。
- *d*0 是 **Seat orifice diameter**。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=d0[1−1−cos(θ2)]sin(θ)。

对于任何大于 *h*max 的针阀位移，*A*open 是最大孔口面积与 **Leakage area** 之和：

Aopen=π4d02+Aleak。

对于端口 **S** 处的信号与针阀偏移的任何小于 0 的组合，最小阀面积为 **Leakage area**。

如果 **Smoothing factor** 参数非零，模块会在 `0` 和 *h*max 之间平滑地饱和位移。有关更多信息，请参阅数值平滑。

### 质量流率方程

通过阀门的质量守恒：

m˙A+m˙B=0。

通过阀门的质量流率计算如下：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *C*d 是 **Discharge coefficient**。
- *A*valve 是瞬时阀门开口面积。
- *A*port 是 **Cross-sectional area at ports A and B**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差 *p*A – *p*B。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 相关的压差，即层流与湍流之间的流态转变点：

Δpcrit=πρ¯8Avalve(νRecritCd)2。

*压力损失* 描述了由于面积减小而导致的阀门压力降低。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

*压力恢复* 描述了由于面积增加而导致的阀门正压力变化。如果您不希望捕获此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。
