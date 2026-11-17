---
type: simulink-block
title: 'CI Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Controllers'
documentation_page: 'cicontroller'
documentation_source_path: 'ref/cicontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# CI Controller

## 端口

### 输入

### **TrqCmd** — 指令发动机扭矩 `scalar`

指令发动机扭矩，*Trqcmd,input*，单位为 N·m。

### **EngSpd** — 测量的发动机转速 `scalar`

测量的发动机转速，*N*，单位为 rpm。

### **Map** — 测量的进气歧管绝对压力 `scalar`

测量的进气歧管绝对压力，*MAP*，单位为 Pa。

### **Mat** — 测量的进气歧管绝对温度 `scalar`

测量的进气歧管绝对温度，*MAT*，单位为 K。

### **AmbPrs** — 环境压力 `scalar`

绝对环境压力，PAmb，单位为 Pa。

### **EgrVlvAreaPct** — EGR 阀面积百分比 `scalar`

测量的 EGR 阀面积百分比，*EGRap*，单位为 %。

### **VgtPos** — VGT 转速 `scalar`

测量的 VGT 齿条位置，*VGTpos*。

### **VgtSpd** — VGT 转速 `scalar`

测量的 VGT 转速，*Nvgt*，单位为 rpm。

### **Ect** — 发动机冷却温度 `scalar`

发动机冷却温度，*Tcoolant*，单位为 K。

### **IgSw** — 点火开关 `Boolean`

车辆点火开关状态，无量纲。

#### 依赖关系

要创建此端口，请在 **Stop-Start** 选项卡上，选择 **Enable Engine Stop-Start**。

### **ESSEnable** — 发动机起停使能 `Boolean`

用于使能或禁用起停逻辑的命令，无量纲。

#### 依赖关系

要创建此端口，请在 **Stop-Start** 选项卡上，选择 **Enable Engine Stop-Start**。选择 **External Enable Port**。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `InjPw` | 燃油喷射器脉冲宽度 | Pwinj | ms |
| `EgrVlvAreaPctCmd` | EGR 阀面积百分比指令 | *EGRcmd* | % |
| `TurbRackPosCmd` | VGT 齿条位置指令 | *RPcmd* | N/A |
| `TrqCmd` | 发动机扭矩 | *Trqcmd* | N·m |
| `FuelMassTotCmd` | 每次喷射的指令总燃油质量 | *Fcmd,tot* | mg |
| `FuelMainSoi` | 主喷射开始正时 | *MAINSOI* | degATDC |
| `FuelMassFlwCmd` | 指令燃油质量流量 | m˙fuel,cmd | kg/s |
| `EstIntkPortMassFlw` | 估计的进气口质量流量 | m˙port,est | kg/s |
| `EstEngTrq` | 估计的发动机扭矩 | *Trqest* | N·m |
| `EstExhManGasTemp` | 估计的排气歧管气体温度 | *Texh,est* | K |
| `EstExhPrs` | 估计的排气背压 | *Pex* | Pa |
| `EstEGRFlow` | `EstEGRFlow` | `EstEGRFlow` | `EstEGRFlow` |
| `EstAfr` | 估计的空燃比 | *AFRest* | N/A |
| `EngRevLimAct` | 指示转速限制器控制是否激活的标志 | N/A | N/A |

### **InjPw** — 燃油喷射器脉冲宽度 `scalar`

燃油喷射器脉冲宽度，Pwinj，单位为 ms。

### **FuelMainSoi** — 燃油主喷射正时 `scalar`

主喷射开始正时，*MAINSOI*，单位为上止点后曲轴转角（degATDC）。

### **TurbRackPosCmd** — 齿条位置 `scalar`

VGT 齿条位置指令，*RPcmd*。

### **EgrVlvAreaPctCmd** — 进气凸轮相位器角度指令 `scalar`

EGR 阀面积百分比指令，*EGRcmd*。

## 参数

### 控制

#### 空气 - EGR

### **EGR 阀面积百分比，f\_egrcmd** — 查找表 `array`

指令废气再循环（EGR）阀面积百分比查找表是指令扭矩和发动机转速的函数

EGRcmd=fEGRcmd(Trqcmd,N)

其中：

- *EGRcmd* 是指令 EGR 阀面积百分比，单位为百分比。
- *Trqcmd* 是指令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

指令 EGR 阀面积百分比相对于指令扭矩和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egrcmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **指令扭矩断点，f\_egr\_tq\_bpt** — 断点 `[10 26.43 42.86 59.29 75.71 92.14 108.6 125 141.4 157.9 174.3 190.7 207.1 223.6 240]`（默认）| `vector`

指令扭矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_tq_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点，f\_egr\_n\_bpt** — 断点 `[1000 1411 1821 2232 2643 3054 3464 3875 4286 4696 5107 5518 5929 6339 6750]`（默认）| `vector`

转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 空气 - VGR

### **VGT 齿条位置表，f\_rpcmd** — 查找表 `array`

可变几何涡轮增压器（VGT）齿条位置查找
表是命令扭矩和发动机转速的函数

RPcmd=fRPcmd(Trqcmd,N)

其中：

- *RPcmd* 是
  VGT 齿条位置命令，单位为百分比。
- *Trqcmd* 是
  命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

齿条位置与命令扭矩和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_rpcmd` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **命令扭矩断点，f\_rp\_tq\_bpt** — 断点 `[10 26.43 42.86 59.29 75.71 92.14 108.6 125 141.4 157.9 174.3 190.7 207.1 223.6 240]`（默认）| `vector`

断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_rp_tq_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转速断点，f\_rp\_n\_bpt** — 断点 `[1000 1411 1821 2232 2643 3054 3464 3875 4286 4696 5107 5518 5929 6339 6750]`（默认）| `vector`

断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_rp_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 燃油

### **喷油器斜率，Sinj** — 斜率 `6.452`（默认）| `scalar`

燃油喷油器斜率，Sinj，单位为 mg/ms。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sinj` |
| **值：** | `6.452`（默认）| `scalar` |
| **数据类型：** | `double` |

### **化学计量空燃比，afr\_stoich** — 比值 `14.6`（默认）| `scalar`

化学计量空燃比，
*AFRstoich*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `afr_stoich` |
| **值：** | `14.6`（默认）| `scalar` |
| **数据类型：** | `double` |

### **燃油低热值，fuel\_lhv** — 热量 `42e6`（默认）| `scalar`

燃油低热值，单位为 J/kg。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `fuel_lhv` |
| **值：** | `42e6`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Fuel mass per injection table, f\_fcmd\_tot** — 查找表 `array`

指令的每次喷射总燃油质量表是扭矩指令和发动机转速的函数

Fcmd,tot=fFcmd,tot(Trqcmd,N)

其中：

- *Fcmd,tot* = *F* 是指令的每次喷射总燃油质量，单位为 mg/缸。
- *Trqcmd* 是指令的发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

指令的每次喷射总燃油质量与指令扭矩和发动机转速的三维图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_fcmd_tot` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Fuel main injection timing table, f\_main\_soi** — 查找表 `array`

主喷射开始（SOI）正时查找表是指令燃油质量和发动机转速的函数

MAINSOI=f(Fcmd,tot,N)

其中：

- *MAINSOI* 是主喷射开始正时，单位为上止点后曲轴转角（degATDC）。
- *Fcmd,tot* = *F* 是指令燃油质量，单位为 mg/次喷射。
- *N* 是发动机转速，单位为 rpm。

主喷射开始正时与指令燃油质量和发动机转速的三维图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_main_soi` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Fuel main injection timing fuel breakpoints, f\_main\_soi\_f\_bpt** — 断点 `vector`

主喷射正时燃油断点，单位为 mg/次喷射。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_main_soi_f_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Fuel main injection timing speed breakpoints, f\_main\_soi\_n\_bpt** — 断点 `[1000,1410.71428571429,1821.42857142857,2232.14285714286,2642.85714285714,3053.57142857143,3464.28571428571,3875,4285.71428571429,4696.42857142857,5107.14285714286,5517.85714285714,5928.57142857143,6339.28571428572,6750]`（默认） | `vector`

主喷射正时转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_main_soi_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Commanded torque breakpoints, f\_f\_tot\_tq\_bpt** — 断点 `[0 10 26.43 42.86 59.29 75.71 92.14 108.6 125 141.4 157.9 174.3 190.7 207.1 223.6 240]`（默认） | `vector`

指令扭矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_f_tot_tq_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Speed breakpoints, f\_f\_tot\_n\_bpt** — 断点 `[1000 1411 1821 2232 2643 3054 3464 3875 4286 4696 5107 5518 5929 6339 6750]`（默认） | `vector`

转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_f_tot_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 怠速

### **Base idle speed, N\_idle** — 转速 `750`（默认） | `scalar`

基础怠速转速，*Nidle*，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_idle` |
| **值：** | `750`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Enable torque command limit, Trq\_idlecmd\_enable** — Torque `1`（默认） | `scalar`

用于启用怠速转速控制器的扭矩，*Trqidlecmd,enable*，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_idlecmd_enable` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Maximum torque command, Trq\_idlecmd\_max** — Torque `50`（默认） | `scalar`

怠速控制器命令扭矩最大值，*Trqidlecmd,max*，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_idlecmd_max` |
| **值：** | `50`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Proportional gain, Kp\_idle** — PI Controller `0.05`（默认） | `scalar`

怠速转速控制的比例增益，*Kp,idle*，单位为 N·m/rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_idle` |
| **值：** | `0.05`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Integral gain, Ki\_idle** — PI Controller `0.2`（默认） | `scalar`

怠速转速控制的积分增益，*Ki,idle*，单位为 N·m/(rpm·s)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki_idle` |
| **值：** | `0.2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Rev-limiter speed threshold, EngRevLim** — Engine speed limit `6000`（默认） | `scalar`

发动机转速限制，*Nlim*，单位为 rpm。

如果发动机转速 *N* 超过发动机转速限制 *Nlim*，该模块将命令发动机扭矩设置为 0。

为了在发动机转速接近转速限制时使扭矩命令平滑过渡到 0，该模块实现了一个查找表乘数。该查找表将扭矩命令乘以一个值，该值范围为 0（发动机转速超过限制）到 1（发动机转速未超过限制）。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngRevLim` |
| **值：** | `6000`（默认） | `scalar` |
| **数据类型：** | `double` |

#### Stop-Start

### **Enable Engine Stop-Start** — Select to enable the engine stop-start logic `off`（默认） | `on`

选择以启用发动机停启逻辑。选择此选项将激活附加参数，以修改 Engine Stop-Start 模块的行为。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ESSEnable` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **External Enable Port** — Create input port `off`（默认） | `on`

选择以向发动机控制器模块添加一个端口，用于启用或禁用停启逻辑。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ESSExternalPortEnable` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上，选择 **Enable Engine Stop-Start**。

### **Engine stop time, EngStopTime** — 发动机停止时间 `5`（默认） | `scalar`

停止-启动逻辑的发动机停止时间，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngStopTime` |
| **值：** | `5`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上，选择 **Enable Engine Stop-Start**。

### **Catalyst light off time, CatLightOffTime** — 催化器起燃时间 `0`（默认） | `scalar`

停止-启动逻辑的催化器起燃时间，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CatLightOffTime` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上，选择 **Enable Engine Stop-Start**。

### **Sample time, Ts** — 采样时间 `0.01`（默认） | `scalar`

停止-启动逻辑的采样时间，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ts` |
| **值：** | `0.01`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Stop-Start** 选项卡上，选择 **Enable Engine Stop-Start**。

### 估计

#### 空气

### **Number of cylinders, NCyl** — 发动机气缸数 `4`（默认） | `scalar`

发动机气缸数，Ncyl。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Crank revolutions per power stroke, Cps** — 每做功冲程的转数 `2`（默认） | `scalar`

每做功冲程的曲轴转数，Cps，单位为 rev/stroke。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Total displaced volume, Vd** — 体积 `0.0015`（默认） | `scalar`

排量，Vd，单位为 m^3。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Ideal gas constant air, Rair** — 常数 `287`（默认） | `scalar`

理想气体常数，Rair，单位为 J/(kg·K)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

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

### **Speed density volumetric efficiency, f\_nv** — 查找表 `array`

容积效率查找表是进气门关闭（IVC）时进气歧管绝对压力和发动机转速的函数

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

### **Speed density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — 断点 `[95 100.3 105.7 111 116.4 121.7 127.1 132.4 137.8 143.1 148.4 153.8 159.1 164.5 169.8 175.2 180.5 185.9 191.2 196.6 201.9 207.2 212.6 217.9 223.3 228.6 234 239.3 244.7 250]`（默认）| `vector`

速度密度容积效率查找表的进气歧管压力断点，单位为 KPa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_prs_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Speed density engine speed breakpoints, f\_nv\_n\_bpt** — 断点 `[750 956.9 1164 1371 1578 1784 1991 2198 2405 2612 2819 3026 3233 3440 3647 3853 4060 4267 4474 4681 4888 5095 5302 5509 5716 5922 6129 6336 6543 6750]`（默认）| `vector`

速度密度容积效率查找表的发动机转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR valve standard flow calibration, f\_egr\_stdflow** — 查找表 `array`

标准废气再循环（EGR）质量流量是一个查找表，它是标准流量压力比和 EGR 阀流通面积的函数

m˙egr,std=f(MAPPexh,est,EGRap)

其中：

- m˙egr,std 是标准 EGR 阀质量流量，单位为 g/s。
- *Pexh,est* 是估计的排气背压，单位为 Pa。
- *MAP* 是循环平均进气歧管绝对压力，单位为 Pa。
- *EGRap* 是测量的 EGR 阀面积，单位为百分比。

标准 EGR 阀质量流量与循环平均进气歧管绝对压力和测量的 EGR 阀面积的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR valve standard flow pressure ratio breakpoints, f\_egr\_stdflow\_pr\_bpt** — 断点 `vector`

EGR 阀标准流量压力比断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow_pr_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **EGR valve standard flow area percent breakpoints, f\_egr\_stdflow\_egrap\_bpt** — 断点 `vector`

EGR 阀标准流量面积百分比断点，以百分比为单位。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_egr_stdflow_egrap_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Turbocharger pressure ratio, f\_turbo\_pr** — 查找表 `array`

涡轮增压器压力比，已针对可变几何涡轮增压器（VGT）转速进行修正，是一个查找表，它是标准空气质量流量和修正涡轮增压器转速的函数，Prturbo=f(m˙airstd,Nvgtcorr)，其中：

- *Prturbo* 是涡轮增压器压力比，已针对 VGT 转速进行修正。
- m˙airstd 是标准空气质量流量，单位为 g/s。
- *Nvgtcorr* 是修正涡轮增压器转速，单位为 rpm/K^(1/2)。

涡轮增压器压力比与标准空气质量流量和修正涡轮增压器转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_turbo_pr` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Turbocharger pressure ratio standard flow breakpoints, f\_turbo\_pr\_stdflow\_bpt** — 断点 `vector`

涡轮增压器压力比标准流量断点，单位为 g/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_turbo_pr_stdflow_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Turbocharger pressure ratio corrected speed breakpoints, f\_turbo\_pr\_corrspd\_bpt** — 断点 `vector`

涡轮增压器压力比修正转速断点，单位为 rpm/K^(1/2)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_turbo_pr_corrspd_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Turbocharger pressure ratio VGT position correction, f\_turbo\_pr\_vgtposcorr** — 查找表 `array`

可变几何涡轮增压器压力比修正值是齿条位置的函数，*Prvgtcorr*= ƒ(*VGTpos*)，其中：

- *Prvgtcorr* 是涡轮增压器压力比修正值。
- *VGTpos* 是可变几何涡轮增压器（VGT）齿条位置。

涡轮增压器压力比修正值与可变几何涡轮增压器（VGT）齿条位置的图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_turbo_pr_vgtposcorr` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Turbocharger pressure ratio VGT position correction breakpoints, f\_turbo\_pr\_vgtposcorr\_bpt** — 断点 `vector`

涡轮增压器压力比 VGT 位置修正断点，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 扭矩 - 简单扭矩查找

### **扭矩表，f\_tq\_nf** — 查找表 `array`

对于简单扭矩查找表模型，CI 发动机使用一个查找表，该查找表是发动机转速和喷射燃油质量的函数，Tbrake=fTnf(F,N)，其中：

- *Tq* = *Tbrake* 是考虑发动机机械摩擦和泵气摩擦效应后的发动机制动扭矩，单位为 N·m。
- *F* 是喷射燃油质量，单位为 mg/次喷射。
- *N* 是发动机转速，单位为 rpm。

发动机制动扭矩与喷射燃油质量和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Simple Torque Lookup`。

### **扭矩表每次喷射燃油质量断点，f\_tq\_nf\_f\_bpt** — 断点 `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]`（默认）| `vector`

扭矩表每次喷射燃油质量断点，单位为 mg/次喷射。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf_f_bpt` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Simple Torque Lookup`。

### **扭矩表转速断点，f\_tq\_nf\_n\_bpt** — 断点 `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]`（默认）| `vector`

发动机转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Simple Torque Lookup`。

#### 扭矩 - 扭矩结构

### **每次喷射燃油质量断点，f\_tqs\_f\_bpt** — 断点 `vector`

每次喷射燃油质量断点，单位为 mg/次喷射。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **发动机转速断点，f\_tqs\_n\_bpt** — 断点 `[500 750 1000 1250 1500 1750 2000 2250 2500 2750 3000 3250 3500 3750 4000]`（默认）| `vector`

发动机转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Optimal main start of injection timing, f\_tqs\_mainsoi** — 最优 MAINSOI `array`

最优主喷正时（SOI）查找表 *ƒSOIc* 是发动机转速和喷射燃油质量的函数，*SOIc = ƒSOIc(F,N)*，其中：

- *SOIc* 为最优 SOI 正时，单位为 degATDC。
- *F* 为压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 为发动机转速，单位为 rpm。

最优 SOI 正时随喷射燃油质量和发动机转速变化的三维图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mainsoi` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal intake manifold gas pressure, f\_tqs\_map** — 最优 intake MAP `array`

最优进气歧管气体压力查找表 *ƒMAP* 是发动机转速和喷射燃油质量的函数，*MAP = ƒMAP(F,N)*，其中：

- *MAP* 为最优进气歧管气体压力，单位为 Pa。
- *F* 为压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 为发动机转速，单位为 rpm。

最优进气歧管气体压力随喷射燃油质量和发动机转速变化的三维图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_map` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal exhaust manifold gas pressure, f\_tqs\_emap** — 最优 exhaust MAP `array`

最优排气歧管气体压力查找表 *ƒEMAP* 是发动机转速和喷射燃油质量的函数，*EMAP = ƒEMAP(F,N)*，其中：

- *EMAP* 为最优排气歧管气体压力，单位为 Pa。
- *F* 为压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 为发动机转速，单位为 rpm。

排气歧管气体压力随喷射燃油质量和发动机转速变化的三维图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_emap` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal intake manifold gas temperature, f\_tqs\_mat** — 最优 intake MAT `array`

最优进气歧管气体温度查找表 *ƒMAT* 是发动机转速和喷射燃油质量的函数，*MAT = ƒMAT(F,N)*，其中：

- *MAT* 为最优进气歧管气体温度，单位为 K。
- *F* 为压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 为发动机转速，单位为 rpm。

最优进气气体温度随压缩冲程喷射燃油质量和发动机转速变化的三维图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mat` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal intake gas oxygen percent, f\_tqs\_o2pct** — Optimal intake gas oxygen `array`

最佳进气氧气百分比查找表 *ƒO2* 是发动机转速和喷射燃油质量的函数，*O2PCT = ƒO2(F,N)*，其中：

- *O2PCT* 是最佳进气氧气百分比，单位为百分比。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/injection。
- *N* 是发动机转速，单位为 rpm。

最佳进气氧气百分比与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Optimal fuel rail pressure, f\_tqs\_fuelpress** — Optimal fuel rail pressure `array`

最佳燃油轨压力查找表 *ƒfuelp* 是发动机转速和喷射燃油质量的函数，*FUELP = ƒfuelp(F,N)*，其中：

- *FUELP* 是最佳燃油轨压力，单位为 MPa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/injection。
- *N* 是发动机转速，单位为 rpm。

最佳燃油轨压力与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Optimal gross indicated mean effective pressure, f\_tqs\_imepg** — Optimal mean effective pressure `array`

最佳总指示平均有效压力查找表 *ƒimepg* 是发动机转速和喷射燃油质量的函数，*IMEPG = ƒimepg(F,N)*，其中：

- *IMEPG* 是最佳总指示平均有效压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/injection。
- *N* 是发动机转速，单位为 rpm。

最佳总指示平均有效压力与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_imepg` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Optimal friction mean effective pressure, f\_tqs\_fmep** — Optimal friction mean effective pressure `array`

最佳摩擦平均有效压力查找表 *ƒfmep* 是发动机转速和喷射燃油质量的函数，*FMEP = ƒfmep(F,N)*，其中：

- *FMEP* 是最佳摩擦平均有效压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/injection。
- *N* 是发动机转速，单位为 rpm。

最佳摩擦平均有效压力与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fmep` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Optimal pumping mean effective pressure, f\_tqs\_pmep** — 最佳泵气平均有效压力 `array`

最佳泵气平均有效压力查找表 *ƒpmep* 是发动机转速和喷射燃油质量的函数，*PMEP = ƒpmep(F,N)*，其中：

- *PMEP* 是最佳泵气平均有效压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 是发动机转速，单位为 rpm。

最佳泵气平均有效压力相对于进气歧管气体压力比与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_pmep` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Friction multiplier as a function of temperature, f\_tqs\_fric\_temp\_mod** — 摩擦乘数 `array`

摩擦乘数作为温度的函数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fric_temp_mod` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Friction multiplier temperature breakpoints, f\_tqs\_fric\_temp\_bpt** — 断点 `vector`

摩擦乘数温度断点，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fric_temp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Main start of injection timing efficiency multiplier, f\_tqs\_mainsoi\_eff** — MAINSOI 效率乘数 `array`

主喷射开始（SOI）正时效率乘数查找表 *ƒSOIeff* 是发动机转速和主 SOI 正时相对于最佳正时的函数，*SOIeff = ƒSOIeff(ΔSOI,N)*，其中：

- *SOIeff* 是主 SOI 正时效率乘数，无量纲。
- *ΔSOI* 是主 SOI 正时相对于最佳正时，单位为 degBTDC。
- *N* 是发动机转速，单位为 rpm。

SOI 正时效率乘数相对于主 SOI 正时与最佳正时之差和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mainsoi_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **Main start of injection timing relative to optimal timing breakpoints, f\_tqs\_mainsoi\_delta\_bpt** — 断点 `vector`

主喷射开始正时相对于最佳正时的断点，单位为 degBTDC。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mainsoi_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **进气歧管气体压力效率乘数，f\_tqs\_map\_eff** — 进气压力效率乘数 `array`

进气歧管气体压力效率乘数查找表，*ƒMAPeff*，是进气歧管气体压力比相对于最优压力比和 lambda 的函数，*MAPeff = ƒMAPeff(MAPratio,λ)*，其中：

- *MAPeff* 是进气歧管气体压力效率乘数，无量纲。
- *MAPratio* 是进气歧管气体压力比相对于最优压力比，无量纲。
- *λ* 是进气歧管气体 lambda，无量纲。

进气歧管气体压力效率乘数相对于进气歧管气体压力比（相对于最优压力比）和进气歧管气体 lambda 的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_map_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体压力比相对于最优压力比断点，f\_tqs\_map\_ratio\_bpt** — 断点 `[0.8;0.85;0.9;0.95;1;1.05;1.1;1.15;1.2;1.25;1.3;1.35;1.4;1.45;1.5]`（默认） | `vector`

进气歧管气体压力比相对于最优压力比断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_map_ratio_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体 lambda 断点，f\_tqs\_lambda\_bpt** — 断点 `[1.5 1.678571428571429 1.857142857142857 2.035714285714286 2.214285714285714 2.392857142857143 2.571428571428571 2.75 2.928571428571429 3.107142857142857 3.285714285714286 3.464285714285714 3.642857142857143 3.821428571428572 4]`（默认） | `vector`

进气歧管气体 lambda 断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_lambda_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体温度效率乘数，f\_tqs\_mat\_eff** — 进气温度效率乘数 `array`

进气歧管气体温度效率乘数查找表，*ƒMATeff*，是发动机转速和进气歧管气体温度相对于最优温度的函数，*MATeff = ƒMATeff(ΔMAT,N)*，其中：

- *MATeff* 是进气歧管气体温度效率乘数，无量纲。
- *ΔMAT* 是进气歧管气体温度相对于最优温度，单位为 K。
- *N* 是发动机转速，单位为 rpm。

进气歧管气体温度效率乘数相对于进气气体氧百分比（相对于最优值）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mat_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体温度相对于最佳气体温度的断点，f\_tqs\_mat\_delta\_bpt** — 断点 `[-55;-50;-45;-40;-35;-30;-25;-20;-15;-10;-5;0;5;10;15]`（默认）| `vector`

进气歧管气体温度相对于最佳气体温度的断点，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mat_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体氧气效率乘数，f\_tqs\_o2pct\_eff** — 进气氧气效率乘数 `array`

进气歧管气体氧气效率乘数查找表 *ƒO2Peff* 是发动机转速和进气歧管气体氧气百分比相对于最佳的值的函数，*O2Peff = ƒO2Peff(ΔO2P,N)*，其中：

- *O2Peff* 是进气歧管气体氧气效率乘数，无量纲。
- *ΔO2P* 是进气气体氧气百分比相对于最佳的值，单位为百分比。
- *N* 是发动机转速，单位为 rpm。

最佳进气歧管气体氧气效率乘数相对于进气气体氧气百分比相对于最佳的值和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气气体氧气百分比相对于最佳的断点，f\_tqs\_o2pct\_delta\_bpt** — 断点 `vector`

进气气体氧气百分比相对于最佳的断点，单位为百分比。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **燃油轨压力效率乘数，f\_tqs\_fuelpress\_eff** — 效率乘数 `array`

燃油轨压力效率乘数查找表 *ƒFUELPeff* 是发动机转速和燃油轨压力相对于最佳值的断点的函数，*FUELPeff = ƒFUELPeff(ΔFUELP,N)*，其中：

- *FUELPeff* 是燃油轨压力效率乘数，无量纲。
- *ΔFUELP* 是燃油轨压力相对于最佳的值，单位为 MPa。
- *N* 是发动机转速，单位为 rpm。

燃油轨压力效率乘数相对于燃油轨压力相对于最佳的值和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **燃油轨压力相对于最佳的断点，f\_tqs\_fuelpress\_delta\_bpt** — 断点 `vector`

燃油轨压力相对于最佳的断点，单位为 MPa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **燃油质量喷射类型标识符，f\_tqs\_f\_inj\_type** — 类型标识符 `0`（默认）| `scalar`

燃油质量喷射类型标识符，无量纲。

在 CI Core Engine 和 CI Controller 模块中，您可以通过模型的正时喷射开始（SOI）和燃油质量输入来表示多次喷射。要指定喷射类型，请使用 **Fuel mass injection type identifier** 参数。

| 喷射类型 | 参数值 |
| --- | --- |
| Pilot | `0` |
| Main | `1` |
| Post | `2` |
| Passed | `3` |

模型将 `Passed` 燃油喷射以及晚于阈值喷射的燃油视为未燃烧燃油。使用 **Maximum start of injection angle for burned fuel, f\_tqs\_f\_burned\_soi\_limit** 参数来指定阈值。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_f_inj_type` |
| **值**：| `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **指示平均有效压力后喷射修正，f\_tqs\_imep\_post\_corr** — 后喷射修正 `array`

指示平均有效压力后喷射修正查找表，*ƒIMEPpost*，是发动机转速和燃油轨压力相对于最优断点的函数，*ΔIMEPpost = ƒIMEPpost(ΔSOIpost,Fpost)*，其中：

- *ΔIMEPpost* 是指示平均有效压力后喷射修正，单位为 Pa。
- *ΔSOIpost* 是指示平均有效压力后喷射开始正时质心，单位为 degATDC。
- *Fpost* 是指示平均有效压力后喷射质量总和，单位为 mg per injection。

指示平均有效压力与压力后喷射开始正时和压力后喷射质量总和的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_imep_post_corr` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **指示平均有效压力后喷射质量总和断点，f\_tqs\_f\_post\_sum\_bpt** — 断点 `[0 3.571428571428572 7.142857142857143 10.71428571428571 14.28571428571429 17.85714285714286 21.42857142857143 25 28.57142857142857 32.14285714285715 35.71428571428572 39.28571428571428 42.85714285714285 46.42857142857143 50]`（默认）| `vector`

指示平均有效压力后喷射质量总和断点，单位为 mg per injection。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_f_post_sum_bpt` |
| **值**：| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择 `Torque Structure`。

### **指示平均有效压力后喷射开始正时质心断点，f\_tqs\_soi\_post\_cent\_bpt** — 断点 `[150 160.7142857142857 171.4285714285714 182.1428571428571 192.8571428571429 203.5714285714286 214.2857142857143 225 235.7142857142857 246.4285714285714 257.1428571428571 267.8571428571429 278.5714285714286 289.2857142857143 300]`（默认）| `vector`

指示平均有效压力后喷射开始正时质心断点，单位为 degATDC。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_soi_post_cent_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择
`Torque Structure`。

### **已燃烧燃料的最大喷射开始角，f\_tqs\_f\_burned\_soi\_limit** — 已燃烧燃料的最大 SOI 角 `500`（默认）| `scalar`

已燃烧燃料的最大喷射开始角，单位为 degATDC。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_bpt` |
| **值：** | `500`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择
`Torque Structure`。

#### 排气

### **排气定压比热，cp\_exh** — 比热 `1005`（默认）| `scalar`

排气比热，Cpexh，单位为 J/(kg·K)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp_exh` |
| **值：** | `1005`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 排气温度 - 简单扭矩查找

### **排气温度表，f\_t\_exh** — 查找表 `array`

排气温度的查找表是喷射燃料质量和发动机转速的
函数

Texh=fTexh(F,N)

其中：

- Texh 是
  排气温度，单位为 K。
- *F* 是喷射燃料质量，单位为 mg
  每次喷射。
- *N* 是发动机转速，单位为 rpm。

排气温度与发动机转速和发动机扭矩的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择
`Simple Torque Lookup`。

### **每次喷射燃料质量断点，f\_t\_exh\_f\_bpt** — 断点 `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]`（默认）| `vector`

用于排气温度查找表的发动机负荷断点，单位为 mg 每次
喷射。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_f_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择
`Simple Torque Lookup`。

### **转速断点，f\_t\_exh\_n\_bpt** — 断点 `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]`（默认）| `vector`

用于排气温度查找表的发动机转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择
`Simple Torque Lookup`。

#### 排气温度 - 扭矩结构

### **Optimal exhaust manifold gas temperature, f\_tqs\_exht** — 最优排气歧管气体温度 `array`

最优排气歧管气体温度查找表，
*ƒTexh*，是发动机转速
engine speed 和喷射燃油质量的函数，*Texhopt =
ƒTexh(F,N)*，其中：

- *Texhopt* 是最优排气歧管气体
  温度，单位为 K。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per
  injection。
- *N* 是发动机转速，单位为 rpm。

最优排气歧管气体温度与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择
`Torque Structure`。

### **Main start of injection timing exhaust temperature efficiency multiplier, f\_tqs\_exht\_mainsoi\_eff** — 主 SOI 正时效率乘数 `array`

主喷射开始 (SOI) 正时排气温度
效率乘数查找表，*ƒSOIexhteff*，是
发动机转速 engine speed 和喷射燃油质量的函数，
*SOIexhteff =
ƒSOIexhteff(ΔSOI,N)*，其中：

- *SOIexhteff* 是主 SOI 排气
  温度效率乘数，无量纲。
- *ΔSOI* 是主 SOI 正时相对于最优正时，单位为
  degBTDC。
- *N* 是发动机转速，单位为 rpm。

SOI 排气温度效率乘数与主 SOI 正时相对于最优正时和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_mainsoi_eff` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择
`Torque Structure`。

### **Intake manifold gas pressure exhaust temperature efficiency multiplier, f\_tqs\_exht\_map\_eff** — 进气歧管效率乘数 `array`

进气歧管气体压力排气温度效率
乘数查找表，*ƒMAPexheff*，是
进气歧管气体压力比相对于最优压力比和 lambda 的函数，
*MAPexheff =
ƒMAPexheff(MAPratio,λ)*，其中：

- *MAPexheff* 是进气歧管气体
  压力排气温度效率乘数，无量纲。
- *MAPratio* 是进气歧管气体压力
  比相对于最优压力比，无量纲。
- *λ* 是进气歧管气体 lambda，无量纲。

进气歧管气体压力排气温度效率乘数与进气歧管气体压力比相对于最优压力比和进气歧管气体 lambda 的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_map_eff` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请为 **Torque model** 选择
`Torque Structure`。

### **进气歧管气体温度排气温度效率乘数，f\_tqs\_exht\_mat\_eff** — 进气歧管效率乘数 `array`

进气歧管气体温度排气温度效率乘数查找表，*ƒMATexheff*，是发动机转速和进气歧管气体温度相对于最优温度的函数，*MATexheff = ƒMATexheff(ΔMAT,N)*，其中：

- *MATexheff* 是进气歧管气体温度排气温度效率乘数，无量纲。
- *ΔMAT* 是进气歧管气体温度相对于最优温度，单位为 K。
- *N* 是发动机转速，单位为 rpm。

进气歧管气体温度排气温度效率乘数相对于进气歧管气体温度相对于最优温度和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_mat_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **进气歧管气体氧气排气温度效率乘数，f\_tqs\_exht\_o2pct\_eff** — 进气歧管效率乘数 `array`

进气歧管气体氧气排气温度效率乘数查找表，*ƒO2Pexheff*，是发动机转速和进气歧管气体氧气百分比相对于最优值的函数，*O2Pexheff = ƒO2Pexheff(ΔO2P,N)*，其中：

- *O2Pexheff* 是进气歧管气体氧气排气温度效率乘数，无量纲。
- *ΔO2P* 是进气气体氧气百分比相对于最优值，单位为百分比。
- *N* 是发动机转速，单位为 rpm。

最优进气歧管气体氧气排气温度效率乘数相对于进气气体氧气百分比相对于最优值和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_o2pct_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **燃油轨压力排气温度效率乘数，f\_tqs\_exht\_fuelpress\_eff** — 燃油轨压力排气温度效率乘数 `array`

燃油轨压力效率排气温度乘数查找表，*ƒFUELPexheff*，是发动机转速和燃油轨压力相对于最优断点的函数，*FUELPexheff = ƒFUELPexheff(ΔFUELP,N)*，其中：

- *FUELPexheff* 是燃油轨压力排气温度效率乘数，无量纲。
- *ΔFUELP* 是燃油轨压力相对于最优值，单位为 MPa。
- *N* 是发动机转速，单位为 rpm。

燃油轨压力排气温度效率乘数相对于燃油轨压力相对于最优值和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_fuelpress_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **后喷气缸壁热损失传递系数，f\_tqs\_exht\_post\_inj\_wall\_htc** — 后喷偏移 `0`（默认） | `scalar`

后喷气缸壁热损失传递系数，单位为 W/K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_post_inj_wall_htc` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择
`Torque Structure`。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

包含空气质量流量、扭矩和 EGR 估计的压燃式控制器

CI Controller 模块实现了一个压燃式（CI）控制器，具有
空气质量流量、扭矩、废气再循环（EGR）流量、排气背压和
排气温度估计功能。您可以在发动机控制设计或性能、燃油经济性和排放权衡研究中使用 CI Controller 模块。
核心发动机模块需要 CI
Controller 模块输出的命令。

该模块使用指令扭矩和测量的发动机转速
来确定以下开环执行器命令：

- 喷油器脉冲宽度
- 燃油喷射正时
- 可变几何涡轮增压器（VGT）齿条位置
- EGR 阀面积百分比

CI Controller 模块有两个子系统：

- `Controller` 子系统 —
  基于作为指令扭矩和测量发动机转速函数的表格
  确定命令。

  | 基于 | 确定以下命令 |
  | --- | --- |
  | 指令扭矩  测量的发动机转速 | 喷油器脉冲宽度  燃油喷射正时  VGT 齿条位置  EGR 阀面积百分比 |
- `Estimator` 子系统 —
  基于这些发动机属性确定估计值。

  | 基于 | 估计 |
  | --- | --- |
  | 测量的发动机转速  燃油喷射正时  循环平均进气歧管压力和温度  燃油喷射器脉冲宽度  绝对环境压力  EGR 阀面积百分比  VGT 齿条位置  VGT 转速 | 空气质量流量  扭矩  排气温度  排气背压  EGR 阀气体质量流量 |

该图展示了信号流。

CI Controller 模块连接，显示燃烧和流体流动

该图使用了这些变量。

|  |  |
| --- | --- |
| *N* | 发动机转速 |
| *MAP* | 循环平均进气歧管绝对压力 |
| *MAT* | 循环平均进气歧管气体绝对温度 |
| *EGRap*、*EGRcmd* | 分别为 EGR 阀面积百分比和 EGR 阀面积百分比命令 |
| *VGTpos* | VGT 齿条位置 |
| *Nvgt* | 校正后的涡轮增压器转速 |
| *RPcmd* | VGT 齿条位置命令 |
| Pwinj | 燃油喷射器脉冲宽度 |
| *MAINSOI* | 主燃油喷射脉冲的喷射开始正时 |

Model-Based Calibration Toolbox™ 用于开发
Powertrain Blockset™ 中可用的表格。

### Controller

控制器通过指令 VGT 齿条位置、EGR 阀面积百分比、燃油喷射正时和喷油器脉冲宽度来控制燃烧过程。前馈查找表是测量的发动机转速和指令扭矩的函数，用于确定控制指令。

**Air**

控制器指令 EGR 阀面积百分比和 VGT 齿条位置。改变 VGT 齿条位置会改变涡轮流量特性。在低请求扭矩下，齿条位置可以降低排气背压，从而导致较低的涡轮增压器转速和增压压力。当指令燃油需要额外的空气质量流量时，齿条位置被设置为关闭涡轮增压器叶片，从而增加涡轮增压器转速和进气歧管增压压力。

可变几何涡轮增压器 (VGT) 齿条位置查找表是指令扭矩和发动机转速的函数

RPcmd=fRPcmd(Trqcmd,N)

其中：

- *RPcmd* 是 VGT 齿条位置指令，以百分比表示。
- *Trqcmd* 是指令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

齿条位置与指令扭矩和发动机转速的 3D 图

指令废气再循环 (EGR) 阀面积百分比查找表是指令扭矩和发动机转速的函数

EGRcmd=fEGRcmd(Trqcmd,N)

其中：

- *EGRcmd* 是指令 EGR 阀面积百分比，以百分比表示。
- *Trqcmd* 是指令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

指令 EGR 阀面积百分比与指令扭矩和发动机转速的 3D 图

**Fuel**

为启动燃烧，CI 发动机将燃油直接喷入燃烧室。喷射后，燃油自燃，增加气缸压力。喷射燃油的总质量和主喷射正时决定扭矩产生。

假设燃油轨压力恒定，CI 控制器基于总请求燃油质量指令喷油器脉冲宽度：

Pwinj=Fcmd, totSinj

该方程使用这些变量。

|  |  |
| --- | --- |
| Pwinj | 燃油喷油器脉冲宽度 |
| *Sinj* | 燃油喷油器斜率 |
| *Fcmd,tot* | 每次喷射的指令总燃油质量 |
| *MAINSOI* | 主喷射开始正时 |
| *N* | 发动机转速 |

每次喷射的指令总燃油质量表是扭矩指令和发动机转速的函数

Fcmd,tot=fFcmd,tot(Trqcmd,N)

其中：

- *Fcmd,tot* = *F* 是每次喷射的指令总燃油质量，单位为 mg/cylinder。
- *Trqcmd* 是指令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

每次喷射的指令总燃油质量与指令扭矩和发动机转速的 3D 图

主喷射开始 (SOI) 正时查找表是指令燃油质量和发动机转速的函数

MAINSOI=f(Fcmd,tot,N)

其中：

- *MAINSOI* 是主喷射开始正时，单位为上止点后曲轴转角 (degATDC)。
- *Fcmd,tot* = *F* 是指令燃油质量，单位为 mg/injection。
- *N* 是发动机转速，单位为 rpm。

主喷射开始正时与指令燃油质量和发动机转速的 3D 图

**Idle Speed**

当指令扭矩低于阈值时，怠速控制器调节发动机转速。

| If | Idle Speed Controller |
| --- | --- |
| *Trqcmd,input* < *Trqidlecmd,enable* | Enabled |
| *Trqidlecmd,enable* ≤ *Trqcmd,input* | 未启用 |

怠速控制器使用离散 PI 控制器通过指令扭矩来调节目标怠速。

PI 控制器使用此传递函数：

Cidle(z)=Kp,idle+Ki,idletsz−1

怠速指令扭矩必须小于最大指令扭矩：

0 ≤ *Trqidlecomd* ≤*Trqidlecmd,max*

怠速控制在这些条件下激活。如果指令输入扭矩降至启用怠速控制器的阈值以下 (*Trqcmd,input* < *Trqidlecmd,enable*)，则指令发动机扭矩由下式给出：

*Trqcmd* = max(*Trqcmd,input*,*Trqidlecmd*)。

这些方程使用这些变量。

|  |  |
| --- | --- |
| *Trqcmd* | 指令发动机扭矩 |
| *Trqcmd,input* | 输入指令发动机扭矩 |
| *Trqidlecmd,enable* | 启用怠速控制器的阈值 |
| *Trqidlecmd* | 怠速控制器指令扭矩 |
| *Trqidlecmd,max* | 最大指令扭矩 |
| *Nidle* | 基础怠速转速 |
| *Kp,idle* | 怠速控制器比例增益 |
| *Ki,idle* | 怠速控制器积分增益 |

**转速限制器**

为防止发动机超速运转，该模块实现了一个发动机转速限制控制器，将发动机转速限制为 **Controls** > **Idle Speed** 选项卡上 **Rev-limiter speed threshold** 参数指定的值。

如果发动机转速 *N* 超过发动机转速限制 *Nlim*，该模块将指令发动机扭矩设置为 0。

为了在发动机转速接近转速限制时平滑地将扭矩指令过渡到 0，该模块实现了一个查找表乘数。该查找表将扭矩指令乘以一个从 0（发动机转速超过限制）到 1（发动机转速未超过限制）的值。

### Estimator

使用 CI Core Engine 模块，CI Controller 模块根据传感器反馈估计空气质量流量、EGR 阀质量流量、排气背压、发动机扭矩、AFR 和排气温度。`Info` 端口提供估计值，但模块不使用这些值来确定开环发动机执行器命令。

**空气质量流量**

为了计算空气质量流量，压燃式（CI）发动机使用 CI Engine Speed-Density Air Mass Flow Model。速度-密度模型使用速度-密度方程来计算发动机空气质量流量，将发动机进气口质量流量与进气歧管压力、进气歧管温度和发动机转速相关联。

**EGR 阀质量流量**

为了计算估计的废气再循环（EGR）阀质量流量，模块计算在标准温度和压力条件下会发生的 EGR 流量，然后将该流量校正到实际温度和压力条件。模块的 EGR 计算使用估计的排气背压、估计的排气温度、标准温度和标准压力。

m˙egr,est=m˙egr,stdPexh,estPstdTstdTexh,est

- 标准废气再循环（EGR）质量流量是一个查找表，它是标准流量压力比和 EGR 阀流通面积的函数

  m˙egr,std=f(MAPPexh,est,EGRap)

  其中：

  - m˙egr,std 是标准 EGR 阀质量流量，单位为 g/s。
  - *Pexh,est* 是估计的排气背压，单位为 Pa。
  - *MAP* 是循环平均进气歧管绝对压力，单位为 Pa。
  - *EGRap* 是测得的 EGR 阀面积，单位为百分比。

  标准 EGR 阀质量流量与循环平均进气歧管绝对压力和测得 EGR 阀面积的 3D 图

这些方程使用以下变量。

|  |  |
| --- | --- |
| m˙egr,est | 估计的 EGR 阀质量流量 |
| m˙egr,std | 标准 EGR 阀质量流量 |
| Pstd | 标准压力 |
| Tstd | 标准温度 |
| *Texh,est* | 估计的排气歧管气体温度 |
| *MAP* | 测得的循环平均进气歧管绝对压力 |
| *Pexh,est* | 估计的排气背压 |
| PAmb | 绝对环境压力 |
| *EGRap* | 测得的 EGR 阀面积百分比 |

**排气背压**

为了估计 EGR 阀质量流量，模块需要排气背压的估计值。为了估计排气背压，模块使用环境压力和涡轮增压器压力比。

Pexh,est=PAmbPrturbo

对于涡轮增压器压力比计算，模块使用两个查找表。第一个查找表根据涡轮增压器质量流量和校正后的涡轮增压器转速确定近似涡轮增压器压力比。使用第二个查找表，模块根据 VGT 齿条位置校正近似涡轮增压器压力比。

Prturbo=f(m˙airstd,Nvgtcorr)f(VGTpos)其中：Nvgtcorr=NvgtTexh,est

这些方程使用以下变量。

|  |  |
| --- | --- |
| m˙egr,est | 估计的 EGR 阀质量流量 |
| m˙egr,std | 标准 EGR 阀质量流量 |
| m˙port,est | 估计的进气口质量流量 |
| m˙airstd | 标准空气质量流量 |
| *EGRap* | 测得的 EGR 阀面积 |
| *MAP* | 测得的循环平均进气歧管绝对压力 |
| *MAT* | 测得的循环平均进气歧管气体绝对温度 |
| Pstd | 标准压力 |
| Tstd | 标准温度 |
| *Texh,est* | 估计的排气歧管气体温度 |
| *Prvgtcorr* | 针对 VGT 齿条位置的涡轮增压器压力比校正 |
| *Prturbo* | 涡轮增压器压力比 |
| *Pexh,est* | 估计的排气背压 |
| PAmb | 绝对环境压力 |
| *Nvgtcorr* | 校正后的涡轮增压器转速 |
| *VGTpos* | 测得的 VGT 齿条位置 |

排气背压计算使用以下查找表：

- 涡轮增压器压力比，针对可变几何涡轮增压器（VGT）转速进行修正，是一个查找表，它是标准空气质量流量和修正后涡轮增压器转速的函数，Prturbo=f(m˙airstd,Nvgtcorr)，其中：

  - *Prturbo* 是针对 VGT 转速修正后的涡轮增压器压力比。
  - m˙airstd 是标准空气质量流量，单位为 g/s。
  - *Nvgtcorr* 是修正后的涡轮增压器转速，单位为 rpm/K^(1/2)。

  涡轮增压器压力比与标准空气质量流量和修正后涡轮增压器转速的 3D 图

  为了计算通过涡轮增压器的标准空气质量流量，该模块使用质量守恒、估计的进气端口以及 EGR 质量流量（来自上一次估计计算）。该计算假设排气歧管填充动态可忽略。

  m˙airstd=(m˙port,est−m˙egr,est)PstdMAPMATTstd
- 可变几何涡轮增压器压力比修正是齿条位置的函数，*Prvgtcorr*= ƒ(*VGTpos*)，其中：

  - *Prvgtcorr* 是涡轮增压器压力比修正。
  - *VGTpos* 是可变几何涡轮增压器（VGT）齿条位置。

  涡轮增压器压力比修正与可变几何涡轮增压器（VGT）齿条位置的关系图

**发动机扭矩**

为了计算发动机扭矩，您可以将该模块配置为使用以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| CI 发动机扭矩结构模型 | CI 核心发动机扭矩结构模型通过在这些发动机条件偏离标称值时降低最大发动机扭矩潜力来确定发动机扭矩：  - 喷油开始（SOI）正时 - 排气背压 - 已燃烧燃料质量 - 进气歧管气体压力、温度和氧气百分比 - 燃油轨压力  为了考虑后喷燃油对扭矩的影响，该模型使用标定的扭矩偏移表。 |
| CI 发动机简单扭矩模型 | 对于简单发动机扭矩计算，CI 发动机使用作为发动机转速和喷射燃料质量函数的扭矩查找表映射。 |

**排气温度**

排气温度计算取决于扭矩模型。对于这两种扭矩模型，该模块都实现为查找表。

| 扭矩模型 | 描述 | 方程 |
| --- | --- | --- |
| `Simple Torque Lookup` | 排气温度查找表是喷射燃料质量和发动机转速的函数。 | Texh=fTexh(F,N) |
| `Torque Structure` | 标称排气温度 *Texhnom* 是以下排气温度效率的乘积：  - SOI 正时 - 进气歧管气体压力 - 进气歧管气体温度 - 进气歧管气体氧气百分比 - 燃油轨压力 - 最佳温度  排气温度 *Texhnom* 由后温度效应 *ΔTpost* 偏移，该效应考虑了膨胀和排气冲程期间的后喷和晚喷。 | Texhnom=SOIexhteffMAPexhteffMATexhteffO2pexhteffFUELPexhteffTexhoptTexh=Texhnom+ΔTpostSOIexhteff=fSOIexhteff(ΔSOI,N)MAPexhteff=fMAPexhteff(MAPratio,λ)MATexhteff=fMATexhteff(ΔMAT,N)O2pexhteff=fO2pexhteff(ΔO2p,N)Texhopt=fTexh(F,N) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *F* | 压缩冲程喷射燃油质量 |
| *N* | 发动机转速 |
| *Texh* | 排气歧管气体温度 |
| *Texhopt* | 最佳排气歧管气体温度 |
| *ΔTpost* | 后喷射温度效应 |
| *Texhnom* | 标称排气温度 |
| *SOIexhteff* | 主SOI排气温度效率乘数 |
| *ΔSOI* | 主SOI正时相对于最佳正时 |
| *MAPexheff* | 进气歧管气体压力排气温度效率乘数 |
| *MAPratio* | 进气歧管气体压力比相对于最佳压力比 |
| *λ* | 进气歧管气体lambda |
| *MATexheff* | 进气歧管气体温度排气温度效率乘数 |
| *ΔMAT* | 进气歧管气体温度相对于最佳温度 |
| *O2Pexheff* | 进气歧管气体氧气排气温度效率乘数 |
| *ΔO2P* | 进气气体氧气百分比相对于最佳值 |
| *FUELPexheff* | 燃油轨压力排气温度效率乘数 |
| *ΔFUELP* | 燃油轨压力相对于最佳值 |

**空燃比**

测得的发动机转速和喷油器脉冲宽度决定指令燃油质量流量：

m˙fuel,cmd=NSinjPwinjNcylCps(60smin)(1000mgg)

指令总燃油质量流量和估计的进气口质量流量决定估计的AFR：

AFRest=m˙port,estm˙fuel,cmd

这些方程使用以下变量。

|  |  |
| --- | --- |
| Pwinj | 喷油器脉冲宽度 |
| *AFRest* | 估计空燃比 |
| m˙fuel,cmd | 指令燃油质量流量 |
| Sinj | 喷油器斜率 |
| *N* | 发动机转速 |
| *Ncyl* | 发动机气缸数 |
| *Cps* | 每动力冲程的曲轴转数，rev/stroke |
| m˙port,est | 进气口处总估计发动机空气质量流量 |
