---
type: simulink-block
title: 'Pipe (TL)'
family: 'thermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'pipetl'
documentation_source_path: 'ref/pipetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (TL)

## 端口

### 守恒

### **A** — 入口或出口热液体

与管入口或出口相关联的热液体守恒端口。
此模块没有固有方向性。

### **B** — 入口或出口热液体

与管入口或出口相关联的热液体守恒端口。
此模块没有固有方向性。

### **H** — 管壁温度热

与管壁温度相关联的热守恒端口。此温度可能不同于管内部热液体的温度。

## 参数

### 几何

### **Pipe length** — 管的长度 `5 m`（默认）

管沿流动方向的长度。

### **Cross-sectional area** — 管的内横截面积 `0.01 m^2`（默认）

垂直于流动方向的管内横截面积。

### **Hydraulic diameter** — 具有相同横截面积的等效圆柱管直径 `0.1128 m`（默认）

具有相同横截面积的等效圆柱管直径。

### 摩擦与传热

### **Aggregate equivalent length of local resistances** — 管中存在的所有局部阻力的总长度 `1 m`（默认）

管中存在的所有局部阻力的总长度。局部阻力包括弯头、管件、附件以及管入口和出口。局部阻力的作用是增加管段的有效长度。仅在进行摩擦计算时，将此长度加到几何管长上。管内的液体体积仅取决于由 **Pipe length** 参数定义的管几何长度。

### **Internal surface absolute roughness** — 管内表面所有表面缺陷的平均深度 `15e-6 m`（默认）

管内表面所有表面缺陷的平均深度，它会影响湍流流态中的压力损失。

### **Laminar flow upper Reynolds number limit** — 高于该 Reynolds 数时流动开始从层流转变为湍流 `2000`（默认）

高于该 Reynolds 数时流动开始从层流转变为湍流。该数等于对应于充分发展层流的最大 Reynolds 数。

### **Turbulent flow lower Reynolds number limit** — 低于该 Reynolds 数时流动开始从湍流转变为层流 `4000`（默认）

低于该 Reynolds 数时流动开始从湍流转变为层流。该数等于对应于充分发展湍流的最小 Reynolds 数。

### **Shape factor for laminar flow viscous friction** — 管几何形状对黏性摩擦损失的影响 `64`（默认）

无量纲因子，用于编码管横截面几何形状对层流流态中黏性摩擦损失的影响。典型值为：圆形横截面为 64，方形横截面为 57，长宽比为 2 的矩形横截面为 62，薄环形横截面为 96 [1]。

### **Nusselt number for laminar flow heat transfer** — 对流换热与导热之比 `3.66`（默认）

层流流态中对流换热与导热之比。其值取决于管横截面几何形状和管壁热边界条件，例如恒定温度或恒定热流。典型值为 3.66，适用于具有恒定壁温的圆形横截面 [2]。

### 效应与初始条件

### **Enable dynamic compressibility** — 选择是否对流体动态可压缩性建模 `On`（默认） | `Off`

选择是否考虑液体的动态可压缩性。动态可压缩性使液体密度依赖于压力和温度，从而影响系统在小时间尺度上的瞬态响应。

### **Enable fluid inertia** — 选择是否对流体惯性建模 `Off`（默认） | `On`

选择是否考虑液体的流动惯性。流动惯性使液体对质量流量的变化具有阻力。

#### 依赖关系

要启用此复选框，请选中 **Enable dynamic compressibility** 复选框。

### **Initial liquid pressure** — 时间零点的液体压力 `0.101325 MPa`（默认）

仿真开始时管中的液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。

### **Initial liquid temperature** — 时间零点的液体温度 `293.15 K`（默认）

仿真开始时管中的液体温度。

### **Nominal liquid pressure** — 标称工况下的液体压力 `0.101325 MPa`（默认）

标称工况下的热液体压力。当动态可压缩性被禁用时，模块使用此值计算标称密度，以用于质量和能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid temperature** — 标称工况下的液体温度 `293.15 K`（默认）

标称工况下的热液体温度。当动态可压缩性被禁用时，模块使用此值计算标称密度，以用于质量和能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial mass flow rate from port A to port B** — 时间零点的质量流量 `0 kg/s`（默认）

时间零点从端口 **A** 到端口 **B** 的质量流量。

#### 依赖关系

要启用此参数，请选中 **Enable fluid inertia** 复选框。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

热液体系统中用于流体流动的刚性导管

Pipe (TL) 模块表示具有固定液体体积的管段。液体会经历由黏性摩擦引起的压力损失，以及流体与管壁之间由对流引起的传热。黏性摩擦遵循 Darcy-Weisbach 方程，而换热系数遵循 Nusselt 数关联式。

### 管效应

该模块允许包含动态可压缩性和流体惯性效应。启用这些效应中的每一个都可以提高模型保真度，但代价是增加方程复杂性，并可能增加仿真成本：

- 当动态可压缩性为 off 时，液体被假定在管容积中停留的时间可忽略。因此，管中没有质量累积，质量流入等于质量流出。这是最简单的选项。当管中的液体质量占系统总液体质量的比例可忽略时，它是合适的。
- 当动态可压缩性为 on 时，质量流入和质量流出之间的不平衡会导致液体在管中累积或减少。因此，管容积中的压力可以动态上升和下降，这为系统提供一定的顺应性，并调节快速压力变化。这是默认选项。
- 如果动态可压缩性为 on，还可以启用流体惯性。除了由摩擦引起的阻力之外，此效应还会产生额外的流动阻力。该额外阻力与质量流量的变化率成正比。考虑流体惯性会减慢流量的快速变化，但也可能导致流量超调并振荡。此选项适用于非常长的管。启用流体惯性并将多个管段串联连接，以对沿管传播的压力波（例如水锤现象）进行建模。

### 质量平衡

管道的质量守恒方程为

m˙A+m˙B={0,if fluid dynamic compressibility is 'off'Vρ(1βdpdt−αdTdt),if fluid dynamic compressibility is 'on'

其中：

- m˙A 和 m˙B 是通过端口 **A** 和 **B** 的质量流量。
- *V* 是管内流体体积。
- *ρ* 是管内热液体密度。
- *β* 是管内等温体积模量。
- *α* 是管内等压热膨胀系数。
- *p* 是管内热液体压力。
- *T* 是管内热液体温度。

### 动量平衡

下表显示了每个半管的动量守恒方程。

|  |  |
| --- | --- |
| 对于与端口 **A** 相邻的半管 | pA−p={Δpv,A,if fluid inertia is offΔpv,A+L2Sm¨A,if fluid inertia is on |
| 对于与端口 **B** 相邻的半管 | pB−p={Δpv,B,if fluid inertia is offΔpv,B+L2Sm¨B,if fluid inertia is on |

在这些方程中：

- *S* 是管的横截面积。
- *p*、*p*A 和 *p*B 是管内、端口 **A** 和端口 **B** 处的液体压力。
- *Δp*v,A 和 *Δp*v,B 是管容积中心与端口 **A** 和 **B** 之间的黏性摩擦压力损失。

### 黏性摩擦压力损失

下表显示了每个半管的黏性摩擦压力损失方程。

|  |  |
| --- | --- |
| 对于与端口 **A** 相邻的半管 | Δpv,A={λν(L+Leq2)m˙A2D2S,if ReA<RelfA(L+Leq2)m˙A|m˙A|2ρDS2,if ReA≥Ret |
| 对于与端口 **B** 相邻的半管 | Δpv,B={λν(L+Leq2)m˙B2D2S,if ReB<RelfB(L+Leq2)m˙B|m˙B|2ρDS2,if ReB≥Ret |

在这些方程中：

- *λ* 是管形状因子。
- *ν* 是管内热液体的运动黏度。
- *L*eq 是局部管阻力的总等效长度。
- *D* 是管的水力直径。
- *f*A 和 *f*B 是与端口 **A** 和 **B** 相邻的各半管中的 Darcy 摩擦因子。
- ReA 和 *Re*B 是端口 **A** 和 **B** 处的 Reynolds 数。
- Rel 是高于该值时流动开始向湍流转变的 Reynolds 数。
- Ret 是低于该值时流动开始向层流转变的 Reynolds 数。

Darcy 摩擦因子由湍流区的 Haaland 近似公式给出：

f=1[−1.8log10(6.9Re+(13.7rD)1.11)]2,

其中：

- *f* 是 Darcy 摩擦因子。
- *r* 是管表面粗糙度。

### 能量平衡

管道的能量守恒方程为

Vd(ρu)dt=ϕA+ϕB+QH,

其中：

- *Φ*A 和 *Φ*B 是通过端口 **A** 和 **B** 进入管的总能量流率。
- *Q*H 是通过管壁进入管的热流率。

### 壁面热流率

热液体与管壁之间的热流率为：

QH=Qconv+kSHD(TH−T),

其中：

- *Q*H 是净热流率。
- *Q*conv 是在非零流量下归因于对流的那部分热流率。
- *k* 是管内热液体的热导率。
- *S*H 是管壁表面积，即管周长与长度的乘积。
- *T*H 是管壁处的温度。

假设沿管温度呈指数分布，对流换热为

Qconv=|m˙avg|cp,avg(TH−Tin)(1−exp(−hcoeffSH|m˙avg|cp,avg)),

其中：

- m˙avg=(m˙A−m˙B)/2 是从端口 **A** 到端口 **B** 的平均质量流量。
- cpavg 是在平均温度下计算的比热。
- *T*in 是取决于流动方向的入口温度。

换热系数 *h*coeff 取决于 Nusselt 数：

hcoeff=NukavgD,

其中 *k*avg 是在平均温度下计算的热导率。Nusselt 数取决于流态。层流流态中的 Nusselt 数为常数，并等于 **Nusselt number for laminar flow heat transfer** 参数值。湍流流态中的 Nusselt 数由 Gnielinski 关联式计算：

Nutur=favg8(Reavg−1000)Pravg1+12.7favg8(Pravg2/3−1),

其中 *f*avg 是平均 Reynolds 数 *Re*avg 下的 Darcy 摩擦因子，*Pr*avg 是在平均温度下计算的 Prandtl 数。平均 Reynolds 数计算为：

Reavg=|m˙avg|DSμavg,

其中 *μ*avg 是在平均温度下计算的动力黏度。当平均 Reynolds 数介于 **Laminar flow upper Reynolds number limit** 和 **Turbulent flow lower Reynolds number limit** 参数值之间时，Nusselt 数在层流和湍流 Nusselt 数值之间平滑过渡。

### 假设与限制

- 管壁是刚性的。
- 流动是充分发展的。
- 重力效应可忽略。
