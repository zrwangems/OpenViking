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

### 输出

### **Clustered detections** — 聚类目标检测，包含 MATLAB® 结构的 Simulink® 总线

聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

使用聚类检测时，模块为每个目标输出单个检测，其中每个检测是该目标的未聚类检测的质心。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测数 | Nonnegative integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | Boolean |
| `Detections` | 目标检测 | 目标检测结构体数组，其长度由 **最大目标报告数** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器的初始化函数使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 以 **用于报告检测的坐标系** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和 `MeasurementNoise` 在基于传感器直角坐标系的球坐标系中报告。

**`Measurement` 和
`MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| `Body` | 下表显示坐标如何受 **启用距离变化率测量** 参数影响。  | **启用距离变化率测量** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | 下表显示坐标如何受 **启用仰角测量** 和 **启用距离变化率测量** 参数影响。  | **启用距离变化率测量** | **启用仰角测量** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |

对于 `ObjectAttributes`，下表描述用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的 actor `ActorID` 的标识符。对于虚警，此值为负。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **用于报告检测的坐标系** 参数设置为 `Body` 时，父坐标系为自车车身。当您将 **用于报告检测的坐标系** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系为传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量的坐标系。当 `Frame` 设置为 `'rectangular'` 时，检测以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的方位。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖项

要启用此端口，请在 **参数** 选项卡上，将 **生成目标报告的格式** 设置为 `Clustered detections`。

### **Tracks** — 目标航迹，包含 MATLAB 结构的 Simulink 总线

目标航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

下表显示结构字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数 |
| `Tracks` | 航迹结构体数组，其长度由 **最大航迹数** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

下表显示每个航迹结构的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新时的时间。单位为 seconds。 |
| `Age` | 航迹更新的次数。 |
| `State` | 更新时状态向量的值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1-by-*K* 逻辑数组。*K* 是记录的最新航迹逻辑状态数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认是真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回为 `true`。 |
| `ObjectAttributes` | 有关航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack` (Automated Driving Toolbox)。

该模块仅输出确认航迹，即在航迹初始化后的前 *N* 次更新期间，模块为其分配至少 *M* 个检测的航迹。要指定值 *M* 和 *N*，请使用 **M-out-of-N 确认的 M 和 N** 参数。

#### 依赖项

要启用此端口，请在 **参数** 选项卡上，将 **生成目标报告的格式** 设置为 `Tracks`。

### **Detections** — 未聚类目标检测，包含 MATLAB 结构的 Simulink 总线

未聚类目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

使用未聚类检测时，模块输出所有检测，一个目标可以有多个检测。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器（例如 Multi-Object Tracker (Automated Driving Toolbox) 模块），并生成航迹。

该结构必须包含以下字段：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 有效检测数 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | Boolean |
| `Detections` | 目标检测 | 目标检测结构体数组，其长度由 **最大目标报告数** 参数设置。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器的初始化函数使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于直角坐标，`Measurement` 和 `MeasurementNoise` 以 **用于报告检测的坐标系** 参数指定的直角坐标系报告。
- 对于球坐标，`Measurement` 和 `MeasurementNoise` 在基于传感器直角坐标系的球坐标系中报告。

**`Measurement` 和
`MeasurementNoise`**

| **坐标系** | `Measurement` 和 `MeasurementNoise` 坐标 |
| --- | --- |
| `Body` | 下表显示坐标如何受 **启用距离变化率测量** 参数影响。  | **启用距离变化率测量** | 坐标 | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | 下表显示坐标如何受 **启用仰角测量** 和 **启用距离变化率测量** 参数影响。  | **启用距离变化率测量** | **启用仰角测量** | 坐标 | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |

对于 `ObjectAttributes`，下表描述用于跟踪的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的 actor `ActorID` 的标识符。对于虚警，此值为负。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。当您将 **用于报告检测的坐标系** 参数设置为 `Body` 时，父坐标系为自车车身。当您将 **用于报告检测的坐标系** 设置为 `Sensor rectangular` 或 `Sensor spherical` 时，父坐标系为传感器。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量的坐标系。当 `Frame` 设置为 `'rectangular'` 时，检测以笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `Orientation` | 雷达传感器坐标系相对于父坐标系的方位。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含仰角分量。 |

#### 依赖项

要启用此端口，请在 **参数** 选项卡上，将 **生成目标报告的格式** 设置为 `Detections`。

## 参数

### 安装

#### 传感器标识

### **传感器标识符** — 唯一传感器标识符 `1`（默认） | positive integer

唯一传感器标识符，指定为 positive integer。使用此参数区分多传感器系统中来自不同传感器的检测或航迹。为每个传感器指定唯一值。

### **父级名称** — 父车辆的名称 `Scene Origin`（默认） | vehicle name

传感器安装到的父级名称，指定为 `Scene Origin` 或模型中某个 actor 的名称。您可以选择 actor 名称，它们对应于模型中 simulation 3D vehicle 模块的 **名称** 参数。如果选择 `Scene Origin`，模块将传感器放置在场景原点。

**示例：** `SimulinkVehicle1`

### **坐标系** — 用于 actor 变换的坐标系 `Default`（默认） | `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*自 R2025a 起*

指定 actor 在 3D 环境中用于平移和旋转的坐标系。

- `Default` – 世界坐标系
- `MATLAB` – MATLAB 坐标系
- `ISO8855` – ISO 8855 标准坐标系
- `AERO` – SAE 坐标系
- `VRML` – X3D ISO 标准坐标系
- `SAE` – SAE 坐标系

有关不同坐标系的更多详细信息，请参阅 Coordinate Systems in Simulink 3D Animation。

**示例：** `MATLAB`

#### 传感器安装

### **安装位置** — 传感器安装位置 `Origin`（默认）

传感器安装位置。

- 当 **父级名称** 为 `Scene Origin` 时，模块将传感器安装到场景原点。您只能将 **安装位置** 设置为 `Origin`。在仿真期间，传感器保持静止。
- 当 **父级名称** 为车辆名称时，模块将传感器安装到表中描述的预定义安装位置之一。在仿真期间，传感器随车辆移动。例如，下表提供了 ISO 8855 标准坐标系中的安装位置。

  | 安装位置 | 描述 | 相对于车辆原点的方位 [Roll, Pitch, Yaw] (deg) |
  | --- | --- | --- |
  | `Origin` | 前向传感器，安装到车辆原点，该原点位于地面上且位于车辆几何中心（请参阅 Coordinate Systems in Simulink 3D Animation）。 车辆，传感器安装在原点 | [0, 0, 0] |
  | `Front bumper`  `Front center` | 前向传感器，安装到前保险杠。 车辆，传感器安装在前保险杠 | [0, 0, 0] |
  | `Rear bumper`  `Rear center` | 后向传感器，安装到后保险杠。 车辆，传感器安装在后保险杠 | [0, 0, 180] |
  | `Right mirror` | 向下传感器，安装到右侧后视镜。 车辆，传感器安装在右侧后视镜 | [0, –90, 0] |
  | `Left mirror` | 向下传感器，安装到左侧后视镜。 车辆，传感器安装在左侧后视镜 | [0, –90, 0] |
  | `Rearview mirror` | 前向传感器，安装到车内后视镜。 车辆，传感器安装在后视镜 | [0, 0, 0] |
  | `Hood center` | 前向传感器，安装到引擎盖中心。 车辆，传感器安装在引擎盖中心 | [0, 0, 0] |
  | `Roof center` | 前向传感器，安装到车顶中心。 车辆，传感器安装在车顶中心 | [0, 0, 0] |

  传感器的 *X*-*Y*-*Z* 安装位置相对于车辆的位置取决于车辆类型。要指定车辆类型，请使用您将传感器安装到的 Simulation 3D Vehicle with Ground Following 的 **类型** 参数。要获取某车辆类型的 *X*-*Y*-*Z* 安装位置，请参阅该车辆的参考页。

### **指定偏移** — 指定相对于安装位置的偏移 `off`（默认） | `on`

选择此参数以使用 **相对平移 [X, Y, Z]** 和 **相对旋转 [Roll, Pitch, Yaw]** 参数指定相对于安装位置的偏移。

### **相对平移 [X, Y, Z]** — 相对于安装位置的平移偏移 `[0, 0, 0]`（默认） | real-valued 1-by-3 vector

相对于传感器安装位置的平移偏移，指定为形如 [*X*, *Y*, *Z*] 的 real-valued 1-by-3 vector。

您可以通过将 **父级名称** 设置为该车辆的名称来将传感器安装到车辆。原点是 **安装位置** 参数中指定的安装位置。此原点不同于车辆原点，车辆原点是车辆的几何中心。您还可以通过将 **父级名称** 设置为 `Scene Origin` 来将传感器安装到场景原点。

**示例：** `[0,0,0.01]`

### **Relative rotation [Roll, Pitch, Yaw]** — 相对于安装位置 `[0, 0, 0]` 的旋转偏移（默认） | real-valued 1-by-3 vector

相对于传感器安装位置的旋转偏移，指定为形式为 [*Roll*,
*Pitch*, *Yaw*] 的 real-valued 1-by-3 vector。Roll、pitch 和 yaw 分别是绕 *X*、*Y* 和 *Z* 轴旋转的角度。

可以通过将 **Parent name** 设置为该车辆的名称，将传感器安装到车辆上。原点是 **Mounting location** 参数中指定的安装位置。该原点不同于车辆原点，车辆原点是车辆的几何中心。还可以通过将 **Parent name** 设置为 `Scene Origin`，将传感器安装到场景原点。

**示例:** `[0,0,10]`

### **Sample time** — 采样时间 `-1`（默认） | positive scalar

模块的采样时间，以 seconds 为单位，指定为 positive scalar。3D 仿真环境帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，模块将从 Simulation 3D Scene Configuration 模块继承其采样时间。

### 参数

#### 检测报告

### **Enable elevation angle measurements** — 使雷达能够测量目标仰角 `on`（默认） | `off`

选中此复选框可对能够估计目标仰角的雷达传感器建模。

### **Enable range rate measurements** — 使雷达能够测量目标距离变化率 `on`（默认） | `off`

选中此复选框可使雷达测量目标检测的距离变化率。

### **Add measurement noise to observations** — 启用向雷达传感器测量添加噪声 `on`（默认） | `off`

选中此参数可向雷达测量添加噪声。否则，测量不含噪声。即使清除此参数，在生成的检测输出的 `MeasurementNoise` 字段中报告的测量噪声协方差矩阵仍表示当选择 **Add noise to measurements** 时添加的测量噪声。

### **Enable generation of reports from false observations** — 启用创建虚警雷达检测 `on`（默认） | `off`

选中此参数可启用创建虚警雷达测量。如果清除此参数，雷达仅报告实际检测。

### **Maximum number of target reports** — 检测或航迹的最大数量 `50`（默认） | positive integer

将传感器报告的检测或航迹的最大数量指定为 positive integer。传感器按距传感器距离递增的顺序报告检测，直到达到此最大数量。

### **Format of generated target reports** — 生成目标报告的格式 `Clustered detections`（默认） | `Tracks` | `Detections`

生成目标报告的格式，指定为以下选项之一：

- `Clustered detections` — 模块将目标报告生成为 *clustered detections*，其中每个目标报告为单个检测，该检测是未聚类目标检测的质心。模块在 Clustered detections 输出端口返回聚类检测。
- `Tracks` — 模块将目标报告生成为 *tracks*，这些是已经过跟踪滤波器处理的聚类检测。模块在 Tracks 输出端口返回聚类检测。
- `Detections` — 模块将目标报告生成为 *unclustered detections*，其中每个目标可以有多个检测。模块在 Detections 输出端口返回聚类检测。

### **Coordinate frame used to report detections** — 报告检测所用的坐标系 `Body`（默认） | `Sensor rectangular` | `Sensor spherical`

报告检测的坐标系，指定为以下选项之一：

- `Body` — 检测在自车的矩形车身坐标系中报告。
- `Sensor rectangular` — 检测在雷达传感器的矩形车身坐标系中报告。
- `Sensor spherical` — 检测在以雷达传感器为中心并与雷达在自车上的朝向对齐的球坐标系中报告。

### 测量

#### 分辨率设置

### **Azimuthal resolution (deg)** — 雷达的方位角分辨率 `4`（默认） | positive real scalar

雷达的方位角分辨率，指定为 positive scalar。*azimuth resolution* 定义雷达可区分两个目标的最小方位角间隔。方位角分辨率通常是雷达方位角波束宽度的 3 dB 下降点。单位为 degrees。

### **Elevation resolution (deg)** — 雷达的仰角分辨率 `5`（默认） | positive real scalar

雷达的仰角分辨率，指定为 positive scalar。*elevation resolution* 定义雷达可区分两个目标的最小仰角间隔。仰角分辨率通常是雷达仰角波束宽度的 3 dB 下降点。单位为 degrees。

#### 依赖项

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **Range resolution (m)** — 雷达的距离分辨率 `2.5`（默认） | positive real scalar

雷达的距离分辨率，以 meters 为单位，指定为 positive real scalar。*range resolution* 定义雷达可区分两个目标的最小距离间隔。单位为 meters。

### **Range rate resolution (m/s)** — 雷达的距离变化率分辨率 `0.5`（默认） | positive real scalar

雷达的距离变化率分辨率，指定为 positive real scalar。*range rate resolution* 定义雷达可区分两个目标的最小距离变化率间隔。单位为 meters per second。

#### 依赖项

要启用此参数，请在 **参数** 选项卡上选中 **Enable range rate measurements** 复选框。

#### 偏差设置

### **Azimuth bias fraction** — 雷达的方位角偏差系数 `0.1`（默认） | nonnegative scalar

雷达的方位角偏差系数，指定为 nonnegative scalar。*Azimuth bias* 表示为 **Azimuth resolution (deg)** 参数中指定的方位角分辨率的分数。此值设置雷达方位角精度的下界，并且是无量纲的。

### **Elevation bias fraction** — 雷达的仰角偏差系数 `0.1`（默认） | nonnegative scalar

雷达的仰角偏差系数，指定为 nonnegative scalar。*Elevation bias* 表示为 **Elevation resolution (deg)** 参数中指定的仰角分辨率的分数。此值设置雷达仰角精度的下界，并且是无量纲的。

#### 依赖项

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **Range bias fraction** — 距离偏差系数 `0.05`（默认） | nonnegative scalar

雷达的距离偏差系数，指定为 nonnegative scalar。距离偏差表示为 **Range resolution (m)** 属性指定的距离分辨率的分数。此属性设置雷达距离精度的下界，并且是无量纲的。

### **Range rate bias fraction** — 距离变化率偏差系数 `0.05`（默认） | nonnegative scalar

雷达的距离变化率偏差系数，指定为 nonnegative scalar。距离变化率偏差表示为 **Range rate resolution (m/s)** 参数指定的距离变化率分辨率的分数。此属性设置雷达距离变化率精度的下界，并且是无量纲的。

#### 依赖项

要启用此参数，请选中 **Enable range rate measurements** 复选框。

#### 检测器设置

### **Total angular field of view [AZ, EL] (deg)** — 雷达的角视场 `[20 5]`（默认） | 1-by-2 positive real-valued vector of form `[azfov,elfov]`

雷达的角视场，指定为形式为 `[azfov elfov]` 的 1-by-2 positive real-valued vector。视场定义传感器覆盖的总角度范围。方位角视场 `azfov` 必须位于区间 (0, 360]。仰角视场 `elfov` 必须位于区间 (0, 180]。单位为 degrees

### **Range limits [MIN, MAX] (m)** — 雷达的最小和最大距离 `[0 150]`（默认） | 1-by-2 nonnegative real-valued vector of form `[min max]`

雷达的最小和最大距离，指定为形式为 `[min max]` 的 1-by-2 nonnegative real-valued vector。雷达不检测此范围之外的目标。最大距离 `max` 必须大于最小距离 `min`。单位为 meters。

### **Range rate limits [MIN, MAX] (m/s)** — 雷达的最小和最大距离变化率 (m/s) `[-100 100]`（默认） | 1-by-2 real-valued vector of form `[min max]`

雷达的最小和最大距离变化率，形式为 `[min max]` 的 1-by-2 real-valued vector。雷达不检测此距离变化率之外的目标。最大距离变化率 `max` 必须大于最小距离变化率 `min`。单位为 meters per second。

#### 依赖项

要启用此参数，请选中 **Enable range rate measurements** 复选框。

### **Detection probability** — 检测目标的概率 `0.9`（默认） | scalar in range (0, 1]

检测目标的概率，指定为区间 (0, 1] 内的 scalar。此量定义检测具有雷达截面积的目标的概率，其中雷达截面积由 **Reference target RCS (dBsm)** 参数在 **Reference target range (m)** 参数指定的参考检测距离处指定。单位为无量纲。

### **False alarm rate** — 虚警报告率 `1e-06`（默认） | positive real scalar in range [10–7, 10–3]

每个雷达分辨率单元内的虚警报告率，指定为区间 [10–7,
10–3] 内的 positive real scalar。模块根据 **Azimuth resolution (deg)** 和 **Range resolution (m)** 参数确定分辨率单元，并在启用时根据 **Elevation resolution (deg)** 和 **Range rate resolution (m/s)** 参数确定。单位为无量纲。

### **Reference target range (m)** — 给定检测概率下的参考距离 `100`（默认） | positive real scalar

给定检测概率和给定参考雷达截面积 (RCS) 下的参考距离，指定为 positive real scalar。*reference range* 是目标被检测到的距离，该目标具有由 **Reference target RCS (dBsm)** 参数指定的雷达截面积，并以由 **Detection probability** 参数指定的检测概率被检测到。单位为 meters。

### **Reference target RCS (dBsm)** — 给定检测概率下的参考雷达截面积 `0`（默认） | real scalar

给定检测概率和参考距离下的参考雷达截面积 (RCS)，指定为 real scalar。*reference RCS* 是目标被检测到的 RCS 值，检测概率由 **Detection probability** 参数指定，距离为指定的 **Reference target range (m)** 参数值。值以 dBsm 表示。

### **Center frequency (Hz)** — 雷达频带的中心频率 `77e9`（默认） | positive real scalar

雷达频带的中心频率，指定为 positive scalar。单位为 Hz。

#### 随机数生成器设置

### **Select method to specify initial seed** — 指定随机数生成器种子 `Repeatable`（默认） | `Specify seed` | `Not repeatable` 的方法

设置随机数生成器种子的方法，为表中选项之一。

| Option | Description |
| --- | --- |
| `Repeatable` | 模块在第一次仿真时生成随机初始种子，并在所有后续仿真中重用此种子。选择此参数可从统计传感器模型生成可重复结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 通过 **Initial seed** 参数指定您自己的随机初始种子以获得可复现结果。 |
| `Not repeatable` | 模块在每次仿真运行后生成新的随机初始种子。选择此参数可从统计传感器模型生成不可重复结果。 |

### **Initial seed** — 随机数生成器种子 `0`（默认） | nonnegative integer less than 232

随机数生成器种子，指定为小于 232 的 nonnegative integer。

#### 依赖项

要启用此参数，请将 **Select method to specify initial seed** 参数设置为 `Specify seed`。

#### 采样设置

### **Actor types to oversample** — 用于改进目标检测的 actor 类型 `Simulation 3D Vehicles`（默认） | `None` | `Simulation 3D Actors` | `All Actors`

*自 R2025a 起*

选择 3D 环境中要围绕其改进目标检测的 actor 类型。此参数使传感器能够向指定的 actor 类型过采样射线，从而改进目标检测。将参数设置为表中选项之一。

| Option | Description |
| --- | --- |
| `None` | 禁用改进的目标检测。 |
| `Simulation 3D Vehicles` | 在传感器视场内的任何车辆周围启用改进的目标检测。 |
| `Simulation 3D Actors` | 在传感器视场内的任何使用类或模块创建的 actor 周围启用改进的目标检测。 |
| `All Actors` | 在传感器视场内的任何 actor 周围启用改进的目标检测。 |

有关目标检测的详细信息，请参阅 Target Detection。

#### 提示

- 向 3D 环境中的 actor 过采样射线可提高 actor 周围的检测精度，并且需要更多计算资源。

## 所属库

Simulink 3D Animation / Simulation 3D / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

### R2025a: 启用改进的目标检测

使用 **测量** 选项卡中的 **Actor types to oversample** 参数启用围绕指定 actor 对象的改进目标检测。可以将该参数设置为以下选项之一。

- `None`
- `Simulation 3D Vehicles`
- `Simulation 3D Actors`
- `All Actors`

### R2025a: 设置坐标系参数

在 Simulation 3D Radar Data Generator 模块中设置 **Coordinate system** 参数，以表示 3D 环境中 actor 变换的坐标系。

## 描述

生成雷达传感器检测和航迹

**注意**

使用 Simulation 3D Radar Data Generator 模块对模型进行仿真需要 Radar Toolbox。

Simulation 3D Radar Data Generator 模块从雷达传感器模型生成目标的检测报告和航迹报告。使用此模块从 3D 仿真环境中的 actor 生成传感器数据。此环境使用 Epic Games® 的 Unreal Engine® 渲染。

Simulation 3D Radar Data Generator 模块可生成带有附加随机噪声的聚类或非聚类检测，还可生成虚警检测。还可生成航迹。使用 **Format of generated target reports** 参数指定目标输出为聚类检测、非聚类检测还是航迹。

**提示**

Simulation 3D Scene Configuration 模块必须在 Simulation 3D Radar Data Generator 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Radar Data Generator 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Radar Data Generator — `1`

有关执行顺序的更多信息，请参阅 Control and Display Execution Order (Simulink)。

模块的 **Coordinate system** 参数指定 actor 变换在 3D 环境中的应用方式。模块的输出也遵循指定的坐标系。
