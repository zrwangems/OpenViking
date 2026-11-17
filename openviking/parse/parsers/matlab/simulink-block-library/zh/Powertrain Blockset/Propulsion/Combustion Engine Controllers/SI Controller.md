---
type: simulink-block
title: 'SI Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Controllers'
documentation_page: 'sicontroller'
documentation_source_path: 'ref/sicontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# SI Controller

## 端口

### 输入

### **TrqCmd** — 指令发动机扭矩 `scalar`

指令发动机扭矩，
*Trqcmd,input*，单位为
N·m。

### **EngSpd** — 测量的发动机转速 `scalar`

测量的发动机转速，*N*，单位为 rpm。

### **AmbPrs** — 测量的绝对环境压力 `scalar`

测量的环境压力，PAmb，单位为 Pa。

### **Map** — 测量的进气歧管绝对压力 `scalar`

测量的进气歧管绝对压力MAP，单位为 Pa。

### **Mat** — 测量的进气歧管绝对温度 `scalar`

测量的进气歧管绝对温度，MAT，单位为 K。

### **IntkCamPhase** — 进气凸轮相位器角度 `scalar`

进气凸轮相位器角度，φICP，单位为 degCrkAdv，即从驻车位置起的曲轴提前角度。

### **ExhCamPhase** — 排气凸轮相位器角度 `scalar`

排气凸轮相位器角度，φECP，单位为 degCrkRet，即从驻车位置起的曲轴延迟角度。

### **Iat** — 进气空气温度 `scalar`

进气空气温度，*IAT*，单位为 K。

### **Ect** — 发动机冷却温度 `scalar`

发动机冷却温度，
*Tcoolant*，单位为 K。

### **EgrVlvInTemp** — EGR 阀入口温度 `scalar`

EGR 阀入口温度，
*Tin,EGR*，单位为 K。

### **EgrVlvAreaPct** — EGR 阀面积百分比 `scalar`

EGR 阀面积百分比，*EGRap*，单位为 %。

### **EgrVlvDeltaPrs** — EGR 阀压差 `scalar`

EGR 阀压差，
*ΔPEGR*，单位为 Pa。

### **O2VoltSen** — 氧传感器电压 `scalar`

用于闭环空燃比（lambda）控制的氧传感器电压，
单位为 mV。

要将模块配置为使用闭环空燃比控制，请在
**Fuel** 选项卡的 **Closed-loop
fuel** 窗格中，选择 **Closed-loop
feedback**。

### **LambdaCmd** — 指令 AFR，lambda `scalar`

指令空燃比（lambda），
*λcmd*，
无量纲。

#### 依赖

要创建此端口，请在 **Fuel** 选项卡的
**Open-loop fuel** 窗格中，选择 **Input
lambda**。

### **IgSw** — 点火开关 `Boolean`

车辆点火开关状态，无量纲。

#### 依赖

要创建此端口，请在 **Stop-Start** 选项卡中，选择 **Enable Engine Stop-Start**。

### **ESSEnable** — 发动机起停使能 `Boolean`

用于使能或禁用起停逻辑的命令，无量纲。

#### 依赖

要创建此端口，请在 **Stop-Start** 选项卡中，选择 **Enable Engine Stop-Start**。选择 **External Enable Port**。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `TrqCmd` | 发动机扭矩 | *Trqcmd* | N·m |
| `LdCmd` | 指令负荷 | *Lcmd* | N/A |
| `ThrPosCmd` | 节气门面积百分比指令 | *TAPcmd* | % |
| `WgAreaPctCmd` | 废气门面积百分比指令 | *WAPcmd* | % |
| `InjPw` | 燃油喷射器脉宽 | Pwinj | ms |
| `SpkAdv` | 点火提前角 | SA | degBTDC |
| `IntkCamPhaseCmd` | 进气凸轮相位器角度指令 | φICPCMD | degCrkAdv |
| `ExhCamPhaseCmd` | 排气凸轮相位器角度指令 | φECPCMD | degCrkRet |
| `EgrVlvAreaPctCmd` | 排气凸轮相位器角度指令 | *EGRapcmd* | % |
| `FuelMassFlwCmd` | EGR 阀面积百分比指令 | m˙fuel,cmd | kg/s |
| `AfrCmd` | 指令空燃比 | *AFRcmd* | N/A |
| `EstEngTrq` | 估计发动机扭矩 | *Trqest* | N·m |
| `EstNrmlzdAirCharg` | 估计归一化气缸空气质量 | N/A | N/A |
| `EstIntkPortMassFlw` | 估计进气道空气质量流量 | m˙intk,est | kg/s |
| `EstIntkAirMassFlw` | 估计空气质量流量 | m˙air,est | kg/s |
| `EstEgrMassFlw` | 估计低压 EGR 质量流量 | m˙EGR,est | kg/s |
| `EstExhManGasTemp` | 估计排气歧管气体温度 | *Texh,est* | K |
| `EngRevLimAct` | 指示转速限制器控制是否激活的标志 | N/A | N/A |
| `ClsdLpFuelMult` | 用于闭环 AFR 控制的燃油喷射器脉宽乘数 | *Pwinj\_mult* | N/A |

### **ThrPosPctCmd** — 节气门面积百分比指令 `scalar`

节气门面积百分比指令，*TAPcmd*。

### **WgAreaPctCmd** — 废气门面积百分比指令 `scalar`

废气门面积百分比指令，*WAPcmd*。

### **InjPw** — 燃油喷射器脉冲宽度 `scalar`

燃油喷射器脉冲宽度，Pwinj，单位为 ms。

### **SpkAdv** — 点火提前角 `scalar`

点火提前角，SA，单位为上止点前曲轴转角（degBTDC）。

### **IntkCamPhaseCmd** — 进气凸轮相位器角度指令 `scalar`

进气凸轮相位器角度指令，φICPCMD。

### **ExhCamPhaseCmd** — 排气凸轮相位器角度指令 `scalar`

排气凸轮相位器角度指令，φECPCMD。

### **EgrVlvAreaPctCmd** — EGR 阀面积百分比指令 `scalar`

EGR 阀面积百分比指令，*EGRapcmd*，单位为 %。

## 参数

### 配置

### **Air mass flow estimation model** — 选择空气质量流量估算模型 `Dual Variable Cam Phasing`（默认）| `Simple Speed-Density`

要计算发动机空气质量流量，请将 SI 发动机配置为使用以下任一空气质量流量模型。

| 空气质量流量模型 | 描述 |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | 使用速度-密度方程计算发动机空气质量流量，将发动机空气质量流量与进气歧管压力和发动机转速相关联。在配气机构设计固定的发动机中，可考虑使用此空气质量流量模型。 |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | 为计算发动机空气质量流量，双独立凸轮相位器模型使用：  - 根据发动机 mapping 测量开发的经验标定参数 - 根据发动机计算机辅助设计（CAD）数据推导的桌面标定参数  与基于使用空气质量流量（MAF）传感器直接测量空气质量流量的典型嵌入式空气质量流量计算相比，此空气质量流量模型具有以下优势：  - 在双凸轮相位可变配气机构应用中消除 MAF 传感器 - 随海拔变化具有合理精度 - 半物理建模方法 - 有界行为 - 适用于电子控制单元（ECU）实现的执行时间 - 系统化开发相对较少数量的标定参数 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `AirEstOptionPopup` |
| **值**：| `Dual Variable Cam Phasing`（默认）| `Simple Speed-Density` |
| **Data Types:** | `character vector` |

#### 依赖关系

下表总结了参数依赖关系。

| 空气质量流量估算模型 | 启用 **Estimation** > **Air** 选项卡上的参数 |
| --- | --- |
| `Dual Variable Cam Phasing` | **进气门关闭时气缸容积表，f\_vivc**  **气缸容积进气凸轮相位断点，f\_vivc\_icp\_bpt**  **气缸滞留质量修正系数，f\_tm\_corr**  **归一化密度断点，f\_tm\_corr\_nd\_bpt**  **发动机转速断点，f\_tm\_corr\_n\_bpt**  **空气质量流量，f\_mdot\_air**  **排气凸轮相位断点，f\_mdot\_air\_ecp\_bpt**  **滞留质量流量断点，f\_mdot\_trpd\_bpt**  **空气质量流量修正系数，f\_mdot\_air\_corr**  **空气质量流量修正的发动机负荷断点，f\_mdot\_air\_corr\_ld\_bpt**  **空气质量流量修正的发动机转速断点，f\_mdot\_air\_corr\_n\_bpt** |
| `Simple Speed-Density` | **Speed-density volumetric efficiency, f\_nv**  **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt**  **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** |

### **Torque estimation model** — 选择扭矩估计模型 `Torque Structure`（默认）| `Simple Torque Lookup`

要计算制动扭矩，请将 SI 发动机配置为使用以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| SI Engine Torque Structure Model | 对于结构化制动扭矩计算，SI 发动机使用内扭矩、摩擦扭矩、最佳点火、点火效率和 lambda 效率的表。如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，您可以： - 基于从模型或实验室测试记录的作为曲轴转角函数的缸内压力，在桌面仿真和 HIL 台架上仿真高级闭环发动机控制。 - 仿真由于高频曲轴扭转而在发动机下游产生的传动系统振动。 - 通过使用喷油器脉冲宽度输入，仿真由于稀薄运行或火花塞积垢导致的发动机失火。 - 仿真气缸停用效果（进气门和排气门关闭，不喷射燃油）对单个气缸压力、均值气流、均值扭矩和基于曲轴转角的扭矩的影响。 - 仿真断油效果对单个气缸压力、均值扭矩和基于曲轴转角的扭矩的影响。 |
| SI Engine Simple Torque Model | 对于简单制动扭矩计算，SI 发动机模块使用作为发动机转速和负载函数的扭矩查找表映射。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TrqEstOptionPopup` |
| **值**：| `Torque Structure`（默认）| `Simple Torque Lookup` |
| **Data Types:** | `character vector` |

#### 依赖关系

下表总结了参数依赖关系。

| 扭矩估计模型 | 启用 **Estimation** > **Torque** 选项卡上的参数 |
| --- | --- |
| `Torque Structure` | **内部扭矩表，f\_tq\_inr**  **摩擦扭矩表，f\_tq\_fric**  **摩擦扭矩的发动机温度修正量，f\_fric\_temp\_mod**  **发动机温度修正量断点，f\_fric\_temp\_bpt**  **泵气扭矩表，f\_tq\_pump**  **最佳点火提前角表，f\_sa\_opt**  **内部扭矩负荷断点，f\_tq\_inr\_l\_bpt**  **内部扭矩转速断点，f\_tq\_inr\_n\_bpt**  **点火效率表，f\_m\_sa**  **相对最佳点火提前角的点火延迟，f\_del\_sa\_bpt**  **Lambda效率，f\_m\_lam**  **Lambda断点，f\_m\_lam\_bpt** |
| `Simple Torque Lookup` | **Torque table, f\_tq\_nl**  **Torque table load breakpoints, f\_tq\_nl\_l\_bpt**  **Torque table speed breakpoints, f\_tq\_nl\_n\_bpt** |

### Controls

#### Air

### **Engine commanded load table, f\_lcmd** — 查找表 `array`

指令发动机负载查找表 fLcmd 是指令扭矩和发动机转速的函数

Lcmd=fLcmd(Tcmd,N)

其中：

- *Lcmd*=*L* 是指令发动机负载，无量纲。
- *Tcmd* 是指令扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

指令发动机负载与指令扭矩和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_lcmd` |
| **值**：| `array` |
| **Data Types:** | `double` |

### **Torque command breakpoints, f\_lcmd\_tq\_bpt** — 断点 `[15 26.43 37.86 49.29 60.71 72.14 83.57 95 106.4 117.9 129.3 140.7 152.1 163.6 175]`（默认）| `vector`

扭矩指令断点，单位为 N·m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_lcmd_tq_bpt` |
| **值**：| `vector` |
| **Data Types:** | `double` |

### **Speed breakpoints, f\_lcmd\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_lcmd_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Throttle area percent, f\_tap** — 查找表，% `array`

节气门面积百分比指令查找
表，fTAPcmd，
是指令负荷和发动机转速的函数

TAPcmd=fTAPcmd(Lcmd,N)

其中：

- *TAPcmd* 是
  节气门面积百分比指令，单位为百分比。
- *Lcmd*=*L* 是
  指令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

节气门面积百分比指令与指令发动机负荷和发动机转速的三维图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tap` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Throttle area percent load breakpoints, f\_tap\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

节气门面积百分比负荷断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tap_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Throttle area percent speed breakpoints, f\_tap\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

节气门面积百分比转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tap_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Throttle area percent to position percent table, f\_tpp** — 查找表 `[0 100]`（默认）| `vector`

节气门位置百分比指令查找
表，fTPPcmd，
是节气门面积百分比指令的函数

TPPcmd=fTPPcmd(TAPcmd)

其中：

- *TPPcmd* 是
  节气门位置百分比指令，单位为百分比。
- *TAPcmd* 是
  节气门面积百分比指令，单位为百分比。

节气门位置与节气门面积的图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tpp` |
| **值：** | `[0 100]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Throttle area percent to position percent area breakpoints, f\_tpp\_tap\_bpt** — 断点 `[0 100]`（默认）| `vector`

节气门面积百分比到位置百分比的面积断点，
无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tpp_tap_bpt` |
| **值：** | `[0 100]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Wastegate area percent, f\_wap** — 查找表，% `array`

废气门面积百分比指令查找表 fWAPcmd 是指令发动机负荷和发动机转速的函数

WAPcmd=fWAPcmd(Lcmd,N)

其中：

- *WAPcmd* 是废气门面积百分比指令，单位为百分比。
- *Lcmd*=*L* 是指令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

废气门面积百分比指令与指令发动机负荷和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_wap` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Load breakpoints, f\_wap\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

负荷断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_wap_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Speed breakpoints, f\_wap\_n\_bpt** — 断点，rpm `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_wap_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Intake cam phaser angle, f\_icp** — 查找表 `array`

进气凸轮相位器角度指令查找表 fICPCMD 是发动机负荷和发动机转速的函数

φICPCMD=fICPCMD(Lest,N)

其中：

- φICPCMD 是指令进气凸轮相位器角度，单位为从驻车位置起的曲轴转角提前量。
- *Lest*=*L* 是指令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

指令进气凸轮相位器角度与指令发动机负荷和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_icp` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Exhaust cam phaser angle, f\_ecp** — 查找表 `array`

排气凸轮相位器角度指令查找表 fECPCMD 是发动机负荷和发动机转速的函数

φECPCMD=fECPCMD(Lest,N)

其中：

- φECPCMD 是指令排气凸轮相位器角度，单位为从驻车位置起的曲轴转角延迟量。
- *Lest*=*L* 是估计发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

指令排气凸轮相位器角度与估计发动机负荷和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_ecp` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Load breakpoints, f\_cp\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

负荷断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_cp_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Speed breakpoints, f\_cp\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_cp_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **指令 EGR 百分比，f\_egrpct\_cmd** — 查找表 `array`

EGR 百分比指令 *EGRpct,cmd* 查找表是估计发动机负荷和发动机转速的函数

EGRpct,cmd=fEGRpct,cmd(Lest,N)

其中：

- *EGRpct,cmd* 是指令 EGR 百分比，无量纲。
- *Lest*=*L* 是估计发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

指令 EGR 百分比与估计发动机负荷和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egrpct_cmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **负荷断点，f\_egrpct\_ld\_bpt** — 断点 `[0 0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

发动机负荷断点 *L*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egrpct_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点，f\_egrpct\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

发动机转速断点 *N*，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egrpct_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR 阀面积百分比，f\_egr\_areapct\_cmd** — 查找表 `array`

EGR 面积百分比指令 *EGRapcmd* 查找表是归一化质量流量和压力比的函数

EGRapcmd=fEGRap,cmd(m˙EGRstd,cmdm˙EGRstd,max,Pout,EGRPin,EGR)

其中：

- *EGRapcmd* 是指令 EGR 面积百分比，无量纲。
- m˙EGRstd,cmdm˙EGRstd,max 是归一化质量流量，无量纲。
- Pout,EGRPin,EGR 是压力比，无量纲。

指令 EGR 百分比与归一化质量流量和压力比的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_areapct_cmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **开启 EGR 阀标准流量，f\_egr\_max\_stdflow** — 断点 `[74.87 74.87 74.74 74.39 73.81 72.98 71.91 70.58 68.97 67.06 64.84 62.25 59.27 55.81 51.79 47.07 36.33 24.22 12.11 0]`（默认）| `vector`

最大标准 EGR 阀质量流量断点 m˙EGRstd,max，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_max_stdflow` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **归一化 EGR 阀标准流量断点，f\_egr\_areapct\_nrmlzdflow\_bpt** — 断点 `[0 0.03448 0.06897 0.1034 0.1379 0.1724 0.2069 0.2414 0.2759 0.3103 0.3448 0.3793 0.4138 0.4483 0.4828 0.5172 0.5517 0.5862 0.6207 0.6552 0.6897 0.7241 0.7586 0.7931 0.8276 0.8621 0.8966 0.931 0.9655 1]`（默认）| `vector`

归一化质量流量断点 m˙EGRstd,cmdm˙EGRstd,max，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_areapct_nrmlzdflow_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR valve pressure ratio breakpoints, f\_egr\_areapct\_pr\_bpt** — 断点 `vector`

压力比断点，Pout,EGRPin,EGR，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_areapct_pr_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 燃油

### **Injector slope, Sinj** — 斜率 `6.452`（默认）| `scalar`

燃油喷射器斜率，Sinj，单位为 mg/ms。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sinj` |
| **值：** | `6.452`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Stoichiometric air-fuel ratio, afr\_stoich** — 比值 `14.6`（默认）| `scalar`

理论空燃比，*AFRstoich*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `afr_stoich` |
| **值：** | `14.6`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Relative air-fuel ratio lambda, f\_lamcmd** — 空燃比（AFR）查找表 `array`

指令 lambda，λcmd，查找表是估计发动机负荷和测量发动机转速的函数

λcmd=fλcmd(Lest,N)

其中：

- λcmd 是指令相对 AFR，无量纲。
- *Lest*=*L* 是指令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

指令相对 AFR 与指令发动机负荷和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_lamcmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **Fuel** 选项卡的 **Open-loop fuel** 窗格中，清除 **Input lambda**。

### **Load breakpoints, f\_lamcmd\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

负荷断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_lamcmd_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **Fuel** 选项卡的 **Open-loop fuel** 窗格中，清除 **Input lambda**。

### **Speed breakpoints, f\_lamcmd\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_lamcmd_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **Fuel** 选项卡的 **Open-loop fuel** 窗格中，清除 **Input lambda**。

### **Engine startup lambda enrichment delta vs coolant temperature, f\_startup\_lambda\_delta** — 查找表 `[0.5 0.3 0.2 0]`（默认）| `vector`

发动机启动 lambda 加浓增量随冷却液温度变化的函数，无量纲。

SI Controller 模块使用此参数来考虑在启动期间向火花点火（SI）发动机提供的额外燃油。如果发动机转速大于 **Engine cranking speed** 参数，SI Controller 模块会使用指数衰减的 delta lambda 对最佳相对空燃比（lambda）进行加浓。为了初始化 delta lambda，该模块使用 **Engine startup lambda enrichment delta vs coolant temperature** 参数来创建作为发动机冷却液温度函数的 lambda 加浓表。delta lambda 根据 **Engine startup lambda enrichment delta time constant vs coolant temperature** 参数指定的时间常数按指数衰减至零。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_startup_lambda_delta` |
| **值**：| `[0.5 0.3 0.2 0]`（默认）| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要创建此参数，请在 **Fuel** 选项卡的 **Open-loop fuel** 窗格中清除 **Input lambda**。

### **Engine startup lambda enrichment delta time constant vs coolant temperature, f\_startup\_lambda\_delta\_timecnst** — Lambda 时间常数 `[90 40 12 0]`（默认）| `vector`

发动机启动 lambda 加浓增量时间常数随冷却液温度变化的函数，单位为 s。

SI Controller 模块使用此参数来考虑在启动期间向火花点火（SI）发动机提供的额外燃油。如果发动机转速大于 **Engine cranking speed** 参数，SI Controller 模块会使用指数衰减的 delta lambda 对最佳相对空燃比（lambda）进行加浓。为了初始化 delta lambda，该模块使用 **Engine startup lambda enrichment delta vs coolant temperature** 参数来创建作为发动机冷却液温度函数的 lambda 加浓表。delta lambda 根据 **Engine startup lambda enrichment delta time constant vs coolant temperature** 参数指定的时间常数按指数衰减至零。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_startup_lambda_delta_timecnst` |
| **值**：| `[90 40 12 0]`（默认）| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要创建此参数，请在 **Fuel** 选项卡的 **Open-loop fuel** 窗格中清除 **Input lambda**。

### **Engine startup coolant temperature breakpoints, f\_startup\_ect\_bpt** — 断点 `[-40 0 20 50]`（默认）| `vector`

发动机启动冷却液温度断点，单位为 C。

SI Controller 模块使用此参数来考虑在启动期间向火花点火（SI）发动机提供的额外燃油。如果发动机转速大于 **Engine cranking speed** 参数，SI Controller 模块会使用指数衰减的 delta lambda 对最佳相对空燃比（lambda）进行加浓。为了初始化 delta lambda，该模块使用 **Engine startup lambda enrichment delta vs coolant temperature** 参数来创建作为发动机冷却液温度函数的 lambda 加浓表。delta lambda 根据 **Engine startup lambda enrichment delta time constant vs coolant temperature** 参数指定的时间常数按指数衰减至零。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_startup_ect_bpt` |
| **值：** | `[-40 0 20 50]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **Fuel** 选项卡的 **Open-loop
fuel** 窗格中，清除 **Input lambda**。

### **Closed-loop feedback** — 最小化指令 AFR 误差 `off`（默认） | `on`

选择此选项以最小化指令空燃比（lambda）
*λcmd* 误差。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelEn` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character array` |

### **Dither** — 模拟催化转化效率 `off`（默认） | `on`

配置模块以模拟 dither。对于开环分析，选择
此选项以调谐至最大催化转化效率。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OpenLpDitherEn` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character array` |

#### 依赖关系

默认情况下，选择 **Closed-loop feedback**
会将模块配置为模拟 dither。

要为开环空燃比（lambda）
指令启用此参数，请清除 **Closed-loop feedback**。

选择此参数将启用以下参数：

- **Lambda dither amplitude,
  LambdaDitherAmp**
- **Lambda dither frequency,
  LambdaDitherFrq**

### **Closed-loop fuel proportional gain, ClsdLpFuelPGain** — 比例增益 `0.005`（默认） | `scalar`

闭环燃油比例增益，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelPGain` |
| **值：** | `0.005`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的
**Closed-loop fuel** 窗格中，选择 **Closed-loop
feedback**。

### **Closed-loop fuel integral gain, ClsdLpFuelIGain** — 积分增益 `0.05`（默认） | `scalar`

闭环燃油积分增益，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelIGain` |
| **值：** | `0.05`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的
**Closed-loop fuel** 窗格中，选择 **Closed-loop
feedback**。

### **Closed-loop fuel integrator limit, ClsdLpFuelIntgLmt** — 积分器限幅 `0.2`（默认） | `scalar`

闭环燃油积分器限幅，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelIntgLmt` |
| **值：** | `0.2`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的
**Closed-loop fuel** 窗格中，选择 **Closed-loop
feedback**。

### **Lambda dither amplitude, LambdaDitherAmp** — 幅值 `0.03`（默认） | `scalar`

Lambda dither 幅值，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LambdaDitherAmp` |
| **值：** | `0.03`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback** 或 **Dither**。

### **Lambda 抖动频率，LambdaDitherFrq** — 频率 `0.75`（默认） | `scalar`

Lambda 抖动频率，单位为 Hz。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LambdaDitherFrq` |
| **值：** | `0.75`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback** 或 **Dither**。

### **氧传感器化学计量比复位电压，O2ResetStoichVoltSen** — 闭环 AFR 控制 `2500`（默认） | `scalar`

氧传感器化学计量比复位电压，O2ResetStoichVoltSen，单位为 mV。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2ResetStoichVoltSen` |
| **值：** | `2500`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback**。

### **氧传感器最小电压复位，O2ResetMinVoltSen** — 闭环 AFR 控制 `0`（默认） | `scalar`

氧传感器最小电压复位，O2ResetMinVoltSen，单位为 mV。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2ResetMinVoltSen` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback**。

### **氧传感器最大电压复位，O2ResetMaxVoltSen** — 闭环 AFR 控制 `5000`（默认） | `scalar`

氧传感器最大电压复位，O2ResetMaxVoltSen，单位为 mV。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2ResetMaxVoltSen` |
| **值：** | `5000`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback**。

### **氧传感器电压学习更新周期，O2LearnUpdatePerSen** — 闭环 AFR 控制 `4`（默认） | `scalar`

氧传感器电压学习更新周期，O2LearnUpdatePerSen，单位为 mV。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2LearnUpdatePerSen` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback**。

### **氧传感器电压幅值最小值，O2AmpMinVoltSen** — 闭环 AFR 控制 `250`（默认） | `scalar`

氧传感器电压幅值最小值，O2AmpMinVoltSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2AmpMinVoltSen` |
| **值：** | `250`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback**。

### **氧传感器就绪电压，O2ReadyVoltSen** — 闭环 AFR 控制 `1150`（默认） | `scalar`

氧传感器就绪电压，O2ReadyVoltSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2ReadyVoltSen` |
| **值：** | `1150`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback**。

### **氧传感器未就绪电压，O2NotReadyVoltSen** — 闭环 AFR 控制 `1950`（默认） | `scalar`

氧传感器未就绪电压，O2NotReadyVoltSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2NotReadyVoltSen` |
| **值：** | `1950`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Closed-loop feedback**。

#### 点火

### **点火提前角表，f\_sa** — 查找表 `array`

点火提前角查找表是估计负荷和发动机转速的函数。

SA=fSA(Lest,N)

其中：

- *SA* 是点火提前角，单位为曲轴提前角。
- *Lest*=*L* 是命令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

点火提前角与命令发动机负荷和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_sa` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **负荷断点，f\_sa\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector`

负荷断点，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_sa_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点，f\_sa\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认） | `vector`

转速断点，单位为 rpm。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_sa_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 怠速

### **目标怠速转速，N\_idle** — 转速 `750`（默认） | `scalar`

目标怠速转速，*Nidle*，单位为 rpm。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_idle` |
| **值：** | `750`（默认） | `scalar` |
| **数据类型：** | `double` |

### **启用扭矩命令限值，Trq\_idlecmd\_enable** — 扭矩 `1`（默认） | `scalar`

用于启用怠速控制器的扭矩，*Trqidlecmd,enable*，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_idlecmd_enable` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **最大扭矩指令，Trq\_idlecmd\_max** — 扭矩 `50`（默认） | `scalar`

最大怠速控制器指令扭矩，*Trqidlecmd,max*，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_idlecmd_max` |
| **值：** | `50`（默认） | `scalar` |
| **数据类型：** | `double` |

### **比例增益，Kp\_idle** — PI 控制器 `0.05`（默认） | `scalar`

怠速控制的比例增益，*Kp,idle*，单位为 N·m/rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_idle` |
| **值：** | `0.05`（默认） | `scalar` |
| **数据类型：** | `double` |

### **积分增益，Ki\_idle** — PI 控制器 `0.2`（默认） | `scalar`

怠速控制的积分增益，*Ki,idle*，单位为 N·m/(rpm·s)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki_idle` |
| **值：** | `0.2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **转速限制器速度阈值，EngRevLim** — 发动机转速限制 `6000`（默认） | `scalar`

发动机转速限制，*Nlim*，单位为 rpm。

如果发动机转速 *N* 超过发动机转速限制 *Nlim*，模块将指令发动机扭矩设置为 0。

为了在发动机转速接近速度限制时平滑地将扭矩指令过渡到 0，模块实现了一个查找表乘数。该查找表将扭矩指令乘以一个值，该值范围从 0（发动机转速超过限制）到 1（发动机转速未超过限制）。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngRevLim` |
| **值：** | `6000`（默认） | `scalar` |
| **数据类型：** | `double` |

### **发动机起动转速，CrankSpeed** — 发动机转速 `150`（默认） | `scalar`

发动机起动转速，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CrankSpeed` |
| **值：** | `150`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 起停

### **启用发动机起停** — 选择以启用发动机起停逻辑 `off`（默认） | `on`

选择以启用发动机起停逻辑。选择此选项将激活附加参数以修改发动机起停模块的行为。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ESSEnable` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **外部启用端口** — 创建输入端口 `off`（默认） | `on`

选择以向发动机控制器模块添加一个端口，用于启用或禁用起停逻辑。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ESSExternalPortEnable` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上选择 **Enable Engine Stop-Start**。

### **Engine stop time, EngStopTime** — 发动机停止时间 `5`（默认） | `scalar`

停止-启动逻辑的发动机停止时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngStopTime` |
| **值：** | `5`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上选择 **Enable Engine Stop-Start**。

### **Catalyst light off time, CatLightOffTime** — 催化器起燃时间 `0`（默认） | `scalar`

停止-启动逻辑的催化器起燃时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CatLightOffTime` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上选择 **Enable Engine Stop-Start**。

### **Sample time, Ts** — 采样时间 `0.01`（默认） | `scalar`

停止-启动逻辑的采样时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ts` |
| **值：** | `0.01`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上选择 **Enable Engine Stop-Start**。

### 估计

#### 空气

### **Number of cylinders, NCyl** — 发动机气缸数 `4`（默认） | `scalar`

发动机气缸数，Ncyl。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Crank revolutions per power stroke, Cps** — 每做功冲程的转数 `2`（默认） | `scalar`

每做功冲程的曲轴转数，Cps，单位为 rev/stroke。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Total displaced volume, Vd** — 体积 `0.0015`（默认） | `scalar`

排量，Vd，单位为 m^3。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Ideal gas constant air, Rair** — 常数 `287`（默认） | `scalar`

理想气体常数，Rair，单位为 J/(kg·K)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rair` |
| **值：** | `287`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Air standard pressure, Pstd** — 压力 `101325`（默认）| `scalar`

标准空气压力 Pstd，单位为 Pa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `101325`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Air standard temperature, Tstd** — 温度 `293.15`（默认）| `scalar`

标准空气温度 Tstd，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tstd` |
| **值：** | `293.15`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Speed-density volumetric efficiency, f\_nv** — 查找表 `array`

发动机容积效率查找表 fηv 是进气歧管绝对压力和发动机转速的函数

ηv=fηv(MAP,N)

其中：

- ηv 是发动机容积效率，无量纲。
- *MAP* 是进气歧管绝对压力，单位为 KPa。
- *N* 是发动机转速，单位为 rpm。

发动机容积效率与进气歧管绝对压力和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Air mass flow estimation model** 参数选择为 `Simple Speed-Density`。

### **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — 断点 `[31 40.64 50.29 59.93 69.57 79.21 88.86 98.5 108.1 117.8 127.4 137.1 146.7 156.4 166]`（默认）| `vector`

速度密度容积效率查找表的进气歧管压力断点，单位为 KPa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_prs_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Air mass flow estimation model** 参数选择为 `Simple Speed-Density`。

### **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

速度密度容积效率查找表的发动机转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Air mass flow estimation model** 参数选择为 `Simple Speed-Density`。

### **Cylinder volume at intake valve close table, f\_vivc** — 二维查找表 `array`

进气门关闭时气缸容积表（IVC），fVivc 是进气凸轮相位器角度的函数

VIVC=fVivc(φICP)

其中：

- VIVC 是 IVC 时的气缸容积，单位为 L。
- φICP 是进气凸轮相位器角度，以相对于进气相位器驻车位置的曲轴提前角表示。

气缸容积与进气凸轮相位器角度的图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_vivc` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow estimation model** 参数，选择 `Dual Variable Cam Phasing`。

### **Engine speed breakpoints, f\_tm\_corr\_n\_bpt** — 断点 `[750 973.7 1197 1421 1645 1868 2092 2316 2539 2763 2987 3211 3434 3658 3882 4105 4329 4553 4776 5000]`（默认）| `vector`

发动机转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow estimation model** 参数，选择 `Dual Variable Cam Phasing`。

### **Cylinder volume intake cam phase breakpoints, f\_vivc\_icp\_bpt** — 断点 `[0 2.632 5.263 7.895 10.53 13.16 15.79 18.42 21.05 23.68 26.32 28.95 31.58 34.21 36.84 39.47 42.11 44.74 47.37 50]`（默认）| `vector`

进气门关闭时气缸容积表的断点。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_vivc_icp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow estimation model** 参数，选择 `Dual Variable Cam Phasing`。

### **Cylinder trapped mass correction factor, f\_tm\_corr** — 查找表 `array`

截留质量修正系数表 fTMcorr 是归一化密度和发动机转速的函数

TMcorr=fTMcorr(ρnorm, N)

其中：

- TMcorr 是截留质量修正乘数，无量纲。
- ρnorm 是归一化密度，无量纲。
- *N* 是发动机转速，单位为 rpm。

截留质量修正乘数与归一化密度和发动机转速的三维图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow estimation model** 参数，选择 `Dual Variable Cam Phasing`。

### **Normalized density breakpoints, f\_tm\_corr\_nd\_bpt** — 断点 `[0.3 0.3895 0.4789 0.5684 0.6579 0.7474 0.8368 0.9263 1.016 1.105 1.195 1.284 1.374 1.463 1.553 1.642 1.732 1.821 1.911 2]`（默认）| `vector`

归一化密度断点。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr_nd_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow estimation model** 参数，选择 `Dual Variable Cam Phasing`。

### **Intake mass flow, f\_mdot\_intk** — 查找表 `array`

相位器进气质量流量模型查找表是排气凸轮相位器角度和截留空气质量流量的函数

m˙intkideal=fintkideal(φECP,TMflow)

其中：

- m˙intkideal 是任意凸轮相位器角度下的发动机进气道质量流量，单位为 g/s。
- φECP 是排气凸轮相位器角度，以相对于排气相位器停放位置的曲轴转角延迟度数表示。
- TMflow 是在当前发动机转速下等效于修正截留质量的流量，单位为 g/s。

空气质量流量与排气凸轮相位器角度和流量等效值的三维图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_intk` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Air mass flow estimation model** 参数选择 `Dual Variable Cam Phasing`。

### **Exhaust cam phase breakpoints, f\_mdot\_air\_ecp\_bpt** — 断点 `[0 2.632 5.263 7.895 10.53 13.16 15.79 18.42 21.05 23.68 26.32 28.95 31.58 34.21 36.84 39.47 42.11 44.74 47.37 50]`（默认）| `vector`

空气流量查找表的排气凸轮相位器断点。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_ecp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Air mass flow estimation model** 参数选择 `Dual Variable Cam Phasing`。

### **Trapped mass flow breakpoints, f\_mdot\_trpd\_bpt** — 断点 `[0 5.79 11.58 17.37 23.16 28.95 34.74 40.53 46.32 52.11 57.89 63.68 69.47 75.26 81.05 86.84 92.63 98.42 104.2 110]`（默认）| `vector`

空气流量查找表的截留质量流量断点。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_trpd_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Air mass flow estimation model** 参数选择 `Dual Variable Cam Phasing`。

### **Air mass flow correction factor, f\_mdot\_air\_corr** — 查找表 `array`

进气空气流量修正查找表 faircorr 是理想负载和发动机转速的函数

m˙air=m˙intkidealfaircorr(Lideal,N)

其中：

- Lideal 是任意凸轮相位器角度下的发动机负载（归一化气缸空气量），未针对最终稳态凸轮相位器角度进行修正，无量纲。
- *N* 是发动机转速，单位为 rpm。
- m˙air 是稳态凸轮相位器角度下的发动机进气空气流量最终修正值，单位为 g/s。
- m˙intkideal 是任意凸轮相位器角度下的发动机进气道质量流量，单位为 g/s。

发动机进气空气流量最终修正值与发动机负载和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_corr` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Air mass flow estimation model** 参数选择 `Dual Variable Cam Phasing`。

### **Engine load breakpoints for air mass flow correction, f\_mdot\_air\_corr\_ld\_bpt** — 断点 `vector`

空气流量最终修正的发动机负载断点。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_corr_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Air mass flow estimation model** 参数选择 `Dual Variable Cam Phasing`。

### **Engine speed breakpoints for air mass flow correction, f\_mdot\_air\_n\_bpt** — 断点 `[750 973.7 1197 1421 1645 1868 2092 2316 2539 2763 2987 3211 3434 3658 3882 4105 4329 4553 4776 5000]`（默认）| `vector`

空气流量最终修正的发动机转速断点。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **空气质量流量估算模型** 参数，选择 `双可变凸轮相位`。

### **EGR 流量时间常数，tau\_egr** — 常量 `0.2`（默认） | `scalar`

EGR 流量时间常数，
*τEGR*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_egr` |
| **值：** | `0.2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **进气系统压力比表，f\_intksys\_stdflow\_pr** — 表 `array`

压力比是标准质量流量的函数

Pout,EGRPamb=fintksys,pr(m˙air,std)

其中：

- m˙air,std 是标准质量流量，单位为 g/s。
- Pout,EGRPamb 是压力比，无量纲。

压力比与质量流量的关系图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_intksys_stdflow_pr` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **进气压力比的标准质量流量断点，f\_intksys\_stdflow\_bpt** — 断点 `[0 29.67 59.34 89.01 117.8 144.1 155.7 166 175.2 183.3 190.7 197 202.7 207.7 212.2 216.1 219.4 222.2 224.5 226.4]`（默认） | `vector`

标准质量流量，m˙air,std，单位为 g/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_intksys_stdflow_bpt` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **EGR 阀标准质量流量，f\_egr\_stdflow** — 表 `vector`

EGR 阀标准质量流量查找
表是 EGR 阀面积百分比和压力比的函数

m˙EGR,std=fEGR,std(EGRap,Pout,EGRPin,EGR)

其中：

- m˙EGR,std 是 EGR 阀标准质量流量，无量纲。
- *EGRap* 是 EGR 阀流通面积百分比，单位为百分比。
- Pout,EGRPin,EGR 是压力比，无量纲。

标准质量流量与压力比和流通面积百分比的三维图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **EGR 阀标准流量压力比断点，f\_egr\_stdflow\_pr\_bpt** — 断点 `vector`

EGR 阀标准流量压力比，Pout,EGRPin,EGR，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow_pr_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR 阀标准流量面积百分比断点，f\_egr\_stdflow\_egrap\_bpt** — 断点 `[0;5;10;15;20;25;30;35;40;45;50;55;60;65;70;75;80;85;90;95;100]`（默认） | `vector`

EGR 阀流通面积百分比，*EGRap*，单位为
百分比。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow_egrap_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 扭矩

### **Torque table, f\_tq\_nl** — 查找表 `[L x N] array`

对于简单扭矩查找表模型，SI 发动机使用一个作为发动机转速和负载函数的查找表映射，Tbrake=fTnL(L,N)，其中：

- Tbrake 是考虑点火提前角、AFR 和摩擦效应后的发动机制动扭矩，单位为 N·m。
- *L* 是发动机负载，表示为归一化气缸空气质量，无量纲。
- *N* 是发动机转速，单位为 rpm。

考虑点火提前角后的发动机制动扭矩相对于发动机负载和发动机转速的 3D 图

简单扭矩查找模型假设标定数据包含负扭矩值，以表示不点火发动机负载 (L) 与转速 (N) 工况。标定表 (L-by-N) 在第一行表数据 (1-by-N) 中包含不点火数据。当输送到发动机的燃料为零时，模型在 AFR 大于或等于 100 时使用第一行表数据 (1-by-N)。100 AFR 由断油或无法发生燃烧的极稀运行导致。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Simple Torque Lookup`。

### **Torque table load breakpoints, f\_tq\_nl\_l\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector` | `[1 x L] vector`

发动机负载断点，*L*，无量纲。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Simple Torque Lookup`。

### **Torque table speed breakpoints, f\_tq\_nl\_n\_bpt** — 断点 `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认） | `vector` | `[1 x N] vector`

发动机转速断点，*N*，单位为 rpm。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Simple Torque Lookup`。

### **Crank angle pressure and torque** — 启用曲轴转角信号 `off`（默认） | `on`

如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，您可以：

- 基于模型或实验室测试记录的作为曲轴转角函数的气缸压力，在桌面仿真和 HIL 台架上仿真高级闭环发动机控制。
- 仿真由于高频曲轴扭转振动引起的发动机下游动力传动系统振动。
- 通过使用喷油器脉冲宽度输入，仿真由于稀薄运行或火花塞积污导致的发动机失火。
- 仿真气缸停用效果（进气和排气门关闭、无喷射燃料）对单个气缸压力、平均值气流、平均值扭矩和基于曲轴转角的扭矩的影响。
- 仿真断油对单个气缸压力、平均值扭矩和基于曲轴转角的扭矩的影响。

#### 依赖关系

要启用此参数，请将 **Torque model** 设置为 `Torque Structure`。

### **Cylinder pressure, f\_crk\_prs** — 气缸压力表 `L x M x N` array

气缸压力表 *Prs*，作为转速 *N*、负载 *L* 和曲轴转角 *M* 的函数，单位为 Pa。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Brake torque, f\_crk\_btq** — 制动扭矩表 `L x M x N` array

制动扭矩表 *Tbrake*，作为转速 *N*、负载 *L* 和曲轴转角 *M* 的函数，单位为 N·m。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Speed breakpoints, f\_crk\_n\_bpt** — 转速断点 `[750 5000]`（默认） | `1 x N` vector

转速断点，*N*，单位为 rpm。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Load breakpoints, f\_crk\_l\_bpt** — 负载断点 `[0.2 1.4]`（默认）| `1 x L` 向量

负载断点，*L*。无量纲。

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。选择 **Crank angle
pressure and torque**。

### **Crank angle breakpoints, f\_crk\_ang\_bpt** — 曲轴转角断点 `[60 660]`（默认）| `1 x M` 向量

曲轴转角断点，*M*，单位为 deg。

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。选择 **Crank angle
pressure and torque**。

### **TDC compression angles by cylinder, f\_crk\_tdc\_ang** — 按气缸的上止点压缩角 `[0 540 180 360]`（默认）| 向量

按气缸的上止点（TDC）压缩角，单位为 deg。

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。选择 **Crank angle
pressure and torque**。

### **Inner torque table, f\_tq\_inr** — 查找表 `array`

内部
扭矩查找表 fTqinr，
是发动机转速和发动机负载的函数，Tqinr=fTqinr(L,N)，
其中：

- Tqinr 是
  基于总指示平均有效压力的内部扭矩，单位为
  N·m。
- *L* 是任意凸轮
  相位角下的发动机负载，已针对最终稳态凸轮相位角
  进行修正，无量纲。
- *N* 是发动机转速，单位为 rpm。

基于总指示平均有效压力的内部扭矩与任意凸轮相位角下的发动机负载及发动机转速的 3D 图

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。

### **Friction torque table, f\_tq\_fric** — 查找表 `array`

摩擦扭矩查找表 fTfric，
是发动机转速和发动机负载的函数，Tfric=fTfric(L,N)，
其中：

- Tfric 是
  内部扭矩的摩擦扭矩偏移，单位为 N·m。
- *L* 是任意凸轮
  相位角下的发动机负载，已针对最终稳态凸轮相位角
  进行修正，无量纲。
- *N* 是发动机转速，单位为 rpm。

内部扭矩的摩擦扭矩偏移与任意凸轮相位角下的发动机负载及发动机转速的 3D 图

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。

### **Engine temperature modifier on friction torque, f\_fric\_temp\_mod** — 查找表 `[3.96 3.22 2.56 2.26 2.11 2 1.9 1.83 1.76 1.7 1.65 1.6 1.55 1.49 1.44 1.41 1.38 1.35 1.32 1.3 1.27 1.25 1.24 1.21 1.2 1.18 1.16 1.15 1.13 1.12 1.11 1.1 1.09 1.08 1.07 1.06 1.05 1.05 1.04 1.03 1.02 1.02 1.01 1.01 1 1 1 0.999 0.997 0.995 0.993 0.991 0.989 0.987]`（默认）| `vector` | `vector`

摩擦扭矩的发动机温度修正因子，
*ƒfric,temp*，无量纲。

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。

### **Engine temperature modifier breakpoints, f\_fric\_temp\_bpt** — 断点 `[274 276 278 280 282 284 286 288 290 292 294 296 298 300 302 304 306 308 310 312 314 316 318 320 322 324 326 328 330 332 334 336 338 340 342 344 346 348 350 352 354 356 358 360 362 364 366 368 370 372 374 376 378 380]`（默认）| `vector` | `vector`

发动机温度修正因子断点，单位为 K。

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。

### **Pumping torque table, f\_tq\_pump** — 查找表 `array`

泵气扭矩查找
表 *ƒTpump*，是发动机负载和发动机
转速的函数，
`Tpump=ƒTpump(L,N)`，其中：

- *Tpump* 是泵气扭矩，单位为 N·m。
- *L* 是发动机负载，作为归一化气缸空气质量，
  无量纲。
- *N* 是发动机转速，单位为 rpm。

泵气扭矩与发动机负载及发动机转速的 3D 图

#### 依赖

要启用此参数，请将 **Torque model** 参数设置为
`Torque Structure`。

### **Optimal spark table, f\_sa\_opt** — 查找表 `array`

最优点火查找表 fSAopt 是发动机转速和发动机负荷的函数，SAopt=fSAopt(L,N)，其中：

- *SAopt* 是在化学计量空燃比（AFR）下实现最大内部扭矩的最优点火提前角，单位为 deg。
- *L* 是在任意凸轮相位角下的发动机负荷，已针对最终稳态凸轮相位角进行修正，无量纲。
- *N* 是发动机转速，单位为 rpm。

化学计量空燃比（AFR）下实现最大内部扭矩的最优点火提前角随发动机负荷和发动机转速变化的三维图

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。

### **Inner torque load breakpoints, f\_tq\_inr\_l\_bpt** — 断点 `[0.2 0.28571 0.37143 0.45714 0.54286 0.62857 0.71429 0.8 0.88571 0.97143 1.0571 1.1429 1.2286 1.3143 1.4]`（默认）| `vector`

内部扭矩负荷断点，无量纲。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。

### **Inner torque speed breakpoints, f\_tq\_inr\_n\_bpt** — 断点 `[750 1053.5714 1357.1429 1660.7143 1964.2857 2267.8571 2571.4286 2875 3178.5714 3482.1429 3785.7143 4089.2857 4392.8571 4696.4286 5000]`（默认）| `vector`

内部扭矩转速断点，单位为 rpm。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。

### **Spark efficiency table, f\_m\_sa** — 查找表 `array`

点火效率查找表 fMsa 是相对于最优点的点火延迟的函数

Msa=fMsa(ΔSA)ΔSA=SAopt−SA

其中：

- Msa 是点火延迟效率乘数，无量纲。
- ΔSA 是相对于最优提前角的点火延迟正时距离，单位为 deg。

点火延迟效率随点火延迟正时距离变化的图

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。

### **Spark retard from optimal, f\_del\_sa\_bpt** — 断点 `[0 0.75 1.5 2.25 3 3.75 4.5 5.25 6 6.75 7.5 8.25 9 9.75 10.5 11.25 12 12.75 13.5 14.25 15 15.75 16.5 17.25 18 18.75 19.5 20.25 21 21.75 22.5 23.25 24 24.75 25.5 26.25 27 27.75 28.5 29.25 30 30.75 31.5 32.25 33 33.75 34.5 35.25 36 36.75 37.5 38.25 39 39.75 40.5 41.25 42 42.75 43.5 44.25 45 45.75 46.5 47.25 48]`（默认）| `vector`

相对于最优内部扭矩正时的点火延迟断点，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。

### **Lambda efficiency, f\_m\_lam** — 查找表 `array`

Lambda 效率查找表 fMλ 是 lambda 的函数，Mλ=fMλ(λ)，其中：

- Mλ 是用于考虑空燃比（AFR）影响的内扭矩 lambda 乘数，无量纲。
- λ 是 lambda，即 AFR 相对于化学计量燃料 AFR 的归一化值，无量纲。

Lambda 乘数随 lambda 变化的图

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。

### **Lambda breakpoints, f\_m\_lam\_bpt** — 断点 `[0.65 0.7 0.75 0.8 0.85 0.9 0.95 1 1.05 1.1]`（默认）| `vector`

Lambda 对内部扭矩影响的 lambda 断点，无量纲。

#### 依赖关系

要启用此参数，请将 **Torque model** 参数设置为 `Torque Structure`。

#### 排气

### **Exhaust temperature table, f\_t\_exh** — 查找表 `array`

排气温度查找表 fTexh 是发动机负荷和发动机转速的函数

Texh=fTexh(L,N)

其中：

- *Texh* 是发动机排气温度，单位为 K。
- *L* 是归一化气缸空气质量或发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

发动机排气温度随发动机转速和发动机负荷变化的三维图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **负荷断点，f\_t\_exh\_l\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

用于排气温度查找表的发动机负荷断点。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_l_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点，f\_t\_exh\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

用于排气温度查找表的发动机转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

使用驾驶员扭矩请求的火花点火发动机控制器

SI Controller 模块实现了一个火花点火（SI）控制器，该控制器使用驾驶员扭矩请求来计算满足驾驶员需求所需的开环空气、燃油和火花执行器指令。

您可以在发动机控制设计或性能、燃油经济性和排放权衡研究中使用 SI Controller 模块。核心发动机、节气门和涡轮增压器废气门子系统需要 SI Controller 模块输出的指令。

该模块使用指令扭矩和发动机转速来确定以下开环执行器指令：

- 节气门位置百分比
- 废气门面积百分比
- 喷油器脉冲宽度
- 点火提前角
- 进气凸轮相位器角度
- 排气凸轮相位器角度
- 废气再循环（EGR）阀面积百分比

SI Controller 模块有两个子系统：

- `Controller` 子系统 — 根据指令扭矩、测量的发动机转速和估计的气缸空气质量确定指令。
- `Estimator` 子系统 — 根据进气歧管气体压力、进气歧管气体温度、发动机转速和凸轮相位器位置确定估计的空气质量流量、扭矩和排气温度。

下图展示了信号流。

下图使用了以下变量。

|  |  |
| --- | --- |
| *N* | 发动机转速 |
| *MAP* | 循环平均进气歧管压力 |
| *IAT* | 进气温度 |
| *Tin,EGR* | EGR 阀入口处温度 |
| *MAT* | 循环平均进气歧管气体绝对温度 |
| φICP, φICPCMD | 分别为进气凸轮相位器角度和进气凸轮相位器角度指令 |
| φECP, φECPCMD | 分别为排气凸轮相位器角度和排气凸轮相位器角度指令 |
| *EGRap*, *EGRapcmd* | 分别为 EGR 阀面积百分比和 EGR 阀面积百分比指令 |
| *ΔPEGR* | EGR 阀入口和出口处的压力差 |
| *WAPcmd* | 涡轮增压器废气门面积百分比指令 |
| *SA* | 点火提前角 |
| Pwinj | 燃油喷油器脉冲宽度 |
| *TPPcmd* | 节气门位置百分比指令 |

Model-Based Calibration Toolbox™ 用于开发 Powertrain Blockset™ 中提供的表格。

### Controller

**Air**

该模块根据一个查找表确定指令发动机负载（即归一化气缸空气质量），该查找表是指令扭矩和测得发动机转速的函数。

Lcmd=fLcmd(Tcmd,N)

为达到指令负载，控制器使用前馈查找表设置节气门位置百分比和涡轮增压器废气门面积百分比。这些查找表是指令负载和测得发动机转速的函数。

TAPcmd=fTAPcmd(Lcmd,N)

TPPcmd=fTPPcmd(TAPcmd)

WAPcmd=fWAPcmd(Lcmd,N)

为确定凸轮相位器角度指令，该模块使用估计发动机负载和测得发动机转速的函数查找表。

φICPCMD=fICPCMD(Lest,N)

φECPCMD=fECPCMD(Lest,N)

该模块使用以下方程计算期望发动机负载。

Lest=CpsRairTstdm˙air,estPstdVdN

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Lest* | 估计发动机负载 |
| *Lcmd* | 指令发动机负载 |
| *N* | 发动机转速 |
| *Tcmd* | 指令发动机扭矩 |
| *TAPcmd* | 节气门面积百分比指令 |
| *TPPcmd* | 节气门位置百分比指令 |
| *WAPcmd* | 涡轮增压器废气门面积百分比指令 |
| Cps | 每动力冲程的曲轴转数 |
| Pstd | 标准压力 |
| Tstd | 标准温度 |
| Rair | 空气与燃烧气体混合物的理想气体常数 |
| Vd | 排量 |
| m˙air,est | 估计发动机空气质量流量 |

控制器子系统使用这些查找表进行空气计算。

- 节气门面积百分比指令查找表 fTAPcmd 是指令负载和发动机转速的函数

  TAPcmd=fTAPcmd(Lcmd,N)

  其中：

  - *TAPcmd* 是节气门面积百分比指令，单位为百分比。
  - *Lcmd*=*L* 是指令发动机负载，无量纲。
  - *N* 是发动机转速，单位为 rpm。

  节气门面积百分比指令相对于指令发动机负载和发动机转速的 3D 图
- 为考虑节气门位置到节气门面积的非线性，节气门位置百分比查找表对开环空气质量流量控制进行线性化。

  节气门位置百分比指令查找表 fTPPcmd 是节气门面积百分比指令的函数

  TPPcmd=fTPPcmd(TAPcmd)

  其中：

  - *TPPcmd* 是节气门位置百分比指令，单位为百分比。
  - *TAPcmd* 是节气门面积百分比指令，单位为百分比。

  节气门位置相对于节气门面积的图
- 废气门面积百分比指令查找表 fWAPcmd 是指令发动机负载和发动机转速的函数

  WAPcmd=fWAPcmd(Lcmd,N)

  其中：

  - *WAPcmd* 是废气门面积百分比指令，单位为百分比。
  - *Lcmd*=*L* 是指令发动机负载，无量纲。
  - *N* 是发动机转速，单位为 rpm。

  废气门面积百分比指令相对于指令发动机负载和发动机转速的 3D 图
- 指令发动机负载查找表 fLcmd 是指令扭矩和发动机转速的函数

  Lcmd=fLcmd(Tcmd,N)

  其中：

  - *Lcmd*=*L* 是指令发动机负载，无量纲。
  - *Tcmd* 是指令扭矩，单位为 N·m。
  - *N* 是发动机转速，单位为 rpm。

  指令发动机负载相对于指令扭矩和发动机转速的 3D 图
- 进气凸轮相位器角度指令查找表 fICPCMD 是发动机负载和发动机转速的函数

  φICPCMD=fICPCMD(Lest,N)

  其中：

  - φICPCMD 是指令进气凸轮相位器角度，单位为从驻车位置起的曲轴角度提前量。
  - *Lest*=*L* 是指令发动机负载，无量纲。
  - *N* 是发动机转速，单位为 rpm。

  指令进气凸轮相位器角度相对于指令发动机负载和发动机转速的 3D 图
- 排气凸轮相位器角度指令查找表 fECPCMD 是发动机负载和发动机转速的函数

  φECPCMD=fECPCMD(Lest,N)

  其中：

  - φECPCMD 是指令排气凸轮相位器角度，单位为从驻车位置起的曲轴角度延迟量。
  - *Lest*=*L* 是估计发动机负载，无量纲。
  - *N* 是发动机转速，单位为 rpm。

指令的排气凸轮相位器角度与估算发动机负荷和发动机转速的 3D 图

**EGR**

EGR 通常表示为总进气口流量的百分比。

EGRpct=100m˙EGRm˙EGR+m˙air

为了计算 EGR 面积百分比指令，该模块使用方程和查找表。

|  |  |
| --- | --- |
| 方程 | m˙EGRstd,cmd=m˙EGR,cmdPstdPin,EGRTin,EGRTstdm˙EGRstd,max=fEGRstd,max(Pout,EGRPin,EGR)m˙EGR,cmd=EGRpct,cmdm˙intk,est |
| 查找表 | EGR 面积百分比指令 *EGRapcmd* 查找表是归一化质量流量和压力比的函数  EGRapcmd=fEGRap,cmd(m˙EGRstd,cmdm˙EGRstd,max,Pout,EGRPin,EGR)  其中：  - *EGRapcmd* 是指令 EGR 面积百分比，无量纲。 - m˙EGRstd,cmdm˙EGRstd,max 是归一化质量流量，无量纲。 - Pout,EGRPin,EGR 是压力比，无量纲。    指令 EGR 百分比与归一化质量流量和压力比的 3D 图 |

方程和表格使用这些变量。

|  |  |
| --- | --- |
| *EGRap*、*EGRapcmd* | 分别为 EGR 阀面积百分比和 EGR 阀面积百分比指令 |
| *EGRpct,cmd* | EGR 百分比指令 |
| m˙EGRstd,cmd | 指令标准质量流量 |
| m˙EGRstd,max | 最大标准质量流量 |
| m˙EGR,cmd | 指令质量流量 |
| m˙intk,est | 估算进气口质量流量 |
| *Tstd*、*Pstd* | 标准温度和压力 |
| *Tin,EGR* | EGR 阀入口处温度 |
| *Pout,EGR*、*Pin,EGR* | 分别为 EGR 阀入口和出口处压力 |

**燃油**

空燃比（AFR）影响三元催化器（TWC）转化效率、扭矩产生和燃烧温度。发动机控制器通过根据期望的相对 AFR 指令喷油器脉冲宽度来管理 AFR。相对 AFR，λcmd，是指令 AFR 与燃料化学计量 AFR 之间的比值。

λcmd=AFRcmdAFRstoich

AFRcmd=m˙air,estm˙fuel,cmd

SI Controller 模块考虑了启动期间输送到 SI 发动机的额外燃油。如果发动机转速大于启动发动机起动转速，则 SI Controller 模块使用指数衰减的 delta lambda 来加浓最佳 AFR，lambda。为了初始化 delta lambda，该模块使用启动时的发动机冷却液温度。delta lambda 根据作为发动机冷却液温度函数的时间常数呈指数衰减至零。

您可以将该模块配置为开环和闭环 AFR 控制。

| 目的 | 使用 | **Controls** > **Fuel** > **Closed-loop feedback** 参数设置 |
| --- | --- | --- |
| - 评估控制器空气流量估算和燃油输送的动态和稳态精度。 | （默认）开环控制 | `off` |
| - 使平均 AFR 保持在接近化学计量 AFR，以维持较高的 TWC 转化效率。 | 闭环控制 | `on` |

**开环控制**

要为指令 AFR（lambda）创建输入端口，请在 **Controls** > **Fuel** > **Open-loop fuel** 窗格中，选择 **Input lambda**。

您可以在开环 AFR 控制期间手动调节催化器以获得最大效率，无论是否使用抖动。如果您希望在开环控制期间实现抖动，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格中，选择 **Dither**。

默认情况下，该模块配置为使用查找表来获取指令 AFR。

指令 lambda，λcmd，查找表是估算发动机负荷和测得发动机转速的函数

λcmd=fλcmd(Lest,N)

其中：

- λcmd 是指令相对 AFR，无量纲。
- *Lest*=*L* 是指令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

指令相对 AFR 与指令发动机负荷和发动机转速的 3D 图

该模块使用指令 lambda，λcmd、化学计量 AFR 和估算空气质量流量来计算估算燃油质量流量。

m˙fuel,cmd=m˙air,estAFRcmd=m˙air,estλcmdAFRstoich

该模块假设电池电压和燃油压力处于标称设置，此时不需要脉冲宽度校正。指令燃油喷射器脉冲宽度与每次喷射的燃油质量成正比。每次喷射的燃油质量根据指令燃油质量流量、发动机转速和气缸数计算。

Pwinj={m˙fuel,cmdCps(60smin)(1000mgg)(1000gkg)NSinjNcylwhen  Trqcmd>00when  Trqcmd≤0

**闭环控制**

当排气 AFR 接近化学计量 AFR 时，TWC 转换器效率最高，此时空气和燃油燃烧最完全。围绕该理想点，AFR 处于*催化剂窗口*内，在该窗口内，催化剂将一氧化碳、碳氢化合物和氮氧化物转化为无害排气产物的效率最高。经验研究表明，在优化的 AFR 频率、幅值和偏置下，使 AFR 围绕化学计量值振荡会拓宽 TWC 窗口，在存在不可避免扰动的情况下提高催化剂转化效率。

为降低量产硬件成本，AFR 控制系统包括廉价的开关型氧传感器，安装在发动机排气流中催化剂的上游和下游。氧传感器具有窄范围。本质上，它们在过稀（即，可用空气多于燃烧可用燃油所需的空气）和过浓（即，可用空气多于燃烧可用燃油所需的空气）之间切换。

该模块实现一种基于周期的方法，将平均 AFR 控制在催化剂窗口内的某个值，以实现最大转化效率。基于周期的 AFR 控制独立于从燃油喷射点到传感器测量点跨越发动机的传输延迟。有关该方法的更多信息，请参阅 Developing a Period-Based Air-Fuel Ratio Controller Using a Low-Cost Switching Sensor。

**点火**

点火提前角是在做功冲程上止点前（BTDC）发出火花时的曲轴转角。点火提前角会影响发动机效率、扭矩、排气温度、爆震和排放。

点火提前角查找表是估计负载和发动机转速的函数。

SA=fSA(Lest,N)

其中：

- *SA* 是点火提前角，单位为曲轴提前角。
- *Lest*=*L* 是指令发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

点火提前角与指令发动机负载和发动机转速的 3D 图

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Lest* | 估计发动机负载，基于归一化气缸空气质量 |
| *N* | 发动机转速 |
| fSA | 点火提前角查找表 |
| *N* | 点火提前角 |

**怠速**

当指令扭矩低于阈值时，怠速控制器调节发动机转速。

| 如果 | 怠速控制器 |
| --- | --- |
| *Trqcmd,input* < *Trqidlecmd,enable* | 启用 |
| *Trqidlecmd,enable* ≤ *Trqcmd,input* | 未启用 |

怠速控制器使用离散 PI 控制器，通过指令扭矩来调节目标怠速。

PI 控制器使用以下传递函数：

Cidle(z)=Kp,idle+Ki,idletsz−1

怠速指令扭矩必须小于最大指令扭矩：

0 ≤ *Trqidlecomd* ≤*Trqidlecmd,max*

怠速控制在这些条件下激活。如果指令输入扭矩降至启用怠速控制器的阈值以下（*Trqcmd,input* < *Trqidlecmd,enable*），则指令发动机扭矩由下式给出：

*Trqcmd* = max(*Trqcmd,input*,*Trqidlecmd*).

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Trqcmd* | 指令发动机扭矩 |
| *Trqcmd,input* | 输入指令发动机扭矩 |
| *Trqidlecmd,enable* | 启用怠速控制器的阈值 |
| *Trqidlecmd* | 怠速控制器指令扭矩 |
| *Trqidlecmd,max* | 最大指令扭矩 |
| *Nidle* | 基础怠速 |
| *Kp,idle* | 怠速控制器比例增益 |
| *Ki,idle* | 怠速控制器积分增益 |

**转速限制器**

为防止发动机超速，该模块实现了一个发动机转速限制控制器，将发动机转速限制在 **Controls** > **Idle Speed** 选项卡上 **Rev-limiter speed threshold** 参数指定的值。

如果发动机转速 *N* 超过发动机转速限值 *Nlim*，该模块将指令发动机扭矩设置为 0。

为了在发动机转速接近转速限值时将扭矩指令平滑过渡到 0，该模块实现了一个查找表乘数。该查找表将扭矩指令乘以一个从 0（发动机转速超过限值）到 1（发动机转速未超过限值）的值。

### Estimator

估计器子系统根据传感器反馈和标定参数确定估计的空气流量、扭矩、EGR 流量和排气温度。

|  |  |
| --- | --- |
| m˙air,est | 估计的发动机空气质量流量 |
| *Trqest* | 估计的发动机扭矩 |
| *Texh,est* | 估计的发动机排气温度 |
| m˙EGR,est | 估计的低压 EGR 质量流量 |

**空气质量流量**

要计算发动机空气质量流量，请将 SI 发动机配置为使用以下任一空气质量流量模型。

| 空气质量流量模型 | 描述 |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | 使用速度-密度方程计算发动机空气质量流量，将发动机空气质量流量与进气歧管压力和发动机转速相关联。考虑在固定气门机构设计的发动机中使用此空气质量流量模型。 |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | 为计算发动机空气质量流量，双独立凸轮相位器模型使用： - 根据发动机映射测量开发的经验标定参数 - 根据发动机计算机辅助设计 (CAD) 数据推导的桌面标定参数  与典型的基于空气质量流量 (MAF) 传感器直接测量空气质量流量的嵌入式空气质量流量计算相比，此空气质量流量模型提供： - 在双凸轮相位气门机构应用中消除 MAF 传感器 - 随海拔变化具有合理精度 - 半物理建模方法 - 有界行为 - 适合电子控制单元 (ECU) 实现的执行时间 - 系统化开发相对较少数量的标定参数 |

为确定估计的空气质量流量，该模块使用进气空气质量分数。进气口处的 EGR 质量分数滞后于 EGR 阀出口附近的质量分数。为对该滞后建模，该模块使用带时间常数的一阶系统。

yintk,EGR,est=m˙EGR,estm˙intk,esttszτEGRz+ts−τEGR

其余气体为空气。

yintk,air,est=1−yintk,EGR,est

这些方程使用以下变量。

|  |  |
| --- | --- |
| *yintk,EGR,est* | 估计的进气歧管 EGR 质量分数 |
| *yintk,air,est* | 估计的进气歧管空气质量分数 |
| m˙EGR,est | 估计的低压 EGR 质量流量 |
| m˙intk,est | 估计的进气口质量流量 |
| *τEGR* | EGR 时间常数 |

**扭矩**

要计算制动扭矩，请将 SI 发动机配置为使用以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| SI Engine Torque Structure Model | 对于结构化制动扭矩计算，SI 发动机使用内扭矩、摩擦扭矩、最佳点火、点火效率和 lambda 效率表。  如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，则可以： - 基于从模型或实验室测试记录的作为曲轴转角函数的缸内压力，在桌面仿真和 HIL 台架上仿真高级闭环发动机控制。 - 仿真由于高频曲轴扭转振动引起的发动机下游动力传动系统振动。 - 通过使用喷油器脉冲宽度输入，仿真由于稀薄运行或火花塞积污导致的发动机失火。 - 仿真气缸停用效果（进排气门关闭、不喷射燃油）对单个气缸压力、均值空气流量、均值扭矩和基于曲轴转角的扭矩的影响。 - 仿真断油效果对单个气缸压力、均值扭矩和基于曲轴转角的扭矩的影响。 |
| SI Engine Simple Torque Model | 对于简单制动扭矩计算，SI 发动机模块使用作为发动机转速和负载函数的扭矩查找表映射。 |

**EGR**

控制器使用由 F. Liu 和 J. Pfeiffer 开发的算法来估计低压质量流量、EGR 阀入口压力和 EGR 阀出口压力。该估计器需要测量的 EGR 阀压差、EGR 阀面积百分比、进气温度和 EGR 阀入口温度。

为了估计 EGR 阀指令，该模块使用：

- 方程

  m˙air,std=m˙air,estPstdPambIATTstdPin,EGR=Pout,EGR+ΔPEGRm˙EGR,est=m˙EGR,stdPin,EGRPstdTstdTin,EGR

- 表格

  - EGR 阀标准质量流量查找表是 EGR 阀面积百分比和压力比的函数

    m˙EGR,std=fEGR,std(EGRap,Pout,EGRPin,EGR)

    其中：

    - m˙EGR,std 是 EGR 阀标准质量流量，无量纲。
    - *EGRap* 是 EGR 阀流通面积百分比，单位为百分比。
    - Pout,EGRPin,EGR 是压力比，无量纲。

    标准质量流量与压力比和流通面积百分比的三维图

  - 压力比是标准质量流量的函数

    Pout,EGRPamb=fintksys,pr(m˙air,std)

    其中：

    - m˙air,std 是标准质量流量，单位为 g/s。
    - Pout,EGRPamb 是压力比，无量纲。

    压力比与质量流量的图

这些方程使用以下变量。

|  |  |
| --- | --- |
| *EGRap* | EGR 阀面积百分比指令 |
| *IAT* | 进气温度 |
| m˙air,std, m˙EGR,std | 分别为标准空气和 EGR 阀质量流量 |
| m˙air,est,m˙EGR,est | 分别为估计的空气和 EGR 阀质量流量 |
| *Tstd*, *Pstd* | 标准温度和压力 |
| *Tamb*, *Pamb* | 环境温度和压力 |
| *ΔPEGR* | EGR 阀入口和出口处的压差 |
| *Tin,EGR*, *Tout,EGR* | 分别为 EGR 阀入口和出口处的温度 |
| *Pin,EGR*, *Pout,EGR* | 分别为 EGR 阀入口和出口处的压力 |

**排气温度**

排气温度查找表 fTexh 是发动机负荷和发动机转速的函数

Texh=fTexh(L,N)

其中：

- *Texh* 是发动机排气温度，单位为 K。
- *L* 是归一化气缸空气质量或发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

发动机排气温度与发动机转速和发动机负荷的三维图
