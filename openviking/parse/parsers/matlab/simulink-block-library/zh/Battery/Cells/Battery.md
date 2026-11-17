---
type: simulink-block
title: 'Battery'
family: 'cells'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cells'
documentation_page: 'battery'
documentation_source_path: 'ref/battery.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery

## 端口

### 输出

### **q** — 电池电荷水平，C 物理信号

物理信号端口，输出内部电荷，单位为库仑 (C)。使用此输出端口可根据电荷改变负载行为，而无需构建荷电状态估计器的复杂性。

#### 依赖关系

要启用此端口，请将 **Expose charge measurement port** 设置为 `Yes`。

### 守恒

### **+** — 正极端子电气

与电池正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电池负极端子关联的电气守恒端口。

### **H** — 电池热质量热

表示电池热质量的热守恒端口。当您暴露此端口时，请提供额外参数以定义电池在第二个温度下的行为。有关详细信息，请参阅 Modeling Thermal Effects。

#### 依赖关系

要启用此端口，请在 **热端口** 部分中，将 **热端口** 设置为 `Model`。

## 参数

### 主

### **标称电压, Vnom** — 电池完全充电时的输出电压 `12` `V`（默认） | 正数

电池完全充电时其两端的空载电压。

### **电流方向性** — 启用电流方向性 `Disabled`（默认） | `Enabled`

是否启用电流方向性。如果将此参数设置为 `Enabled`，则端子电阻取决于电流方向。

### **内阻** — 电池内阻 `2` `Ohm`（默认） | 正数

电池的内部连接电阻。

#### 依赖关系

要启用此参数，请将 **电流方向性** 设置为 `Disabled`。

### **充电期间的电池内阻** — 充电期间的电池内阻 `2` `Ohm`（默认） | 正数

充电阶段电池的内部连接电阻。

#### 依赖关系

要启用此参数，请将 **电流方向性** 设置为 `Enabled`。

### **放电期间的电池内阻** — 放电期间的电池内阻 `2` `Ohm`（默认） | 正数

放电阶段电池的内部连接电阻。

#### 依赖关系

要启用此参数，请将 **电流方向性** 设置为 `Enabled`。

### **电池电荷容量** — 选择电池模型 `Infinite`（默认） | `Finite`

选择用于对电池电荷容量建模的选项之一：

- `Infinite` — 电池电压与从电池汲取的电荷无关。
- `Finite` — 电池电压随电荷减少而降低。

### **电芯容量 (Ah 额定值)** — 完全充电时的标称电池容量 `50` `hr*A`（默认） | 正数

电池的最大（标称）电荷，单位为安培小时。要在仿真开始时指定初始电池电荷的目标值，请使用高优先级 **Charge** 变量。有关详细信息，请参阅 Variables (Simscape Electrical)。

#### 依赖关系

要启用此参数，请将 **电池电荷容量** 设置为 `Finite`。

### **电荷为 AH1 时的电压 V1** — 电荷水平为 AH1 时的输出电压 `11.5` `V`（默认） | 正数

当电荷水平为 AH1 时，基础电池输出电压，AH1 由 **空载电压为 V1 时的电荷 AH1** 参数指定。此参数必须小于 **标称电压, Vnom**。

#### 依赖关系

要启用此参数，请将 **电池电荷容量** 设置为 `Finite`。

### **空载电压为 V1 时的电荷 AH1** — 空载输出电压为 V1 时的电荷水平 `25` `hr*A`（默认） | 正数

与 **电荷为 AH1 时的电压 V1** 参数指定的空载输出电压对应的电池电荷水平。

#### 依赖关系

要启用此参数，请将 **电池电荷容量** 设置为 `Finite`。

### **自放电** — 选择是否对电池的自放电电阻建模 `Disabled`（默认） | `Enabled`

选择是否对电池的自放电电阻建模。该模块将此效应建模为基础电池模型端子两端的一个电阻器。

随着温度升高，自放电电阻减小，导致自放电增加。如果电阻减小过快，可能会发生电池热失控和数值不稳定性。您可以通过执行以下任一操作来解决此问题：

- 减小热阻
- 减小自放电电阻相对于温度的梯度
- 增大自放电电阻

#### 依赖关系

要启用此参数，请将 **电池电荷容量** 设置为 `Finite`。

### **自放电电阻** — 表示电池自放电的电阻 `2000` `Ohm`（默认） | 正数

基础电池模型两端的电阻，表示电池自放电。

#### 依赖关系

要启用此参数，请将 **自放电** 设置为 `Enabled`。

### **测量温度** — 测量模块参数时的温度 `298.15` `K`（默认） | 正数

温度 *T1*，在此温度下测量 **主** 部分中的模块参数。有关详细信息，请参阅 Modeling Thermal Effects。

#### 依赖关系

要启用此参数，请在 **热端口** 部分中，将 **热端口** 设置为 `Model`。

### **Expose charge measurement port** — 是否暴露电荷测量端口 `No`（默认） | `Yes`

*自 R2023a 起*

是否暴露电荷测量端口并测量电池的内部电荷水平。

### 动态

### **电荷动态** — 电池电荷动态模型 `No dynamics`（默认） | `One time-constant dynamics` | `Two time-constant dynamics` | `Three time-constant dynamics` | `Four time-constant dynamics` | `Five time-constant dynamics`

选择如何对电池电荷动态建模。此参数确定等效电路中并联 RC 段的数量：

- `No dynamics` — 等效电路不包含并联 RC 段。电池端子电压与内部充电电压之间没有延迟。
- `One time-constant dynamics` — 等效电路包含一个并联 RC 段。使用 **第一时间常数** 参数指定时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 段。使用 **第一时间常数** 和 **第二时间常数** 参数指定时间常数。
- `Three time-constant dynamics` — 等效电路包含三个并联 RC 段。使用 **第一时间常数**、**第二时间常数** 和 **第三时间常数** 参数指定时间常数。
- `Four time-constant dynamics` — 等效电路包含四个并联 RC 段。使用 **第一时间常数**、**第二时间常数**、**第三时间常数** 和 **第四时间常数** 参数指定时间常数。
- `Five time-constant dynamics` — 等效电路包含五个并联 RC 段。使用 **第一时间常数**、**第二时间常数**、**第三时间常数**、**第四时间常数** 和 **第五时间常数** 参数指定时间常数。

### **第一极化电阻** — 第一 RC 电阻 `0.005` `Ohm`（默认） | 正数

第一个并联 RC 段的电阻。此参数主要影响该 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第一时间常数** — 第一 RC 时间常数 `30` `s`（默认） | 正数

第一个并联 RC 段的时间常数。此值等于 *RC* 并影响该 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第二极化电阻** — 第二 RC 电阻 `0.005` `Ohm`（默认） | 正数

第二个并联 RC 段的电阻。此参数主要影响该 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第二时间常数** — 第二 RC 时间常数 `30` `s`（默认） | 正数

第二个并联 RC 段的时间常数。此值等于 *RC* 并影响该 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第三极化电阻** — 第三 RC 电阻 `0.005` `Ohm`（默认） | 正数

第三个并联 RC 段的电阻。此参数主要影响该 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第三时间常数** — 第三 RC 时间常数 `30` `s`（默认） | 正数

第三个并联 RC 段的时间常数。此值等于 *RC* 并影响该 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第四极化电阻** — 第四 RC 电阻 `0.005` `Ohm`（默认） | 正数

第四个并联 RC 段的电阻。此参数主要影响该 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第四时间常数** — 第四 RC 时间常数 `30` `s`（默认） | 正数

第四个并联 RC 段的时间常数。此值等于 *RC* 并影响该 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **第五极化电阻** — 第五 RC 电阻 `0.005` `Ohm`（默认） | 正数

第五个并联 RC 段的电阻。此参数主要影响该 RC 段的欧姆损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Five time-constant dynamics`。

### **第五时间常数** — 第五 RC 时间常数 `30` `s`（默认） | 正数

第五个并联 RC 段的时间常数。此值等于 *RC* 并影响该 RC 段的动态。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Five time-constant dynamics`。

### 衰减

### **电池衰减** — 选择是否对电池性能随老化的退化建模 `Disabled`（默认） | `Enabled`

选择是否包括电池衰减建模：

- `Disabled` — 电池性能不依赖于老化。
- `Enabled` — 电池性能取决于已完成的充放电循环次数。选择此选项会暴露此部分中的额外参数，这些参数定义一定数量的放电循环后的电池性能。该模块使用这些参数值计算缩放系数 *k1*、*k2* 和 *k3*。有关详细信息，请参阅 Modeling Battery Fade。

#### 依赖关系

要启用此参数，请在 **主** 部分中，将 **电池电荷容量** 设置为 `Finite`。如果 **电池电荷容量** 为 `Infinite`，则 **衰减** 部分为空。

### **放电循环次数, N** — 定义第二组数据点的循环次数 `100`（默认） | 正数

测量此部分中其他参数之前所经过的充放电循环次数。这第二组数据点定义用于电池衰减建模的缩放系数 *k1*、*k2* 和 *k3*。

#### 依赖关系

要启用此参数，请将 **电池衰减** 设置为 `Enabled`。

### **N 次放电循环后的电芯容量** — N 次放电循环后的最大电池容量 `45` `hr*A`（默认） | 正数

在 **放电循环次数, N** 参数指定的放电循环次数后，电池的最大电荷，单位为安培小时。

#### 依赖关系

要启用此参数，请将 **电池衰减** 设置为 `Enabled`。

### **N 次放电循环后的内阻** — N 次放电循环后的电池内阻 `2.02` `Ohm`（默认） | 正数

在 **放电循环次数, N** 参数指定的放电循环次数后的电池内阻。

#### 依赖关系

要启用此参数，请将 **电池衰减** 设置为 `Enabled`，并在 **主** 部分中，将 **电流方向性** 设置为 `Disabled`。

### **N 次放电循环后的平均内阻** — N 次放电循环后的电池平均内阻 `2.02` `Ohm`（默认） | 正数

在 **放电循环次数, N** 参数指定的放电循环次数后，电池充电和放电内阻的平均值。

#### 依赖关系

要启用此参数，请将 **电池衰减** 设置为 `Enabled`，并在 **主** 部分中，将 **电流方向性** 设置为 `Enabled`。

### **N 次放电循环后电荷为 AH1 时的电压 V1** — N 次放电循环后电荷水平为 AH1 时的输出电压 `10.35` `V`（默认） | 正数

在 **放电循环次数, N** 参数指定的放电循环次数后，基础电池模型在电荷水平 AH1 时的输出电压。

#### 依赖关系

要启用此参数，请将 **电池衰减** 设置为 `Enabled`。

### 日历老化

要暴露这些参数，请在 **主** 选项卡中，将 **电池电荷容量** 设置为 `Finite`。

### **日历老化** — 日历老化选项 `Disabled`（默认） | `Enabled`

是否启用电池的日历老化。

### **存储条件** — 存储条件 `Fixed open-circuit voltage`（默认） | `Fixed state of charge`

是否指定存储期间的开路电压或荷电状态。

#### 依赖关系

要启用此参数，请将 **日历老化** 设置为 `Enabled`。

### **存储期间的归一化开路电压, V/Vnom** — 存储期间的归一化开路电压 `0.9`（默认） | 标量

存储期间的归一化开路电压。

#### 依赖关系

要启用此参数，请将 **日历老化** 设置为 `Enabled`，并将 **存储条件** 设置为 `Fixed open-circuit voltage`。

### **开路测量温度** — 开路测量温度 `298.15` `K`（默认） | 正数

开路测量温度。

#### 依赖关系

要启用此参数，请暴露模块热端口，并将 **日历老化** 设置为 `Enabled`，将 **存储条件** 设置为 `Fixed open-circuit voltage`。

### **存储期间的荷电状态 (%)** — 存储期间的荷电状态百分比 `60`（默认） | 正数

存储期间的荷电状态，以百分比表示。

#### 依赖关系

要启用此参数，请将 **日历老化** 设置为 `Enabled`，并将 **存储条件** 设置为 `Fixed state of charge`。

### **时间间隔向量** — 时间间隔 `[0]` `d`（默认） | 标量

时间间隔。此参数的大小必须与 **温度向量** 相同。

#### 依赖关系

要启用此参数，请将 **日历老化** 设置为 `Enabled`。

### **温度向量** — 存储温度 `[273]` `K`（默认） | 标量

存储温度集合。此参数的大小必须与 **时间间隔向量** 相同。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Linear scaling for voltage, b** — 电压线性缩放 `2.2134e6`（默认） | scalar

开路电压的线性缩放系数。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Constant offset for voltage, c** — 电压常数偏移 `1.632e6`（默认） | scalar

开路电压的常数偏移。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Temperature-dependent exponential increase, d** — 温度依赖的指数增长 `0.515833569` `V`（默认） | scalar

温度依赖的指数增长。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### **Time exponent, a** — 时间指数 `0.75`（默认） | scalar

时间指数。

#### 依赖关系

要启用此参数，请将 **Calendar aging** 设置为 `Enabled`。

### 温度依赖性

本节仅适用于具有暴露热端口的模块。要暴露热端口，请在 **Thermal Port** 部分将 **Thermal port** 设置为 `Model`。有关详细信息，请参阅 Modeling Thermal Effects。

### **Nominal voltage at second measurement temperature** — 电池完全充电时的输出电压 `12` `V`（默认） | positive number

在第二测量温度下，电池完全充电时电池两端的空载电压。

### **Internal resistance at second measurement temperature** — 电池内阻 `2.2` `Ohm`（默认） | positive number

电池在第二测量温度下的内部连接电阻。

### **Voltage V1 at second measurement temperature** — 充电水平 AH1 下的输出电压 `11.4` `V`（默认） | positive number

在第二测量温度和充电水平 AH1 下，基本电池模型的输出电压，由 **Charge AH1 when no-load voltage is V1** 参数指定。

#### 依赖关系

要启用此参数，请在 **Main** 部分将 **Battery charge capacity** 参数设置为 `Finite`。

### **Self-discharge resistance at second measurement temperature** — 表示电池自放电的电阻 `2200` `Ohm`（默认） | positive number

在第二测量温度下，基本电池模型两端的电阻。此电阻表示自放电。

#### 依赖关系

要启用此参数，请在 **Main** 部分将 **Self-discharge resistance** 参数设置为 `Enabled`。

### **First polarization resistance at second measurement temperature** — 第二测量温度下的第一个 RC 电阻 `0.005` `Ohm`（默认） | positive number

第二测量温度下第一个并联 RC 段的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **First time constant at second measurement temperature** — 第二测量温度下的第一个 RC 时间常数 `30` `s`（默认） | positive number

第二测量温度下第一个并联 RC 段的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `One time-constant dynamics`、`Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Second polarization resistance at second measurement temperature** — 第二测量温度下的第二个 RC 电阻 `0.005` `Ohm`（默认） | positive number

第二测量温度下第二个并联 RC 段的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Second time constant at second measurement temperature** — 第二测量温度下的第二个 RC 时间常数 `30` `s`（默认） | positive number

第二测量温度下第二个并联 RC 段的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Two time-constant dynamics`、`Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Third polarization resistance at second measurement temperature** — 第二测量温度下的第三个 RC 电阻 `0.005` `Ohm`（默认） | positive number

第二测量温度下第三个并联 RC 段的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Third time constant at second measurement temperature** — 第二测量温度下的第三个 RC 时间常数 `30` `s`（默认） | positive number

第二测量温度下第三个并联 RC 段的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Three time-constant dynamics`、`Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fourth polarization resistance at second measurement temperature** — 第二测量温度下的第四个 RC 电阻 `0.005` `Ohm`（默认） | positive number

第二测量温度下第四个并联 RC 段的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fourth time constant at second measurement temperature** — 第二测量温度下的第四个 RC 时间常数 `30` `s`（默认） | positive number

第二测量温度下第四个并联 RC 段的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Four time-constant dynamics` 或 `Five time-constant dynamics`。

### **Fifth polarization resistance at second measurement temperature** — 第二测量温度下的第五个 RC 电阻 `0.005` `Ohm`（默认） | positive number

第二测量温度下第五个并联 RC 段的电阻。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Five time-constant dynamics`。

### **Fifth time constant at second measurement temperature** — 第二测量温度下的第五个 RC 时间常数 `30` `s`（默认） | positive number

第二测量温度下第五个并联 RC 段的时间常数。

#### 依赖关系

要启用此参数，请将 **Charge dynamics** 设置为 `Five time-constant dynamics`。

### **Second measurement temperature** — 本节中模块参数的测量温度 `273.15` `K`（默认） | positive number

温度 *T*2，即测量 **Temperature Dependence** 部分中模块参数时的温度。有关详细信息，请参阅 Modeling Thermal Effects (Simscape Electrical)。

要指定仿真开始时的初始温度，请使用高优先级 **Temperature** 变量。有关详细信息，请参阅 Variables (Simscape Electrical)。

### 热端口

### **Thermal port** — 是否暴露热端口 `Omit`（默认） | `Model`

*自 R2023a 起*

是否暴露模块的热端口并仿真电池的热效应。

### **Thermal mass** — 与热端口关联的热质量 `30000` `J/K`（默认） | positive number

与热端口 H 关联的热质量。它表示使热端口温度升高一度所需的能量。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Model`。

## 所属库

Simscape / Electrical / Sources Simscape / Battery / Cells

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

### R2023a：**Modeling option** 参数已被替换

模块的 **Modeling option** 参数已移除，并替换为 **Expose charge measurement port** 和 **Thermal port** 参数。要暴露内部电荷输出端口，请将 **Expose charge measurement port** 参数设置为 `Yes`。要暴露热端口并仿真热效应，请将 **Thermal port** 参数设置为 `Model`。

由于此更改，如果您在较早版本中使用 Battery 模块创建了自定义组件，则必须相应地更新该自定义组件。

    For batteryecm.battery_thermal:
    charge_measurement_port=simscape.enum.thermaleffects.model

    For batteryecm.battery_instrumented:
    charge_measurement_port=simscape.enum.battery.enable.yes

    For batteryecm.battery_thermal_instrumented:
    charge_measurement_port=simscape.enum.thermaleffects.model
    charge_measurement_port=simscape.enum.battery.enable.yes

## 描述

行为电池模型

Battery 模块表示一个简单的电池模型。您还可以暴露电池的电荷输出端口和热端口。

要测量电池的内部电荷水平，请在 **Main** 部分将 **Expose charge measurement port** 设置为 `Yes`。此操作会暴露一个额外的物理信号端口，用于输出内部荷电状态。使用此功能可根据荷电状态改变负载行为，而无需构建荷电状态估计器的复杂性。

要仿真电池的热效应，请在 **Thermal Port** 部分将 **Thermal port** 参数设置为 `Model`。此操作会暴露一个额外的热端口，该端口表示电池热质量。选择此选项时，请提供其他参数来定义电池在第二温度下的行为。有关详细信息，请参阅 Modeling Thermal Effects。

电池等效电路由基本电池模型、自放电电阻 *RSD*、电荷动态模型和串联电阻 *R0* 组成。

### 电池模型

如果您为 **Battery charge capacity** 参数选择 `Infinite`，则模块将电池建模为串联电阻和恒定电压源。如果您为 **Battery charge capacity** 参数选择 `Finite`，则模块将电池建模为串联电阻和电荷相关电压源。在有限情况下，电压是电荷的函数，并具有以下关系：

V=V0(SOC1−β(1−SOC))

其中：

- `SOC`（state-of-charge）是当前电荷与额定电池容量的比率。
- *V*0 是电池在空载且完全充电时的电压，由 **Nominal voltage, Vnom** 参数定义。
- *β* 是一个常数，其计算使得当电荷为 *AH1* 时电池电压为 *V1*。使用模块参数指定电压 *V1* 和电池容量 *AH1*。*AH1* 是空载（开路）电压为 *V1* 时的电荷，且 *V1* 小于标称电压。

该方程定义了电压与剩余电荷之间的近似关系。此近似再现了低电荷值下电压下降速率增加的现象，并确保当电荷水平为零时电池电压变为零。此模型的优点是所需参数很少，而这些参数在大多数数据表中很容易获得。

### 电池衰减建模

对于具有有限电池电荷容量的电池模型，您可以根据放电循环次数对电池性能劣化进行建模。这种劣化称为 *battery fade*。要启用电池衰减，请将 **Battery fade** 参数设置为 `Enabled`。此设置会在 **Fade** 部分中暴露其他参数。

模块通过根据已完成的放电循环次数缩放您在 **Main** 部分指定的某些电池参数值来实现电池衰减。模块分别在 **Cell capacity (Ah rating)**、**Internal resistance** 和 **Voltage V1 when charge is AH1** 参数值上使用乘数 *λ*AH、*λ*R0 和 *λ*V1。这些乘数又取决于放电循环次数：

λAH=1−k1N0.5

λR0=1+k2N0.5

λV1=1−k3N

N=N0+1AH∫0ti(t)⋅H(i(t))λAH(t)dt

其中：

- *λAH* 是电池标称容量的乘数。
- *λR0* 是电池串联电阻的乘数。
- *λV1* 是电压 *V1* 的乘数。
- *N* 是已完成的放电循环次数。
- *N0* 是仿真开始前已完成的完整放电循环次数。
- *AH* 是以安培小时为单位的额定电池容量。
- *i(t)* 是瞬时电池输出电流。
- *H(i(t))* 是瞬时电池输出电流的 Heaviside 函数。如果自变量为负，此函数返回 0；如果自变量为正，则返回 1。

**注意**

Battery 模块跟踪电流并对其随时间积分。每当提取等效电池放电容量时，已完成的放电循环次数 *N* 增加 1。

模块通过将您在 **Fade** 部分提供的参数值代入这些电池方程来计算系数 *k1*、*k2* 和 *k3*。例如，默认模块参数集对应以下系数值：

- *k1* = 1e-2
- *k2* = 1e-3
- *k3* = 1e-3

您还可以通过使用高优先级变量 **Discharge cycles**，基于先前的充放电历史为仿真定义起点。有关详细信息，请参阅 Variables (Simscape Electrical)。

### 热效应建模

如果您将 **Thermal port** 参数设置为 `Model`，则必须提供其他参数来定义电池在第二温度下的行为。暴露热端口时，电压的扩展方程为：

V=V0T(SOC1−βT(1−SOC))

V0T=V0(1+λV(T−T1))

其中：

- *T* 是电池温度。
- *T1* 是标称测量温度。
- *λV* 是 *V*0 的参数温度依赖系数。
- βT=β[1+λβ(T−T1)].
- *λβ* 是 *β* 的参数温度依赖系数。
- *β* 的计算方式与 Battery Model 中相同，使用
  温度修正后的标称电压
  *V0T*。

内部串联电阻、自放电电阻以及任何电荷动态电阻也是温度的函数：

RT=R(1+λR(T−T1))

其中 *λR* 是参数温度依赖系数。

所有温度依赖系数均由您在标称温度和第二测量温度下提供的对应值确定。如果您在模型中包含电荷动态，则时间常数以相同方式随温度变化。

电池温度由模型中包含的所有欧姆损耗之和确定：

MthT˙=∑iVT,i2/RT,i

其中：

- *Mth* 是电池热质量。
- *i* 对应于第 *i* 个欧姆损耗贡献项。根据您配置模块的方式，损耗包括：

  - 串联电阻
  - 自放电电阻
  - 第一个电荷动态段
  - 第二个电荷动态段
  - 第三个电荷动态段
  - 第四个电荷动态段
  - 第五个电荷动态段
- *VT,i* 是电阻 *i* 两端的电压降。
- *RT,i* 是电阻 *i*。

### 建模充电动态

您可以使用 **Charge dynamics** 参数对电池充电动态进行建模：

- `No dynamics` — 等效电路不包含并联 RC 部分。电池的端电压与内部充电电压之间没有延迟。
- `One time-constant dynamics` — 等效电路包含一个并联 RC 部分。使用 **First time constant** 参数指定时间常数。
- `Two time-constant dynamics` — 等效电路包含两个并联 RC 部分。使用 **First time constant** 和 **Second time constant** 参数指定时间常数。
- `Three time-constant dynamics` — 等效电路包含三个并联 RC 部分。使用 **First time constant**、**Second time constant** 和 **Third time constant** 参数指定时间常数。
- `Four time-constant dynamics` — 等效电路包含四个并联 RC 部分。使用 **First time constant**、**Second time constant**、**Third time constant** 和 **Fourth time constant** 参数指定时间常数。
- `Five time-constant dynamics` — 等效电路包含五个并联 RC 部分。使用 **First time constant**、**Second time constant**、**Third time constant**、**Fourth time constant** 和 **Fifth time constant** 参数指定时间常数。

下图展示了配置为 two time-constant dynamics 的模块的等效电路。

图中：

- *RRC1* 和 *RRC2* 是并联 RC 电阻。分别使用 **First polarization resistance** 和 **Second polarization resistance** 参数指定这些值。
- *CRC1* 和 *CRC2* 是并联 RC 电容。每个并联部分的时间常数 *τ* 通过关系式 C=τ/R 关联 *R* 和 *C* 值。分别使用 **First time constant** 和 **Second time constant** 参数为每个部分指定 *τ*。
- *R0* 是串联电阻。使用 **Internal resistance** 参数指定该值。

### 建模电池老化

对于具有有限电池充电容量的电池模型，您可以对电池未使用时发生的电池性能退化进行建模。日历老化会影响内阻和容量。具体而言，电阻增加取决于多种机制，例如在阳极和阴极形成固体电解质界面（SEI）以及集流体腐蚀。这些过程主要取决于存储温度、存储荷电状态和时间。

**注意**

Battery 模块仅在初始化期间应用日历老化。当您将 **Calendar aging** 参数设置为 `Enabled` 时，该模块会显示 **Vector of time intervals** 参数，该参数表示电池在仿真开始之前已老化的时间。此选项不涵盖仿真期间的日历老化。

此方程定义由于日历老化导致的电池端子电阻增加：

αr(T,Voc)=(bVoc−c)e−qdkT,R=R0(1+∑i=1i=nαr(Ti,Voc)(tia−ti−1a)),

式中：

- *Voc* 是 **Normalized open-circuit voltage during storage, V/Vnom**。
- *R0* 是 **Internal resistance**。
- *ti* 是从 **Vector of time intervals** 参数导出的时间采样。
- *Ti* 从 **Vector of temperatures** 参数导出。
- *b* 是 **Linear scaling for voltage, b**。
- *c* 是 **Constant offset for voltage, c**。
- *d* 是 **Temperature-dependent exponential increase, d**。
- *a* 是 **Time exponent, a**。
- *q* 是电子的基本电荷，单位为 C。
- *k* 是玻尔兹曼常数，单位为 J/K。

**Simscape Results Explorer** 中的 *R1\_age\_multiplier* 变量以电阻增加的形式存储电池的日历老化：

R1\_age\_multiplier=RR0.

对于模块的热建模选项，如果您将 **Storage condition** 参数设置为 `Fixed open-circuit voltage`，则必须指定额外的 **Open-circuit voltage measurement temperature** 参数，以将存储开路电压转换为与温度无关的存储荷电状态：

SOC=OCV(1−β(TOCVmeasurement))1−β(TOCVmeasurement)OCV.

然后，根据存储温度的开路电压由以下方程定义：

OCVTstorage=SOC1−β(Tstorage)(1−β(Tstorage)SOC).

最后，此方程根据存储温度定义由于日历老化导致的电池端子电阻增加：

R=R0(1+∑i=1i=nαr(Tstoragei,OCVTstoragei)(tia−ti−1a)).

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

当您对电池衰减建模时，**Discharge cycles** 变量允许您指定仿真开始前已完成的充放电循环次数。如果您禁用电池衰减建模，则该模块不使用此变量。

### 绘制基本电压-电荷特性

您无需构建完整模型即可绘制 Battery 模块的基本电压-电荷特性。使用这些图可探究参数选择对器件特性的影响。如果您根据数据手册对模块进行参数化，则可以将图与数据手册进行比较，以检查模块参数化是否正确。如果您有完整的工作模型但不知道要使用哪个制造部件，则可以将图与数据手册进行比较以帮助决策。

要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Battery** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅 Plot Basic Voltage-Charge Characteristics of Battery Blocks (Simscape Electrical)。

### 假设和限制

- 假设自放电电阻不强烈依赖于放电循环次数。
- 对于电池的热建模选项，您仅提供参考温度运行下的衰减数据。该模块将相同的派生 *λAH*、*λR0* 和 *λV1* 乘数应用于对应于第二温度的参数值。
- 使用热模块建模选项时，在 **Measurement temperature** 和 **Second measurement temperature** 值所限定的温度范围之外运行时要小心。该模块对推导的方程系数使用线性插值，在指定范围之外仿真结果可能变得非物理。该模块会检查内部串联电阻、自放电电阻和标称电压始终保持为正。如果存在违反，该模块会发出错误消息。
