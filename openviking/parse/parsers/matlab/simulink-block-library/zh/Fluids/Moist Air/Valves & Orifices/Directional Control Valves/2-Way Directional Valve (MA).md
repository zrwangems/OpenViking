---
type: simulink-block
title: '2-Way Directional Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Directional Control Valves'
documentation_page: '2waydirectionalvalvema'
documentation_source_path: 'ref/2waydirectionalvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-Way Directional Valve (MA)

## 端口

### 守恒

### **A** — 湿空气入口或出口湿空气

与阀入口或出口相关联的湿空气守恒端口。

### **B** — 湿空气入口或出口湿空气

与阀入口或出口相关联的湿空气守恒端口。

### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移相关联的物理信号，单位为 m。正值使阀打开。

## 参数

### **Valve parameterization** — 可变或恒定孔口参数化 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据孔口压差计算质量流量，或根据质量流量计算压差的方法。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

### **Spool position at maximum orifice area** — 最大面积时的阀芯偏移 `5e-3` `m`（默认）| 正标量

阀完全打开时阀芯行程构件的位置。默认值表示零重叠系统。正非零值表示欠重叠或部分关闭系统。负非零值表示重叠系统，其中阀在一段位移范围内保持打开。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `5e-3` `m`（默认）| 正标量

阀打开面积最大时的阀芯偏移。

#### 依赖

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Spool travel vector** — 阀芯位置向量 `[0, .003, .006, .009, .012, .015] m`（默认）| 1-by-*n* 向量

用于表格化孔口参数化的阀芯位置向量。向量元素与 **Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的值一一对应。

#### 依赖

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 与最大打开组件对应的 *Cv* 系数 `4`（默认）| 正标量

当孔口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量在压差驱动下蒸气穿过阻力元件的容易程度。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 与构件位置向量中的值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1-by-*n* 向量

*Cv* 流量系数向量。每个系数对应于 **Spool travel vector** 参数中的一个值。此参数衡量在压差驱动下蒸气穿过阻力元件的容易程度。向量大小必须与 **Spool travel vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在该比值处首次发生阻塞。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 与最大打开组件对应的 *Kv* 系数 `3.6`（默认）| 正标量

当孔口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量在压差驱动下蒸气穿过阻力元件的容易程度。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 与构件位置向量中的值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1-by-*n* 向量

*Kv* 流量系数向量。每个系数对应于 **Spool travel vector** 参数中的一个值。此参数衡量在压差驱动下蒸气穿过阻力元件的容易程度。向量大小必须与 **Spool travel vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum sonic conductance** — 与最大打开组件对应的声导 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 指定的控制信号为 `1` 且可用于流动的横截面积最大时的声导值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流动首次阻塞时下游与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到局部声速时的压力比。压力比是出口压力除以入口压力。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确计算亚声速流态中质量流量的经验值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 与控制构件位置向量中的值对应的声导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声导向量。每个声导对应于 **Spool travel vector** 参数中的一个值。向量大小必须与 **Spool travel vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 与控制构件位置向量中的值对应的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应于 **Spool travel vector** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到局部声速。向量大小必须与 **Spool travel vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum orifice area** — 最大孔口开口面积 `1e-4 m^2`（默认）| 正标量

孔口完全打开时的孔口面积。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Orifice area vector** — 孔口开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1-by-*n* 向量

用于孔口面积表格化参数化的孔口面积值向量。此向量中的值与 **Spool travel vector** 参数中的元素一一对应。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

实际流量与理想流量之比。此参数考虑了孔口方程中未捕获的实际损失。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

孔口关闭时与打开时的流量之比。

#### 依赖

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入一层逐渐变化。将此参数设置为大于零且小于一的值，以提高这些区域中仿真的稳定性。

#### 依赖

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间过渡时的孔口出口压力与孔口入口压力之比。压力损失在层流中与质量流量成线性关系，在湍流中成二次关系。

### **Cross-sectional area at ports A and B** — 阀端口面积 `0.01` m^2（默认）| 正标量

孔口端口 **A** 和 **B** 的面积。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的二通方向控制阀

2-Way Directional Valve (MA) 模块表示一个具有两个端口 **A** 和 **B** 以及一条流路 **A**–**B** 的阀。该路径穿过一个宽度可变的孔口。端口 **S** 指定的输入信号控制阀芯位置。当阀芯覆盖孔口开口时，阀关闭。有关模块如何计算通过可变孔口的流量的更多详细信息，请参阅 Orifice (MA)。

### 阀参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量在特定压差驱动下湿空气流动的容易程度。
- `Kv flow coefficient` — 流量系数 *Kv*，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量在特定压差驱动下湿空气流动的容易程度。
- `Sonic conductance` — 阻力元件在稳态下的声导决定模块参数化。声导衡量湿空气在*阻塞*时流动的容易程度，阻塞是流速达到局部声速的状态。当下游与上游压力之比达到称为*临界压力比*的临界值时发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 开口特性

流量特性将阀的开口与产生该开口的输入（通常是阀芯行程）联系起来。根据 **Valve parameterization** 参数的设置，模块将开口表示为声导、流量系数或限流面积。控制输入是孔口打开分数，它是端口 **S** 指定的阀芯位移的函数。

流量特性通常在稳态下给出，入口处于恒定且受精确控制的压力。流量特性仅取决于阀，可以是线性或非线性的。要捕获流量特性，请使用 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量是孔口打开分数的线性函数。随着打开分数增加，流量能力的度量从指定最小值缩放到指定最大值。
- `Tabulated` — 流量能力的度量是孔口打开分数的一般函数，可以是线性或非线性的。该函数以表格形式指定，自变量由 **Opening fraction vector** 指定。

### 可视化孔口开口

要可视化阀芯偏移和位移，请右键单击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示声导、*Kv* 流量系数、*Cv* 流量系数或孔口面积随阀芯位置的变化。

更改模块参数后要更新数据，请在图窗中点击 **Reload Data**。

此图显示具有默认值的阀配置。

每个孔口的面积与阀芯位置关系图。

### 假设和限制

- **Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于含有高水平痕量气体的湿空气，或者正在对空气以外的流体进行建模，则可能需要将该声导按混合物比重的平方根进行缩放。
- 此模块不对超声速流进行建模。
- 阀与环境之间没有热交换。
