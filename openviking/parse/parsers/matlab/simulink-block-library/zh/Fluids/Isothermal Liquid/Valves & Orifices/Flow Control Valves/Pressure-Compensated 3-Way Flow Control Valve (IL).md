---
type: simulink-block
title: 'Pressure-Compensated 3-Way Flow Control Valve (IL)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 阀液体端口，等温液体
  direction: conserving
- name: B
  summary: 节流孔液体端口，等温液体
  direction: conserving
- name: R
  summary: 减压阀液体端口，等温液体
  direction: conserving
- name: S
  summary: 物理信号，单位为 m，物理信号
  direction: input
```

### 守恒端口

### **A** — 阀液体端口，等温液体

三通阀的液体进入或出口端口。

### **B** — 节流孔液体端口，等温液体

节流孔的液体进入或出口端口。

### **R** — 减压阀液体端口，等温液体

减压阀的液体出口端口。
### 输入

### **S** — 物理信号，单位为 m，物理信号

节流孔开度，单位为 m，设定为物理信号。
## 参数
```yaml
parameters:
- name: Orifice parameterization
  summary: 节流孔开度的建模方法 Linear - area vs. control member position（默认）| Tabulated data - Area vs. control member position | Tabulated
    data - Volumetric flow rate vs. control member position and pressure drop
  group: ''
- name: Control member position at closed orifice
  summary: 控制构件偏移量 0 m（默认）| 标量
  group: ''
- name: Control member travel between closed and opened orifice
  summary: 最大控制构件行程 5e-3 m（默认）| 正标量
  group: ''
- name: Maximum orifice area
  summary: 最大节流孔横截面积 8e-5 m^2（默认）| 正标量
  group: ''
- name: Control member position vector
  summary: 开度位置向量 [0, .002, .007] m（默认）| 1×*n* 向量
  group: ''
- name: Orifice area vector
  summary: 开度面积向量 [1e-09, 4e-09, 1e-05] m^2（默认）| 1×*n* 向量
  group: ''
- name: Control member position vector, s
  summary: 控制构件位置向量 [0, .002, .004, .007, .017] m（默认）| 1×*n* 向量
  group: ''
- name: Pressure drop vector, dp
  summary: 压差值向量 [.3, .5, .7] MPa（默认）| 1×*n* 向量
  group: ''
- name: Volumetric flow rate table, q(s,dp)
  summary: 体积流量值数组 [1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s（默认）|
    *M*×*N* 数组
  group: ''
- name: Set orifice pressure differential
  summary: 补偿阀操作的阈值 0.6 MPa（默认）| 正标量
  group: ''
- name: Pressure compensator valve regulation range
  summary: 压力补偿阀完全打开时的面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Pressure compensator valve maximum area
  summary: 压力补偿阀的压力工作区域 0.1 MPa（默认）| 标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的正标量
  group: ''
```

### **Orifice parameterization** — 节流孔开度的建模方法 `Linear - area vs. control member position`（默认）| `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

节流孔开度的建模方法。开度可以通过线性参数化建模，即将开度面积与控制构件位置关联；通过用户提供的数据将节流孔开度面积与控制构件位置关联；或通过一组数据将阀流量与控制构件位置和阀压降关联。

### **Control member position at closed orifice** — 控制构件偏移量 `0 m`（默认）| 标量

节流孔完全打开时的控制构件偏移量。正值且非零表示节流孔部分关闭。负值且非零表示节流孔重叠，在由端口 **S** 处的物理信号设定的初始位移下保持打开。

### **Control member travel between closed and opened orifice** — 最大控制构件行程 `5e-3 m`（默认）| 正标量

使节流孔完全打开的控制构件行程。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member position`。

### **Maximum orifice area** — 最大节流孔横截面积 `8e-5 m^2`（默认）| 正标量

节流孔在其完全打开位置时的横截面积。此参数用作仿真期间面积-压力计算的上限。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. control member position`。

### **Control member position vector** — 开度位置向量 `[0, .002, .007] m`（默认）| 1×*n* 向量

用于节流孔开度面积表格参数化的节流孔开度距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。元素按升序排列，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Orifice area vector** — 开度面积向量 `[1e-09, 4e-09, 1e-05] m^2`（默认）| 1×*n* 向量

用于阀开度面积表格参数化的阀开度面积向量。向量元素必须与 **Control member position vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Control member position vector, s** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于体积流量表格参数化的控制构件位置向量。控制构件位置向量与 **Pressure drop vector, dp** 参数一起构成三维因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。正位移对应于阀打开。值按升序排列，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Pressure drop vector, dp** — 压差值向量 `[.3, .5, .7] MPa`（默认）| 1×*n* 向量

用于阀开度面积表格参数化的阀开度面积向量。压降向量与 **Control member position vector, s** 参数一起构成三维因变量 **Volumetric flow rate table, q(s,dp)** 参数的独立轴。值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认）| *M*×*N* 数组

基于压降和滑阀行程距离独立值的体积流量数组。*M* 和 *N* 是对应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中的元素数量。
- *N* 是 **Control member position vector, s** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Set orifice pressure differential** — 补偿阀操作的阈值 `0.6 MPa`（默认）| 正标量

触发阀打开或关闭的压差大小。

### **Pressure compensator valve regulation range** — 压力补偿阀完全打开时的面积 `1e-4 m^2`（默认）| 正标量

阀在其完全打开位置时的横截面积。此参数用作仿真期间面积-压力计算的上限。

### **Pressure compensator valve maximum area** — 压力补偿阀的压力工作区域 `0.1 MPa`（默认）| 标量

阀的工作压力范围。压力调节范围介于 **Set orifice pressure differential** 与最大阀工作压力之间。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

考虑理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的三通流量控制

Pressure-Compensated 3-Way Flow Control Valve (IL) 模块对恒压流量控制进行建模。当控制压力 *p*A – *p*B 达到或超过 **Set orifice pressure differential** 时，底层补偿阀的溢流组件打开以维持模块中的压力。

流量控制阀的打开和关闭由端口 **S** 处接收的物理信号控制，该信号决定底层节流孔模块的面积。正信号打开阀。端口 **R** 将液体排放到网络的另一部分。

有关不带排放的压力补偿流量控制，请参见 Pressure-Compensated Flow Control Valve (IL) 模块。

### 节流孔参数化

您可以通过 **Orifice parameterization** 设置选择阀模型：

- `Linear - area vs. control member position` 是一种解析公式，假设阀开度面积与阀控制构件呈线性关系。
- `Tabulated data - Area vs. control member position` 是用户提供的数据表，将节流孔开度面积与控制构件位置关联。模块在数据点之间使用线性插值进行查询，对于超出表格边界的点使用最近邻外推。
- `Tabulated data - Volumetric flow rate vs. control member position and pressure drop` 是用户提供的数据表，将控制构件位置、节流孔压降和节流孔体积流量关联。模块在数据点之间使用线性插值进行查询，对于超出表格边界的点使用最近邻外推。

### 数值平滑的面积和压力

当节流孔参数化为线性时，您可以通过将 **Smoothing factor** 参数调整为小于 1 的非零值，在节流孔面积和阀压力范围的极值处保持数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会对所有计算的面积和压力应用平滑函数，但它主要在这些范围的极值处影响仿真。

如果启用平滑，模块会在 **Leakage area** 和 **Maximum orifice area** 参数之间平滑饱和节流孔面积。模块会在 **Set orifice pressure differential** 参数与 **Set orifice pressure differential** 和 **Pressure compensator valve regulation range** 参数之和之间平滑饱和阀压力。

有关更多信息，请参见 Numerical Smoothing。

### 模块原理图

Pressure-Compensated 3-Way Flow Control Valve (IL) 由 Pressure Compensator Valve (IL) 和 Orifice (IL) 模块构成。

**三通流量控制阀原理图**
