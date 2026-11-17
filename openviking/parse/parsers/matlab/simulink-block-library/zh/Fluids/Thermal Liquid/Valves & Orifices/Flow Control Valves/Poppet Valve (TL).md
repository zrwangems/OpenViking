---
type: simulink-block
title: 'Poppet Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'poppetvalvetl'
documentation_source_path: 'ref/poppetvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Poppet Valve (TL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口 thermal liquid
  direction: conserving
- name: B
  summary: 液体端口 thermal liquid
  direction: conserving
- name: S
  summary: 阀芯位移，m physical signal
  direction: input
```

### 守恒端口

### **A** — 液体端口 thermal liquid

与阀入口 A 关联的热液体守恒端口。

### **B** — 液体端口 thermal liquid

与阀入口 B 关联的热液体守恒端口。

### 输入

### **S** — 阀芯位移，m physical signal

与阀芯位移关联的物理信号端口，单位为 m。
## 参数
```yaml
parameters:
- name: Valve seat specification
  summary: 阀座几何形状 Sharp-edged（默认）| Conical
  group: ''
- name: Cone angle
  summary: 阀座开口角度 120 deg（默认）| 正标量
  group: ''
- name: Ball diameter
  summary: 阀芯直径 0.01 m（默认）| 正标量
  group: ''
- name: Orifice diameter
  summary: 阀座孔口直径 7e-3 m（默认）| 正标量
  group: ''
- name: Poppet position when in the seat
  summary: 阀芯偏移量 0 m（默认）| 非负标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 完全关闭位置时的间隙面积 0.01（默认）| 范围 [0,1] 内的标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
```

### **Valve seat specification** — 阀座几何形状 `Sharp-edged`（默认）| `Conical`

阀座的几何形状。模块使用此参数计算阀芯与阀座之间的开口面积。

### **Cone angle** — 阀座开口角度 `120` `deg`（默认）| 正标量

阀座开口的角度。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Conical`。

### **Ball diameter** — 阀芯直径 `0.01` `m`（默认）| 正标量

阀芯的直径。

### **Orifice diameter** — 阀座孔口直径 `7e-3` `m`（默认）| 正标量

阀座孔口直径。

### **Poppet position when in the seat** — 阀芯偏移量 `0` `m`（默认）| 非负标量

阀关闭时的阀芯偏移量。正的、非零值表示阀部分开启。负的、非零值表示重叠阀，该阀在由端口 **S** 处物理信号设定的初始位移范围内保持关闭。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。模块将较小的数值饱和到此值。此参数通过保持流量连续性来帮助提高数值稳定性。

### **Smoothing factor** — 完全关闭位置时的间隙面积 `0.01`（默认）| 范围 [0,1] 内的标量

连续平滑因子，在阀处于接近开启或接近关闭位置时引入一层流量响应的渐变变化。将此值设置为小于 1 的非零数值，以提高在这些工况下仿真的稳定性。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `0.01` `m^2`（默认）| 正标量

端口 **A** 和 **B** 处的面积，用于确定通过阀的质量流量的压力-流量速率方程。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

热液体网络中的阀芯流量控制阀

Poppet Valve (TL) 模块表示热液体网络中的流量控制。您可以将阀座几何形状指定为锐边或锥形。使用端口 **S** 处的物理信号设置阀芯位移。

两个阀芯阀示意图。锐边阀座具有 90 度阀座角。锥形阀座具有锐角阀座角。正位移是指阀芯远离阀座移动。

### 质量平衡

阀中的质量守恒方程为

m˙A+m˙B=0,

其中：

- m˙A 是通过端口 **A** 流入阀的质量流量。
- m˙B 是通过端口 **B** 流入阀的质量流量。

### Momentum Balance

阀门上的压差为：

pA−pB=m˙m˙2+m˙cr22ρAvgCd2S2[1−(SRS)2]PRLoss，

其中：

- *p*A 是端口 **A** 处的压力。
- *p*B 是端口 **B** 处的压力。
- m˙ 是质量流量。
- *ρ*Avg 是平均液体密度。
- *C*d 是 **Discharge coefficient** 参数的值。
- m˙cr 是临界质量流量：

  m˙cr=RecrμAvgπ4SR。

  其中：

  - *Recr* 是 **Critical Reynolds number** 参数的值。
  - *μAvg* 是平均流体动力粘度。
- *S* 是 **Cross-sectional area at port A and B** 参数的值。
- *PR*Loss 是压力比：

  PRLoss=1−(SR/S)2(1−Cd2)−Cd(SR/S)1−(SR/S)2(1−Cd2)+Cd(SR/S)。

### Energy Balance

阀门中的能量守恒方程为

ϕA+ϕB=0，

其中：

- *ϕ*A 是通过端口 **A** 流入阀门的能量流率。
- *ϕ*B 是通过端口 **B** 流入阀门的能量流率。

### Opening Area With a Sharp-Edged Seat

当您将 **Valve seat specification** 设置为 `Sharp-edged` 时，该模块使用以下公式计算阀门开口面积

A=πro(1−(rpdOB)2)dOB(h)+Aleak，

其中：

- *r*o 是阀孔半径。
- *r*p 是阀锥半径。
- *d*OB(*h*) 是阀锥中心与孔边缘之间的距离。该距离是阀门升程 *h* 的函数。
- *Aleak* 是泄漏面积。

最大位移 *h*max 为

hmax=2rp2−ro2+roro2+4rp22−rp2−ro2。

该图显示了锐边阀座的示意图。

锐边阀座的示意图。

### Opening Area With a Conical Seat

当您将 **Valve seat specification** 设置为 `Conical` 时，该模块使用几何关系计算阀门开口面积，使得

A=πrpsin(θ)h+π2sin(θ2)sin(θ)h2+Aleak。

最大位移 *h*max 为：

hmax=rp2+ro2cos(θ2)−rpsin(θ2)，

其中 *θ* 是 **Cone angle**。该图显示了锥形阀座的示意图。

锥形阀座的示意图。

### Numerically Smoothed Displacement

该模块计算阀锥位移 *h*，使得

h={0,(S−Smin)≤0hMax,(S−Smin)≥hMax(S−Smin),Else

其中：

- *S* 是物理信号输入。
- *Smin* 是 **Poppet position when in the seat** 参数。
- *hMax* 是最大位移。

如果 **Smoothing factor** 参数非零，则该模块在 `0` 和 *hMax* 之间平滑饱和阀锥位移。

有关详细信息，请参阅 Numerical Smoothing。
