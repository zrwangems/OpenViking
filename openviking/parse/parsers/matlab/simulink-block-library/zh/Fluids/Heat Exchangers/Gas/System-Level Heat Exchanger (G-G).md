---
type: simulink-block
title: 'System-Level Heat Exchanger (G-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'systemlevelheatexchangergg'
documentation_source_path: 'ref/systemlevelheatexchangergg.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Heat Exchanger (G-G)

## 端口

### 输出

### **Q1** — 传递到气体 1 的传热速率，W 物理信号

传递到气体 1 的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **Q2** — 传递到气体 2 的传热速率，W 物理信号

传递到气体 2 的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。
### 守恒

### **A1** — 侧 1 气体端口 gas

与第一个气体网络关联的入口或出口端口。

### **B1** — 侧 1 气体端口 gas

与第一个气体网络关联的入口或出口端口。

### **A2** — 侧 2 气体端口 gas

与第二个气体网络关联的入口或出口端口。

### **B2** — 侧 2 气体端口 gas

与第二个气体网络关联的入口或出口端口。

## 参数

### 配置

### **Flow arrangement at nominal operating conditions** — 额定工况下的流路排列 `Counter flow - Gas 1 flows from A to B, Gas 2 flows from B to A`（默认）| `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

额定工况下换热器两侧之间的流路排列。可用的流动布置为：

- `Counter flow - Gas 1 flows from A to B, Gas 2
  flows from B to A` — 两股流体彼此平行、方向相反地流动。
- `Parallel flow - Both fluids flow from A to
  B` — 两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to
  B` — 两股流体彼此垂直地流动。

平行流与逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效果最差，满足指定性能所需的尺寸最大。

额定工况下的流动方向（从 A 到 B，或从 B 到 A）仅在选择 **Initialize gas 1 to nominal operating conditions** 或 **Initialize gas 2 to nominal operating conditions** 时影响模型初始化。如果设置不同的初始工况，则流动方向可以不同。

在模块确定换热器尺寸之后，此设置不再影响模块在仿真期间计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果将该参数设置为平行流，但将模型设置为以逆流运行，则即使其余边界条件相同，仿真期间的传热速率也不会与指定性能匹配。

如果将该参数设置为交叉流，则模块将换热器内部的流路建模为彼此垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。选择此参数时，模块会为仿真引入额外的动态特性，并且需要更长时间才能达到稳态，但此参数不会影响稳态仿真结果。

### **Wall mass** — 传热表面的质量 `1 kg`（默认）| 正标量

传热表面的质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 传热表面的比热 `490 J/(K*kg)`（默认）| 正标量

传热表面的比热。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initialize wall temperature to nominal operating conditions** — 初始化壁面温度的选项 `on`（默认）| `off`

将壁面温度初始化为额定工况或指定值的选项。如果选择此参数，模块将根据为两侧流体指定的额定工况计算初始壁面温度。如果清除此参数，则可以直接使用 **Initial wall temperature** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K`（默认）| 正标量或二元素向量

壁面的初始温度。如果指定标量，则模块假定初始壁面温度均匀。如果指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

气体 1 端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

气体 1 端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

气体 2 端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

气体 2 端口 **B2** 处的流通面积。

### 气体 1

### **Nominal operating condition** — 额定工况 `Heat transfer from Gas 1 to Gas 2`（默认）| `Heat transfer from Gas 2 to Gas 1`

用于气体 1 网络的额定工况：

- `Heat transfer from Gas 1 to Gas 2` —
  侧 1 被冷却，侧 2 被加热。
- `Heat transfer from Gas 2 to Gas 1` —
  侧 2 被冷却，侧 1 被加热。

此设置仅与额定工况参数相关。这并不意味着在仿真期间热量只能沿指定方向传递。

### **Nominal mass flow rate** — 额定工况下气体 1 端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **Nominal pressure drop** — 额定工况下气体 1 端口之间的压降 `0.001 MPa`（默认）| 正标量

额定工况下从端口 **A1** 到端口 **B1** 的压降。

### **Nominal inlet pressure** — 气体 1 入口处的压力 `0.101325 MPa`（默认）| 正标量

额定工况下换热器气体 1 入口处的压力。

### **Nominal inlet temperature** — 气体 1 入口处的温度 `333.15 K`（默认）| 正标量

额定工况下换热器气体 1 入口处的温度。

### **Heat transfer capacity specification** — 如何指定气体 1 的传热能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过传热速率，还是间接通过出口条件来指定换热器在额定工况下对气体 1 的性能。

### **Nominal rate of heat transfer** — 传热速率 `1 kW`（默认）| 正标量

传热速率。**Nominal Operating condition** 参数决定热量从哪个气体网络传递以及传递到哪个气体网络：

- 如果 **Nominal operating condition** 为
  `Heat transfer from Gas 1 to Gas
  2`，则此参数为额定工况下从气体侧 1 传递到气体侧 2 的传热速率。
- 如果 **Nominal operating condition** 为
  `Heat transfer from Gas 2 to Gas
  1`，则此参数为额定工况下从气体侧 2 传递到气体侧 1 的传热速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Rate of heat transfer`。

### **Nominal outlet temperature** — 出口温度 `323.15 K`（默认）| 正标量

额定工况下换热器气体 1 出口处的温度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Outlet condition`。

### **Gas 1 volume** — 气体 1 的总体积 `0.1 m^3`（默认）| 正标量

换热器内气体 1 的总体积。

### **Initialize gas 1 to nominal operating conditions** — 初始化气体 1 的选项 `on`（默认）| `off`

将气体 1 初始化为额定工况或指定值的选项。如果选择此参数，模块将气体 1 初始化为额定工况。如果清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial gas 1 pressure** — 仿真开始时气体 1 的压力 `0.101325 MPa`（默认）| 正标量

仿真开始时气体 1 的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize gas 1 to nominal operating conditions** 复选框。

### **Initial gas 1 temperature** — 仿真开始时气体 1 的温度 `293.15 K`（默认）| 正标量

仿真开始时气体 1 的温度。

#### 依赖关系

要启用此参数，请清除 **Initialize gas 1 to nominal operating conditions** 复选框。

### 气体 2

### **Nominal mass flow rate** — 额定工况下气体 2 端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的质量流量。

### **Nominal pressure drop** — 额定工况下气体 2 端口之间的压降 `0.001 MPa`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的压降。

### **Nominal inlet pressure** — 气体 2 入口处的压力 `0.101325 MPa`（默认）| 正标量

额定工况下换热器气体 2 入口处的压力。

### **Nominal inlet temperature** — 气体 2 入口处的温度 `293.15 K`（默认）| 正标量

额定工况下换热器气体 2 入口处的温度。

### **Gas 2 volume** — 换热器中气体 2 的总体积 `0.1 m^3`（默认）| 正标量

换热器中气体 2 的总体积。

### **Initialize gas 2 to nominal operating conditions** — 初始化气体 2 的选项 `on`（默认）| `off`

将气体 2 初始化为额定工况或指定值的选项。如果选择此参数，模块将气体 2 初始化为额定工况。如果清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial gas 2 pressure** — 仿真开始时气体 2 的压力 `0.101325 MPa`（默认）| 正标量

仿真开始时气体 2 的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize gas 2 to nominal operating conditions** 复选框。

### **Initial gas 2 temperature** — 仿真开始时气体 2 的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时气体 2 的温度。如果该值为标量，则模块假定初始温度均匀。如果该值为二元素向量，则模块假定初始温度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize gas 2 to nominal operating conditions** 复选框。

### 相关系数

### **a in Nu = a\*Re^b\*Pr^c for gas 1** — 气体 1 的相关系数 `0.023`（默认）| 正标量

气体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for gas 1** — 气体 1 关联式中的雷诺数指数 `0.8`（默认）| 正标量

气体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。

### **c in Nu = a\*Re^b\*Pr^c for gas 1** — 气体 1 关联式中的普朗特数指数 `0.33`（默认）| 正标量

气体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。

### **a in Nu = a\*Re^b\*Pr^c for gas 2** — 气体 2 的相关系数 `0.023`（默认）| 正标量

气体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for gas 2** — 气体 2 关联式中的雷诺数指数 `0.8`（默认）| 正标量

气体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。默认值基于 Colburn 方程。

### **c in Nu = a\*Re^b\*Pr^c for gas 2** — 气体 2 关联式中的普朗特数指数 `0.33`（默认）| 正标量

气体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。默认值基于 Colburn 方程。

## 所属库

Simscape / Fluids / Heat Exchangers / Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

基于两个气体网络之间性能数据的换热器

System-Level Heat Exchanger (G-G) 模块基于两个不同气体网络之间的性能数据来建模换热器。每个网络都有自己的一套流体属性。

该模块使用换热器数据表中的性能数据，而不是换热器的详细几何结构。您可以在设计迭代期间调整换热器的尺寸和性能，或者对具有不常见几何结构的换热器进行建模。您还可以在早期设计阶段使用此模块来建模具有一定性能水平的换热器，此时详细的几何数据尚不可用。

您通过标称工况来参数化该模块。该模块对换热器进行尺寸设计，以在稳态下匹配标称工况下的指定性能。

该模块与 Heat Exchanger (G-G) 模块类似，但使用不同的参数化模型。下表比较了这两个模块：

| Heat Exchanger (G-G) | System-Level Heat Exchanger (G-G) |
| --- | --- |
| 模块参数基于换热器几何结构 | 模块参数基于性能和工况 |
| 换热器几何结构可能受可用几何参数选项的限制 | 模型独立于特定换热器几何结构 |
| 您可以通过调整几何参数（如翅片尺寸和管长）来调整模块以满足不同的性能要求 | 您可以通过直接指定所需的热流量和质量流量来调整模块以满足不同的性能要求 |
| 您可以在平行流、逆流、管壳式或叉流配置之间进行选择 | 您可以在标称工况下在平行流、逆流或叉流布置之间进行选择，以帮助进行尺寸设计 |
| 在广泛工况范围内具有预测性准确的结果，但受 E-NTU 方程和传热系数关联式适用性的约束 | 在指定工况附近结果非常准确；远离指定工况时精度可能下降 |
| 传热计算通过使用 E-NTU 模型来考虑温度沿流动路径的变化 | 传热计算通过将流动路径分为三段来近似温度沿流动路径的变化 |

### 传热

该模块将模块中的两股气体流（气体 1 和气体 2）分为三个大小相等的段。该模块计算每个段内流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **Enable wall thermal mass** 复选框，则换热器中的热平衡为

Qseg,G1+Qseg,G2=0，

其中：

- *Qseg,G1* 是从壁面（即传热表面）到段内气体 1 的热流量。
- *Qseg,G2* 是从壁面到段内气体 2 的热流量。

如果选中 **Enable wall thermal mass**，则换热器中的热平衡为

Qseg,G1+Qseg,G2=−MwallcpwallNdTseg,walldt，

其中：

- *Mwall* 是壁面的质量。
- *cpwall* 是壁面的比热。
- *N* = 3 是段数。
- *Tseg,wall* 是段内壁面的平均温度。
- *t* 是时间。

从壁面到段内气体 1 的热流量为

Qseg,G1=UAseg,G1(Tseg,wall−Tseg,G1)，

其中：

- *UAseg,G1* 是段内气体 1 的传热导。
- *Tseg,G1* 是段内气体的平均温度。

从壁面到段内气体 2 的热流量为

Qseg,G2=UAseg,G2(Tseg,wall−Tseg,G2)，

其中：

- *UAseg,G2* 是段内气体 2 的传热导。
- *Tseg,G2* 是段内气体 2 的平均温度。

该模块在传热计算中使用的流体属性是入口值与流体体积内值之间的平均值。

### 气体传热关联式

该模块使用相同的表达式计算两种气体的传热导。为简单起见，本节中的方程针对一侧，但适用于两侧。传热导方程为：

UAseg,G=aG(Reseg,G)bG(Prseg,G)cGkseg,GGGN，

其中：

- *aG*、*bG* 和 *cG* 是努塞尔数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Reseg,G* 是段内的平均雷诺数。
- *Prseg,G* 是段内的平均普朗特数。
- *kseg,G* 是段内的平均热导率。
- *GG* 是换热器气体侧的几何比例因子。该模块计算几何比例因子，使得所有段的总传热量在标称工况下与指定性能匹配。

平均雷诺数为

Reseg,G=m˙seg,GDref,Gμseg,GSref,G，

其中：

- *ṁseg,G* 是通过该段的质量流量。
- *μseg,G* 是段内的平均动力粘度。
- *Dref,G* 是任意参考直径。
- *Sref,G* 是任意参考流通面积。

**注意**

*Dref,G* 和 *Sref,G* 项仅出于单位计算目的包含在此方程中，以使 *Reseg,G* 无量纲。*Dref,G* 和 *Sref,G* 的值是任意的，因为 *GG* 的计算会覆盖这些值。

### 压力损失

气体 1 侧的压力损失为

pA,G1−pG1=KG12m˙A,G1m˙2A,G1+m˙2thres,G12ρavg,G1pB,G1−pG1=KG12m˙B,G1m˙2B,G1+m˙2thres,G12ρavg,G1

其中：

- *pA,G1* 和 *pB,G1* 分别是端口 **A1** 和 **B1** 处的压力。
- *pG1* 是该模块计算传热时的内部气体 1 压力。
- *ṁA,G1* 和 *ṁB,G1* 分别是流入端口 **A1** 和 **B1** 的质量流量。
- *ρavg,G1* 是所有段上的平均气体 1 密度。
- *ṁthres,G1* 是压力损失的层流阈值，近似为标称质量流量的 1e-4。该模块计算压力损失系数 *KG1*，使得 *pA,G1* – *pB,G1* 在标称质量流量下与标称压力损失匹配。

气体 2 侧的压力损失为

pA,G2−pG2=KG22m˙A,G2m˙2A,G2+m˙2thres,G22ρavg,G2pB,G2−pG2=KG22m˙B,G2m˙2B,G2+m˙2thres,G22ρavg,G2

其中：

- *pA,G2* 和 *pB,G2* 分别是端口 **A2** 和 **B2** 处的压力。
- *pG2* 是该模块计算传热时的内部气体 2 压力。
- *ṁA,G2* 和 *ṁB,G2* 分别是流入端口 **A2** 和 **B2** 的质量流量。
- *ρavg,G2* 是所有段上的平均气体密度。
- *ṁthres,G2* 是压力损失的层流阈值，近似为标称质量流量的 1e-4。该模块计算压力损失系数 *KG2*，使得 *pA,G2* – *pB,G2* 在标称质量流量下与标称压力损失匹配。

### 气体质量和能量守恒

该模块对两种气体使用相同的质量和能量守恒表达式。为简单起见，本节中的方程针对一侧，但适用于两侧。

(dpGdt∑segments(∂ρseg,G∂p)+∑segments(dTseg,Gdt∂ρseg,G∂T))VGN=m˙A,G+m˙B,G，

其中：

- ∂ρseg,G∂p 是段内密度对压力的偏导数。
- ∂ρseg,G∂T 是段内密度对温度的偏导数。
- *Tseg,G* 是该段的温度。
- *VG* 是总气体体积。

求和是对所有段进行的。

**注意**

尽管该模块将气体流分为 *N*=3 个段进行传热计算，但它假设所有段处于相同的内部压力 *pG*。因此，*pG* 在求和之外。

每个段的能量守恒方程为

(dpGdt∂useg,G∂p+dTseg,Gdt∂useg,G∂T)MGN+useg,G(m˙seg,in,G−m˙seg,out,G)=Φseg,in,G−Φseg,out,G+Qseg,G，

其中：

- ∂useg,G∂p 是段内比内能对压力的偏导数。
- ∂useg,G∂T 是段内比内能对温度的偏导数。
- *MG* 是总气体质量。
- *ṁseg,in,G* 和 *ṁseg,out,G* 是流入和流出该段的质量流量。
- *Φseg,in,G* 和 *Φseg,out,G* 是流入和流出该段的能量流量。

该模块假设段之间的质量流量在 *ṁA,G* 和 *ṁB,G* 的值之间线性分布。
