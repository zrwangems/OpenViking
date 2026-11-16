---
type: simulink-block
title: 'Equivalent Consumption Minimization Strategy'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Supervisory Controllers'
documentation_page: 'equivalentconsumptionminimizationstrategy'
documentation_source_path: 'ref/equivalentconsumptionminimizationstrategy.html'
language: zh-CN
chinese_source: worker-translation
---

# Equivalent Consumption Minimization Strategy

## 端口

### 输入

### **WhlTrqCmd** — 车轮扭矩命令 `scalar`

车轮扭矩命令。

**数据类型：** `double`

### **BattSoc** — 电池荷电状态 `scalar`

电池荷电状态。

**数据类型：** `double`

### **BattVolt** — 电池电压 `scalar`

电池电压。

**数据类型：** `double`

### **Gear** — 变速器挡位 `scalar`

变速器挡位。

**数据类型：** `double`

### **MtrSpd** — 电机转速 `scalar`

电机转速。

**数据类型：** `double`

### **VehSpd** — 车速 `scalar`

车速，单位为 m/s。

**数据类型：** `double`

### **TransTemp** — 变速器温度 `scalar`

变速器温度，单位为 K。

**数据类型：** `double`

### 输出

### **Info** — 模块数据总线

模块数据，以总线信号形式返回，其中包含以下模块值。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `EngTrqCmd` | | | 发动机扭矩命令 | N·m |
| `MtrTrqCmd` | | | 电机扭矩命令 | N·m |
| `EquivFctr` | | | 等效因子 | NA |
| `MinHamil` | | | 最小哈密顿量 | kW |

### **EngTrqCmd** — 发动机扭矩命令 `scalar`

发动机扭矩命令，单位为 N·m。

**数据类型：** `double`

### **MtrTrqCmd** — 电机扭矩命令 `scalar`

电机扭矩命令，单位为 N·m。

**数据类型：** `double`

## 参数

#### 模块选项

### **Motor location** — 电机位置 `P0`（默认） | `P1` | `P2` | `P3` | `P4`

指定 HEV 电机位置。

### **ECMS method** — ECMS 方法 `Non-adaptive`（默认） | `Adaptive`

使用 **ECMS method** 参数来实现自适应或非自适应 ECMS 方法。HEV 架构是电量维持型，这意味着电池 SOC 必须保持在一个指定范围内，因为没有插电充电能力来为电池充电。电池是一个能量缓冲器，如果在驾驶循环中 SOC 变化最小化，则所有能量都来自燃料。为了在指定驾驶循环中维持电量，模块实现以下任一 ECMS 方法。

| ECMS 方法 | 描述 |
| --- | --- |
| `Non-adaptive`（默认） | 模块使用恒定的 ECMS 等效因子。  - 使用此方法确定驾驶循环中的最佳燃油经济性。  - 如果更改驾驶循环或 HEV 架构，请重新调整 **ECMS weighting factor** 以维持结束 SOC。 - 默认情况下，模块使用单个常量。 |
| `Adaptive` | 模块通过使用 PI 控制器的输出调整 ECMS 等效因子。  - 使用此方法在多个驾驶循环中维持 SOC 并最小化 SOC 变化量。模块：  - 调整 PI 控制器增益。   - 维持 SOC。 - PI 控制器最小化目标 SOC 与当前 SOC 之间的误差。 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EcmsMethod` |
| **值：** | `Non-adaptive`（默认） | `Adaptive` |
| **数据类型：** | `character vector` |

#### 差速器

### **Differential gear ratio, N\_diff** — 差速器传动比 `3.32`（默认） | `scalar`

差速器传动比。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_diff` |
| **值：** | `3.32`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Differential efficiency factor, eta\_diff** — 差速器效率因子 `0.98`（默认） | `scalar`

差速器效率因子。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_diff` |
| **值：** | `0.98`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Loaded wheel radius, Re** — 承载车轮半径 `0.327`（默认） | `scalar`

承载车轮半径，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Re` |
| **值：** | `0.327`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 变速器

### **Transmission efficiency factors** — 变速器效率因子 `Gear, input torque, input speed, and temperature`（默认） | `Gear only`

变速器效率因子。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TransEffFactors` |
| **值：** | `Gear, input torque, input speed, and temperature`（默认） | `Gear only` |
| **数据类型：** | `character vector` |

### **Transmission gear number vector, G\_trans** — 变速器挡位编号向量 `[0 1 2 3 4 5 6]`（默认） | `vector`

变速器挡位编号向量。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `G_trans` |
| **值：** | `[0 1 2 3 4 5 6]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Transmission gear ratio vector, N\_trans** — 变速器传动比向量 `[1 4.212 2.637 1.8 1.386 1 0.772]`（默认） | `vector`

变速器传动比向量。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_trans` |
| **值：** | `[1 4.212 2.637 1.8 1.386 1 0.772]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Transmission efficiency vector, eta\_trans** — 变速器效率向量 `[1 1 1 1 1 1 1]`（默认） | `vector`

变速器效率向量。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_trans` |
| **值：** | `[1 1 1 1 1 1 1]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Transmission efficiency factors** 设置为 `Gear only`。

### **Transmission efficiency torque breakpoints, Trq\_trans\_bpts** — 变速器效率扭矩断点 `[25 50 75 100 150 200 250]`（默认） | `vector`

变速器效率扭矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_trans_bpts` |
| **值：** | `[25 50 75 100 150 200 250]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Transmission efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Transmission efficiency speed breakpoints, omega\_trans\_bpts** — 变速器效率转速断点 `[500.383141080919 749.619781962827 1002.676141478941 1250.957852702297 1499.239563925654 1747.521275149011 1995.802986372368 2501.915705404595 2998.479127851308 4001.155269330249 5003.83141080919]`（默认） | `vector`

变速器效率转速断点，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_trans_bpts` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Transmission efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Transmission efficiency temperature breakpoints, Temp\_trans\_bpts** — 变速器效率温度断点 `[313 358]`（默认） | `vector`

变速器效率温度断点，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_trans_bpts` |
| **值：** | `[313 358]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Transmission efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Transmission efficiency vector, eta\_trans\_tbl** — 变速器效率向量 `array`

变速器效率向量。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_trans_tbl` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Transmission efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

#### 发动机

### **Speed breakpoints, f\_tbrake\_n\_bpt** — 转速断点 `[0 750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认） | `vector`

转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Commanded torque breakpoints, f\_tbrake\_t\_bpt** — 指令扭矩断点 `[0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286 95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175]`（默认） | `vector`

指令扭矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_t_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Brake torque map, f\_tbrake** — 制动扭矩映射 `array`

制动扭矩映射，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Minimum engine torque command table, f\_tbrake\_min** — 最小发动机扭矩命令表 `vector`

最小发动机扭矩命令表，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_min` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Fuel flow map, f\_fuel** — 燃料流量映射 `array`

燃料流量映射，单位为 kg/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_fuel` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Minimum engine torque command, HEVEngTrq\_min** — 最小发动机扭矩命令 `16.18610438796213`（默认） | `scalar`

最小发动机扭矩命令，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `HEVEngTrq_min` |
| **值：** | `16.18610438796213`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Fuel lower heating value, LHV** — 燃料低热值 `46000000`（默认） | `scalar`

燃料低热值，单位为 J/kg。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LHV` |
| **值：** | `46000000`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Engine idle speed, N\_idle** — 发动机怠速转速 `750`（默认） | `scalar`

发动机怠速转速，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_idle` |
| **值：** | `750`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 电池

### **Battery state-of-charge breakpoints, SOC\_bpt** — 电池荷电状态断点 `[0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1]`（默认） | `vector`

电池荷电状态断点。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SOC_bpt` |
| **值：** | `[0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Battery charge limit table, ChrgLmt** — 电池充电限制表 `[1 1 1 1 1 1 1 0.9 0.7 0.5 0]`（默认） | `vector`

电池充电限制表。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ChrgLmt` |
| **值：** | `[1 1 1 1 1 1 1 0.9 0.7 0.5 0]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Battery discharge limit table, DischrgLmt** — 电池放电限制表 `[0 0.5 0.7 0.9 1 1 1 1 1 1 1]`（默认） | `vector`

电池放电限制表。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DischrgLmt` |
| **值：** | `[0 0.5 0.7 0.9 1 1 1 1 1 1 1]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Maximum battery current, BattCurrMax** — 最大电池电流 `150`（默认） | `scalar`

最大电池电流，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BattCurrMax` |
| **值：** | `150`（默认） | `scalar` |
| **数据类型：** | `double` |

### **DC/DC converter efficiency, eta\_dcdc** — DC/DC 转换器效率 `1`（默认） | `scalar`

DC/DC 转换器效率。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_dcdc` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Maximum battery charge power, BattChrgPwrMax** — 最大电池充电功率 `-30000`（默认） | `scalar`

最大电池充电功率，单位为 W。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BattChrgPwrMax` |
| **值：** | `-30000`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Maximum battery discharge power, BattDischrgPwrMax** — 最大电池放电功率 `46000`（默认） | `scalar`

最大电池放电功率，单位为 W。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BattDischrgPwrMax` |
| **值：** | `46000`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 电机

### **Motor maximum torque table, f\_tmtr\_max** — 电机最大扭矩表 `vector`

电机最大扭矩表，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tmtr_max` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Motor speed breakpoints, f\_mtr\_w\_bpt** — 电机转速断点 `vector`

电机转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mtr_w_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Motor torque breakpoints, f\_mtr\_t\_bpt** — 电机扭矩断点 `vector`

电机扭矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mtr_t_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Motor efficiency map, f\_mtr\_eta** — 电机效率映射 `array`

电机效率映射。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mtr_eta` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Number of motor torque calculation points, Ngrid** — 电机扭矩计算点数 `200`（默认） | `scalar`

电机扭矩计算点数。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ngrid` |
| **值：** | `200`（默认） | `scalar` |
| **数据类型：** | `double` |

### **P0 belt ratio, N\_P0** — P0 皮带传动比 `3`（默认） | `scalar`

P0 皮带传动比。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_P0` |
| **值：** | `3`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Motor location** 设置为 `P0`。

#### 能量管理

### **ECMS weighting factor, ECMS\_s** — ECMS 加权因子 `3.385`（默认） | `scalar`

ECMS 加权因子。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ECMS_s` |
| **值：** | `3.385`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Penalty factor power, a** — 惩罚因子幂 `3`（默认） | `scalar`

惩罚因子幂。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PenaltyFctrPwr` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Adaptive ECMS proportional gain, ECMS\_Kp** — 自适应 ECMS 比例增益 `0`（默认） | `scalar`

自适应 ECMS 比例增益。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ECMS_Kp` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **ECMS method** 设置为 `Adaptive`。

### **Adaptive ECMS integral gain, ECMS\_Ki** — 自适应 ECMS 积分增益 `0`（默认） | `scalar`

自适应 ECMS 积分增益。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ECMS_Ki` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **ECMS method** 设置为 `Adaptive`。

### **Constraint penalty factor, PenaltyFctr** — 约束惩罚因子 `10000000`（默认） | `scalar`

约束惩罚因子。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PenaltyFctr` |
| **值：** | `10000000`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Target battery state-of-charge, SOCTrgt** — 目标电池荷电状态 `60`（默认） | `scalar`

目标电池荷电状态。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SOCTrgt` |
| **值：** | `60`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Minimum battery state-of-charge, SOCmin** — 最小电池荷电状态 `40`（默认） | `scalar`

最小电池荷电状态。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SOCmin` |
| **值：** | `40`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Maximum battery state-of-charge, SOCmax** — 最大电池荷电状态 `80`（默认） | `scalar`

最大电池荷电状态。无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SOCmax` |
| **值：** | `80`（默认） | `scalar` |
| **数据类型：** | `double` |

### 致谢

MathWorks® 谨感谢 Dr. Simona Onori 对本模块中实现的 ECMS 最优控制算法所作的贡献。Dr. Onori 是 Stanford University 的能源资源工程教授。她的研究兴趣包括汽车和电网级应用中的电化学建模、储能设备的估计与优化，混合动力与电动汽车建模和控制，PDE 建模，以及排放缓解系统的模型降阶和估计。她是 IEEE® 的高级会员。

## 所属库

Powertrain Blockset / Propulsion / Supervisory Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

用于 P0–P4 混合动力电动汽车的能量管理控制器

使用 Equivalent Consumption Minimization Strategy (ECMS) 模块控制混合动力电动汽车 (HEV) 的能量管理。该模块优化发动机和电机之间的扭矩分配，以在维持电池荷电状态 (SOC) 的同时最小化能量消耗。

HEV P0、P1、P2、P3 和 P4 参考应用使用 Equivalent Consumption Minimization Strategy 模块进行混合动力控制。

使用 **Motor location** 参数指定 HEV 电机位置。

使用 **ECMS method** 参数实现自适应或非自适应 ECMS 方法。HEV 架构是电量维持型，这意味着电池 SOC 必须保持在一个指定范围内，因为没有插电充电能力来为电池充电。电池是一个能量缓冲器，如果在驾驶循环中 SOC 变化最小化，则所有能量都来自燃料。为了在指定驾驶循环中维持电量，模块实现以下任一 ECMS 方法。

| ECMS 方法 | 描述 |
| --- | --- |
| `Non-adaptive`（默认） | 模块使用恒定的 ECMS 等效因子。  - 使用此方法确定驾驶循环中的最佳燃油经济性。  - 如果更改驾驶循环或 HEV 架构，请重新调整 **ECMS weighting factor** 以维持结束 SOC。 - 默认情况下，模块使用单个常量。 |
| `Adaptive` | 模块通过使用 PI 控制器的输出调整 ECMS 等效因子。  - 使用此方法在多个驾驶循环中维持 SOC 并最小化 SOC 变化量。模块：  - 调整 PI 控制器增益。   - 维持 SOC。 - PI 控制器最小化目标 SOC 与当前 SOC 之间的误差。 |

### ECMS 控制算法

该模块实现一个动态监督控制器，用于确定发动机扭矩、电机扭矩、起动机、离合器和制动压力命令。具体而言，该模块：

- 将驾驶员加速踏板信号转换为车轮扭矩请求。为了计算车轮处的总动力总成扭矩，该算法使用最大发动机扭矩和电机扭矩曲线以及变速器和差速器传动比。
- 将驾驶员制动踏板信号转换为制动压力请求。该算法将制动踏板信号乘以最大制动压力。
- 为牵引电机实现再生制动算法，以从车辆回收最大量的动能。

  该模块实现 ECMS 算法[2]，该算法优化发动机和电机之间的扭矩分配，以在维持电池 SOC 的同时最小化能量消耗。具体而言，ECMS：

  - 为电能分配成本，使得使用存储的电能等同于消耗燃料能量。

    | 电池模式 | 等效电能 | 描述 |
    | --- | --- | --- |
    | Discharging | Positive | 当电机使用时，电池放出存储的电能。 |
    | Charging | Negative | 电池存储来自以下任一来源的电能：  - 发动机和作为发电机运行的电机 - 再生制动期间作为发电机运行的电机 |

  - 是一种瞬时最小化方法，软件在每个控制器时间步求解。为实现该策略，ECMS 在优化策略中选择最优电机和发动机扭矩，以最小化等效能量消耗。
  - 实现自适应或非自适应 ECMS 方法。
