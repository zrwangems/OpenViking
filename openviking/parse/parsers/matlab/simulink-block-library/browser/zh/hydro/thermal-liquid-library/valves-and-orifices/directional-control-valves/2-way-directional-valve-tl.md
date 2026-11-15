---
type: simulink-block
title: '2-Way Directional Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Valves and Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalvetl'
documentation_source_path: 'ref/2waydirectionalvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-Way Directional Valve (TL)

## 端口

### 守恒端口

### **A** — 液体端口 thermal liquid

Thermal liquid 守恒端口。

### **B** — 液体端口 thermal liquid

Thermal liquid 守恒端口。
### 输入

### **S** — 阀芯位移，m physical signal

与阀芯位移关联的 physical signal，单位为 m。正值使阀门打开。

## 参数

### 模型参数化

### **Orifice parameterization** — 开口面积关系 `Linear - Area vs. spool travel`（默认） | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | `Tabulated data - Mass flow rate vs. spool travel and pressure drop`

该模块用于计算阀门流通面积的方法。

### **Spool position at maximum orifice area** — 最大面积处的阀芯偏移 `5e-3` `m`（默认） | positive scalar

阀门完全打开时阀芯行程构件的位置。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `5e-3` `m`（默认） | positive scalar

阀门最大打开面积处的阀芯偏移。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Maximum orifice area** — 完全打开阀门时的面积 `1e-4` `m^2`（默认） | positive scalar

仿真期间经历的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Leakage area** — 完全关闭位置时的阀门间隙面积 `1e-10` `m^2`（默认） | positive scalar

当阀门处于完全关闭位置时所有间隙的总和。该模块将任何小于此值的面积保持在指定的泄漏面积。此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | positive scalar in the range [0,1]

连续平滑因子，当阀门处于接近打开和接近关闭位置时，基于流量响应引入一层渐变。要在此类工况下提高仿真稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`。

### **Spool travel vector** — 阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认） | vector

控制构件行程距离的向量。正值使阀门打开。此向量中的值与 **Orifice area vector** 参数中的值一一对应。这些值必须从 0 开始递增。该模块对这些点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Orifice area vector** — 阀门开口面积值 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356]` `m^2`（默认） | vector

用于开口面积表格参数化的阀门面积值向量。此向量中的值与 **Spool travel vector** 参数中的元素一一对应。此向量的第一个元素是泄漏面积，最后一个元素是最大阀门面积。该模块对这些点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | positive scalar

液压结构的流量损失。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为以下之一：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认） | positive scalar

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为以下之一：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `on`（默认） | `off`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **Spool travel vector, ds** — 表格阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认） | vector

控制构件行程距离的向量。阀芯行程向量与 **Pressure drop vector, dp** 参数一起形成 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴，该参数为 3-D 因变量。正位移对应于阀门打开。这些值从 0 开始递增。该模块对这些点进行线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Pressure drop vector, dp** — 表格压降值 `[.3, .5, .7]` `MPa`（默认） | vector

体积流量的压降值向量。压降向量与 **Spool travel vector, ds** 参数一起形成 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴，该参数为 3-D 因变量。这些值必须递增。该模块对这些点进行线性插值

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data -Volumetric flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 给定阀芯行程和压降下的体积流量 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `m^3/s`（默认） | matrix

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Mass flow rate table, mdot(ds,dp)** — 给定阀芯行程和压降下的质量流量 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] kg/s`（默认） | matrix

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow temperature** — 指定质量流量数据时的温度 `293.15 K`（默认） | positive scalar

指定表格质量流量数据时的温度。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow pressure** — 指定质量流量表格数据时的压力 `0.101325 MPa`（默认） | positive scalar

指定表格质量流量数据时的压力。该模块使用此参数计算第三个参考参数，即参考密度。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Cross-sectional area at ports A and B** — 守恒端口处的阀门面积 `0.01` `m^2`（默认） | positive scalar

端口 **A** 和 **B** 处的横截面积。该模块在压力-流量方程中使用此面积来确定通过阀门的体积流量。

#### 依赖关系

要启用此参数，请将 **Orifice parametrization** 设置为以下之一：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### 故障

### **2-Way Directional Valve Area fault** — 对阀芯位置故障建模的选项 `Add fault`

在模块中对阀芯位置故障建模的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀门面积将基于 **Spool position when faulted** 参数中指定的值设置。

### **Spool position when faulted** — 故障时的阀门特性 `Positive`（默认） | `Negative` | `Maintain last value`

故障时的阀门阀芯位置。您可以选择当阀芯处于正位置、负位置或故障触发时的位置时使阀门卡滞。

#### 依赖关系

要启用此参数，请单击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

2-Way Directional Valve (TL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Simscape 故障简介。

### R2022b：右键单击模块以查看开度特性图

您可以通过右键单击模块并选择 **Fluids** > **Plot Valve Characteristics**，查看每个孔口的面积或体积流量随阀芯位置变化的图。

## 描述

thermal liquid 网络中的二通方向阀

2-Way Directional Valve (TL) 模块表示二通阀，例如截止阀。使用此模块可仿真响应系统另一部分压力的减流控制元件。

该模块使用可变孔口控制端口 **A** 和 **B** 之间的流量。端口 **S** 处的 physical signal 触发阀芯运动以打开或关闭阀门。有关该模块如何计算通过可变孔口的流量的更多详细信息，请参阅 Orifice (TL)。

### 孔口参数化

您可以线性地或使用表格数据参数化阀门开度。

**线性**

当您将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 时，开口面积是阀芯行程距离的线性函数。

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

其中

- *Aorifice* 是开口面积。
- *ΔS* 是端口 **S** 处的阀芯行程距离输入。ΔS=S−Smax+ΔSmax。
- *ΔSmax* 是 **Spool travel between closed and open orifice** 参数的值。
- *ALeak* 是 **Leakage area** 参数的值。
- *Amax* 是 **Maximum orifice area** 参数的值。

注意图中从 *ALeak* 到 *Amax* 的线性缩放。

当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真的数值稳健性。如果 **Smoothing factor** 参数非零，该模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关更多信息，请参阅 Numerical Smoothing。

**表格数据**

当您将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel` 时，该模块使用 **Spool travel vector** 和 **Orifice area vector** 参数，通过插值定义 *Aorifice* 和 *ΔS* 之间的关系。*Aleak* 和 *Amax* 分别是 **Orifice area vector** 参数的第一个和最后一个参数。

当您将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 时，该模块使用 **Volumetric flow rate table, q(ds,dp)**、**Pressure drop vector, dp** 和 **Spool travel vector, ds** 参数来定义体积流量 *q(**ΔS**,**p**)*。

当您将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. opening and pressure drop` 时，该模块直接根据阀芯位置和阀门两端压降计算质量流量。这三个变量之间的关系可以是非线性的，它由 **Spool travel vector, ds**、**Pressure drop vector, dp** 和 **Mass flow rate table, mdot(ds,dp)** 参数中的表格数据给出。

### 可视化孔口开口

要可视化阀芯偏移和位移，请右键单击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示阀门开口面积或体积流量随阀芯位置变化的关系。

要在更改模块参数后更新数据，请单击图窗中的 **Reload Data**。

下图显示了具有以下设置的阀门配置：

- **Spool position at maximum orifice area** 设置为 `2e-3` m。
- **Spool travel between closed and open orifice** 设置为 `6e-3` m。

所有其他参数均为默认值。

每个孔口的面积与阀芯位置关系图。

### 故障

要对故障建模，请在 **故障** 部分中，单击您要建模的故障旁边的 **添加故障** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Introduction to Simscape Faults。

您可以使用 **发生故障时的滑阀位置** 参数选择故障类型：

- `Negative` — 该模块将阀冻结在其最小值。表中显示了根据 **节流孔参数化** 参数的设置，该模块使用哪个值。

  | **节流孔参数化** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **泄漏面积** 参数 |
  | `Tabulated data - Area vs. spool travel` | **节流孔面积向量** 参数的第一个元素 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **体积流量表, q(ds,dp)** 参数的第一行 |
  | `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **质量流量表, mdot(ds,dp)** 参数的第一行 |
- `Positive` — 该模块将阀冻结在其最大值。表中显示了根据 **节流孔参数化** 参数的设置，该模块使用哪个值。

  | **节流孔参数化** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **最大开口面积** 参数 |
  | `Tabulated data - Area vs. spool travel` | **节流孔面积向量** 参数的最后一个元素 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **体积流量表, q(ds,dp)** 参数的最后一行 |
  | `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **质量流量表, mdot(ds,dp)** 参数的最后一行 |
- `Maintain last value` — 该模块将阀冻结在其最后一个值。表中显示了根据 **节流孔参数化** 参数的设置，该模块使用哪个值。

  | **节流孔参数化** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | 触发发生时的阀开口面积 |
  | `Tabulated data - Area vs. spool travel` | 触发发生时的阀开口面积 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | 当前位置 |
  | `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | 当前位置 |

  当您将 **节流孔参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop` 时，在阀冻结后，体积流量或质量流量会根据阀中的压力变化继续变化。

由于在阀面积极值处进行数值平滑，在线性参数化中，该模块使用的最小面积大于 **泄漏面积**，最大面积小于 **最大节流孔面积**，且与 **平滑因子** 值成比例。有关详细信息，请参阅 Numerical Smoothing。
