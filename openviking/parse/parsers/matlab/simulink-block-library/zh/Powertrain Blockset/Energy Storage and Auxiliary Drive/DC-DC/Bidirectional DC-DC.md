---
type: simulink-block
title: 'Bidirectional DC-DC'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage and Auxiliary Drive / DC-DC'
documentation_page: 'bidirectionaldcdc'
documentation_source_path: 'ref/bidirectionaldcdc.html'
language: zh-CN
chinese_source: worker-translation
---

# Bidirectional DC-DC

## 端口
```yaml
ports:
- name: VoltCmd
  summary: 指令电压 scalar
  direction: input
- name: SrcVolt
  summary: 输入电压 scalar
  direction: input
- name: LdCurr
  summary: 负载电流 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: LdVolt
  summary: 负载电压 scalar
  direction: output
- name: SrcCurr
  summary: 源电流 scalar
  direction: output
```

### 输入

### **VoltCmd** — 指令电压 `scalar`

DC-to-DC 转换器的指令输出电压，
*VoltCmd*，单位为 V。

### **SrcVolt** — 输入电压 `scalar`

DC-to-DC 转换器的源输入电压，
*SrcVolt*，单位为 V。

### **LdCurr** — 负载电流 `scalar`

DC-to-DC 转换器的负载电流，
*LdAmp*，单位为 A。
### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `SrcPwr` | | | DC-to-DC 转换器的源功率 | *SrcPwr* | W |
| `LdPwr` | | | DC-to-DC 转换器的负载功率 | *LdPwr* | W |
| `PwrLoss` | | | 功率损耗 | *PwrLoss* | W |
| `LdVoltCmd` | | | 应用时间常数之前 DC-to-DC 转换器的指令负载电压 | *LdVoltCmd* | V |
| `PwrInfo` | `PwrTrnsfrd` | `PwrBusSrc` | DC-to-DC 转换器的源功率 | *Psrc* | W |
| `PwrBusLd` | DC-to-DC 转换器的负载功率 | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 转换器功率损耗 | *Ploss* | W |
| `PwrStored` | *未使用* | | | |

### **LdVolt** — 负载电压 `scalar`

DC-to-DC 转换器的负载电压，
*LdVolt*，单位为 V。

### **SrcCurr** — 源电流 `scalar`

DC-to-DC 转换器的源电流消耗，
*SrcAmp*，单位为 A。
## 参数
```yaml
parameters:
- name: Converter response time constant, Tc
  summary: 常量 1/1000（默认）| scalar
  group: ''
  block_parameter: Tc
  values: 1/1000（默认）| scalar
- name: Converter response initial voltage, Vinit
  summary: 电压 0（默认）| scalar
  group: ''
  block_parameter: Vinit
  values: 0（默认）| scalar
- name: Converter power limit, Plimit
  summary: 功率 100000（默认）| scalar
  group: ''
  block_parameter: Plimit
  values: 100000（默认）| scalar
- name: Parameterize losses by
  summary: 损耗计算 Single efficiency measurement（默认）| Tabulated loss data | Tabulated efficiency data
  group: ''
  block_parameter: param_loss
  values: Single efficiency measurement（默认）| Tabulated loss data | Tabulated efficiency data
- name: Overall DC to DC converter efficiency, eff
  summary: 常量 98（默认）| scalar
  group: ''
  block_parameter: eff
  values: 98（默认）| scalar
- name: Vector of voltages (v) for tabulated loss, v_loss_bp
  summary: 断点 [0 200 400 600 800 1000]（默认）| 1-by-M vector
  group: ''
  block_parameter: v_loss_bp
  values: '[0 200 400 600 800 1000]（默认）| 1-by-M vector'
- name: Vector of currents (i) for tabulated loss, i_loss_bp
  summary: 断点 [0 25 50 75 100]（默认）| 1-by-N vector
  group: ''
  block_parameter: i_loss_bp
  values: '[0 25 50 75 100]（默认）| 1-by-N vector'
- name: Corresponding losses, losses_table
  summary: 二维查找表 N×M 矩阵
  group: ''
  block_parameter: losses_table
  values: N×M 矩阵
- name: Vector of voltages (v) for tabulated efficiency, v_eff_bp
  summary: 断点 [200 400 600 800 1000]（默认）| 1×M 向量
  group: ''
  block_parameter: v_eff_bp
  values: '[200 400 600 800 1000]（默认）| 1×M 向量'
- name: Vector of currents (i) for tabulated efficiency, i_eff_bp
  summary: 断点 [25 50 75 100]（默认）| 1×N 向量
  group: ''
  block_parameter: i_eff_bp
  values: '[25 50 75 100]（默认）| 1×N 向量'
- name: Corresponding efficiency, efficiency_table
  summary: 二维查找表 N×M 矩阵
  group: ''
  block_parameter: efficiency_table
  values: N×M 矩阵
- name: Calibrate Maps
  summary: 使用测量数据校准表格 selection
  group: ''
  block_parameter: CalLossMapsButton
  values: selection
```

#### 电气控制

### **Converter response time constant, Tc** — 常量 `1/1000`（默认）| `scalar`

转换器响应时间，*τ*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tc` |
| **值：** | `1/1000`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Converter response initial voltage, Vinit** — 电压 `0`（默认）| `scalar`

DC-to-DC 转换器的初始负载电压，
*Vinit*，单位为 V。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vinit` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Converter power limit, Plimit** — 功率 `100000`（默认）| `scalar`

DC-to-DC 转换器的初始负载电压，
*Plimit*，单位为 W。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Plimit` |
| **值：** | `100000`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 电气损耗

### **Parameterize losses by** — 损耗计算 `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data`

此表汇总了用于计算电气损耗的损耗选项。

| 参数选项 | 描述 |
| --- | --- |
| `Single efficiency measurement` | 使用恒定转换效率值计算电气损耗。 |
| `Tabulated loss data` | 电气损耗作为负载电流和电压的函数计算。DC-to-DC 转换器数据手册通常以该格式提供损耗数据。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果仅提供部分数据，模块将对其他象限采用相同的损耗模式。模块不会外推超出所提供电压和电流范围的损耗。模块允许您考虑在零电压或零电流时仍然存在的固定损耗。如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据对二维查找表进行虚拟标定。 |
| `Tabulated efficiency data` | 电气损耗使用作为负载电流和电压函数的转换效率计算。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果仅提供部分数据，模块将对其他象限采用相同的效率模式。模块： - 当电压或电流为零时，假定损耗为零。 - 使用线性插值确定损耗。在较低功率条件下，为保证计算精度，请提供低电压和低电流下的效率。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `param_loss` |
| **值**：| `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data` |
| **Data Types:** | `character vector` |

### **Overall DC to DC converter efficiency, eff** — 常量 `98`（默认）| `scalar`

总体转换效率 *Eff*，以 % 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `eff` |
| **值**：| `98`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Single efficiency measurement`。

### **Vector of voltages (v) for tabulated loss, v\_loss\_bp** — 断点 `[0 200 400 600 800 1000]`（默认）| `1`-by-`M` vector

用于 `M` 个负载电压的表格化损耗断点，以 V 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `v_loss_bp` |
| **值**：| `[0 200 400 600 800 1000]`（默认）| `1`-by-`M` vector |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated loss data`。

### **Vector of currents (i) for tabulated loss, i\_loss\_bp** — 断点 `[0 25 50 75 100]`（默认）| `1`-by-`N` vector

用于 `N` 个负载电流的表格化损耗断点，以 A 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `i_loss_bp` |
| **值**：| `[0 25 50 75 100]`（默认）| `1`-by-`N` vector |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated loss data`。

### **Corresponding losses, losses\_table** — 二维查找表 `N`×`M` 矩阵

电损耗映射，作为 `N` 个负载电流和 `M` 个负载电压的函数，单位为 W。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table` |
| **值：** | `N`×`M` 矩阵 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，选择 `Tabulated loss data`。

### **Vector of voltages (v) for tabulated efficiency, v\_eff\_bp** — 断点 `[200 400 600 800 1000]`（默认）| `1`×`M` 向量

用于 `M` 个负载电压的列表效率断点，单位为 V。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `v_eff_bp` |
| **值：** | `[200 400 600 800 1000]`（默认）| `1`×`M` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data`。

### **Vector of currents (i) for tabulated efficiency, i\_eff\_bp** — 断点 `[25 50 75 100]`（默认）| `1`×`N` 向量

用于 `N` 个负载电流的列表效率断点，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `i_eff_bp` |
| **值：** | `[25 50 75 100]`（默认）| `1`×`N` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data`。

### **Corresponding efficiency, efficiency\_table** — 二维查找表 `N`×`M` 矩阵

电效率映射，作为 `N` 个负载电流和 `M` 个负载电压的函数，单位为 %。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table` |
| **值：** | `N`×`M` 矩阵 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data`。

### **Calibrate Maps** — 使用测量数据校准表格 `selection`

如果您拥有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，以使用测量数据对查找表进行虚拟校准。该对话框将引导您完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入数据 | 从文件导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksutilities/mbctemplates/MappedDCDCConverterDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。所需数据： - Current, A - Voltage, V - Power loss, W 在稳态工况下采集数据。要筛选或编辑数据，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Data Editor。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合到高斯过程模型（GPM）。要评估或调整响应模型拟合，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Model Browser。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准后的表格。要评估或调整校准，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox CAGE Browser。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准结果更新以下模块查找表和断点参数。 - **Vector of voltages (v) for tabulated loss, v\_loss\_bp** - **Vector of currents (i) for tabulated loss, i\_loss\_bp** - **Corresponding losses, losses\_table** |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CalLossMapsButton` |
| **值**：| selection |
| **Data Types:** | `character vector` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated loss data`。
## 所属库

Powertrain Blockset / Energy Storage and Auxiliary Drive / DC-DC

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

支持双向升压和降压的 DC-DC 转换器

Bidirectional DC-DC 模块实现了一个支持双向升压和降压（降低）操作的 DC-DC 转换器。除非 DC-DC 转换限制了功率，否则输出电压会跟踪电压指令。您可以指定电气损耗或实测效率。

根据您的电池系统配置，电压可能不在电气系统组件（如逆变器和电机）所需的电位上。您可以使用该模块来升压或降压电压。将该模块连接到电池以及以下模块之一：

- Mapped Motor
- IM Controller
- Interior PM Controller
- Surface Mount PM Controller

要计算 DC-DC 转换期间的电气损耗，请使用 **Parameterize losses by**。

| 参数选项 | 描述 |
| --- | --- |
| `Single efficiency measurement` | 使用恒定转换效率值计算电气损耗。 |
| `Tabulated loss data` | 电气损耗作为负载电流和电压的函数计算。DC-DC 转换器数据手册通常以这种格式提供损耗数据。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果提供部分数据，模块将对其他象限采用相同的损耗模式。模块不会外推您提供的电压和电流范围之外的损耗。该模块允许您考虑在零电压或零电流时仍然存在的固定损耗。如果您有 Model-Based Calibration Toolbox™，请点击 **Calibrate Maps** 使用实测数据对二维查找表进行虚拟标定。 |
| `Tabulated efficiency data` | 使用作为负载电流和电压函数的转换效率计算电气损耗。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果提供部分数据，模块将对其他象限采用相同的效率模式。该模块：- 当电压或电流为零时，假定损耗为零。- 使用线性插值确定损耗。在较低功率条件下，为保证计算精度，请提供低电压和低电流下的效率。 |

**注意**

该模块不支持反相。输入电压的极性与输出电压的极性匹配。

### 理论

Bidirectional DC-DC 模块使用指令电压和实际电压来确定是升压还是降压（降低）电压。您可以为电压响应指定时间常数。

| 如果 | 则 |
| --- | --- |
| *Voltcmd* > *SrcVolt* | 升压 |
| *Voltcmd* < *SrcVolt* | 降压 |

Bidirectional DC-DC 模块使用基于时间常数的调节器来提供与负载电流无关的固定输出电压。使用输出电压和电流，模块确定 DC-DC 转换的损耗。模块使用转换损耗来计算输入电流。模块考虑：

- 双向电流流动

  - 源到负载 — 电池放电
  - 负载到源 — 电池充电
- 额定功率限制

该模块提供基于以下方程进行功率限制的电压控制。电压是固定的。该模块不实现电压降，因为负载电流以大于负载电流抽取的带宽近似 DC-DC 转换。

|  |  |
| --- | --- |
| DC-DC 转换器负载电压 | LdVoltCmd=min(VoltCmd,PlimitLdAmp,0)LdVolt=LdVoltCmd⋅1τs+1 |
| 单向效率源到负载的功率损耗 | PwrLoss=100−EffEff⋅LdVolt⋅LdAmp |
| 单向效率负载到源的功率损耗 | PwrLoss=100−EffEff⋅|LdVolt⋅LdAmp| |
| 表格化效率的功率损耗 | PrwLoss=f(LdVolt,LdAmp) |
| DC-DC 转换器的源电流抽取 | SrcAmp=LdPwr+PrwLossSrcVolt |
| DC-DC 转换器的源功率 | SrcPwr=SrcAmp⋅SrcVolt |

### Virtual Calibration

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据对查找表进行虚拟标定。该对话框将逐步完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入数据 | 从文件导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksutilities/mbctemplates/MappedDCDCConverterDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。所需数据： - Current, A - Voltage, V - Power loss, W 在稳态运行条件下采集数据。要筛选或编辑数据，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Data Editor。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用测试计划将数据拟合到高斯过程模型（GPM）。要评估或调整响应模型拟合，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Model Browser。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定响应模型进行标定并生成标定表。要评估或调整标定，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox CAGE Browser。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定更新以下模块查找表和断点参数。 - **Vector of voltages (v) for tabulated loss, v\_loss\_bp** - **Vector of currents (i) for tabulated loss, i\_loss\_bp** - **Corresponding losses, losses\_table** |

### Power Accounting

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率 - 正信号表示流入模块 - 负信号表示流出模块 | `PwrBusSrc` | 到 DC-to-DC converter 的源功率 | *Psrc* | Psrc= SrcPwr |
| `PwrBusLd` | 来自 DC-to-DC converter 的负载功率 | *Pbus* | Pbus= −LdVolt |
| `PwrNotTrnsfrd` — 跨越模块边界但未传输的功率 - 正信号表示输入 - 负信号表示损耗 | `PwrLoss` | Converter 功率损耗 | *Ploss* | Ploss= PwrLoss |
| `PwrStored` — 存储能量的变化率 - 正信号表示增加 - 负信号表示减少 | | *未使用* | | |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *VoltCmd* | DC-to-DC converter 的命令输出电压 |
| *SrcVolt* | 到 DC-to-DC converter 的源输入电压 |
| *LdAmp* | DC-to-DC converter 的负载电流 |
| *LdVolt* | DC-to-DC converter 的负载电压 |
| *SrcAmp* | 来自 DC-to-DC converter 的源电流消耗 |
| *τ* | 转换时间常数 |
| *Vinit* | DC-to-DC converter 的初始负载电压 |
| *Plimit* | DC-to-DC converter 的输出功率限制 |
| *Eff* | 输入到输出效率 |
| *SrcPwr* | 到 DC-to-DC converter 的源功率 |
| *LdPwr* | 来自 DC-to-DC converter 的负载功率 |
| *PwrLoss* | 功率损耗 |
| *LdVoltCmd* | 在应用时间常数之前 DC-to-DC converter 的命令负载电压 |
