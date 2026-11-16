---
type: simulink-block
title: 'Orifice (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices'
documentation_page: 'orificema'
documentation_source_path: 'ref/orificema.html'
language: zh-CN
chinese_source: worker-translation
---

# Orifice (MA)

## 端口

### 守恒

### **A** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。

### **B** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。
### 输入

### **S** — 控制构件位置，m 物理信号

设置孔口开度的控制构件位置。

#### 依赖关系

要启用此端口，请将 **孔口类型** 设置为 `Variable`。

## 参数

### **孔口类型** — 恒定或可变孔口 `Variable`（默认） | `Constant`

孔口类型。将此参数设置为 `Variable` 时，孔口面积根据端口 **S** 接收的输入信号而变化。

### **孔口参数化** — 可变或恒定孔口参数化 `Cv flow coefficient`（默认） | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据孔口两侧压差计算质量流量，或根据质量流量计算压差的方法。

### **开口特性** — 将控制信号转换为流量能力度量的方法 `Linear`（默认） | `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`。

### **孔口关闭时的控制构件位置** — 控制构件偏移 `0` m（默认） | 正标量

控制构件偏移，或孔口完全关闭时 **S** 处的值。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，并将 **开口特性** 设置为 `Linear`。

### **孔口从关闭到打开的控制构件行程** — 控制构件行程 `5e-3` m（默认） | 正标量

控制构件在孔口关闭与打开之间移动的距离。将 **打开方向** 设置为 `Positive control member displacement opens orifice` 时，孔口在 **孔口关闭时的控制构件位置** 与 **孔口从关闭到打开的控制构件行程** 两个参数之和处完全打开。将 **打开方向** 设置为 `Negative control member displacement opens orifice` 时，孔口在 **孔口关闭时的控制构件位置** 与 **孔口从关闭到打开的控制构件行程** 两个参数之差处完全打开。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，并将 **开口特性** 设置为 `Linear`。

### **打开方向** — 打开孔口的位移方向 `Positive control member displacement opens orifice`（默认） | `Negative control member displacement opens orifice`

打开可变孔口的构件位移方向。正方向表示 **S** 处信号增加会打开孔口。负方向表示 **S** 处信号减小会打开孔口。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，并将 **开口特性** 设置为 `Linear`。

### **Cv 流量系数** — 流量系数 `4`（默认） | 正标量

恒定 *Cv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Constant`，并将 **孔口参数化** 设置为 `Cv flow coefficient`。

### **最大 Cv 流量系数** — 组件最大打开时对应的 *Cv* 系数 `4`（默认） | 正标量

孔口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Cv flow coefficient`，并将 **开口特性** 设置为 `Linear`。

### **控制构件位置向量** — 控制构件位置向量 `[0, .002, .004, .007, .017] m`（默认） | 1×*n* 向量

用于表格化孔口参数化的控制构件位置向量。向量元素与 **孔口面积向量**、**Cv 流量系数向量** 或 **Kv 流量系数向量** 参数中的值一一对应。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，并将 **开口特性** 设置为 `Tabulated`。

### **Cv 流量系数向量** — 与构件位置向量中的值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **控制构件位置向量** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Cv flow coefficient`，并将 **开口特性** 设置为 `Tabulated`。

### **阻塞流时的 xT 压差比因子** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞时的值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Kv 流量系数** — 流量系数 `3.6`（默认） | 正标量

恒定 *Kv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Constant`，并将 **孔口参数化** 设置为 `Kv flow coefficient`。

### **最大 Kv 流量系数** — 组件最大打开时对应的 *Kv* 系数 `3.6`（默认） | 正标量

孔口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Kv flow coefficient`，并将 **开口特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 与构件位置向量中的值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **控制构件位置向量** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Kv flow coefficient`，并将 **开口特性** 设置为 `Tabulated`。

### **声速流导** — 阻塞流状态下流量能力的度量 `12 l/(bar*s)`（默认） | 正标量

在阻塞开始时测得的、通过阻力元件的质量流量与上游压力及 ISO 8778 中定义的标准条件下质量密度的乘积之比。此参数确定给定上游压力下允许的最大流量。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Constant`，并将 **孔口参数化** 设置为 `Sonic conductance`。

### **最大声速流导** — 组件最大打开时对应的声速流导 `12 l/(bar*s)`（默认） | 正标量

端口 **S** 指定的控制信号为 `1` 且可用于流动的横截面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Sonic conductance`，并将 **开口特性** 设置为 `Linear`。

### **临界压力比** — 流动首次阻塞时的下游与上游压力之比 `0.3`（默认） | 正标量

流动首次开始阻塞且流速达到其最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **孔口类型** 设置为
  `Constant`，并将
  **孔口参数化** 设置为
  `Sonic conductance`。
- 将 **孔口类型** 设置为
  `Variable`，将 **孔口参数化** 设置为
  `Sonic conductance`，并将 **开口特性** 设置为
  `Linear`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认） | 正标量

用于更准确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认） | 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声速流导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声速流导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Sonic conductance`。

### **声速流导向量** — 与控制构件位置向量中的值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认） | 正值向量

阻力元件内部的声速流导向量。每个流导对应 **控制构件位置向量** 参数中的一个值。向量大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Sonic conductance`，并将 **开口特性** 设置为 `Tabulated`。

### **临界压力比向量** — 与控制构件位置向量中的值对应的临界压力比 `0.3 * ones(1,6)`（默认） | 正数向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应 **控制构件位置向量** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。向量大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Sonic conductance`，并将 **开口特性** 设置为 `Tabulated`。

### **孔口面积** — 孔口开口面积 `1e-4` `m^2`（默认） | 正标量

孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Constant`，并将 **孔口参数化** 设置为 `Orifice area`。

### **最大孔口面积** — 最大孔口开口面积 `1e-4 m^2`（默认） | 正标量

孔口完全打开时的孔口面积。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Orifice area`，并将 **开口特性** 设置为 `Linear`。

### **孔口面积向量** — 孔口开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认） | 1×*n* 向量

用于孔口面积表格化参数化的孔口面积值向量。此向量中的值与 **控制构件位置向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，将 **孔口参数化** 设置为 `Orifice area`，并将 **开口特性** 设置为 `Tabulated`。

### **流出系数** — 流出系数 `0.64`（默认） | 正标量

实际流量与理想流量之比。此参数说明孔口方程中未捕获的实际损失。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Orifice area`。

### **泄漏流量分数** — 流量比 `1e-6`（默认） | 正标量

孔口关闭时流量与打开时流量之比。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，并将 **开口特性** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | [0,1] 范围内的正标量

连续平滑因子，在孔口接近打开或接近关闭位置时为流量响应引入渐进变化层。将此参数设置为非零且小于 1 的值，可提高这些区域中仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **孔口类型** 设置为 `Variable`，并将 **开口特性** 设置为 `Linear`。

### **层流压力比** — 层流-湍流过渡压力比 `0.999`（默认） | 正标量

流体在层流和湍流状态之间过渡时的孔口出口压力与孔口入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **端口 A 和 B 处横截面积** — 阀端口面积 `0.01` m^2（默认） | 正标量

孔口端口 **A** 和 **B** 的面积。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2025a 中引入**

## 描述

湿空气网络中的孔口

Orifice (MA) 模块对湿空气网络中恒定或可变面积孔口导致的压力损失进行建模。模块根据入口条件计算阀内流体属性。流体与环境之间没有热交换，因此孔口内部的相变仅由于压降或从模型其他部分传播的相变而发生。

孔口可以是恒定的或可变的。当 **孔口类型** 参数为 `Variable` 时，端口 **S** 处的物理信号设置控制构件的位置，从而打开和关闭孔口。

### 孔口参数化

模块行为取决于 **Orifice parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量当受到一定压差驱动时湿空气流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v（其中 Kv=0.865Cv）决定模块参数化。流量系数衡量当受到一定压差驱动时湿空气流动的容易程度。
- `Sonic conductance` — 稳态下阻力元件的声速导纳决定模块参数化。声速导纳衡量当发生*阻塞*时湿空气流动的容易程度，*阻塞*是一种流速达到当地声速的状态。当上下游压力之比达到称为*临界压力比*的临界值时，会发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 可变孔口

当您将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear` 时，模块使用端口 **S** 处的输入计算孔口开度，

λ=ε(1−fleak)(S−Smin)ΔS+fleak,

其中 *S* 是端口 **S** 处信号的值，*Smin* 和 *ΔS* 分别是 **Control member position at closed orifice** 和 **Control member travel between closed and open orifice** 参数的值。

当您将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Tabulated` 时，模块根据 **Control member position vector** 参数和端口 **S** 处的输入对孔口特性进行插值。

对于可变孔口，孔口中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量与端口 **S** 处的控制信号成正比。随着控制信号增加，流量能力的度量从指定的最小值缩放到指定的最大值。

  当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为独立于控制信号的常量。
- `Tabulated` — 模块将流量能力的度量计算为端口 **S** 处控制信号的函数。此函数使用一维查找表。

  当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为控制信号的函数。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。

**Cv 流量系数参数化**

当您将 **Orifice parametrization** 设置为 `Cv flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin,

其中：

- *Cv* 是流量系数。
- *N6* 是常量，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时等于 27.3。
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

当压力比 pout/pin 降至 1−FγxT 以下时，孔口发生阻塞，模块使用方程

m˙=23CvN6FγxTpinvin.

**Kv 流量系数参数化**

当您将 **Orifice parametrization** 设置为 `Kv flow coefficient` 时，模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**声速导纳参数化**

当您将 **Orifice parametrization** 设置为 `Sonic conductance` 时，质量流量为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是声速导纳。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞，模块切换到方程

m˙=CρrefpinTrefTin.

**Orifice parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模除空气以外的流体，您可能需要用混合物比重的平方根来缩放声速导纳。

**孔口面积参数化**

当您将 **Orifice parametrization** 设置为 `Orifice area` 时，质量流量为

m˙=CdAorifice2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AorificeAport)2(poutpin)2γ],

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAorifice2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AorificeAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口发生阻塞，模块使用方程

m˙=CdAorifice2γγ+1pin1vin1(γ+12)2γ−1−(AorificeAport)2.

### 质量平衡

模块通过阀门保持质量守恒

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### 能量平衡

能量在孔口中守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间没有热交换。
