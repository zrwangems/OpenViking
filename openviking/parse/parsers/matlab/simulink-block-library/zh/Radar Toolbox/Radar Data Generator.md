---
type: simulink-block
title: 'Radar Data Generator'
family: 'radar-toolbox'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Radar Toolbox'
documentation_page: 'radardatagenerator'
documentation_source_path: 'ref/radardatagenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Radar Data Generator

## 端口

### 输入

### **Targets (Body Frame)** — 目标位姿 Simulink® 总线，包含 MATLAB® 结构

平台坐标系中的目标位姿，指定为包含 MATLAB 结构的 Simulink 总线。`Targets` 输入端口可以接受 Automated Driving Toolbox™ 中 Scenario Reader (Automated Driving Toolbox) 模块的 `Actors` 输出端口的输出，或 Sensor Fusion and Tracking Toolbox™ 中 Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) 的 `Platforms` 输出端口的输出。

Scenario Reader 模块和 Tracking Scenario Reader 模块以不同格式输出位姿数据。Radar Data Generator 从任一模块读取数据。在每种情况下，数据由两个数据字段后跟一个结构体数组组成。这些结构体定义 `Platforms` 的数量或 `Actors` 的数量。`Platforms` 和 `Actors` 统称为 `Targets`。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| |  |  | | --- | --- | | **输入模块** | **字段名** | | Scenario Reader (Automated Driving Toolbox) | `NumActors` | | Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) | `NumPlatforms` | | 有效目标位姿数 | Nonnegative integer |
| **Time** | 当前仿真时间（可选）。如果缺失，则使用当前 Simulink 仿真时间。 | Real-valued scalar |
| |  |  | | --- | --- | | **输入模块** | **字段名** | | Scenario Reader (Automated Driving Toolbox) | `Actors` | | Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) | `Platforms` | | 有效目标位姿 | Array of target pose structures |

`Actors` 结构体在 Scenario Reader (Automated Driving Toolbox) 模块的输出端口中描述，`Platforms` 结构体在 Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) 模块的输出端口中描述。

### **INS** — 来自 INS 的雷达位姿 Simulink 总线，包含 MATLAB 结构

来自惯性导航系统 (INS) 的雷达位姿信息，指定为包含单个 MATLAB 结构的 Simulink 总线。该结构包含由 INS 提供的雷达平台位姿信息。然后可以使用 INS 信息估计 NED 坐标系中的目标位置。INS 是一个 `struct`，具有以下字段：

|  |  |
| --- | --- |
| **字段** | **定义** |
| `Position` | 场景坐标系中的位置，指定为实值 1×3 向量。单位为 meters。 |
| `Velocity` | 场景坐标系中的速度，指定为实值 1×3 向量。单位为 m/s。 |
| `Orientation` | 相对场景坐标系的姿态，指定为 3×3 实值旋转矩阵。该旋转从导航坐标系到当前 INS 本体坐标系。这也称为“父到子”旋转。 |

#### 依赖关系

要启用此端口，请选中 **Enable INS** 复选框。

### **Time** — 当前仿真时间，非负标量

当前仿真时间，指定为非负标量。传感器仅在对应于更新间隔整数倍的仿真时间生成报告，该更新间隔由 **Update rate (Hz)** 参数的倒数给出。单位为 seconds。

#### 依赖关系

要启用此端口，请将 **Source of target truth time** 设置为 `Input port`。

如果未启用此端口，则时间取自 `Target poses` 输入总线上的时间。如果该总线上没有时间，则使用当前 Simulink 仿真时间。

**数据类型：** `double`

### 输出

### **Clustered detections** — 聚类目标检测 Simulink 总线，包含 MATLAB 结构

聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

使用聚类检测时，该模块为每个目标输出单个检测，其中每个检测是该目标的未聚类检测的质心。

您可以将这些传感器和其他传感器的目标检测传递给跟踪器，例如 Sensor Fusion and Tracking Toolbox 中的 Global Nearest Neighbor Multi Object Tracker (Sensor Fusion and Tracking Toolbox) 模块。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测数 | Nonnegative integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 False | Boolean |
| `Detections` | 目标检测 | 目标检测结构体数组，其长度由 **Maximum number of target reports** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构体包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器的初始化函数所使用的参数 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 按 **Coordinate system** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和 `MeasurementNoise` 按球坐标系报告，该球坐标系基于传感器直角坐标系。

**`Measurement` 和 `MeasurementNoise`**

| **Coordinate System** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| Scenario | 此表显示坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |

对于 `ObjectAttributes`，此表描述用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的目标的 `ActorID` 或 `PlatformID` 标识符。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |
| `BounceTargetIndex` | 生成产生鬼影目标报告的多径反弹的目标的标识符。仅当 **HasGhosts** 为 `true` 时存在。 |
| `BouncePathIndex` | 与目标报告关联的反弹路径的索引。仅当 **HasGhosts** 为 `true` 时存在。  **Bounce-Path Index**  | BouncePathIndex | 描述 | | --- | --- | | 0 | 直接路径目标报告 | | 1 | 第一个 2 次反弹路径检测 | | 2 | 第二个 2 次反弹路径 | | 3 | 3 次反弹路径 | |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate system** 参数设置为 `Body` 时，父坐标系是平台本体。当您将 **Coordinate system** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系是传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 用于报告测量的坐标系的枚举类型。当 `Frame` 设置为 `'rectangular'` 时，检测按笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测按球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量是否包含仰角分量。 |

#### 依赖关系

要启用此端口，请将 **Target reporting format** 下拉菜单选择为 `Clustered detections`。

### **Tracks** — 目标航迹 Simulink 总线，包含 MATLAB 结构

目标航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

此表显示结构体字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 False |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of target reports** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

此表显示每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多条航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为 seconds。 |
| `Age` | 航迹已更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于已确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，以表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1-by-*K* logical 数组。*K* 是记录的最近航迹逻辑状态数。在该数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认是真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示该航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回 `true`。 |
| `ObjectAttributes` | 有关航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

该模块仅输出已确认航迹，即在航迹初始化后的前 *N* 次更新期间，模块至少为其分配 *M* 个检测的航迹。要指定 *M* 和 *N* 的值，请使用 **M and N for the M-out-of-N confirmation** 参数。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡上，将 **Target reporting format** 参数设置为 `Tracks`。

### **Detections** — 未聚类目标检测 Simulink 总线，包含 MATLAB 结构

未聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

使用未聚类检测时，该模块输出所有检测，并且一个目标可以有多个检测。

您可以将这些传感器和其他传感器的目标检测传递给跟踪器，例如 Multi-Object Tracker (Automated Driving Toolbox) 模块，并生成航迹。

该结构必须包含以下字段：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测数 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 False | Boolean |
| `Detections` | 目标检测 | 目标检测结构体数组，其长度由 **Maximum number of target reports** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构体包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器的初始化函数所使用的参数 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 按 **Coordinate system** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和 `MeasurementNoise` 按球坐标系报告，该球坐标系基于传感器直角坐标系。

**`Measurement` 和 `MeasurementNoise`**

| **Coordinate System** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| Scenario | 此表显示坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |

对于 `ObjectAttributes`，此表描述用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的目标的 `ActorID` 或 `PlatformID` 标识符。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |
| `BounceTargetIndex` | 生成产生鬼影目标报告的多径反弹的目标的标识符。仅当 **HasGhosts** 为 `true` 时存在。 |
| `BouncePathIndex` | 与目标报告关联的反弹路径的索引。仅当 **HasGhosts** 为 `true` 时存在。  **Bounce-Path Index**  | BouncePathIndex | 描述 | | --- | --- | | 0 | 直接路径目标报告 | | 1 | 第一个 2 次反弹路径检测 | | 2 | 第二个 2 次反弹路径 | | 3 | 3 次反弹路径 | |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate system** 参数设置为 `Body` 时，父坐标系是平台本体。当您将 **Coordinate system** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系是传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 用于报告测量的坐标系的枚举类型。当 `Frame` 设置为 `'rectangular'` 时，检测按笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测按球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量是否包含仰角分量。 |

#### 依赖关系

要启用此端口，请将 **Target reporting format** 参数设置为 `Detections`。

### **Configuration** — 当前传感器配置 Simulink 总线，包含 MATLAB 结构体

Configuration，返回为包含 MATLAB 结构体的 Simulink 总线。此输出可用于在对象执行期间确定哪些对象落入雷达波束内。该结构体字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumConfigurations` | 有效配置的数量 | integer |
| `Configurations` | 配置结构体 | 由 `NumConfigurations` 个配置结构体组成的数组 |

该配置结构体具有以下字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `SensorIndex` | 唯一传感器索引，返回为正整数。 |
| `IsValidTime` | 有效检测时间，返回为 `true` 或 `false`。当在由更新率指定的更新间隔之间请求检测更新时，`IsValidTime` 为 `false`。 |
| `IsScanDone` | 当传感器完成一次扫描时，`IsScanDone` 为 `true`。 |
| `FieldOfView` | 传感器的视场，返回为 2×1 正实数值向量 [`azfov`;`elfov`]。`azfov` 和 `elfov` 分别表示方位角和仰角视场。 |
| `RangeLimits` | 传感器的最小和最大距离，以米为单位，指定为形式 `[rmin,rmax]` 的 1×2 非负实数值向量。 |
| `RangeRateLimits` | 传感器的最小和最大距离变化率，以米每秒为单位，指定为形式 `[rrmin,rrmax]` 的 1×2 实数值向量。 |
| `MeasurementParameters` | 传感器测量参数，返回为结构体数组，其中包含将顶层坐标系中的位置和速度变换到当前传感器坐标系所需的坐标系变换。有关 `MeasurementParameters` 的详细信息，请参阅“测量参数”。 |

#### 依赖关系

要启用此端口，请选中 **启用雷达配置输出** 复选框。

## 参数

### 参数

#### 传感器标识

### **传感器的唯一标识符** — 唯一传感器标识符 `0` (默认) | 正整数

唯一传感器标识符，指定为正整数。使用此参数可区分多传感器系统中来自不同传感器的检测或航迹。为每个传感器指定唯一值。如果未将 **传感器的唯一标识符** 从默认值 `0` 更新，则雷达在仿真开始时返回错误。

### **更新率 (Hz)** — 传感器更新率 `10` (默认) | 正实数标量

更新率，指定为正实数标量。雷达按此值的倒数定义的间隔生成新报告。在更新间隔之间请求的任何传感器更新都不包含检测或航迹。单位为 Hz。

#### 传感器安装

### **相对于 ego 原点的平移 [ X, Y, Z ] (m)** — 雷达在平台上的安装位置 `[3.4,0,0.2]` (默认) | 形式为 `[x,y,z]` 的 1×3 实数值向量

雷达传感器在平台上的位置，指定为形式 `[x,y,z]` 的 1×3 实数值向量。此参数定义传感器相对于平台原点沿 *x* 轴、*y* 轴和 *z* 轴的坐标。单位为米。

### **相对于 ego 坐标系的旋转 [Yaw,Pitch,Roll] (deg)** — 雷达的安装旋转角 `[0 0 0]` (默认) | 形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实数值向量

雷达的安装旋转角，指定为形式 [*z*yaw *y*pitch *x*roll] 的 1×3 实数值向量。此参数定义传感器相对于平台坐标系的固有欧拉角旋转，即绕 *z* 轴、*y* 轴和 *x* 轴的旋转，其中：

- *z*yaw，或 *yaw 角*，使传感器绕平台坐标系的 *z* 轴旋转。
- *y*pitch，或 *pitch 角*，使传感器绕平台坐标系的 *y* 轴旋转。此旋转相对于 *z*yaw 旋转后得到的传感器位置。
- *x*roll，或 *roll 角*，使传感器绕平台坐标系的 *x* 轴旋转。此旋转相对于 *z*yaw 和 *y*pitch 旋转后得到的传感器位置。

这些角在分别沿 *z* 轴、*y* 轴和 *x* 轴的正方向观察时为顺时针正。单位为度。

#### 检测报告

### **启用仰角测量** — 启用雷达测量目标仰角 `off` (默认) | `on`

选中此复选框可对能够估计目标仰角的雷达传感器建模。

### **启用距离变化率测量** — 启用雷达测量目标距离变化率 `on` (默认) | `off`

选中此复选框可使雷达根据目标检测测量距离变化率。

### **为测量添加噪声** — 启用向雷达传感器测量添加噪声 `on` (默认) | `off`

选择此参数可向雷达测量添加噪声。否则，测量不包含噪声。即使清除此参数，生成检测输出的 `MeasurementNoise` 字段中报告的测量噪声协方差矩阵仍表示在选中 **为测量添加噪声** 时所添加的测量噪声。

### **启用虚假报告** — 启用创建虚假警报雷达检测 `on` (默认) | `off`

选择此参数可启用创建虚假警报雷达测量。如果清除此参数，雷达仅报告实际检测。

### **启用遮挡** — 启用视线遮挡 `on` (默认) | `off`

选择此参数可启用视线遮挡，此时雷达仅对雷达具有直接视线的对象生成检测。例如，启用此参数时，雷达不会为位于另一对象后方且被遮挡不可见的对象生成检测。

### **启用鬼影** — 启用鬼影目标 `off` (默认) | `on`

选择此参数可为在雷达信号发射和接收之间具有最多三次反射的多径传播路径生成鬼影目标。

### **目标报告最大数量** — 最大检测或航迹数量 `50` (默认) | 正整数

传感器报告的最大检测或航迹数量，指定为正整数。传感器按距传感器距离递增的顺序报告检测，直到达到此最大数量。

### **目标报告格式** — 生成的目标报告格式 **Clustered detections** (默认) | **Tracks** | **Detections**

生成的目标报告格式，指定为以下选项之一：

- **Clustered detections** — 模块以 *聚类检测* 形式生成目标报告，其中每个目标报告为单个检测，该检测是未聚类目标检测的质心。模块在 **Clustered detections** 输出端口返回聚类检测。
- **Tracks** — 模块以 *航迹* 形式生成目标报告，航迹是已经过跟踪滤波器处理的聚类检测。模块在 **Tracks** 输出端口返回聚类检测。
- **Detections** — 模块以 *未聚类检测* 形式生成目标报告，其中每个目标可以有多个检测。模块在 **Detections** 输出端口返回聚类检测。

### **坐标系** — 所报告检测的坐标系 **Body** (默认) | **Sensor rectangular** | **Sensor spherical** | **Scenario**

所报告检测的坐标系，指定为以下选项之一：

- **Body** — 检测在传感器平台的矩形本体系中报告。
- **Sensor rectangular** — 检测在传感器矩形本体坐标系中报告。
- **Sensor spherical** — 检测在以雷达传感器为中心并与雷达在平台上的方向对齐的球坐标系中报告。
- **Scenario** — 检测在矩形场景坐标系中报告。场景坐标系定义为仿真开始时的局部导航坐标系。

#### 端口设置

### **目标真值时间来源** — 输出真值时间来源 `Auto` (默认) | `Input port`

输出真值时间来源，指定为以下选项之一：

- `Auto` — 模块使用目标总线上提供的时间，如果不存在，则使用当前 Simulink 仿真时间。
- `Input port` — 模块使用模块 `Time` 输入端口上提供的时间。

### **启用 INS** — 启用 INS 输入端口 off (默认) | on

选中此参数以允许使用 `INS` 输入端口输入 INS 数据。

### **输出目标报告总线名称来源** — 输出目标报告总线名称来源 `Auto` (默认) | `Property`

输出目标报告总线名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建总线名称。
- `Property` — 通过使用 **指定输出目标报告总线名称** 参数来指定总线名称。

此总线包含 Clustered detections、Tracks 或 Detections 输出端口数据。

### **指定输出目标报告总线名称** — 目标报告输出总线名称 `BusRadarDataGenerator` (默认) | 有效总线名称

要在输出端口中返回的目标报告总线名称，指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **输出目标报告总线名称来源** 参数设置为 `Property`。

### **启用雷达配置输出** — 启用雷达配置输出 `off` (默认) | `on`

启用 `Configuration` 输出端口。

### **输出 config 总线名称来源** — 输出 config 总线名称来源 `Auto` (默认) | `Property`

输出 `config` 总线名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建总线名称。
- `Property` — 通过使用 **指定输出 config 总线名称** 参数来指定总线名称。

### **指定输出 config 总线名称** — 目标报告输出总线名称 `BusRadarDataGeneratorConfig` (默认) | 有效总线名称

指定输出端口中返回的 `config` 总线名称。

#### 依赖关系

要启用此参数，请将 **输出 config 总线名称来源** 参数设置为 `Property`。

### 测量

#### 分辨率设置

### **方位角分辨率 (deg)** — 雷达的方位角分辨率 `4` (默认) | 正实数标量

雷达的方位角分辨率，指定为正标量。*方位角分辨率* 定义了雷达能够区分两个目标的最小方位角间隔。方位角分辨率通常是雷达方位角波束宽度的 3 dB 下降点。单位为度。

### **仰角分辨率 (deg)** — 雷达的仰角分辨率 `5` (默认) | 正实数标量

雷达的仰角分辨率，指定为正标量。*仰角分辨率* 定义了雷达能够区分两个目标的最小仰角间隔。仰角分辨率通常是雷达仰角波束宽度的 3 dB 下降点。单位为度。

#### 依赖关系

要启用此参数，请选中 **启用仰角测量** 复选框。

### **距离分辨率 (m)** — 雷达的距离分辨率 `2.5` (默认) | 正实数标量

雷达的距离分辨率，以米为单位，指定为正实数标量。*距离分辨率* 定义了雷达能够区分两个目标的最小距离间隔。单位为米。

### **距离变化率分辨率 (m/s)** — 雷达的距离变化率分辨率 `0.5` (默认) | 正实数标量

雷达的距离变化率分辨率，指定为正实数标量。*距离变化率分辨率* 定义了雷达能够区分两个目标的最小距离变化率间隔。单位为米每秒。

#### 依赖关系

要启用此参数，请在 **参数** 选项卡上选中 **启用距离变化率测量** 复选框。

#### 偏置设置

### **方位角偏置比例** — 雷达的方位角偏置比例 `0.1` (默认) | 非负标量

雷达的方位角偏置比例，指定为非负标量。*方位角偏置* 表示为 **方位角分辨率 (deg)** 参数中指定的方位角分辨率的比例。此值设置雷达方位角精度的下界，并且无量纲。

### **仰角偏置比例** — 雷达的仰角偏置比例 `0.1` (默认) | 非负标量

雷达的仰角偏置比例，指定为非负标量。*仰角偏置* 表示为 **仰角分辨率 (deg)** 参数中指定的仰角分辨率的比例。此值设置雷达仰角精度的下界，并且无量纲。

#### 依赖关系

要启用此参数，请选中 **启用仰角测量** 复选框。

### **距离偏置比例** — 距离偏置比例 `0.05` (默认) | 非负标量

雷达的距离偏置比例，指定为非负标量。距离偏置表示为 **距离分辨率 (m)** 属性指定的距离分辨率的比例。此属性设置雷达距离精度的下界，并且无量纲。

### **距离变化率偏置比例** — 距离变化率偏置比例 `0.05` (默认) | 非负标量

雷达的距离变化率偏置比例，指定为非负标量。距离变化率偏置表示为 **距离变化率分辨率 (m/s)** 参数指定的距离变化率分辨率的比例。此属性设置雷达距离变化率精度的下界，并且无量纲。

#### 依赖关系

要启用此参数，请选中 **启用距离变化率测量** 复选框。

#### 检测器设置

### **总角度视场 [AZ, EL] (deg)** — 雷达的角度视场 `[20 5]` (默认) | 形式为 `[azfov,elfov]` 的 1×2 正实数值向量

雷达的角度视场，指定为形式 `[azfov elfov]` 的 1×2 正实数值向量。视场定义传感器覆盖的总角度范围。方位角视场 `azfov` 必须位于区间 (0, 360] 内。仰角视场 `elfov` 必须位于区间 (0, 180] 内。单位为度

### **距离限值 [MIN, MAX] (m)** — 雷达的最小和最大距离 `[0 150]` (默认) | 形式为 `[min max]` 的 1×2 非负实数值向量

雷达的最小和最大距离，指定为形式 `[min max]` 的 1×2 非负实数值向量。雷达不会检测此范围之外的目标。最大距离 `max` 必须大于最小距离 `min`。单位为米。

### **距离变化率限值 [MIN, MAX] (m/s)** — 雷达的最小和最大距离变化率 (m/s) `[-100 100]` (默认) | 形式为 `[min max]` 的 1×2 实数值向量

雷达的最小和最大距离变化率，指定为形式 `[min max]` 的 1×2 实数值向量。雷达不会检测此距离变化率范围之外的目标。最大距离变化率 `max` 必须大于最小距离变化率 `min`。单位为米每秒。

#### 依赖关系

要启用此参数，请选中 **启用距离变化率测量** 复选框。

### **检测概率** — 检测目标的概率 `0.9` (默认) | 范围 (0, 1] 内的标量

检测目标的概率，指定为范围 (0, 1] 内的标量。此量定义检测具有特定雷达横截面积的目标的概率，该雷达横截面积由 **Reference target RCS (dBsm)** 参数指定，对应的参考检测距离由 **Reference target range (m)** 参数指定。该量为无量纲量。

### **False alarm rate** — 虚警报告率 `1e-06` (默认) | positive real scalar in range [10–7, 10–3]

每个雷达分辨单元内的虚警报告率，指定为 positive real scalar，范围为 [10–7, 10–3]。模块根据 **Azimuth resolution (deg)** 和 **Range resolution (m)** 参数确定分辨单元，并且在启用时，还根据 **Elevation resolution (deg)** 和 **Range rate resolution (m/s)** 参数确定。单位为无量纲。

### **Reference target range (m)** — 给定检测概率的参考距离 `100` (默认) | positive real scalar

给定检测概率和给定参考雷达散射截面 (RCS) 的参考距离，指定为 positive real scalar。*参考距离* 是这样一个距离：具有由 **Reference target RCS (dBsm)** 参数指定的雷达散射截面的目标，以由 **Detection probability** 参数指定的检测概率被检测到。单位为 meters。

### **Reference target RCS (dBsm)** — 给定检测概率的参考雷达散射截面 `0` (默认) | real scalar

给定检测概率和参考距离的参考雷达散射截面 (RCS)，指定为 real scalar。*参考 RCS* 是这样一个 RCS 值：在指定的 **Reference target range (m)** 参数值处，目标以由 **Detection probability** 参数指定的概率被检测到。值以 dBsm 表示。

### **Center frequency (Hz)** — 雷达频带的中心频率 `77e9` (默认) | positive real scalar

雷达频带的中心频率，指定为 positive scalar。单位为 Hz。

#### 跟踪器设置

### **Filter initialization function name** — 卡尔曼滤波器初始化函数 `initcvekf` (默认) | function handle

卡尔曼滤波器初始化函数，指定为有效卡尔曼滤波器初始化函数名称的 character vector 或 string scalar。

下表显示了可用于指定 **Filter initialization function name** 的初始化函数。

| 初始化函数 | 函数定义 |
| --- | --- |
| `initcaabf` | 初始化常加速度 alpha-beta 卡尔曼滤波器 |
| `initcvabf` | 初始化常速度 alpha-beta 卡尔曼滤波器 |
| `initcakf` | 初始化常加速度线性卡尔曼滤波器。 |
| `initcvkf` | 初始化常速度线性卡尔曼滤波器。 |
| `initcaekf` | 初始化常加速度扩展卡尔曼滤波器。 |
| `initctekf` | 初始化常转弯率扩展卡尔曼滤波器。 |
| `initcvekf` | 初始化常速度扩展卡尔曼滤波器。 |
| `initcaukf` | 初始化常加速度无迹卡尔曼滤波器。 |
| `initctukf` | 初始化常转弯率无迹卡尔曼滤波器。 |
| `initcvukf` | 初始化常速度无迹卡尔曼滤波器。 |

你也可以编写自己的初始化函数。该函数必须具有以下语法：

    filter = filterInitializationFcn(detection)

此函数的输入是检测报告，类似于由 `objectDetection` 对象创建的检测报告。此函数的输出必须是跟踪滤波器对象，例如 `trackingKF`、`trackingEKF`、`trackingUKF` 或 `trackingABF`。

为指导你编写此函数，你可以在 MATLAB 中查看所提供函数的详细信息。例如：

    type initcvekf

#### 依赖项

要启用此参数，请将 **Target reporting format** 参数设置为 `'Tracks'`。

### **M and N for the M-out-of-N confirmation** — 航迹确认阈值 `[2 3]` (默认) | 1-by-2 vector of positive integers

航迹确认阈值，指定为形式为 `[M N]` 的 1-by-2 vector of positive integers。如果一条航迹在最近 `N` 次更新中接收到至少 `M` 次检测，则该航迹被确认。`M` 必须小于或等于 `N`。

- 设置 `M` 时，请考虑传感器对目标的检测概率。检测概率取决于遮挡或杂波等因素。当航迹无法确认时，可以减小 `M`；当过多虚警检测被分配给航迹时，可以增大 `M`。
- 设置 `N` 时，请考虑你希望跟踪器在做出确认决策前更新的次数。例如，如果跟踪器每 0.05 秒更新一次，并且你希望允许 0.5 秒来做出确认决策，请设置 `N = 10`。

#### 依赖项

要启用此参数，请将 **Target reporting format** 参数设置为 `'Tracks'`。

### **P and R for the P-out-of-R deletion** — 航迹删除阈值 `[5 5]` (默认) | 1-by-2 vector of positive integers

航迹删除阈值，指定为形式为 `[P R]` 的 1-by-2 vector of positive integers。如果在最近 `R` 次跟踪器更新中，一条已确认航迹有 `P` 次未分配给任何检测，则该航迹被删除。`P` 必须小于或等于 `R`。

- 要缩短雷达维持航迹的时间，减小 `R` 或增大 `P`。
- 要更长时间维持航迹，增大 `R` 或减小 `P`。

#### 依赖项

要启用此参数，请将 **Target reporting format** 参数设置为 `'Tracks'`。

#### 随机数生成器设置

### **Random number generation** — 指定随机数生成器种子的方法 `Repeatable` (默认) | `Specify seed` | `Not repeatable`

将随机数生成器种子设置为表中选项之一。

| 选项 | 描述 |
| --- | --- |
| `Repeatable` | 模块在首次仿真时生成随机初始种子，并在所有后续仿真中重用此种子。选择此参数可从统计传感器模型生成可重复结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 通过 **Initial seed** 参数指定你自己的随机初始种子，以获得可重复结果。 |
| `Not repeatable` | 模块在每次仿真运行后生成新的随机初始种子。选择此参数可从统计传感器模型生成不可重复结果。 |

### **Initial seed** — 随机数生成器种子 `0` (默认) | nonnegative integer less than 232

随机数生成器种子，指定为小于 232 的 nonnegative integer。

#### 依赖项

要启用此参数，请将 **Random number generation** 参数设置为 `Specify seed`。

### 目标配置文件

### **Target profiles definition** — 指定目标 profiles 的方法 `From Scenario Reader block` (默认) | `MATLAB expression` | `Parameters`

将目标 profiles 指定为 `Parameters`、`MATLAB expression`、`From Scenario Reader block` 之一。Profiles 是场景中目标的物理特性和雷达特性。

- `Parameters` — 模块从以下参数获取目标 profiles：

  - **Unique target identifiers**
  - **Target classification identifiers**
  - **Length of target cuboids (m)**
  - **Width of target cuboids (m)**
  - **Height of target cuboids (m)**
  - **Rotational center of target cuboids (m)**
  - **Target signatures**
- `MATLAB expression` — 模块从 **MATLAB expression for target profiles** 参数指定的 MATLAB 表达式获取目标 profiles。
- `From Scenario Reader block` — 模块从由场景读取器模块（如 Scenario Reader (Automated Driving Toolbox)）指定的场景中获取 actor profiles。

### **MATLAB expression for target profiles** — 目标 profiles 的 MATLAB 表达式 MATLAB structure | MATLAB structure array | valid MATLAB expression

将目标 profiles 的 MATLAB 表达式指定为 MATLAB structure、MATLAB structure array，或生成此类 structure 或 structure array 的有效 MATLAB 表达式。

如果你的 Scenario Reader 模块从 `drivingScenario` (Automated Driving Toolbox) 对象读取数据，要直接从此对象获取 actor profiles，请将此表达式设置为对该对象调用 `actorProfiles` (Automated Driving Toolbox) 函数。例如：`actorProfiles(scenario)`。

默认目标 profile 表达式生成一个 MATLAB structure，并具有以下形式：

    struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4, ...
    'OriginOffset',[-1.35 0 0],'RCSPattern',[10 10;10 10], ...
    'RCSAzimuthAngles',[-180 180],'RCSElevationAngles',[-90 90])

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `MATLAB expression`。

### **Unique target identifiers** — 场景定义的目标标识符 `[]` (默认) | positive integer | length-*L* vector of unique positive integers

将场景定义的目标标识符指定为 positive integer 或 length-*L* vector of unique positive integers。*L* 必须等于输入到 **Targets (Body Frame)** 输入端口的目 标数量。向量元素必须与目标的 `TargetID` 值匹配。你可以将 **Unique target identifiers** 指定为 `[]`。在这种情况下，相同的目标 profile 参数适用于所有目标。

**示例：** `[1 2]`

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Target classification identifiers** — 用户定义的分类标识符 `0` (默认) | integer | length-*L* vector of integers

将用户定义的分类标识符指定为 integer 或 length-*L* vector of integers。当 **Unique target identifiers** 是向量时，此参数是与 **Unique target identifiers** 中目标一一对应的相同长度向量。当 **Unique target identifiers** 为空 `[]` 时，必须将此参数指定为一个 integer，其值适用于所有目标。

**示例：** `2`

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Length of target cuboids (m)** — 目标长方体的长度 `4.7` (默认) | positive real scalar | length-*L* vector of positive values

将目标长方体的长度指定为 positive real scalar 或 length-*L* vector of positive values。当 **Unique target identifiers** 是向量时，此参数是与 **Unique target identifiers** 中目标一一对应的相同长度向量。当 **Unique target identifiers** 为空 `[]` 时，必须将此参数指定为一个 positive real scalar，其值适用于所有目标。单位为 meters。

**示例：** `6.3`

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Width of target cuboids (m)** — 目标长方体的宽度 `1.8` (默认) | positive real scalar | length-*L* vector of positive values

将目标长方体的宽度指定为 positive real scalar 或 length-*L* vector of positive values。当 **Unique target identifiers** 是向量时，此参数是与 **Unique target identifiers** 中目标一一对应的相同长度向量。当 **Unique target identifiers** 为空 `[]` 时，必须将此参数指定为一个 positive real scalar，其值适用于所有目标。单位为 meters。

**示例：** `4.7`

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Height of heights cuboids (m)** — actor 长方体的高度 `1.4` (默认) | positive real scalar | length-*L* vector of positive values

将目标长方体的高度指定为 positive real scalar 或 length-*L* vector of positive values。当 **Unique target identifiers** 是向量时，此参数是与 **Unique target identifiers** 中目标一一对应的相同长度向量。当 **Unique target identifiers** 为空 `[]` 时，必须将此参数指定为一个 positive real scalar，其值适用于所有目标。单位为 meters。

**示例：** `2.0`

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Rotational center of target cuboids (m)** — 目标长方体的旋转中心 `{[-1.35, 0, 0]}` (默认) | length-*L* cell array of real-valued 1-by-3 vectors

将目标长方体的旋转中心指定为 length-*L* cell array of real-valued 1-by-3 vectors。每个向量表示目标长方体的旋转中心相对于目标中心的偏移。旋转中心根据 `Dimensions` 中详述的约定定义。当 **Unique target identifiers** 是向量时，此参数是与 **Unique target identifiers** 中目标一一对应的向量 cell array。当 **Unique target identifiers** 为空 `[]` 时，必须将此参数指定为包含一个偏移向量的 cell array，其值适用于所有目标。单位为 meters。

**示例：** `{[-1.35, 0.2, 0.3]}`

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Target signatures** — 目标签名 cell array

目标签名，指定为 `rcsSignature` 对象的 cell array，这些对象指定目标的 RCS 签名。

#### 依赖项

#### 依赖项

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

## 所属库

Radar Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2023a: Simulink 总线不在工作区中显示

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

生成雷达传感器检测和航迹

Radar Data Generator 模块从场景读取器读取目标位姿和时间，并根据雷达传感器模型生成目标的检测报告和航迹报告。使用此模块从包含目标、传感器和轨迹的场景生成传感器数据，你可以从 Scenario Reader (Automated Driving Toolbox) 模块或 Tracking Scenario Reader (Sensor Fusion and Tracking Toolbox) 读取这些数据。

Radar Data Generator 模块可以生成带有附加随机噪声的聚类或非聚类检测，还可以生成虚警检测。你也可以从 Radar Data Generator 模块生成航迹。使用 **Target reporting format** 参数指定目标输出为聚类检测、非聚类检测还是航迹。
