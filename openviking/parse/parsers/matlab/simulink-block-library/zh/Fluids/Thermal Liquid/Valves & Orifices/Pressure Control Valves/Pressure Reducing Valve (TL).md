---
type: simulink-block
title: 'Pressure Reducing Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalvetl'
documentation_source_path: 'ref/pressurereducingvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Reducing Valve (TL)

## 端口
```yaml
ports:
- name: Ps
  summary: 设定压力信号，Pa 物理信号
  direction: input
- name: A
  summary: 液体端口 热液体
  direction: input
- name: B
  summary: 液体端口 热液体
  direction: input
```

### 输入

### **Ps** — 设定压力信号，Pa 物理信号

受控阀操作的压力阈值，单位为 Pa。

#### 依赖

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

### 守恒

### **A** — 液体端口 热液体

与阀入口 A 关联的热液体守恒端口。

### **B** — 液体端口 热液体

与阀入口 B 关联的热液体守恒端口。
## 参数
```yaml
parameters:
- name: Opening parameterization
  summary: 开度参数化 Linear - Area vs. pressure（默认）| Tabulated data - Area vs. pressure | Tabulated data - Volumetric flow rate
    vs. pressure
  group: 参数
- name: Set pressure control
  summary: 阀操作方法 Constant（默认）| Controlled
  group: 参数
- name: Set pressure (gauge)
  summary: 阀开始关闭时的表压 0.1 MPa（默认）| 正标量
  group: 参数
- name: Pressure regulation range
  summary: 阀压力范围 0.01 MPa（默认）| 正标量
  group: 参数
- name: Maximum opening area
  summary: 全开位置的开度面积 1e-4 m^2（默认）| 正标量
  group: 参数
- name: Leakage area
  summary: 全关位置的间隙面积 1e-10 m^2（默认）| 正标量
  group: 参数
- name: Pressure at port B (gauge) vector
  summary: '表格化面积参数化的表压值向量 [0.2 : 0.2 : 1.2] MPa（默认）| 1×*n* 向量'
  group: 参数
- name: Opening area vector
  summary: 用于表格化面积参数化的阀开口面积 [1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10] m^2（默认）| 1×*n* 向量
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
- name: 端口 A 和 B 处的横截面积
  summary: 守恒端口处的面积 0.01 m^2（默认）| 正标量
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
  summary: 包含面积扩大期间压力增加的选项 off（默认）| on
  group: 参数
- name: Opening dynamics
  summary: 包含阀门开启流量响应的选项 off（默认）| on
  group: 参数
- name: Opening time constant
  summary: 阀门开启时间常数 0.1 s（默认）| 正标量
  group: 参数
- name: Enable check valve
  summary: 单向阀选项 off（默认）| on
  group: Check Valve
- name: Cracking pressure differential
  summary: 单向阀操作设定压力 0.1 MPa（默认）| 正标量
  group: Check Valve
- name: Maximum opening pressure differential
  summary: 阀门最大压力 0.2 MPa（默认）| 正标量
  group: Check Valve
- name: Maximum opening area
  summary: 最大开启面积 1e-4 m^2（默认）| 正标量
  group: Check Valve
- name: Pressure differential vector
  summary: '单向阀操作的压差 [0.01 : 0.01 : 1] MPa（默认）| 1×*n* 向量'
  group: Check Valve
- name: Opening area vector
  summary: 单向级开启面积 [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2（默认）| 1×*n* 向量
  group: Check Valve
- name: Volumetric flow rate vector
  summary: 单向级体积流量 [.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s（默认）| 1×*n* 向量
  group: Check Valve
- name: Pressure-Reducing Valve Area fault
  summary: 建模减压阀故障的选项 Add fault
  group: 故障
- name: Reducing valve opening when faulted
  summary: 减压阀故障位置 Closed（默认）| Open | Maintain last value
  group: 故障
- name: Check Valve Area fault
  summary: 止回阀故障建模选项 Add fault
  group: 故障
- name: Check valve opening when faulted
  summary: 故障阀门特性 Closed（默认）| Open | Maintain last value
  group: 故障
```

### 参数

### **Opening parameterization** — 开度参数化 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀开度的建模方法。当您将此参数设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，模块将开度面积与控制压力关联。当您将此参数设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块采用减压阀的参考流量和压差曲线。

### **Set pressure control** — 阀操作方法 `Constant`（默认）| `Controlled`

阀操作方法。当您将此参数设置为 `Constant` 时，阀在固定的压力调节范围内或根据您提供的表格化压力和开度面积数据线性关闭。当您将此参数设置为 `Controlled` 时，阀根据端口 **Ps** 处的可变设定压力信号在固定的压力调节范围内关闭。

### **Set pressure (gauge)** — 阀开始关闭时的表压 `0.1` `MPa`（默认）| 正标量

阀开始关闭时的压力。在阀的压力调节范围内，开度面积保持可变。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Pressure regulation range** — 阀压力范围 `0.01` `MPa`（默认）| 正标量

阀开度面积变化的压力区间。该区间从 **Set pressure (gauge)** 参数的值开始。

#### 依赖

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 全开位置的开度面积 `1e-4` `m^2`（默认）| 正标量

当阀处于压力调节范围下限时，由于密封不完美，阀在全开位置的开度面积。模块使用此参数在整个压力调节范围内缩放阀开度。

#### 依赖

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 全关位置的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀处于全关位置时所有间隙的总和。模块将较小的数值饱和到此值。此参数通过保持流量连续性来增强数值稳定性。

#### 依赖

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure at port B (gauge) vector** — 表格化面积参数化的表压值向量 `[0.2 : 0.2 : 1.2]` `MPa`（默认）| 1×*n* 向量

用于阀开度面积表格化面积参数化的表压值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素必须为正且按升序排列。模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Opening area vector** — 用于表格化面积参数化的阀开口面积 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2`（默认）| 1×*n* 向量

用于阀开口面积的表格化面积参数化的阀开口面积向量。向量元素必须与 **Pressure at Port B (gauge) vector** 参数中的元素一一对应。元素必须为正且按升序排列。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Reference pressure at port A (gauge)** — 端口 A 处的参考压力 `1.5` `MPa`（默认）| 正标量

端口 **A** 处的恒定压力，构成参考曲线的基础。此值通常对应于阀的最大工作压力。仿真期间，端口 **A** 处的压力可以是任意值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference pressure at port B (gauge) vector** — 端口 B 处的参考压力 `[1.2, 1, .8, .6, .4, .2]` `MPa`（默认）| 1×*n* 向量

参考曲线中端口 **B** 处随阀开口面积变化的单调递减压力值向量。第一个元素是参考最大压力，即阀完全关闭时的压力。最后一个元素是参考设定压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference volumetric flow rate vector** — 参考体积流量 `[1e-09, 1.8e-05, 6.6e-05, .00013, .0002, .00028]` `m^3/s`（默认）| 1×*n* 向量

通过阀的单调递增参考流量向量。模块使用此曲线为变化的阀面积生成流量系数。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **端口 A 和 B 处的横截面积** — 守恒端口处的面积 `0.01` `m^2`（默认）| 正标量

端口 **A** 和 **B** 处的面积，模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

模块用于修正理论流量中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 包含面积扩大期间压力增加的选项 `off`（默认）| `on`

是否捕获流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening dynamics** — 包含阀门开启流量响应的选项 `off`（默认）| `on`

是否近似模拟阀门开启对流体系统造成的瞬态效应。选择 **Opening dynamics** 通过引入流量响应的一阶滞后来近似开启条件。

### **Opening time constant** — 阀门开启时间常数 `0.1` `s`（默认）| 正标量

用于计算开启动态滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### Check Valve

### **Enable check valve** — 单向阀选项 `off`（默认）| `on`

模块是否模拟内部单向阀。

### **Cracking pressure differential** — 单向阀操作设定压力 `0.1` `MPa`（默认）| 正标量

开启单向阀的压差。

#### 依赖关系

要启用此参数，请选择 **Enable check valve** 并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening pressure differential** — 阀门最大压力 `0.2` `MPa`（默认）| 正标量

单向阀完全关闭时的压差。

#### 依赖关系

要启用此参数，请选择 **Enable check valve** 并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 最大开启面积 `1e-4` `m^2`（默认）| 正标量

负载管路中单向阀的最大开启面积。在内部，单向阀与减压级并联。

#### 依赖关系

要启用此参数，请选择 **Enable check valve** 并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 单向阀操作的压差 `[0.01 : 0.01 : 1]` `MPa`（默认）| 1×*n* 向量

单向阀级的压差向量。模块将单向阀压差计算为端口 **B** 处压力相对于端口 **A** 处压力。

#### 依赖关系

要启用此参数，请选择 **Enable check valve** 并将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Opening area vector** — 单向级开启面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2`（默认）| 1×*n* 向量

单向阀级的开启面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请选择 **Enable check valve** 并将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Volumetric flow rate vector** — 单向级体积流量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s`（默认）| 1×*n* 向量

单向阀级的体积流量向量。此向量的元素必须与 **Pressure differential vector** 参数中的元素对应。

#### 依赖关系

要启用此参数，请选择 **Enable check valve** 并将 **Valve parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### 故障

### **Pressure-Reducing Valve Area fault** — 建模减压阀故障的选项 `Add fault`

启用减压阀故障参数的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，模块将开启面积设置为 **Reducing valve opening when faulted** 参数指定的位置。

### **Reducing valve opening when faulted** — 减压阀故障位置 `Closed`（默认）| `Open` | `Maintain last value`

故障减压阀位置。您可以选择阀门在开启、关闭或保持原位时发生故障。

#### 依赖关系

要启用此参数，请通过点击 **Pressure-Reducing Valve Area fault** 参数的 **Add fault** 超链接为模块启用故障。

### **Check Valve Area fault** — 止回阀故障建模选项 `Add fault`

用于启用止回阀故障参数的选项。要添加故障，请点击 **Add fault** 超链接。当故障发生时，模块将开启面积设置为 **Check valve opening when faulted** 参数指定的位置。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**。

### **Check valve opening when faulted** — 故障阀门特性 `Closed`（默认）| `Open` | `Maintain last value`

故障止回阀位置。您可以选择阀门在开启、关闭或保持原位时发生故障。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并通过点击 **Check Valve Area fault** 参数的 **Add fault** 超链接来启用模块的故障。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

Pressure Reducing Valve (TL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2024b：新的阀门控制选项

将 **Set pressure control** 设置为 `Controlled`，以通过端口 **Ps** 处的信号控制模块设定压力。选择 **Enable check valve** 以对在流动反向期间功能与 Check Valve (TL) 模块相同的止回阀进行建模。

### R2023a：新的参数化选项

使用 **Opening parameterization** 参数选择模块参数化 `Linear - Area vs. pressure`、`Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

## 描述

热液网络中的减压阀

Pressure Reducing Valve (TL) 模块表示一个降低热液网络下游压力的阀门。当端口 **B** 处的压力小于指定压力时，阀门保持开启。当端口 **B** 处的压力达到或超过此压力时，阀门关闭。模块基于设定压力与端口 **B** 处压力之间的差值运行。模块包含一个止回阀部分，其在流动反向期间功能与 Check Valve (TL) 模块相同。

### 压力控制

模块在设定压力和最大压力之间调节压力。当您将 **Set pressure control** 设置为：

- `Controlled` — 您可以将压力信号连接到端口 **Ps**。当端口 **B** 处的压力大于参考设定压力 *Pset* 且低于 *Pmax* 时，模块调节压力。端口 **B** 处的压力充当此阀门的控制压力 *Pcontrol*。

  *Pmax* 是 *Pset* 与压力调节范围之和。
- `Constant` — **Set pressure (gauge)** 参数定义恒定设定压力。

当 **Opening parameterization** 为 `Linear - Area vs. pressure` 时，归一化压力 p^ 控制阀门开启面积。归一化压力为

p^=pcontrol-psetpmax-pset，

其中：

- *pcontrol* 是控制压力，*pB ̶ pAtm*，其中 *pAtm* 是大气压力。
- *pset* 是阀门设定压力

  pset=pset,gauge+pAtm，

  其中 *Pset,gauge* 是 **Set pressure (gauge)** 参数的值。
- *pmax* 是最大压力，*pmax = pset + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。

### 开度参数化

质量流量取决于 **Opening parameterization** 参数的值。

**面积 vs. 压力参数化**

当您将 **Opening parameterization** 设置为
`Linear - Area vs. pressure` 或
`Tabulated data - Area vs. pressure` 时，质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 是
  **Discharge coefficient** 参数的值。
- *Avalve* 是
  瞬时阀门开启面积。
- *Aport* 是
  **端口 A 和 B 处的横截面积**
  参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差
  *pA* –
  *pB*。

临界压差
*Δpcrit* 是与 **Critical Reynolds number**
*Recrit* 相关的压差，
即层流与湍流之间的流态
转变点：

Δpcrit=π8Avalveρ¯(μRecritCd)2,

其中 *μ* 是热液体的
动力粘度。

压力损失 *PRloss* 描述了
由于面积减小而导致的阀门压力
降低。该模块计算 *PRloss* 如下

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

压力恢复描述了由于面积增加而导致的阀门正压力变化。当您清除 **Pressure
recovery** 复选框时，该模块将
*PRloss* 设置为 1。

当您将 **Opening parameterization** 参数设置为
`Linear - Area vs. pressure` 时，该模块计算
开启面积如下

Avalve=p^(Aleak−Amax)+Amax,

其中 *Aleak* 是
**Leakage Area** 参数的值，
*Amax* 是
**Maximum opening area** 参数的值。

下图显示了该模块如何使用线性
参数化控制开启面积。

使用线性参数化的常开阀，端口 X 和 Y 之间的压差与开启面积的关系

当阀门在线性参数化中处于接近开启或
接近关闭位置时，您可以通过调整 **Smoothing
factor** 参数来保持仿真中的数值
鲁棒性。如果 **Smoothing factor**
参数非零，该模块会在
*pset* 和
*pmax* 之间平滑地饱和控制压力。有关更多信息，
请参阅数值平滑。

当您将 **Opening parameterization** 设置为
`Tabulated data - Area vs. pressure` 时，该模块
计算开启面积如下

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

其中：

- *pcontrol,TLU,ref*
  = *pTLU* +
  *poffset*。
- *pTLU* 是
  **Pressure differential vector**
  参数。
- *poffset* 是一个内部
  压力偏移量，使得阀门在
  *pcontrol,TLU,ref* =
  *pset* 时开始关闭。
- *ATLU* 是
  **Opening area vector** 参数。

下图显示了当
**Opening parameterization** 为 `Tabulated data
- Area vs. pressure` 时，该模块如何控制开启面积。

使用表格参数化的常开阀，端口 X 和 Y 之间的压差与开启面积的关系

**体积流量 vs. 压力参数化**

当您将 **Opening parameterization** 设置为
`Tabulated data - Volumetric flow rate vs.
pressure` 时，阀门根据用户提供的
端口 **A** 和 **B** 之间的体积流量和压差
表格数据打开。

该模块计算质量流量如下

m˙=ρ¯V˙,

其中：

- V˙ 是体积流量。
- ρ¯ 是平均流体密度。

该模块使用以下公式计算质量流量与压力
之间的关系

m˙=Kρ¯Δp,

其中

K=V˙|Δp|.

### 开度动态

当您选中 **Opening dynamics** 时，该模块引入
控制压力滞后，其中 *pcontrol*
变为动态控制压力
*pdyn*。动态
开启面积的瞬时变化基于 **Opening time constant**
参数 *τ* 计算：

p˙dyn=pcontrol−pdynτ.

默认情况下，该模块清除 **Opening
dynamics** 复选框。

### Energy Balance

阀门中的能量守恒方程为

ϕA+ϕB=0，

其中：

- *ϕA* 是通过端口 **A** 进入阀门的能量流率。
- *ϕB* 是通过端口 **B** 进入阀门的能量流率。

### 故障

要对故障建模，请在 **Faults** 部分中，
单击要建模的故障旁边的 **Add fault** 超链接。使用
故障参数来指定故障属性。有关故障建模的更多信息，
请参阅 Introduction to Simscape Faults。

减压阀和单向阀有三个故障选项。对于
**Reducing valve opening when faulted** 和 **Check
valve opening when faulted** 参数，您可以选择：

- `Closed` — 阀门关闭到其最小
  开度值，具体取决于 **Opening
  parameterization** 参数。当您将
  **Opening parameterization** 设置为：

  - `Linear - Area vs. pressure` —
    阀门面积减小到 **Leakage
    area** 参数的值。
  - `Tabulated data - Area vs.
    pressure` — 阀门面积减小到
    **Opening area
    vector** 参数中最后一个元素的值。
  - `Tabulated data - Volumetric flow rate vs.
    pressure` — 流量系数减小到
    导出的流量系数查找表
    *KTLU,Ref* 中最后一个元素的值。
- `Open` — 阀门打开到其最大
  开度值，具体取决于 **Opening
  parameterization** 参数。当您将
  **Opening parameterization** 设置为：

  - `Linear - Area vs. pressure` —
    阀门面积打开到 **Maximum
    opening area** 的值。
  - `Tabulated data - Area vs.
    pressure` — 阀门面积打开到
    **Opening area
    vector** 中第一个元素的值。
  - `Tabulated data - Volumetric flow rate vs.
    pressure` — 流量系数减小到
    导出的流量系数查找表
    *KTLU,Ref* 中第一个元素的值。
- `Maintain last value` — 触发发生时，阀门面积
  保持在阀门开度面积。

对于线性参数化，阀门面积极值处的数值平滑
会导致应用的最小面积大于
**Leakage area** 参数，而最大值小于
**Maximum orifice area** 参数。

故障触发后，阀门在仿真的剩余时间内保持
故障面积。

### Predefined Parameterization

您可以使用预参数化的制造数据填充该模块，从而
对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击
   模块对话框设置中 **Selected part** 旁边的
   "<click to select>" 超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，
   然后单击 **Apply all**。您可以使用
   **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。
   该模块现在具有您指定的参数化。
4. 您可以在 Block Parameterization Manager 窗口中选择一个部件并查看
   **将选定部分与模块进行比较**
   部分中的数据，从而将当前参数设置与特定供应商组件
   进行比较。

**Note**

预定义模块参数化使用可用数据源来提供参数
值。该模块会用工程判断和简化假设替代
缺失数据。因此，预计仿真行为与实际物理
行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，
并根据需要细化您的组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
