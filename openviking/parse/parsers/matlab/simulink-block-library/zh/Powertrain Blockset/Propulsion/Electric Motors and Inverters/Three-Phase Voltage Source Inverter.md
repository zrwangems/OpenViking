---
type: simulink-block
title: 'Three-Phase Voltage Source Inverter'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors and Inverters'
documentation_page: 'threephasevoltagesourceinverter'
documentation_source_path: 'ref/threephasevoltagesourceinverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-Phase Voltage Source Inverter

## 端口
```yaml
ports:
- name: PhaseVoltCmd
  summary: a、b、c 相线对中性点电压指令 1×3 数组
  direction: input
- name: SwitchCmd
  summary: 开关指令 1×3 数组
  direction: input
- name: BusVolt
  summary: 电源母线电压 bus
  direction: input
- name: PhaseCurr
  summary: a、b、c 相电流 1×3 数组
  direction: input
- name: MtrTrq
  summary: 电机转矩 scalar
  direction: input
- name: MtrSpd
  summary: 电机转速 scalar
  direction: input
- name: InvrtrTemp
  summary: 逆变器工作温度 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: PhaseVolt
  summary: a、b、c 相线对中性点电压 1×3 数组
  direction: output
- name: BusCurr
  summary: 电源母线电流 scalar
  direction: output
```

### 输入

### **PhaseVoltCmd** — a、b、c 相线对中性点电压指令 `1`×`3` 数组

a、b、c 相线对中性点电压指令，
*Va\_cmd*、
*Vb\_cmd* 和
*Vc\_cmd*，单位为 V。

#### 依赖

要创建此端口，请将 **Switching voltage
function** 设置为 `Commanded phase
voltage`。

### **SwitchCmd** — 开关指令 `1`×`3` 数组

开关指令，*Sa*、
*Sb* 和
*Sc*，
无量纲。

#### 依赖

要创建此端口，请将 **Switching voltage
function** 设置为 `Switch
inputs`。

### **BusVolt** — 电源母线电压 `bus`

电源母线电压，
*Vbus*，单位为 V。

### **PhaseCurr** — a、b、c 相电流 `1`×`3` 数组

a、b、c 相电流，*ia*、
*ib* 和
*ic*，单位为 A。

### **MtrTrq** — 电机转矩 `scalar`

电机转矩，*Tmtr*，单位为
N·m。

### **MtrSpd** — 电机转速 `scalar`

电机的角速度，
*ωmtr*，单位为 rad/s。

### **InvrtrTemp** — 逆变器工作温度 `scalar`

逆变器工作温度，
*TempInvrtr*，单位为
K。

#### 依赖

要创建此端口，请选择 **Input inverter
temperature**。
### 输出

### **Info** — 总线信号 bus

该总线信号包含以下模块计算结果。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `BusCurr` | | | 电源母线电流 | *ibus* | A |
| `PwrLossInv` | | | 逆变器功率损耗 | *εinv* | 无量纲 |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 传递至电机的功率 | *PTrnsfrdMtr* | W |
| `PwrBus` | 来自输入母线的功率 | *PTrnsfrdBus* | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 功率损耗 | *PNotTrnsfrd* | W |
| `PwrStored` | | *未使用* | | |

### **PhaseVolt** — a、b、c 相线对中性点电压 `1`×`3` 数组

a、b、c 相线对中性点电压，
*Van*、
*Vbn* 和
*Vcn*，单位为 V。

### **BusCurr** — 电源母线电流 `scalar`

电源母线电流，
*ibus*，单位为 A。
## 参数
```yaml
parameters:
- name: Input inverter temperature
  summary: 创建输入端口 off（默认）| on
  group: ''
  block_parameter: InvrtrTmpInpEnbl
  values: off（默认）| on
- name: Enable memory optimized 2D LUT
  summary: 选择 off（默认）| on
  group: ''
  block_parameter: enable_hdl
  values: off（默认）| on
- name: Calibrate Maps
  summary: 使用测量数据校准表 selection
  group: ''
- name: Switching voltage function
  summary: Selection Commanded phase voltage (default) | Switch inputs
  group: ''
  block_parameter: model_type
  values: Commanded phase voltage (default) | Switch inputs
- name: 速度断点 (w)，w_eff_bp
  summary: 速度断点 [-1000 -500 0 500 1000]（默认）| 1×M 向量
  group: ''
  block_parameter: w_eff_bp
  values: '[-1000 -500 0 500 1000]（默认）| 1×M 向量'
- name: w_eff_bp 的重采样存储大小，n1
  summary: 速度位大小 128（默认）| 2 | 4 | 8 | 16 | 32 | 64 | 256
  group: ''
  block_parameter: n1
  values: 128（默认）| 2 | 4 | 8 | 16 | 32 | 64 | 256
- name: 负载输入 (T) 的断点，T_eff_bp
  summary: 转矩断点 [-200 -100 0 100 200]（默认）| 1×N 向量
  group: ''
  block_parameter: T_eff_bp
  values: '[-200 -100 0 100 200]（默认）| 1×N 向量'
- name: T_eff_bp 的重采样存储大小，n2
  summary: 转矩位大小 128（默认）| 2 | 4 | 8 | 16 | 32 | 64 | 256
  group: ''
  block_parameter: n2
  values: 128（默认）| 2 | 4 | 8 | 16 | 32 | 64 | 256
- name: 温度输入的断点，Temp_eff_bp
  summary: 温度断点 [213.15 293.15 373.15]（默认）| 1×L 向量
  group: ''
  block_parameter: Temp_eff_bp
  values: '[213.15 293.15 373.15]（默认）| 1×L 向量'
- name: 对应功率损耗，ploss_table
  summary: 2D 查找表 [1 0.999 0.989 0.997 0.996;0.995 0.994 0.993 0.992 0.991;0.990 0.989 0.988 0.987 0.986;0.985 0.984 0.983
    0.982 0.981;0.980 0.979 0.978 0.977 0.976]（默认）| M×N 数组
  group: ''
  block_parameter: ploss_table
  values: M×N 数组
- name: Corresponding power loss, ploss_table_3d
  summary: 3D 查找表 M×N×L 数组
  group: ''
  block_parameter: ploss_table_3d
  values: M×N×L 数组
- name: w_eff_bp max endpoint, u1max
  summary: 转速断点 1000（默认）| scalar
  group: ''
  block_parameter: u1max
  values: 1000（默认）| scalar
- name: w_eff_bp min endpoint, u1min
  summary: 转速断点 -1000（默认）| scalar
  group: ''
  block_parameter: u1min
  values: -1000（默认）| scalar
- name: T_eff_bp max endpoint, u2max
  summary: 转矩断点 200（默认）| scalar
  group: ''
  block_parameter: u2max
  values: 200（默认）| scalar
- name: T_eff_bp min endpoint, u2min
  summary: 转矩断点 -200（默认）| scalar
  group: ''
  block_parameter: u2min
  values: -200（默认）| scalar
```

#### 模块选项

### **Input inverter temperature** — 创建输入端口 `off`（默认）| `on`

选择此参数以创建 `InvrtrTemp` 输入
端口。

该模块允许您指定逆变器
功率损耗查找表，这些查找表是电机转矩
*Tmtr* 和电机转速
*ωmtr* 的函数。如果您选择
**Input inverter temperature**，则这些表还是
逆变器温度
*TempInvrtr* 的函数。

| **Input Inverter Temperature** 参数设置 | 启用的效率表 | 函数关系 |
| --- | --- | --- |
| `off` | **Corresponding power loss, ploss\_table** | *ƒ*(*Tmtr*, *ωmtr*) |
| `on` | **Corresponding power loss, ploss\_table\_3d** | *ƒ*(*Tmtr*, *ωmtr*, *TempInvrtr*) |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InvrtrTmpInpEnbl` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

#### 依赖

如果您选择 **Input inverter temperature** 以
指定作为电机转矩、
电机转速和逆变器温度函数的 3D 功率损耗查找表，则不能选择
**Enable memory optimized 2D LUT** 来启用
内存优化。

### **Enable memory optimized 2D LUT** — 选择 `off`（默认）| `on`

启用内存优化查找表的生成，适用于限制内存的
代码生成目标。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `enable_hdl` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

#### 依赖

如果您选择 **Enable memory optimized 2D LUT**，则
不能选择 **Input inverter temperature**。

### **Calibrate Maps** — 使用测量数据校准表 `selection`

如果您拥有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据对查找表进行虚拟校准。该对话框将逐步引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| Import Loss Data | 从文件中导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedInverterDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Input inverter temperature** 设置 | 所需数据 | | --- | --- | | `off` | - 电机转速，rad/s - 电机转矩，N·m - 功率损耗，W | | `on` | - 电机转速，rad/s - 电机转矩，N·m - 电机温度，K - 功率损耗，W |  在稳态运行条件下采集逆变器数据。数据应覆盖逆变器的转速、转矩和温度运行范围。  要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| Generate Response Models | Model-Based Calibration Toolbox 使用试验计划将数据拟合到高斯过程模型（GPM）。  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| Generate Calibration | Model-Based Calibration Toolbox 校准响应模型并生成校准表。  要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| Update block parameters | 使用校准结果更新这些参数。  | **Input inverter temperature** 设置 | 参数 | | --- | --- | | `off` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Corresponding power loss,   ploss\_table** | | `on` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Breakpoints for temperature input,   Temp\_eff\_bp** - **Corresponding power loss,   ploss\_table\_3d** | |

#### Electrical Model

### **Switching voltage function** — Selection `Commanded phase voltage` (default) | `Switch inputs`

使用 **Switching voltage function** 参数设置开关电压函数。

| 设置 | 实现 | 图示 |
| --- | --- | --- |
| **Commanded phase voltage** | 相位 a、b、c 线对中性点电压指令输入。适用于连续正弦或空间矢量调制输入信号。 | 参数 Switching voltage function 设置为 Commanded phase voltage 时的电路图 |
| **Switch inputs** (default) | 逆变器开关输入指令。适用于硬件在环（HIL）仿真。  逆变器开关 S1、S3 和 S5 使用 S2、S4 和 S6 的互补控制。 | 参数 Switching voltage function 设置为 Switch inputs 时的电路图 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `model_type` |
| **值**：| `Commanded phase voltage` (default) | `Switch inputs` |
| **Data Types:** | `character vector` |

### **速度断点 (w)，w\_eff\_bp** — 速度断点 `[-1000 -500 0 500 1000]`（默认）| `1`×`M` 向量

电机转速 *ωmtr* 的向量，功率损耗的断点，单位为 rad/s。如果您设置 **Enable memory optimized 2D LUT**，模块会将数据转换为单精度。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff_bp` |
| **值：** | `[-1000 -500 0 500 1000]`（默认）| `1`×`M` 向量 |
| **数据类型：** | `double` |

### **w\_eff\_bp 的重采样存储大小，n1** — 速度位大小 `128`（默认）| `2` | `4` | `8` | `16` | `32` | `64` | `256`

速度断点存储大小 *n1*，无量纲。模块根据存储大小对**对应功率损耗，ploss\_table**数据进行重采样。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `n1` |
| **值：** | `128`（默认）| `2` | `4` | `8` | `16` | `32` | `64` | `256` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择**启用内存优化的 2D LUT**。

### **负载输入 (T) 的断点，T\_eff\_bp** — 转矩断点 `[-200 -100 0 100 200]`（默认）| `1`×`N` 向量

电机转矩 *Tmtr* 的向量，功率损耗的断点，单位为 N·m。如果设置**启用内存优化的 2D LUT**，模块会将数据转换为单精度。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff_bp` |
| **值：** | `[-200 -100 0 100 200]`（默认）| `1`×`N` 向量 |
| **数据类型：** | `double` |

### **T\_eff\_bp 的重采样存储大小，n2** — 转矩位大小 `128`（默认）| `2` | `4` | `8` | `16` | `32` | `64` | `256`

转矩断点存储大小 *n2*，无量纲。模块根据存储大小对**对应功率损耗，ploss\_table**数据进行重采样。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `n2` |
| **值：** | `128`（默认）| `2` | `4` | `8` | `16` | `32` | `64` | `256` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择**启用内存优化的 2D LUT**。

### **温度输入的断点，Temp\_eff\_bp** — 温度断点 `[213.15 293.15 373.15]`（默认）| `1`×`L` 向量

逆变器温度 *TempInvrtr* 的向量，功率损耗的断点，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_eff_bp` |
| **值：** | `[213.15 293.15 373.15]`（默认）| `1`×`L` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择**输入逆变器温度**。

### **对应功率损耗，ploss\_table** — 2D 查找表 `[1 0.999 0.989 0.997 0.996;0.995 0.994 0.993 0.992 0.991;0.990 0.989 0.988 0.987 0.986;0.985 0.984 0.983 0.982 0.981;0.980 0.979 0.978 0.977 0.976]`（默认）| `M`×`N` 数组

功率损耗值的数组，作为 `M` 个电机速度 *ωmtr* 和 `N` 个电机转矩 *Tmtr* 的函数，单位为 W。每个值指定特定电机速度和电机转矩组合下的功率损耗。数组大小必须与速度和转矩向量定义的维度匹配。

如果您有 Model-Based Calibration Toolbox，请点击**校准映射**以使用测量数据虚拟校准查找表。

如果设置**启用内存优化的 2D LUT**，模块会将数据转换为单精度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ploss_table` |
| **值：** | `M`×`N` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请清除 **Input inverter temperature**。

### **Corresponding power loss, ploss\_table\_3d** — 3D 查找表 `M`×`N`×`L` 数组

功率损耗值的数组，作为 `M` 个电机转速 *ωmtr*、`N` 个电机转矩 *Tmtr* 和 `L` 个电机温度 *TempInvrtr* 的函数，单位为 W。每个值指定特定电机转速、电机转矩和温度组合下的功率损耗。数组大小必须与转速、转矩和温度向量定义的维度匹配。

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据虚拟校准查找表。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ploss_table_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Input inverter temperature**。

#### 指定外推

### **w\_eff\_bp max endpoint, u1max** — 转速断点 `1000`（默认）| `scalar`

转速断点最大外推端点 *u1max*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u1max` |
| **值：** | `1000`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。

### **w\_eff\_bp min endpoint, u1min** — 转速断点 `-1000`（默认）| `scalar`

转速断点最小外推端点 *u1min*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u1min` |
| **值：** | `-1000`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。

### **T\_eff\_bp max endpoint, u2max** — 转矩断点 `200`（默认）| `scalar`

转矩断点最大外推端点 *u2max*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u2max` |
| **值：** | `200`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。

### **T\_eff\_bp min endpoint, u2min** — 转矩断点 `-200`（默认）| `scalar`

转矩断点最小外推端点 *u2min*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u2min` |
| **值：** | `-200`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。
## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

三相电压源逆变器

三相电压源逆变器模块实现了一个三相电压源逆变器，为平衡三相负载生成中性点电压指令。为连续矢量调制或逆变器开关输入信号配置电压开关函数。您可以将该模块集成到闭环模型中，以仿真功率逆变器。该模块控制理想开关状态。

要启用适用于限制内存的代码生成目标的功率损耗计算，请选择 **Enable memory optimized 2D LUT**。点击 **Calibrate Maps**，以根据电机转矩和电机转速虚拟校准逆变器功率损耗查找表。

如果您选择 **Input inverter temperature**，请点击 **Calibrate Maps**，以根据电机转矩、电机转速和逆变器温度虚拟校准功率损耗表。您无法为 3D 功率损耗查找表启用内存优化。

使用 **Switching voltage function** 参数设置开关电压函数。

| 设置 | 实现 | 图示 |
| --- | --- | --- |
| **Commanded phase voltage** | a、b、c 相线对中性点电压指令输入。适用于连续正弦或空间矢量调制输入信号。 | 当参数 Switching voltage function 设置为 Commanded phase voltage 时的电路图 |
| **Switch inputs**（默认） | 逆变器开关输入指令。适用于硬件在环（HIL）仿真。逆变器开关 S1、S3 和 S5 使用 S2、S4 和 S6 的互补控制。 | 当参数 Switching voltage function 设置为 Switch inputs 时的电路图 |

### 虚拟校准

如果您拥有 Model-Based Calibration Toolbox™，请点击 **Calibrate Maps**，以使用测量数据虚拟校准查找表。该对话框会逐步执行以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedInverterDataset.xlsx`。有关更多信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Input inverter temperature** 设置 | 所需数据 | | --- | --- | | `off` | - 电机转速，rad/s - 电机转矩，N·m - 功率损耗，W | | `on` | - 电机转速，rad/s - 电机转矩，N·m - 电机温度，K - 功率损耗，W |  在稳态运行条件下采集逆变器数据。数据应覆盖逆变器转速、转矩和温度运行范围。  要筛选或编辑数据，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Data Editor。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合到高斯过程模型（GPM）。  要评估或调整响应模型拟合，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Model Browser。有关更多信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准表。  要评估或调整校准，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox CAGE Browser。有关更多信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准更新这些参数。  | **Input inverter temperature** 设置 | 参数 | | --- | --- | | `off` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Corresponding power loss,   ploss\_table** | | `on` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Breakpoints for temperature input,   Temp\_eff\_bp** - **Corresponding power loss,   ploss\_table\_3d** |

### Switching Function

对于开关电压，模块实现取决于 **Switching voltage function** 设置。

| 设置 | 计算 | 方程 |
| --- | --- | --- |
| `Commanded phase voltage` | 连续线对中性点电压指令设置为相 a、b、c 线对中性点电压指令输入 | van=va\_cmdvbn=vb\_cmdvcn=vc\_cmd |
| Line-to-line voltage | vab= van− vbnvbc= vbn− vcnvca= vcn− van |
| `Switch inputs` | 开关函数 | SFa={1      S1 on and S2 off−1   S1 off and S2 onSFb={1      S3 on and S4 off−1   S3 off and S4 onSFc={1      S5 on and S6 off−1   S5 off and S6 on |
| Line-to-center point voltage | vao= vbus2 SFavbo= vbus2 SFbvco= vbus2 SFc |
| Line-to-neutral voltage | van= vao− vnovbn= vbo− vnovcn= vco− vnovan+ vbn+ vcn= 0vno= 13(vao+ vbo+ vco)van= vao− 13(vao+ vbo+ vco)vbn= vbo−13(vao+ vbo+ vco)vcn= vco− 13(vao+ vbo+ vco) |
| Line-to-line voltage | vab= van− vbnvbc= vbn− vcnvca= vcn− van |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *SFa*, *SFb*, *SFc* | 分别为相 a、b、c 线开关函数 |
| *vbus* | 电源母线电压 |
| *Vao*, *Vbo*, *Vco* | 分别为相 a、b、c 线对中心点电压 |
| *Van*, *Vbn*, *Vcn* | 分别为相 a、b、c 线对中性点电压 |
| *Vab*, *Vbc*, *Vca* | 分别为相 ab、bc、ca 线对中性点电压 |
| *Va\_cmd*, *Vb\_cmd*, *Vc\_cmd* | 分别为相 a、b、c 线对中性点电压指令 |

### Current and Power Loss

对于线对中心点、线对中性点和线对线电压，模块实现以下方程。

| 计算 | | 方程 |
| --- | --- | --- |
| 电机和母线功率 | | Pmtr= vania+vbnib+vcnicPbus= vbusibus |
| 逆变器功率损耗和母线电流 | | Pin= Pbus= vbusibusPout= Pmtr= vania+vbnib+vcnic+PLossInvibus= vania+vbnib+vcnic+PLossInv vbus |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Pmtr* | 输送到电机的功率 |
| *Pbus* | 来自输入母线的功率 |
| *Ploss* | 功率损耗 |
| *ibus* | 电源母线电流 |
| *ia*, *ib*, *ic* | 分别为相 a、b、c 线电流 |
| *Van*, *Vbn*, *Vcn* | 分别为相 a、b、c 线对中性点电压 |
| *vbus* | 电源母线电压 |

### Power Accounting

对于功率核算，模块实现以下方程。

| 母线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 输送到电机的功率 | *PTrnsfrdMtr* | PTrnsfrdMtr= −(vania+vbnib+vcnic ) |
| `PwrBus` | 来自输入母线的功率 | *PTrnsfrdBus* | PTrnsfrdBus= Pbus |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrLoss` | 功率损耗  负值表示功率损耗 | *PNotTrnsfrd* | PNotTrnsfrd= −(PTrnsfrdBus+PTrnsfrdMtr) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | | *未使用* | | |

### 查找表内存优化

逆变器功率损耗表参数 **Corresponding power loss, ploss\_table** 数据是不同电池电压下电机转矩和电机转速的函数。正电流表示电池放电。负电流表示电池充电。

要为限制内存的代码生成目标启用功率损耗计算，请选择 **Enable memory optimized 2D LUT**。该模块使用线性插值来优化用于代码生成的逆变器功率损耗查找表值。下表总结了优化实现。

| 使用情形 | | 实现 |
| --- | --- | --- |
| 电机转速和转矩输入与查找表断点值对齐。 | | 内存优化功率损耗是电机转速和转矩交点处的功率损耗查找表值。 |
| 电机转速和转矩输入与查找表断点值不对齐，但在范围内。 | | 内存优化功率损耗是相应电机转速和转矩之间的线性插值。 |
| 电机转速和转矩输入与查找表断点值不对齐，且超出范围。 | | 无法计算内存优化功率损耗。模块使用外推数据。 |

**外推**

为代码生成优化的查找表不支持对超出范围的数据进行外推。但是，您可以通过选择 **Specify Extrapolation** 将预先计算的外推值包含在功率损耗查找表中。

该模块使用端点参数调整表数据大小。

| 用户输入 | 外推 |
| --- | --- |
| 要外推以覆盖所需工作范围的查找表 | 外推查找表与原始表一同显示 |
