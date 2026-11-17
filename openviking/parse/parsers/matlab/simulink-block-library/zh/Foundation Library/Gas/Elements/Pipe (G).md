---
type: simulink-block
title: 'Pipe (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'pipeg'
documentation_source_path: 'ref/pipeg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (G)

## 端口
```yaml
ports:
- name: A
  summary: 入口或出口气体
  direction: conserving
- name: B
  summary: 入口或出口气体
  direction: conserving
- name: H
  summary: 管壁热温度
  direction: conserving
```

### 守恒端口

### **A** — 入口或出口气体

与管道入口或出口关联的气体守恒端口。该模块没有固有方向性。

### **B** — 入口或出口气体

与管道入口或出口关联的气体守恒端口。该模块没有固有方向性。

### **H** — 管壁热温度

与管壁温度关联的热守恒端口。该温度可能与气体体积的温度不同。
## 参数
```yaml
parameters:
- name: Pipe length
  summary: 管道长度 5 m（默认值）
  group: 几何
- name: Cross-sectional area
  summary: 管道内部面积 0.01 m^2（默认值）
  group: 几何
- name: Hydraulic diameter
  summary: 具有相同横截面积的等效圆柱形管道的直径 0.1 m（默认值）
  group: 几何
- name: Aggregate equivalent length of local resistances
  summary: 管道中所有局部阻力的合计长度 0.1 m（默认值）
  group: 摩擦与传热
- name: Internal surface absolute roughness
  summary: 管道内表面所有表面缺陷的平均深度 15e-6 m（默认值）
  group: 摩擦与传热
- name: Laminar flow upper Reynolds number limit
  summary: 流动开始从层流过渡到湍流时的雷诺数 2000（默认值）
  group: 摩擦与传热
- name: Turbulent flow lower Reynolds number limit
  summary: 流动开始从湍流过渡到层流时的雷诺数 4000（默认值）
  group: 摩擦与传热
- name: Shape factor for laminar flow viscous friction
  summary: 管道几何形状对粘性摩擦损失的影响 64（默认值）
  group: 摩擦与传热
- name: Nusselt number for laminar flow heat transfer
  summary: 对流传热与导热传热之比 3.66（默认值）
  group: 摩擦与传热
- name: Enable dynamic compressibility
  summary: 选择是否对气体压力动态建模 On（默认值）| Off
  group: 效应与初始条件
- name: Enable fluid inertia
  summary: 选择是否对气体惯性建模 Off（默认值）| On
  group: 效应与初始条件
- name: Initial pressure
  summary: 仿真开始时的气体压力 0.101325 MPa（默认值）| 正标量
  group: 效应与初始条件
- name: Initial pressure priority
  summary: 压力参数优先级 High（默认值）| Low | None
  group: 效应与初始条件
- name: Initial temperature
  summary: 仿真开始时的温度 293.15 K（默认值）| 正标量
  group: 效应与初始条件
- name: Initial temperature priority
  summary: 温度参数优先级 High（默认值）| Low | None
  group: 效应与初始条件
- name: Nominal pressure
  summary: 标称气体压力 0.101325 MPa（默认值）| 正标量
  group: 效应与初始条件
- name: Nominal temperature
  summary: 标称气体温度 293.15 K（默认值）| 正标量
  group: 效应与初始条件
- name: Initial mass flow rate from port A to port B
  summary: 零时刻的质量流量 0 kg/s（默认值）| 标量
  group: 效应与初始条件
- name: Initial mass flow rate priority
  summary: 质量流量参数优先级 High（默认值）| Low | None
  group: 效应与初始条件
```

### 几何

### **Pipe length** — 管道长度 `5 m`（默认值）

管道沿流动方向的长度。

### **Cross-sectional area** — 管道内部面积 `0.01 m^2`（默认值）

管道垂直于流动方向的内部面积。

### **Hydraulic diameter** — 具有相同横截面积的等效圆柱形管道的直径 `0.1 m`（默认值）

具有相同横截面积的等效圆柱形管道的直径。

### 摩擦与传热

### **Aggregate equivalent length of local resistances** — 管道中所有局部阻力的合计长度 `0.1 m`（默认值）

管道中所有局部阻力的合计长度。局部阻力包括弯头、管件、附件以及管道入口和出口。局部阻力的作用是增加管段的等效长度。该长度仅在摩擦计算中加到管道几何长度上。气体体积仅取决于由 **Pipe length** 参数定义的管道几何长度。

### **Internal surface absolute roughness** — 管道内表面所有表面缺陷的平均深度 `15e-6 m`（默认值）

管道内表面所有表面缺陷的平均深度，它会影响湍流流态下的压力损失。

### **Laminar flow upper Reynolds number limit** — 流动开始从层流过渡到湍流时的雷诺数 `2000`（默认值）

流动开始从层流过渡到湍流时的雷诺数。该数值等于充分发展层流所对应的最大雷诺数。

### **Turbulent flow lower Reynolds number limit** — 流动开始从湍流过渡到层流时的雷诺数 `4000`（默认值）

流动开始从湍流过渡到层流时的雷诺数。该数值等于充分发展湍流所对应的最小雷诺数。

### **Shape factor for laminar flow viscous friction** — 管道几何形状对粘性摩擦损失的影响 `64`（默认值）

无量纲因子，用于表征管道横截面几何形状对层流流态下粘性摩擦损失的影响。典型值为：圆形横截面为 64，方形横截面为 57，长宽比为 2 的矩形横截面为 62，薄环形横截面为 96 [1]。

### **Nusselt number for laminar flow heat transfer** — 对流传热与导热传热之比 `3.66`（默认值）

层流流态下对流传热与导热传热之比。其值取决于管道横截面几何形状和管壁热边界条件，例如恒定温度或恒定热通量。典型值为 3.66，对应于恒定壁温的圆形横截面 [2]。

### 效应与初始条件

### **Enable dynamic compressibility** — 选择是否对气体压力动态建模 `On`（默认值）| `Off`

选择是否考虑气体的动态可压缩性。动态可压缩性使气体密度依赖于压力，从而影响系统在小时间尺度上的瞬态响应。如果您希望在仿真期间快速达到稳态或简化模型初始化，请禁用动态可压缩性。

### **Enable fluid inertia** — 选择是否对气体惯性建模 `Off`（默认值）| `On`

选择是否考虑气体流动惯性。流动惯性提供对质量流量变化的阻力。

#### 依赖关系

要启用此复选框，请选中 **Enable dynamic compressibility** 复选框。

### **Initial pressure** — 仿真开始时的气体压力 `0.101325 MPa`（默认值）| 正标量

仿真开始时的气体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。如果该模块不对动态可压缩性建模，则不需要初始气体压力的值。

### **Initial pressure priority** — 压力参数优先级 `High`（默认值）| `Low` | `None`

求解器在初始化模块时分配给 **Initial pressure** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认值）| 正标量

初始气体温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认值）| `Low` | `None`

求解器在初始化模块时分配给 **Initial temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **Nominal pressure** — 标称气体压力 `0.101325 MPa`（默认值）| 正标量

标称气体压力。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal temperature** — 标称气体温度 `293.15 K`（默认值）| 正标量

标称气体温度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial mass flow rate from port A to port B** — 零时刻的质量流量 `0 kg/s`（默认值）| 标量

零时刻从端口 **A** 到端口 **B** 的质量流量。

#### 依赖关系

要启用此参数，请选中 **Enable fluid inertia** 复选框。

### **Initial mass flow rate priority** — 质量流量参数优先级 `High`（默认值）| `Low` | `None`

求解器在初始化模块时分配给 **Initial mass flow rate from port A to port B** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请选中 **Enable fluid inertia** 复选框。
## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2025a：可选的动态可压缩性和流体惯性建模

两个新复选框 **Enable dynamic compressibility** 和 **Enable fluid inertia** 提供了对气体动态可压缩性和惯性建模的选项。模块参数化选项也已更改。现在，您不再为模块变量指定初始目标，而是在 **Effects and Initial Conditions** 部分中指定初始参数值和优先级。

### R2024a：管道低流量计算的数值改进

为了提高低速流动时管道内压降的精度，Pipe (G) 模块中的动量平衡计算已略有更改。与之前的版本相比，仿真结果可能会有细微差异，尤其是在马赫数较低时。

## 描述

用于气体流动的刚性管道

Pipe (G) 模块对气体管网中的管道流动动力学进行建模。该模块考虑了粘性摩擦损失以及与管壁的对流传热。管道内包含恒定体积的气体。压力和温度基于该气体体积的可压缩性和热容量演化。当出口达到声速条件时，发生阻塞。

**注意**

通过该模块的气体流动可能发生阻塞。如果连接到 Pipe (G) 模块的 Mass Flow Rate Source (G) 模块或 Controlled Mass Flow Rate Source (G) 模块指定的质量流量大于可能发生阻塞的质量流量，则会出现仿真错误。有关详细信息，请参阅阻塞流。

### 质量平衡

质量守恒将质量流量与代表气体体积的内部节点的压力和温度动力学联系起来。当您选中 **Enable dynamic compressibility** 时，质量平衡为

∂M∂p⋅dpIdt+∂M∂T⋅dTIdt=m˙A+m˙B

其中：

- ∂M∂p 是气体体积的质量在恒定温度和体积下对压力的偏导数。
- ∂M∂T 是气体体积的质量在恒定压力和体积下对温度的偏导数。
- *p*I 是气体体积的压力。
- *T*I 是气体体积的温度。
- *t* 是时间。
- m˙A 和 m˙B 分别是端口 A 和 B 处的质量流量。与端口相关的流量在流入模块时为正。

当您清除 **Enable dynamic compressibility** 复选框时，流入管道的质量等于流出管道的质量

m˙A+m˙B=0

### 能量平衡

能量守恒将能量和热流量与代表气体体积的内部节点的压力和温度动力学联系起来。当您选中 **Enable dynamic compressibility** 时，能量平衡为

∂U∂p⋅dpIdt+∂U∂T⋅dTIdt=ΦA+ΦB+QH

其中：

- ∂U∂p 是气体体积的内能在恒定温度和体积下对压力的偏导数。
- ∂U∂T 是气体体积的内能在恒定压力和体积下对温度的偏导数。
- *Φ*A 和 *Φ*B 分别是端口 **A** 和 **B** 处的能量流量。
- *Q*H 是端口 **H** 处的热流量。

当您清除 **Enable dynamic compressibility** 复选框时，能量平衡为

ρ0⋅cp⋅V⋅dTdt=ΦA+ΦB+QH

其中：

- *cp* 是气体比热。
- *V* 是管道体积。
- *ρ0* 是气体密度。该模块根据 **Nominal liquid temperature** 和 **Nominal liquid pressure** 参数计算此常数值。

### 完全气体和半完全气体模型的偏导数

气体体积的质量 *M* 和内能 *U* 在恒定体积下对压力和温度的偏导数取决于气体属性模型。对于完全气体和半完全气体模型，方程为：

∂M∂p=VρIpI∂M∂T=−VρITI∂U∂p=V(hIZRTI−1)∂U∂T=VρI(cpI−hITI)

其中：

- *ρ*I 是气体体积的密度。
- *V* 是气体体积。
- *h*I 是气体体积的比焓。
- *Z* 是压缩因子。
- *R* 是比气体常数。
- *c*pI 是气体体积的定压比热。

### 真实气体模型的偏导数

对于真实气体模型，气体体积的质量 *M* 和内能 *U* 在恒定体积下对压力和温度的偏导数为：

∂M∂p=VρIβI∂M∂T=−VρIαI∂U∂p=V(ρIhIβI−TIαI)∂U∂T=VρI(cpI−hIαI)

其中：

- *β* 是气体体积的等温体积模量。
- *α* 是气体体积的等压热膨胀系数。

### 动量平衡

管道每一半的动量平衡对由动量通量和粘性摩擦引起的压降进行建模。如果管道不建模流体惯性，则管道每一半的动量平衡为

pA−pI=(m˙AS)2⋅(1ρI−1ρA)+ΔpAIpB−pI=(m˙BS)2⋅(1ρI−1ρB)+ΔpBI

其中：

- *p* 是端口 **A**、端口 **B** 或内部节点 I 处的气体压力，由下标指示。
- *ρ* 是端口 **A**、端口 **B** 或内部节点 I 处的密度，由下标指示。
- *S* 是管道的横截面积。
- *Δp*AI 和 *Δp*BI 是由粘性摩擦引起的压力损失。

当您选中 **Enable fluid inertia** 时，管道每一半的动量平衡增加一个惯性项

pA−pI=(m˙AS)2⋅(1ρI−1ρA)+ΔpAI+inertiaApB−pI=(m˙BS)2⋅(1ρI−1ρB)+ΔpBI+inertiaB

inertiaA=L2S⋅dm˙AdtinertiaB=L2S⋅dm˙Bdt

其中 *L* 是管道长度。

通过端口 **H** 与管壁交换的热量通过能量守恒方程添加到由内部节点代表的气体体积的能量中（请参阅能量平衡）。因此，管道每一半（端口 **A** 与内部节点之间以及端口 **B** 与内部节点之间）的动量平衡假定为绝热过程。绝热关系为：

hA+12(m˙AρAS)2=hI+12(m˙AρIS)2hB+12(m˙BρBS)2=hI+12(m˙BρIS)2

其中 *h* 是端口 **A**、端口 **B** 或内部节点 I 处的比焓，由下标指示。

由粘性摩擦引起的压力损失 *Δp*AI 和 *Δp*BI 取决于流态。管道每一半的雷诺数定义为：

ReA=|m˙A|⋅DhS⋅μIReB=|m˙B|⋅DhS⋅μI

其中：

- *D*h 是管道的水力直径。
- *μ*I 是内部节点处的动力粘度。

如果雷诺数小于 **Laminar flow upper Reynolds number limit** 参数值，则流动处于层流流态。如果雷诺数大于 **Turbulent flow lower Reynolds number limit** 参数值，则流动处于湍流流态。

在层流流态中，由粘性摩擦引起的压力损失为：

ΔpAIlam=fshapem˙A⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2ΔpBIlam=fshapem˙B⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2

其中：

- *f*shape 是 **Shape factor for laminar flow viscous friction** 参数值。
- *L*eqv 是 **Aggregate equivalent length of local resistances** 参数值。

在湍流流态中，由粘性摩擦引起的压力损失为：

ΔpAItur=fDarcyAm˙A⋅|m˙A|2ρI⋅Dh⋅S2⋅L+Leqv2ΔpBItur=fDarcyBm˙B⋅|m˙B|2ρI⋅Dh⋅S2⋅L+Leqv2

其中 *f*Darcy 是端口 **A** 或 **B** 处的 Darcy 摩擦因子，由下标指示。

Darcy 摩擦因子根据 Haaland 关联式计算：

fDarcyA=[−1.8log10(6.9ReA+(εrough3.7Dh)1.11)]−2fDarcyB=[−1.8log10(6.9ReB+(εrough3.7Dh)1.11)]−2

其中 *ε*rough 是 **Internal surface absolute roughness** 参数值。

当雷诺数介于 **Laminar flow upper Reynolds number limit** 和 **Turbulent flow lower Reynolds number limit** 参数值之间时，流动处于层流和湍流之间的过渡状态。过渡区域中由粘性摩擦引起的压力损失在层流流态和湍流流态之间平滑连接。

### Convective Heat Transfer

管壁与内部气体体积之间的对流传热方程为：

QH=Qconv+kISsurfDh(TH−TI)

*S*surf 是管道表面积，
*S*surf =
4*S**L*/*D*h。
假设沿管道温度呈指数分布，对流传热为

Qconv=|m˙avg|cpavg(TH−Tin)(1−exp(−hcoeffSsurf|m˙avg|cpavg))

其中：

- *T*in 是入口温度，取决于流动方向。
- m˙avg=(m˙A−m˙B)/2 是从端口 **A** 到端口 **B** 的平均质量流量。
- cpavg 是在平均温度下计算的比热。

传热系数 *h*coeff 取决于努塞尔数：

hcoeff=NukavgDh

其中 *k*avg 是在平均温度下计算的热导率。努塞尔数取决于流态。层流流态下的努塞尔数为常数，等于 **Nusselt number for laminar flow heat transfer** 参数的值。湍流流态下的努塞尔数由 Gnielinski 关联式计算：

Nutur=fDarcy8(Reavg−1000)Pravg1+12.7fDarcy8(Pravg2/3−1)

其中 *Pr*avg 是在平均温度下计算的普朗特数。平均雷诺数为

Reavg=|m˙avg|DhSμavg

其中 *μ*avg 是在平均温度下计算的动力黏度。当平均雷诺数介于 **Laminar flow upper Reynolds number limit** 和 **Turbulent flow lower Reynolds number limit** 参数值之间时，努塞尔数在层流和湍流努塞尔数值之间平滑过渡。

### Choked Flow

管道在端口 **A** 和 **B** 处的阻塞质量流量为：

m˙Achoked=ρA⋅aA⋅Sm˙Bchoked=ρB⋅aB⋅S

其中 *a*A 和 *a*B 分别是端口 **A** 和 **B** 处的声速。

端口 **A** 或 **B** 处的未阻塞压力是该端口对应 Across 变量的值：

pAunchoked=A.ppBunchoked=B.p

端口 **A** 和 **B** 处的阻塞压力通过将阻塞质量流量代入管道动量平衡方程得到：

pAchoked=pI+(m˙AchokedS)2⋅(1ρI−1ρA)+ΔpAIchokedpBchoked=pI+(m˙BchokedS)2⋅(1ρI−1ρB)+ΔpBIchoked

*Δp*AIchoked 和 *Δp*BIchoked 是假设发生阻塞时由黏性摩擦引起的压力损失。它们的计算方式类似于 *Δp*AI 和 *Δp*BI，只是将端口 **A** 和 **B** 处的质量流量替换为阻塞质量流量值。

根据是否发生阻塞，模块将阻塞或未阻塞压力值指定为端口的实际压力。阻塞可能发生在管道出口，但不会发生在管道入口。因此，如果 *p*Aunchoked ≥ *p*I，则端口 **A** 是入口，且 *p*A = *p*Aunchoked。如果 *p*Aunchoked < *p*I，则端口 **A** 是出口，且

pA={pAunchoked,if pAunchoked≥pAchokedpAchoked,if pAunchoked<pAchoked

类似地，如果 *p*Bunchoked ≥ *p*I，则端口 **B** 是入口，且 *p*B = *p*Bunchoked。如果 *p*Bunchoked < *p*I，则端口 **B** 是出口，且

pB={pBunchoked,if pBunchoked≥pBchokedpBchoked,if pBunchoked<pBchoked

### 假设和限制

- 管壁完全刚性。
- 流动充分发展。摩擦损失和传热不包括入口效应。
- 重力影响可忽略。
- 该模块不模拟超声速流动。
