---
type: simulink-block
title: 'E-NTU Heat Transfer'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'entuheattransfer'
documentation_source_path: 'ref/entuheattransfer.html'
language: zh-CN
chinese_source: worker-translation
---

# E-NTU Heat Transfer

## 端口
```yaml
ports:
- name: C1
  summary: 流体 1 热容量的物理信号
  direction: input
- name: C2
  summary: 流体 2 热容量的物理信号
  direction: input
- name: HC1
  summary: 流体 1 传热系数的物理信号
  direction: input
- name: HC2
  summary: 流体 2 传热系数的物理信号
  direction: input
- name: H1
  summary: 流体 1 热入口温度的热学端口
  direction: input
- name: H2
  summary: 流体 2 热入口温度的热学端口
  direction: input
```

### 输入

### **C1** — 流体 1 热容量的物理信号

流体 1 热容量的物理信号输入端口。
热容量是质量流量乘以流体的比热系数。

### **C2** — 流体 2 热容量的物理信号

流体 2 热容量的物理信号输入端口。
热容量是质量流量乘以流体的比热系数。

### **HC1** — 流体 1 传热系数的物理信号

流体 1 与界面壁之间传热系数的物理信号输入端口。

### **HC2** — 流体 2 传热系数的物理信号

流体 2 与界面壁之间传热系数的物理信号输入端口。
### 守恒

### **H1** — 流体 1 热入口温度的热学端口

与流体 1 入口温度关联的热学守恒端口。

### **H2** — 流体 2 热入口温度的热学端口

与流体入口温度关联的热学守恒端口。
## 参数
```yaml
parameters:
- name: Flow arrangement
  summary: 换热器中流动对齐的方式 Parallel or counter flow（默认）| Shell and tube | Cross flow | Generic — effectiveness table
  group: ''
- name: Wall thermal resistance
  summary: 壁对热传导热流的阻力 0 K/W（默认）| 正标量
  group: ''
- name: Number of shell passes
  summary: 流体在离开前穿过壳程的次数 1（默认）| 正标量
  group: ''
- name: Cross flow type
  summary: 每个流道中的混合条件 Both fluids mixed（默认）| Both fluids unmixed | Controlled Fluid 1 mixed & Controlled Fluid 2 unmixed |
    Controlled Fluid 1 unmixed & Controlled Fluid 2 mixed
  group: ''
- name: Number of heat transfer units vector, NTU
  summary: 换热器效能查找表中每个断点处的传热单元数 [.5, 1, 2, 3, 4, 5]（默认）| 正标量向量
  group: ''
- name: Thermal capacity ratio vector, CR
  summary: 换热器效能查找表中每个断点处的热容量比 [0, .25, .5, .75, 1]（默认）| 正标量向量
  group: ''
- name: Effectiveness table, E(NTU,CR)
  summary: 换热器效能查找表中在传热单元数和热容量比上每个断点处的换热器效能 [.3, .3, .3, .3, .3; .6, .55, .5, .47, .43; .85, .76, .68, .61, .55; .94, .83,
    .72, .65, .58; .98, .86, .75, .66, .58; .99, .86, .75, .66, .58]（默认）| 正标量表格
  group: ''
- name: Enable wall thermal mass
  summary: 对壁热质量建模的选项 off（默认）| on
  group: ''
- name: Wall mass
  summary: 换热器壁质量 1 kg（默认）| 正标量
  group: ''
- name: Wall specific heat
  summary: 换热器壁比热 490 J/(K*kg)（默认）| 正标量
  group: ''
- name: Heat transfer surface area
  summary: 受控流体 1 侧的聚合计热表面积 0.01 m^2（默认）| 正标量
  group: Controlled Fluid 1
- name: Fouling factor
  summary: 由污垢沉积引起的热阻度量 1e-4 K*m^2/W（默认）| 正标量
  group: Controlled Fluid 1
- name: Minimum fluid-wall heat transfer coefficient
  summary: 传热系数的下界 1 W/(m^2 * K)（默认）| 正标量
  group: Controlled Fluid 1
- name: Heat transfer surface area
  summary: 受控流体 2 侧的聚合计热表面积 0.01 m^2（默认）| 正标量
  group: Controlled Fluid 2
- name: Fouling factor
  summary: 由污垢沉积引起的热阻度量 1e-4 K*m^2/W（默认）| 正标量
  group: Controlled Fluid 2
- name: Minimum fluid-wall heat transfer coefficient
  summary: 传热系数的下界 1 W/(m^2 * K)（默认）| 正标量
  group: Controlled Fluid 2
```

### **Flow arrangement** — 换热器中流动对齐的方式 `Parallel or counter flow`（默认）| `Shell and tube` | `Cross flow` | `Generic — effectiveness table`

换热器几何结构。选择 `Generic —
effectiveness table` 以基于表格化的效能数据对其他换热器几何结构进行建模。

在 `Parallel or counter flow` 配置中，流体 1 和流体 2 的相对流动方向决定了换热器是基于平行流还是逆流。流动方向取决于 Simscape
Fluids™ 模型的其余部分。

### **Wall thermal resistance** — 壁对热传导热流的阻力 `0 K/W`（默认）| 正标量

分隔两种换热器流体的界面壁的热阻。

### **Number of shell passes** — 流体在离开前穿过壳程的次数 `1`（默认）| 正标量

流体在离开前穿过壳程的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为
`Shell and tube`。

### **Cross flow type** — 每个流道中的混合条件 `Both fluids mixed`（默认）| `Both fluids unmixed` | `Controlled Fluid 1 mixed & Controlled Fluid 2 unmixed` | `Controlled Fluid 1 unmixed & Controlled Fluid 2 mixed`

流体混合配置。流体可以是混合的或未混合的。模块使用混合配置来确定使用哪些经验传热关联式。混合流意味着流体在沿流动路径行进时可以自由地沿横向移动。未混合流意味着流体被限制为仅沿流动路径行进。例如，带翅片的一侧被视为未混合流。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为
`Cross flow`。

### **Number of heat transfer units vector, NTU** — 换热器效能查找表中每个断点处的传热单元数 `[.5, 1, 2, 3, 4, 5]`（默认）| 正标量向量

用于指定效能表格数据的 *M* 元素 NTU 值向量。传热单元数（NTU）是一个无量纲参数，定义为

NTU=AsUCmin，

其中：

- *A*S 是传热表面积。
- *U* 是总传热系数。
- *C*min 是热流体和冷流体热容量中的较小值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为
`Generic — effectiveness
table`。

### **Thermal capacity ratio vector, CR** — 换热器效能查找表中每个断点处的热容量比 `[0, .25, .5, .75, 1]`（默认）| 正标量向量

用于指定效能表格数据的 *N* 元素热容量比向量。热容量比是分数

Cr=CminCmax，

其中 *C*min 和
*C*max 分别是最小和最大热容量。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为
`Generic — effectiveness
table`。

### **Effectiveness table, E(NTU,CR)** — 换热器效能查找表中在传热单元数和热容量比上每个断点处的换热器效能 `[.3, .3, .3, .3, .3; .6, .55, .5, .47, .43; .85, .76, .68, .61, .55; .94, .83, .72, .65, .58; .98, .86, .75, .66, .58; .99, .86, .75, .66, .58]`（默认）| 正标量表格

包含换热器效能值的 *M*×*N* 矩阵。矩阵行对应于 **Number of heat transfer units vector,
NTU** 参数中指定的不同值。矩阵列对应于 **Thermal capacity ratio vector, CR**
参数中指定的值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为
`Generic — effectiveness
table`。

### **Enable wall thermal mass** — 对壁热质量建模的选项 `off`（默认）| `on`

是否对换热器壁热质量建模。对壁热质量建模会在壁对温度或热流变化的热瞬态响应中引入延迟。如果清除 **Enable wall thermal
mass**，模块会假定壁足够薄，以至于在传热的时间尺度上瞬态响应是即时的。

### **Wall mass** — 换热器壁质量 `1 kg`（默认）| 正标量

换热器壁的质量。模块使用此值计算壁热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 换热器壁比热 `490 J/(K*kg)`（默认）| 正标量

换热器壁的比热。模块使用此值计算壁热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### Controlled Fluid 1

### **Heat transfer surface area** — 受控流体 1 侧的聚合计热表面积 `0.01 m^2`（默认）| 正标量

流体 1 侧用于冷热流体之间传热的聚合表面积。

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W`（默认）| 正标量

用于量化传热表面上污垢沉积导致的热阻增加的经验参数。

### **Minimum fluid-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)`（默认）| 正标量

允许的最小传热系数值。通过物理信号端口 HC1 指定的传热系数在此值处饱和。模块使用传热系数计算流体 1 和流体 2 之间的传热速率，如传热速率中所述。

### Controlled Fluid 2

### **Heat transfer surface area** — 受控流体 2 侧的聚合计热表面积 `0.01 m^2`（默认）| 正标量

流体 2 侧用于冷热流体之间传热的聚合表面积。

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W`（默认）| 正标量

用于量化传热表面上污垢沉积导致的热阻增加的经验参数。

### **Minimum fluid-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)`（默认）| 正标量

允许的最小传热系数值。通过物理信号端口 HC2 指定的传热系数在此值处饱和。模块使用传热系数计算流体 1 和流体 2 之间的传热速率，如传热速率中所述。
## 所属库

Simscape / Fluids / Heat Exchangers / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2025a：对换热器壁的热质量建模

选择 **Wall thermal dynamics** 以对换热器壁的热质量建模。

## 描述

两种通用流体之间的详细传热模型

E-NTU Heat Transfer 模块基于标准效能-NTU 方法对两种通用流体之间的热交换进行建模。流体热物性通过 Simscape™ 物理信号显式指定。与 Heat Exchanger Interface (TL) 或 Heat Exchanger Interface
(G) 模块结合使用，以对换热器入口和出口之间的压降和温度变化进行建模。

模块对话框提供常见换热器配置的选择。这些配置包括具有平行流和逆流的同心管、具有一个或多个壳程的管壳式，以及具有混合流和未混合流的交叉流。通用配置允许您基于表格化效能数据对其他换热器进行建模。

**换热器配置**

### 传热速率

E-NTU 模型以效能参数 *ε* 定义流体 1 和流体 2 之间的传热速率

Q=ϵQMax,0<ε<1，

其中：

- *Q* 是净传热速率。
- *Q*Max 是在给定一组运行条件下流体 1 和流体 2 之间可能的最大传热速率。
- *ε* 是效能参数。

如果清除 **Enable wall thermal mass** 复选框，

−Q1=Q2=Q，

其中 *Q*1 和
*Q*2 是进入流体 1 和流体 2 的传热速率。

两种流体之间可能的最大传热速率为

QMax=CMin(T1,In−T2,In)，

其中：

- *C*Min 是热容量的最小值：

  CMin=min(m˙1cp,1,m˙2cp,2)
- *T*1,In 和
  *T*2,In 是流体 1 和流体 2 的入口温度。
- m˙1 和 m˙2 是通过入口进入换热器体积的流体 1 和流体 2 的质量流量。
- *c*p,1 和
  *c*p,2 是流体 1 和流体 2 的定压比热系数。模块对话框中的 **Minimum fluid-wall heat transfer coefficient**
  参数为允许的传热系数值设置下界。

模块在传热计算中使用的流体物性是入口处的值与流体体积中的值之间的平均值。

### 换热器效能

换热器效能计算取决于模块对话框中选择的流动布置类型。对于除 `Generic —
effectiveness table` 之外的所有类型，模块通过以传热单元数（NTU）和热容量比表示的解析表达式计算热交换效能。传热单元数定义为

NTU=UOverallAHeatCMin=1CMinROverall，

其中：

- *NTU* 是传热单元数。
- *U*Overall 是流体 1 和流体 2 之间的总传热系数。
- *R*Overall 是流体 1 和流体 2 之间的总热阻。
- *A*Heat 是一次和二次（即翅片）传热表面的聚合面积。

热容量比定义为

Crel=CMinCMax

其中：

- *C*rel 是热容量比。

NTU 计算中使用的总传热系数和热阻是起作用传热机制的函数。这些机制包括流体与换热器界面之间的对流传热以及通过界面壁的传导 [2]：

ROverall=1UOverallAHeat=1U1A1+RFoul,1+RWall+RFoul,2+1U2A2，

其中：

- *U*1 和
  *U*2 是流体 1 与界面壁之间以及流体 2 与界面壁之间的传热系数。
- *A*1 和
  *A*2 是流体 1 侧和流体 2 侧的传热表面积。
- *R*Foul,1 和
  *R*Foul,2 是流体 1 侧和流体 2 侧的污垢热阻。污垢热阻等于污垢系数参数除以传热表面积。
- *R*Wall 是界面壁热阻。

**从流体 1 到流体 2 的传热**

这些表格显示了用于计算热交换效能的一些解析表达式 [1]。
参数 *N* 指壳程数，参数 *ε*1 指单个壳程的效能。

|  |  |
| --- | --- |
| **Concentric Tubes** | |
| Counter Flow | ε={1−exp[−NTU(1−Crel)]1−Crelexp[−NTU(1−Crel)],if Crel<1NTU1+NTU,if Crel=1 |
| Parallel Flow | ε=1−exp[−NTU(1+Crel)]1+Crel |
| **Shell and Tube** | |
| One shell pass and two, four, or six tube passes | ε1=21+Crel+1+Crel21+exp(−NTU1+Crel2)1−exp(−NTU1+Crel2) |
| *N* Shell Passes and 2*N*, 4*N*, or 6*N* Tube Passes | ε=[(1−ε1Crel)/(1−ε1)]N−1[(1−ε1Crel)/(1−ε1)]N−Crel |
| **Cross Flow (Single Pass)** | |
| Both Fluids Unmixed | ε=1−exp(exp(−CrelNTU0.78)−1CrelNTU−0.22) |
| Both Fluids Mixed | ε=111−exp(−NTU)+Crel1−exp(−CrelNTU)−1NTU |
| *C*Max mixed, *C*Min unmixed | ε=1Crel(1−exp(−Crel(1−exp(−NTU)))) |
| *C*Max unmixed, *C*Min mixed | ε=1−exp(−1Crel(1−exp(−CrelNTU))) |

### 壁热质量

如果选择 **Enable wall thermal mass**，模块会对换热器壁热质量建模，这会在壁对温度或热流变化的热瞬态响应中引入延迟。如果对热质量建模，壁会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流速率平衡为止。

如果选择 **Enable wall thermal mass**，壁能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall
  mass** 参数的值。
- *cp,wall* 是
  **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁温。模块使用此值对瞬态响应建模。您无法测量此值。

传递到每种流体的热量为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容量。

每一侧流体与壁之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁表面积，*U* 是传热系数。
