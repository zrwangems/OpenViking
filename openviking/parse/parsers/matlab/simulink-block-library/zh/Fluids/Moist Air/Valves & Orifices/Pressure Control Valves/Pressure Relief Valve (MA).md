---
type: simulink-block
title: 'Pressure Relief Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalvema'
documentation_source_path: 'ref/pressurereliefvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Relief Valve (MA)

## 端口
```yaml
ports:
- name: A
  summary: 流体入口或出口湿空气
  direction: conserving
- name: B
  summary: 流体入口或出口湿空气
  direction: conserving
- name: Ps
  summary: 设定压力，Pa 物理信号
  direction: input
```

### 守恒端口

### **A** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。

### **B** — 流体入口或出口湿空气

与流体入口或出口端口关联的湿空气守恒端口。
### 输入

### **Ps** — 设定压力，Pa 物理信号

用于变化设定压力信号的输入端口。

#### 依赖

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。
## 参数
```yaml
parameters:
- name: Valve parameterization
  summary: 阀门参数化模型 Cv flow coefficient（默认）| Kv flow coefficient | Sonic conductance | Orifice area
  group: ''
- name: Opening characteristic
  summary: 将控制信号转换为流量容量度量的方法 Linear（默认）| Tabulated
  group: ''
- name: Opening pressure specification
  summary: 控制压力 Pressure differential（默认）| Gauge pressure at port A
  group: ''
- name: Set pressure control
  summary: 可变或恒定设定压力 Constant（默认）| Controlled
  group: ''
- name: Set pressure differential
  summary: 设定压力 0.01 MPa（默认）| 正标量
  group: ''
- name: Set pressure (gauge)
  summary: 设定压力 0.1 MPa（默认）| 正标量
  group: ''
- name: Pressure regulation range
  summary: 阀门工作范围 0.1 MPa（默认）| 正标量
  group: ''
- name: Opening pressure differential vector
  summary: '压差向量 [0.2 : 0.2 : 1.2] MPa（默认）| 1×*n* 向量'
  group: ''
- name: Opening pressure (gauge) vector
  summary: '表压向量 [0.2 : 0.2 : 1.2] MPa（默认）| 1×*n* 向量'
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Maximum Cv flow coefficient
  summary: 对应于组件最大开启状态的 *Cv* 系数 4（默认）| 正标量
  group: ''
- name: Cv flow coefficient vector
  summary: 对应于成员位置向量中值的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: ''
- name: Maximum Kv flow coefficient
  summary: 对应于组件最大开启状态的 *Kv* 系数 3.6（默认）| 正标量
  group: ''
- name: Kv flow coefficient vector
  summary: 对应于成员位置向量中值的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: ''
- name: Maximum sonic conductance
  summary: 对应于组件最大开启状态的声速流导 12 l/(bar*s)（默认）| 正标量
  group: ''
- name: Critical pressure ratio
  summary: 流动首次阻塞时的下游与上游压力之比 0.3（默认）| 正标量
  group: ''
- name: Subsonic index
  summary: 用于表征亚声速流态中质量流量的指数 0.5（默认）| 正标量
  group: ''
- name: ISO reference temperature
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: ''
- name: ISO 参考密度
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: ''
- name: 声速导纳向量
  summary: 与控制构件位置向量中的值对应的声速导纳 [1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)（默认）| 正值向量
  group: ''
- name: 临界压力比向量
  summary: 与控制构件位置向量中的值对应的临界压力比 0.3 * ones(1,6)（默认）| 正数向量
  group: ''
- name: 阻塞流时的 xT 压差比系数
  summary: 压差比 0.7（默认）| 正标量
  group: ''
- name: 最大孔口面积
  summary: 最大阀门开口面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: 孔口面积向量
  summary: 阀门开口面积值向量 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认）| 1×*n* 向量
  group: ''
- name: 泄漏流量分数
  summary: 流量比 1e-6（默认）| 正标量
  group: ''
- name: 平滑因子
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: 层流压力比
  summary: 层流-湍流过渡压力比 0.999（默认）| 正标量
  group: ''
- name: 端口 A 和 B 的横截面积
  summary: 阀门端口面积 0.01 m^2（默认）| 正标量
  group: ''
- name: 开启动态特性
  summary: 是否考虑流量对阀门开启的响应 off（默认）| on
  group: ''
- name: 开启时间常数
  summary: 阀门开启时间常数 0.1 s（默认）| 正标量
  group: ''
```

### **Valve parameterization** — 阀门参数化模型 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

模块用于根据阀门两端的压差计算质量流量或根据质量流量计算压差的方法。

### **Opening characteristic** — 将控制信号转换为流量容量度量的方法 `Linear`（默认）| `Tabulated`

对所选的流量容量度量进行参数化的方法。

### **Opening pressure specification** — 控制压力 `Pressure differential`（默认）| `Gauge pressure at port A`

控制压力规格：

- 当此参数为 `Pressure differential` 时，当 *pA ̶ pB* 超过 **Set pressure differential** 时阀门打开。
- 当此参数为 `Gauge pressure at port A` 时，当 *pA ̶ patm* 超过 **Set pressure (gauge)** 时阀门打开。

### **Set pressure control** — 可变或恒定设定压力 `Constant`（默认）| `Controlled`

压力阈值是恒定的还是可变的。将此参数设置为 `Controlled` 会暴露物理信号端口 **Ps**。

### **Set pressure differential** — 设定压力 `0.01` MPa（默认）| 正标量

阀门压力阈值。当控制压力 *pA ̶ pB* 超过设定压力时，阀门开始打开。

#### 依赖

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，并将 **Set pressure control** 设置为 `Constant`。

### **Set pressure (gauge)** — 设定压力 `0.1` MPa（默认）| 正标量

阀门压力阈值。当控制压力 *pA ̶ patm* 超过设定压力时，阀门开始打开。

#### 依赖

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并将 **Set pressure control** 设置为 `Constant`。

### **Pressure regulation range** — 阀门工作范围 `0.1` MPa（默认）| 正标量

阀门工作范围。阀门在设定压力值处开始打开，并在 *pmax* 处完全打开，*pmax* 是压力调节范围的终点，其中 *pmax = pset + prange*。

#### 依赖

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Opening pressure differential vector** — 压差向量 `[0.2 : 0.2 : 1.2] MPa`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的压差值向量。

#### 依赖

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Opening pressure (gauge) vector** — 表压向量 `[0.2 : 0.2 : 1.2] MPa`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的表压值向量。

#### 依赖

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

实际流量与理想流量之比。此参数考虑了孔口方程中未捕获的实际损失。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Maximum Cv flow coefficient** — 对应于组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

当可用于流动的节流面积最大时的 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应于成员位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应于组件最大开启状态的 *Kv* 系数 `3.6`（默认）| 正标量

当可用于流动的节流面积最大时的 *Kv* 流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应于成员位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum sonic conductance** — 对应于组件最大开启状态的声速流导 `12 l/(bar*s)`（默认）| 正标量

当端口 **S** 处指定的控制信号为 `1` 且可用于流动的横截面积最大时的声速流导值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **声速导纳向量** — 与控制构件位置向量中的值对应的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻力元件内部的声速导纳向量。此向量中的值与 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **临界压力比向量** — 与控制构件位置向量中的值对应的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次发生阻塞时的临界压力比向量。临界压力比是流动速度达到当地声速时下游与上游压力之比的分数。此向量中的值与 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

首次发生阻塞时的入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大孔口面积** — 最大阀门开口面积 `1e-4 m^2`（默认）| 正标量

阀门完全打开时的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **孔口面积向量** — 阀门开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1×*n* 向量

蒸汽阀面积表格化参数化的孔口面积值向量。此向量中的值与 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **泄漏流量分数** — 流量比 `1e-6`（默认）| 正标量

阀门关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值可提高这些区域中仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **层流压力比** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间过渡时的阀门出口压力与阀门入口压力之比。在层流中，压力损失与质量流量成线性关系，在湍流中成二次关系。

### **端口 A 和 B 的横截面积** — 阀门端口面积 `0.01` m^2（默认）| 正标量

端口 **A** 和 **B** 的面积。

### **开启动态特性** — 是否考虑流量对阀门开启的响应 `off`（默认）| `on`

是否考虑阀门开启对流体系统造成的瞬态效应。选择此参数通过引入流量响应的一阶滞后来近似开启条件。

### **开启时间常数** — 阀门开启时间常数 `0.1` s（默认）| 正标量

用于计算开启动态特性滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。
## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的压力泄放阀

Pressure Relief Valve (MA) 模块用于对湿空气网络中的压力控制泄放阀进行建模。当压力超过设定压力时，阀门打开。在 **Set pressure specification** 参数中指定打开阀门的压差，该压差可以是端口 **A** 和 **B** 之间的压力差，也可以是端口 **A** 处的表压。当您将 **Set pressure control** 设置为 `Controlled` 时，设定压力根据端口 **Ps** 处的输入信号而变化。对于基于流体网络中其他位置的压力控制，请参阅 Pressure Compensator Valve (MA) 模块。

### 压力控制

当阀门中的压力 *pcontrol* 超过设定压力 *pset* 时，阀门打开。当控制压力达到 *pset* + *prange* 时，阀门完全打开，其中 *prange* 是 **Pressure regulation range** 参数的值。

对于线性参数化，模块计算阀门的开启分数 *λ*。当您将 **Set pressure control** 设置为 `Constant` 时，*λ* 为

λ=(1−fleak)(pcontrol−pset)prange+fleak，

其中：

- *fleak* 是 **Leakage flow fraction** 参数的值。
- *pcontrol* 是控制压力，取决于 **Set pressure specification** 参数的值。

  当您将 **Set pressure specification** 设置为 `Pressure differential` 时，控制压力为 *pA ̶ pB*。

  当您将 **Set pressure specification** 设置为 `Gauge pressure at port A` 时，控制压力为端口 **A** 处的压力与大气压力之差。
- *pset* 是设定压力，取决于 **Set pressure specification** 参数的值。

  当您将 **Set pressure specification** 设置为 `Pressure differential` 时，*pset* 是 **Set pressure differential** 参数的值。

  当您将 **Set pressure specification** 设置为 `Gauge pressure at port A` 时，*pset* 是 **Set pressure (gauge)** 参数的值。

当您将 **Set pressure control** 设置为 `Controlled` 时，阀门开启分数为

λ=(1−fleak)(pcontrol−ps)prange+fleak，

其中 *ps* 是端口 **Ps** 处信号的值。如果控制压力超过阀门压力调节范围，则阀门开启分数为 1。

### Momentum Balance

阀门中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 该模块将流量容量的度量乘以 *λ* 以考虑阀门开口面积。
- `Tabulated` — 该模块从 **Cv flow coefficient vector**、**Kv flow coefficient vector**、**Orifice area vector** 或 **Sonic conductance vector** 参数中插值得到流量容量的度量。此函数使用一维查找表。

**Cv Flow Coefficient Parameterization**

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

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，阀门变为阻塞，该模块使用方程

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient Parameterization**

当您将 **Valve parametrization** 设置为 `Kv flow coefficient` 时，该模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**Valve Area Parameterization**

当您将 **Valve parametrization** 设置为 `Orifice area` 时，质量流量为

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块平滑过渡到方程的线性化形式，

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，阀门变为阻塞，该模块使用方程

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

**Sonic Conductance Parameterization**

当您将 **Valve parameterization** 设置为 `Sonic conductance` 时，质量流量为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是声速导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口变为阻塞，该模块切换到方程

m˙=CρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能需要按混合物比重的平方根来缩放声速导。

### Opening Dynamics

当您选择 **Opening dynamics** 时，该模块引入控制压力滞后，并将 *pcontrol* 替换为动态控制压力 *pdyn*。该模块基于 **Opening time constant** 参数 *τ* 计算动态控制压力

p˙dyn=pcontrol−pdynτ.

默认情况下，该模块清除 **Opening dynamics** 复选框。

### Mass Balance

该模块通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### Energy Balance

能量在阀门中守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间没有热交换。
