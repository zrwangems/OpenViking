---
type: simulink-block
title: 'Mapped Motor'
family: 'autoblks'
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
```yaml
ports:
- name: BattVolt
  summary: 电池电压标量
  direction: input
- name: TrqCmd
  summary: 指令电机转矩标量
  direction: input
- name: LdTrq
  summary: 电机负载转矩标量
  direction: input
- name: MtrSpd
  summary: 电机输出轴转速标量
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: BattCurr
  summary: 电池电流标量
  direction: output
- name: MtrTrq
  summary: 电机转矩标量
  direction: output
- name: MtrSpd
  summary: 电机轴转速标量
  direction: output
```

### 输入

### **BattVolt** — 电池电压标量

提供的电压，*BattVolt*，单位为伏特（DC）。

### **TrqCmd** — 指令电机转矩标量

指令电机转矩，*Trqcmd*，单位为 N·m。

### **LdTrq** — 电机负载转矩标量

电机负载转矩，*Tload*，单位为 N·m。

#### 依赖

要启用此端口，请将 **Port configuration** 设置为 `Torque`。

### **MtrSpd** — 电机输出轴转速标量

电机轴转速，*Mtrspd*，单位为 rad/s。

#### 依赖

要启用此端口，请将 **Port configuration** 设置为 `Speed`。

### 输出

### **Info** — 总线信号 bus

该总线信号包含以下模块计算量。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `MtrTrq` | | | 电机输出轴转矩 | N·m |
| `MechPwr` | | | 机械功率 | W |
| `PwrLoss` | | | 内部逆变器和电机功率损耗 | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | W |
| `PwrBus` | 电功率 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 电机功率损耗 | W |
| `PwrStored` | `PwrStoredShft` | 电机储能 | W |

### **BattCurr** — 电池电流标量

提供的电流消耗或需求，*Ibatt*，单位为安培（DC）。

### **MtrTrq** — 电机转矩标量

电机输出轴转矩，*Mtrtrq*，单位为 N·m。

#### 依赖

要启用此端口，请将 **Port configuration** 设置为 `Speed`。

### **MtrSpd** — 电机轴转速标量

电机轴转速，*Mtrspd*，单位为 rad/s。

#### 依赖

要启用此端口，请将 **Port configuration** 设置为 `Torque`。
## 参数
```yaml
parameters:
- name: Port configuration
  summary: 端口配置 Torque（默认）| Speed
  group: ''
  block_parameter: port_config
  values: Torque（默认）| Speed
- name: Import Torque Limits Calibration
  summary: 直接导入转矩限值标定表的方法选择
  group: ''
- name: Calibrate Maps
  summary: 使用测量数据选择来标定损耗表的方法
  group: ''
- name: Import Loss Calibration
  summary: 直接导入损耗标定表选择的方法
  group: ''
- name: Import Efficiency Calibration
  summary: 直接导入效率校准表选择的方法
  group: ''
- name: Parameterized by
  summary: 扭矩包络的参数化方法 Tabulated torque-speed envelope（默认）| Maximum torque and power | Tabulated torque-speed-voltage envelope
  group: ''
  block_parameter: param_by
  values: Tabulated torque-speed envelope（默认）| Maximum torque and power | Tabulated torque-speed-voltage envelope
- name: Speed breakpoints for maximum torque, w_t
  summary: 转速 [0 375 750 800]（默认）| 向量
  group: ''
  block_parameter: w_t
  values: '[0 375 750 800]（默认）| 向量'
- name: Maximum torque values, T_t
  summary: 扭矩 [0.09 0.08 0.07 0]（默认）| 向量
  group: ''
  block_parameter: T_t
  values: '[0.09 0.08 0.07 0]（默认）| 向量'
- name: Maximum torque, torque_max
  summary: 扭矩 0.1（默认）| 标量
  group: ''
  block_parameter: torque_max
  values: 0.1（默认） | 标量
- name: Maximum power, power_max
  summary: 功率 30（默认） | 标量
  group: ''
  block_parameter: power_max
  values: 30（默认） | 标量
- name: Torque control time constant, Tc
  summary: 时间常数 0.02（默认） | 标量
  group: ''
  block_parameter: Tc
  values: 0.02（默认） | 标量
- name: Maximum torque as a function of speed and voltage, Tmax_w_V
  summary: 转矩 [0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]（默认） | 向量
  group: ''
  block_parameter: Tmax_w_V
  values: '[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]（默认） | 向量'
- name: Speed breakpoints for maximum torque, w_Tmax_bp
  summary: 转速 [ 0 375 750 800 ]（默认） | 向量
  group: ''
  block_parameter: w_Tmax_bp
  values: '[ 0 375 750 800 ]（默认） | 向量'
- name: Voltage breakpoints for maximum torque, V_Tmax_bp
  summary: 电压 [ 500 750 900 ]（默认） | 向量
  group: ''
  block_parameter: V_Tmax_bp
  values: '[ 500 750 900 ]（默认） | 向量'
- name: Minimum torque as a function of speed and voltage, Tmin_w_V
  summary: 转矩 [-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]（默认） | 向量
  group: ''
  block_parameter: Tmin_w_V
  values: '[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]（默认）| 向量'
- name: 最小转矩的转速断点，w_Tmin_bp
  summary: 转速 [ 0 375 750 800 ]（默认）| 向量
  group: ''
  block_parameter: w_Tmin_bp
  values: '[ 0 375 750 800 ]（默认）| 向量'
- name: 最小转矩的电压断点，V_Tmin_bp
  summary: 电压 [ 500 750 900 ]（默认）| 向量
  group: ''
  block_parameter: V_Tmin_bp
  values: '[ 500 750 900 ]（默认）| 向量'
- name: Parameterize losses by
  summary: 电气损耗的参数化方法 Single efficiency measurement（默认） | Tabulated loss data | Tabulated loss data with temperature | Tabulated
    loss data with temperature and voltage | Tabulated efficiency data | Tabulated efficiency data with temperature | Tabulated
    efficiency data with temperature and voltage
  group: ''
  block_parameter: param_loss
  values: Single efficiency measurement（默认） | Tabulated loss data | Tabulated loss data with temperature | Tabulated loss
    data with temperature and voltage | Tabulated efficiency data | Tabulated efficiency data with temperature | Tabulated
    efficiency data with temperature and voltage
- name: 电机和驱动器的总效率，eff
  summary: 电机和电机驱动器的组合效率 *η*0，在效率设定点处测量，以百分比表示 100（默认） | 标量
  group: ''
  block_parameter: eff
  values: 100（默认） | 标量
- name: 测量效率时的转速，w_eff
  summary: 转速 375（默认） | 标量
  group: ''
  block_parameter: w_eff
  values: 375（默认） | 标量
- name: 测量效率时的转矩，T_eff
  summary: 转矩 0.08（默认） | 标量
  group: ''
  block_parameter: T_eff
  values: 0.08（默认） | 标量
- name: 铁损耗，Piron
  summary: 功率 0（默认） | 标量
  group: ''
  block_parameter: Piron
  values: 0（默认） | 标量
- name: Fixed losses independent of torque and speed, Pbase
  summary: 功率 0（默认） | 标量
  group: ''
  block_parameter: Pbase
  values: 0（默认） | 标量
- name: Speed breakpoints for losses, w_eff_bp
  summary: 断点 [-800 -400 0 400 800]（默认） | 1×M 向量
  group: ''
  block_parameter: w_eff_bp
  values: '[-800 -400 0 400 800]（默认） | 1×M 向量'
- name: Torque breakpoints for losses, T_eff_bp
  summary: 断点 [0 0.03 0.06 0.09]（默认） | 1×N 向量
  group: ''
  block_parameter: T_eff_bp
  values: '[0 0.03 0.06 0.09]（默认） | 1×N 向量'
- name: Temperature breakpoints for losses, Temp_eff_bp
  summary: 断点 [233.15 293.15 373.15]（默认） | 1×L 向量
  group: ''
  block_parameter: Temp_eff_bp
  values: '[233.15 293.15 373.15]（默认） | 1×L 向量'
- name: Voltage breakpoints for losses, V_eff_bp
  summary: 断点 [500 700 900]（默认）| 1×K 向量
  group: ''
  block_parameter: V_eff_bp
  values: '[500 700 900]（默认）| 1×K 向量'
- name: Loss table, losses_table
  summary: 二维查找表 M×N 矩阵
  group: ''
  block_parameter: losses_table
  values: M×N 矩阵
- name: Loss table, losses_table_3d
  summary: 三维查找表 M×N×L 数组
  group: ''
  block_parameter: losses_table_3d
  values: M×N×L 数组
- name: Loss table, losses_table_4d
  summary: 四维查找表 N×M×K×L 数组
  group: ''
  block_parameter: losses_table_4d
  values: N×M×K×L 数组
- name: Efficiency table, efficiency_table
  summary: 二维查找表 M×N 矩阵
  group: ''
  block_parameter: efficiency_table
  values: M×N 矩阵
- name: Efficiency table, efficiency_table_3d
  summary: 3-D lookup table M×N×L 数组
  group: ''
  block_parameter: efficiency_table_3d
  values: M×N×L 数组
- name: Efficiency table, efficiency_table_4d
  summary: 4-D lookup table N×M×K×L 数组
  group: ''
  block_parameter: efficiency_table_4d
  values: N×M×K×L 数组
- name: Rotor inertia, J
  summary: 惯性 5e-6（默认）| 标量
  group: ''
  block_parameter: J
  values: 5e-6（默认）| 标量
- name: Rotor damping, b
  summary: 阻尼 1e-5（默认）| 标量
  group: ''
  block_parameter: b
  values: 1e-5（默认）| 标量
- name: Initial rotor speed, omega_o
  summary: 转速 0（默认）| 标量
  group: ''
  block_parameter: omega_o
  values: 0（默认） | 标量
```

#### 模块选项

### **Port configuration** — 端口配置 `Torque`（默认）| `Speed`

下表总结了端口配置。

| 端口配置 | 启用的端口 |
| --- | --- |
| `Torque` | - 输入 `LdTrq` - 输出 `MtrSpd` |
| `Speed` | - 输入 `MtrSpd` - 输出 `MtrTrq` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **值**：| `Torque`（默认）| `Speed` |
| **Data Types:** | `character vector` |

### **Import Torque Limits Calibration** — 直接导入转矩限值标定表的方法选择

如果您有自己的转矩-转速-电压包络标定，可以直接导入。下表列出了操作步骤。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **Electrical Torque** 选项卡上，将 **Parameterized by** 设置为 `Tabulated torque-speed-voltage envelope`。 |
| 选择电转矩标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入转矩限值数据 | 点击 **Import Torque Limits Calibration**。模块将读取并导入电子表格 **MaxTorque** 和 **MinTorque** 选项卡中的数据。 |

### **Calibrate Maps** — 使用测量数据选择来标定损耗表的方法

如果您拥有 Model-Based Calibration Toolbox，您可以虚拟标定二维或三维实测损耗查找表。

1. 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为以下之一：

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. 点击 **Calibrate Maps**。

对话框将逐步引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入损耗数据，例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`。有关更多信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Parameterize losses by** | 所需数据 | | --- | --- | | `Tabulated loss data` | - Motor speed, rad/s - Motor torque, N·m - Power loss, W | | `Tabulated loss data with temperature` | - Motor speed, rad/s - Motor torque, N·m - Motor temperature, K - Power loss, W |  在稳态工况下采集电机数据。数据应覆盖电机转速、转矩和温度的运行范围。  要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合到高斯过程模型（GPM）。  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关更多信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定响应模型进行标定并生成标定表。  要评估或调整标定，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关更多信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定结果更新以下参数。  | **Parameterize losses by** | 参数 | | --- | --- | | `Tabulated loss data` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Loss table,   losses\_table** | | `Tabulated loss data with temperature` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Temperature breakpoints for   losses, Temp\_eff\_bp** - **Loss table,   losses\_table\_3d** | |

### **Import Loss Calibration** — 直接导入损耗标定表选择的方法

如果您拥有自己的损耗标定数据（与转矩、转速、供电直流电压和温度相关），您可以直接导入。此表将逐步引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated loss data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入损耗数据 | 点击 **Import Loss Calibration**。模块将读取并导入电子表格 **PowerLoss** 选项卡中的数据。 |

### **Import Efficiency Calibration** — 直接导入效率校准表选择的方法

如果您有自己的效率校准与扭矩、转速、供电直流电压和温度的关系数据，可以直接导入。此表逐步列出各项任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated efficiency data with temperature and voltage`。 |
| 选择校准数据文件 | 导航到校准数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择校准数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入效率数据 | 点击 **Import Efficiency Calibration**。模块读取并导入电子表格 **Efficiency** 选项卡中的数据。 |

#### Electrical Torque

### **Parameterized by** — 扭矩包络的参数化方法 `Tabulated torque-speed envelope`（默认）| `Maximum torque and power` | `Tabulated torque-speed-voltage envelope`

| 设置 | 模块实现 |
| --- | --- |
| `Tabulated torque-speed envelope` | 范围指定为一组轴转速数据点及其对应的最大扭矩值。最小扭矩设置为最大扭矩的负值。 |
| `Maximum torque and power` | 范围使用最大扭矩和最大功率值指定。 |
| `Tabulated torque-speed-voltage envelope` | 范围指定为一组转速和供电直流电压数据点及其对应的最大和最小扭矩值。要直接导入您自己的扭矩限值校准表，请点击 **Import Torque Limits Calibration**。 |

对于上述任一方法，模块实现的扭矩包络类似于下图中的包络。如果 **Parameterized by** 设置为 `Tabulated torque-speed-voltage envelope`，则该包络将供电直流电压添加为第三个轴。

扭矩包络与转速的关系图，指示允许的稳态运行范围

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `param_by` |
| **值**：| `Tabulated torque-speed envelope`（默认）| `Maximum torque and power` | `Tabulated torque-speed-voltage envelope` |
| **Data Types:** | `character vector` |

### **Speed breakpoints for maximum torque, w\_t** — 转速 `[0 375 750 800]`（默认）| 向量

跨越允许稳态范围的转速，单位为 rad/s。为避免因扭矩-转速曲线中的无限斜率导致性能不佳，请指定一个不包含重复连续值的转速断点向量。

#### 依赖关系

要创建此参数，请将 **Parameterized by** 选择为 `Tabulated torque-speed envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `w_t` |
| **值**：| `[0 375 750 800]`（默认）| 向量 |
| **Data Types:** | `double` |

### **Maximum torque values, T\_t** — 扭矩 `[0.09 0.08 0.07 0]`（默认）| 向量

最大允许扭矩值，单位为 N·m。

#### 依赖关系

要创建此参数，请将 **Parameterized by** 选择为 `Tabulated torque-speed envelope`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `T_t` |
| **值**：| `[0.09 0.08 0.07 0]`（默认）| 向量 |
| **Data Types:** | `double` |

### **Maximum torque, torque\_max** — 扭矩 `0.1`（默认）| 标量

最大允许电机扭矩，单位为 N·m。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Maximum torque and power`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `torque_max` |
| **值：** | `0.1`（默认） | 标量 |
| **数据类型：** | `double` |

### **Maximum power, power\_max** — 功率 `30`（默认） | 标量

最大允许电机功率，单位为 W。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Maximum torque and power`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `power_max` |
| **值：** | `30`（默认） | 标量 |
| **数据类型：** | `double` |

### **Torque control time constant, Tc** — 时间常数 `0.02`（默认） | 标量

电机驱动器跟踪转矩需求的时间常数，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tc` |
| **值：** | `0.02`（默认） | 标量 |
| **数据类型：** | `double` |

### **Maximum torque as a function of speed and voltage, Tmax\_w\_V** — 转矩 `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]`（默认） | 向量

在给定的一组转速和供电直流电压断点处，最大允许转矩（含符号），单位为 N·m。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Tabulated torque-speed-voltage envelope`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmax_w_V` |
| **值：** | `[0.09 0.09 0.09;0.08 0.08 0.08;0.07 0.07 0.07;0 0 0]`（默认） | 向量 |
| **数据类型：** | `double` |

### **Speed breakpoints for maximum torque, w\_Tmax\_bp** — 转速 `[ 0 375 750 800 ]`（默认） | 向量

每个最大转矩值对应的转速，单位为 rad/s。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Tabulated torque-speed-voltage envelope`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_Tmax_bp` |
| **值：** | `[ 0 375 750 800 ]`（默认） | 向量 |
| **数据类型：** | `double` |

### **Voltage breakpoints for maximum torque, V\_Tmax\_bp** — 电压 `[ 500 750 900 ]`（默认） | 向量

每个最大转矩值对应的供电直流电压，单位为伏特（DC）。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Tabulated torque-speed-voltage envelope`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_Tmax_bp` |
| **值：** | `[ 500 750 900 ]`（默认） | 向量 |
| **数据类型：** | `double` |

### **Minimum torque as a function of speed and voltage, Tmin\_w\_V** — 转矩 `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]`（默认） | 向量

在给定的一组转速和供电直流电压断点处，最小允许转矩（含符号），单位为 N·m。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Tabulated torque-speed-voltage envelope`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmin_w_V` |
| **值：** | `[-0.09 -0.09 -0.09;-0.08 -0.08 -0.08;-0.07 -0.07 -0.07;0 0 0]`（默认）| 向量 |
| **数据类型：** | `double` |

### **最小转矩的转速断点，w\_Tmin\_bp** — 转速 `[ 0 375 750 800 ]`（默认）| 向量

最小转矩各值对应的转速，单位为 rad/s。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Tabulated torque-speed-voltage envelope`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_Tmin_bp` |
| **值：** | `[ 0 375 750 800 ]`（默认）| 向量 |
| **数据类型：** | `double` |

### **最小转矩的电压断点，V\_Tmin\_bp** — 电压 `[ 500 750 900 ]`（默认）| 向量

最小转矩各值对应的供电直流电压，单位为伏特（DC）。

#### 依赖关系

要创建此参数，对于 **Parameterized by**，选择 `Tabulated torque-speed-voltage envelope`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_Tmin_bp` |
| **值：** | `[ 500 750 900 ]`（默认）| 向量 |
| **数据类型：** | `double` |

#### 电气损耗

### **Parameterize losses by** — 电气损耗的参数化方法 `Single efficiency measurement`（默认） | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage`

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用三个损耗项计算效率。一项为常数，在零转速和零转矩下测量：    - 与转矩和转速无关的固定损耗，*P*0。使用 *P*0 来考虑固定变换器损耗。    两项取决于运行条件。模块根据在效率设定点处测得的效率 *η*0 确定其系数，其中电机转矩为 *τ*0，电机转速为 *ω*0：    - 与转矩相关的电气损耗 *k**τ*2，其中 *k* 为常数，*τ* 为转矩。该项表示铜绕组中的欧姆损耗。 - 与转速相关的电气损耗 *kw**ω*2，其中 *kw* 为常数，*ω* 为转速。该项表示由涡流引起的铁损耗。 |
| `Tabulated loss data` | 损耗标定查找表，是电机转速和负载转矩的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据对二维查找表进行虚拟标定。 |
| `Tabulated loss data with temperature` | 损耗标定查找表，是电机转速、负载转矩和工作温度的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据对三维查找表进行虚拟标定。 |
| `Tabulated loss data with temperature and voltage` | 损耗标定查找表，是负载转矩、电机转速、供电直流电压和工作温度的函数。  要直接导入您自己的四维损耗标定表，请点击 **Import Loss Calibration**。 |
| `Tabulated efficiency data` | 二维效率标定查找表，是电机转速和负载转矩的函数。该模块：  - 将您提供的效率值转换为损耗，并在仿真中使用表格化损耗。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。请根据需要为低转速和低转矩值提供表格化数据，以获得较低功率条件下所需的精度水平。 - 不对超出表格范围的转速和转矩幅值外推损耗值。 |
| `Tabulated efficiency data with temperature` | 三维效率标定查找表，是电机转速、负载转矩和工作温度的函数。该模块：    - 将您提供的效率值转换为损耗，并在仿真中使用表格化损耗。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。请根据需要为低转速和低转矩值提供表格化数据，以获得较低功率条件下所需的精度水平。 - 不对超出表格范围的转速、转矩或温度幅值外推损耗值。 |
| `Tabulated efficiency data with temperature and voltage` | 效率标定查找表，是负载转矩、电机转速、供电直流电压和工作温度的函数。  要直接导入您自己的四维效率标定表，请点击 **Import Efficiency Calibration**。该模块：  - 将您提供的效率值转换为损耗，并在仿真中使用表格化损耗。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。请根据需要为低转速和低转矩值提供表格化数据，以获得较低功率条件下所需的精度水平。 - 不对超出表格范围的转速、转矩、温度或电压幅值外推损耗值。 |

作为最佳实践，请使用 `Tabulated loss data`、`Tabulated loss data with temperature` 或 `Tabulated loss data with temperature and voltage`，而不是 `Tabulated efficiency data`、`Tabulated efficiency data with temperature` 或 `Tabulated efficiency data with temperature and voltage`：

- 当转速为零或转矩为零时，效率变得无法定义。
- 您可以考虑在转速或转矩为零时仍然存在的固定损耗。

**注意**

由于存在损耗，当电机转矩为零时，电机驱动系统仍可能消耗电流。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `param_loss` |
| **值：** | `Single efficiency measurement`（默认） | `Tabulated loss data` | `Tabulated loss data with temperature` | `Tabulated loss data with temperature and voltage` | `Tabulated efficiency data` | `Tabulated efficiency data with temperature` | `Tabulated efficiency data with temperature and voltage` |
| **数据类型：** | `character vector` |

### **电机和驱动器的总效率，eff** — 电机和电机驱动器的组合效率 *η*0，在效率设定点处测量，以百分比表示 `100`（默认） | 标量

在效率设定点处，电机转矩为 *τ*0，电机转速为 *ω*0。在此条件下测得的效率为 *η*0。

该模块将运行期间的总效率百分比定义为：

η=100τωτω+P0+kτ2+kwω2

该方程使用以下变量。

|  |  |
| --- | --- |
| *τ* | 电机转矩 |
| *ω* | 电机转速 |
| *P*0 | 与转矩或转速无关的固定损耗，以零电机转矩和转速下的基础损耗来衡量 |
| kτ2 | 与转矩相关的电气损耗 |
| *kw**ω2* | 与转速相关的铁损耗，*PIron* = *kw**ω2* |

在初始化时，该模块根据铁损耗方程，使用在效率设定点转矩 *τ*0 和转速 *ω*0 处测得的铁损耗来设置 *kw* 的值：

PIron,0=kwω02

然后，该模块根据效率方程，使用在效率设定点处测得的效率值 *η*0 来设置 *k* 的值：

η0=100τ0ω0τ0ω0+P0+kτ02+kwω02

该模块忽略与转子阻尼相关的损耗。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eff` |
| **值：** | `100`（默认） | 标量 |
| **数据类型：** | `double` |

### **测量效率时的转速，w\_eff** — 转速 `375`（默认） | 标量

效率设定点处的电机转速 *ω0*，单位为 rad/s。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff` |
| **值：** | `375`（默认） | 标量 |
| **数据类型：** | `double` |

### **测量效率时的转矩，T\_eff** — 转矩 `0.08`（默认） | 标量

效率设定点处的转矩 *τ0*，单位为 N·m。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Single efficiency measurement`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff` |
| **值：** | `0.08`（默认） | 标量 |
| **数据类型：** | `double` |

### **铁损耗，Piron** — 功率 `0`（默认） | 标量

效率设定点处的铁损耗 *PIron*,0，单位为 W。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Single efficiency measurement`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Piron` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **Fixed losses independent of torque and speed, Pbase** — 功率 `0`（默认） | 标量

与电机驱动相关的功率损耗的恒定分量 *P*0，在零转矩和零转速下评估，单位为 W。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Single efficiency measurement`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pbase` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **Speed breakpoints for losses, w\_eff\_bp** — 断点 `[-800 -400 0 400 800]`（默认） | `1`×`M` 向量

损耗查找表的转速断点，单位为 rad/s。数组维度为 `1` 乘以转速断点数量 `M`。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择以下选项之一：

- `Tabulated loss data`
- `Tabulated loss data with temperature`
- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data`
- `Tabulated efficiency data with temperature`
- `Tabulated efficiency data with temperature and voltage`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff_bp` |
| **值：** | `[-800 -400 0 400 800]`（默认） | `1`×`M` 向量 |
| **数据类型：** | `double` |

### **Torque breakpoints for losses, T\_eff\_bp** — 断点 `[0 0.03 0.06 0.09]`（默认） | `1`×`N` 向量

损耗查找表的转矩断点，单位为 N·m。数组维度为 `1` 乘以转矩断点数量 `N`。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择以下选项之一：

- `Tabulated loss data`
- `Tabulated loss data with temperature`
- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data`
- `Tabulated efficiency data with temperature`
- `Tabulated efficiency data with temperature and voltage`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff_bp` |
| **值：** | `[0 0.03 0.06 0.09]`（默认） | `1`×`N` 向量 |
| **数据类型：** | `double` |

### **Temperature breakpoints for losses, Temp\_eff\_bp** — 断点 `[233.15 293.15 373.15]`（默认） | `1`×`L` 向量

损耗查找表的温度断点，单位为 K。数组维度为 `1` 乘以温度断点数量 `L`。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择以下选项之一：

- `Tabulated loss data with temperature`
- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data with temperature`
- `Tabulated efficiency data with temperature and voltage`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_eff_bp` |
| **值：** | `[233.15 293.15 373.15]`（默认） | `1`×`L` 向量 |
| **数据类型：** | `double` |

### **Voltage breakpoints for losses, V\_eff\_bp** — 断点 `[500 700 900]`（默认）| `1`×`K` 向量

损耗查找表的电压断点，单位为伏特。数组维度为 `1` 乘以电压断点数量 `K`。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择以下选项之一：

- `Tabulated loss data with temperature and voltage`
- `Tabulated efficiency data with temperature and voltage`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `V_eff_bp` |
| **值：** | `[500 700 900]`（默认）| `1`×`K` 向量 |
| **数据类型：** | `double` |

### **Loss table, losses\_table** — 二维查找表 `M`×`N` 矩阵

作为转速和转矩函数的电气损耗值数组，单位为 W。每个值指定特定转速和转矩组合下的损耗。数组维度必须与转速 `M` 和转矩 `N` 的断点向量维度匹配。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated loss data`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

### **Loss table, losses\_table\_3d** — 三维查找表 `M`×`N`×`L` 数组

作为转速、转矩和温度函数的电气损耗值数组，单位为 W。每个值指定特定转速、转矩和温度组合下的损耗。数组维度必须与转速 `M`、转矩 `N` 和温度 `L` 的断点向量维度匹配。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated loss data with temperature`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

### **Loss table, losses\_table\_4d** — 四维查找表 `N`×`M`×`K`×`L` 数组

作为转速、转矩、温度和供电直流电压函数的电气损耗值数组，单位为 W。每个值指定特定转速、转矩、温度和供电直流电压组合下的损耗。数组维度必须与转矩 `N`、转速 `M`、电压 `K` 和温度 `L` 的断点向量维度匹配。

#### 依赖关系

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated loss data with temperature and voltage`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table_4d` |
| **值：** | `N`×`M`×`K`×`L` 数组 |
| **数据类型：** | `double` |

### **Efficiency table, efficiency\_table** — 二维查找表 `M`×`N` 矩阵

作为转速和转矩函数的效率值数组，单位为百分比。每个值指定特定转速和转矩组合下的损耗。数组维度必须与转速 `M` 和转矩 `N` 的断点向量维度匹配。

模块忽略零转速或零转矩时的效率值。当转矩或转速为零时，损耗为零。模块使用线性插值。

为获得较低功率条件下所需的精度水平，您可以提供低转速和低转矩值的表格数据。

#### 依赖项

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

### **Efficiency table, efficiency\_table\_3d** — 3-D lookup table `M`×`N`×`L` 数组

效率随转速、转矩和温度变化的数组，以百分比表示。每个值指定了特定转速、转矩和温度组合下的损耗。数组维度必须与转速 `M`、转矩 `N` 和温度 `L` 的断点向量维度匹配。

模块忽略零转速或零转矩时的效率值。当转矩或转速为零时，损耗为零。模块使用线性插值。

为了在低功率条件下获得所需的精度水平，您可以提供低转速和低转矩值的表格数据。

#### 依赖项

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data with temperature`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `character vector` |

### **Efficiency table, efficiency\_table\_4d** — 4-D lookup table `N`×`M`×`K`×`L` 数组

效率随转速、转矩、温度和供电直流电压变化的数组，以百分比表示。每个值指定了特定转速、转矩、温度和供电直流电压组合下的损耗。数组维度必须与转矩 `N`、转速 `M`、电压 `K` 和温度 `L` 的断点向量维度匹配。

模块忽略零转速或零转矩时的效率值。当转矩或转速为零时，损耗为零。模块使用线性插值。

为了在低功率条件下获得所需的精度水平，您可以提供低转速和低转矩值的表格数据。

#### 依赖项

要创建此参数，对于 **Parameterize losses by**，选择 `Tabulated efficiency data with temperature and voltage`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table_4d` |
| **值：** | `N`×`M`×`K`×`L` 数组 |
| **数据类型：** | `double` |

#### 机械

### **Rotor inertia, J** — 惯性 `5e-6`（默认）| 标量

转子对角速度变化的阻力，单位为 kg·m2。您可以将该值设置为零。

#### 依赖项

要创建此参数，请将 **Port configuration** 设置为 `Torque`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J` |
| **值：** | `5e-6`（默认）| 标量 |
| **数据类型：** | `double` |

### **Rotor damping, b** — 阻尼 `1e-5`（默认）| 标量

转子阻尼，单位为 N·m/(rad/s)。您可以将该值设置为零。

#### 依赖项

要创建此参数，请将 **Port configuration** 设置为 `Torque`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b` |
| **值：** | `1e-5`（默认）| 标量 |
| **数据类型：** | `double` |

### **Initial rotor speed, omega\_o** — 转速 `0`（默认）| 标量

仿真开始时的转子转速，单位为 rad/s。

#### 依赖关系

要创建此参数，请将 **端口配置** 设置为 `Torque`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_o` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |
## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters Vehicle Dynamics Blockset / Powertrain / Propulsion

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2025a：导入电机负载转矩

R2025a 引入了电机负载转矩输入端口 `LdTrq`。要启用该端口，请将 **端口配置** 设置为 `Torque`。

电机输出轴转矩 `MtrTrq` 在 Info 总线中输出。

### R2024b：直接导入映射电机的标定表

从 R2024b 开始，为改进标定工作流，您可以将映射电机标定表直接导入 Mapped Motor 模块，作为以下四个参数的函数：

- 电机转矩
- 电机转速
- 供电电压
- 电机温度

在模块封装上，将 **端口配置** 设置为 `Torque`，点击 **电气损耗** 选项卡，并将 **损耗参数化方式：** 设置为 `带温度和电压的表格化损耗数据`。然后，点击 **导入标定**。

## 描述

在转矩控制模式下运行的映射电机和驱动电子设备

Mapped Motor 模块实现在转矩控制模式下运行的映射电机和驱动电子设备。输出转矩跟踪转矩参考需求，同时包含电机和电机驱动器的组合时间常数。当您不知道电机的详细物理参数时，例如进行电机功率和转矩权衡研究时，可使用该模块进行快速系统级仿真。根据您的需求，可以使用具有不同详细程度的映射表。

您可以指定：

- 端口配置 — 输入转矩或电机轴转速。
- 电气转矩范围 — 通过转矩-转速包络、最大电机功率和转矩，或转矩-转速-电压包络进行参数化。如果您有自己的转矩-转速-电压包络，可以直接导入。
- 电气损耗 — 通过单个测量工作点、测量损耗表或测量效率表进行参数化。如果您有 Model-Based Calibration Toolbox™，可以对测量损耗表进行虚拟标定。如果您有自己的标定表，可以直接导入。

标定表中使用电压的地方，均指提供给电机驱动电子设备的直流电压。

### 电气转矩

要指定模块允许的转矩范围，请在 **电气转矩** 选项卡上，为 **参数化方式** 选择以下选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `表格化转矩-转速包络` | 范围指定为一组轴转速数据点及其对应的最大转矩值。最小转矩设置为最大转矩的负值。 |
| `最大转矩和功率` | 范围使用最大转矩和最大功率值指定。 |
| `表格化转矩-转速-电压包络` | 范围指定为一组转速和供电直流电压数据点及其对应的最大和最小转矩值。要直接导入您自己的转矩限值标定表，请点击 **导入转矩限值标定**。 |

对于上述任何方法，模块实现的转矩包络类似于下图中的包络。如果 **参数化方式** 设置为 `表格化转矩-转速-电压包络`，则该包络将供电直流电压添加为第三个轴。

转矩包络与转速的关系图，指示允许的稳态运行区域

### 直接导入电气转矩

如果您有自己的转矩-转速-电压包络标定数据，可以直接导入。下表逐步列出了各项任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **Electrical Torque** 选项卡上，将 **Parameterized by** 设置为 `Tabulated torque-speed-voltage envelope`。 |
| 选择电气转矩标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入转矩限值数据 | 点击 **Import Torque Limits Calibration**。该模块读取并导入电子表格 **MaxTorque** 和 **MinTorque** 选项卡中的数据。 |

### Electrical Losses

要指定电气损耗，请在 **Electrical Losses** 选项卡上，对于 **Parameterize losses by**，选择以下选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用三个损耗项计算效率。一个项是常数，并在零转速和零转矩下测量：    - 与转矩和转速无关的固定损耗，*P*0。使用 *P*0 来考虑固定变流器损耗。    两个项取决于运行条件。模块根据在效率设定点测得的效率 *η*0 确定它们的系数，其中电机转矩为 *τ*0，电机转速为 *ω*0：    - 与转矩相关的电气损耗 *k**τ*2，其中 *k* 是常数，*τ* 是转矩。该项表示铜绕组中的欧姆损耗。 - 与转速相关的电气损耗 *kw**ω*2，其中 *kw* 是常数，*ω* 是转速。该项表示由涡流引起的铁耗。 |
| `Tabulated loss data` | 损耗标定查找表，它是电机转速和负载转矩的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据对二维查找表进行虚拟标定。 |
| `Tabulated loss data with temperature` | 损耗标定查找表，它是电机转速、负载转矩和工作温度的函数。  如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据对三维查找表进行虚拟标定。 |
| `Tabulated loss data with temperature and voltage` | 损耗标定查找表，它是负载转矩、电机转速、供电直流电压和工作温度的函数。  要直接导入您自己的四维损耗标定表，请点击 **Import Loss Calibration**。 |
| `Tabulated efficiency data` | 二维效率标定查找表，它是电机转速和负载转矩的函数。该模块：  - 将您提供的效率值转换为损耗，并在仿真中使用表列损耗。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。请根据需要为低转速和低转矩值提供表列数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的转速和转矩幅值，不外推损耗值。 |
| `Tabulated efficiency data with temperature` | 三维效率标定查找表，它是电机转速、负载转矩和工作温度的函数。该模块：    - 将您提供的效率值转换为损耗，并在仿真中使用表列损耗。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。请根据需要为低转速和低转矩值提供表列数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的转速、转矩或温度幅值，不外推损耗值。 |
| `Tabulated efficiency data with temperature and voltage` | 效率标定查找表，它是负载转矩、电机转速、供电直流电压和工作温度的函数。  要直接导入您自己的四维效率标定表，请点击 **Import Efficiency Calibration**。该模块：  - 将您提供的效率值转换为损耗，并在仿真中使用表列损耗。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。请根据需要为低转速和低转矩值提供表列数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的转速、转矩、温度或电压幅值，不外推损耗值。 |

作为最佳实践，请使用 `Tabulated loss data`、`Tabulated loss data with temperature` 或 `Tabulated loss data with temperature and voltage`，而不是 `Tabulated efficiency data`、`Tabulated efficiency data with temperature` 或 `Tabulated efficiency data with temperature and voltage`：

- 当转速为零或转矩为零时，效率变得定义不明确。
- 您可以考虑在转速或转矩为零时仍然存在的固定损耗。

**注意**

由于存在损耗，当电机转矩为零时，电机驱动系统仍可能消耗电流。

### 电气损耗的虚拟标定

如果您拥有 Model-Based Calibration Toolbox，您可以对二维或三维实测损耗查找表进行虚拟标定。

1. 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为以下之一：

   - `Tabulated loss data`
   - `Tabulated loss data with temperature`
2. 点击 **Calibrate Maps**。

对话框将逐步引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入损耗数据 | 从文件导入损耗数据，例如，打开 `<matlabroot>/toolbox/autoblks/autoblksshared/mbctemplates/MappedMotorDataset.xlsx`。有关更多信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | **Parameterize losses by** | 所需数据 | | --- | --- | | `Tabulated loss data` | - 电机转速，rad/s - 电机转矩，N·m - 功率损耗，W | | `Tabulated loss data with temperature` | - 电机转速，rad/s - 电机转矩，N·m - 电机温度，K - 功率损耗，W | 在稳态工况下采集电机数据。数据应覆盖电机转速、转矩和温度的工作范围。要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 使用试验计划将数据拟合为高斯过程模型（GPM）。要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关更多信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定响应模型进行标定并生成标定表。要评估或调整标定，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关更多信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定结果更新以下参数。  | **Parameterize losses by** | 参数 | | --- | --- | | `Tabulated loss data` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Loss table,   losses\_table** | | `Tabulated loss data with temperature` | - **Speed breakpoints for losses,   w\_eff\_bp** - **Torque breakpoints for losses,   T\_eff\_bp** - **Temperature breakpoints for   losses, Temp\_eff\_bp** - **Loss table,   losses\_table\_3d** | |

### 电气损耗的直接导入

如果您有自己的损耗标定数据（相对于转矩、转速、供电直流电压和温度），可以直接导入。下表将逐步引导完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated loss data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入损耗数据 | 点击 **Import Loss Calibration**。模块将读取并导入电子表格 **PowerLoss** 选项卡中的数据。 |

### 电气效率的直接导入

如果您有自己的效率标定数据（相对于扭矩、转速、供电直流电压和温度），可以直接导入。下表列出了各项任务。

| 任务 | 描述 |
| --- | --- |
| 选择参数化方式 | 在 **Electrical Losses** 选项卡上，将 **Parameterize losses by** 设置为 `Tabulated efficiency data with temperature and voltage`。 |
| 选择标定数据文件 | 导航到标定数据文件夹，例如 `<matlabroot>/toolbox/autoblks/`。选择标定数据文件，例如 `MotorCalibrationImportData.xlsx`。点击 **Open**。 |
| 导入效率数据 | 点击 **Import Efficiency Calibration**。模块读取并导入电子表格 **Efficiency** 选项卡中的数据。 |

### 电池电流

模块使用机械功率、功率损耗和电池电压计算电池电流。正电流表示电池放电。负电流表示电池充电。

BattAmp=MechPwr+PwrLossBattVolt

该方程使用以下变量。

|  |  |
| --- | --- |
| *BattVolt* | 进入电机驱动电子设备的直流电压 |
| *MechPwr* | 机械功率 |
| *PwrLoss* | 功率损耗 |
| *BattCurr* | 进入电机驱动电子设备的直流电流 |

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 定义 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd`  - 正信号表示功率流入模块。 - 负信号表示功率流出模块。 | `PwrMtr` | 机械功率 | **Port configuration** 设置： - `Torque`：Pmot= Tloadω    - `Speed`：Pmot= −Teω | W |
| `PwrBus` | 电功率 | Pbus= BattVolt×BattAmp | W |
| `PwrNotTrnsfrd`  - 负信号表示热损耗。 | `PwrLoss` | 电机功率损耗 — 包括电气损耗和机械损耗 | Ploss,total= PwrLoss+Pd其中 Pd=−bω2 | W |
| `PwrStored`  - 正值表示动能增加。 | `PwrStoredShft` | 转子动能存储速率 | Pstored= Jω˙ω | W |

该方程使用以下变量。

|  |  |
| --- | --- |
| *Te* | 施加到轴上的电机扭矩，假设转子转速恒定 |
| *Tload* | 电机扭矩负载 |
| *ω* | 转子转速 |
| *b* | 旋转阻尼系数 |
| *J* | 转子惯量 |
| *Pd* | 与任何损耗表中的损耗分开的阻尼损耗 |
| *Ploss,total* | 总热损耗，等于 `PwrNotTrnsfrd` |
