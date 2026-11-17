---
type: simulink-block
title: '2-Way Directional Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalvema'
documentation_source_path: 'ref/2waydirectionalvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-Way Directional Valve (MA)

## 端口
```yaml
ports:
- name: A
  summary: 湿空气入口或出口 湿空气
  direction: conserving
- name: B
  summary: 湿空气入口或出口 湿空气
  direction: conserving
- name: S
  summary: 阀芯位移，m 物理信号
  direction: input
```

### 守恒端口

### **A** — 湿空气入口或出口 湿空气

与阀入口或出口关联的湿空气守恒端口。

### **B** — 湿空气入口或出口 湿空气

与阀入口或出口关联的湿空气守恒端口。

### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移关联的物理信号，单位为 m。正值使阀打开。
## 参数
```yaml
parameters:
- name: Valve parameterization
  summary: 可变或恒定孔口参数化 Cv flow coefficient（默认）| Kv flow coefficient | Sonic conductance | Orifice area
  group: ''
- name: Opening characteristic
  summary: 将控制信号转换为流量能力度量的方法 Linear（默认）| Tabulated
  group: ''
- name: Spool position at maximum orifice area
  summary: 最大面积处的阀芯偏移 5e-3 m（默认）| 正标量
  group: ''
- name: Spool travel between closed and open orifice
  summary: 最大阀芯行程 5e-3 m（默认）| 正标量
  group: ''
- name: Spool travel vector
  summary: 阀芯位置向量 [0, .003, .006, .009, .012, .015] m（默认）| 1×*n* 向量
  group: ''
- name: Maximum Cv flow coefficient
  summary: 对应最大开启组件的 *Cv* 系数 4（默认）| 正标量
  group: ''
- name: Cv flow coefficient vector
  summary: 对应构件位置向量中值的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: 压差比系数 0.7（默认）| 正标量
  group: ''
- name: Maximum Kv flow coefficient
  summary: 对应最大开度元件的 *Kv* 系数 3.6（默认）| 正标量
  group: ''
- name: Kv flow coefficient vector
  summary: 对应构件位置向量中各值的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: ''
- name: Maximum sonic conductance
  summary: 对应最大开度元件的声速导流 12 l/(bar*s)（默认）| 正标量
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
  summary: 对应控制构件位置向量中各值的声速导流 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 正值向量
  group: ''
- name: Critical pressure ratio vector
  summary: 与控制构件位置向量 0.3 * ones(1,6)（默认）中的值对应的临界压力比 | 正数向量
  group: ''
- name: Maximum orifice area
  summary: 最大节流口开度面积 1e-4 m^2（默认） | 正标量
  group: ''
- name: Orifice area vector
  summary: 节流口开度面积值向量 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认） | 1×*n* 向量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认） | 正标量
  group: ''
- name: Leakage flow fraction
  summary: 流量比 1e-6（默认） | 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认） | 范围 [0,1] 内的正标量
  group: ''
- name: Laminar flow pressure ratio
  summary: 层流-湍流过渡压力比 0.999（默认） | 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 阀端口面积 0.01 m^2（默认） | 正标量
  group: ''
```

### **Valve parameterization** — 可变或恒定孔口参数化 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据孔口两端的压差计算质量流量，或根据质量流量计算压差的方法。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 处指定的控制信号转换为所选流量能力度量的方法。

### **Spool position at maximum orifice area** — 最大面积处的阀芯偏移 `5e-3` `m`（默认）| 正标量

阀完全打开时阀芯行程构件的位置。默认值表示零遮盖系统。正的非零值表示负遮盖（或部分关闭）系统。负的非零值表示正遮盖系统，其中阀在一定位移范围内保持打开。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `5e-3` `m`（默认）| 正标量

最大阀打开面积处的阀芯偏移。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Spool travel vector** — 阀芯位置向量 `[0, .003, .006, .009, .012, .015] m`（默认）| 1×*n* 向量

用于表格化孔口参数化的阀芯位置向量。向量元素与 **Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的值一一对应。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大开启组件的 *Cv* 系数 `4`（默认）| 正标量

孔口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应构件位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **Spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞流时的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应最大开度元件的 *Kv* 系数 `3.6`（默认）| 正标量

当节流口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **Spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum sonic conductance** — 对应最大开度元件的声速导流 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 处指定的控制信号为 `1` 且可用于流动的横截面积最大时的声速导流值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导流值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导流值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 对应控制构件位置向量中各值的声速导流 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声速导流向量。每个导流对应 **Spool travel vector** 参数中的一个值。向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 与控制构件位置向量 `0.3 * ones(1,6)`（默认）中的值对应的临界压力比 | 正数向量

临界压力比向量，在该压力比下流动首次发生阻塞，每个临界压力比对应于 **Spool travel vector** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。该向量的大小必须与 **Spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认） | 正标量

节流口完全打开时的面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Orifice area vector** — 节流口开度面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认） | 1×*n* 向量

用于节流口面积表格化参数化的节流口面积值向量。该向量中的值与 **Spool travel vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | 正标量

实际流量与理想流量之比。此参数用于考虑节流口方程中未涵盖的实际损失。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认） | 正标量

节流口关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，当节流口处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，以提高仿真在这些区域中的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认） | 正标量

流体在层流和湍流状态之间过渡时的节流口出口压力与节流口入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Cross-sectional area at ports A and B** — 阀端口面积 `0.01` m^2（默认） | 正标量

节流口端口 **A** 和 **B** 的面积。
## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的二通方向阀

2-Way Directional Valve (MA) 模块表示一个具有两个端口 **A** 和 **B** 以及一条流路 **A**–**B** 的阀。该流路通过一个宽度可变的节流口。在端口 **S** 处指定的输入信号控制阀芯的位置。当阀芯覆盖节流口开口时，阀关闭。有关该模块如何计算通过可变节流口的流量的更多详细信息，请参阅 Orifice (MA)。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量在特定压差驱动下湿空气流动的难易程度。
- `Kv flow coefficient` — 流量系数 *Kv*，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量在特定压差驱动下湿空气流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速导决定模块参数化。声速导衡量湿空气在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，就会发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 开度特性

流量特性将阀门的开度与产生该开度的输入（通常是阀芯行程）关联起来。根据 **Valve parameterization** 参数的设置，模块将开度表示为声速导、流量系数或限制面积。控制输入是节流口开度分数，它是端口 **S** 处指定的阀芯位移的函数。

流量特性通常在稳态下给出，入口处于恒定且经过精确控制的压力下。流量特性仅取决于阀门，可以是线性的或非线性的。要捕获流量特性，请使用 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量是节流口开度分数的线性函数。随着开度分数的增加，流量能力的度量从指定的最小值按比例变化到指定的最大值。
- `Tabulated` — 流量能力的度量是节流口开度分数的一般函数，可以是线性的或非线性的。该函数以表格形式指定，自变量由 **Opening fraction vector** 指定。

### 可视化节流口开度

要可视化阀芯偏移和位移，请右键单击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示声速导、*Kv* 流量系数、*Cv* 流量系数或节流口面积随阀芯位置的变化。

要在更改模块参数后更新数据，请在图窗中单击 **Reload Data**。

下图显示了使用默认值的阀门配置。

每个节流口的面积与阀芯位置的关系图。

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能需要按混合气体比重的平方根来缩放声速导。
- 该模块不建模超声速流动。
- 阀门与环境之间没有热交换。
