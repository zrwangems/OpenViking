---
type: simulink-block
title: 'Fusion Radar Sensor'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Tracking Scenario and Sensor Models'
documentation_page: 'fusionradarsensor'
documentation_source_path: 'ref/fusionradarsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Fusion Radar Sensor

## 端口

### 输入

### **Platforms** — 目标平台位姿 Simulink® 总线，包含 MATLAB® 结构体

以参考平台坐标系表示的目标平台位姿，指定为包含 MATLAB 结构体的 Simulink 总线。参考平台是雷达传感器的安装平台。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。
该结构体具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `NumPlatforms` | 平台数量，指定为非负整数。 |
| `Platforms` | 平台位姿，指定为平台位姿结构体数组。该模块仅读取 `NumPlatforms` 中指定的平台数量对应的平台位姿。 |

每个平台位姿结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `PlatformID` | 目标平台的唯一标识符，指定为正整数。 |
| `ClassID` | 用于对目标平台类型进行分类的用户定义整数，指定为非负整数。`0` 保留用于未分类的平台类型，为默认值。 |
| `Position` | 目标平台在参考平台机体坐标系中的位置，指定为实值 1×3 向量。单位为米。 |
| `Velocity` | 目标平台在参考平台机体坐标系中的速度，指定为实值 1×3 向量。单位为米每秒。 |
| `Acceleration` | 目标平台在参考平台机体坐标系中的加速度，指定为实值 1×3 向量。单位为米每二次方秒。 |
| `Orientation` | 目标平台相对于参考平台机体坐标系的姿态，指定为 3×3 旋转矩阵。姿态定义了从平台坐标系到目标机体坐标系的坐标系旋转。 |
| `AngularVelocity` | 目标平台在参考平台机体坐标系中的角速度，指定为实值 1×3 向量。向量的大小定义了角速率。单位为度每秒。默认值为 `[0 0 0]`。 |

您可以使用 Tracking Scenario Reader 模块生成以场景坐标系表示的目标平台位姿。然后使用 Scenario To Platform 模块获取参考平台坐标系中的目标平台位姿。

### **INS** — 来自 INS 的雷达参考平台位姿 Simulink 总线，包含 MATLAB 结构体

来自惯性导航系统（INS）的雷达参考平台位姿信息，指定为包含 MATLAB 结构体的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。
该结构体包含 INS 提供的雷达平台位姿信息。
INS 结构体具有以下字段。

|  |  |
| --- | --- |
| **字段** | **定义** |
| `Position` | 平台在场景坐标系中的位置，指定为实值 1×3 向量。单位为米。 |
| `Velocity` | 平台在场景坐标系中的速度，指定为实值 1×3 向量。单位为 m/s。 |
| `Orientation` | 平台机体坐标系相对于场景坐标系的姿态，指定为 3×3 实值旋转矩阵。该旋转是从场景坐标系到平台机体坐标系的旋转。这也称为父到子旋转。 |

#### 依赖关系

要启用此端口，请选中 **Enable INS** 复选框。

### **Time** — 当前仿真时间 非负标量

当前仿真时间，指定为非负标量。请注意，传感器仅在对应于更新间隔整数倍的仿真时间生成报告，更新间隔为指定 **Update rate (Hz)** 参数的倒数。单位为秒。

#### 依赖关系

要启用此端口，请将 **Source of target truth time** 参数设置为 `Input port`。

如果未启用此端口，则该模块使用当前 Simulink 仿真时间。

**数据类型：** `double`
### 输出

### **Clustered Detections** — 包含 MATLAB 结构的 Simulink 总线，用于聚类后的目标检测

聚类后的目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于聚类检测，该模块为每个目标输出单个检测，其中每个检测是该目标的未聚类检测的质心。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | 非负整数 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | 布尔值 |
| `Detections` | 目标检测 | 目标检测结构数组，其长度由 **Maximum number of target reports** 参数设置。其中只有前 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下字段。

| 字段 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器的初始化函数所使用的参数 |

- 对于直角坐标，该模块在由 **Coordinate system** 参数指定的直角坐标系中报告 `Measurement` 和 `MeasurementNoise`。
- 对于球坐标，该模块在由 **Coordinate system** 参数指定的球坐标系中报告 `Measurement` 和 `MeasurementNoise`。

**`Measurement` 和 `MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| Scenario | 此表显示了坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示了坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |  `az` 是方位角，`el` 是仰角，`rng` 是距离，`rr` 是距离变化率。角度的单位是度。 |

`ObjectAttributes` 结构包含以下字段。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 与该检测对应的目标平台的 `PlatformID`，返回为正整数。对于虚警，该值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

`MeasurementParameters` 字段可以包含至少一个测量参数结构，表示从平台机体坐标系到传感器视角坐标系的变换。如果您通过 **INS** 输入端口指定 INS 信息，并且还将 **Coordinate system** 参数指定为 `scenario`，则 `MeasurementParameters` 字段还包含一个额外的测量参数结构，表示从场景坐标系到参考平台机体坐标系的变换。每个测量参数结构包含以下字段。

|  |  |
| --- | --- |
| **字段** | **描述** |
| `Frame` | 枚举类型，指示用于报告测量的坐标系。当使用矩形坐标系报告检测结果时，`Frame` 设置为 `'rectangular'`。当使用球坐标系报告检测结果时，`Frame` 设置为 `'spherical'`。 |
| `OriginPosition` | 子坐标系原点相对于父坐标系的位置偏移，表示为 3×1 向量。 |
| `OriginVelocity` | 子坐标系原点相对于父坐标系的速度偏移，表示为 3×1 向量。 |
| `Orientation` | 3×3 实值正交坐标系旋转矩阵。旋转方向取决于 `IsParentTochild` 字段。 |
| `IsParentToChild` | 逻辑标量，指示 `Orientation` 是否执行从父坐标系到子坐标系的坐标系旋转。如果为 `false`，则 `Orientation` 执行从子坐标系到父坐标系的坐标系旋转。 |
| `HasElevation` | 逻辑标量，指示测量中是否包含仰角。对于在矩形坐标系中报告的测量，如果 `HasElevation` 为 `false`，则测量报告假定仰角为 0 度。 |
| `HasAzimuth` | 逻辑标量，指示测量中是否包含方位角。 |
| `HasRange` | 逻辑标量，指示测量中是否包含距离。 |
| `HasVelocity` | 逻辑标量，指示报告的检测结果是否包含速度测量。  - 对于在矩形坐标系中报告的测量，如果   `HasVelocity` 为   `false`，则测量报告为   `[x y z]`。如果   `HasVelocity` 为   `true`，则测量报告为   `[x y z vx vy vz]`。 - 对于在球坐标系中报告的测量，如果   `HasVelocity` 为   `false`，则测量报告为   `[az el rng]`。如果   `HasVelocity` 为   `true`，则测量报告为   `[az;el;rng;rr]`。 |

#### 依赖关系

要启用此端口，请将 **目标报告格式** 参数设置为 `Clustered detections`。

### **Tracks** — 包含 MATLAB 结构的 Simulink 总线对象航迹

对象航迹，以包含 MATLAB 结构的 Simulink 总线形式返回。请参阅 Create Nonvirtual Buses (Simulink)。

每个结构具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `IsValidTime` | 当您在模块调用间隔之间请求更新时为 False |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of target reports** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

下表显示了每个航迹结构的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为秒。 |
| `Age` | 航迹被更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 状态估计误差的不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于已确认的航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，以 1×*K* 逻辑数组形式返回。*K* 是记录的最新逻辑航迹状态的数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下被更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

该模块仅输出已确认的航迹，即在航迹初始化后的前 *N* 次更新中至少被分配 *M* 次检测的航迹。要指定 *M* 和 *N* 的值，请使用 **M and N for the M-out-of-N confirmation** 参数。

#### 依赖关系

要启用此端口，请将 **Target reporting format** 参数设置为 `Tracks`。

### **Detections** — 包含 MATLAB 结构的 Simulink 总线，用于未聚类目标检测

未聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于未聚类检测，该模块输出所有检测结果，一个目标可以有多个检测。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | 非负整数 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | 布尔值 |
| `Detections` | 目标检测 | 目标检测结构数组，其长度由 **Maximum number of target reports** 参数设置。其中只有前 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下字段。

| 字段 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数使用的参数 |

- 对于直角坐标，该模块在由 **Coordinate system** 参数指定的直角坐标系中报告 `Measurement` 和 `MeasurementNoise`。
- 对于球坐标，该模块在由 **Coordinate system** 参数指定的球坐标系中报告 `Measurement` 和 `MeasurementNoise`。

**`Measurement` 和 `MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| Scenario | 此表显示了坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示了坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |  `az` 是方位角，`el` 是仰角，`rng` 是距离，`rr` 是距离变化率。角度单位为度。 |

`ObjectAttributes` 结构具有以下字段。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 与检测对应的目标平台的 `PlatformID`，返回为正整数。对于虚警，该值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

`MeasurementParameters` 字段可以包含至少一个测量参数结构，表示从平台机体坐标系到传感器视线角坐标系的变换。如果您通过 **INS** 输入端口指定 INS 信息，并且还将 **Coordinate system** 参数指定为 `scenario`，则 `MeasurementParameters` 字段还包含一个额外的测量参数结构，表示从场景坐标系到参考平台机体坐标系的变换。每个测量参数结构具有以下字段。

|  |  |
| --- | --- |
| **字段** | **描述** |
| `Frame` | 枚举类型，指示用于报告测量值的坐标系。当检测结果使用矩形坐标系报告时，`Frame` 设置为 `'rectangular'`。当检测结果使用球坐标系报告时，`Frame` 设置为 `'spherical'`。 |
| `OriginPosition` | 子坐标系原点相对于父坐标系的位置偏移，表示为 3×1 向量。 |
| `OriginVelocity` | 子坐标系原点相对于父坐标系的速度偏移，表示为 3×1 向量。 |
| `Orientation` | 3×3 实值正交坐标系旋转矩阵。旋转方向取决于 `IsParentTochild` 字段。 |
| `IsParentToChild` | 逻辑标量，指示 `Orientation` 是否执行从父坐标系到子坐标系的坐标系旋转。如果为 `false`，则 `Orientation` 执行从子坐标系到父坐标系的坐标系旋转。 |
| `HasElevation` | 逻辑标量，指示测量中是否包含仰角。对于在矩形坐标系中报告的测量值，如果 `HasElevation` 为 `false`，则测量值按仰角 0 度报告。 |
| `HasAzimuth` | 逻辑标量，指示测量中是否包含方位角。 |
| `HasRange` | 逻辑标量，指示测量中是否包含距离。 |
| `HasVelocity` | 逻辑标量，指示报告的检测结果是否包含速度测量值。  - 对于在矩形坐标系中报告的测量值，如果   `HasVelocity` 为   `false`，则测量值报告为   `[x y z]`。如果   `HasVelocity` 为   `true`，则测量值报告为   `[x y z vx vy vz]`。 - 对于在球坐标系中报告的测量值，如果   `HasVelocity` 为   `false`，则测量值报告为   `[az el rng]`。如果   `HasVelocity` 为   `true`，则测量值报告为   `[az;el;rng;rr]`。 |

#### 依赖关系

要启用此端口，请将 **Target reporting format** 参数设置为 `Detections`。

### **Configuration** — 当前传感器配置 包含 MATLAB 结构的 Simulink 总线

配置，返回为包含 MATLAB 结构的 Simulink 总线。您可以使用此端口在对象执行期间确定落入雷达波束内的对象。该结构具有以下字段：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumConfigurations` | 有效配置的数量 | 整数 |
| `Configurations` | 配置结构 | `NumConfigurations` 个配置结构的数组 |

配置结构具有以下字段。

|  |  |
| --- | --- |
| **字段** | **描述** |
| `SensorIndex` | 唯一传感器索引，返回为正整数。 |
| `IsValidTime` | 有效检测时间，返回为 `true` 或 `false`。当在更新速率指定的更新间隔之间请求检测更新时，`IsValidTime` 为 `false`。 |
| `IsScanDone` | 当传感器完成一次扫描时，`IsScanDone` 为 `true`。 |
| `FieldOfView` | 传感器的视场，返回为 2×1 正实数值向量，[`azfov`;`elfov`]。`azfov` 和 `elfov` 分别表示方位角和仰角方向的视场。单位为度。 |
| `RangeLimits` | 传感器的最小和最大距离，以米为单位，指定为 1×2 非负实值向量，形式为 `[rmin,rmax]`。单位为米。 |
| `RangeRateLimits` | 传感器的最小和最大距离变化率，以米每秒为单位，指定为 1×2 实值向量，形式为 `[rrmin,rrmax]`。单位为米。 |
| `MeasurementParameters` | 传感器测量参数，返回为结构数组，包含将顶层坐标系中的位置和速度变换到当前传感器坐标系所需的坐标系变换。有关 `MeasurementParameters` 的详细信息，请参阅 `Measurement Parameters`。 |

#### 依赖关系

要启用此端口，请选中 **Enable radar configuration output** 复选框。

## 参数

### 参数

#### 传感器标识

### **Unique identifier of sensor** — 唯一传感器标识符 `0`（默认）| 正整数

唯一传感器标识符，指定为正整数。使用此参数区分多传感器系统中来自不同传感器的检测或航迹。为每个传感器指定一个唯一值。如果您未将 **Unique identifier of sensor** 从默认值 `0` 更新，则雷达在仿真开始时返回错误。

### **Update rate (Hz)** — 传感器更新率 `10`（默认）| 正实数标量

传感器更新率，指定为正实数标量。雷达按此值的倒数所定义的间隔生成新报告。例如，如果更新率为 `10` Hz，则传感器每 0.1 秒生成一次检测。更新间隔之间的传感器更新请求不包含任何检测或航迹。单位为 Hz。

#### 传感器安装

### **Translation [ X, Y, Z ] relative to platform origin (m)** — 雷达在平台上的安装位置 `[0,0,0]`（默认）| 形式为 `[x,y,z]` 的 1×3 实值向量

雷达在参考平台上的传感器位置，指定为形式为 `[x,y,z]` 的 1×3 实值向量。此参数定义传感器相对于平台原点沿 *x* 轴、*y* 轴和 *z* 轴的坐标。单位为米。

### **Rotation [Yaw,Pitch,Roll] relative to platform's frame (deg)** — 雷达的安装角度 `[0 0 0]`（默认）| 形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量

雷达的安装角度，指定为形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量。此参数定义传感器相对于平台坐标系的固有欧拉角旋转，即绕 *z* 轴、*y* 轴和 *x* 轴的旋转，其中：

- *z*yaw，即 *yaw angle*，使传感器绕平台坐标系的 *z* 轴旋转。
- *y*pitch，即 *pitch angle*，使传感器绕平台坐标系的 *y* 轴旋转。此旋转相对于由 *z*yaw 旋转产生的传感器位置。
- *x*roll，即 *roll angle*，使传感器绕平台坐标系的 *x* 轴旋转。此旋转相对于由 *z*yaw 和 *y*pitch 旋转产生的传感器位置。

单位为度。

#### 检测报告

### **Enable elevation angle measurements** — 使雷达能够测量目标仰角 `off`（默认）| `on`

选中此复选框可对能够测量目标仰角的雷达传感器进行建模。

### **Enable range rate measurements** — 使雷达能够测量目标距离变化率 `off`（默认）| `on`

选中此复选框可使雷达能够从目标检测中测量距离变化率。

### **Add noise to measurements** — 启用向雷达传感器测量值添加噪声 `on`（默认）| `off`

选中此参数可向雷达测量值添加噪声。否则，测量值不含噪声。即使您清除此参数，生成的检测输出中 `MeasurementNoise` 字段所报告的测量噪声协方差矩阵仍表示在选中 **Add noise to measurements** 时所添加的测量噪声。

### **Enable false reports** — 启用创建虚假警报雷达检测 `on`（默认）| `off`

选中此参数可启用创建虚假警报雷达测量值。如果您清除此参数，则雷达仅报告实际检测。

### **Enable occlusion** — 启用视线遮挡 `on`（默认）| `off`

选择此参数以启用来自扩展目标的视线遮挡。如果启用此参数，传感器会建模两种类型的遮挡：自遮挡和目标间遮挡。自遮挡发生在扩展目标的一侧遮挡另一侧时。目标间遮挡发生在一个扩展目标位于另一个扩展目标或点目标的视线中时。扩展目标和点目标都可能被扩展目标遮挡，但点目标不能遮挡另一个点目标或扩展目标。

### **Maximum number of target reports** — 最大检测数或航迹数 `100`（默认）| 正整数

传感器报告的最大检测数或航迹数，指定为正整数。传感器按距传感器距离递增的顺序报告检测，直到达到此最大数量。

### **Target reporting format** — 生成目标报告的格式 `Clustered detections`（默认）| `Tracks` | `Detections`

生成目标报告的格式，指定为以下选项之一：

- **Clustered detections** — 该模块将目标报告生成为*聚类检测*，其中每个目标报告为单个检测，该检测是未聚类目标检测的质心。该模块在 **Clustered detections** 输出端口返回聚类检测。
- **Tracks** — 该模块将目标报告生成为*航迹*，即已经过跟踪器处理的聚类检测。该模块在 **Tracks** 输出端口返回航迹。
- **Detections** — 该模块将目标报告生成为*未聚类检测*，其中每个目标可以有多个检测。该模块在 **Detections** 输出端口返回聚类检测。

### **Coordinate system** — 所报告检测的坐标系 `Body`（默认）| `Sensor rectangular` | `Sensor spherical` | `Scenario`

所报告检测的坐标系，指定为以下选项之一：

- `Body` — 检测在传感器平台的矩形机体坐标系中报告。
- `Sensor rectangular` — 检测在传感器矩形机体坐标系中报告。
- `Sensor spherical` — 检测在以雷达传感器为中心并与平台上雷达朝向对齐的球坐标系中报告。
- `Scenario` — 检测在矩形场景坐标系中报告。要使用此选项，必须指定 **INS** 输入端口。

#### Inputs and Outputs

### **Source of target truth time** — 目标真值时间来源 `Auto`（默认）| `Input port`

目标真值时间来源，指定为以下选项之一：

- `Auto` — 该模块使用当前 Simulink 仿真时间。
- `Input port` — 该模块使用该模块 `Time` 输入端口提供的时间。

### **Enable INS** — 启用 INS 输入端口 `off`（默认）| `on`

选择此参数以允许使用 **INS** 输入端口输入 INS 数据。

### **Source of output target report bus name** — 输出目标报告总线名称来源 `Auto`（默认）| `Property`

输出目标报告总线名称来源，指定为以下选项之一：

- `Auto` — 该模块自动创建总线名称。
- `Property` — 通过 **Specify an output target report bus name** 参数指定总线名称。

此总线名称适用于 **Clustered detections**、**Tracks** 和 **Detections** 输出端口。

### **Specify an output target report bus name** — 目标报告输出总线名称 `BusFusionRadarSensor`（默认）| 有效总线名称

要在输出端口中返回的目标报告总线名称，指定为有效总线名称。此总线名称适用于 **Clustered detections**、**Tracks** 和 **Detections** 输出端口。

#### 依赖关系

要启用此参数，请将**输出目标报告总线名称来源**参数设置为 `Property`。

### **启用雷达配置输出** — 启用雷达配置输出 `off`（默认）| `on`

启用 **Configuration** 输出端口。

### **输出配置总线名称来源** — 输出配置总线名称来源 `Auto`（默认）| `Property`

**Configuration** 输出端口的总线名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建总线名称。
- `Property` — 通过 **指定输出配置总线名称** 参数指定总线名称。

#### 依赖关系

要启用此参数，请选中 **启用雷达配置输出** 复选框。

### **指定输出配置总线名称** — 传感器配置输出总线名称 `BusFusionRadarSensorConfig`（默认）| 有效总线名称

指定在 **Configuration** 输出端口中返回的雷达配置总线名称。

#### 依赖关系

要启用此参数，请将**输出配置总线名称来源**参数设置为 `Property`。

### 测量

#### 分辨率设置

### **方位角分辨率 (deg)** — 雷达方位角分辨率 `1`（默认）| 正标量

雷达的方位角分辨率，指定为正标量。*方位角分辨率*定义了雷达能够区分两个目标的最小方位角间隔。方位角分辨率通常为雷达方位角波束宽度的 3 dB 下降点。单位为度。

### **俯仰角分辨率 (deg)** — 雷达俯仰角分辨率 `5`（默认）| 正标量

雷达的俯仰角分辨率，指定为正标量。*俯仰角分辨率*定义了雷达能够区分两个目标的最小俯仰角间隔。俯仰角分辨率通常为雷达俯仰角波束宽度的 3 dB 下降点。单位为度。

#### 依赖关系

要启用此参数，请选中 **启用俯仰角测量** 复选框。

### **距离分辨率 (m)** — 雷达距离分辨率 `100`（默认）| 正实标量

雷达的距离分辨率，以米为单位，指定为正实标量。*距离分辨率*定义了雷达能够区分两个目标的最小距离间隔。单位为米。

### **距离变化率分辨率 (m/s)** — 雷达距离变化率分辨率 `10`（默认）| 正实标量

雷达的距离变化率分辨率，指定为正实标量。*距离变化率分辨率*定义了雷达能够区分两个目标的最小距离变化率间隔。单位为米每秒。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡中选中 **启用距离变化率测量** 复选框。

#### 偏差设置

### **方位角偏差系数** — 雷达方位角偏差系数 `0.1`（默认）| 非负标量

雷达的方位角偏差系数，指定为非负标量。*方位角偏差*表示为 **方位角分辨率 (deg)** 参数中指定的方位角分辨率的一个分数。此值设定了雷达方位角精度的下界，为无量纲量。

### **俯仰角偏差系数** — 雷达俯仰角偏差系数 `0.1`（默认）| 非负标量

雷达的俯仰角偏差系数，指定为非负标量。*俯仰角偏差*表示为 **俯仰角分辨率 (deg)** 参数中指定的俯仰角分辨率的一个分数。此值设定了雷达俯仰角精度的下界，为无量纲量。

#### 依赖关系

要启用此参数，请选中 **启用俯仰角测量** 复选框。

### **距离偏差比例** — 距离偏差比例 `0.05`（默认）| 非负标量

雷达的距离偏差比例，指定为非负标量。距离偏差表示为 **距离分辨率 (m)** 属性所指定距离分辨率的一个比例。该参数为雷达的距离精度设定下界，且无量纲。

### **距离变化率偏差比例** — 距离变化率偏差比例 `0.05`（默认）| 非负标量

雷达的距离变化率偏差比例，指定为非负标量。距离变化率偏差表示为 **距离变化率分辨率 (m/s)** 参数所指定距离变化率分辨率的一个比例。该参数为雷达的距离变化率精度设定下界，且无量纲。

#### 依赖关系

要启用此参数，请选中 **Enable range rate measurements** 复选框。

#### 检测器设置

### **总角视场 [AZ, EL] (deg)** — 雷达的角视场 `[1 5]`（默认）| 形式为 `[azfov,elfov]` 的 1×2 正实值向量

雷达的角视场，指定为形式为 `[azfov elfov]` 的 1×2 正实值向量。视场定义了传感器所张成的角度范围。方位视场 `azfov` 必须位于区间 (0, 360] 内。俯仰视场 `elfov` 必须位于区间 (0, 180] 内。单位为度

### **距离限制 [MIN, MAX] (m)** — 雷达的最小和最大距离 `[0 100e3]`（默认）| 形式为 `[min max]` 的 1×2 非负实值向量

雷达的最小和最大距离，指定为形式为 `[min max]` 的 1×2 非负实值向量。雷达不会检测此范围之外的目标。最大距离 `max` 必须大于最小距离 `min`。单位为米。

### **距离变化率限制 [MIN, MAX] (m/s)** — 雷达的最小和最大距离变化率 (m/s) `[-200, 200]`（默认）| 形式为 `[min max]` 的 1×2 实值向量

雷达的最小和最大距离变化率，指定为形式为 `[min max]` 的 1×2 实值向量。雷达不会检测此距离变化率之外的目标。最大距离变化率 `max` 必须大于最小距离变化率 `min`。单位为米每秒。

#### 依赖关系

要启用此参数，请选中 **Enable range rate measurements** 复选框。

### **检测概率** — 检测目标的概率 `0.9`（默认）| 范围 (0, 1] 内的标量

检测目标的概率，指定为范围 (0, 1] 内的标量。该参数定义了检测具有由 **Reference target RCS (dBsm)** 参数指定的雷达散射截面 (RCS) 且位于由 **Reference target range (m)** 参数指定距离处的目标的概率。单位为无量纲。

### **虚警率** — 虚警报告率 `1e-06`（默认）| 范围 [10–7, 10–3] 内的正实标量

每个雷达分辨率单元内的虚警报告率，指定为范围 [10–7, 10–3] 内的正实标量。该模块根据 **Azimuth resolution (deg)** 和 **Range resolution (m)** 参数确定分辨率单元，并且在启用时还根据 **Elevation resolution (deg)** 和 **Range rate resolution (m/s)** 参数确定分辨率单元。单位为无量纲。

### **参考目标距离 (m)** — 参考目标距离 `1000e3`（默认）| 正实标量

给定检测概率和给定参考雷达散射截面 (RCS) 下的参考目标距离，指定为正实标量。*参考距离* 是指具有由 **Reference target RCS (dBsm)** 参数指定的雷达散射截面的目标以由 **Detection probability** 参数指定的检测概率被检测到时的距离。单位为米。

### **Reference target RCS (dBsm)** — 参考目标雷达散射截面 `0`（默认）| 实数标量

给定检测概率和参考距离下的参考目标雷达散射截面（RCS），指定为实数标量。*参考 RCS* 是在指定的 **Reference target range (m)** 参数值下，以 **Detection probability** 参数指定的概率检测到目标时的 RCS 值。数值以 dBsm 表示。

### **Center frequency (Hz)** — 雷达频段中心频率 `300e6`（默认）| 正实数标量

雷达频段的中心频率，指定为正标量。单位为 Hz。

#### Tracker Setting

### **Filter initialization function name** — 卡尔曼滤波器初始化函数 `initcvekf`（默认）| 函数名

卡尔曼滤波器初始化函数，指定为有效的卡尔曼滤波器初始化函数的名称。

下表显示了可用于指定 **Filter initialization function name** 的初始化函数。

| Initialization Function | Function Definition |
| --- | --- |
| `initcaabf` | Initialize constant-acceleration alpha-beta Kalman filter |
| `initcvabf` | Initialize constant-velocity alpha-beta Kalman filter |
| `initcakf` | Initialize constant-acceleration linear Kalman filter. |
| `initcvkf` | Initialize constant-velocity linear Kalman filter. |
| `initcaekf` | Initialize constant-acceleration extended Kalman filter. |
| `initctekf` | Initialize constant-turnrate extended Kalman filter. |
| `initcvekf` | Initialize constant-velocity extended Kalman filter. |
| `initcaukf` | Initialize constant-acceleration unscented Kalman filter. |
| `initctukf` | Initialize constant-turnrate unscented Kalman filter. |
| `initcvukf` | Initialize constant-velocity unscented Kalman filter. |

您也可以编写自己的初始化函数。该函数必须具有以下语法。

```
filter = filterInitializationFcn(detection)
```

该函数的输入是由 `objectDetection` 对象创建的检测报告。该函数的输出必须是跟踪滤波器对象，例如 `trackingKF`、`trackingEKF`、`trackingUKF` 或 `trackingABF`。

为帮助您编写此函数，您可以在 MATLAB 中查看表中某个函数的详细信息。

```
type initcvekf
```

#### 依赖关系

要启用此参数，请将 **Target reporting format** 参数设置为 `Tracks`。

### **M and N for the M-out-of-N confirmation** — 航迹确认阈值 `[2 3]`（默认）| 1×2 正整数向量

航迹确认阈值，指定为形式为 `[M N]` 的 1×2 正整数向量。如果航迹在最近 `N` 次更新中至少收到 `M` 次检测，则该航迹被确认。`M` 必须小于或等于 `N`。

- 设置 `M` 时，请考虑传感器的目标检测概率。检测概率取决于遮挡或杂波等因素。当航迹无法被确认时，您可以减小 `M`；当过多虚假检测被分配给航迹时，您可以增大 `M`。
- 设置 `N` 时，请考虑您希望跟踪器在做出确认决策之前更新的次数。例如，如果跟踪器每 0.05 秒更新一次，而您希望允许 0.5 秒来做出确认决策，则设置 `N = 10`。

#### 依赖关系

要启用此参数，请将 **Target reporting format** 参数设置为 `Tracks`。

### **P and R for the P-out-of-R deletion** — 航迹删除阈值 `[5 5]`（默认）| 1×2 正整数向量

航迹删除阈值，指定为形式为 `[P R]` 的 1×2 正整数向量。如果已确认航迹在最近 `R` 次跟踪器更新中未被分配到任何检测 `P` 次，则该航迹被删除。`P` 必须小于或等于 `R`。

- 要缩短雷达维持航迹的时间，减小 `R` 或增大 `P`。
- 要更长时间地维持航迹，增大 `R` 或减小 `P`。

#### 依赖关系

要启用此参数，请将 **Target reporting format** 参数设置为 `Tracks`。

#### Random Number Generator Settings

### **Random number generation** — 指定随机数生成器种子的方法 `Repeatable`（默认）| `Specify seed` | `Not repeatable`

将随机数生成器种子设置为表中选项之一的方法。

| Option | Description |
| --- | --- |
| `Repeatable` | 该模块在首次仿真时生成随机初始种子，并在所有后续仿真中复用此种子。选择此参数可从统计传感器模型生成可重复的结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 通过 **Initial seed** 参数指定您自己的随机初始种子以获得可重复的结果。 |
| `Not repeatable` | 该模块在每次仿真运行后生成新的随机初始种子。选择此参数可从统计传感器模型生成不可重复的结果。 |

### **Initial seed** — 随机数生成器种子 `0`（默认）| 小于 232 的非负整数

随机数生成器种子，指定为小于 232 的非负整数。

#### 依赖关系

要启用此参数，请将 **Random number generation** 参数设置为 `Specify seed`。

### Target Profiles

### **Target profiles definition** — 指定目标剖面的方法 `From Scenario Reader block`（默认）| `MATLAB expression` | `Parameters`

指定目标剖面的方法，指定为 `Parameters`、`MATLAB expression`、`From Scenario Reader block` 之一。剖面是场景中目标的物理特性和雷达特性。

- `Parameters` — 该模块从以下参数获取目标剖面：

  - **Unique target identifiers**
  - **Target classification identifiers**
  - **Length of target cuboids (m)**
  - **Width of target cuboids (m)**
  - **Height of target cuboids (m)**
  - **Rotational center of target cuboids (m)**
  - **Target signatures**
- `MATLAB expression` — 该模块从 **MATLAB expression for target profiles** 参数指定的 MATLAB 表达式获取目标剖面。
- `From Scenario Reader block` — 该模块从 Tracking Scenario Reader 模块获取平台剖面。

### **MATLAB expression for target profiles** — 目标剖面的 MATLAB 表达式 MATLAB 结构体 | MATLAB 结构体数组 | 有效的 MATLAB 表达式

指定目标剖面的 MATLAB 表达式，作为 MATLAB 结构体、MATLAB 结构体数组或生成此类结构体或结构体数组的有效 MATLAB 表达式。

您可以使用 `trackingScenario` 对象的 `platformProfiles` 对象函数的输出指定目标剖面。

默认目标剖面表达式生成一个 MATLAB 结构体，其形式如下。

```
struct('ClassID',0,'Dimensions', ...
'Length',0,'Width',0,'Height',0,'OriginOffset',[0 0 0]), ...
'Signatures',{rcsSignature})
```

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `MATLAB expression`。

### **唯一目标标识符** — 场景定义的目标标识符 `[]`（默认）| 正整数 | 长度为 *L* 的唯一正整数向量

将场景定义的目标标识符指定为正整数或长度为 *L* 的唯一正整数向量。*L* 必须等于输入到 **Platforms** 输入端口的目标数量。向量元素必须与目标的 `PlatformID` 值匹配。您可以将 **唯一目标标识符** 指定为 `[]`。在这种情况下，相同的目标轮廓参数适用于所有目标。

**示例：** `[1 2]`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **目标分类标识符** — 用户定义的分类标识符 `0`（默认）| 整数 | 长度为 *L* 的整数向量

将用户定义的分类标识符指定为整数或长度为 *L* 的整数向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，您必须将此参数指定为单个整数，其值适用于所有目标。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **目标长方体的长度 (m)** — 目标长方体的长度 `0`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将目标长方体的长度指定为正实数标量或长度为 *L* 的正值向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，您必须将此参数指定为正实数标量，其值适用于所有目标。单位为米。

**示例：** `6.3`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **目标长方体的宽度 (m)** — 目标长方体的宽度 `0`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将目标长方体的宽度指定为正实数标量或长度为 *L* 的正值向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，您必须将此参数指定为正实数标量，其值适用于所有目标。单位为米。

**示例：** `4.7`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **目标长方体的高度 (m)** — 目标长方体的高度 `0`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将目标长方体的高度指定为正实数标量或长度为 *L* 的正值向量。当 **唯一目标标识符** 为向量时，此参数为相同长度的向量，其元素与 **唯一目标标识符** 中的目标一一对应。当 **唯一目标标识符** 为空 `[]` 时，您必须将此参数指定为正实数标量，其值适用于所有目标。单位为米。

**示例：** `2.0`

#### 依赖关系

要启用此参数，请将 **目标轮廓定义** 参数设置为 `Parameters`。

### **Rotational center of target cuboids (m)** — 目标长方体的旋转中心 `{[0, 0, 0]}`（默认）| 长度为 *L* 的实数 1×3 向量元胞数组

将目标长方体的旋转中心指定为长度为 *L* 的实数 1×3 向量元胞数组。每个向量表示目标长方体的旋转中心相对于目标中心的偏移量。旋转中心按照平台输入参数的 Dimensions 属性中详细说明的约定定义。当 **Unique target identifiers** 为向量时，此参数为向量元胞数组，其元胞与 **Unique target identifiers** 中的目标一一对应。当 **Unique target identifiers** 为空 `[]` 时，必须将此参数指定为包含一个偏移向量的单元素元胞数组，其值适用于所有目标。单位为米。

**示例：** `{[-1.35, 0.2, 0.3]}`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Target signatures** — 目标签名 `{rcsSignature}`（默认）| 长度为 *L* 的元胞数组

目标签名，指定为长度为 *L* 的 `rcsSignature` 对象元胞数组，用于指定目标的 RCS 签名。*L* 是 **Platforms** 输入端口中指定的目标数量。

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

## 所属库

Sensor Fusion and Tracking Toolbox / Tracking Scenario and Sensor Models

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2023a：Simulink 总线不再显示在工作区中

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

生成雷达传感器检测和航迹

Fusion Radar Sensor 模块读取目标平台位姿，并基于雷达传感器模型从目标生成检测报告和航迹报告。目前，Fusion Radar Sensor 模块仅支持非扫描模式。Fusion Radar Sensor 模块可以生成带有附加随机噪声的聚类或非聚类检测，还可以生成虚警检测。您还可以从 Fusion Radar Sensor 模块生成航迹。使用 **Target reporting format** 参数将传感器输出指定为聚类检测、非聚类检测或航迹。
