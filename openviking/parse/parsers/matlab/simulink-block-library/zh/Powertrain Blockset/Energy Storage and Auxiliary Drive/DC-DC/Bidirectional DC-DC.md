---
type: simulink-block
title: 'Bidirectional DC-DC'
family: 'energy-storage-and-auxiliary-drive'
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

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `SrcPwr` | | | DC-to-DC 转换器的源功率 | *SrcPwr* | W |
| `LdPwr` | | | 来自 DC-to-DC 转换器的负载功率 | *LdPwr* | W |
| `PwrLoss` | | | 功率损耗 | *PwrLoss* | W |
| `LdVoltCmd` | | | 应用时间常数之前 DC-to-DC 转换器的指令负载电压 | *LdVoltCmd* | V |
| `PwrInfo` | `PwrTrnsfrd` | `PwrBusSrc` | DC-to-DC 转换器的源功率 | *Psrc* | W |
| `PwrBusLd` | 来自 DC-to-DC 转换器的负载功率 | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 转换器功率损耗 | *Ploss* | W |
| `PwrStored` | *未使用* | | | |

### **LdVolt** — 负载电压 `scalar`

DC-to-DC 转换器的负载电压，
*LdVolt*，单位为 V。

### **SrcCurr** — 源电流 `scalar`

来自 DC-to-DC 转换器的源电流消耗，
*SrcAmp*，单位为 A。

## 参数

#### 电气控制

### **转换器响应时间常数, Tc** — 常量 `1/1000`（默认）| `scalar`

转换器响应时间，*τ*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tc` |
| **值：** | `1/1000` (default) | `scalar` |
| **数据类型：** | `double` |

### **转换器响应初始电压, Vinit** — 电压 `0`（默认）| `scalar`

DC-to-DC 转换器的初始负载电压，
*Vinit*，单位为 V。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vinit` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **转换器功率限制, Plimit** — 功率 `100000`（默认）| `scalar`

DC-to-DC 转换器的输出功率限制，
*Plimit*，单位为 W。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Plimit` |
| **值：** | `100000` (default) | `scalar` |
| **数据类型：** | `double` |

#### 电气损耗

### **损耗参数化方式** — 损耗计算 `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data`

此表总结了用于计算电气损耗的损耗选项。

| 参数选项 | 描述 |
| --- | --- |
| `Single efficiency measurement` | 使用恒定转换效率值计算电气损耗。 |
| `Tabulated loss data` | 根据负载电流和电压函数计算电气损耗。DC-to-DC 转换器数据表通常以这种格式提供损耗数据。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果提供部分数据，模块将对其他象限假定相同的损耗模式。对于超出您提供的电压和电流范围的损耗，模块不会进行外推。模块允许您考虑在电压或电流为零时仍然存在的固定损耗。  如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据虚拟校准二维查找表。 |
| `Tabulated efficiency data` | 使用作为负载电流和电压函数的转换效率计算电气损耗。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果提供部分数据，模块将对其他象限假定相同的效率模式。模块：  - 当电压或电流为零时假定损耗为零。 - 使用线性插值确定损耗。在较低功率条件下，为提高计算精度，请提供低电压和低电流下的效率。 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `param_loss` |
| **值：** | `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated efficiency data` |
| **数据类型：** | `character vector` |

### **整体 DC to DC 转换器效率, eff** — 常量 `98`（默认）| `scalar`

整体转换效率，*Eff*，单位为 %。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eff` |
| **值：** | `98` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Single efficiency measurement`。

### **用于表格损耗的电压向量 (v), v\_loss\_bp** — 断点 `[0 200 400 600 800 1000]`（默认）| `1`-by-`M` vector

`M` 个负载电压的表格损耗断点，单位为
V。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `v_loss_bp` |
| **值：** | `[0 200 400 600 800 1000]` (default) | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Tabulated loss data`。

### **用于表格损耗的电流向量 (i), i\_loss\_bp** — 断点 `[0 25 50 75 100]`（默认）| `1`-by-`N` vector

`N` 个负载电流的表格损耗断点，单位为
A。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `i_loss_bp` |
| **值：** | `[0 25 50 75 100]` (default) | `1`-by-`N` vector |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Tabulated loss data`。

### **对应损耗, losses\_table** — 二维查找表 `N`-by-`M` matrix

电气损耗映射，作为 `N` 个负载电流和
`M` 个负载电压的函数，单位为 W。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table` |
| **值：** | `N`-by-`M` matrix |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Tabulated loss data`。

### **用于表格效率的电压向量 (v), v\_eff\_bp** — 断点 `[200 400 600 800 1000]`（默认）| `1`-by-`M` vector

`M` 个负载电压的表格效率断点，
单位为 V。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `v_eff_bp` |
| **值：** | `[200 400 600 800 1000]` (default) | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Tabulated efficiency data`。

### **用于表格效率的电流向量 (i), i\_eff\_bp** — 断点 `[25 50 75 100]`（默认）| `1`-by-`N` vector

`N` 个负载电流的表格效率断点，
单位为 A。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `i_eff_bp` |
| **值：** | `[25 50 75 100]` (default) | `1`-by-`N` vector |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Tabulated efficiency data`。

### **对应效率, efficiency\_table** — 二维查找表 `N`-by-`M` matrix

电气效率映射，作为
`N` 个负载电流和 `M` 个负载
电压的函数，单位为 %。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table` |
| **值：** | `N`-by-`M` matrix |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Tabulated efficiency data`。

### **Calibrate Maps** — 使用测量数据校准表格 `selection`

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据虚拟校准查找表。该对话框将逐步执行以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入数据 | 从文件导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksutilities/mbctemplates/MappedDCDCConverterDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  所需数据：  - 电流, A - 电压, V - 功率损耗, W  在稳态工作条件下采集数据。  要过滤或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox 数据编辑器将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合到高斯过程模型 (GPMs)。  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox 模型浏览器将打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准后的表格。  要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE 浏览器将打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准更新这些模块查找表和断点参数。  - **用于表格损耗的电压向量 (v), v\_loss\_bp** - **用于表格损耗的电流向量 (i), i\_loss\_bp** - **对应损耗, losses\_table** |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CalLossMapsButton` |
| **值：** | selection |
| **数据类型：** | `character vector` |

#### 依赖项

要启用此参数，请在 **损耗参数化方式** 中，选择
`Tabulated loss data`。

## 所属库

Powertrain Blockset / Energy Storage and Auxiliary Drive / DC-DC

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

支持双向升压和降压的 DC-to-DC 转换器

Bidirectional DC-DC 模块实现了一个支持双向升压和降压（降低）操作的 DC-to-DC 转换器。除非 DC-to-DC 转换限制功率，否则输出电压会跟踪电压指令。您可以指定电气损耗或测量效率。

根据您的电池系统配置，电压可能不是逆变器和电机等电气系统组件所需的电势。您可以使用该模块升压或降压。将模块连接到电池以及以下模块之一：

- Mapped Motor
- IM Controller
- Interior PM Controller
- Surface Mount PM Controller

要计算 DC-to-DC 转换期间的电气损耗，请使用 **损耗参数化方式**。

| 参数选项 | 描述 |
| --- | --- |
| `Single efficiency measurement` | 使用恒定转换效率值计算电气损耗。 |
| `Tabulated loss data` | 根据负载电流和电压函数计算电气损耗。DC-to-DC 转换器数据表通常以这种格式提供损耗数据。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果提供部分数据，模块将对其他象限假定相同的损耗模式。对于超出您提供的电压和电流范围的损耗，模块不会进行外推。模块允许您考虑在电压或电流为零时仍然存在的固定损耗。  如果您有 Model-Based Calibration Toolbox™，请点击 **Calibrate Maps** 以使用测量数据虚拟校准二维查找表。 |
| `Tabulated efficiency data` | 使用作为负载电流和电压函数的转换效率计算电气损耗。使用此选项时，请提供仿真将运行的所有工作象限的数据。如果提供部分数据，模块将对其他象限假定相同的效率模式。模块：  - 当电压或电流为零时假定损耗为零。 - 使用线性插值确定损耗。在较低功率条件下，为提高计算精度，请提供低电压和低电流下的效率。 |

**注意**

该模块不支持反相。输入电压的极性与输出电压的极性匹配。

### 理论

Bidirectional DC-DC 模块使用指令电压和实际电压来确定是升压还是降压（降低）电压。您可以为电压响应指定时间常数。

| 如果 | 则 |
| --- | --- |
| *Voltcmd* > *SrcVolt* | 升压 |
| *Voltcmd* < *SrcVolt* | 降压 |

Bidirectional DC-DC 模块使用基于时间常数的调节器来提供与负载电流无关的固定输出电压。使用输出电压和电流，模块确定 DC-to-DC 转换的损耗。模块使用转换损耗计算输入电流。模块考虑：

- 双向电流流动

  - 源到负载 — 电池放电
  - 负载到源 — 电池充电
- 额定功率限制

该模块提供基于以下方程的功率受限电压控制。电压是固定的。该模块不实现电压降，因为负载电流近似 DC-to-DC 转换，其带宽大于负载电流消耗。

|  |  |
| --- | --- |
| DC-to-DC 转换器负载电压 | LdVoltCmd=min(VoltCmd,PlimitLdAmp,0)LdVolt=LdVoltCmd⋅1τs+1 |
| 单效率源到负载的功率损耗 | PwrLoss=100−EffEff⋅LdVolt⋅LdAmp |
| 单效率负载到源的功率损耗 | PwrLoss=100−EffEff⋅|LdVolt⋅LdAmp| |
| 表格效率的功率损耗 | PrwLoss=f(LdVolt,LdAmp) |
| 来自 DC-to-DC 转换器的源电流消耗 | SrcAmp=LdPwr+PrwLossSrcVolt |
| 来自 DC-to-DC 转换器的源功率 | SrcPwr=SrcAmp⋅SrcVolt |

### 虚拟校准

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据虚拟校准查找表。该对话框将逐步执行以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入数据 | 从文件导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksutilities/mbctemplates/MappedDCDCConverterDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  所需数据：  - 电流, A - 电压, V - 功率损耗, W  在稳态工作条件下采集数据。  要过滤或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox 数据编辑器将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合到高斯过程模型 (GPMs)。  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox 模型浏览器将打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准后的表格。  要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE 浏览器将打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准更新这些模块查找表和断点参数。  - **用于表格损耗的电压向量 (v), v\_loss\_bp** - **用于表格损耗的电流向量 (i), i\_loss\_bp** - **对应损耗, losses\_table** |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrBusSrc` | DC-to-DC 转换器的源功率 | *Psrc* | Psrc= SrcPwr |
| `PwrBusLd` | 来自 DC-to-DC 转换器的负载功率 | *Pbus* | Pbus= −LdVolt |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrLoss` | 转换器功率损耗 | *Ploss* | Ploss= PwrLoss |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | | *未使用* | | |

方程使用以下变量。

|  |  |
| --- | --- |
| *VoltCmd* | DC-to-DC 转换器指令输出电压 |
| *SrcVolt* | DC-to-DC 转换器的源输入电压 |
| *LdAmp* | DC-to-DC 转换器的负载电流 |
| *LdVolt* | DC-to-DC 转换器的负载电压 |
| *SrcAmp* | 来自 DC-to-DC 转换器的源电流消耗 |
| *τ* | 转换时间常数 |
| *Vinit* | DC-to-DC 转换器的初始负载电压 |
| *Plimit* | DC-to-DC 转换器的输出功率限制 |
| *Eff* | 输入到输出效率 |
| *SrcPwr* | DC-to-DC 转换器的源功率 |
| *LdPwr* | 来自 DC-to-DC 转换器的负载功率 |
| *PwrLoss* | 功率损耗 |
| *LdVoltCmd* | 应用时间常数之前 DC-to-DC 转换器的指令负载电压 |
