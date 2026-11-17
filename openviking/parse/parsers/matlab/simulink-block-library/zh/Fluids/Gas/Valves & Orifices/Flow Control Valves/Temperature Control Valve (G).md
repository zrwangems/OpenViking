---
type: simulink-block
title: 'Temperature Control Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Flow Control Valves'
documentation_page: 'temperaturecontrolvalveg'
documentation_source_path: 'ref/temperaturecontrolvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Temperature Control Valve (G)

## 端口

### 守恒端口

### **A** — 阀门入口气体

与流体进入或离开阀门的开口相关联的气体守恒端口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **B** — 阀门入口气体

工作流体可以进入或离开阀门的开口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **T** — 传感端口气体 | 热

与温度传感相关联的气体或热守恒端口。通过该端口没有质量或能量流动。当**Temperature sensing**为`Gas sensing port`时，端口**T**为气体传感端口。当**Temperature sensing**为`Thermal sensing port`时，端口**T**为热传感端口。

#### 依赖关系

要启用此端口，请将**Temperature sensing**设置为`Gas sensing port`或`Thermal sensing port`。

## 参数

### **Valve operation** — 开口面积变化的符号 `Opens above activation temperature`（默认）| `Closes above activation temperature`

由升温引起的开口面积变化的符号。开口面积可以随温度升高而扩大，也可以随温度升高而收缩。该变化从激活温度开始，并在阀门的整个温度调节范围内随升温条件持续进行。

默认设置对应于常闭阀，随温度升高而打开。替代设置对应于常开阀，随温度升高而关闭。

### **Temperature sensing** — 控制阀门温度传感的方法 `Valve inlet temperature`（默认）| `Gas sensing port` | `Thermal sensing port`

模块用于测量控制阀门温度的方法：

- 当将**Temperature sensing**设置为`Valve inlet temperature`时，阀门使用上游温度来控制阀门。
- 当将**Temperature sensing**设置为`Gas sensing port`时，模块启用端口**T**，该端口为气体传感端口。将此端口连接到气体网络的任何部分，以使用该温度来控制阀门。端口**T**仅用于传感，没有流入或流出的流量。
- 当将**Temperature sensing**设置为`Thermal sensing port`时，模块启用热传感端口**T**。将此端口连接到热网络的任何部分，以使用该温度来控制阀门。端口**T**仅用于传感，与环境没有热交换。

### **Activation temperature** — 触发开启机构的温度 `330 K`（默认）| 标量

触发开启机构的温度。高于此温度的升温将打开或关闭阀门，具体取决于**Valve operation**参数的设置。在阀门的整个温度调节范围内，开口面积保持可变。

### **Temperature regulation range** — 开口面积可变的温度区间跨度 `8 K`（默认）| 正标量

阀门开口面积随温度变化的温度区间跨度。该区间从阀门的激活温度开始，到激活温度与此处指定的调节范围之和结束。

### **Sensor time constant** — 温度变化在入口传感器处记录所需的时间 `1.5 s`（默认）| 以时间为单位的正标量

温度变化在入口传感器处记录的特征时间。该参数决定了变化开始与稳定测量之间的延迟，该测量在传感器接近其新稳态时取得。值为`0`表示传感器对温度变化瞬时响应。

### **Valve parameterization** — 用于指定节流孔流动特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻力元件的声速导决定模块参数化。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### **Maximum Cv flow coefficient** — 对应于组件最大开启状态的Cv系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大时，*Cv*流量系数的值。该参数衡量气体在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 阻塞流时的压差比系数 `0.7`（默认）| 正标量

首次发生阻塞时入口压力
*pin*与出口压力
*pout*之间的比值，定义为(pin−pout)/pin。如果您没有此值，请查阅ISA-75.01.01 [3]中的表2。否则，对于许多阀门而言，默认值0.7是合理的。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Cv flow coefficient`或`Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应于组件最大开启状态的Kv系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大时，*Kv*流量系数的最大值。该参数衡量气体在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Kv flow coefficient`。

### **Maximum sonic conductance** — 对应于组件最大开启状态的声速导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大时的声速导值。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **ISO reference temperature** — ISO 8778参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在ISO 8778中定义为293.15 K。

仅当您使用的声速导值是在不同参考值下获得时，才需要调整ISO参考参数值。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **ISO reference density** — ISO 8778参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在ISO 8778中定义为1.185 kg/m3。

仅当您使用的声速导值是在不同参考值下获得时，才需要调整ISO参考参数值。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Sonic conductance`。

### **Maximum orifice area** — 对应于组件最大开启状态的流动面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积达到最大时节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Orifice area`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围[0,1]内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将**Valve parameterization**设置为`Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围[0,1]内的正标量

连续平滑因子，在节流孔接近打开或接近关闭位置时为流动响应引入一层渐变。将此参数设置为小于1的非零值，以提高这些工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间过渡的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间过渡的压力比。压力比为出口压力除以入口压力。典型值范围为`0.995`到`0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流动面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。各端口尺寸相同。此参数的值应与阻力元件所连接组件的入口面积相匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b中未记录。

## 扩展功能

### C/C++代码生成 使用Simulink® Coder™生成C和C++代码。

## 版本历史

**在R2018b中引入**

### R2023b：选择额外的温度控制选项

您现在可以使用**Temperature sensing**参数来指定模块用于控制阀门的温度数据。

### R2022b：使用改进的流量计算对气体系统建模

在以前的版本中，气体库中的模块使用转换因子来以声速导实现不同的节流孔参数化。您可以使用**Valve parameterization**参数来指定参数化方法。

新的参数化方法还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替代了**Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow**和**Restriction area at leakage flow**参数。

为提高清晰度：

- **Opening parameterization**参数已重命名为**Opening characteristic**。
- **Reference temperature**和**Reference density**参数已分别重命名为**ISO reference temperature**和**ISO reference density**。
- **Cv coefficient (USCS) at maximum flow**和**Kv coefficient (USCS) at maximum flow**参数已分别重命名为**Maximum Cv coefficient**和**Maximum Kv coefficient**。
- **Sonic conductance at maximum flow**参数已重命名为**Maximum sonic conductance**。

## 描述

气体网络中的温度控制阀

Temperature Control Valve (G)模块表示一个带有恒温器的节流孔，作为流量控制机构。恒温器包含温度传感器和开启机构。传感器位于入口处，对温度变化以一阶时间滞后所捕获的轻微延迟做出响应。

当传感器读取到超过预设激活值的温度时，开启机构启动，阀门开始打开或关闭，具体取决于**Valve operation**参数指定的操作模式。开口面积的变化持续到阀门温度范围的极限，超过该极限后开口面积为常数。在温度范围内，开口面积是温度的线性函数。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力的下降不再能增加速度时，流动阻塞且速度饱和。当背压比达到阀门特有的临界值时发生阻塞。该模块不捕获超声速流动。

### 控制温度

入口处的温度读数是阀门的控制信号。当**Valve operation**为`Opens above activation temperature`时，温度读数超过激活温度越多，开口面积偏离最大关闭状态越多；当**Valve operation**为`Closes above activation temperature`时，开口面积偏离完全打开状态越多。

传感器温度读数与激活温度之间的差值为温度超调量。模块将此变量对阀门的温度调节范围进行归一化。阀门开度分数为

T^=TS-TActΔT，

其中：

- *TAct*是**Activation temperature**参数的值。
- *TS*是传感器温度读数。

  - 当**Temperature sensing**为`Valve inlet temperature`时，*TS*是阀门的上游温度。
  - 当**Temperature sensing**为`Gas sensing port`时，*TS*是气体网络在连接到端口**T**处的温度。
  - 当**Temperature sensing**为`Thermal sensing port`时，*TS*是热网络在连接到端口**T**处的温度。
- *ΔT*是**Temperature regulation range**参数的值。

**数值平滑**

当**Smoothing factor**参数非零时，模块对阀门开度分数T^应用数值平滑。启用平滑有助于在仿真中保持数值鲁棒性。

有关详细信息，请参阅Numerical Smoothing。

**传感器动态特性**

为了模拟真实温度传感器只能逐渐记录温度变化的行为，模块对温度读数*TS*添加一阶时间滞后。该滞后使传感器对温度变化具有瞬态响应。*TS*的表达式为

ddtTS=TIn−TSτ，

其中*TIn*是仿真当前时间步的实际入口温度，*τ*是**Sensor time constant**参数的值。此参数越小，传感器响应越快。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在一定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在一定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速导纳决定模块参数化。声速导纳衡量气体在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

模块按阀门开度比例缩放指定的流通能力。当阀门开度比例从 `0` 上升到 `1` 时，流通能力的度量从其指定的最小值缩放到指定的最大值。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。当 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin，

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是等熵指数与 1.4 之比。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞，模块切换到方程

m˙=23CvN6FγxTpinρin。

当 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时质量流量方程的更多信息，请参阅 [2][3]。

当 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是声速导纳。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口变为阻塞，模块切换到方程

m˙=CρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于空气以外的气体，可能需要按比重的平方根缩放声速导纳。

有关 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时质量流量方程的更多信息，请参阅 [1]。

当 **Orifice parametrization** 设置为 `Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ]，

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1−Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞，模块切换到方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2。

有关 **Orifice parametrization** 参数为 `Orifice area parameterization` 时质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

模块假设阀门内部流体的体积和质量非常小，并忽略这些值。因此，不会有流体在阀门中积聚。根据质量守恒原理，通过一个端口流入阀门的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0，

其中 m˙ 定义为通过 **A** 或 **B** 下标所指示端口流入阀门的质量流量。

### 能量平衡

模块的阻力元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口的过程中，没有对流体做功或由流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 流入阀门的能量流率。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。

### 假设和限制

- `Orifice area` 参数化的方程对于远离理想气体的气体不太准确。
- 此模块不建模超声速流动。
