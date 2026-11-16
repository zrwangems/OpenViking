---
type: simulink-block
title: 'Pressure-Compensated Flow Control Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'pressurecompensatedflowcontrolvalveil'
documentation_source_path: 'ref/pressurecompensatedflowcontrolvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Compensated Flow Control Valve (IL)

## 端口

### 守恒

### **A** — 液体端口（等温液体）

液体进入或离开阀的点。

### **B** — 液体端口（等温液体）

液体进入或离开阀的点。
### 输入

### **S** — 物理信号，单位为 m 的物理信号

以 m 表示的孔口开度，以物理信号形式返回。正信号打开孔口。

## 参数

### **Orifice parameterization** — 孔口开度的建模方法 `Linear - area vs. control member position` (default) | `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

对孔口开度建模的方法。开度可以是线性参数化的，将开度面积与控制构件位置相关联；也可以由用户提供的数据参数化，这些数据将孔口开度面积与控制构件位置相关联；或者由一组数据参数化，这些数据将阀流量与控制构件位置和阀压降相关联。

### **Control member travel between closed and open valve** — 最大控制构件行程 `5e-3 m` (default) | positive scalar

使孔口完全打开的控制构件行程。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member travel`。

### **Maximum orifice area** — 最大孔口横截面积 `8e-5 m^2` (default) | positive scalar

孔口在其完全打开位置处的横截面积。此参数用作仿真期间面积-压力计算的上限。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member travel`。

### **Control member position at closed valve** — 控制构件偏移 `0 m` (default) | positive scalar

孔口完全打开时的控制构件偏移量。正的、非零值表示部分关闭的孔口。负的、非零值表示重叠孔口，该孔口在由端口 **S** 处物理信号设定的初始位移下保持打开。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member travel`。

### **Control member position vector** — 控制构件行程距离向量 `[0, .002, .007]` (default) | 1-by-*n* vector

用于孔口开度面积表格参数化的孔口开度距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。元素按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Orifice area vector** — 开度面积向量 `[1e-09, 4e-09, 1e-05] m^2` (default) | 1-by-*n* vector

用于阀开度面积表格参数化的阀开度面积向量。向量元素必须与 **Control member position vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Control member position vector, s** — 控制构件位移向量 `[0, .002, .004, .007, .017] m` (default) | 1-by-*n* vector

用于体积流量表格参数化的控制构件位置向量。控制构件位置向量与 **Pressure drop vector, dp** 参数一起构成 3-D 因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。正位移对应阀打开。值按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Pressure drop vector, dp** — 压差向量 `[.3, .5, .7] MPa` (default) | 1-by-*n* vector

用于阀开度面积表格参数化的阀开度面积向量。压降向量与 **Control member position vector, s** 参数一起构成 3-D 因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。值按升序列出，且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s` (default) | *M*-by-*N* array

基于压降和滑阀行程距离的独立值的体积流量数组。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数。
- *N* 是 **Control member position vector, s** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Set orifice pressure differential** — 补偿阀操作的阈值 `0.6 MPa` (default) | scalar

触发阀打开或关闭的压降大小。

### **Pressure compensator valve regulation range** — 压力补偿阀的压力工作区域 `0.1 MPa` (default) | scalar

阀的工作压力范围。压力调节范围位于 **Set orifice pressure differential** 与最大阀工作压力之间。

### **Pressure compensator valve maximum area** — 完全打开的压力补偿阀面积 `1.5 * 8e-5 m^2` (default) | positive scalar

阀在其完全打开位置处的横截面积。此参数用作仿真期间面积-压力计算的上限。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2` (default) | positive scalar

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持在指定的泄漏面积。这通过保持流量连续性来帮助提高数值稳定性。

### **Discharge coefficient** — 排放系数 `0.64` (default) | positive scalar

用于修正理论流量中排放损失的修正系数。

### **Critical Reynolds number** — 层流的上限雷诺数 `150` (default) | positive scalar

通过阀的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01` (default) | positive scalar in the range [0,1]

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为大于零且小于 1 的值，以提高这些工况下仿真的稳定性。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的带压力调节的流量控制

Pressure-Compensated Flow Control Valve (IL) 模块通过串联连接的 Pressure Compensator Valve (IL)，经由 Orifice (IL) 模块提供恒压流量控制。当孔口上的控制压力 *p*A – *p*B 达到或超过 **Set orifice pressure differential** 时，压力补偿器组件中的减压阀开始关闭，从而维持孔口中的压力。对于需要将流体排放或重新引导到系统另一部分的系统，请参阅 Pressure-Compensated 3-Way Flow Control Valve (IL) 模块。

阀的打开和关闭由端口 **S** 接收的物理信号控制。正信号打开阀。

**流量控制阀示意图**

### 数值平滑后的面积与压力

当孔口参数化为线性时，可以通过将 **Smoothing factor** 参数调整为大于零且小于 1 的值，在孔口面积和阀压力范围的极值处保持数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会对所有计算得到的面积和压力应用平滑函数，但它主要在这些范围的极值处影响仿真。

如果启用平滑，模块会在 **Leakage area** 和 **Maximum orifice area** 参数之间平滑饱和孔口面积，并应用平滑函数。模块会在 **Set orifice pressure differential** 参数与 **Set orifice pressure differential** 和 **Pressure compensator valve regulation range** 参数之和之间平滑饱和阀压力。

更多信息，请参阅数值平滑。

### 孔口参数化

将 **Orifice parameterization** 设置为：

- `Linear - area vs. control member position`
  假定滑阀位置与孔口开度面积成线性关系。
- `Tabulated data - Area vs. control member
  position` 使用用户提供的数据，在孔口开度面积与控制构件位置之间进行插值，并可能采用非线性关系。
- `Tabulated data - Volumetric flow rate vs. control member
  position and pressure drop` 直接根据用户提供的数据，在控制构件位置、孔口压降和孔口体积流量之间对孔口体积流量进行插值。
