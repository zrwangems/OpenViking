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

### **A** — 等温液体端口

液体进入或离开阀的点。

### **B** — 等温液体端口

液体进入或离开阀的点。
### 输入

### **S** — 物理信号，单位为 m

孔口开度，单位为 m，以物理信号形式返回。正信号打开孔口。

## 参数

### **Orifice parameterization** — 孔口开度建模方法 `Linear - area vs. control member position`（默认）| `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

孔口开度的建模方法。开度可以通过线性方式参数化，即将开度面积与控制构件位置相关联；也可以通过用户提供的数据将孔口开度面积与控制构件位置相关联；或者通过一组数据数组将阀流量与控制构件位置和阀压降相关联。

### **Control member travel between closed and open valve** — 控制构件最大行程 `5e-3 m`（默认）| 正标量

使孔口完全打开的控制构件行程。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member travel`。

### **Maximum orifice area** — 最大孔口横截面积 `8e-5 m^2`（默认）| 正标量

孔口完全打开时的横截面积。此参数在仿真期间用作面积-压力计算的上限。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member travel`。

### **Control member position at closed valve** — 控制构件偏移量 `0 m`（默认）| 正标量

孔口完全打开时的控制构件偏移量。正的、非零值表示孔口部分关闭。负的、非零值表示孔口重叠，在由端口 **S** 处的物理信号设定的初始位移下保持打开。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member travel`。

### **Control member position vector** — 控制构件行程距离向量 `[0, .002, .007]`（默认）| 1×*n* 向量

用于孔口开度面积表格参数化的孔口开度距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。元素按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Orifice area vector** — 开度面积向量 `[1e-09, 4e-09, 1e-05] m^2`（默认）| 1×*n* 向量

用于阀开度面积表格参数化的阀开度面积向量。向量元素必须与 **Control member position vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Control member position vector, s** — 控制构件位移向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于体积流量表格参数化的控制构件位置向量。控制构件位置向量与 **Pressure drop vector, dp** 参数一起构成三维因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。正位移对应于阀打开。值按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Pressure drop vector, dp** — 压差值向量 `[.3, .5, .7] MPa`（默认）| 1×*n* 向量

用于阀开度面积表格参数化的阀开度面积向量。压降向量与 **Control member position vector, s** 参数一起构成三维因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认）| *M*×*N* 数组

基于压降和滑阀行程距离独立值的体积流量数组。*M* 和 *N* 是对应向量的尺寸：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数量。
- *N* 是 **Control member position vector, s** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Set orifice pressure differential** — 补偿阀操作的阈值 `0.6 MPa`（默认）| 标量

触发阀打开或关闭的压降大小。

### **Pressure compensator valve regulation range** — 压力补偿阀的压力工作区域 `0.1 MPa`（默认）| 标量

阀的工作压力范围。压力调节范围介于 **Set orifice pressure differential** 与最大阀工作压力之间。

### **Pressure compensator valve maximum area** — 压力补偿阀完全打开时的面积 `1.5 * 8e-5 m^2`（默认）| 正标量

阀完全打开时的横截面积。此参数在仿真期间用作面积-压力计算的上限。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。这通过保持流量连续性来帮助数值稳定性。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

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

Pressure-Compensated Flow Control Valve (IL) 模块通过串联连接的 Pressure Compensator Valve (IL) 经由 Orifice (IL) 模块提供恒压流量控制。当孔口上的控制压力 *p*A – *p*B 达到或超过 **Set orifice pressure differential** 时，压力补偿器组件中的减压阀开始关闭，从而维持孔口中的压力。对于需要排气或将流体重新导向系统另一部分的系统，请参阅 Pressure-Compensated 3-Way Flow Control Valve (IL) 模块。

阀的打开和关闭由端口 **S** 处接收的物理信号控制。正信号打开阀。

**流量控制阀示意图**

### 数值平滑的面积和压力

当孔口参数化为线性时，您可以通过将 **Smoothing factor** 参数调整为小于 1 的非零值，在孔口面积和阀压力范围的极值处保持数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会对所有计算的面积和压力应用平滑函数，但它主要在这些范围的极值处影响仿真。

如果启用平滑，模块会在 **Leakage area** 和 **Maximum orifice area** 参数之间平滑地饱和孔口面积，并应用平滑函数。模块会在 **Set orifice pressure differential** 参数与 **Set orifice pressure differential** 和 **Pressure compensator valve regulation range** 参数之和之间平滑地饱和阀压力。

有关详细信息，请参阅数值平滑。

### 孔口参数化

将 **Orifice parameterization** 设置为：

- `Linear - area vs. control member position` 假定滑阀位置与孔口开度面积之间为线性关系。
- `Tabulated data - Area vs. control member position` 在用户提供的孔口开度面积与控制构件位置之间的数据中进行插值，可能为非线性关系。
- `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 直接从用户提供的控制构件位置、孔口压降和孔口体积流量之间的数据中插值孔口体积流量。
