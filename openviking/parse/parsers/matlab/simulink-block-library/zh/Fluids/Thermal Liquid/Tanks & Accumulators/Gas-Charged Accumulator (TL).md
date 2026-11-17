---
type: simulink-block
title: 'Gas-Charged Accumulator (TL)'
family: 'thermal-liquid'
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

### 守恒

### **A** — 液体端口 Thermal Liquid

与蓄能器入口关联的 Thermal Liquid 守恒端口。
如果液体流入蓄能器，则流量为正。

### **H** — 热端口 Thermal

与液体体积的热质量关联的热守恒端口。

## 参数

### **总蓄能器容积** — 蓄能器容积 `8e-3` `m^3` (默认) | 正标量

蓄能器的总容积，包括液体腔室和气体腔室。它是液体腔室容量与最小气体体积之和。

### **最小气体体积** — 气体腔室死体积 `4e-5` `m^3` (默认) | 正标量

气体腔室死体积。这是液体腔室充满时剩余的气体量。必须为非零体积，以便当液体腔室充满时气体压力不会变为无穷大。

### **预充压力（表压）** — 气体腔室压力 `0` `MPa` (默认) | 非负标量

空蓄能器腔室的初始表压。如果入口压力等于或大于预充压力，流体进入蓄能器。

### **比热比** — 比热比 `1.4` (默认) | 正标量

腔室中气体的比热比。对于 20°C 的空气，该值通常为 1.4。

### **端口 A 的横截面积** — 入口横截面积 `0.01` `m^2`正标量 (默认)

蓄能器入口处的流通横截面积。

### **硬止挡刚度系数** — 刚度系数 `1e4` `MPa/m^3` (默认) | 正标量

顶部和底部蓄能器硬止挡的刚度系数。硬止挡将隔膜运动限制在零与最大液体腔室液位之间。

### **硬止挡阻尼系数** — 阻尼系数 `1e4` `MPa*s/m^6` (默认) | 正标量

顶部和底部蓄能器硬止挡的阻尼系数。硬止挡将隔膜运动限制在零与最大液体腔室液位之间。阻尼系数用于考虑硬止挡接触力的耗散部分。

## 所属库

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

Thermal Liquid 网络中的气体充压蓄能器

Gas-Charged Accumulator (TL) 模块表示一个带有压缩气体充压的加压 Thermal Liquid 容器。蓄能器由 Thermal Liquid 腔室和气体腔室组成，二者由密封且隔热的隔膜隔开。

**蓄能器示意图**

隔膜将密封的气体腔室与带有一个端口的液体腔室隔开。蓄能器顶部和底部附近有硬止挡。

如果入口压力大于气体充压压力，则液体腔室体积增大，压缩气体腔室。如果入口压力低于气体充压压力，则液体腔室体积减小，使气体腔室减压。

硬止挡在液体腔室达到容量时以及液体腔室为空时限制隔膜运动。如果指定的弹簧刚度过低，液体体积可能瞬间降至零以下或升至容量以上。使用 **硬止挡刚度系数** 参数来修正此问题。

### 质量平衡

液体腔室中的质量守恒方程为

VLρL(1βLdpLdt−αLdTLdt)+ρLdVLdt=m˙A,

其中：

- *ρ*L 是 Thermal Liquid 密度。
- *β*L 是等温体积模量。
- *α*L 是等压热膨胀系数。
- *p*L 是 Thermal Liquid 压力。
- *T*L 是 Thermal Liquid 温度。
- m˙A 是经由端口 **A** 进入蓄能器的 Thermal Liquid 质量流量。

该模块使用以下条件方程计算液体腔室体积随时间的变化

dVLdt={p˙LkpprVTkVG(−k−1)+Ks+Kdm˙+/ρL,VL≥VCp˙LkpprVTkVG(−k−1)+Ks−Kdm˙−/ρL,VL≤0p˙LkpprVTkVG(−k−1),Else,

其中：

- *Ks* 是 **硬止挡刚度系数** 参数。
- *Kd* 是 **硬止挡阻尼系数** 参数。
- m˙+ 是当蓄能器隔膜接触顶部硬止挡时进入液体腔室的质量流量：

  m˙+={m˙,m˙>00,Else,
- m˙− 是当蓄能器隔膜接触底部硬止挡时从液体腔室流出的质量流量：

  m˙−={m˙,m˙<00,Else,

### 动量平衡

蓄能器体积中的动量守恒方程为

pL=pG+pHS,

其中 *pHS* 是硬止挡接触压力：

- pHS={(VL−VC)(Ks+Kdm˙+/ρ),VL≥VCVL(Ks−Kdm˙−/ρ),VL≤00,Else,

### 能量平衡

液体腔室体积中的能量守恒方程为

ddt(ρLuLVL)=ϕA+ϕH,

其中：

- *u*L 是 Thermal Liquid 比内能。
- *Φ*A 是经由蓄能器入口进入液体腔室的能量流率。
- *Φ*H 是经由蓄能器壁进入液体腔室的热能流率。

### 腔室体积

液体腔室体积是蓄能器总容积与气体腔室体积之差：

VL=VT−VG,

其中：

- *V*L 是液体腔室体积。
- *V*T 是蓄能器总容积。
- *V*G 是气体腔室体积。

**腔室体积**

该图显示了蓄能器体积测量的示意图。

液体腔室容量是蓄能器总容积与蓄能器满容量时气体死体积之差：

VC=VT−VDead,

其中：

- *V*C 是液体腔室容量。
- *V*Dead 是满容量时的气体死体积。

气体腔室压力和体积由预充状态根据以下多变方程给出

pGVGk=pprVTk,

其中：

- *p*G 是给定时间步长下的气体腔室压力。
- *V*G 是给定时间步长下的气体腔室体积。
- *p*pr 是液体腔室为空时的预充气体腔室压力。
- *V*T 是总液体腔室体积。
- *k* 是多变指数。

### 初始目标

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

### 假设和限制

- 该模块将气体腔室压缩视为多变过程。
- 该模块忽略隔膜载荷。
- 该模块忽略流体惯性的影响。
