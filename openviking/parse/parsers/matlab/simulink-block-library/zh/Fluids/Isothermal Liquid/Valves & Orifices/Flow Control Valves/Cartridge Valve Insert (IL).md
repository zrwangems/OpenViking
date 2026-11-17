---
type: simulink-block
title: 'Cartridge Valve Insert (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'cartridgevalveinsertil'
documentation_source_path: 'ref/cartridgevalveinsertil.html'
language: zh-CN
chinese_source: worker-translation
---

# Cartridge Valve Insert (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口 等温液体
  direction: conserving
- name: B
  summary: 液体端口 等温液体
  direction: conserving
- name: X
  summary: 压力端口 等温液体
  direction: conserving
```

### 守恒端口

### **A** — 液体端口 等温液体

液体进入或出口端口。

### **B** — 液体端口 等温液体

液体进入或出口端口。

### **X** — 压力端口 等温液体

先导压力端口。通过端口 **X** 无质量流量。
## 参数
```yaml
parameters:
- name: Valve seat specification
  summary: 阀座几何形状 Conical（默认）| Custom
  group: ''
- name: Poppet diameter
  summary: 阀控制构件直径 0.01 m（默认）| 正标量
  group: ''
- name: Seat cone angle
  summary: 阀座开口角度 120 deg（默认）| 正标量
  group: ''
- name: Orifice parameterization
  summary: 节流孔面积计算方法 Linear - area vs. control member position（默认）| Tabulated data - Area vs. control member position | Tabulated
    data - Volumetric flow rate vs. control member position and pressure drop
  group: ''
- name: Poppet stroke
  summary: 阀芯最大位移 5e-3 m（默认）| 正标量
  group: ''
- name: Maximum orifice area
  summary: 最大节流孔横截面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Poppet position vector
  summary: 开口位置向量 [0, .002, .004, .007, .017] m（默认）| 1×*n* 向量
  group: ''
- name: Orifice area vector
  summary: 开口面积向量 [1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2（默认）| 1×*n* 向量
  group: ''
- name: Poppet position vector, s
  summary: 控制构件位置向量 [0, .002, .004, .007, .017] m（默认）| 1×*n* 向量
  group: ''
- name: Pressure drop vector, dp
  summary: 压差值向量 [.3, .5, .7] MPa（默认）| 1×*n* 向量
  group: ''
- name: Volumetric flow rate table, q(s,dp)
  summary: 体积流量值数组 [1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s（默认）|
    *M*×*N* 数组
  group: ''
- name: Port A poppet area
  summary: 端口 A 横截面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Port A poppet to port X pilot area ratio
  summary: 入口与先导端口面积比 0.5（默认）| 正标量
  group: ''
- name: Spring preload force
  summary: 阀芯中立位置时的弹簧力 25 N（默认）| 正标量
  group: ''
- name: Spring stiffness
  summary: 刚度常数 15e3 N/m（默认）| 正标量
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
- name: Valve opening time constant
  summary: 阀门时间常数 0.1 s（默认）| 正标量
  group: ''
```

### **Valve seat specification** — 阀座几何形状 `Conical`（默认）| `Custom`

阀座几何形状。该参数用于计算阀芯与阀座之间的开口面积。

### **Poppet diameter** — 阀控制构件直径 `0.01 m`（默认）| 正标量

阀控制构件的直径。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Conical`。

### **Seat cone angle** — 阀座开口角度 `120 deg`（默认）| 正标量

阀座开口的角度。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Conical`。

### **Orifice parameterization** — 节流孔面积计算方法 `Linear - area vs. control member position`（默认）| `Tabulated data - Area vs. control member position` | `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`

阀门开度通过以下三种方式之一计算，线性或通过表格数据：

- `Linear - area vs. control member position`：节流孔面积由与阀芯开启或关闭距离的线性关系确定。
- `Tabulated data - Area vs. control member position`：开口面积根据当前阀芯位置，从 **Poppet position vector** 和 **Orifice area vector** 插值得到。
- `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`。体积流量根据当前阀芯位置，直接从提供的 **Poppet position vector, s**、**Pressure drop vector, dp** 和 **Volumetric flow rate table, q(s,dp)** 参数插值得到。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`。

### **Poppet stroke** — 阀芯最大位移 `5e-3 m`（默认）| 正标量

阀芯最大位移。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`，并将 **Orifice parameterization** 设置为 `Linear - area vs. control member position`。

### **Maximum orifice area** — 最大节流孔横截面积 `1e-4 m^2`（默认）| 正标量

节流孔完全打开时的横截面积。该参数用作仿真期间面积-压力计算的上限。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`，并将 **Orifice parameterization** 设置为 `Linear - area vs. control member position`。

### **Poppet position vector** — 开口位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于节流孔开口面积表格参数化的节流孔开口位置向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Orifice area vector** — 开口面积向量 `[1e-09, 2.0352e-07, 4.0736e-05, .00011438, .00034356] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格参数化的阀门开口面积向量。向量元素必须与 **Poppet position vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`。

### **Poppet position vector, s** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认）| 1×*n* 向量

用于体积流量表格参数化的控制构件位置向量。阀芯行程向量与 **Pressure drop vector, dp** 参数构成独立轴，用于三维因变量 **Volumetric flow rate table, q(s,dp)** 参数。正位移对应阀门开启。值按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Pressure drop vector, dp** — 压差值向量 `[.3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格参数化的压降值向量。压降向量与 **Poppet position vector, s** 参数构成独立轴，用于三维因变量 **Volumetric flow rate table, q(s,dp)** 参数。值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Volumetric flow rate table, q(s,dp)** — 体积流量值数组 `[1.7e-05, 2e-05, 2.6e-05; .0035, .0045, .0053; .7, .9, 1.06; 1.96, 2.5, 3; 6, 7.7, 9.13] .* 1e-3 m^3/s`（默认）| *M*×*N* 数组

基于压降和阀芯行程距离独立值的体积流量矩阵。*M* 和 *N* 是对应向量的尺寸：

- *M* 是 **Poppet position vector, s** 参数中的元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Custom`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. control member position and pressure drop`。

### **Port A poppet area** — 端口 A 横截面积 `1e-4 m^2`（默认）| 正标量

端口 **A** 的横截面积。

### **Port A poppet to port X pilot area ratio** — 入口与先导端口面积比 `0.5`（默认）| 正标量

入口端口 **A** 与先导压力端口 **X** 的面积比。该值用于计算端口 **X** 处的力。该比值必须小于或等于 1。

### **Spring preload force** — 阀芯中立位置时的弹簧力 `25 N`（默认）| 正标量

阀芯处于中立位置时作用在阀芯上的弹簧力。该参数是一个阈值，当与端口 **X** 处的先导压力相加时，可平衡由于端口 **A** 和 **B** 处压力引起的阀门开启。

### **Spring stiffness** — 刚度常数 `15e3 N/m`（默认）| 正标量

弹簧刚度常数。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于该值的面积都会被饱和到指定的泄漏面积。这通过保持流动的连续性来有助于数值稳定性。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Valve seat specification** 设置为 `Conical`。
- **Valve seat specification** 设置为 `Custom`，且 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正因子。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Valve seat specification** 设置为 `Conical`。
- **Valve seat specification** 设置为 `Custom`，且 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Valve seat specification** 设置为 `Conical`。
- **Valve seat specification** 设置为 `Custom`，且 **Orifice parameterization** 设置为 `Linear - Area vs. control member position` 或 `Tabulated data - Area vs. control member position`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀门处于接近开启或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Valve seat specification** 设置为 `Conical`。
- **Valve seat specification** 设置为 `Custom`，且 **Orifice parameterization** 设置为 `Linear - Area vs. control member position`。

### **Valve opening time constant** — 阀门时间常数 `0.1 s`（默认）| 正标量

表征阀门从一个位置开启或关闭到另一个位置时，流体达到稳态条件所需时间的常数。该参数影响所建模的开启动态特性。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中的插装式流量控制阀

Cartridge Valve Insert (IL) 模块对等温液体网络中的插装式流量控制阀进行建模。阀座可指定为锥形，或指定为通过解析或表格公式参数化的自定义开口。当端口 **A** 和 **B** 处的组合压力超过 **Spring preload force** 和端口 **X** 处的压力时，阀门开启。

您可以将模块阀座几何形状指定为锥形或自定义。该阀座设置决定了构成模块的子组件。在两种配置中，**Port A poppet to port X pilot area ratio** 参数设置底层 Cartridge Valve Actuator 模块中的力比。

当您希望通过先导压力管路设置流量控制时，请使用 Cartridge Valve Insert (IL) 模块。对于由压差引起的流量控制，请使用 Pressure-Compensated 3-Way Flow Control Valve (IL) 或 Pressure-Compensated Flow Control Valve (IL) 模块；对于由外部物理信号控制阀门开启的情况，请使用 Poppet Valve (IL) 模块。

### 锥形阀座

锥形插装式阀芯是以下两个等温液体库模块的复合体：

- Poppet Valve (IL)
- Cartridge Valve Actuator (IL)

**锥形插装式阀芯示意图**

### 自定义阀座

自定义插装式阀芯是以下两个等温液体库模块的复合体：

- Orifice (IL)
- Cartridge Valve Actuator (IL)

**自定义插装式阀芯示意图**

在自定义配置中，您可以通过解析方式或数据集来参数化阀门开口。

**解析参数化**

通过将 **Orifice parameterization** 设置为 `Linear - area vs. control member position`，阀门开口面积与阀芯位置成线性比例。一旦端口 **A** 或 **B** 处的压力超过 **Spring preload force**，阀门开启，直到达到 **Maximum orifice area**。当阀门完全关闭时，一个小的 **Leakage area** 保持对流动开放，以维持网络中的数值连续性。

**表格参数化**

通过将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. control member position`，您可以基于开口面积和阀芯位置提供开口轮廓。模块在数据点之间使用线性插值进行查询，并对超出表格边界的点使用最近邻外推。

通过将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. control member position and pressure drop`，您可以将通过阀门的体积流量作为阀芯位置和阀门压降的参数化表格提供。模块在数据点之间使用线性插值进行查询，并对超出表格边界的点使用线性外推。体积流量乘以流体密度转换为质量流量。

### 开启动态特性

如果对开启动态特性进行建模，则会对所建模控制压力的流量响应引入一个滞后。*p*control 变为动态控制压力 *p*dyn；否则，*p*control 为稳态压力。动态控制压力的瞬时变化基于 **Opening time constant** *τ* 计算：

p˙dyn=pcontrol−pdynτ。

默认情况下，**Opening dynamics** 设置为 `Off`。

### 数值平滑的力和开度

当执行器接近完全伸出或完全缩回，且 **Orifice parameterization** 设置为 `Linear - area vs. control member position` 时，您可以通过调整模块 **Smoothing factor** 来保持仿真中的数值鲁棒性。平滑函数应用于执行器力和节流孔开度或面积，但主要在这些范围的极值处影响仿真。

开启阀门的归一化力为

F^=FA+FB−FPreload−FPilotkxstroke。

其中：

- *FA* 是端口 **A** 处的力。
- *FB* 是端口 **B** 处的力。
- *FPreload* 是 **Spring preload force**。
- *FPilot* 是端口 **X** 处的力。

当 **Valve seat specification** 设置为 `Conical` 时，模块将节流孔开启距离在 `0` 和最大节流孔开启距离之间平滑饱和。当 **Valve seat specification** 设置为 `Custom` 时，模块将阀门开口面积在 **Leakage area** 参数和 **Maximum orifice area** 参数之间平滑饱和。

有关详细信息，请参阅数值平滑。
