---
type: simulink-block
title: 'Gate Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'gatevalvetl'
documentation_source_path: 'ref/gatevalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Gate Valve (TL)

## 端口
```yaml
ports:
- name: S
  summary: 闸门位移，m 物理信号
  direction: input
- name: A
  summary: 液体端口 热液体
  direction: input
- name: B
  summary: 液体端口 热液体
  direction: input
```

### 输入

### **S** — 闸门位移，m 物理信号

与阀门闸门位移相关联的物理信号端口，单位为
m。正信号使闸门缩回并打开阀门。
### 守恒

### **A** — 液体端口 热液体

与阀门入口 A 相关联的热液体守恒端口。

### **B** — 液体端口 热液体

与阀门入口 B 相关联的热液体守恒端口。
## 参数
```yaml
parameters:
- name: Orifice diameter
  summary: 孔口直径 0.01 m（默认）| 正标量
  group: ''
- name: Gate position when fully covering orifice
  summary: 闸门偏移 0 m（默认）| 非负标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的孔口面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
```

### **Orifice diameter** — 孔口直径 `0.01` `m`（默认）| 正标量

阀门开启面积直径。

### **Gate position when fully covering orifice** — 闸门偏移 `0` `m`（默认）| 非负标量

阀门关闭时的闸门偏移。一个正的、非零值表示当端口 **S** 处的信号为 0 时阀门部分开启。
一个负的、非零值表示重叠的阀门，在端口 **S** 处的物理信号设定的初始正位移范围内保持关闭。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。该模块将较小的数值饱和到此值。该参数通过保持流动的连续性来贡献数值稳定性。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的标量

连续平滑因子，当阀门处于接近开启或接近关闭位置时，为流量响应引入一层渐变变化。

### **Cross-sectional area at ports A and B** — 守恒端口处的孔口面积 `0.01` `m^2`（默认）| 正标量

入口和出口端口 **A** 和
**B** 处的面积，用于确定通过孔口的质量流量的压力-流量方程中。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

考虑理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

热液体系统中的闸阀

Gate Valve (TL) 模块表示热液体网络中的闸阀。该阀门包括一个圆形、锐边孔口和一个直径相同的圆形闸门。闸门根据端口 **S** 处的位移信号打开或关闭。正信号提升闸门以打开阀门。该图显示了开启面积与闸门净位移之间的关系。

显示开启面积与闸门净位移之间关系的图。

平滑函数允许阀门开启面积在完全关闭和完全开启位置之间平滑变化。平滑函数减少了在零和最大闸门位置处的突然开启面积变化。

### 质量平衡

阀门中的质量守恒方程为

m˙A+m˙B=0，

其中：

- m˙A 是通过端口
  **A** 进入阀门的质量流量。
- m˙B 是通过端口
  **B** 进入阀门的质量流量。

### 动量平衡

阀门中的动量守恒方程为

pA−pB=m˙m˙2+m˙cr22ρAvgCd2S2[1−(SRS)2]PRLoss，

其中：

- *p*A 和
  *p*B 是端口 **A** 和端口 **B** 处的压力。
- m˙ 是质量流量。
- m˙cr 是临界质量流量：

  m˙cr=RecrμAvgπ4SR。
- *ρ*Avg 是平均液体
  密度。
- *C*d 是流量
  系数。
- *S* 是阀门入口面积。
- *PR*Loss 是压力比：

  PRLoss=1−(SR/S)2(1−Cd2)−Cd(SR/S)1−(SR/S)2(1−Cd2)+Cd(SR/S)。

### 能量平衡

阀门中的能量守恒方程为

ϕA+ϕB=0，

其中：

- *ϕ*A 是通过端口 **A**
  进入阀门的能量流量。
- *ϕ*B 是通过端口 **B**
  进入阀门的能量流量。

### 阀门开启面积

该模块使用以下表达式计算阀门开启面积

A=πd024−ACovered+Aleak，

其中：

- *A* 是阀门开启面积。
- *Aleak* 是
  **Leakage area** 参数的值。
- *d*0 是阀门孔口
  直径。
- *A*Covered 是阀门孔口面积中被闸门覆盖的部分：

  ACovered=d022acos(Δld0)−Δl2d02−(Δl)2。
- *Δl* 是闸门中心相对于孔口中心的净位移。

  Δl={0,(Sd−Smin)≤0d0,(Sd−Smin)≥d0(Sd−Smin),Else
- *S*min 是在模块对话框中指定的
  **Gate position when fully covering orifice**
  参数的值。
- *S*d 是通过物理信号输入端口 S 指定的闸门位移。

### 数值平滑位移

当阀门处于接近开启或接近关闭位置时，
您可以通过调整
**Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing
factor** 参数非零，该模块在 `0` 和 **Valve orifice
diameter** 参数之间平滑地饱和闸门位移。有关更多信息，请参阅数值平滑。
