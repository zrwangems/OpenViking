---
type: simulink-block
title: 'Battery'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'battery'
documentation_source_path: 'ref/battery.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery

## 端口

### 输出

### **q** — 电池电荷水平，C 物理信号

物理信号端口，输出内部电荷，单位为库仑（C）。使用此输出端口可根据电荷改变负载行为，而无需构建电荷状态估计器的复杂性。

#### 依赖关系

要启用此端口，请将 **Expose charge measurement port** 设置为
`Yes`。
### 守恒

### **+** — 正极端子电气

与电池正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电池负极端子关联的电气守恒端口。

### **H** — 电池热质量热

表示电池热质量的热守恒端口。当您暴露此端口时，请提供附加参数以定义第二个温度下的电池行为。有关详细信息，请参阅建模热效应。

#### 依赖关系

要启用此端口，请在 **Thermal Port** 部分中，将 **Thermal
port** 设置为 `Model`。

## 参数

### 主要

### **Nominal voltage, Vnom** — 电池完全充电时的输出电压 `12` `V`（默认）| 正数

电池完全充电时的空载电压。

### **Current directionality** — 启用电流方向性 `Disabled`（默认）| `Enabled`

是否启用电流方向性。如果将此参数设置为 `Enabled`，则端子电阻取决于电流方向。

### **Internal resistance** — 电池内阻 `2` `Ohm`（默认）| 正数

电池的内部连接电阻。

#### 依赖关系

要启用此参数，请将 **Current directionality** 设置为 `Disabled`。

### **Internal resistance during charging** — 充电期间的电池内阻 `2` `Ohm`（默认）| 正数

充电阶段电池的内部连接电阻。

#### 依赖关系

要启用此参数，请将 **Current directionality** 设置为 `Enabled`。

### **Internal resistance during discharging** — 放电期间的电池内阻 `2` `Ohm`（默认）| 正数

放电阶段电池的内部连接电阻。

#### 依赖关系

要启用此参数，请将 **Current directionality** 设置为 `Enabled`。

### **Battery charge capacity** — 选择电池模型 `Infinite`（默认）| `Finite`

选择用于对电池电荷容量建模的选项之一：

- `Infinite` — 电池电压与从电池汲取的电荷无关。
- `Finite` — 电池电压随电荷减少而降低。

### **Cell capacity (Ah rating)** — 完全充电时的标称电池容量 `50` `hr*A`（默认）| 正数

最大（标称）电池电荷，单位为安培小时。要在仿真开始时指定初始电池电荷的目标值，请使用高优先级 **Charge** 变量。有关详细信息，请参阅变量。

#### 依赖关系

要启用此参数，请将 **Battery charge capacity** 设置为
`Finite`。

### **Voltage V1 when charge is AH1** — 电荷水平为 AH1 时的输出电压 `11.5` `V`（默认）| 正数

当电荷水平为 AH1 时的基本电池输出电压，由 **Charge AH1 when no-load voltage is V1** 参数指定。此参数必须小于 **Nominal voltage, Vnom**。

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`。

### **Charge AH1 when no-load voltage is V1** — 空载输出电压为 V1 时的电荷水平 `25` `hr*A`（默认）| 正数

对应于由 **Voltage V1 when charge is AH1** 参数指定的空载输出电压的电池电荷水平。

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`。

### **Self-discharge** — 选择是否对电池的自放电电阻建模 `Disabled`（默认）| `Enabled`

选择是否对电池的自放电电阻建模。该模块将此效应建模为基本电池模型端子两端的电阻器。

随着温度升高，自放电电阻减小，导致自放电增加。如果电阻减小过快，可能会发生电池热失控和数值不稳定。您可以通过执行以下任一操作来解决此问题：

- 减小热阻
- 减小自放电电阻相对于温度的梯度
- 增大自放电电阻

#### 依赖关系

要启用此参数，请将 **Battery charge
capacity** 设置为 `Finite`。

### **Self-discharge resistance** — 表示电池自放电的电阻 `2000` `Ohm`（默认）| 正数

基本电池模型两端的电阻，表示电池自放电。

#### 依赖关系

要启用此参数，请将 **Self-discharge** 设置为
`Enabled`。

### **Measurement temperature** — 测量模块参数时的温度 `298.15` `K`（默认）| 正数

温度 *T1*，在该温度下测量 **Main** 部分中的模块参数。有关详细信息，请参阅建模热效应。

#### 依赖关系

要启用此参数，请在 **Thermal Port** 部分中，将
**Thermal port** 设置为
`Model`。

### **Expose charge measurement port** — 是否暴露电荷测量端口 `No`（默认）| `Yes`

*自 R2023a 起*

是否暴露电荷测量端口并测量电池的内部电荷水平。

### 动态

### **Charge dynamics** — 电池电荷动态模型 `No dynamics`（默认）| `One time-constant dynamics` | `Two time-constant dynamics` | `Three time-constant dynamics` | `Four time-constant dynamics` | `Five time-constant dynamics`

选择如何对电池电荷动态建模。此参数确定等效电路中的并联 RC 段数：

- `No dynamics` — 等效电路不包含并联 RC 段。电池的端子电压与内部充电电压之间没有延迟。
- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。使用 **First time constant** 参数指定时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。使用 **First time constant** 和 **Second time constant** 参数指定时间常数。
- `Three time-constant dynamics` — 等效电路包含三个并联 RC 段。使用 **First time constant**、**Second time constant** 和 **Third time constant** 参数指定时间常数。
- `Four time-constant dynamics` — 等效电路包含四个并联 RC 段。使用 **First time constant**、**Second time constant**、**Third time constant** 和 **Fourth time constant** 参数指定时间常数。
- `Five time-constant dynamics` — 等效电路包含五个并联 RC 段。使用 **First time constant**、**Second time constant**、**Third time constant**、**Fourth time constant** 和 **Fifth time constant** 参数指定时间常数。

### **First polarization resistance** — 第一个 RC 电阻 `0.005` `Ohm`（默认）| 正数

第一个并联 RC 段的电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **First time constant** — 第一个 RC 时间常数 `30` `s`（默认）| 正数

第一个并联 RC 段的时间常数。此值等于 *RC*，并影响 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Second polarization resistance** — 第二个 RC 电阻 `0.005` `Ohm`（默认）| 正数

第二个并联 RC 段的电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Second time constant** — 第二个 RC 时间常数 `30` `s`（默认）| 正数

第二个并联 RC 段的时间常数。此值等于 *RC*，并影响 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Third polarization resistance** — 第三个 RC 电阻 `0.005` `Ohm`（默认）| 正数

第三个并联 RC 段的电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Third time constant** — 第三个 RC 时间常数 `30` `s`（默认）| 正数

第三个并联 RC 段的时间常数。此值等于 *RC*，并影响 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fourth polarization resistance** — 第四个 RC 电阻 `0.005` `Ohm`（默认）| 正数

第四个并联 RC 段的电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fourth time constant** — 第四个 RC 时间常数 `30` `s`（默认）| 正数

第四个并联 RC 段的时间常数。此值等于 *RC*，并影响 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fifth polarization resistance** — 第五个 RC 电阻 `0.005` `Ohm`（默认）| 正数

第五个并联 RC 段的电阻。此参数主要影响 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Five time-constant dynamics`。

### **Fifth time constant** — 第五个 RC 时间常数 `30` `s`（默认）| 正数

第五个并联 RC 段的时间常数。此值等于 *RC*，并影响 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Five time-constant dynamics`。

### 衰减

### **Battery fade** — 选择是否对电池性能随老化的退化建模 `Disabled`（默认）| `Enabled`

选择是否包含电池衰减建模：

- `Disabled` — 电池性能不依赖于老化。
- `Enabled` — 电池性能
  根据已完成的充放电循环次数而变化。选择此选项将在此部分中暴露附加参数，这些参数定义了一定放电循环次数后的电池性能。该模块使用这些参数值来计算缩放系数
  *k1*、
  *k2* 和
  *k3*。有关详细信息，请参阅建模电池衰减。

#### 依赖关系

要启用此参数，请在 **Main** 部分中，将 **Battery
charge capacity** 设置为 `Finite`。
如果 **Battery charge capacity** 为
`Infinite`，则
**Fade** 部分为空。

### **Number of discharge cycles, N** — 定义第二组数据点的循环次数 `100`（默认）| 正数

测量此部分中其他参数所经过的充放电循环次数。此第二组数据点定义了用于建模电池衰减的缩放系数 *k1*、*k2* 和 *k3*。

#### 依赖关系

要启用此参数，请将 **Battery fade** 设置为
`Enabled`。

### **Cell capacity after N discharge cycles** — N 次放电循环后的最大电池容量 `45` `hr*A`（默认）| 正数

在由 **Number of discharge cycles, N** 参数指定的放电循环次数后的最大电池电荷，单位为安培小时。

#### 依赖关系

要启用此参数，请将 **Battery fade** 设置为
`Enabled`。

### **Internal resistance after N discharge cycles** — N 次放电循环后的电池内阻 `2.02` `Ohm`（默认）| 正数

在由 **Number of discharge cycles, N** 参数指定的放电循环次数后的电池内阻。

#### 依赖关系

要启用此参数，请将 **Battery fade** 设置为
`Enabled`，并在
**Main** 部分中，将 **Current
Directionality** 设置为
`Disabled`。

### **Average internal resistance after N discharge cycles** — N 次放电循环后的电池平均内阻 `2.02` `Ohm`（默认）| 正数

在由 **Number of discharge cycles, N** 参数指定的放电循环次数后的电池充电和放电内阻的平均值。

#### 依赖关系

要启用此参数，请将 **Battery fade** 设置为
`Enabled`，并在
**Main** 部分中，将 **Current
Directionality** 设置为
`Enabled`。

### **Voltage V1 at charge AH1 after N discharge cycles** — N 次放电循环后电荷水平为 AH1 时的输出电压 `10.35` `V`（默认）| 正数

在由 **Number of discharge cycles, N** 参数指定的放电循环次数后，电荷水平为 AH1 时的基本电池模型输出电压。

#### 依赖关系

要启用此参数，请将 **Battery fade** 设置为
`Enabled`。

### 日历老化

要暴露这些参数，请在 **Main** 选项卡中，将 **Battery charge capacity** 设置为 `Finite`。

### **Calendar aging** — 日历老化选项 `Disabled`（默认）| `Enabled`

是否启用电池的日历老化。

### **Storage condition** — 存储条件 `Fixed open-circuit voltage`（默认）| `Fixed state of charge`

在存储期间指定开路电压还是荷电状态。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Normalized open-circuit voltage during storage, V/Vnom** — 存储期间的归一化开路电压 `0.9`（默认）| 标量

存储期间的归一化开路电压。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`，并将 **Storage condition** 设置为 `Fixed open-circuit voltage`。

### **Open-circuit measurement temperature** — 开路测量温度 `298.15` `K`（默认）| 正数

开路测量温度。

#### 依赖关系

要启用此参数，请暴露模块热端口，并将 **Calendar aging** 设置为 `Enabled`，将 **Storage condition** 设置为 `Fixed open-circuit voltage`。

### **State of charge during storage (%)** — 存储期间的荷电状态百分比 `60`（默认）| 正数

存储期间的荷电状态，以百分比表示。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`，并将 **Storage condition** 设置为 `Fixed state of charge`。

### **Vector of time intervals** — 时间间隔 `[0]` `d`（默认）| 标量

时间间隔。此参数的大小必须与 **Vector of temperatures** 相等。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Vector of temperatures** — 存储温度 `[273]` `K`（默认）| 标量

存储温度集合。此参数的大小必须与 **Vector of time intervals** 相等。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Linear scaling for voltage, b** — 电压线性缩放 `2.2134e6`（默认）| 标量

开路电压的线性缩放系数。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Constant offset for voltage, c** — 电压恒定偏移 `1.632e6`（默认）| 标量

开路电压的恒定偏移。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Temperature-dependent exponential increase, d** — 温度相关指数增长 `0.515833569` `V`（默认）| 标量

温度相关指数增长。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Time exponent, a** — 时间指数 `0.75`（默认）| 标量

时间指数。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### 温度依赖性

本节仅对具有暴露热端口的模块显示。要暴露热端口，请在 **Thermal Port** 部分中，将 **Thermal port** 设置为 `Model`。有关详细信息，请参阅 Modeling Thermal Effects。

### **Nominal voltage at second measurement temperature** — 电池完全充电时的输出电压 `12` `V`（默认）| 正数

电池在第二测量温度下完全充电时的空载电压。

### **Internal resistance at second measurement temperature** — 电池内阻 `2.2` `Ohm`（默认）| 正数

电池在第二测量温度下的内部连接电阻。

### **Voltage V1 at second measurement temperature** — 充电水平 AH1 时的输出电压 `11.4` `V`（默认）| 正数

基本电池模型在第二测量温度下以及由 **Charge AH1 when no-load voltage is V1** 参数指定的充电水平 AH1 时的输出电压。

#### 依赖关系

要启用此参数，请在 **Main** 部分中，将 **Battery charge capacity** 参数设置为 `Finite`。

### **Self-discharge resistance at second measurement temperature** — 表示电池自放电的电阻 `2200` `Ohm`（默认）| 正数

基本电池模型在第二测量温度下的电阻。此电阻表示自放电。

#### 依赖关系

要启用此参数，请在 **Main** 部分中，将 **Self-discharge resistance** 参数设置为 `Enabled`。

### **First polarization resistance at second measurement temperature** — 第二测量温度下的第一 RC 电阻 `0.005` `Ohm`（默认）| 正数

第一并联 RC 部分在第二测量温度下的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **First time constant at second measurement temperature** — 第二测量温度下的第一 RC 时间常数 `30` `s`（默认）| 正数

第一并联 RC 部分在第二测量温度下的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Second polarization resistance at second measurement temperature** — 第二测量温度下的第二 RC 电阻 `0.005` `Ohm`（默认）| 正数

第二并联 RC 部分在第二测量温度下的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Second time constant at second measurement temperature** — 第二测量温度下的第二 RC 时间常数 `30` `s`（默认）| 正数

第二并联 RC 部分在第二测量温度下的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Third polarization resistance at second measurement temperature** — 第二测量温度下的第三 RC 电阻 `0.005` `Ohm`（默认）| 正数

第三并联 RC 部分在第二测量温度下的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Third time constant at second measurement temperature** — 第二测量温度下的第三 RC 时间常数 `30` `s`（默认）| 正数

第三并联 RC 部分在第二测量温度下的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fourth polarization resistance at second measurement temperature** — 第二测量温度下的第四 RC 电阻 `0.005` `Ohm`（默认）| 正数

第四并联 RC 部分在第二测量温度下的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fourth time constant at second measurement temperature** — 第二测量温度下的第四 RC 时间常数 `30` `s`（默认）| 正数

第四并联 RC 部分在第二测量温度下的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fifth polarization resistance at second measurement temperature** — 第二测量温度下的第五 RC 电阻 `0.005` `Ohm`（默认）| 正数

第五并联 RC 部分在第二测量温度下的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Five time-constant dynamics`。

### **Fifth time constant at second measurement temperature** — 第二测量温度下的第五 RC 时间常数 `30` `s`（默认）| 正数

第五并联 RC 部分在第二测量温度下的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Five time-constant dynamics`。

### **Second measurement temperature** — 测量本节中模块参数时的温度 `273.15` `K`（默认）| 正数

温度 *T*2，即测量 **Temperature Dependence** 部分中模块参数时的温度。有关详细信息，请参阅 Modeling Thermal Effects。

要指定仿真开始时的初始温度，请使用高优先级 **Temperature** 变量。有关详细信息，请参阅 Variables。

### 热端口

### **Thermal port** — 是否暴露热端口 `Omit`（默认）| `Model`

*自 R2023a 起*

是否暴露模块的热端口并仿真电池的热效应。

### **Thermal mass** — 与热端口关联的热质量 `30000` `J/K`（默认）| 正数

与热端口 H 关联的热质量。它表示将热端口温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Model`。

## 所属库

Simscape / Electrical / Sources Simscape / Battery / Cells

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

### R2023a：**Modeling option** 参数已被替换

模块的 **Modeling option** 参数已被移除，并替换为 **Expose charge measurement port** 和 **Thermal port** 参数。要暴露内部电荷输出端口，请将 **Expose charge measurement port** 参数设置为 `Yes`。要暴露热端口并仿真热效应，请将 **Thermal port** 参数设置为 `Model`。

由于此更改，如果您在早期版本中使用 Battery 模块创建了自定义组件，则必须相应地更新该自定义组件。

```
For batteryecm.battery_thermal:
charge_measurement_port=simscape.enum.thermaleffects.model
```

```
For batteryecm.battery_instrumented:
charge_measurement_port=simscape.enum.battery.enable.yes
```

```
For batteryecm.battery_thermal_instrumented:
charge_measurement_port=simscape.enum.thermaleffects.model
charge_measurement_port=simscape.enum.battery.enable.yes
```

## 描述

行为电池模型

Battery 模块表示一个简单的电池模型。您还可以暴露电池的电荷输出端口和热端口。

要测量电池的内部电荷水平，请在 **Main** 部分中，将 **Expose charge measurement port** 设置为 `Yes`。此操作会暴露一个额外的物理信号端口，用于输出内部荷电状态。使用此功能可以根据荷电状态改变负载行为，而无需构建荷电状态估计器的复杂性。

要仿真电池的热效应，请在 **Thermal Port** 部分中，将 **Thermal port** 参数设置为 `Model`。此操作会暴露一个额外的热端口，该端口表示电池热质量。当您选择此选项时，请提供额外参数以定义电池在第二温度下的行为。有关详细信息，请参阅 Modeling Thermal Effects。

电池等效电路由基本电池模型、自放电电阻 *RSD*、充电动态模型和串联电阻 *R0* 组成。

### 电池模型

如果您为 **Battery charge capacity** 参数选择 `Infinite`，则模块将电池建模为串联电阻和恒定电压源。如果您为 **Battery charge capacity** 参数选择 `Finite`，则模块将电池建模为串联电阻和电荷相关电压源。在有限情况下，电压是电荷的函数，并具有以下关系：

V=V0(SOC1−β(1−SOC))

其中：

- `SOC`（荷电状态）是当前电荷与额定电池容量的比值。
- *V*0 是电池在空载下完全充电时的电压，由 **Nominal voltage, Vnom** 参数定义。
- *β* 是一个常数，其计算使得当电荷为 *AH1* 时电池电压为 *V1*。使用模块参数指定电压 *V1* 和电池容量 *AH1*。*AH1* 是空载（开路）电压为 *V1* 时的电荷，且 *V1* 小于标称电压。

该方程定义了电压与剩余电荷之间的近似关系。此近似再现了低电荷值时电压下降速率增加的现象，并确保当电荷水平为零时电池电压变为零。该模型的优点是所需参数很少，且大多数数据表中均可轻松获得。

### 电池衰减建模

对于具有有限电池电荷容量的电池模型，您可以根据放电循环次数对电池性能退化进行建模。这种退化称为*电池衰减*。要启用电池衰减，请将 **Battery fade** 参数设置为 `Enabled`。此设置会在 **Fade** 部分中暴露额外参数。

模块通过根据已完成的放电循环次数缩放您在 **Main** 部分中指定的某些电池参数值来实现电池衰减。模块分别在 **Cell capacity (Ah rating)**、**Internal resistance** 和 **Voltage V1 when charge is AH1** 参数值上使用乘数 *λ*AH、*λ*R0 和 *λ*V1。这些乘数又取决于放电循环次数：

λAH=1−k1N0.5

λR0=1+k2N0.5

λV1=1−k3N

N=N0+1AH∫0ti(t)⋅H(i(t))λAH(t)dt

其中：

- *λAH* 是电池标称容量的乘数。
- *λR0* 是电池串联电阻的乘数。
- *λV1* 是电压 *V1* 的乘数。
- *N* 是已完成的放电循环次数。
- *N0* 是仿真开始前已完成的全放电循环次数。
- *AH* 是电池额定容量，单位为安培小时。
- *i(t)* 是瞬时电池输出电流。
- *H(i(t))* 是瞬时电池输出电流的 Heaviside 函数。如果参数为负，此函数返回 0；如果参数为正，则返回 1。

**注意**

Battery 模块跟踪电流并对其随时间进行积分。每当提取等效电池放电容量时，已完成的放电循环次数 *N* 增加 1。

模块通过将您在 **Fade** 部分中提供的参数值代入这些电池方程来计算系数 *k1*、*k2* 和 *k3*。例如，默认模块参数集对应于以下系数值：

- *k1* = 1e-2
- *k2* = 1e-3
- *k3* = 1e-3

您还可以使用高优先级变量 **Discharge cycles** 根据先前的充放电历史定义仿真的起点。有关详细信息，请参阅 Variables。

### 热效应建模

如果您将 **Thermal port** 参数设置为 `Model`，则必须提供额外参数以定义电池在第二温度下的行为。当您暴露热端口时，电压的扩展方程为：

V=V0T(SOC1−βT(1−SOC))

V0T=V0(1+λV(T−T1))

其中：

- *T* 是电池温度。
- *T1* 是标称测量温度。
- *λV* 是 *V*0 的参数温度依赖系数。
- βT=β[1+λβ(T−T1)]。
- *λβ* 是 *β* 的参数温度依赖系数。
- *β* 的计算方式与电池模型相同，使用温度修正后的标称电压 *V0T*。

内部串联电阻、自放电电阻以及任何充电动态电阻也是温度的函数：

RT=R(1+λR(T−T1))

其中 *λR* 是参数温度依赖系数。

所有温度依赖系数均由您在标称温度和第二测量温度下提供的相应值确定。如果模型中包含充电动态，则时间常数以相同方式随温度变化。

电池温度由模型中包含的所有欧姆损耗之和确定：

MthT˙=∑iVT,i2/RT,i

其中：

- *Mth* 是电池热质量。
- *i* 对应于第 *i* 个欧姆损耗贡献者。根据您配置模块的方式，损耗包括：

  - 串联电阻
  - 自放电电阻
  - 第一充电动态段
  - 第二充电动态段
  - 第三充电动态段
  - 第四充电动态段
  - 第五充电动态段
- *VT,i* 是电阻 *i* 上的电压降。
- *RT,i* 是电阻 *i*。

### 对电荷动态建模

您可以使用 **Charge dynamics** 参数对电池电荷动态建模：

- `No dynamics` — 等效电路不包含并联 RC 段。端子电压与电池内部充电电压之间没有延迟。
- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。使用 **First time constant** 参数指定时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。使用 **First time constant** 和 **Second time constant** 参数指定时间常数。
- `Three time-constant dynamics` — 等效电路包含三个并联 RC 段。使用 **First time constant**、**Second time constant** 和 **Third time constant** 参数指定时间常数。
- `Four time-constant dynamics` — 等效电路包含四个并联 RC 段。使用 **First time constant**、**Second time constant**、**Third time constant** 和 **Fourth time constant** 参数指定时间常数。
- `Five time-constant dynamics` — 等效电路包含五个并联 RC 段。使用 **First time constant**、**Second time constant**、**Third time constant**、**Fourth time constant** 和 **Fifth time constant** 参数指定时间常数。

下图显示了配置为两个时间常数动态的模块的等效电路。

在图中：

- *RRC1* 和 *RRC2* 是并联 RC 电阻。分别使用 **First polarization resistance** 和 **Second polarization resistance** 参数指定这些值。
- *CRC1* 和 *CRC2* 是并联 RC 电容。每个并联段的时间常数 *τ* 通过关系式 C=τ/R 将 *R* 和 *C* 值关联起来。分别使用 **First time constant** 和 **Second time constant** 参数指定每个段的 *τ*。
- *R0* 是串联电阻。使用 **Internal resistance** 参数指定此值。

### 对电池老化建模

对于具有有限电池电荷容量的电池模型，您可以对电池不使用时发生的电池性能退化建模。日历老化同时影响内阻和容量。特别是，电阻增加取决于多种机制，例如在阳极和阴极形成固体电解质界面（SEI）以及集流体腐蚀。这些过程主要取决于存储温度、存储荷电状态和时间。

**注意**

Battery 模块仅在初始化期间应用日历老化。当您将 **Calendar aging** 参数设置为 `Enabled` 时，模块会显示 **Vector of time intervals** 参数，该参数表示电池在仿真开始前已经老化的时间。此选项不涵盖仿真期间的日历老化。

此方程定义了由于日历老化导致的电池端子电阻增加：

αr(T,Voc)=(bVoc−c)e−qdkT,R=R0(1+∑i=1i=nαr(Ti,Voc)(tia−ti−1a)),

其中：

- *Voc* 是 **Normalized open-circuit voltage during storage, V/Vnom**。
- *R0* 是 **Internal resistance**。
- *ti* 是从 **Vector of time intervals** 参数导出的时间样本。
- *Ti* 是从 **Vector of temperatures** 参数导出的。
- *b* 是 **Linear scaling for voltage, b**。
- *c* 是 **Constant offset for voltage, c**。
- *d* 是 **Temperature-dependent exponential increase, d**。
- *a* 是 **Time exponent, a**。
- *q* 是电子的基本电荷，单位为 C。
- *k* 是玻尔兹曼常数，单位为 J/K。

**Simscape Results Explorer** 中的 *R1\_age\_multiplier* 变量以电阻增加的形式存储电池的日历老化：

R1\_age\_multiplier=RR0。

对于模块的热建模选项，如果您将 **Storage condition** 参数设置为 `Fixed open-circuit voltage`，则必须指定额外的 **Open-circuit voltage measurement temperature** 参数，以将存储开路电压转换为存储期间与温度无关的荷电状态：

SOC=OCV(1−β(TOCVmeasurement))1−β(TOCVmeasurement)OCV。

然后，根据存储温度的开路电压由以下方程定义：

OCVTstorage=SOC1−β(Tstorage)(1−β(Tstorage)SOC)。

最后，此方程定义了根据存储温度由于日历老化导致的电池端子电阻增加：

R=R0(1+∑i=1i=nαr(Tstoragei,OCVTstoragei)(tia−ti−1a))。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

当您对电池衰减建模时，**Discharge cycles** 变量允许您指定仿真开始前已完成的充放电循环次数。如果您禁用电池衰减建模，则模块不使用此变量。

### 绘制基本电压-电荷特性

您可以在不构建完整模型的情况下绘制 Battery 模块的基本电压-电荷特性。使用这些图来探究您的参数选择对设备特性的影响。如果您根据数据表对模块进行参数化，可以将图与数据表进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整的工作模型但不知道使用哪个制造部件，可以将图与数据表进行比较以帮助您做出决定。

要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Battery** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅 Plot Basic Voltage-Charge Characteristics of Battery Blocks。

### 假设和限制

- 假设自放电电阻不强烈依赖于放电循环次数。
- 对于电池的热建模选项，您仅提供参考温度运行的衰减数据。模块将相同的导出 *λAH*、*λR0* 和 *λV1* 乘数应用于对应于第二温度的参数值。
- 使用热模块建模选项时，在超出由 **Measurement temperature** 和 **Second measurement temperature** 值界定的温度范围之外的温度下运行时要小心。模块对导出的方程系数使用线性插值，在指定范围之外仿真结果可能变得非物理。模块检查内部串联电阻、自放电电阻和标称电压始终保持为正。如果存在违反，模块会发出错误消息。
