---
type: simulink-block
title: 'SI Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Engines and Controllers'
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

测量的进气歧管绝对压力 MAP，单位为 Pa。

### **Mat** — 测量的进气歧管绝对温度 `scalar`

测量的进气歧管绝对温度，MAT，单位为 K。

### **IntkCamPhase** — 进气凸轮相位器角度 `scalar`

进气凸轮相位器角度，φICP，单位为 degCrkAdv，即从驻车位置起的曲轴提前角度。

### **ExhCamPhase** — 排气凸轮相位器角度 `scalar`

排气凸轮相位器角度，φECP，单位为 degCrkRet，即从驻车位置起的曲轴延迟角度。

### **Iat** — 进气温度 `scalar`

进气温度，*IAT*，单位为 K。

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

#### 依赖关系

要创建此端口，请在 **Fuel** 选项卡的
**Open-loop fuel** 窗格中，选择 **Input
lambda**。

### **IgSw** — 点火开关 `Boolean`

车辆点火开关状态，无量纲。

#### 依赖关系

要创建此端口，请在 **Stop-Start** 选项卡中，选择 **Enable Engine Stop-Start**。

### **ESSEnable** — 发动机起停使能 `Boolean`

用于使能或禁用起停逻辑的命令，无量纲。

#### 依赖关系

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
| `InjPw` | 燃油喷射器脉冲宽度 | Pwinj | ms |
| `SpkAdv` | 点火提前角 | SA | degBTDC |
| `IntkCamPhaseCmd` | 进气凸轮相位器角度指令 | φICPCMD | degCrkAdv |
| `ExhCamPhaseCmd` | 排气凸轮相位器角度指令 | φECPCMD | degCrkRet |
| `EgrVlvAreaPctCmd` | 排气凸轮相位器角度指令 | *EGRapcmd* | % |
| `FuelMassFlwCmd` | EGR 阀面积百分比指令 | m˙fuel,cmd | kg/s |
| `AfrCmd` | 指令空燃比 | *AFRcmd* | N/A |
| `EstEngTrq` | 估计发动机扭矩 | *Trqest* | N·m |
| `EstNrmlzdAirCharg` | 估计的归一化气缸空气质量 | N/A | N/A |
| `EstIntkPortMassFlw` | 估计的进气道空气质量流量 | m˙intk,est | kg/s |
| `EstIntkAirMassFlw` | 估计的空气质量流量 | m˙air,est | kg/s |
| `EstEgrMassFlw` | 估计的低压 EGR 质量流量 | m˙EGR,est | kg/s |
| `EstExhManGasTemp` | 估计的排气歧管气体温度 | *Texh,est* | K |
| `EngRevLimAct` | 指示转速限制器控制是否激活的标志 | N/A | N/A |
| `ClsdLpFuelMult` | 用于闭环 AFR 控制的燃油喷射器脉冲宽度乘数 | *Pwinj\_mult* | N/A |

### **ThrPosPctCmd** — 节气门面积百分比指令 `scalar`

节气门面积百分比指令，*TAPcmd*。

### **WgAreaPctCmd** — 废气门面积百分比指令 `scalar`

废气门面积百分比指令，*WAPcmd*。

### **InjPw** — 燃油喷射器脉冲宽度 `scalar`

燃油喷射器脉冲宽度，Pwinj，
单位为 ms。

### **SpkAdv** — 点火提前角 `scalar`

点火提前角，SA，单位为
上止点前曲轴转角（degBTDC）。

### **IntkCamPhaseCmd** — 进气凸轮相位器角度指令 `scalar`

进气凸轮相位器角度指令，φICPCMD。

### **ExhCamPhaseCmd** — 排气凸轮相位器角度指令 `scalar`

排气凸轮相位器角度指令，φECPCMD。

### **EgrVlvAreaPctCmd** — EGR 阀面积百分比指令 `scalar`

EGR 阀面积百分比指令，
*EGRapcmd*，单位为 %。

## 参数

### 配置

### **Air mass flow estimation model** — 选择空气质量流量估计模型 `Dual Variable Cam Phasing`（默认）| `Simple Speed-Density`

要计算发动机空气质量流量，请将 SI 发动机配置为
使用以下任一空气质量流量模型。

| 空气质量流量模型 | 描述 |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | 使用速度-密度方程计算发动机空气质量流量，将发动机空气质量流量与进气歧管压力和发动机转速相关联。对于固定气门机构设计的发动机，可考虑使用此空气质量流量模型。 |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | 为计算发动机空气质量流量，双独立凸轮相位器模型使用：  - 根据发动机  映射测量开发的经验标定参数 - 根据发动机  计算机辅助设计 (CAD) 数据推导的桌面标定参数  与基于使用空气质量流量 (MAF) 传感器直接测量空气质量流量的典型嵌入式空气质量流量计算相比，此空气质量流量模型具有以下优势：  - 在双凸轮相位可变气门机构  应用中无需 MAF 传感器 - 随海拔变化具有合理精度 - 半物理建模方法 - 有界行为 - 适合电子控制单元 (ECU)  实现的执行时间 - 相对较少数量的标定参数的系统化开发 |

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `AirEstOptionPopup` |
| **Values:** | `Dual Variable Cam Phasing`（默认）| `Simple Speed-Density` |
| **Data Types:** | `character vector` |

#### 依赖关系

下表总结了参数依赖关系。

| 空气质量流量估计模型 | 启用 **Estimation** > **Air** 选项卡上的参数 |
| --- | --- |
| `Dual Variable Cam Phasing` | **Cylinder volume at intake valve close table, f\_vivc**  **Cylinder volume intake cam phase breakpoints, f\_vivc\_icp\_bpt**  **Cylinder trapped mass correction factor, f\_tm\_corr**  **Normalized density breakpoints, f\_tm\_corr\_nd\_bpt**  **Engine speed breakpoints, f\_tm\_corr\_n\_bpt**  **Air mass flow, f\_mdot\_air**  **Exhaust cam phase breakpoints, f\_mdot\_air\_ecp\_bpt**  **Trapped mass flow breakpoints, f\_mdot\_trpd\_bpt**  **Air mass flow correction factor, f\_mdot\_air\_corr**  **Engine load breakpoints for air mass flow correction, f\_mdot\_air\_corr\_ld\_bpt**  **Engine speed breakpoints for air mass flow correction, f\_mdot\_air\_corr\_n\_bpt** |
| `Simple Speed-Density` | **Speed-density volumetric efficiency, f\_nv**  **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt**  **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** |

### **Torque estimation model** — 选择扭矩估计模型 `Torque Structure`（默认）| `Simple Torque Lookup`

要计算制动扭矩，请将 SI 发动机配置为使用
以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| SI Engine Torque Structure Model | 对于结构化制动扭矩计算，SI 发动机使用内扭矩、摩擦扭矩、最佳点火、点火效率和 lambda 效率表。  如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，则可以：  - 基于从模型或实验室测试记录的作为  曲轴转角函数的气缸压力，在桌面  仿真和 HIL 台架上仿真高级闭环发动机控制。 - 仿真由于高频曲轴扭转而在发动机下游产生的  传动系振动。 - 通过使用喷射器脉冲宽度输入，仿真由于稀薄运行或火花塞  积垢导致的发动机失火。 - 仿真气缸停用效果（进气门和  排气门关闭、无喷射燃油）对单个气缸压力、均值气流、均值扭矩和  基于曲轴转角的扭矩的影响。 - 仿真断油效果对单个气缸压力、均值扭矩和  基于曲轴转角的扭矩的影响。 |
| SI Engine Simple Torque Model | 对于简单制动扭矩计算，SI 发动机模块使用作为发动机转速和负荷函数的扭矩查找表映射。 |

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TrqEstOptionPopup` |
| **Values:** | `Torque Structure`（默认）| `Simple Torque Lookup` |
| **Data Types:** | `character vector` |

#### 依赖关系

下表总结了参数依赖关系。

| 扭矩估计模型 | 启用 **Estimation** > **Torque** 选项卡上的参数 |
| --- | --- |
| `Torque Structure` | **Inner torque table, f\_tq\_inr**  **Friction torque table, f\_tq\_fric**  **Engine temperature modifier on friction torque, f\_fric\_temp\_mod**  **Engine temperature modifier breakpoints, f\_fric\_temp\_bpt**  **Pumping torque table, f\_tq\_pump**  **Optimal spark table, f\_sa\_opt**  **Inner torque load breakpoints, f\_tq\_inr\_l\_bpt**  **Inner torque speed breakpoints, f\_tq\_inr\_n\_bpt**  **Spark efficiency table, f\_m\_sa**  **Spark retard from optimal, f\_del\_sa\_bpt**  **Lambda efficiency, f\_m\_lam**  **Lambda breakpoints, f\_m\_lam\_bpt** |
| `Simple Torque Lookup` | **Torque table, f\_tq\_nl**  **Torque table load breakpoints, f\_tq\_nl\_l\_bpt**  **Torque table speed breakpoints, f\_tq\_nl\_n\_bpt** |

### 控制

#### 空气

### **Engine commanded load table, f\_lcmd** — 查找表 `array`

指令发动机负荷查找表，fLcmd，
是命令扭矩和发动机转速的函数

Lcmd=fLcmd(Tcmd,N)

其中：

- *Lcmd*=*L* 是
  指令发动机负荷，无量纲。
- *Tcmd* 是
  命令扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

指令发动机负荷对命令扭矩和发动机转速的 3D 图

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_lcmd` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Torque command breakpoints, f\_lcmd\_tq\_bpt** — 断点 `[15 26.43 37.86 49.29 60.71 72.14 83.57 95 106.4 117.9 129.3 140.7 152.1 163.6 175]`（默认）| `vector`

扭矩命令断点，单位为 N·m。

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_lcmd_tq_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Speed breakpoints, f\_lcmd\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

转速断点，单位为 rpm。

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_lcmd_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Throttle area percent, f\_tap** — 查找表，% `array`

节气门面积百分比指令查找
表，fTAPcmd，
是命令负荷和发动机转速的函数

TAPcmd=fTAPcmd(Lcmd,N)

其中：

- *TAPcmd* 是
  节气门面积百分比指令，单位为百分比。
- *Lcmd*=*L* 是
  指令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

节气门面积百分比指令对指令发动机负荷和发动机转速的 3D 图

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tap` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **Throttle area percent load breakpoints, f\_tap\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

节气门面积百分比负荷断点，无量纲。

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tap_ld_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Throttle area percent speed breakpoints, f\_tap\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认）| `vector`

节气门面积百分比转速断点，单位为 rpm。

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tap_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

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

节气门位置对节气门面积的图

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tpp` |
| **Values:** | `[0 100]`（默认）| `vector` |
| **Data Types:** | `double` |

### **Throttle area percent to position percent area breakpoints, f\_tpp\_tap\_bpt** — 断点 `[0 100]`（默认）| `vector`

节气门面积百分比到位置百分比面积断点，
无量纲。

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tpp_tap_bpt` |
| **Values:** | `[0 100]`（默认）| `vector` |
| **Data Types:** | `double` |

### **Wastegate area percent, f\_wap** — 查找表，% `array`

废气门面积百分比指令查找
表，fWAPcmd，
是指令发动机负荷和发动机转速的函数

WAPcmd=fWAPcmd(Lcmd,N)

其中：

- *WAPcmd* 是
  废气门面积百分比指令，单位为百分比。
- *Lcmd*=*L* 是
  指令发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

废气门面积百分比指令对指令发动机负荷和发动机转速的 3D 图

#### Programmatic Use

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_wap` |
| **Values:** | `array` |
| **Data Types:** | `double` |

### **负载断点, f\_wap\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector`

负载断点，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_wap_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点, f\_wap\_n\_bpt** — 断点, rpm `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认） | `vector`

转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_wap_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **进气凸轮相位器角度, f\_icp** — 查找表 `array`

进气凸轮相位器角度命令查找表，fICPCMD，是发动机负载和发动机转速的函数

φICPCMD=fICPCMD(Lest,N)

其中：

- φICPCMD 是命令进气凸轮相位器角度，以从 park 起的曲轴转角提前量（crank degrees）表示。
- *Lest*=*L* 是命令发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

命令进气凸轮相位器角度相对于命令发动机负载和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_icp` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **排气凸轮相位器角度, f\_ecp** — 查找表 `array`

排气凸轮相位器角度命令查找表，fECPCMD，是发动机负载和发动机转速的函数

φECPCMD=fECPCMD(Lest,N)

其中：

- φECPCMD 是命令排气凸轮相位器角度，以从 park 起的曲轴转角延迟量（crank degrees）表示。
- *Lest*=*L* 是估计发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

命令排气凸轮相位器角度相对于估计发动机负载和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_ecp` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **负载断点, f\_cp\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector`

负载断点，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_cp_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点, f\_cp\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认） | `vector`

转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_cp_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **命令 EGR 百分比, f\_egrpct\_cmd** — 查找表 `array`

EGR 百分比命令，*EGRpct,cmd*，查找表是估计发动机负载和发动机转速的函数

EGRpct,cmd=fEGRpct,cmd(Lest,N)

其中：

- *EGRpct,cmd* 是命令 EGR 百分比，无量纲。
- *Lest*=*L* 是估计发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

命令 EGR 百分比相对于估计发动机负载和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egrpct_cmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **负载断点, f\_egrpct\_ld\_bpt** — 断点 `[0 0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector`

发动机负载断点，*L*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egrpct_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点, f\_egrpct\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认） | `vector`

发动机转速断点，*N*，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egrpct_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR 阀面积百分比, f\_egr\_areapct\_cmd** — 查找表 `array`

EGR 面积百分比命令，*EGRapcmd*，查找表是归一化质量流量和压力比的函数

EGRapcmd=fEGRap,cmd(m˙EGRstd,cmdm˙EGRstd,max,Pout,EGRPin,EGR)

其中：

- *EGRapcmd* 是命令 EGR 面积百分比，无量纲。
- m˙EGRstd,cmdm˙EGRstd,max 是归一化质量流量，无量纲。
- Pout,EGRPin,EGR 是压力比，无量纲。

命令 EGR 百分比相对于归一化质量流量和压力比的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_areapct_cmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **EGR 阀打开标准流量, f\_egr\_max\_stdflow** — 断点 `[74.87 74.87 74.74 74.39 73.81 72.98 71.91 70.58 68.97 67.06 64.84 62.25 59.27 55.81 51.79 47.07 36.33 24.22 12.11 0]`（默认） | `vector`

最大标准 EGR 阀质量流量断点，m˙EGRstd,max，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_max_stdflow` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **归一化 EGR 阀标准流量断点, f\_egr\_areapct\_nrmlzdflow\_bpt** — 断点 `[0 0.03448 0.06897 0.1034 0.1379 0.1724 0.2069 0.2414 0.2759 0.3103 0.3448 0.3793 0.4138 0.4483 0.4828 0.5172 0.5517 0.5862 0.6207 0.6552 0.6897 0.7241 0.7586 0.7931 0.8276 0.8621 0.8966 0.931 0.9655 1]`（默认） | `vector`

归一化质量流量断点，m˙EGRstd,cmdm˙EGRstd,max，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_areapct_nrmlzdflow_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR 阀压力比断点, f\_egr\_areapct\_pr\_bpt** — 断点 `vector`

压力比断点，Pout,EGRPin,EGR，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_areapct_pr_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 燃料

### **喷油器斜率, Sinj** — 斜率 `6.452`（默认） | `scalar`

燃油喷油器斜率，Sinj，单位为 mg/ms。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sinj` |
| **值：** | `6.452`（默认） | `scalar` |
| **数据类型：** | `double` |

### **化学计量空燃比, afr\_stoich** — 比率 `14.6`（默认） | `scalar`

化学计量空燃比，*AFRstoich*。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `afr_stoich` |
| **值：** | `14.6`（默认） | `scalar` |
| **数据类型：** | `double` |

### **相对空燃比 lambda, f\_lamcmd** — 空燃比 (AFR) 查找表 `array`

命令 lambda，λcmd，查找表是估计发动机负载和测量发动机转速的函数

λcmd=fλcmd(Lest,N)

其中：

- λcmd 是命令相对 AFR，无量纲。
- *Lest*=*L* 是命令发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

命令相对 AFR 相对于命令发动机负载和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_lamcmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **燃料** 选项卡上的 **开环燃油** 窗格中，清除 **输入 lambda**。

### **负载断点, f\_lamcmd\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector`

负载断点，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_lamcmd_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **燃料** 选项卡上的 **开环燃油** 窗格中，清除 **输入 lambda**。

### **转速断点, f\_lamcmd\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]`（默认） | `vector`

转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_lamcmd_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **燃料** 选项卡上的 **开环燃油** 窗格中，清除 **输入 lambda**。

### **发动机启动 lambda 加浓增量与冷却液温度的关系, f\_startup\_lambda\_delta** — 查找表 `[0.5 0.3 0.2 0]`（默认） | `vector`

发动机启动 lambda 加浓增量作为冷却液温度的函数，无量纲。

SI Controller 模块使用此参数来考虑在启动期间输送到火花点火 (SI) 发动机的额外燃料。如果发动机转速大于 **发动机起动转速** 参数，则 SI Controller 模块使用按指数衰减的 delta lambda 对最佳相对空燃比 (lambda) 进行加浓。为了初始化 delta lambda，模块使用 **发动机启动 lambda 加浓增量与冷却液温度的关系** 参数创建 lambda 加浓表，该表是发动机冷却液温度的函数。delta lambda 根据 **发动机启动 lambda 加浓增量时间常数与冷却液温度的关系** 参数指定的时间常数按指数衰减到零。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_startup_lambda_delta` |
| **值：** | `[0.5 0.3 0.2 0]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **燃料** 选项卡上的 **开环燃油** 窗格中，清除 **输入 lambda**。

### **发动机启动 lambda 加浓增量时间常数与冷却液温度的关系, f\_startup\_lambda\_delta\_timecnst** — Lambda 时间常数 `[90 40 12 0]`（默认） | `vector`

发动机启动 lambda 加浓增量时间常数与冷却液温度的关系，单位为 s。

SI Controller 模块使用此参数来考虑在启动期间输送到火花点火 (SI) 发动机的额外燃料。如果发动机转速大于 **发动机起动转速** 参数，则 SI Controller 模块使用按指数衰减的 delta lambda 对最佳相对空燃比 (lambda) 进行加浓。为了初始化 delta lambda，模块使用 **发动机启动 lambda 加浓增量与冷却液温度的关系** 参数创建 lambda 加浓表，该表是发动机冷却液温度的函数。delta lambda 根据 **发动机启动 lambda 加浓增量时间常数与冷却液温度的关系** 参数指定的时间常数按指数衰减到零。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_startup_lambda_delta_timecnst` |
| **值：** | `[90 40 12 0]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **燃料** 选项卡上的 **开环燃油** 窗格中，清除 **输入 lambda**。

### **发动机启动冷却液温度断点, f\_startup\_ect\_bpt** — 断点 `[-40 0 20 50]`（默认） | `vector`

发动机启动冷却液温度断点，单位为 C。

SI Controller 模块使用此参数来考虑在启动期间输送到火花点火 (SI) 发动机的额外燃料。如果发动机转速大于 **发动机起动转速** 参数，则 SI Controller 模块使用按指数衰减的 delta lambda 对最佳相对空燃比 (lambda) 进行加浓。为了初始化 delta lambda，模块使用 **发动机启动 lambda 加浓增量与冷却液温度的关系** 参数创建 lambda 加浓表，该表是发动机冷却液温度的函数。delta lambda 根据 **发动机启动 lambda 加浓增量时间常数与冷却液温度的关系** 参数指定的时间常数按指数衰减到零。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_startup_ect_bpt` |
| **值：** | `[-40 0 20 50]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **燃料** 选项卡上的 **开环燃油** 窗格中，清除 **输入 lambda**。

### **闭环反馈** — 最小化命令 AFR 误差 `off`（默认） | `on`

选择选项以最小化命令空燃比 (lambda)，*λcmd* 误差。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelEn` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character array` |

### **抖动** — 对催化转化效率建模 `off`（默认） | `on`

配置模块以对抖动建模。对于开环分析，选择此选项以调整获得最大催化转化效率。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OpenLpDitherEn` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character array` |

#### 依赖项

默认情况下，选择 **闭环反馈** 会将模块配置为对抖动建模。

要为开环空燃比（lambda）命令启用此参数，请清除 **闭环反馈**。

选择此参数将启用以下参数：

- **Lambda 抖动幅度，
  LambdaDitherAmp**
- **Lambda 抖动频率，
  LambdaDitherFrq**

### **闭环燃油比例增益，ClsdLpFuelPGain** — 比例增益 `0.005`（默认） | `scalar`

闭环燃油比例增益，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelPGain` |
| **值：** | `0.005`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

### **闭环燃油积分增益，ClsdLpFuelIGain** — 积分增益 `0.05`（默认） | `scalar`

闭环燃油积分增益，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelIGain` |
| **值：** | `0.05`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

### **闭环燃油积分器限制，ClsdLpFuelIntgLmt** — 积分器限制 `0.2`（默认） | `scalar`

闭环燃油积分器限制，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClsdLpFuelIntgLmt` |
| **值：** | `0.2`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

### **Lambda 抖动幅度，LambdaDitherAmp** — 幅度 `0.03`（默认） | `scalar`

Lambda 抖动幅度，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LambdaDitherAmp` |
| **值：** | `0.03`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈** 或 **抖动**。

### **Lambda 抖动频率，LambdaDitherFrq** — 频率 `0.75`（默认） | `scalar`

Lambda 抖动频率，单位为 Hz。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LambdaDitherFrq` |
| **值：** | `0.75`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈** 或 **抖动**。

### **氧传感器化学计量复位电压，O2ResetStoichVoltSen** — 闭环 AFR 控制 `2500`（默认） | `scalar`

氧传感器化学计量复位电压，O2ResetStoichVoltSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2ResetStoichVoltSen` |
| **值：** | `2500`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

### **氧传感器最小电压复位，O2ResetMinVoltSen** — 闭环 AFR 控制 `0`（默认） | `scalar`

氧传感器最小电压复位，O2ResetMinVoltSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2ResetMinVoltSen` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

### **氧传感器最大电压复位，O2ResetMaxVoltSen** — 闭环 AFR 控制 `5000`（默认） | `scalar`

氧传感器最大电压复位，O2ResetMaxVoltSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2ResetMaxVoltSen` |
| **值：** | `5000`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

### **氧传感器电压学习更新周期，O2LearnUpdatePerSen** — 闭环 AFR 控制 `4`（默认） | `scalar`

氧传感器电压学习更新周期，O2LearnUpdatePerSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2LearnUpdatePerSen` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

### **氧传感器电压幅度最小值，O2AmpMinVoltSen** — 闭环 AFR 控制 `250`（默认） | `scalar`

氧传感器电压幅度最小值，O2AmpMinVoltSen，单位为 mV。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `O2AmpMinVoltSen` |
| **值：** | `250`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

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

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

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

#### 依赖项

要启用此参数，请在 **燃油** 选项卡的 **闭环燃油** 窗格上，选择 **闭环反馈**。

#### 点火

### **点火提前表，f\_sa** — 查找表 `array`

点火提前查找表是估计负载和发动机转速的函数。

SA=fSA(Lest,N)

其中：

- *SA* 是点火提前角，单位为曲轴提前角。
- *Lest*=*L* 是指令发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

点火提前角与指令发动机负载和发动机转速的三维图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_sa` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **负载断点，f\_sa\_ld\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector`

负载断点，无量纲。

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

#### 怠速转速

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

### **启用扭矩命令限制，Trq\_idlecmd\_enable** — 扭矩 `1`（默认） | `scalar`

用于启用怠速转速控制器的扭矩，*Trqidlecmd,enable*，单位为 N·m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_idlecmd_enable` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **最大扭矩命令，Trq\_idlecmd\_max** — 扭矩 `50`（默认） | `scalar`

最大怠速控制器指令扭矩，*Trqidlecmd,max*，单位为 N·m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_idlecmd_max` |
| **值：** | `50`（默认） | `scalar` |
| **数据类型：** | `double` |

### **比例增益，Kp\_idle** — PI 控制器 `0.05`（默认） | `scalar`

用于怠速转速控制的比例增益，*Kp,idle*，单位为 N·m/rpm。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_idle` |
| **值：** | `0.05`（默认） | `scalar` |
| **数据类型：** | `double` |

### **积分增益，Ki\_idle** — PI 控制器 `0.2`（默认） | `scalar`

用于怠速转速控制的积分增益，*Ki,idle*，单位为 N·m/(rpm·s)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki_idle` |
| **值：** | `0.2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **转速限制器阈值，EngRevLim** — 发动机转速限制 `6000`（默认） | `scalar`

发动机转速限制，*Nlim*，单位为 rpm。

如果发动机转速 *N* 超过发动机转速限制 *Nlim*，该模块将指令发动机扭矩设置为 0。

为了在发动机转速接近转速限制时将扭矩命令平滑过渡到 0，该模块实现了一个查找表乘数。该查找表将扭矩命令乘以一个值，该值的范围为 0（发动机转速超过限制）到 1（发动机转速未超过限制）。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngRevLim` |
| **值：** | `6000`（默认） | `scalar` |
| **数据类型：** | `double` |

### **发动机起动转速，CrankSpeed** — 发动机转速 `150`（默认） | `scalar`

发动机起动转速，单位为 rpm。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CrankSpeed` |
| **值：** | `150`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 停止-启动

### **启用 Engine Stop-Start** — 选择以启用发动机停止-启动逻辑 `off`（默认） | `on`

选择以启用发动机停止-启动逻辑。选择此选项将激活其他参数，以修改 Engine Stop-Start 模块的行为。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ESSEnable` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **外部使能端口** — 创建输入端口 `off`（默认） | `on`

选择此选项可向发动机控制器模块添加一个端口，用于启用或禁用停止-启动逻辑。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ESSExternalPortEnable` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

#### 依赖项

要启用此参数，请在 **停止-启动** 选项卡上，选择 **启用 Engine Stop-Start**。

### **发动机停止时间，EngStopTime** — 发动机停止时间 `5`（默认） | `scalar`

停止-启动逻辑的发动机停止时间，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngStopTime` |
| **值：** | `5`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **停止-启动** 选项卡上，选择 **启用 Engine Stop-Start**。

### **催化器起燃时间，CatLightOffTime** — 催化器起燃时间 `0`（默认） | `scalar`

停止-启动逻辑的催化器起燃时间，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CatLightOffTime` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **停止-启动** 选项卡上，选择 **启用 Engine Stop-Start**。

### **采样时间, Ts** — 采样时间 `0.01` (默认) | `scalar`

起停逻辑的采样时间，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ts` |
| **值：** | `0.01` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请在 **起停** 选项卡上选择 **启用发动机起停**。

### 估计

#### 空气

### **气缸数, NCyl** — 发动机气缸 `4` (默认) | `scalar`

发动机气缸数，Ncyl。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4` (默认) | `scalar` |
| **数据类型：** | `double` |

### **每动力冲程曲轴转数, Cps** — 每冲程转数 `2` (默认) | `scalar`

每动力冲程的曲轴转数，Cps，单位为 rev/stroke。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2` (默认) | `scalar` |
| **数据类型：** | `double` |

### **总排量, Vd** — 体积 `0.0015` (默认) | `scalar`

排量，Vd，单位为 m^3。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015` (默认) | `scalar` |
| **数据类型：** | `double` |

### **空气理想气体常数, Rair** — 常数 `287` (默认) | `scalar`

理想气体常数，Rair，单位为 J/(kg·K)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rair` |
| **值：** | `287` (默认) | `scalar` |
| **数据类型：** | `double` |

### **空气标准压力, Pstd** — 压力 `101325` (默认) | `scalar`

标准空气压力，Pstd，单位为 Pa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `101325` (默认) | `scalar` |
| **数据类型：** | `double` |

### **空气标准温度, Tstd** — 温度 `293.15` (默认) | `scalar`

标准空气温度，Tstd，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tstd` |
| **值：** | `293.15` (默认) | `scalar` |
| **数据类型：** | `double` |

### **速度-密度容积效率, f\_nv** — 查找表 `array`

发动机容积效率查找表 fηv 是进气歧管绝对压力和发动机转速的函数

ηv=fηv(MAP,N)

其中：

- ηv 是发动机容积效率，无量纲。
- *MAP* 是进气歧管绝对压力，单位为 KPa。
- *N* 是发动机转速，单位为 rpm。

发动机容积效率与进气歧管绝对压力和发动机转速的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Simple Speed-Density`。

### **速度-密度进气歧管压力断点, f\_nv\_prs\_bpt** — 断点 `[31 40.64 50.29 59.93 69.57 79.21 88.86 98.5 108.1 117.8 127.4 137.1 146.7 156.4 166]` (默认) | `vector`

速度-密度容积效率查找表的进气歧管压力断点，单位为 KPa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_prs_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Simple Speed-Density`。

### **速度-密度发动机转速断点, f\_nv\_n\_bpt** — 断点 `[750 1054 1357 1661 1964 2268 2571 2875 3179 3482 3786 4089 4393 4696 5000]` (默认) | `vector`

速度-密度容积效率查找表的发动机转速断点，单位为 rpm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Simple Speed-Density`。

### **进气门关闭时气缸容积表, f\_vivc** — 2-D 查找表 `array`

进气门关闭（IVC）时气缸容积表 fVivc 是进气凸轮相位器角度的函数

VIVC=fVivc(φICP)

其中：

- VIVC 是 IVC 时的气缸容积，单位为 L。
- φICP 是进气凸轮相位器角度，以相对进气相位器驻留位置的曲轴提前角度表示。

气缸容积与进气凸轮相位器角度的图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_vivc` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **发动机转速断点, f\_tm\_corr\_n\_bpt** — 断点 `[750 973.7 1197 1421 1645 1868 2092 2316 2539 2763 2987 3211 3434 3658 3882 4105 4329 4553 4776 5000]` (默认) | `vector`

发动机转速断点，单位为 rpm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **气缸容积进气凸轮相位断点, f\_vivc\_icp\_bpt** — 断点 `[0 2.632 5.263 7.895 10.53 13.16 15.79 18.42 21.05 23.68 26.32 28.95 31.58 34.21 36.84 39.47 42.11 44.74 47.37 50]` (默认) | `vector`

进气门关闭时气缸容积表断点。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_vivc_icp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **气缸截留质量修正系数, f\_tm\_corr** — 查找表 `array`

截留质量修正系数表 fTMcorr 是归一化密度和发动机转速的函数

TMcorr=fTMcorr(ρnorm, N)

其中：

- TMcorr 是截留质量修正乘数，无量纲。
- ρnorm 是归一化密度，无量纲。
- *N* 是发动机转速，单位为 rpm。

截留质量修正乘数与归一化密度和发动机转速的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **归一化密度断点, f\_tm\_corr\_nd\_bpt** — 断点 `[0.3 0.3895 0.4789 0.5684 0.6579 0.7474 0.8368 0.9263 1.016 1.105 1.195 1.284 1.374 1.463 1.553 1.642 1.732 1.821 1.911 2]` (默认) | `vector`

归一化密度断点。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr_nd_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **进气质量流量, f\_mdot\_intk** — 查找表 `array`

相位器进气质量流量模型查找表是排气凸轮相位器角度和截留空气质量流量的函数

m˙intkideal=fintkideal(φECP,TMflow)

其中：

- m˙intkideal 是任意凸轮相位器角度下的发动机进气道质量流量，单位为 g/s。
- φECP 是排气凸轮相位器角度，以相对排气相位器驻留位置的曲轴延迟角度表示。
- TMflow 是在当前发动机转速下等效于修正截留质量的流量，单位为 g/s。

空气质量流量与排气凸轮相位器角度和流量等效值的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_intk` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **排气凸轮相位断点, f\_mdot\_air\_ecp\_bpt** — 断点 `[0 2.632 5.263 7.895 10.53 13.16 15.79 18.42 21.05 23.68 26.32 28.95 31.58 34.21 36.84 39.47 42.11 44.74 47.37 50]` (默认) | `vector`

空气质量流量查找表的排气凸轮相位器断点。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_ecp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **截留质量流量断点, f\_mdot\_trpd\_bpt** — 断点 `[0 5.79 11.58 17.37 23.16 28.95 34.74 40.53 46.32 52.11 57.89 63.68 69.47 75.26 81.05 86.84 92.63 98.42 104.2 110]` (默认) | `vector`

空气质量流量查找表的截留质量流量断点。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_trpd_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **空气质量流量修正系数, f\_mdot\_air\_corr** — 查找表 `array`

进气空气质量流量修正查找表 faircorr 是理想负荷和发动机转速的函数

m˙air=m˙intkidealfaircorr(Lideal,N)

其中：

- Lideal 是任意凸轮相位器角度下的发动机负荷（归一化气缸空气质量），未针对最终稳态凸轮相位器角度修正，无量纲。
- *N* 是发动机转速，单位为 rpm。
- m˙air 是稳态凸轮相位器角度下的发动机进气空气质量流量最终修正，单位为 g/s。
- m˙intkideal 是任意凸轮相位器角度下的发动机进气道质量流量，单位为 g/s。

发动机进气空气质量流量最终修正与发动机负荷和发动机转速的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_corr` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **用于空气质量流量修正的发动机负荷断点, f\_mdot\_air\_corr\_ld\_bpt** — 断点 `vector`

用于空气质量流量最终修正的发动机负荷断点。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_corr_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **用于空气质量流量修正的发动机转速断点, f\_mdot\_air\_n\_bpt** — 断点 `[750 973.7 1197 1421 1645 1868 2092 2316 2539 2763 2987 3211 3434 3658 3882 4105 4329 4553 4776 5000]` (默认) | `vector`

用于空气质量流量最终修正的发动机转速断点。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **空气流量估计模型** 参数选择 `Dual Variable Cam Phasing`。

### **EGR 流量时间常数, tau\_egr** — 常数 `0.2` (默认) | `scalar`

EGR 流量时间常数，*τEGR*，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_egr` |
| **值：** | `0.2` (默认) | `scalar` |
| **数据类型：** | `double` |

### **进气系统压力比表, f\_intksys\_stdflow\_pr** — 表 `array`

压力比是标准质量流量的函数

Pout,EGRPamb=fintksys,pr(m˙air,std)

其中：

- m˙air,std 是标准质量流量，单位为 g/s。
- Pout,EGRPamb 是压力比，无量纲。

压力比与质量流量的图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_intksys_stdflow_pr` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **进气压力比的标准质量流量断点, f\_intksys\_stdflow\_bpt** — 断点 `[0 29.67 59.34 89.01 117.8 144.1 155.7 166 175.2 183.3 190.7 197 202.7 207.7 212.2 216.1 219.4 222.2 224.5 226.4]` (默认) | `vector`

标准质量流量，m˙air,std，单位为 g/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_intksys_stdflow_bpt` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **EGR 阀标准质量流量，f\_egr\_stdflow** — 表 `vector`

EGR 阀标准质量流量查找表是 EGR 阀流通面积百分比和压力比的函数

m˙EGR,std=fEGR,std(EGRap,Pout,EGRPin,EGR)

其中：

- m˙EGR,std 是 EGR 阀标准质量流量，无量纲。
- *EGRap* 是 EGR 阀流通面积百分比，单位为 percent。
- Pout,EGRPin,EGR 是压力比，无量纲。

标准质量流量与压力比和流通面积百分比的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **EGR 阀标准流量压力比断点，f\_egr\_stdflow\_pr\_bpt** — 断点 `vector`

EGR 阀标准流量压力比，Pout,EGRPin,EGR，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow_pr_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR 阀标准流量面积百分比断点，f\_egr\_stdflow\_egrap\_bpt** — 断点 `[0;5;10;15;20;25;30;35;40;45;50;55;60;65;70;75;80;85;90;95;100]`（默认）| `vector`

EGR 阀流通面积百分比，*EGRap*，单位为 percent。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow_egrap_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 扭矩

### **扭矩表，f\_tq\_nl** — 查找表 `[L x N] array`

对于简单扭矩查找表模型，SI 发动机使用一个作为发动机转速和负载函数的查找表映射，Tbrake=fTnL(L,N)，其中：

- Tbrake 是计入火花提前、AFR 和摩擦效应后的发动机制动扭矩，单位为 N·m。
- *L* 是发动机负载，作为归一化气缸空气质量，无量纲。
- *N* 是发动机转速，单位为 rpm。

计入火花提前后的发动机制动扭矩与发动机负载和发动机转速的 3D 图

简单扭矩查找模型假定校准中具有负扭矩值，以指示不点火发动机负载 (L) 与转速 (N) 工况。校准表 (L-by-N) 在第一个表行 (1-by-N) 中包含不点火数据。当输送到发动机的燃料为零时，模型在 AFR 大于等于 100 时使用第一个表行 (1-by-N) 中的数据。AFR 为 100 是由断油或无法发生燃烧的极稀运行导致的。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Simple Torque Lookup`。

### **扭矩表负载断点，f\_tq\_nl\_l\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector` | `[1 x L] vector`

发动机负载断点，*L*，无量纲。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Simple Torque Lookup`。

### **扭矩表转速断点，f\_tq\_nl\_n\_bpt** — 断点 `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认）| `vector` | `[1 x N] vector`

发动机转速断点，*N*，单位为 rpm。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Simple Torque Lookup`。

### **曲轴角压力和扭矩** — 启用曲轴角信号 `off`（默认）| `on`

如果在模块 **Torque** 选项卡上选择 **曲轴角压力和扭矩**，您可以：

- 在桌面仿真和 HIL 台架上，基于从模型或实验室测试记录的作为曲轴角函数的气缸压力，仿真高级闭环发动机控制。
- 仿真由高频曲轴扭转引起的发动机下游传动系统振动。
- 通过使用喷油器脉冲宽度输入，仿真由稀薄运行或火花塞积垢导致的发动机失火。
- 仿真气缸停用效果（进气和排气门关闭，不喷油）对单独气缸压力、均值空气流量、均值扭矩和基于曲轴角的扭矩的影响。
- 仿真断油效果对单独气缸压力、均值扭矩和基于曲轴角的扭矩的影响。

#### 依赖项

要启用此参数，请将 **扭矩模型** 设置为 `Torque Structure`。

### **气缸压力，f\_crk\_prs** — 气缸压力表 `L x M x N` array

气缸压力表 *Prs*，作为转速 *N*、负载 *L* 和曲轴角 *M* 的函数，单位为 Pa。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。选择 **曲轴角压力和扭矩**。

### **制动扭矩，f\_crk\_btq** — 制动扭矩表 `L x M x N` array

制动扭矩表 *Tbrake*，作为转速 *N*、负载 *L* 和曲轴角 *M* 的函数，单位为 N·m。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。选择 **曲轴角压力和扭矩**。

### **转速断点，f\_crk\_n\_bpt** — 转速断点 `[750 5000]`（默认）| `1 x N` vector

转速断点，*N*，单位为 rpm。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。选择 **曲轴角压力和扭矩**。

### **负载断点，f\_crk\_l\_bpt** — 负载断点 `[0.2 1.4]`（默认）| `1 x L` vector

负载断点，*L*。无量纲。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。选择 **曲轴角压力和扭矩**。

### **曲轴角断点，f\_crk\_ang\_bpt** — 曲轴角断点 `[60 660]`（默认）| `1 x M` vector

曲轴角断点，*M*，单位为 deg。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。选择 **曲轴角压力和扭矩**。

### **各气缸 TDC 压缩角，f\_crk\_tdc\_ang** — 各气缸 TDC 压缩角 `[0 540 180 360]`（默认）| vector

各气缸上止点 (TDC) 压缩角，单位为 deg。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。选择 **曲轴角压力和扭矩**。

### **内部扭矩表，f\_tq\_inr** — 查找表 `array`

内部扭矩查找表 fTqinr 是发动机转速和发动机负载的函数，Tqinr=fTqinr(L,N)，其中：

- Tqinr 是基于总指示平均有效压力的内部扭矩，单位为 N·m。
- *L* 是在任意凸轮相位器角度下、已针对最终稳态凸轮相位器角度修正的发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

基于总指示平均有效压力的内部扭矩与任意凸轮相位器角度下的发动机负载和发动机转速的 3D 图

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **摩擦扭矩表，f\_tq\_fric** — 查找表 `array`

摩擦扭矩查找表 fTfric 是发动机转速和发动机负载的函数，Tfric=fTfric(L,N)，其中：

- Tfric 是内部扭矩的摩擦扭矩偏移，单位为 N·m。
- *L* 是在任意凸轮相位器角度下、已针对最终稳态凸轮相位器角度修正的发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

内部扭矩的摩擦扭矩偏移与任意凸轮相位器角度下的发动机负载和发动机转速的 3D 图

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **摩擦扭矩的发动机温度修正系数，f\_fric\_temp\_mod** — 查找表 `[3.96 3.22 2.56 2.26 2.11 2 1.9 1.83 1.76 1.7 1.65 1.6 1.55 1.49 1.44 1.41 1.38 1.35 1.32 1.3 1.27 1.25 1.24 1.21 1.2 1.18 1.16 1.15 1.13 1.12 1.11 1.1 1.09 1.08 1.07 1.06 1.05 1.05 1.04 1.03 1.02 1.02 1.01 1.01 1 1 1 0.999 0.997 0.995 0.993 0.991 0.989 0.987]`（默认）| `vector` | `vector`

摩擦扭矩的发动机温度修正系数，*ƒfric,temp*，无量纲。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **发动机温度修正系数断点，f\_fric\_temp\_bpt** — 断点 `[274 276 278 280 282 284 286 288 290 292 294 296 298 300 302 304 306 308 310 312 314 316 318 320 322 324 326 328 330 332 334 336 338 340 342 344 346 348 350 352 354 356 358 360 362 364 366 368 370 372 374 376 378 380]`（默认）| `vector` | `vector`

发动机温度修正系数断点，单位为 K。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **泵气扭矩表，f\_tq\_pump** — 查找表 `array`

泵气扭矩查找表 *ƒTpump* 是发动机负载和发动机转速的函数，`Tpump=ƒTpump(L,N)`，其中：

- *Tpump* 是泵气扭矩，单位为 N·m。
- *L* 是发动机负载，作为归一化气缸空气质量，无量纲。
- *N* 是发动机转速，单位为 rpm。

泵气扭矩与发动机负载和发动机转速的 3D 图

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **最佳点火表，f\_sa\_opt** — 查找表 `array`

最佳点火查找表 fSAopt 是发动机转速和发动机负载的函数，SAopt=fSAopt(L,N)，其中：

- *SAopt* 是在化学计量空燃比 (AFR) 下获得最大内部扭矩的最佳点火提前正时，单位为 deg。
- *L* 是在任意凸轮相位器角度下、已针对最终稳态凸轮相位器角度修正的发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

在化学计量空燃比 (AFR) 下获得最大内部扭矩的最佳点火提前正时与发动机负载和发动机转速的 3D 图

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **内部扭矩负载断点，f\_tq\_inr\_l\_bpt** — 断点 `[0.2 0.28571 0.37143 0.45714 0.54286 0.62857 0.71429 0.8 0.88571 0.97143 1.0571 1.1429 1.2286 1.3143 1.4]`（默认）| `vector`

内部扭矩负载断点，无量纲。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **内部扭矩转速断点，f\_tq\_inr\_n\_bpt** — 断点 `[750 1053.5714 1357.1429 1660.7143 1964.2857 2267.8571 2571.4286 2875 3178.5714 3482.1429 3785.7143 4089.2857 4392.8571 4696.4286 5000]`（默认）| `vector`

内部扭矩转速断点，单位为 rpm。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **点火效率表，f\_m\_sa** — 查找表 `array`

点火效率查找表 fMsa 是相对于最佳点的点火延迟的函数

Msa=fMsa(ΔSA)ΔSA=SAopt−SA

其中：

- Msa 是点火延迟效率乘数，无量纲。
- ΔSA 是距最佳点火提前的点火延迟正时距离，单位为 deg。

点火延迟效率与点火延迟正时距离的关系

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **相对于最佳点的点火延迟，f\_del\_sa\_bpt** — 断点 `[0 0.75 1.5 2.25 3 3.75 4.5 5.25 6 6.75 7.5 8.25 9 9.75 10.5 11.25 12 12.75 13.5 14.25 15 15.75 16.5 17.25 18 18.75 19.5 20.25 21 21.75 22.5 23.25 24 24.75 25.5 26.25 27 27.75 28.5 29.25 30 30.75 31.5 32.25 33 33.75 34.5 35.25 36 36.75 37.5 38.25 39 39.75 40.5 41.25 42 42.75 43.5 44.25 45 45.75 46.5 47.25 48]`（默认）| `vector`

相对于最佳内部扭矩正时的点火延迟断点，单位为 deg。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **Lambda 效率，f\_m\_lam** — 查找表 `array`

Lambda 效率查找表 fMλ 是 lambda 的函数，Mλ=fMλ(λ)，其中：

- Mλ 是用于考虑空燃比 (AFR) 效应对内部扭矩影响的 lambda 乘数，无量纲。
- λ 是 lambda，即 AFR 归一化到化学计量燃料 AFR，无量纲。

lambda 乘数与 lambda 的关系图

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

### **Lambda 断点，f\_m\_lam\_bpt** — 断点 `[0.65 0.7 0.75 0.8 0.85 0.9 0.95 1 1.05 1.1]`（默认）| `vector`

Lambda 对内部扭矩影响的 lambda 断点，无量纲。

#### 依赖项

要启用此参数，请对 **扭矩模型** 参数选择 `Torque Structure`。

#### 排气

### **排气温度表，f\_t\_exh** — 查找表 `array`

排气温度查找表 fTexh 是发动机负载和发动机转速的函数

Texh=fTexh(L,N)

其中：

- *Texh* 是发动机排气温度，单位为 K。
- *L* 是归一化气缸空气质量或发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

发动机排气温度与发动机转速和发动机负载的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **负载断点，f\_t\_exh\_l\_bpt** — 断点 `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认）| `vector`

用于排气温度查找表的发动机负载断点。

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

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

使用驾驶员扭矩请求的火花点火发动机控制器

SI Controller 模块实现了一个火花点火
(SI) 控制器，使用驾驶员扭矩请求计算满足驾驶员需求所需的
开环空气、燃油和火花执行器命令。

您可以在发动机控制设计或性能、燃油经济性和排放权衡研究中使用 SI Controller 模块。核心发动机、节气门和涡轮增压器废气门子系统需要 SI Controller 模块输出的命令。

该模块使用指令扭矩和发动机转速确定以下开环执行器命令：

- 节气门位置百分比
- 废气门面积百分比
- 喷油器脉冲宽度
- 点火提前角
- 进气凸轮相位器角度
- 排气凸轮相位器角度
- 废气再循环 (EGR) 阀面积百分比

SI Controller 模块有两个子系统：

- `Controller` 子系统 —
  根据指令扭矩、测量的发动机转速和估计的气缸空气质量确定命令。
- `Estimator` 子系统 —
  根据进气歧管气体压力、进气歧管气体温度、发动机转速和凸轮相位器位置确定估计的空气质量流量、扭矩和排气温度。

下图说明了信号流。

下图使用以下变量。

|  |  |
| --- | --- |
| *N* | 发动机转速 |
| *MAP* | 循环平均进气歧管压力 |
| *IAT* | 进气温度 |
| *Tin,EGR* | EGR 阀入口处的温度 |
| *MAT* | 循环平均进气歧管气体绝对温度 |
| φICP, φICPCMD | 进气凸轮相位器角度和进气凸轮相位器角度命令，分别 |
| φECP, φECPCMD | 排气凸轮相位器角度和排气凸轮相位器角度命令，分别 |
| *EGRap*, *EGRapcmd* | EGR 阀面积百分比和 EGR 阀面积百分比命令，分别 |
| *ΔPEGR* | EGR 阀入口和出口处的压差 |
| *WAPcmd* | 涡轮增压器废气门面积百分比命令 |
| *SA* | 点火提前角 |
| Pwinj | 燃油喷油器脉冲宽度 |
| *TPPcmd* | 节气门位置百分比命令 |

Model-Based Calibration Toolbox™ 用于开发 Powertrain Blockset™ 中可用的表格。

### Controller

**空气**

该模块根据作为指令扭矩和测量发动机转速函数的查找表确定指令发动机负荷（即归一化气缸空气质量）。

Lcmd=fLcmd(Tcmd,N)

为实现指令负荷，控制器使用前馈查找表设置节气门位置百分比和涡轮增压器废气门面积百分比。查找表是指令负荷和测量发动机转速的函数。

TAPcmd=fTAPcmd(Lcmd,N)

TPPcmd=fTPPcmd(TAPcmd)

WAPcmd=fWAPcmd(Lcmd,N)

为确定凸轮相位器角度命令，该模块使用作为估计发动机负荷和测量发动机转速函数的查找表。

φICPCMD=fICPCMD(Lest,N)

φECPCMD=fECPCMD(Lest,N)

该模块使用以下方程计算期望发动机负荷。

Lest=CpsRairTstdm˙air,estPstdVdN

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Lest* | 估计发动机负荷 |
| *Lcmd* | 指令发动机负荷 |
| *N* | 发动机转速 |
| *Tcmd* | 指令发动机扭矩 |
| *TAPcmd* | 节气门面积百分比命令 |
| *TPPcmd* | 节气门位置百分比命令 |
| *WAPcmd* | 涡轮增压器废气门面积百分比命令 |
| Cps | 每做功冲程的曲轴转数 |
| Pstd | 标准压力 |
| Tstd | 标准温度 |
| Rair | 空气和已燃气混合物的理想气体常数 |
| Vd | 排量 |
| m˙air,est | 估计发动机空气质量流量 |

Controller 子系统使用以下查找表进行空气计算。

- 节气门面积百分比命令查找表 fTAPcmd 是指令负荷和发动机转速的函数

  TAPcmd=fTAPcmd(Lcmd,N)

  其中：

  - *TAPcmd* 是节气门面积百分比命令，单位为 percent。
  - *Lcmd*=*L* 是指令发动机负荷，dimensionless。
  - *N* 是发动机转速，单位为 rpm。

  节气门面积百分比命令与指令发动机负荷和发动机转速的 3D 图
- 为考虑节气门位置与节气门面积之间的非线性，节气门位置百分比查找表将开环空气质量流量控制线性化。

  节气门位置百分比命令查找表 fTPPcmd 是节气门面积百分比命令的函数

  TPPcmd=fTPPcmd(TAPcmd)

  其中：

  - *TPPcmd* 是节气门位置百分比命令，单位为 percent。
  - *TAPcmd* 是节气门面积百分比命令，单位为 percent。

  节气门位置与节气门面积的关系图
- 废气门面积百分比命令查找表 fWAPcmd 是指令发动机负荷和发动机转速的函数

  WAPcmd=fWAPcmd(Lcmd,N)

  其中：

  - *WAPcmd* 是废气门面积百分比命令，单位为 percent。
  - *Lcmd*=*L* 是指令发动机负荷，dimensionless。
  - *N* 是发动机转速，单位为 rpm。

  废气门面积百分比命令与指令发动机负荷和发动机转速的 3D 图
- 指令发动机负荷查找表 fLcmd 是指令扭矩和发动机转速的函数

  Lcmd=fLcmd(Tcmd,N)

  其中：

  - *Lcmd*=*L* 是指令发动机负荷，dimensionless。
  - *Tcmd* 是指令扭矩，单位为 N·m。
  - *N* 是发动机转速，单位为 rpm。

  指令发动机负荷与指令扭矩和发动机转速的 3D 图
- 进气凸轮相位器角度命令查找表 fICPCMD 是发动机负荷和发动机转速的函数

  φICPCMD=fICPCMD(Lest,N)

  其中：

  - φICPCMD 是指令进气凸轮相位器角度，单位为 crank degrees advance from park。
  - *Lest*=*L* 是指令发动机负荷，dimensionless。
  - *N* 是发动机转速，单位为 rpm。

  指令进气凸轮相位器角度与指令发动机负荷和发动机转速的 3D 图
- 排气凸轮相位器角度命令查找表 fECPCMD 是发动机负荷和发动机转速的函数

  φECPCMD=fECPCMD(Lest,N)

  其中：

  - φECPCMD 是指令排气凸轮相位器角度，单位为 crank degrees retard from park。
  - *Lest*=*L* 是估计发动机负荷，dimensionless。
  - *N* 是发动机转速，单位为 rpm。

  指令排气凸轮相位器角度与估计发动机负荷和发动机转速的 3D 图

**EGR**

EGR 通常表示为总进气道流量的百分比。

EGRpct=100m˙EGRm˙EGR+m˙air

为计算 EGR 面积百分比命令，该模块使用方程和查找表。

|  |  |
| --- | --- |
| 方程 | m˙EGRstd,cmd=m˙EGR,cmdPstdPin,EGRTin,EGRTstdm˙EGRstd,max=fEGRstd,max(Pout,EGRPin,EGR)m˙EGR,cmd=EGRpct,cmdm˙intk,est |
| 查找表 | EGR 面积百分比命令 *EGRapcmd* 查找表是归一化质量流量和压力比的函数

EGRapcmd=fEGRap,cmd(m˙EGRstd,cmdm˙EGRstd,max,Pout,EGRPin,EGR)

其中：

- *EGRapcmd* 是指令 EGR 面积百分比，
  dimensionless。
- m˙EGRstd,cmdm˙EGRstd,max 是归一化质量流量，dimensionless。
- Pout,EGRPin,EGR 是压力比，dimensionless。

    指令 EGR 百分比与归一化质量流量和压力比的 3D 图 |

方程和表使用以下变量。

|  |  |
| --- | --- |
| *EGRap*, *EGRapcmd* | EGR 阀面积百分比和 EGR 阀面积百分比命令，分别 |
| *EGRpct,cmd* | EGR 百分比命令 |
| m˙EGRstd,cmd | 指令标准质量流量 |
| m˙EGRstd,max | 最大标准质量流量 |
| m˙EGR,cmd | 指令质量流量 |
| m˙intk,est | 估计进气道质量流量 |
| *Tstd*, *Pstd* | 标准温度和压力 |
| *Tin,EGR* | EGR 阀入口处的温度 |
| *Pout,EGR*, *Pin,EGR* | EGR 阀入口和出口处的压力，分别 |

**燃油**

空燃比 (AFR) 影响三元催化器 (TWC) 转化效率、扭矩产生和燃烧温度。发动机控制器通过根据期望相对 AFR 指令喷油器脉冲宽度来管理 AFR。相对 AFR，λcmd，是指令 AFR 与燃料化学计量 AFR 之比。

λcmd=AFRcmdAFRstoich

AFRcmd=m˙air,estm˙fuel,cmd

SI Controller 模块考虑了启动期间输送到 SI 发动机的额外燃油。如果发动机转速大于启动发动机拖动转速，SI Controller 模块使用指数衰减的 delta lambda 对最佳 AFR、lambda 进行加浓。为初始化 delta lambda，该模块使用启动时的发动机冷却液温度。delta lambda 基于作为发动机冷却液温度函数的时间常数指数衰减到零。

您可以将该模块配置为开环和闭环 AFR 控制。

| 目的 | 使用 | **Controls** > **Fuel** > **Closed-loop feedback** 参数设置 |
| --- | --- | --- |
| - 评估控制器空气流量估计和燃油输送的动态和稳态精度。 | （默认）开环控制 | `off` |
| - 将平均 AFR 保持在接近化学计量 AFR，以维持高 TWC 转化效率。 | 闭环控制 | `on` |

**开环控制**

要为指令 AFR (lambda) 创建输入端口，请在 **Controls** > **Fuel** > **Open-loop fuel** 窗格上选择 **Input lambda**。

在开环 AFR 控制期间，您可以使用或不使用 dither 手动调整催化器以获得最大效率。如果要在开环控制期间实现 dither，请在 **Fuel** 选项卡的 **Closed-loop fuel** 窗格上选择 **Dither**。

默认情况下，该模块配置为对指令 AFR 使用查找表。

指令 lambda，λcmd，查找表是估计发动机负荷和测量发动机转速的函数

λcmd=fλcmd(Lest,N)

其中：

- λcmd 是指令相对 AFR，dimensionless。
- *Lest*=*L* 是指令发动机负荷，dimensionless。
- *N* 是发动机转速，单位为 rpm。

指令相对 AFR 与指令发动机负荷和发动机转速的 3D 图

该模块使用指令 lambda、λcmd、化学计量 AFR 和估计空气质量流量计算估计燃油质量流量率。

m˙fuel,cmd=m˙air,estAFRcmd=m˙air,estλcmdAFRstoich

该模块假设电池电压和燃油压力处于标称设置，此时不需要脉冲宽度校正。指令燃油喷油器脉冲宽度与每次喷射的燃油质量成正比。每次喷射的燃油质量根据指令燃油质量流量率、发动机转速和气缸数计算。

Pwinj={m˙fuel,cmdCps(60smin)(1000mgg)(1000gkg)NSinjNcylwhen  Trqcmd>00when  Trqcmd≤0

**闭环控制**

当排气 AFR 接近化学计量 AFR 时，TWC 转化器效率最高，此时空气和燃油燃烧最完全。在此理想点附近，AFR 处于 *催化器窗口* 内，在该窗口内催化剂将一氧化碳、碳氢化合物和氮氧化物转化为无害排气产物的效率最高。实证研究表明，以优化的 AFR 频率、幅度和偏置使 AFR 在化学计量附近振荡会拓宽 TWC 窗口，在存在不可避免扰动时提高催化剂转化效率。

为降低量产硬件成本，AFR 控制系统包括廉价的开关型氧传感器，放置在发动机排气流中催化器的上游和下游。氧传感器具有窄范围。本质上，它们在过稀（即，可用空气多于燃烧可用燃油所需）和过浓（即，可用空气多于燃烧可用燃油所需）之间切换。

该模块实现基于周期的方法，将平均 AFR 控制在催化器窗口内的某个值，以获得最大转化效率。基于周期的 AFR 控制独立于从燃油喷射点到传感器测量点跨发动机的传输延迟。有关该方法的更多信息，请参见 Developing a Period-Based Air-Fuel Ratio Controller Using a Low-Cost Switching Sensor。

**火花**

点火提前角是在做功冲程中火花发出时相对于上止点前 (BTDC) 的曲轴转角。点火提前角影响发动机效率、扭矩、排气温度、爆震和排放。

点火提前角查找表是估计负荷和发动机转速的函数。

SA=fSA(Lest,N)

其中：

- *SA* 是点火提前角，单位为 crank advance degrees。
- *Lest*=*L* 是指令发动机负荷，dimensionless。
- *N* 是发动机转速，单位为 rpm。

点火提前角与指令发动机负荷和发动机转速的 3D 图

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Lest* | 估计发动机负荷，基于归一化气缸空气质量 |
| *N* | 发动机转速 |
| fSA | 点火提前角查找表 |
| *N* | 点火提前角 |

**怠速**

当指令扭矩低于阈值时，怠速控制器调节发动机转速。

| 如果 | 怠速控制器 |
| --- | --- |
| *Trqcmd,input* < *Trqidlecmd,enable* | 启用 |
| *Trqidlecmd,enable* ≤ *Trqcmd,input* | 未启用 |

怠速控制器使用离散 PI 控制器通过指令扭矩来调节目标怠速转速。

PI 控制器使用以下传递函数：

Cidle(z)=Kp,idle+Ki,idletsz−1

怠速指令扭矩必须小于最大指令扭矩：

0 ≤ *Trqidlecomd* ≤*Trqidlecmd,max*

在这些条件下，怠速控制处于活动状态。如果指令输入扭矩降至启用怠速控制器的阈值以下 (*Trqcmd,input* < *Trqidlecmd,enable*)，则指令发动机扭矩由下式给出：

*Trqcmd* = max(*Trqcmd,input*,*Trqidlecmd*).

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Trqcmd* | 指令发动机扭矩 |
| *Trqcmd,input* | 输入指令发动机扭矩 |
| *Trqidlecmd,enable* | 启用怠速控制器的阈值 |
| *Trqidlecmd* | 怠速控制器指令扭矩 |
| *Trqidlecmd,max* | 最大指令扭矩 |
| *Nidle* | 基准怠速转速 |
| *Kp,idle* | 怠速控制器比例增益 |
| *Ki,idle* | 怠速控制器积分增益 |

**转速限制器**

为防止发动机超转，该模块实现了一个发动机转速限制控制器，将发动机转速限制为 **Controls** > **Idle Speed** 选项卡上 **Rev-limiter speed threshold** 参数指定的值。

如果发动机转速 *N* 超过发动机转速限制 *Nlim*，该模块将指令发动机扭矩设置为 0。

为使扭矩命令在发动机转速接近转速限制时平滑过渡到 0，该模块实现了一个查找表乘数。该查找表将扭矩命令乘以一个值，该值范围从 0（发动机转速超过限制）到 1（发动机转速未超过限制）。

### Estimator

Estimator 子系统根据传感器反馈和标定参数确定估计的空气质量流量、扭矩、EGR 质量流量和排气温度。

|  |  |
| --- | --- |
| m˙air,est | 估计的发动机空气质量流量 |
| *Trqest* | 估计的发动机扭矩 |
| *Texh,est* | 估计的发动机排气温度 |
| m˙EGR,est | 估计的低压 EGR 质量流量 |

**空气流量**

要计算发动机空气质量流量，请将 SI 发动机配置为使用以下任一空气流量模型。

| 空气流量模型 | 描述 |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | 使用速度密度方程计算发动机空气质量流量，将发动机空气质量流量与进气歧管压力和发动机转速关联。考虑在采用固定气门机构设计的发动机中使用此空气流量模型。 |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | 为计算发动机空气质量流量，dual-independent cam phaser 模型使用：  - 根据发动机 mapping 测量开发的经验标定参数 - 从发动机计算机辅助设计 (CAD) 数据推导的桌面标定参数  与基于使用空气流量 (MAF) 传感器直接测量空气流量的典型嵌入式空气流量计算相比，此空气流量模型具有：  - 在双凸轮相位气门机构应用中无需 MAF 传感器 - 在海拔变化时具有合理的精度 - 半物理建模方法 - 有界行为 - 适合电子控制单元 (ECU) 实现的执行时间 - 系统化开发相对较少数量的标定参数 |

为确定估计的空气流量，模块使用进气空气质量分数。进气口处的 EGR 质量分数滞后于 EGR 阀出口附近的质量分数。为对该滞后建模，模块使用带时间常数的一阶系统。

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
| SI Engine Torque Structure Model | 对于结构化制动扭矩计算，SI 发动机使用内部扭矩、摩擦扭矩、最佳点火、点火效率和 lambda 效率表。  如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，您可以：  - 基于从模型或实验室测试记录的作为曲轴转角函数的气缸压力，在桌面仿真和 HIL 台架上仿真高级闭环发动机控制。 - 仿真由于高频曲轴扭转引起的发动机下游动力传动系统振动。 - 通过使用喷油器脉冲宽度输入，仿真由于稀薄运行或火花塞积污导致的发动机失火。 - 仿真气缸停用效果（进气门和排气门关闭，不喷射燃油）对单个气缸压力、均值空气流量、均值扭矩和基于曲轴转角的扭矩的影响。 - 仿真断油效果对单个气缸压力、均值扭矩和基于曲轴转角的扭矩的影响。 |
| SI Engine Simple Torque Model | 对于简单制动扭矩计算，SI 发动机模块使用作为发动机转速和负载函数的扭矩查找表映射。 |

**EGR**

控制器使用由 F. Liu 和 J. Pfeiffer 开发的算法估计低压质量流量、EGR 阀进口压力和 EGR 阀出口压力。Estimator 需要测量的 EGR 阀压差、EGR 阀面积百分比、进气温度和 EGR 阀进口温度。

为估计 EGR 阀命令，模块使用：

- 方程

  m˙air,std=m˙air,estPstdPambIATTstdPin,EGR=Pout,EGR+ΔPEGRm˙EGR,est=m˙EGR,stdPin,EGRPstdTstdTin,EGR

- 表

  - EGR 阀标准质量流量查找表是 EGR 阀面积百分比和压力比的函数

    m˙EGR,std=fEGR,std(EGRap,Pout,EGRPin,EGR)

    其中：

    - m˙EGR,std 是 EGR 阀标准质量流量，无量纲。
    - *EGRap* 是 EGR 阀流通面积百分比，单位为 percent。
    - Pout,EGRPin,EGR 是压力比，无量纲。

    标准质量流量随压力比和流通面积百分比变化的三维图

  - 压力比是标准质量流量的函数

    Pout,EGRPamb=fintksys,pr(m˙air,std)

    其中：

    - m˙air,std 是标准质量流量，单位为 g/s。
    - Pout,EGRPamb 是压力比，无量纲。

    压力比随质量流量变化的图

这些方程使用以下变量。

|  |  |
| --- | --- |
| *EGRap* | EGR 阀面积百分比命令 |
| *IAT* | 进气温度 |
| m˙air,std, m˙EGR,std | 分别表示标准空气质量流量和 EGR 阀质量流量 |
| m˙air,est,m˙EGR,est | 分别表示估计的空气质量流量和 EGR 阀质量流量 |
| *Tstd*, *Pstd* | 标准温度和压力 |
| *Tamb*, *Pamb* | 环境温度和压力 |
| *ΔPEGR* | EGR 阀进口和出口处的压差 |
| *Tin,EGR*, *Tout,EGR* | 分别表示 EGR 阀进口和出口处的温度 |
| *Pin,EGR*, *Pout,EGR* | 分别表示 EGR 阀进口和出口处的压力 |

**排气温度**

排气温度查找表 fTexh 是发动机负载和发动机转速的函数

Texh=fTexh(L,N)

其中：

- *Texh* 是发动机排气温度，单位为 K。
- *L* 是归一化气缸空气质量或发动机负载，无量纲。
- *N* 是发动机转速，单位为 rpm。

发动机排气温度随发动机转速和发动机负载变化的三维图
