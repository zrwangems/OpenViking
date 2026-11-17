---
type: simulink-block
title: 'Radar Data Generator'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'radardatagenerator'
documentation_source_path: 'ref/radardatagenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Radar Data Generator

## 端口
```yaml
ports:
- name: Targets (Body Frame)
  summary: 目标位姿 Simulink® 总线，包含 MATLAB® 结构体
  direction: input
- name: INS
  summary: 来自 INS 的雷达位姿 Simulink 总线，包含 MATLAB 结构体
  direction: input
- name: Time
  summary: 当前仿真时间 非负标量
  direction: input
  data_types: double
- name: Clustered detections
  summary: 包含 MATLAB 结构的 Simulink 总线，用于聚类目标检测
  direction: output
- name: Tracks
  summary: 目标航迹，包含 MATLAB 结构的 Simulink 总线
  direction: output
- name: Detections
  summary: 包含 MATLAB 结构的 Simulink 总线，用于未聚类目标检测
  direction: output
- name: Configuration
  summary: 当前传感器配置 包含 MATLAB 结构的 Simulink 总线
  direction: output
```

### 输入

### **Targets (Body Frame)** — 目标位姿 Simulink® 总线，包含 MATLAB® 结构体

平台坐标系中的目标位姿，指定为包含 MATLAB 结构体的 Simulink 总线。`Targets` 输入端口可以接受来自 Automated Driving Toolbox™ 中 Scenario Reader (Automated Driving Toolbox) 模块的 `Actors` 输出端口的输出，或来自 Sensor Fusion and Tracking Toolbox™ 中 Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) 的 `Platforms` 输出端口的输出。

Scenario Reader 模块和 Tracking Scenario Reader 模块输出的位姿数据格式不同。Radar Data Generator 可读取来自任一模块的数据。在每种情况下，数据由两个数据字段后跟一个结构体数组组成。这些结构体定义了 `Platforms` 的数量或 `Actors` 的数量。`Platforms` 和 `Actors` 统称为 `Targets`。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| |  |  | | --- | --- | | **输入模块** | **字段名** | | Scenario Reader (Automated Driving Toolbox) | `NumActors` | | Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) | `NumPlatforms` | | 有效目标位姿数量 | 非负整数 |
| **Time** | 当前仿真时间（可选）。如果缺失，则使用当前 Simulink 仿真时间。 | 实值标量 |
| |  |  | | --- | --- | | **输入模块** | **字段名** | | Scenario Reader (Automated Driving Toolbox) | `Actors` | | Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) | `Platforms` | | 有效目标位姿 | 目标位姿结构体数组 |

`Actors` 结构体在 Scenario Reader (Automated Driving Toolbox) 模块的输出端口中有描述，`Platforms` 结构体在 Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) 模块的输出端口中有描述。

### **INS** — 来自 INS 的雷达位姿 Simulink 总线，包含 MATLAB 结构体

来自惯性导航系统（INS）的雷达位姿信息，指定为包含单个 MATLAB 结构体的 Simulink 总线。该结构体包含由 INS 提供的雷达平台位姿信息。然后可以使用 INS 信息来估计 NED 坐标系中的目标位置。INS 是一个 `struct`，具有以下字段：

|  |  |
| --- | --- |
| **字段** | **定义** |
| `Position` | 场景坐标系中的位置，指定为实值 1×3 向量。单位为米。 |
| `Velocity` | 场景坐标系中的速度，指定为实值 1×3 向量。单位为 m/s。 |
| `Orientation` | 相对于场景坐标系的姿态，指定为 3×3 实值旋转矩阵。该旋转是从导航坐标系到当前 INS 机体坐标系的旋转。这也称为“父到子”旋转。 |

#### 依赖关系

要启用此端口，请选中 **Enable INS** 复选框。

### **Time** — 当前仿真时间 非负标量

当前仿真时间，指定为非负标量。传感器仅在对应于更新间隔整数倍的仿真时间生成报告，更新间隔由 **Update rate (Hz)** 参数的倒数给出。单位为秒。

#### 依赖关系

要启用此端口，请将 **Source of target truth time** 设置为 `Input port`。

如果未启用此端口，则时间取自 `Target poses` 输入总线上的时间。如果该总线上没有时间，则使用当前 Simulink 仿真时间。

**数据类型：** `double`
### 输出

### **Clustered detections** — 包含 MATLAB 结构的 Simulink 总线，用于聚类目标检测

聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于聚类检测，该模块对每个目标输出单个检测，其中每个检测是该目标未聚类检测的质心。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器，例如 Sensor Fusion and Tracking Toolbox 中的 Global
Nearest Neighbor Multi Object Tracker (Sensor Fusion and Tracking Toolbox) 模块。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测的数量 | 非负整数 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | 布尔值 |
| `Detections` | 目标检测 | 目标检测结构体数组，长度由 **Maximum number of target reports** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构体包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数使用的参数 |

- 对于直角坐标，`Measurement` 和
  `MeasurementNoise` 以 **Coordinate system** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和
  `MeasurementNoise` 以球坐标系报告，该坐标系基于传感器直角坐标系。

**`Measurement` 和 `MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| Scenario | 此表显示了坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示了坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

对于 `ObjectAttributes`，此表描述了用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的目标的 `ActorID` 或 `PlatformID` 标识符。对于虚警，该值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |
| `BounceTargetIndex` | 生成多径反射的目标标识符，该多径反射产生了鬼影目标报告。仅当 **HasGhosts** 为 `true` 时存在。 |
| `BouncePathIndex` | 与目标报告相关联的反射路径索引。仅当 **HasGhosts** 为 `true` 时存在。  **反射路径索引**  | BouncePathIndex | 描述 | | --- | --- | | 0 | 直接路径目标报告 | | 1 | 第一条 2 次反射路径检测 | | 2 | 第二条 2 次反射路径 | | 3 | 3 次反射路径 | |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate system** 参数设置为
`Body` 时，父坐标系为平台本体。当您将
**Coordinate system** 设置为 `Sensor rectangular` 或
`Sensor spherical` 时，父坐标系为传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量值的坐标系。当 `Frame` 设置为 `'rectangular'` 时，检测结果以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测结果以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的三维向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖关系

要启用此端口，请将 **Target reporting format** 下拉菜单选择为 `Clustered detections`。

### **Tracks** — 目标航迹，包含 MATLAB 结构的 Simulink 总线

目标航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

下表显示了结构体字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of target reports** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

下表显示了每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为秒。 |
| `Age` | 航迹被更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于已确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1×*K* 逻辑数组。*K* 是记录的最新航迹逻辑状态的数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下被更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回为 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

该模块仅输出已确认航迹，即在航迹初始化后的前 *N* 次更新中，模块为其分配至少 *M* 次检测的航迹。要指定 *M* 和 *N* 的值，请使用 **M and N for the M-out-of-N confirmation** 参数。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡上将 **Target reporting format** 参数设置为 `Tracks`。

### **Detections** — 包含 MATLAB 结构的 Simulink 总线，用于未聚类目标检测

未聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于未聚类检测，该模块输出所有检测，并且一个目标可以有多个检测。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器，例如 Multi-Object
Tracker (Automated Driving Toolbox) 模块，并生成航迹。

该结构必须包含以下字段：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测的数量 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | Boolean |
| `Detections` | 目标检测 | 目标检测结构的数组，其长度由 **Maximum number of target reports** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器的初始化函数所使用的参数 |

- 对于直角坐标，`Measurement` 和
  `MeasurementNoise` 以 **Coordinate system** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和
  `MeasurementNoise` 以球坐标系报告，该坐标系基于传感器直角坐标系。

**`Measurement` 和 `MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| Scenario | 此表显示了坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示了坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

对于 `ObjectAttributes`，此表描述了用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的目标的 `ActorID` 或 `PlatformID` 的标识符。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |
| `BounceTargetIndex` | 生成多径反射的目标的标识符，该多径反射产生了鬼影目标报告。仅当 **HasGhosts** 为 `true` 时存在。 |
| `BouncePathIndex` | 与目标报告相关联的反射路径的索引。仅当 **HasGhosts** 为 `true` 时存在。  **反射路径索引**  | BouncePathIndex | 描述 | | --- | --- | | 0 | 直接路径目标报告 | | 1 | 第一个 2 次反射路径检测 | | 2 | 第二个 2 次反射路径 | | 3 | 3 次反射路径 | |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate system** 参数设置为
`Body` 时，父坐标系为平台本体。当您将
**Coordinate system** 设置为 `Sensor rectangular` 或
`Sensor spherical` 时，父坐标系为传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量的坐标系。当 `Frame` 设置为 `'rectangular'` 时，检测结果以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测结果以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的三维向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖关系

要启用此端口，请将 **Target reporting format** 参数设置为 `Detections`。

### **Configuration** — 当前传感器配置 包含 MATLAB 结构的 Simulink 总线

Configuration，返回为包含 MATLAB 结构的 Simulink 总线。此输出可用于确定在目标执行期间哪些目标落在雷达波束内。结构体字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumConfigurations` | 有效配置的数量 | 整数 |
| `Configurations` | 配置结构体 | 由 `NumConfigurations` 个配置结构体组成的数组 |

配置结构体具有以下字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `SensorIndex` | 唯一传感器索引，返回为正整数。 |
| `IsValidTime` | 有效检测时间，返回为 `true` 或 `false`。当在由更新速率指定的更新间隔之间请求检测更新时，`IsValidTime` 为 `false`。 |
| `IsScanDone` | 当传感器完成一次扫描时，`IsScanDone` 为 `true`。 |
| `FieldOfView` | 传感器的视场，返回为 2×1 正实数值向量，[`azfov`;`elfov`]。`azfov` 和 `elfov` 分别表示方位角和仰角方向的视场。 |
| `RangeLimits` | 传感器的最小和最大距离，以米为单位，指定为 1×2 非负实数值向量，形式为 `[rmin,rmax]`。 |
| `RangeRateLimits` | 传感器的最小和最大距离变化率，以米每秒为单位，指定为 1×2 实数值向量，形式为 `[rrmin,rrmax]`。 |
| `MeasurementParameters` | 传感器测量参数，返回为结构体数组，包含将顶层坐标系中的位置和速度变换到当前传感器坐标系所需的坐标坐标系变换。有关 `MeasurementParameters` 的详细信息，请参阅 Measurement Parameters。 |

#### 依赖关系

要启用此端口，请选中 **Enable radar configuration output** 复选框。
## 参数
```yaml
parameters:
- name: Unique identifier of sensor
  summary: 唯一传感器标识符 0（默认）| 正整数
  group: 参数
- name: Update rate (Hz)
  summary: 传感器更新速率 10（默认）| 正实数标量
  group: 参数
- name: Translation [ X, Y, Z ] relative to ego origin (m)
  summary: 雷达在平台上的安装位置 [3.4,0,0.2]（默认）| 形式为 [x,y,z] 的 1×3 实数值向量
  group: 参数
- name: Rotation [Yaw,Pitch,Roll] relative to ego's frame (deg)
  summary: 雷达的安装旋转角度 [0 0 0]（默认）| 形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量
  group: 参数
- name: Enable elevation angle measurements
  summary: 使雷达能够测量目标仰角 off（默认）| on
  group: 参数
- name: Enable range rate measurements
  summary: 使雷达能够测量目标距离变化率 on（默认）| off
  group: 参数
- name: Add noise to measurements
  summary: 启用向雷达传感器测量值添加噪声 on（默认）| off
  group: 参数
- name: Enable false reports
  summary: 启用生成虚警雷达检测 on（默认）| off
  group: 参数
- name: Enable occlusion
  summary: 启用视线遮挡 on（默认）| off
  group: 参数
- name: Enable ghosts
  summary: 启用鬼影目标 off（默认）| on
  group: 参数
- name: Maximum number of target reports
  summary: 最大检测数或航迹数 50（默认）| 正整数
  group: 参数
- name: Target reporting format
  summary: 生成的目标报告的格式 Clustered detections（默认）| Tracks | Detections
  group: 参数
- name: Coordinate system
  summary: 所报告检测的坐标系 Body（默认）| Sensor rectangular | Sensor spherical | Scenario
  group: 参数
- name: Source of target truth time
  summary: 目标真值时间的来源 Auto（默认）| Input port
  group: 参数
- name: Enable INS
  summary: 启用 INS 输入端口 off（默认）| on
  group: 参数
- name: Source of output target report bus name
  summary: 输出目标报告总线名称的来源 Auto（默认）| Property
  group: 参数
- name: Specify an output target report bus name
  summary: 目标报告输出总线的名称 BusRadarDataGenerator（默认）| 有效总线名称
  group: 参数
- name: Enable radar configuration output
  summary: 启用雷达配置输出 off（默认）| on
  group: 参数
- name: Source of output config bus name
  summary: 输出 config 总线名称的来源 Auto（默认）| Property
  group: 参数
- name: Specify an output config bus name
  summary: 目标报告输出总线的名称 BusRadarDataGeneratorConfig（默认）| 有效总线名称
  group: 参数
- name: Azimuth resolution (deg)
  summary: 雷达方位分辨率 4（默认）| 正实数标量
  group: Measurements
- name: Elevation resolution (deg)
  summary: 雷达俯仰分辨率 5（默认）| 正实数标量
  group: Measurements
- name: Range resolution (m)
  summary: 雷达距离分辨率 2.5（默认）| 正实数标量
  group: Measurements
- name: Range rate resolution (m/s)
  summary: 雷达距离变化率分辨率 0.5（默认）| 正实数标量
  group: Measurements
- name: Azimuth bias fraction
  summary: 雷达方位偏置系数 0.1（默认）| 非负标量
  group: Measurements
- name: Elevation bias fraction
  summary: 雷达俯仰偏置系数 0.1（默认）| 非负标量
  group: Measurements
- name: Range bias fraction
  summary: 距离偏置系数 0.05（默认）| 非负标量
  group: Measurements
- name: Range rate bias fraction
  summary: 距离变化率偏置系数 0.05（默认）| 非负标量
  group: Measurements
- name: 总角视场 [AZ, EL] (deg)
  summary: 雷达的角视场 [20 5]（默认）| 形式为 [azfov,elfov] 的 1×2 正实值向量
  group: Measurements
- name: 距离限制 [MIN, MAX] (m)
  summary: 雷达的最小和最大距离 [0 150]（默认）| 形式为 [min max] 的 1×2 非负实值向量
  group: Measurements
- name: 距离变化率限制 [MIN, MAX] (m/s)
  summary: 雷达的最小和最大距离变化率 (m/s) [-100 100]（默认）| 形式为 [min max] 的 1×2 实值向量
  group: Measurements
- name: 检测概率
  summary: 检测目标的概率 0.9（默认）| 范围 (0, 1] 内的标量
  group: Measurements
- name: 虚警率
  summary: 虚警报告率 1e-06（默认）| 范围 [10–7, 10–3] 内的正实标量
  group: Measurements
- name: 参考目标距离 (m)
  summary: 给定检测概率的参考距离 100（默认）| 正实标量
  group: Measurements
- name: 参考目标 RCS (dBsm)
  summary: 给定检测概率的参考雷达截面积 0（默认）| 实标量
  group: Measurements
- name: 中心频率 (Hz)
  summary: 雷达频带的中心频率 77e9（默认）| 正实标量
  group: Measurements
- name: 滤波器初始化函数名称
  summary: 卡尔曼滤波器初始化函数 initcvekf（默认）| 函数句柄
  group: Measurements
- name: M-out-of-N 确认的 M 和 N
  summary: 航迹确认阈值 [2 3]（默认）| 正整数的 1×2 向量
  group: Measurements
- name: P-out-of-R 删除的 P 和 R
  summary: 航迹删除阈值 [5 5]（默认）| 正整数的 1×2 向量
  group: Measurements
- name: 随机数生成
  summary: 指定随机数生成器种子的方法 Repeatable（默认）| Specify seed | Not repeatable
  group: Measurements
- name: Initial seed
  summary: 随机数生成器种子 0（默认）| 小于 232 的非负整数
  group: Measurements
- name: 目标配置文件定义
  summary: 指定目标配置文件的方法 From Scenario Reader block（默认）| MATLAB expression | Parameters
  group: 目标配置文件
- name: MATLAB expression for target profiles
  summary: 目标配置文件的 MATLAB 表达式 MATLAB 结构体 | MATLAB 结构体数组 | 有效的 MATLAB 表达式
  group: 目标配置文件
- name: Unique target identifiers
  summary: 场景定义的目标标识符 []（默认）| 正整数 | 长度为 *L* 的唯一正整数向量
  group: 目标配置文件
- name: 目标分类标识符
  summary: 用户自定义分类标识符 0（默认）| 整数 | 长度为 *L* 的整数向量
  group: 目标配置文件
- name: 目标长方体长度 (m)
  summary: 目标长方体长度 4.7（默认）| 正实数标量 | 长度为 *L* 的正值向量
  group: 目标配置文件
- name: 目标长方体宽度 (m)
  summary: 目标长方体宽度 1.8（默认）| 正实数标量 | 长度为 *L* 的正值向量
  group: 目标配置文件
- name: 高度长方体高度 (m)
  summary: 角色长方体高度 1.4（默认）| 正实数标量 | 长度为 *L* 的正值向量
  group: 目标配置文件
- name: 目标长方体旋转中心 (m)
  summary: 目标长方体旋转中心 {[-1.35, 0, 0]}（默认）| 长度为 *L* 的元胞数组，包含实值 1×3 向量
  group: 目标配置文件
- name: Target signatures
  summary: 目标签名元胞数组
  group: 目标配置文件
```

### 参数

#### 传感器标识

### **Unique identifier of sensor** — 唯一传感器标识符 `0`（默认）| 正整数

唯一传感器标识符，指定为正整数。使用此参数区分多传感器系统中来自不同传感器的检测或航迹。为每个传感器指定唯一的值。如果您未将 **Unique identifier of sensor** 从默认值 `0` 更新，则雷达在仿真开始时返回错误。

### **Update rate (Hz)** — 传感器更新速率 `10`（默认）| 正实数标量

更新速率，指定为正实数标量。雷达按此倒数定义的间隔生成新报告。在更新间隔之间请求的任何传感器更新不包含检测或航迹。单位为 Hz。

#### 传感器安装

### **Translation [ X, Y, Z ] relative to ego origin (m)** — 雷达在平台上的安装位置 `[3.4,0,0.2]`（默认）| 形式为 `[x,y,z]` 的 1×3 实数值向量

雷达在平台上的传感器位置，指定为形式为 `[x,y,z]` 的 1×3 实数值向量。此参数定义传感器相对于平台原点沿 *x* 轴、*y* 轴和 *z* 轴的坐标。单位为米。

### **Rotation [Yaw,Pitch,Roll] relative to ego's frame (deg)** — 雷达的安装旋转角度 `[0 0 0]`（默认）| 形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量

雷达的安装旋转角度，指定为形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量。该参数定义传感器相对于平台坐标系的固有欧拉角旋转，依次绕 *z* 轴、*y* 轴和 *x* 轴旋转，其中：

- *z*yaw，即 *偏航角*，使传感器绕平台坐标系的 *z* 轴旋转。
- *y*pitch，即 *俯仰角*，使传感器绕平台坐标系的 *y* 轴旋转。该旋转相对于 *z*yaw 旋转后所得的传感器位置。
- *x*roll，即 *横滚角*，使传感器绕平台坐标系的 *x* 轴旋转。该旋转相对于 *z*yaw 和 *y*pitch 旋转后所得的传感器位置。

当分别沿 *z* 轴、*y* 轴和 *x* 轴的正方向观察时，这些角度为顺时针正方向。单位为度。

#### 检测报告

### **Enable elevation angle measurements** — 使雷达能够测量目标仰角 `off`（默认）| `on`

选中此复选框可对能够估计目标仰角的雷达传感器进行建模。

### **Enable range rate measurements** — 使雷达能够测量目标距离变化率 `on`（默认）| `off`

选中此复选框可使雷达能够从目标检测中测量距离变化率。

### **Add noise to measurements** — 启用向雷达传感器测量值添加噪声 `on`（默认）| `off`

选择此参数可向雷达测量值添加噪声。否则，测量值不含噪声。即使清除此参数，生成的检测输出中 `MeasurementNoise` 字段所报告的测量噪声协方差矩阵仍表示选中 **Add noise to measurements** 时所添加的测量噪声。

### **Enable false reports** — 启用生成虚警雷达检测 `on`（默认）| `off`

选择此参数可启用生成虚警雷达测量值。如果清除此参数，雷达仅报告实际检测。

### **Enable occlusion** — 启用视线遮挡 `on`（默认）| `off`

选择此参数可启用视线遮挡，此时雷达仅对雷达具有直接视线的对象生成检测。例如，启用此参数后，雷达不会为位于另一对象后方且被遮挡而不可见的对象生成检测。

### **Enable ghosts** — 启用鬼影目标 `off`（默认）| `on`

选择此参数可为雷达信号发射与接收之间具有最多三次反射的多径传播路径生成鬼影目标。

### **Maximum number of target reports** — 最大检测数或航迹数 `50`（默认）| 正整数

传感器报告的最大检测数或航迹数，指定为正整数。传感器按距传感器距离递增的顺序报告检测，直到达到此最大数量。

### **Target reporting format** — 生成的目标报告的格式 **Clustered detections**（默认）| **Tracks** | **Detections**

生成的目标报告的格式，指定为以下选项之一：

- **Clustered detections** — 该模块将目标报告生成为*聚类检测*，其中每个目标报告为一个单一检测，该检测是未聚类目标检测的质心。该模块在 **Clustered detections** 输出端口返回聚类检测。
- **Tracks** — 该模块将目标报告生成为*航迹*，即经过跟踪滤波器处理后的聚类检测。该模块在 **Tracks** 输出端口返回聚类检测。
- **Detections** — 该模块将目标报告生成为*未聚类检测*，其中每个目标可以有多个检测。该模块在 **Detections** 输出端口返回聚类检测。

### **Coordinate system** — 所报告检测的坐标系 **Body**（默认）| **Sensor rectangular** | **Sensor spherical** | **Scenario**

所报告检测的坐标系，指定为以下选项之一：

- **Body** — 检测在传感器平台的矩形本体系中报告。
- **Sensor rectangular** — 检测在传感器矩形本体坐标系中报告。
- **Sensor spherical** — 检测在以雷达传感器为中心并与平台上雷达朝向对齐的球坐标系中报告。
- **Scenario** — 检测在矩形场景坐标系中报告。场景坐标系定义为仿真开始时的局部导航坐标系。

#### Port Settings

### **Source of target truth time** — 目标真值时间的来源 `Auto`（默认）| `Input port`

输出真值时间的来源，指定为以下选项之一：

- `Auto` — 该模块使用目标总线上提供的时间，如果不存在，则使用当前 Simulink 仿真时间。
- `Input port` — 该模块使用该模块的 `Time` 输入端口上提供的时间。

### **Enable INS** — 启用 INS 输入端口 off（默认）| on

选择此参数以允许使用 `INS` 输入端口输入 INS 数据。

### **Source of output target report bus name** — 输出目标报告总线名称的来源 `Auto`（默认）| `Property`

输出目标报告总线名称的来源，指定为以下选项之一：

- `Auto` — 该模块自动创建总线名称。
- `Property` — 通过使用 **Specify an output target report bus name** 参数指定总线名称。

此总线包含 Clustered detections、Tracks 或 Detections 输出端口数据。

### **Specify an output target report bus name** — 目标报告输出总线的名称 `BusRadarDataGenerator`（默认）| 有效总线名称

要在输出端口中返回的目标报告总线的名称，指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **Source of output target report bus name** 参数设置为 `Property`。

### **Enable radar configuration output** — 启用雷达配置输出 `off`（默认）| `on`

启用 `Configuration` 输出端口。

### **Source of output config bus name** — 输出 config 总线名称的来源 `Auto`（默认）| `Property`

输出 `config` 总线名称的来源，指定为以下选项之一：

- `Auto` — 该模块自动创建总线名称。
- `Property` — 通过使用 **Specify an output config bus name** 参数指定总线名称。

### **Specify an output config bus name** — 目标报告输出总线的名称 `BusRadarDataGeneratorConfig`（默认）| 有效总线名称

指定在输出端口中返回的 `config` 总线的名称。

#### 依赖关系

要启用此参数，请将 **Source of output config bus name** 参数设置为 `Property`。

### Measurements

#### Resolution Settings

### **Azimuth resolution (deg)** — 雷达方位分辨率 `4`（默认）| 正实数标量

雷达的方位分辨率，指定为正标量。*方位分辨率*定义了雷达能够区分两个目标的最小方位角间隔。方位分辨率通常为雷达方位角波束宽度的 3 dB 下降点。单位为度。

### **Elevation resolution (deg)** — 雷达俯仰分辨率 `5`（默认）| 正实数标量

雷达的俯仰分辨率，指定为正标量。*俯仰分辨率*定义了雷达能够区分两个目标的最小俯仰角间隔。俯仰分辨率通常为雷达俯仰角波束宽度的 3 dB 下降点。单位为度。

#### 依赖关系

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **Range resolution (m)** — 雷达距离分辨率 `2.5`（默认）| 正实数标量

雷达的距离分辨率，以米为单位，指定为正实数标量。*距离分辨率*定义了雷达能够区分两个目标的最小距离间隔。单位为米。

### **Range rate resolution (m/s)** — 雷达距离变化率分辨率 `0.5`（默认）| 正实数标量

雷达的距离变化率分辨率，指定为正实数标量。*距离变化率分辨率*定义了雷达能够区分两个目标的最小距离变化率间隔。单位为米每秒。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上选中 **Enable range rate measurements** 复选框。

#### 偏置设置

### **Azimuth bias fraction** — 雷达方位偏置系数 `0.1`（默认）| 非负标量

雷达的方位偏置系数，指定为非负标量。*方位偏置*表示为 **Azimuth resolution (deg)** 参数中指定的方位分辨率的一部分。此值设定了雷达方位精度的下界，并且是无量纲的。

### **Elevation bias fraction** — 雷达俯仰偏置系数 `0.1`（默认）| 非负标量

雷达的俯仰偏置系数，指定为非负标量。*俯仰偏置*表示为 **Elevation resolution (deg)** 参数中指定的俯仰分辨率的一部分。此值设定了雷达俯仰精度的下界，并且是无量纲的。

#### 依赖关系

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **Range bias fraction** — 距离偏置系数 `0.05`（默认）| 非负标量

雷达的距离偏置系数，指定为非负标量。距离偏置表示为 **Range resolution (m)** 属性指定的距离分辨率的一部分。此属性设定了雷达距离精度的下界，并且是无量纲的。

### **Range rate bias fraction** — 距离变化率偏置系数 `0.05`（默认）| 非负标量

雷达的距离变化率偏置系数，指定为非负标量。距离变化率偏置表示为 **Range rate resolution (m/s)** 参数指定的距离变化率分辨率的一部分。此属性设定了雷达距离变化率精度的下界，并且是无量纲的。

#### 依赖关系

要启用此参数，请选中 **Enable range rate measurements** 复选框。

#### 检测器设置

### **总角视场 [AZ, EL] (deg)** — 雷达的角视场 `[20 5]`（默认）| 形式为 `[azfov,elfov]` 的 1×2 正实值向量

雷达的角视场，指定为形式为 `[azfov elfov]` 的 1×2 正实值向量。视场定义传感器所张成的总角度范围。方位视场 `azfov` 必须位于区间 (0, 360] 内。俯仰视场 `elfov` 必须位于区间 (0, 180] 内。单位为度

### **距离限制 [MIN, MAX] (m)** — 雷达的最小和最大距离 `[0 150]`（默认）| 形式为 `[min max]` 的 1×2 非负实值向量

雷达的最小和最大距离，指定为形式为 `[min max]` 的 1×2 非负实值向量。雷达不会检测位于此范围之外的目标。最大距离 `max` 必须大于最小距离 `min`。单位为米。

### **距离变化率限制 [MIN, MAX] (m/s)** — 雷达的最小和最大距离变化率 (m/s) `[-100 100]`（默认）| 形式为 `[min max]` 的 1×2 实值向量

雷达的最小和最大距离变化率，指定为形式为 `[min max]` 的 1×2 实值向量。雷达不会检测位于此距离变化率范围之外的目标。最大距离变化率 `max` 必须大于最小距离变化率 `min`。单位为米每秒。

#### 依赖

要启用此参数，请选中 **Enable range rate measurements** 复选框。

### **检测概率** — 检测目标的概率 `0.9`（默认）| 范围 (0, 1] 内的标量

检测目标的概率，指定为范围 (0, 1] 内的标量。此量定义具有雷达截面积的目标的检测概率，其中雷达截面积由 **Reference target RCS (dBsm)** 参数在由 **Reference target range (m)** 参数指定的参考检测距离处指定。单位无量纲。

### **虚警率** — 虚警报告率 `1e-06`（默认）| 范围 [10–7, 10–3] 内的正实标量

每个雷达分辨率单元内的虚警报告率，指定为范围 [10–7, 10–3] 内的正实标量。该模块根据 **Azimuth resolution (deg)** 和 **Range resolution (m)** 参数确定分辨率单元，并且在启用时还根据 **Elevation resolution (deg)** 和 **Range rate resolution (m/s)** 参数确定分辨率单元。单位无量纲。

### **参考目标距离 (m)** — 给定检测概率的参考距离 `100`（默认）| 正实标量

给定检测概率和给定参考雷达截面积 (RCS) 的参考距离，指定为正实标量。*参考距离* 是指具有由 **Reference target RCS (dBsm)** 参数指定的雷达截面积的目标以由 **Detection probability** 参数指定的检测概率被检测到的距离。单位为米。

### **参考目标 RCS (dBsm)** — 给定检测概率的参考雷达截面积 `0`（默认）| 实标量

给定检测概率和参考距离的参考雷达截面积 (RCS)，指定为实标量。*参考 RCS* 是指在指定的 **Reference target range (m)** 参数值处，目标以由 **Detection probability** 参数指定的概率被检测到时的 RCS 值。数值以 dBsm 表示。

### **中心频率 (Hz)** — 雷达频带的中心频率 `77e9`（默认）| 正实标量

雷达频带的中心频率，指定为正标量。单位为 Hz。

#### 跟踪器设置

### **滤波器初始化函数名称** — 卡尔曼滤波器初始化函数 `initcvekf`（默认）| 函数句柄

卡尔曼滤波器初始化函数，指定为有效卡尔曼滤波器初始化函数名称的字符向量或字符串标量。

下表显示了可用于指定**滤波器初始化函数名称**的初始化函数。

| 初始化函数 | 函数定义 |
| --- | --- |
| `initcaabf` | 初始化匀加速 alpha-beta 卡尔曼滤波器 |
| `initcvabf` | 初始化匀速度 alpha-beta 卡尔曼滤波器 |
| `initcakf` | 初始化匀加速线性卡尔曼滤波器。 |
| `initcvkf` | 初始化匀速度线性卡尔曼滤波器。 |
| `initcaekf` | 初始化匀加速扩展卡尔曼滤波器。 |
| `initctekf` | 初始化匀转弯率扩展卡尔曼滤波器。 |
| `initcvekf` | 初始化匀速度扩展卡尔曼滤波器。 |
| `initcaukf` | 初始化匀加速无迹卡尔曼滤波器。 |
| `initctukf` | 初始化匀转弯率无迹卡尔曼滤波器。 |
| `initcvukf` | 初始化匀速度无迹卡尔曼滤波器。 |

您也可以编写自己的初始化函数。该函数必须具有以下语法：

```
filter = filterInitializationFcn(detection)
```

此函数的输入是检测报告，类似于由 `objectDetection` 对象创建的检测报告。此函数的输出必须是跟踪滤波器对象，例如 `trackingKF`、`trackingEKF`、`trackingUKF` 或 `trackingABF`。

为帮助您编写此函数，您可以在 MATLAB 中查看所提供函数的详细信息。例如：

```
type initcvekf
```

#### 依赖关系

要启用此参数，请将**目标报告格式**参数设置为 `'Tracks'`。

### **M-out-of-N 确认的 M 和 N** — 航迹确认阈值 `[2 3]`（默认）| 正整数的 1×2 向量

航迹确认阈值，指定为形式为 `[M N]` 的正整数 1×2 向量。如果航迹在最近 `N` 次更新中至少收到 `M` 次检测，则该航迹被确认。`M` 必须小于或等于 `N`。

- 设置 `M` 时，请考虑传感器的目标检测概率。检测概率取决于遮挡或杂波等因素。当航迹无法被确认时，您可以减小 `M`；当过多虚假检测被分配给航迹时，您可以增大 `M`。
- 设置 `N` 时，请考虑您希望跟踪器在做出确认决策之前更新的次数。例如，如果跟踪器每 0.05 秒更新一次，而您希望允许 0.5 秒来做出确认决策，请设置 `N = 10`。

#### 依赖关系

要启用此参数，请将**目标报告格式**参数设置为 `'Tracks'`。

### **P-out-of-R 删除的 P 和 R** — 航迹删除阈值 `[5 5]`（默认）| 正整数的 1×2 向量

航迹删除阈值，指定为形式为 `[P R]` 的正整数 1×2 向量。如果已确认航迹在最近 `R` 次跟踪器更新中未分配到任何检测达到 `P` 次，则该航迹被删除。`P` 必须小于或等于 `R`。

- 要缩短雷达维持航迹的时间，请减小 `R` 或增大 `P`。
- 要更长时间地维持航迹，请增大 `R` 或减小 `P`。

#### 依赖关系

要启用此参数，请将**目标报告格式**参数设置为 `'Tracks'`。

#### 随机数生成器设置

### **随机数生成** — 指定随机数生成器种子的方法 `Repeatable`（默认）| `Specify seed` | `Not repeatable`

将随机数生成器种子设置为表中选项之一的方法。

| 选项 | 描述 |
| --- | --- |
| `Repeatable` | 该模块在首次仿真时生成随机初始种子，并在所有后续仿真中重用该种子。选择此参数可从统计传感器模型生成可重复的结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 通过 **Initial seed** 参数指定您自己的随机初始种子以获得可重复的结果。 |
| `Not repeatable` | 该模块在每次仿真运行后生成新的随机初始种子。选择此参数可从统计传感器模型生成不可重复的结果。 |

### **Initial seed** — 随机数生成器种子 `0`（默认）| 小于 232 的非负整数

随机数生成器种子，指定为小于 232 的非负整数。

#### 依赖关系

要启用此参数，请将 **Random number generation** 参数设置为 `Specify seed`。

### 目标配置文件

### **目标配置文件定义** — 指定目标配置文件的方法 `From Scenario Reader block`（默认）| `MATLAB expression` | `Parameters`

指定目标配置文件的方法，为 `Parameters`、`MATLAB expression`、`From Scenario Reader block` 之一。配置文件是场景中目标的物理特性和雷达特性。

- `Parameters` — 该模块从以下参数获取目标配置文件：

  - **Unique target identifiers**
  - **Target classification identifiers**
  - **Length of target cuboids (m)**
  - **Width of target cuboids (m)**
  - **Height of target cuboids (m)**
  - **Rotational center of target cuboids (m)**
  - **Target signatures**
- `MATLAB expression` — 该模块从 **MATLAB expression for target profiles** 参数指定的 MATLAB 表达式获取目标配置文件。
- `From Scenario Reader block` — 该模块从场景读取器模块（如 Scenario Reader (Automated Driving Toolbox)）所指定的场景中获取参与者配置文件。

### **MATLAB expression for target profiles** — 目标配置文件的 MATLAB 表达式 MATLAB 结构体 | MATLAB 结构体数组 | 有效的 MATLAB 表达式

将目标配置文件的 MATLAB 表达式指定为 MATLAB 结构体、MATLAB 结构体数组或生成此类结构体或结构体数组的有效 MATLAB 表达式。

如果您的 Scenario Reader 模块从 `drivingScenario` (Automated Driving Toolbox) 对象读取数据，要直接从该对象获取参与者配置文件，请将此表达式设置为对该对象调用 `actorProfiles` (Automated Driving Toolbox) 函数。例如：`actorProfiles(scenario)`。

默认目标配置文件表达式生成一个 MATLAB 结构体，其形式如下：

```
struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4, ...
'OriginOffset',[-1.35 0 0],'RCSPattern',[10 10;10 10], ...
'RCSAzimuthAngles',[-180 180],'RCSElevationAngles',[-90 90])
```

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `MATLAB expression`。

### **Unique target identifiers** — 场景定义的目标标识符 `[]`（默认）| 正整数 | 长度为 *L* 的唯一正整数向量

将场景定义的目标标识符指定为正整数或长度为 *L* 的唯一正整数向量。*L* 必须等于输入到 **Targets (Body Frame)** 输入端口的目标数量。向量元素必须与目标的 `TargetID` 值匹配。您可以将 **Unique target identifiers** 指定为 `[]`。在这种情况下，相同的目标配置文件参数适用于所有目标。

**示例：** `[1 2]`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **目标分类标识符** — 用户自定义分类标识符 `0`（默认）| 整数 | 长度为 *L* 的整数向量

将用户自定义分类标识符指定为整数或长度为 *L* 的整数向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，必须将此参数指定为单个整数，其值适用于所有目标。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **目标长方体长度 (m)** — 目标长方体长度 `4.7`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将目标长方体长度指定为正实数标量或长度为 *L* 的正值向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，必须将此参数指定为正实数标量，其值适用于所有目标。单位为米。

**示例：** `6.3`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **目标长方体宽度 (m)** — 目标长方体宽度 `1.8`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将目标长方体宽度指定为正实数标量或长度为 *L* 的正值向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，必须将此参数指定为正实数标量，其值适用于所有目标。单位为米。

**示例：** `4.7`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **高度长方体高度 (m)** — 角色长方体高度 `1.4`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将目标长方体高度指定为正实数标量或长度为 *L* 的正值向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，必须将此参数指定为正实数标量，其值适用于所有目标。单位为米。

**示例：** `2.0`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **目标长方体旋转中心 (m)** — 目标长方体旋转中心 `{[-1.35, 0, 0]}`（默认）| 长度为 *L* 的元胞数组，包含实值 1×3 向量

将目标长方体旋转中心指定为长度为 *L* 的元胞数组，包含实值 1×3 向量。每个向量表示目标长方体旋转中心相对于目标中心的偏移量。旋转中心根据 `Dimensions` 中详述的约定定义。当 **唯一目标标识符** 为向量时，此参数为向量元胞数组，其元胞与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，必须将此参数指定为包含一个元素的元胞数组，其中包含一个偏移向量，其值适用于所有目标。单位为米。

**示例：** `{[-1.35, 0.2, 0.3]}`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **Target signatures** — 目标签名元胞数组

目标签名，指定为 `rcsSignature` 对象的元胞数组，用于指定目标的 RCS 签名。

#### 依赖关系

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。
## 所属库

Radar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2023a：Simulink 总线不显示在工作区中

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

生成雷达传感器检测和航迹

Radar Data Generator 模块从场景读取器读取目标位姿和时间，并从雷达传感器模型生成目标的检测报告和航迹报告。使用此模块可从包含目标、传感器和轨迹的场景中生成传感器数据，您可以从 Scenario Reader (Automated Driving Toolbox) 模块或 Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) 读取这些数据。

Radar Data Generator 模块可以生成带有附加随机噪声的聚类或非聚类检测，还可以生成虚警检测。您还可以从 Radar Data Generator 模块生成航迹。使用 **Target reporting format** 参数指定目标输出为聚类检测、非聚类检测还是航迹。
