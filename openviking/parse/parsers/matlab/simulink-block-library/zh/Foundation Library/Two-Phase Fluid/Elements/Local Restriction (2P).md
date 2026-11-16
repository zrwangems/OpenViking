---
type: simulink-block
title: 'Local Restriction (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'localrestriction2p'
documentation_source_path: 'ref/localrestriction2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Restriction (2P)

## 端口

### 输入

### **AR** — 节流面积控制信号，m^2 物理信号

输入物理信号，用于控制节流面积。当该信号的值超出由 **Minimum restriction area** 和 **Maximum restriction area** 参数指定的最小和最大节流面积限值时，该信号会饱和。

#### 依赖项

要启用此端口，请将 **Restriction type** 参数设置为 `Variable`。

### 守恒

### **A** — 入口或出口两相流体

与局部节流的入口或出口关联的两相流体守恒端口。该模块没有固有方向性。

### **B** — 入口或出口两相流体

与局部节流的入口或出口关联的两相流体守恒端口。该模块没有固有方向性。

## 参数

### **Restriction type** — 节流面积是否可在仿真期间变化 `Variable` (默认) | `Fixed`

节流面积是否可在仿真期间变化：

- `Variable` — 端口 **AR** 处的输入物理信号指定节流面积，该面积可在仿真期间变化。**Minimum restriction area** 和 **Maximum restriction area** 参数指定节流面积的下界和上界。
- `Fixed` — 由 **Restriction area** 模块参数值指定的节流面积在仿真期间保持恒定。

### **Minimum restriction area** — 节流横截面积的下界 `1e-10 m^2` (默认) | 正标量

节流横截面积的下界。您可以使用此参数表示泄漏面积。端口 **AR** 处的输入信号在此值处饱和，以防止节流面积进一步减小。

#### 依赖项

要启用此参数，请将 **Restriction type** 设置为 `Variable`。

### **Maximum restriction area** — 节流横截面积的上界 `0.005 m^2` (默认) | 正标量

节流横截面积的上界。端口 **AR** 处的输入信号在此值处饱和，以防止节流面积进一步增大。

#### 依赖项

要启用此参数，请将 **Restriction type** 设置为 `Variable`。

### **Restriction area** — 节流处垂直于流动路径的面积 `1e-3 m^2` (默认) | 正标量

节流处垂直于流动路径的面积。

#### 依赖项

要启用此参数，请将 **Restriction type** 设置为 `Fixed`。

### **Pressure loss model** — 动量平衡计算是否假定均匀流体密度 `Bernoulli` (默认) | `Control volume`

用于动量平衡计算的方程：

- `Bernoulli` — 模块使用 Bernoulli 方程，该方程假定从入口到出口密度均匀。此选项有时不如 `Control volume` 方法准确，但更稳健，并提供更快的仿真。
- `Control volume` — 模块使用控制体分析，而不假定密度均匀。它将从入口到节流的流动建模为流动收缩，并将从节流到出口的流动建模为流动膨胀。

### **Cross-sectional area at ports A and B** — 端口处与流动路径垂直的面积 `0.01 m^2` (默认) | 正标量

端口 **A** 和 **B** 处与流动路径垂直的面积。假定两个端口的该面积相同。

### **Discharge coefficient** — 通过节流的实际质量流量与理论质量流量之比 `0.64` (默认) | 0 到 1 之间的无量纲标量

流量系数是一个半经验参数，通常用于表征孔口的流通能力。此参数表示通过孔口的实际质量流量与理想质量流量之比。

### **Laminar flow pressure ratio** — 用于在层流和湍流状态之间切换的压力比 `0.999` (默认) | 0 到 1 之间的无量纲标量

假定流态从层流切换为湍流时，出口端口压力与入口端口压力之比。主导流态决定仿真中使用的方程。如果流动为层流，则节流两端的压降与质量流量呈线性关系。如果流动为湍流，则节流两端的压降与质量流量呈二次关系。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2024a：使用 Bernoulli 方程计算压力损失

Local Restriction (2P) 模块现在具有 **Pressure loss model** 参数，允许您在两种压力损失模型之间进行选择。`Control volume` 选项是以前版本中可用的功能，在某些场景中更准确。新的 `Bernoulli` 选项假定从入口到出口密度均匀，更稳健，并提供更快的仿真。

此更改没有兼容性影响。对于新模块，`Bernoulli` 选项是默认设置，但当您打开现有模型时，其中的 Local Restriction (2P) 模块会自动将 **Pressure loss model** 参数设置为 `Control volume`。

### R2022b：对固定面积和可变面积节流进行建模

Local Restriction (2P) 模块现在具有 **Restriction type** 参数，允许您在固定面积和可变面积节流建模之间切换。模块使用 **Restriction area** 参数或输入物理信号端口 **AR** 来指定局部节流的面积。

在以前的版本中，该模块仅对固定节流建模。Two-Phase Fluid 库还包含单独的 Variable Local Restriction (2P) 模块，该模块不再可用。此更改没有兼容性影响。当您打开现有模型时，其中的所有 Variable Local Restriction (2P) 模块会自动替换为具有暴露控制端口 **AR** 的 Local Restriction (2P) 模块。

## 描述

两相流体网络中的流动面积节流

Local Restriction (2P) 模块对两相流体网络中由于流动面积局部减小（例如阀门或孔口）引起的压降进行建模。

端口 **A** 和 **B** 表示节流的入口和出口。端口 **AR** 处的输入物理信号指定节流面积。或者，您可以将固定节流面积指定为模块参数。

模块图标根据 **Restriction type** 参数的值而变化。

| 节流类型 | 模块图标 |
| --- | --- |
| `Variable` | Variable Local Restriction (2P) 模块图标 |
| `Fixed` | Fixed Local Restriction (2P) 模块图标 |

节流是绝热的。它不与环境交换热量。

节流由流动面积的收缩以及随后的突然膨胀组成。

**局部节流示意图**

流体流经局部节流

流体在收缩期间加速，这导致压力下降。在伴随一些动量损失通过节流后，流体膨胀并朝向出口减速，使得压力在节流后略微升高。此压力损失模型对应于 **Pressure loss model** 参数的 `Control volume` 选项。它提供更好的精度，但相比默认的 `Bernoulli` 选项稳健性和效率较低，后者假定节流入口和出口之间密度均匀。

在以下情况下使用 `Bernoulli` 选项：

- 局部节流在完全过冷液体状态下运行。流体近似不可压缩，均匀密度假定是合适的。
- 局部节流在制冷循环中用作膨胀阀。入口处的流体是来自冷凝器的过冷液体，因此均匀密度假定是合适的。
- 局部节流在完全过热蒸气状态下运行，但流速为低亚声速，这在 HVAC 系统中通常是这种情况。在这种情况下，密度变化也不大，均匀密度假定是合适的。

对于所有其他情况，您也可以使用 `Bernoulli` 选项，以精度换取更快且更稳健的仿真。

### 质量平衡

质量平衡方程为

m˙A+m˙B=0,

其中：

- m˙A 和 m˙B 是通过端口 **A** 和端口 **B** 流入节流的质量流量。

### 能量平衡

能量平衡方程为

ϕA+ϕB=0,

其中 *ϕ*A 和 *ϕ*B 是通过端口 **A** 和端口 **B** 流入节流的能量流量。

假定局部节流是绝热的，因此比总焓的变化为零。在端口 **A** 处，

uA+pAνA+wA22=uR+pRνR+wR22,

而在端口 **B** 处，

uB+pBνB+wB22=uR+pRνR+wR22,

其中：

- *u*A、*u*B 和 *u*R 分别是端口 **A**、端口 **B** 和节流孔口处的比内能。
- *p*A、*p*B 和 *p*R 分别是端口 **A**、端口 **B** 和节流孔口处的压力。
- *ν*A、*ν*B 和 *ν*R 分别是端口 **A**、端口 **B** 和节流孔口处的比容。
- *w*A、*w*B 和 *w*R 分别是端口 **A**、端口 **B** 和节流孔口处的理想流速。

模块将理想流速计算为

wA=m˙idealνAS

在端口 **A** 处，为

wB=m˙idealνBS

在端口 **B** 处，以及为

wR=m˙idealνRSR,

在节流内部，其中：

- m˙ideal 是通过节流的理想质量流量。
- *S* 是端口 **A** 和端口 **B** 处的流通面积。
- *S*R 是节流孔口的流通面积。

模块将通过节流的理想质量流量计算为：

m˙ideal=m˙ACD,

其中 *C*D 是局部节流的流量系数。

**局部节流变量**

局部节流中变量的示意图表示

### 使用 Bernoulli 方程时的动量平衡

从端口 **A** 到端口 **B** 的质量流量为：

m˙A=CdSRΔp(Δp+Δplam2)1/42νinPRloss(1−(SRS)2),Δp=pA−pB,

其中：

- *Δp*lam 是流动开始在层流和湍流之间平滑过渡的阈值压降。
- *v*in 是入口比容。哪个端口作为入口、哪个端口作为出口取决于节流两端的压差。如果端口 **A** 处的压力大于端口 **B**，则端口 **A** 是入口；如果端口 **B** 处的压力更大，则端口 **B** 是入口。
- *PR*loss 是压力损失比。

压力损失比 *PR*loss 是入口与出口之间的压差与入口与节流之间的压差之比。它是一个考虑节流后流动膨胀期间压力恢复的项：

PRloss=1−(SRS)2(1−Cd2)−CdSRS1−(SRS)2(1−Cd2)+CdSRS.

### 使用控制体分析时的动量平衡

湍流时从端口 **A** 到端口 **B** 的质量流量为：

m˙A=CdSRΔp2|Δp|νRKT.

*K*T 定义为：

KT=(1+SRS)(1−νinνRSRS)−2SRS(1−νoutνRSRS),

其中下标 `in` 表示入口端口，下标 `out` 表示出口端口。哪个端口作为入口、哪个端口作为出口取决于节流两端的压差。如果端口 **A** 处的压力大于端口 **B**，则端口 **A** 是入口；如果端口 **B** 处的压力更大，则端口 **B** 是入口。

层流时从端口 **A** 到端口 **B** 的质量流量为：

m˙A=CdSRΔp2ΔplamνR(1−SRS)2.

*Δp*lam 表示流动开始在层流和湍流之间平滑过渡的阈值压降：

Δplam=(pA+pB2)(1−Blam),

其中 *B*lam 是 **Laminar flow pressure ratio** 参数。如果从端口 **A** 到端口 **B** 的压降低于阈值，则流动为层流；否则，流动为湍流。

节流面积处的压力 *p*R 也取决于流态。当流动为湍流时：

pR,T=pin−νR2(m˙ACdSR)2(1+SRS)(1−νinνRSRS).

当流动为层流时：

pR,L=pA+pB2.

### 假设和限制

- 节流是绝热的。它不与周围环境交换热量。
- `Bernoulli` 压力损失模型假定节流入口和出口之间流体密度均匀。
