---
type: simulink-block
title: 'DC-DC Converter'
family: 'semiconductors-converters'
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

### 守恒

### **1+** — 输入正极端子 electrical

与输入侧正极端子关联的 electrical 守恒端口。

### **1-** — 输入负极端子 electrical

与输入侧负极端子关联的 electrical 守恒端口。

### **2+** — 输出正极端子 electrical

与输出侧正极端子关联的 electrical 守恒端口。

### **2-** — 输出负极端子 electrical

与输出侧负极端子关联的 electrical 守恒端口。

### **Vref** — 电压参考 physical

提供外部电压参考信号的 physical 信号输入端口。

#### 依赖关系

要启用此端口，请将 **电压参考** 参数设置为 `External`。

### **H** — 热质量 thermal

表示热质量的 thermal 守恒端口。当您暴露此端口时，请提供附加参数以定义第二个温度下的电池行为。有关详细信息，请参阅热参数。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 是否启用热端口 `No thermal port` (default) | `Show thermal port`

是否启用模块的热端口并建模热参数。

### 主

### **电压参考** — 电压参考 `Internal` (default) | `External`

是否在内部或外部对电压参考建模。

### **输出电压参考需求** — 电压设定点 `10` `V` (default)

电压调节器的设定点，以及没有输出电流时的输出电压值。

#### 依赖关系

此参数仅在 **电压参考** 参数设置为 `Internal` 时可见。

### **额定输出功率** — 额定功率 `10` `W` (default)

给出效率百分比值所对应的输出功率。如果下垂指定为百分比，此参数还用于计算下垂 *D*。

### **启用下垂** — 下垂选项 `On` (default) | `Off`

是否启用电压下垂。

### **下垂参数化** — 下垂模型 `By voltage droop with output current` (default) | `By percent voltage droop at rated load`

选择以下下垂参数化方法之一：

- `By voltage droop with output current` — 指定下垂的绝对值 *D*。这是默认选项。
- `By percent voltage droop at rated load` — 指定额定负载下下垂 *D* 的百分比。

#### 依赖关系

要启用此参数，请选择 **启用下垂** 参数。

### **带输出电流的输出电压下垂** — 1 A 时的电压下垂 `0.1` `V/A` (default)

对于 1 A 的输出电流，输出电压相对于设定点下降的伏特数。

#### 依赖关系

要启用此参数，请选择 **启用下垂** 参数，并将 **下垂参数化** 设置为 `By voltage droop with output current`。

### **额定负载下的电压下垂百分比** — 额定负载下的电压下垂百分比 `2` (default)

在提供额定负载时，电压相对于标称输出电压下降的百分比。如果将 **电压参考** 参数设置为 `Internal`，则模块使用 **输出电压参考需求** 参数计算下垂百分比。如果将 **电压参考** 参数设置为 `External`，则模块改用 **用于计算下垂百分比的电压参考** 参数。

#### 依赖关系

要启用此参数，请选择 **启用下垂** 参数，并将 **下垂参数化** 设置为 `By percent voltage droop at rated load`。

### **用于计算下垂百分比的电压参考** — 额定负载下的电压下垂百分比 `10` `V` (default)

**额定负载下的电压下垂百分比** 参数在仿真期间用于计算电压下垂的电压参考。

#### 依赖关系

要启用此参数：

- 将 **电压参考** 设置为 `External`。
- 选择 **启用下垂** 参数。
- 将 **下垂参数化** 设置为 `By percent voltage droop at rated load`。

### **功率方向** — 功率流向 `Unidirectional power flow from supply to regulated side` (default) | `Bidirectional power flow`

选择以下功率转换方向方法之一：

- `Unidirectional power flow from supply to regulated side` — 大多数小功率稳压器是单向的。这是默认选项。
- `Bidirectional power flow` — 较大功率转换器可以是双向的，例如电动汽车中用于允许再生制动的转换器。

### **二极管关断态电导** — 单向二极管 `1e-8` `1/Ohm` (default)

在单向配置中，输出侧集成的理想二极管用于防止电流被强制馈入转换器。

### 损耗

### **零输出功率时的转换器损耗** — 恒定损耗 `1` `W` (default)

等效电路图中 Pfixed 组件消耗的功率，它对应于与负载电流无关的转换器损耗。

### **转换器损耗** — 转换器损耗 `Assume proportional to square of output current` (default) | `Tabulate efficiency`

转换器损耗参数化。

### **额定输出功率下的效率百分比** — 额定效率 `80` (default)

效率定义为输出负载功率除以输入电源功率再乘以 100。

#### 依赖关系

要启用此参数，请将 **转换器损耗** 设置为 `Assume proportional to square of output current`。

### **用于制表的变量** — 制表变量 `Output current` (default) | `Output current and input voltage` | `Output current and temperature` | `Output current, input voltage, and temperature`

是否根据输出电流、输入电压和温度来制表效率。要启用温度选项，需要暴露模块的热端口。

### **用于制表效率的输出电流向量，I2** — 用于制表效率的输出电流 `[-2, -1, 1, 2]` `A` (default) | 正递增标量向量

用于制表效率的输出电流向量。此参数的大小必须等于或大于 `3`，并且等于 **效率百分比表，eff(I)** 的大小。

#### 依赖关系

要启用此参数，请将 **转换器损耗** 设置为 `Tabulate efficiency`。

### **效率百分比表，eff(I2)** — 以电流为函数的效率表 `[66, 76, 80, 74]` (default) | 正标量向量

以电流为函数、以百分比表示的效率表。此参数的大小必须等于 **用于制表效率的输出电流向量，I2** 的大小。

#### 依赖关系

要启用此参数，请将 **转换器损耗** 设置为 `Tabulate efficiency`，并将 **用于制表的变量** 设置为 `Output current`。

### **用于制表效率的输入电压向量，V1** — 用于制表效率的输入电压 `[15, 30, 45]` `V` (default) | 正递增标量向量

用于制表效率的输入电压向量。此参数的大小必须等于或大于 `2`。

#### 依赖关系

要启用此参数，请将 **转换器损耗** 设置为 `Tabulate efficiency`，并将 **用于制表的变量** 设置为 `Output current and input voltage` 或 `Output current, input voltage, and temperature`。

### **效率百分比表，eff(I2,V1)** — 以电流和电压为函数的效率表 `[66, 66, 66; 76, 76, 76; 80, 80, 80; 74, 74, 74]` (default) | 正标量向量

以电流为函数、以百分比表示的效率表。

#### 依赖关系

要启用此参数，请将 **转换器损耗** 设置为 `Tabulate efficiency`，并将 **用于制表的变量** 设置为 `Output current`。

### **用于制表效率的温度向量，T** — 用于制表效率的温度 `[280, 300, 320]` `K` (default) | 正递增标量向量

用于制表效率的温度向量。此参数的大小必须等于或大于 `2`。

#### 依赖关系

要启用此参数，请暴露此模块的热端口，并将 **转换器损耗** 设置为 `Tabulate efficiency`。

### **效率百分比表，eff(I2,T)** — 以电流和温度为函数的效率表 `[66, 66, 66; 76, 76, 76; 80, 80, 80; 74, 74, 74]` (default) | 标量向量

以电流和温度为函数、以百分比表示的效率表。

#### 依赖关系

要启用此参数，请暴露此模块的热端口，并将 **转换器损耗** 设置为 `Tabulate efficiency`，将 **用于制表的变量** 设置为 `Output current and temperature`。

### **效率百分比表，eff(I2,V1,T)** — 以电流、电压和温度为函数的效率表 `repmat([66; 76; 80; 74], 1, 3, 3)` (default) | 标量向量

以电流、电压和温度为函数、以百分比表示的效率表。

#### 依赖关系

要启用此参数，请暴露此模块的热端口，并将 **转换器损耗** 设置为 `Tabulate efficiency`，将 **用于制表的变量** 设置为 `Output current, input voltage, and temperature`。

### 动态

### **动态** — 动态模型 `No dynamics` (default) | `Specify voltage regulation time constant`

指定是否包括电压调节动态：

- `No dynamics` — 不考虑电压调节动态。
- `Specify voltage regulation time constant` — 向定义电压源值的方程添加一阶滞后。启用动态后，负载阶跃变化会导致输出电压瞬态变化。

### **电压调节时间常数** — 动态时间常数 `0.02` `s` (default)

当负载电流阶跃变化时，与电压瞬态关联的时间常数。

#### 依赖关系

要启用此参数，请将 **动态** 设置为 `Specify voltage regulation time constant`。

### **初始输出电压需求** — 初始需求电压 `10` `V` (default)

时间零点的 *v*ref 值。通常，*v*ref 由 **输出电压参考需求** 参数定义。但是，如果您希望在提供稳态负载电流时初始化模型且没有瞬态，可以使用此参数设置初始 *v*ref 值，并相应地增大该值以考虑输出电阻和下垂。

#### 依赖关系

要启用此参数，请将 **动态** 设置为 `Specify voltage regulation time constant`。

### 关断状态

### **最低工作供电电压** — 运行所需的最低供电电压 `1` `V` (default)

转换器运行并将输出电压调节到设定点所需的最低供电电压。当供电电压降至低于此参数值的 `90`% 时，DC-DC Converter 模块的输入表现为固定电阻，其值等于 **不工作时的输入电阻** 参数的值。类似地，DC-DC Converter 模块的输出表现为固定电阻，其值等于 **不工作时的输出电阻** 参数的值。

### **不工作时的输入电阻** — 不工作时的输入电阻 `1000` `Ohm` (default)

当供电电压降至低于 **最低工作供电电压** 参数值的 `90`% 时的输入电阻。

### **不工作时的输出电阻** — 不工作时的输出电阻 `1000` `Ohm` (default)

当供电电压降至低于 **最低工作供电电压** 参数值的 `90`% 时的输出电阻。

### 故障

### **开路故障** — 添加开路故障的选项 `Add fault` (default)

添加输出开路故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **在指定时间触发故障** — 进入故障状态前的时间 `0` `s` (default) | 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Timed`。

### 热

要启用这些参数，请将 **建模选项** 设置为 `Show thermal port`。

### **热质量** — 与热端口关联的热质量 `100` `J/K` (default)

与热端口 **H** 关联的热质量。它表示将热端口温度升高一度所需的能量。

### **初始温度** — 热端口处的初始温度 `298.15` `K` (default)

与热端口 **H** 关联的初始温度。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2022b：支持串联连接的电源开关

现在，您可以将一个开关串联连接在电压电源和 DC-DC Converter 模块之间，并在仿真期间打开和关闭此开关。

为反映此更改，**最大预期电源侧电流** 参数现在称为 **最低工作供电电压**。如果供电电压降至低于此值，转换器的输入侧和输出侧都会表现为恒定阻抗，转换器停止转换。

如果保存在较早版本中的模型包含启用了动态的 DC-DC Converter 模块，并且您配置此模块以阻止功率从负载流向电源，则仿真结果可能会略有不同。电压调节时间常数不再滞后于防止反向功率流动的阻塞二极管，现在为瞬时。

## 描述

功率转换器的行为模型

DC-DC Converter 模块表示功率转换器的行为模型。
此功率转换器调节负载侧电压。为了平衡输入功率、输出功率和损耗，所需功率量从电源侧抽取。
或者，转换器可以支持从负载到电源的再生功率流。

此电路说明了转换器的行为。

*Pfixed* 分量抽取恒定功率，对应于与负载电流无关的转换器损耗。抽取的功率由 **Converter losses at zero output power** 参数值设置。
电阻 *Rout* 对应于随负载电流增加的损耗，并由您为 **Percentage efficiency at rated output power** 参数指定的值确定。

电压源由以下方程定义：

*v* = *vref* – *i*load*D* + *iload* *Rout*

其中：

- *vref* 是负载侧电压设定点，由您为 **Output voltage reference demand** 参数指定的值定义。或者，当 **Voltage reference** 参数设置为 `External` 时，您可以将此值作为 **Vref** 端口的输入提供。
- *D* 是您为 **Output voltage droop with output current** 参数指定的值。有关详细信息，请参阅电压下垂。

计算电流源值 *i*，使得流入转换器的功率等于流出功率加上转换器损耗之和。

要指定当负载呈现的电压高于转换器输出电压参考需求时转换器的行为，请使用 **Power direction** 参数：

- `Unidirectional power flow from supply to regulated side` — 电流被关断状态二极管阻断，并且电流源电流 *i* 为零。使用 **Diode off-state conductance** 参数设置此二极管的电导。
- `Bidirectional power flow` — 功率传输到电源侧，并且 *i* 变为负值。

可选地，模块可以包含电压调节动态特性。如果您为 **Dynamics** 参数选择 `Specify voltage regulation time constant`，则会将一阶滞后添加到定义电压源值的方程中。启用动态特性后，负载阶跃变化会导致输出电压发生瞬态变化，时间常数由 **Voltage regulation time constant** 参数定义。

### 电压下垂

电压下垂是驱动负载的器件输出电压的损失。电压下垂在电压调节电路中很重要，因为它提高了系统对负载瞬变的容差。

单独的电压下垂值允许您控制输出电压如何随负载变化，而不受与负载相关的损耗影响。要启用电压下垂，请选择 **Enable droop** 参数。要指定电压下垂，请将 **Droop parameterization** 参数设置为：

- `By voltage droop with output current` — 通过指定 **Output voltage droop with output current** 参数的值来直接设置电压下垂。
- `By percent voltage droop at rated load` — 此方程基于 **Voltage droop percent at rated load** 参数的值，将电压下垂计算为 **Output voltage reference demand** 参数的百分比：

  ΔV=Dpercent100Vref\_droopD=ΔV(Vref\_droop−ΔV)Prated

  其中
  `Vref_droop` 是 **Output voltage reference demand** 参数的值。如果您将 **Voltage reference** 参数设置为 `External`，则模块改为使用 **Voltage reference used to calculate droop percent** 参数的常量值来计算电压下垂。

  下图显示了模块如何计算电压下垂：

  电压下垂 *D* 是该直线的斜率，其中 Irated=PratedVrated 且 Vrated=Vref\_droop−ΔV。

### 表格化效率

您可以根据输出电流、输入电压和温度来表格化 DC-DC Converter 模块的效率。

此方程定义了损耗与效率之间的关系：

loss(i2,v1,T)=[1−eff(i2,v1,T)100]abs(v1i1)if i2<0 (power flow 1→2)loss(i2,v1,T)=[1−eff(i2,v1,T)100]abs(v2i2)if i2>0 (power flow 2→1)

其中

- *loss(i2,v1,T)* 是 DC-DC 转换器损耗。
- *v1* 是输入电压。
- *i1* 是输入电流。
- *i2* 是输出电流。
- *T* 是器件温度，如果您暴露此模块的热端口。
- *eff(i2,v1,T)* 是 DC-DC 转换器的效率，它是输出电流、输入电压和温度的函数，如 **Percentage efficiency table, eff(I2,V1,T)** 中所指定。

如果输出电流等于 `0`，则转换器损耗等于 **Converter losses at zero output power**。

以下是根据输出电流计算所用功率损耗的步骤：

1. 如果输出电流小于 **Vector of output currents for tabulated efficiencies, I2** 参数中的最后一个负电流点，或大于第一个正电流点，则模块使用 **Percentage efficiency table, eff(I2)** 参数查找相应效率（使用线性插值或最近外插），然后将该效率转换为损耗。
2. 否则，模块将零输出电流情况与表中的最后一个负点或第一个正点混合，如下图所示：

如果您将 **Modeling option** 参数设置为 `Show thermal port`，则模块除了根据输出电流和输入电压外，还会根据温度来表格化效率。损耗计算与隐藏热端口的选项相同。

### 电源无法满足负载时的仿真

当电压电源无法提供负载需求时，DC-DC Converter 模块使用 **Minimum supply voltage to function** 参数来保护网络。如果您将开关与电源串联连接然后将其关闭，或者电源连接具有会降低过多电压的串联电阻，则会发生这种情况。在仿真期间，如果电压下降到 **Minimum supply voltage to function** 参数的值以下，则模块放宽对输出电压的调节。一旦电压下降到 **Minimum supply voltage to function** 参数的 `90`% 以下，转换器的输入行为就像等于 **Input resistance if not functioning** 参数值的固定电阻。类似地，DC-DC Converter 模块的输出行为就像等于 **Output resistance if not functioning** 参数值的固定电阻。

### 故障仿真

要对 DC-DC Converter 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

DC-DC Converter 模块允许您对开路故障建模。当故障触发时，伺服电机停止运行，从电源侧抽取的电流为零，向负载侧提供的电流为零。

### 热效应建模

此模块有一个可选热端口。要控制热端口的可见性，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

该模块通过 Controlled Heat Flow Rate Source 将电气损耗产生的热量传递到 Thermal Mass 模块。该模块的电气属性不随温度变化。使用 **Thermal mass** 和 **Initial temperature** 参数指定此模块的热属性。
