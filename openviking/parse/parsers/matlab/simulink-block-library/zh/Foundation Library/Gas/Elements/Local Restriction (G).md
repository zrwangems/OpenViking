---
type: simulink-block
title: 'Local Restriction (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'localrestrictiong'
documentation_source_path: 'ref/localrestrictiong.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Restriction (G)

## 端口

### 输入

### **AR** — 节流面积控制信号，m^2 physical signal

输入 physical signal，用于控制气体流动节流面积。当该信号的值超出由模块参数指定的最小和最大节流面积限值时，信号饱和。

#### 依赖关系

仅当将 **Restriction type** 参数设置为 `Variable` 时，此端口可见。

### 守恒

### **A** — 入口或出口气体

与局部节流的入口或出口关联的气体守恒端口。此模块没有固有方向性。

### **B** — 入口或出口气体

与局部节流的入口或出口关联的气体守恒端口。此模块没有固有方向性。

## 参数

### **Restriction type** — 指定节流面积在仿真期间是否可变 `Variable`（默认）| `Fixed`

选择节流面积在仿真期间是否可变：

- `Variable` — 端口 **AR** 处的输入 physical signal 指定节流面积，该面积在仿真期间可变。**Minimum restriction area** 和 **Maximum restriction area** 参数指定节流面积的下限和上限。
- `Fixed` — 由 **Restriction area** 模块参数值指定的节流面积在仿真期间保持恒定。端口 **AR** 隐藏。

### **Minimum restriction area** — 节流横截面积的下限 `1e-10 m^2`（默认）

节流横截面积的下限。可以使用此参数表示泄漏面积。输入信号 AR 在此值处饱和，以防止节流面积进一步减小。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Maximum restriction area** — 节流横截面积的上限 `0.005 m^2`（默认）

节流横截面积的上限。输入信号 AR 在此值处饱和，以防止节流面积进一步增大。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Restriction area** — 节流处垂直于流动路径的面积 `1e-3 m^2`（默认）

节流处垂直于流动路径的面积。

#### 依赖关系

当 **Restriction type** 参数设置为 `Fixed` 时启用。

### **Cross-sectional area at ports A and B** — 端口处垂直于流动路径的面积 `0.01 m^2`（默认）

端口 **A** 和 **B** 处垂直于流动路径的面积。假定两个端口的该面积相同。

### **Discharge coefficient** — 通过节流的实际质量流量与理论质量流量之比 `0.64`（默认）

通过节流的实际质量流量与理论质量流量之比。流量系数是考虑非理想效应的经验参数。

### **Laminar flow pressure ratio** — 气体流动在层流和湍流状态之间转换时的压力比 `0.999`（默认）

气体流动在层流和湍流状态之间转换时的压力比。在层流状态下，压力损失与质量流量呈线性关系；在湍流状态下，压力损失与质量流量呈二次关系。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体网络中的流动面积节流

Local Restriction (G) 模块对气体网络中因局部流动面积减小（例如阀门或节流孔）导致的压降进行建模。当节流处达到声速条件时，会发生阻塞。

端口 **A** 和 **B** 表示节流的入口和出口。端口 **AR** 处的输入 physical signal 指定节流面积。或者，可以将节流面积指定为模块参数的固定值。

模块图标根据 **Restriction type** 参数的值而变化。

| 节流类型 | 模块图标 |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

该节流是绝热的。它不与环境交换热量。

节流由流动面积收缩段及其后的突然扩张组成。气体在收缩段期间加速，导致压力下降。气体在突然扩张期间与壁面分离，由于动量损失，压力仅部分恢复。

**Local Restriction 示意图**

**注意**

通过此模块的气体流动可能会阻塞。如果连接到 Local Restriction (G) 模块的 Mass Flow Rate Source (G) 模块或 Controlled Mass Flow Rate Source (G) 模块指定的质量流量大于可能发生阻塞的质量流量，则仿真会生成错误。有关详细信息，请参见阻塞流。

### 质量平衡

质量平衡方程为：

m˙A+m˙B=0

其中 m˙A 和 m˙B 分别是端口 **A** 和 **B** 处的质量流量。当与端口关联的流量流入模块时，该流量为正。

### 能量平衡

能量平衡方程为：

ΦA+ΦB=0

其中 *Φ*A 和 *Φ*B 分别是端口 **A** 和 **B** 处的能量流率。

假定该模块是绝热的。因此，端口 **A**、端口 **B** 和节流之间的比总焓没有变化：

hA+wA22=hR+wR22hB+wB22=hR+wR22

其中 *h* 是端口 **A**、端口 **B** 或节流 R 处的比焓，由下标指示。

端口 **A**、端口 **B** 和节流处的理想流速为：

wA=m˙idealρASwB=m˙idealρBSwR=m˙idealρRSR

其中：

- *S* 是端口 **A** 和 **B** 处的横截面积。
- *S*R 是节流处的横截面积。
- *ρ* 是端口 **A**、端口 **B** 或节流 R 处的气体体积密度，由下标指示。

无非理想效应时的理论质量流量为：

m˙ideal=m˙ACd

其中 *C*d 是流量系数。

### 动量平衡

端口 **A** 和 **B** 之间的压力差基于入口与节流之间流动面积收缩的动量平衡，加上节流与出口之间流动面积突然扩张的动量平衡。

对于从端口 **A** 到端口 **B** 的流动：

ΔpAB=ρR⋅wR⋅|wR|⋅(1+r2(1−rρRρA)−r(1−rρRρB))

其中 *r* 是面积比，*r* = *S*R/*S*。

对于从端口 **B** 到端口 **A** 的流动：

ΔpBA=ρR⋅wR⋅|wR|⋅(1+r2(1−rρRρB)−r(1−rρRρA))

前两个方程中的压力差与流率的平方成正比。这是湍流的典型行为。然而，对于层流，压力差变为与流率呈线性关系。压力差的层流近似为：

Δplam=ρRΔptransition2(1−r)

从湍流到层流转换的阈值定义为 *Δp*transition = *p*avg(1 — *B*lam)，其中 *B*lam 是层流与湍流状态之间转换处的压力比（**Laminar flow pressure ratio** 参数值），并且 *p*avg = (*p*A + *p*B)/2。

节流处的压力基于入口与节流之间流动面积收缩的动量平衡。

对于从端口 **A** 到端口 **B** 的流动：

pRAB=pA−ρR⋅wR⋅|wR|⋅1+r2(1−rρRρA)

对于从端口 **B** 到端口 **A** 的流动：

pRBA=pB+ρR⋅wR⋅|wR|⋅1+r2(1−rρRρB)

对于层流，节流处的压力近似为

pRlam=pavg−ρR⋅wR21−r22

该模块使用关于 (*p*A – *p*B) 的三次多项式，以在湍流状态和层流状态之间平滑混合压力差和节流压力：

- 当 *Δp*transition ≤ *p*A – *p*B 时，

  则 *p*A – *p*B = *Δp*AB

  并且 *p*R = *p*RAB。
- 当 0 ≤ *p*A – *p*B < *Δp*transition 时，

  则 *p*A – *p*B 在 *Δp*AB 和 *Δp*lam 之间平滑混合

  并且 *p*R 在 *p*RAB 和 *p*Rlam 之间平滑混合。
- 当 –*Δp*transition < *p*A – *p*B ≤ 0 时，

  则 *p*A – *p*B 在 *Δp*BA 和 *Δp*lam 之间平滑混合

  并且 *p*R 在 *p*RBA 和 *p*Rlam 之间平滑混合。
- 当 *p*A – *p*B ≤ –*Δp*transition 时，

  则 *p*A – *p*B = *Δp*BA

  并且 *p*R = *p*RBA。

### 阻塞流

当通过节流的流动发生阻塞时，流量的进一步变化取决于上游条件，而与下游条件无关。

如果 *A.p* 是端口 **A** 处的 Across variable，且 *p*Bchoked 是假设从端口 **A** 到端口 **B** 发生阻塞流时端口 **B** 处的假想压力，则

A.p−pBchoked=ρR⋅aR2(1+r2(1−rρRρA)−r(1−rρRρB))

如果 *B.p* 是端口 **B** 处的 Across variable，且 *p*Achoked 是假设从端口 **B** 到端口 **A** 发生阻塞流时端口 **A** 处的假想压力，则

B.p−pAchoked=ρR⋅aR2(1+r2(1−rρRρB)−r(1−rρRρA))

端口 **A** 和 **B** 处的实际压力 *p*A 和 *p*B 分别取决于是否已发生阻塞。

对于从端口 A 到端口 B 的流动，*p*A = *A.p* 且

pB={B.p,if B.p≥pBchokedpBchoked,if B.p<pBchoked

对于从端口 **B** 到端口 **A** 的流动，*p*B = *B.p* 且

pA={A.p,if A.p≥pAchokedpAchoked,if A.p<pAchoked

### 假设与限制

- 该节流是绝热的。它不与环境交换热量。
- 此模块不对超声速流动建模。
