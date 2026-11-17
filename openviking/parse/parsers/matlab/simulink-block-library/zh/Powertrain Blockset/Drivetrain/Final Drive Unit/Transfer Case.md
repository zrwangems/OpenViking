---
type: simulink-block
title: 'Transfer Case'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Final Drive Unit'
documentation_page: 'transfercase'
documentation_source_path: 'ref/transfercase.html'
language: zh-CN
chinese_source: worker-translation
---

# Transfer Case

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
- name: TrqSplitRatioConstant
  summary: 前轴扭矩分配比 scalar
  direction: input
- name: SpdLockConstant
  summary: 车轴速度锁定 scalar
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

### **TrqSplitRatioConstant** — 前轴扭矩分配比 `scalar`

前轴扭矩分配比。

#### 依赖关系

要启用此端口，请选择 **Input front axle torque split ratio,
TrqSplitRatio**。

### **SpdLockConstant** — 车轴速度锁定 `scalar`

车轴速度锁定。

#### 依赖关系

要启用此端口，请选择 **Input axle speed lock,
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
- name: Input front axle torque split ratio, TrqSplitRatio
  summary: 创建输入端口 off（默认）| on
  group: ''
  block_parameter: TrqSplitRatio
  values: off（默认）| on
- name: Input axle speed lock, SpdLock
  summary: 创建输入端口 off（默认）| on
  group: ''
  block_parameter: SpdLock
  values: off（默认）| on
- name: Crown wheel (ring gear) located
  summary: 指定冠齿轮连接位置 To the left of center-line（默认）| To the right of center-line
  group: ''
  block_parameter: shaftSwitchMask
  values: To the left of center-line（默认）| To the right of center-line
- name: Carrier to drive shaft ratio, Ndiff
  summary: 比值 4（默认）| scalar
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
  values: .1（默认） | scalar
- name: Axle 1 damping, bw1
  summary: 阻尼 1e-3（默认） | scalar
  group: ''
  block_parameter: bw1
  values: 1e-3（默认） | scalar
- name: Axle 2 inertia, Jw2
  summary: 惯量 .1（默认） | scalar
  group: ''
  block_parameter: Jw2
  values: .1（默认） | scalar
- name: Axle 2 damping, bw2
  summary: 阻尼 1e-3（默认） | scalar
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
  summary: 转矩断点 [25, 50, 75, 100, 150, 200, 250]（默认）| 1×M 向量
  group: ''
  block_parameter: Trq_bpts
  values: '[25, 50, 75, 100, 150, 200, 250]（默认）| 1×M 向量'
- name: Efficiency speed breakpoints, omega_bpts
  summary: 转速断点 [52.4 78.5 105 131 157 183 209 262 314 419 524]（默认）| 1×N 向量
  group: ''
  block_parameter: omega_bpts
  values: '[52.4 78.5 105 131 157 183 209 262 314 419 524]（默认）| 1×N 向量'
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
- name: Front axle torque split ratio, TrqSplitRatio
  summary: 前轴转矩分配比 0.5（默认）| scalar
  group: ''
  block_parameter: TrqSplitRatio
  values: 0.5（默认）| scalar
- name: Axle speed lock, SpdLock
  summary: 车轴转速锁定 0（默认）| scalar
  group: ''
  block_parameter: SpdLock
  values: 0（默认）| scalar
```

#### 模块选项

### **Efficiency factors** — 指定配置 `Constant`（默认） | `Driveshaft torque, speed and temperature`

要计入模块效率，请使用 **Efficiency factors** 参数。此表总结了每种设置的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率作为基础齿轮输入扭矩、空气温度和传动轴速度的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以  创建输入端口。 - 设置 **Ambient temperature, Tamb**  参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅插值方法。 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DiffEffModelPopup` |
| **值：** | `Constant`（默认） | `Driveshaft torque, speed and temperature` |
| **数据类型：** | `character vector` |

### **Interpolation method** — 方法 `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

有关详细信息，请参阅插值方法。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InterpMethod` |
| **值：** | `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为
`Driveshaft torque, speed and temperature`。

### **Input ambient temperature** — 创建输入端口 `off`（默认）| `on`

选择以创建温度输入端口 `Temp`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `extTamb` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为
`Driveshaft torque, speed and temperature`。

### **Input front axle torque split ratio, TrqSplitRatio** — 创建输入端口 `off`（默认）| `on`

选择以创建前轴扭矩分配比输入端口 `TrqSplitRatioConstant`。

#### 编程方式使用

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqSplitRatio` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

### **Input axle speed lock, SpdLock** — 创建输入端口 `off`（默认）| `on`

选择以创建车轴速度锁输入端口 `SpdLockConstant`。

#### 编程方式使用

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SpdLock` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

### **Crown wheel (ring gear) located** — 指定冠齿轮连接位置 `To the left of center-line`（默认）| `To the right of center-line`

指定冠齿轮与传动轴的连接位置。

#### 编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `shaftSwitchMask` |
| **值：** | `To the left of center-line`（默认）| `To the right of center-line` |
| **数据类型：** | `character vector` |

### **Carrier to drive shaft ratio, Ndiff** — 比值 `4`（默认）| `scalar`

行星架与传动轴的齿轮比，*N*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndiff` |
| **值：** | `4`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Carrier inertia, Jd** — 惯量 `.1`（默认）| `scalar`

冠齿轮组件的转动惯量，
*Jd*，单位为 kg·m^2。您可以包含
传动轴惯量。

#### 编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jd` |
| **值：** | `.1`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Carrier damping, bd** — 阻尼 `1e-3`（默认）| `scalar`

冠齿轮线性粘性阻尼，*bd*，单位为
N·m·s/rad。

#### 编程方式使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bd` |
| **值：** | `1e-3`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Axle 1 inertia, Jw1** — 惯量 `.1`（默认）| `scalar`

车轴 1 转动惯量，*J1*，单位为
kg·m^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw1` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 damping, bw1** — 阻尼 `1e-3`（默认） | `scalar`

轴 1 线性粘性阻尼，*b1*，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw1` |
| **值：** | `1e-3`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 inertia, Jw2** — 惯量 `.1`（默认） | `scalar`

轴 2 转动惯量，*J2*，单位为 kg·m^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jw2` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 damping, bw2** — 阻尼 `1e-3`（默认） | `scalar`

轴 2 线性粘性阻尼，*b2*，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bw2` |
| **值：** | `1e-3`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 1 initial velocity, omegaw1o** — 角速度 `0`（默认） | `scalar`

轴 1 初始速度，*ωo1*，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw1o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Axle 2 initial velocity, omegaw2o** — 角速度 `0`（默认） | `scalar`

轴 2 初始速度，*ωo2*，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegaw2o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 效率

### **Constant efficiency factor, eta** — 效率 `1`（默认） | 正标量

恒定效率，*η*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta` |
| **值：** | `1`（默认） | 正标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Constant`。

### **Efficiency lookup table, eta\_tbl** — 查找表 `M`×`N`×`L` 数组

效率的无量纲数值数组，作为以下量的函数：

- `M` 个输入扭矩
- `N` 个输入转速
- `L` 个空气温度

每个值指定了特定扭矩、转速和温度组合下的效率。数组大小必须与扭矩、转速和温度断点向量定义的维度匹配。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_tbl` |
| **值：** | `M`×`N`×`L` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency torque breakpoints, Trq\_bpts** — 转矩断点 `[25, 50, 75, 100, 150, 200, 250]`（默认）| `1`×`M` 向量

输入转矩向量，效率断点，单位为 N·m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Trq_bpts` |
| **值**：| `[25, 50, 75, 100, 150, 200, 250]`（默认）| `1`×`M` 向量 |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency speed breakpoints, omega\_bpts** — 转速断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认）| `1`×`N` 向量

转速向量，效率断点，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `omega_bpts` |
| **值**：| `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认）| `1`×`N` 向量 |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency temperature breakpoints, Temp\_bpts** — 温度断点 `[290 358]`（默认）| `1`×`L` 向量

环境温度断点向量，用于效率计算，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Temp_bpts` |
| **值**：| `[290 358]`（默认）| `1`×`L` 向量 |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Ambient temperature, Tamb** — 环境温度 `297.15`（默认）| `scalar`

环境空气温度，*Tair*，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Tamb` |
| **值**：| `297.15`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数：

- 将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。
- 清除 **Input ambient temperature**。

### **Front axle torque split ratio, TrqSplitRatio** — 前轴转矩分配比 `0.5`（默认）| `scalar`

前轴转矩分配比。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TrqSplitRatio` |
| **值**：| `0.5`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input front axle torque split ratio, TrqSplitRatio**。

### **Axle speed lock, SpdLock** — 车轴转速锁定 `0`（默认）| `scalar`

车轴转速锁定。将此值设置为 0，以使前轴和后轴转速不固定。将此值设置为 1，以使前轴和后轴转速固定。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SpdLock` |
| **值**：| `0`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请清除 **Input axle speed lock, SpdLock**。
## 所属库

Powertrain Blockset / Drivetrain / Final Drive Unit Vehicle Dynamics Blockset / Powertrain / Drivetrain / Final Drive Unit

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

作为行星锥齿轮的差速器

Transfer Case 模块将差速器实现为行星锥齿轮传动系。该模块将传动轴锥齿轮与冠（环）锥齿轮匹配。您可以指定：

- 行星架与传动轴比
- 冠轮位置
- 车轴和行星架的粘性和阻尼系数

使用 Transfer Case 模块来：

- 将变速器后的传动轴动态耦合到车轮车轴或万向节
- 在最优牵引力控制不需要被动或主动扭矩矢量分配时，对简化或较旧的传动系统进行建模
- 在通用变速箱和传动系场景中对机械功率分流进行建模

该模块适用于硬件在环（HIL）和优化工作流。所有参数均可调。

### 效率

要考虑模块效率，请使用 **Efficiency factors** 参数。下表总结了每个设置的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 作为基础齿轮输入扭矩、空气温度和传动轴速度的函数的效率。使用以下参数指定查找表和断点： - **Efficiency lookup table, eta\_tbl** - **Efficiency torque breakpoints, Trq\_bpts** - **Efficiency speed breakpoints, omega\_bpts** - **Efficiency temperature breakpoints, Temp\_bpts**    对于空气温度，您可以： - 选择 **Input ambient temperature** 以创建输入端口。 - 设置 **Ambient temperature, Tamb** 参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅插值方法。 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率 - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 来自传动轴的机械功率 | ηTdωd |
| `PwrAxl1` | 来自车轴 1 的机械功率 | ηT1ω1 |
| `PwrAxl2` | 来自车轴 2 的机械功率 | ηT2ω2 |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率 - 正信号表示输入 - 负信号表示损失 | `PwrMechLoss` | 总功率损失 | W˙loss= −(Pt+Pd)+PsPt=ηTdωd+ηT1ω1+ηT2ω2 |
| `PwrDampLoss` | 由于阻尼导致的功率损失 | Pd=−(b1|ω1|+b2|ω2|+bd|ωd|) |
| `PwrStored` — 存储能量的变化率 - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 存储内能的变化率 | Ps=−(ω1ω˙1J1+ω2ω˙2J2+ωdω˙dJd) |

### 动力学

Transfer Case 模块实现以下微分方程，以表示冠齿轮、前轴和后轴的机械动态响应。

| 机械动态响应 | 微分方程 |
| --- | --- |
| 冠齿轮 | ω˙dJd=ηTd-ωdbd-Ti |
| 前轴 | ω˙1J1=ηT1-ω1b1-Ti1 |
| 后轴 | ω˙2J2=ηT2-ω2b2-Ti2 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *N* | 行星架与传动轴的齿轮比 |
| *Jd* | 冠齿轮组件的转动惯量 |
| *bd* | 冠齿轮线性粘性阻尼 |
| *ωd* | 传动轴角速度 |
| *η* | 差速器效率 |
| *J1* | 轴 1 转动惯量 |
| *b1* | 轴 1 线性粘性阻尼 |
| *ω1* | 轴 1 转速 |
| *J2* | 轴 2 转动惯量 |
| *b2* | 轴 2 线性粘性阻尼 |
| *ω2* | 轴 2 角速度 |
| *Td* | 传动轴扭矩 |
| *T1* | 轴 1 扭矩 |
| *T2* | 轴 2 扭矩 |
| *Ti* | 传动轴内阻扭矩 |
| *Ti1* | 轴 1 内阻扭矩 |
| *Ti2* | 轴 2 内阻扭矩 |
