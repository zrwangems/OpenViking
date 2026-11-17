---
type: simulink-block
title: '2-Way Directional Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalvetl'
documentation_source_path: 'ref/2waydirectionalvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-Way Directional Valve (TL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口 thermal liquid
  direction: conserving
- name: B
  summary: 液体端口 thermal liquid
  direction: conserving
- name: S
  summary: 阀芯位移，m physical signal
  direction: input
```

### 守恒端口

### **A** — 液体端口 thermal liquid

thermal liquid 守恒端口。

### **B** — 液体端口 thermal liquid

thermal liquid 守恒端口。

### 输入

### **S** — 阀芯位移，m physical signal

与阀芯位移关联的 physical signal，单位为 m。正值使阀门打开。
## 参数
```yaml
parameters:
- name: Orifice parameterization
  summary: 开口面积关系 Linear - Area vs. spool travel（默认）| Tabulated data - Area vs. spool travel | 表格数据 - 体积流量与阀芯行程和 pressure
    drop | Tabulated data - Mass flow rate vs. spool travel and pressure drop
  group: 模型参数化
- name: Spool position at maximum orifice area
  summary: 最大面积处的阀芯偏移 5e-3 m（默认）| 正标量
  group: 模型参数化
- name: Spool travel between closed and open orifice
  summary: 最大阀芯行程 5e-3 m（默认）| 正标量
  group: 模型参数化
- name: Maximum orifice area
  summary: 阀门完全打开时的面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: Leakage area
  summary: 完全关闭位置时的阀门间隙面积 1e-10 m^2（默认）| 正标量
  group: 模型参数化
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: 模型参数化
- name: Spool travel vector
  summary: 阀芯开口距离值 [0, .002, .004, .007, .017] m（默认）| 向量
  group: 模型参数化
- name: Orifice area vector
  summary: 阀门开口面积值 [1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2（默认）| 向量
  group: 模型参数化
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: 模型参数化
- name: Critical Reynolds number
  summary: 层流的雷诺数上限 150（默认）| 正标量
  group: 模型参数化
- name: Pressure recovery
  summary: 是否考虑面积扩大时的压力升高 on（默认）| off
  group: 模型参数化
- name: Spool travel vector, ds
  summary: 表格化阀芯开口距离值 [0, .002, .004, .007, .017] m（默认）| 向量
  group: 模型参数化
- name: Pressure drop vector, dp
  summary: 表格化压降值 [.3, .5, .7] MPa（默认）| 向量
  group: 模型参数化
- name: Volumetric flow rate table, q(ds,dp)
  summary: 给定阀芯行程和压降下的体积流量 [1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] m^3/s（默认）|
    矩阵
  group: 模型参数化
- name: Mass flow rate table, mdot(ds,dp)
  summary: 给定阀芯行程和压降下的质量流量 [1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] kg/s（默认）|
    矩阵
  group: 模型参数化
- name: Reference inflow temperature
  summary: 指定质量流量数据时的温度 293.15 K（默认）| 正标量
  group: 模型参数化
- name: Reference inflow pressure
  summary: 指定质量流量表格化数据时的压力 0.101325 MPa（默认）| 正标量
  group: 模型参数化
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的阀面积 0.01 m^2（默认）| 正标量
  group: 模型参数化
- name: 2-Way Directional Valve Area fault
  summary: 用于对阀芯位置故障建模的选项 Add fault
  group: 故障
- name: Spool position when faulted
  summary: 故障时的阀特性 Positive（默认）| Negative | Maintain last value
  group: 故障
```

### 模型参数化

### **Orifice parameterization** — 开口面积关系 `Linear - Area vs. spool travel`（默认）| `Tabulated data - Area vs. spool travel` | `表格数据 - 体积流量与阀芯行程和 pressure drop` | `Tabulated data - Mass flow rate vs. spool travel and pressure drop`

模块用于计算阀门流通面积的方法。

### **Spool position at maximum orifice area** — 最大面积处的阀芯偏移 `5e-3` `m`（默认）| 正标量

阀门完全打开时阀芯行程构件的位置。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `5e-3` `m`（默认）| 正标量

阀门最大打开面积处的阀芯偏移。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Maximum orifice area** — 阀门完全打开时的面积 `1e-4` `m^2`（默认）| 正标量

仿真过程中经历的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Leakage area** — 完全关闭位置时的阀门间隙面积 `1e-10` `m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。模块将任何小于此值的面积保持为指定的泄漏面积。此参数通过保持流动的连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在阀门接近打开和接近关闭位置时基于流量响应引入一层渐变。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Spool travel vector** — 阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认）| 向量

控制构件行程距离的向量。正值打开阀门。此向量中的值与 **Orifice area vector** 参数中的值一一对应。值必须从 0 开始递增。模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Orifice area vector** — 阀门开口面积值 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356]` `m^2`（默认）| 向量

用于开口面积表格参数化的阀门面积值向量。此向量中的值与 **Spool travel vector** 参数中的元素一一对应。此向量的第一个元素是泄漏面积，最后一个元素是最大阀门面积。模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

液压结构的排放损失。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为以下之一：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### **Critical Reynolds number** — 层流的雷诺数上限 `150`（默认）| 正标量

通过阀门的层流的雷诺数上限。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为以下任一值：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### **Pressure recovery** — 是否考虑面积扩大时的压力升高 `on`（默认）| `off`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力升高。

### **Spool travel vector, ds** — 表格化阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认）| 向量

控制构件行程距离的向量。阀芯行程向量与 **Pressure drop vector, dp** 参数一起构成三维因变量 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴。正位移对应于阀门打开。值从 0 开始递增。该模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `表格数据 - 体积流量与阀芯行程和 pressure drop`。

### **Pressure drop vector, dp** — 表格化压降值 `[.3, .5, .7]` `MPa`（默认）| 向量

体积流量的压降值向量。压降向量与 **Spool travel vector, ds** 参数一起构成三维因变量 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴。值必须递增。该模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data -Volumetric flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 给定阀芯行程和压降下的体积流量 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `m^3/s`（默认）| 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `表格数据 - 体积流量与阀芯行程和 pressure drop`。

### **Mass flow rate table, mdot(ds,dp)** — 给定阀芯行程和压降下的质量流量 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] kg/s`（默认）| 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow temperature** — 指定质量流量数据时的温度 `293.15 K`（默认）| 正标量

指定表格化质量流量数据时的温度。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow pressure** — 指定质量流量表格化数据时的压力 `0.101325 MPa`（默认）| 正标量

指定表格化质量流量数据时的压力。该模块使用此参数计算第三个参考参数，即参考密度。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data -
Mass flow rate vs. spool travel and pressure
drop`。

### **Cross-sectional area at ports A and B** — 守恒端口处的阀面积 `0.01` `m^2`（默认）| 正标量

端口 **A** 和 **B** 处的横截面积。模块在压力-流量方程中使用此面积来确定通过阀门的体积流量。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为以下任一值：

- `Tabulated data - Area vs. spool
  travel`
- `Linear - area vs. spool
  travel`

### 故障

### **2-Way Directional Valve Area fault** — 用于对阀芯位置故障建模的选项 `Add fault`

用于在模块中对阀芯位置故障建模的选项。要添加故障，请点击 **Add fault** 超链接。当故障发生时，通常由开度参数化设置的阀面积将根据 **Spool position when faulted** 参数中指定的值来设置。

### **Spool position when faulted** — 故障时的阀特性 `Positive`（默认）| `Negative` | `Maintain last value`

故障时的阀芯位置。您可以选择阀芯在正位置、负位置或故障触发时的位置卡滞。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

2-Way Directional Valve (TL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：右键点击模块以查看开度特性图

您可以通过右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**，查看每个节流口的面积或体积流量相对于阀芯位置的图。

## 描述

热液体网络中的二通方向阀

2-Way Directional Valve (TL) 模块表示一个二通阀，例如截止阀。使用此模块可模拟响应系统其他部分压力的减流控制元件。

该模块使用可变节流口来控制端口 **A** 和 **B** 之间的流量。端口 **S** 处的物理信号触发阀芯运动以打开或关闭阀门。有关模块如何计算通过可变节流口的流量的更多详细信息，请参阅 Orifice (TL)。

### 节流孔参数化

您可以线性地或使用表格数据来参数化阀门开度。

**线性**

当您将 **Orifice parameterization** 设置为
`Linear - Area vs. spool travel` 时，开口面积
是阀芯行程距离的线性函数。

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

其中

- *Aorifice* 是开口
  面积。
- *ΔS* 是在端口
  **S** 处输入的阀芯行程距离。ΔS=S−Smax+ΔSmax。
- *ΔSmax* 是
  **Spool travel between closed and open
  orifice** 参数的值。
- *ALeak* 是
  **Leakage area** 参数的值。
- *Amax* 是
  **Maximum orifice area** 参数的值。

请注意图中从
*ALeak* 到
*Amax* 的线性缩放。

当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整
**Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing
factor** 参数非零，该模块会在 *Aleak* 和
*Amax* 之间平滑地饱和开口面积。有关更多信息，请参阅数值平滑。

**表格化**

当您将 **Orifice parameterization** 设置为
`Tabulated data - Area vs. spool travel` 时，该模块
使用 **Spool travel vector** 和 **Orifice area
vector** 参数，通过插值来定义
*Aorifice* 与
*ΔS* 之间的关系。
*Aleak* 和
*Amax* 分别是 **Orifice area vector** 参数的第一个和最后一个
参数。

当您将 **Orifice parameterization** 设置为
`表格数据 - 体积流量与阀芯行程和
pressure drop` 时，该模块使用 **Volumetric flow
rate table, q(ds,dp)**、**Pressure drop vector,
dp** 和 **Spool travel vector, ds** 参数
来定义体积流量，
*q(**ΔS**,**p**)*。

当您将 **Orifice parameterization** 设置为
`表格数据 - 质量流量与开度和压力
drop` 时，该模块根据阀芯位置和阀门两端的压降直接计算质量流量。这三个变量之间的关系可以是非线性的，并且由
**Spool travel vector, ds**、**Pressure drop
vector, dp** 和 **Mass flow rate table,
mdot(ds,dp)** 参数中的表格数据给出。

### 可视化节流孔开口

要可视化阀芯偏移和位移，请右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示阀门开口面积或体积流量随
阀芯位置变化的函数关系。

要在更改模块参数后更新数据，请单击图形窗口中的 **Reload
Data**。

下图显示了具有以下配置的阀门：

- **Spool position at maximum orifice area** 设置为
  `2e-3` m。
- **Spool travel between closed and open orifice** 设置
  为 `6e-3` m。

所有其他参数均为默认值。

每个节流孔的面积与阀芯位置关系图。

### 故障

要对故障建模，请在 **Faults** 部分中，
单击要建模的故障旁边的 **Add fault** 超链接。使用
故障参数指定故障属性。有关故障建模的更多信息，
请参阅 Introduction to Simscape Faults。

你可以通过 **Spool position when
faulted** 参数选择故障类型：

- `Negative` — 该模块将阀冻结在
  其最小值。下表显示了该模块根据
  **Orifice parameterization**
  参数的设置使用哪个值。

  | **Orifice parameterization** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **Leakage area** 参数 |
  | `Tabulated data - Area vs. spool travel` | **Orifice area vector** 参数的第一个元素 |
  | `表格数据 - 体积流量与阀芯行程和 pressure drop` | **Volumetric flow rate table, q(ds,dp)** 参数的第一行 |
  | `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **Mass flow rate table, mdot(ds,dp)** 参数的第一行 |
- `Positive` — 阀冻结在
  其最大值。下表显示了该模块根据
  **Orifice parameterization**
  参数的设置使用哪个值。

  | **Orifice parameterization** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **Maximum opening area** 参数 |
  | `Tabulated data - Area vs. spool travel` | **Orifice area vector** 参数的最后一个元素 |
  | `表格数据 - 体积流量与阀芯行程和 pressure drop` | **Volumetric flow rate table, q(ds,dp)** 参数的最后一行 |
  | `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **Mass flow rate table, mdot(ds,dp)** 参数的最后一行 |
- `Maintain last value` — 阀冻结在
  其最后一个值。下表显示了该模块根据
  **Orifice parameterization**
  参数的设置使用哪个值。

  | **Orifice parameterization** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | 触发发生时的阀开口面积 |
  | `Tabulated data - Area vs. spool travel` | 触发发生时的阀开口面积 |
  | `表格数据 - 体积流量与阀芯行程和 pressure drop` | 当前位置 |
  | `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | 当前位置 |

  当你将 **Orifice
  parameterization** 设置为 `Tabulated data -
  Volumetric flow rate vs. spool travel and pressure
  drop` 或 `Tabulated data - Mass flow rate
  vs. spool travel and pressure drop` 时，在阀冻结后，体积
  流量或质量流量会根据阀中的压力
  变化继续变化。

由于阀面积极值处的数值平滑，在
线性参数化中，该模块使用的最小面积大于
**Leakage area**，并且最大值小于
**Maximum orifice area**，其比例与
**Smoothing factor** 值成比例。有关更多信息，请参阅 Numerical Smoothing。
