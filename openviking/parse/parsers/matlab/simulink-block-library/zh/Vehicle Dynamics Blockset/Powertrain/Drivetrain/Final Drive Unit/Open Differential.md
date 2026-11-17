---
type: simulink-block
title: 'Open Differential'
family: 'powertrain'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Final Drive Unit'
documentation_page: 'opendifferential'
documentation_source_path: 'ref/opendifferential.html'
language: zh-CN
chinese_source: worker-translation
---

# Open Differential

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

- 将 **Efficiency factors** 设置为 `Driveshaft
  torque, speed and temperature`。
- 选择 **Input temperature**。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `Driveshft` | `DriveshftTrq` | | 驱动轴扭矩 | N·m |
| `DriveshftSpd` | | 驱动轴转速 | rad/s |
| `Axl1` | `Axl1Trq` | | 车轴 1 扭矩 | N·m |
| `Axl1Spd` | | 车轴 1 转速 | rad/s |
| `Axl2` | `Axl2Trq` | | 车轴 2 扭矩 | N·m |
| `Axl2Spd` | | 车轴 2 转速 | rad/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | 来自驱动轴的机械功率 | W |
| `PwrAxl1` | 来自车轴 1 的机械功率 | W |
| `PwrAxl2` | 来自车轴 2 的机械功率 | W |
| `PwrTrnsfrd` | `PwrMechLoss` | 总功率损失 | W |
| `PwrDampLoss` | 阻尼导致的功率损失 | W |
| `PwrStored` | `PwrStoredShft` | 存储内能的变化率 | W |

### **DriveshftSpd** — 角速度 `scalar`

驱动轴角速度，*ωd*，单位为 rad/s。

### **Axl1Spd** — 角速度 `scalar`

车轴 1 角速度，*ω1*，单位为 rad/s。

### **Axl2Spd** — 角速度 `scalar`

车轴 2 角速度，*ω2*，单位为 rad/s。

## 参数

#### 模块选项

### **Efficiency factors** — 指定配置 `Constant` (default) | `Driveshaft torque, speed and temperature`

为了考虑模块效率，请使用 **Efficiency factors** 参数。下表总结了每种设置对应的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可使用 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率是基础齿轮输入扭矩、空气温度和驱动轴转速的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以创建输入端口。 - 设置 **Ambient temperature, Tamb** 参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅 Interpolation Methods。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DiffEffModelPopup` |
| **值：** | `Constant` (default) | `Driveshaft torque, speed and temperature` |
| **数据类型：** | `character vector` |

### **Interpolation method** — 方法 `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

有关详细信息，请参阅 Interpolation Methods。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InterpMethod` |
| **值：** | `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Input ambient temperature** — 创建输入端口 `off` (default) | `on`

选择以创建用于温度的输入端口 `Temp`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `extTamb` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Crown wheel (ring gear) located** — 指定冠轮连接 `To the left of center-line` (default) | `To the right of center-line`

指定冠轮与驱动轴的连接。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `shaftSwitchMask` |
| **值：** | `To the left of center-line` (default) | `To the right of center-line` |
| **数据类型：** | `character vector` |

### **Carrier to drive shaft ratio, Ndiff** — 传动比 `4` (default) | `scalar`

托架与驱动轴之间的齿轮传动比，*N*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndiff` |
| **值：** | `4` (default) | `scalar` |
| **数据类型：** | `double` |

### **Carrier inertia, Jd** — 转动惯量 `.1` (default) | `scalar`

冠齿轮组件的转动惯量，*Jd*，单位为 kg·m^2。您可以包括驱动轴转动惯量。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jd` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **Carrier damping, bd** — 阻尼 `1e-3` (default) | `scalar`

冠轮线性粘性阻尼，*bd*，单位为 N·m·s/rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bd` |
| **值：** | `1e-3` (default) | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 inertia, Jw1** — 转动惯量 `.1` (default) | `scalar`

车轴 1 转动惯量，*J1*，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw1` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 damping, bw1** — 阻尼 `1e-3` (default) | `scalar`

车轴 1 线性粘性阻尼，*b1*，单位为 N·m·s/rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw1` |
| **值：** | `1e-3` (default) | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 inertia, Jw2** — 转动惯量 `.1` (default) | `scalar`

车轴 2 转动惯量，*J2*，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw2` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 damping, bw2** — 阻尼 `1e-3` (default) | `scalar`

车轴 2 线性粘性阻尼，*b2*，单位为 N·m·s/rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw2` |
| **值：** | `1e-3` (default) | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 initial velocity, omegaw1o** — 角速度 `0` (default) | `scalar`

车轴 1 初始速度，*ωo1*，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw1o` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 initial velocity, omegaw2o** — 角速度 `0` (default) | `scalar`

车轴 2 初始速度，*ωo2*，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw2o` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

#### 效率

### **Constant efficiency factor, eta** — 效率 `1` (default) | positive scalar

恒定效率，*η*。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta` |
| **值：** | `1` (default) | positive scalar |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Constant`。

### **Efficiency lookup table, eta\_tbl** — 查找表 `M`-by-`N`-by-`L` array

无量纲效率值数组，它是以下各项的函数：

- `M` 个输入扭矩
- `N` 个输入转速
- `L` 个空气温度

每个值指定特定扭矩、转速和温度组合下的效率。数组大小必须与扭矩、转速和温度断点向量定义的维度匹配。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_tbl` |
| **值：** | `M`-by-`N`-by-`L` array |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency torque breakpoints, Trq\_bpts** — 扭矩断点 `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector

用于效率的输入扭矩断点向量，单位为 N·m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_bpts` |
| **值：** | `[25, 50, 75, 100, 150, 200, 250]` (default) | `1`-by-`M` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency speed breakpoints, omega\_bpts** — 转速断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector

用于效率的转速断点向量，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_bpts` |
| **值：** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]` (default) | `1`-by-`N` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency temperature breakpoints, Temp\_bpts** — 温度断点 `[290 358]` (default) | `1`-by-`L` vector

用于效率的环境温度断点向量，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_bpts` |
| **值：** | `[290 358]` (default) | `1`-by-`L` vector |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Ambient temperature, Tamb** — 环境温度 `297.15` (default) | `scalar`

环境空气温度，*Tair*，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tamb` |
| **值：** | `297.15` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数：

- 将 **Efficiency factors** 设置为 `Driveshaft
  torque, speed and temperature`。
- 清除 **Input ambient temperature**。

## 所属库

Powertrain Blockset / Drivetrain / Final Drive Unit Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

作为行星锥齿轮的差速器

Open Differential 模块将差速器实现为行星锥齿轮系。该模块将驱动轴锥齿轮与冠轮（齿圈）锥齿轮匹配。您可以指定：

- 托架与驱动轴传动比
- 冠轮位置
- 车轴和托架的粘性阻尼系数

使用 Open Differential 模块可以：

- 将变速器后的驱动轴动态耦合到车轮车轴或万向节
- 在最优牵引力控制不需要被动或主动扭矩矢量分配时，对简化或旧式传动系统建模
- 在通用变速箱和传动系场景中对机械功率分流建模

该模块适用于硬件在环 (HIL) 和优化工作流。所有参数均可调。

该模块使用的坐标系对于标准发动机、变速器和差速器配置会产生正的轮胎和车辆运动。箭头表示正运动。

传动系统图

### 效率

为了考虑模块效率，请使用 **Efficiency factors** 参数。下表总结了每种设置对应的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可使用 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率是基础齿轮输入扭矩、空气温度和驱动轴转速的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以创建输入端口。 - 设置 **Ambient temperature, Tamb** 参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅 Interpolation Methods。 |

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 来自驱动轴的机械功率 | ηTdωd |
| `PwrAxl1` | 来自半轴 1 的机械功率 | ηT1ω1 |
| `PwrAxl2` | 来自半轴 2 的机械功率 | ηT2ω2 |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrMechLoss` | 总功率损耗 | W˙loss= −(Pt+Pd)+PsPt=ηTdωd+ηT1ω1+ηT2ω2 |
| `PwrDampLoss` | 阻尼导致的功率损耗 | Pd=−(b1|ω1|+b2|ω2|+bd|ωd|) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 存储内部能量的变化率 | Ps=−(ω1ω˙1J1+ω2ω˙2J2+ωdω˙dJd) |

### 动力学

Open Differential 模块实现以下微分方程，以表示冠齿轮、左半轴和右半轴的机械动态响应。

| 机械动态响应 | 微分方程 |
| --- | --- |
| 冠齿轮 | ω˙dJd=ηTd-ωdbd-Ti |
| 左半轴 | ω˙1J1=ηT1-ω1b1-Ti1 |
| 右半轴 | ω˙2J2=ηT2-ω2b2-Ti2 |

Open Differential 模块假定冠齿轮与半轴之间为刚性耦合。以下约束方程适用。

ηTi1= ηTi2=N2Ti

ωd=N2(ω1+ω2)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *N* | 行星架到驱动轴的传动比 |
| *Jd* | 冠齿轮组件的转动惯量 |
| *bd* | 冠齿轮线性粘性阻尼 |
| *ωd* | 驱动轴角速度 |
| *η* | 差速器效率 |
| *J1* | 半轴 1 的转动惯量 |
| *b1* | 半轴 1 的线性粘性阻尼 |
| *ω1* | 半轴 1 转速 |
| *J2* | 半轴 2 的转动惯量 |
| *b2* | 半轴 2 的线性粘性阻尼 |
| *ω2* | 半轴 2 角速度 |
| *Td* | 驱动轴扭矩 |
| *T1* | 半轴 1 扭矩 |
| *T2* | 半轴 2 扭矩 |
| *Ti* | 驱动轴内部阻力扭矩 |
| *Ti1* | 半轴 1 内部阻力扭矩 |
| *Ti2* | 半轴 2 内部阻力扭矩 |
