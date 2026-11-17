---
type: simulink-block
title: 'Local Restriction (MA)'
family: 'moist-air'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'localrestrictionma'
documentation_source_path: 'ref/localrestrictionma.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Restriction (MA)

## 端口

### 输入

### **AR** — 限制面积控制信号，m^2 物理信号

控制空气流限制面积的输入物理信号。当信号值超出模块参数指定的最小和最大限制面积限值时，信号饱和。

#### 依赖关系

仅当将 **Restriction type** 参数设置为 `Variable` 时，此端口才可见。

### 守恒

### **A** — 入口或出口湿空气

与局部限制的入口或出口关联的湿空气守恒端口。此模块没有固有方向性。

### **B** — 入口或出口湿空气

与局部限制的入口或出口关联的湿空气守恒端口。此模块没有固有方向性。

## 参数

### **Restriction type** — 指定限制面积是否可以在仿真期间变化 `Variable`（默认）| `Fixed`

选择限制面积是否可以在仿真期间变化：

- `Variable` — 端口 **AR** 的输入物理信号指定限制面积，该面积可在仿真期间变化。**Minimum restriction area** 和 **Maximum restriction area** 参数指定限制面积的下界和上界。
- `Fixed` — 由 **Restriction area** 模块参数值指定的限制面积在仿真期间保持恒定。端口 **AR** 隐藏。

### **Minimum restriction area** — 限制横截面积的下界 `1e-10 m^2`（默认）

限制横截面积的下界。可使用此参数表示泄漏面积。输入信号 **AR** 在此值处饱和，以防止限制面积进一步减小。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Maximum restriction area** — 限制横截面积的上界 `0.005 m^2`（默认）

限制横截面积的上界。输入信号 **AR** 在此值处饱和，以防止限制面积进一步增大。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Restriction area** — 限制处垂直于流路的面积 `1e-3 m^2`（默认）

限制处垂直于流路的面积。

#### 依赖关系

当 **Restriction type** 参数设置为 `Fixed` 时启用。

### **Cross-sectional area at ports A and B** — 端口处垂直于流路的面积 `0.01 m^2`（默认）

端口 **A** 和 **B** 处垂直于流路的面积。假定两个端口的该面积相同。

### **Discharge coefficient** — 通过限制的实际质量流量与理论质量流量之比 `0.64`（默认）

通过限制的实际质量流量与理论质量流量之比。流量系数是考虑非理想效应的经验参数。

### **Laminar flow pressure ratio** — 湿空气流在层流和湍流状态之间转换时的压力比 `0.999`（默认）

湿空气流在层流和湍流状态之间转换时的压力比。在层流状态下，压力损失与质量流量成线性关系；在湍流状态下，压力损失与质量流量成二次关系。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的流通面积限制

Local Restriction (MA) 模块对湿空气网络中由于流通面积局部减小（例如阀门或孔口）引起的压力降进行建模。当限制达到声速条件时，会发生阻塞。

端口 **A** 和 **B** 表示限制的入口和出口。端口 **AR** 处的输入物理信号指定限制面积。或者，可以将固定限制面积指定为模块参数。

模块图标根据 **Restriction type** 参数的值而变化。

| Restriction Type | 模块图标 |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

该限制是绝热的。它不与环境交换热量。

该限制由流通面积的收缩和随后的突然扩张组成。湿空气在收缩期间加速，导致压力下降。湿空气在突然扩张期间与壁面分离，由于动量损失，压力仅部分恢复。

**局部限制示意图**

**注意**

湿空气通过此模块时可能发生阻塞。如果连接到 Local Restriction (MA) 模块的 Mass Flow Rate Source (MA) 模块或 Controlled Mass Flow Rate Source (MA) 模块指定的质量流量大于可能的阻塞质量流量，仿真会生成错误。有关详细信息，请参阅 Choked Flow。

模块方程使用以下符号。

|  |  |
| --- | --- |
| m˙ | 质量流量 |
| *Φ* | 能量流量 |
| *p* | 压力 |
| *ρ* | 密度 |
| *R* | 比气体常数 |
| *S* | 横截面积 |
| *C*d | 流量系数 |
| *h* | 比焓 |
| *c*p | 定压比热 |
| *T* | 温度 |

下标 `a`、`w`、`d` 和 `g` 分别表示干空气、水蒸气、水滴和微量气体的属性。下标 `lam` 和 `tur` 分别表示层流和湍流状态。下标 `A` 和 `B` 表示相应端口。下标 `R` 表示限制。

质量平衡：

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

能量平衡：

ΦA+ΦB=0

当流动未阻塞时，湍流状态下的混合物质量流量（从端口 **A** 到端口 **B** 为正）为

m˙tur=CdSR(pA−pB)2ρR|pA−pB|KturKtur=(1+SRS)(1−ρRρinSRS)−2SRS(1−ρRρoutSRS)

下标 `in` 和 `out` 分别表示入口和出口。如果 *p*A ≥ *p*B，则入口是端口 **A**，出口是端口 **B**；否则，它们互换。假定横截面积 *S* 在端口 **A** 和 **B** 处相等。*S*R 是限制处的面积。

混合物质量流量方程通过组合两个控制体分析的方程推导而来：

- 从入口到限制的流通面积收缩的动量平衡
- 从限制到出口的流通面积突然扩张的动量平衡

在流通面积收缩的分析中，压力 *p*in 作用在入口面积 *S* 上，压力 *p*R 作用在限制面积 *S*R 上。作用在限制外部面积 *S* − *S*R 上的压力假定为 (*p*in*S* + *p*R*S*R)/(*S* + *S*R)。

在流通面积扩张的分析中，由于流动与限制分离，作用在限制面积 *S*R 和限制外部面积 *S* − *S*R 上的压力均假定为 *p*R。作用在出口面积 *S* 上的压力等于 *p*out。

层流状态下的混合物质量流量（从端口 **A** 到端口 **B** 为正）相对于压差线性化：

m˙lam=CdSR(pA−pB)2ρRΔpthreshold(1−SRS)2

其中，层流和湍流状态之间转换的阈值基于层流压力比 *B*lam 定义为

Δpthreshold=(pA+pB2)(1−Blam)

当 |pA−pB|≥Δpthreshold 时，流动被假定为湍流，因此 m˙unchoked=m˙tur。

当 |pA−pB|<Δpthreshold 时，m˙unchoked 平滑过渡到 m˙lam。

当流动阻塞时，限制处的速度等于声速，且不能进一步增大。假设流动阻塞，混合物质量流量为

m˙choked=CdSRpRγRRTR

其中 γR=cpR/(cpR−R)。因此，实际混合物质量流量等于 m˙unchoked，但其大小受 m˙choked 限制：

m˙A={−m˙choked,if m˙unchoked≤−m˙chokedm˙unchoked,if -m˙choked<m˙unchoked<m˙chokedm˙choked,if m˙unchoked≥m˙choked

限制处压力的表达式仅通过考虑从入口到限制的流通面积收缩的动量平衡获得。

pR=pin−12ρR(m˙ACdSR)2(1+SRS)(1−ρRρinSRS)

局部限制假定为绝热，因此混合物的比总焓相等。因此，混合物比焓的变化为：

hA−hR=(1ρR2SR2−1ρA2S2)m˙A22CD2hB−hR=(1ρR2SR2−1ρB2S2)m˙B22CD2

### 假设和限制

- 该限制是绝热的。它不与环境交换热量。
- 此模块不对超声速流动建模。
