---
type: simulink-block
title: 'Fuel Cell Equivalent Circuit'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cells'
documentation_page: 'fuelcellequivalentcircuit'
documentation_source_path: 'ref/fuelcellequivalentcircuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Fuel Cell Equivalent Circuit

## 端口

### 输入

### **Anode water content** — 阳极中的水含量，无量纲物理信号

与阳极中的水含量关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请在 **Membrane** 设置中将 **Interface for lambda boundary conditions** 设置为 `Physical Signal Inputs`。

### **Cathode water content** — 阴极中的水含量，无量纲物理信号

与阴极中的水含量关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请在 **Membrane** 设置中将 **Interface for lambda boundary conditions** 设置为 `Physical Signal Inputs`。

### **Cell temperature** — 电池温度，K 物理信号

与电池温度关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请在 **Thermal** 设置中将 **Interface for temperature** 设置为 `Physical Signal Inputs`。
### 守恒

### **+** — 燃料电池正极端子电气

与燃料电池正极端子关联的电气守恒端口。

### **-** — 燃料电池负极端子电气

与燃料电池负极端子关联的电气守恒端口。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Active surface area** — 活性电池的总表面积 `14.8` `cm^2`（默认）| 正标量

活性电池的总表面积。

### 开路电压

### **Open-circuit voltage** — 开路电压 `1.23` `V`（默认）| 非负标量

开路电压。模块使用此值计算理想 PEM 燃料电池的电位。

### **Terminal voltage operating range, [Min Max]** — 端子电压的工作范围 `[0, inf]` `V`（默认）| 两个非负标量的向量

端子电压的工作范围。

### 过电位

### **Tafel slope** — Tafel 斜率 `0.0136` `V`（默认）| 非负标量

Tafel 斜率。模块使用此值计算理想 PEM 燃料电池的电位。

### **Nominal exchange current** — 标称交换电流 `0.04777` `A`（默认）| 正标量

标称交换电流。模块使用此值计算理想 PEM 燃料电池的电位。

### **Activation and concentration equivalent resistance** — 活化和浓差等效电阻 `5e-3` `Ohm`（默认）| 正标量

活化和浓差等效电阻。模块使用此值对燃料电池的动态过电位贡献进行建模。

### **Overpotential time constant** — 过电位时间常数 `100` `s`（默认）| 正标量

过电位时间常数。模块使用此值对燃料电池的动态过电位贡献进行建模。

### 膜

### **Total membrane thickness** — 膜的总厚度 `0.127` `mm`（默认）| 正标量

膜的总厚度。

### **Dry density of material** — 膜材料的干密度 `19` `g/cm^3`（默认）| 正标量

膜材料的干密度。

### **Molecular mass of material** — 材料的分子质量 `1400` `g/mol`（默认）| 正标量

膜材料的分子质量。

### **Number of membrane discretizations** — 膜离散化数量 `3`（默认）| 正标量

膜离散化数量。此参数的值指定将膜划分成的切片数量。

### **Interface for lambda boundary conditions** — lambda 边界条件的选项 `Mask Parameters`（默认）| `Physical Signal Inputs`

将 lambda 边界条件指定为掩码参数或物理信号输入。

### **Anode water content** — 阳极中的水含量 `1`（默认）| 非负标量

阳极中的水含量。

#### 依赖关系

要启用此参数，请将 **Interface for lambda boundary conditions** 设置为 `Mask Parameters`。

### **Cathode water content** — 阴极中的水含量 `1`（默认）| 非负标量

阴极中的水含量。

#### 依赖关系

要启用此参数，请将 **Interface for lambda boundary conditions** 设置为 `Mask Parameters`。

### **Initial lambda of each slice** — 每个切片的初始 lambda `1`（默认）| 非负标量

每个切片的 lambda 初始值。

### **Interface for diffusion parameters** — 扩散参数的选项 `Mask Parameters`（默认）| `Lookup table` | `Literature Heuristic`

将 lambda 边界条件指定为掩码参数、查找表或使用文献启发式方法。

### **Diffusion coefficient** — 扩散系数 `1.5e-10` `m^2/s`（默认）| 正标量

扩散系数。

#### 依赖关系

要启用此参数，请将 **Interface for diffusion parameters** 设置为 `Mask Parameters`。

### **Diffusion coefficient table data (1-D)** — 扩散系数表数据 `[1e-10, 1.5e-10]` `m^2/s`（默认）| 正标量的向量

扩散系数的查找表数据。此参数的值必须是至少包含两个正标量的向量。此向量的元素数量必须等于 **Diffusion coefficient breakpoints** 参数值的元素数量。

#### 依赖关系

要启用此参数，请将 **Interface for diffusion parameters** 设置为 `Lookup table`。

### **Diffusion coefficient breakpoints** — 扩散系数查找表的断点 `[0, 400]` `K`（默认）| 非负标量的向量

扩散系数查找表数据的断点。此参数的值必须是至少包含两个严格递增的非负标量的向量。此向量的元素数量必须等于 **Diffusion coefficient table data (1-D)** 参数值的元素数量。

#### 依赖关系

要启用此参数，请将 **Interface for diffusion parameters** 设置为 `Lookup table`。

### **Interface for electro-osmotic drag parameters** — 电渗透拖曳参数的选项 `Mask Parameters`（默认）| `Lookup table` | `Literature Heuristic`

将 lambda 边界条件指定为掩码参数、查找表或使用文献启发式方法。

### **Electro-osmotic drag coefficient** — 电渗透拖曳系数 `2.5`（默认）| 正标量

电渗透拖曳系数。

#### 依赖关系

要启用此参数，请将 **Interface for electro-osmotic parameters** 设置为 `Mask Parameters`。

### **Drag table data (1-D)** — 拖曳表数据 `[1, 2.5, 2.5]`（默认）| 非负标量的向量

拖曳的查找表数据。此参数的值必须是至少包含两个非负标量的向量。此向量的元素数量必须等于 **Electro-osmotic drag coefficient breakpoints** 参数值的元素数量。

#### 依赖关系

要启用此参数，请将 **Interface for electro-osmotic parameters** 设置为 `Lookup table`。

### **Electro-osmotic drag coefficient breakpoints** — 拖曳系数查找表的断点 `[1, 14, 20]`（默认）| 非负标量的向量

拖曳系数查找表数据的断点。此参数的值必须是至少包含两个严格递增的标量的向量。此向量的元素数量必须等于 **Drag table data (1-D)** 参数值的元素数量。

#### 依赖关系

要启用此参数，请将 **Interface for electro-osmotic parameters** 设置为 `Lookup table`。

### **Drag scale factor** — 拖曳比例因子 `1`（默认）| 正标量

拖曳比例因子。该值对模块用于根据水含量对电渗透拖曳进行建模的启发式方程进行缩放。

#### 依赖关系

要启用此参数，请将 **Interface for electro-osmotic parameters** 设置为 `Literature Heuristic`。

### 热

### **Interface for temperature** — 温度参数的选项 `Mask Parameters`（默认）| `Physical Signal Inputs`

将电池温度指定为掩码参数或物理信号输入。

### **Cell temperature** — 燃料电池的温度 `303.15` `K`（默认）| 正标量

燃料电池的温度。

#### 依赖关系

要启用此参数，请将 **Interface for temperature** 设置为 `Mask Parameters`。

## 所属库

Simscape / Battery / Cells

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

使用电路元件和动态膜水含量建模的聚合物电解质膜燃料电池

Fuel Cell Equivalent Circuit 模块通过使用电路元件和确定电池欧姆损耗的动态膜水含量模型来对聚合物电解质膜（PEM）燃料电池进行建模。

Fuel Cell Equivalent Circuit 模块对燃料电池的以下部分进行建模：

- 燃料电池电位 — 使用 Tafel 方程近似损耗来对理想 PEM 燃料电池电位进行建模。
- 燃料电池动态过电位 — 对燃料电池的动态过电位贡献进行建模。
- 燃料电池膜 — 对水含量动态进行建模。

### 燃料电池电位

模块通过使用 Tafel 方程近似损耗来对理想 PEM 燃料电池电位进行建模：

E=Eoc−A⋅ln(II0).

在此方程中：

- *EOC* 是标称电位，等于 **Open-circuit voltage** 参数的值。
- *A* 是 **Tafel slope** 参数的值，单位为伏特。
- *I0* 是 **Nominal exchange current** 参数的值，单位为安培。
- *I* 是从燃料电池汲取的电流，单位为安培。

### 燃料电池动态过电位

模块对燃料电池的动态过电位贡献进行建模：

1Rd(τdvddt+vd)=I.

在此方程中：

- *τ* 是 **Overpotential time constant** 参数的值，单位为秒。
- *Rd* 是 **Activation and concentration equivalent resistance** 参数的值，单位为欧姆。
- *vd* 是考虑燃料电池动态的电压降。

### Fuel Cell Membrane

该模块通过将膜厚度从阳极到阴极离散化为多个切片，对燃料电池膜的欧姆电阻动态特性进行建模。水通过每个切片的净摩尔流量决定了局部水含量，从而决定了质子流的局部电阻。该模块通过对所有切片电阻求和来计算总膜欧姆电阻。

下图描述了燃料电池膜薄元件的控制体积分析：

燃料电池膜薄元件的控制体积分析。左侧，W\_in 表示流入膜切片的水分子的摩尔流率，单位为 mol/s。右侧，W\_out 表示流出切片控制体积的水分子的摩尔流率，单位为 mol/s。

该模块应用质量守恒定律来生成第 *i* 个膜切片内水含量的控制方程，

αdλidt=Win−Wout,

其中：

- *Win* 是流入膜切片的水分子的摩尔流率，单位为 mol/s。
- *Wout* 是流出切片控制体积的水分子的摩尔流率，单位为 mol/s。
- *λi* 是一个无量纲值，用于表示相对于膜材料的局部水浓度。累积的水量与通过膜切片的水的净摩尔流量成正比。

在该方程中，*α* 是一个常数，等于

α=S⋅δN⋅ρΜ,

其中：

- *S* 是 **Active surface area** 参数的值。
- *δ/N* 是切片厚度。*δ* 是 **Total membrane thickness** 参数的值。*N* 是 **Number of membrane discretizations** 参数的值。
- *ρ* 是 **Dry density of material** 参数的值。
- *Μ* 是 **Molecular mass of material** 参数的值。

扩散和电渗透拖曳是水通过燃料电池膜传输的两个关键机制。氢燃料电池在阴极产生水分子，并通过扩散机制，水分子向膜的阳极侧扩散。电渗透拖曳将水分子从膜的阳极侧转移到阴极侧。扩散机制可以在阳极和阴极之间双向进行，而电渗透拖曳仅导致水分子从阳极流向阴极。

这些方程描述了扩散和电渗透拖曳机制：

Wdrag=κ1GIλWdiff=κ2Ddλdz

在这些方程中：

- *dz* 指的是进入膜的长度，从阳极或膜界面开始测量。
- *dλ* 表示在长度为 *dz* 的膜上水含量的差值。
- *G* 是电渗透拖曳系数。要指定此值，请将 **Interface for electro-osmotic drag parameters** 参数设置为：

  - `Mask Parameters` — *G* 是常数，等于 **Electro-osmotic drag coefficient** 参数的值。
  - `Lookup table` — 该模块通过使用 **Drag table data (1-D)** 和 **Electro-osmotic drag coefficient breakpoints** 参数的值来计算 *G* 的值。查找表的值基于平均膜水含量。
  - `Literature Heuristic` — 该模块通过使用文献启发式和 **Drag scale factor** 参数的值来控制 *G*。
- *D* 是扩散系数。要指定此值，请将 **Interface for diffusion parameters** 参数设置为：

  - `Mask Parameters` — *D* 是常数，等于 **Diffusion coefficient** 参数的值。
  - `Lookup table` — 该模块通过使用 **Diffusion coefficient table data (1-D)** 和 **Diffusion coefficient breakpoints** 参数的值来计算 *D* 的值。查找表的值基于温度。
  - `Literature Heuristic` — 该模块通过使用从实验推导出的经验函数来控制 *D*。
- κ1=122F，其中 *F* 是法拉第常数，单位为 `S*A/mol`。
- κ2=S⋅ρΜ⋅δN。

该模块将整个膜厚度视为一系列链接的切片，并具有适当且各自的边界条件。在第 *i* 个切片处，该模块将水的摩尔流入和流出视为两种水传输机制的贡献。该模块假设这两种机制独立地对水的摩尔质量流量做出贡献：

Win=Wdrag,in+Wdiff,inWout=Wdrag,out+Wdiff,out

对于厚度为 *δ/N* 的一般膜切片 *i*，该模块假设：

- 由于电渗透拖曳进入第 *i* 个切片的水分子等于由于电渗透拖曳离开第 *i-1* 个切片的水分子。
- 由于电渗透拖曳离开第 *i* 个切片的水分子等于：

  Wdrag,out,i=κ1GIλiWdrag,in,i=Wdrag,out,i−1
- 由于扩散进入和离开第 *i* 个切片的水分子等于：

  Wdiff,out,i=κ2Dλi−λi+1δNWdiff,in,i=κ2Dλi−1−λiδN
- 电流 *I* 对于所有膜切片是恒定的。质子流严格在平面内，并且在每个切片中相等。

通过求解 *λi* 的动态系统，该模块通过对每个切片评估以下方程来确定电导率 *σ*，单位为 S/m：

σ=(0.005139λ−0.00326)e1268(1303.15−1T),

其中 *T* 是温度，单位为开尔文。您可以将每个切片的电导率转换为切片电阻。总膜电阻等于每个切片电阻之和。

**边界条件**

燃料电池膜模型考虑膜离散切片的水含量动态特性。该模块还必须考虑膜外边缘的环境。为了建立整个膜的边界条件，该模块假设：

- 在阳极侧，水的摩尔流入仅由扩散引起。
- 在阴极侧，水的摩尔流出由电渗透拖曳和扩散共同引起。

要设置膜的边界条件，请将 **Interface for lambda boundary conditions** 参数设置为以下选项之一：

- `Mask Parameters` — 通过使用 **Anode water content** 和 **Cathode water content** 参数直接指定边界条件的值。
- `Physical Signal Inputs` — 使用 **Anode water content** 和 **Cathode water content** 输入端口从外部控制边界条件。
