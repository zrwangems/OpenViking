---
type: simulink-block
title: 'Gate Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'gatevalveil'
documentation_source_path: 'ref/gatevalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Gate Valve (IL)

## 端口
```yaml
ports:
- name: S
  summary: 闸门位移，m 物理信号
  direction: input
- name: A
  summary: 液体端口 等温液体
  direction: input
- name: B
  summary: 液体端口 等温液体
  direction: input
```

### 输入

### **S** — 闸门位移，m 物理信号

与阀门闸门位移相关联的物理信号端口，单位为
m。正信号使闸门回缩并打开阀门。
### 守恒

### **A** — 液体端口 等温液体

与阀门入口 A 相关联的等温液体守恒端口。

### **B** — 液体端口 等温液体

与阀门入口
B 相关联的等温液体守恒端口。
## 参数
```yaml
parameters:
- name: Valve orifice diameter
  summary: 孔口直径 5e-3 m^2（默认）| 正标量
  group: ''
- name: Gate position when fully covering orifice
  summary: 闸门偏移 0 m（默认）| 正标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的孔口面积 inf m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Pressure recovery
  summary: 是否考虑面积扩大中的压力增加 off（默认）| on
  group: ''
```

### **Valve orifice diameter** — 孔口直径 `5e-3` `m^2`（默认）| 正标量

阀门开启面积直径。

### **Gate position when fully covering orifice** — 闸门偏移 `0` `m`（默认）| 正标量

阀门关闭时的闸门偏移。正的、非零值表示当端口 **S** 处的信号为 0 时阀门部分开启。
负的、非零值表示重叠阀门，该阀门在端口
**S** 处的物理信号设定的初始正位移范围内保持关闭。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会被饱和到指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

### **Cross-sectional area at ports A and B** — 守恒端口处的孔口面积 `inf` `m^2`（默认）| 正标量

入口和出口端口 **A** 和
**B** 处的面积，用于确定通过孔口的质量流率的压力-流率方程中。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀门处于接近开启或接近关闭位置时，为流动响应引入一层渐变变化。

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `off`（默认）| `on`

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

等温液体系统中的闸阀

Gate Valve (IL) 模块表示等温液体网络中闸阀的流量控制。该阀门包括一个圆形、锐边孔口和一个直径相同的圆形闸门。闸门根据端口 **S** 处的位移信号打开或关闭。正信号使闸门回缩并打开阀门。

### 开启面积

**闸阀开启示意图**

闸门回缩时开放流动的面积为：

Aopen=πd024−Ashielded，

其中 *d*0 是
**Valve orifice diameter**。部分开启阀门中闸门遮蔽的面积为：

Ashielded=d022cos−1(Δld0)−Δl2d02−(Δl)2，

其中 *Δl* 是闸门位移，它是端口 **S** 处的信号与 **Gate position
when fully covering orifice** 之和。

如果位移超过 **Orifice diameter**，阀门面积
*A*open 为最大
孔口面积与 **Leakage area** 之和：

Aopen=π4d02+Aleak。

对于端口 **S** 处的信号
与闸门偏移的任何小于 0 的组合，最小阀门面积为
**Leakage area**。

### 数值平滑位移

当阀门处于接近开启或接近关闭位置时，
您可以通过调整
**Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing
factor** 参数非零，模块会在 `0` 和 **Valve orifice
diameter** 参数之间平滑地饱和闸门
位移。有关详细信息，请参阅 Numerical Smoothing。

### 质量流率方程

通过阀门的质量守恒：

m˙A+m˙B=0。

通过阀门的质量流率计算为：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *C*d 是
  **Discharge coefficient**。
- *A*valve 是阀门开启
  面积。
- *A*port 是
  **端口 A 和 B 处的横截面积**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差
  *p*A –
  *p*B。

临界压差，
*Δp*crit，是与 **Critical Reynolds number**、
*Re*crit 相关联的压差，它是层流和湍流之间的流态
过渡点：

Δpcrit=πρ¯8Avalve(νRecritCd)2。

*Pressure loss* 描述了由于面积减小而导致阀门中压力的降低。*PR*loss
计算为：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

*Pressure recovery* 描述了由于面积增加而导致阀门中压力的正向变化。如果您不想捕获这种压力增加，
请清除 **Pressure recovery** 复选框。在这种情况下，
*PR*loss 为 1。
