---
type: simulink-block
title: 'Mapped SI Engine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Propulsion'
documentation_page: 'mappedsiengine'
documentation_source_path: 'ref/mappedsiengine.html'
language: zh-CN
chinese_source: worker-translation
---

# Mapped SI Engine

## 端口

### 输入

### **TrqCmd** — 指令扭矩 `scalar`

扭矩，*Tcmd*，单位为 N·m。

### **EngSpd** — 发动机转速 `scalar`

发动机转速，*N*，单位为 rpm。

### **EngTemp** — 发动机温度 `scalar`

发动机温度，*TempEng*，单位为 K。

#### 依赖

要启用此端口，请选择 **Input engine temperature**。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `IntkGassMassFlw` | | | 发动机空气质量流量输出 | kg/s |
| `NrmlzdAirChrg` | | | 归一化发动机气缸空气质量 | N/A |
| `Afr` | | | 空燃比（AFR） | N/A |
| `FuelMassFlw` | | | 发动机燃油流量输出 | kg/s |
| `FuelVolFlw` | | | 体积燃油流量 | m3/s |
| `ExhManGasTemp` | | | 发动机排气温度 | K |
| `EngTrq` | | | 发动机扭矩输出 | N·m |
| `EngSpd` | | | 发动机转速 | rpm |
| `CrkAng` | | | 发动机曲轴绝对角度  ∫0(360)CpsEngSpd18030dθ  其中 Cps 为每动力冲程的曲轴转数。 | degrees crank angle |
| `Bsfc` | | | 发动机制动比油耗（BSFC） | g/kWh |
| `EoHC` | | | 发动机出口碳氢化合物排放质量流量 | kg/s |
| `EoCO` | | | 发动机出口一氧化碳排放质量流量 | kg/s |
| `EoNOx` | | | 发动机出口一氧化氮和二氧化氮排放质量流量 | kg/s |
| `EoCO2` | | | 发动机出口二氧化碳排放质量流量 | kg/s |
| `EoPM` | | | 发动机出口颗粒物排放质量流量 | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCrkshft` | 曲轴功率 | W |
| `PwrNotTrnsfrd` | `PwrFuel` | 燃油输入功率 | W |
| `PwrLoss` | 功率损失 | W |
| `PwrStored` | | *未使用* | |

### **EngTrq** — 发动机制动扭矩 `scalar`

发动机制动扭矩，Tbrake，单位为 N·m。

## 参数

#### 模块选项

### **Include turbocharger lag effect** — 增加时间常数 `off` (default) | `on`

要对涡轮增压器迟滞进行建模，请选择 **Include
turbocharger lag effect**。在节气门控制期间，时间常数对进气歧管填充和排空动态进行建模。当扭矩请求需要涡轮增压器增压时，模块使用更大的时间常数来表示涡轮增压器迟滞。模块使用以下方程。

|  |  |
| --- | --- |
| 动态扭矩 | dTbrakedt=1τeng(Tstdy−Tbrake) |
| 增压时间常数 | τbst={τbst,rising       when Tstdy>Tbrakeτbst,falling      when Tstdy≤Tbrake |
| 最终时间常数 | τeng={τthr       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Tbrake* | 制动扭矩 |
| *Tstdy* | 稳态目标扭矩 |
| *τbst* | 增压时间常数 |
| *τbst,rising*、*τbst,falling* | 分别为增压上升和下降时间常数 |
| *τeng* | 最终时间常数 |
| *τthr* | 节气门控制期间的时间常数 |
| *ƒbst(N)* | 增压扭矩转速线 |
| *N* | 发动机转速 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TurboLagCheckbox` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

#### 依赖

选择 **Include turbocharger lag effect** 会启用
以下参数：

- **Boost torque line,
  f\_tbrake\_bst**
- **Time constant below boost line,
  tau\_thr**
- **Rising torque boost time constant,
  tau\_bst\_rising**
- **Falling torque boost time constant,
  tau\_bst\_falling**

### **Input engine temperature** — 创建输入端口 `off`（默认）| `on`

选择此项以创建 `EngTemp` 输入端口。

该模块允许您为这些发动机特性指定查找表。这些查找表使用 Model-Based Calibration Toolbox 开发，是命令扭矩 *Tcmd*、制动扭矩 *Tbrake* 和发动机转速 *N* 的函数。如果您选择 **Input engine temperature**，这些表还是发动机温度 *TempEng* 的函数。

| 表 | **Input Engine Temperature** 参数设置 | |
| --- | --- | --- |
| `off` | `on` |
| Power | *ƒ(Tcmd,N)* | *ƒ(Tcmd,N,TempEng)* |
| Air | *ƒ(Tbrake,N)* | *ƒ(Tbrake,N,TempEng)* |
| Fuel |
| Temperature |
| Efficiency |
| HC |
| CO |
| NOx |
| CO2 |
| PM |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `EngTmpInpEnbl` |
| **值**：| `off`（默认）| `on` |
| **Data Types:** | `character vector` |

#### 配置

### **Calibrate Maps** — 使用测量数据校准表 `selection`

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps** 以使用测量数据虚拟校准二维查找表。该对话框会逐步执行以下任务。

| 任务 | 描述 |
| --- | --- |
| Import firing data | 从文件导入此损失数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`。有关更多信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | 必需数据 | 可选数据 | | --- | --- | | - Engine speed, rpm - Engine torque, N·m | - Air mass flow rate, kg/s - Brake specific fuel consumption,   g/(kW·h) - CO2 mass flow rate, kg/s - CO mass flow rate, kg/s - Exhaust temperature, K - Fuel mass flow rate, kg/s - HC mass flow rate, kg/s - NOx mass flow rate, kg/s - Particulate matter mass flow rate,   kg/s |  在喷油器输送燃料时，在稳态工况下采集点火数据。数据应覆盖发动机转速和扭矩工作范围。Model-Based Calibration Toolbox 使用点火数据边界作为最大扭矩。要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| Import non-firing data | 从文件导入此非点火数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`。    - Engine speed, rpm - Engine torque, N·m  在燃料切断时，在稳态工况下采集非点火（倒拖）数据。所有非点火扭矩点都必须小于零。非点火数据仅是发动机转速的函数。 |
| Generate response models | 对于点火数据和非点火数据，Model-Based Calibration Toolbox 使用试验计划将数据拟合为高斯过程模型（GPM）。要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关更多信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| Generate calibration | Model-Based Calibration Toolbox 校准点火和非点火响应模型，并生成校准后的表。要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关更多信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| Update block parameters | 使用校准结果更新模块查找表和断点参数。 |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Breakpoints for commanded torque, f\_tbrake\_t\_bpt** — 断点 `1`×`M` 向量

断点，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_f_bpt` |
| **值：** | `1`×`M` 向量 |
| **数据类型：** | `double` |

### **发动机转速输入的断点，f\_tbrake\_n\_bpt** — 断点 `1`×`N` 向量

断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_t_bpt` |
| **值：** | `1`×`M` 向量 |
| **数据类型：** | `double` |

### **温度输入的断点，f\_tbrake\_engtmp\_bpt** — 断点 `[233.15 273.15 373.15]`（默认）| `1`×`L` 向量

断点，单位为 K。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_engtmp_bpt` |
| **值：** | `1`×`L` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

### **气缸数，NCyl** — 数量 `4`（默认）| `标量`

气缸数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4`（默认）| `标量` |
| **数据类型：** | `double` |

### **每动力冲程的曲轴转数，Cps** — 曲轴转数 `2`（默认）| `标量`

每动力冲程的曲轴转数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2`（默认）| `标量` |
| **数据类型：** | `double` |

### **总排量，Vd** — 体积 `0.0015`（默认）| `标量`

发动机排量，单位为 m^3。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015`（默认）| `标量` |
| **数据类型：** | `double` |

### **燃料低热值，Lhv** — 热值 `45e6`（默认）| `标量`

燃料低热值，*LHV*，单位为 J/kg。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lhv` |
| **值：** | `45e6`（默认）| `标量` |
| **数据类型：** | `double` |

### **燃料比重，Sg** — 比重 `0.745`（默认）| `标量`

燃料比重，*Sgfuel*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sg` |
| **值：** | `0.832`（默认）| `标量` |
| **数据类型：** | `double` |

### **空气理想气体常数，Rair** — 常数 `287`（默认）| `标量`

进入发动机进气口的空气和残余气体的理想气体常数，单位为 J/(kg\*K)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rair` |
| **值：** | `287`（默认）| `标量` |
| **数据类型：** | `double` |

### **Air standard pressure, Pstd** — 压力 `101325`（默认）| `scalar`

标准空气压力，单位为 Pa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `101325`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Air standard temperature, Tstd** — 温度 `293.15`（默认）| `scalar`

标准空气温度，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tstd` |
| **值：** | `293.15`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Boost torque line, f\_tbrake\_bst** — 增压滞后 `1`×`M` 向量

增压扭矩线，*ƒbst(N)*，单位为
N·m。

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag
effect**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_bst` |
| **值：** | `1`×`M` 向量 |
| **数据类型：** | `double` |

### **Time constant below boost line, tau\_thr** — 增压线以下时间常数 `0.2`（默认）| `scalar`

增压线以下时间常数，
*τthr*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_thr` |
| **值：** | `0.1`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag
effect**。

### **Rising torque boost time constant, tau\_bst\_rising** — 上升时间常数 `1.5`（默认）| `scalar`

上升扭矩增压时间常数，
*τbst,rising*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_bst_rising` |
| **值：** | `1.0`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag
effect**。

### **Falling torque boost time constant, tau\_bst\_falling** — 下降时间常数 `1`（默认）| `scalar`

下降扭矩增压时间常数，
*τbst,falling*，单位为 s。

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag
effect**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_bst_falling` |
| **值：** | `0.7`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 功率

### **Brake torque map, f\_tbrake** — 二维查找表 `M`×`N` 矩阵

发动机扭矩查找表是命令发动机
扭矩和发动机转速的函数，*T* = ƒ(*Tcmd*, *N*)，
其中：

- *T* 是发动机扭矩，单位为 N·m。
- *Tcmd* 是
  命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

显示实际扭矩随发动机转速和命令扭矩变化的图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

### **Plot brake torque map** — 绘制表按钮

点击以绘制表。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Brake torque map, f\_tbrake\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

发动机扭矩查找表是命令发动机扭矩、发动机转速和发动机温度的函数，
*T* = ƒ(*Tcmd*,
*N*,
*TempEng*)，其中：

- *T* 是发动机扭矩，单位为 N·m。
- *Tcmd* 是命令
  发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机
  温度，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tbrake_3d` |
| **值**：| `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### Air

### **Air mass flow map, f\_air** — 2D lookup table `M`-by-`N` matrix

发动机空气质量流量查找表是
命令发动机扭矩和发动机转速的函数，m˙intk = ƒ(*Tcmd*, *N*)，其中：

- m˙intk 是发动机空气质量流量，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为
  N·m。
- *N* 是发动机转速，单位为 rpm。

显示空气质量流量作为发动机转速和命令扭矩函数的图

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_air` |
| **值**：| `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot air mass map** — Plot table button

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Air mass flow map, f\_air\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

发动机空气质量流量查找表是
命令发动机扭矩、发动机转速和发动机温度的函数，m˙intk = ƒ(*Tcmd*,
*N*,
*TempEng*)，其中：

- m˙intk 是发动机空气质量流量，单位为 kg/s。
- *Tcmd* 是命令
  发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机
  温度，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_air_3d` |
| **值**：| `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### Fuel

### **Fuel flow map, f\_fuel** — 2D lookup table `M`-by-`N` matrix

发动机燃料质量流量查找表是命令
发动机扭矩和发动机转速的函数，*MassFlow* = ƒ(*Tcmd*, *N*)，
其中：

- *MassFlow* 是发动机燃料质量流量，
  单位为 kg/s。
- *Tcmd* 是
  命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

显示燃料质量流量作为发动机转速和命令扭矩函数的图

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_fuel` |
| **值**：| `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot fuel flow map** — Plot table button

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Fuel flow map, f\_fuel\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

发动机燃料质量流量查找表是
命令发动机扭矩、发动机转速和发动机温度的函数，
*MassFlow* =
ƒ(*Tcmd*, *N*,
*TempEng*)，其中：

- *MassFlow* 是发动机燃料质量流量，单位为
  kg/s。
- *Tcmd* 是命令
  发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机
  温度，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_fuel_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### 温度

### **排气温度脉谱图，f\_texh** — 二维查找表 `M`×`N` 矩阵

发动机排气温度查找表是
指令发动机扭矩和发动机转速的函数，*Texh* =
ƒ(*Tcmd*, *N*)，
其中：

- *Texh* 为
  排气温度，单位为 K。
- *Tcmd* 为
  指令发动机扭矩，单位为 N·m。
- *N* 为发动机转速，单位为 rpm。

显示排气温度随发动机转速和指令扭矩变化的图

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_texh` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **绘制排气温度脉谱图** — 绘制表按钮

点击以绘制表。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **排气温度脉谱图，f\_texh\_3d** — 三维查找表 `array`

发动机排气温度查找
表是指令发动机扭矩、发动机转速和发动机
温度的函数，*Texh* =
ƒ(*Tcmd*,
*N*,
*TempEng*)，其中：

- *Texh* 为排气
  温度，单位为 K。
- *Tcmd* 为指令
  发动机扭矩，单位为 N·m。
- *N* 为发动机转速，单位为 rpm。
- *TempEng* 为发动机
  温度，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_texh_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### 效率

### **BSFC 脉谱图，f\_eff** — 二维查找表 `M`×`N`×`L` 数组

制动比油耗（BSFC）效率是指令发动机扭矩和发动机转速的函数，*BSFC* =
ƒ(*Tcmd*, *N*)，
其中：

- *BSFC* 为 BSFC，单位为 g/kWh。
- *Tcmd* 为
  指令发动机扭矩，单位为 N·m。
- *N* 为发动机转速，单位为 rpm。

显示 BSFC 随发动机转速和指令扭矩变化的图

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_eff` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **绘制 BSFC 脉谱图** — 绘制表按钮

点击以绘制表。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **BSFC 脉谱图，f\_eff\_3d** — 三维查找表 `M`×`N`×`L` 数组

制动比油耗
（BSFC）效率是指令发动机扭矩、发动机转速
和发动机温度的函数，*BSFC* =
ƒ(*Tcmd*,
*N*,
*TempEng*)，其中：

- *BSFC* 为 BSFC，单位为 g/kWh。
- *Tcmd* 为指令
  发动机扭矩，单位为 N·m。
- *N* 为发动机转速，单位为 rpm。
- *TempEng* 为发动机
  温度，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_eff_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### HC

### **EO HC map, f\_hc** — 2D lookup table `M`-by-`N` matrix

发动机出口碳氢化合物排放是命令发动机扭矩和发动机转速的函数，*EO HC* = ƒ(*Tcmd*, *N*)，其中：

- *EO HC* 是发动机出口碳氢化合物排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

显示 EO HC 随发动机转速和命令扭矩变化的图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_hc` |
| **值**：| `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO HC map** — Plot table button

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO HC map, f\_hc\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

发动机出口碳氢化合物排放是命令发动机扭矩、发动机转速和发动机温度的函数，*EO HC* = ƒ(*Tcmd*, *N*, *TempEng*)，其中：

- *EO HC* 是发动机出口碳氢化合物排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机温度，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_hc_3d` |
| **值**：| `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### CO

### **EO CO map, f\_co** — 2D lookup table `M`-by-`N` matrix

发动机出口一氧化碳排放是命令发动机扭矩和发动机转速的函数，*EO CO* = ƒ(*Tcmd*, *N*)，其中：

- *EO CO* 是发动机出口一氧化碳排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

显示 EO CO 随发动机转速和命令扭矩变化的图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_co` |
| **值**：| `M`-by-`N` matrix |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO CO map** — Plot table button

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO HC map, f\_hc\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

发动机出口碳氢化合物排放是命令发动机扭矩、发动机转速和发动机温度的函数，*EO HC* = ƒ(*Tcmd*, *N*, *TempEng*)，其中：

- *EO HC* 是发动机出口碳氢化合物排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机温度，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_co_3d` |
| **值**：| `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### NOx

### **EO NOx map, f\_nox** — 2D lookup table `M`-by-`N` matrix

发动机出口一氧化氮和二氧化氮排放是命令发动机扭矩和发动机转速的函数，*EO NOx* = ƒ(*Tcmd*, *N*)，其中：

- *EO NOx* 是发动机出口一氧化氮和二氧化氮排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

显示 EO NOX 随发动机转速和命令扭矩变化的图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nox` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO NOx map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO NOx map, f\_nox\_3d** — 3D 查找表 `M`×`N`×`L` 数组

发动机出口一氧化氮和二氧化氮排放是命令发动机扭矩、发动机转速和发动机温度的函数，*EO NOx* = ƒ(*Tcmd*, *N*, *TempEng*)，其中：

- *EO NOx* 是发动机出口一氧化氮和二氧化氮排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机温度，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nox_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### CO2

### **EO CO2 map, f\_co2** — 2D 查找表 `M`×`N` 矩阵

发动机出口二氧化碳排放是命令发动机扭矩和发动机转速的函数，*EO CO2* = ƒ(*Tcmd*, *N*)，其中：

- *EO CO2* 是发动机出口二氧化碳排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

显示 EO CO2 作为发动机转速和命令扭矩函数的图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_co2` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot CO2 map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO CO2 map, f\_co2\_3d** — 3D 查找表 `M`×`N`×`L` 数组

发动机出口二氧化碳排放是命令发动机扭矩、发动机转速和发动机温度的函数，*EO CO2* = ƒ(*Tcmd*, *N*, *TempEng*)，其中：

- *EO CO2* 是发动机出口二氧化碳排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机温度，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_co2_3d` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### PM

### **EO PM map, f\_pm** — 2D 查找表 `M`×`N` 矩阵

发动机出口颗粒物排放是命令发动机扭矩和发动机转速的函数，其中：

- *EO PM* 是发动机出口 PM 排放，单位为 kg/s。
- *Tcmd* 是命令发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_pm` |
| **值：** | `M`×`N` 矩阵 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO PM map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO PM map, f\_pm\_3d** — 3D lookup table `M`-by-`N`-by-`L` array

发动机输出颗粒物排放是命令发动机扭矩、发动机转速和发动机温度的函数，其中：

- *EO PM* 是发动机输出 PM 排放，单位为
  kg/s。
- *Tcmd* 是命令
  发动机扭矩，单位为 N·m。
- *N* 是发动机转速，单位为 rpm。
- *TempEng* 是发动机
  温度，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_pm_3d` |
| **值**：| `M`-by-`N`-by-`L` array |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engines Vehicle Dynamics Blockset / Powertrain / Propulsion

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

使用查找表的火花点火发动机模型

Mapped SI Engine 模块使用功率、空气质量流量、燃料流量、排气温度、效率和排放性能查找表实现了一个映射火花点火 (SI) 发动机模型。您可以将该模块用于：

- 硬件在环 (HIL) 发动机控制设计
- 车辆级燃油经济性和性能仿真

该模块使您能够为这些发动机特性指定查找表。这些查找表使用 Model-Based Calibration Toolbox™ 开发，是命令扭矩
*Tcmd*、制动扭矩
*Tbrake* 和发动机转速
*N* 的函数。如果您选择 **Input engine temperature**，这些表
也是发动机温度
*TempEng* 的函数。

| 表 | **Input Engine Temperature** 参数设置 | |
| --- | --- | --- |
| `off` | `on` |
| Power | *ƒ(Tcmd,N)* | *ƒ(Tcmd,N,TempEng)* |
| Air | *ƒ(Tbrake,N)* | *ƒ(Tbrake,N,TempEng)* |
| Fuel |
| Temperature |
| Efficiency |
| HC |
| CO |
| NOx |
| CO2 |
| PM |

为了约束 Mapped SI Engine 模块的输出，该模块不会
外推查找表数据。

### 虚拟标定

如果您拥有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据对二维查表进行虚拟标定。该对话框将逐步引导您完成以下任务。

| 任务 | 描述 |
| --- | --- |
| 导入点火数据 | 从文件导入此点火损失数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。    | 必需数据 | 可选数据 | | --- | --- | | - 发动机转速，rpm - 发动机扭矩，N·m | - 空气质量流量，kg/s - 制动比油耗，g/(kW·h) - CO2 质量流量，kg/s - CO 质量流量，kg/s - 排气温度，K - 燃料质量流量，kg/s - HC 质量流量，kg/s - NOx 质量流量，kg/s - 颗粒物质量流量，kg/s |  在喷油器输送燃料时，在稳态工况下采集点火数据。数据应覆盖发动机转速和扭矩运行范围。Model-Based Calibration Toolbox 使用点火数据边界作为最大扭矩。  要过滤或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 将打开。 |
| 导入非点火数据 | 从文件导入此非点火数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/SiEngineData.xlsx`。    - 发动机转速，rpm - 发动机扭矩，N·m  在断油时，在稳态工况下采集非点火（倒拖）数据。所有非点火扭矩点必须小于零。非点火数据仅是发动机转速的函数。 |
| 生成响应模型 | 对于点火和非点火数据，Model-Based Calibration Toolbox 使用试验计划将数据拟合为高斯过程模型（GPM）。  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 将打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成标定 | Model-Based Calibration Toolbox 对标定点火和非点火响应模型进行标定，并生成标定表。  要评估或调整标定，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 将打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用标定结果更新模块查表和断点参数。 |

### Cylinder Air Mass

该模块使用以下方程计算归一化气缸空气质量。

MNom=PstdVdNcylRairTstdL=(60smin)Cps⋅m˙air(1000gKg)Ncyl⋅N⋅MNom

这些方程使用以下变量。

|  |  |
| --- | --- |
| *L* | 归一化气缸空气质量 |
| MNom | 标准温度和压力下、活塞位于下止点（BDC）最大体积时的标称发动机气缸空气质量，单位为 kg |
| Cps | 每个动力冲程的曲轴转数，rev/stroke |
| Pstd | 标准压力 |
| Tstd | 标准温度 |
| Rair | 空气和燃烧气体混合物的理想气体常数 |
| Vd | 排量 |
| Ncyl | 发动机气缸数 |
| *N* | 发动机转速 |
| m˙intk | 发动机空气质量流量，单位为 g/s |

### Turbocharger Lag

要对涡轮增压器迟滞建模，请选择 **Include
turbocharger lag effect**。在节气门控制期间，时间常数对进气歧管的充填和排空动态进行建模。当扭矩请求需要涡轮增压器增压时，该模块使用更大的时间常数来表示涡轮增压器迟滞。该模块使用以下方程。

|  |  |
| --- | --- |
| 动态扭矩 | dTbrakedt=1τeng(Tstdy−Tbrake) |
| 增压时间常数 | τbst={τbst,rising       when Tstdy>Tbrakeτbst,falling      when Tstdy≤Tbrake |
| 最终时间常数 | τeng={τthr       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Tbrake* | 制动扭矩 |
| *Tstdy* | 稳态目标扭矩 |
| *τbst* | 增压时间常数 |
| *τbst,rising*、*τbst,falling* | 分别为增压上升和下降时间常数 |
| *τeng* | 最终时间常数 |
| *τthr* | 节气门控制期间的时间常数 |
| *ƒbst(N)* | 增压扭矩转速线 |
| *N* | 发动机转速 |

### Fuel Flow

为了计算高保真模型的燃油经济性，该模块使用体积燃油流量。

Qfuel=m˙fuel(1000kgm3)Sgfuel

该方程使用以下变量。

|  |  |
| --- | --- |
| m˙fuel | 燃油质量流量 |
| *Sgfuel* | 燃油比重 |
| *Qfuel* | 体积燃油流量 |

### Power Accounting

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrCrkshft` | 曲轴功率 | −τengω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃油输入功率 | m˙fuelLHV |
| `PwrLoss` | 功率损失 | τengω−m˙fuelLHV |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | | *未使用* | |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *LHV* | 燃油低热值 |
| *ω* | 发动机转速，rad/s |
| m˙fuel | 燃油质量流量 |
| *τeng* | 每次喷射燃油质量的时间常数 |
