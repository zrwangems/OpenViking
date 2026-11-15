---
type: simulink-block
title: 'Mapped CI Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Engines and Controllers'
documentation_page: 'mappedciengine'
documentation_source_path: 'ref/mappedciengine.html'
language: zh-CN
chinese_source: worker-translation
---

# Mapped CI Engine

## 端口

### 输入

### **FuelMassCmd** — 喷射燃料质量指令 `scalar`

喷射燃料质量指令，*F*，单位为 mg/inj。

#### 依赖关系

要启用此端口，对于 **Input command**，选择 `Fuel mass`。

### **TrqCmd** — 扭矩指令 `scalar`

扭矩指令，*T*，单位为 N·m。

#### 依赖关系

要启用此端口，对于 **Input command**，选择 `Torque`。

### **EngSpd** — 发动机转速 `scalar`

发动机转速，*N*，单位为 rpm。

### **EngTemp** — 发动机温度 `scalar`

发动机温度，*TempEng*，单位为 K。

#### 依赖关系

要启用此端口，选择 **Input engine temperature**。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `IntkGasMassFlw` | | | 发动机空气质量流量输出 | kg/s |
| `NrmlzdAirChrg` | | | 归一化发动机气缸空气质量 | N/A |
| `Afr` | | | 空燃比 (AFR) | N/A |
| `FuelMassFlw` | | | 发动机燃料流量输出 | kg/s |
| `FuelVolFlw` | | | 体积燃料流量 | m3/s |
| `ExhManGasTemp` | | | 发动机排气温度 | K |
| `EngTrq` | | | 发动机扭矩输出 | N·m |
| `EngSpd` | | | 发动机转速 | rpm |
| `CrkAng` | | | 发动机曲轴绝对角度  ∫0(360)CpsEngSpd18030dθ  其中 Cps 是每动力冲程的曲轴转数。 | degrees crank angle |
| `Bsfc` | | | 发动机制动比燃料消耗 (BSFC) | g/kWh |
| `EoHC` | | | 发动机出口碳氢化合物排放质量流量 | kg/s |
| `EoCO` | | | 发动机出口一氧化碳排放质量流量 | kg/s |
| `EoNOx` | | | 发动机出口一氧化氮和二氧化氮排放质量流量 | kg/s |
| `EoCO2` | | | 发动机出口二氧化碳排放质量流量 | kg/s |
| `EoPM` | | | 发动机出口颗粒物排放质量流量 | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCrkshft` | 曲轴功率 | W |
| `PwrNotTrnsfrd` | `PwrFuel` | 燃料输入功率 | W |
| `PwrLoss` | 功率损失 | W |
| `PwrStored` | | *未使用* | |

### **EngTrq** — 功率 `scalar`

发动机功率，Tbrake，单位为 N·m。

## 参数

#### 模块选项

### **Input command** — 查表函数 `Fuel mass` (默认) | `Torque`

这些查找表由 Model-Based Calibration Toolbox 开发，是喷射燃料质量 *F*、发动机扭矩 *T*、发动机转速 *N* 和发动机温度 *TempEng* 的函数。

| **Input Command** 设置 | **Input Engine Temperature** 参数设置 | 查找表 |
| --- | --- | --- |
| `Fuel mass` | `off` | *ƒ(F,N)* |
| `on` | *ƒ(F,N,TempEng)* |
| `Torque` | `off` | *ƒ(T,N)* |
| `on` | *ƒ(T,N,TempEng)* |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InputCmdPopup` |
| **值：** | `Fuel mass` (默认) | `Torque` |
| **数据类型：** | `character vector` |

#### 依赖关系

- 选择 `Fuel mass` 会启用 **Breakpoints for commanded fuel mass input, f\_tbrake\_f\_bpt**。
- 选择 `Torque` 会启用 **Breakpoints for commanded torque input, f\_tbrake\_t\_bpt**。
- 选择 **Input engine temperature** 会启用 **Breakpoints for temperature input, f\_tbrake\_engtmp\_bpt**。

### **Include turbocharger lag effect** — 增加时间常数 `off` (默认) | `on`

要对涡轮增压滞后建模，请选择 **Include turbocharger lag effect**。涡轮增压滞后限制每次喷射的最大燃料质量。为对每次喷射的最大燃料质量建模，模块使用带时间常数的一阶系统。在低扭矩下，发动机不需要增压即可提供足够的空气流量。当请求的燃料质量需要增压时，模块使用时间常数确定每次喷射的最大燃料质量。模块针对指定的 **Input command** 设置使用这些方程。

| 计算 | **Input command** 参数设置 | |
| --- | --- | --- |
| `Fuel mass` | `Torque` |
| 动态扭矩 | dFmaxdt=1τeng(Fcmd−Fmax) | dTmaxdt=1τeng(Tcmd−Tmax) |
| 带涡轮增压滞后的每冲程喷射燃料质量或扭矩 | F={Fcmd       when Fcmd<FmaxFmax      when Fcmd≥Fmax | Ttarget={Tcmd       when Tcmd<TmaxTmax      when Tcmd≥Tmax |
| 不带涡轮增压滞后的每冲程喷射燃料质量或扭矩 | F=Fcmd=Fmax | Ttarget=Tcmd=Tmax |
| 增压时间常数 | τbst={τbst,rising       when Fcmd>Fmaxτbst,falling      when Fcmd≤Fmax | τbst={τbst,rising       when Tcmd>Tmaxτbst,falling      when Tcmd≤Tmax |
| 最终时间常数 | τeng={τnat       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) | |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Tbrake* | 制动扭矩 |
| *F* | 每冲程喷射燃料质量 |
| *Fcmd*, *Fmax* | 分别为指令和最大每冲程喷射燃料质量 |
| *Ttarget*, *Tcmd*, *Tmax* | 分别为目标、指令和最大扭矩 |
| *τbst* | 增压时间常数 |
| *τbst,rising*, *τbst,falling* | 分别为增压上升和下降时间常数 |
| *τeng* | 最终时间常数 |
| *τnat* | 低于增压扭矩转速线的时间常数 |
| *ƒbst(N)* | 增压扭矩/转速线 |
| *N* | 发动机转速 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TurboLagCheckbox` |
| **值：** | `off` (默认) | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

选择 **Include turbocharger lag effect** 会启用这些参数：

- **Boost torque line, f\_tbrake\_bst**
- **Time constant below boost line, tau\_nat**
- **Rising maximum fuel mass boost time constant, tau\_bst\_rising**
- **Falling maximum fuel mass boost time constant, tau\_bst\_falling**

### **Input engine temperature** — 创建输入端口 `off` (默认) | `on`

选择此选项可创建 `EngTemp` 输入端口。

这些查找表由 Model-Based Calibration Toolbox 开发，是喷射燃料质量 *F*、发动机扭矩 *T*、发动机转速 *N* 和发动机温度 *TempEng* 的函数。

| **Input Command** 设置 | **Input Engine Temperature** 参数设置 | 查找表 |
| --- | --- | --- |
| `Fuel mass` | `off` | *ƒ(F,N)* |
| `on` | *ƒ(F,N,TempEng)* |
| `Torque` | `off` | *ƒ(T,N)* |
| `on` | *ƒ(T,N,TempEng)* |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngTmpInpEnbl` |
| **值：** | `off` (默认) | `on` |
| **数据类型：** | `character vector` |

#### 配置

### **Calibrate Maps** — 使用测量数据校准表格 `selection`

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据虚拟校准 2D 查找表。该对话框会逐步执行这些任务。

| 任务 | 描述 |
| --- | --- |
| 导入着火数据 | 从文件导入此损失数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  | **Input command** | Required Data | Optional Data | | --- | --- | --- | | `Fuel mass` | - 发动机转速，rpm - 每冲程喷射的指令燃料质量，mg - 发动机扭矩，N·m | - 空气质量流量，kg/s - 制动比燃料消耗，  g/(kW·h) - CO2 质量流量，kg/s - CO 质量流量，kg/s - 排气温度，K - 燃料质量流量，kg/s - HC 质量流量，kg/s - NOx 质量流量，kg/s - 颗粒物质量流量，  kg/s | | `Torque` | - 发动机转速，rpm - 发动机扭矩，N·m |  在喷油器喷射燃料时，在稳态运行条件下采集着火数据。数据应覆盖发动机转速和扭矩运行范围。Model-Based Calibration Toolbox 使用着火数据边界作为最大扭矩。  要过滤或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox 数据编辑器打开。 |
| 导入非着火数据 | 从文件导入此非着火数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`。  - 发动机转速，rpm - 发动机扭矩，N·m    在燃料切断时，在稳态运行条件下采集非着火（倒拖）数据。所有非着火扭矩点必须小于零。非着火数据仅是发动机转速的函数。 |
| 生成响应模型 | 对于着火和非着火数据，Model-Based Calibration Toolbox 使用测试计划将数据拟合到高斯过程模型 (GPM)。  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准着火和非着火响应模型并生成校准后的表格。  要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准结果更新模块查找表和断点参数。 |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Breakpoints for commanded fuel mass input, f\_tbrake\_f\_bpt** — 断点 `1`-by-`M` vector

断点，单位为 mg/inj。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_f_bpt` |
| **值：** | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖关系

将 **Input command** 设置为 `Fuel mass` 会启用此参数。

### **Breakpoints for commanded torque input, f\_tbrake\_t\_bpt** — 断点 `1`-by-`M` vector

断点，单位为 N·m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_t_bpt` |
| **值：** | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖关系

将 **Input command** 设置为 `Torque` 会启用此参数。

### **Breakpoints for engine speed input, f\_tbrake\_n\_bpt** — 断点 `1`-by-`N` vector

断点，单位为 rpm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_n_bpt` |
| **值：** | `1`-by-`N` vector |
| **数据类型：** | `double` |

### **Breakpoints for temperature input, f\_tbrake\_engtmp\_bpt** — 断点 `[233.15 273.15 373.15]` (默认) | `1`-by-`L` vector

断点，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_engtmp_bpt` |
| **值：** | `1`-by-`L` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

### **Number of cylinders, NCyl** — 数值 `4` (默认) | `scalar`

气缸数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Crank revolutions per power stroke, Cps** — 曲轴转数 `2` (默认) | `scalar`

每动力冲程的曲轴转数。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Total displaced volume, Vd** — 体积 `0.0015` (默认) | `scalar`

发动机排量，单位为 m^3。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Fuel lower heating value, Lhv** — 热值 `45e6` (默认) | `scalar`

燃料低热值，*LHV*，单位为 J/kg。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lhv` |
| **值：** | `45e6` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Fuel specific gravity, Sg** — 比重 `0.832` (默认) | `scalar`

燃料比重，*Sgfuel*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sg` |
| **值：** | `0.832` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Ideal gas constant air, Rair** — 常数 `287` (默认) | `scalar`

进入发动机进气口的空气和残余气体的理想气体常数，单位为 J/(kg·K)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rair` |
| **值：** | `287` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Air standard pressure, Pstd** — 压力 `101325` (默认) | `scalar`

标准空气压力，单位为 Pa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `101325` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Air standard temperature, Tstd** — 温度 `293.15` (默认) | `scalar`

标准空气温度，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tstd` |
| **值：** | `293.15` (默认) | `scalar` |
| **数据类型：** | `double` |

### **Boost torque line, f\_tbrake\_bst** — 增压滞后 `[90,95,95,95,96,100,104,104,104,100,95,85,75,67,60,55]` (默认) | `1`-by-`M` vector

增压扭矩线，*ƒbst(N)*，单位为 N·m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_bst` |
| **值：** | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag effect**。

### **Time constant below boost line, tau\_nat** — 低于 `0.1` 的时间常数 (默认) | `scalar`

低于增压线的时间常数，*τnat*，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_nat` |
| **值：** | `0.1` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag effect**。

### **Rising maximum fuel mass boost time constant, tau\_bst\_rising** — 上升时间常数 `1.0` (默认) | `scalar`

上升最大燃料质量增压时间常数，*τbst,rising*，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_bst_rising` |
| **值：** | `1.0` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag effect**。

### **Falling maximum fuel mass boost time constant, tau\_bst\_falling** — 下降时间常数 `0.7` (默认) | `scalar`

下降最大燃料质量增压时间常数，*τbst,falling*，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_bst_falling` |
| **值：** | `0.7` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag effect**。

### **Turbocharger time constant blend fuel mass fraction, f\_blend\_frac** — 时间常数 `0.01` (默认) | `scalar`

涡轮增压器时间常数混合燃料质量分数，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_blend_frac` |
| **值：** | `0.01` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Include turbocharger lag effect**。

#### 功率

### **Brake torque map, f\_tbrake** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机制动扭矩查找表是指令燃料质量和发动机转速的函数，Tbrake = ƒ(*F*, *N*)，其中：  - Tbrake 是发动机扭矩，单位为 N·m。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示实际扭矩随发动机转速和指令燃料变化的图 |
| `Torque` | 发动机制动扭矩查找表是目标扭矩和发动机转速的函数，Tbrake = ƒ(*Ttarget*, *N*)，其中：  - Tbrake 是发动机扭矩，单位为 N·m。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot brake torque map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Brake torque map, f\_tbrake\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机制动扭矩查找表是指令燃料质量和发动机转速的函数，Tbrake = ƒ(*F*, *N*, *TempEng*)，其中：  - Tbrake 是发动机扭矩，单位为 N·m。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机制动扭矩查找表是目标扭矩和发动机转速的函数，Tbrake = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - Tbrake 是发动机扭矩，单位为 N·m。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tbrake_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### 空气

### **Air mass flow map, f\_air** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 空气质量流量查找表是指令燃料质量和发动机转速的函数，m˙intk = ƒ(*Fmax*, *N*)，其中：  - m˙intk 是发动机空气质量流量，单位为 kg/s。 - *Fmax* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示空气质量流量随发动机转速和指令燃料变化的图 |
| `Torque` | 空气质量流量查找表是最大扭矩和发动机转速的函数，m˙intk = ƒ(*Tmax*, *N*)，其中：  - m˙intk 是发动机空气质量流量，单位为 kg/s。 - *Tmax* 是最大扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_air` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot air mass map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Air mass flow map, f\_air\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 空气质量流量查找表是指令燃料质量和发动机转速的函数，m˙intk = ƒ(*Fmax*, *N*, *TempEng*)，其中：  - m˙intk 是发动机空气质量流量，单位为 kg/s。 - *Fmax* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 空气质量流量查找表是最大扭矩和发动机转速的函数，m˙intk = ƒ(*Tmax*, *N*, *TempEng*)，其中：  - m˙intk 是发动机空气质量流量，单位为 kg/s。 - *Tmax* 是最大扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_air_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### 燃料

### **Fuel flow map, f\_fuel** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机燃料流量查找表是指令燃料质量和发动机转速的函数，*MassFlow* = ƒ(*F*, *N*)，其中：  - *MassFlow* 是发动机燃料质量流量，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示燃料质量流量随发动机转速和指令燃料变化的图 |
| `Torque` | 发动机燃料流量查找表是目标扭矩和发动机转速的函数，*MassFlow* = ƒ(*Ttarget*, *N*)，其中：  - *MassFlow* 是发动机燃料质量流量，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_fuel` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot fuel flow map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Fuel flow map, f\_fuel\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机燃料流量查找表是指令燃料质量、发动机转速和发动机温度的函数，*MassFlow* = ƒ(*F*, *N*, *TempEng*)，其中：  - *MassFlow* 是发动机燃料质量流量，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机燃料流量查找表是目标扭矩、发动机转速和发动机温度的函数，*MassFlow* = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - *MassFlow* 是发动机燃料质量流量，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_fuel_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### 温度

### **Exhaust temperature map, f\_texh** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机排气温度表是指令燃料质量和发动机转速的函数，*Texh* = ƒ(*F*, *N*)，其中：  - *Texh* 是排气温度，单位为 K。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示排气温度随发动机转速和指令燃料变化的图 |
| `Torque` | 发动机排气温度表是目标扭矩和发动机转速的函数，*Texh* = ƒ(*Ttarget*, *N*)，其中：  - *Texh* 是排气温度，单位为 K。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_texh` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot exhaust temperature map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Exhaust temperature map, f\_texh\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机排气温度表是指令燃料质量和发动机转速的函数，*Texh* = ƒ(*F*, *N*, *TempEng*)，其中：  - *Texh* 是排气温度，单位为 K。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机排气温度表是目标扭矩和发动机转速的函数，*Texh* = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - *Texh* 是排气温度，单位为 K。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_texh_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### 效率

### **BSFC map, f\_eff** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 制动比燃料消耗 (BSFC) 效率是指令燃料质量和发动机转速的函数，*BSFC* = ƒ(*F*, *N*)，其中：  - *BSFC* 是 BSFC，单位为 g/kWh。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示 BSFC 随发动机转速和指令燃料变化的图 |
| `Torque` | 制动比燃料消耗 (BSFC) 效率是目标扭矩和发动机转速的函数，*BSFC* = ƒ(*Ttarget*, *N*)，其中：  - *BSFC* 是 BSFC，单位为 g/kWh。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_eff` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot BSFC map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **BSFC map, f\_eff\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 制动比燃料消耗 (BSFC) 效率是指令燃料质量和发动机转速的函数，*BSFC* = ƒ(*F*, *N*, *TempEng*)，其中：  - *BSFC* 是 BSFC，单位为 g/kWh。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 制动比燃料消耗 (BSFC) 效率是目标扭矩和发动机转速的函数，*BSFC* = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - *BSFC* 是 BSFC，单位为 g/kWh。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_eff_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### HC

### **EO HC map, f\_hc** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口碳氢化合物排放是指令燃料质量和发动机转速的函数，*EO HC* = ƒ(*F*, *N*)，其中：  - *EO HC* 是发动机出口碳氢化合物排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示 EO HC 随发动机转速和指令燃料变化的图 |
| `Torque` | 发动机出口碳氢化合物排放是目标扭矩和发动机转速的函数，*EO HC* = ƒ(*Ttarget*, *N*)，其中：  - *EO HC* 是发动机出口碳氢化合物排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_hc` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO HC map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO HC map, f\_hc\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口碳氢化合物排放是指令燃料质量和发动机转速的函数，*EO HC* = ƒ(*F*, *N*, *TempEng*)，其中：  - *EO HC* 是发动机出口碳氢化合物排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机出口碳氢化合物排放是目标扭矩和发动机转速的函数，*EO HC* = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - *EO HC* 是发动机出口碳氢化合物排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_hc_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### CO

### **EO CO map, f\_co** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口一氧化碳排放是指令燃料质量和发动机转速的函数，*EO CO* = ƒ(*F*, *N*)，其中：  - *EO CO* 是发动机出口一氧化碳排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示 EO CO 随发动机转速和指令燃料变化的图 |
| `Torque` | 发动机出口一氧化碳排放是目标扭矩和发动机转速的函数，*EO CO* = ƒ(*Ttarget*, *N*)，其中：  - *EO CO* 是发动机出口一氧化碳排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_co` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO CO map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO CO map, f\_co\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口一氧化碳排放是指令燃料质量和发动机转速的函数，*EO CO* = ƒ(*F*, *N*, *TempEng*)，其中：  - *EO CO* 是发动机出口一氧化碳排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机出口一氧化碳排放是目标扭矩和发动机转速的函数，*EO CO* = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - *EO CO* 是发动机出口一氧化碳排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_co_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### NOx

### **EO NOx map, f\_nox** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口一氧化氮和二氧化氮排放是指令燃料质量和发动机转速的函数，*EO NOx* = ƒ(*F*, *N*)，其中：  - *EO NOx* 是发动机出口一氧化氮和二氧化氮排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示 EO NOX 随发动机转速和指令燃料变化的图 |
| `Torque` | 发动机出口一氧化氮和二氧化氮排放是目标扭矩和发动机转速的函数，*EO NOx* = ƒ(*Ttarget*, *N*)，其中：  - *EO NOx* 是发动机出口一氧化氮和二氧化氮排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nox` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO NOx map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO NOx map, f\_nox\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口一氧化氮和二氧化氮排放是指令燃料质量、发动机转速和发动机温度的函数，*EO NOx* = ƒ(*F*, *N*, *TempEng*)，其中：  - *EO NOx* 是发动机出口一氧化氮和二氧化氮排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机出口一氧化氮和二氧化氮排放是目标扭矩、发动机转速和发动机温度的函数，*EO NOx* = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - *EO NOx* 是发动机出口一氧化氮和二氧化氮排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nox_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### CO2

### **EO CO2 map, f\_co2** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口二氧化碳排放是指令燃料质量和发动机转速的函数，*EO CO2* = ƒ(*F*, *N*)，其中：  - *EO CO2* 是发动机出口二氧化碳排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。    显示 EO CO2 随发动机转速和指令燃料变化的图 |
| `Torque` | 发动机出口二氧化碳排放是目标扭矩和发动机转速的函数，*EO CO2* = ƒ(*Ttarget*, *N*)，其中：  - *EO CO2* 是发动机出口二氧化碳排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_co2` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot CO2 map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO CO2 map, f\_co2\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口二氧化碳排放是指令燃料质量、发动机转速和发动机温度的函数，*EO CO2* = ƒ(*F*, *N*, *TempEng*)，其中：  - *EO CO2* 是发动机出口二氧化碳排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机出口二氧化碳排放是目标扭矩、发动机转速和发动机温度的函数，*EO CO2* = ƒ(*Ttarget*, *N*, *TempEng*)，其中：  - *EO CO2* 是发动机出口二氧化碳排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_co2_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

#### PM

### **EO PM map, f\_pm** — 2D 查表 `M`-by-`N` matrix

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口 PM 排放是指令燃料质量和发动机转速的函数，其中：  - *EO PM* 是发动机出口 PM 排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 |
| `Torque` | 发动机出口 PM 排放是目标扭矩和发动机转速的函数，*EO PM* = ƒ(*Ttarget*, *N*)，其中：  - *EO PM* 是发动机出口 PM 排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_pm` |
| **值：** | `M`-by-`N` matrix |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **Plot EO PM map** — 绘制表格按钮

点击以绘制表格。

#### 依赖关系

要启用此参数，请清除 **Input engine temperature**。

### **EO PM map, f\_pm\_3d** — 3D 查表 `M`-by-`N`-by-`L` array

| **Input Command** 设置 | 描述 |
| --- | --- |
| `Fuel mass` | 发动机出口 PM 排放是指令燃料质量、发动机转速和发动机温度的函数，其中：  - *EO PM* 是发动机出口 PM 排放，单位为 kg/s。 - *F* 是指令燃料质量，单位为 mg 每冲程。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |
| `Torque` | 发动机出口 PM 排放是目标扭矩、发动机转速和发动机温度的函数，*EO PM* = ƒ(*Ttarget*, *N*, *T*)，其中：  - *EO PM* 是发动机出口 PM 排放，单位为 kg/s。 - *Ttarget* 是目标扭矩，单位为 N·m。 - *N* 是发动机转速，单位为 rpm。 - *TempEng* 是发动机温度，单位为 K。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_pm_3d` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engines Vehicle Dynamics Blockset / Powertrain / Propulsion

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

使用查找表的压燃式发动机模型

Mapped CI Engine 模块使用功率、空气质量流量、燃料流量、排气温度、效率和排放性能查找表实现映射的压燃式 (CI) 发动机模型。您可以将该模块用于：

- 硬件在环 (HIL) 发动机控制设计
- 车辆级燃料经济性和性能仿真

这些查找表由 Model-Based Calibration Toolbox™ 开发，是喷射燃料质量 *F*、发动机扭矩 *T*、发动机转速 *N* 和发动机温度 *TempEng* 的函数。

| **Input Command** 设置 | **Input Engine Temperature** 参数设置 | 查找表 |
| --- | --- | --- |
| `Fuel mass` | `off` | *ƒ(F,N)* |
| `on` | *ƒ(F,N,TempEng)* |
| `Torque` | `off` | *ƒ(T,N)* |
| `on` | *ƒ(T,N,TempEng)* |

该模块允许您为以下发动机特性指定查找表：

- 功率
- 空气
- 燃料
- 温度
- 效率
- 碳氢化合物 (HC) 排放
- 一氧化碳 (CO) 排放
- 一氧化氮和二氧化氮 (NOx) 排放
- 二氧化碳 (CO2) 排放
- 颗粒物 (PM) 排放

为限定 Mapped CI Engine 模块输出，该模块不会外推查找表数据。

### 虚拟校准

如果您有 Model-Based Calibration Toolbox，请点击 **Calibrate Maps**，使用测量数据虚拟校准 2D 查找表。该对话框会逐步执行这些任务。

| 任务 | 描述 |
| --- | --- |
| 导入着火数据 | 从文件导入此损失数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  | **Input command** | Required Data | Optional Data | | --- | --- | --- | | `Fuel mass` | - 发动机转速，rpm - 每冲程喷射的指令燃料质量，mg - 发动机扭矩，N·m | - 空气质量流量，kg/s - 制动比燃料消耗，  g/(kW·h) - CO2 质量流量，kg/s - CO 质量流量，kg/s - 排气温度，K - 燃料质量流量，kg/s - HC 质量流量，kg/s - NOx 质量流量，kg/s - 颗粒物质量流量，  kg/s | | `Torque` | - 发动机转速，rpm - 发动机扭矩，N·m |  在喷油器喷射燃料时，在稳态运行条件下采集着火数据。数据应覆盖发动机转速和扭矩运行范围。Model-Based Calibration Toolbox 使用着火数据边界作为最大扭矩。  要过滤或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox 数据编辑器打开。 |
| 导入非着火数据 | 从文件导入此非着火数据。例如，打开 `<matlabroot>/toolbox/mbc/mbctraining/CiEngineData.xlsx`。  - 发动机转速，rpm - 发动机扭矩，N·m    在燃料切断时，在稳态运行条件下采集非着火（倒拖）数据。所有非着火扭矩点必须小于零。非着火数据仅是发动机转速的函数。 |
| 生成响应模型 | 对于着火和非着火数据，Model-Based Calibration Toolbox 使用测试计划将数据拟合到高斯过程模型 (GPM)。  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准着火和非着火响应模型并生成校准后的表格。  要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准结果更新模块查找表和断点参数。 |

### 气缸空气质量

该模块使用以下方程计算归一化气缸空气质量。

MNom=PstdVdNcylRairTstdL=(60smin)Cps⋅m˙air(1000gKg)Ncyl⋅N⋅MNom

这些方程使用以下变量。

|  |  |
| --- | --- |
| *L* | 归一化气缸空气质量 |
| MNom | 标准温度和压力下、活塞位于下止点 (BDC) 最大体积时的标称发动机气缸空气质量，单位为 kg |
| Cps | 每动力冲程的曲轴转数，rev/stroke |
| Pstd | 标准压力 |
| Tstd | 标准温度 |
| Rair | 空气和已燃气体的混合物的理想气体常数 |
| Vd | 排量 |
| Ncyl | 发动机气缸数 |
| *N* | 发动机转速 |
| m˙intk | 发动机空气质量流量，单位为 g/s |

### 涡轮增压滞后

要对涡轮增压滞后建模，请选择 **Include turbocharger lag effect**。涡轮增压滞后限制每次喷射的最大燃料质量。为对每次喷射的最大燃料质量建模，模块使用带时间常数的一阶系统。在低扭矩下，发动机不需要增压即可提供足够的空气流量。当请求的燃料质量需要增压时，模块使用时间常数确定每次喷射的最大燃料质量。模块针对指定的 **Input command** 设置使用这些方程。

| 计算 | **Input command** 参数设置 | |
| --- | --- | --- |
| `Fuel mass` | `Torque` |
| 动态扭矩 | dFmaxdt=1τeng(Fcmd−Fmax) | dTmaxdt=1τeng(Tcmd−Tmax) |
| 带涡轮增压滞后的每冲程喷射燃料质量或扭矩 | F={Fcmd       when Fcmd<FmaxFmax      when Fcmd≥Fmax | Ttarget={Tcmd       when Tcmd<TmaxTmax      when Tcmd≥Tmax |
| 不带涡轮增压滞后的每冲程喷射燃料质量或扭矩 | F=Fcmd=Fmax | Ttarget=Tcmd=Tmax |
| 增压时间常数 | τbst={τbst,rising       when Fcmd>Fmaxτbst,falling      when Fcmd≤Fmax | τbst={τbst,rising       when Tcmd>Tmaxτbst,falling      when Tcmd≤Tmax |
| 最终时间常数 | τeng={τnat       when Tbrake<fbst(N)τbst       when Tbrake≥fbst(N) | |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Tbrake* | 制动扭矩 |
| *F* | 每冲程喷射燃料质量 |
| *Fcmd*, *Fmax* | 分别为指令和最大每冲程喷射燃料质量 |
| *Ttarget*, *Tcmd*, *Tmax* | 分别为目标、指令和最大扭矩 |
| *τbst* | 增压时间常数 |
| *τbst,rising*, *τbst,falling* | 分别为增压上升和下降时间常数 |
| *τeng* | 最终时间常数 |
| *τnat* | 低于增压扭矩转速线的时间常数 |
| *ƒbst(N)* | 增压扭矩/转速线 |
| *N* | 发动机转速 |

### 燃料流量

为计算高保真模型的燃料经济性，模块使用体积燃料流量。

Qfuel=m˙fuel(1000kgm3)Sgfuel

该方程使用以下变量。

|  |  |
| --- | --- |
| m˙fuel | 燃料质量流量 |
| *Sgfuel* | 燃料比重 |
| *Qfuel* | 体积燃料流量 |

### 功率核算

对于功率核算，模块实现这些方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrCrkshft` | 曲轴功率 | −τengω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃料输入功率 | m˙fuelLHV |
| `PwrLoss` | 功率损失 | τengω−m˙fuelLHV |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | | *未使用* | |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *LHV* | 燃料低热值 |
| *ω* | 发动机转速，rad/s |
| m˙fuel | 燃料质量流量 |
| *τeng* | 每冲程喷射燃料质量时间常数 |
