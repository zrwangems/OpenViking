---
type: simulink-block
title: 'Active Differential'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Final Drive Unit'
documentation_page: 'activedifferential'
documentation_source_path: 'ref/activedifferential.html'
language: zh-CN
chinese_source: worker-translation
---

# Active Differential

## 端口

### 输入

### **Prs1** — 离合器 1 压力 `scalar`

离合器 1 压力，*P1*，单位为
Pa。

### **Prs2** — 离合器 2 压力 `scalar`

离合器 2 压力，*P2*，单位为
Pa。

### **DriveshftTrq** — 驱动轴扭矩 `scalar`

施加的输入扭矩，*Td*，
通常来自发动机驱动轴，单位为 N·m。

### **Axl1Trq** — 扭矩 `scalar`

车轴 1 扭矩，*T1*，单位为
N·m。

### **Axl2Trq** — 扭矩 `scalar`

车轴 2 扭矩，*T2*，单位为
N·m。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | 描述 | 单位 |
| --- | --- | --- | --- |
| `Driveshft` | `DriveshftTrq` | 驱动轴扭矩 | N·m |
| `DriveshftSpd` | 驱动轴角速度 | rad/s |
| `Axl1` | `Axl1Trq` | 车轴 1 扭矩 | N·m |
| `Axl1Spd` | 车轴 1 角速度 | rad/s |
| `Axl2` | `Axl2Trq` | 车轴 2 扭矩 | N·m |
| `Axl2Spd` | 车轴 2 角速度 | rad/s |
| `Cplng` | `CplngTrq1` | 离合器 1 耦合扭矩 | N·m |
| `CplngTrq2` | 离合器 2 耦合扭矩 | N·m |
| `CplngSlipSpd1` | 离合器 1 滑差速度 | rad/s |
| `CplngSlipSpd2` | 离合器 2 滑差速度 | rad/s |
| `CplngPrs1` | 离合器 1 输入压力 | Pa |
| `CplngPrs2` | 离合器 2 输入压力 | Pa |

### **DriveshftSpd** — 角速度 `scalar`

驱动轴角速度，
*ωd*，单位为 rad/s。

### **Axl1Spd** — 角速度 `scalar`

车轴 1 角速度，*ω1*，
单位为 rad/s。

### **Axl2Spd** — 角速度 `scalar`

车轴 2 角速度，*ω2*，
单位为 rad/s。

## 参数

#### Active Differential

### **Active differential type** — 差速器 `Spur gears, superposition clutches`（默认）| `Double planetary gears, stationary clutches`

指定主动差速器的类型。

| 设置 | 模块实现 |
| --- | --- |
| `Spur gears, superposition clutches` | 离合器通过三连齿轮系统和差速器壳体叠加 |
| `Double planetary gears, stationary clutches` | 离合器通过双行星齿轮组固定到行星架和车轴上 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `diffType` |
| **值**：| `Spur gears, superposition clutches`（默认）| `Double planetary gears, stationary clutches` |
| **Data Types:** | `character vector` |

### **Clutch 1 to differential case gear ratio, Ns1** — 离合器 1 直齿轮传动比 `.875`（默认）| `scalar`

离合器 1 到行星架的直齿轮传动比，
*Ns1*，无量纲。

#### 依赖关系

要启用直齿轮参数，请为 **Active differential
type** 参数选择 `Spur
gears, superposition clutches`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Ns1` |
| **值**：| `.875`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Clutch 2 to differential case gear ratio, Ns2** — 离合器 2 直齿轮传动比 `1.125`（默认）| `scalar`

离合器 2 到行星架的直齿轮传动比，
*Ns2*，无量纲。

#### 依赖关系

要启用直齿轮参数，请为 **Active differential
type** 参数选择 `Spur
gears, superposition clutches`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Ns2` |
| **值**：| `1.125`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Three-gang gear inertia, Jgc** — 转动惯量 `.003`（默认）| `scalar`

三连齿轮转动惯量，
*Jgc*，单位为 kg·m^2。

#### 依赖关系

要启用直齿轮参数，请为 **Active differential
type** 参数选择 `Spur
gears, superposition clutches`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jgc` |
| **值：** | `.003`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 planetary carrier to axle gear ratio, Np1** — Planetary 1 carrier gear ratio `1.125`（默认） | `scalar`

行星排 1 行星架到车轴的传动比，
*Np1*，无量纲。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Np1` |
| **值：** | `1.125`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 sun gear inertia, Js1** — Planetary 1 sun gear inertia `.001`（默认） | `scalar`

行星排 1 太阳轮惯量，
*Js1*，单位为 kg·m^2。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Js1` |
| **值：** | `.001`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 carrier inertia, Jc1** — Planetary 1 carrier inertia `.001`（默认） | `scalar`

行星排 1 行星架惯量，
*Jc1*，单位为 kg·m^2。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jc1` |
| **值：** | `.001`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 ring inertia, Jr1** — Planetary 1 ring gear inertia `.002`（默认） | `scalar`

行星排 1 齿圈惯量，
*Jr1*，kg·m^2。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jr1` |
| **值：** | `.002`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 planetary carrier to axle gear ratio, Np2** — Planetary 2 carrier gear ratio `1.125`（默认） | `scalar`

行星排 2 行星架到车轴的传动比，
*Np2*，无量纲。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Np2` |
| **值：** | `1.125`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 sun gear inertia, Js2** — Planetary 2 sun gear inertia `.001`（默认） | `scalar`

行星排 2 太阳轮惯量，
*Js2*，单位为 kg·m^2。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Js2` |
| **值：** | `.001`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 carrier inertia, Jc2** — Planetary 2 carrier inertia `.001`（默认） | `scalar`

行星齿轮 2 行星架惯量，
*Jc2*，单位为 kg·m^2。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jc2` |
| **值：** | `.001`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 ring inertia, Jr2** — Planetary 2 ring gear inertia `.002`（默认） | `scalar`

行星齿轮 2 齿圈惯量，
*Jr2*，单位为 kg·m^2。

#### 依赖关系

要启用行星齿轮参数，请为
**Active differential type** 参数选择
`Double planetary gears, stationary clutches`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jr2` |
| **值：** | `.002`（默认） | `scalar` |
| **数据类型：** | `double` |

#### Open Differential

### **Crown wheel (ring gear) located** — Specify crown wheel connection `To the left of center-line`（默认） | `To the right of center-line`

指定冠齿轮与驱动轴的连接。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `shaftSwitchMask` |
| **值：** | `To the left of center-line`（默认） | `To the right of center-line` |
| **数据类型：** | `character vector` |

### **Carrier to drive shaft ratio, NC/ND** — Ratio `4`（默认） | `scalar`

行星架与驱动轴的齿轮比，*N*。

指定冠齿轮与驱动轴的连接。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndiff` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Carrier inertia, Jd** — Inertia `.1`（默认） | `scalar`

冠齿轮组件的转动惯量，
*Jd*，单位为 kg·m^2。您可以
包含驱动轴惯量。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jd` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Carrier damping, bd** — Damping `1e-3`（默认） | `scalar`

冠齿轮线性粘性阻尼，
*bd*，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bd` |
| **值：** | `1e-3`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 inertia, Jw1** — Inertia `.1`（默认） | `scalar`

轴 1 转动惯量，*J1*，
单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw1` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 damping, bw1** — 阻尼 `1e-3`（默认）| `scalar`

轴 1 线性粘性阻尼，
*b1*，单位为 N·m·s/rad。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `bw1` |
| **值**：| `1e-3`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Axle 2 inertia, Jw2** — 惯量 `.1`（默认）| `scalar`

轴 2 转动惯量，*J2*，
单位为 kg·m^2。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Jw2` |
| **值**：| `.1`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Axle 2 damping, bw2** — 阻尼 `1e-3`（默认）| `scalar`

轴 2 线性粘性阻尼，
*b2*，单位为 N·m·s/rad。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `bw2` |
| **值**：| `1e-3`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Axle 1 initial velocity, omegaw1o** — 角速度 `0`（默认）| `scalar`

轴 1 初始速度，*ωo1*，单位为
rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `omegaw1o` |
| **值**：| `0`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Axle 2 initial velocity, omegaw2o** — 角速度 `0`（默认）| `scalar`

轴 2 初始速度，*ωo2*，单位为
rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `omegaw2o` |
| **值**：| `0`（默认）| `scalar` |
| **Data Types:** | `double` |

#### Slip Coupling

### **Coupling type** — 扭矩耦合 `Ideal pre-loaded clutch`（默认）| `Slip speed dependent torque data` | `Input torque dependent torque data`

指定扭矩耦合的类型。

| Setting | Block Implementation |
| --- | --- |
| `Pre-loaded ideal clutch` | 扭矩建模为具有恒定速度的湿式离合器 |
| `Slip speed dependent torque data` | 扭矩由查找表确定，该查找表是滑差速度和离合器压力的函数 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `couplingType` |
| **值**：| `Ideal pre-loaded clutch`（默认）| `Slip speed dependent torque data` | `Input torque dependent torque data` |
| **Data Types:** | `character vector` |

### **Effective applied pressure area** — 压力面积 `0.01`（默认）| `scalar`

有效施加压力面积，单位为 N/m^2。

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Ideal pre-loaded clutch`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Aeff` |
| **值**：| `0.01`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Number of disks, Ndisks** — 扭矩耦合 `4`（默认）| `scalar`

磁盘数量。

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Ideal pre-loaded clutch`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndisks` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

### **有效半径，Reff** — 半径 `.20`（默认） | `scalar`

有效半径 Reff，与施加的离合器摩擦力一起用于确定摩擦力。有效半径定义为：

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

该方程使用以下变量。

|  |  |
| --- | --- |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Ideal pre-loaded clutch`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Reff` |
| **值：** | `.20`（默认） | `scalar` |
| **数据类型：** | `double` |

### **标称预紧力，Fc** — 力 `500`（默认） | `scalar`

标称预紧力，单位为 N。

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Ideal pre-loaded clutch`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fc` |
| **值：** | `500`（默认） | `scalar` |
| **数据类型：** | `double` |

### **摩擦系数向量，mu** — 摩擦 `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125 .10125]`（默认） | `vector`

摩擦系数向量。

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Ideal pre-loaded clutch`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu` |
| **值：** | `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125 .10125]`（默认） | `vector` |
| **数据类型：** | `double` |

### **滑移速度向量，dw** — 角速度 `[0 10 20 40 60 80 100 500]`（默认） | `vector`

滑移速度向量，单位为 rad/s。

要启用离合器参数，请为 **Coupling type** 参数选择 `Ideal pre-loaded clutch`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dw` |
| **值：** | `[0 10 20 40 60 80 100 500]`（默认） | `vector` |
| **数据类型：** | `double` |

### **扭矩 - 滑移速度矩阵，TdPdw** — 离合器扭矩 `[-1000,-500,-90,-50,-5,0,5,50,90,500,1000].*ones(11)`（默认） | `matrix`

扭矩矩阵，*Tc*，单位为 N·m。

#### 依赖关系

要启用滑移速度参数，请为 **Coupling type** 参数选择 `Slip speed dependent torque data`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TdPdw` |
| **值：** | `[-1000,-500,-90,-50,-5,0,5,50,90,500,1000].*ones(11)`（默认） | `matrix` |
| **数据类型：** | `double` |

### **离合器压力向量，pT** — 离合器压力断点 `[0 1e3 5e3 7e3 1e4 2e4 5e4 1e5 5e5 1e6 5e6]`（默认） | `vector`

离合器压力断点向量，*P1,2*，单位为 Pa。

#### 依赖关系

要启用滑移速度参数，请为 **Coupling type** 参数选择 `Slip speed dependent torque data`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `pT` |
| **值：** | `[0 1e3 5e3 7e3 1e4 2e4 5e4 1e5 5e5 1e6 5e6]`（默认） | `vector` |
| **数据类型：** | `double` |

### **转差速度向量，dwT** — 转差速度断点 `[-500 -200, -175, -100, - 50, 0, 50, 100, 175, 200, 500]`（默认） | `vector`

转差速度断点向量，*ω*，单位为 rad/s。

#### 依赖关系

要启用转差速度参数，请为 **Coupling type** 参数选择 `Slip speed dependent torque data`。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dwT` |
| **值：** | `[-500 -200, -175, -100, - 50, 0, 50, 100, 175, 200, 500]`（默认） | `vector` |
| **数据类型：** | `double` |

### **耦合时间常数，tauC** — 常数 `.01`（默认） | `scalar`

耦合时间常数，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tauC` |
| **值：** | `.01`（默认） | `scalar` |
| **数据类型：** | `double` |

## 所属库

Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

斜齿轮或行星齿轮主动差速器

Active Differential 模块实现主动差速器，用于考虑从变速器到车轴的功率传递。该模块将主动差速器建模为开放式差速器与斜齿轮或行星齿轮差速器组耦合的形式。该模块使用外部压力信号来调节离合器压力，以加速或减速每个车轴的旋转。

在硬件在环（HIL）和优化工作流中使用该模块，当您想要将变速器扭矩引导至特定车轴时，动态地将传动轴与车轮车轴耦合。对于详细的前轮驱动研究，使用该模块将传动轴与万向节耦合。该模块适用于系统级闭环控制研究，例如横摆稳定性和扭矩矢量分配。所有参数均可调。

要指定主动差速器，请打开 **Active Differential** 参数并指定 **Active differential type**。

| 设置 | 模块实现 |
| --- | --- |
| `Spur gears, superposition clutches` | 离合器通过三挡齿轮系统和差速器壳体叠加 |
| `Double planetary gears, stationary clutches` | 离合器通过双行星齿轮组固定在行星架和车轴上 |

使用 **Open Differential** 参数 **Crown wheel (ring gear) located** 来指定开放式差速器的位置，位于中心线的左侧或右侧。

根据可用数据，要指定耦合施加到车轴的不同扭矩的方法，请使用 **Slip Coupling** 参数 **Coupling type**。

| 设置 | 模块实现 |
| --- | --- |
| `Pre-loaded ideal clutch` | 扭矩建模为具有恒定摩擦系数的干式离合器 |
| `Slip speed dependent torque data` | 扭矩由查找表确定，该查找表是滑移速度和离合器压力的函数 |

Active Differential 模块不包括控制器或外部离合器执行器动力学。使用此信息来控制输入离合器压力。信息总线包含离合器 1 处的滑移速度 *Δωcl1* 和离合器 2 处的滑移速度 *Δωcl2*。

| 输入车轴扭矩 | *Δωcl1* | *Δωcl2* | 输入离合器压力 |
| --- | --- | --- | --- |
| 正车轴 1 扭矩 | `> 0` | 不适用 | 增加离合器 1 压力 |
| 正车轴 1 扭矩 | `< 0` | 不适用 | 分离离合器 1 和 2 |
| 正车轴 2 扭矩 | 不适用 | `> 0` | 增加离合器 1 压力 |
| 正车轴 2 扭矩 | 不适用 | `< 0` | 分离离合器 1 和 2 |

### Differentials

Active Differential 模块实现这些方程，以表示叠加式和固定式离合器配置的机械动态响应。为确定齿轮比，该模块使用离合器速度和每个齿轮副的齿数。允许车轮速度差（AWSD）限制正扭矩下的车轮速度差。

| 机械动态响应 | 方程 | |
| --- | --- | --- |
| 叠加式离合器和直齿轮传动 | 固定式离合器和行星齿轮传动 |
| 冠齿轮 | ω˙d(Jd+Jgs)=Td−ωdbd−Ti | ω˙d( Jd+Js1+Js2)=Td−ωdbd−Ti |
| 车轴 1 | ω˙1J1=ηT1-ω1b1-Ti1 | ω˙1(J1+Jr1)=T1−ω1b1−Ti1 |
| 车轴 2 | ω˙2J2=ηT2-ω2b2-Ti2 | ω˙2(Jaxle2+Jr1)=T2−ω2b2−Ti2 |
| 齿轮比 | ωcl1ωd=Ns1=z1z6z4z3ωcl2ωd=Ns2=z1z5z4z2 | ωcl1ωd=Np1=z1z6z4z3ωcl2ωd=Np2=z1z5z4z2 |
| 刚性联接约束 | T1= NTi2−Ns22Tcl2+Ns12Tcl1T2= NTi2+(1−Ns22)Tcl2−(1−Ns12)Tcl1ωd==N2(ω1+ω2) | T1= NTi2−Np2(Np2−1)2Tcl2+(2−Np1)(Np1−1)2Tcl1T2= NTi2+(2−Np2)(Np2−1)2Tcl2−Np1(Np1−1)2Tcl1ωd==N2(ω1+ω2) |
| 允许车轮速度差（AWSD） | Δω¯max=(Ns2−Ns1)⋅100% | Δω¯max=(Np1,2−1)⋅100% |

**叠加式离合器和直齿轮传动**

这些叠加式离合器图示展示了向左侧车轮传递扭矩的离合器配置和示意图。

向左侧车轮传递扭矩的详细图示

向左侧车轮传递离合器扭矩的示意图

**固定式离合器和行星齿轮传动**

这些图示展示了固定式离合器配置和示意图。

固定式离合器的详细图示

固定式离合器的示意图

### Slip Coupling

对于理想离合器和滑移转速两种配置，滑移耦合都是滑移转速和离合器压力的函数。滑移转速取决于每个离合器接口处的滑移速度。

ϖ=[Δωc1,Δωc2]

**理想离合器**

理想离合器耦合模型使用车轴滑移转速、离合器压力和摩擦来计算离合器扭矩。摩擦系数是滑移转速的函数。

TC=FTNdμ(|ω¯|)Refftanh(4ω¯)

为计算总离合器力，该模块使用有效半径、离合器压力和离合器预紧力。

FT= FC+P1,2Aeff, FT≥0

圆盘半径决定离合器力作用的有效离合器半径。

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

**滑移转速**

为计算离合器扭矩，滑移转速耦合模型使用作为滑移转速和离合器压力函数的扭矩数据。车轴的角速度决定滑移转速。

TC=TC(ϖ, P1,2)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Aeff* | 有效离合器压力面积 |
| *bd* | 冠齿轮线性粘性阻尼 |
| *b1*、*b2* | 分别为车轴 1 和 2 的线性粘性阻尼 |
| *Fc*、*FT* | 分别为离合器预紧力和总力 |
| *Jd* | 行星架转动惯量 |
| *Jgc* | 三联齿轮转动惯量 |
| *Jc1*、*Jc2* | 分别为行星架 1 和 2 的转动惯量 |
| *Jr1*、*Jr2* | 分别为行星齿圈 1 和 2 的转动惯量 |
| *Js1*、*Js2* | 分别为行星太阳轮 1 和 2 的转动惯量 |
| *J1*、*J2* | 分别为车轴 1 和 2 的转动惯量 |
| *N* | 行星架到驱动轴齿轮比 |
| *Nd* | 圆盘数 |
| *Ns1*、*Ns2* | 分别为离合器 1 和 2 的行星架到正齿轮齿轮比 |
| *Np1*、*Np2* | 分别为行星齿轮 1 和 2 的行星架到车轴齿轮比 |
| *P1*、*P2* | 分别为离合器 1 和 2 的压力 |
| *Reff* | 有效离合器半径 |
| *Ri*、*Ro* | 分别为环形圆盘内半径和外半径 |
| *Tc* | 离合器扭矩 |
| *Tcl1*、*Tcl2* | 分别为离合器 1 和 2 的耦合扭矩 |
| *Td* | 驱动轴扭矩 |
| *T1*、*T2* | 分别为车轴 1 和 2 的扭矩 |
| *Ti* | 车轴内阻扭矩 |
| *Ti1*、*Ti2* | 车轴 1 和 2 的内阻扭矩 |
| *ωd* | 驱动轴角速度 |
| *ϖ* | 滑移转速 |
| *ω1*、*ω2* | 分别为车轴 1 和 2 的角速度 |
| *Δωcl1*、*Δωcl2* | 分别为离合器 1 和 2 在接口处的滑移转速 |
| *ωcl1*、*ωcl2* | 分别为离合器 1 和 2 的角速度 |
| *μ* | 离合器摩擦系数 |
| *zi* | 齿轮 *i* 的齿数 |
