---
type: simulink-block
title: 'DC-DC Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'dcdcconverter'
documentation_source_path: 'ref/dcdcconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# DC-DC Converter

## 端口

### 守恒端口

### **1+** — 输入正极端口 electrical

与输入侧正极端子关联的电气守恒端口。

### **1-** — 输入负极端口 electrical

与输入侧负极端子关联的电气守恒端口。

### **2+** — 输出正极端口 electrical

与输出侧正极端子关联的电气守恒端口。

### **2-** — 输出负极端口 electrical

与输出侧负极端子关联的电气守恒端口。

### **Vref** — 电压参考 physical

提供外部电压参考信号的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Voltage Reference** 参数设置为 `External`。

### **H** — 热质量 thermal

表示热质量的热守恒端口。当您暴露此端口时，需要提供额外参数来定义第二个温度下的电池行为。有关详细信息，请参阅热参数。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对热参数进行建模。

### 主参数

### **Voltage reference** — 电压参考 `Internal`（默认）| `External`

是在内部还是外部对电压参考进行建模。

### **Output voltage reference demand** — 电压设定点 `10` `V`（默认）

电压调节器的设定点，以及无输出电流时的输出电压值。

#### 依赖关系

此端口仅在 **Voltage Reference** 参数设置为 `Internal` 时可见。

### **Rated output power** — 额定功率 `10` `W`（默认）

给出百分比效率值所对应的输出功率。如果以百分比形式指定下垂，此参数也用于计算下垂 *D*。

### **Enable droop** — 下垂选项 `On`（默认）| `Off`

是否启用电压下垂。

### **Droop parameterization** — 下垂模型 `By voltage droop with output current`（默认）| `By percent voltage droop at rated load`

选择以下下垂参数化方法之一：

- `By voltage droop with output current` — 指定下垂的绝对值 *D*。这是默认选项。
- `By percent voltage droop at rated load` — 以额定负载下的百分比形式指定下垂 *D*。

#### 依赖关系

要启用此参数，请选择 **Enable droop** 参数。

### **Output voltage droop with output current** — 1 A 时的电压下垂 `0.1` `V/A`（默认）

输出电流为 1 A 时，输出电压相对于设定点下降的伏特数。

#### 依赖关系

要启用此参数，请选择 **Enable droop** 参数并将 **Droop parameterization** 设置为 `By voltage droop with output current`。

### **Voltage droop percent at rated load** — 额定负载下的电压下垂百分比 `2`（默认）

在提供额定负载时，电压相对于标称输出电压下降的百分比。如果将 **Voltage reference** 参数设置为 `Internal`，模块使用 **Output voltage reference demand** 参数来计算下垂百分比。如果将 **Voltage reference** 参数设置为 `External`，模块则使用 **Voltage reference used to calculate droop percent** 参数。

#### 依赖关系

要启用此参数，请选择 **Enable droop** 参数并将 **Droop parameterization** 设置为 `By percent voltage droop at rated load`。

### **Voltage reference used to calculate droop percent** — 额定负载下的电压下垂百分比 `10` `V`（默认）

**Voltage droop percent at rated load** 参数在仿真期间用于计算电压下垂的电压参考。

#### 依赖关系

要启用此参数：

- 将 **Voltage reference** 设置为 `External`。
- 选择 **Enable droop** 参数。
- 将 **Droop parameterization** 设置为 `By percent voltage droop at rated load`。

### **Power direction** — 功率流向 `Unidirectional power flow from supply to regulated side`（默认）| `Bidirectional power flow`

选择以下功率转换方向方法之一：

- `Unidirectional power flow from supply to regulated side` — 大多数小功率调节器是单向的。这是默认选项。
- `Bidirectional power flow` — 较大的功率转换器可以是双向的，例如电动汽车中用于实现再生制动的转换器。

### **Diode off-state conductance** — 单向二极管 `1e-8` `1/Ohm`（默认）

在单向配置中，输出侧集成的理想二极管用于防止电流被强制流入转换器。

### 损耗

### **Converter losses at zero output power** — 恒定损耗 `1` `W`（默认）

等效电路图中 Pfixed 组件消耗的功率，对应于与负载电流无关的转换器损耗。

### **Converter losses** — 转换器损耗 `Assume proportional to square of output current`（默认）| `Tabulate efficiency`

转换器损耗参数化。

### **Percentage efficiency at rated output power** — 额定效率 `80`（默认）

效率定义为输出负载功率除以输入电源功率的 100 倍。

#### 依赖关系

要启用此参数，请将 **Converter losses** 设置为 `Assume proportional to square of output current`。

### **Variables for tabulation** — 制表变量 `Output current`（默认）| `Output current and input voltage` | `Output current and temperature` | `Output current, input voltage, and temperature`

是否根据输出电流、输入电压和温度来制表效率。要启用温度选项，需要暴露模块的热端口。

### **Vector of output currents for tabulated efficiencies, I2** — 制表效率的输出电流 `[-2, -1, 1, 2]` `A`（默认）| 正递增标量向量

制表效率的输出电流向量。此参数的大小必须大于或等于 `3`，并且与 **Percentage efficiency table, eff(I)** 的大小相等。

#### 依赖关系

要启用此参数，请将 **Converter losses** 设置为 `Tabulate efficiency`。

### **Percentage efficiency table, eff(I2)** — 电流函数形式的效率表 `[66, 76, 80, 74]`（默认）| 正标量向量

以百分比表示的电流函数形式的效率表。此参数的大小必须与 **Vector of output currents for tabulated efficiencies, I2** 的大小相等。

#### 依赖关系

要启用此参数，请将 **Converter losses** 设置为 `Tabulate efficiency`，并将 **Variables for tabulation** 设置为 `Output current`。

### **Vector of input voltages for tabulated efficiencies, V1** — 制表效率的输入电压 `[15, 30, 45]` `V`（默认）| 正递增标量向量

制表效率的输入电压向量。此参数的大小必须大于或等于 `2`。

#### 依赖关系

要启用此参数，请将 **Converter losses** 设置为 `Tabulate efficiency`，并将 **Variables for tabulation** 设置为 `Output current and input voltage` 或 `Output current, input voltage, and temperature`。

### **Percentage efficiency table, eff(I2,V1)** — 电流和电压函数形式的效率表 `[66, 66, 66; 76, 76, 76; 80, 80, 80; 74, 74, 74]`（默认）| 正标量向量

以百分比表示的电流函数形式的效率表。

#### 依赖关系

要启用此参数，请将 **Converter losses** 设置为 `Tabulate efficiency`，并将 **Variables for tabulation** 设置为 `Output current`。

### **Vector of temperatures for tabulated efficiencies, T** — 制表效率的温度 `[280, 300, 320]` `K`（默认）| 正递增标量向量

制表效率的温度向量。此参数的大小必须大于或等于 `2`。

#### 依赖关系

要启用此参数，请暴露此模块的热端口，并将 **Converter losses** 设置为 `Tabulate efficiency`。

### **Percentage efficiency table, eff(I2,T)** — 电流和温度函数形式的效率表 `[66, 66, 66; 76, 76, 76; 80, 80, 80; 74, 74, 74]`（默认）| 标量向量

以百分比表示的电流和温度函数形式的效率表。

#### 依赖关系

要启用此参数，请暴露此模块的热端口，将 **Converter losses** 设置为 `Tabulate efficiency`，并将 **Variables for tabulation** 设置为 `Output current and temperature`。

### **Percentage efficiency table, eff(I2,V1,T)** — 电流、电压和温度函数形式的效率表 `repmat([66; 76; 80; 74], 1, 3, 3)`（默认）| 标量向量

以百分比表示的电流、电压和温度函数形式的效率表。

#### 依赖关系

要启用此参数，请暴露此模块的热端口，将 **Converter losses** 设置为 `Tabulate efficiency`，并将 **Variables for tabulation** 设置为 `Output current, input voltage, and temperature`。

### 动态特性

### **Dynamics** — 动态模型 `No dynamics`（默认）| `Specify voltage regulation time constant`

指定是否包含电压调节动态特性：

- `No dynamics` — 不考虑电压调节动态特性。
- `Specify voltage regulation time constant` — 在定义电压源值的方程中添加一阶滞后。启用动态特性后，负载阶跃变化会导致输出电压的瞬态变化。

### **Voltage regulation time constant** — 动态时间常数 `0.02` `s`（默认）

负载电流阶跃变化时与电压瞬态相关的时间常数。

#### 依赖关系

要启用此参数，请将 **Dynamics** 设置为 `Specify voltage regulation time constant`。

### **Initial output voltage demand** — 初始需求电压 `10` `V`（默认）

时间零点时的 *v*ref 值。通常，*v*ref 由 **Output voltage reference demand** 参数定义。但是，如果您希望在提供稳态负载电流时以无瞬态的方式初始化模型，可以使用此参数设置初始 *v*ref 值，并相应地增加该值以考虑输出电阻和下垂。

#### 依赖关系

要启用此参数，请将 **Dynamics** 设置为 `Specify voltage regulation time constant`。

### 关断状态

### **Minimum supply voltage to function** — 最低工作电源电压 `1` `V`（默认）

转换器工作并将输出电压调节至设定点的最低电源电压。当电源电压降至此参数值的 `90`% 以下时，DC-DC Converter 模块的输入表现为等于 **Input resistance if not functioning** 参数值的固定电阻。类似地，DC-DC Converter 模块的输出表现为等于 **Output resistance if not functioning** 参数值的固定电阻。

### **Input resistance if not functioning** — 不工作时的输入电阻 `1000` `Ohm`（默认）

电源电压降至 **Minimum supply voltage to function** 参数值的 `90`% 以下时的输入电阻。

### **Output resistance if not functioning** — 不工作时的输出电阻 `1000` `Ohm`（默认）

电源电压降至 **Minimum supply voltage to function** 参数值的 `90`% 以下时的输出电阻。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

添加输出开路故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### 热参数

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Thermal mass** — 与热端口关联的热质量 `100` `J/K`（默认）

与热端口 **H** 关联的热质量。它表示将热端口温度升高一度所需的能量。

### **Initial temperature** — 热端口的初始温度 `298.15` `K`（默认）

与热端口 **H** 关联的初始温度。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2022b：支持串联电源开关

您现在可以在电压电源和 DC-DC Converter 模块之间串联连接一个开关，并在仿真期间打开和关闭该开关。

为反映此更改，**Maximum expected supply-side current** 参数现在称为 **Minimum supply voltage to function**。如果电源电压降至该值以下，转换器的输入侧和输出侧都表现为恒定阻抗，转换器停止转换。

如果您在早期版本中保存的模型包含启用了动态特性的 DC-DC Converter 模块，并且您将该模块配置为阻止功率从负载流向电源，则仿真结果可能会有细微差异。电压调节时间常数不再滞后于防止反向功率流动的阻塞二极管，现在它是瞬时的。

## 描述

功率变换器的行为模型

DC-DC Converter 模块表示功率变换器的行为模型。该功率变换器调节负载侧的电压。为了平衡输入功率、输出功率和损耗，所需功率从电源侧汲取。或者，变换器可以支持从负载到电源的再生功率流动。

该电路说明了变换器的行为。

*Pfixed* 分量消耗恒定功率，对应于与负载电流无关的变换器损耗。所消耗的功率由 **Converter losses at zero output power** 参数值设定。电阻 *Rout* 对应于随负载电流增加的损耗，由您为 **Percentage efficiency at rated output power** 参数指定的值确定。

电压源由以下方程定义：

*v* = *vref* –
*i*
load
*D* + *iload*
*Rout*

其中：

- *vref* 是负载侧电压设定点，由您为 **Output voltage
  reference demand** 参数指定的值定义。或者，当 **Voltage
  reference** 参数设置为
  `External` 时，您可以将此值作为 **Vref** 端口的输入提供。
- *D* 是您为 **Output voltage
  droop with output current** 参数指定的值。有关详细信息，请参阅电压跌落。

电流源值 *i* 的计算使得流入变换器的功率等于流出功率加上变换器损耗之和。

要指定当负载呈现的电压高于变换器输出电压参考需求时变换器的行为，请使用 **Power direction** 参数：

- `Unidirectional power flow from supply to regulated
  side` — 电流被关断状态二极管阻断，电流源电流 *i* 为零。使用 **Diode off-state conductance** 参数设置该二极管的电导。
- `Bidirectional power flow` — 功率传输到电源侧，*i* 变为负值。

可选地，该模块可以包含电压调节动态特性。如果您为 **Dynamics** 参数选择 `Specify voltage regulation time constant`，则在定义电压源值的方程中添加一阶滞后。启用动态特性后，负载阶跃变化会导致输出电压的瞬态变化，时间常数由 **Voltage regulation time constant** 参数定义。

### 电压跌落

电压跌落是驱动负载的器件输出电压的损失。跌落在线性电压调节电路中很重要，因为它增加了系统对负载瞬态的容限。

独立的跌落值允许您控制输出电压如何随负载变化，而与负载相关损耗无关。要启用跌落，请选择 **Enable droop** 参数。要指定跌落，请将 **Droop parameterization** 参数设置为：

- `By voltage droop with output current` — 通过指定 **Output voltage droop with output current** 参数的值直接设置电压跌落。
- `By percent voltage droop at rated load` —
  此方程根据 **Voltage droop percent at rated
  load** 参数的值，将电压跌落计算为 **Output voltage reference demand** 参数的百分比：

  ΔV=Dpercent100Vref\_droopD=ΔV(Vref\_droop−ΔV)Prated

  其中
  `Vref_droop` 是 **Output voltage reference demand** 参数的值。如果您将 **Voltage reference** 参数设置为 `External`，则该模块使用 **Voltage reference used to calculate droop percent** 参数的常量值来计算跌落。

  此图显示了该模块如何计算电压跌落：

  电压跌落 *D* 是直线的斜率，其中 Irated=PratedVrated 且 Vrated=Vref\_droop−ΔV。

### 表格化效率

您可以根据输出电流、输入电压和温度来表格化 DC-DC Converter 模块的效率。

此方程定义了损耗与效率之间的关系：

loss(i2,v1,T)=[1−eff(i2,v1,T)100]abs(v1i1)if i2<0 (power flow 1→2)loss(i2,v1,T)=[1−eff(i2,v1,T)100]abs(v2i2)if i2>0 (power flow 2→1)

其中

- *loss(i2,v1,T)*
  是 DC-DC 变换器损耗。
- *v1* 是输入电压。
- *i1* 是输入电流。
- *i2* 是输出电流。
- *T* 是器件温度（如果您暴露此模块的热端口）。
- *eff(i2,v1,T)*
  是 DC-DC 变换器的效率，作为输出电流、输入电压和温度的函数，如 **Percentage efficiency table,
  eff(I2,V1,T)** 中所指定。

如果输出电流等于 `0`，则变换器损耗等于 **Converter losses at zero output power**。

以下是根据输出电流计算所用功率损耗的步骤：

1. 如果输出电流小于 **Vector of
   output currents for tabulated efficiencies, I2** 参数中的最后一个负电流点，或大于第一个正电流点，则该模块使用 **Percentage efficiency table,
   eff(I2)** 参数来查找对应的效率（使用线性插值或最近邻外推），然后将该效率转换为损耗。
2. 否则，该模块将零输出电流情况与表中的最后一个负点或第一个正点进行混合，如下图所示：

如果您将 **Modeling option** 参数设置为 `Show thermal
port`，则该模块除了根据输出电流和输入电压外，还根据温度来表格化效率。损耗计算与隐藏热端口的选项相同。

### 当电源无法匹配负载时的仿真

DC-DC Converter 模块使用 **Minimum supply voltage to function** 参数来在电压电源无法满足负载需求时保护网络。如果您将开关与电源串联连接然后将其关断，或者电源连接具有压降过大的串联电阻，就会发生这种情况。在仿真期间，如果电压降至 **Minimum supply voltage to function** 参数的值以下，则该模块放宽对输出电压的调节。一旦电压降至 **Minimum supply voltage to function** 参数的 `90`% 以下，变换器的输入表现为等于 **Input resistance if not functioning** 参数值的固定电阻。类似地，DC-DC Converter 模块的输出表现为等于 **Output resistance if not functioning** 参数值的固定电阻。

### 仿真故障

要对 DC-DC Converter 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

DC-DC Converter 模块允许您对开路故障进行建模。当故障被触发时，伺服电机停止运行，从电源侧汲取零电流，并向负载侧提供零电流。

### 对热效应建模

此模块有一个可选热端口。要控制热端口的可见性，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口。
- `Show thermal port` — 该模块包含一个热守恒端口。

该模块将通过受控热流率源从电气损耗产生的热量传递到 Thermal Mass 模块。该模块的电气属性不随温度变化。使用 **Thermal
mass** 和 **Initial temperature** 参数指定此模块的热属性。
