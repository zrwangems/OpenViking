---
type: simulink-block
title: 'Pipe (TL)'
family: 'simscape'
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

### 守恒端口

### **A** — 入口或出口热液体

与管道入口或出口相关联的热液体守恒端口。
该模块没有固有的方向性。

### **B** — 入口或出口热液体

与管道入口或出口相关联的热液体守恒端口。
该模块没有固有的方向性。

### **H** — 管壁温度热端口

与管壁温度相关联的热守恒端口。该温度可能不同于管道内热液体的温度。

## 参数

### 几何

### **Pipe length** — 管道长度 `5 m`（默认值）

管道沿流动方向的长度。

### **Cross-sectional area** — 管道内部面积 `0.01 m^2`（默认值）

管道垂直于流动方向的内部面积。

### **Hydraulic diameter** — 具有相同横截面积的等效圆柱形管道直径 `0.1128 m`（默认值）

具有相同横截面积的等效圆柱形管道直径。

### 摩擦与传热

### **Aggregate equivalent length of local resistances** — 管道中所有局部阻力的总长度 `1 m`（默认值）

管道中所有局部阻力的总长度。局部阻力包括弯头、管件、附件以及管道入口和出口。局部阻力的作用是增加管段的等效长度。该长度仅在摩擦计算中加到管道几何长度上。管道内的液体体积仅取决于由 **Pipe length** 参数定义的管道几何长度。

### **Internal surface absolute roughness** — 管道内表面所有表面缺陷的平均深度 `15e-6 m`（默认值）

管道内表面所有表面缺陷的平均深度，影响湍流流态下的压力损失。

### **Laminar flow upper Reynolds number limit** — 流动开始从层流过渡到湍流的上限雷诺数 `2000`（默认值）

流动开始从层流过渡到湍流的上限雷诺数。该数值等于完全发展层流对应的最大雷诺数。

### **Turbulent flow lower Reynolds number limit** — 流动开始从湍流过渡到层流的下限雷诺数 `4000`（默认值）

流动开始从湍流过渡到层流的下限雷诺数。该数值等于完全发展湍流对应的最小雷诺数。

### **Shape factor for laminar flow viscous friction** — 管道几何形状对粘性摩擦损失的影响 `64`（默认值）

无量纲因子，用于表征管道横截面几何形状对层流流态下粘性摩擦损失的影响。典型值为：圆形横截面为 64，方形横截面为 57，长宽比为 2 的矩形横截面为 62，薄环形横截面为 96 [1]。

### **Nusselt number for laminar flow heat transfer** — 对流传热与导热传热之比 `3.66`（默认值）

层流流态下对流传热与导热传热之比。其值取决于管道横截面几何形状和管壁热边界条件，例如恒定温度或恒定热通量。典型值为 3.66，适用于恒定壁温的圆形横截面 [2]。

### 效应与初始条件

### **Enable dynamic compressibility** — 选择是否对流体动态可压缩性建模 `On`（默认值） | `Off`

选择是否考虑液体的动态可压缩性。动态可压缩性使液体密度依赖于压力和温度，在小时间尺度上影响系统的瞬态响应。

### **Enable fluid inertia** — 选择是否对流体惯性建模 `Off`（默认）| `On`

选择是否考虑液体的流动惯性。流动惯性使液体对质量流量的变化产生阻力。

#### 依赖关系

要启用此复选框，请选中 **Enable dynamic compressibility** 复选框。

### **Initial liquid pressure** — 零时刻的液体压力 `0.101325 MPa`（默认）

仿真开始时管道中的液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。

### **Initial liquid temperature** — 零时刻的液体温度 `293.15 K`（默认）

仿真开始时管道中的液体温度。

### **Nominal liquid pressure** — 标称工况下的液体压力 `0.101325 MPa`（默认）

标称工况下的热液体压力。当动态可压缩性禁用时，模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid temperature** — 标称工况下的液体温度 `293.15 K`（默认）

标称工况下的热液体温度。当动态可压缩性禁用时，模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial mass flow rate from port A to port B** — 零时刻的质量流量 `0 kg/s`（默认）

零时刻从端口 **A** 到端口 **B** 的质量流量。

#### 依赖关系

要启用此参数，请选中 **Enable fluid inertia** 复选框。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

热液体系统中用于流体流动的刚性导管

Pipe (TL) 模块表示一段具有固定液体体积的管道。液体由于粘性摩擦而经历压力损失，并由于流体与管壁之间的对流而经历热传递。粘性摩擦遵循 Darcy-Weisbach 方程，而热交换系数遵循 Nusselt 数关联式。

### Pipe Effects

该模块允许您包含动态可压缩性和流体惯性效应。开启这些效应中的每一个都可以提高模型保真度，但代价是方程复杂度增加，并可能增加仿真成本：

- 当动态可压缩性关闭时，假设液体在管道体积中停留的时间可以忽略不计。因此，管道中没有质量积聚，质量流入等于质量流出。这是最简单的选项。当管道中的液体质量占系统总液体质量的比例可以忽略不计时，该选项适用。
- 当动态可压缩性开启时，质量流入和质量流出的不平衡会导致液体在管道中积聚或减少。因此，管道体积中的压力会动态上升和下降，这为系统提供了一定的柔量，并调节快速压力变化。这是默认选项。
- 如果动态可压缩性开启，您还可以开启流体惯性。除了由摩擦引起的阻力之外，该效应还会导致额外的流动阻力。该额外阻力与质量流量的变化率成正比。考虑流体惯性会减慢流量的快速变化，但也可能导致流量超调和振荡。该选项适用于非常长的管道。开启流体惯性并串联连接多个管道段，以模拟压力波沿管道传播，例如水锤现象。

### Mass Balance

管道的质量守恒方程为

m˙A+m˙B={0,if fluid dynamic compressibility is 'off'Vρ(1βdpdt−αdTdt),if fluid dynamic compressibility is 'on'

其中：

- m˙A 和 m˙B 是通过端口 **A** 和 **B** 的质量流量。
- *V* 是管道流体体积。
- *ρ* 是管道中的热液体密度。
- *β* 是管道中的等温体积模量。
- *α* 是管道中的等压热膨胀系数。
- *p* 是管道中的热液体压力。
- *T* 是管道中的热液体温度。

### Momentum Balance

下表显示了每个半管道的动量守恒方程。

|  |  |
| --- | --- |
| 对于与端口 **A** 相邻的半管道 | pA−p={Δpv,A,if fluid inertia is offΔpv,A+L2Sm¨A,if fluid inertia is on |
| 对于与端口 **B** 相邻的半管道 | pB−p={Δpv,B,if fluid inertia is offΔpv,B+L2Sm¨B,if fluid inertia is on |

在方程中：

- *S* 是管道横截面积。
- *p*、*p*A 和 *p*B 是管道中、端口 **A** 处和端口 **B** 处的液体压力。
- *Δp*v,A 和 *Δp*v,B 是管道体积中心与端口 **A** 和 **B** 之间的黏性摩擦压力损失。

### Viscous Friction Pressure Losses

下表显示了每个半管道的黏性摩擦压力损失方程。

|  |  |
| --- | --- |
| 对于与端口 **A** 相邻的半管道 | Δpv,A={λν(L+Leq2)m˙A2D2S,if ReA<RelfA(L+Leq2)m˙A|m˙A|2ρDS2,if ReA≥Ret |
| 对于与端口 **B** 相邻的半管道 | Δpv,B={λν(L+Leq2)m˙B2D2S,if ReB<RelfB(L+Leq2)m˙B|m˙B|2ρDS2,if ReB≥Ret |

在方程中：

- *λ* 是管道形状因子。
- *ν* 是管道中热液体的运动黏度。
- *L*eq 是局部管道阻力的总等效长度。
- *D* 是管道的水力直径。
- *f*A 和 *f*B 是与端口 **A** 和 **B** 相邻的管道半段中的 Darcy 摩擦因子。
- ReA 和 *Re*B 是端口 **A** 和 **B** 处的 Reynolds 数。
- Rel 是流动转变为湍流时所高于的 Reynolds 数。
- Ret 是流动转变为层流时所低于的 Reynolds 数。

Darcy 摩擦因子由湍流区域的 Haaland 近似给出：

f=1[−1.8log10(6.9Re+(13.7rD)1.11)]2,

其中：

- *f* 是 Darcy 摩擦因子。
- *r* 是管道表面粗糙度。

### Energy Balance

管道的能量守恒方程为

Vd(ρu)dt=ϕA+ϕB+QH，

其中：

- *Φ*A 和
  *Φ*B 是通过端口 **A** 和 **B** 进入管道的总能量流率。
- *Q*H 是通过管壁进入管道的热流率。

### Wall Heat Flow Rate

热液体与管壁之间的热流率为：

QH=Qconv+kSHD(TH−T)，

其中：

- *Q*H 是净热流率。
- *Q*conv 是在非零流量下归因于对流的热流率部分。
- *k* 是管道中热液体的导热系数。
- *S*H 是管壁的表面积，即管道周长与长度的乘积。
- *T*H 是管壁处的温度。

假设沿管道呈指数温度分布，对流换热为

Qconv=|m˙avg|cp,avg(TH−Tin)(1−exp(−hcoeffSH|m˙avg|cp,avg))，

其中：

- m˙avg=(m˙A−m˙B)/2 是从端口 **A** 到端口 **B** 的平均质量流率。
- cpavg 是在平均温度下评估的比热容。
- *T*in 是取决于流动方向的入口温度。

传热系数 *h*coeff 取决于努塞尔数：

hcoeff=NukavgD，

其中 *k*avg 是在平均温度下评估的导热系数。努塞尔数取决于流态。层流流态下的努塞尔数为常数，等于 **Nusselt number for laminar flow heat transfer** 参数值。湍流流态下的努塞尔数由 Gnielinski 关联式计算：

Nutur=favg8(Reavg−1000)Pravg1+12.7favg8(Pravg2/3−1)，

其中 *f*avg 是在平均雷诺数 *Re*avg 下的达西摩擦因子，*Pr*avg 是在平均温度下评估的普朗特数。平均雷诺数计算为：

Reavg=|m˙avg|DSμavg，

其中 *μ*avg 是在平均温度下评估的动力粘度。当平均雷诺数介于 **Laminar flow upper Reynolds number limit** 和 **Turbulent flow lower Reynolds number limit** 参数值之间时，努塞尔数在层流和湍流努塞尔数值之间平滑过渡。

### 假设和限制

- 管壁是刚性的。
- 流动是充分发展的。
- 重力的影响可忽略不计。
