---
type: simulink-block
title: 'Pressure Reducing Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Valves and Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalvema'
documentation_source_path: 'ref/pressurereducingvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Reducing Valve (MA)

## 端口

### 守恒

### **A** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。

### **B** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。
### 输入

### **Ps** — 设定压力，Pa 物理信号

用于改变设定压力信号的输入端口。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

## 参数

### **Valve parameterization** — 阀门参数化模型 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据阀门两端压差计算质量流量，或根据质量流量计算压差的方法。

### **Opening characteristic** — 将控制信号转换为流量容量度量的方法 `Linear`（默认）| `Tabulated`

用于对所选流量容量度量进行参数化的方法。

### **Set pressure control** — 可变或恒定设定压力 `Constant`（默认）| `Controlled`

压力阈值是恒定还是可变。将此参数设置为 `Controlled` 会显示物理信号端口 **Ps**。

### **Set pressure (gauge)** — 设定压力 `0.1` MPa（默认）| 正标量

阀门压力阈值。当控制压力 *pA ̶ patm* 超过设定压力时，阀门开始打开。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Pressure regulation range** — 阀门工作范围 `0.1` MPa（默认）| 正标量

阀门工作范围。阀门在设定压力值处开始打开，并在 *pmax*（压力调节范围的终点）处完全打开，其中 *pmax = pset + prange*。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Opening pressure (gauge) vector** — 表压力向量 `[0.2 : 0.2 : 1.2] MPa`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的表压力值向量。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大开启组件的 *Cv* 系数 `4`（默认）| 正标量

当可用于流动的限制面积最大时 *Cv* 流量系数的值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应构件位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积最大时 *Kv* 流量系数的值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应构件位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum sonic conductance** — 对应最大开启组件的声速流导 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 处指定的控制信号为 `1` 且可用于流动的横截面积最大时，声速流导的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流区域质量流量的指数 `0.5`（默认）| 正标量

用于更准确计算亚声速流区域质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

只有在使用按不同参考值获得的声速流导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

只有在使用按不同参考值获得的声速流导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 对应控制构件位置向量中值的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声速流导向量。此向量中的值与 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 对应控制构件位置向量中值的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次阻塞时的临界压力比向量。临界压力比是流速达到当地声速时的下游压力与上游压力之比。此向量中的值与 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中首次发生阻塞。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum orifice area** — 最大阀门开口面积 `1e-4 m^2`（默认）| 正标量

阀门完全打开时的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Orifice area vector** — 阀门开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1×*n* 向量

用于蒸气阀门面积表格化参数化的孔口面积值向量。此向量中的值与 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

实际流量与理想流量之比。此参数考虑了孔口方程中未捕获的实际损失。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

阀门关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间过渡时的阀门出口压力与阀门入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Cross-sectional area at ports A and B** — 阀门端口面积 `0.01` m^2（默认）| 正标量

端口 **A** 和 **B** 的面积。

### **Opening dynamics** — 是否考虑阀门开启的流动响应 `off`（默认）| `on`

是否考虑阀门开启对流体系统的瞬态影响。选择此参数会通过在流量响应中引入一阶滞后来近似开启条件。

### **Opening time constant** — 阀门开启时间常数 `0.1` s（默认）| 正标量

用于计算开启动态滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2025a 中引入**

## 描述

湿空气网络中的减压阀

Pressure-Reducing Valve (MA) 模块对湿空气网络中的压力控制减压阀进行建模。当端口 **B** 处的压力小于设定压力时，阀门打开；当压力超过该值时，阀门关闭。控制压力可以是常量，或者，当您将 **Set pressure control** 设置为 `Controlled` 时，设定压力可以根据端口 **Ps** 处的输入信号变化。对于基于流体网络中另一位置的压力控制，请参阅 Pressure Compensator Valve (MA) 模块。

### 压力控制

当阀门中的压力 *pcontrol* 超过设定压力 *pset* 时，阀门关闭。当控制压力达到 *pset* + *prange* 时，阀门完全关闭，其中 *prange* 是 **Pressure regulation range** 参数的值。

对于线性参数化，模块计算阀门的开启分数 *λ*。当您将 **Set pressure control** 设置为 `Constant` 时，*λ* 为

λ=1−(1−fleak)(pcontrol−pset)prange,

其中：

- *fleak* 是 **Leakage flow fraction** 参数的值。
- *pcontrol* 是控制压力，即端口 **B** 处的压力与大气压力之差。
- *pset* 是 **Set pressure (gauge)** 参数的值。

当您将 **Set pressure control** 设置为 `Controlled` 时，阀门开启分数为

λ=1−(1−fleak)(pcontrol−ps)prange,

其中 *ps* 是端口 **Ps** 处信号的值。如果控制压力超过阀门压力范围，则阀门开启分数为 *fleak*。

### 动量平衡

阀中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 模块将流量容量的度量按 *λ* 缩放，以考虑阀门开口面积。
- `Tabulated` — 模块根据 **Cv flow coefficient vector**、**Kv flow coefficient vector**、**Orifice area vector** 或 **Sonic conductance vector** 参数之一对流量容量的度量进行插值。此函数使用一维查找表。

**Cv 流量系数参数化**

当您将 **Valve parametrization** 设置为 `Cv flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin,

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *vin* 是入口比容。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，阀门发生阻塞流，模块使用方程

m˙=23CvN6FγxTpinvin.

**Kv 流量系数参数化**

当您将 **Valve parametrization** 设置为 `Kv flow coefficient` 时，模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**阀门面积参数化**

当您将 **Valve parametrization** 设置为 `Orifice area` 时，质量流量为

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，阀门发生阻塞流，模块使用方程

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

**Sonic Conductance 参数化**

当您将 **Valve parametrization** 设置为 `Sonic conductance` 时，质量流量为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是声速流导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞流，模块切换到方程

m˙=CρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者对空气以外的流体进行建模，则可能需要用混合物比重的平方根来缩放声速流导。

### 质量平衡

模块通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### 开度动态

当您选择 **Opening dynamics** 时，模块引入控制压力滞后，并用动态控制压力 *pdyn* 替换 *pcontrol*。模块基于 **Opening time constant** 参数 *τ* 计算动态控制压力

p˙dyn=pcontrol−pdynτ.

默认情况下，模块清除 **Opening dynamics** 复选框。

### 能量平衡

能量在阀门中守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间没有热交换。
