---
type: simulink-block
title: 'Tank (G-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Tanks & Accumulators'
documentation_page: 'tankgtl'
documentation_source_path: 'ref/tankgtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Tank (G-TL)

## 端口

### 输出

### **V** — 热液体体积，`m^3` 物理信号

物理信号输出端口，报告储罐中热液体的体积，单位为 m3。

### **L** — 热液体液位，`m` 物理信号

物理信号输出端口，报告热液体体积相对于储罐底部的高度，单位为 m。
### 守恒

### **A1** — 气体入口 气体

与气体流入或流出储罐的开口相关联的气体守恒端口。

### **B1** — 气体入口 气体

与气体流入或流出储罐的开口相关联的气体守恒端口。

### **A2** — 热液体入口 热液体

与热液体流入或流出储罐的开口相关联的热液体守恒端口。

### **B2** — 热液体入口 热液体

与热液体流入或流出储罐的开口相关联的热液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **C2** — 热液体入口 热液体

与热液体流入或流出储罐的开口相关联的热液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`3`、`4`、
`5` 或
`6`。

### **D2** — 热液体入口 热液体

与热液体流入或流出储罐的开口相关联的热液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`4`、`5` 或
`6`。

### **E2** — 热液体入口 热液体

与热液体流入或流出储罐的开口相关联的热液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`5` 或
`6`。

### **F2** — 热液体入口 热液体

与热液体流入或流出储罐的开口相关联的热液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`6`。

### **H1** — 气体温度 热

与气体体积内部温度相关联的热守恒端口。

### **H2** — 热液体温度 热

与热液体体积内部温度相关联的热守恒端口。

## 参数

### **Number of inlets** — 热液体端口数量 `1`（默认）| `2` | `3` | `4` | `5` | `6`

模块的热液体端口数量。

### **Total tank volume** — 气体和热液体体积之和 `10 m^3`（默认）| 正标量

储罐中气体和热液体部分的总容积。

### **Tank volume parameterization** — 热液体体积的参数化方式 `Constant cross-sectional area`（默认）| `Tabulated data — volume vs. level`

热液体体积的参数化方式选择。选择
`Constant cross-sectional area` 以指定恒定的储罐横截面积。选择 `Tabulated data
— volume vs. level` 以通过表格数据的插值或外推来计算热液体体积。

### **Tank cross-sectional area** — 恒定储罐横截面的面积 `1` m^2（默认）| 正标量

储罐横截面的面积。模块假定该值在允许的液位范围内恒定。模块使用此参数计算储罐内热液体的体积。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Constant cross-sectional
area`。

### **Liquid level vector** — 指定热液体体积所对应的热液体液位 `[0, 3, 5]` m（默认）| 向量

用于指定储罐中热液体体积的热液体液位向量。模块使用此向量构建热液体体积作为热液体液位函数的单向查找表。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Tabulated data - volume
vs. level`。

### **Liquid volume vector** — 指定热液体液位下的热液体体积 `[0, 4, 6]` m^3（默认）| 向量

与 **Liquid level vector** 参数元素对应的热液体体积向量。模块使用此向量构建热液体体积作为热液体液位函数的单向查找表。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Tabulated data - volume
vs. level`。

### **Cross-sectional area vector for inlets A1 and B1** — 气体入口的流通面积 `[.01, .01] m^2`（默认）| 向量

指定气体入口流通面积的双元素向量。

### **Inlet height at port A2** — 热液体入口的高度 `0.1 m`（默认）| 正标量

热液体入口的高度。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`1`。

### **Cross-sectional area at port A2** — 热液体入口的流通面积 `0.01 m^2`（默认）| 正标量

热液体入口的流通面积。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`1`。

### **Height vector for inlets A2 and B2** — 端口高度向量 `[.1, .1]` m（默认）| 1×*n* 向量

多个已启用端口的高度向量。参数名称和向量长度取决于 **Number of
inlets** 参数的值。向量的每个元素对应一个入口端口，从端口 **A2** 开始。每个入口的默认高度为 `.1 m`。此向量的每个元素必须大于或等于 0。

例如，如果 **Number of inlets** 为
`4`，则此参数的名称为
**Height vector for inlets A2, B2, C2, and D2**，默认值为 `0.1 * ones(1, 4)` m。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **Cross-sectional area vector for inlets A2 and B2** — 端口入口面积向量 `[.01, .01] m^2`（默认）| 1×*n* 向量

多个已启用端口的横截面积向量。参数名称和向量长度取决于 **Number of
inlets** 参数的值。向量的每个元素对应一个入口端口，从端口 **A2** 开始。每个入口的默认高度为 `.01 m`。此向量的每个元素必须大于 0。

例如，如果 **Number of inlets** 为
`4`，则此参数的名称为
**入口 A2、B2、C2 和
D2**，默认值为 `0.01 * ones(1,
4)` m2。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **Liquid volume above max capacity** — 是否收到储罐体积过高的通知 `None`（默认）| `Warning` | `Error`

是否在仿真期间储罐流体体积超过 **Total tank volume** 参数值时收到通知。将此参数设置为 `Warning` 以在仿真期间发生此情况时收到警告。将此参数设置为
`Error` 以在发生此情况时停止仿真。

### **Maximum tank liquid capacity** — 储罐的填充限值 `10 m^3`（默认）| 正标量

储罐的填充限值。

#### 依赖关系

要启用此参数，请将 **Liquid volume above max
capacity** 设置为 `Warning` 或
`Error`。

### **Gravitational acceleration** — 重力加速度常数 `9.81` m/s^2（默认）| 正标量

储罐所在高度处的重力加速度值。模块假定该值在储罐高度范围内恒定。

## 所属库

Simscape / Fluids / Thermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2023b：最多可建模六个热液体端口

以前，Tank (G-TL) 模块最多只能建模三个热液体端口。现在，您可以使用 **Number of inlets** 参数来建模最多六个热液体端口。

## 描述

具有可变气体和热液体体积的加压罐

Tank (G-TL) 模块对具有独立气体和热液体体积的腔室中的质量和能量积聚进行建模。总流体体积是固定的，但各个气体和热液体体积可以变化。两个气体端口允许气体流动，数量可变的热液体端口（范围从一到六）允许热液体流动。热液体端口可以处于不同的高度。

图示：罐中热液体达到高度 y，并包含端口 A2、B2 和 C2。罐的顶部包含气体以及端口 A1 和 B1。

该罐是加压的，但压力不是固定的。它在仿真过程中随气体体积中的压力而变化。当气体体积的压力升高时，压力升高；当气体体积的压力降低时，压力降低。假设热液体体积与气体体积处于平衡状态，因此其压力与气体压力相同。

流体体积可以与其他流体组件以及环境交换能量，但彼此之间不能交换能量。流体体积的行为就像它们被绝缘膜彼此隔离一样。与其他组件的能量交换通过气体或热液体端口发生，而与环境的交换严格以热量的形式通过热端口发生。

使用此模块来建模诸如排水罐之类的组件，其中从压缩气体系统中冷凝出的水因重力而被截留在底部，并通过排水出口排出。但请注意，气体域和热液体域都不捕捉相变效应——因此该模块无法捕捉冷凝效应。

### 热液体端口

您可以使用 **Number of inlets** 参数指定热液体端口的数量：

| Number of inlets | 暴露的热液体端口 |
| --- | --- |
| `1` | 端口 **A2** |
| `2` | 端口 **A2** 和 **B2** |
| `3` | 端口 **A2**、**B2** 和 **C2** |
| `4` | 端口 **A2**、**B2**、**C2** 和 **D2** |
| `5` | 端口 **A2**、**B2**、**C2**、**D2** 和 **E2** |
| `6` | 端口 **A2**、**B2**、**C2**、**D2**、**E2** 和 **F2** |

### 流体体积

罐的总体积等于其所包含的气体和热液体体积之和，

VT=VL+VG，

其中 *V* 是体积，*T*、*L* 和 *G* 分别表示总体、液体和气体。由于总体积是固定的，气体体积的时间变化率必须与热液体体积测得的变化率相反，

V˙G=−V˙L。

热液体体积的时间变化率通过对表达式

ML=ρLVL

求导来计算，其中 *M* 是质量，*ρ* 是密度。求导得到进入热液体体积的质量流量，

M˙L=VLρ˙L+V˙LρL，

热液体密度的时间变化率为

ρ˙L=ρLβLp˙L−αLρLT˙L，

其中：

- *β* 是热体积模量。
- *ɑ* 是等压热膨胀系数。
- *p* 是流体压力。
- *T* 是流体温度。

整理各项后得到热液体体积的变化率，并由此得到气体体积的变化率

V˙G=−V˙L≈VL(p˙LβL−αLT˙L)−M˙LρL。

### 质量平衡

每个流体体积中的质量积聚率等于进入该流体体积的净质量流量。在热液体体积中

M˙L=∑i=A2,B2,...F2m˙i，

*M*L 是热液体体积中的质量积聚率，m˙i 是通过热液体端口 **A2**、**B2**、**C2**、**D2**、**E2** 或 **F2** 进入该体积的各个质量流量。质量积聚率包含来自压力、温度和体积变化的贡献，

M˙L=VL(ρLβLp˙G−αLρLT˙L)+V˙LρL，

其中根据定义，热液体体积的压力等于气体体积的压力，因此该方程以气体压力表示。在气体体积中

M˙G=∑i=A1, B1m˙i，

其中 *MG* 是气体体积中的质量积聚率，m˙i 是通过气体端口 **A1** 和 **B1** 进入该体积的各个质量流量。与热液体体积一样，质量积聚率包含来自压力、温度和体积变化的贡献

M˙G=dMdp|Gp˙G+dMdT|GT˙G+V˙GρG，

其中压力和温度导数取决于 Gas Properties (G) 模块中指定的气体类型。Translational Mechanical Converter (G) 页面的方程部分定义了这些导数。将 *VG* 替换为此变量先前获得的表达式，并合并 *MG* 的两个表达式

dMdp|Gp˙G+dMdT|GT˙G+[VL(p˙GβL−αLT˙L)−M˙LρL]ρG=∑i=A1, B1m˙i。

整理各项后得到气体体积中质量平衡的最终表达式

p˙G(dMdp|G+ρGVLβL)+(T˙GdMdT|G−T˙LρGVLαL)=∑i=A1, B1m˙i+ρGρL∑i=A2, B2,...F2m˙i，

其中 M˙L 已替换为进入热液体体积的质量流量之和。

### 能量平衡

每个流体体积中的能量积聚率是流体入口的能量流率、通过相应热端口的热流率以及由体积变化引起的能量流率之和。对于气体体积

p˙G(dUdp|G+ρGhGVLβL)+(T˙GdUdT|G−T˙LρGhGVLαL)=QH1+∑i=A1, B1ϕi+ρGρLhG∑i=A2, B2,...F2m˙i，

其中：

- *U* 是流体体积的总能量。
- *h* 是流体焓。
- *Q* 是通过热端口的热流率。
- *ϕi* 是通过流体入口的能量流率。

如前所述，压力和温度导数取决于 Gas Properties (G) 模块中指定的气体类型。有关定义，请参见 Translational Mechanical Converter (G) 页面的方程部分。对于热液体体积

p˙LdUdp|L+T˙LdUdT|L=QH2+∑i=A2, B2,...F2ϕi+∑i=A2, B2,...F2m˙g(y(i)−y)−hL∑i=A2, B2,...F2m˙i，

其中压力导数为

dUdp|L=−TLαLVL，

温度导数为

dUdT|L=cp,LρLVL，

其中 *c*p 是罐内热液体的等压比热。

### 动量平衡

两个流体体积中都忽略由摩擦或其他原因引起的流动阻力。该模块还忽略高度对入口压力的影响，但仅在气体侧如此。因此，气体入口压力彼此相等，并且等于气体体积的内部压力

pA1=pB1=pG。

热液体入口压力各自是入口深度的函数。热液体体积的内部压力等于气体体积压力，*pL* = *pG*。该模块通过以下方程包含入口处的动压 *p*i*,dyn*

pi+pi,dyn=pG+ρL(y−yi)g，

其中 *y* 是热液体表面的高度，*y*i 是热液体入口的高度，*g* 是重力常数。项 *y* - *yi* 给出热液体入口相对于气体-热液体边界的深度。每个热液体入口处的动压取决于该入口处的流动方向

pi,dyn={12ρivi2,if m˙i<00,if m˙i≥0

其中 *vi* 是流速。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参见 Set Priority and Initial Target for Block Variables 和 Initial Conditions for Blocks with Finite Gas Volume。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参见 Modify Nominal Values for a Block Variable。

### 假设与限制

- 由于流体突然膨胀进入罐体容积，流体动量在罐体入口处损失。
