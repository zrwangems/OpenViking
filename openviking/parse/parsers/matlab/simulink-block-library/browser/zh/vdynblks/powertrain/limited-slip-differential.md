---
type: simulink-block
title: 'Limited Slip Differential'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain'
documentation_page: 'limitedslipdifferential'
documentation_source_path: 'ref/limitedslipdifferential.html'
language: zh-CN
chinese_source: worker-translation
---

# Limited Slip Differential

## 端口

### 输入

### **DriveshftTrq** — 扭矩 `scalar`

施加的输入扭矩，通常来自发动机曲轴，单位为 N·m。

### **Axl1Trq** — 扭矩 `scalar`

半轴 1 扭矩，*T1*，单位为 N·m。

### **Axl2Trq** — 扭矩 `scalar`

半轴 2 扭矩，*T2*，单位为 N·m。

### **Temp** — 温度 `scalar`

温度，单位为 K。

#### 依赖

要启用此端口：

- 将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。
- 选择 **输入温度**。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `Driveshft` | `DriveshftTrq` | | 驱动轴扭矩 | N·m |
| `DriveshftSpd` | | 驱动轴速度 | rad/s |
| `Axl1` | `Axl1Trq` | | 半轴 1 扭矩 | N·m |
| `Axl1Spd` | | 半轴 1 速度 | rad/s |
| `Axl2` | `Axl2Trq` | | 半轴 2 扭矩 | N·m |
| `Axl2Spd` | | 半轴 2 速度 | rad/s |
| `Cplng` | `CplngTrq` | | 扭矩耦合 | N·m |
| `CplngSlipSpd` | | 滑差速度 | rad/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | 来自驱动轴的机械功率 | W |
| `PwrAxl1` | 来自半轴 1 的机械功率 | W |
| `PwrAxl2` | 来自半轴 2 的机械功率 | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | 总功率损耗 | W |
| `PwrDampLoss` | 因阻尼导致的功率损耗 | W |
| `PwrCplngLoss` | 因离合器导致的功率损耗 | W |
| `PwrStoredShft` | `PwrStoredShft` | 存储内能的变化率 | W |

### **DriveshftSpd** — 角速度 `scalar`

驱动轴角速度，*ωd*，单位为 rad/s。

### **Axl1Spd** — 角速度 `scalar`

半轴 1 角速度，*ω1*，单位为 rad/s。

### **Axl2Spd** — 角速度 `scalar`

半轴 2 角速度，*ω2*，单位为 rad/s。

## 参数

#### 模块选项

### **效率因子** — 指定配置 `Constant` (默认) | `Driveshaft torque, speed and temperature`

为了考虑模块效率，请使用 **效率因子** 参数。下表总结了每种设置下的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率作为基础齿轮输入扭矩、空气温度和驱动轴速度的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以    创建输入端口。 - 设置 **Ambient temperature, Tamb**   参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅 Interpolation Methods。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DiffEffModelPopup` |
| **值：** | `Constant` (默认) | `Driveshaft torque, speed and temperature` |
| **数据类型：** | `character vector` |

### **插值方法** — 方法 `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

有关详细信息，请参阅 Interpolation Methods。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InterpMethod` |
| **值：** | `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **数据类型：** | `character vector` |

#### 依赖

要启用此参数，请将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。

### **输入环境温度** — 创建输入端口 `off` (默认) | `on`

选择此项可创建用于温度的输入端口 `Temp`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `extTamb` |
| **值：** | `off` (默认) | `on` |
| **数据类型：** | `character vector` |

#### 依赖

要启用此参数，请将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。

#### 开放式差速器

### **冠齿轮（齿圈）位置** — 指定冠齿轮连接 `To the left of center-line` (默认) | `To the right of center-line`

指定冠齿轮与驱动轴的连接。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `shaftSwitchMask` |
| **值：** | `To the left of center-line` (默认) | `To the right of center-line` |
| **数据类型：** | `character vector` |

### **行星架与驱动轴传动比, NC/ND** — 传动比 `4` (默认) | `scalar`

行星架与驱动轴的齿轮传动比，*N*。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndiff` |
| **值：** | `4` (默认) | `scalar` |
| **数据类型：** | `double` |

### **行星架惯性, Jd** — 惯性 `.1` (默认) | `scalar`

冠齿轮组件的转动惯量，*Jd*，单位为 kg·m^2。您可以包含驱动轴惯量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jd` |
| **值：** | `.1` (默认) | `scalar` |
| **数据类型：** | `double` |

### **行星架阻尼, bd** — 阻尼 `1e-3` (默认) | `scalar`

冠齿轮线性粘性阻尼，*bd*，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bd` |
| **值：** | `1e-3` (默认) | `scalar` |
| **数据类型：** | `double` |

### **半轴 1 惯性, Jw1** — 惯性 `.1` (默认) | `scalar`

半轴 1 转动惯量，*J1*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw1` |
| **值：** | `.1` (默认) | `scalar` |
| **数据类型：** | `double` |

### **半轴 1 阻尼, bw1** — 阻尼 `1e-3` (默认) | `scalar`

半轴 1 线性粘性阻尼，*b1*，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw1` |
| **值：** | `1e-3` (默认) | `scalar` |
| **数据类型：** | `double` |

### **半轴 2 惯性, Jw2** — 惯性 `.1` (默认) | `scalar`

半轴 2 转动惯量，*J2*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw2` |
| **值：** | `.1` (默认) | `scalar` |
| **数据类型：** | `double` |

### **半轴 2 阻尼, bw2** — 阻尼 `1e-3` (默认) | `scalar`

半轴 2 线性粘性阻尼，*b2*，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw2` |
| **值：** | `1e-3` (默认) | `scalar` |
| **数据类型：** | `double` |

### **半轴 1 初始速度, omegaw1o** — 角速度 `0` (默认) | `scalar`

半轴 1 初始速度，*ωo1*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw1o` |
| **值：** | `0` (默认) | `scalar` |
| **数据类型：** | `double` |

### **半轴 2 初始速度, omegaw2o** — 角速度 `0` (默认) | `scalar`

半轴 2 初始速度，*ωo2*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw2o` |
| **值：** | `0` (默认) | `scalar` |
| **数据类型：** | `double` |

### **恒定效率因子, eta** — 效率 `1` (默认) | positive scalar

恒定效率，*η*。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta` |
| **值：** | `1` (默认) | positive scalar |
| **数据类型：** | `double` |

#### 依赖

要启用此参数，请将 **效率因子** 设置为 `Constant`。

### **效率查找表, eta\_tbl** — 查找表 `M`-by-`N`-by-`L` array

无量纲效率值数组，作为以下量的函数：

- `M` 个输入扭矩
- `N` 个输入速度
- `L` 个空气温度

每个值指定特定扭矩、速度和温度组合下的效率。数组大小必须与扭矩、速度和温度断点向量定义的维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_tbl` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖

要启用此参数，请将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。

### **效率扭矩断点, Trq\_bpts** — 扭矩断点 `[25, 50, 75, 100, 150, 200, 250]` (默认) | `1`-by-`M` vector

输入扭矩向量，效率断点，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_bpts` |
| **值：** | `[25, 50, 75, 100, 150, 200, 250]` (默认) | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖

要启用此参数，请将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。

### **效率速度断点, omega\_bpts** — 速度断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (默认) | `1`-by-`N` vector

速度向量，效率断点，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_bpts` |
| **值：** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (默认) | `1`-by-`N` vector |
| **数据类型：** | `double` |

#### 依赖

要启用此参数，请将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。

### **效率温度断点, Temp\_bpts** — 温度断点 `[290 358]` (默认) | `1`-by-`L` vector

环境温度断点向量，用于效率，单位为 K。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_bpts` |
| **值：** | `[290 358]` (默认) | `1`-by-`L` vector |
| **数据类型：** | `double` |

#### 依赖

要启用此参数，请将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。

### **环境温度, Tamb** — 环境温度 `297.15` (默认) | `scalar`

环境空气温度，*Tair*，单位为 K。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tamb` |
| **值：** | `297.15` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖

要启用此参数：

- 将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。
- 清除 **输入环境温度**。

#### 滑差耦合

### **耦合类型** — 扭矩耦合 `Pre-loaded ideal clutch` (默认) | `Slip speed dependent torque data` | `Input torque dependent torque data`

指定扭矩耦合的类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `couplingType` |
| **值：** | `Pre-loaded ideal clutch` (默认) | `Slip speed dependent torque data` | `Input torque dependent torque data` |
| **数据类型：** | `character vector` |

### **盘片数量, Ndisks** — 扭矩耦合 `4` (默认) | `scalar`

盘片数量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndisks` |
| **值：** | `4` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖

要启用理想离合器参数，请为 **耦合类型** 参数选择 `Pre-loaded ideal clutch`。

### **有效半径, Reff** — 半径 `.20` (默认) | `scalar`

有效半径 Reff，与施加的离合器摩擦力一起用于确定摩擦力。有效半径定义为：

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

该方程使用以下变量。

|  |  |
| --- | --- |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Reff` |
| **值：** | `.20` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖

要启用离合器参数，请为 **耦合类型** 参数选择 `Pre-loaded ideal clutch`。

### **标称预载力, Fc** — 力 `500` (默认) | `scalar`

标称预载力，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fc` |
| **值：** | `500` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖

要启用离合器参数，请为 **耦合类型** 参数选择 `Pre-loaded ideal clutch`。

### **摩擦系数向量, muc** — 摩擦 `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125]` (默认) | `vector`

摩擦系数向量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `muc` |
| **值：** | `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用离合器参数，请为 **耦合类型**
参数选择 `Pre-loaded ideal clutch`。

### **滑移速度向量，dw** — 角速度 `[0 10 20 40 60 80 100]`（默认） | `vector`

滑移速度向量，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dw` |
| **值：** | `[0 10 20 40 60 80 100]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用离合器参数，请为 **耦合类型** 参数选择 `Pre-loaded ideal clutch`。

### **扭矩 - 滑移速度向量，Tdw** — 扭矩 `[-100, -90, -50, -5, 0, 5, 50, 90, 100]`（默认） | `vector`

扭矩向量，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tdw` |
| **值：** | `[-100, -90, -50, -5, 0, 5, 50, 90, 100]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用滑移速度参数，请为 **耦合类型** 参数选择 `Slip speed dependent torque data`。

### **滑移速度向量，dwT** — 角速度 `[-200, -175, -100, - 50, 0, 50, 100, 175, 200]`（默认） | `vector`

滑移速度向量，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dwT` |
| **值：** | `[-200, -175, -100, - 50, 0, 50, 100, 175, 200]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用滑移速度参数，请为 **耦合类型** 参数选择 `Slip speed dependent torque data`。

### **扭矩 - 输入扭矩向量，TTin** — 扭矩 `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector`

扭矩向量，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TTin` |
| **值：** | `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用输入扭矩参数，请为 **耦合类型** 参数选择 `Input torque dependent torque data`。

### **输入扭矩向量，Tin** — 扭矩 `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector`

扭矩向量，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tin` |
| **值：** | `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用输入扭矩参数，请为 **耦合类型** 参数选择 `Input torque dependent torque data`。

### **耦合时间常数，tauC** — 常数 `.01`（默认） | `scalar`

耦合时间常数，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tauC` |
| **值：** | `.01`（默认） | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Drivetrain / Final Drive Unit Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

作为行星锥齿轮的限滑差速器

Limited Slip Differential 模块将差速器实现为行星锥齿轮系。该模块将传动轴锥齿轮与冠状（齿圈）锥齿轮匹配。您可以指定：

- 行星架与传动轴传动比
- 冠状轮位置
- 车轴和行星架的粘性系数和阻尼系数
- 滑移耦合类型

在系统级传动系统分析中使用该模块，以考虑从变速器到车轮的功率传输。该模块适用于硬件在环（HIL）和优化工作流。所有参数均可调。

在限滑差速器中，为防止其中一个车轮打滑，差速器会分配施加到左、右车轴的扭矩。由于施加到车轴的扭矩不同，车轮可以以不同的角速度运动，从而防止打滑。该模块实现三种方法，用于耦合施加到车轴的不同扭矩：

- Pre-loaded ideal clutch
- Slip speed-dependent torque data
- Input torque dependent torque data

该模块使用一个坐标系，对于标准发动机、变速器和差速器配置，该坐标系产生正的轮胎和车辆运动。箭头指示正方向运动。

变速器示意图

### 效率

为了考虑模块效率，请使用 **效率因子** 参数。下表汇总了每个设置的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可使用 **恒定效率因子，eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率作为基础齿轮输入扭矩、空气温度和传动轴速度的函数。使用以下参数指定查找表和断点：  - **效率查找表，eta\_tbl** - **效率扭矩断点，Trq\_bpts** - **效率速度断点，omega\_bpts** - **效率温度断点，Temp\_bpts**    对于空气温度，您可以：  - 选择 **输入环境温度** 以创建输入端口。 - 设置 **环境温度，Tamb** 参数值。    要选择插值方法，请使用 **插值方法** 参数。有关详细信息，请参阅“插值方法”。 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 来自传动轴的机械功率 | ηTdωd |
| `PwrAxl1` | 来自车轴 1 的机械功率 | ηT1ω1 |
| `PwrAxl2` | 来自车轴 2 的机械功率 | ηT2ω2 |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrMechLoss` | 总功率损失 | W˙loss= −(Pt+Pd+Pc)+PsPt=η(Tdωd+T1ω1+T2ω2) |
| `PwrDampLoss` | 阻尼导致的功率损失 | Pd=−(b1|ω1|+b2|ω2|+bd|ωd|) |
| `PwrCplngLoss` | 离合器导致的功率损失 | Pc=Tc|ω¯| |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 存储内能的变化率 | Ps=−(ω1ω˙1J1+ω2ω˙2J2+ωdω˙dJd) |

### 动力学

Limited Slip Differential 模块实现以下微分方程，以表示冠状齿轮、左车轴和右车轴的机械动态响应。

| 机械动态响应 | 微分方程 |
| --- | --- |
| 冠状齿轮 | ω˙dJd=ηTd-ωdbd-Ti |
| 左车轴 | ω˙1J1=ηT1-ω1b1-Ti1 |
| 右车轴 | ω˙2J2=ηT2-ω2b2-Ti2 |

该模块假设冠状齿轮与车轴之间为刚性耦合。这些约束方程适用。

ηT1=N2Ti−12TcηT2=N2Ti+12Tc

ωd=N2(ω1+ω2)

方程使用以下变量。

|  |  |
| --- | --- |
| *N* | 行星架与传动轴传动比 |
| *Jd* | 冠状齿轮总成的转动惯量 |
| *bd* | 冠状齿轮线性粘性阻尼 |
| *ωd* | 传动轴角速度 |
| ϖ | 滑移速度 |
| *J1* | 车轴 1 转动惯量 |
| *b1* | 车轴 1 线性粘性阻尼 |
| *ω1* | 车轴 1 速度 |
| *J2* | 车轴 2 转动惯量 |
| *b2* | 车轴 2 线性粘性阻尼 |
| *ω2* | 车轴 2 角速度 |
| *η* | 效率 |
| *Td* | 传动轴扭矩 |
| *T1* | 车轴 1 扭矩 |
| *T2* | 车轴 2 扭矩 |
| *Ti* | 车轴内阻扭矩 |
| *Ti1* | 车轴 1 内阻扭矩 |
| *Ti2* | 车轴 2 内阻扭矩 |
| *μ* | 摩擦系数 |
| Reff | 有效离合器半径 |
| Ro | 环形盘外半径 |
| *Ri* | 环形盘内半径 |
| *Fc* | 离合器力 |
| *Tc* | 离合器扭矩 |
| *μ* | 摩擦系数 |

Limited Slip Differential 中的 Table 模块具有以下参数设置：

- **插值方法** — `Linear`
- **外推方法** — `Clip`

**理想离合器耦合**

理想离合器耦合模型使用车轴滑移速度和摩擦来计算离合器扭矩。摩擦系数是滑移速度的函数。

Tc=FcNμ(|ϖ|)Refftanh(4|ϖ|)

圆盘半径确定离合器力作用的有效离合器半径。

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

车轴的角速度确定滑移速度。

ϖ=ω1−ω2

**滑移速度耦合**

为计算离合器扭矩，滑移速度耦合模型使用作为滑移速度函数的扭矩数据。车轴的角速度确定滑移速度。

ϖ=ω1−ω2

**输入扭矩耦合**

为计算离合器扭矩，输入扭矩耦合模型使用作为输入扭矩函数的扭矩数据。

Open Differential 模块假设冠状齿轮与车轴之间为刚性耦合。这些约束方程适用。

ηTi1= ηTi2=N2Ti

ωd=N2(ω1+ω2)
