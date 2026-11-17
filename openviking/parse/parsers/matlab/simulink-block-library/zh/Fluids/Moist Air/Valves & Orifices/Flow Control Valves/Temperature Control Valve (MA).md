---
type: simulink-block
title: 'Temperature Control Valve (MA)'
family: 'hydro'
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
```yaml
ports:
- name: A
  summary: 阀门入口或出口湿空气
  direction: conserving
- name: B
  summary: 阀门入口或出口湿空气
  direction: conserving
- name: T
  summary: 传感端口湿空气 | 热
  direction: conserving
```

### 守恒端口

### **A** — 阀门入口或出口湿空气

与流体进入或离开阀门的开口相关联的湿空气守恒端口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **B** — 阀门入口或出口湿空气

与流体进入或离开阀门的开口相关联的湿空气守恒端口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **T** — 传感端口湿空气 | 热

与温度传感相关联的湿空气或热守恒端口。通过该端口没有质量或能量流动。当**Temperature sensing**为`Moist air sensing port`时，端口**T**为湿空气传感端口。当**Temperature sensing**为`Thermal sensing port`时，端口**T**为热传感端口。

#### 依赖关系

要启用此端口，请将**Temperature sensing**设置为`Moist air sensing port`或`Thermal sensing port`。
## 参数
```yaml
parameters:
- name: Valve operation
  summary: 开口面积变化的符号 Opens above activation temperature（默认）| Closes above activation temperature
  group: ''
- name: Temperature sensing
  summary: 控制阀门温度传感的方法 Valve inlet temperature（默认）| Moist air sensing port | Thermal sensing port
  group: ''
- name: Activation temperature
  summary: 触发开启机构的温度 330 K（默认）| 标量
  group: ''
- name: Temperature regulation range
  summary: 开口面积可变的温度区间跨度 8 K（默认）| 正标量
  group: ''
- name: Sensor time constant
  summary: 温度变化在入口传感器处记录所需的时间 1.5 s（默认）| 以时间为单位的正标量
  group: ''
- name: Valve parameterization
  summary: 用于指定节流孔流动特性的参数化方法 Cv flow coefficient（默认）| Kv flow coefficient | Sonic conductance | Orifice area
  group: ''
- name: Maximum Cv flow coefficient
  summary: 对应于组件最大开启状态的Cv系数 4（默认）| 正标量
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: 压差比 0.7（默认）| 正标量
  group: ''
- name: Maximum Kv flow coefficient
  summary: 对应于组件最大开启状态的Kv系数 3.6（默认）| 正标量
  group: ''
- name: Maximum sonic conductance
  summary: 对应于组件最大开启状态的声速导纳 12 l/(bar*s)（默认）| 正标量
  group: ''
- name: Critical pressure ratio
  summary: 流动首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: ''
- name: Subsonic index
  summary: 用于表征亚声速流态中质量流量的指数 0.5（默认）| 正标量
  group: ''
- name: ISO reference temperature
  summary: ISO 8778参考温度 293.15 K（默认）| 标量
  group: ''
- name: ISO reference density
  summary: ISO 8778参考密度 1.185 kg/m^3（默认）| 正标量
  group: ''
- name: Maximum orifice area
  summary: 对应组件最大开启状态的流通面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 取值范围为 [0,1] 的正标量
  group: ''
- name: Leakage flow fraction
  summary: 流量比 1e-6（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 取值范围为 [0,1] 的正标量
  group: ''
- name: Laminar flow pressure ratio
  summary: 流动在层流和湍流状态之间转换时的压力比 0.999（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 湿空气端口处的流通面积 0.01 m^2（默认）| 正标量
  group: ''
```

### **Valve operation** — 开口面积变化的符号 `Opens above activation temperature`（默认）| `Closes above activation temperature`

由升温引起的开口面积变化的符号。开口面积可以随温度升高而扩大，也可以收缩。变化从激活温度开始，并随着温度升高在阀门的整个温度调节范围内持续。

默认设置对应于随温度升高而开启的常闭阀门。替代设置对应于随温度升高而关闭的常开阀门。

### **Temperature sensing** — 控制阀门温度传感的方法 `Valve inlet temperature`（默认）| `Moist air sensing port` | `Thermal sensing port`

模块用于测量控制阀门的温度的方法：

- 当将**Temperature sensing**设置为`Valve inlet temperature`时，阀门使用上游温度来控制阀门。
- 当将**Temperature sensing**设置为`Moist air sensing port`时，模块启用端口**T**，该端口为湿空气传感端口。将此端口连接到湿空气网络的任何部分，以使用该温度来控制阀门。端口**T**仅用于传感，没有流入或流出的流体。
- 当将**Temperature sensing**设置为`Thermal sensing port`时，模块启用热传感端口**T**。将此端口连接到热网络的任何部分，以使用该温度来控制阀门。端口**T**仅用于传感，与环境没有热交换。

### **Activation temperature** — 触发开启机构的温度 `330 K`（默认）| 标量

触发开启机构的温度。高于此温度的升温将开启或关闭阀门，具体取决于**Valve operation**参数的设置。开口面积在阀门的整个温度调节范围内保持可变。

### **Temperature regulation range** — 开口面积可变的温度区间跨度 `8 K`（默认）| 正标量

阀门开口面积随温度变化的温度区间跨度。该区间从阀门的激活温度开始，到激活温度与此处指定的调节范围之和结束。

### **Sensor time constant** — 温度变化在入口传感器处记录所需的时间 `1.5 s`（默认）| 以时间为单位的正标量

温度变化在入口传感器处记录的特征时间。此参数确定变化开始与稳定测量之间的延迟，该测量在传感器接近其新稳态时取得。值为`0`表示传感器对温度变化瞬时响应。

### **Valve parameterization** — 用于指定节流孔流动特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数
  *C*v
  确定模块参数化。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中Kv=0.865Cv，确定模块参数化。
- `Sonic conductance` — 稳态下阻力元件的声速导纳确定模块参数化。
- `Orifice area` — 流动限制的尺寸确定模块参数化。

### **Maximum Cv flow coefficient** — 对应于组件最大开启状态的Cv系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大时的*Cv*流量系数值。此参数衡量在压差驱动下湿空气通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

首次发生阻塞时入口压力*pin*与出口压力*pout*之间的比值，定义为(pin−pout)/pin。如果您没有此值，请查阅ISA-75.01.01 [3]中的表2。否则，对于许多阀门而言，默认值0.7是合理的。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Cv flow coefficient`或`Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应于组件最大开启状态的Kv系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大时的*Kv*流量系数最大值。此参数衡量在压差驱动下湿空气通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Kv flow coefficient`。

### **Maximum sonic conductance** — 对应于组件最大开启状态的声速导纳 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大时的声速导纳值。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **ISO reference temperature** — ISO 8778参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在ISO 8778中定义为293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整ISO参考参数值。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **ISO reference density** — ISO 8778参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在ISO 8778中定义为1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整ISO参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Maximum orifice area** — 对应组件最大开启状态的流通面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积达到最大值时，节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 取值范围为 [0,1] 的正标量

用于修正理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时与开启时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 取值范围为 [0,1] 的正标量

连续平滑因子，当节流孔处于接近开启或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，可提高仿真在这些工况下的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流状态之间转换时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。各端口尺寸相同。此参数的值应与阻力元件所连接的组件的入口面积相匹配。
## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的温度控制阀

Temperature Control Valve (MA) 模块表示一个带有恒温器的节流孔，作为流量控制机构。恒温器包含温度传感器和开启机构。传感器位于入口处，对温度变化做出响应时带有轻微延迟，该延迟由一阶时间滞后捕获。

当传感器读取到的温度超过预设的激活值时，开启机构动作，阀门开始打开或关闭，具体取决于 **Valve operation** 参数指定的运行模式。开启面积的变化持续到阀门温度范围的限值，超过该限值后开启面积为常数。在温度范围内，开启面积是温度的线性函数。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门特有的临界值时发生阻塞。该模块不捕获超音速流动。

### 控制温度

入口处的温度读数是阀门的控制信号。当 **Valve operation** 为 `Opens above activation temperature` 时，温度读数超过激活温度越多，开启面积偏离最大关闭状态的程度越大；当 **Valve operation** 为 `Closes above activation temperature` 时，温度读数超过激活温度越多，开启面积偏离完全开启状态的程度越大。

传感器温度读数与激活温度之间的差值即为温度超调量。该模块将此变量对阀门的温度调节范围进行归一化。阀门开启分数为

T^=TS-TActΔT，

其中：

- *TAct* 是 **Activation temperature** 参数的值。
- *TS* 是传感器温度读数。

  - 当 **Temperature sensing** 为 `Valve inlet temperature` 时，*TS* 是阀门的上游温度。
  - 当 **Temperature sensing** 为 `Moist air sensing port` 时，*TS* 是湿空气网络在连接到端口 **T** 处的温度。
  - 当 **Temperature sensing** 为 `Thermal sensing port` 时，*TS* 是热网络在连接到端口 **T** 处的温度。
- *ΔT* 是 **Temperature regulation range** 参数的值。

**数值平滑**

当 **Smoothing factor** 参数非零时，该模块对阀门开启分数 T^ 应用数值平滑。启用平滑有助于在仿真中保持数值鲁棒性。

有关详细信息，请参阅数值平滑。

**传感器动态特性**

为了模拟真实温度传感器只能逐渐记录温度变化的行为，该模块对温度读数 *TS* 添加一阶时间滞后。该滞后使传感器对温度变化具有瞬态响应。*TS* 的表达式为

ddtTS=TIn−TSτ，

其中 *TIn* 是仿真当前时间步的实际入口温度，*τ* 是 **Sensor time constant** 参数的值。此参数越小，传感器响应越快。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Sonic conductance` — 阻力元件在稳态下的声速导纳决定模块参数化。声速导纳衡量湿空气在*阻塞*状态下流动的难易程度，阻塞是指流动速度达到当地声速的工况。当下游压力与上游压力之比达到称为*临界压力比*的临界值时发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

该模块按阀门开启分数对指定的流通能力进行缩放。当阀门开启分数从 `0` 上升到 `1` 时，流通能力的度量从其指定的最小值缩放到指定的最大值。

### Momentum Balance

模块方程取决于 **Orifice parametrization** 参数。当您将 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin，

其中：

- *Cv* 是 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 是阀门开口面积。
- *SMax* 是阀门完全打开时的最大阀门面积。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞，模块切换到方程

m˙=23CvSopenSMaxN6FγxTpinρin。

当您将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Orifice parametrization** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Orifice parametrization** 设置为 `Sonic conductance` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是 **Maximum sonic conductance** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口变为阻塞，模块切换到方程

m˙=CSopenSMaxρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能需要按混合物比重的平方根来缩放声导。

有关当 **Orifice parametrization** 参数为 `Sonic conductance` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Orifice parametrization** 设置为 `Orifice area` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ]，

其中：

- *Sopen* 是阀门开口面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞，模块切换到方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2。

有关当 **Orifice parametrization** 参数为 `Orifice area` 时的质量流量方程的更多信息，请参阅 [4]。

### Mass Balance

模块通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### Energy Balance

模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动时，没有对流体做功，也没有流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。

### 假设和限制

- 此模块不建模超声速流动。
