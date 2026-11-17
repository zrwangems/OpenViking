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
```yaml
ports:
- name: AR
  summary: 节流面积控制信号，m^2 物理信号
  direction: input
- name: A
  summary: 入口或出口气体
  direction: input
- name: B
  summary: 入口或出口气体
  direction: input
```

### 输入

### **AR** — 节流面积控制信号，m^2 物理信号

控制气体节流面积的输入物理信号。当该信号的值超出模块参数指定的最小和最大节流面积限值时，信号饱和。

#### 依赖关系

仅当您将 **Restriction type** 参数设置为 `Variable` 时，此端口才可见。

### 守恒

### **A** — 入口或出口气体

与局部节流入口或出口关联的气体守恒端口。此模块没有固有方向性。

### **B** — 入口或出口气体

与局部节流入口或出口关联的气体守恒端口。此模块没有固有方向性。
## 参数
```yaml
parameters:
- name: Restriction type
  summary: 指定节流面积是否可以在仿真期间变化 Variable（默认）| Fixed
  group: ''
- name: Minimum restriction area
  summary: 节流横截面积的下限 1e-10 m^2（默认）
  group: ''
- name: Maximum restriction area
  summary: 节流横截面积的上限 0.005 m^2（默认）
  group: ''
- name: Restriction area
  summary: 节流处垂直于流路的面积 1e-3 m^2（默认）
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 端口处垂直于流路的面积 0.01 m^2（默认）
  group: ''
- name: Discharge coefficient
  summary: 通过节流的实际质量流量与理论质量流量之比 0.64（默认）
  group: ''
- name: Laminar flow pressure ratio
  summary: 气体流动在层流和湍流状态之间转换时的压力比 0.999（默认）
  group: ''
```

### **Restriction type** — 指定节流面积是否可以在仿真期间变化 `Variable`（默认）| `Fixed`

选择节流面积是否可以在仿真期间变化：

- `Variable` — 端口 **AR** 处的输入物理信号指定节流面积，该面积可以在仿真期间变化。**Minimum restriction area** 和 **Maximum restriction area** 参数指定节流面积的下限和上限。
- `Fixed` — 由 **Restriction area** 模块参数值指定的节流面积在仿真期间保持恒定。端口 **AR** 被隐藏。

### **Minimum restriction area** — 节流横截面积的下限 `1e-10 m^2`（默认）

节流横截面积的下限。您可以使用此参数表示泄漏面积。输入信号 AR 在此值处饱和，以防止节流面积进一步减小。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Maximum restriction area** — 节流横截面积的上限 `0.005 m^2`（默认）

节流横截面积的上限。输入信号 AR 在此值处饱和，以防止节流面积进一步增大。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Restriction area** — 节流处垂直于流路的面积 `1e-3 m^2`（默认）

节流处垂直于流路的面积。

#### 依赖关系

当 **Restriction type** 参数设置为 `Fixed` 时启用。

### **Cross-sectional area at ports A and B** — 端口处垂直于流路的面积 `0.01 m^2`（默认）

端口 **A** 和 **B** 处垂直于流路的面积。假定两个端口的该面积相同。

### **Discharge coefficient** — 通过节流的实际质量流量与理论质量流量之比 `0.64`（默认）

通过节流的实际质量流量与理论质量流量之比。流量系数是一个经验参数，用于考虑非理想效应。

### **Laminar flow pressure ratio** — 气体流动在层流和湍流状态之间转换时的压力比 `0.999`（默认）

气体流动在层流和湍流状态之间转换时的压力比。在层流状态下，压力损失与质量流量成线性关系；在湍流状态下，压力损失与质量流量成二次关系。
## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体管网中流通面积的限制

局部阻力（G）模块对气体管网中因流通面积局部缩小（例如阀门或孔板）而产生的压降进行建模。当阻力达到声速条件时，会发生阻塞。

端口 **A** 和 **B** 分别表示阻力的入口和出口。端口 **AR** 处的输入物理信号指定阻力面积。或者，您可以将固定阻力面积指定为模块参数。

模块图标根据 **Restriction type** 参数的值而变化。

| 阻力类型 | 模块图标 |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

该阻力是绝热的。它不与环境交换热量。

该阻力由流通面积的收缩和随后的突然扩张组成。气体在收缩期间加速，导致压力下降。气体在突然扩张期间与壁面分离，由于动量损失，压力仅部分恢复。

**局部阻力示意图**

**注意**

通过该模块的气体流动可能发生阻塞。如果连接到局部阻力（G）模块的质量流量源（G）模块或受控质量流量源（G）模块指定的质量流量大于可能的阻塞质量流量，仿真将生成错误。有关详细信息，请参阅阻塞流。

### 质量平衡

质量平衡方程为：

m˙A+m˙B=0

其中 m˙A 和 m˙B 分别是端口 **A** 和 **B** 处的质量流量。与端口相关的流量在流入模块时为正。

### 能量平衡

能量平衡方程为：

ΦA+ΦB=0

其中 *Φ*A 和 *Φ*B 分别是端口 **A** 和 **B** 处的能量流量。

假设该模块是绝热的。因此，端口 **A**、端口 **B** 和阻力之间的比总焓没有变化：

hA+wA22=hR+wR22hB+wB22=hR+wR22

其中 *h* 是端口 **A**、端口 **B** 或阻力 R 处的比焓，由下标指示。

端口 **A**、端口 **B** 和阻力处的理想流速为：

wA=m˙idealρASwB=m˙idealρBSwR=m˙idealρRSR

其中：

- *S* 是端口 **A** 和 **B** 处的横截面积。
- *S*R 是阻力处的横截面积。
- *ρ* 是端口 **A**、端口 **B** 或阻力 R 处的气体体积密度，由下标指示。

无非理想效应的理论质量流量为：

m˙ideal=m˙ACd

其中 *C*d 是流量系数。

### Momentum Balance

端口 **A** 和 **B** 之间的压差基于入口与节流口之间流通面积收缩的动量平衡，加上节流口与出口之间流通面积突然扩张的动量平衡。

对于从端口 **A** 到端口 **B** 的流动：

ΔpAB=ρR⋅wR⋅|wR|⋅(1+r2(1−rρRρA)−r(1−rρRρB))

其中 *r* 是面积比，*r* = *S*R/*S*。

对于从端口 **B** 到端口 **A** 的流动：

ΔpBA=ρR⋅wR⋅|wR|⋅(1+r2(1−rρRρB)−r(1−rρRρA))

前两个方程中的压差与流量的平方成正比。这是湍流的典型行为。然而，对于层流，压差相对于流量变为线性。压差的层流近似为：

Δplam=ρRΔptransition2(1−r)

从湍流过渡到层流的阈值定义为 *Δp*transition = *p*avg(1 — *B*lam)，其中 *B*lam 是层流和湍流 regime 之间过渡处的压力比（**Laminar flow pressure ratio** 参数值），*p*avg = (*p*A + *p*B)/2。

节流口处的压力基于入口与节流口之间流通面积收缩的动量平衡。

对于从端口 **A** 到端口 **B** 的流动：

pRAB=pA−ρR⋅wR⋅|wR|⋅1+r2(1−rρRρA)

对于从端口 **B** 到端口 **A** 的流动：

pRBA=pB+ρR⋅wR⋅|wR|⋅1+r2(1−rρRρB)

对于层流，节流口处的压力近似为

pRlam=pavg−ρR⋅wR21−r22

该模块使用关于 (*p*A – *p*B) 的三次多项式，在湍流 regime 和层流 regime 之间平滑混合压差和节流口压力：

- 当 *Δp*transition ≤ *p*A – *p*B 时，

  则 *p*A – *p*B = *Δp*AB

  且 *p*R = *p*RAB。
- 当 0 ≤ *p*A – *p*B < *Δp*transition 时，

  则 *p*A – *p*B 在 *Δp*AB 和 *Δp*lam 之间平滑混合

  且 *p*R 在 *p*RAB 和 *p*Rlam 之间平滑混合。
- 当 –*Δp*transition < *p*A – *p*B ≤ 0 时，

  则 *p*A – *p*B 在 *Δp*BA 和 *Δp*lam 之间平滑混合

  且 *p*R 在 *p*RBA 和 *p*Rlam 之间平滑混合。
- 当 *p*A – *p*B ≤ –*Δp*transition 时，

  则 *p*A – *p*B = *Δp*BA

  且 *p*R = *p*RBA。

### Choked Flow

当通过节流口的流动发生阻塞时，流动的进一步变化取决于上游条件，而与下游条件无关。

如果 *A.p* 是端口 **A** 处的 Across 变量，*p*Bchoked 是假设从端口 **A** 到端口 **B** 发生阻塞流动时端口 **B** 处的假设压力，则

A.p−pBchoked=ρR⋅aR2(1+r2(1−rρRρA)−r(1−rρRρB))

其中 *a* 是声速。

如果 *B.p* 是端口 **B** 处的 Across 变量，*p*Achoked 是假设从端口 **B** 到端口 **A** 发生阻塞流动时端口 **A** 处的假设压力，则

B.p−pAchoked=ρR⋅aR2(1+r2(1−rρRρB)−r(1−rρRρA))

端口 **A** 和 **B** 处的实际压力 *p*A 和 *p*B 分别取决于是否发生阻塞。

对于从端口 A 到端口 B 的流动，*p*A = *A.p* 且

pB={B.p,if B.p≥pBchokedpBchoked,if B.p<pBchoked

对于从端口 **B** 到端口 **A** 的流动，*p*B = *B.p* 且

pA={A.p,if A.p≥pAchokedpAchoked,if A.p<pAchoked

### 假设和限制

- 节流口是绝热的。它不与环境交换热量。
- 该模块不建模超声速流动。
