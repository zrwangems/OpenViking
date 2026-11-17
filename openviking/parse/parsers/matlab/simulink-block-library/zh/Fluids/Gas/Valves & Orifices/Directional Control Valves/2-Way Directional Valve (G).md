---
type: simulink-block
title: '2-Way Directional Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalveg'
documentation_source_path: 'ref/2waydirectionalvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-Way Directional Valve (G)

## 端口
```yaml
ports:
- name: S
  summary: 阀门控制信号，unitless 物理信号
  direction: input
- name: A
  summary: 阀门开口气体
  direction: input
- name: B
  summary: 阀门开口气体
  direction: input
```

### 输入

### **S** — 阀门控制信号，`unitless` 物理信号

控制构件相对于其正常未致动位置的瞬时位移，指定为物理信号。该模块将位移相对于完全打开节流孔所需控制构件的最大位置进行归一化。该信号是无量纲的，其瞬时值通常在 `0` 到 `1` 之间。

### 守恒

### **A** — 阀门开口气体

与流体进入或离开阀门的开口相关联的气体守恒端口。

### **B** — 阀门开口气体

与流体进入或离开阀门的开口相关联的气体守恒端口。
## 参数
```yaml
parameters:
- name: Valve parameterization
  summary: 用于指定节流孔流动特性的参数化方法 Cv flow coefficient（默认）| Kv flow coefficient | Sonic conductance | Orifice area
  group: ''
- name: Opening characteristic
  summary: 计算阀门开启特性的方法 Linear（默认）| Tabulated
  group: ''
- name: Opening fraction vector
  summary: '用于指定表格化参数数据的控制信号值 0 : 0.2 : 1（默认）| 正数向量'
  group: ''
- name: Maximum Cv flow coefficient
  summary: 对应于最大开启组件的 Cv 系数 4（默认）| 正标量
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: 压差比系数 0.7（默认）| 正标量
  group: ''
- name: Leakage flow fraction
  summary: 流量比 1e-6（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的正标量
  group: ''
- name: Cv flow coefficient vector
  summary: 与开度分数向量中各值对应的 Cv 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 正数向量
  group: ''
- name: Maximum Kv flow coefficient
  summary: 对应最大开启组件的 Kv 系数 3.6（默认）| 正标量
  group: ''
- name: Kv flow coefficient vector
  summary: 与开度分数向量中各值对应的 Kv 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 正数向量
  group: ''
- name: Maximum sonic conductance
  summary: 对应最大开启组件的声速流导 12 l/(bar*s)（默认）| 正标量
  group: ''
- name: Critical pressure ratio
  summary: 流量首次发生阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: ''
- name: Subsonic index
  summary: 用于表征亚声速流态下质量流量的指数 0.5（默认）| 正标量
  group: ''
- name: ISO reference temperature
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: ''
- name: ISO reference density
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: ''
- name: Sonic conductance vector
  summary: 与开口分数向量中的值对应的声速导纳 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 正值向量
  group: ''
- name: Critical pressure ratio vector
  summary: 与开口分数向量中的值对应的临界压力比 0.3 * ones(1,6)（默认）| 正数向量
  group: ''
- name: Maximum orifice area
  summary: 最大开启状态组件对应的流通面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 范围在 [0,1] 内的正标量
  group: ''
- name: Orifice area vector
  summary: 节流孔开口面积值向量 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认）| 向量
  group: ''
- name: Valve opening fraction offset
  summary: 零位移信号时阀门的开口分数 0（默认）| 无量纲标量
  group: ''
- name: Laminar flow pressure ratio
  summary: 流动在层流和湍流状态之间转换时的压力比 0.999（默认值）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 气体端口处的流通面积 0.01 m^2（默认值）| 正标量
  group: ''
```

### **Valve parameterization** — 用于指定节流孔流动特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速导纳决定模块参数化。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### **Opening characteristic** — 计算阀门开启特性的方法 `Linear`（默认）| `Tabulated`

模块用于计算阀门开启面积的方法。`Linear` 设置将开启面积视为节流孔开启分数的线性函数。`Tabulated` 设置允许使用以表格形式指定的通用非线性关系。

### **Opening fraction vector** — 用于指定表格化参数数据的控制信号值 `0 : 0.2 : 1`（默认）| 正数向量

用于指定所选流量能力度量的控制信号值向量：**Sonic conductance vector**、**Cv coefficient vector**、**Kv coefficient vector** 或 **Orifice area vector**。控制信号在 `0` 到 `1` 之间，每个值对应阻性元件的开启分数。值越大，开启越大，流动越容易。

开启分数必须在向量中从左到右单调递增。该向量的大小必须与 **Sonic conductance vector**、**Cv coefficient vector**、**Kv coefficient vector** 或 **Orifice area vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应于最大开启组件的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大时的 *Cv* 流量系数值。此参数衡量当由压差驱动时气体通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，此时首次发生阻塞流。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀门来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时的流量与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为
`Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当节流孔处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。
将此参数设置为小于 1 的非零值，以提高在这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为
`Linear`。

### **Cv flow coefficient vector** — 与开度分数向量中各值对应的 Cv 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 正数向量

*Cv* 流量系数向量。
每个系数对应 **Opening fraction
vector** 参数中的一个值。此参数衡量气体在压差驱动下通过阻力元件的难易程度。流量系数必须从左到右单调递增，较大的开度分数对应较大的流量系数。向量的大小必须与
**Opening fraction vector** 相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Cv flow coefficient`，并将
**Opening characteristic** 设置为
`Tabulated`。

### **Maximum Kv flow coefficient** — 对应最大开启组件的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的节流面积达到最大时的 *Kv* 流量系数值。此参数衡量气体在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Kv flow coefficient`，并将
**Opening characteristic** 设置为
`Linear`。

### **Kv flow coefficient vector** — 与开度分数向量中各值对应的 Kv 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 正数向量

*Kv* 流量系数向量。
每个系数对应 **Opening fraction
vector** 参数中的一个值。此参数衡量气体在压差驱动下通过阻力元件的难易程度。流量系数必须从左到右单调递增，较大的开度分数对应较大的流量系数。向量的大小必须与
**Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Kv flow coefficient`，并将
**Opening characteristic** 设置为
`Tabulated`。

### **Maximum sonic conductance** — 对应最大开启组件的声速流导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大时的声速流导值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`，并将 **Opening
characteristic** 设置为
`Linear`。

### **Critical pressure ratio** — 流量首次发生阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`，并将 **Opening
characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为
`Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 与开口分数向量中的值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声速导纳向量。每个导纳对应于 **Opening fraction vector** 参数中的一个值。声速导纳必须从左到右单调递增，较大的开口分数表示较大的声速导纳。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 与开口分数向量中的值对应的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次发生阻塞时的临界压力比向量，每个临界压力比对应于 **Opening fraction vector** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum orifice area** — 最大开启状态组件对应的流通面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积达到最大时，节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围在 [0,1] 内的正标量

用于修正理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Orifice area vector** — 节流孔开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 向量

节流孔开口的横截面积向量。此向量中的值与 **Opening fraction vector** 参数中的元素一一对应。此向量的第一个元素是节流孔泄漏面积，最后一个元素是最大节流孔面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Valve opening fraction offset** — 零位移信号时阀门的开口分数 `0`（默认）| 无量纲标量

当输入信号 **S** 的值为零时阀门的开口分数。此时阀门处于正常位置。开口分数衡量阀芯台肩与阀门节流孔之间的距离，以最大允许值进行归一化。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换时的压力比 `0.999`（默认值）| 正标量

流动在层流和湍流状态之间转换时的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流通面积 `0.01 m^2`（默认值）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相同。该参数值应与阻力元件所连接组件的入口面积相匹配。
## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b：使用改进的流量计算对气体系统建模

在之前的版本中，气体库中的模块使用转换因子来实现基于声速导的不同孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化方式。

新的参数化方式还包含新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。该参数替换了 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。

## 描述

气体网络中带两个端口的受控阀

2-Way Directional Valve (G) 模块表示一个具有两个端口 **A** 和 **B**、以及一条流动路径 **A**–**B** 的阀。该路径通过一个宽度可变的孔口。在端口 **S** 处指定的输入信号控制阀芯的位置。当阀芯覆盖孔口开口时，阀关闭。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀的喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀的临界值时发生阻塞。该模块不捕获超声速流动。

### Valve Positions

阀是连续可变的，它在一个正常位置和一个工作位置之间平滑切换。

当阀芯在端口 **S** 处的瞬时位移为零时，阀恢复到正常位置，此时它不再工作。除非阀芯的台肩相对于阀口存在偏移，否则阀完全关闭。工作位置是当阀芯从正常位置沿正方向达到最大位移时阀所移动到的位置。此时阀口完全打开。

使阀处于工作位置的阀芯位移取决于阀芯上台肩的偏移。**Valve opening fraction offset** 参数指定端口阀芯位移的模块常量。

**Orifice Opening Fractions**

在阀位置之间，**A**–**B** 阀口的开度取决于阀芯台肩相对于边缘的位置。该距离即为阀口开度，模块对该距离进行归一化，使其值为阀口完全打开时最大距离的分数。归一化后的变量即为阀口开度分数。

阀口开度分数的范围可以从正常位置的 `0` 到工作位置的 `1`。模块根据阀芯位移和开度分数偏移计算开度分数。位移和偏移是最大台肩-阀口距离的无量纲分数。阀口开度分数为：

hAB=HAB+x，

其中：

- *h* 是 **A**–**B** 阀口的开度分数。如果计算结果超出 `0 - 1` 范围，模块将使用最接近的限值。
- *H* 是 **Valve opening fraction offset** 参数的值。为允许不常见的阀配置，模块对其值不施加限制，尽管通常这些值会落在 `-1` 和 `+1` 之间。
- *x* 是阀芯的归一化瞬时位移，由端口 **S** 处的物理信号指定。为补偿极端的开度分数偏移，对该信号值没有限制。该值通常在 `0` 和 `+1` 之间。

**Opening Fraction Offsets**

默认情况下，当控制位移为零时，阀完全关闭。在此状态下，阀为零重叠。

您可以偏移阀芯的台肩，以模拟负重叠或正重叠阀。负重叠阀在正常位置部分打开。正重叠阀在略超过正常位置时完全关闭。该图显示了阀口开度分数如何随瞬时阀芯位移变化：

- 图 **I**：零重叠阀。开度分数偏移为零。当阀处于正常位置时，阀芯的台肩完全覆盖阀口。
- 图 **II**：负重叠阀。开度分数偏移为正。当阀处于正常位置时，阀芯的台肩部分覆盖阀口。
- 图 **III**：正重叠阀。开度分数偏移为负。阀芯的台肩不仅在正常位置完全覆盖阀口，而且在其周围的一小段阀芯位移范围内也完全覆盖阀口。

**Control Position in Zero-Lapped, Underlapped, and Overlapped valves**

**Leakage Flow**

泄漏流量确保流体网络的任何部分都不会被隔离。被隔离的流体段会降低模型的数值鲁棒性，减慢仿真速度，并在某些情况下导致仿真失败。**Leakage flow fraction** 参数将模块中的泄漏流通面积表示为大于零的小数。

**Composite Structure**

该模块是一个复合组件，由连接在端口 **A**、**B** 和 **S** 之间的单个 Orifice (G) 模块组成。有关阀参数化和模块计算的更多详细信息，请参阅 Orifice (G) 模块。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。[2][3]
- `Kv flow coefficient` — 流量系数
  *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。[2][3]
- `Sonic conductance` — 阻性元件在稳态下的声速导决定模块参数化。声速导衡量气体在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，就会发生阻塞。[1]
- `Orifice area` — 流动限制的尺寸决定模块参数化。[4]

### 开度特性

流量特性将阀门开度与产生该开度的输入关联起来，该输入通常是阀芯行程。根据 **Valve parameterization** 参数的设置，模块将开度表示为声速导、流量系数或限制面积。控制输入是节流口开度分数，它是端口 **S** 处指定阀芯位移的函数。

流量特性通常在稳态下给出，入口处于恒定且精心控制的压力下。流量特性仅取决于阀门，可以是线性的或非线性的。要捕获流量特性，请使用 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量是节流口开度分数的线性函数。当开度分数从 `0` 上升到 `1` 时，流量能力的度量从指定的最小值按比例变化到指定的最大值。
- `Tabulated` — 流量能力的度量是节流口开度分数的一般函数，可以是线性的或非线性的。该函数以表格形式指定，其中自变量由 **Opening fraction vector** 指定

### 数值平滑

当 **Opening characteristic** 参数为 `Linear`，且 **Smoothing factor** 参数非零时，模块会对节流口开度分数应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅数值平滑。

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于空气以外的气体，您可能需要按比重的平方根缩放声速导。
- `Orifice area based on geometry` 参数化的方程对于远离理想气体的气体不太准确。
- 此模块不建模超声速流动。
