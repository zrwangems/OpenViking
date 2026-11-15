---
type: simulink-block
title: 'Three-Phase Voltage Source Inverter'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors, Inverters, and Controllers'
documentation_page: 'threephasevoltagesourceinverter'
documentation_source_path: 'ref/threephasevoltagesourceinverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-Phase Voltage Source Inverter

## 端口

### 输入

### **PhaseVoltCmd** — 相 a、b、c 相对中性点电压命令 `1`-by-`3` array

相 a、b、c 相对中性点电压命令，
*Va\_cmd*、
*Vb\_cmd* 和
*Vc\_cmd*，单位为 V。

#### 依赖关系

要创建此端口，请将 **Switching voltage function** 设置为 `Commanded phase voltage`。

### **SwitchCmd** — 开关命令 `1`-by-`3` array

开关命令，*Sa*、
*Sb* 和
*Sc*，
dimensionless。

#### 依赖关系

要创建此端口，请将 **Switching voltage function** 设置为 `Switch inputs`。

### **BusVolt** — 电源总线电压 `bus`

电源总线电压，
*Vbus*，单位为 V。

### **PhaseCurr** — 相 a、b、c 电流 `1`-by-`3` array

相 a、b、c 电流，*ia*、
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

#### 依赖关系

要创建此端口，请选择 **Input inverter temperature**。
### 输出

### **Info** — 总线信号 bus

该总线信号包含以下模块计算。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `BusCurr` | | | 电源总线电流 | *ibus* | A |
| `PwrLossInv` | | | 逆变器功率损耗 | *εinv* | dimensionless |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 传递给电机的功率 | *PTrnsfrdMtr* | W |
| `PwrBus` | 来自输入总线的功率 | *PTrnsfrdBus* | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 功率损耗 | *PNotTrnsfrd* | W |
| `PwrStored` | | *未使用* | | |

### **PhaseVolt** — 相 a、b、c 相对中性点电压 `1`-by-`3` array

相 a、b、c 相对中性点电压，
*Van*、
*Vbn* 和
*Vcn*，单位为 V。

### **BusCurr** — 电源总线电流 `scalar`

电源总线电流，
*ibus*，单位为 A。

## 参数

#### 模块选项

### **Input inverter temperature** — 创建输入端口 `off` (default) | `on`

选择此参数可创建 `InvrtrTemp` 输入端口。

该模块允许您指定逆变器功率损耗查找表，这些查找表是电机转矩
*Tmtr* 和电机转速
*ωmtr* 的函数。如果选择
**Input inverter temperature**，这些表还是逆变器温度
*TempInvrtr* 的函数。

| **Input Inverter Temperature** 参数设置 | 启用的效率表 | 函数取决于 |
| --- | --- | --- |
| `off` | **Corresponding power loss, ploss\_table** | *ƒ*(*Tmtr*, *ωmtr*) |
| `on` | **Corresponding power loss, ploss\_table\_3d** | *ƒ*(*Tmtr*, *ωmtr*, *TempInvrtr*) |

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InvrtrTmpInpEnbl` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

如果选择 **Input inverter temperature** 来
指定作为电机转矩、电机转速和逆变器温度函数的 3D 功率损耗查找表，则不能选择
**Enable memory optimized 2D LUT** 来启用
内存优化。

### **Enable memory optimized 2D LUT** — 选择 `off` (default) | `on`

启用生成内存优化的查找表，适用于限制内存的代码
生成目标。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `enable_hdl` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

如果选择 **Enable memory optimized 2D LUT**，则
不能选择 **Input inverter temperature**。

### **Calibrate Maps** — 使用测量数据标定表 `selection`

如果有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，以使用测量数据虚拟标定查找
表。该对话框将引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedInverterDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Input inverter temperature** 设置 | 所需数据 | | --- | --- | | `off` | - 电机转速，rad/s - 电机转矩，N·m - 功率损耗，W | | `on` | - 电机转速，rad/s - 电机转矩，N·m - 电机温度，K - 功率损耗，W |  在稳态工作条件下采集逆变器数据。数据应覆盖逆变器的转速、转矩和温度工作范围。  要筛选或编辑数据，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Data Editor。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合为高斯过程模型 (GPM)。  要评估或调整响应模型拟合，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Model Browser。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 标定响应模型并生成已标定的表。  要评估或调整标定，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox CAGE Browser。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定更新这些参数。  | **Input inverter temperature** 设置 | 参数 | | --- | --- | | `off` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Corresponding power loss,   ploss\_table** | | `on` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Breakpoints for temperature input,   Temp\_eff\_bp** - **Corresponding power loss,   ploss\_table\_3d** | |

#### 电气模型

### **Switching voltage function** — 选择 `Commanded phase voltage` (default) | `Switch inputs`

使用 **Switching voltage function**
参数来设置开关电压函数。

| 设置 | 实现 | 图示 |
| --- | --- | --- |
| **Commanded phase voltage** | 相 a、b、c 相对中性点电压命令输入。适用于连续正弦或空间矢量调制输入信号。 | 当参数 Switching voltage function 设置为 Commanded phase voltage 时的电路图 |
| **Switch inputs** (default) | 逆变器开关输入命令。适用于硬件在环 (HIL) 仿真。  逆变器开关 S1、S3 和 S5 使用 S2、S4 和 S6 的互补控制。 | 当参数 Switching voltage function 设置为 Switch inputs 时的电路图 |

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `model_type` |
| **值：** | `Commanded phase voltage` (default) | `Switch inputs` |
| **数据类型：** | `character vector` |

### **Breakpoints for speeds (w), w\_eff\_bp** — 速度断点 `[-1000 -500 0 500 1000]` (default) | `1`-by-`M` vector

电机转速 *ωmtr*
断点向量，用于功率损耗，单位为 rad/s。如果设置 **Enable memory
optimized 2D LUT**，该模块会将数据转换为 single
precision。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff_bp` |
| **值：** | `[-1000 -500 0 500 1000]` (default) | `1`-by-`M` vector |
| **数据类型：** | `double` |

### **Resample storage size for w\_eff\_bp, n1** — 速度位大小 `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256`

速度断点存储大小，*n1*，dimensionless。该
模块根据存储大小对 **Corresponding power loss,
ploss\_table** 数据进行重采样。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `n1` |
| **值：** | `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D
LUT**。

### **Breakpoints for load input (T), T\_eff\_bp** — 转矩断点 `[-200 -100 0 100 200]` (default) | `1`-by-`N` vector

电机转矩 *Tmtr*
断点向量，用于功率损耗，单位为 N·m。如果设置 **Enable memory
optimized 2D LUT**，该模块会将数据转换为 single
precision。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff_bp` |
| **值：** | `[-200 -100 0 100 200]` (default) | `1`-by-`N` vector |
| **数据类型：** | `double` |

### **Resample storage size for T\_eff\_bp, n2** — 转矩位大小 `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256`

转矩断点存储大小，*n2*，dimensionless。该
模块根据存储大小对 **Corresponding power loss,
ploss\_table** 数据进行重采样。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `n2` |
| **值：** | `128` (default) | `2` | `4` | `8` | `16` | `32` | `64` | `256` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D
LUT**。

### **Breakpoints for temperature input, Temp\_eff\_bp** — 温度断点 `[213.15 293.15 373.15]` (default) | `1`-by-`L` vector

逆变器温度 *TempInvrtr*
断点向量，用于功率损耗，单位为 K。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_eff_bp` |
| **值：** | `[213.15 293.15 373.15]` (default) | `1`-by-`L` vector |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Input inverter
temperature**。

### **Corresponding power loss, ploss\_table** — 2D 查找表 `[1 0.999 0.989 0.997 0.996;0.995 0.994 0.993 0.992 0.991;0.990 0.989 0.988 0.987 0.986;0.985 0.984 0.983 0.982 0.981;0.980 0.979 0.978 0.977 0.976]` (default) | `M`-by-`N` array

功率损耗值数组，作为 `M` 个电机转速
*ωmtr* 和
`N` 个电机转矩
*Tmtr* 的函数，单位为 W。每个值
指定特定电机转速和电机转矩组合下的功率损耗。数组大小必须与速度和
转矩向量定义的维度匹配。

如果有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据虚拟
标定查找表。

如果设置 **Enable memory optimized 2D LUT**，该模块
会将数据转换为 single precision。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ploss_table` |
| **值：** | `M`-by-`N` array |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请清除 **Input inverter
temperature**。

### **Corresponding power loss, ploss\_table\_3d** — 3D 查找表 `M`-by-`N`-by-`L` array

功率损耗值数组，作为 `M` 个电机转速
*ωmtr*、`N`
个电机转矩 *Tmtr* 和
`L` 个电机温度
*TempInvrtr* 的函数，单位为 W。每个
值指定特定电机转速、电机转矩和温度组合下的功率损耗。数组大小必须与速度、转矩和温度向量定义的维度
匹配。

如果有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据虚拟
标定查找表。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ploss_table_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Input inverter
temperature**。

#### 指定外插

### **w\_eff\_bp max endpoint, u1max** — 速度断点 `1000` (default) | `scalar`

速度断点最大外插端点，*u1max*，
单位为 rad/s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u1max` |
| **值：** | `1000` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和
**Specify Extrapolation**。

### **w\_eff\_bp min endpoint, u1min** — 速度断点 `-1000` (default) | `scalar`

速度断点最小外插端点，*u1min*，
单位为 rad/s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u1min` |
| **值：** | `-1000` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和
**Specify Extrapolation**。

### **T\_eff\_bp max endpoint, u2max** — 转矩断点 `200` (default) | `scalar`

转矩断点最大外插端点，
*u2max*，单位为 rad/s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u2max` |
| **值：** | `200` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和
**Specify Extrapolation**。

### **T\_eff\_bp min endpoint, u2min** — 转矩断点 `-200` (default) | `scalar`

转矩断点最小外插端点，
*u2min*，单位为 rad/s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u2min` |
| **值：** | `-200` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和
**Specify Extrapolation**。

## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

三相电压源逆变器

Three-Phase Voltage Source Inverter 模块实现一个三相
电压源逆变器，为平衡
三相负载生成中性点电压命令。可为连续矢量
调制或逆变器开关输入信号配置电压开关函数。您可以将该模块并入
闭环模型以仿真功率逆变器。该模块控制理想开关
状态。

要启用适用于限制内存的代码生成目标的功率损耗计算，请选择 **Enable memory optimized 2D LUT**。点击
**Calibrate Maps**，以虚拟标定作为电机转矩和电机转速函数的逆变器功率损耗
查找表。

如果选择 **Input inverter temperature**，请点击
**Calibrate Maps**，以虚拟标定作为电机转矩、电机转速和逆变器温度函数的功率损耗表。不能为
3D 功率损耗查找表启用内存优化。

使用 **Switching voltage function**
参数来设置开关电压函数。

| 设置 | 实现 | 图示 |
| --- | --- | --- |
| **Commanded phase voltage** | 相 a、b、c 相对中性点电压命令输入。适用于连续正弦或空间矢量调制输入信号。 | 当参数 Switching voltage function 设置为 Commanded phase voltage 时的电路图 |
| **Switch inputs** (default) | 逆变器开关输入命令。适用于硬件在环 (HIL) 仿真。  逆变器开关 S1、S3 和 S5 使用 S2、S4 和 S6 的互补控制。 | 当参数 Switching voltage function 设置为 Switch inputs 时的电路图 |

### 虚拟标定

如果有 Model-Based Calibration Toolbox™，请点击 **Calibrate Maps**，以使用测量数据虚拟标定查找
表。该对话框将引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入此损耗数据。例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedInverterDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Input inverter temperature** 设置 | 所需数据 | | --- | --- | | `off` | - 电机转速，rad/s - 电机转矩，N·m - 功率损耗，W | | `on` | - 电机转速，rad/s - 电机转矩，N·m - 电机温度，K - 功率损耗，W |  在稳态工作条件下采集逆变器数据。数据应覆盖逆变器的转速、转矩和温度工作范围。  要筛选或编辑数据，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Data Editor。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合为高斯过程模型 (GPM)。  要评估或调整响应模型拟合，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox Model Browser。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 标定响应模型并生成已标定的表。  要评估或调整标定，请选择 **Edit in Application**。将打开 Model-Based Calibration Toolbox CAGE Browser。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定更新这些参数。  | **Input inverter temperature** 设置 | 参数 | | --- | --- | | `off` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Corresponding power loss,   ploss\_table** | | `on` | - **Breakpoints for speeds (w),   w\_eff\_bp** - **Breakpoints for load input (T),   T\_eff\_bp** - **Breakpoints for temperature input,   Temp\_eff\_bp** - **Corresponding power loss,   ploss\_table\_3d** | |

### 开关函数

对于开关电压，模块实现取决于
**Switching voltage function** 设置。

| 设置 | 计算 | 方程 |
| --- | --- | --- |
| `Commanded phase voltage` | 将连续相对中性点电压命令设置为相 a、b、c 相对中性点电压命令输入 | van=va\_cmdvbn=vb\_cmdvcn=vc\_cmd |
| 线电压 | vab= van− vbnvbc= vbn− vcnvca= vcn− van |
| `Switch inputs` | 开关函数 | SFa={1      S1 on and S2 off−1   S1 off and S2 onSFb={1      S3 on and S4 off−1   S3 off and S4 onSFc={1      S5 on and S6 off−1   S5 off and S6 on |
| 相对中心点电压 | vao= vbus2 SFavbo= vbus2 SFbvco= vbus2 SFc |
| 相对中性点电压 | van= vao− vnovbn= vbo− vnovcn= vco− vnovan+ vbn+ vcn= 0vno= 13(vao+ vbo+ vco)van= vao− 13(vao+ vbo+ vco)vbn= vbo−13(vao+ vbo+ vco)vcn= vco− 13(vao+ vbo+ vco) |
| 线电压 | vab= van− vbnvbc= vbn− vcnvca= vcn− van |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *SFa*, *SFb*, *SFc* | 分别为相 a、b、c 线路开关函数 |
| *vbus* | 电源总线电压 |
| *Vao*, *Vbo*, *Vco* | 分别为相 a、b、c 相对中心点电压 |
| *Van*, *Vbn*, *Vcn* | 分别为相 a、b、c 相对中性点电压 |
| *Vab*, *Vbc*, *Vca* | 分别为相 ab、bc、ca 相对中性点电压 |
| *Va\_cmd*, *Vb\_cmd*, *Vc\_cmd* | 分别为相 a、b、c 相对中性点电压命令 |

### 电流和功率损耗

对于相对中心点、相对中性点和线电压，模块
实现以下方程。

| 计算 | | 方程 |
| --- | --- | --- |
| 电机和总线功率 | | Pmtr= vania+vbnib+vcnicPbus= vbusibus |
| 逆变器功率损耗和总线电流 | | Pin= Pbus= vbusibusPout= Pmtr= vania+vbnib+vcnic+PLossInvibus= vania+vbnib+vcnic+PLossInv vbus |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Pmtr* | 传递给电机的功率 |
| *Pbus* | 来自输入总线的功率 |
| *Ploss* | 功率损耗 |
| *ibus* | 电源总线电流 |
| *ia*, *ib*, *ic* | 分别为相 a、b、c 线路电流 |
| *Van*, *Vbn*, *Vcn* | 分别为相 a、b、c 相对中性点电压 |
| *vbus* | 电源总线电压 |

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 传递给电机的功率 | *PTrnsfrdMtr* | PTrnsfrdMtr= −(vania+vbnib+vcnic ) |
| `PwrBus` | 来自输入总线的功率 | *PTrnsfrdBus* | PTrnsfrdBus= Pbus |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrLoss` | 功率损耗  负值表示功率损耗 | *PNotTrnsfrd* | PNotTrnsfrd= −(PTrnsfrdBus+PTrnsfrdMtr) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | | *未使用* | | |

### 查找表内存优化

逆变器功率损耗表参数 **Corresponding power loss,
ploss\_table** 的数据是不同电池电压下电机转矩和电机转速的函数。正电流表示电池放电。负
电流表示电池充电。

要启用适用于限制内存的代码生成目标的功率损耗计算，请选择 **Enable memory optimized 2D LUT**。该模块使用
线性插值来为代码生成优化逆变器功率损耗查找表值。下表总结了优化
实现。

| 用例 | | 实现 |
| --- | --- | --- |
| 电机转速和转矩输入与查找表断点值对齐。 | | 内存优化功率损耗是电机转速和转矩交点处的功率损耗查找表值。 |
| 电机转速和转矩输入与查找表断点值不对齐，但在范围内。 | | 内存优化功率损耗是相应电机转速和转矩之间的线性插值。 |
| 电机转速和转矩输入与查找表断点值不对齐，且超出范围。 | | 无法计算内存优化功率损耗。模块使用外插数据。 |

**外插**

为代码生成优化的查找表不支持对超出范围的数据进行外插。但是，您可以通过选择
**Specify Extrapolation** 在功率损耗查找表中包含预先计算的外插值。

该模块使用端点参数来调整表数据的大小。

| 用户输入 | 外插 |
| --- | --- |
| 用于外插以覆盖所需工作范围的查找表 | 显示的外插查找表以及原始表 |
