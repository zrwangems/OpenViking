---
type: simulink-block
title: '2-Way Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalveil'
documentation_source_path: 'ref/2waydirectionalvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-Way Directional Valve (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

等温液体守恒端口。

### **B** — 液体端口，等温液体

等温液体守恒端口。
### 输入

### **S** — 阀芯位移，m，物理信号

与阀芯位移相关联的物理信号，单位为 m。正值使阀门打开。

## 参数

### 模型参数化

### **Orifice parameterization** — 开口面积关系 `Linear - area vs. spool travel`（默认）| `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

模块用于计算阀门流通面积的方法。了解更多信息，请参阅 Orifice Parameterizations。

### **Spool position at maximum orifice area** — 最大面积时的阀芯偏移 `5e-3` `m`（默认）| 正标量

阀门完全打开时阀芯行程构件的位置。默认值表示零开口系统。正的、非零值表示负开口（部分关闭）系统。负的、非零值表示正开口系统，阀门在一定位移范围内保持打开。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `5e-3` `m`（默认）| 正标量

最大阀门开口面积时的阀芯偏移。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Linear - area vs.
spool travel`。

### **Maximum orifice area** — 阀门完全打开时的面积 `1e-4` `m^2`（默认）| 正标量

仿真过程中经历的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Linear - area vs.
spool travel`。

### **Leakage area** — 完全关闭位置时的阀门间隙面积 `1e-10` `m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。模块将任何小于此值的面积保持为指定的泄漏面积。此参数通过保持流动的连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Linear - area vs.
spool travel`。

### **Spool travel vector** — 阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认）| 向量

控制构件行程距离的向量。正值打开阀门。此向量中的值与 **Orifice area vector** 参数中的值一一对应。值必须从 0 开始递增。模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Tabulated data - Area
vs. spool travel`。

### **Orifice area vector** — 阀门开口面积值 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356]` `m^2`（默认）| 向量

用于开口面积表格参数化的阀门面积值向量。此向量中的值与 **Spool travel vector** 参数中的元素一一对应。此向量的第一个元素是泄漏面积，最后一个元素是最大阀门面积。模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Tabulated data - Area
vs. spool travel`。

### **Spool travel vector, ds** — 表格阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认）| 向量

控制构件行程距离的向量。阀芯行程向量与 **Pressure drop vector,
dp** 参数一起构成三维因变量 **Volumetric
flow rate table, q(ds,dp)** 参数的独立轴。正位移对应阀门打开。值从 0 开始递增。模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### **Pressure drop vector, dp** — 表格压降值 `[.3, .5, .7]` `MPa`（默认）| 向量

体积流量的压降值向量。压降向量与 **Spool
travel vector, ds** 参数一起构成三维因变量
**Volumetric flow rate table, q(ds,dp)** 参数的独立轴。值必须为正且递增。模块对数据点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Tabulated data
-Volumetric flow rate vs. spool travel and pressure
drop`。

### **Volumetric flow rate table, q(ds,dp)** — 给定阀芯行程和压降下的体积流量 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `m^3/s`（默认）| 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds**
  参数中的元素数量。
- *N* 是 **Pressure drop vector, dp**
  参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

液压结构的排放损失。Simscape™
Fluids™ 中阀门的默认流量系数为 0.64。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为以下之一：

- `Tabulated data - Area vs. spool
  travel`
- `Linear - area vs. spool
  travel`

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为以下之一：

- `Tabulated data - Area vs. spool
  travel`
- `Linear - area vs. spool
  travel`

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，在阀门接近打开和接近关闭位置时基于流量响应引入逐渐变化的层。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Linear - area vs.
spool travel`。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `on`（默认）| `off`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **Cross-sectional area at ports A and B** — 守恒端口处的阀门面积 `inf` `m^2`（默认）| 正标量

端口 **A** 和 **B** 处的横截面积。模块在压力-流量方程中使用此面积来确定通过阀门的体积流量。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为以下之一：

- `Tabulated data - Area vs. spool
  travel`
- `Linear - area vs. spool
  travel`

### 故障

### **2-Way Directional Valve Area fault** — 建模阀芯位置故障的选项 `Add fault`

用于在模块中建模阀芯位置故障的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀门面积将根据 **Spool position when
faulted** 参数中指定的值进行设置。

### **Spool position when faulted** — 故障时的阀门特性 `Positive`（默认）| `Negative` | `Maintain last value`

故障时的阀芯位置。您可以选择阀门在阀芯处于正位置、负位置或故障触发时的位置时卡滞。

#### 依赖关系

要启用此参数，请单击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a: 使用 Simscape faults 接口对故障建模

2-Way Directional Valve (IL) 模块现在支持 Simscape faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体系统中的二通流量控制阀

2-Way Directional Valve (IL) 模块表示一个二通阀，例如截止阀。使用此模块可模拟响应系统另一部分压力的减流控制元件。

该模块使用可变节流孔来控制端口 **A** 和 **B** 之间的流量。端口 **S** 处的物理信号触发阀芯运动以打开或关闭阀门。有关该模块如何计算通过可变节流孔的流量的更多详细信息，请参阅 Orifice (IL)。

### 节流孔参数化

您可以线性地或使用表格数据来参数化阀门开度。

**线性**

当您将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 时，开口面积是阀芯行程距离的线性函数。

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

其中

- *Aorifice* 是开口面积。
- *ΔS* 是在端口 **S** 处输入的阀芯行程距离。ΔS=S−Smax+ΔSmax。
- *ΔSmax* 是 **Spool travel between closed and open orifice** 参数的值。
- *ALeak* 是 **Leakage area** 参数的值。
- *Amax* 是 **Maximum orifice area** 参数的值。

请注意图中从 *ALeak* 到 *Amax* 的线性缩放。

当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，则该模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关更多信息，请参阅 Numerical Smoothing。

**表格化**

当您将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel` 时，该模块使用 **Spool travel vector** 和 **Orifice area vector** 参数通过插值来定义 *Aorifice* 与 *ΔS* 之间的关系。*Aleak* 和 *Amax* 分别是 **Orifice area vector** 参数的第一个和最后一个参数。

当您将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 时，该模块使用 **Volumetric flow rate table, q(ds,dp)**、**Pressure drop vector, dp** 和 **Spool travel vector, ds** 参数来定义体积流量，*q(**ΔS**,**p**)*。

### 可视化节流孔开口

要可视化阀芯偏移和位移，请右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示阀门开口面积或体积流量随阀芯位置的变化。

要在更改模块参数后更新数据，请在图形窗口中点击 **Reload Data**。

下图显示了具有以下配置的阀门：

- **Spool position at maximum orifice area** 设置为 `2e-3` m。
- **Spool travel between closed and open orifice** 设置为 `6e-3` m。

所有其他参数均为默认值。

每个节流孔的面积与阀芯位置的关系图。

### 故障

要对故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Introduction to Simscape Faults。

您可以通过 **Spool position when faulted** 参数选择故障类型：

- `Negative` — 该模块将阀门冻结在其最小值。下表显示了根据 **Orifice parameterization** 参数的设置，该模块使用哪个值。

  | **Orifice parameterization** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **Leakage area** 参数 |
  | `Tabulated data - Area vs. spool travel` | **Orifice area vector** 参数的第一个元素 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **Volumetric flow rate table, q(ds,dp)** 参数的第一行 |
- `Positive` — 阀门冻结在其最大值。下表显示了根据 **Orifice parameterization** 参数的设置，该模块使用哪个值。

  | **Orifice parameterization** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **Maximum opening area** 参数 |
  | `Tabulated data - Area vs. spool travel` | **Orifice area vector** 参数的最后一个元素 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **Volumetric flow rate table, q(ds,dp)** 参数的最后一行 |
- `Maintain last value` — 阀门冻结在其最后一个值。下表显示了根据 **Orifice parameterization** 参数的设置，该模块使用哪个值。

  | **Orifice parameterization** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | 触发发生时阀门开口面积 |
  | `Tabulated data - Area vs. spool travel` | 触发发生时阀门开口面积 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | 当前位置 |

  当您将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 时，在阀门冻结后，体积流量会根据阀门中的压力变化继续变化。

由于线性参数化中阀门面积极值处的数值平滑，该模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，其比例与 **Smoothing factor** 值成正比。有关更多信息，请参阅 Numerical Smoothing。
