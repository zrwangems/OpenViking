---
type: simulink-block
title: 'Transfer Case'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain'
documentation_page: 'transfercase'
documentation_source_path: 'ref/transfercase.html'
language: zh-CN
chinese_source: worker-translation
---

# Transfer Case

## 端口

### 输入

### **DriveshftTrq** — 扭矩 `scalar`

施加的输入扭矩，通常来自发动机曲轴，单位为 N·m。

### **Axl1Trq** — 扭矩 `scalar`

车轴 1 扭矩，*T1*，单位为 N·m。

### **Axl2Trq** — 扭矩 `scalar`

车轴 2 扭矩，*T2*，单位为 N·m。

### **Temp** — 温度 `scalar`

温度，单位为 K。

#### 依赖关系

要启用此端口：

- 将 **效率因子** 设置为 `Driveshaft
  torque, speed and temperature`。
- 选择 **输入温度**。

### **TrqSplitRatioConstant** — 前轴扭矩分配比 `scalar`

前轴扭矩分配比。

#### 依赖关系

要启用此端口，请选择 **输入前轴扭矩分配比,
TrqSplitRatio**。

### **SpdLockConstant** — 车轴速度锁 `scalar`

车轴速度锁。

#### 依赖关系

要启用此端口，请选择 **输入车轴速度锁,
SpdLock**。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `Driveshft` | `DriveshftTrq` | | 传动轴扭矩 | N·m |
| `DriveshftSpd` | | 传动轴速度 | rad/s |
| `Axl1` | `Axl1Trq` | | 车轴 1 扭矩 | N·m |
| `Axl1Spd` | | 车轴 1 速度 | rad/s |
| `Axl2` | `Axl2Trq` | | 车轴 2 扭矩 | N·m |
| `Axl2Spd` | | 车轴 2 速度 | rad/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | 来自传动轴的机械功率 | W |
| `PwrAxl1` | 来自车轴 1 的机械功率 | W |
| `PwrAxl2` | 来自车轴 2 的机械功率 | W |
| `PwrTrnsfrd` | `PwrMechLoss` | 总功率损失 | W |
| `PwrDampLoss` | 阻尼导致的功率损失 | W |
| `PwrStored` | `PwrStoredShft` | 存储内能的变化率 | W |

### **DriveshftSpd** — 角速度 `scalar`

传动轴角速度，*ωd*，单位为
rad/s。

### **Axl1Spd** — 角速度 `scalar`

车轴 1 角速度，*ω1*，单位为
rad/s。

### **Axl2Spd** — 角速度 `scalar`

车轴 2 角速度，*ω2*，单位为
rad/s。

## 参数

#### 模块选项

### **效率因子** — 指定配置 `Constant` (default) | `Driveshaft torque, speed and temperature`

为了考虑模块效率，请使用 **效率因子** 参数。下表总结了每种设置下的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **恒定效率因子, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率随基础齿轮输入扭矩、空气温度和传动轴速度变化。使用以下参数指定查找表和断点：  - **效率查找表,   eta\_tbl** - **效率扭矩断点,   Trq\_bpts** - **效率速度断点,   omega\_bpts** - **效率温度断点,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **输入环境温度** 以   创建输入端口。 - 设置 **环境温度, Tamb**   参数值。    要选择插值方法，请使用 **插值方法** 参数。有关详细信息，请参阅插值方法。 |

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DiffEffModelPopup` |
| **值：** | `Constant` (default) | `Driveshaft torque, speed and temperature` |
| **数据类型：** | `character vector` |

### **插值方法** — 方法 `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

有关详细信息，请参阅插值方法。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InterpMethod` |
| **值：** | `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为
`Driveshaft torque, speed and temperature`。

### **输入环境温度** — 创建输入端口 `off` (default) | `on`

选择此项可创建用于温度的输入端口 `Temp`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `extTamb` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为
`Driveshaft torque, speed and temperature`。

### **输入前轴扭矩分配比, TrqSplitRatio** — 创建输入端口 `off` (default) | `on`

选择此项可创建用于前轴扭矩分配比的输入端口 `TrqSplitRatioConstant`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqSplitRatio` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

### **输入车轴速度锁, SpdLock** — 创建输入端口 `off` (default) | `on`

选择此项可创建用于车轴速度锁的输入端口 `SpdLockConstant`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SpdLock` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

### **冠齿轮（齿圈）位置** — 指定冠齿轮连接 `To the left of center-line` (default) | `To the right of center-line`

指定冠齿轮与传动轴的连接。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `shaftSwitchMask` |
| **值：** | `To the left of center-line` (default) | `To the right of center-line` |
| **数据类型：** | `character vector` |

### **差速器壳体到传动轴比, Ndiff** — 比例 `4` (default) | `scalar`

差速器壳体到传动轴齿轮比，*N*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndiff` |
| **值：** | `4` (default) | `scalar` |
| **数据类型：** | `double` |

### **差速器壳体惯量, Jd** — 惯量 `.1` (default) | `scalar`

冠齿轮总成的转动惯量，*Jd*，单位为 kg·m^2。您可以包括传动轴惯量。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jd` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **差速器壳体阻尼, bd** — 阻尼 `1e-3` (default) | `scalar`

冠齿轮线性粘性阻尼，*bd*，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bd` |
| **值：** | `1e-3` (default) | `scalar` |
| **数据类型：** | `double` |

### **车轴 1 惯量, Jw1** — 惯量 `.1` (default) | `scalar`

车轴 1 转动惯量，*J1*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw1` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **车轴 1 阻尼, bw1** — 阻尼 `1e-3` (default) | `scalar`

车轴 1 线性粘性阻尼，*b1*，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw1` |
| **值：** | `1e-3` (default) | `scalar` |
| **数据类型：** | `double` |

### **车轴 2 惯量, Jw2** — 惯量 `.1` (default) | `scalar`

车轴 2 转动惯量，*J2*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw2` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **车轴 2 阻尼, bw2** — 阻尼 `1e-3` (default) | `scalar`

车轴 2 线性粘性阻尼，*b2*，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw2` |
| **值：** | `1e-3` (default) | `scalar` |
| **数据类型：** | `double` |

### **车轴 1 初始速度, omegaw1o** — 角速度 `0` (default) | `scalar`

车轴 1 初始速度，*ωo1*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw1o` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **车轴 2 初始速度, omegaw2o** — 角速度 `0` (default) | `scalar`

车轴 2 初始速度，*ωo2*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw2o` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

#### 效率

### **恒定效率因子, eta** — 效率 `1` (default) | positive scalar

恒定效率，*η*。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta` |
| **值：** | `1` (default) | positive scalar |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子**
设置为 `Constant`。

### **效率查找表, eta\_tbl** — 查找表 `M`-by-`N`-by-`L` array

无量纲的效率值数组，它是以下项的函数：

- `M` 个输入扭矩
- `N` 个输入速度
- `L` 个空气温度

每个值指定特定扭矩、速度和温度组合下的效率。数组大小必须与扭矩、速度和温度断点向量定义的维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_tbl` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为
`Driveshaft torque, speed and temperature`。

### **效率扭矩断点, Trq\_bpts** — 扭矩断点 `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector

输入扭矩向量，效率断点，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_bpts` |
| **值：** | `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为
`Driveshaft torque, speed and temperature`。

### **效率速度断点, omega\_bpts** — 速度断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector

速度向量，效率断点，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_bpts` |
| **值：** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为
`Driveshaft torque, speed and temperature`。

### **效率温度断点, Temp\_bpts** — 温度断点 `[290 358]` (default) | `1`-by-`L` vector

环境温度断点向量，用于效率，单位为 K。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_bpts` |
| **值：** | `[290 358]` (default) | `1`-by-`L` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为
`Driveshaft torque, speed and temperature`。

### **环境温度, Tamb** — 环境温度 `297.15` (default) | `scalar`

环境空气温度，*Tair*，单位为 K。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tamb` |
| **值：** | `297.15` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数：

- 将 **效率因子** 设置为 `Driveshaft
  torque, speed and temperature`。
- 清除 **输入环境温度**。

### **前轴扭矩分配比, TrqSplitRatio** — 前轴扭矩分配比 `0.5` (default) | `scalar`

前轴扭矩分配比。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqSplitRatio` |
| **值：** | `0.5` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **输入前轴扭矩分配比,
TrqSplitRatio**。

### **车轴速度锁, SpdLock** — 车轴速度锁 `0` (default) | `scalar`

车轴速度锁。将此值设置为 0 可使前、后车轴的转速不固定。将此值设置为 1 可使前、后车轴的转速固定。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SpdLock` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **输入车轴速度锁,
SpdLock**。

## 所属库

Powertrain Blockset / Drivetrain / Final Drive Unit Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

作为行星锥齿轮的差速器

Transfer Case 模块将差速器实现为行星锥齿轮系。该模块将传动轴锥齿轮与冠状（齿圈）锥齿轮匹配。您可以指定：

- 行星架与传动轴速比
- 冠状齿轮位置
- 车轴和行星架的粘性系数与阻尼系数

使用 Transfer Case 模块可以：

- 将变速箱后的传动轴动态耦合到车轮车轴或万向节
- 在最优牵引力控制不需要被动或主动扭矩矢量分配时，对简化或较旧的传动系统进行建模
- 在通用变速箱和传动系场景中对机械功率分流进行建模

该模块适用于硬件在环 (HIL) 和优化工作流。所有参数均可调。

### 效率

为了考虑模块效率，请使用 **Efficiency factors** 参数。下表总结了每种设置的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率是基础齿轮输入扭矩、空气温度和传动轴转速的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以创建输入端口。 - 设置 **Ambient temperature, Tamb** 参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅 Interpolation Methods。 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 来自传动轴的机械功率 | ηTdωd |
| `PwrAxl1` | 来自车轴 1 的机械功率 | ηT1ω1 |
| `PwrAxl2` | 来自车轴 2 的机械功率 | ηT2ω2 |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrMechLoss` | 总功率损耗 | W˙loss= −(Pt+Pd)+PsPt=ηTdωd+ηT1ω1+ηT2ω2 |
| `PwrDampLoss` | 阻尼导致的功率损耗 | Pd=−(b1|ω1|+b2|ω2|+bd|ωd|) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 存储内部能量的变化率 | Ps=−(ω1ω˙1J1+ω2ω˙2J2+ωdω˙dJd) |

### 动力学

Transfer Case 模块实现以下微分方程，以表示冠状齿轮、前车轴和后车轴的机械动态响应。

| 机械动态响应 | 微分方程 |
| --- | --- |
| 冠状齿轮 | ω˙dJd=ηTd-ωdbd-Ti |
| 前车轴 | ω˙1J1=ηT1-ω1b1-Ti1 |
| 后车轴 | ω˙2J2=ηT2-ω2b2-Ti2 |

方程使用以下变量。

|  |  |
| --- | --- |
| *N* | 行星架与传动轴齿轮比 |
| *Jd* | 冠状齿轮组件的转动惯量 |
| *bd* | 冠状齿轮线性粘性阻尼 |
| *ωd* | 传动轴角速度 |
| *η* | 差速器效率 |
| *J1* | 车轴 1 转动惯量 |
| *b1* | 车轴 1 线性粘性阻尼 |
| *ω1* | 车轴 1 转速 |
| *J2* | 车轴 2 转动惯量 |
| *b2* | 车轴 2 线性粘性阻尼 |
| *ω2* | 车轴 2 角速度 |
| *Td* | 传动轴扭矩 |
| *T1* | 车轴 1 扭矩 |
| *T2* | 车轴 2 扭矩 |
| *Ti* | 传动轴内部阻力扭矩 |
| *Ti1* | 车轴 1 内部阻力扭矩 |
| *Ti2* | 车轴 2 内部阻力扭矩 |
