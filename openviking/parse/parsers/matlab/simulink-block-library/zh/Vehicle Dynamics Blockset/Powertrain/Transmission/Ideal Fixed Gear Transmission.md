---
type: simulink-block
title: 'Ideal Fixed Gear Transmission'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Transmission'
documentation_page: 'idealfixedgeartransmission'
documentation_source_path: 'ref/idealfixedgeartransmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Fixed Gear Transmission

## 端口
```yaml
ports:
- name: Gear
  summary: 要接合的挡位编号 scalar
  direction: input
- name: EngTrq
  summary: 施加的输入扭矩 scalar
  direction: input
- name: DiffTrq
  summary: 施加的负载扭矩 scalar
  direction: input
- name: Temp
  summary: 油温 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: EngSpd
  summary: 角速度 scalar
  direction: output
- name: DiffSpd
  summary: 角速度 scalar
  direction: output
```

### 输入

### **Gear** — 要接合的挡位编号 `scalar`

要接合的挡位编号的整数值，
*Gcmd*。

### **EngTrq** — 施加的输入扭矩 `scalar`

施加的输入扭矩，*Ti*，
通常来自发动机曲轴或双质量飞轮减振器，单位为
N·m。

### **DiffTrq** — 施加的负载扭矩 `scalar`

施加的负载扭矩，*To*，
通常来自差速器，单位为 N·m。

### **Temp** — 油温 `scalar`

油温，单位为 K。为确定效率，该模块使用一个
4D 查找表，其为以下量的函数：

- Gear
- 输入扭矩
- 输入转速
- 油温

#### 依赖关系

要启用此端口，请将 **Efficiency factors**
设置为 `Gear, input torque, input speed, and
temperature`。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `Eng` | `EngTrq` | | 施加的输入扭矩，通常来自发动机曲轴或双质量飞轮减振器 | *Ti* | N·m |
| `EngSpd` | | 施加的驱动轴角速度输入 | *ωi* | rad/s |
| `Diff` | `DiffTrq` | | 施加的负载扭矩，通常来自差速器 | *To* | N·m |
| `DiffSpd` | | 驱动轴角速度输出 | *ωo* | rad/s |
| `Trans` | `TransSpdRatio` | | 时刻 t 的输入输出转速比 | *Φ(t)* | N/A |
| `TransEta` | | 输出功率与输入功率之比 | *ηN* | N/A |
| `TransGearCmd` | | 指令挡位 | *Ncmd* | N/A |
| `TransGear` | | 已接合挡位 | *N* | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrEng` | 发动机功率 | *Peng* | W |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | W |
| `PwrNotTrnsfrd` | `PwrEffLoss` | 机械功率损失 | *Peffloss* | W |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | W |
| `PwrStored` | `PwrStoredTrans` | 旋转动能变化率 | *Pstr* | W |

### **EngSpd** — 角速度 `scalar`

施加的驱动轴角速度输入，
*ωi*，单位为 rad/s。

### **DiffSpd** — 角速度 `scalar`

驱动轴角速度输出，
*ωo*，单位为 rad/s。
## 参数
```yaml
parameters:
- name: Efficiency factors
  summary: 指定效率计算 Gear only (default) | Gear, input torque, input speed, and temperature
  group: ''
  block_parameter: TransEffModelPopup
  values: Gear only (default) | Gear, input torque, input speed, and temperature
- name: Gear property interpolation method
  summary: 插值 Nearest (default) | Linear | Flat | Cubic spline
  group: ''
  block_parameter: gearInterp
  values: Nearest (default) | Linear | Flat | Cubic spline
- name: Gear number vector, G
  summary: 指定变速器速度数量 [-1,0,1,2,3,4,5]（默认）| vector
  group: ''
  block_parameter: G
  values: '[-1,0,1,2,3,4,5]（默认）| vector'
- name: Efficiency torque breakpoints, Trq_bpts
  summary: 断点 [25,50,75,100,150,200,250]（默认）| vector
  group: ''
  block_parameter: Trq_bpts
  values: '[25,50,75,100,150,200,250]（默认）| vector'
- name: Efficiency speed breakpoints, omega_bpts
  summary: 断点 [52.4 78.5 105 131 157 183 209 262 314 419 524]（默认）| vector
  group: ''
  block_parameter: omega_bpts
  values: '[52.4 78.5 105 131 157 183 209 262 314 419 524]（默认）| vector'
- name: Efficiency temperature breakpoints, Temp_bpts
  summary: 断点 [313 358]（默认）| vector
  group: ''
  block_parameter: Temp_bpts
  values: '[313 358]（默认）| vector'
- name: Gear ratio vector, N
  summary: 输入速度与输出速度之比 [-4.47,4.47,4.47,2.47,1.47,1,0.8]（默认）| vector
  group: ''
  block_parameter: N
  values: '[-4.47,4.47,4.47,2.47,1.47,1,0.8]（默认） | vector'
- name: 惯性向量，Jout
  summary: 齿轮转动惯量 [0.128 0.01 0.128 0.1 0.062 0.028 0.01]（默认） | vector
  group: ''
  block_parameter: Jout
  values: '[0.128 0.01 0.128 0.1 0.062 0.028 0.01]（默认） | vector'
- name: 阻尼向量，bout
  summary: 齿轮粘性阻尼系数 [.003 .001 .003 .0025 .002 .001 .001]（默认） | vector
  group: ''
  block_parameter: bout
  values: '[.003 .001 .003 .0025 .002 .001 .001]（默认） | vector'
- name: 效率向量，eta
  summary: 齿轮效率 [0.9,0.9,0.9,0.9,0.9,0.95,0.95]（默认） | vector
  group: ''
  block_parameter: eta
  values: '[0.9,0.9,0.9,0.9,0.9,0.95,0.95]（默认） | vector'
- name: 效率查找表，eta_tbl
  summary: 齿轮效率 array
  group: ''
  block_parameter: eta_tbl
  values: array
- name: 初始挡位编号，G_o
  summary: 挡位 0（默认）| scalar
  group: ''
  block_parameter: G_o
  values: 0（默认）| scalar
- name: 初始输出速度，omega_o
  summary: 输出转速 0（默认）| scalar
  group: ''
  block_parameter: omega_o
  values: 0（默认）| scalar
- name: 初始空挡输入速度，omegainN_o
  summary: 空挡输入转速 0（默认）| scalar
  group: ''
  block_parameter: omegainN_o
  values: 0（默认）| scalar
- name: 换挡时间常数，tau_s
  summary: 时间 .01（默认）| scalar
  group: ''
  block_parameter: tau_s
  values: .01（默认）| scalar
```

### **Efficiency factors** — 指定效率计算 `Gear only` (default) | `Gear, input torque, input speed, and temperature`

要指定模块效率计算，对于 **Efficiency factors**，请选择以下选项之一。

| Setting | Block Implementation |
| --- | --- |
| `Gear only` | 效率由作为挡位函数的 1D 查找表确定。 |
| `Gear, input torque, input speed, and temperature` | 效率由作为以下量的函数的 4D 查找表确定：  - Gear - 输入扭矩 - 输入转速 - 油温 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TransEffModelPopup` |
| **值**：| `Gear only` (default) | `Gear, input torque, input speed, and temperature` |
| **Data Types:** | `character vector` |

#### 依赖关系

| Setting Parameter To | Enables |
| --- | --- |
| `Gear only` | **Efficiency vector, eta** |
| `Gear, input torque, input speed, and temperature` | **Efficiency torque breakpoints, Trq\_bpts**  **Efficiency speed breakpoints, omega\_bpts**  **Efficiency temperature breakpoints, Temp\_bpts**  **Efficiency lookup table, eta\_tbl** |

### **Gear property interpolation method** — 插值 `Nearest` (default) | `Linear` | `Flat` | `Cubic spline`

模块在换挡期间用于切换传动比的方法。

#### 程序化使用

要以程序化方式设置模块
参数值，请使用 `set_param`
函数。

要以程序化方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `gearInterp` |
| **值**：| `Nearest` (default) | `Linear` | `Flat` | `Cubic spline` |
| **Data Types:** | `character vector` |

#### Transmission

### **Gear number vector, G** — 指定变速器速度数量 `[-1,0,1,2,3,4,5]`（默认）| `vector`

用于指定变速器速度数量的整数挡位指令向量。空挡为 `0`。例如，您可以设置以下参数值。

| 要指定 | 将 **Gear number, G** 设置为 |
| --- | --- |
| 四个变速器速度，包括空挡 | `[0,1,2,3,4]` |
| 三个变速器速度，包括空挡和倒挡 | `[-1,0,1,2,3]` |
| 五个变速器速度，包括空挡和倒挡 | `[-1,0,1,2,3,4,5]` |

**Gear number vector**、**Gear ratio vector**、**Inertia vector**、**Damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `G` |
| **值**：| `[-1,0,1,2,3,4,5]`（默认）| `vector` |
| **Data Types:** | `double` |

### **Efficiency torque breakpoints, Trq\_bpts** — 断点 `[25,50,75,100,150,200,250]`（默认）| `vector`

效率表的转矩断点。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Trq_bpts` |
| **值**：| `[25,50,75,100,150,200,250]`（默认）| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Efficiency speed breakpoints, omega\_bpts** — 断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认）| `vector`

效率表的转速断点，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `omega_bpts` |
| **值**：| `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认）| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Efficiency temperature breakpoints, Temp\_bpts** — 断点 `[313 358]`（默认）| `vector`

效率表的温度断点。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Temp_bpts` |
| **值**：| `[313 358]`（默认）| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Gear ratio vector, N** — 输入速度与输出速度之比 `[-4.47,4.47,4.47,2.47,1.47,1,0.8]`（默认）| `vector`

挡位传动比向量（即输入速度与输出速度之比），其索引对应于 **Gear number, G** 中指定的传动比。对于空挡，将传动比设置为 `1`。例如，您可以设置以下参数值。

| 要为以下对象指定挡位传动比 | 将 **Gear number, G** 设置为 | 将 **Gear ratio, N** 设置为 |
| --- | --- | --- |
| 四个变速器速度，包括空挡 | `[0,1,2,3,4]` | `[1,4.47,2.47,1.47,1]` |
| 五个变速器速度，包括空挡和倒挡 | `[-1,0,1,2,3,4,5]` | `[-4.47,1,4.47,2.47, 1.47,1,0.8]` |

**Gear number vector**、**Gear ratio vector**、**Inertia vector**、**Damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N` |
| **值：** | `[-4.47,4.47,4.47,2.47,1.47,1,0.8]`（默认） | `vector` |
| **数据类型：** | `double` |

### **惯性向量，Jout** — 齿轮转动惯量 `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]`（默认） | `vector`

齿轮转动惯量向量，
*JN*，其索引对应于
**Gear number, G** 中指定的惯量，单位为 kg\*m^2。
例如，您可以设置以下参数值。

| 要为以下对象指定惯量 | 将 **Gear number, G** 设置为 | 将 **Inertia, J** 设置为 |
| --- | --- | --- |
| 四个齿轮，包括空挡 | `[0,1,2,3,4]` | `[0.01,2.28,2.04, 0.32,0.028]` |
| 五个齿轮的惯量，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[2.28,0.01,2.28, 2.04,0.32,0.028,0.01]` |

**Gear number
vector**、**Gear ratio vector**、**Inertia
vector**、**Damping vector** 和 **Efficiency
vector** 参数的向量维度必须相等。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jout` |
| **值：** | `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]`（默认） | `vector` |
| **数据类型：** | `double` |

### **阻尼向量，bout** — 齿轮粘性阻尼系数 `[.003 .001 .003 .0025 .002 .001 .001]`（默认） | `vector`

齿轮粘性阻尼系数向量，
*bN*，其索引
对应于 **Gear number,
G** 中指定的系数，单位为 N·m·s/rad。例如，您可以设置以下参数
值。

| 要为以下对象指定阻尼 | 将 **Gear number, G** 设置为 | 将 **Damping, b** 设置为 |
| --- | --- | --- |
| 四个齿轮，包括空挡 | `[0,1,2,3,4]` | `[0.001,0.003, 0.0025,0.002,0.001]` |
| 五个齿轮，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[0.003,0.001, 0.003,0.0025, 0.002,0.001,0.001]` |

**Gear number
vector**、**Gear ratio vector**、**Inertia
vector**、**Damping vector** 和 **Efficiency
vector** 参数的向量维度必须相等。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bout` |
| **值：** | `[.003 .001 .003 .0025 .002 .001 .001]`（默认） | `vector` |
| **数据类型：** | `double` |

### **效率向量，eta** — 齿轮效率 `[0.9,0.9,0.9,0.9,0.9,0.95,0.95]`（默认） | `vector`

齿轮机械效率向量，
*ηN*，其索引对应于
**Gear number, G** 中指定的效率。例如，
您可以设置以下参数值。

| 要为以下对象指定效率 | 将 **Gear number, G** 设置为 | 将 **Efficiency, eta** 设置为 |
| --- | --- | --- |
| 四个齿轮，包括空挡 | `[0,1,2,3,4]` | `[0.9,0.9,0.9,0.9,0.95]` |
| 五个齿轮，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[0.9,0.9,0.9, 0.9,0.9,0.95,0.95]` |

**Gear number
vector**、**Gear ratio vector**、**Inertia
vector**、**Damping vector** 和 **Efficiency
vector** 参数的向量维度必须相等。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta` |
| **值：** | `[0.9,0.9,0.9,0.9,0.9,0.95,0.95]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors**
设置为 `Gear only`。

### **效率查找表，eta\_tbl** — 齿轮效率 `array`

齿轮机械效率表，
*ηN* 作为齿轮、
输入扭矩、输入速度和温度的函数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_tbl` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为 `Gear, input torque, input speed, and temperature`。

### **初始挡位编号，G\_o** — 挡位 `0`（默认）| `scalar`

初始挡位编号，*Go*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `G_o` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **初始输出速度，omega\_o** — 输出转速 `0`（默认）| `scalar`

变速器初始输出旋转速度，*ωo*，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_o` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **初始空挡输入速度，omegainN\_o** — 空挡输入转速 `0`（默认）| `scalar`

初始空挡输入旋转速度，*ωNo*，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegainN_o` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **换挡时间常数，tau\_s** — 时间 `.01`（默认）| `scalar`

换挡时间常数，*τs*，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_s` |
| **值：** | `.01`（默认）| `scalar` |
| **数据类型：** | `double` |
## 所属库

Powertrain Blockset / Transmission / Transmission Systems Vehicle Dynamics Blockset / Powertrain / Transmission

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

无离合器或同步器的理想固定挡位变速器

Ideal Fixed Gear Transmission 实现了一个理想化的固定挡位变速器，不含离合器或同步器。当您不需要详细的变速器模型时，例如在组件选型、燃油经济性和排放研究中，可使用该模块来建模整体传动比和功率损失。该模块实现了一个参数化程度最低或计算成本最低的变速器模型。

要指定模块效率计算方式，请为 **效率因子** 选择以下任一选项。

| 设置 | 模块实现 |
| --- | --- |
| `Gear only` | 效率由作为挡位函数的一维查找表确定。 |
| `Gear, input torque, input speed, and temperature` | 效率由作为以下函数的三维查找表确定： - 挡位 - 输入扭矩 - 输入转速 - 油温 |

该模块使用以下方程确定变速器动力学：

ω˙iJNN2=ηN(ToN+Ti)−ωiN2bNωi=Nωo

该模块对挡位指令信号进行滤波：

GGcmd(s)=1τss+1

### Neutral Gear

当 **Initial gear number, G\_o** 等于 `0` 时，初始挡位为空挡。该模块使用以下参数将输入飞轮与下游齿轮传动解耦。

- **Initial input velocity, omega\_o**
- **Initial neutral input velocity, omegainN\_o**

该模块使用以下方程计算空挡速度和飞轮。

ω˙neutralJNN2=ηNToN−ωneutralN2bNωneutral=Nωo

ω˙1JF=η@N=0Ti−b@N=0ωiJF=J@N=1−J@N=0

### Power Accounting

对于功率核算，该模块实现以下方程。

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrEng` | 发动机功率 | *Peng* | ωiTi |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | ωoTo |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrEffLoss` | 机械功率损失 | *Peffloss* | ωoTo(ηN−1) |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | 对于  G=0:     −bNωi2|N2|对于  G≠0:  −bNωi2 −bNωneutral2|N2| |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredTrans` | 旋转动能变化率 | *Pstr* | 对于  G=0:     JNN2ω˙iωi对于  G≠0:   JFω˙iωi+JNN2ω˙neutralωneutral |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *bN* | 接合挡位粘性阻尼 |
| *JN* | 接合挡位转动惯量 |
| *JF* | 飞轮转动惯量 |
| *ηN* | 接合挡位效率 |
| *G* | 接合挡位编号 |
| *Gcmd* | 要接合的挡位编号 |
| *N* | 接合挡位传动比 |
| *Ti* | 施加的输入扭矩，通常来自发动机曲轴或双质量飞轮减振器 |
| *To* | 施加的负载扭矩，通常来自差速器或传动轴 |
| *ωo* | 初始输入传动轴旋转速度 |
| *ωi*, *ώi* | 施加的传动轴角速度和角加速度 |
| *ωNo* | 初始空挡输入旋转速度 |
| *ωneutral* | 空挡传动轴旋转速度 |
| *τs* | 换挡时间常数 |
