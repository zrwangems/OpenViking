---
type: simulink-block
title: 'Heat Exchanger Interface (TL)'
family: 'heat-exchangers'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'heatexchangerinterfacetl'
documentation_source_path: 'ref/heatexchangerinterfacetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger Interface (TL)

## 端口

### 输出

### **C** — 热容量率物理信号

热液体热容量率的物理信号输出端口。

### **HC** — 传热系数物理信号

热液体与接口壁之间传热系数的物理信号输出端口。

### 守恒

### **A** — 热液体端口 热液体

表示热液体入口的热液体守恒端口。

### **B** — 热液体端口 热液体

表示热液体出口的热液体守恒端口。

### **H** — 热入口温度 热

与热液体入口温度关联的热守恒端口。

## 参数

### **最小自由流通面积** — 流道最窄点处的横截面积 `0.01 m^2`（默认） | scalar

入口和出口之间最小的总横截流动面积。如果通道是由管道、管子、槽或沟组成的集合，则此参数的值是最小流动面积点处最小面积的总和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在一个横截面中管间间隙之和最小时的各间隙之和。

### **压力损失的水力直径** — 通道的直径或等效直径 `0.1 m`（默认） | scalar

构成换热接口的管子或通道的水力直径。水力直径是流动横截面积与通道周长之比。

### **热液体体积** — 流道中包含的流体总体积 `0.01 m^3`（默认） | scalar with units of length squared

热液体流道中包含的流体总体积。

### **层流上限雷诺数** — 层流与湍流状态之间过渡的起点 `2000`（默认） | scalar

从层流状态过渡到湍流状态的起点。高于此数值时，惯性力变得越来越占主导。默认值适用于具有光滑表面的圆管和管子。

### **湍流下限雷诺数** — 层流与湍流状态之间过渡的终点 `4000`（默认） | scalar

从层流状态过渡到湍流状态的终点。低于此数值时，黏性力变得越来越占主导。

### **压力损失模型** — 由摩擦引起的压力损失的数学模型 `Pressure loss coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

由摩擦引起的压力损失的数学模型。此设置确定用于计算的表达式以及要作为输入指定的模块参数。有关按参数化进行的计算，请参见 Heat Exchanger Interface (TL) 模块。

### **压力损失系数** — 端口之间所有流动阻力的总损失系数 `0.1`（默认） | scalar

流道中所有流动阻力的总损失系数，包括壁面摩擦（主要损失）以及由弯头、弯管和其他几何变化引起的局部阻力（次要损失）。

损失系数是用于表示由摩擦引起的压力损失的经验无量纲数。它可以从实验数据计算得出，或从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Pressure loss coefficient`。

### **从入口到出口的流动路径长度** — 从端口到端口行进的距离 `1 m`（默认） | scalar with units of length

流动必须在端口之间行进的总距离。在多程管壳式换热器中，总距离是所有壳程的总和。在管束、波纹板和其他流动被分成平行分支的通道中，它是单个分支中经过的距离。流动路径越长，由于壁面摩擦引起的主要压力损失越陡峭。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **局部阻力的总等效长度** — 以长度表示的次要压力损失总和 `0.1 m`（默认） | scalar

以长度表示的次要压力损失总和。直通道的长度会导致与弯头、三通和管接头现有局部阻力总和相等的损失。等效长度越大，由局部阻力引起的次要压力损失越陡峭。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **内表面绝对粗糙度** — 导致摩擦损失的壁面表面变化的平均高度 `15e-6 m`（默认） | scalar with units of length

管道内表面上所有表面缺陷的平均高度。表面粗糙度可用于计算湍流状态下的摩擦因子。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流条件下流动横截面的压力损失修正 `64`（默认） | scalar

层流的压力损失修正。此参数称为形状因子，可用于推导层流状态下压力损失计算所需的 Darcy 摩擦因子。默认值适用于圆柱形管道和管子。

一些用于非圆形横截面的额外形状因子可以从 Navier-Stokes 方程的解析解中确定。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`。平行板之间的细长导管也具有形状因子 `96`。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的雷诺数向量** — Darcy 摩擦因子查找表中每个断点处的雷诺数 `[400, 1000, 1500, 3000, 4000, 6000, 10000, 20000, 40000, 60000, 100000, 100000000]`（默认） | array

用于指定 Darcy 摩擦因子的雷诺数向量。该模块使用此向量创建 Darcy 摩擦因子的查找表。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy 摩擦因子向量** — 雷诺数查找表中每个断点处的 Darcy 摩擦因子 `[.264, .112, .071, .0417, .0387, .0268, .025, .0232, .0226, .022, .0214, .0214]`（默认） | array

与 **Darcy 摩擦因子的雷诺数向量** 参数中指定的值对应的 Darcy 摩擦因子向量。该模块使用此向量创建 Darcy 摩擦因子的查找表。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Euler 数的雷诺数向量** — Euler 数查找表中每个断点处的雷诺数 `[50, 500, 1000, 2000]`（默认） | array

用于指定 Euler 数的雷诺数向量。该模块使用此向量创建 Euler 数的查找表。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler 数向量** — 雷诺数查找表中每个断点处的 Euler 数 `[4.4505, .6864, .4791, .3755]`（默认） | array

与 **Euler 数的雷诺数向量** 参数中指定的值对应的 Euler 数向量。该模块使用此向量创建 Euler 数的查找表。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **传热系数模型** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

用于计算换热器流体之间传热速率的参数化。您可以假定恒定压力损失系数，使用管内流动的经验关联式，或指定 Colburn 数或 Nusselt 数的表格数据。

### **液体-壁面传热系数** — 流体与壁面之间对流的传热系数 `100 W/(m^2 * K)`（默认） | scalar

热液体与传热表面之间的传热系数。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Constant heat transfer coefficient`。

### **传热表面积** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认） | scalar with units of length squared

可用于换热器流体之间传热的表面积总和。

### **传热流动路径长度** — 流体与壁面之间传热所经过的特征长度 `1 m`（默认） | scalar with units of length

流体进行热交换所经过的距离。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **层流换热的 Nusselt 数** — 层流中假定的 Nusselt 数常数 `3.66`（默认） | positive scalar

层流状态下对流传热与导热传热之间的比例常数。此参数可用于计算层流中的对流传热速率。所用适当值取决于组件几何形状。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Correlation for flow inside tubes`。

### **Colburn 因子的雷诺数向量** — Colburn 因子查找表中每个断点处的雷诺数 `[100, 150, 1000]`（默认） | array

用于指定 Colburn 因子的雷诺数向量。该模块使用此向量创建 Colburn 数的查找表。此向量中的值数量必须等于 **Colburn 因子向量** 参数的大小，以便计算表格断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn 因子向量** — 雷诺数查找表中每个断点处的 Colburn 因子 `[.019, .013, .002]`（默认） | array

与 **Colburn 数的雷诺数向量** 参数中指定的值对应的 Colburn 因子向量。该模块使用此向量创建 Colburn 因子的查找表。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Nusselt 数的雷诺数向量** — Nusselt 数查找表中每个断点处的雷诺数 `[100, 150, 1000]`（默认） | array

用于指定 Nusselt 数的雷诺数向量。该模块使用此向量创建 Nusselt 数的查找表。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt 数的 Prandtl 数向量** — Nusselt 数查找表中每个断点处的 Prandtl 数 `[1, 10]`（默认） | array

用于指定 Nusselt 数的 Prandtl 数向量。该模块使用此向量创建 Nusselt 数的查找表。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt 数表，Nu(Re,Pr)** — Reynolds-Prandtl 数查找表中每个断点处的 Nusselt 数 `[3.72, 4.21; 3.75, 4.44; 4.21, 7.15]`（默认） | array

与 **Nusselt 数的雷诺数向量** 和 **Nusselt 数的 Prandtl 数向量** 参数中指定的值对应的 Nusselt 数矩阵。该模块使用此向量创建 Nusselt 因子的查找表。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **污垢系数** — 因污垢而增加的阻力 `1e-4 m^2*K/W`（默认） | scalar

用于量化由于传热表面上的污垢沉积而增加的热阻的经验参数。

#### 影响和初始条件

### **启用动态可压缩性** — 换热器中液体可压缩性的设置 `On`（默认） | `Off` | scalar

用于对换热器内部压力动态进行建模的选项。将此参数设置为 `Off` 会从组件能量和质量守恒方程中移除压力导数项。然后，换热器内部压力会降为两个端口压力的加权平均值。

### **热液体标称温度** — 标称工况下的温度 `293.15 K`（默认） | scalar

标称工况下的热液体温度。当动态可压缩性禁用时，该模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **热液体标称压力** — 标称工况下的压力 `0.101325 MPa`（默认） | scalar

标称工况下的热液体压力。当动态可压缩性禁用时，该模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **热液体初始温度** — 仿真开始时热液体通道中的温度 `293.15 K`（默认） | scalar with units of temperature

仿真开始时热液体通道中的温度。

### **热液体初始压力** — 仿真开始时热液体通道中的压力 `0.101325 MPa`（默认） | scalar with units of pressure

仿真开始时热液体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

## 所属库

Simscape / Fluids / Heat Exchangers / Fundamental Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

热液体与其周围环境之间的热接口

Heat Exchanger Interface (TL) 模块表示热液体网络中用于与其他流体进行传热的液体接口。该模块对热接口的热液体入口和出口之间的压力降和温度变化进行建模，并且当与 E-NTU Heat Transfer 模块结合时，对两种流体之间跨接口的传热速率进行建模。

### 质量平衡

质量平衡方程的形式取决于动态可压缩性设置。如果清除 **启用动态可压缩性** 复选框，则质量平衡方程为

m˙A+m˙B=0,

其中：

- *m˙A* 和 *m˙B* 是经由端口 **A** 和 **B** 流入界面的质量流量。

如果选中 **启用动态可压缩性**，则质量平衡方程为

m˙A+m˙B=(dpdt1β−dTdtα)ρV,

其中：

- *p* 是热液体体积的压力。
- *T* 是热液体体积的温度。
- *ɑ* 是热液体体积的等压热膨胀系数。
- *β* 是热液体体积的等温体积模量。
- *ρ* 是热液体体积的质量密度。
- *V* 是热交换器接口中热液体的体积。

### 动量平衡

热交换器接口中的动量平衡取决于流体动态可压缩性设置。如果选中 **启用动态可压缩性**，动量平衡会显式计入热交换器接口的内部压力。端口 **A** 与内部接口节点之间的半体积中的动量平衡为

pA−p=ΔpLoss,A,

而端口 **B** 与内部接口节点之间的半体积中为

pB−p=ΔpLoss,B,

其中：

- *p*A 和 *p*B 是端口 **A** 和 **B** 处的压力。
- *p* 是接口体积内部节点中的压力。
- *Δp*Loss,A 和 *Δp*Loss,B 是端口 **A** 与内部接口节点之间以及端口 **B** 与内部接口节点之间的压力损失。

如果清除 **启用动态可压缩性** 复选框，则接口体积中的动量平衡直接在端口 **A** 和 **B** 之间计算为

pA−pB=ΔpLoss,A−ΔpLoss,B.

### 压力损失计算

压力损失项的确切形式取决于模块对话框中的 **压力损失模型** 设置。如果压力损失模型设置为 `Pressure loss coefficient`，则与端口 **A** 相邻的半体积中的压力损失为

ΔpLoss,A={m˙AμA(CP)LossReL14Dh,pρASMin,ReA≤ReL(CP)Lossm˙A|m˙A|4ρASMin2,ReA≥ReT,

而与端口 **B** 相邻的半体积中为

ΔpLoss,B={m˙BμB(CP)LossReL14Dh,pρBSMin,ReB≤ReL(CP)Lossm˙B|m˙B|4ρBSMin2,ReB≥ReT,

其中：

- *μ*A 和 *μ*B 是端口 **A** 和 **B** 处的流体动力黏度。
- *CP*Loss 是模块对话框中指定的 **压力损失系数** 参数。
- *Re*L 是层流流态的 Reynolds 数上限。
- *Re*T 是湍流流态的 Reynolds 数下限。
- *D*h,p 是用于压力损失计算的水力直径。
- *ρ*A 和 *ρ*B 是端口 **A** 和 **B** 处的流体质量密度。
- *S*Min 是最小自由流通面积总和。

如果压力损失模型设置为 `Correlation for flow inside tubes`，则与端口 **A** 相邻的半体积中的压力损失为

ΔpLoss,A={m˙AμAλ(Lpress+Ladd)4Dh,pρASMin,ReA≤ReLfT,A(Lpress+Ladd)4Dh,pm˙A|m˙A|ρASMin2,ReA≥ReT,

而与端口 **B** 相邻的半体积中为

ΔpLoss,B={m˙BμBλ(Lpress+Ladd)4Dh,pρBSMin,ReB≤ReLfT,B(Lpress+Ladd)4Dh,pm˙B|m˙B|ρBSMin2,ReB≥ReT,

其中：

- *L*press 是从入口到出口的流路长度。
- *L*add 是局部阻力的总等效长度。
- *f*T,A 和 *f*T,B 是端口 **A** 和 **B** 处的湍流流态 Darcy 摩擦因子。

与端口 **A** 相邻的半体积中的 Darcy 摩擦因子为

fT,A=1[−1.8log10(6.9ReA+r3.7Dh,p)1.11]2,

而与端口 **B** 相邻的半体积中为

fT,B=1[−1.8log10(6.9ReB+r3.7Dh,p)1.11]2,

其中 *r* 是内表面绝对粗糙度。

如果压力损失模型设置为 `Tabulated data — Darcy friction factor vs. Reynolds number`，则与端口 **A** 相邻的半体积中的压力损失为

ΔpLoss,A={m˙AμAλLpress4Dh,p2ρASMin,ReA≤ReLf(ReA)Lpress4Dh,pm˙A|m˙A|ρASMin2,ReA≥ReT,

而与端口 **B** 相邻的半体积中为

ΔpLoss,B={m˙BμBλLpress4Dh,p2ρBSMin,ReB≤ReLf(ReB)Lpress4Dh,pm˙B|m˙B|ρBSMin2,ReB≥ReT,

其中：

- *λ* 是层流黏性摩擦的形状因子。
- *f*(*Re*A) 和 *f*(*Re*B) 是端口 **A** 和 **B** 处的 Darcy 摩擦因子。模块从相对于 Reynolds 数指定的表格数据中获取摩擦因子。

如果压力损失模型设置为 `Tabulated data — Euler number vs. Reynolds number`，则与端口 **A** 相邻的半体积中的压力损失为

ΔpLoss,A={m˙AμAEu(ReL)ReL14Dh,pρASMin,ReA≤ReLEu(ReA)m˙A|m˙A|4ρASMin2,ReA≥ReT,

而与端口 **B** 相邻的半体积中为

ΔpLoss,B={m˙BμBEu(ReL)ReL14Dh,pρBSMin,ReB≤ReLEu(ReB)m˙B|m˙B|4ρBSMin2,ReB≥ReT,

其中：

- *Eu*(*Re*L) 是层流流动的 Reynolds 数上限处的 Euler 数。
- *Eu*(*Re*A) 和 *Eu*(*Re*B) 是端口 **A** 和 **B** 处的 Euler 数。模块从相对于 Reynolds 数指定的表格数据中获取 Euler 数。

### 能量平衡

热交换器接口中的能量平衡取决于流体动态可压缩性设置。如果选中 **启用动态可压缩性**，则能量平衡为

dpdtdUdp+dTdtdUdT=ϕA+ϕB+QH,

其中：

- *U* 是热交换器接口体积中包含的内能。
- *ϕ*A 和 *ϕ*B 是经由端口 **A** 和 **B** 流入热交换器接口体积的能量流率。
- *Q*H 是经由端口 **H**（表示接口壁）流入热交换接口体积的热流率。

内能导数定义为

dUdp=[1β(ρu+p)−Tα]V

和

dUdT=[cp−α(u+pρ)]ρV,

其中 *u* 是热液体的比内能，即单位质量热液体所包含的内能。

如果清除 **启用动态可压缩性** 复选框，则热液体密度被视为常数。此时体积模量实际上为无穷大，热膨胀系数为零。可压缩情况下的压力和温度导数消失，能量平衡重新表述为

dEdt=ϕA+ϕB+QH,

其中 *E* 是不可压缩热液体的总内能，或

E=ρuV.

模块根据 **额定液体温度** 和 **额定液体压力** 参数计算 *ρ*。

### 传热关联式

模块计算并输出液体-壁面传热系数值。该计算取决于模块对话框中的 **传热系数规格** 设置。如果传热系数规格为 `Constant heat transfer coefficient`，则传热系数就是模块对话框中指定的常数值，

hL−W=hConst,

其中：

- *h*L-W 是液体-壁面传热系数。
- *h*Const 是模块对话框中指定的 **液体-壁面传热系数值**。

对于所有其他传热系数参数化方式，传热系数定义为端口传热系数的算术平均值：

hL−W=hA+hB2,

其中：

- *h*A 和 *h*B 是端口 **A** 和 **B** 处的液体-壁面传热系数。

端口 **A** 处的传热系数为

hA=NuAkADh,heat,

而端口 **B** 处为

hB=NuBkBDh,heat,

其中：

- *Nu*A 和 *Nu*B 是端口 **A** 和 **B** 处的 Nusselt 数。
- *kA* 和 *kB* 是端口 **A** 和 **B** 处的热导率。
- *Dh,heat* 是用于传热计算的水力直径。

传热计算中使用的水力直径定义为

Dh,heat=4SMinLheatSheat,

其中：

- *L*heat 是传热计算中使用的流路长度。
- *S*heat 是总传热表面积。

### Nusselt 数计算

Nusselt 数计算取决于模块对话框中的 **传热系数规格** 设置。如果传热规格设置为 `Correlation for flow inside tubes`，则端口 **A** 处的 Nusselt 数为

NuA={NuL,ReA≤ReL(fT,A8)(ReA−1000)PrA1+12.7(fT,A8)1/2(PrB2/3−1),ReA≥ReT,

而端口 B 处为

NuB={NuL,ReB≤ReL(fT,B8)(ReB−1000)PrB1+12.7(fT,B8)1/2(PrB2/3−1),ReB≥ReT,

其中：

- *Nu*L 是模块对话框中指定的 **层流传热 Nusselt 数** 值。
- *Pr*A 和 *Pr*B 是端口 **A** 和 **B** 处的 Prandtl 数。

如果传热规格设置为 `Tabulated data — Colburn data vs. Reynolds number`，则端口 **A** 处的 Nusselt 数为

NuA=j(ReA,heat)ReA,heatPrA1/3,

而端口 **B** 处为

NuB=j(ReB,heat)ReB,heatPrB1/3,

其中：

- *j*(*Re*A,heat) 和 *j*(*Re*B,heat) 是端口 **A** 和 **B** 处的 Colburn 数。模块从作为 Reynolds 数函数提供的表格数据中获取 Colburn 数。
- *Re*A,heat 和 *Re*B,heat 是基于端口 **A** 和 **B** 处用于传热计算的水力直径的 Reynolds 数。该参数在端口 **A** 处定义为

  ReA,heat=m˙ADh,heatSMinμA,

  而在端口 **B** 处定义为

  ReB=m˙BDh,heatSMinμB.

如果传热规格设置为 `Tabulated data — Nusselt number vs. Reynolds number and Prandtl number`，则端口 **A** 处的 Nusselt 数为

NuA=Nu(ReA,heat,PrA),

而端口 **B** 处为

NuB=Nu(ReB,heat,PrB).

### 水力直径计算

传热计算中使用的水力直径可能与压力损失计算中采用的水力直径不同；如果加热周长和摩擦周长不相同，则二者不同。对于具有环形横截面的同心管热交换器，传热计算的水力直径为

Dh,heat=4(π/4)(Do2−Di2)πDi=Do2−Di2Di,

而压力计算的水力直径为

Dh,p=4(π/4)(Do2−Di2)π(Di+Do)=Do−Di,

其中：

- *D*o 是环形空间外径。
- *D*i 是环形空间内径。

**环形空间示意图**

以橙色表示的外径与内径之间的差值代表热液体。内径内的蓝色区域是与热液体交换热量的流体。
