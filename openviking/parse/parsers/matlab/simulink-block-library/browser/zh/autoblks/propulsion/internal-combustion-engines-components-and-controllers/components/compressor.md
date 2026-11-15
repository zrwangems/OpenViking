---
type: simulink-block
title: 'Compressor'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'compressor'
documentation_source_path: 'ref/compressor.html'
language: zh-CN
chinese_source: worker-translation
---

# Compressor

## 端口

### 输入

### **Ds** — 驱动轴转速双向连接端口

`ShftSpd` — 信号，包含驱动轴角速度，ω，单位为 rad/s。

### **A** — 入口压力、温度、焓、质量分数双向连接端口

总线，包含入口控制体：

- `InPrs` — 压力，pinlet，单位为 Pa
- `InTemp` — 温度，Tinlet，单位为 K
- `InEnth` — 比焓，hinlet，单位为 J/kg

### **B** — 出口压力、温度、焓、质量分数双向连接端口

总线，包含出口控制体：

- `OutPrs` — 压力，poutlet，单位为 Pa
- `OutTemp` — 温度，Toutlet，单位为 K
- `OutEnth` — 比焓，houtlet，单位为 J/kg

### 输出

### **Info** — 总线信号总线

总线信号，包含这些模块计算值。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `CmprsOutletTemp` | | | 离开压缩机的温度 | K |
| `DriveshftPwr` | | | 驱动轴功率 | W |
| `DriveshftTrq` | | | 驱动轴扭矩 | N·m |
| `CmprsMassFlw` | | | 通过压缩机的质量流量 | kg/s |
| `PrsRatio` | | | 压比 | N/A |
| `DriveshftCorrSpd` | | | 校正驱动轴转速 | rad/s |
| `CmprsEff` | | | 压缩机等熵效率 | N/A |
| `CorrMassFlw` | | | 校正质量流量 | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | 从轴传输的功率 | W |
| `PwrHeatFlwIn` | 端口 A 处的热流量 | W |
| `PwrHeatFlwOut` | 端口 B 处的热流量 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 功率损失 | W |
| `PwrStored` | | *未使用* | W |

### **Ds** — 驱动轴扭矩双向连接端口

`Trq` — 信号，包含驱动轴扭矩，τcomp，单位为 N·m。

### **A** — 入口质量流量、热流量、温度、质量分数双向连接端口

总线，包含：

- `MassFlwRate` — 通过入口的质量流量，m˙comp，单位为 kg/s
- `HeatFlwRate` — 入口热流量，qinlet，单位为 J/s
- `Temp` — 入口温度，单位为 K
- `MassFrac` — 入口质量分数，无量纲。

  具体而言，包含以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气

### **B** — 出口质量流量、热流量、温度、质量分数双向连接端口

总线，包含：

- `MassFlwRate` — 出口质量流量，m˙comp，单位为 kg/s
- `HeatFlwRate` — 出口热流量，qoutlet，单位为 J/s
- `Temp` — 出口温度，单位为 K
- `MassFrac` — 出口质量分数，无量纲。

  具体而言，包含以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气

## 参数

#### 性能表

### **校准性能图** — 使用测量数据校准表 `selection`

如果您有 Model-Based Calibration Toolbox，请点击 **校准性能图**，使用测量数据虚拟校准质量流量和涡轮效率查找表。该对话框会逐步执行以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入压缩机数据 | 从文件导入此压缩机数据。有关详细信息，请参阅使用数据（Model-Based Calibration Toolbox）。  - 转速，Spd，单位为 rad/s - 质量流量，MassFlwRate，单位为 kg/s - 压比，PrsRatio，无量纲 - 效率，Eff，无量纲    转速、质量流量、压比和效率分别位于数据文件的第 2 至第 5 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用以下格式。  |  |  |  |  |  | | --- | --- | --- | --- | --- | | 名称： | Spd | MassFlwRate | PrsRatio | Eff | | 单位： | rad/s | kg/s |  |  | | 数据： | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... |    Model-Based Calibration Toolbox 将转速和压比断点值限制为文件中的最大值。  要筛选或编辑数据，请选择 **在应用程序中编辑**。Model-Based Calibration Toolbox 数据编辑器打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 将导入的数据拟合到响应模型。  | 数据 | 响应模型 | | --- | --- | | 质量流量 | 在 *Modeling and Control of Engines and Drivelines*2 中描述的扩展椭圆响应模型 | | 效率 | 多项式 |    要评估或调整响应模型拟合，请选择 **在应用程序中编辑**。Model-Based Calibration Toolbox 模型浏览器打开。有关详细信息，请参阅模型评估（Model-Based Calibration Toolbox）。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准表。  要评估或调整校准，请选择 **在应用程序中编辑**。Model-Based Calibration Toolbox CAGE 浏览器打开。有关详细信息，请参阅校准查找表（Model-Based Calibration Toolbox）。 |
| 更新模块参数 | 使用校准结果更新这些质量流量和效率参数。  - **校正质量流量表，   mdot\_corr\_tbl** - **效率表，eta\_comp\_tbl** - **校正转速断点，   w\_corr\_bpts1** - **压比断点，   Pr\_bpts2** |

### **校正质量流量表， mdot\_corr\_tbl** — 查找表 `array`

校正质量流量查找表，m˙corr,tbl，作为校正驱动轴转速 *ωcorr* 和压比 *pr* 的函数，单位为 kg/s。

校正质量流量随驱动轴转速和压比变化。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mdot_corr_tbl` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **效率表， eta\_comp\_tbl** — 查找表 `array`

效率查找表，ηcomb,tbl，作为校正驱动轴转速 *ωcorr* 和压比 *pr* 的函数，无量纲。

效率随驱动轴转速和压比变化。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_comp_tbl` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **校正转速断点， w\_corr\_bpts1** — 断点 `vector`

校正驱动轴转速断点，ωcorr,bpts1，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_corr_bpts1` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **压比断点， Pr\_bpts2** — 断点 `vector`

压比断点，pr,bpts2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pr_bpts2` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **参考温度， T\_ref** — 参考 `293.15`（默认） | `scalar`

查找表参考温度，Tref，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_ref` |
| **值：** | `293.15`（默认） | `scalar` |
| **数据类型：** | `double` |

### **参考压力， P\_ref** — 参考 `101325`（默认） | `scalar`

查找表参考压力，Pref，单位为 Pa。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `P_ref` |
| **值：** | `101325`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 气体属性

### **理想气体常数， R** — 常数 `287`（默认） | `scalar`

理想气体常数，R，单位为 J/(kg\*K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R` |
| **值：** | `287`（默认） | `scalar` |
| **数据类型：** | `double` |

### **定压比热， cp** — 比热 `1005`（默认） | `scalar`

定压比热，cp，单位为 J/(kg\*K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp` |
| **值：** | `1005`（默认） | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

用于增压发动机的压缩机

Compressor 模块通过使用驱动轴能量提高进气歧管压力来模拟发动机增压。该模块是机械增压器和涡轮增压器模型的组件。该模块使用双向端口连接到入口和出口控制体以及驱动轴。控制体为压缩机提供压力、温度和比焓，以计算质量和能量流量。为了计算扭矩和流量，驱动轴向压缩机提供转速。通常，压缩机制造商提供作为校正转速和压比函数的质量流量和效率表。您可以指定查找表以计算质量流量和效率。该模块不支持反向质量流量。

如果您有 Model-Based Calibration Toolbox™，请点击 **校准性能图**，使用测量数据虚拟校准质量流量和涡轮效率查找表。

质量流从入口控制体流向出口控制体。

示意图显示质量流从入口控制体流向出口控制体。

### 虚拟校准

如果您有 Model-Based Calibration Toolbox，请点击 **校准性能图**，使用测量数据虚拟校准质量流量和涡轮效率查找表。该对话框会逐步执行以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入压缩机数据 | 从文件导入此压缩机数据。有关详细信息，请参阅使用数据（Model-Based Calibration Toolbox）。  - 转速，Spd，单位为 rad/s - 质量流量，MassFlwRate，单位为 kg/s - 压比，PrsRatio，无量纲 - 效率，Eff，无量纲    转速、质量流量、压比和效率分别位于数据文件的第 2 至第 5 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用以下格式。  |  |  |  |  |  | | --- | --- | --- | --- | --- | | 名称： | Spd | MassFlwRate | PrsRatio | Eff | | 单位： | rad/s | kg/s |  |  | | 数据： | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... |    Model-Based Calibration Toolbox 将转速和压比断点值限制为文件中的最大值。  要筛选或编辑数据，请选择 **在应用程序中编辑**。Model-Based Calibration Toolbox 数据编辑器打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 将导入的数据拟合到响应模型。  | 数据 | 响应模型 | | --- | --- | | 质量流量 | 在 *Modeling and Control of Engines and Drivelines*2 中描述的扩展椭圆响应模型 | | 效率 | 多项式 |    要评估或调整响应模型拟合，请选择 **在应用程序中编辑**。Model-Based Calibration Toolbox 模型浏览器打开。有关详细信息，请参阅模型评估（Model-Based Calibration Toolbox）。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准表。  要评估或调整校准，请选择 **在应用程序中编辑**。Model-Based Calibration Toolbox CAGE 浏览器打开。有关详细信息，请参阅校准查找表（Model-Based Calibration Toolbox）。 |
| 更新模块参数 | 使用校准结果更新这些质量流量和效率参数。  - **校正质量流量表，   mdot\_corr\_tbl** - **效率表，eta\_comp\_tbl** - **校正转速断点，   w\_corr\_bpts1** - **压比断点，   Pr\_bpts2** |

### 热力学

该模块使用这些方程来建模热力学。

| 计算 | 方程 |
| --- | --- |
| 正向质量流量 | m˙comp>0  p01=pinlet  p02=poutlet  T01=Tinlet  h01=hinlet |
| 热力学第一定律 | W˙comp=m˙compcp(T01−T02) |
| 等熵效率 | ηcomp=h02s−h01h02−h01=T02s−T01T02−T01 |
| 等熵出口温度，假设理想气体和定比热 | T02s=T01(p02p01)γ−1γ |
| 比热比 | γ=cpcp−R |
| 出口温度 | T02=T01+T01ηcomb{(p02p01)γ−1γ−1} |
| 热流量 | qinlet=m˙comph01  qoutlet=m˙comph02=m˙compcpT02 |
| 校正质量流量 | m˙corr=m˙compT01/Trefp01/pref |
| 校正转速 | ωcorr=ωT01/Tref |
| 压比 | pr=p01p02 |

该模块使用内部信号 `FlwDir` 跟踪流动方向。

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
| qinlet | 入口热流量 |
| qoutlet | 出口热流量 |
| ηcomp | 压缩机等熵效率 |
| T02s | 等熵出口总温 |
| h02s | 等熵出口总比焓 |
| R | 理想气体常数 |
| cp | 定压比热 |
| γ | 比热比 |
| m˙corr | 校正质量流量 |
| ω | 驱动轴转速 |
| ωcorr | 校正驱动轴转速 |
| Tref | 查找表参考温度 |
| Pref | 查找表参考压力 |
| τcomp | 压缩机驱动轴扭矩 |
| pr | 压比 |
| ηcomb,tbl | 压缩机效率 3-D 查找表 |
| m˙corr,tbl | 校正质量流量 3-D 查找表 |
| ωcorr,bpts1 | 校正转速断点 |
| pr,bpts2 | 压比断点 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 从轴传输的功率 | −W˙turb |
| `PwrHeatFlwIn` | 端口 A 处的热流量 | qoutlet |
| `PwrHeatFlwOut` | 端口 B 处的热流量 | qoutlet |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrLoss` | 功率损失 | −qinlet−qoutlet+W˙turb |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

这些方程使用以下变量。

|  |  |
| --- | --- |
| W˙turb | 驱动轴功率 |
| qoutlet | 出口总热流量 |
| qinlet | 入口总热流量 |
