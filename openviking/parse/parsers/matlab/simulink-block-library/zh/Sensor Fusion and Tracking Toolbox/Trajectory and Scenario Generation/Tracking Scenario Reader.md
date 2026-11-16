---
type: simulink-block
title: 'Tracking Scenario Reader'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Trajectory and Scenario Generation'
documentation_page: 'trackingscenarioreader'
documentation_source_path: 'ref/trackingscenarioreader.html'
language: zh-CN
chinese_source: worker-translation
---

# Tracking Scenario Reader

## 端口

### 输入

### **Platform Poses** — 平台位姿信息，由包含 MATLAB® 结构体的 Simulink® 总线表示

平台位姿信息，指定为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumPlatforms` | 有效平台数，指定为非负整数。 |
| `Platforms` | 平台，指定为平台位姿结构体数组。这些结构体中的前 `NumPlatforms` 个是实际平台位姿。 |

每个平台结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `PlatformID` | 唯一平台标识符，指定为正整数。 |
| `ClassID` | 平台分类标识符，指定为非负整数 |
| `Position` | 平台的位置，指定为 3 元素实值向量。 - 如果场景的 `IsEarthCentered` 属性设置为 `false`，则将位置指定为三元素 Cartesian 状态 [`x`, `y`, `z`]，单位为 meters。 - 如果场景的 `IsEarthCentered` 属性设置为 `true`，则将位置指定为三元素 geodetic 状态：`latitude` 以 degrees 为单位，`longitude` 以 degrees 为单位，`altitude` 以 meters 为单位。 |
| `Velocity` | 平台的速度，指定为 3 元素实值向量，单位为 m/s。 |
| `Acceleration` | 平台的加速度，指定为 3 元素实值向量，单位为 m/s2。 |
| `Orientation` | 平台相对于局部场景坐标系的姿态，指定为 3×3 旋转矩阵。 |
| `AngularVelocity` | 平台相对于局部场景坐标系的角速度，指定为 3 元素实值向量，单位为 degrees per second。 |

在将平台位姿指定为输入之前，必须在场景中预定义每个平台。当无法在场景中预定义平台属性（例如其位置）时，请使用此输入。例如，在场景运行期间，为了实现碰撞避免，根据其他平台的位置来定义平台位置。选择此选项会禁用除默认 **Platforms** 和 **Simulation Time** 输出端口之外的所有模块输出端口。

#### 依赖关系

要启用此端口，请在 **Scenario** 选项卡中，将 **Source of platform pose** 参数选择为 `Input port`。

### 输出

### **Platforms** — 场景中平台的信息，由包含 MATLAB 结构体的 Simulink 总线表示

场景中平台的信息，返回为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumPlatforms` | 有效平台数，返回为非负整数。 |
| `Platforms` | 平台，返回为平台位姿结构体数组。这些结构体中的前 `NumPlatforms` 个是实际平台位姿。 |

每个平台结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `PlatformID` | 唯一平台标识符，返回为正整数。 |
| `ClassID` | 平台分类标识符，返回为非负整数 |
| `Position` | 平台的位置，返回为 3 元素实值向量。 - 如果场景的 `IsEarthCentered` 属性设置为 `false`，则位置返回为三元素 Cartesian 状态 [`x`, `y`, `z`]，单位为 meters。 - 如果场景的 `IsEarthCentered` 属性设置为 `true`，则位置返回为三元素 geodetic 状态：`latitude` 以 degrees 为单位，`longitude` 以 degrees 为单位，`altitude` 以 meters 为单位。 |
| `Velocity` | 平台的速度，返回为 3 元素实值向量，单位为 m/s。 |
| `Acceleration` | 平台的加速度，返回为 3 元素实值向量，单位为 m/s2。 |
| `Orientation` | 平台相对于局部场景坐标系的姿态，返回为 3×3 旋转矩阵。 |
| `AngularVelocity` | 平台相对于局部场景坐标系的角速度，返回为 3 元素实值向量，单位为 degrees per second。 |

如果在 **Output Setting** 选项卡中选择 **Include profiles information with platforms** 参数，则平台结构体还包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `Dimensions` | 平台尺寸和原点偏移，返回为结构体。该结构体包含近似平台尺寸的长方体的 `Length`、`Width`、`Height` 和 `OriginOffset`。`OriginOffset` 是从长方体中心到平台坐标系原点的位置向量。有关更多详细信息，请参阅 `Platform` 的 `Dimensions` 属性。 |
| `Mesh` | 平台的网格，返回为结构体。 |

网格结构体包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `NumVertices` | 有效顶点数，返回为正整数。 |
| `Vertices` | 平台网格的顶点，返回为 *N*-by-3 实值矩阵，其中 *N* 是场景中所有平台网格的最大顶点数。每行的第一个、第二个和第三个元素分别表示每个顶点的 x-、y- 和 z-位置。 |
| `NumFaces` | 有效面数，返回为正整数。 |
| `Faces` | 平台网格的面，返回为 *M*-by-3 正整数矩阵，其中 *M* 是场景中所有平台网格的最大面数。每行中的三个元素是构成三角形面的三个顶点的顶点 ID。顶点的 ID 是其在 `Vertices` 字段中指定的对应行号。 |

### **Simulation Time** — 当前仿真时间，非负标量

当前仿真时间，返回为非负标量，单位为 seconds。

### **Coverage Configurations** — 场景中的覆盖配置，由包含 MATLAB 结构体的 Simulink 总线表示

场景中的覆盖配置，返回为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumConfigurations` | 有效覆盖配置数，返回为非负整数。 |
| `Configurations` | 覆盖配置，返回为覆盖配置结构体数组。这些结构体中的前 `NumConfigurations` 个是实际覆盖配置。 |

每个覆盖配置结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `Index` | 唯一的传感器或发射器索引，对于传感器返回为正整数，对于发射器返回为负整数。 |
| `LookAngle` | 传感器或发射器的当前视轴角，如果传感器或发射器在方位角和俯仰角两个方向扫描，则返回为二元素向量 [`azimuth`; `elevation`]，单位为 degrees。如果传感器仅在方位角方向扫描，则第二个元素返回为 `NaN`。 |
| `FieldOfView` | 传感器或发射器的视场，返回为 2-by-2 实值矩阵，单位为 degrees。如果传感器是 lidar 传感器，则第一行返回方位角下限和上限，第二行返回俯仰角下限和上限。对于其他类型的传感器或发射器，第一列包含方位角和俯仰角视场，第二列返回为 `NaN`。 |
| `ScanLimits` | 传感器或发射器从其安装姿态起可以扫描的最小和最大角度，如果传感器或发射器在方位角和俯仰角两个方向扫描，则返回为 2-by-2 矩阵 [`minAz`, `maxAz`; `minEl`, `maxEl`]，单位为 degrees。如果传感器仅在方位角方向扫描，则 `minEl` 和 `maxEl` 返回为 `NaN`。 |
| `Range` | 传感器或发射器的波束和覆盖区域的距离，返回为标量，单位为 meters。 |
| `Position` | 传感器或发射器的原点位置，返回为三元素向量 [`x`, `y`, `z`]，单位为 meters。 |
| `Orientation` | 从场景坐标系到传感器或发射器安装坐标系的旋转变换，返回为旋转矩阵。 |

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择 **Coverage** 参数。

### **Detections** — 检测列表，由包含 MATLAB 结构体的 Simulink 总线表示

检测列表，返回为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumDetections` | 检测数，返回为非负整数。 |
| `Detections` | 目标检测，返回为目标检测结构体数组。这些检测中的前 `NumDetections` 个是实际检测。 |

每个目标检测结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `Time` | 测量时间，返回为正标量。 |
| `Measurement` | 目标测量值，返回为实值向量。 |
| `MeasurementNoise` | 测量噪声协方差矩阵，返回为正定矩阵。 |
| `SensorIndex` | 传感器的唯一 ID，返回为正整数。 |
| `ObjectClassID` | 目标分类 ID，返回为非负整数。 |
| `MeasurementParameters` | 测量参数，返回为结构体。 |
| `ObjectAttributes` | 传递给跟踪器的附加信息，返回为结构体。 |

有关这些字段的更详细说明，请参阅 `objectDetection`。

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择 **Detections** 参数。

### **Sensor Configuratons** — 场景中的传感器配置，由包含 MATLAB 结构体的 Simulink 总线表示

场景中的传感器配置，返回为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumConfigurations` | 有效传感器配置数，返回为非负整数。 |
| `Configurations` | 传感器配置，返回为覆盖配置结构体数组。这些结构体中的前 `NumConfigurations` 个是实际传感器配置。 |

每个传感器配置结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `SensorIndex` | 唯一传感器标识符，返回为正整数。 |
| `IsValidTime` | 指示传感器是否应在当前时间至少报告一次检测，返回为 `false` 或 `true`。 |
| `IsScanDone` | 指示传感器是否已完成当前扫描，返回为 `false` 或 `true`。 |
| `FieldOfView` | 传感器或发射器的视场，返回为 2-by-2 实值矩阵，单位为 degrees。如果传感器是 lidar 传感器，则第一行返回方位角下限和上限，第二行返回俯仰角下限和上限。对于其他类型的传感器或发射器，第一列包含方位角和俯仰角视场，第二列返回为 `NaN`。 |
| `MeasurementParameters` | 传感器测量参数，返回为结构体数组，其中包含将场景坐标系中的位置和速度变换到当前传感器坐标系所需的坐标坐标系变换。有关更多详细信息，请参阅 `objectDetection` 对象的 `MeasurementParameters` 属性。 |

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择 **Sensor** 参数。

### **Emissions** — 场景中的雷达和声纳发射，由包含 MATLAB 结构体的 Simulink 总线表示

场景中的雷达和声纳发射，返回为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumEmissions` | 有效发射数，返回为非负整数。 |
| `Emissions` | 发射，返回为发射结构体数组。这些结构体中的前 `NumEmissions` 个是实际发射。 |

每个发射结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `PlatformID` | 平台标识符，返回为正整数。 |
| `EmitterIndex` | 发射器标识符，返回为正整数。 |
| `OriginPosition` | 发射器的位置，返回为 1-by-3 实值向量，单位为 meters。 |
| `OriginVelocity` | 发射器的速度，返回为 1-by-3 实值向量，单位为 m/s。 |
| `Orientation` | 发射器相对于局部场景坐标系的姿态，返回为 3×3 旋转矩阵。 |
| `FieldOfView` | 发射器的视场，返回为二元素向量 [`azimuth` `elevation`]，单位为 degrees。 |
| `EIRP` | 雷达发射的有效各向同性辐射功率，对于雷达发射返回为标量，单位为 dB；对于声纳发射返回为 `NaN`。 |
| `RCS` | 累积雷达横截面，对于雷达发射返回为标量，单位为 dBsm；对于声纳发射返回为 `NaN`。 |
| `CenterFrequency` | 信号的中心频率，返回为正标量，单位为 Hz。 |
| `BandWidth` | 信号的半功率带宽，返回为正标量，单位为 Hz。 |
| `WaveformType` | 波形类型标识符，返回为非负整数。 |
| `ProcessingGain` | 与信号波形相关的处理增益，返回为标量，单位为 dB。 |
| `PropagationRange` | 信号已传播的总距离，返回为非负标量，单位为 meters。对于直接路径信号，该距离为零。 |
| `PropagationRangeRate` | 信号已传播路径的总距离变化率，返回为标量，单位为 m/s。对于直接路径信号，距离变化率为零。 |
| `SourceLevel` | 发射信号的累积源级，对于声纳发射返回为标量，单位为 dB per micro-pascal；对于雷达发射返回为 `NaN`。发射信号的累积源级（以 decibels 为单位）相对于均方根压力为 1 micro-pascal 的声波强度。 |
| `TargetStrength` | 发射信号的源平台的累积目标强度，对于声纳发射返回为标量，单位为 dB；对于雷达发射返回为 `NaN`。 |

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择 **Emissions** 参数。

### **Emitter Configurations** — 场景中的发射器配置，由包含 MATLAB 结构体的 Simulink 总线表示

场景中的发射器配置，返回为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumConfigurations` | 有效发射器配置数，返回为非负整数。 |
| `Configurations` | 发射器配置，返回为发射器配置结构体数组。这些结构体中的前 `NumConfigurations` 个是实际发射器配置。 |

每个发射器配置的字段为：

| 字段 | 描述 |
| --- | --- |
| `EmitterIndex` | 唯一发射器标识符，返回为正整数。 |
| `IsValidTime` | 指示传感器的发射状态，返回为 `false` 或 `true`。 |
| `IsScanDone` | 指示发射器是否已完成其当前扫描，返回为 `false` 或 `true`。 |
| `FieldOfView` | 发射器的视场，指定为二元素向量 [`azimuth`; `elevation`]，单位为 degrees。 |
| `MeasurementParameters` | 发射器测量参数，返回为结构体数组，其中包含将场景坐标系中的位置和速度变换到当前发射器坐标系所需的坐标坐标系变换。有关更多详细信息，请参阅 `objectDetection` 对象的 `MeasurementParameters` 属性。 |

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择 **Emitter** 参数。

### **Point Clouds** — 包含 MATLAB 结构的点云 Simulink 总线

点云，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumPointClouds` | 有效点云的数量，返回为非负整数。 |
| `PointClouds` | 点云，返回为点云结构体数组。这些点云结构体中的前 `NumPointClouds` 个表示实际点云。 |

每个点云结构体的字段为：

| 字段 | 描述 |
| --- | --- |
| `NumPoints` | `Points` 字段中有效点的数量，返回为非负整数。 |
| `Points` | 从激光雷达报告的未组织点，返回为 *N*×3 实值矩阵，其中 *N* 是场景中所有激光雷达传感器的最大点数。前 `NumPoints` 行表示由激光雷达生成的实际点。 |
| `Clusters` | `Points` 字段中点的簇标签，返回为非负整数的 *N*×2 矩阵，其中 *N* 是场景中所有激光雷达传感器的最大点数。前 `NumPoint` 行表示点的实际簇标签。对于矩阵的每一行，第一个元素表示生成该点的目标的 `PlatformID`，第二个元素表示目标的 `ClassID`。 |

有关详细信息，请参阅 `monostaticLidarSensor`。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **点云** 参数。

## 参数

### 场景

### **场景源** — 跟踪场景源 `trackingScenario`（默认）| `Tracking Scenario Designer session file`

将跟踪场景源指定为以下选项之一：

- `trackingScenario` — 在 **工作区变量名称** 参数中，指定表示 `trackingScenario` 对象的 MATLAB 工作区变量的名称。
- `Tracking Scenario Designer session file` — 在 **会话文件** 参数中，指定从 Tracking Scenario Designer 应用保存的会话文件的名称。

### **工作区变量名称** — 工作区变量名称 `trackingScenario` 变量名称

将工作区变量名称指定为 MATLAB 工作区中 `trackingScenario` 对象的名称。

如果更改跟踪场景的定义，请使用 **场景** 选项卡上的 **刷新场景数据** 按钮更新场景。

#### 依赖关系

要启用此参数，请将 **场景源** 参数设置为 `trackingScenario`。

### **会话文件** — 会话文件 `Tracking Scenario Designer` 会话文件名称

将会话文件指定为从 Tracking Scenario Designer 应用保存的会话文件的名称。

如果更改会话文件，请使用 **场景** 选项卡上的 **刷新场景数据** 按钮更新文件。

#### 依赖关系

要启用此参数，请将 **场景源** 参数设置为 `Tracking Scenario Designer session file`。

### **平台位姿源** — 平台位姿源 `Scenario`（默认）| `Input port`

选择平台位姿源为

- `Scenario` — 使用由 **工作区变量名称** 或 **会话文件** 参数指定的场景中定义的平台位姿。
- `Input port` — 使用 **Platform poses** 输入端口指定平台位姿。当无法在场景中预定义平台属性（例如其位置）时，选择此选项。例如，在场景运行期间，根据其他平台的位置定义平台位置以实现碰撞避免。此外，选择此选项将禁用除默认 **Platforms** 和 **Simulation Time** 输出端口之外的所有模块输出端口。

### **采样时间 (s)** — 仿真采样时间 `0.1`（默认）| 正实数标量

将仿真采样时间指定为以 seconds 为单位的正实数标量。不支持继承采样时间和连续采样时间。

此采样时间会覆盖 `trackignScenario` 对象或 Tracking Scenario Designer 应用会话文件中定义的采样时间。要获得与场景源相同或相似的输出，请根据 `trackignScenario` 对象或 Tracking Scenario Designer 应用会话文件中定义的采样时间定义此参数。

### **报告平台位姿的坐标系** — 报告平台位姿的坐标系 `Cartesian`（默认）| `Geodetic`

将报告平台位姿的坐标系指定为

- `Cartesian` — 将每个平台位置报告为相对于场景坐标系的 3 元素笛卡尔位置坐标，以 meters 为单位。
- `Geodetic` — 将每个平台位置报告为 3 元素大地坐标：纬度（以 degrees 为单位）、经度（以 degrees 为单位）和海拔（以 meters 为单位）。要选择此选项，必须将 **场景源** 参数指定为 `trackingScenario`，并将场景的 `IsEarthCentered` 属性设置为 `true`。

### 输出设置

#### 平台

### **在平台中包含轮廓信息** — 在平台中包含轮廓信息 `off`（默认）| `on`

选择此参数可在 **Platforms** 输出中包含平台轮廓信息，包括平台尺寸和网格。

#### 传感器和发射器

### **检测** — 启用检测输出端口 `off`（默认）| `on`

选择此参数以启用 **Detections** 输出端口。

#### 依赖关系

要启用此参数，请在 **场景** 选项卡上将 **平台位姿源** 参数选择为 `Scenario`。

### **点云** — 启用点云输出端口 `off`（默认）| `on`

选择此参数以启用 **Point Clouds** 输出端口。

#### 依赖关系

要启用此参数，请在 **场景** 选项卡上将 **平台位姿源** 参数选择为 `Scenario`。

### **发射** — 启用发射输出端口 `off`（默认）| `on`

选择此参数以启用 **Emissions** 输出端口。

#### 依赖关系

要启用此参数，请在 **场景** 选项卡上将 **平台位姿源** 参数选择为 `Scenario`。

### **在发射传播中启用遮挡** — 在发射传播中启用遮挡 `on`（默认）| `off`

选择此参数以启用在发射传播中来自平台的信号遮挡。

#### 依赖关系

要启用此参数，请选择 **发射** 参数。

#### 配置

### **覆盖范围** — 启用覆盖范围配置输出端口 `off`（默认）| `on`

选择此参数以启用 **Coverage Configurations** 输出端口。

#### 依赖关系

要启用此参数，请在 **场景** 选项卡上将 **平台位姿源** 参数选择为 `Scenario`。

### **传感器** — 启用传感器配置输出端口 `off`（默认）| `on`

选择此参数以启用 **Sensor Configurations** 输出端口。

#### 依赖关系

要启用此参数，请在 **场景** 选项卡上将 **平台位姿源** 参数选择为 `Scenario`。

### **发射器** — 启用发射器配置输出端口 `off`（默认）| `on`

选择此参数以启用 **Emitter Configurations** 输出端口。

#### 依赖关系

要启用此参数，请在 **场景** 选项卡上将 **平台位姿源** 参数选择为 `Scenario`。

#### 随机数生成器设置

### **随机数生成** — 生成随机数种子的方法 `Repeatable`（默认）| `Not repeatable` | `Specify seed`

将生成随机数种子的方法选择为 `Repeatable`、`Not repeatable` 或 `Specify seed`。当选择为

- `Repeatable` — 模块每次使用相同的随机种子。
- `Not repeatable` — 模块每次使用不同的随机种子。
- `Specify seed` — 使用 **初始种子** 参数为模块指定随机种子。

#### 依赖关系

要启用此参数，请选择 **检测**、**点云** 或 **发射** 参数。

### **初始种子** — 用于随机化的初始种子 `0`（默认）| 非负整数

将模块中用于随机化的初始种子指定为非负整数。

#### 依赖关系

要启用此参数，请将 **随机数生成** 参数选择为 `Specify seed`。

### 总线设置

#### 平台

### **平台总线名称源** — 平台位姿总线名称来源 `Auto`（默认）| `Property`

将 **Platforms** 输出端口中返回的平台位姿总线名称来源指定为以下选项之一：

- `Auto` — 模块自动创建平台位姿总线名称。
- `Property` — 使用 **指定平台总线名称** 参数指定平台位姿总线名称。

### **指定平台总线名称** — 指定平台总线名称 `BusPlatforms`（默认）| 有效总线名称

将 **Platforms** 输出端口中返回的平台位姿总线名称指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **平台总线名称源** 参数选择为 `Property`。

### **最大平台数量源** — 最大平台数量来源 `Auto`（默认）| `Property`

将跟踪场景中可拥有的最大平台数量来源指定为以下选项之一：

- `Auto` — 模块将最大平台数量设置为跟踪场景中的平台数量。
- `Property` — 使用 **最大平台数量** 参数指定最大平台数量。

### **最大平台数量** — 最大平台数量 `50`（默认）| 正整数

将最大平台数量指定为正整数。

#### 依赖关系

要启用此参数，请将 **最大平台数量源** 参数设置为 `Property`。

#### 检测

### **检测总线名称源** — 检测总线名称来源 `Auto`（默认）| `Property`

将 **Detections** 输出端口中返回的检测总线名称来源指定为以下选项之一：

- `Auto` — 模块自动创建检测总线名称。
- `Property` — 使用 **指定检测总线名称** 参数指定检测总线名称。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **检测** 参数。

### **指定检测总线名称** — 指定检测总线名称 `BusDetection`（默认）| 有效总线名称

将 **Detections** 输出端口中返回的检测总线名称指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **检测总线名称源** 参数选择为 `Property`。

### **最大检测数量源** — 最大平台数量来源 `Auto`（默认）| `Property`

将可以从跟踪场景生成的最大检测数量来源指定为以下选项之一：

- `Auto` — 模块将最大检测数量设置为跟踪场景中生成的检测数量。
- `Property` — 使用 **最大检测数量** 参数指定最大检测数量。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **检测** 参数。

### **最大检测数量** — 最大检测数量 `50`（默认）| 正整数

将最大检测数量指定为正整数。

#### 依赖关系

要启用此参数，请将 **最大检测数量源** 参数设置为 `Property`。

#### 点云

### **点云总线名称源** — 点云总线名称来源 `Auto`（默认）| `Property`

将 **Point Clouds** 输出端口中返回的点总线名称来源指定为以下选项之一：

- `Auto` — 模块自动创建点云总线名称。
- `Property` — 使用 **指定点云总线名称** 参数指定点云总线名称。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **点云** 参数。

### **指定点云总线名称** — 指定点云总线名称 `BusPointCloud`（默认）| 有效总线名称

将 **Point Clouds** 输出端口中返回的点云总线名称指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **点云总线名称源** 参数选择为 `Property`。

### **最大激光雷达传感器数量** — 最大激光雷达传感器数量 `10`（默认）| 正整数

将最大激光雷达传感器数量指定为正整数。

#### 依赖关系

要启用此参数，请将 **最大激光雷达传感器数量源** 参数设置为 `Property`。

### **最大激光雷达传感器数量源** — 最大激光雷达传感器数量来源 `Auto`（默认）| `Property`

将跟踪场景中可拥有的最大激光雷达传感器数量来源指定为以下选项之一：

- `Auto` — 模块将最大激光雷达传感器数量设置为跟踪场景中的激光雷达传感器数量。
- `Property` — 使用 **最大激光雷达传感器数量** 参数指定最大检测数量。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **点云** 参数。

#### 发射

### **发射总线名称源** — 发射总线名称来源 `Auto`（默认）| `Property`

将 **Emissions** 输出端口中返回的发射总线名称来源指定为以下选项之一：

- `Auto` — 模块自动创建发射总线名称。
- `Property` — 使用 **指定发射总线名称** 参数指定发射总线名称。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **发射** 参数。

### **指定发射总线名称** — 指定发射总线名称 `BusEmission`（默认）| 有效总线名称

将 **Emissions** 输出端口中返回的发射总线名称指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **发射总线名称源** 参数选择为 `Property`。

### **最大发射数量源** — 最大发射数量来源 `Auto`（默认）| `Property`

将可以从跟踪场景生成的最大发射数量来源指定为以下选项之一：

- `Auto` — 模块将最大发射数量设置为跟踪场景中生成的发射数量。
- `Property` — 使用 **最大发射数量** 参数指定最大发射数量。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **发射** 参数。

### **最大发射数量** — 最大发射数量 `50`（默认）| 正整数

将最大发射数量指定为正整数。

#### 依赖关系

要启用此参数，请将 **最大发射数量源** 参数设置为 `Property`。

#### 配置

### **覆盖范围配置总线名称源** — 覆盖范围配置总线名称来源 `Auto`（默认）| `Property`

将 **Coverage Configurations** 输出端口中返回的覆盖范围配置总线名称来源指定为以下选项之一：

- `Auto` — 模块自动创建覆盖范围配置总线名称。
- `Property` — 使用 **指定覆盖范围配置总线名称** 参数指定覆盖范围配置总线名称。

#### 依赖关系

要启用此端口，请在 **输出设置** 选项卡中，选择 **覆盖范围** 参数。

### **指定覆盖范围配置总线名称** — 指定覆盖范围配置总线名称 `BusCovConf`（默认）| 有效总线名称

将 **Coverage Configurations** 输出端口中返回的覆盖范围配置总线名称指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **Source of coverage configuration
bus name** 参数选择为 `Property`。

### **Source of sensor configuration bus name** — 传感器配置总线的名称来源 `Auto`（默认） | `Property`

指定在 **Sensor Configurations** 输出端口中返回的传感器配置总线的名称来源，为以下选项之一：

- `Auto` — 该模块自动创建传感器配置总线名称。
- `Property` — 使用 **Specify sensor configuration bus name**
  参数指定传感器配置总线名称。

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择
**Sensor** 参数。

### **Specify sensor configuration bus name** — 指定传感器配置总线名称 `BusSensorConf`（默认） | 有效总线名称

将 **Sensor Configurations** 输出端口中返回的传感器配置总线名称指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **Source of sensor configuration
bus name** 参数选择为 `Property`。

### **Source of emitter configuration bus name** — 发射器配置总线的名称来源 `Auto`（默认） | `Property`

指定在 **Emitter Configurations** 输出端口中返回的发射器配置总线的名称来源，为以下选项之一：

- `Auto` — 该模块自动创建发射器配置总线名称。
- `Property` — 使用 **Specify emitter configuration bus name**
  参数指定发射器配置总线名称。

### **Specify emitter configuration bus name** — 指定发射器配置总线名称 `BusEmitterConf`（默认） | 有效总线名称

将 **Emitter Configurations** 输出端口中返回的发射器配置总线名称指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **Source of emitter configuration
bus name** 参数选择为 `Property`。

### **Source of maximum number of sensors** — 最大传感器数量的来源 `Auto`（默认） | `Property`

指定跟踪场景中可拥有的最大传感器数量的来源，为以下选项之一：

- `Auto` — 该模块将最大发射数量设置为跟踪场景中的传感器数量。
- `Property` — 使用 **Maximum number of sensors** 参数指定最大传感器数量。

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择
**Coverage** 或 **Sensor** 参数。

### **Maximum number of sensors** — 最大传感器数量 `10`（默认） | 正整数

将最大传感器数量指定为正整数。

#### 依赖关系

要启用此参数，请将 **Source of maximum number of
sensors** 参数设置为 `Property`。

### **Source of maximum number of emitters** — 最大发射器数量的来源 `Auto`（默认） | `Property`

指定跟踪场景中可拥有的最大发射器数量的来源，为以下选项之一：

- `Auto` — 该模块将最大发射器数量设置为跟踪场景中的发射器数量。
- `Property` — 使用 **Maximum number of emitters** 参数指定最大发射器数量。

#### 依赖关系

要启用此端口，请在 **Output Settings** 选项卡中选择
**Emitter** 或 **Sensor** 参数。

### **Maximum number of emitters** — 最大发射器数量 `10`（默认） | 正整数

将最大发射器数量指定为正整数。

#### 依赖关系

要启用此参数，请将 **Source of maximum number of
emitters** 参数设置为 `Property`。

## 所属库

Sensor Fusion and Tracking Toolbox / Tracking Scenario and Sensor Models

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2023a：Simulink 总线不在工作区中显示

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

读取跟踪场景并生成仿真数据

`Tracking Scenario Reader` 模块读取 `trackingScenario`
对象或 Tracking Scenario Designer
会话文件，并输出平台位姿和仿真时间。您可以将该模块配置为
可选地输出场景中的检测、点云、发射、传感器和发射器配置以及
传感器覆盖范围。
