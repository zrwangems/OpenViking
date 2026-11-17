---
type: simulink-block
title: 'Pilot-Operated Check Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'pilotoperatedcheckvalveil'
documentation_source_path: 'ref/pilotoperatedcheckvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pilot-Operated Check Valve (IL)

## 端口
```yaml
ports:
- name: A
  summary: 等温液体液体端口
  direction: conserving
- name: B
  summary: 等温液体液体端口
  direction: conserving
- name: X
  summary: 等温液体压力端口
  direction: conserving
```

### 守恒端口

### **A** — 等温液体液体端口

与阀入口关联的等温液体守恒端口。当控制压力超过开启压力时，液体可以从该端口流出。

### **B** — 等温液体液体端口

与阀出口关联的等温液体守恒端口。当控制压力超过开启压力时，液体可以从该端口进入阀。

### **X** — 等温液体压力端口

与压力端口关联的等温液体守恒端口，该压力端口对通过阀的流量控制有贡献。该端口没有质量流量。
## 参数
```yaml
parameters:
- name: Pilot pressure direction
  summary: 先导压力是辅助阀打开还是辅助阀关闭 Pilot-to-open（默认）| Pilot-to-close
  group: ''
- name: Spool configuration
  summary: 阀几何结构 Rigidly connected pilot spool and poppet（默认）| Disconnected pilot spool and poppet
  group: ''
- name: Opening pilot pressure specification
  summary: 用于阀控制的参考压差 Pressure difference of port X relative to port A（默认）| Gauge pressure at port X
  group: ''
- name: Opening parameterization
  summary: 计算阀开度的方法 Linear - Area vs. pressure（默认）| Tabulated data - Area vs. pressure | Tabulated data - Volumetric flow
    rate vs. pressure
  group: ''
- name: Cracking pressure differential
  summary: 压力阈值 0.01 MPa（默认）| 正标量
  group: ''
- name: Maximum opening pressure differential
  summary: 阀打开时的最大压差 0.02 MPa（默认）| 正标量
  group: ''
- name: Pilot ratio
  summary: 先导端口面积比 1（默认）| 范围 (0,1] 内的正标量
  group: ''
- name: Maximum opening area
  summary: 最大阀面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Control pressure vector
  summary: '表格参数化的控制压力值 [0.01 : 0.01 : 0.1] MPa（默认）| 1×*n* 向量'
  group: ''
- name: Opening area vector
  summary: 表格参数化的阀开口面积 [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2（默认）| 1×*n* 向量
  group: ''
- name: Reference pressure differential vector
  summary: '表格体积流量参数化的压差向量 [0.01 : 0.01 : 0.1] MPa（默认）| 1×*n* 向量'
  group: ''
- name: Reference volumetric flow rate vector
  summary: 表格数据参数化的体积流量向量 [.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s（默认）| 1×*n* 向量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的面积 inf m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Pressure recovery
  summary: 是否考虑面积扩大时的压力增加 off（默认）| on
  group: ''
- name: Opening dynamics
  summary: 是否引入阀打开导致的流量滞后 off（默认）| on
  group: ''
- name: Opening time constant
  summary: 阀打开时间常数 0.1 s（默认）| 正标量
  group: ''
```

### **Pilot pressure direction** — 先导压力是辅助阀打开还是辅助阀关闭 `Pilot-to-open`（默认）| `Pilot-to-close`

先导压力是辅助阀打开还是辅助阀关闭。如果将参数设置为 `Pilot-to-open`，则先导压力辅助阀打开。如果将参数设置为 `Pilot-to-close`，则先导压力辅助阀关闭。

### **Spool configuration** — 阀几何结构 `Rigidly connected pilot spool and poppet`（默认）| `Disconnected pilot spool and poppet`

阀几何结构。使用 `Rigidly connected pilot spool and poppet` 来建模开启机构与阀芯连接的阀，或使用 `Disconnected pilot spool and poppet` 来建模与阀芯对齐但可自由远离阀芯移动的开启机构。该参数决定先导压力计算。

#### 依赖关系

要启用此参数，请将 **Pilot pressure direction** 设置为 `Pilot-to-open`。

### **Opening pilot pressure specification** — 用于阀控制的参考压差 `Pressure difference of port X relative to port A`（默认）| `Gauge pressure at port X`

用于阀控制的参考先导压差。该模块将先导压差与端口 **A** 和 **B** 之间的压差相加，并与阀阈值 **Cracking pressure differential** 进行比较。

#### 依赖关系

要启用此参数，请将 **Pilot pressure direction** 设置为 `Pilot-to-open`。

### **Opening parameterization** — 计算阀开度的方法 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

计算阀开度的方法：

- `Linear - Area vs. pressure` — 阀开口面积与阀压力呈线性对应关系。
- `Tabulated data - Area vs. pressure` — 该模块根据面积值相对于压差的表来确定阀质量流量。
- `Tabulated data - Volumetric flow rate vs. pressure` — 该模块根据体积流量值相对于压差的表来确定阀质量流量。

### **Cracking pressure differential** — 压力阈值 `0.01 MPa`（默认）| 正标量

设置阀操作的压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening pressure differential** — 阀打开时的最大压差 `0.02 MPa`（默认）| 正标量

阀打开时的最大压差。该值为仿真压力提供上限，以使结果保持物理意义。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pilot ratio** — 先导端口面积比 `1`（默认）| 范围 (0,1] 内的正标量

端口 **X** 面积与端口 **A** 面积之比。

### **Maximum opening area** — 最大阀面积 `1e-4 m^2`（默认）| 正标量

最大阀面积。该模块使用此值来确定运行期间的归一化阀压力和阀开口面积。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。该参数通过保持流量连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Control pressure vector** — 表格参数化的控制压力值 `[0.01 : 0.01 : 0.1] MPa`（默认）| 1×*n* 向量

用于阀开口面积表格参数化的压差值向量。该向量的第一个元素是开启压差。

向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素按升序排列且必须大于 0。该模块在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Opening area vector** — 表格参数化的阀开口面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀开口面积表格面积参数化的阀开口面积向量。该向量的第一个元素是阀完全关闭时的泄漏面积，最后一个元素是最大阀面积。

向量元素必须与 **Control pressure vector** 参数中的元素一一对应。元素按升序排列且必须大于 0。该模块在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Reference pressure differential vector** — 表格体积流量参数化的压差向量 `[0.01 : 0.01 : 0.1] MPa`（默认）| 1×*n* 向量

用于表格体积流量参数化的压差值向量。这些值是先导压力为 `0` 时的自由流动数据。向量元素必须与 **Reference volumetric flow rate vector** 参数中的元素一一对应。元素按升序排列且必须大于 0。该模块在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference volumetric flow rate vector** — 表格数据参数化的体积流量向量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s`（默认）| 1×*n* 向量

用于表格参数化的体积流量值向量。这些值是先导压力为 `0` 时的自由流动数据。该向量必须与 **Reference pressure differential vector** 参数具有相同数量的元素。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的面积，该模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入逐渐变化的层。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening dynamics** — 是否引入阀打开导致的流量滞后 `off`（默认）| `on`

是否考虑打开阀对流体系统造成的瞬态效应。选择 **Opening dynamics** 通过在压力响应中引入一阶滞后来近似开启条件。

### **Opening time constant** — 阀打开时间常数 `0.1 s`（默认）| 正标量

当阀从一个位置打开或关闭到另一个位置时，流体达到稳态条件所需时间的常数。该参数影响建模的开启动态。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2025a：使用表格数据参数化模块

使用面积与压力或体积流量与压力的表格数据参数化模块。将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 以保留之前的模块功能

### R2025a：建模先导关闭单向阀

将 **Pilot pressure direction** 参数设置为 `Pilot-to-close` 以建模先导压力辅助阀关闭的阀。将 **Pilot pressure direction** 设置为 `Pilot-to-open` 以保留之前的模块功能。

## 描述

等温液体系统中带先导压力控制的单向阀

Pilot-Operated Check Valve (IL) 模块建模一种基于先导管压力允许可变方向流动的流量控制阀。自由流动方向为从端口 **A** 到端口 **B**，当控制压力升至开启压力以上时阀打开。当控制压力超过 **Cracking pressure differential** 参数的值或 **Control pressure vector** 或 **Reference pressure differential vector** 参数第一个元素的值时，阀芯移动以允许任一方向的流动。端口 **X** 处或端口 **X** 与端口 **A** 和 **B** 之间没有质量流量。

先导操作单向阀示意图

当 **Pilot pressure direction** 参数为 `Pilot-to-open` 时，控制压力 *pcontrol* 为

pcontrol=ppilotkp+(pA−pB),

其中：

- *ppilot* 是控制先导压差。

  - 当 **Opening pilot pressure specification** 参数为 `Pressure difference of port X relative to port A` 时，*ppilot* 是端口 **X** 和端口 **A** 之间的压差。
  - 当 **Opening pilot pressure specification** 为 `Gauge pressure at port X` 时，*ppilot* 是端口 **X** 和大气压力之间的压差。
- *kp* 是 **Pilot ratio** 参数的值，即端口 **X** 面积与端口 **A** 面积之比，kp=AXAA。
- *pA* – *pB* 是阀上的压差。

当 **Pilot pressure direction** 参数为 `Pilot-to-close` 时，控制压力为

pcontrol=−ppilotkp+(pA−pB),

其中 *ppilot = pX - pB*。

### 阀芯配置

当 **Pilot pressure direction** 参数为 `Pilot-to-open` 时，您可以将阀芯和阀芯配置为刚性连接或断开连接。当 **Spool configuration** 参数为 `Disconnected pilot spool and poppet` 时，端口 **X** 处的相对压力必须为正。如果测得的先导压力为负，则控制压力仅基于端口 **A** 和 **B** 之间的压差。当 **Spool configuration** 参数为 `Rigidly connected pilot spool and poppet` 时，先导压力是根据开启规范测得的压差。

当 **Pilot pressure direction** 参数为 `Pilot-to-close` 时，先导阀芯和阀芯断开连接。端口 **X** 处的相对压力必须为正。如果测得的先导压力为负，则控制压力仅基于端口 **A** 和 **B** 之间的压差。

### 面积与压力开启参数化

当 **Opening parameterization** 为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，通过阀的质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *Avalve* 是瞬时阀开口面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差，*p*A – *p*B。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit（层流和湍流之间的流态转变点）相关的压差，

Δpcrit=πρ¯8Avalve(νRecritCd)2.

压力损失是由于面积减小导致的阀中压力降低。*PR*loss 为

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

压力恢复是由于面积增加导致的阀中正压力变化。如果您不想捕获此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。

**线性面积与压力**

当 **Opening parameterization** 为 `Linear - Area vs. pressure` 时，阀面积为

Avalve=p^(Amax−Aleak)+Aleak,

其中归一化压力 p^ 为

p^=pcontrol−pcrackingpmax−pcracking.

当阀处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，则该模块在 *pmax* 和 *pcracking* 之间平滑地饱和控制压力。有关更多信息，请参阅数值平滑。

**表格面积与压力**

当 **Opening parameterization** 为 `Tabulated data - Area vs. pressure` 时，该模块将阀面积插值为

Avalve=tablelookup(pcontrol,TLU,Avalve,TLU,pcontrol,interpolation=linear,extrapolation=nearest),

其中：

- *pcontrol,TLU* 是 **Control pressure vector** 参数
- *Avalve,TLU* 是 **Opening area vector** 参数。

阀面积在 **Opening area vector** 参数的第一个和最后一个元素之间饱和。**Control pressure vector** 参数的第一个元素对应于开启压差。

### 体积流量与压力参数化

当 **Opening parameterization** 为 `Tabulated data
- Volumetric flow rate vs. pressure` 时，质量流量为

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4,

并且

K=tablelookup(Δpref,TLU,V˙ref,TLUΔpref,TLU,pcontrol,interpolation=linear,extrapolation=nearest),

其中：

- *Δpref,TLU* 是
  **Reference pressure differential vector**
  参数。
- V˙ref,TLU 是
  **Reference volumetric flow rate vector**
  参数。

*K* 的值在 V˙ref,TLU(1)Δpref,TLU(1) 和 V˙ref,TLU(end)Δpref,TLU(end) 之间饱和，这意味着 **Reference
pressure differential vector** 和 **Reference volumetric flow
rate vector** 参数的第一个元素对应于泄漏质量流量，
最后一个元素对应于最大质量流量。

### 开启动态

如果选择 **Opening dynamics**，该模块会为受建模控制压力影响的流量
响应引入一个滞后。
*p*control 变为动态控制
压力 *p*dyn。动态控制压力的瞬时变化
取决于 **Opening time
constant** 参数 *τ*，

p˙dyn=pcontrol−pdynτ.

默认情况下，**Opening dynamics** 复选框
处于清除状态。

### 质量守恒

质量通过阀门守恒，

m˙A+m˙B=0.
