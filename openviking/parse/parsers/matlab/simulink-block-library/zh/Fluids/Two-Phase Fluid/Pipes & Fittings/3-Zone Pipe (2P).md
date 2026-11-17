---
type: simulink-block
title: '3-Zone Pipe (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Pipes & Fittings'
documentation_page: '3zonepipe2p'
documentation_source_path: 'ref/3zonepipe2p.html'
language: zh-CN
chinese_source: worker-translation
---

# 3-Zone Pipe (2P)

## 端口

### 输出

### **Z** — 区域长度分数物理信号

管道中液相、混合相和汽相区域的长度分数向量。
### 守恒

### **A** — 管道开口两相流体

两相流体流入或流出管道的开口。端口 **A** 和 **B** 均可作为入口或出口。两相流体端口与管道内部流体之间允许热传导（尽管其影响通常仅在接近零流量时相关）。

### **B** — 管道开口两相流体

两相流体流入或流出管道的开口。端口 **A** 和 **B** 均可作为入口或出口。两相流体端口与管道内部流体之间允许热传导（尽管其影响通常仅在接近零流量时相关）。

### **H** — 管壁热

管壁外表面的热边界条件。使用此端口可捕获管壁与环境之间的各种热交换——例如传导、对流或辐射。管壁内表面与流体之间的热交换直接在模块中捕获。

## 参数

### 几何

### **Pipe length** — 管道端口之间的距离 `5 m`（默认）| 带长度单位的正标量

管道端口之间的距离。液相、两相和汽相区域各占此距离的一部分。区域分数可以变化，但其总长度与管道距离相同，是固定的。

### **Cross-sectional area** — 垂直于流动方向的内部面积 `0.01 m^2`（默认）| 带面积单位的正标量

管道垂直于流动方向的内部面积。假设管道横截面沿其长度方向恒定。

### **Hydraulic diameter** — 具有给定横截面积的圆柱形管道的直径 `0.1 m`（默认）| 带长度单位的正标量

管道横截面的开口面积与该面积周长之比。管道不要求为圆柱形，其横截面可以具有任何形状。此参数给出一般横截面若为圆形时所需的直径。

### **Elevation gain from port A to port B** — 恒定管道高程差 `0 m`（默认）| 标量

管道两端的高程差。

### **Gravitational acceleration** — 重力加速度 `9.81 m/s^2`（默认）| 标量

管道环境中的重力加速度。

### 粘性摩擦

### **Aggregate equivalent length of local resistances** — 以长度表示的管道局部压力损失 `1 m`（默认）| 带长度单位的正标量

管道中所有局部阻力的总长度。局部阻力包括弯头、管件、附件以及管道进出口。局部阻力的作用是增加管道的有效长度。此长度在摩擦计算中加到管道几何长度上。

### **Internal surface absolute roughness** — 管道内表面缺陷的平均深度 `15e-6 m`（默认）| 带长度单位的正标量

管道内表面所有表面缺陷的平均深度。表面缺陷影响湍流流态下管道的压力损失。

### **Laminar flow upper Reynolds number limit** — 低于此雷诺数时流动为层流 `2e+3`（默认）| 正无量纲标量

高于此雷诺数时管道流动开始从层流过渡到湍流。此值是对应于充分发展层流的最大雷诺数。

### **Turbulent flow lower Reynolds number limit** — 高于此雷诺数时流动为湍流 `4e+3`（默认）| 正无量纲标量

低于此雷诺数时管道流动开始从湍流过渡到层流。此值是对应于充分发展湍流的最小雷诺数。

### **Shape factor for laminar flow viscous friction** — 用于捕获几何形状对粘性摩擦损失影响的无量纲因子 `64`（默认）| 正无量纲标量

用于捕获横截面几何形状对层流流态中粘性摩擦损失影响的无量纲因子。典型值为：圆形横截面为 `64`，方形横截面为 `57`，长宽比为 2 的矩形横截面为 `62`。

### 传热

### **External environment heat transfer coefficient** — 环境与管壁之间的传热系数 `100 W/(m^2*K)`（默认）| 带功率/(面积\*温度)单位的正标量

环境（在端口 **H** 处）与管壁外表面之间热交换的传热系数。如果此参数设置为 `inf`，则假定环境与管壁之间的热阻为零。此时管壁温度均匀，等于端口 **H** 处的温度。

### **Wall thickness** — 管壁材料的平均厚度 `0 m`（默认）| 带长度单位的正标量

管壁材料的平均厚度。如果此值设置为 `0`，则假定通过管壁传导产生的热阻以及管壁热质量产生的热存储均可忽略不计。

### **Wall thermal conductivity** — 管壁材料的导热系数 `390 W/(m*K)`（默认）| 带功率/(长度\*温度)单位的正标量

管壁材料的导热系数。如果此参数设置为 `inf`，则假定通过管壁传导产生的热阻可忽略不计。

### **Wall specific heat** — 管壁材料单位质量的热容量 `390 J/kg/K`（默认）| 带能量/(质量\*温度)单位的正标量

管壁材料单位质量的热容量。如果此参数设置为 `0`，则假定管道热质量产生的热存储可忽略不计。

### **Wall density** — 管壁材料的质量密度 `9e3 kg/m^3`（默认）| 带质量/体积单位的正标量

管壁材料的质量密度。如果此参数设置为 `0`，则假定管壁热质量产生的热存储可忽略不计。

### **Ratio of external fins surface area to no-fin surface area** — 带外部翅片的传热表面积与无翅片传热表面积之比 `0`（默认）| 正无量纲标量

管壁外侧翅片的总传热表面积与无翅片管壁传热表面积之比。翅片的存在用于增强管壁与环境之间的对流换热。

### **External fin efficiency** — 带外部翅片的实际换热率与理想换热率之比 `0.5`（默认）| 正无量纲标量

外部翅片与环境之间的实际换热率与其理想值（如果翅片完全保持在管壁温度）之比。此参数是翅片几何形状的函数。

### **Ratio of internal fins surface area to no-fin surface area** — 带内部翅片的传热表面积与无翅片传热表面积之比 `0`（默认）| 正无量纲标量

管壁内侧翅片的总传热表面积与无翅片管壁传热表面积之比。翅片的存在用于增强管壁与流体之间的对流换热。

### **Internal fin efficiency** — 内部翅片实际与理想换热率之比 `0.5`（默认）| 正的无量纲标量

内部翅片与环境之间的实际换热率与其理想值（如果翅片完全保持在管壁温度下）之比。此参数是翅片几何形状的函数。

### **Heat transfer coefficient model** — 流体与壁面之间换热系数的计算方法 `Correlation for flow inside tubes`（默认）| `Colburn equation`

计算流体与壁面之间换热系数的方法。可用设置包括：

- `Colburn equation`。使用此设置可通过用户定义的变量 *a*、*b* 和 *c* 计算换热系数。在液相区和气相区，换热系数基于 Colburn 方程。在液-汽混合物区，换热系数基于 Cavallini-Zecchin 方程。
- `Correlation for flow inside tubes`。使用此设置可计算管道流动的换热系数。在液相区和气相区，换热系数使用 Gnielinski 关联式计算。在液-汽混合物区，换热系数使用 Cavallini-Zecchin 方程计算。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid zone** — 液相区 Colburn 方程系数 `[.023, .8, .33]`（默认）| 由正标量组成的三元素向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，模块通过为每个区使用 Colburn 方程来计算该值。Colburn 方程的一般形式为：

Nu=aRebPrc。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** — 混合物区 Cavallini-Zecchin 方程系数 `[.05, .8, .33]`（默认）| 由正标量组成的三元素向量

包含 Cavallini-Zecchin 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，模块在混合物区通过使用 Cavallini-Zecchin 方程来计算该值：

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn)。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone** — 气相区 Colburn 方程系数 `[.023, .8, .33]`（默认）| 由正标量组成的三元素向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，模块通过为每个区使用 Colburn 方程来计算该值。Colburn 方程的一般形式为：

Nu=aRebPrc。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Nusselt number for laminar flow heat transfer** — 层流流态下对流传热与导热换热率之比 `3.66`（默认）

层流流态下对流传热与导热换热率之比。此参数是管道横截面几何形状的函数。典型值为：圆形横截面为 `3.66`，方形横截面为 `2.98`，长宽比为 2 的矩形横截面为 `3.39`。

### Effects and Initial Conditions Tab

### **Initial fluid energy specification** — 要设置其初始值的热力学变量 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于定义组件初始条件的热力学变量。

**Initial fluid energy specification** 参数的值限制了双相流体的可用初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸汽。不能指定液-汽混合物，因为在液-汽混合物区域温度是恒定的。
- `Vapor quality` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液相质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液相质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

### **Initial pressure** — 仿真开始时的绝对压力 `0.101325 MPa`（默认）| 带压力单位的标量

仿真开始时管道中的压力，相对于绝对零压指定。

### **Initial temperature** — 仿真开始时的绝对温度 `293.15 K`（默认）| 带温度单位的标量或二元素向量

仿真开始时管道中的流体温度。此参数可以是标量或二元素向量。如果是标量，则假定初始温度在整个管道内均匀分布。如果是向量，则假定初始温度在端口之间线性变化。向量的第一个元素给出入口处的初始温度，第二个元素给出出口处的初始温度。

#### 依赖关系

当 **Initial fluid energy specification** 选项设置为 `Temperature` 时，此参数处于激活状态。

### **Initial vapor quality** — 仿真开始时的蒸汽质量分数 `0.5`（默认）| 介于 0 和 1 之间的无量纲标量

仿真开始时管道中的蒸汽干度，即蒸汽质量分数。此参数可以是标量或二元素向量。如果是标量，则假定初始蒸汽干度在整个管道内均匀分布。如果是向量，则假定初始蒸汽干度在端口之间线性变化。向量的第一个元素给出入口处的初始蒸汽干度，第二个元素给出出口处的初始蒸汽干度。

#### 依赖关系

当 **Initial fluid energy specification** 选项设置为 `Vapor quality` 时，此参数处于激活状态。

### **Initial vapor void fraction** — 仿真开始时的蒸汽体积分数 `0.5`（默认）| 介于 0 和 1 之间的无量纲标量

仿真开始时管道中的蒸汽空隙率，即蒸汽体积分数。此参数可以是标量或二元素向量。如果是标量，则假定初始蒸汽空隙率在整个管道内均匀分布。如果是向量，则假定初始蒸汽空隙率在端口之间线性变化。向量的第一个元素给出入口处的初始蒸汽空隙率，第二个元素给出出口处的初始蒸汽空隙率。

#### 依赖关系

当 **Initial fluid energy specification** 选项设置为 `Vapor void fraction` 时，此参数处于激活状态。

### **初始比焓** — 仿真开始时的比焓 `1500 kJ/kg`（默认）| 单位为能量/质量的标量

仿真开始时管道中流体的比焓。
此参数可以是标量或 2 元素向量。如果为标量，
则假定初始比焓在整个管道中均匀分布。
如果为向量，则假定初始比焓在端口之间
线性变化。向量的第一个元素给出
入口处的初始比焓，第二个元素给出
出口处的初始比焓。

#### 依赖关系

当 **初始流体能量指定** 选项设置为 `比焓` 时，此参数处于激活状态。

### **初始比内能** — 仿真开始时的比内能 `1500 kJ/kg`（默认）| 单位为能量/质量的标量

仿真开始时管道中流体的比内能。此参数可以是标量或 2 元素向量。如果
为标量，则假定初始比内能在整个管道中
均匀分布。如果为向量，则假定初始比内能在端口之间线性变化。向量的第一个
元素给出入口处的初始比内能，
第二个元素给出出口处的初始比内能。

#### 依赖关系

当 **初始流体能量指定** 选项设置为 `比内能` 时，此参数处于激活状态。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2023b：模型高程增益和静水压力

3-Zone Pipe (2P) 模块现在允许您对高程增益和静水压力进行建模。使用新的 **从端口 A 到端口 B 的高程增益** 和 **重力加速度** 参数来控制这些效应。

### R2022b：使用新的传热系数模型进行参数化

3-Zone Pipe (2P) 模块现在允许您更明确地控制传热过程。您可以将新的 **传热系数模型** 参数设置为：

- `管内流动关联式` — Gnielinski 关联式预测过冷液体或过热蒸汽区域中湍流的传热，Cavallini-Zecchin 关联式预测液-汽混合物区域中湍流的传热。模块预定义系数 *a*、*b* 和 *c*。这是模块在先前版本中的运行方式。
- `Colburn 方程` — 模块允许您通过 **液相区域中 a\*Re^b\*Pr^c 的系数 [a, b, c]**、**混合物区域中 a\*Re^b\*Pr^c 的系数 [a, b, c]** 和 **汽相区域中 a\*Re^b\*Pr^c 的系数 [a, b, c]** 参数为每个流动区域定义系数 *a*、*b* 和 *c*。您将这些参数指定为三元素向量，其中第一个元素是 *a*，第二个是 *b*，第三个是 *c*。

## 描述

两相流体网络中的相变流体管道

3-Zone Pipe (2P) 模块对具有相变流体的管道进行建模。每个流体相称为一个*区域*，它是介于 0 和 1 之间的分数值。区域不会混合。模块使用边界跟随模型来跟踪三个区域中的过冷液体 (L)、汽-液混合物 (M) 和过热蒸汽 (V)。区域在系统中所占的相对空间量称为系统中的*区域长度分数*。

端口 **H** 是表示环境温度的热端口。流体与环境之间的传热速率取决于每个区域的流体相。模块对管壁进行建模，每个区域的管壁温度可能不同。流体动态可压缩性和流体区域热容量影响流体压力和温度。

### 流体与壁面之间的传热

流体与壁面之间的对流换热系数 *αF* 随区域变化，取决于努塞尔数

αF=NukDH，

其中：

- `Nu` 是区域努塞尔数。
- *k* 是平均流体导热系数。
- *DH* 是 **Hydraulic diameter** 参数的值，即非圆管的等效直径。

用于换热系数的努塞尔数取湍流和层流努塞尔数中的较大值。

对于过冷液体或过热蒸汽区域中的湍流，努塞尔数使用 Gnielinski 关联式计算

Nu=f8(Re−1000)Pr1+12.7( f8)1/2(Pr2/3−1)，

其中：

- `Re` 是区域平均雷诺数。
- `Pr` 是区域平均普朗特数。
- *f* 是 Darcy 摩擦因子，由 Haaland 关联式计算

  1f=−1.8log10[(εDH3.7)1.11+6.9Re]，

  其中 *ε* 是 **Internal surface absolute
  roughness** 参数的值。

对于液-汽混合物区域中的湍流，努塞尔数使用 Cavallini-Zecchin 关联式计算

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn)，

其中：

- *ReSL* 是饱和液体的雷诺数。
- *PrSL* 是饱和液体的普朗特数。
- *ρSL* 是饱和液体的密度。
- *ρSV* 是饱和蒸汽的密度。
- *a*= 0.05，*b* = 0.8，*c*= 0.33。

当在管道内表面建模翅片时，换热系数为

αF=NukDH(1+ηIntsInt)，

其中：

- *η*Int 是 **Internal fin efficiency** 参数的值。
- *s*Int 是 **Ratio of internal fins surface area to no-fin surface
  area** 参数的值。

对于层流，努塞尔数是 **Laminar flow
Nusselt number** 参数的值。

**经验努塞尔数公式**

当 **Heat transfer coefficient model** 参数为 `Colburn equation` 时，模块使用经验 Colburn 方程计算过冷液体和过热蒸汽区域的努塞尔数

Nu=aRebPrc，

其中 *a*、*b* 和 *c* 是 **Coefficients [a, b, c] for
a\*Re^b\*Pr^c in liquid zone** 和 **Coefficients [a, b, c]
for a\*Re^b\*Pr^c in vapor zone** 参数中的值。

模块使用 Cavallini-Zecchin 方程计算液-汽混合物区域的努塞尔数，其中的变量来自 **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** 参数。

**比焓**

来自流体的传热速率基于每个区域中比焓的变化

Q=m˙Q(ΔhL+ΔhM+ΔhV)，

其中 m˙Q 是用于传热的质量流量。它是管道入口质量流量，即 m˙A 或 m˙B，取决于流体流动方向。

在液体和蒸汽区域中，比焓变化定义为

Δh=cp(TH−TI)[1−exp(−zSWm˙Qcp(αF−1+αE−1))]，

其中：

- *cp* 是液体或蒸汽的比热。
- *TH* 是环境温度。
- *TI* 是液体入口温度。
- *z* 是流体区域长度分数。
- *αE* 是壁面与环境之间的换热系数。
- *SW* 是壁面表面积

  SW=4ADHL，

  其中：

  - *A* 是 **Cross-sectional area** 参数的值。
  - *L* 是 **Pipe length** 参数的值。

  壁面表面积不包括翅片面积，翅片面积由 **Ratio of external fins surface area to
  no-fin surface area** 和 **Ratio of internal
  fins surface area to no-fin surface area** 参数设置。翅片按壁面表面积的比例设置。值为 `0` 表示管道壁上没有翅片。

在液-汽混合物区域中，比焓变化计算为

Δh=(TH−TS)zSWm˙Q(αF−1+αE−1)，

其中 *TS* 是流体饱和温度。假设液-汽混合物始终处于该温度。

**传热速率**

流体与管壁之间的总传热是各流体相中传热之和

QF=QF,L+QF,V+QF,M。

液体区域中流体与管道之间的传热速率为

QF,L=m˙Qcp,L[TW,L−min(TI,TS)][1−exp(−zLSWαLm˙Qcp,L)]。

其中 *TW,L* 是围绕液体区域的壁面温度。

混合物区域中流体与管道之间的传热速率为

QF,M=(TH−TSat)zMSWαM。

蒸汽区域中流体与管道之间的传热速率为

QF,V=m˙Qcp,V[TW,V−min(TI,TSat)][1−exp(−zVSWαVm˙Qcp,V)]，

其中 *TW,V* 是围绕蒸汽区域的壁面温度。

### 壁面与环境之间的传热

如果管壁具有有限厚度，则壁面与环境之间的换热系数 *αE* 定义为

1αE=1αW+1αExt(1+ηExtsExt)，

其中 *α*W 是由于通过壁面导热产生的换热系数

αW=kWDHln(1+tWDH)，

并且其中：

- *kW* 是 **Wall thermal conductivity** 参数的值。
- *tW* 是 **Wall thickness** 参数的值。
- *αExt* 是 **External environment heat transfer coefficient** 参数的值。
- *ηExt* 是 **External fin efficiency** 参数的值。
- *sExt* 是 **Ratio of external fins surface area to no-fin surface
  area** 参数的值。

如果壁面没有热质量，则壁面与环境之间的换热系数等于环境的换热系数 *α*Ext。

**传热速率**

每个壁面区域与环境之间的传热速率为

QH,zone=(TH−TW)zSWαE。

壁面与环境之间的总传热为

QH=QH,L+QH,V+QH,M。

**控制微分方程**

传热速率取决于壁面的热质量 *CW*

CW=cp,WρWSW(tW+tW2DH)，

其中：

- *c*p,W 是 **Wall specific heat** 参数的值。
- *ρW* 是 **Wall density** 参数的值。

液体区域中流体与外部环境之间传热的控制方程为

QH,L−QF,L=CW[zLdTW,Ldt+max(dzLdt,0)(TW,L−TW,M)]，

混合物区域为

QH,M−QF,M=CW[zMdTW,Mdt+min(dzLdt,0)(TW,L−TW,M)+min(dzVdt,0)(TW,V−TW,M)]，

蒸汽区域为

QH,V−QF,V=CW[zVdTW,Vdt+max(dzVdt,0)(TW,V−TW,M)]。

### Momentum Balance

有两个因素决定管道上的压差：由密度变化引起的压力变化，以及由管壁摩擦引起的压力变化。

对于湍流，当雷诺数高于 **Turbulent flow lower Reynolds number limit** 参数的值时，模块根据 Darcy 摩擦因子计算压力损失。端口 **A** 与内部节点 I 之间的压差为

pA−pI=(1ρI−1ρA\*)(m˙AS)2+fAm˙A|m˙A|2ρIDHS2(L+LAdd2)+Δphydrostatic2,

其中：

- *ρI* 是内部节点 I 处的流体密度。
- *ρA\** 是端口 **A** 处的流体密度，当流动为稳态时，它与 *ρA* 相同。当流动为瞬态时，模块根据内部节点 I 处的流体内部状态，通过绝热表达式计算 *ρA\**

  uA\*+pAρA\*+12(m˙AρA\*S)2=h+12(m˙AρS)2,

  其中：

  - *h* 是平均比焓，h=hLzL+hVzV+hMzM。
  - *ρ* 是平均密度，ρ=ρLzL+ρMzM+ρVzV。
- m˙A 是通过端口 **A** 的质量流量。
- *L* 是 **Pipe length** 参数的值。
- *LAdd* 是 **Aggregate equivalent length of local resistances** 参数的值，它是一段管子的等效长度，该管子引入的损失与其他局部阻力损失之和相同。
- Δphydrostatic=MVgΔz 是静水压力，其中：

  - *M* 是管道中的流体总质量。
  - *V* 是流体总体积，即管道体积。
  - *g* 是 **Gravitational acceleration** 参数的值。
  - *Δz* 是 **Elevation gain from port A to port B** 参数的值。

Darcy 摩擦因子取决于雷诺数，模块会在两个端口处计算该值。

端口 **B** 与内部节点 I 之间的压差为

pB−pI=(1ρI−1ρB\*)(m˙BS)2+fBm˙B|m˙B|2ρIDHS2(L+LAdd2)−Δphydrostatic2,

其中：

- *ρB\** 是端口 **B** 处的流体密度，当流动为稳态时，它与 *ρB* 相同。当流动为瞬态时，模块根据流体内部状态，通过绝热表达式计算 *ρB\**

  uB\*+pBρB\*+12(m˙BρB\*S)2=h+12(m˙BρS)2.
- m˙B 是通过端口 **B** 的质量流量。

对于层流，当雷诺数低于 **Laminar flow upper Reynolds number limit** 参数的值时，模块根据 **Laminar friction constant for Darcy friction factor** 参数 *λ* 计算由摩擦引起的压力损失。端口 **A** 与内部节点 I 之间的压差为

pA−pI=(1ρI−1ρA\*)(m˙AS)2+λμm˙A2ρIDH2S(L+LAdd2)+Δphydrostatic2,

其中 *μ* 是平均流体动力黏度

μ=μLzL+μMzM+μVzV.

端口 **B** 与内部节点 I 之间的压差为

pB−pI=(1ρI−1ρB\*)(m˙BS)2+λμm˙B2ρIDH2S(L+LAdd2)−Δphydrostatic2.

对于过渡流，模块会在层流和湍流压力损失值之间平滑处理由黏性摩擦引起的压差。

### Mass Balance

总质量累积率为

dMdt=m˙A+m˙B.

就流体区域而言，质量累积率是密度 *ρ* 相对于压力 *p* 的变化以及流体比内能 *u* 的函数

dMdt=[(∂ρ∂p)udpdt+(∂ρ∂u)pduoutdt+ρLdzLdt+ρMdzMdt+ρVdzVdt]V,

其中 *uout* 是所有传热发生后的比内能。

### Energy Balance

能量守恒方程为

Mduoutdt+(m˙A+m˙B)uout=ϕA+ϕB+QF−m˙avggΔz,

其中：

- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。
- *QF* 是流体与壁面之间的传热率。
- m˙avg=m˙A−m˙B2.

### 假设和限制

- 管壁是完全刚性的。
- 流动是充分发展的。摩擦损失和传热不包括入口效应。
- 流体惯性可忽略不计。
- 模块在整体系统层面建模重力效应，不建模管道内由于重力引起的液体和蒸气分离。
- 当压力高于流体临界压力时，热流体性质（如 Prandtl 数、热导率和比热）的较大值可能无法准确反映管道中的热交换。
