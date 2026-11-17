---
type: simulink-block
title: 'Temperature Control Valve (MA)'
family: 'moist-air'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Flow Control Valves'
documentation_page: 'temperaturecontrolvalvema'
documentation_source_path: 'ref/temperaturecontrolvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Temperature Control Valve (MA)

## 端口

### 守恒

### **A** — 阀门入口或出口湿空气

与流动进入或离开阀门的开口相关联的湿空气守恒端口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **B** — 阀门入口或出口湿空气

与流动进入或离开阀门的开口相关联的湿空气守恒端口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **T** — 传感端口 湿空气 | 热

与温度传感相关联的湿空气或热守恒端口。通过该端口没有质量或能量流动。当 **Temperature sensing** 为 `Moist air sensing port` 时，端口 **T** 是湿空气传感端口。当 **Temperature sensing** 为 `Thermal sensing port` 时，端口 **T** 是热传感端口。

#### 依赖关系

要启用此端口，请将 **Temperature sensing** 设置为 `Moist air sensing port` 或 `Thermal sensing port`。

## 参数

### **Valve operation** — 开口面积变化的符号 `Opens above activation temperature`（默认）| `Closes above activation temperature`

由升温引起的开口面积变化的符号。开口面积可以随温度升高而增大，也可以缩小。该变化从激活温度开始，并在整个阀门温度调节范围内随升温条件持续。

默认设置对应于常闭阀，其随温度升高而打开。替代设置对应于常开阀，其随温度升高而关闭。

### **Temperature sensing** — 控制阀门温度传感的方法 `Valve inlet temperature`（默认）| `Moist air sensing port` | `Thermal sensing port`

该模块用于测量控制阀门温度的方法：

- 当将 **Temperature sensing** 设置为 `Valve inlet temperature` 时，阀门使用上游温度来控制阀门。
- 当将 **Temperature sensing** 设置为 `Moist air sensing port` 时，该模块启用端口 **T**，这是一个湿空气传感端口。将此端口连接到湿空气网络的任意部分，以使用该温度来控制阀门。端口 **T** 仅用于传感，没有流入或流出的流动。
- 当将 **Temperature sensing** 设置为 `Thermal sensing port` 时，该模块启用热传感端口 **T**。将此端口连接到热网络的任意部分，以使用该温度来控制阀门。端口 **T** 仅用于传感，并且与环境没有热交换。

### **Activation temperature** — 触发开启机构的温度 `330 K`（默认）| 标量

触发开启机构的温度。温度升高到超过此温度时，将打开或关闭阀门，具体取决于 **Valve operation** 参数的设置。在整个阀门温度调节范围内，开口面积保持可变。

### **Temperature regulation range** — 开口面积可变所处的温度区间跨度 `8 K`（默认）| 正标量

阀门开口面积随温度变化的温度区间跨度。该区间始于阀门的激活温度。其结束于该激活温度与在此指定的调节范围之和。

### **Sensor time constant** — 温度变化在入口传感器处记录所需的时间 `1.5 s`（默认）| 以时间单位表示的正标量

温度变化在入口传感器处记录的特征时间。此参数确定变化开始与稳定测量同一变化之间的延迟，该稳定测量是在传感器接近其新的稳态时取得的。`0` 值意味着传感器对温度变化瞬时响应。

### **Valve parameterization** — 用于指定孔口流动特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 确定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，确定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声导确定模块参数化。
- `Orifice area` — 流动限制的尺寸确定模块参数化。

### **Maximum Cv flow coefficient** — 对应于组件最大开度的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积为最大时 *Cv* 流量系数的值。此参数衡量湿空气在压差驱动下穿过阻性元件的容易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为首次发生阻塞处的 (pin−pout)/pin。如果没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，对于许多阀门，默认值 0.7 是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应于组件最大开度的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积为最大时 *Kv* 流量系数的最大值。此参数衡量湿空气在压差驱动下穿过阻性元件的容易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应于组件最大开度的声导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积为最大时声导的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游压力与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Maximum orifice area** — 对应于组件最大开度的流通面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积为最大时孔口开度的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Discharge coefficient** — 排放系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于考虑理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

孔口关闭时与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流动响应引入一层渐变变化。将此参数设置为小于 1 的非零值，以提高在这些工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间过渡时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间过渡时的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。各端口尺寸相等。此参数的值应与阻性元件所连接组件的入口面积匹配。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的温度控制阀

Temperature Control Valve (MA) 模块表示带有恒温器的孔口作为流量控制机构。恒温器包含温度传感器和开启机构。传感器位于入口处，并以略微延迟（由一阶时间滞后捕获）响应温度变化。

当传感器读取到超过预设激活值的温度时，开启机构动作，阀门开始打开或关闭，具体取决于 **Valve operation** 参数指定的操作模式。开口面积的变化持续到阀门温度范围的极限，超过该极限后开口面积为常数。在温度范围内，开口面积是温度的线性函数。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞且速度饱和。当背压比达到阀门的临界特征值时发生阻塞。该模块不捕获超声速流动。

### 控制温度

入口处的温度读数是阀门的控制信号。当 **Valve operation** 为 `Opens above activation temperature` 时，温度读数超过激活温度越多，开口面积偏离最大关闭状态的程度越大；当 **Valve operation** 为 `Closes above activation temperature` 时，开口面积偏离完全打开状态的程度越大。

传感器温度读数与激活温度之间的差值为温度超调。该模块根据阀门的温度调节范围对该变量进行归一化。阀门开度分数为

T^=TS-TActΔT,

其中：

- *TAct* 是 **Activation temperature** 参数的值。
- *TS* 是传感器温度读数。

  - 当 **Temperature sensing** 为 `Valve inlet temperature` 时，*TS* 是阀门的上游温度。
  - 当 **Temperature sensing** 为 `Moist air sensing port` 时，*TS* 是湿空气网络在连接到端口 **T** 处的温度。
  - 当 **Temperature sensing** 为 `Thermal sensing port` 时，*TS* 是热网络在连接到端口 **T** 处的温度。
- *ΔT* 是 **Temperature regulation range** 参数的值。

**数值平滑**

当 **Smoothing factor** 参数非零时，该模块对阀门开度分数 T^ 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅数值平滑。

**传感器动态**

为了模拟真实温度传感器（其只能逐渐记录温度变化），该模块向温度读数 *TS* 添加一阶时间滞后。该滞后使传感器对温度变化具有瞬态响应。*TS* 的表达式为

ddtTS=TIn−TSτ,

其中 *TIn* 是仿真当前时间步的实际入口温度，*τ* 是 **Sensor time constant** 参数的值。此参数越小，传感器响应越快。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 确定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，确定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的容易程度。
- `Sonic conductance` — 稳态下阻性元件的声导确定模块参数化。声导衡量湿空气在 *阻塞* 条件下流动的容易程度，阻塞是流速达到当地声速的状态。当下游压力与上游压力之比达到称为 *临界压力比* 的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸确定模块参数化。

该模块按阀门开度分数缩放指定的流通能力。当阀门开度分数从 `0` 上升到 `1` 时，流通能力的度量从其指定的最小值缩放到指定的最大值。

### 动量平衡

模块方程取决于 **孔口参数化** 参数。当您将 **孔口参数化** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：

- *Cv* 是 **最大 Cv 流量系数** 参数的值。
- *Sopen* 是阀门开口面积。
- *SMax* 是阀门完全打开时的最大阀门面积。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 之比。
- *xT* 是 **阻塞流下的 xT 压差比系数** 参数的值。

当压力比 pout/pin 升高到 **层流压力比** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，孔口发生阻塞，模块切换到以下方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当您将 **孔口参数化** 设置为 `Kv flow coefficient parameterization` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **孔口参数化** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **孔口参数化** 设置为 `Sonic conductance` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是 **最大声速导率** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **亚声速指数** 参数的值。
- *Tref* 是 **ISO 参考温度** 参数的值。
- *ρref* 是 **ISO 参考密度** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升高到 **层流压力比** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞，模块切换到以下方程

m˙=CSopenSMaxρrefpinTrefTin.

**阀门参数化** 参数的 `Sonic conductance` 设置用于气动应用。如果您将此设置用于含有高浓度痕量气体的湿空气，或正在对空气以外的流体建模，则可能需要按混合气体比重的平方根缩放声速导率。

有关当 **孔口参数化** 参数为 `Sonic conductance` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **孔口参数化** 设置为 `Orifice area` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

其中：

- *Sopen* 是阀门开口面积。
- *S* 是 **端口 A 和 B 处的横截面积** 参数的值。
- *Cd* 是 **流量系数** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升高到 **层流压力比** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口发生阻塞，模块切换到以下方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关当 **孔口参数化** 参数为 `Orifice area` 时的质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

模块通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### 能量平衡

模块的阻性元件是绝热组件。流体与其周围壁面之间不能发生热交换。流体从入口到出口流动时，不对流体做功，流体也不做功。能量只能通过对流经由端口 **A** 和 **B** 流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是经由端口 **A** 或 **B** 流入阀门的能量流率。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。

### 假设和限制

- 此模块不对超声速流动建模。
