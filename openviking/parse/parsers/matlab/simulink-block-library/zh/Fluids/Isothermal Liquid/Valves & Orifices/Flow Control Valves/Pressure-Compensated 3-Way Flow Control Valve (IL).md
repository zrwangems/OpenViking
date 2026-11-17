---
type: simulink-block
title: 'Pressure-Compensated 3-Way Flow Control Valve (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'pressurecompensated3wayflowcontrolvalveil'
documentation_source_path: 'ref/pressurecompensated3wayflowcontrolvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Compensated 3-Way Flow Control Valve (IL)

## 端口

### 守恒

### **A** — 阀门液体端口，等温液体

三通阀的液体进入或离开端口。

### **B** — 孔口液体端口，等温液体

孔口的液体进入或离开端口。

### **R** — 减压阀液体端口，等温液体

减压阀的液体离开端口。
### 输入

### **S** — 物理信号，单位为 m 的物理信号

孔口开度，单位为 m，设置为物理信号。

## 参数

### **孔口参数化** — 孔口开度的建模方法 `Linear - area vs. control member position`（默认）| `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

孔口开度的建模方法。开度可以按线性方式进行参数化，即将开度面积与控制构件位置相关联；也可以由用户提供的数据进行参数化，这些数据将孔口开度面积与控制构件位置相关联；或者由将阀流量与控制构件位置及阀压降相关联的数据数组进行参数化。

### **孔口关闭时的控制构件位置** — 控制构件偏移 `0 m`（默认）| 标量

孔口完全打开时的控制构件偏移。正的非零值表示孔口部分关闭。负的非零值表示重叠孔口，该孔口在由端口 **S** 处的物理信号设定的初始位移下保持打开。

### **孔口从关闭到开启之间的控制构件行程** — 最大控制构件行程 `5e-3 m`（默认）| 正标量

使孔口完全打开的控制构件行程。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Linear - area vs. control member position`。

### **最大孔口面积** — 最大孔口横截面积 `8e-5 m^2`（默认）| 正标量

孔口在其完全打开位置时的横截面积。此参数用作仿真期间面积-压力计算的上限。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Linear - area vs. control member position`。

### **控制构件位置向量** — 开度位置向量 `[0, .002, .007] m`（默认）| 1-by-*n* 向量

用于孔口开度面积表格参数化的孔口开度距离向量。向量元素必须与 **孔口面积向量** 参数中的元素一一对应。元素按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Area vs. control member position`。

### **孔口面积向量** — 开度面积向量 `[1e-09, 4e-09, 1e-05] m^2`（默认）| 1-by-*n* 向量

用于阀开度面积表格参数化的阀开度面积向量。向量元素必须与 **控制构件位置向量** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Area vs. control member position`。

### **控制构件位置向量，s** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1-by-*n* 向量

用于体积流量表格参数化的控制构件位置向量。控制构件位置向量与 **压降向量，dp** 参数一起构成独立轴，用于 3-D 因变量 **体积流量表，q(s,dp)** 参数。正位移对应于阀打开。值按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **压降向量，dp** — 压差值的向量 `[.3, .5, .7] MPa`（默认）| 1-by-*n* 向量

用于阀开度面积表格参数化的阀开度面积向量。压降向量与 **控制构件位置向量，s** 参数一起构成独立轴，用于 3-D 因变量 **体积流量表，q(s,dp)** 参数。值按升序列出，且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **体积流量表，q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认）| *M*-by-*N* 数组

基于压降和阀芯行程独立值的体积流量数组。*M* 和 *N* 是相应向量的大小：

- *M* 是 **压降向量，dp** 参数中的元素数。
- *N* 是 **控制构件位置向量，s** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **设定孔口压差** — 补偿阀操作的阈值 `0.6 MPa`（默认）| 正标量

触发阀打开或关闭的压差大小。

### **压力补偿阀调节范围** — 完全打开的压力补偿阀面积 `1e-4 m^2`（默认）| 正标量

阀在其完全打开位置的横截面积。此参数用作仿真期间面积-压力计算的上限。

### **压力补偿阀最大面积** — 压力补偿阀的压力工作区域 `0.1 MPa`（默认）| 标量

阀的工作压力范围。压力调节范围介于 **设定孔口压差** 与最大阀工作压力之间。

### **泄漏面积** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。这通过保持流动连续性来帮助数值稳定性。

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正因子。

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的三通流量控制

Pressure-Compensated 3-Way Flow Control Valve (IL) 模块对恒压流量控制进行建模。当控制压力 *p*A – *p*B 达到或超过 **设定孔口压差** 时，底层补偿阀的泄压组件打开，以维持模块中的压力。

流量控制阀的打开和关闭由端口 **S** 处接收的物理信号控制，该信号决定底层孔口模块的面积。正信号打开阀。端口 **R** 将液体排放到网络的另一部分。

对于不带排放的压力补偿流量控制，请参阅 Pressure-Compensated Flow Control Valve (IL) 模块。

### 孔口参数化

您可以使用 **孔口参数化** 设置选择阀模型：

- `Linear - area vs. control member position` 是一种解析公式，假定阀开度面积与阀控制构件呈线性关系。
- `Tabulated data - Area vs. control member position` 是用户提供的数据表，将孔口开度面积与控制构件位置相关联。该模块在数据点之间采用线性插值进行查询，并对超出表边界的点使用最近邻外插。
- `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 是用户提供的数据表，将控制构件位置、孔口压降和孔口体积流量相关联。该模块在数据点之间采用线性插值进行查询，并对超出表边界的点使用最近邻外插。

### 数值平滑的面积和压力

当孔口参数化为线性时，您可以通过将 **平滑因子** 参数调整为小于 1 的非零值，在孔口面积和阀压力范围的极值处保持数值稳健性。如果 **平滑因子** 参数非零，则该模块会对所有计算得到的面积和压力应用平滑函数，但它主要影响这些范围极值处的仿真。

如果启用平滑，该模块会在 **泄漏面积** 和 **最大孔口面积** 参数之间平滑地饱和孔口面积。该模块会在 **设定孔口压差** 参数与 **设定孔口压差** 和 **压力补偿阀调节范围** 参数之和之间平滑地饱和阀压力。

有关详细信息，请参阅数值平滑。

### 模块示意图

Pressure-Compensated 3-Way Flow Control Valve (IL) 由 Pressure Compensator Valve (IL) 和 Orifice (IL) 模块构成。

**三通流量控制阀示意图**
