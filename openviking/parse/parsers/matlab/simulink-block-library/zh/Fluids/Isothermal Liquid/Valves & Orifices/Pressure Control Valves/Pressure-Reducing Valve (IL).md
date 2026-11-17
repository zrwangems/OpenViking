---
type: simulink-block
title: 'Pressure-Reducing Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalveil'
documentation_source_path: 'ref/pressurereducingvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Reducing Valve (IL)

## 端口
```yaml
ports:
- name: Ps
  summary: 设定压力信号，Pa 物理信号
  direction: input
- name: A
  summary: 液体端口 等温液体
  direction: input
- name: B
  summary: 液体端口 等温液体
  direction: input
```

### 输入

### **Ps** — 设定压力信号，Pa 物理信号

受控阀操作的压力阈值，单位为 Pa。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为
`Controlled`。
### 守恒

### **A** — 液体端口 等温液体

阀的入口或出口点。

### **B** — 液体端口 等温液体

阀的入口或出口点。
## 参数
```yaml
parameters:
- name: Set pressure control
  summary: 阀操作方法 Constant（默认）| Controlled
  group: 参数
- name: Opening parameterization
  summary: 开度参数化 Linear - Area vs. pressure（默认）| Tabulated data - Area vs. pressure | Tabulated data - Volumetric flow rate
    vs. pressure
  group: 参数
- name: Set pressure (gauge)
  summary: 触发阀操作的表压 0.1 MPa（默认）| 正标量
  group: 参数
- name: Pressure regulation range
  summary: 阀工作压力范围 1 MPa（默认）| 正标量
  group: 参数
- name: Maximum opening area
  summary: 全开阀的面积 1e-4 m^2（默认）| 正标量
  group: 参数
- name: Leakage area
  summary: 全关位置时的阀间隙面积 1e-10 m^2（默认）| 正标量
  group: 参数
- name: Pressure at port B (gauge) vector
  summary: '表格化面积参数化的表压值向量 [0.2 : 0.2 : 1.2] MPa（默认）| 1×*n* 向量'
  group: 参数
- name: Opening area vector
  summary: 表格化参数化的阀开度面积 [1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10] m^2（默认）| 1×*n* 向量
  group: 参数
- name: Cross-sectional area at ports A and B
  summary: 阀入口或出口处的面积 inf m^2（默认）| 正标量
  group: 参数
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: 参数
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: 参数
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: 参数
- name: Pressure recovery
  summary: 包含面积扩展期间压力增加的选项 off（默认）| on
  group: 参数
- name: Opening dynamics
  summary: 包含阀打开流量响应的选项 off（默认）| on
  group: 参数
- name: Opening time constant
  summary: 阀打开时间常数 0.1 s（默认）| 正标量
  group: 参数
- name: Reference pressure at port A (gauge)
  summary: 端口 A 处的参考压力 1.5 MPa（默认）| 正标量
  group: 参数
- name: Reference pressure at port B (gauge) vector
  summary: 端口 B 处的参考压力 [1.2, 1, .8, .6, .4, .2] MPa（默认）| 1×*n* 向量
  group: 参数
- name: Reference volumetric flow rate vector
  summary: 参考体积流量 [1e-09, 1.8e-05, 6.6e-05, .00013, .0002, .00028] m^3/s（默认）| 1×*n* 向量
  group: 参数
- name: Enable check valve
  summary: 单向阀选项 off（默认）| on
  group: 单向阀
- name: Cracking pressure differential
  summary: 单向阀操作的设定压力 0.1 MPa（默认）| 正标量
  group: 单向阀
- name: Maximum opening pressure differential
  summary: 阀中的最大压力 0.2 MPa（默认）| 正标量
  group: 单向阀
- name: Maximum opening area
  summary: 最大开度面积 1e-4 m^2（默认）| 正标量
  group: 单向阀
- name: Pressure differential vector
  summary: '单向阀操作的压差 [0.01 : 0.01 : 1] MPa（默认）| 1×*n* 向量'
  group: 单向阀
- name: Opening area vector
  summary: 单向阀级开度面积 [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 单向阀
- name: Volumetric flow rate vector
  summary: 单向阀级体积流量 [.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s（默认）| 1×*n* 向量
  group: 单向阀
- name: Pressure-Reducing Valve Area fault
  summary: 建模减压阀故障的选项 Add fault
  group: 故障
- name: Reducing valve opening when faulted
  summary: 减压阀故障位置 Closed（默认）| Open | Maintain last value
  group: 故障
- name: Check Valve Area fault
  summary: 建模单向阀故障的选项 Add fault
  group: 故障
- name: Check valve opening when faulted
  summary: 故障阀特性 Closed（默认）| Open | Maintain last value
  group: 故障
```

### 参数

### **Set pressure control** — 阀操作方法 `Constant`（默认）| `Controlled`

阀操作方法。当您将此参数设置为
`Constant` 时，阀在固定的压力调节范围内线性关闭，或根据您提供的表格化
压力和开度面积数据关闭。当您将此参数设置为 `Controlled` 时，阀
根据端口 **Ps** 处的可变设定压力信号在固定的压力调节
范围内关闭。

### **Opening parameterization** — 开度参数化 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀开度的建模方法。当您选择 `Linear - Area
vs. pressure` 或 `Tabulated data - Area vs.
pressure` 时，模块将开度面积与控制压力关联。当您选择 `Tabulated data -
Volumetric flow rate vs. pressure` 时，模块采用减压阀的
参考流量和压差曲线。

### **Set pressure (gauge)** — 触发阀操作的表压 `0.1` `MPa`（默认）| 正标量

触发阀操作的表压。当端口 **B** 处的压力达到此值时，阀
开始关闭。此参数偏移参考曲线，使减压阀在端口
**B** 处的压力等于设定压力时开始关闭。

#### 依赖关系

要启用此参数，请将 **Set pressure
control** 设置为
`Constant`。

### **Pressure regulation range** — 阀工作压力范围 `1` `MPa`（默认）| 正标量

阀的工作压力范围。压力调节范围
从 **Set pressure (gauge)** 开始，范围的终点是阀的最大工作压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为
`Linear - Area vs. pressure`。

### **Maximum opening area** — 全开阀的面积 `1e-4` `m^2`（默认）| 正标量

阀在全开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Linear - Area vs.
pressure`。

### **Leakage area** — 全关位置时的阀间隙面积 `1e-10` `m^2`（默认）| 正标量

阀处于全关位置时所有间隙的总和。任何小于
此值的面积饱和到指定的泄漏面积。此参数
通过保持流量连续性来贡献数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Linear - Area vs.
pressure`。

### **Pressure at port B (gauge) vector** — 表格化面积参数化的表压值向量 `[0.2 : 0.2 : 1.2]` `MPa`（默认）| 1×*n* 向量

用于阀开度面积表格化参数化的表压值
向量。向量元素必须与 **Opening area vector**
参数中的元素一一对应。元素必须为正且按升序排列。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Tabulated data -
Area vs. pressure`。

### **Opening area vector** — 表格化参数化的阀开度面积 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2`（默认）| 1×*n* 向量

用于阀开度面积表格化参数化的阀开度面积
向量。向量元素必须与 **Pressure at port B (gauge) vector** 参数中的元素
一一对应。元素必须为正且按升序排列。模块在数据点之间使用
线性插值。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Tabulated data -
Area vs. pressure`。

### **Cross-sectional area at ports A and B** — 阀入口或出口处的面积 `inf` `m^2`（默认）| 正标量

入口和出口端口 **A** 和
**B** 处的横截面积。模块在确定通过
阀的质量流量的压力-流量方程中使用这些面积。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Linear - Area vs.
pressure` 或 `Tabulated data - Area vs.
pressure`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

考虑理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Linear - Area vs.
pressure` 或 `Tabulated data - Area vs.
pressure`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Linear - Area vs.
pressure` 或 `Tabulated data - Area vs.
pressure`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在阀处于接近打开或接近关闭
位置时引入一层逐渐变化的流量响应。将此值设置为小于一的非零值以增加
这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为
`Linear - Area vs. pressure`。

### **Pressure recovery** — 包含面积扩展期间压力增加的选项 `off`（默认）| `on`

是否捕获流体从较小
横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Linear - Area vs.
pressure` 或 `Tabulated data - Area vs.
pressure`。

### **Opening dynamics** — 包含阀打开流量响应的选项 `off`（默认）| `on`

是否近似阀打开对流体系统的瞬态效应。
选择 **Opening dynamics** 通过在流量响应中引入一阶滞后来近似打开
条件。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Linear - Area vs.
pressure` 或 `Tabulated data - Area vs.
pressure`。

### **Opening time constant** — 阀打开时间常数 `0.1` `s`（默认）| 正标量

用于计算开度动力学滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics** 并将
**Opening parameterization** 设置为
`Linear - Area vs. pressure` 或
`Tabulated data - Area vs.
pressure`。

### **Reference pressure at port A (gauge)** — 端口 A 处的参考压力 `1.5` `MPa`（默认）| 正标量

端口 **A** 处的恒定压力，构成参考
曲线的基础。此值通常对应于阀的最大工作
压力。端口 **A** 处的压力在仿真期间可以为任意值。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure`。

### **Reference pressure at port B (gauge) vector** — 端口 B 处的参考压力 `[1.2, 1, .8, .6, .4, .2]` `MPa`（默认）| 1×*n* 向量

参考曲线中端口 **B** 处随阀开度面积变化的单调递减压力值
向量。第一个元素是参考最大压力，即阀
完全关闭时的压力。最后一个元素是参考设定压力。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure`。

### **Reference volumetric flow rate vector** — 参考体积流量 `[1e-09, 1.8e-05, 6.6e-05, .00013, .0002, .00028]` `m^3/s`（默认）| 1×*n* 向量

通过阀的单调递增参考流量向量。模块
使用此曲线为变化的阀面积生成流量系数。

#### 依赖关系

要启用此参数，请将 **Opening
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. pressure`。

### 单向阀

### **Enable check valve** — 单向阀选项 `off`（默认）| `on`

模块是否模拟内部单向阀。

### **Cracking pressure differential** — 单向阀操作的设定压力 `0.1` `MPa`（默认）| 正标量

提升单向阀的压差。

#### 依赖关系

要启用此参数，请将 **Enable check
valve** 设置为 `On`，并将
**Valve parameterization** 设置为
`Linear - Area vs. pressure`。

### **Maximum opening pressure differential** — 阀中的最大压力 `0.2` `MPa`（默认）| 正标量

单向阀完全关闭时的压差。

#### 依赖关系

要启用此参数，请将 **Enable check
valve** 设置为 `On`，并将
**Valve parameterization** 设置为
`Linear - Area vs. pressure`。

### **Maximum opening area** — 最大开度面积 `1e-4` `m^2`（默认）| 正标量

负载管路中单向阀的最大开度面积。在内部，单向阀与
减压级并联。

#### 依赖关系

要启用此参数，请将 **Enable check
valve** 设置为 `On`，并将
**Valve parameterization** 设置为
`Linear - Area vs. pressure`。

### **Pressure differential vector** — 单向阀操作的压差 `[0.01 : 0.01 : 1]` `MPa`（默认）| 1×*n* 向量

单向阀级的压差向量。模块将单向
阀压差计算为端口 **B** 处压力相对于端口 **A** 处压力。

#### 依赖关系

要启用此参数，请将 **Enable check
valve** 设置为 `On`，并将
**Valve parameterization** 设置为
`Tabulated data - Area vs. pressure` 或
`Tabulated data - Volumetric flow rate vs.
pressure`。

### **Opening area vector** — 单向阀级开度面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2`（默认）| 1×*n* 向量

单向阀级的开度面积向量。向量元素
必须与 **Pressure
differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Enable check
valve** 设置为 `On`，并将
**Valve parameterization** 设置为
`Tabulated data - Area vs.
pressure`。

### **Volumetric flow rate vector** — 单向阀级体积流量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s`（默认）| 1×*n* 向量

单向阀级的体积流量向量。此向量的
元素必须与 **Pressure differential vector** 参数中的元素对应。

#### 依赖关系

要启用此参数，请将 **Enable check
valve** 设置为 `On`，并将
**Valve parameterization** 设置为
`Tabulated data - Volumetric flow rate vs.
pressure`。

### 故障

### **Pressure-Reducing Valve Area fault** — 建模减压阀故障的选项 `Add fault`

启用减压阀故障参数的选项。要添加故障，请单击
**Add fault** 超链接。当故障发生时，模块将开度面积设置为
**Reducing valve opening when faulted** 参数指定的位置。

### **Reducing valve opening when faulted** — 减压阀故障位置 `Closed`（默认）| `Open` | `Maintain last value`

故障减压阀位置。您可以选择阀在打开、关闭或
原位时发生故障。

#### 依赖关系

要启用此参数，请单击 **Pressure-Reducing Valve Area fault**
参数的 **Add fault** 超链接。

### **Check Valve Area fault** — 建模单向阀故障的选项 `Add fault`

启用单向阀故障参数的选项。要添加故障，请单击
**Add fault** 超链接。当故障发生时，模块将开度面积设置为
**Check valve opening when faulted** 参数指定的位置。

#### 依赖关系

要启用此参数，请选择 **Enable check
valve**。

### **Check valve opening when faulted** — 故障阀特性 `Closed`（默认）| `Open` | `Maintain last value`

故障单向阀位置。您可以选择阀在打开、关闭或
原位时发生故障。

#### 依赖关系

要启用此参数，请选择 **Enable check valve** 并单击
**Check Valve Area fault** 参数的 **Add fault** 超链接。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口建模故障

Pressure-Reducing Valve (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：按体积流量与压力进行参数化

您可以将 **Opening parameterization** 设置为
`Tabulated data - Volumetric flow rate vs.
pressure`。

### R2022b：访问预参数化模块选项

模块支持预参数化选项。供应商包括 Hawe Hydraulik、
Rexroth Bosch Group 和 Sun Hydraulics。

## 描述

等温液体网络中的减压阀

Pressure-Reducing Valve (IL) 模块表示
等温液体网络中的减压阀。当端口 **B** 处的压力小于指定压力时，阀保持打开。当
端口 **B** 处的压力达到或超过此压力时，阀
关闭。模块基于设定压力与端口 **B** 处压力之间的差值运行。模块包含一个单向阀部分，其功能与 Check Valve
(IL) 模块在流量反向时相同。要基于
流体网络中的其他位置进行压力控制，请参阅 Pressure Compensator
Valve (IL) 模块。

### 设定压力控制

模块在设定压力和最大压力之间调节压力。当您将
**Set pressure control** 设置为：

- `Controlled` — 您可以将压力
  信号连接到端口 **Ps**。当端口 **B** 处的压力大于
  参考设定压力 *Pset*
  且低于 *Pmax* 时，模块调节压力。端口 **B** 处的压力
  充当此阀的控制压力
  *Pcontrol*。

  *Pmax* 是
  *Pset* 与压力
  调节范围之和。
- `Constant` — **Set pressure
  (gauge)** 参数定义恒定设定压力。

模块如何确定压力调节范围取决于
**Opening parameterization** 参数：

- `Linear - Area vs. pressure` —
  **Pressure regulation range** 参数定义
  压力调节范围。
- `Tabulated data - Area vs. Pressure` —
  压力调节范围是 **Pressure at port B (gauge) vector**
  参数最后一个元素与第一个元素之差。
- `Tabulated data - Volumetric flow rate vs.
  pressure` — 压力调节范围是
  **Reference pressure at port B (gauge) vector**
  参数第一个元素与最后一个元素之差。

### 面积与压力参数化

当您将 **Opening parameterization** 设置为 `Linear - Area
vs. pressure` 时，模块按如下方式计算阀口面积

Avalve=p^(Aleak−Amax)+Amax，

其中，归一化压力 p^ 为

p^=pcontrol−psetpmax−pset。

当阀门在线性参数化下处于接近开启或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *pset* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅数值平滑。

下图展示了使用线性面积参数化时阀门的开启特性。开启面积 *Avalve* 随出口压力 *pB,gauge* 线性下降。开启面积范围从 *Aleak* 到 *AMax*，压力工作范围从 *pset* 开始到 *pmax*。

线性面积参数化下开启面积随压力变化的图

当您将 **Opening parameterization** 设置为 `Tabulated data -
Area vs. Pressure` 时，模块按如下方式计算开启面积

Avalve=tablelookup(pcontrol,TLU,ATLU,pcontrol,interpolation=linear,extrapolation=nearest)，

其中：

- *pcontrol* = *pB,gauge* 是控制压力。
- *pcontrol,TLU* = *pB,TLU* + *poffset*。
- *pB,TLU* 是 **Pressure at port B (gauge) vector** 参数。
- *poffset* 是内部压力偏移，使阀门在 *pB,Gauge* = *pset* 时开始关闭，其中 *poffset* = *pset* - *pB,TLU(1)*。
- *ATLU* 是 **Opening area vector** 参数。

*Amax* 和 *Aleak* 分别是 **Opening area vector** 参数的第一个和最后一个参数。下图展示了使用表格面积参数化时阀门的开启特性。

表格面积参数化下开启面积随压力变化的图

**质量守恒**

当您将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. Pressure` 时，模块按如下方式保持质量守恒：

m˙A+m˙B=0。

模块按如下方式计算质量流量

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *Cd* 是 **Discharge coefficient** 参数。
- *Avalve* 是阀门瞬时开启面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差 *pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number** 参数 *Recrit* 相关的压差，即层流与湍流之间的流态转变点：

Δpcrit=πρ¯8Avalve(νRecritCd)2。

*压力损失* 描述了由于面积减小而导致的阀门压力降低。模块按如下方式计算 *PRloss*：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

*压力恢复* 描述了由于面积增加而导致的阀门正压力变化。如果您不希望捕获这种压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PRloss* 为 1。

模块使用阀门开启动态来确定开启面积 *Avalve*。

**开启动态**

对于任一种面积参数化，您都可以选择模拟阀门响应的开启动态。如果您选择 **Opening dynamics**，模块会在阀门开启时向流量响应添加滞后，并且 *Avalve* 变为动态开启面积 *Adyn*。否则，*Avalve* 是稳态开启面积。模块基于 **Opening time constant** 参数 *τ* 计算动态开启面积的瞬时变化：

p˙dyn=pcontrol−pdynτ。

默认情况下，模块忽略开启动态。

模块基于控制压力 *pcontrol* 并使用与阀门开启相同的参数化来计算稳态动态。

### 体积流量与压力参数化

体积流量参数化方程涉及以下量：

- *⩒TLU,ref* 是 **Reference volumetric flow rate vector** 参数。
- *PA,gauge,ref* 和 *PB,gauge,ref* 分别是 **Reference pressure at port A (gauge) vector** 和 **Reference pressure at port B (gauge) vector** 参数。
- *pset,gauge* 是 **Set pressure (gauge)** 参数或端口 **Ps** 处的信号。
- *K* 是通过减压级的流量系数，模块在仿真期间计算该系数。
- ρ¯ 是减压阀中的平均流体密度。
- *Δp* 是流体流过阀门时的压降。
- *Δpcrit* 是流体流动的临界压降。
- *Cd* 是流量系数，模块为体积流量参数化在内部设置该系数。
- *Recrit* 是临界雷诺数，模块在内部设置该值。
- *ν* 是运动粘度，对于等温液体网络为常数。

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块按如下方式计算减压阀的平滑质量流量

m˙valve=ρ¯KΔp(Δp2+Δp2)14Δp=pA−pBΔpcrit=π2ρ¯8CdK(Recritν)2

其中，模块使用 `tablelookup` 函数计算 *K*，如下所示

K=tablelookup(Δpcontrol,TLU,Ref,KTLU,Ref,Δpcontrol,interpolation=linear,extrapolation=nearest)KTLU,Ref=V˙TLU,RefΔpTLU,Ref

模块按如下方式计算控制压力

Δpcontrol=pB−pdrain，

其中，模块将排放压力 *pdrain* 设置为 1 atm。模块按如下方式计算参考控制压力向量

Δpcontrol,TLU,Ref=pB,gauge,ref+poffset，

其中 *poffset* 是内部计算的压力偏移，使阀门在 *pB,gauge,ref* = *pset,gauge* 时开始关闭。因此，*poffset* = *pset,gauge* - *pB,gauge,ref*。下图展示了模块如何使用表格体积流量参数化来控制压力。

表格体积参数化下开启面积随压力变化的图

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

减压阀和单向阀有三种故障选项可用。对于 **Reducing valve opening when faulted** 和 **Check valve opening when faulted** 参数，您可以选择：

- `Closed` — 阀门关闭到其最小开启值，具体取决于 **Opening parameterization** 参数。当您将 **Opening parameterization** 设置为：

  - `Linear - Area vs. pressure` — 阀门面积减小到 **Leakage area** 参数的值。
  - `Tabulated data - Area vs. pressure` — 阀门面积减小到 **Opening area vector** 参数中最后一个元素的值。
  - `Tabulated data - Volumetric flow rate vs. pressure` — 流量系数减小到导出的流量系数查找表 *KTLU,Ref* 中最后一个元素的值。
- `Open` — 阀门开启到其最大开启值，具体取决于 **Opening parameterization** 参数。当您将 **Opening parameterization** 设置为：

  - `Linear - Area vs. pressure` — 阀门面积开启到 **Maximum opening area** 的值。
  - `Tabulated data - Area vs. pressure` — 阀门面积开启到 **Opening area vector** 中第一个元素的值。
  - `Tabulated data - Volumetric flow rate vs. pressure` — 流量系数减小到导出的流量系数查找表 *KTLU,Ref* 中第一个元素的值。
- `Maintain last value` — 阀门面积在触发发生时保持在阀门开启面积。

对于线性参数化，阀门面积极值处的数值平滑会导致应用的最小面积大于 **Leakage area** 参数，并且最大值小于 **Maximum orifice area** 参数。

故障触发后，阀门在仿真的剩余时间内保持在故障面积。

### 预定义参数化

您可以使用预参数化的制造数据填充模块，这允许您对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，单击 **Selected part** 旁边的“<click to select>”超链接，该链接位于模块对话框设置的 **Selected part** 旁边。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件，并在 **Compare selected part with block** 部分查看数据，来将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用数据源来提供参数值。模块对缺失数据使用工程判断和简化假设进行替代。因此，预计仿真行为与实际物理行为之间会存在一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。
