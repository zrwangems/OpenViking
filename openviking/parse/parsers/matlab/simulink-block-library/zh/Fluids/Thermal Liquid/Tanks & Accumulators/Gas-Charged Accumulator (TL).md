---
type: simulink-block
title: 'Gas-Charged Accumulator (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Tanks & Accumulators'
documentation_page: 'gaschargedaccumulatortl'
documentation_source_path: 'ref/gaschargedaccumulatortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Gas-Charged Accumulator (TL)

## 端口

### 守恒端口

### **A** — 液体端口（热液体）

与蓄能器入口相关联的热液体守恒端口。
如果液体流入蓄能器，则流量为正。

### **H** — 热端口（热）

与液体体积热质量相关联的热守恒端口。

## 参数

### **Total accumulator volume** — 蓄能器体积 `8e-3` `m^3`（默认）| 正标量

蓄能器的总体积，包括液体腔和气体腔。这是液体腔容量与最小气体体积之和。

### **Minimum gas volume** — 气体腔死区体积 `4e-5` `m^3`（默认）| 正标量

气体腔死区体积。这是液体腔充满时剩余的气体量。必须为非零体积，以便液体腔充满时气体压力不会变为无穷大。

### **Precharge pressure (gauge)** — 气体腔压力 `0` `MPa`（默认）| 非负标量

空蓄能器腔的初始表压。如果入口压力等于或大于预充压力，则流体进入蓄能器。

### **Specific heat ratio** — 比热比 `1.4`（默认）| 正标量

腔内气体的比热比。对于 20°C 的空气，该值通常为 1.4。

### **Cross-sectional area at port A** — 入口横截面积 `0.01` `m^2` 正标量（默认）

蓄能器入口处的流通横截面积。

### **Hard stop stiffness coefficient** — 刚度系数 `1e4` `MPa/m^3`（默认）| 正标量

蓄能器顶部和底部硬限位的刚度系数。硬限位将隔膜运动限制在零和最大液体腔液位之间。

### **Hard-stop damping coefficient** — 阻尼系数 `1e4` `MPa*s/m^6`（默认）| 正标量

蓄能器顶部和底部硬限位的阻尼系数。硬限位将隔膜运动限制在零和最大液体腔液位之间。阻尼系数考虑了硬限位接触力的耗散部分。

## 所属库

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

热液体网络中的充气式蓄能器

Gas-Charged Accumulator (TL) 模块表示一个带有压缩气体充能的加压热液体容器。蓄能器由热液体腔和气体腔组成，两者由密封且隔热的隔膜隔开。

**蓄能器示意图**

隔膜将密封的气体腔与带有一个端口的液体腔隔开。蓄能器顶部和底部附近有硬限位。

如果入口压力大于气体充能压力，液体腔体积增大，压缩气体腔。如果入口压力低于气体充能压力，液体腔体积减小，气体腔膨胀。

当液体腔达到容量以及液体腔为空时，硬限位限制隔膜运动。如果指定的弹簧刚度过低，液体体积可能瞬间降至零以下或升至容量以上。使用 **Hard stop stiffness coefficient** 参数来修正此问题。

### 质量平衡

液体腔中的质量守恒方程为

VLρL(1βLdpLdt−αLdTLdt)+ρLdVLdt=m˙A，

其中：

- *ρ*L 是热液体密度。
- *β*L 是等温体积模量。
- *α*L 是等压热膨胀系数。
- *p*L 是热液体压力。
- *T*L 是热液体温度。
- m˙A 是通过端口 **A** 进入蓄能器的热液体质量流量。

该模块使用条件方程计算液体腔体积的时间变化

dVLdt={p˙LkpprVTkVG(−k−1)+Ks+Kdm˙+/ρL,VL≥VCp˙LkpprVTkVG(−k−1)+Ks−Kdm˙−/ρL,VL≤0p˙LkpprVTkVG(−k−1),Else，

其中：

- *Ks* 是 **Hard-stop stiffness coefficient** 参数。
- *Kd* 是 **Hard-stop damping coefficient** 参数。
- m˙+ 是当蓄能器隔膜接触顶部硬限位时进入液体腔的质量流量：

  m˙+={m˙,m˙>00,Else，
- m˙− 是当蓄能器隔膜接触底部硬限位时从液体腔流出的质量流量：

  m˙−={m˙,m˙<00,Else，

### 动量平衡

蓄能器体积中的动量守恒方程为

pL=pG+pHS，

其中 *pHS* 是硬限位接触压力：

- pHS={(VL−VC)(Ks+Kdm˙+/ρ),VL≥VCVL(Ks−Kdm˙−/ρ),VL≤00,Else，

### 能量平衡

液体腔体积中的能量守恒方程为

ddt(ρLuLVL)=ϕA+ϕH，

其中：

- *u*L 是热液体比内能。
- *Φ*A 是通过蓄能器入口进入液体腔的能量流量。
- *Φ*H 是通过蓄能器壁进入液体腔的热能流量。

### 腔体积

液体腔体积是蓄能器总体积与气体腔体积之差：

VL=VT−VG，

其中：

- *V*L 是液体腔体积。
- *V*T 是蓄能器总体积。
- *V*G 是气体腔体积。

**腔体积**

该图显示了蓄能器体积测量示意图。

液体腔容量是蓄能器总体积与满容量时蓄能器中气体死区体积之差：

VC=VT−VDead，

其中：

- *V*C 是液体腔容量。
- *V*Dead 是满容量时的气体死区体积。

气体腔压力和体积由预充状态根据多方方程得出

pGVGk=pprVTk，

其中：

- *p*G 是给定时间步长下的气体腔压力。
- *V*G 是给定时间步长下的气体腔体积。
- *p*pr 是液体腔为空时的预充气体腔压力。
- *V*T 是液体腔总体积。
- *k* 是多方指数。

### 初始目标

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

### 假设和限制

- 该模块将气体腔压缩视为多方过程。
- 该模块忽略隔膜载荷。
- 该模块忽略流体惯性的影响。
