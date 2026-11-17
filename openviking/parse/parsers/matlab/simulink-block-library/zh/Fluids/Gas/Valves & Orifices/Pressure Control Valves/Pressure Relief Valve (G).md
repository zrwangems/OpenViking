---
type: simulink-block
title: 'Pressure Relief Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalveg'
documentation_source_path: 'ref/pressurereliefvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Relief Valve (G)

## 端口
```yaml
ports:
- name: A
  summary: 阀入口气体
  direction: conserving
- name: B
  summary: 阀入口气体
  direction: conserving
```

### 守恒端口

### **A** — 阀入口气体

与流必须进入阀的开口相关联的气体守恒端口。

### **B** — 阀入口气体

与流必须离开阀的开口相关联的气体守恒端口。
## 参数
```yaml
parameters:
- name: Opening pressure specification
  summary: 选择用作阀控制信号的压力测量值 Pressure difference of port A relative to port B（默认）| Gauge pressure at port A
  group: ''
- name: Valve parameterization
  summary: 用于指定阀流量特性的参数化方法 Cv flow coefficient（默认）| Kv flow coefficient | Sonic conductance | Orifice area
  group: ''
- name: Opening characteristic
  summary: 计算阀开启特性的方法 Linear（默认）| Tabulated
  group: ''
- name: Set pressure differential
  summary: 阀操作的阈值压差 0 MPa（默认）| 正标量
  group: ''
- name: Pressure regulation range
  summary: 开启面积可变的压力范围宽度 0.1 MPa（默认）| 正标量
  group: ''
- name: Set pressure (gauge)
  summary: 打开阀所需的入口表压 0.1 MPa（默认）| 以压力单位表示的正标量
  group: ''
- name: Opening pressure differential vector
  summary: '用于指定阀开启数据的控制压力向量 0.2 : 0.2 : 1.2 MPa（默认）| 向量'
  group: ''
- name: Opening pressure (gauge) vector
  summary: '用于指定阀开启数据的控制压力向量 0.2 : 0.2 : 1.2 MPa（默认）| 向量'
  group: ''
- name: Maximum Cv flow coefficient
  summary: 对应于最大开启状态的 Cv 系数 4（默认）| 正标量
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: 压差比系数 0.7（默认）| 正标量
  group: ''
- name: Leakage flow fraction
  summary: 流率比 1e-6（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Cv flow coefficient vector
  summary: 对应于开启分数向量中各值的 Cv 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 正数向量
  group: ''
- name: Maximum Kv flow coefficient
  summary: 对应于最大开启状态的 Kv 系数 3.6（默认）| 正标量
  group: ''
- name: Kv flow coefficient vector
  summary: 对应于开启分数向量中各值的 Kv 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 正数向量
  group: ''
- name: Maximum sonic conductance
  summary: 对应于最大开启状态的声速导纳 12 l/(bar*s)（默认）| 正标量
  group: ''
- name: Critical pressure ratio
  summary: 流动首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: ''
- name: Subsonic index
  summary: 用于表征亚声速流态中质量流量的指数 0.5（默认）| 正标量
  group: ''
- name: ISO reference temperature
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: ''
- name: ISO reference density
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: ''
- name: Sonic conductance vector
  summary: 对应于开启分数向量中各值的声速导纳 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 正值向量
  group: ''
- name: Critical pressure ratio vector
  summary: 对应于开启分数向量中各值的临界压力比 0.3 * ones(1,6)（默认）| 正数向量
  group: ''
- name: Maximum orifice area
  summary: 对应于最大开启状态的流动面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Orifice area vector
  summary: 孔口开启面积值向量 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认）| 向量
  group: ''
- name: Laminar flow pressure ratio
  summary: 流动在层流和湍流状态之间过渡时的压力比 0.999（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 气体端口处的流动面积 0.01 m^2（默认）| 正标量
  group: ''
```

### **Opening pressure specification** — 选择用作阀控制信号的压力测量值 `Pressure difference of port A relative to port B`（默认）| `Gauge pressure at port A`

选择用作阀控制信号的压力测量值。该模块使用此设置来确定阀应何时开始打开。在默认设置 `Pressure difference of port A relative to port B` 下，阀的开启压力表示为从入口到出口的压降。在替代设置 `Gauge pressure at port A` 下，它表示为入口表压。

### **Valve parameterization** — 用于指定阀流量特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流率的方法。

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻力元件的声速导纳决定模块参数化。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### **Opening characteristic** — 计算阀开启特性的方法 `Linear`（默认）| `Tabulated`

模块用于计算阀开启面积的方法。线性设置将开启面积视为孔口开启分数的线性函数。表格设置允许使用以表格形式指定的通用非线性关系。

### **Set pressure differential** — 阀操作的阈值压差 `0 MPa`（默认）| 正标量

打开阀所需的从入口到出口的压降。该值标志着压力调节范围的起点，在此范围内阀逐渐打开以试图抑制压力上升。阀的开启面积取决于实际压降与该处指定值之间的差值。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure difference at port A relative to port B`，并将 **Opening characteristic** 设置为 `Linear`。

### **Pressure regulation range** — 开启面积可变的压力范围宽度 `0.1 MPa`（默认）| 正标量

阀的工作范围。阀在设定压力值处开始打开，并在 *pmax* 处完全打开，*pmax* 是压力调节范围的终点，其中
*pmax = pset + prange*。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Set pressure (gauge)** — 打开阀所需的入口表压 `0.1 MPa`（默认）| 以压力单位表示的正标量

打开阀所需的入口表压。此参数标志着压力调节范围的起点，在此范围内阀逐渐打开以试图抑制压力上升。阀的开启面积取决于实际入口压力与该处指定值之间的差值。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并将 **Opening characteristic** 设置为 `Linear`。

### **Opening pressure differential vector** — 用于指定阀开启数据的控制压力向量 `0.2 : 0.2 : 1.2 MPa`（默认）| 向量

用于指定所选阀开启度量（声速导纳、流量系数或开启面积）的控制压力向量。此向量的大小必须与包含阀开启数据的向量相同。向量元素必须为正，并从左到右单调递增。这些压力值为从入口到出口的压降。

此参数的第一个元素是阀的压力设定值，此时阀开始打开。最后一个元素是最大压力，此时阀完全打开。两者之差即为阀的压力调节范围。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure difference at port A relative to port B`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Opening pressure (gauge) vector** — 用于指定阀开启数据的控制压力向量 `0.2 : 0.2 : 1.2 MPa`（默认）| 向量

用于指定所选阀开启度量（声速导纳、流量系数或开启面积）的控制压力向量。此向量的大小必须与包含阀开启数据的向量相同。向量元素必须为正，并从左到右单调递增。这些压力为入口处的表压。

此参数的第一个元素是阀的压力设定值，此时阀开始打开。最后一个元素是最大压力，此时阀完全打开。两者之差即为阀的压力调节范围。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应于最大开启状态的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大时的 *Cv* 流量系数值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，此时首次发生阻塞流。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Leakage flow fraction** — 流率比 `1e-6`（默认）| 正标量

孔口关闭时与打开时的流率之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应于开启分数向量中各值的 Cv 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 正数向量

*Cv* 流量系数向量。每个系数对应于 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。流量系数必须从左到右单调递增，较大的开启分数表示较大的流量系数。向量的大小必须与 **Opening fraction vector** 相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应于最大开启状态的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大时的 *Kv* 流量系数值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应于开启分数向量中各值的 Kv 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 正数向量

*Kv* 流量系数向量。每个系数对应于 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻力元件的难易程度。流量系数必须从左到右单调递增，较大的开启分数表示较大的流量系数。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum sonic conductance** — 对应于最大开启状态的声速导纳 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大时的声速导纳值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态中质量流率。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 对应于开启分数向量中各值的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声速导纳向量。每个导纳对应于 **Opening fraction vector** 参数中的一个值。声速导纳必须从左到右单调递增，较大的开启分数表示较大的声速导纳。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 对应于开启分数向量中各值的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应于 **Opening fraction vector** 参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum orifice area** — 对应于最大开启状态的流动面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积达到最大时孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于修正理论流量中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Orifice area vector** — 孔口开启面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 向量

孔口开口的横截面积向量。此向量中的值与 **Opening fraction vector** 参数中的元素一一对应。此向量的第一个元素是孔口泄漏面积，最后一个元素是最大孔口面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间过渡时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间过渡时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流动面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相等。此参数的值应与阻力元件所连接组件的入口面积相匹配。
## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在之前的版本中，气体库中的模块使用转换因子来根据声速流导实现不同的孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked
  flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数取代了
  **Cv coefficient (USCS) at leakage flow**、
  **Kv coefficient (SI) at leakage flow**、
  **Sonic conductance at leakage flow** 和
  **Restriction area at leakage flow**
  参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference
  density** 参数已分别重命名为 **ISO
  reference temperature** 和 **ISO reference
  density**。
- **Cv coefficient (USCS) at maximum flow** 和
  **Kv coefficient (USCS) at maximum flow**
  参数已分别重命名为 **Maximum Cv
  coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic
  conductance**。
- **Pressure control specification** 参数已重命名为 **Opening pressure specification**。此参数的选项已重命名为 `Pressure
  difference of port A relative to port B` 和
  `Gauge pressure at port A`。
- **Control pressure vector** 参数已重命名为 **Opening pressure differential vector** 或
  **Opening pressure (gauge) vector**，具体取决于 **Opening pressure
  specification** 的选择。

## 描述

气体网络中的泄压阀

Pressure Relief Valve (G) 模块表示一个孔口，它随入口压力打开以防止压力达到极端水平。在正常压力下，阀门关闭，仅释放泄漏流量。当压力超过指定的设定压力时，阀门开始打开，允许气体从高压区域排出。打开面积随入口压力增加而增大，直至达到最大值，此时阀门完全打开，压力不再受抑制地上升。

阀门响应相对于出口压力的入口压力，或相对于环境的入口压力。所选择的压力测量值是阀门的*控制压力*。**Control pressure
specification** 参数决定模块在仿真期间使用哪种测量值。

打开面积与压降之间的关系取决于阀门的参数化。该关系可以采用线性解析表达式或表格函数的形式。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门特有的临界值时，发生阻塞。该模块不捕获超声速流动。

### 阀门开度分数

入口压力是阀门控制信号。入口压力超过阀门设定压力越多，打开面积就越大。控制压力超过设定压力的量决定阀门打开的程度。当 **Opening characteristic** 参数为
`Linear` 时，模块计算阀门开度分数以缩放流量特性参数。归一化控制压力为

p^=PCtl-PSetΔP，

其中：

- *PCtl* 是控制压力。

  当 **Opening pressure specification** 为
  `Pressure difference of port A relative to port
  B` 时，

  PCtl=PA−PB，

  其中 *PA* 是端口 **A** 的绝对压力，*PB* 是端口 **B** 的绝对压力。

  当 **Opening pressure specification** 为
  `Gauge pressure at port A` 时，

  PCtl=PA−PAtm，

  其中 *PAtm* 是模型 Gas Properties
  (G) 模块中指定的大气压。
- *PSet* 是设定压力。

  当 **Opening pressure specification** 为
  `Pressure difference of port A relative to port
  B` 时，*PSet* 是 **Set pressure differential**
  参数的值。

  当 **Opening pressure specification** 为
  `Gauge pressure at port A` 时，*PSet* 是
  **Set pressure (gauge)** 参数的值。
- *ΔP* 是 **Pressure
  regulation range** 参数的值。

阀门开度分数 *L* 为

L=(1-Lleak)P^+Lleak，

其中 *Lleak* 是 **Leakage flow fraction** 参数的值。

**数值平滑**

当 **Opening characteristic** 参数为
`Linear` 且 **Smoothing
factor** 参数非零时，模块对归一化控制压力 p^ 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅数值平滑。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数
  *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速流导决定模块参数化。声速流导衡量气体在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 打开特性

流量特性将阀门开度与产生该开度的输入相关联。开度表示为声速流导、流量系数或限制面积，由 **Valve parameterization** 参数决定。

流量特性通常在稳态下给出，入口处于恒定且精心控制的压力下。流量特性仅取决于阀门，可以是线性的或非线性的。要捕获流量特性，请使用 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量是阀门开度分数的线性函数。当开度分数从 `0` 上升到 `1` 时，流量能力的度量从指定的最小值缩放到指定的最大值。
- `Tabulated` — 流量能力的度量是孔口开度分数的一般函数，可以是线性的或非线性的。该函数以表格形式指定，自变量由 **Opening pressure
  differential vector** 或 **Opening pressure
  (gauge) vector** 指定。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。当您将 **Orifice parametrization** 设置为 `Cv
flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin，

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked
  flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口发生阻塞，模块切换到方程

m˙=23CvN6FγxTpinρin。

当您将 **Orifice parametrization** 设置为 `Kv flow
coefficient parameterization` 时，模块使用相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Orifice parametrization** 参数为 `Kv
flow coefficient parameterization` 或 `Cv flow
coefficient parameterization` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Orifice parametrization** 设置为
`Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是声速流导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic
  index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞，模块切换到方程

m˙=CρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于空气以外的气体，可能需要按比重的平方根缩放声速流导。

有关当 **Orifice
parametrization** 参数为 `Sonic conductance
parameterization` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Orifice parametrization** 设置为
`Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ]，

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional
  area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口发生阻塞，模块切换到方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2。

有关当 **Orifice
parametrization** 参数为 `Orifice area
parameterization` 时的质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

模块假设阀门内流体的体积和质量非常小，并忽略这些值。因此，不会有流体在阀门中积聚。根据质量守恒原理，通过一个端口进入阀门的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0，

其中 m˙ 定义为通过 **A** 或 **B** 下标所指示端口进入阀门的质量流量。

### 能量平衡

模块的阻力元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口的过程中，没有对流体做功，也没有流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 假设和限制

- `Orifice area` 参数化的方程对于远离理想气体的气体不太准确。
- 该模块不建模超声速流动。
