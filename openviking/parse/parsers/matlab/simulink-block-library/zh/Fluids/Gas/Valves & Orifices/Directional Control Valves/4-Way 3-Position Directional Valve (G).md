---
type: simulink-block
title: '4-Way 3-Position Directional Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Directional Control Valves'
documentation_page: '4way3positiondirectionalvalveg'
documentation_source_path: 'ref/4way3positiondirectionalvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 3-Position Directional Valve (G)

## 端口

### 输入

### **S** — 阀控制信号，`unitless` 物理信号

控制构件相对于其正常未致动位置的瞬时位移，
指定为物理信号。该模块将位移
相对于完全打开
节流口所需控制构件的最大位置进行归一化。该信号是无量纲的，其瞬时值
通常在 `-1` 到
`+1` 的范围内。
### 守恒

### **A** — 阀开口气体

与开口关联的气体守恒端口，流体通过该开口
进入或离开阀。

### **B** — 阀开口气体

与开口关联的气体守恒端口，流体通过该开口
进入或离开阀。

### **P** — 阀开口气体

与开口关联的气体守恒端口，流体通过该开口
进入或离开阀。

### **T** — 阀开口气体

与开口关联的气体守恒端口，流体通过该开口
进入或离开阀。

## 参数

### **Valve parameterization** — 用于指定节流口流量特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量
  系数
  *C*v
  决定模块参数化方法。
- `Kv flow coefficient` — 流量
  系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化方法。
- `Sonic conductance` — 稳态下阻力元件的
  声速导纳决定
  模块参数化方法。
- `Orifice area` — 流动
  限制的尺寸决定
  模块参数化方法。

### **Opening characteristic** — 计算阀开口特性的方法 `Linear`（默认）| `Tabulated`

模块用于计算阀开口面积的方法。线性
设置将开口面积视为节流口
开度分数的线性函数。表格设置允许使用可
以表格形式指定的通用非线性
关系。

### **Opening fraction vector** — 用于指定表格参数数据的控制信号值 `0 : 0.2 : 1`（默认）| 正数向量

用于指定所选流量能力度量的控制信号值向量：
**Sonic conductance vector**、**Cv
coefficient vector**、**Kv coefficient
vector** 或 **Orifice area vector**。控制
信号介于 `0` 和 `1` 之间，
每个值对应阻力元件的开度分数。值越大，开口越大，
流动越容易。

开度分数必须在向量中从左到右单调递增。
该向量的大小必须与 **Sonic conductance
vector**、**Cv coefficient vector**、
**Kv coefficient vector** 或 **Orifice area
vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为
`Tabulated`。

### **Maximum Cv flow coefficient** — 对应于最大开度构件的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积最大时
*Cv* 流量系数的值。此参数
衡量气体在压差驱动下通过阻力元件的
难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Cv flow coefficient`，并将
**Opening characteristic** 设置为
`Linear`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与
出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞流时的值。如果您没有此值，
请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对
许多阀来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Cv flow coefficient` 或 `Kv
flow coefficient`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流口关闭时与打开时的
流量之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为
`Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当节流口处于接近打开或接近关闭位置时，
为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，以提高
这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为
`Linear`。

### **Cv flow coefficient vector** — 对应于开度分数向量中各值的 Cv 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 正数向量

*Cv* 流量系数向量。
每个系数对应于 **Opening fraction
vector** 参数中的一个值。此参数衡量
气体在压差驱动下通过阻力元件的
难易程度。流量系数必须从左到右
单调递增，较大的开度分数表示较大的流量
系数。向量的大小必须与
**Opening fraction vector** 相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Cv flow coefficient`，并将
**Opening characteristic** 设置为
`Tabulated`。

### **Maximum Kv flow coefficient** — 对应于最大开度构件的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积最大时
*Kv* 流量系数的值。此参数
衡量气体在压差驱动下通过阻力元件的
难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Kv flow coefficient`，并将
**Opening characteristic** 设置为
`Linear`。

### **Kv flow coefficient vector** — 对应于开度分数向量中各值的 Kv 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 正数向量

*Kv* 流量系数向量。
每个系数对应于 **Opening fraction
vector** 参数中的一个值。此参数衡量
气体在压差驱动下通过阻力元件的
难易程度。流量系数必须从左到右
单调递增，较大的开度分数表示较大的流量
系数。向量的大小必须与
**Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Kv flow coefficient`，并将
**Opening characteristic** 设置为
`Tabulated`。

### **Maximum sonic conductance** — 对应于最大开度构件的声速导纳 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积最大时
声速导纳的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`，并将 **Opening
characteristic** 设置为
`Linear`。

### **Critical pressure ratio** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到其
最大值（由当地声速给出）时的压力比。压力比是出口
压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`，并将 **Opening
characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态中
质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`。

### **Sonic conductance vector** — 与开度分数向量中的值对应的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声导向量。每个声导对应 **Opening fraction
vector** 参数中的一个值。声导必须从左到右单调递增，较大的开度分数对应较大的声导。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`，并将 **Opening
characteristic** 设置为
`Tabulated`。

### **Critical pressure ratio vector** — 与开度分数向量中的值对应的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次发生阻塞时的临界压力比向量，每个临界压力比对应 **Opening fraction vector** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`，并将 **Opening
characteristic** 设置为
`Tabulated`。

### **Maximum orifice area** — 组件最大开启时对应的流通面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积达到最大时，孔口的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Orifice area`，并将 **Opening
characteristic** 设置为
`Linear`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围在 [0,1] 内的正标量

用于修正理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Orifice area`。

### **Orifice area vector** — 孔口开启面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 向量

孔口开启的横截面积向量。此向量中的值与 **Opening
fraction vector** 参数中的元素一一对应。此向量的第一个元素是孔口泄漏面积，最后一个元素是最大孔口面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Orifice area`，并将 **Opening
characteristic** 设置为
`Tabulated`。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流状态之间转换时的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到
`0.999`。

### **Cross-sectional area at ports A, B, P, and T** — 阀端口处垂直于流动路径的面积 `0.01 m^2`（默认）| 以面积为单位的正标量

阀端口处垂直于流动路径的面积。假设各端口尺寸相同。此处指定的流通面积理想情况下应与相邻组件的入口面积匹配。

#### 阀开度分数偏移

### **Between Ports P and A** — P–A 孔口的开度分数偏移 `0`（默认）| 无量纲标量

当输入信号 **S** 的值为零时，**P**–**A** 孔口的开度分数。此时阀处于正常位置。开度分数衡量滑阀的台肩到其指定孔口（此处为
**P**–**A**）的距离，并按最大距离归一化。它是无量纲的，通常在 `0` 到
`1` 之间。

### **Between Ports B and T** — B–T 孔口的开度分数偏移 `0`（默认）| 无量纲标量

当输入信号 **S** 的值为零时，**B**–**T** 孔口的开度分数。此时阀处于正常位置。开度分数衡量滑阀的台肩到其指定孔口（此处为
**B**–**T**）的距离，并按最大距离归一化。它是无量纲的，通常在 `0` 到
`1` 之间。

### **Between Ports P and B** — P–B 孔口的开度分数偏移 `0`（默认）| 无量纲标量

当输入信号 **S** 的值为零时，**P**–**B** 孔口的开度分数。此时阀处于正常位置。开度分数衡量滑阀的台肩到其指定孔口（此处为
**P**–**B**）的距离，并按最大距离归一化。它是无量纲的，通常在 `0` 到
`1` 之间。

### **Between Ports A and T** — A–T 孔口的开度分数偏移 `0`（默认）| 无量纲标量

当输入信号 **S** 的值为零时，**A**–**T** 孔口的开度分数。此时阀处于正常位置。开度分数衡量滑阀的台肩到其指定孔口（此处为
**A**–**T**）的距离，并按最大距离归一化。它是无量纲的，通常在 `0` 到
`1` 之间。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b：使用改进的流量计算对气体系统进行建模

在之前的版本中，气体库中的模块使用转换因子来以声导的形式实现不同的孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化方式。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked
  flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替换了
  **Cv coefficient (USCS) at leakage flow**、
  **Kv coefficient (SI) at leakage flow**、
  **Sonic conductance at leakage flow** 和
  **Restriction area at leakage flow**
  参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为
  **Opening characteristic**。
- **Reference temperature** 和 **Reference
  density** 参数已分别重命名为 **ISO
  reference temperature** 和 **ISO reference
  density**。
- **Cv coefficient (USCS) at maximum flow** 和
  **Kv coefficient (USCS) at maximum flow**
  参数已分别重命名为 **Maximum Cv
  coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数
  已重命名为 **Maximum sonic
  conductance**。

### R2022b：更新了模块名称

4-Way Directional Valve (G) 模块的标题
更改为 4-Way 3-Position Directional Valve
(G)。

## 描述

气网络中带四个端口的受控阀

四通三位方向阀 (G) 模块表示一个具有四个气体端口（**P**、**A**、**B** 和 **T**）的阀，以及 **P**–**A** 与 **A**–**T** 之间和 **P**–**B** 与 **B**–**T** 之间的流动路径。每条路径均通过一个宽度可变的节流孔。在端口 **S** 处指定的输入信号控制阀芯的位置。当阀芯覆盖节流孔开口时，阀关闭。

在一个典型系统中，**P** 端口连接到泵，**T** 端口连接到油箱，**A** 和 **B** 端口连接到双作用执行器。打开 **P**–**A** 和 **B**–**T** 流动路径允许泵对执行器的一侧加压，并使油箱对另一侧泄压。执行器轴在某些系统中伸出，在另一些系统中缩回。打开 **P**–**B** 和 **A**–**T** 流动路径会翻转执行器的加压侧和泄压侧，使轴能够反向移动。

此图展示了四通三位方向阀在物理系统中的常见用途：

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀的喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀特有的临界值时，发生阻塞。该模块不捕捉超声速流动。

### 阀位置

该阀是连续可变的，并且在一个正常位置和两个工作位置之间平滑切换。

当端口 **S** 处阀芯的瞬时位移为零时，阀恢复到正常位置，此时它不再工作。除非阀芯的台肩相对于其节流孔存在偏移，否则阀完全关闭。工作位置是当阀芯从其正常位置最大程度位移时阀移动到的位置。在一种情况下该位移为正，在另一种情况下为负。

图 **I** 显示了一个位移为正的阀，**P**–**A** 和 **B**–**T** 节流孔完全打开，**P**–**B** 和 **A**–**T** 节流孔完全关闭。图 **II** 显示了一个位移为负的阀，**P**–**A** 和 **B**–**T** 节流孔完全关闭，**P**–**B** 和 **A**–**T** 节流孔完全打开。图 **III** 显示了一个阀芯处于中位且所有节流孔均关闭的阀。

使阀处于工作位置的阀芯位移取决于阀芯上台肩的偏移。**Valve Opening Fraction Offsets** 部分中的参数指定了各端口阀芯位移的模块常量。

**节流孔开度分数**

在阀位置之间，节流孔的开度取决于阀芯台肩相对于边缘的位置。该距离即为节流孔开度，模块对该距离进行归一化，使其值为节流孔完全打开时最大距离的分数。归一化后的变量即为节流孔开度分数。

节流孔开度分数的范围从阀处于图 **I** 所示位置时的 `-1` 到阀处于图 **II** 所示位置时的 `+1`。

模块根据阀芯位移和开度分数偏移计算开度分数。位移和偏移是无量纲的，为最大台肩-节流孔距离的分数。

**P**–**A** 节流孔的开度分数为：

hPA=HPA+x。

**B**–**T** 节流孔的开度分数为：

hBT=HBT+x。

**A**–**T** 节流孔的开度分数为：

hAT=HAT−x。

**P**–**B** 节流孔的开度分数为：

hPB=HPB−x。

在方程中：

- *h* 是节流孔的开度分数。如果计算返回的值超出 `0 - 1` 范围，模块使用最接近的限值。
- *H* 是节流孔的开度分数偏移。**Valve Opening Fraction Offsets** 部分中的参数指定开度分数偏移。为允许不常见的阀配置，模块对其值不施加限制，尽管它们通常在 `-1` 和 `+1` 之间。
- *x* 是阀芯的归一化瞬时位移，由端口 **S** 处的物理信号指定。为补偿极端的开度分数偏移，对信号值没有限制。该值通常在 `-1` 和 `+1` 之间。

**开度分数偏移**

默认情况下，当控制位移为零时，阀完全关闭。在此状态下，阀为零重叠。

您可以偏移阀芯的台肩，以建模负重叠或正重叠阀。负重叠阀在正常位置部分打开。正重叠阀在略超出正常位置时完全关闭。该图显示了节流孔开度分数如何随瞬时阀芯位移变化：

- 图 **I**：零重叠阀。开度分数偏移均为零。当阀处于正常位置时，阀芯的台肩完全覆盖所有四个节流孔。
- 图 **II**：负重叠阀。**P**–**A** 和 **B**–**T** 开度分数偏移为正，**P**–**B** 和 **A**–**T** 开度分数偏移为负。当阀处于正常位置时，阀芯的台肩部分覆盖四个节流孔。
- 图 **III**：正重叠阀。**P**–**A** 和 **B**–**T** 开度分数偏移为负，**P**–**B** 和 **A**–**T** 开度分数偏移为正。控制元件不仅在正常位置完全覆盖所有节流孔，而且在其周围的一小段阀芯位移范围内也是如此。

### 阀参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。[2][3]
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。[2][3]
- `Sonic conductance` — 稳态下阻力元件的声导决定模块参数化。声导衡量气体在*阻塞*条件下流动的难易程度，阻塞是指流动速度达到当地声速的条件。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。[1]
- `Orifice area` — 流动限制的尺寸决定模块参数化。[4]

### 开度特性

流量特性将阀的开度与产生该开度的输入关联起来，该输入通常是阀芯行程。该模块根据 **Valve parameterization** 参数的设置，将开度表示为声速导、流量系数或节流面积。控制输入是节流口开度分数，它是端口 **S** 处指定的阀芯位移的函数。

流量特性通常在稳态下给出，入口处于恒定且精心控制的压力下。流量特性仅取决于阀本身，并且可以是线性的或非线性的。要捕获流量特性，请使用 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量是节流口开度分数的线性函数。当开度分数从 `0` 上升到 `1` 时，流量能力的度量从指定的最小值按比例变化到指定的最大值。
- `Tabulated` — 流量能力的度量是节流口开度分数的一般函数，可以是线性的或非线性的。该函数以表格形式指定，其中自变量由 **Opening fraction vector** 指定。

### 数值平滑

当 **Opening characteristic** 参数为 `Linear`，且 **Smoothing factor** 参数非零时，该模块会对节流口开度分数应用数值平滑。启用平滑有助于在仿真中保持数值鲁棒性。

有关更多信息，请参阅数值平滑。

### 泄漏流量

泄漏流量可确保流体网络的任何部分都不会被隔离。被隔离的流体段会降低模型的数值鲁棒性，减慢仿真速度，并在某些情况下导致仿真失败。**Leakage flow fraction** 参数将该模块中的泄漏流动面积表示为大于零的小数值。

### 复合结构

该模块是一个复合组件，由四个 Orifice (G) 模块实例组成，并连接到端口 **P**、**A**、**B**、**T** 和 **S**。有关阀参数化和模块计算的更多详细信息，请参阅 Orifice (G) 模块。

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于空气以外的气体，您可能需要按比重的平方根对声速导进行缩放。
- `Orifice area based on geometry` 参数化的方程对于远离理想气体的气体来说精度较低。
- 该模块不建模超声速流动。
