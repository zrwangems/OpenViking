---
type: simulink-block
title: 'Limited Slip Differential'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Final Drive Unit'
documentation_page: 'limitedslipdifferential'
documentation_source_path: 'ref/limitedslipdifferential.html'
language: zh-CN
chinese_source: worker-translation
---

# Limited Slip Differential

## 端口
```yaml
ports:
- name: DriveshftTrq
  summary: 扭矩 scalar
  direction: input
- name: Axl1Trq
  summary: 扭矩 scalar
  direction: input
- name: Axl2Trq
  summary: 扭矩 scalar
  direction: input
- name: Temp
  summary: 温度 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: DriveshftSpd
  summary: 角速度 scalar
  direction: output
- name: Axl1Spd
  summary: 角速度 scalar
  direction: output
- name: Axl2Spd
  summary: 角速度 scalar
  direction: output
```

### 输入

### **DriveshftTrq** — 扭矩 `scalar`

施加的输入扭矩，通常来自发动机曲轴，单位为 N·m。

### **Axl1Trq** — 扭矩 `scalar`

轴 1 扭矩，*T1*，单位为 N·m。

### **Axl2Trq** — 扭矩 `scalar`

轴 2 扭矩，*T2*，单位为 N·m。

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
| `Axl1` | `Axl1Trq` | | 轴 1 扭矩 | N·m |
| `Axl1Spd` | | 轴 1 转速 | rad/s |
| `Axl2` | `Axl2Trq` | | 轴 2 扭矩 | N·m |
| `Axl2Spd` | | 轴 2 转速 | rad/s |
| `Cplng` | `CplngTrq` | | 扭矩耦合 | N·m |
| `CplngSlipSpd` | | 滑差转速 | rad/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | 来自驱动轴的机械功率 | W |
| `PwrAxl1` | 来自轴 1 的机械功率 | W |
| `PwrAxl2` | 来自轴 2 的机械功率 | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | 总功率损失 | W |
| `PwrDampLoss` | 阻尼导致的功率损失 | W |
| `PwrCplngLoss` | 离合器导致的功率损失 | W |
| `PwrStoredShft` | `PwrStoredShft` | 存储内能的变化率 | W |

### **DriveshftSpd** — 角速度 `scalar`

驱动轴角速度，*ωd*，单位为 rad/s。

### **Axl1Spd** — 角速度 `scalar`

轴 1 角速度，*ω1*，单位为 rad/s。

### **Axl2Spd** — 角速度 `scalar`

轴 2 角速度，*ω2*，单位为 rad/s。
## 参数
```yaml
parameters:
- name: Efficiency factors
  summary: 指定配置 Constant（默认） | Driveshaft torque, speed and temperature
  group: ''
  block_parameter: DiffEffModelPopup
  values: Constant（默认） | Driveshaft torque, speed and temperature
- name: Interpolation method
  summary: 方法 Flat | Nearest | Linear point-slope | Linear Lagrange | Cubic spline
  group: ''
  block_parameter: InterpMethod
  values: Flat | Nearest | Linear point-slope | Linear Lagrange | Cubic spline
- name: Input ambient temperature
  summary: 创建输入端口 off（默认）| on
  group: ''
  block_parameter: extTamb
  values: off（默认）| on
- name: Crown wheel (ring gear) located
  summary: 指定冠轮连接 To the left of center-line（默认）| To the right of center-line
  group: ''
  block_parameter: shaftSwitchMask
  values: To the left of center-line（默认）| To the right of center-line
- name: Carrier to drive shaft ratio, NC/ND
  summary: 传动比 4（默认）| scalar
  group: ''
  block_parameter: Ndiff
  values: 4（默认）| scalar
- name: Carrier inertia, Jd
  summary: 惯量 .1（默认）| scalar
  group: ''
  block_parameter: Jd
  values: .1（默认）| scalar
- name: Carrier damping, bd
  summary: 阻尼 1e-3（默认）| scalar
  group: ''
  block_parameter: bd
  values: 1e-3（默认）| scalar
- name: Axle 1 inertia, Jw1
  summary: 惯量 .1（默认）| scalar
  group: ''
  block_parameter: Jw1
  values: .1（默认）| scalar
- name: Axle 1 damping, bw1
  summary: 阻尼 1e-3（默认）| scalar
  group: ''
  block_parameter: bw1
  values: 1e-3（默认）| scalar
- name: Axle 2 inertia, Jw2
  summary: 惯量 .1（默认）| scalar
  group: ''
  block_parameter: Jw2
  values: .1（默认）| scalar
- name: Axle 2 damping, bw2
  summary: 阻尼 1e-3（默认）| scalar
  group: ''
  block_parameter: bw2
  values: 1e-3（默认） | scalar
- name: Axle 1 initial velocity, omegaw1o
  summary: 角速度 0（默认） | scalar
  group: ''
  block_parameter: omegaw1o
  values: 0（默认） | scalar
- name: Axle 2 initial velocity, omegaw2o
  summary: 角速度 0（默认） | scalar
  group: ''
  block_parameter: omegaw2o
  values: 0（默认） | scalar
- name: Constant efficiency factor, eta
  summary: 效率 1（默认） | 正标量
  group: ''
  block_parameter: eta
  values: 1（默认） | 正标量
- name: Efficiency lookup table, eta_tbl
  summary: 查找表 M×N×L 数组
  group: ''
  block_parameter: eta_tbl
  values: M×N×L 数组
- name: Efficiency torque breakpoints, Trq_bpts
  summary: 扭矩断点 [25, 50, 75, 100, 150, 200, 250]（默认） | 1×M 向量
  group: ''
  block_parameter: Trq_bpts
  values: '[25, 50, 75, 100, 150, 200, 250]（默认） | 1×M 向量'
- name: Efficiency speed breakpoints, omega_bpts
  summary: 转速断点 [52.4 78.5 105 131 157 183 209 262 314 419 524]（默认） | 1×N 向量
  group: ''
  block_parameter: omega_bpts
  values: '[52.4 78.5 105 131 157 183 209 262 314 419 524]（默认） | 1×N 向量'
- name: Efficiency temperature breakpoints, Temp_bpts
  summary: 温度断点 [290 358]（默认）| 1×L 向量
  group: ''
  block_parameter: Temp_bpts
  values: '[290 358]（默认）| 1×L 向量'
- name: Ambient temperature, Tamb
  summary: 环境温度 297.15（默认）| scalar
  group: ''
  block_parameter: Tamb
  values: 297.15（默认）| scalar
- name: Coupling type
  summary: 扭矩耦合 Pre-loaded ideal clutch（默认）| Slip speed dependent torque data | Input torque dependent torque data
  group: ''
  block_parameter: couplingType
  values: Pre-loaded ideal clutch（默认）| Slip speed dependent torque data | Input torque dependent torque data
- name: Number of disks, Ndisks
  summary: 扭矩耦合 4（默认）| scalar
  group: ''
  block_parameter: Ndisks
  values: 4（默认）| scalar
- name: Effective radius, Reff
  summary: 半径 .20（默认）| scalar
  group: ''
  block_parameter: Reff
  values: .20（默认）| scalar
- name: Nominal preload force, Fc
  summary: 力 500（默认）| scalar
  group: ''
  block_parameter: Fc
  values: 500（默认）| scalar
- name: Friction coefficient vector, muc
  summary: 摩擦 [.16 0.13 0.115 0.11 0.105 0.1025 0.10125]（默认）| vector
  group: ''
  block_parameter: muc
  values: '[.16 0.13 0.115 0.11 0.105 0.1025 0.10125]（默认） | vector'
- name: Slip speed vector, dw
  summary: 角速度 [0 10 20 40 60 80 100]（默认） | vector
  group: ''
  block_parameter: dw
  values: '[0 10 20 40 60 80 100]（默认） | vector'
- name: Torque - slip speed vector, Tdw
  summary: 转矩 [-100, -90, -50, -5, 0, 5, 50, 90, 100]（默认） | vector
  group: ''
  block_parameter: Tdw
  values: '[-100, -90, -50, -5, 0, 5, 50, 90, 100]（默认） | vector'
- name: Slip speed vector, dwT
  summary: 角速度 [-200, -175, -100, - 50, 0, 50, 100, 175, 200]（默认） | vector
  group: ''
  block_parameter: dwT
  values: '[-200, -175, -100, - 50, 0, 50, 100, 175, 200]（默认） | vector'
- name: Torque - input torque vector, TTin
  summary: 转矩 [-200 -175 -100 - 50 0 50 100 175 200]（默认） | vector
  group: ''
  block_parameter: TTin
  values: '[-200 -175 -100 - 50 0 50 100 175 200]（默认） | vector'
- name: Input torque vector, Tin
  summary: 转矩 [-200 -175 -100 - 50 0 50 100 175 200]（默认） | vector
  group: ''
  block_parameter: Tin
  values: '[-200 -175 -100 - 50 0 50 100 175 200]（默认） | vector'
- name: Coupling time constant, tauC
  summary: 常量 .01（默认） | scalar
  group: ''
  block_parameter: tauC
  values: .01（默认） | scalar
```

#### 模块选项

### **Efficiency factors** — 指定配置 `Constant`（默认） | `Driveshaft torque, speed and temperature`

要计入模块效率，请使用 **Efficiency factors** 参数。此表总结了每种设置的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率作为基础齿轮输入扭矩、空气温度和驱动轴转速的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以  创建输入端口。 - 设置 **Ambient temperature, Tamb**  参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅插值方法。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DiffEffModelPopup` |
| **值：** | `Constant`（默认） | `Driveshaft torque, speed and temperature` |
| **数据类型：** | `character vector` |

### **Interpolation method** — 方法 `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

有关详细信息，请参阅插值方法。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InterpMethod` |
| **值：** | `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Input ambient temperature** — 创建输入端口 `off`（默认）| `on`

选择此项可为温度创建输入端口 `Temp`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `extTamb` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

#### Open Differential

### **Crown wheel (ring gear) located** — 指定冠轮连接 `To the left of center-line`（默认）| `To the right of center-line`

指定冠轮与驱动轴的连接。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `shaftSwitchMask` |
| **值：** | `To the left of center-line`（默认）| `To the right of center-line` |
| **数据类型：** | `character vector` |

### **Carrier to drive shaft ratio, NC/ND** — 传动比 `4`（默认）| `scalar`

行星架与驱动轴的齿轮传动比，*N*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndiff` |
| **值：** | `4`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Carrier inertia, Jd** — 惯量 `.1`（默认）| `scalar`

冠齿轮组件的转动惯量，*Jd*，单位为 kg·m^2。你可以包含驱动轴惯量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jd` |
| **值：** | `.1`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Carrier damping, bd** — 阻尼 `1e-3`（默认）| `scalar`

冠齿轮线性粘性阻尼，*bd*，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bd` |
| **值：** | `1e-3`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Axle 1 inertia, Jw1** — 惯量 `.1`（默认）| `scalar`

车轴 1 的转动惯量，*J1*，单位为 kg·m^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw1` |
| **值：** | `.1`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Axle 1 damping, bw1** — 阻尼 `1e-3`（默认）| `scalar`

车轴 1 的线性粘性阻尼，*b1*，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw1` |
| **值：** | `1e-3`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Axle 2 inertia, Jw2** — 惯量 `.1`（默认）| `scalar`

车轴 2 的转动惯量，*J2*，单位为 kg·m^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw2` |
| **值：** | `.1`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Axle 2 damping, bw2** — 阻尼 `1e-3`（默认）| `scalar`

车轴 2 的线性粘性阻尼，*b2*，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw2` |
| **值：** | `1e-3`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 initial velocity, omegaw1o** — 角速度 `0`（默认） | `scalar`

轴 1 初始速度，*ωo1*，单位为
rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw1o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 initial velocity, omegaw2o** — 角速度 `0`（默认） | `scalar`

轴 2 初始速度，*ωo2*，单位为
rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw2o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Constant efficiency factor, eta** — 效率 `1`（默认） | 正标量

恒定效率，*η*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta` |
| **值：** | `1`（默认） | 正标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors**
设置为 `Constant`。

### **Efficiency lookup table, eta\_tbl** — 查找表 `M`×`N`×`L` 数组

效率值的无量纲数组，作为以下量的函数：

- `M` 个输入扭矩
- `N` 个输入转速
- `L` 个空气温度

每个值指定了特定扭矩、
转速和温度组合下的效率。数组大小必须与扭矩、
转速和温度断点向量定义的维度匹配。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_tbl` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为
`Driveshaft torque, speed and temperature`。

### **Efficiency torque breakpoints, Trq\_bpts** — 扭矩断点 `[25, 50, 75, 100, 150, 200, 250]`（默认） | `1`×`M` 向量

输入扭矩向量，效率的断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_bpts` |
| **值：** | `[25, 50, 75, 100, 150, 200, 250]`（默认） | `1`×`M` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为
`Driveshaft torque, speed and temperature`。

### **Efficiency speed breakpoints, omega\_bpts** — 转速断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认） | `1`×`N` 向量

转速向量，效率的断点，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_bpts` |
| **值：** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认） | `1`×`N` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为
`Driveshaft torque, speed and temperature`。

### **Efficiency temperature breakpoints, Temp\_bpts** — 温度断点 `[290 358]`（默认）| `1`×`L` 向量

效率的环境温度断点向量，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_bpts` |
| **值：** | `[290 358]`（默认）| `1`×`L` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Ambient temperature, Tamb** — 环境温度 `297.15`（默认）| `scalar`

环境空气温度，*Tair*，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tamb` |
| **值：** | `297.15`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数：

- 将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。
- 清除 **Input ambient temperature**。

#### Slip Coupling

### **Coupling type** — 扭矩耦合 `Pre-loaded ideal clutch`（默认）| `Slip speed dependent torque data` | `Input torque dependent torque data`

指定扭矩耦合的类型。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `couplingType` |
| **值：** | `Pre-loaded ideal clutch`（默认）| `Slip speed dependent torque data` | `Input torque dependent torque data` |
| **数据类型：** | `character vector` |

### **Number of disks, Ndisks** — 扭矩耦合 `4`（默认）| `scalar`

磁盘数量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndisks` |
| **值：** | `4`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用理想离合器参数，请为 **Coupling type** 参数选择 `Pre-loaded ideal clutch`。

### **Effective radius, Reff** — 半径 `.20`（默认）| `scalar`

有效半径 Reff，与施加的离合器摩擦力一起用于确定摩擦力。有效半径定义为：

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

该方程使用以下变量。

|  |  |
| --- | --- |
| Ro | 环形磁盘外半径 |
| Ri | 环形磁盘内半径 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Reff` |
| **值：** | `.20`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Pre-loaded ideal clutch`。

### **Nominal preload force, Fc** — 力 `500`（默认）| `scalar`

标称预紧力，单位为 N。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fc` |
| **值：** | `500`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Pre-loaded ideal clutch`。

### **Friction coefficient vector, muc** — 摩擦 `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125]`（默认）| `vector`

摩擦系数向量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `muc` |
| **值：** | `[.16 0.13 0.115 0.11 0.105 0.1025 0.10125]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Pre-loaded ideal clutch`。

### **Slip speed vector, dw** — 角速度 `[0 10 20 40 60 80 100]`（默认） | `vector`

滑差速度向量，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dw` |
| **值：** | `[0 10 20 40 60 80 100]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用离合器参数，请为 **Coupling type** 参数选择 `Pre-loaded ideal clutch`。

### **Torque - slip speed vector, Tdw** — 转矩 `[-100, -90, -50, -5, 0, 5, 50, 90, 100]`（默认） | `vector`

转矩向量，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tdw` |
| **值：** | `[-100, -90, -50, -5, 0, 5, 50, 90, 100]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用滑差速度参数，请为 **Coupling type** 参数选择 `Slip speed dependent torque data`。

### **Slip speed vector, dwT** — 角速度 `[-200, -175, -100, - 50, 0, 50, 100, 175, 200]`（默认） | `vector`

滑差速度向量，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dwT` |
| **值：** | `[-200, -175, -100, - 50, 0, 50, 100, 175, 200]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用滑差速度参数，请为 **Coupling type** 参数选择 `Slip speed dependent torque data`。

### **Torque - input torque vector, TTin** — 转矩 `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector`

转矩向量，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TTin` |
| **值：** | `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用输入转矩参数，请为 **Coupling type** 参数选择 `Input torque dependent torque data`。

### **Input torque vector, Tin** — 转矩 `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector`

转矩向量，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tin` |
| **值：** | `[-200 -175 -100 - 50 0 50 100 175 200]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用输入转矩参数，请为 **Coupling type** 参数选择 `Input torque dependent torque data`。

### **Coupling time constant, tauC** — 常量 `.01`（默认） | `scalar`

耦合时间常数，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tauC` |
| **值：** | `.01`（默认） | `scalar` |
| **数据类型：** | `double` |
## 所属库

Powertrain Blockset / Drivetrain / Final Drive Unit Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

作为行星锥齿轮的限滑差速器

Limited Slip Differential 模块将差速器实现为行星锥齿轮系。该模块将传动轴锥齿轮与从动（齿圈）锥齿轮匹配。您可以指定：

- 行星架与传动轴之比
- 从动轮位置
- 车轴和行星架的黏性系数和阻尼系数
- 滑移联轴器类型

在系统级传动系分析中使用该模块，以考虑从变速器到车轮的功率传递。该模块适用于硬件在环（HIL）和优化工作流。所有参数均可调。

在限滑差速器中，为防止其中一个车轮打滑，差速器分配施加到左、右车轴的扭矩。由于施加到车轴的扭矩不同，车轮可以以不同的角速度运动，从而防止打滑。该模块实现了三种联轴器方法，用于耦合施加到各轴的不同的扭矩：

- 预载理想离合器
- 滑移速度相关扭矩数据
- 输入扭矩相关扭矩数据

该模块使用的坐标系可为标准发动机、变速器和差速器配置产生正的轮胎和车辆运动。箭头表示正运动。

变速器图

### 效率

要考虑模块效率，请使用 **Efficiency factors** 参数。下表总结了每个设置的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率作为基础齿轮输入扭矩、空气温度和传动轴速度的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以  创建输入端口。 - 设置 **Ambient temperature, Tamb**  参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅 Interpolation Methods。 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 来自传动轴的机械功率 | ηTdωd |
| `PwrAxl1` | 来自车轴 1 的机械功率 | ηT1ω1 |
| `PwrAxl2` | 来自车轴 2 的机械功率 | ηT2ω2 |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrMechLoss` | 总功率损失 | W˙loss= −(Pt+Pd+Pc)+PsPt=η(Tdωd+T1ω1+T2ω2) |
| `PwrDampLoss` | 阻尼导致的功率损失 | Pd=−(b1|ω1|+b2|ω2|+bd|ωd|) |
| `PwrCplngLoss` | 离合器导致的功率损失 | Pc=Tc|ω¯| |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 存储的内部能量的变化率 | Ps=−(ω1ω˙1J1+ω2ω˙2J2+ωdω˙dJd) |

### 动力学

限滑差速器模块实现这些微分方程，以表示冠齿轮、左半轴和右半轴的机械动态响应。

| 机械动态响应 | 微分方程 |
| --- | --- |
| 冠齿轮 | ω˙dJd=ηTd-ωdbd-Ti |
| 左半轴 | ω˙1J1=ηT1-ω1b1-Ti1 |
| 右半轴 | ω˙2J2=ηT2-ω2b2-Ti2 |

该模块假设冠齿轮与半轴之间为刚性耦合。这些约束方程适用。

ηT1=N2Ti−12TcηT2=N2Ti+12Tc

ωd=N2(ω1+ω2)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *N* | 行星架到驱动轴齿轮比 |
| *Jd* | 冠齿轮组件的转动惯量 |
| *bd* | 冠齿轮线性粘性阻尼 |
| *ωd* | 驱动轴角速度 |
| ϖ | 滑移速度 |
| *J1* | 半轴 1 转动惯量 |
| *b1* | 半轴 1 线性粘性阻尼 |
| *ω1* | 半轴 1 速度 |
| *J2* | 半轴 2 转动惯量 |
| *b2* | 半轴 2 线性粘性阻尼 |
| *ω2* | 半轴 2 角速度 |
| *η* | 效率 |
| *Td* | 驱动轴扭矩 |
| *T1* | 半轴 1 扭矩 |
| *T2* | 半轴 2 扭矩 |
| *Ti* | 半轴内阻扭矩 |
| *Ti1* | 半轴 1 内阻扭矩 |
| *Ti2* | 半轴 2 内阻扭矩 |
| *μ* | 摩擦系数 |
| Reff | 有效离合器半径 |
| Ro | 环形盘外半径 |
| *Ri* | 环形盘内半径 |
| *Fc* | 离合器力 |
| *Tc* | 离合器扭矩 |
| *μ* | 摩擦系数 |

限滑差速器中的 Table 模块具有以下参数设置：

- **插值方法** —
  `Linear`
- **外推方法** —
  `Clip`

**理想离合器耦合**

理想离合器耦合模型使用半轴滑移速度和摩擦来计算离合器扭矩。摩擦系数是滑移速度的函数。

Tc=FcNμ(|ϖ|)Refftanh(4|ϖ|)

圆盘半径决定离合器力作用的有效离合器半径。

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

半轴的角速度决定滑移速度。

ϖ=ω1−ω2

**滑移速度耦合**

为计算离合器扭矩，滑移速度耦合模型使用作为滑移速度函数的扭矩数据。半轴的角速度决定滑移速度。

ϖ=ω1−ω2

**输入扭矩耦合**

为计算离合器扭矩，输入扭矩耦合模型使用作为输入扭矩函数的扭矩数据。

Open Differential 模块假设冠齿轮与半轴之间为刚性耦合。这些约束方程适用。

ηTi1= ηTi2=N2Ti

ωd=N2(ω1+ω2)
