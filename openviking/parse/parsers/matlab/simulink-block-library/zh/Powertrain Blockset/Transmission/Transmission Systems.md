---
type: simulink-block
title: 'Automated Manual Transmission'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission'
documentation_page: 'automatedmanualtransmission'
documentation_source_path: 'ref/automatedmanualtransmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Automated Manual Transmission

## 端口

### 输入

### **Gear** — 要接合的挡位编号 `scalar`

要接合的挡位编号的整数值。

### **CltchCmd** — 离合器命令 `scalar`

离合器压力命令。

#### 依赖关系

要创建此端口，请选择 **Control type** 参数 `External control`。

### **EngTrq** — 施加的输入扭矩 `scalar`

施加的输入扭矩，*Ti*，通常来自发动机曲轴或双质量飞轮减振器，单位为 N·m。

### **DiffTrq** — 施加的负载扭矩 `scalar`

施加的负载扭矩，*Td*，通常来自差速器或传动轴，单位为 N·m。

### **Temp** — 油温 `scalar`

油温，单位为 K。为确定效率，该模块使用一个 4D 查找表，该查找表是以下量的函数：

- 挡位
- 输入扭矩
- 输入转速
- 油温

#### 依赖关系

要创建此端口，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。
### 输出

### **Info** — 总线信号 bus

总线信号包含以下模块计算量。

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `Eng` | `EngTrq` | | 输入施加扭矩 | *Ti* | N·m |
| `EngSpd` | | 输入驱动轴转速 | *ωi* | rad/s |
| `Diff` | `DiffTrq` | | 输出驱动轴扭矩 | *Tt* | N·m |
| `DiffSpd` | | 输出驱动轴转速 | *ωt* | rad/s |
| `Cltch` | `CltchForce` | | 施加的离合器力 | *Fc* | N |
| `CltchLocked` | | 离合器锁定状态，布尔值：  - Locked — `0` - Unlocked —   `1` | N/A | N/A |
| `Trans` | `TransSpdRatio` | | 时刻 *t* 的速比 | ϕ(t) | N/A |
| `TransEta` | | 输出功率与输入功率之比 | η | N/A |
| `TransGearCmd` | | 命令挡位 | *Ncmd* | N/A |
| `TransGear` | | 已接合挡位 | *N* | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrEng` | 发动机功率 | *Peng* | W |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | W |
| `PwrNotTrnsfrd` | `PwrEffLoss` | 机械功率损失 | *Peffloss* | W |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | W |
| `PwrCltchLoss` | 离合器功率损失 | *Pmech* | W |
| `PwrStored` | `PwrStoredTrans` | 旋转动能变化率 | *Pstr* | W |

### **EngSpd** — 角速度 `scalar`

施加的驱动轴角速度输入，*ωi*，单位为 rad/s。

### **DiffSpd** — 角速度 `scalar`

驱动轴角速度输出，*ωd*，单位为 rad/s。

## 参数

### **Control type** — 指定控制类型 `Ideal integrated controller` (default) | `External control`

AMT 通过控制来自离合器的压力信号来连续输出驱动轴扭矩。如果选择 **Control type** 参数 `Ideal integrated controller`，该模块会生成理想化的离合器压力信号。要使用您自己的离合器控制信号，请选择 **Control type** 参数 `External control`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `cntrlType` |
| **值**：| `Ideal integrated controller` (default) | `External control` |
| **Data Types:** | `character vector` |

#### 依赖关系

此表总结了端口配置。

| Control Mode | Creates Ports |
| --- | --- |
| `External control` | `CltchCmd` |

### **Efficiency factors** — 指定效率计算 `Gear only` (default) | `Gear, input torque, input speed, and temperature`

要指定模块效率计算，对于 **Efficiency factors**，请选择以下选项之一。

| Setting | Block Implementation |
| --- | --- |
| `Gear only` | 效率由作为挡位函数的 1D 查找表确定。 |
| `Gear, input torque, input speed, and temperature` | 效率由作为以下量函数的 4D 查找表确定：  - 挡位 - 输入扭矩 - 输入转速 - 油温 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TransEffModelPopup` |
| **值：** | `Gear only`（默认） | `Gear, input torque, input speed, and temperature` |
| **数据类型：** | `character vector` |

#### 依赖关系

| 将参数设置为 | 启用 |
| --- | --- |
| `Gear only` | **Efficiency vector, eta** |
| `Gear, input torque, input speed, and temperature` | **Efficiency torque breakpoints, Trq\_bpts**  **Efficiency speed breakpoints, omega\_bpts**  **Efficiency temperature breakpoints, Temp\_bpts**  **Efficiency lookup table, eta\_tbl** |

#### Transmission

### **Input shaft inertia, Jin** — 惯性 `.01`（默认） | `scalar`

输入轴惯性，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jin` |
| **值：** | `.01`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Input shaft damping, bin** — 阻尼 `.001`（默认） | `scalar`

输入轴阻尼，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bin` |
| **值：** | `.001`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Initial input velocity, omegain\_o** — 角速度 `0`（默认） | `scalar`

角速度，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegain_o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Gear number vector, G** — 指定变速器挡位数 `[-1, 0, 1, 2, 3, 4, 5]`（默认） | `vector`

用于指定变速器挡位数的整数挡位指令向量。空挡为 `0`。例如，您可以设置以下参数值。

| 要指定 | 将 **Gear number, G** 设置为 |
| --- | --- |
| 四个变速器挡位，包括空挡 | `[0,1,2,3,4]` |
| 三个变速器挡位，包括空挡和倒挡 | `[-1,0,1,2,3]` |
| 五个变速器挡位，包括空挡和倒挡 | `[-1,0,1,2,3,4,5]` |

**Gear number vector**、**Gear ratio vector**、**Transmission inertia vector**、**Transmission damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `G` |
| **值：** | `[-1, 0, 1, 2, 3, 4, 5]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Efficiency torque breakpoints, Trq\_bpts** — 断点 `[25, 50, 75, 100, 150, 200, 250]`（默认） | `vector`

效率表的扭矩断点，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_bpts` |
| **值：** | `[25, 50, 75, 100, 150, 200, 250]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Efficiency speed breakpoints, omega\_bpts** — 断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认） | `vector`

效率表的转速断点，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_bpts` |
| **值：** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认）| `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Efficiency temperature breakpoints, Temp\_bpts** — 断点 `[313 358]`（默认）| `vector`

效率表的温度断点，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_bpts` |
| **值：** | `[313 358]`（默认）| `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Gear ratio vector, N** — 输入速度与输出速度之比 `[-4.47, 1, 4.47, 2.47, 1.47, 1, 0.8]`（默认）| `vector`

齿轮比（即输入速度与输出速度之比）向量，其索引对应于 **Gear number, G** 中指定的比值。对于空挡，将齿轮比设置为 `1`。例如，您可以设置以下参数值。

| 要为以下对象指定齿轮比 | 将 **Gear number, G** 设置为 | 将 **Gear ratio, N** 设置为 |
| --- | --- | --- |
| 四个变速器速度，包括空挡 | `[0,1,2,3,4]` | `[1,4.47,2.47,1.47,1]` |
| 五个变速器速度，包括空挡和倒挡 | `[-1,0,1,2,3,4,5]` | `[-4.47,1,4.47,2.47,1.47,1,0.8]` |

**Gear number vector**、**Gear ratio vector**、**Transmission inertia vector**、**Transmission damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N` |
| **值：** | `[-4.47, 1, 4.47, 2.47, 1.47, 1, 0.8]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Transmission inertia vector, Jout** — 齿轮转动惯量 `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]`（默认）| `vector`

齿轮转动惯量向量，其索引对应于 **Gear number, G** 中指定的惯量，单位为 kg·m^2。例如，您可以设置以下参数值。

| 要为以下对象指定惯量 | 将 **Gear number, G** 设置为 | 将 **Inertia, J** 设置为 |
| --- | --- | --- |
| 四个齿轮，包括空挡 | `[0,1,2,3,4]` | `[0.01,2.28,2.04,0.32,0.028]` |
| 五个齿轮的惯量，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[2.28,0.01,2.28,2.04,0.32,0.028,0.01]` |

**Gear number vector**、**Gear ratio vector**、**Transmission inertia vector**、**Transmission damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jout` |
| **值：** | `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Transmission damping vector, bout** — 齿轮粘性阻尼系数 `[.003 .001 .003 .0025 .002 .001 .001]`（默认）| `vector`

齿轮粘性阻尼系数向量，其索引对应于 **Gear number, G** 中指定的系数，单位为 N·m·s/rad。例如，您可以设置以下参数值。

| 为以下对象指定阻尼 | 将 **Gear number, G** 设置为 | 将 **Damping, b** 设置为 |
| --- | --- | --- |
| 四个齿轮，包括空挡 | `[0,1,2,3,4]` | `[0.001,0.003,0.0025, 0.002,0.001]` |
| 五个齿轮，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[0.003,0.001,0.003, 0.0025,0.002,0.001,0.001]` |

**Gear number vector**、**Gear ratio vector**、**Transmission inertia vector**、**Transmission damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `bout` |
| **值**：| `[.003 .001 .003 .0025 .002 .001 .001]`（默认）| `vector` |
| **Data Types:** | `double` |

### **Efficiency vector, eta** — 齿轮效率 `[0.9, 0.9, 0.9, 0.9, 0.9, 0.95, 0.95]`（默认）| `vector`

齿轮机械效率向量，其索引对应于 **Gear number, G** 中指定的效率。例如，您可以设置以下参数值。

| 为以下对象指定效率 | 将 **Gear number, G** 设置为 | 将 **Efficiency, eta** 设置为 |
| --- | --- | --- |
| 四个齿轮，包括空挡 | `[0,1,2,3,4]` | `[0.9,0.9,0.9,0.9,0.95]` |
| 五个齿轮，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[0.9,0.9,0.9, 0.9,0.9,0.95,0.95]` |

**Gear number vector**、**Gear ratio vector**、**Transmission inertia vector**、**Transmission damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `eta` |
| **值**：| `[0.9, 0.9, 0.9, 0.9, 0.9, 0.95, 0.95]`（默认）| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear only`。

### **Efficiency lookup table, eta\_tbl** — 齿轮效率 `array`

齿轮机械效率表，*ηN* 作为齿轮、输入扭矩、输入速度和温度的函数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `eta_tbl` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Initial output velocity, omegaout\_o** — 变速器 `0`（默认）| `scalar`

变速器初始输出转速，*ωto*，单位为 rad/s。如果您选择 **Start simulation with clutch locked**，模块将忽略 **Initial output velocity, omega\_o** 参数值。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `omegaout_o` |
| **值**：| `0`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Initial gear, G\_o** — 接合挡位 `0`（默认）| `scalar`

初始接合挡位，*Go*。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `G_o` |
| **值**：| `0`（默认）| `scalar` |
| **Data Types:** | `double` |

#### Clutch and Synchronizer

### **Clutch pressure time constant, tauc** — Time `.02` (default) | `scalar`

压力输入滤波器时间常数，
*τc*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `tauc` |
| **值**：| `.02` (default) | `scalar` |
| **Data Types:** | `double` |

### **Synchronization time, ts** — Time `.25` (default) | `scalar`

换挡和同步所需的时间，
*ts*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ts` |
| **值**：| `.25` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch time, tc** — Time `.5` (default) | `scalar`

在换挡事件期间接合和分离离合器所需的时间，
*tc*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `tc` |
| **值**：| `.5` (default) | `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要创建此参数，请选择 **Control type**
参数 `Ideal integrated controller`。

### **Effective clutch radius, R** — Radius `.2` (default) | `scalar`

有效半径 Reff，与施加的离合器摩擦力一起用于确定摩擦力，
单位为 m。有效半径定义为：

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

该方程使用以下变量。

|  |  |
| --- | --- |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `R` |
| **值**：| `.2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch force gain, K\_c** — Force `5e3` (default) | `scalar`

开环锁止离合器增益，
*Kc*，单位为 N。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `K_c` |
| **值**：| `5e3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch static friction coefficient, mus** — Coefficient `0.6` (default) | `scalar`

无量纲的离合器盘静摩擦系数，
*μs*。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `mus` |
| **值**：| `0.6` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch kinematic friction coefficient, muk** — Coefficient `0.4` (default) | `scalar`

无量纲的离合器盘动摩擦系数，
*μk*。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `muk` |
| **值**：| `0.4` (default) | `scalar` |
| **Data Types:** | `double` |

### **以离合器锁止状态开始仿真** — 选择以初始锁止离合器 `off`（默认）| `on`

选择以在初始时锁止离合器。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `locked` |
| **值**：| `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### 依赖关系

要创建此参数，请选择 **Control type** 参数 `Ideal integrated controller`。

### **Start simulation with synchronizer locked** — 选择以初始锁定同步器 `off`（默认）| `on`

选择以初始锁定同步器。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClutchLocked` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

## 所属库

Powertrain Blockset / Transmission / Transmission Systems

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

理想自动手动变速器

Automated Manual Transmission 模块实现理想自动变速器（AMT）。AMT 是一种手动变速器，带有额外的执行器和电子控制单元（ECU），用于根据控制器的命令调节离合器和挡位选择。挡位数量通过一个整数向量指定，并带有相应的传动比、惯量、粘性阻尼和效率因子。离合器和同步器接合速率是线性的且可调。

使用该模块进行：

- 功率和扭矩容量选型
- 确定传动比对燃油经济性和性能的影响

为了确定旋转驱动轴速度和反作用扭矩，Automated Manual Transmission 模块计算：

- 离合器锁止和离合器摩擦
- 锁止旋转动力学
- 未锁止旋转动力学

要指定模块效率计算，对于 **Efficiency factors**，选择以下任一选项。

| 设置 | 模块实现 |
| --- | --- |
| `Gear only` | 效率由一维查找表确定，该查找表是挡位的函数。 |
| `Gear, input torque, input speed, and temperature` | 效率由四维查找表确定，该查找表是以下量的函数：  - 挡位 - 输入扭矩 - 输入转速 - 油温 |

### 离合器控制

AMT 通过控制来自离合器的压力信号来连续输出驱动轴扭矩。如果选择 **Control type** 参数 `Ideal integrated controller`，则该模块生成理想化的离合器压力信号。要使用您自己的离合器控制信号，请选择 **Control type** 参数 `External control`。

### 离合器锁止和离合器摩擦

根据离合器锁止状态，该模块实现以下摩擦模型之一。

| 如果 | 离合器状态 | 摩擦模型 |
| --- | --- | --- |
| ωi≠NωdorTS<|Tf−Nwibi| | 未锁止 | Tf=Tkwhere,Tk=FcReffμktanh[4(wiN−wd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) |
| ωi=NωtandTS≥|Tf−Nbiωi| | 锁止 | *Tf* = *Ts* |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωt* | 输出驱动轴速度 |
| *ωi* | 输入驱动轴速度 |
| *ωd* | 驱动轴速度 |
| bi | 粘性阻尼 |
| *Fc* | 施加的离合器力 |
| *N* | 接合挡位 |
| Tf | 摩擦力矩 |
| Tk | 动摩擦力矩 |
| Ts | 静摩擦力矩 |
| Reff | 有效离合器半径 |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |
| *μs* | 静摩擦系数 |
| *μk* | 动摩擦系数 |

### 锁止旋转动力学

为了在离合器锁止时对旋转动力学建模，该模块实现以下方程。

ω˙dJN=ηNTd−ωiNbN+NTiωi=Nωd

该模块通过微分确定输入扭矩 *Ti*。

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωi* | 输入驱动轴速度 |
| *ωd* | 驱动轴速度 |
| *N* | 接合挡位 |
| *bN* | 接合挡位粘性阻尼 |
| *JN* | 接合挡位惯量 |
| *ηN* | 接合挡位效率 |
| *Td* | 驱动轴扭矩 |
| *Ti* | 施加的输入扭矩 |

### Unlocked Rotational Dynamics

为了在离合器未锁止时对旋转动力学进行建模，该模块实现以下方程。

ω˙dJN=NTf−ωdbN+Td

其中：

|  |  |
| --- | --- |
| *ωd* | 驱动轴转速 |
| *N* | 接合挡位 |
| *bN* | 接合挡位粘性阻尼 |
| *JN* | 接合挡位惯量 |
| *Td* | 驱动轴扭矩 |
| *Ti* | 施加的输入扭矩 |

### Power Accounting

对于功率核算，该模块实现以下方程。

| Bus Signal | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrEng` | 发动机功率 | *Peng* | ωiTi |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | ωdTd |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrEffLoss` | 机械功率损失 | *Peffloss* | ωdTd(ηN−1) |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | −bNωd2 −binωi2 |
| `PwrCltchLoss` | 离合器功率损失 | *Pmech* | 锁止时：0  未锁止时：−Tk(ωi−Nωd) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredTrans` | 旋转动能变化率 | *Pstr* | 锁止时：ω˙iωi(Jin+JNN2)  未锁止时：Jinω˙iωi+JNω˙dωd |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *bN* | 接合挡位粘性阻尼 |
| *JN* | 接合挡位转动惯量 |
| *Jin* | 飞轮转动惯量 |
| *ηN* | 接合挡位效率 |
| *N* | 接合挡位传动比 |
| *Ti* | 施加的输入扭矩，通常来自发动机曲轴或双质量飞轮减振器 |
| *Td* | 施加的负载扭矩，通常来自差速器或驱动轴 |
| *ωd* | 初始输入驱动轴旋转速度 |
| *ωi*, *ώi* | 施加的驱动轴角速度和角加速度 |
