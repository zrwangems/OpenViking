---
type: simulink-block
title: 'Simulation 3D Radar Data Generator'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Sensors'
documentation_page: 'simulation3dradardatagenerator'
documentation_source_path: 'simulation3dradardatagenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Radar Data Generator

## 端口
```yaml
ports:
- name: Clustered detections
  summary: 包含 MATLAB® 结构的 Simulink® 总线，用于表示聚类后的目标检测
  direction: output
- name: Tracks
  summary: 目标航迹 Simulink 总线，包含 MATLAB 结构体
  direction: output
- name: Detections
  summary: 包含 MATLAB 结构的 Simulink 总线，用于未聚类目标检测
  direction: output
```

### 输出

### **Clustered detections** — 包含 MATLAB® 结构的 Simulink® 总线，用于表示聚类后的目标检测

聚类后的目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于聚类检测，该模块为每个目标输出单个检测，其中每个检测是该目标的未聚类检测的质心。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测的数量 | 非负整数 |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | 布尔值 |
| `Detections` | 目标检测 | 目标检测结构数组，其长度由 **Maximum number of target reports** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数所使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 以 **Coordinate frame used to report detections** 参数指定的直角坐标系报告。
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
| `TargetIndex` | 生成该检测的参与者 `ActorID` 的标识符。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate frame used to report detections** 参数设置为 `Body` 时，父坐标系是自车车身。当您将 **Coordinate frame used to report detections** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系是传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量值的坐标系。当 `Frame` 设置为 `'rectangular'` 时，检测以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖关系

要启用此端口，请在**参数**选项卡上，将**生成目标报告的格式**设置为 `Clustered detections`。

### **Tracks** — 目标航迹 Simulink 总线，包含 MATLAB 结构体

目标航迹，以包含 MATLAB 结构体的 Simulink 总线形式返回。请参阅 Create Nonvirtual Buses (Simulink)。

下表显示了结构体字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由**最大航迹数量**参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

下表显示了每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 唯一航迹标识符，用于区分多条航迹。 |
| `BranchID` | 唯一航迹分支标识符，用于区分多个航迹分支。 |
| `SourceIndex` | 唯一源索引，用于在多跟踪器环境中区分跟踪源。 |
| `UpdateTime` | 航迹更新的时间。单位为秒。 |
| `Age` | 航迹更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于已确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，以 1×*K* 逻辑数组形式返回。*K* 是记录的最新航迹逻辑状态的数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack` (Automated Driving Toolbox)。

该模块仅输出已确认航迹，即在航迹初始化后的前 *N* 次更新中，该模块至少分配了 *M* 次检测的航迹。要指定值 *M* 和 *N*，请使用 **M-out-of-N 确认的 M 和 N** 参数。

#### 依赖关系

要启用此端口，请在**参数**选项卡上，将**生成目标报告的格式**设置为 `Tracks`。

### **Detections** — 包含 MATLAB 结构的 Simulink 总线，用于未聚类目标检测

未聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

对于未聚类检测，该模块输出所有检测结果，一个目标可以有多个检测。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器，例如 Multi-Object Tracker (Automated Driving Toolbox) 模块，并生成航迹。

该结构必须包含以下字段：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测的数量 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时刻请求更新时为 False | Boolean |
| `Detections` | 目标检测 | 目标检测结构的数组，其长度由 **Maximum number of target reports** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数所使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 以 **Coordinate frame used to report detections** 参数指定的直角坐标系报告。
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
| `TargetIndex` | 生成该检测的参与者 `ActorID` 的标识符。对于虚警，该值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **Coordinate frame used to report detections** 参数设置为 `Body` 时，父坐标系为自车车身。当您将 **Coordinate frame used to report detections** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系为传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量值的坐标系。当 `Frame` 设置为 `'rectangular'` 时，检测结果以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测结果以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的三维向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的姿态。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖

要启用此端口，请在**参数**选项卡上，将**生成目标报告的格式**设置为
`Detections`。
## 参数
```yaml
parameters:
- name: 传感器标识符
  summary: 唯一传感器标识符 1（默认）| 正整数
  group: 安装
- name: 父级名称
  summary: 父级载具名称 Scene Origin（默认）| 载具名称
  group: 安装
- name: 坐标系
  summary: 用于对象变换的坐标系 Default（默认）| MATLAB | ISO8855 | AERO | VRML | SAE
  group: 安装
- name: Mounting location
  summary: 传感器安装位置 Origin（默认）
  group: 安装
- name: Specify offset
  summary: 指定相对于安装位置的偏移 off（默认） | on
  group: 安装
- name: Relative translation [X, Y, Z]
  summary: 相对于安装位置的平移偏移 [0, 0, 0]（默认） | 实值 1×3 向量
  group: 安装
- name: Relative rotation [Roll, Pitch, Yaw]
  summary: 相对于安装位置 [0, 0, 0]（默认）| 实值 1×3 向量 的旋转偏移
  group: 安装
- name: Sample time
  summary: 采样时间 -1（默认）| 正标量
  group: 安装
- name: Enable elevation angle measurements
  summary: 使雷达能够测量目标仰角 on（默认）| off
  group: 参数
- name: Enable range rate measurements
  summary: 使雷达能够测量目标距离变化率 on（默认）| off
  group: 参数
- name: Add measurement noise to observations
  summary: 启用向雷达传感器测量添加噪声 on（默认）| off
  group: 参数
- name: Enable generation of reports from false observations
  summary: 启用从虚假观测生成报告 on（默认）| off
  group: 参数
- name: Maximum number of target reports
  summary: 检测或航迹的最大数量 50（默认）| 正整数
  group: 参数
- name: Format of generated target reports
  summary: 生成的目标报告格式 Clustered detections（默认）| Tracks | Detections
  group: 参数
- name: 用于报告检测的坐标系
  summary: 所报告检测的坐标系 Body（默认）| Sensor rectangular | Sensor spherical
  group: 参数
- name: 方位角分辨率 (deg)
  summary: 雷达的方位角分辨率 4（默认）| 正实数标量
  group: 测量
- name: 俯仰角分辨率 (deg)
  summary: 雷达的俯仰角分辨率 5（默认）| 正实数标量
  group: 测量
- name: 距离分辨率 (m)
  summary: 雷达的距离分辨率 2.5（默认）| 正实数标量
  group: 测量
- name: 距离变化率分辨率 (m/s)
  summary: 雷达的距离变化率分辨率 0.5（默认）| 正实数标量
  group: 测量
- name: 方位角偏置系数
  summary: 雷达的方位角偏置系数 0.1（默认）| 非负标量
  group: 测量
- name: 俯仰角偏置系数
  summary: 雷达的俯仰角偏置系数 0.1（默认）| 非负标量
  group: 测量
- name: 距离偏置系数
  summary: 距离偏置系数 0.05（默认）| 非负标量
  group: 测量
- name: Range rate bias fraction
  summary: 距离变化率偏差系数 0.05（默认）| 非负标量
  group: 测量
- name: Total angular field of view [AZ, EL] (deg)
  summary: 雷达的角视场 [20 5]（默认）| 形式为 [azfov,elfov] 的 1×2 正实值向量
  group: 测量
- name: Range limits [MIN, MAX] (m)
  summary: 雷达的最小和最大距离 [0 150]（默认）| 形式为 [min max] 的 1×2 非负实值向量
  group: 测量
- name: Range rate limits [MIN, MAX] (m/s)
  summary: 雷达的最小和最大距离变化率 (m/s) [-100 100]（默认）| 形式为 [min max] 的 1×2 实值向量
  group: 测量
- name: Detection probability
  summary: 检测目标的概率 0.9（默认）| 范围 (0, 1] 内的标量
  group: 测量
- name: False alarm rate
  summary: 虚警报告率 1e-06（默认）| 范围 [10–7, 10–3] 内的正实标量
  group: 测量
- name: Reference target range (m)
  summary: 给定检测概率的参考距离 100（默认）| 正实标量
  group: 测量
- name: Reference target RCS (dBsm)
  summary: 给定检测概率下的参考雷达截面积 0（默认）| 实数标量
  group: 测量
- name: Center frequency (Hz)
  summary: 雷达频段的中心频率 77e9（默认）| 正实数标量
  group: 测量
- name: Select method to specify initial seed
  summary: 指定随机数生成器种子的方法 Repeatable（默认）| Specify seed | Not repeatable
  group: 测量
- name: Initial seed
  summary: 随机数生成器种子 0（默认）| 小于 232 的非负整数
  group: 测量
- name: Actor types to oversample
  summary: 用于改进目标检测的 Actor 类型 Simulation 3D Vehicles（默认）| None | Simulation 3D Actors | All Actors
  group: 测量
```

### 安装

#### 传感器标识

### **传感器标识符** — 唯一传感器标识符 `1`（默认）| 正整数

唯一传感器标识符，指定为正整数。使用此参数可
区分多传感器系统中来自不同传感器的检测或航迹。为每个传感器指定唯一值。

### **父级名称** — 父级载具名称 `Scene Origin`（默认）| 载具名称

传感器安装到的父级名称，指定为 `Scene
Origin` 或模型中某个对象的名称。可供选择的对象名称
对应于模型中
仿真三维载具模块的 **Name** 参数。如果选择 `Scene
Origin`，该模块会将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **坐标系** — 用于对象变换的坐标系 `Default`（默认）| `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定对象在三维环境中用于
平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Simulink 3D Animation 中的坐标系。

**示例：** `MATLAB`

#### 传感器安装

### **Mounting location** — 传感器安装位置 `Origin`（默认）

传感器安装位置。

- 当 **Parent name** 为 `Scene
  Origin` 时，模块将传感器安装到场景原点。
  只能将 **Mounting location** 设置为
  `Origin`。在仿真期间，传感器保持
  静止。
- 当 **Parent name** 为车辆名称时，模块
  将传感器安装到表中描述的某个预定义安装位置。在仿真期间，
  传感器随车辆移动。例如，
  该表提供了 ISO 8855 标准坐标系中的安装位置。

  | Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
  | --- | --- | --- |
  | `Origin` | 前向传感器，安装在车辆原点，该原点位于地面上且位于车辆几何中心（参见 Coordinate Systems in Simulink 3D Animation）。 传感器安装在原点的车辆 | [0, 0, 0] |
  | `Front bumper`  `Front center` | 前向传感器，安装在前保险杠上  传感器安装在前保险杠的车辆 | [0, 0, 0] |
  | `Rear bumper`  `Rear center` | 后向传感器，安装在后保险杠上  传感器安装在后保险杠的车辆 | [0, 0, 180] |
  | `Right mirror` | 向下传感器，安装在右侧后视镜上  传感器安装在右侧后视镜的车辆 | [0, –90, 0] |
  | `Left mirror` | 向下传感器，安装在左侧后视镜上  传感器安装在左侧后视镜的车辆 | [0, –90, 0] |
  | `Rearview mirror` | 前向传感器，安装在车辆内部的后视镜上  传感器安装在后视镜的车辆 | [0, 0, 0] |
  | `Hood center` | 前向传感器，安装在发动机舱盖中心  传感器安装在发动机舱盖中心的车辆 | [0, 0, 0] |
  | `Roof center` | 前向传感器，安装在车顶中心  传感器安装在车顶中心的车辆 | [0, 0, 0] |

  传感器相对于车辆的
  *X*-*Y*-*Z* 安装
  位置取决于车辆类型。要
  指定车辆类型，请使用所安装传感器的
  Simulation 3D Vehicle
  with Ground Following 的 **Type** 参数。要获取
  某一车辆类型的
  *X*-*Y*-*Z* 安装
  位置，请参阅该车辆的参考页。

### **Specify offset** — 指定相对于安装位置的偏移 `off`（默认） | `on`

选择此参数可通过
**Relative translation [X, Y, Z]** 和 **Relative rotation
[Roll, Pitch, Yaw]** 参数指定相对于安装位置的偏移。

### **Relative translation [X, Y, Z]** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认） | 实值 1×3 向量

相对于传感器安装位置的平移偏移，指定为
形式为 [*X*, *Y*,
*Z*] 的实值 1×3 向量。

可以通过将 **Parent name**
设置为某辆车辆的名称，将传感器安装到该车辆上。原点是
**Mounting location** 参数中指定的安装位置。该原点不同于
车辆原点，车辆原点是车辆的几何中心。也可以通过将 **Parent name** 设置为
`Scene Origin`，将传感器安装到场景原点。

**Example:** `[0,0,0.01]`

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置 `[0, 0, 0]`（默认）| 实值 1×3 向量 的旋转偏移

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*,
*Pitch*, *Yaw*] 的实值 1×3 向量。Roll、pitch 和 yaw 分别是绕 *X*、*Y* 和
*Z* 轴的旋转角度。

您可以通过将 **Parent name**
设置为该载具的名称，将传感器安装到载具上。原点是在
**Mounting location** 参数中指定的安装位置。该原点不同于
载具原点，载具原点是载具的几何中心。您还可以通过将 **Parent name** 设置为
`Scene Origin`，将传感器安装到场景原点。

**示例：** `[0,0,10]`

### **Sample time** — 采样时间 `-1`（默认）| 正标量

模块的采样时间，以秒为单位，指定为正标量。3D 仿真
环境帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

#### 检测报告

### **Enable elevation angle measurements** — 使雷达能够测量目标仰角 `on`（默认）| `off`

选中此复选框以对能够估计目标
仰角的雷达传感器进行建模。

### **Enable range rate measurements** — 使雷达能够测量目标距离变化率 `on`（默认）| `off`

选中此复选框以使雷达能够测量目标
检测的距离变化率。

### **Add measurement noise to observations** — 启用向雷达传感器测量添加噪声 `on`（默认）| `off`

选择此参数以向雷达测量添加噪声。否则，
测量没有噪声。即使清除此参数，生成的检测输出 `MeasurementNoise` 字段中报告的测量噪声
协方差矩阵，仍表示当您选择 **Add noise to measurements** 时添加的测量噪声。

### **Enable generation of reports from false observations** — 启用从虚假观测生成报告 `on`（默认）| `off`

选择此参数以启用创建虚假警报雷达测量。如果
清除此参数，雷达仅报告实际检测。

### **Maximum number of target reports** — 检测或航迹的最大数量 `50`（默认）| 正整数

将传感器报告的检测或航迹的最大数量指定为正整数。传感器按距
传感器距离递增的顺序报告检测，直到达到此最大数量。

### **Format of generated target reports** — 生成的目标报告格式 `Clustered detections`（默认）| `Tracks` | `Detections`

生成的目标报告格式，指定为以下选项之一：

- `Clustered detections` — 该模块将目标
  报告生成为*聚类检测*，其中每个目标报告为单个检测，即未聚类目标
  检测的质心。该模块在 Clustered detections
  输出端口返回聚类检测。
- `Tracks` — 该模块将目标报告生成为
  *航迹*，即已经过跟踪滤波器处理的聚类检测。该模块在
  Tracks 输出端口返回聚类检测。
- `Detections` — 该模块将目标报告生成为
  *未聚类检测*，其中每个目标可以有
  多个检测。该模块在 Detections
  输出端口返回聚类检测。

### **用于报告检测的坐标系** — 所报告检测的坐标系 `Body`（默认）| `Sensor rectangular` | `Sensor spherical`

所报告检测的坐标系，指定为以下选项之一：

- `Body` — 检测以自车的矩形车身坐标系报告。
- `Sensor rectangular` — 检测以雷达传感器的矩形车身坐标系报告。
- `Sensor spherical` — 检测以球坐标系报告，该坐标系以雷达传感器为中心，并与雷达在自车上的朝向对齐。

### 测量

#### 分辨率设置

### **方位角分辨率 (deg)** — 雷达的方位角分辨率 `4`（默认）| 正实数标量

雷达的方位角分辨率，指定为正标量。*方位角分辨率*定义了雷达能够区分两个目标的最小方位角间隔。方位角分辨率通常为雷达方位角波束宽度的 3 dB 下降点。单位为度。

### **俯仰角分辨率 (deg)** — 雷达的俯仰角分辨率 `5`（默认）| 正实数标量

雷达的俯仰角分辨率，指定为正标量。*俯仰角分辨率*定义了雷达能够区分两个目标的最小俯仰角间隔。俯仰角分辨率通常为雷达俯仰角波束宽度的 3 dB 下降点。单位为度。

#### 依赖关系

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **距离分辨率 (m)** — 雷达的距离分辨率 `2.5`（默认）| 正实数标量

雷达的距离分辨率，以米为单位，指定为正实数标量。*距离分辨率*定义了雷达能够区分两个目标的最小距离间隔。单位为米。

### **距离变化率分辨率 (m/s)** — 雷达的距离变化率分辨率 `0.5`（默认）| 正实数标量

雷达的距离变化率分辨率，指定为正实数标量。*距离变化率分辨率*定义了雷达能够区分两个目标的最小距离变化率间隔。单位为米每秒。

#### 依赖关系

要启用此参数，请在 **Parameters** 选项卡上选中 **Enable range rate measurements** 复选框。

#### 偏置设置

### **方位角偏置系数** — 雷达的方位角偏置系数 `0.1`（默认）| 非负标量

雷达的方位角偏置系数，指定为非负标量。*方位角偏置*表示为 **Azimuth resolution (deg)** 参数中指定的方位角分辨率的一个分数。此值设定了雷达方位角精度的下界，且为无量纲量。

### **俯仰角偏置系数** — 雷达的俯仰角偏置系数 `0.1`（默认）| 非负标量

雷达的俯仰角偏置系数，指定为非负标量。*俯仰角偏置*表示为 **Elevation resolution (deg)** 参数中指定的俯仰角分辨率的一个分数。此值设定了雷达俯仰角精度的下界，且为无量纲量。

#### 依赖关系

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **距离偏置系数** — 距离偏置系数 `0.05`（默认）| 非负标量

雷达的距离偏置系数，指定为非负标量。距离偏置表示为 **Range resolution (m)** 属性所指定的距离分辨率的一个分数。此属性设定了雷达距离精度的下界，且为无量纲量。

### **Range rate bias fraction** — 距离变化率偏差系数 `0.05`（默认）| 非负标量

雷达的距离变化率偏差系数，指定为非负标量。距离变化率偏差表示为 **Range rate resolution (m/s)** 参数所指定的距离变化率分辨率的一个分数。此属性为雷达的距离变化率精度设定下界，且无量纲。

#### 依赖关系

要启用此参数，请选中 **Enable range rate measurements** 复选框。

#### 检测器设置

### **Total angular field of view [AZ, EL] (deg)** — 雷达的角视场 `[20 5]`（默认）| 形式为 `[azfov,elfov]` 的 1×2 正实值向量

雷达的角视场，指定为形式为 `[azfov elfov]` 的 1×2 正实值向量。视场定义了传感器所张的总角度范围。方位角视场 `azfov` 必须位于区间 (0, 360] 内。俯仰角视场 `elfov` 必须位于区间 (0, 180] 内。单位为度。

### **Range limits [MIN, MAX] (m)** — 雷达的最小和最大距离 `[0 150]`（默认）| 形式为 `[min max]` 的 1×2 非负实值向量

雷达的最小和最大距离，指定为形式为 `[min max]` 的 1×2 非负实值向量。雷达不会检测此范围之外的目标。最大距离 `max` 必须大于最小距离 `min`。单位为米。

### **Range rate limits [MIN, MAX] (m/s)** — 雷达的最小和最大距离变化率 (m/s) `[-100 100]`（默认）| 形式为 `[min max]` 的 1×2 实值向量

雷达的最小和最大距离变化率，指定为形式为 `[min max]` 的 1×2 实值向量。雷达不会检测此距离变化率范围之外的目标。最大距离变化率 `max` 必须大于最小距离变化率 `min`。单位为米每秒。

#### 依赖关系

要启用此参数，请选中 **Enable range rate measurements** 复选框。

### **Detection probability** — 检测目标的概率 `0.9`（默认）| 范围 (0, 1] 内的标量

检测目标的概率，指定为范围 (0, 1] 内的标量。此量定义了在 **Reference target range (m)** 参数所指定的参考检测距离处，检测具有由 **Reference target RCS (dBsm)** 参数所指定的雷达截面积的目标的概率。此量无量纲。

### **False alarm rate** — 虚警报告率 `1e-06`（默认）| 范围 [10–7, 10–3] 内的正实标量

每个雷达分辨率单元内的虚警报告率，指定为范围 [10–7, 10–3] 内的正实标量。该模块根据 **Azimuth resolution (deg)** 和 **Range resolution (m)** 参数确定分辨率单元，并且在启用时，还根据 **Elevation resolution (deg)** 和 **Range rate resolution (m/s)** 参数确定分辨率单元。此量无量纲。

### **Reference target range (m)** — 给定检测概率的参考距离 `100`（默认）| 正实标量

给定检测概率和给定参考雷达截面积 (RCS) 的参考距离，指定为正实标量。*参考距离* 是指具有由 **Reference target RCS (dBsm)** 参数所指定的雷达截面积的目标以由 **Detection probability** 参数所指定的检测概率被检测到的距离。单位为米。

### **Reference target RCS (dBsm)** — 给定检测概率下的参考雷达截面积 `0`（默认）| 实数标量

给定检测概率和参考距离下的参考雷达截面积（RCS），指定为实数标量。*参考 RCS* 是在指定 **Reference target range (m)** 参数值下，以 **Detection probability** 参数指定的概率检测到目标时的 RCS 值。值以 dBsm 表示。

### **Center frequency (Hz)** — 雷达频段的中心频率 `77e9`（默认）| 正实数标量

雷达频段的中心频率，指定为正标量。单位为 Hz。

#### 随机数生成器设置

### **Select method to specify initial seed** — 指定随机数生成器种子的方法 `Repeatable`（默认）| `Specify seed` | `Not repeatable`

设置随机数生成器种子的方法，为下表中的一个选项。

| 选项 | 描述 |
| --- | --- |
| `Repeatable` | 该模块在首次仿真时生成随机初始种子，并在所有后续仿真中复用该种子。选择此参数可从统计传感器模型生成可重复的结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 通过 **Initial seed** 参数指定您自己的随机初始种子以获得可重复的结果。 |
| `Not repeatable` | 该模块在每次仿真运行后生成新的随机初始种子。选择此参数可从统计传感器模型生成不可重复的结果。 |

### **Initial seed** — 随机数生成器种子 `0`（默认）| 小于 232 的非负整数

随机数生成器种子，指定为小于 232 的非负整数。

#### 依赖关系

要启用此参数，请将 **Select method to specify initial seed** 参数设置为 `Specify seed`。

#### 采样设置

### **Actor types to oversample** — 用于改进目标检测的 Actor 类型 `Simulation 3D Vehicles`（默认）| `None` | `Simulation 3D Actors` | `All Actors`

*自 R2025a 起*

选择 3D 环境中要改进目标检测的 actor 类型。此参数使传感器能够向指定的 actor 类型过采样射线，从而改进目标检测。将该参数设置为下表中的一个选项。

| 选项 | 描述 |
| --- | --- |
| `None` | 禁用改进的目标检测。 |
| `Simulation 3D Vehicles` | 在传感器视场内任何车辆周围启用改进的目标检测。 |
| `Simulation 3D Actors` | 在传感器视场内使用类或模块创建的任何 actor 周围启用改进的目标检测。 |
| `All Actors` | 在传感器视场内任何 actor 周围启用改进的目标检测。 |

有关目标检测的更多信息，请参阅 Target Detection。

#### 提示

- 向 3D 环境中的 actor 过采样射线可提高 actor 周围的检测精度，但需要更多计算资源。
## 所属库

Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a：启用改进的目标检测

使用 **Measurements** 选项卡中的 **Actor types to oversample** 参数，在指定的 actor 对象周围启用改进的目标检测。您可以将该参数设置为以下选项之一。

- `None`
- `Simulation 3D Vehicles`
- `Simulation 3D Actors`
- `All Actors`

### R2025a：设置坐标系参数

在 Simulation 3D Radar Data Generator 模块中设置 **Coordinate system** 参数，以表示 3D 环境中 actor 变换的坐标系。

## 描述

生成雷达传感器检测和航迹

**注意**

使用 Simulation 3D Radar Data Generator 模块仿真模型需要 Radar Toolbox。

Simulation 3D Radar Data Generator 模块从雷达传感器模型生成目标的检测报告和航迹报告。使用此模块可从 3D 仿真环境中的 actor 生成传感器数据。此环境使用 Epic Games® 的 Unreal Engine® 渲染。

Simulation 3D Radar Data Generator 模块可以生成带有附加随机噪声的聚类或非聚类检测，还可以生成虚警检测。您也可以生成航迹。使用 **Format of generated target reports** 参数指定目标输出为聚类检测、非聚类检测还是航迹。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Radar Data Generator 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Radar Data Generator 模块接收数据之前准备好数据。要检查模块执行顺序，请右键点击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- 仿真 3D 雷达数据生成器 — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order (Simulink)。

模块的 **Coordinate system** 参数指定 actor 变换在 3D 环境中的应用方式。模块的输出也遵循指定的坐标系。
