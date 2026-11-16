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

### 守恒

### **A** — 液体端口，等温液体

等温液体守恒端口。

### **B** — 液体端口，等温液体

等温液体守恒端口。
### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移相关联的物理信号，单位为 m。正值会使阀门打开。

## 参数

### 模型参数化

### **孔口参数化** — 开口面积关系 `Linear - area vs. spool travel`（默认） | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

模块用于计算阀门流通面积的方法。要了解更多信息，请参阅孔口参数化。

### **最大孔口面积处的阀芯位置** — 最大面积处的阀芯偏移 `5e-3` `m`（默认） | 正标量

阀门完全打开时阀芯行程部件的位置。默认值表示零开口系统。正值非零值表示正开口（或部分关闭）系统。负值非零值表示负开口系统，此时阀门在一段位移范围内保持打开。

### **关闭和打开孔口之间的阀芯行程** — 最大阀芯行程 `5e-3` `m`（默认） | 正标量

最大阀门开启面积处的阀芯偏移。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Linear - area vs. spool travel`。

### **最大孔口面积** — 完全打开阀门的面积 `1e-4` `m^2`（默认） | 正标量

仿真期间经历的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Linear - area vs. spool travel`。

### **泄漏面积** — 完全关闭位置时的阀门间隙面积 `1e-10` `m^2`（默认） | 正标量

阀门处于完全关闭位置时所有间隙的总和。模块会将任何小于此值的面积保持为指定的泄漏面积。此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Linear - area vs. spool travel`。

### **阀芯行程向量** — 阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认） | 向量

控制部件行程距离的向量。正值使阀门打开。此向量中的值与 **孔口面积向量** 参数中的值一一对应。这些值必须从 0 开始递增。模块对这些点进行线性插值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **孔口面积向量** — 阀门开口面积值 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356]` `m^2`（默认） | 向量

用于开口面积表格参数化的阀门面积值向量。此向量中的值与 **阀芯行程向量** 参数中的元素一一对应。此向量的第一个元素是泄漏面积，最后一个元素是最大阀门面积。模块对这些点进行线性插值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **阀芯行程向量, ds** — 表格阀芯开口距离值 `[0, .002, .004, .007, .017]` `m`（默认） | 向量

控制部件行程距离的向量。阀芯行程向量与 **压降向量, dp** 参数一起，为 3-D 因变量 **体积流量表, q(ds,dp)** 参数构成一个独立轴。正位移对应阀门打开。这些值从 0 开始递增。模块对这些点进行线性插值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **压降向量, dp** — 表格压降值 `[.3, .5, .7]` `MPa`（默认） | 向量

用于体积流量的压降值向量。压降向量与 **阀芯行程向量, ds** 参数一起，为 3-D 因变量 **体积流量表, q(ds,dp)** 参数构成一个独立轴。这些值必须为正且递增。模块对这些点进行线性插值

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **体积流量表, q(ds,dp)** — 给定阀芯行程和压降下的体积流量 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13]` `m^3/s`（默认） | 矩阵

*M*×*N* 体积流量矩阵，基于压降和阀芯行程距离的独立值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **阀芯行程向量, ds** 参数中的元素数。
- *N* 是 **压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **流量系数** — 流量系数 `0.64`（默认） | 正标量

液压结构的流量损失。Simscape™ Fluids™ 中阀门的默认流量系数为 0.64。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为以下任一项：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认） | 正标量

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为以下任一项：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### **平滑因子** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，当阀门处于接近打开和接近关闭位置时，它基于流量响应引入一层渐变变化。为提高在这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Linear - area vs. spool travel`。

### **压力恢复** — 是否考虑面积扩大时的压力增加 `on`（默认） | `off`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **端口 A 和 B 处的横截面积** — 守恒端口处的阀门面积 `inf` `m^2`（默认） | 正标量

端口 **A** 和 **B** 处的横截面积。模块在压力-流量方程中使用此面积来确定通过阀门的体积流量。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为以下任一项：

- `Tabulated data - Area vs. spool travel`
- `Linear - area vs. spool travel`

### 故障

### **2-Way Directional Valve 面积故障** — 对阀芯位置故障建模的选项 `Add fault`

对模块中的阀芯位置故障建模的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀门面积将根据 **发生故障时的阀芯位置** 参数中指定的值进行设置。

### **发生故障时的阀芯位置** — 故障阀门特性 `Positive`（默认） | `Negative` | `Maintain last value`

故障时的阀门阀芯位置。您可以选择阀门在阀芯处于正位置、负位置或故障触发时所在位置时卡住。

#### 依赖关系

要启用此参数，请单击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障界面进行故障建模

2-Way Directional Valve (IL) 模块现在支持 Simscape 故障界面。要了解更多信息，请参阅 Simscape 故障简介。

## 描述

等温液体系统中的二通流量控制阀

2-Way Directional Valve (IL) 模块表示一个二通阀，例如截止阀。使用此模块可对响应系统另一部分压力的减流控制元件进行仿真。

模块使用可变孔口来控制端口 **A** 和 **B** 之间的流量。端口 **S** 处的物理信号触发阀芯运动以打开或关闭阀门。有关模块如何计算通过可变孔口的流量的更多详细信息，请参阅 Orifice (IL)。

### 孔口参数化

您可以线性地或使用表格数据来参数化阀门开口。

**线性**

当您将 **孔口参数化** 设置为 `Linear - Area vs. spool travel` 时，开口面积是阀芯行程距离的线性函数。

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

其中

- *Aorifice* 是开口面积。
- *ΔS* 是端口 **S** 处的阀芯行程距离输入。ΔS=S−Smax+ΔSmax。
- *ΔSmax* 是 **关闭和打开孔口之间的阀芯行程** 参数的值。
- *ALeak* 是 **泄漏面积** 参数的值。
- *Amax* 是 **最大孔口面积** 参数的值。

请注意图中从 *ALeak* 到 *Amax* 的线性缩放。

在线性参数化中，当阀门处于接近打开或接近关闭位置时，您可以通过调整 **平滑因子** 参数来保持仿真的数值稳健性。如果 **平滑因子** 参数非零，模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关更多信息，请参阅数值平滑。

**表格**

当您将 **孔口参数化** 设置为 `Tabulated data - Area vs. spool travel` 时，模块使用 **阀芯行程向量** 和 **孔口面积向量** 参数，通过插值定义 *Aorifice* 与 *ΔS* 之间的关系。*Aleak* 和 *Amax* 分别是 **孔口面积向量** 参数的第一个和最后一个参数。

当您将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 时，模块使用 **体积流量表, q(ds,dp)**、**压降向量, dp** 和 **阀芯行程向量, ds** 参数来定义体积流量 *q(**ΔS**,**p**)*。

### 可视化孔口开度

要可视化阀芯偏移和位移，请右键单击该模块，然后选择 **Fluids** > **Plot Valve Characteristics**。该图显示阀门开口面积或体积流量随阀芯位置的变化。

更改模块参数后要更新数据，请在图形窗口中单击 **Reload Data**。

下图显示了具有以下配置的阀门：

- **最大孔口面积处的阀芯位置** 设置为 `2e-3` m。
- **关闭和打开孔口之间的阀芯行程** 设置为 `6e-3` m。

所有其他参数均为默认值。

每个孔口的面积与阀芯位置关系图。

### 故障

要对故障建模，请在 **故障** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Simscape 故障简介。

您可以通过 **发生故障时的阀芯位置** 参数选择故障类型：

- `Negative` — 模块将阀门冻结在其最小值。下表显示了根据 **孔口参数化** 参数的设置，模块使用哪个值。

  | **孔口参数化** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **泄漏面积** 参数 |
  | `Tabulated data - Area vs. spool travel` | **孔口面积向量** 参数的第一个元素 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **体积流量表, q(ds,dp)** 参数的第一行 |
- `Positive` — 阀门冻结在其最大值。下表显示了根据 **孔口参数化** 参数的设置，模块使用哪个值。

  | **孔口参数化** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | **最大开口面积** 参数 |
  | `Tabulated data - Area vs. spool travel` | **孔口面积向量** 参数的最后一个元素 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **体积流量表, q(ds,dp)** 参数的最后一行 |
- `Maintain last value` — 阀门冻结在其最后一个值。下表显示了根据 **孔口参数化** 参数的设置，模块使用哪个值。

  | **孔口参数化** 参数设置 | 冻结位置值 |
  | --- | --- |
  | `Linear - Area vs. spool travel` | 触发发生时的阀门开口面积 |
  | `Tabulated data - Area vs. spool travel` | 触发发生时的阀门开口面积 |
  | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | 当前位置 |

  当您将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 时，阀门冻结后，体积流量会继续根据阀门中的压力变化而变化。

由于阀门面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于 **泄漏面积**，最大值小于 **最大孔口面积**，其比例与 **平滑因子** 值成比例。有关更多信息，请参阅数值平滑。
