---
type: simulink-block
title: 'Mapped Motor'
family: 'powertrain'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Propulsion'
documentation_page: 'mappedmotor'
documentation_source_path: 'ref/mappedmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Mapped Motor

## 端口

### 输入

### **BattVolt** — 电池电压 scalar

供电电压，*BattVolt*，单位为 volts (DC)。

### **TrqCmd** — 命令电机扭矩 scalar

命令电机扭矩，*Trqcmd*，单位为 N·m。

### **LdTrq** — 电机负载扭矩 scalar

电机负载扭矩，*Tload*，单位为 N·m。

#### 依赖关系

要启用此端口，请将 **端口配置** 设置为 `Torque`。

### **MtrSpd** — 电机输出轴转速 scalar

电机轴转速，*Mtrspd*，单位为 rad/s。

#### 依赖关系

要启用此端口，请将 **端口配置** 设置为 `Speed`。
### 输出

### **Info** — 总线信号 bus

总线信号包含以下模块计算。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `MtrTrq` | | | 电机输出轴扭矩 | N·m |
| `MechPwr` | | | 机械功率 | W |
| `PwrLoss` | | | 逆变器和电机内部功率损耗 | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | W |
| `PwrBus` | 电功率 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 电机功率损耗 | W |
| `PwrStored` | `PwrStoredShft` | 电机储存功率 | W |

### **BattCurr** — 电池电流 scalar

供电电流消耗或需求，*Ibatt*，单位为 amperes (DC)。

### **MtrTrq** — 电机扭矩 scalar

电机输出轴扭矩，*Mtrtrq*，单位为 N·m。

#### 依赖关系

要启用此端口，请将 **端口配置** 设置为 `Speed`。

### **MtrSpd** — 电机轴转速 scalar

电机轴转速，*Mtrspd*，单位为 rad/s。

#### 依赖关系

要启用此端口，请将 **端口配置** 设置为 `Torque`。

## 参数

#### 模块选项

### **端口配置** — 端口配置 `Torque` (default) | `Speed`

此表总结了端口配置。

| 端口配置 | 启用的端口 |
| --- | --- |
| `Torque` | - 输入 `LdTrq` - 输出端口 `MtrSpd` |
| `Speed` | - 输入 `MtrSpd` - 输出端口 `MtrTrq` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Torque` (default) | `Speed` |
| **数据类型：** | `character vector` |

### **导入扭矩限制校准** — 直接导入扭矩限制校准表的方法选择

如果您有自己的扭矩-转速-电压包络校准，可以直接导入。此表逐步说明任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **电气扭矩** 选项卡上，将 **参数化依据** 设置为 `Tabulated torque-speed-voltage envelope`。 |
| 选择电气扭矩校准数据文件 | 导航到校准数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择校准数据文件，例如 `MotorCalibrationImportData.xlsx`。单击 **打开**。 |
| 导入扭矩限制数据 | 单击 **导入扭矩限制校准**。模块读取并导入电子表格 **MaxTorque** 和 **MinTorque** 选项卡中的数据。 |

### **校准映射** — 用测量数据校准损耗表的方法选择

如果您有 Model-Based Calibration Toolbox，可以虚拟校准 2-D 或 3-D 测量损耗查找表。

1. 在 **电气损耗** 选项卡上，将 **损耗参数化依据** 设置为以下之一：

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. 单击 **校准映射**。

对话框将逐步引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入损耗数据，例如打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **损耗参数化依据** | 所需数据 | | --- | --- | | `Tabulated loss data` | - 电机转速，rad/s - 电机扭矩，N·m - 功率损耗，W | | `Tabulated loss data with temperature` | - 电机转速，rad/s - 电机扭矩，N·m - 电机温度，K - 功率损耗，W |  在稳态运行条件下采集电机数据。数据应覆盖电机转速、扭矩和温度运行范围。要过滤或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用测试计划将数据拟合到高斯过程模型 (GPMs)。要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准表。要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准更新这些参数。  | **损耗参数化依据** | 参数 | | --- | --- | | `Tabulated loss data` | - **损耗的速度断点，   w\_eff\_bp** - **损耗的扭矩断点，   T\_eff\_bp** - **损耗表，   losses\_table** | | `Tabulated loss data with temperature` | - **损耗的速度断点，   w\_eff\_bp** - **损耗的扭矩断点，   T\_eff\_bp** - **损耗的温度断点，   Temp\_eff\_bp** - **损耗表，   losses\_table\_3d** | |

### **导入损耗校准** — 直接导入损耗校准表的方法选择

如果您有自己的相对于扭矩、转速、供电 DC 电压和温度的损耗校准，可以直接导入。此表逐步说明任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **电气损耗** 选项卡上，将 **损耗参数化依据** 设置为 `Tabulated loss data with temperature and voltage`。 |
| 选择校准数据文件 | 导航到校准数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择校准数据文件，例如 `MotorCalibrationImportData.xlsx`。单击 **打开**。 |
| 导入损耗数据 | 单击 **导入损耗校准**。模块读取并导入电子表格 **PowerLoss** 选项卡中的数据。 |

### **导入效率校准** — 直接导入效率校准表的方法选择

如果您有自己的相对于扭矩、转速、供电 DC 电压和温度的效率校准，可以直接导入。此表逐步说明任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **电气损耗** 选项卡上，将 **损耗参数化依据** 设置为 `Tabulated efficiency data with temperature and voltage`。 |
| 选择校准数据文件 | 导航到校准数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择校准数据文件，例如 `MotorCalibrationImportData.xlsx`。单击 **打开**。 |
| 导入效率数据 | 单击 **导入效率校准**。模块读取并导入电子表格 **Efficiency** 选项卡中的数据。 |

#### 电气扭矩

### **参数化依据** — 扭矩包络的参数化方法 `Tabulated torque-speed envelope` (default) | `Maximum torque and power` | `Tabulated torque-speed-voltage envelope`

| 设置 | 模块实现 |
| --- | --- |
| `Tabulated torque-speed envelope` | 范围指定为一组轴转速数据点及相应的最大扭矩值。最小扭矩设置为最大扭矩的负值。 |
| `Maximum torque and power` | 范围使用最大扭矩和最大功率值指定。 |
| `Tabulated torque-speed-voltage envelope` | 范围指定为一组转速和供电 DC 电压数据点及相应的最大和最小扭矩值。要直接导入您自己的扭矩限制校准表，请单击 **导入扭矩限制校准**。 |

对于这些方法中的任何一种，模块实现与本图中类似的扭矩包络。如果 **参数化依据** 设置为 `Tabulated torque-speed-voltage envelope`，则该包络将供电 DC 电压添加为第三轴。

扭矩包络与转速的关系图，指示允许的稳态运行

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `param_by` |
| **值：** | `Tabulated torque-speed envelope` (default) | `Maximum torque and power` | `Tabulated torque-speed-voltage envelope` |
| **数据类型：** | `character vector` |

### **最大扭矩的速度断点，w\_t** — 转速 `[0 375 750 800]` (default) | vector

跨越允许稳态范围的转速，单位为 rad/s。为避免因扭矩-转速曲线中的无限斜率导致性能不良，请指定不包含重复连续值的转速断点向量。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_t` |
| **值：** | `[0 375 750 800]` (default) | vector |
| **数据类型：** | `double` |

### **最大扭矩值，T\_t** — 扭矩 `[0.09 0.08 0.07 0]` (default) | vector

最大允许扭矩值，单位为 N·m。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_t` |
| **值：** | `[0.09 0.08 0.07 0]` (default) | vector |
| **数据类型：** | `double` |

### **最大扭矩，torque\_max** — 扭矩 `0.1` (default) | scalar

最大允许电机扭矩，单位为 N·m。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Maximum torque and power`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `torque_max` |
| **值：** | `0.1` (default) | scalar |
| **数据类型：** | `double` |

### **最大功率，power\_max** — 功率 `30` (default) | scalar

最大允许电机功率，单位为 W。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Maximum torque and power`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `power_max` |
| **值：** | `30` (default) | scalar |
| **数据类型：** | `double` |

### **扭矩控制时间常数，Tc** — 时间常数 `0.02` (default) | scalar

电机驱动器跟踪扭矩需求所用的时间常数，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tc` |
| **值：** | `0.02` (default) | scalar |
| **数据类型：** | `double` |

### **作为转速和电压函数的最大扭矩，Tmax\_w\_V** — 扭矩 `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]` (default) | vector

在给定的一组转速和供电 DC 电压断点处，包括符号的最大允许扭矩，单位为 N·m。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed-voltage envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmax_w_V` |
| **值：** | `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]` (default) | vector |
| **数据类型：** | `double` |

### **最大扭矩的速度断点，w\_Tmax\_bp** — 转速 `[ 0 375 750 800 ]` (default) | vector

每个最大扭矩值处的转速，单位为 rad/s。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed-voltage envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_Tmax_bp` |
| **值：** | `[ 0 375 750 800 ]` (default) | vector |
| **数据类型：** | `double` |

### **最大扭矩的电压断点，V\_Tmax\_bp** — 电压 `[ 500 750 900 ]` (default) | vector

每个最大扭矩值处的供电 DC 电压，单位为 volts (DC)。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed-voltage envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_Tmax_bp` |
| **值：** | `[ 500 750 900 ]` (default) | vector |
| **数据类型：** | `double` |

### **作为转速和电压函数的最小扭矩，Tmin\_w\_V** — 扭矩 `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]` (default) | vector

在给定的一组转速和供电 DC 电压断点处，包括符号的最小允许扭矩，单位为 N·m。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed-voltage envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmin_w_V` |
| **值：** | `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]` (default) | vector |
| **数据类型：** | `double` |

### **最小扭矩的速度断点，w\_Tmin\_bp** — 转速 `[ 0 375 750 800 ]` (default) | vector

每个最小扭矩值处的转速，单位为 rad/s。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed-voltage envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_Tmin_bp` |
| **值：** | `[ 0 375 750 800 ]` (default) | vector |
| **数据类型：** | `double` |

### **最小扭矩的电压断点，V\_Tmin\_bp** — 电压 `[ 500 750 900 ]` (default) | vector

每个最小扭矩值处的供电 DC 电压，单位为 volts (DC)。

#### 依赖关系

要创建此参数，请在 **参数化依据** 中选择 `Tabulated torque-speed-voltage envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_Tmin_bp` |
| **值：** | `[ 500 750 900 ]` (default) | vector |
| **数据类型：** | `double` |

#### 电气损耗

### **按以下方式参数化损耗** — 电气损耗的参数化方法 `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage`

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用三个损耗项计算效率。一项是常数，在零速度和零扭矩下测量：    - 与扭矩和速度无关的固定损耗，   *P*0。使用   *P*0 来考虑   固定变换器损耗。    两项取决于运行条件。模块根据在效率设定点测得的效率 *η*0 确定它们的系数，其中电机扭矩为 *τ*0，电机速度为 *ω*0：    - 与扭矩相关的电气损耗 *k**τ*2，其中   *k* 是常数，   且 *τ* 是扭矩。该项表示   铜绕组中的欧姆损耗。 - 与速度相关的电气损耗 *kw**ω*2，其中   *kw* 是   常数，且 *ω* 是速度。该项   表示由涡流引起的铁耗。 |
| `Tabulated loss data` | 作为电机速度和负载扭矩的函数的损耗校准查找表。  如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，以使用测量数据虚拟校准 2-D 查找表。 |
| `Tabulated loss data with temperature` | 作为电机速度、负载扭矩和运行温度的函数的损耗校准查找表。  如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，以使用测量数据虚拟校准 3-D 查找表。 |
| `Tabulated loss data with temperature and voltage` | 作为负载扭矩、电机速度、提供的直流电压和运行温度的函数的损耗校准查找表。  要直接导入您自己的 4-D 损耗校准表，请点击 **Import Loss Calibration**。 |
| `Tabulated efficiency data` | 作为电机速度和负载扭矩的函数的 2-D 效率校准查找表。模块：  - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零速度或零扭矩提供的效率值。当扭矩或速度为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低速度和低扭矩值提供表格化数据，以便在较低功率条件下获得所需的精度水平。 - 对于超出表范围的转速和扭矩量值，不外推损耗值。 |
| `Tabulated efficiency data with temperature` | 作为电机速度、负载扭矩和运行温度的函数的 3-D 效率校准查找表。模块：    - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零速度或零扭矩提供的效率值。当扭矩或速度为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低速度和低扭矩值提供表格化数据，以便在较低功率条件下获得所需的精度水平。 - 对于超出表范围的转速、扭矩或温度量值，不外推损耗值。 |
| `Tabulated efficiency data with temperature and voltage` | 作为负载扭矩、电机速度、提供的直流电压和运行温度的函数的效率校准查找表。  要直接导入您自己的 4-D 效率校准表，请点击 **Import Efficiency Calibration**。模块：  - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零速度或零扭矩提供的效率值。当扭矩或速度为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低速度和低扭矩值提供表格化数据，以便在较低功率条件下获得所需的精度水平。 - 对于超出表范围的转速、扭矩、温度或电压量值，不外推损耗值。 |

作为最佳实践，使用 `Tabulated loss data`、`Tabulated loss data with temperature` 或 `Tabulated loss data with temperature and voltage`，而不是 `Tabulated efficiency data`、`Tabulated efficiency data with temperature` 或 `Tabulated efficiency data with temperature and voltage`：

- 对于零速度或零扭矩，效率会变得没有良好定义。
- 您可以考虑在零速度或扭矩时仍然存在的固定损耗。

**注意**

由于损耗，当电机扭矩为零时，电机驱动系统可能会汲取电流。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `param_loss` |
| **值：** | `Single efficiency measurement` (default) | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage` |
| **数据类型：** | `character vector` |

### **电机和驱动器总体效率, eff** — 电机和电机驱动器的组合效率 *η*0，在效率设定点测量，单位为 percent `100` (default) | scalar

在效率设定点，电机扭矩为 *τ*0，电机速度为 *ω*0。在此条件下测得的效率为 *η*0。

模块将运行期间的总体效率百分比定义为：

η=100τωτω+P0+kτ2+kwω2

该方程使用以下变量。

|  |  |
| --- | --- |
| *τ* | 电机扭矩 |
| *ω* | 电机速度 |
| *P*0 | 与扭矩或速度无关的固定损耗，在零电机扭矩和速度下测量的基础损耗 |
| kτ2 | 与扭矩相关的电气损耗 |
| *kw**ω2* | 与速度相关的铁耗，*PIron* = *kw**ω2* |

初始化时，模块使用在效率设定点扭矩 *τ*0 和速度 *ω*0 下测得的铁耗，根据铁耗方程设置 *kw* 的值：

PIron,0=kwω02

然后，模块使用在效率设定点测得的效率值 *η*0，根据效率方程设置 *k* 的值：

η0=100τ0ω0τ0ω0+P0+kτ02+kwω02

模块忽略与转子阻尼相关的损耗。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eff` |
| **值：** | `100` (default) | scalar |
| **数据类型：** | `double` |

### **测量效率时的速度, w\_eff** — 速度 `375` (default) | scalar

在效率设定点的电机速度 *ω0*，单位为 rad/s。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff` |
| **值：** | `375` (default) | scalar |
| **数据类型：** | `double` |

### **测量效率时的扭矩, T\_eff** — 扭矩 `0.08` (default) | scalar

在效率设定点的扭矩 *τ0*，单位为 N·m。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff` |
| **值：** | `0.08` (default) | scalar |
| **数据类型：** | `double` |

### **铁耗, Piron** — 功率 `0` (default) | scalar

在效率设定点的铁耗 *PIron*,0，单位为 W。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Piron` |
| **值：** | `0` (default) | scalar |
| **数据类型：** | `double` |

### **与扭矩和速度无关的固定损耗, Pbase** — 功率 `0` (default) | scalar

与电机驱动器相关的功率损耗的恒定分量 *P*0，在零扭矩和速度下评估，单位为 W。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pbase` |
| **值：** | `0` (default) | scalar |
| **数据类型：** | `double` |

### **损耗的速度断点, w\_eff\_bp** — 断点 `[-800 -400 0 400 800]` (default) | `1`-by-`M` vector

损耗查找表的速度断点，单位为 rad/s。数组维度为 `1` × 速度断点数 `M`。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择以下选项之一：

- `Tabulated loss data`
- `Tabulated loss data with temperature`
- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data`
- `Tabulated efficiency data with temperature`
- `Tabulated efficiency data with temperature and voltage`

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff_bp` |
| **值：** | `[-800 -400 0 400 800]` (default) | `1`-by-`M` vector |
| **数据类型：** | `double` |

### **损耗的扭矩断点, T\_eff\_bp** — 断点 `[0 0.03 0.06 0.09]` (default) | `1`-by-`N` vector

损耗查找表的扭矩断点，单位为 N·m。数组维度为 `1` × 扭矩断点数 `N`。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择以下选项之一：

- `Tabulated loss data`
- `Tabulated loss data with temperature`
- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data`
- `Tabulated efficiency data with temperature`
- `Tabulated efficiency data with temperature and voltage`

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff_bp` |
| **值：** | `[0 0.03 0.06 0.09]` (default) | `1`-by-`N` vector |
| **数据类型：** | `double` |

### **损耗的温度断点, Temp\_eff\_bp** — 断点 `[233.15 293.15 373.15]` (default) | `1`-by-`L` vector

损耗查找表的温度断点，单位为 K。数组维度为 `1` × 温度断点数 `L`。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择以下选项之一：

- `Tabulated loss data with temperature`
- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data with temperature`
- `Tabulated efficiency data with temperature and voltage`

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_eff_bp` |
| **值：** | `[233.15 293.15 373.15]` (default) | `1`-by-`L` vector |
| **数据类型：** | `double` |

### **损耗的电压断点, V\_eff\_bp** — 断点 `[500 700 900]` (default) | `1`-by-`K` vector

损耗查找表的电压断点，单位为 volts。数组维度为 `1` × 电压断点数 `K`。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择以下选项之一：

- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data with temperature and voltage`

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_eff_bp` |
| **值：** | `[500 700 900]` (default) | `1`-by-`K` vector |
| **数据类型：** | `double` |

### **损耗表, losses\_table** — 2-D 查找表 `M`-by-`N` matrix

作为速度和扭矩的函数的电气损耗值数组，单位为 W。每个值指定特定速度与扭矩组合下的损耗。数组维度必须与速度 `M` 和扭矩 `N` 的断点向量维度匹配。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Tabulated loss data`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

### **损耗表, losses\_table\_3d** — 3-D 查找表 `M`-by-`N`-by-`L` array

作为速度、扭矩和温度的函数的电气损耗值数组，单位为 W。每个值指定特定速度、扭矩和温度组合下的损耗。数组维度必须与速度 `M`、扭矩 `N` 和温度 `L` 的断点向量维度匹配。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Tabulated loss data with temperature`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

### **损耗表, losses\_table\_4d** — 4-D 查找表 `N`-by-`M`-by-`K`-by-`L` array

作为速度、扭矩、温度和提供的直流电压的函数的电气损耗值数组，单位为 W。每个值指定特定速度、扭矩、温度和提供的直流电压组合下的损耗。数组维度必须与扭矩 `N`、速度 `M`、电压 `K` 和温度 `L` 的断点向量维度匹配。

#### 依赖项

要创建此参数，请在 **按以下方式参数化损耗** 中，选择 `Tabulated loss data with temperature and voltage`。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table_4d` |
| **值：** | `N`-by-`M`-by-`K`-by-`L` array |
| **数据类型：** | `double` |

### **效率表, efficiency\_table** — 二维查找表 `M`-by-`N` matrix

效率数组，作为转速和转矩的函数，以 percent 为单位。每个值指定特定转速和转矩组合下的损耗。数组维度必须与转速 `M` 和转矩 `N` 的断点向量维度匹配。

该模块忽略零转速或零转矩的效率值。当转矩或转速为零时，损耗为零。该模块使用线性插值。

为了在较低功率条件下获得所需的精度，您可以为低转速和低转矩值提供表格化数据。

#### 依赖项

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

### **效率表, efficiency\_table\_3d** — 三维查找表 `M`-by-`N`-by-`L` array

效率数组，作为转速、转矩和温度的函数，以 percent 为单位。每个值指定特定转速、转矩和温度组合下的损耗。数组维度必须与转速 `M`、转矩 `N` 和温度 `L` 的断点向量维度匹配。

该模块忽略零转速或零转矩的效率值。当转矩或转速为零时，损耗为零。该模块使用线性插值。

为了在较低功率条件下获得所需的精度，您可以为低转速和低转矩值提供表格化数据。

#### 依赖项

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data with temperature`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `character vector` |

### **效率表, efficiency\_table\_4d** — 四维查找表 `N`-by-`M`-by-`K`-by-`L` array

效率数组，作为转速、转矩、温度和供电 DC 电压的函数，以 percent 为单位。每个值指定特定转速、转矩、温度和供电 DC 电压组合下的损耗。数组维度必须与转矩 `N`、转速 `M`、电压 `K` 和温度 `L` 的断点向量维度匹配。

该模块忽略零转速或零转矩的效率值。当转矩或转速为零时，损耗为零。该模块使用线性插值。

为了在较低功率条件下获得所需的精度，您可以为低转速和低转矩值提供表格化数据。

#### 依赖项

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data with temperature and voltage`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table_4d` |
| **值：** | `N`-by-`M`-by-`K`-by-`L` array |
| **数据类型：** | `double` |

#### 机械

### **转子惯量, J** — 惯量 `5e-6` (default) | scalar

转子对角速度变化的阻力，单位为 kg·m2。您可以将值设置为零。

#### 依赖项

要创建此参数，将 **Port configuration** 设置为 `Torque`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J` |
| **值：** | `5e-6` (default) | scalar |
| **数据类型：** | `double` |

### **转子阻尼, b** — 阻尼 `1e-5` (default) | scalar

转子阻尼，单位为 N·m/(rad/s)。您可以将值设置为零。

#### 依赖项

要创建此参数，将 **Port configuration** 设置为 `Torque`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b` |
| **值：** | `1e-5` (default) | scalar |
| **数据类型：** | `double` |

### **初始转子转速, omega\_o** — 速度 `0` (default) | scalar

仿真开始时的转子转速，单位为 rad/s。

#### 依赖项

要创建此参数，将 **Port configuration** 设置为 `Torque`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_o` |
| **值：** | `0` (default) | scalar |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters Vehicle Dynamics Blockset / Powertrain / Propulsion

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2025a：导入电机负载转矩

R2025a 引入了电机负载转矩输入端口 `LdTrq`。要启用该端口，将 **Port configuration** 设置为 `Torque`。

电机输出轴转矩 `MtrTrq` 在 Info 总线中输出。

### R2024b：直接为映射电机导入校准表

从 R2024b 开始，为改进校准工作流，您可以将映射电机校准表直接导入 Mapped Motor 模块，作为以下四个参数的函数：

- 电机转矩
- 电机转速
- 供电电压
- 电机温度

在模块掩码上，将 **Port Configuration** 设置为 `Torque`，点击 **Electrical Losses** 选项卡，并将 **Parameterize losses by:** 设置为 `Tabulated loss data with temperature and voltage`。然后，点击 **Import Calibration**。

## 描述

工作在转矩控制模式下的映射电机和驱动电子设备

Mapped Motor 模块实现工作在转矩控制模式下的映射电机和驱动电子设备。输出转矩跟踪转矩参考需求，同时包含电机和电机驱动器的组合时间常数。当您不知道电机的详细物理参数时，例如进行电机功率和转矩权衡研究时，可使用该模块进行快速系统级仿真。根据您的需要，可以使用具有不同详细程度的映射表。

您可以指定：

- Port configuration — 输入转矩或电机轴转速。
- Electrical torque range — 通过转矩-转速包络、最大电机功率和转矩，或转矩-转速-电压包络进行参数化。如果您有自己的转矩-转速-电压包络，可以直接导入。
- Electrical loss — 通过使用单个测量工作点、测量损耗表或测量效率表进行参数化。如果您有 Model-Based Calibration Toolbox™，可以虚拟校准测量损耗表。如果您有自己的校准表，可以直接导入。

在校准表中使用电压时，它均指供给电机驱动电子设备的 DC 电压。

### 电气转矩

要指定模块允许的转矩范围，在 **Electrical Torque** 选项卡上，对于 **Parameterized by**，选择以下选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Tabulated torque-speed envelope` | 范围指定为一组轴转速数据点及对应的最大转矩值。最小转矩设置为最大转矩的负值。 |
| `Maximum torque and power` | 范围使用最大转矩和最大功率值指定。 |
| `Tabulated torque-speed-voltage envelope` | 范围指定为一组转速和供电 DC 电压数据点及其对应的最大和最小转矩值。要直接导入您自己的转矩限值校准表，请点击 **Import Torque Limits Calibration**。 |

对于这些方法中的任何一种，模块实现的转矩包络类似于此图中的包络。如果 **Parameterized by** 设置为 `Tabulated torque-speed-voltage envelope`，则该包络将供电 DC 电压添加为第三个轴。

转矩包络随转速变化的图，指示允许的稳态运行

### 直接导入电气转矩

如果您有自己的转矩-转速-电压包络校准，可以直接导入。此表逐步说明任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **Electrical Torque** 选项卡上，将 **Parameterized by** 设置为 `Tabulated torque-speed-voltage envelope`。 |
| 选择电气转矩校准数据文件 | 导航到校准数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择校准数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入转矩限值数据 | 点击 **Import Torque Limits Calibration**。模块读取并导入电子表格 **MaxTorque** 和 **MinTorque** 选项卡中的数据。 |

### 电气损耗

要指定电气损耗，在 **Electrical Losses** 选项卡上，对于 **Parameterize losses by**，选择以下选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用三个损耗项计算效率。一个项是常数，并在零转速和转矩下测量：    - 与转矩和转速无关的固定损耗 *P*0。使用 *P*0 来考虑固定转换器损耗。    两个项取决于运行条件。该模块根据在效率设定点测得的效率 *η*0 确定它们的系数，其中电机转矩为 *τ*0，电机转速为 *ω*0：    - 与转矩相关的电气损耗 *k**τ*2，其中 *k* 是常数，*τ* 是转矩。该项表示铜绕组中的欧姆损耗。 - 与转速相关的电气损耗 *kw**ω*2，其中 *kw* 是常数，*ω* 是转速。该项表示由涡流引起的铁损耗。 |
| `Tabulated loss data` | 损耗校准查找表，是电机转速和负载转矩的函数。如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据虚拟校准二维查找表。 |
| `Tabulated loss data with temperature` | 损耗校准查找表，是电机转速、负载转矩和运行温度的函数。如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据虚拟校准三维查找表。 |
| `Tabulated loss data with temperature and voltage` | 损耗校准查找表，是负载转矩、电机转速、供电 DC 电压和运行温度的函数。要直接导入您自己的四维损耗校准表，请点击 **Import Loss Calibration**。 |
| `Tabulated efficiency data` | 二维效率校准查找表，是电机转速和负载转矩的函数。该模块：  - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值来确定损耗。根据需要，为低转速和低转矩值提供表格化数据，以便在较低功率条件下获得所需的精度。 - 不会对超出表范围的转速和转矩幅值外推损耗值。 |
| `Tabulated efficiency data with temperature` | 三维效率校准查找表，是电机转速、负载转矩和运行温度的函数。该模块：    - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值来确定损耗。根据需要，为低转速和低转矩值提供表格化数据，以便在较低功率条件下获得所需的精度。 - 不会对超出表范围的转速、转矩或温度幅值外推损耗值。 |
| `Tabulated efficiency data with temperature and voltage` | 效率校准查找表，是负载转矩、电机转速、供电 DC 电压和运行温度的函数。要直接导入您自己的四维效率校准表，请点击 **Import Efficiency Calibration**。该模块：  - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值来确定损耗。根据需要，为低转速和低转矩值提供表格化数据，以便在较低功率条件下获得所需的精度。 - 不会对超出表范围的转速、转矩、温度或电压幅值外推损耗值。 |

作为最佳实践，使用 `Tabulated loss data`、`Tabulated loss data with temperature` 或 `Tabulated loss data with temperature and voltage`，而不是 `Tabulated efficiency data`、`Tabulated efficiency data with temperature` 或 `Tabulated efficiency data with temperature and voltage`：

- 对于零转速或零转矩，效率变得定义不明确。
- 您可以考虑在零转速或零转矩时仍然存在的固定损耗。

**注意**

由于损耗，当电机转矩为零时，电机驱动系统可能汲取电流。

### 电气损耗的虚拟标定

如果您有 Model-Based Calibration Toolbox，则可以虚拟标定 2-D 或 3-D 实测损耗查找表。

1. 在 **电气损耗** 选项卡上，将 **损耗参数化方式** 设置为以下任一值：

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. 点击 **标定映射**。

该对话框会逐步引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入损耗数据，例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`。有关详细信息，请参阅 使用数据（Model-Based Calibration Toolbox）。    | **损耗参数化方式** | 所需数据 | | --- | --- | | `Tabulated loss data` | - 电机转速, rad/s - 电机转矩, N·m - 功率损耗, W | | `Tabulated loss data with temperature` | - 电机转速, rad/s - 电机转矩, N·m - 电机温度, K - 功率损耗, W |  在稳态工况下采集电机数据。数据应覆盖电机转速、转矩和温度工作范围。  要筛选或编辑数据，请选择 **在应用程序中编辑**。将打开 Model-Based Calibration Toolbox 数据编辑器。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合到高斯过程模型 (GPMs)。要评估或调整响应模型拟合，请选择 **在应用程序中编辑**。将打开 Model-Based Calibration Toolbox 模型浏览器。有关详细信息，请参阅 模型评估（Model-Based Calibration Toolbox）。 |
| 生成标定 | Model-Based Calibration Toolbox 标定响应模型并生成标定表。要评估或调整标定，请选择 **在应用程序中编辑**。将打开 Model-Based Calibration Toolbox CAGE Browser。有关详细信息，请参阅 标定查找表（Model-Based Calibration Toolbox）。 |
| 更新模块参数 | 使用标定更新这些参数。  | **损耗参数化方式** | 参数 | | --- | --- | | `Tabulated loss data` | - **损耗速度断点,   w\_eff\_bp** - **损耗转矩断点,   T\_eff\_bp** - **损耗表,   losses\_table** | | `Tabulated loss data with temperature` | - **损耗速度断点,   w\_eff\_bp** - **损耗转矩断点,   T\_eff\_bp** - **损耗温度断点,   Temp\_eff\_bp** - **损耗表,   losses\_table\_3d** | |

### 直接导入电气损耗

如果您有自己的损耗标定数据（随转矩、转速、供电直流电压和温度变化），则可以直接导入它。此表逐步说明这些任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **电气损耗** 选项卡上，将 **损耗参数化方式** 设置为 `Tabulated loss data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **打开**。 |
| 导入损耗数据 | 点击 **导入损耗标定**。模块读取并导入电子表格 **PowerLoss** 选项卡中的数据。 |

### 直接导入电气效率

如果您有自己的效率标定数据（随转矩、转速、供电直流电压和温度变化），则可以直接导入它。此表逐步说明这些任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **电气损耗** 选项卡上，将 **损耗参数化方式** 设置为 `Tabulated efficiency data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **打开**。 |
| 导入效率数据 | 点击 **导入效率标定**。模块读取并导入电子表格 **Efficiency** 选项卡中的数据。 |

### 电池电流

模块使用机械功率、功率损耗和电池电压计算电池电流。正电流表示电池放电。负电流表示电池充电。

BattAmp=MechPwr+PwrLossBattVolt

该方程使用以下变量。

|  |  |
| --- | --- |
| *BattVolt* | 电机驱动电子设备的直流电压 |
| *MechPwr* | 机械功率 |
| *PwrLoss* | 功率损耗 |
| *BattCurr* | 电机驱动电子设备的直流电流 |

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 定义 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd`  - 正信号表示功率流入模块。 - 负信号表示功率流出模块。 | `PwrMtr` | 机械功率 | **端口配置** 设置：  - `Torque`: Pmot= Tloadω    - `Speed`: Pmot= −Teω | W |
| `PwrBus` | 电功率 | Pbus= BattVolt×BattAmp | W |
| `PwrNotTrnsfrd`  - 负信号表示功率以热的形式损失。 | `PwrLoss` | 电机功率损耗 — 包括电气损耗和机械损耗 | Ploss,total= PwrLoss+Pd，其中 Pd=−bω2 | W |
| `PwrStored`  - 正值表示动能增加。 | `PwrStoredShft` | 转子动能存储速率 | Pstored= Jω˙ω | W |

该方程使用以下变量。

|  |  |
| --- | --- |
| *Te* | 假设转子速度恒定时，施加到轴的电机转矩 |
| *Tload* | 电机转矩负载 |
| *ω* | 转子速度 |
| *b* | 旋转阻尼系数 |
| *J* | 转子惯量 |
| *Pd* | 与损耗表中任何损耗分开的阻尼损耗 |
| *Ploss,total* | 总热损耗，等于 `PwrNotTrnsfrd` |
