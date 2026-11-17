---
type: simulink-block
title: 'Mapped Motor'
family: 'propulsion'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors and Inverters'
documentation_page: 'mappedmotor'
documentation_source_path: 'ref/mappedmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Mapped Motor

## 端口

### 输入

### **BattVolt** — 电池电压标量

供电电压，*BattVolt*，单位为 volts (DC)。

### **TrqCmd** — 指令电机扭矩标量

指令电机扭矩，
*Trqcmd*，单位为 N·m。

### **LdTrq** — 电机负载扭矩标量

电机负载扭矩，*Tload*，单位为
N·m。

#### 依赖关系

要启用此端口，请将 **端口配置**
设置为 `Torque`。

### **MtrSpd** — 电机输出轴转速标量

电机轴转速，*Mtrspd*，
单位为 rad/s。

#### 依赖关系

要启用此端口，请将 **端口配置**
设置为 `Speed`。
### 输出

### **Info** — 总线信号 bus

总线信号包含以下模块计算。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `MtrTrq` | | | 电机输出轴扭矩 | N·m |
| `MechPwr` | | | 机械功率 | W |
| `PwrLoss` | | | 内部逆变器和电机功率损耗 | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | W |
| `PwrBus` | 电功率 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 电机功率损耗 | W |
| `PwrStored` | `PwrStoredShft` | 电机存储功率 | W |

### **BattCurr** — 电池电流标量

供电电流消耗或需求，
*Ibatt*，单位为 amperes
(DC)。

### **MtrTrq** — 电机扭矩标量

电机输出轴扭矩，
*Mtrtrq*，单位为 N·m。

#### 依赖关系

要启用此端口，请将 **端口配置**
设置为 `Speed`。

### **MtrSpd** — 电机轴转速标量

电机轴转速，*Mtrspd*，
单位为 rad/s。

#### 依赖关系

要启用此端口，请将 **端口配置**
设置为 `Torque`。

## 参数

#### 模块选项

### **端口配置** — 端口配置 `Torque`（默认） | `Speed`

下表总结了端口配置。

| 端口配置 | 启用的端口 |
| --- | --- |
| `Torque` | - 输入 `LdTrq` - 输出端口 `MtrSpd` |
| `Speed` | - 输入 `MtrSpd` - 输出端口 `MtrTrq` |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Torque`（默认） | `Speed` |
| **数据类型：** | `character vector` |

### **导入扭矩限制标定** — 直接导入扭矩限制标定表选择的方法

如果您有自己的扭矩-转速-电压包络标定，
可以直接导入。下表列出了任务步骤。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **Electrical Torque** 选项卡上，将 **Parameterized by** 设置为 `Tabulated torque-speed-voltage envelope`。 |
| 选择电气扭矩标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入扭矩限制数据 | 点击 **导入扭矩限制标定**。模块读取并导入电子表格 **MaxTorque** 和 **MinTorque** 选项卡中的数据。 |

### **标定映射** — 使用测量数据标定损耗表的方法选择

如果您有 Model-Based Calibration Toolbox，可以虚拟标定 2-D 或 3-D 测量损耗查找表。

1. 在 **Electrical Losses** 选项卡上，将 **Parameterize
   losses by** 设置为以下之一：

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. 点击 **标定映射**。

对话框将逐步引导完成这些任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入损耗数据，例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`。有关更多信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Parameterize losses by** | 所需数据 | | --- | --- | | `Tabulated loss data` | - Motor speed, rad/s - Motor torque, N·m - Power loss, W | | `Tabulated loss data with temperature` | - Motor speed, rad/s - Motor torque, N·m - Motor temperature, K - Power loss, W |  在稳态运行条件下采集电机数据。数据应覆盖电机转速、扭矩和温度工作范围。要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用测试计划将数据拟合到高斯过程模型（GPM）。要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关更多信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定响应模型并生成标定表。要评估或调整标定，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关更多信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定更新这些参数。  | **Parameterize losses by** | 参数 | | --- | --- | | `Tabulated loss data` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Loss table,   losses\_table** | | `Tabulated loss data with temperature` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Temperature breakpoints for   losses, Temp\_eff\_bp** - **Loss table,   losses\_table\_3d** | |

### **导入损耗标定** — 直接导入损耗标定表选择的方法

如果您有自己的损耗标定与扭矩、转速、
供电 DC 电压和温度的关系，可以直接导入。下表列出了
任务步骤。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated loss data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入损耗数据 | 点击 **导入损耗标定**。模块读取并导入电子表格 **PowerLoss** 选项卡中的数据。 |

### **导入效率标定** — 直接导入效率标定表选择的方法

如果您有自己的效率标定与扭矩、
转速、供电 DC 电压和温度的关系，可以直接导入。下表列出了
任务步骤。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated efficiency data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入效率数据 | 点击 **导入效率标定**。模块读取并导入电子表格 **Efficiency** 选项卡中的数据。 |

#### 电气扭矩

### **参数化依据** — 扭矩包络的参数化方法 `Tabulated torque-speed envelope`（默认） | `Maximum torque and power` | `Tabulated torque-speed-voltage envelope`

| 设置 | 模块实现 |
| --- | --- |
| `Tabulated torque-speed envelope` | 范围指定为一组轴转速数据点及对应的最大扭矩值。最小扭矩设置为最大扭矩的负值。 |
| `Maximum torque and power` | 范围使用最大扭矩和最大功率值指定。 |
| `Tabulated torque-speed-voltage envelope` | 范围指定为一组转速和供电 DC 电压数据点及其对应的最大和最小扭矩值。  要直接导入您自己的扭矩限制标定表，请点击 **导入扭矩限制标定**。 |

对于任何这些方法，模块实现类似于下图中的扭矩包络。如果 **参数化依据** 设置为
`Tabulated torque-speed-voltage envelope`，该包络
会将供电 DC 电压添加为第三轴。

扭矩包络与转速的关系图，指示允许的稳态运行

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `param_by` |
| **值：** | `Tabulated torque-speed envelope`（默认） | `Maximum torque and power` | `Tabulated torque-speed-voltage envelope` |
| **数据类型：** | `character vector` |

### **最大扭矩的速度断点，w\_t** — 转速 `[0 375 750 800]`（默认） | vector

跨越允许稳态范围的转速，单位为 rad/s。为
避免因扭矩-转速曲线中的无限斜率导致性能不佳，
请指定不包含重复连续值的转速断点向量。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_t` |
| **值：** | `[0 375 750 800]`（默认） | vector |
| **数据类型：** | `double` |

### **最大扭矩值，T\_t** — 扭矩 `[0.09 0.08 0.07 0]`（默认） | vector

最大允许扭矩值，单位为 N·m。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_t` |
| **值：** | `[0.09 0.08 0.07 0]`（默认） | vector |
| **数据类型：** | `double` |

### **最大扭矩，torque\_max** — 扭矩 `0.1`（默认） | scalar

最大允许电机扭矩，单位为 N·m。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Maximum torque and power`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `torque_max` |
| **值：** | `0.1`（默认） | scalar |
| **数据类型：** | `double` |

### **最大功率，power\_max** — 功率 `30`（默认） | scalar

最大允许电机功率，单位为 W。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Maximum torque and power`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `power_max` |
| **值：** | `30`（默认） | scalar |
| **数据类型：** | `double` |

### **扭矩控制时间常数，Tc** — 时间常数 `0.02`（默认） | scalar

电机驱动器跟踪扭矩需求的时间常数，单位为
s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tc` |
| **值：** | `0.02`（默认） | scalar |
| **数据类型：** | `double` |

### **作为转速和电压函数的最大扭矩，Tmax\_w\_V** — 扭矩 `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]`（默认） | vector

在给定的一组转速和
供电 DC 电压断点处，最大允许扭矩（含符号），单位为 N·m。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed-voltage
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmax_w_V` |
| **值：** | `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]`（默认） | vector |
| **数据类型：** | `double` |

### **最大扭矩的速度断点，w\_Tmax\_bp** — 转速 `[ 0 375 750 800 ]`（默认） | vector

每个最大扭矩值处的转速，单位为 rad/s。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed-voltage
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_Tmax_bp` |
| **值：** | `[ 0 375 750 800 ]`（默认） | vector |
| **数据类型：** | `double` |

### **最大扭矩的电压断点，V\_Tmax\_bp** — 电压 `[ 500 750 900 ]`（默认） | vector

每个最大扭矩值处的供电 DC 电压，单位为 volts (DC)。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed-voltage
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_Tmax_bp` |
| **值：** | `[ 500 750 900 ]`（默认） | vector |
| **数据类型：** | `double` |

### **作为转速和电压函数的最小扭矩，Tmin\_w\_V** — 扭矩 `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]`（默认） | vector

在给定的一组转速和
供电 DC 电压断点处，最小允许扭矩（含符号），单位为 N·m。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed-voltage
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmin_w_V` |
| **值：** | `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]`（默认） | vector |
| **数据类型：** | `double` |

### **最小扭矩的速度断点，w\_Tmin\_bp** — 转速 `[ 0 375 750 800 ]`（默认） | vector

每个最小扭矩值处的转速，单位为 rad/s。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed-voltage
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_Tmin_bp` |
| **值：** | `[ 0 375 750 800 ]`（默认） | vector |
| **数据类型：** | `double` |

### **最小扭矩的电压断点，V\_Tmin\_bp** — 电压 `[ 500 750 900 ]`（默认） | vector

每个最小扭矩值处的供电 DC 电压，单位为 volts (DC)。

#### 依赖关系

要创建此参数，对于 **参数化依据**，
选择 `Tabulated torque-speed-voltage
envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_Tmin_bp` |
| **值：** | `[ 500 750 900 ]`（默认） | vector |
| **数据类型：** | `double` |

#### 电气损耗

### **损耗参数化依据** — 电气损耗的参数化方法 `Single efficiency measurement`（默认） | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage`

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用三个损耗项计算效率。一个项是常数，并在零转速和扭矩下测量：    - 与扭矩和转速无关的固定损耗，   *P*0。使用   *P*0 来考虑   固定转换器损耗。    两个项取决于运行条件。模块根据在效率设定点测量的效率 *η*0 确定它们的系数，其中电机扭矩为 *τ*0，电机转速为 *ω*0：    - 扭矩相关电气损耗 *k**τ*2，其中 *k* 是常数，   *τ* 是扭矩。此项表示  铜绕组中的欧姆损耗。 - 转速相关电气损耗 *kw**ω*2，其中   *kw* 是   常数，*ω* 是转速。此项   表示由涡流引起的铁损耗。 |
| `Tabulated loss data` | 损耗标定查找表，是电机转速和负载扭矩的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **标定映射** 以使用测量数据虚拟标定 2-D 查找表。 |
| `Tabulated loss data with temperature` | 损耗标定查找表，是电机转速、负载扭矩和工作温度的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **标定映射** 以使用测量数据虚拟标定 3-D 查找表。 |
| `Tabulated loss data with temperature and voltage` | 损耗标定查找表，是负载扭矩、电机转速、供电 DC 电压和工作温度的函数。  要直接导入您自己的 4-D 损耗标定表，请点击 **导入损耗标定**。 |
| `Tabulated efficiency data` | 2-D 效率标定查找表，是电机转速和负载扭矩的函数。模块：  - 将您提供的效率值转换为损耗，  并使用表格化损耗进行仿真。 - 忽略您为零转速或零扭矩提供的效率值。  当扭矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低转速和低扭矩值提供  表格化数据，以获得较低功率条件下所需的精度。 - 对于超出表范围的转速和扭矩幅值，  不进行损耗值外推。 |
| `Tabulated efficiency data with temperature` | 3-D 效率标定查找表，是电机转速、负载扭矩和工作温度的函数。模块：    - 将您提供的效率值转换为损耗，  并使用表格化损耗进行仿真。 - 忽略您为零转速或零扭矩提供的效率值。  当扭矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低转速和低扭矩值提供  表格化数据，以获得较低功率条件下所需的精度。 - 对于超出表范围的转速、扭矩或温度幅值，  不进行损耗值外推。 |
| `Tabulated efficiency data with temperature and voltage` | 效率标定查找表，是负载扭矩、电机转速、供电 DC 电压和工作温度的函数。  要直接导入您自己的 4-D 效率标定表，请点击 **导入效率标定**。模块：  - 将您提供的效率值转换为损耗，  并使用表格化损耗进行仿真。 - 忽略您为零转速或零扭矩提供的效率值。当扭矩或转速为零时，  损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低转速和低扭矩值提供  表格化数据，以获得较低功率条件下所需的精度。 - 对于超出表范围的转速、扭矩、温度或电压幅值，  不进行损耗值外推。 |

作为最佳实践，请使用 `Tabulated loss data`、
`Tabulated loss data with temperature` 或 `Tabulated
loss data with temperature and voltage`，而不是 `Tabulated
efficiency data`、`Tabulated efficiency data with
temperature` 或 `Tabulated efficiency data with temperature and
voltage`：

- 效率在零转速或零扭矩时变得定义不明确。
- 您可以考虑在零转速或扭矩时仍然存在的固定损耗。

**注意**

由于损耗，当电机扭矩为零时，电机驱动系统可能消耗电流。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `param_loss` |
| **值：** | `Single efficiency measurement`（默认） | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage` |
| **数据类型：** | `character vector` |

### **电机和驱动整体效率，eff** — 电机和电机驱动在效率设定点测量的组合效率 *η*0，单位为 percent `100`（默认） | scalar

在效率设定点，电机扭矩为
*τ*0，电机转速为
*ω*0。在此条件下测量的
效率为 *η*0。

模块将运行期间的整体效率百分比定义为：

η=100τωτω+P0+kτ2+kwω2

该方程使用以下变量。

|  |  |
| --- | --- |
| *τ* | 电机扭矩 |
| *ω* | 电机转速 |
| *P*0 | 与扭矩或转速无关的固定损耗，在零电机扭矩和转速下作为基础损耗测量 |
| kτ2 | 扭矩相关电气损耗 |
| *kw**ω2* | 转速相关铁损耗，*PIron* = *kw**ω2* |

初始化时，模块根据铁损耗
方程，使用在效率设定点扭矩
*τ*0 和转速
*ω*0 下测量的铁损耗，设置
*kw* 的值：

PIron,0=kwω02

然后，模块根据效率
方程，使用在效率设定点测量的效率
*η*0 值，设置 *k* 的值：

η0=100τ0ω0τ0ω0+P0+kτ02+kwω02

模块忽略与转子阻尼相关的损耗。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Single efficiency
measurement`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eff` |
| **值：** | `100`（默认） | scalar |
| **数据类型：** | `double` |

### **测量效率时的转速，w\_eff** — 转速 `375`（默认） | scalar

效率设定点处的电机转速 *ω0*，单位为 rad/s。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Single efficiency
measurement`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff` |
| **值：** | `375`（默认） | scalar |
| **数据类型：** | `double` |

### **测量效率时的扭矩，T\_eff** — 扭矩 `0.08`（默认） | scalar

效率设定点处的扭矩 *τ0*，单位为 N·m。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Single efficiency
measurement`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff` |
| **值：** | `0.08`（默认） | scalar |
| **数据类型：** | `double` |

### **铁损耗，Piron** — 功率 `0`（默认） | scalar

效率设定点处的铁损耗
*PIron*,0
，单位为 W。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Single efficiency
measurement`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Piron` |
| **值：** | `0`（默认） | scalar |
| **数据类型：** | `double` |

### **与扭矩和转速无关的固定损耗，Pbase** — 功率 `0`（默认） | scalar

与电机驱动相关的功率损耗常数分量 *P*0，在零扭矩和转速下评估，单位为
W。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Single efficiency
measurement`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pbase` |
| **值：** | `0`（默认） | scalar |
| **数据类型：** | `double` |

### **损耗的速度断点，w\_eff\_bp** — 断点 `[-800 -400 0 400 800]`（默认） | `1`-by-`M` vector

损耗查找表的速度断点，单位为 rad/s。数组维度为
`1` 乘速度断点数量
`M`。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择以下选项之一：

- `Tabulated loss data`
- `Tabulated loss data with
  temperature`
- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency
  data`
- `Tabulated efficiency data with
  temperature`
- `Tabulated efficiency data with temperature
  and voltage`

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff_bp` |
| **值：** | `[-800 -400 0 400 800]`（默认） | `1`-by-`M` vector |
| **数据类型：** | `double` |

### **损耗的扭矩断点，T\_eff\_bp** — 断点 `[0 0.03 0.06 0.09]`（默认） | `1`-by-`N` vector

损耗查找表的扭矩断点，单位为 N·m。数组维度为
`1` 乘扭矩断点数量
`N`。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择以下选项之一：

- `Tabulated loss data`
- `Tabulated loss data with
  temperature`
- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency
  data`
- `Tabulated efficiency data with
  temperature`
- `Tabulated efficiency data with temperature
  and voltage`

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff_bp` |
| **值：** | `[0 0.03 0.06 0.09]`（默认） | `1`-by-`N` vector |
| **数据类型：** | `double` |

### **损耗的温度断点，Temp\_eff\_bp** — 断点 `[233.15 293.15 373.15]`（默认） | `1`-by-`L` vector

损耗查找表的温度断点，单位为 K。数组维度为
`1` 乘温度断点数量
`L`。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择以下选项之一：

- `Tabulated loss data with
  temperature`
- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency data with
  temperature`
- `Tabulated efficiency data with temperature
  and voltage`

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_eff_bp` |
| **值：** | `[233.15 293.15 373.15]`（默认） | `1`-by-`L` vector |
| **数据类型：** | `double` |

### **损耗的电压断点，V\_eff\_bp** — 断点 `[500 700 900]`（默认） | `1`-by-`K` vector

损耗查找表的电压断点，单位为 volts。数组维度为
`1` 乘电压断点数量
`K`。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择以下选项之一：

- `Tabulated loss data with temperature and
  voltage`
- `Tabulated efficiency data with temperature
  and voltage`

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_eff_bp` |
| **值：** | `[500 700 900]`（默认） | `1`-by-`K` vector |
| **数据类型：** | `double` |

### **损耗表，losses\_table** — 2-D 查找表 `M`-by-`N` matrix

电气损耗作为转速和扭矩函数的值的数组，
单位为 W。每个值指定特定转速和扭矩组合的损耗。数组维度必须与
转速 `M` 和扭矩 `N` 的断点向量维度匹配。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Tabulated loss
data`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

### **损耗表，losses\_table\_3d** — 3-D 查找表 `M`-by-`N`-by-`L` array

电气损耗作为转速、扭矩和温度函数的值的数组，单位为 W。每个值指定特定
转速、扭矩和温度组合的损耗。数组维度必须
与转速 `M`、
扭矩 `N` 和温度 `L` 的断点向量维度匹配。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Tabulated loss data with
temperature`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

### **损耗表，losses\_table\_4d** — 4-D 查找表 `N`-by-`M`-by-`K`-by-`L` array

电气损耗作为转速、扭矩、温度和供电 DC 电压函数的值的数组，单位为 W。每个值指定特定
转速、扭矩、温度和供电 DC 电压组合的损耗。数组维度必须与
扭矩 `N`、转速 `M`、电压
`K` 和温度 `L` 的断点向量维度匹配。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Tabulated loss data with
temperature and voltage`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table_4d` |
| **值：** | `N`-by-`M`-by-`K`-by-`L` array |
| **数据类型：** | `double` |

### **效率表，efficiency\_table** — 2-D 查找表 `M`-by-`N` matrix

效率作为转速和扭矩函数的值的数组，单位为 percent。每个
值指定特定转速和扭矩组合的损耗。
数组维度必须与转速
`M` 和扭矩 `N` 的断点向量维度匹配。

模块忽略零转速或零扭矩的效率值。当扭矩或转速为零时，损耗
为零。模块使用线性
插值。

要获得较低功率条件下所需的精度，您可以
为低转速和低扭矩值提供表格化数据。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Tabulated efficiency
data`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

### **效率表，efficiency\_table\_3d** — 3-D 查找表 `M`-by-`N`-by-`L` array

效率作为转速、扭矩和温度函数的值的数组，单位为
percent。每个值指定特定转速、扭矩和温度组合的损耗。数组维度必须与
转速 `M`、扭矩
`N` 和温度 `L` 的断点向量维度匹配。

模块忽略零转速或零扭矩的效率值。当扭矩或转速为零时，损耗
为零。模块使用线性
插值。

要获得较低功率条件下所需的精度，您可以
为低转速和低扭矩值提供表格化数据。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Tabulated efficiency data with
temperature`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `character vector` |

### **效率表，efficiency\_table\_4d** — 4-D 查找表 `N`-by-`M`-by-`K`-by-`L` array

效率作为转速、扭矩、温度和
供电 DC 电压函数的值的数组，单位为 percent。每个值指定特定转速、扭矩、温度和供电 DC 电压组合的损耗。
数组维度必须与扭矩
`N`、转速 `M`、电压
`K` 和温度 `L` 的断点向量维度匹配。

模块忽略零转速或零扭矩的效率值。当扭矩或转速为零时，损耗
为零。模块使用线性
插值。

要获得较低功率条件下所需的精度，您可以
为低转速和低扭矩值提供表格化数据。

#### 依赖关系

要创建此参数，对于 **损耗参数化
依据**，选择 `Tabulated efficiency data with
temperature and voltage`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table_4d` |
| **值：** | `N`-by-`M`-by-`K`-by-`L` array |
| **数据类型：** | `double` |

#### 机械

### **转子惯量，J** — 惯量 `5e-6`（默认） | scalar

转子对角速度变化的阻力，单位为
kg·m2。您可以将该值设置为零。

#### 依赖关系

要创建此参数，请将 **端口配置**
设置为 `Torque`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J` |
| **值：** | `5e-6`（默认） | scalar |
| **数据类型：** | `double` |

### **转子阻尼，b** — 阻尼 `1e-5`（默认） | scalar

转子阻尼，单位为 N·m/(rad/s)。您可以将该值设置为零。

#### 依赖关系

要创建此参数，请将 **端口配置**
设置为 `Torque`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b` |
| **值：** | `1e-5`（默认） | scalar |
| **数据类型：** | `double` |

### **初始转子转速，omega\_o** — 转速 `0`（默认） | scalar

仿真开始时的转子转速，单位为 rad/s。

#### 依赖关系

要创建此参数，请将 **端口配置**
设置为 `Torque`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_o` |
| **值：** | `0`（默认） | scalar |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters Vehicle Dynamics Blockset / Powertrain / Propulsion

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2025a：导入电机负载扭矩

R2025a 引入了电机负载扭矩输入端口 `LdTrq`。要
启用该端口，请将 **端口配置** 设置为
`Torque`。

电机输出轴扭矩 `MtrTrq` 在 Info
总线中输出。

### R2024b：直接导入映射电机的标定表

从 R2024b 开始，为改进标定工作流，您可以将
映射电机标定表直接导入 Mapped Motor 模块，作为以下四个参数的函数：

- 电机扭矩
- 电机转速
- 供电电压
- 电机温度

在模块封装上，将 **端口配置** 设置为
`Torque`，点击 **Electrical
Losses** 选项卡，并将 **Parameterize losses
by:** 设置为 `Tabulated loss data with temperature and
voltage`。然后，点击 **导入
标定**。

## 描述

在扭矩控制模式下运行的映射电机和驱动电子设备

Mapped Motor 模块实现在扭矩控制模式下运行的映射电机和驱动电子设备。输出扭矩跟踪扭矩参考需求，
同时包含组合电机和电机驱动的时间常数。当您不知道电机的详细物理参数时，例如进行电机功率和扭矩权衡研究时，可使用该模块
进行快速系统级仿真。根据您的
需求，可以使用具有不同详细程度的映射。

您可以指定：

- 端口配置 — 输入扭矩或电机轴转速。
- 电气扭矩范围 — 通过扭矩-转速包络、最大电机功率和扭矩或扭矩-转速-电压包络
  进行参数化。如果您有自己的扭矩-转速-电压包络，可以直接导入
  它。
- 电气损耗 — 通过单个测量工作点、测量损耗表或测量效率表
  进行参数化。如果您有 Model-Based Calibration Toolbox™，可以虚拟标定测量损耗表。如果
  您有自己的标定表，可以直接导入它。

标定表中使用电压时，均指供给电机驱动电子设备的 DC 电压。

### 电气扭矩

要指定模块允许的扭矩范围，请在 **Electrical
Torque** 选项卡上，对于 **Parameterized by**，选择以下
选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Tabulated torque-speed envelope` | 范围指定为一组轴转速数据点及对应的最大扭矩值。最小扭矩设置为最大扭矩的负值。 |
| `Maximum torque and power` | 范围使用最大扭矩和最大功率值指定。 |
| `Tabulated torque-speed-voltage envelope` | 范围指定为一组转速和供电 DC 电压数据点及其对应的最大和最小扭矩值。  要直接导入您自己的扭矩限制标定表，请点击 **导入扭矩限制标定**。 |

对于任何这些方法，模块实现类似于下图中的扭矩包络。如果 **Parameterized by** 设置为
`Tabulated torque-speed-voltage envelope`，该包络
会将供电 DC 电压添加为第三轴。

扭矩包络与转速的关系图，指示允许的稳态运行

### 电气扭矩的直接导入

如果您有自己的扭矩-转速-电压包络标定，
可以直接导入。下表列出了任务步骤。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **Electrical Torque** 选项卡上，将 **Parameterized by** 设置为 `Tabulated torque-speed-voltage envelope`。 |
| 选择电气扭矩标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入扭矩限制数据 | 点击 **导入扭矩限制标定**。模块读取并导入电子表格 **MaxTorque** 和 **MinTorque** 选项卡中的数据。 |

### 电气损耗

要指定电气损耗，请在 **Electrical Losses**
选项卡上，对于 **Parameterize losses by**，选择以下
选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用三个损耗项计算效率。一个项是常数，并在零转速和扭矩下测量：    - 与扭矩和转速无关的固定损耗，   *P*0。使用   *P*0 来考虑   固定转换器损耗。    两个项取决于运行条件。模块根据在效率设定点测量的效率 *η*0 确定它们的系数，其中电机扭矩为 *τ*0，电机转速为 *ω*0：    - 扭矩相关电气损耗 *k**τ*2，其中 *k* 是常数，   *τ* 是扭矩。此项表示  铜绕组中的欧姆损耗。 - 转速相关电气损耗 *kw**ω*2，其中   *kw* 是   常数，*ω* 是转速。此项   表示由涡流引起的铁损耗。 |
| `Tabulated loss data` | 损耗标定查找表，是电机转速和负载扭矩的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **标定映射** 以使用测量数据虚拟标定 2-D 查找表。 |
| `Tabulated loss data with temperature` | 损耗标定查找表，是电机转速、负载扭矩和工作温度的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **标定映射** 以使用测量数据虚拟标定 3-D 查找表。 |
| `Tabulated loss data with temperature and voltage` | 损耗标定查找表，是负载扭矩、电机转速、供电 DC 电压和工作温度的函数。  要直接导入您自己的 4-D 损耗标定表，请点击 **导入损耗标定**。 |
| `Tabulated efficiency data` | 2-D 效率标定查找表，是电机转速和负载扭矩的函数。模块：  - 将您提供的效率值转换为损耗，  并使用表格化损耗进行仿真。 - 忽略您为零转速或零扭矩提供的效率值。  当扭矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低转速和低扭矩值提供  表格化数据，以获得较低功率条件下所需的精度。 - 对于超出表范围的转速和扭矩幅值，  不进行损耗值外推。 |
| `Tabulated efficiency data with temperature` | 3-D 效率标定查找表，是电机转速、负载扭矩和工作温度的函数。模块：    - 将您提供的效率值转换为损耗，  并使用表格化损耗进行仿真。 - 忽略您为零转速或零扭矩提供的效率值。  当扭矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低转速和低扭矩值提供  表格化数据，以获得较低功率条件下所需的精度。 - 对于超出表范围的转速、扭矩或温度幅值，  不进行损耗值外推。 |
| `Tabulated efficiency data with temperature and voltage` | 效率标定查找表，是负载扭矩、电机转速、供电 DC 电压和工作温度的函数。  要直接导入您自己的 4-D 效率标定表，请点击 **导入效率标定**。模块：  - 将您提供的效率值转换为损耗，  并使用表格化损耗进行仿真。 - 忽略您为零转速或零扭矩提供的效率值。当扭矩或转速为零时，  损耗假定为零。 - 使用线性插值确定损耗。根据需要，为低转速和低扭矩值提供  表格化数据，以获得较低功率条件下所需的精度。 - 对于超出表范围的转速、扭矩、温度或电压幅值，  不进行损耗值外推。 |

作为最佳实践，请使用 `Tabulated loss data`、
`Tabulated loss data with temperature` 或 `Tabulated
loss data with temperature and voltage`，而不是 `Tabulated
efficiency data`、`Tabulated efficiency data with
temperature` 或 `Tabulated efficiency data with temperature and
voltage`：

- 效率在零转速或零扭矩时变得定义不明确。
- 您可以考虑在零转速或扭矩时仍然存在的固定损耗。

**注意**

由于损耗，当电机扭矩为零时，电机驱动系统可能消耗电流。

### 电气损耗的虚拟标定

如果您有 Model-Based Calibration Toolbox，可以虚拟标定 2-D 或 3-D 测量损耗查找表。

1. 在 **Electrical Losses** 选项卡上，将 **Parameterize
   losses by** 设置为以下之一：

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. 点击 **标定映射**。

对话框将逐步引导完成这些任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入损耗数据，例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`。有关更多信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Parameterize losses by** | 所需数据 | | --- | --- | | `Tabulated loss data` | - Motor speed, rad/s - Motor torque, N·m - Power loss, W | | `Tabulated loss data with temperature` | - Motor speed, rad/s - Motor torque, N·m - Motor temperature, K - Power loss, W |  在稳态运行条件下采集电机数据。数据应覆盖电机转速、扭矩和温度工作范围。要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用测试计划将数据拟合到高斯过程模型（GPM）。要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关更多信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定响应模型并生成标定表。要评估或调整标定，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关更多信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定更新这些参数。  | **Parameterize losses by** | 参数 | | --- | --- | | `Tabulated loss data` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Loss table,   losses\_table** | | `Tabulated loss data with temperature` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Temperature breakpoints for   losses, Temp\_eff\_bp** - **Loss table,   losses\_table\_3d** | |

### 电气损耗的直接导入

如果您有自己的损耗标定与扭矩、转速、
供电 DC 电压和温度的关系，可以直接导入。下表列出了
任务步骤。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated loss data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入损耗数据 | 点击 **导入损耗标定**。模块读取并导入电子表格 **PowerLoss** 选项卡中的数据。 |

### 电气效率的直接导入

如果您有自己的效率标定与扭矩、
转速、供电 DC 电压和温度的关系，可以直接导入。下表列出了
任务步骤。

| 任务 | 描述 |
| --- | --- |
| 选择参数化 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated efficiency data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入效率数据 | 点击 **导入效率标定**。模块读取并导入电子表格 **Efficiency** 选项卡中的数据。 |

### 电池电流

模块使用机械功率、功率损耗和电池电压计算电池电流。正电流表示电池放电。负电流
表示电池充电。

BattAmp=MechPwr+PwrLossBattVolt

该方程使用以下变量。

|  |  |
| --- | --- |
| *BattVolt* | 输入电机驱动电子设备的 DC 电压 |
| *MechPwr* | 机械功率 |
| *PwrLoss* | 功率损耗 |
| *BattCurr* | 输入电机驱动电子设备的 DC 电流 |

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 定义 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd`  - 正信号表示功率流入模块。 - 负信号表示功率流出模块。 | `PwrMtr` | 机械功率 | **端口配置** 设置：  - `Torque`: Pmot= Tloadω    - `Speed`: Pmot= −Teω | W |
| `PwrBus` | 电功率 | Pbus= BattVolt×BattAmp | W |
| `PwrNotTrnsfrd`  - 负信号表示热损耗。 | `PwrLoss` | 电机功率损耗 — 包括电气和机械损耗 | Ploss,total= PwrLoss+PdWhere Pd=−bω2 | W |
| `PwrStored`  - 正值表示动能增加。 | `PwrStoredShft` | 转子动能存储速率 | Pstored= Jω˙ω | W |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Te* | 施加到轴的电机扭矩，假设转子转速恒定 |
| *Tload* | 电机扭矩负载 |
| *ω* | 转子转速 |
| *b* | 旋转阻尼系数 |
| *J* | 转子惯量 |
| *Pd* | 阻尼损耗，与损耗表中的任何损耗分开 |
| *Ploss,total* | 总热损耗，等于 `PwrNotTrnsfrd` |
