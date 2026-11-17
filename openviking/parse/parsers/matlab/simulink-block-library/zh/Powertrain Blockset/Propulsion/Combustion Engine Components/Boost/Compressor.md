---
type: simulink-block
title: 'Compressor'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Boost'
documentation_page: 'compressor'
documentation_source_path: 'ref/compressor.html'
language: zh-CN
chinese_source: worker-translation
---

# Compressor

## 端口

### 输入

### **Ds** — 驱动轴转速双向连接端口

`ShftSpd` — 包含驱动轴角速度 ω 的信号，单位为 rad/s。

### **A** — 入口压力、温度、焓、质量分数双向连接端口

包含入口控制体积的总线：

- `InPrs` — 压力，pinlet，单位为 Pa
- `InTemp` — 温度，Tinlet，单位为 K
- `InEnth` — 比焓，hinlet，单位为 J/kg

### **B** — 出口压力、温度、焓、质量分数双向连接端口

包含出口控制体积的总线：

- `OutPrs` — 压力，poutlet，单位为 Pa
- `OutTemp` — 温度，Toutlet，单位为 K
- `OutEnth` — 比焓，houtlet，单位为 J/kg
### 输出

### **Info** — 总线信号总线

包含以下模块计算结果的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `CmprsOutletTemp` | | | 离开压缩机的温度 | K |
| `DriveshftPwr` | | | 驱动轴功率 | W |
| `DriveshftTrq` | | | 驱动轴扭矩 | N·m |
| `CmprsMassFlw` | | | 通过压缩机的质量流量 | kg/s |
| `PrsRatio` | | | 压力比 | N/A |
| `DriveshftCorrSpd` | | | 修正驱动轴转速 | rad/s |
| `CmprsEff` | | | 压缩机等熵效率 | N/A |
| `CorrMassFlw` | | | 修正质量流量 | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | 从轴传递的功率 | W |
| `PwrHeatFlwIn` | 端口 A 处的热流率 | W |
| `PwrHeatFlwOut` | 端口 B 处的热流率 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 功率损失 | W |
| `PwrStored` | | *未使用* | W |

### **Ds** — 驱动轴扭矩双向连接端口

`Trq` — 包含驱动轴扭矩 τcomp 的信号，单位为 N·m。

### **A** — 入口质量流量、热流率、温度、质量分数双向连接端口

包含以下内容的总线：

- `MassFlwRate` — 通过入口的质量流量，m˙comp，单位为 kg/s
- `HeatFlwRate` — 入口热流率，qinlet，单位为 J/s
- `Temp` — 入口温度，单位为 K
- `MassFrac` — 入口质量分数，无量纲。

  具体来说，是包含以下质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃烧燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 燃烧气体

### **B** — 出口质量流量、热流率、温度、质量分数双向连接端口

包含以下内容的总线：

- `MassFlwRate` — 出口质量流量，m˙comp，单位为 kg/s
- `HeatFlwRate` — 出口热流率，qoutlet，单位为 J/s
- `Temp` — 出口温度，单位为 K
- `MassFrac` — 出口质量分数，无量纲。

  具体来说，是包含以下质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃烧燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 燃烧气体

## 参数

#### 性能表

### **Calibrate Performance Maps** — 使用测量数据标定表格 `selection`

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Performance Maps**，以使用测量数据虚拟标定质量流量和涡轮效率查找表。该对话框将引导您完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入压缩机数据 | 从文件导入此压缩机数据。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  - 转速，Spd，单位为 rad/s - 质量流量，MassFlwRate，单位为 kg/s - 压力比，PrsRatio，无量纲 - 效率，Eff，无量纲    转速、质量流量、压力比和效率分别位于数据文件的第 2 至第 5 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用以下格式。  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... |    Model-Based Calibration Toolbox 将转速和压力比断点值限制为文件中的最大值。  要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 将导入的数据拟合到响应模型。  | 数据 | 响应模型 | | --- | --- | | 质量流量 | *Modeling and Control of Engines and Drivelines*2 中描述的扩展椭圆响应模型 | | 效率 | 多项式 |    要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定响应模型进行标定并生成标定表格。  要评估或调整标定，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定更新这些质量流量和效率参数。  - **Corrected mass flow rate table,   mdot\_corr\_tbl** - **Efficiency table, eta\_comp\_tbl** - **Corrected speed breakpoints,   w\_corr\_bpts1** - **Pressure ratio breakpoints,   Pr\_bpts2** |

### **Corrected mass flow rate table, mdot\_corr\_tbl** — 查找表 `array`

修正质量流量查找表，m˙corr,tbl，作为修正传动轴转速 *ωcorr* 和压力比 *pr* 的函数，单位为 kg/s。

修正质量流量作为传动轴转速和压力比的函数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `mdot_corr_tbl` |
| **值**：| `array` |
| **Data Types:** | `double` |

### **Efficiency table, eta\_comp\_tbl** — 查找表 `array`

效率查找表，ηcomb,tbl，作为修正传动轴转速 *ωcorr* 和压力比 *pr* 的函数，无量纲。

效率作为传动轴转速和压力比的函数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `eta_comp_tbl` |
| **值**：| `array` |
| **Data Types:** | `double` |

### **Corrected speed breakpoints, w\_corr\_bpts1** — 断点 `vector`

修正传动轴转速断点，ωcorr,bpts1，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_corr_bpts1` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **压力比断点，Pr\_bpts2** — 断点 `vector`

压力比断点，pr,bpts2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pr_bpts2` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **参考温度，T\_ref** — 参考 `293.15`（默认）| `scalar`

查找表参考温度，Tref，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_ref` |
| **值：** | `293.15`（默认）| `scalar` |
| **数据类型：** | `double` |

### **参考压力，P\_ref** — 参考 `101325`（默认）| `scalar`

查找表参考压力，Pref，单位为 Pa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `P_ref` |
| **值：** | `101325`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 气体属性

### **理想气体常数，R** — 常数 `287`（默认）| `scalar`

理想气体常数，R，单位为 J/(kg\*K)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R` |
| **值：** | `287`（默认）| `scalar` |
| **数据类型：** | `double` |

### **定压比热，cp** — 比热 `1005`（默认）| `scalar`

定压比热，cp，单位为 J/(kg\*K)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp` |
| **值：** | `1005`（默认）| `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

用于增压发动机的压缩机

Compressor 模块通过使用驱动轴能量来提高进气歧管压力，从而模拟发动机增压。该模块是机械增压器和涡轮增压器模型的组件。该模块使用双向端口连接到入口和出口控制体积以及驱动轴。控制体积为压缩机提供压力、温度和比焓，以计算质量流量和能量流量。为了计算扭矩和流量，驱动轴向压缩机提供转速。通常，压缩机制造商提供作为修正转速和压力比函数的质量流量和效率表。您可以指定查找表来计算质量流量和效率。该模块不支持反向质量流量。

如果您拥有 Model-Based Calibration Toolbox™，请点击 **Calibrate Performance Maps**，使用测量数据虚拟标定质量流量和涡轮效率查找表。

质量流量从入口控制体积流向出口控制体积。

显示质量流量从入口控制体积流向出口控制体积的示意图。

### 虚拟标定

如果您拥有 Model-Based Calibration Toolbox，请点击 **Calibrate Performance Maps**，以使用测量数据对质量流量和涡轮效率查找表进行虚拟标定。该对话框将逐步完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入压缩机数据 | 从文件导入此压缩机数据。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  - 转速，Spd，单位为 rad/s - 质量流量，MassFlwRate，单位为 kg/s - 压力比，PrsRatio，无量纲 - 效率，Eff，无量纲    转速、质量流量、压力比和效率分别位于数据文件的第 2 至第 5 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用此格式。  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... |    Model-Based Calibration Toolbox 将转速和压力比断点值限制为文件中的最大值。  要筛选或编辑数据，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Data Editor。 |
| 生成响应模型 | Model-Based Calibration Toolbox 将导入的数据拟合到响应模型。  | 数据 | 响应模型 | | --- | --- | | 质量流量 | *Modeling and Control of Engines and Drivelines*2 中描述的扩展椭圆响应模型 | | 效率 | 多项式 |    要评估或调整响应模型拟合，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Model Browser。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定响应模型进行标定并生成标定表。  要评估或调整标定，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox CAGE Browser。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定更新这些质量流量和效率参数。  - **Corrected mass flow rate table,   mdot\_corr\_tbl** - **Efficiency table, eta\_comp\_tbl** - **Corrected speed breakpoints,   w\_corr\_bpts1** - **Pressure ratio breakpoints,   Pr\_bpts2** |

### Thermodynamics

该模块使用这些方程对热力学进行建模。

| Calculation | Equations |
| --- | --- |
| Forward mass flow | m˙comp>0  p01=pinlet  p02=poutlet  T01=Tinlet  h01=hinlet |
| First law of thermodynamics | W˙comp=m˙compcp(T01−T02) |
| Isentropic efficiency | ηcomp=h02s−h01h02−h01=T02s−T01T02−T01 |
| Isentropic outlet temperature, assuming ideal gas and constant specific heats | T02s=T01(p02p01)γ−1γ |
| Specific heat ratio | γ=cpcp−R |
| Outlet temperature | T02=T01+T01ηcomb{(p02p01)γ−1γ−1} |
| Heat flows | qinlet=m˙comph01  qoutlet=m˙comph02=m˙compcpT02 |
| Corrected mass flow rate | m˙corr=m˙compT01/Trefp01/pref |
| Corrected speed | ωcorr=ωT01/Tref |
| Pressure ratio | pr=p01p02 |

该模块使用内部信号 `FlwDir` 来跟踪流动方向。

这些方程使用以下变量。

|  |  |
| --- | --- |
| pinlet, p01 | 入口控制体总压 |
| Tinlet, T01 | 入口控制体总温 |
| hinlet, h01 | 入口控制体总比焓 |
| poutlet, p02 | 出口控制体总压 |
| Toutlet | 出口控制体总温 |
| houtlet | 出口控制体总比焓 |
| W˙comp | 驱动轴功率 |
| T02 | 出口总温 |
| h02 | 出口总比焓 |
| m˙comp | 通过压缩机的质量流量 |
| qinlet | 入口热流率 |
| qoutlet | 出口热流率 |
| ηcomp | 压缩机等熵效率 |
| T02s | 等熵出口总温 |
| h02s | 等熵出口总比焓 |
| R | 理想气体常数 |
| cp | 定压比热 |
| γ | 比热比 |
| m˙corr | 修正质量流量 |
| ω | 驱动轴转速 |
| ωcorr | 修正驱动轴转速 |
| Tref | 查找表参考温度 |
| Pref | 查找表参考压力 |
| τcomp | 压缩机驱动轴扭矩 |
| pr | 压比 |
| ηcomb,tbl | 压缩机效率三维查找表 |
| m˙corr,tbl | 修正质量流量三维查找表 |
| ωcorr,bpts1 | 修正转速断点 |
| pr,bpts2 | 压比断点 |

### Power Accounting

对于功率核算，该模块实现以下方程。

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 从轴传递的功率 | −W˙turb |
| `PwrHeatFlwIn` | 端口 A 处的热流率 | qoutlet |
| `PwrHeatFlwOut` | 端口 B 处的热流率 | qoutlet |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrLoss` | 功率损失 | −qinlet−qoutlet+W˙turb |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

这些方程使用以下变量。

|  |  |
| --- | --- |
| W˙turb | 驱动轴功率 |
| qoutlet | 总出口热流率 |
| qinlet | 总入口热流率 |
