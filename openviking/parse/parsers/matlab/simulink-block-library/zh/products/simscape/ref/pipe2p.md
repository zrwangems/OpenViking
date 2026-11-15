---
type: simulink-block
title: 'Pipe (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'pipe2p'
documentation_source_path: 'ref/pipe2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (2P)

## 端口

### 守恒

### **A** — 入口或出口两相流体

与管道入口或出口关联的两相流体守恒端口。该模块没有固有方向性。

### **B** — 入口或出口两相流体

与管道入口或出口关联的两相流体守恒端口。该模块没有固有方向性。

### **H** — 管壁温度热端口

表示管壁温度的热守恒端口。

## 参数

### 几何

### **Pipe length** — 管道长度 `5 m`（默认）| positive scalar

管道沿流动方向的长度。

### **Cross-sectional area** — 管道内部面积 `0.01 m^2`（默认）| positive scalar

管道内部垂直于流动方向的面积。该面积沿管道长度保持恒定。

### **Hydraulic diameter** — 具有相同横截面积的等效圆柱形管道的直径 `0.1 m`（默认）| positive scalar

具有圆形横截面的等效管道的直径。在圆柱形管道中，水力直径与其实际直径相同。

### 摩擦与传热

### **Aggregate equivalent length of local resistances** — 管道中所有局部阻力的合计长度 `0.1 m`（默认）| positive scalar

管道中所有局部阻力的合计长度。局部阻力包括弯头、管件、附件以及管道入口和出口。局部阻力的作用是增加管段的等效长度。仅出于压力损失计算的目的，将该长度加到几何管道长度上。管道内的流体体积仅取决于管道几何长度，由 **Pipe length** 参数定义。

### **Internal surface absolute roughness** — 管道内表面所有表面缺陷的平均深度 `15e-6 m`（默认）| positive scalar

管道内表面所有表面缺陷的平均深度，它会影响湍流流态下的压力损失。

### **Laminar flow upper Reynolds number limit** — 流动开始从层流过渡为湍流时的雷诺数 `2000`（默认）| positive scalar

流动开始从层流过渡为湍流时的雷诺数。该数值等于对应于充分发展层流的最大雷诺数。

### **Turbulent flow lower Reynolds number limit** — 流动开始从湍流过渡为层流时的雷诺数 `4000`（默认）| positive scalar

流动开始从湍流过渡为层流时的雷诺数。该数值等于对应于充分发展湍流的最小雷诺数。

### **Shape factor for laminar flow viscous friction** — 管道几何形状对黏性摩擦损失的影响 `64`（默认）| positive scalar

无量纲因子，用于体现管道横截面几何形状对层流流态下黏性摩擦损失的影响。典型值为：圆形横截面为 64，方形横截面为 57，长宽比为 2 的矩形横截面为 62，薄环形横截面为 96 [1]。

### **Nusselt number for laminar flow heat transfer** — 对流传热与导热之比 `3.66`（默认）| positive scalar

层流流态下对流传热与导热之比。其值取决于管道横截面几何形状和管壁热边界条件，例如恒定温度或恒定热流。典型值为 3.66，适用于具有恒定壁温的圆形管道横截面 [2]。

### 效应与初始条件

### **Enable fluid inertia** — 是否对流体惯性建模 off（默认）| on

选中此复选框可对流体惯性（即流体对快速加速度的阻力）建模。

### **Initial fluid energy specification** — 用于定义初始条件的热力学变量 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于定义模块初始条件的热力学变量。

**Initial fluid energy specification** 参数的值限制了两相流体的可用初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定为过冷液体或过热蒸气的初始状态。不能指定液-汽混合物，因为在液-汽混合物区域内温度恒定。
- `Vapor quality` — 指定为液-汽混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定为液-汽混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。该模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。该模块不限制初始状态。

### **Initial pressure** — 仿真开始时的绝对压力 `0.101325 MPa`（默认）| positive scalar

仿真开始时管道内的压力，相对于绝对零压指定。

### **Initial temperature** — 仿真开始时的绝对温度 `293.15 K`（默认）| positive scalar

仿真开始时管道内的温度，相对于绝对零度指定。

#### 依赖项

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial vapor quality** — 仿真开始时的蒸气质量分数 `0.5`（默认）| unitless scalar between 0 and 1

仿真开始时管道内蒸气的质量分数。

#### 依赖项

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial vapor void fraction** — 仿真开始时的蒸气体积分数 `0.5`（默认）| unitless scalar between 0 and 1

仿真开始时管道内蒸气的体积分数。

#### 依赖项

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial specific enthalpy** — 仿真开始时的比焓 `1500 kJ/kg`（默认）| positive scalar

仿真开始时管道内流体的比焓。

#### 依赖项

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial specific internal energy** — 仿真开始时的比内能 `1500 kJ/kg`（默认）| positive scalar

仿真开始时管道内流体的比内能。

#### 依赖项

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### **Phase change time constant** — 相变事件的特征持续时间 `0.1 s`（默认）| positive scalar

管道内发生的相变事件达到平衡的特征时间。该常数在相之间的过渡中引入时间滞后。增大此参数值可减慢相变速率，或减小此值可加快速率。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2024a：管道低流量计算的数值改进

为了提高低速流动时管道内压降的精度，Pipe (2P) 模块中的动量平衡计算已略有更改。与先前版本相比，仿真结果可能存在轻微差异，尤其是在马赫数较低时。

## 描述

用于两相流体系统中流体流动的刚性导管

Pipe (2P) 模块对刚性管道内两相流体的流动动力学进行建模。假设流体的动态可压缩性和热容不可忽略。两相流体守恒端口 **A** 和 **B** 表示管道入口。热守恒端口 **H** 表示管壁，通过该端口与管道周围环境进行传热。

### 流体惯性

该模块提供用于对流体惯性建模的选项，即流体对质量流率突然变化的阻力。默认情况下，流体惯性建模处于关闭状态。当驱动流动的压力力远大于作用在流动上的惯性力时，此设置是合适的。

默认设置可降低计算成本，建议用于大多数模型。但是，如果质量流率快速变化，流体惯性可能变得重要。在这种情况下，开启流体惯性建模有助于提高仿真精度。

### 能量平衡

管道中的能量守恒通过以下方程体现：

Mu˙I+(m˙A+m˙B)uI=ϕA+ϕB+QH,

其中：

- *M* 是管道内的流体质量。
- *u*I 是管道内流体的比内能。
- *ϕ*A 是通过端口 A 进入管道的能量流率。
- *ϕ*B 是通过端口 B 进入管道的能量流率。
- *Q*H 是通过管壁进入管道的热流率，由端口 **H** 表示。

**热流率**

管壁与内部流体体积之间的传热建模为对流过程，热流率计算如下：

QH=hcoeffSsurf(TH−TI),

其中：

- *h*coeff 是管道内的平均传热系数。
- *S*Surf 是管道表面积。
- *T*H 是管壁温度。
- *T*I 是管道内流体的温度。

传热系数的计算取决于流体相。在过冷液体和过热蒸气相中，该系数为：

h\*coeff=k\*INu\*Dh,

其中星号表示所考虑相（液相或蒸气相）的特定值，并且：

- `Nu` 是管道内的平均努塞尔数。
- `k`I 是管道内的平均热导率。
- *D*h 是管道的水力直径（即任意形状的横截面若变为圆形时所具有的直径）。

在两相混合物中，同一系数为：

hMcoeff=kMI,SLNuMDh,

其中下标 `M` 表示特定于两相混合物的值，下标 `SL` 表示针对饱和液体获得的值。

**努塞尔数**

在层流中，假设努塞尔数为常数，并等于模块对话框中指定的值。当雷诺数小于 **Laminar flow upper Reynolds number limit** 参数中输入的值时，适用层流努塞尔数。

当雷诺数大于 **Laminar flow upper Reynolds number limit** 参数中输入的值时，适用湍流努塞尔数。在层流与湍流之间的过渡区域，三次多项式函数将这两个努塞尔数混合。这种混合可确保流态之间的平滑过渡。

在液相和蒸气相中，湍流努塞尔数根据 Gnielinski 关联式得到：

Nu\*=f8(Re\*−1000)Pr\*I1+12.7f8(Pr\*I2/3−1),

其中，如前所述，星号表示所考虑的相，并且：

- *f* 是管道的摩擦因子。
- `Re` 是雷诺数。
- *Pr*I 是普朗特数。

摩擦因子计算如下：

f={−1.8log10[6.9Re\*+(ϵr3.7)1.11]}-2,

其中 *ε*r 是管道的粗糙度。雷诺数计算如下：

Re\*=|m˙Avg|DhvI\*SνI\*,

其中下标 `Avg` 表示端口之间的平均值，并且：

- *S* 是管道的横截面积。
- *v*I 是比体积。
- *ν*I 是运动黏度。

在两相混合物中，湍流努塞尔数根据 Cavallini 和 Zecchin 关联式得到：

NuM=0.05[(1−xI+xIvSVvSL)ReSL]0.8PrSL0.33,

其中下标 `SL` 表示饱和液体的值，下标 `SV` 表示饱和蒸气的值，并且：

- *x*I 是蒸气干度。
- *v* 是比体积。

饱和液体的雷诺数计算如下：

ReSL=|m˙Avg|DhvSLSνSL,

### 质量平衡

管道中的质量守恒通过以下方程体现：

[(∂ρ∂p)up˙I+(∂ρ∂u)pu˙I]V=m˙A+m˙B+ϵM,

其中：

- *ρ* 是流体密度。
- *p*I 是管道内的压力。
- *V* 是管道内流体的体积。
- m˙A 是通过端口 **A** 进入管道的质量流率。
- m˙B 是通过端口 **B** 进入管道的质量流率。
- *∊*M 是校正项，用于考虑相变边界上密度偏导数的平滑处理。

该模块使用三次多项式函数混合各个区域的密度偏导数。在蒸气干度为 0–0.1 时，该函数混合过冷液体区域与两相混合物区域的导数。在蒸气干度为 0.9–1 时，它混合两相混合物区域与过热蒸气区域的导数。质量守恒方程中的校正项

ϵM=M−V/vIτ,

被加入以校正由三次多项式函数引入的数值误差，其中：

- *M* 是管道内的流体质量，由以下方程计算：

  M˙=m˙A+m˙B,

- *v*I 是管道内流体的比体积。
- *τ* 是相变时间常数——相变事件的特征持续时间。该常数确保相变不会瞬时发生，从而在每次发生相变时有效引入时间滞后。

### Momentum Balance

动量平衡方程为每个半管段分别定义。在与端口 **A** 相邻的半管中：

pA−pI=m˙AS|m˙AS(νI−νA)|+Fvisc,A+IA,

其中：

- *p*A 是端口 **A** 处的压力。
- *S* 是管道的横截面积。
- *ν*A 是端口 **A** 处流体的比体积。
- *F*visc,A 是与端口 **A** 相邻的半管中的粘性摩擦力。
- *I*A 是端口 **A** 处的流体惯性：

  IA=m¨AL2S

  参数 *L* 是管道长度。

在与端口 **B** 相邻的半管中：

pB−pI=m˙BS|m˙BS(νI−νB)|+Fvisc,B+IB,

其中：

- *p*B 是端口 **B** 处的压力。
- *ν*B 是端口 **B** 处流体的比体积。
- *F*visc,B 是与端口 **B** 相邻的半管中的粘性摩擦力。
- *I*B 是端口 **B** 处的流体惯性：

  IB=m¨BL2S

流体惯性项 *I*A 和 *I*B 在 **Enable fluid inertia** 复选框被清除时为零，即当流体惯性建模为 off 时。粘性摩擦力 *F*visc,A 和 *F*visc,B 的计算取决于流态，层流或湍流。

**层流中的粘性摩擦力**

在层流状态下——即当雷诺数小于模块对话框中指定的 **Laminar flow upper Reynolds number limit** 值时——与端口 **A** 相邻的半管中的粘性摩擦力为

Fvisc,Alaminar=fshapeLeffνIm˙A4Dh2S,

而在与端口 **B** 相邻的半管中为

Fvisc,Blaminar=fshapeLeffνIm˙B4Dh2S,

其中：

- *f*shape 是管道形状因子。
- *L*eff 是有效管道长度——管道长度与局部阻力的总等效长度之和。
- *D*h 是管道的水力直径。

**湍流中的粘性摩擦力**

在湍流状态下——即当雷诺数大于模块对话框中指定的 **Turbulent flow lower Reynolds number limit** 值时——与端口 **A** 相邻的半管中的粘性摩擦力为

Fvisc,Aturbulent=m˙A|m˙A|fALeffνI4DHS2,

而在与端口 **B** 相邻的半管中为

Fvisc,Bturbulent=m˙B|m˙B|fBLeffνI4DHS2,

其中：

- *f*A 是与端口 **A** 相邻的半管中湍流的达西摩擦因子。
- *f*B 是与端口 **B** 相邻的半管中湍流的达西摩擦因子。

与端口 **A** 相邻的半管中湍流的达西摩擦因子由 Haaland 方程给出，为

fA=1{−1.8log10[6.9ReA+(ϵr3.7)1.11]}2,

而在与端口 **B** 相邻的半管中为

fB=1{−1.8log10[6.9ReB+(ϵr3.7)1.11]}2,

其中：

- *∊*r 是管道的相对粗糙度。
- *Re*A 是与端口 **A** 相邻的半管中的雷诺数，

  ReA=|m˙A|DhvISνI.
- *Re*B 是与端口 **B** 相邻的半管中的雷诺数，

  ReB=|m˙B|DhvISνI.

三次多项式函数用于在层流与湍流之间的过渡区混合摩擦损失。

### 假设与限制

- 管道壁是刚性的。
- 流动充分发展。
- 重力的影响可忽略。
- 传热是根据管道中流体体积的温度计算的。要对长管道中因传热导致的温度梯度进行建模，请将多个 Pipe (2P) 模块串联连接。
