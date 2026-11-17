---
type: simulink-block
title: 'Driving Radar Data Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'drivingradardatagenerator'
documentation_source_path: 'ref/drivingradardatagenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Driving Radar Data Generator

## 端口

### 输入

### **Actors** — 场景参与者位姿 包含 MATLAB® 结构的 Simulink 总线

场景参与者在自车坐标系中的位姿，指定为包含 MATLAB 结构的 Simulink 总线。

该结构必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `Actors` | 参与者位姿 | 长度为 `NumActors` 的参与者位姿结构数组 |

`Actors` 中的每个参与者位姿结构必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的实值向量。单位为度每秒。 |
### 输出

### **Clustered detections** — 聚类目标检测 包含 MATLAB 结构的 Simulink 总线

聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于聚类检测，该模块为每个目标输出单个检测，其中每个检测是该目标的未聚类检测的质心。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器（例如 Multi-Object Tracker 模块），并生成航迹。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | 非负整数 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | 布尔值 |
| `Detections` | 目标检测 | 长度由 **Maximum number of reported detections** 参数设置的目标检测结构数组。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 以 **Coordinate system** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和 `MeasurementNoise` 以球坐标系报告，该坐标系基于传感器直角坐标系。

**`Measurement` 和 `MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| `Body` | 此表显示了坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示了坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

对于 `ObjectAttributes`，此表描述了用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成检测的参与者的标识符 `ActorID`。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate system** 参数设置为 `Body` 时，父坐标系为自车车身。当您将 **Coordinate system** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系为传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 指示用于报告测量值的坐标系的枚举类型。当 `Frame` 设置为 `'rectangular'` 时，检测以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡上，将 **Target reporting format** 参数设置为 `Clustered detections`。

### **Tracks** — 目标航迹 包含 MATLAB 结构的 Simulink 总线

目标航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

此表显示了结构字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 长度由 **Maximum number of tracks** 参数设置的航迹结构数组。其中只有前 `NumTracks` 个是实际航迹。 |

此表显示了每个航迹结构的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为秒。 |
| `Age` | 航迹更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于已确认的航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1×*K* 逻辑数组。*K* 是记录的最近航迹逻辑状态的数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

该模块仅输出已确认的航迹，即在航迹初始化后的前 *N* 次更新中，该模块为其分配至少 *M* 个检测的航迹。要指定值 *M* 和 *N*，请使用 **M and N for the M-out-of-N confirmation** 参数。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡上，将 **Target reporting format** 参数设置为 `Tracks`。

### **Detections** — 未聚类目标检测 包含 MATLAB 结构的 Simulink 总线

未聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于未聚类检测，该模块输出所有检测，一个目标可以有多个检测。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器（例如 Multi-Object Tracker 模块），并生成航迹。

该结构必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | 整数 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | 布尔值 |
| `Detections` | 目标检测 | 长度由 **Maximum number of reported detections** 参数设置的目标检测结构数组。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 以 **Coordinate system** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和 `MeasurementNoise` 以球坐标系报告，该坐标系基于传感器直角坐标系。

**`Measurement` 和 `MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| `Body` | 此表显示了坐标如何受 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | 此表显示了坐标如何受 **Enable elevation angle measurements** 和 **Enable range rate measurements** 参数影响。  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

对于 `ObjectAttributes`，此表描述了用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成检测的参与者的标识符 `ActorID`。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate system** 参数设置为 `Body` 时，父坐标系为自车车身。当您将 **Coordinate system** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系为传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 指示用于报告测量值的坐标系的枚举类型。当 `Frame` 设置为 `'rectangular'` 时，检测以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡上，将 **Target reporting format** 参数设置为 `Detections`。

## 参数

### 参数

#### 传感器标识

### **Unique identifier of sensor** — 唯一传感器标识符 `0`（默认）| 正整数

将唯一传感器标识符指定为正整数。使用此参数区分多传感器系统中来自不同传感器的检测或航迹。为每个传感器指定唯一值。如果您未将 **Unique identifier of sensor** 从默认值 `0` 更新，则雷达在仿真开始时返回错误。

### **Update rate (Hz)** — 传感器更新率 `10`（默认）| 正实值标量

将传感器更新率以赫兹指定为正实值标量。更新率的倒数必须是仿真时间间隔的整数倍。雷达按此倒数定义的间隔生成新报告。在更新间隔之间请求的任何传感器更新不包含检测或航迹。

#### 传感器安装

### **Translation [ X, Y, Z ] relative to ego origin (m)** — 自车上的传感器位置 (m) `[3.4, 0, 0.2]`（默认）| 形式为 [*x* *y* *z*] 的 1×3 实值向量

将自车车身坐标系上的传感器位置以米指定为形式为 [*x* *y* *z*] 的 1×3 实值向量。此参数定义传感器相对于自车原点沿 *x* 轴、*y* 轴和 *z* 轴的坐标，其中：

- *x* 轴从车辆指向前方。
- *y* 轴指向车辆左侧。
- *z* 轴从地面指向上方。

默认值对应于安装在轿车前格栅中央的雷达。

有关自车坐标系的更多详细信息，请参阅 Coordinate Systems in Automated Driving Toolbox。

### **Rotation [Yaw, Pitch, Roll] relative to ego's frame (deg)** — 雷达的安装旋转角度 `[0 0 0]`（默认）| 形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量

将雷达的安装旋转角度以度指定为形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量。此参数定义传感器相对于自车车身坐标系绕 *z* 轴、*y* 轴和 *x* 轴的内旋欧拉角旋转，其中：

- *z*yaw，即 *偏航角*，使传感器绕自车的 *z* 轴旋转。
- *y*pitch，即 *俯仰角*，使传感器绕自车的 *y* 轴旋转。此旋转相对于由 *z*yaw 旋转产生的传感器位置。
- *x*roll，即 *横滚角*，使传感器绕自车的 *x* 轴旋转。此旋转相对于由 *z*yaw 和 *y*pitch 旋转产生的传感器位置。

当分别沿 *z* 轴、*y* 轴和 *x* 轴的正方向观察时，这些角度为顺时针正。如果您从鸟瞰视角可视化传感器数据，则偏航角为逆时针正，因为您沿 *z* 轴的负方向查看数据，而 *z* 轴从地面指向上方。

有关此坐标系的更多详细信息，请参阅 Coordinate Systems in Automated Driving Toolbox。

#### 检测报告

### **Enable elevation angle measurements** — 使雷达能够测量目标仰角 `off`（默认）| `on`

选择此参数可对能够估计目标仰角的雷达传感器进行建模。

### **Enable range rate measurements** — 使雷达能够测量目标距离变化率 `on`（默认）| `off`

选择此参数可使雷达能够从目标检测中测量距离变化率。

### **Add noise to measurements** — 启用向雷达传感器测量值添加噪声 `on`（默认）| `off`

选择此参数可向雷达测量值添加噪声。否则，测量值无噪声。即使清除此参数，生成的检测输出中 `MeasurementNoise` 字段所报告的测量噪声协方差矩阵仍表示在选中 **Add noise to measurements** 时所添加的测量噪声。

### **Enable false reports** — 启用生成虚警雷达检测 `on`（默认）| `off`

选择此参数可启用生成虚警雷达测量值。如果清除此参数，雷达仅报告实际检测。

### **Enable occlusion** — 启用视线遮挡 `on`（默认）| `off`

选择此参数可启用视线遮挡，此时雷达仅对雷达具有直接视线的目标生成检测。例如，启用此参数后，雷达不会为被另一辆车遮挡而无法看到的车辆生成检测。

### **Maximum number of target reports** — 检测或航迹的最大数量 `50`（默认）| 正整数

以正整数形式指定传感器报告的最大检测或航迹数量。传感器按距传感器距离递增的顺序报告检测，直到达到此最大数量。

### **Target reporting format** — 生成目标报告的格式 `Clustered detections`（默认）| `Tracks` | `Detections`

将生成目标报告的格式指定为以下选项之一：

- `Clustered detections` — 模块将目标报告生成为*聚类检测*，其中每个目标报告为单个检测，即未聚类目标检测的质心。模块在 **Clustered detections** 输出端口返回聚类检测。
- `Tracks` — 模块将目标报告生成为*航迹*，即经过跟踪滤波器处理的聚类检测。模块在 **Tracks** 输出端口返回聚类检测。
- `Detections` — 模块将目标报告生成为*未聚类检测*，其中每个目标可以有多个检测。模块在 **Detections** 输出端口返回聚类检测。

### **Coordinate system** — 所报告检测的坐标系 `Body`（默认）| `Sensor rectangular` | `Sensor spherical`

所报告检测的坐标系，指定为以下选项之一：

- `Body` — 检测在自车的矩形本体系中报告。
- `Sensor rectangular` — 检测在雷达传感器的矩形本体系中报告。
- `Sensor spherical` — 检测在以雷达传感器为中心并与雷达在自车上的朝向对齐的球坐标系中报告。

#### Port Settings

### **Source of output bus name** — 输出总线名称的来源 `Auto`（默认）| `Property`

输出总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建总线名称。
- `Property` — 使用 **Specify an output bus name** 参数指定总线名称。

### **Specify an output bus name** — 输出总线的名称 `BusDrivingRadarDataGenerator`（默认）| 有效总线名称

指定在 **Actors** 输出端口中返回的 actor 位姿总线的名称。

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

### Measurements

#### Resolution Settings

### **Azimuth resolution (deg)** — 雷达的方位分辨率 `4`（默认）| 正实数标量

以正标量形式指定雷达的方位分辨率（以度为单位）。*方位分辨率*定义了雷达能够区分两个目标的最小方位角间隔。方位分辨率通常为雷达方位角波束宽度的 3 dB 下降点。

### **Elevation resolution (deg)** — 雷达的仰角分辨率 `5`（默认）| 正实数标量

以正实数标量形式指定雷达的仰角分辨率（以度为单位）。*仰角分辨率*定义了雷达能够区分两个目标的最小仰角间隔。仰角分辨率通常为雷达仰角波束宽度的 3 dB 下降点。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上选择 **Enable elevation angle measurements** 参数。

### **Range resolution (m)** — 雷达的距离分辨率 `2.5`（默认）| 正实数标量

以正实数标量形式指定雷达的距离分辨率（以米为单位）。*距离分辨率*定义了雷达能够区分两个目标的最小距离间隔。

### **Range rate resolution (m/s)** — 雷达的距离变化率分辨率 `0.5`（默认）| 正实数标量

以正实数标量形式指定雷达的距离变化率分辨率（以米每秒为单位）。*距离变化率分辨率*定义了雷达能够区分两个目标的最小距离变化率间隔。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上选择 **Enable range rate resolution** 参数。

#### Bias Settings

### **Azimuth bias fraction** — 雷达的方位偏差分数 `0.1`（默认）| 非负标量

以非负标量形式指定雷达的方位偏差分数。*方位偏差*表示为 **Azimuth resolution (deg)** 参数中所指定方位分辨率的一部分。此值设定了雷达方位精度的下界，并且是无量纲的。

### **Elevation bias fraction** — 雷达的仰角偏差分数 `0.1`（默认）| 非负标量

以非负标量形式指定雷达的仰角偏差分数。*仰角偏差*表示为 **Elevation resolution (deg)** 参数所指定仰角分辨率的一部分。此值设定了雷达仰角精度的下界，并且是无量纲的。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上选择 **Enable elevation angle measurements** 参数。

### **Range bias fraction** — 距离偏差分数 `0.05`（默认）| 非负标量

以非负标量形式指定雷达的距离偏差分数。距离偏差表示为 **Range resolution (m)** 属性所指定距离分辨率的一部分。此属性设定了雷达距离精度的下界，并且是无量纲的。

### **Range rate bias fraction** — 距离变化率偏差分数 `0.05`（默认）| 非负标量

以非负标量形式指定雷达的距离变化率偏差分数。距离变化率偏差表示为 **Range rate resolution (m/s)** 参数所指定距离变化率分辨率的一部分。此属性设定了雷达距离变化率精度的下界，并且是无量纲的。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上选择 **Enable range rate measurements** 参数。

#### Detector Settings

### **Total angular field of view [AZ, EL] (deg)** — 雷达的角视场 `[20 5]`（默认）| 形式为 `[azfov, elfov]` 的 1×2 正实值向量

以形式为 `[azfov elfov]` 的 1×2 正实值向量指定雷达的角视场（以度为单位）。视场定义了传感器所跨越的总角度范围。方位视场 `azfov` 必须位于区间 (0, 360] 内。仰角视场 `elfov` 必须位于区间 (0, 180] 内。

### **Range limits [MIN, MAX] (m)** — 雷达的最小和最大距离 `[0 150]`（默认）| 形式为 `[min max]` 的 1×2 非负实值向量

以形式为 `[min max]` 的 1×2 非负实值向量指定雷达的最小和最大距离（以米为单位）。雷达不会检测此范围之外的目标。最大距离 `max` 必须大于最小距离 `min`。

### **Range rate limits [MIN, MAX] (m/s)** — 雷达的最小和最大距离变化率（m/s） `[-100 100]`（默认）| 形式为 `[min max]` 的 1×2 实值向量

以形式为 `[min max]` 的 1×2 实值向量指定雷达的最小和最大距离变化率（以米每秒为单位）。雷达不会检测此距离变化率范围之外的目标。最大距离变化率 `max` 必须大于最小距离变化率 `min`。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上选择 **Enable range rate measurements** 参数。

### **Detection probability** — 检测到目标的概率 `0.9`（默认）| 范围 (0, 1] 内的标量

以范围 (0, 1] 内的标量形式指定检测到目标的概率。此量定义了在 **Reference target range (m)** 参数所指定的参考检测距离处，检测到雷达截面积由 **Reference target RCS (dBsm)** 参数所指定目标的概率。

### **False alarm rate** — 虚警报告率 `1e-06`（默认）| 范围 [10–7, 10–3] 内的正实数标量

以范围 [10–7, 10–3] 内的正实数标量形式指定每个雷达分辨率单元内的虚警报告率。单位为无量纲。模块根据 **Azimuth resolution (deg)** 和 **Range resolution (m)** 参数确定分辨率单元，并在启用时根据 **Elevation resolution (deg)** 和 **Range rate resolution (m/s)** 参数确定。

### **Reference target range (m)** — 给定检测概率的参考距离 `100`（默认）| 正实数标量

以正实数标量形式指定给定检测概率和给定参考雷达截面积（RCS）的参考距离（以米为单位）。*参考距离*是指具有由 **Reference target RCS (dBsm)** 参数所指定雷达截面积的目标以 **Detection probability** 参数所指定检测概率被检测到的距离。

### **Reference target RCS (dBsm)** — 给定检测概率的参考雷达截面积 `0`（默认）| 实标量

以实标量形式指定给定检测概率和参考距离的参考雷达截面积（RCS）（以分贝平方米为单位）。*参考 RCS* 是指在指定的 **Reference target range (m)** 参数值处，目标以 **Detection probability** 参数所指定概率被检测到的 RCS 值。

### **Center frequency (Hz)** — 雷达频带的中心频率 `77e9`（默认）| 正实数标量

以正标量形式指定雷达频带的中心频率（以赫兹为单位）。

#### Tracker Settings

### **Filter initialization function name** — 卡尔曼滤波器初始化函数 `initcvekf`（默认）| 函数名

以函数句柄或有效卡尔曼滤波器初始化函数名称的字符向量或字符串标量形式指定卡尔曼滤波器初始化函数。

下表显示了可用于指定 **Filter initialization function name** 的初始化函数。

| Initialization Function | Function Definition |
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

您也可以编写自己的初始化函数。该函数必须具有以下语法：

```
filter = filterInitializationFcn(detection)
```

此函数的输入是检测报告，类似于由 `objectDetection` 对象创建的报告。此函数的输出必须是跟踪滤波器对象，例如 `trackingKF`、`trackingEKF`、`trackingUKF` 或 `trackingABF`。

为指导您编写此函数，您可以在 MATLAB 中查看所提供函数的详细信息。例如：

```
type initcvekf
```

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上将 **Target reporting format** 参数设置为 `Tracks`。

### **M and N for the M-out-of-N confirmation** — 航迹确认阈值 `[2 3]`（默认）| 1×2 正整数向量

以形式为 `[M N]` 的 1×2 正整数向量指定航迹确认阈值。如果航迹在最近 `N` 次更新中接收到至少 `M` 次检测，则该航迹被确认。`M` 必须小于或等于 `N`。

- 设置 `M` 时，请考虑传感器的目标检测概率。检测概率取决于遮挡或杂波等因素。当航迹未能确认时，可以减小 `M`；当过多虚警检测被分配给航迹时，可以增大 `M`。
- 设置 `N` 时，请考虑您希望跟踪器在做出确认决策之前更新的次数。例如，如果跟踪器每 0.05 秒更新一次，并且您希望允许 0.5 秒来做出确认决策，请设置 `N = 10`。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上将 **Target reporting format** 参数设置为 `Tracks`。

### **P and R for the P-out-of-R deletion** — 航迹删除阈值 `[5 5]`（默认）| 1×2 正整数向量

以形式为 `[P R]` 的 1×2 正整数向量指定航迹删除阈值。如果已确认航迹在最近 `R` 次跟踪器更新中未分配到任何检测达到 `P` 次，则该航迹被删除。`P` 必须小于或等于 `R`。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上将 **Target reporting format** 参数设置为 `Tracks`。

#### Random Number Generator Settings

### **Random number generation** — 指定随机数生成器种子的方法 `Repeatable`（默认）| `Specify seed` | `Not repeatable`

将设置随机数生成器种子的方法指定为表中的选项之一。

| Option | Description |
| --- | --- |
| `Repeatable` | 模块为首次仿真生成随机初始种子，并在所有后续仿真中重用此种子。选择此参数可从统计传感器模型生成可重复的结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 使用 **Initial seed** 参数指定您自己的随机初始种子以获得可重复的结果。 |
| `Not repeatable` | 模块在每次仿真运行后生成新的随机初始种子。选择此参数可从统计传感器模型生成不可重复的结果。 |

### **Initial seed** — 随机数生成器种子 `0`（默认）| 小于 232 的非负整数

以小于 232 的非负整数形式指定随机数生成器种子。

#### 依赖关系

要启用此参数，请将 **Random number generation** 参数设置为 `Specify seed`。

### Target Profiles

### **目标配置文件定义** — 指定目标配置文件的方法 `From Scenario Reader block`（默认）| `MATLAB expression` | `Parameters`

指定目标配置文件的定义方法，即驾驶场景中所有目标的物理特性和雷达特性，可选以下选项之一：

- `Parameters` — 当选择此选项时，模块从 **Target Profiles** 选项卡上启用的参数中获取目标配置文件。
- `MATLAB expression` — 模块从 **MATLAB expression for target profiles** 参数指定的 MATLAB 表达式中获取参与者配置文件。
- `From Scenario Reader block` — 模块从 Scenario Reader 模块或 RoadRunner Scenario Reader 模块指定的场景中获取参与者配置文件。

### **目标配置文件的 MATLAB 表达式** — 目标配置文件的 MATLAB 表达式 MATLAB 结构体 | MATLAB 结构体数组 | 有效的 MATLAB 表达式

指定参与者配置文件的 MATLAB 表达式，可以是 MATLAB 结构体、MATLAB 结构体数组，或生成此类结构体或结构体数组的有效 MATLAB 表达式。

如果您的 Scenario Reader 模块从 `drivingScenario` 对象读取数据，要直接从该对象获取参与者配置文件，请将此表达式设置为对该对象调用 `actorProfiles` 函数。例如：`actorProfiles(scenario)`。

默认目标配置文件表达式生成一个 MATLAB 结构体，形式如下：

```
struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4, ...
'OriginOffset',[-1.35 0 0],'RCSPattern',[10 10;10 10], ...
'RCSAzimuthAngles',[-180 180],'RCSElevationAngles',[-90 90])
```

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `MATLAB expression`。

### **参与者的唯一标识符** — 场景定义的参与者标识符 `[]`（默认）| 正整数 | 长度为 *L* 的唯一正整数向量

将场景定义的参与者标识符指定为正整数或长度为 *L* 的唯一正整数向量。*L* 必须等于输入到 **Actors** 输入端口中的参与者数量。向量元素必须与参与者的 `ActorID` 值匹配。您可以将 **Unique identifier for actors** 指定为 `[]`。在这种情况下，相同的参与者配置文件参数适用于所有参与者。

**示例：** `[1 2]`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **用于对参与者分类的用户定义整数** — 用户定义的分类标识符 `0`（默认）| 整数 | 长度为 *L* 的整数向量

将用户定义的分类标识符指定为整数或长度为 *L* 的整数向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为单个整数，其值适用于所有参与者。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **参与者长方体长度 (m)** — 参与者长方体的长度 `4.7`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将参与者长方体的长度指定为正实数标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为正实数标量，其值适用于所有参与者。单位为米。

**示例：** `6.3`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **参与者长方体宽度 (m)** — 参与者长方体的宽度 `1.8`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将参与者长方体的宽度指定为正实数标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为正实数标量，其值适用于所有参与者。单位为米。

**示例：** `4.7`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **参与者长方体高度 (m)** — 参与者长方体的高度 `1.4`（默认）| 正实数标量 | 长度为 *L* 的正值向量

将参与者长方体的高度指定为正实数标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为正实数标量，其值适用于所有参与者。单位为米。

**示例：** `2.0`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **参与者从底部中心起的旋转中心 (m)** — 参与者的旋转中心 `{[-1.35, 0, 0]}`（默认）| 长度为 *L* 的实值 1×3 向量元胞数组

将参与者的旋转中心指定为长度为 *L* 的实值 1×3 向量元胞数组。每个向量表示参与者旋转中心相对于参与者底部中心的偏移量。对于车辆，该偏移量对应于后轴中心下方地面上的点。当 **Unique identifier for actors** 为向量时，此参数为向量元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为包含一个元素的元胞数组，该元素包含一个偏移向量，其值适用于所有参与者。单位为米。旋转中心根据 Actor and Vehicle Positions and Dimensions 中详述的约定定义。

**示例：** `{[-1.35, 0.2, 0.3]}`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **雷达截面积方向图 (dBsm)** — 雷达截面积 `{[10, 10; 10, 10]}`（默认）| 实值 *Q*×*P* 矩阵 | 长度为 *L* 的实值 *Q*×*P* 矩阵元胞数组

将参与者的雷达截面积 (RCS) 指定为实值 *Q*×*P* 矩阵或长度为 *L* 的实值 *Q*×*P* 矩阵元胞数组。*Q* 是 **Elevation angles defining RCSPattern (deg)** 参数中对应元胞指定的仰角数量。*P* 是 **Azimuth angles defining RCSPattern (deg)** 参数中对应元胞指定的方位角数量。当 **Unique identifier for actors** 为向量时，此参数为矩阵元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。*Q* 和 *P* 的值在不同元胞之间可以不同。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为包含一个元素的元胞数组，该元素包含一个矩阵，其值适用于所有参与者。单位为 dBsm。

**示例：** `{[10 14 10; 9 13 9]}`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **定义 RCSPattern 的方位角 (deg)** — 雷达截面积方向图的方位角 `{[-180 180]}`（默认）| 长度为 *L* 的实值 *P* 长度向量元胞数组

将雷达截面积方向图的方位角指定为长度为 *L* 的实值 *P* 长度向量元胞数组。每个向量表示 **Radar cross section pattern (dBsm)** 中指定的雷达截面积的 *P* 列的方位角。当 **Unique identifier for actors** 为向量时，此参数为向量元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。*P* 的值在不同元胞之间可以不同。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为包含一个元素的元胞数组，该元素包含一个向量，其值适用于所有参与者。单位为度。方位角位于 –180° 到 180° 范围内，且必须严格递增。

当 **Radar cross section pattern (dBsm)** 的元胞中指定的雷达截面积都具有相同维度时，您只需指定包含一个元素的元胞数组，该元素包含方位角向量。

**示例：** `{[-90 90]}`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **定义 RCSPattern 的仰角 (deg)** — 雷达截面积方向图的仰角 `{[-90 90]}`（默认）| 长度为 *L* 的实值 *Q* 长度向量元胞数组

将雷达截面积方向图的仰角指定为长度为 *L* 的实值 *Q* 长度向量元胞数组。每个向量表示 **Radar cross section pattern (dBsm)** 中指定的雷达截面积的 *Q* 列的仰角。当 **Unique identifier for actors** 为向量时，此参数为向量元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。*Q* 的值在不同元胞之间可以不同。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为包含一个元素的元胞数组，该元素包含一个向量，其值适用于所有参与者。单位为度。仰角位于 –90° 到 90° 范围内，且必须严格递增。

当 **Radar cross section pattern (dBsm)** 的元胞中指定的雷达截面积都具有相同维度时，您只需指定包含一个元素的元胞数组，该元素包含仰角向量。

**示例：** `{[-25 25]}`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 对于驾驶场景工作流，Driving Radar Data Generator 模块支持：

  - 快速加速模式仿真。
  - 使用 Simulink Coder™ 以及面向 Simulink Real-Time™ 目标的独立部署。
- 对于 RoadRunner Scenario 工作流，Driving Radar Data Generator 模块支持使用即用型包进行独立部署。有关为您的 Simulink 模型生成即用型包的更多信息，请参阅 Publish Ready-to-Run Actor Behaviors for Reuse and Simulation Performance。

## 版本历史

**在 R2021a 中引入**

### R2024a：与 RoadRunner Scenario 仿真一起使用时，无需使用 `addSensors` 函数注册传感器模型

从 R2024a 开始，Simulink 会自动实例化一个 `SensorSimulation` 对象，并将模型中定义的传感器添加到 RoadRunner 场景中。因此，不再需要使用 `addSensors` 函数手动注册 Driving Radar Data Generator 模块。有关新工作流的更多信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。

在 R2024a 之前的版本中，您必须使用 `addSensors` 函数手动将该模块注册为传感器模型。有关更多信息，请参阅 Adding sensors manually using `addSensors` function is not required for Simulink models。

## 描述

从驾驶场景或 RoadRunner Scenario 生成雷达传感器检测或航迹报告

Driving Radar Data Generator 模块从汽车雷达传感器模型生成目标的检测或航迹报告。使用此模块可从包含参与者和轨迹的驾驶场景生成传感器数据，您可以从 Scenario Reader 模块读取这些数据。

Driving Radar Data Generator 模块可以仿真带有附加随机噪声的聚类或非聚类检测，还可以生成虚警检测。您可以使用 Multi-Object Tracker 模块将生成的检测与其他传感器数据融合并跟踪目标。您还可以直接从 Driving Radar Data Generator 模块输出航迹。要配置目标输出为聚类检测、非聚类检测还是航迹，请使用 **Target reporting format** 参数。

您可以在 Driving Scenario 和 RoadRunner Scenario 仿真中将该模块与车辆参与者一起使用。有关更多信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。
