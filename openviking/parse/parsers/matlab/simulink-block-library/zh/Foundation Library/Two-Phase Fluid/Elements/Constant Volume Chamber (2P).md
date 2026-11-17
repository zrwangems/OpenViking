---
type: simulink-block
title: 'Constant Volume Chamber (2P)'
family: 'two-phase-fluid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'constantvolumechamber2p'
documentation_source_path: 'ref/constantvolumechamber2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Volume Chamber (2P)

## 端口

### 守恒

### **A** — 腔室入口两相流体

与腔室入口相关联的两相流体守恒端口。

### **B** — 腔室入口两相流体

与第二个腔室入口相关联的两相流体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of ports** 参数设置为 `2`、`3` 或 `4`。

### **C** — 腔室入口两相流体

与第三个腔室入口相关联的两相流体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of ports** 参数设置为 `3` 或 `4`。

### **D** — 腔室入口两相流体

与第四个腔室入口相关联的两相流体守恒端口。如果腔室有四个入口端口，您可以将该模块用作交叉连接中的连接点。

#### 依赖关系

要启用此端口，请将 **Number of ports** 参数设置为 `4`。

### **H** — 热端口 thermal

热守恒端口，腔室中的流体通过它与热网络交换热量。

## 参数

### 主要

### **Chamber volume** — 腔室内流体体积 `0.001 m^3`（默认值）| 正标量

腔室中的流体体积。在仿真期间该体积保持不变。

### **Number of ports** — 腔室中入口端口的数量 `1`（默认值）| `2` | `3` | `4`

腔室中入口端口的数量。腔室可以具有一到四个端口，标记为 **A** 到 **D**。修改参数值时，相应的端口会在模块图标中显示或隐藏。

### **Cross-sectional area at port A** — 垂直于流动方向的入口面积 `0.01 m^2`（默认值）| 正标量

端口 **A** 处垂直于流动方向的入口面积。

### **Cross-sectional area at port B** — 垂直于流动方向的入口面积 `0.01 m^2`（默认值）| 正标量

端口 **B** 处垂直于流动方向的入口面积。

#### 依赖关系

要启用此参数，请将 **Number of ports** 设置为 `2`、`3` 或 `4`。

### **Cross-sectional area at port C** — 垂直于流动方向的入口面积 `0.01 m^2`（默认值）| 正标量

端口 **C** 处垂直于流动方向的入口面积。

#### 依赖关系

要启用此参数，请将 **Number of ports** 设置为 `3` 或 `4`。

### **Cross-sectional area at port D** — 垂直于流动方向的入口面积 `0.01 m^2`（默认值）| 正标量

端口 **D** 处垂直于流动方向的入口面积。

#### 依赖关系

要启用此参数，请将 **Number of ports** 设置为 `4`。

### 效应和初始条件

### **Initial fluid energy specification** — 用于定义初始条件的热力学变量 `Temperature`（默认值）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于定义模块初始条件的热力学变量。

**Initial fluid energy specification** 参数的值限制两相流体的可用初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸气。您不能指定液-气混合物，因为在液-气混合物区域中温度是恒定的。
- `Vapor quality` — 指定初始状态为液-气混合物。您不能指定过冷液体或过热蒸气，因为在整个区域中液体质量分数分别为 0 和 1。此外，该模块将压力限制为低于临界压力。
- `Vapor void fraction` — 指定初始状态为液-气混合物。您不能指定过冷液体或过热蒸气，因为在整个区域中液体质量分数分别为 0 和 1。此外，该模块将压力限制为低于临界压力。
- `Specific enthalpy` — 指定流体的比焓。该模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。该模块不限制初始状态。

### **Initial pressure** — 仿真开始时的绝对压力 `0.101325 MPa`（默认值）| 正标量

仿真开始时腔室中的压力，相对于绝对零压指定。

### **Initial temperature** — 仿真开始时的绝对温度 `293.15 K`（默认值）| 正标量

仿真开始时腔室中的温度，相对于绝对零度指定。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial vapor quality** — 仿真开始时的蒸气质量分数 `0.5`（默认值）| 0 到 1 之间的无量纲标量

仿真开始时腔室中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial vapor void fraction** — 仿真开始时蒸气的体积分数 `0.5`（默认值）| 0 到 1 之间的无量纲标量

仿真开始时腔室中蒸气的体积分数。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial specific enthalpy** — 仿真开始时的比焓 `1500 kJ/kg`（默认值）| 正标量

仿真开始时腔室中流体的比焓。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial specific internal energy** — 仿真开始时的比内能 `1500 kJ/kg`（默认值）| 正标量

仿真开始时腔室中流体的比内能。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### **Phase change time constant** — 相变事件的特性持续时间 `0.1 s`（默认值）| 正标量

腔室中发生的相变事件达到平衡的特性时间。增大此参数可减慢相变速率，或减小它以提高速率。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2022b：条件性入口端口可见性

Constant Volume Chamber (2P) 模块可以具有一到四个入口端口，由 **Number of ports** 参数值控制。

在之前的版本中，该模块只有一个入口端口。Two-Phase Fluid 库还包含单独的两端口和三端口模块，这些模块已不再可用。此更改没有兼容性影响。当您打开现有模型时，其中的所有两端口和三端口腔室模块都会自动替换为具有相应数量守恒端口的 Constant Volume Chamber (2P) 模块。

四端口腔室在之前的版本中不可用。

## 描述

具有固定两相流体体积和可变端口数量的腔室

Constant Volume Chamber (2P) 模块对包含固定体积两相流体的腔室中的质量和能量积聚进行建模。腔室可以具有一到四个入口，标记为 **A** 到 **D**，流体可通过这些入口流动。流体体积可以通过热端口 **H** 与热网络（例如表示腔室周围环境的热网络）交换热量。

腔室中流体的质量随密度而变化，对于两相流体，密度通常是压力和温度的函数。当入口上游的压力升至高于腔室中的压力时，流体会进入；当压力梯度反向时，流体会流出。在模型中，其效果通常是平滑压力的突然变化，很像电容器对电压的作用。

假设入口与腔室内部之间的流动阻力可忽略不计。因此，内部压力等于入口处的压力。类似地，假设热端口与腔室内部之间的热阻可忽略不计。内部温度等于热端口处的温度。

### 质量平衡

质量可以通过端口 **A**、**B**、**C** 和 **D** 进入和离开腔室。腔室的体积是固定的，但流体的可压缩性意味着其质量会随压力和温度变化。腔室中的质量积聚速率必须恰好等于通过端口 **A**、**B**、**C** 和 **D** 的质量流量，

[(∂ρ∂p)udpdt+(∂ρ∂u)pdudt]V=m˙A+m˙B+m˙C+m˙D+ϵM,

其中左侧是质量积聚速率，并且：

- *ρ* 是密度。
- *p* 是压力。
- *u* 是比内能。
- *V* 是体积。
- m˙ 是质量流量。
- *ϵ*M 是修正项，用于考虑由偏导数平滑引起的数值误差。

**偏导数平滑的修正项**

该模块通过对 Two-Phase Fluid Properties (2P) 模块中的表格数据应用有限差分法并对结果进行插值，来计算质量平衡方程中的偏导数。然后，该模块通过三次多项式函数在相变边界处平滑偏导数。这些函数应用于：

- 当蒸气干度在 0–0.1 范围内时，应用于过冷液体和两相混合物相域。
- 当蒸气干度在 0–0.9 范围内时，应用于两相混合物和过热蒸气相域。

平滑会引入较小的数值误差，该模块通过向质量平衡中添加修正项 *ϵ*M 来调整该误差，其定义为：

ϵM=M−V/ντ.

其中：

- *M* 是腔室中的流体质量。
- *ν* 是比体积。
- *τ* 是相变事件的特性持续时间。

该模块通过以下方程获得腔室中的流体质量：

dMdt=m˙A+m˙B+m˙C+m˙D.

### 能量平衡

能量可以通过两种方式进入和离开腔室：通过端口 **A**、**B**、**C** 和 **D** 的流体流动，以及通过端口 **H** 的热流。腔室内的流体不做功，也不对其做功。内部流体体积中的能量积聚速率必须等于通过端口 **A**、**B**、**C**、**D** 和 **H** 进入的能量流率之和，

E˙=ϕA+ϕB+ϕC+ϕD+​QH,

其中：

- *ϕ* 是能量流率。
- *Q* 是热流率。
- *E* 是总能量。

忽略流体的动能，腔室中的总能量为：

E=Mu.

### 动量平衡

假设各个端口与腔室内部之间由黏性摩擦引起的压降可忽略不计。忽略重力以及其他体积力。因此，内部流体体积中的压力必须等于端口 **A**、**B**、**C** 和 **D** 处的压力：

p=pA=pB=pC=pD.

### 假设和限制

- 腔室具有固定的流体体积。
- 入口与腔室内部之间的流动阻力可忽略不计。
- 热端口与腔室内部之间的热阻可忽略不计。
- 腔室中流体的动能可忽略不计。
