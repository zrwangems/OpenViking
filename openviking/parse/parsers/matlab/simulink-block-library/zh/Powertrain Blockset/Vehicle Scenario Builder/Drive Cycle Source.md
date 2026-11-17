---
type: simulink-block
title: 'Drive Cycle Source'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenario Builder'
documentation_page: 'drivecyclesource'
documentation_source_path: 'ref/drivecyclesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Drive Cycle Source

## 端口

### 输入

### **VelFdbk** — 车辆纵向速度 `scalar`

车辆纵向速度。

#### 依赖

要启用此端口，请在**故障跟踪**选项卡上，选择**启用故障跟踪**。将**速度反馈单位，inUnit**参数设置为 `VelFdbk` 输入端口信号单位。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | 描述 |
| --- | --- | --- |
| `Reference Speed` | | 车辆参考速度 |
| `Reference Accel` | | 车辆参考加速度 |
| `Gear` | | 车辆挡位 |
| `Fault` | `UpprBnd` | 允许车速范围的上限。 |
| `LowerBnd` | 允许车速范围的下限。 |
| `Fault` | 指示故障条件的布尔值：  - 1 — 故障 - 0 — 无故障    如果车速不在允许速度范围内，模块将设置故障条件。 |
| `FaultCnt` | 故障数量。 |
| `CumFaultTime` | 处于故障条件的累计时间。 |
| `SnglFaultTime` | 单次故障的持续时间。 |
| `Fail` | 指示故障失效的布尔值：  - 1 — 失效 - 0 — 无失效    如果故障条件超过最大故障数量、最大单次故障时间或最大总故障时间，模块将设置故障失效。 |

#### 依赖

要启用此端口，请在**故障跟踪**选项卡上，选择**启用故障跟踪**。

### **RefSpd** — 车辆参考速度 `scalar`

车辆参考速度，以您指定的单位表示。要指定单位，请使用**输出速度单位**参数。

### **RefAcc** — 车辆参考加速度 `scalar`

要计算加速度，模块使用二阶多项式和三点采样滤波器实现 Savitzky-Golay 微分。

#### 依赖

要创建输出加速度端口，请选择**输出加速度**。选择**输出加速度**将启用**输出加速度单位**参数。

### **Gear** — 车辆挡位 `scalar`

#### 依赖

要启用此端口：

1. 首先指定包含换挡计划的行驶循环。您可以使用：

   - 支持包来安装包含换挡计划的标准行驶循环，例如 `JC08` 和 `CUEDC`。
   - 工作区变量。
   - .`mat`、.`xls`、.`xlsx` 或 .`txt` 文件。
2. 选择**输出换挡数据**。

## 参数

### 循环设置

#### 设置

### **Drive cycle source** — 选择行驶循环源 `FTP75`（默认）| `Wide Open Throttle (WOT)` | `Workspace variable` | `.mat, .xls, .xlsx or .txt file`

- `FTP75` — 将 FTP75 行驶循环从 .`mat` 文件加载到一维查找表中。FTP75 代表城市行驶循环，可用于确定乘用车的尾气排放和燃油经济性。

  要从支持包安装其他行驶循环，请参阅安装行驶循环数据。
- `Wide Open Throttle (WOT)` — 使用 WOT 参数指定用于性能测试的行驶循环。
- `Workspace variable` — 将时间、速度和（可选）挡位数据指定为结构体、二维数组或时间序列对象。
- `.mat, .xls, .xlsx or .txt file` — 指定包含列格式的时间、速度和（可选）挡位数据的文件。

安装其他循环后，您可以使用 `set_param` 设置行驶循环。例如，要使用行驶循环 `US06`：

```
set_param([gcs '/Drive Cycle Source'],'cycleVar','US06')
```

#### 依赖关系

下表汇总了参数依赖关系。

| Drive Cycle Source | 启用的参数 |
| --- | --- |
| `Wide Open Throttle (WOT)` | **Start time, t\_wot1** |
| **Initial reference speed, xdot\_woto** |
| **Nominal reference speed, xdot\_wot1** |
| **Time to start deceleration, t\_wot2** |
| **Final reference speed, xdot\_wot2** |
| **WOT simulation time, t\_wotend** |
| **Source velocity units** |
| `Workspace variable` | **From workspace** |
| **Source velocity units** |
| **Output gear shift data**，如果驾驶循环包含换挡计划 |
| `.mat, .xls, .xlsx or .txt file` | **Drive cycle source file** |
| **Source velocity units** |
| **Output gear shift data**，如果驾驶循环包含换挡计划 |

### **From workspace** — 工作区 `variable`

包含单调递增时间向量、速度向量以及可选挡位数据向量的工作区变量。您可以使用结构体、二维数组或时间序列对象。在 **Source velocity units** 参数字段中输入速度的单位。

每个对应的时间值必须存在有效的数据点。不能指定 `inf`、`empty` 或 `NaN`。

下表提供了使用工作区变量创建自定义驾驶循环的示例。

| 工作区变量 | 源速度单位 | 输出速度单位 | 驾驶循环图 |
| --- | --- | --- | --- |
| 不含换挡计划的结构体，**From workspace** 设置为 `myCycleS`。  ``` t = 0:1:100; xdot = 5.*sin(t)+10; myCycleS.time = t'; myCycleS.signals.values = xdot'; ``` | `m/s` | `mph` | 显示正弦波的速度-时间图 |
| 含换挡计划的结构体，**From workspace** 设置为 `myCycleS`。  ``` gears=[0, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4]; t=0:1:10; xdot=[0,5,10,15,20,25,30,30,30,30,30]; myCycleS.time=t'; myCycleS.signals.values=[xdot',gears']; ``` | `m/s` | `mph` | 显示速度从 0 秒时的 0 mph 线性增加到 6 秒时的 70 mph 的速度-时间图。6 秒后，速度保持恒定在 70 mph。 |
| 不含换挡计划的二维数组，**From workspace** 设置为 `myCycleA`。  ``` t = 0:1:100; xdot = 5.*sin(t)+5; myCycleA = [t',xdot']; ``` | `m/s` | `mph` | 显示正弦波的速度-时间图 |
| 含换挡计划的二维数组，**From workspace** 设置为 `myCycleA`。  ``` gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,5,10,15,20,25,30,40,50,60,60]; myCycleA=[t',xdot',gears']; ``` | `mph` | `mph` | 显示速度从 0 秒时的 0 mph 线性增加到 6 秒时的 30 mph，再到 9 秒时的 60 mph 的速度-时间图。9 秒后，速度保持恒定在 60 mph。 |
| 不含换挡计划的时间序列对象，**From workspace** 设置为 `myCycleT`。  ``` myCycleT = timeseries; t = 0:1:100; xdot = 5.*sin(t)+20; myCycleT.Data = xdot'; myCycleT.Time = t'; ``` | `m/s` | `mph` | 显示正弦波的速度-时间图 |
| 不含换挡计划的时间序列对象，**From workspace** 设置为 `myCycleT`。  ``` myCycleT = timeseries; gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,10,20,30,32,33,34,40,50,60,60]; myCycleT.Data = [xdot',gears']; myCycleT.Time = t'; ``` | `mph` | `mph` | 显示以 mph 为单位线性增加的速度-时间图。9 秒后，速度保持恒定在 60 mph。 |

#### 依赖关系

要启用此参数，请从 **Drive cycle source** 中选择 `Workspace variable`。

### **Drive cycle source file** — 文件名 `.mat、.xls、.xlsx 或 .txt`

包含单调递增的时间数据、速度数据，以及可选的挡位数据（列格式或逗号分隔格式）的文件。该模块忽略文件中的单位。请在 **Source velocity units** 参数字段中输入源速度的单位。

| 文件 | 源速度单位 | 输出速度单位 | 行驶循环图 |
| --- | --- | --- | --- |
| 一个 `.mat` 文件，包含一个与文件名同名的矩阵。该矩阵第 1 列为时间，第 2 列为速度。它还可以可选地在第 3 列包含挡位选择。 ``` sampcyc =           0         0     0.5000    0.7000     1.0000    2.0000      1.5000    3.6000     2.0000    5.6000     2.5000    7.9000      3.0000   10.3000     3.5000   13.0000      4.0000   16.0000     4.5000   19.0000     5.0000   22.3000     5.5000   25.7000     6.0000   29.3000 ``` | `m/s` | `m/s` | 速度对时间图 |
| 一个 `.xls` 或 `.xlsx` 文件，A 列为时间，B 列为速度。 11 行，A 列为时间，B 列为速度 | `mph` | `mph` | 速度对时间图 |
| 一个 `.xls` 或 `.xlsx` 文件，A 列为时间，B 列为速度，C 列为挡位。该模块： - 忽略文件中的表头和单位。 - 将挡位信息转换为整数： - N 转换为 0 - D 转换为 2 12 行，A 列为时间（单位：秒），B 列为速度（单位：mph），C 列为挡位 | `mph` | `mph` | 速度对时间图 |
| 一个 `.txt` 文件，第 1 列为时间，第 2 列为速度。该模块忽略表头和单位信息。 20 行，A 列为时间（单位：秒），B 列为速度（单位：mph） | `mph` | `mph` | 速度对时间图 |

您可以从外部来源导入标准行驶循环文件。例如，您可以按照 WTMC 上的说明导入全球统一摩托车排放认证和测试程序（WMTC）循环。具体来说：

1. 下载换挡表和说明。
2. 按照说明根据您的输入计算换挡数据。
3. 速度单位为 `km/hr`。使用换算系数 1000/3600 将速度转换为 `m/s`。
4. 将数据复制并保存到新的 `.xls` 或 `.xlsx` 文件中，以用作源文件。

如果您使用 **P**、**R**、**N**、**D**、**L**、**OD** 提供挡位计划，该模块会将挡位映射为整数。

| 挡位 | 整数 |
| --- | --- |
| P | `80` |
| R | `-1` |
| N | `0` |
| L | `1` |
| D | `2` |
| OD | 最高指定挡位之后的下一个整数。 |

例如，该模块将挡位计划 `P P N L D 3 4 5 6 5 4 5 6 7 OD 7` 转换为 `80 80 0 1 2 3 4 5 6 5 4 5 6 7 8 7`。

#### 依赖关系

要启用此参数，请从 **Drive cycle source** 中选择 `.mat、.xls、.xlsx 或 .txt file`。

### **Repeat cyclically** — 循环重复行驶循环 `off`（默认） | `on`

如果仿真运行时间超过行驶循环的长度，则重复该行驶循环。

### **Output acceleration** — 输出加速度 `off`（默认）

为了计算加速度，该模块使用二阶多项式和三点采样滤波器实现 Savitzky-Golay 微分。

#### 依赖关系

要创建输出加速度端口，请选择 **Output acceleration**。选择 **Output acceleration** 会启用 **Output acceleration units** 参数。

### **Output gear shift data** — 输出挡位 `off`（默认） | `on`

#### 依赖关系

- 首先指定一个包含换挡计划的行驶循环。您可以使用：

  - 一个支持包来安装包含换挡计划的标准行驶循环，例如 `JC08` 和 `CUEDC`。
  - 工作区变量。
  - `.mat`、`.xls`、`.xlsx` 或 `.txt` 文件。
- 单击此参数会创建输入端口 **Gear**。

#### WOT 参数

### **Start time, t\_wot1** — 驾驶循环开始时间 `5`（默认）| `scalar`

驾驶循环开始时间，单位为 s。例如，此图显示了一个开始时间为 `10` s 的驾驶循环。

速度与时间关系图

#### 依赖

要启用此参数，请选择 **Drive cycle source** 参数 `Wide Open Throttle (WOT)`。

### **Initial reference speed, xdot\_woto** — 速度 `0`（默认）| `scalar`

初始参考速度，单位由 **Source velocity units** 参数指定。例如，此图显示了一个初始参考速度为 `4` m/s 的驾驶循环。

速度与时间关系图

#### 依赖

要启用此参数，请选择 **Drive cycle source** 参数 `Wide Open Throttle (WOT)`。

### **Nominal reference speed, xdot\_wot1** — 速度 `30`（默认）| `scalar`

标称参考速度，单位由 **Source velocity units** 参数指定。这是循环中的最大速度。例如，此图显示了一个标称参考速度为 `28` m/s 的驾驶循环。

速度与时间关系图

#### 依赖

要启用此参数，请选择 **Drive cycle source** 参数 `Wide Open Throttle (WOT)`。

### **Time to start deceleration, t\_wot2** — 时间 `20`（默认）| `scalar`

开始车辆减速的时间，单位为 s。例如，此图显示了一个车辆在 `25` s 开始减速的驾驶循环。

速度与时间关系图

#### 依赖

要启用此参数，请选择 **Drive cycle source** 参数 `Wide Open Throttle (WOT)`。

### **Final reference speed, xdot\_wot2** — 速度 `0`（默认）| `scalar`

最终参考速度，单位由 **Source velocity units** 参数指定。例如，此图显示了一个最终参考速度为 `2` m/s 的驾驶循环。

速度与时间关系图

#### 依赖

要启用此参数，请选择 **Drive cycle source** 参数 `Wide Open Throttle (WOT)`。

### **WOT simulation time, t\_wotend** — 仿真时间持续时间 `30`（默认）| `scalar`

驾驶循环 WOT 仿真时间持续时间，单位为 s。例如，此图显示了一个总仿真时间为 `50` s 的驾驶循环。

速度与时间关系图

#### 依赖

要启用此参数，请选择 **Drive cycle source** 参数 `Wide Open Throttle (WOT)`。

#### 单位和采样周期

### **Source velocity units** — 指定速度单位 `m/s`（默认）

输入速度单位。

#### 依赖

要启用此参数，请选择 **Drive cycle source** 参数 `Wide Open Throttle (WOT)`、`Workspace variable` 或 `.mat, .xls, .xlsx or .txt file`。

### **Output velocity units** — 指定速度单位 `m/s`（默认）

输出速度单位。

### **Output acceleration units** — 指定加速度单位 `m/s^2`（默认）

指定输出加速度单位。

#### 依赖

要启用此参数，请选择 **Output acceleration**。

### **Output sample period (0 for continuous), dt** — 采样之间的周期 `0`（默认）| `scalar`

采样周期。设置为 `0` 表示连续采样。对于离散采样，请指定非零周期。

### 故障跟踪

#### 故障设置

### **Enable fault tracking** — 启用故障跟踪 `off`（默认）| `on`

选择此参数以启用驾驶循环故障跟踪。使用这些参数指定故障容差。如果车速不在允许的速度范围内，模块将设置故障条件。

#### 依赖

选择此参数将启用以下参数：

- **Speed tolerance, velBnd**
- **Speed tolerance units, velBndUnit**
- **Velocity feedback units, inUnit**
- **Time tolerance, timeBnd**

### **Speed tolerance, velBnd** — 驾驶循环速度容差 `2.0`（默认）| `scalar`

标准化测试规定了要使用的速度容差。以下是两个示例：

- EPA 测功机驾驶规程 — `2.0`
- WLTP 测试 — `2.0`

请注意，EPA 规程的单位是 mph，WLTP 测试的单位是 km/h。

该模块使用速度容差来确定参考时间处的允许速度范围。在由参考时间 +/- 时间容差定义的时间跨度内，车辆速度必须处于参考速度范围 +/- 速度容差之内，否则该模块将设置故障条件。这些图说明了该模块如何使用速度和时间容差来确定允许速度范围。

|  |  |
| --- | --- |
| 速度随时间变化图，指示速度增加时的允许速度范围 | 速度随时间变化图，指示速度减小时的允许速度范围 |

#### 依赖关系

要启用此参数，请在 **Fault Tracking** 选项卡上，选择 **Enable fault tracking**。

### **Speed tolerance units, velBndUnit** — 设置单位 `mph`（默认）

标准化测试规定了速度容差的单位。以下是两个示例：

- EPA 测功机驾驶规程 — `mph`
- WLTP 测试 — `km/h`

#### 依赖关系

要启用此参数，请在 **Fault Tracking** 选项卡上，选择 **Enable fault tracking**。

### **Velocity feedback units, inUnit** — 设置速度反馈单位 `m/s`（默认）

速度反馈单位。将该值设置为 `VelFdbk` 输入端口信号单位。

#### 依赖关系

要启用此参数，请在 **Fault Tracking** 选项卡上，选择 **Enable fault tracking**。

### **Time tolerance, timeBnd** — 时间容差 `1.0`（默认）| `scalar`

时间容差，单位为秒。标准化测试规定了要使用的时间容差。以下是两个示例：

- EPA 测功机驾驶规程 — `1.0`
- WLTP 测试 — `1.0`

该模块使用时间容差来确定参考时间处的允许速度范围。在由参考时间 +/- 时间容差定义的时间跨度内，车辆速度必须处于参考速度范围 +/- 速度容差之内，否则该模块将设置故障条件。这些图说明了该模块如何使用速度和时间容差来确定允许速度范围。

|  |  |
| --- | --- |
| 速度随时间变化图，指示速度增加时的允许速度范围 | 速度随时间变化图，指示速度减小时的允许速度范围 |

#### 依赖关系

要启用此参数，请在 **Fault Tracking** 选项卡上，选择 **Enable fault tracking**。

#### 故障设置

### **Enable Failure Tracking** — 启用故障跟踪 `off`（默认）| `on`

选择此参数以启用驾驶循环故障跟踪。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking**。选择 **Enable failure tracking** 参数会启用以下参数：

- **跟踪失败时停止仿真，stopSim**
- **Maximum number of faults, maxFaultCnt**
- **Maximum single fault time, maxFaultTime**
- **Maximum total fault time, maxTotFaultTime**

### **Stop simulation when trace fails** — 轨迹失败时停止仿真 `off`（默认）| `on`

选择此参数以在轨迹失败时停止仿真。

要启用此参数，请在 **Fault Tracking** 选项卡上，选择 **Enable failure tracking**。

### **Maximum number of faults, maxFaultCnt** — 允许的最大故障数 `10`（默认）| `scalar`

驾驶循环期间允许的最大故障数。对于标准化测试指定的数量，请使用以下设置：

- EPA 测功机驾驶规程 — *未指定*
- WLTP 测试 — `10`

如果故障数超过最大故障数，该模块将设置故障失败。

#### 依赖关系

要启用此参数，请在 **Fault Tracking** 选项卡上，选择 **Enable failure tracking**。

### **Maximum single fault time, maxFaultTime** — 单个故障的最大允许持续时间 `2.0`（默认）| `scalar`

单个故障的最大持续时间，单位为 s。对于标准化测试所指定的时间，请使用以下设置：

- EPA 测功机驾驶工况 —
  `2.0`
- WLTP 测试 — `1.0`

如果任何故障持续时间超过最大单个故障时间，该模块将设置故障失败。

#### 依赖关系

要启用此参数，请在 **Fault
Tracking** 选项卡上，选择 **Enable failure
tracking**。

### **Maximum total fault time, maxTotFaultTime** — 最大总故障时间 `15.0`（默认）| `scalar`

在故障条件下累计花费的最大时间，单位为 s。

如果故障条件下累计花费的时间超过最大总故障时间，该模块将设置故障失败。

#### 依赖关系

要启用此参数，请在 **Fault
Tracking** 选项卡上，选择 **Enable failure
tracking**。

#### 仿真轨迹

### **Display simulation trace** — 显示速度轨迹 `off`（默认）| `on`

选择此参数以显示速度轨迹窗口。选择此参数可能会减慢仿真时间。

#### 依赖关系

选择此参数将启用以下参数：

- **Simulation trace update rate,
  dtTrace**
- **仿真跟踪显示窗口，
  traceWindow**

### **Simulation trace update rate, dtTrace** — 轨迹更新周期 `1`（默认）| `scalar`

仿真轨迹更新周期，单位为 s。设置为 `0` 表示连续采样周期。对于离散周期，请指定非零速率。

#### 依赖关系

要启用此参数，请在 **Fault
Tracking** 选项卡上，选择 **Display simulation
trace**。

### **Simulation trace display window, traceWindow** — 轨迹窗口更新速率 `10`（默认）| `scalar`

仿真轨迹窗口更新速率，单位为 s。

#### 依赖关系

要启用此参数，请在 **Fault
Tracking** 选项卡上，选择 **Display simulation
trace**。

## 所属库

Powertrain Blockset / Vehicle Scenario Builder Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2023b：安装额外的标准驾驶工况，包括 EPA 测试程序工况和商用车占空比

在 R2023b 中，您可以安装额外的标准驾驶工况，包括：

- `EPA Federal Test Procedure(FTP75) - Without the Hot Soak
  Phase`
- `EPA Federal Test Procedure(FTP75) - Cold Stabilized
  Phase`
- `China Light-Duty Vehicle Test Cycle for Passenger
  Car`
- `China Heavy-Duty Commercial Vehicle Test Cycle for
  Tractor-Trailer`

## 描述

标准或指定的纵向行驶循环

Drive Cycle Source 模块生成标准或用户指定的纵向行驶循环。模块输出是作为时间函数的车辆纵向参考速度，以及适用时的换挡计划。您可以使用该行驶循环来：

- 在给定换挡计划的情况下，预测车辆跟随指定速度曲线所需的发动机扭矩和燃油消耗。
- 为车辆控制和被控对象模型的闭环加速和制动指令生成真实的速度和换挡计划。
- 在覆盖多个行驶循环时，研究、调整和优化车辆控制、系统性能和系统鲁棒性。
- 识别超出标准化测试规定容差的故障。这些包括：

  - EPA 测功机行驶计划1
  - 全球统一轻型车辆测试程序（WLTP）实验室测试2

要生成行驶循环，您可以使用：

- 来自预定义来源的行驶循环。该模块默认包含 `FTP–75` 行驶循环，并且可以从支持包加载额外的循环。

  要从支持包安装额外的行驶循环，请参阅 Install Drive Cycle Data。某些行驶循环包含换挡计划，例如 `JC08` 和 `CUEDC`。
- 定义您自己的行驶循环的工作区变量。
- .`mat`、.`xls`、.`xlsx` 或 .`txt` 文件。这允许您加载其他标准行驶循环，或您自己构建的行驶循环。
- 节气门全开（WOT）参数。设置初始参考速度和标称参考速度以产生参考速度的突然大幅变化，从而在车辆中引发 WOT 工况。

要实现此表中列出的目标，请使用指定的 Drive Cycle Source 模块参数选项。

| 目标 | 操作 |
| --- | --- |
| 如果仿真运行时间超过行驶循环长度，则重复行驶循环。 | 选择 **Repeat cyclically**。 |
| 输出由 Savitzky-Golay 微分计算得到的加速度。 | 选择 **Output acceleration**。 |
| 为离散应用指定采样周期。 | 指定 **Output sample period (0 for continuous), dt** 参数。 |
| 更新仿真运行时间，使其等于行驶循环的长度。 | 点击 **Update simulation time**。如果存在模型配置引用，则该模块不会启用此选项。 |
| 在 MATLAB® 图形中绘制行驶循环。 | 点击 **Plot drive cycle**。 |
| 使用工作区变量指定行驶循环。 | 点击 **Specify variable**。该模块：  - 将 **Drive cycle source** 参数设置为 `Workspace variable`。 - 启用 **From workspace** 参数。    指定工作区变量，使其包含时间、速度以及可选的换挡计划。 |
| 通过选择文件指定行驶循环。  这允许您加载所列标准循环之外的标准循环。 | 点击 **Select file**。该模块：  - 将 **Drive cycle source** 参数设置为 `.mat, .xls, .xlsx or .txt file`。 - 启用 **Drive cycle source file** 参数。    指定包含时间、速度以及可选换挡计划的文件。 |
| 输出行驶循环挡位。 | 首先指定包含换挡计划的行驶循环。您可以使用：  - 支持包来安装包含换挡计划的标准行驶循环，例如 `JC08` 和 `CUEDC`。 - 工作区变量。 - .`mat`、.`xls`、.`xlsx` 或 .`txt` 文件。    然后点击 **Output gear shift data**。 |
| 从支持包安装额外的行驶循环。 | 点击 **Install additional drive cycles**。如果您可以从支持包安装额外的行驶循环，则该模块会启用此选项。 |
| 识别超出标准化测试规定容差的行驶循环故障。 | 在 **Fault Tracking** 选项卡上，使用参数指定故障容差。如果车辆速度不在允许速度范围内，则该模块设置故障条件。 |

### 故障与失效跟踪

在**故障跟踪**选项卡上，使用参数指定故障容差。如果车速在给定参考时间内不在允许范围内，模块将设置故障条件。此处展示了 EPA 和 WLTP 循环的示例：

| 参数 | 描述 | 设置 | |
| --- | --- | --- | --- |
| EPA 标准1 | WLTP 测试2 |
| **速度容差** | 在时间容差内，高于行驶循环速度曲线最高点和低于最低点的速度容差。 | 2.0 mph | 2.0 km/h |
| **时间容差** | 模块用于确定允许速度范围的时间。 | 1.0 s | 1.0 s |
| **最大故障次数** | 行驶循环期间允许的最大故障次数，超过则导致故障失效。 | *未指定* | 10 |
| **最大单次故障时间** | 允许的最大故障持续时间，超过则导致故障失效。 | 2.0 s | 1.0 s |
| **最大总故障时间** | 故障条件下允许的最大累计时间，超过则导致故障失效。 | *未指定* | *未指定* |

模块使用时间容差来确定参考时间处的允许速度范围。在参考时间 +/- 时间容差定义的时间跨度内，车速必须处于参考速度范围 +/- 速度容差之内，否则模块将设置故障条件。这些图说明了模块如何使用速度容差和时间容差来确定允许速度范围。

|  |  |
| --- | --- |
| 速度随时间变化图，指示加速时的允许速度范围 | 速度随时间变化图，指示减速时的允许速度范围 |

### 使用工作区变量创建行驶循环

如果将 **Drive cycle source** 设置为 `Workspace
variable`，则可以指定一个定义行驶循环的工作区变量。

下表提供了使用工作区变量创建您自己的行驶循环的示例。

| 工作区变量 | 源速度单位 | 输出速度单位 | 行驶循环图 |
| --- | --- | --- | --- |
| 不带换挡计划的结构体，**From workspace** 设置为 `myCycleS`。  ``` t = 0:1:100; xdot = 5.*sin(t)+10; myCycleS.time = t'; myCycleS.signals.values = xdot'; ``` | `m/s` | `mph` | 显示正弦波的速度-时间图 |
| 带换挡计划的结构体，**From workspace** 设置为 `myCycleS`。  ``` gears=[0, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4]; t=0:1:10; xdot=[0,5,10,15,20,25,30,30,30,30,30]; myCycleS.time=t'; myCycleS.signals.values=[xdot',gears']; ``` | `m/s` | `mph` | 显示速度-时间图，速度从 0 秒时的 0 mph 线性增加到 6 秒时的 70 mph。6 秒后，速度保持恒定在 70 mph。 |
| 不带换挡计划的二维数组，**From workspace** 设置为 `myCycleA`。  ``` t = 0:1:100; xdot = 5.*sin(t)+5; myCycleA = [t',xdot']; ``` | `m/s` | `mph` | 显示正弦波的速度-时间图 |
| 带换挡计划的二维数组，**From workspace** 设置为 `myCycleA`。  ``` gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,5,10,15,20,25,30,40,50,60,60]; myCycleA=[t',xdot',gears']; ``` | `mph` | `mph` | 显示速度-时间图，速度从 0 秒时的 0 mph 线性增加到 6 秒时的 30 mph，再到 9 秒时的 60 mph。9 秒后，速度保持恒定在 60 mph。 |
| 不带换挡计划的时间序列对象，**From workspace** 设置为 `myCycleT`。  ``` myCycleT = timeseries; t = 0:1:100; xdot = 5.*sin(t)+20; myCycleT.Data = xdot'; myCycleT.Time = t'; ``` | `m/s` | `mph` | 显示正弦波的速度-时间图 |
| 不带换挡计划的时间序列对象，**From workspace** 设置为 `myCycleT`。  ``` myCycleT = timeseries; gears=[0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5]; t=0:1:10; xdot=[0,10,20,30,32,33,34,40,50,60,60]; myCycleT.Data = [xdot',gears']; myCycleT.Time = t'; ``` | `mph` | `mph` | 显示以 mph 为单位线性增加的速度-时间图。9 秒后，速度保持恒定在 60 mph。 |
