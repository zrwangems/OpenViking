---
type: simulink-block
title: 'Grid-Based Multi Object Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'gridbasedmultiobjecttracker'
documentation_source_path: 'ref/gridbasedmultiobjecttracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Grid-Based Multi Object Tracker

## 端口

### 输入

### **Sensor Data** — 包含 MATLAB® 结构的传感器数据 Simulink® 总线

传感器数据，指定为包含 MATLAB 结构的 Simulink 总线。该结构包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `NumSensors` | 传感器数量，指定为非负整数。 |
| `SensorData` | 传感器数据，指定为传感器数据结构体数组。数组的前 `NumSensors` 个元素为实际检测。 |

每个 `SensorData` 结构体包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `Time` | 测量时间，指定为非负标量。 |
| `SensorIndex` | 传感器的唯一标识符，指定为正整数。 |
| `Measurement` | 目标测量值，指定为 *K*×*M* 矩阵。*K* 为每个测量值的维度，*M* 为测量值的数量。每个测量值定义检测在矩形坐标系或球坐标系中的位置信息。 |
| `MeasurementParameters` | 测量参数，指定为描述从粒子状态到测量值变换的结构体。有关设置此字段的详细信息，请参阅 `objectDetection` 对象的 `MeasurementParameter` 属性。 |
| `NumMeasurements` | 测量值数量或点云传感器检测中的点数，指定为正整数。 |

**注意**

每个结构体的 `Time` 字段必须小于或等于模块当前调用时刻的时间。该时间还必须大于模块上一次调用时指定的更新时间。

### **Prediction Time** — 航迹更新时间 实数标量

航迹更新时间，指定为以秒为单位的实数标量。跟踪器将所有航迹更新到该时间。每次调用模块时，更新时间必须递增，且必须至少等于指定给 **Sensor Data** 输入端口的最大 `Time` 值。

如果未启用此端口，则由 Simulink 管理的仿真时钟确定更新时间。

#### 依赖

要启用此端口，请在 **Port Setting** 选项卡中，将 **Prediction time source** 参数设置为 `Input port`。

### **Sensor Configurations** — 跟踪传感器的配置 包含 MATLAB 结构的 Simulink 总线

跟踪传感器的配置，指定为包含 MATLAB 结构的 Simulink 总线。该结构包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `NumConfigurations` | 传感器配置数量，指定为正整数。 |
| `Configurations` | 传感器配置，指定为传感器配置结构体数组。数组的前 `NumConfigurations` 个元素为实际配置。字段名称和定义必须分别对应于 `trackingSensorConfiguration` 对象属性的名称和值。即使您在结构体中指定了 `FilterInitializationFcn`、`SensorTransformFcn` 和 `MaxNumDetsPerObject` 字段，跟踪器也会忽略它们。如果您在跟踪系统中使用 Radar Data Generator (Radar Toolbox) 模块，则可以直接使用 Radar Data Generator (Radar Toolbox) 模块的 **Configuration** 输出来指定此值。 |

#### 依赖

要启用此端口，请在 **Tracker Configuration** 选项卡中，选择 **Update sensor configurations with time** 参数。

### **State Parameters** — 跟踪状态参数 包含 MATLAB 结构的 Simulink 总线

跟踪状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该模块使用此结构作为所生成航迹的 `StateParameters` 字段的值。您可以使用这些参数来定义模块报告航迹时所参照的参考坐标系，以及所生成航迹的其他所需属性。

例如，您可以使用包含以下字段的结构来定义一个矩形参考坐标系，其原点位置为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒，相对于场景坐标系。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **Tracker Configuration** 选项卡中，选择 **Update track state parameters with time** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹 包含 MATLAB 结构的 Simulink 总线

更新到当前时间的确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of tracks** 参数设定。只有数组的前 `NumTracks` 个元素是实际航迹。 |

航迹结构的字段如航迹结构所示。每条航迹的状态形式遵循 **Motion model for tracking** 参数中指定的形式。

### **Tentative Tracks** — 暂定航迹 包含 MATLAB 结构的 Simulink 总线

更新到当前时间的暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在被确认之前为暂定航迹。

该结构包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of tracks** 参数设定。只有数组的前 `NumTracks` 个元素是实际航迹。 |

航迹结构的字段如航迹结构所示。每条航迹的状态形式遵循 **Motion model for tracking** 参数中指定的形式。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable tentative tracks output**。

### **All Tracks** — 确认和暂定航迹 包含 MATLAB 结构的 Simulink 总线

更新到当前时间的确认和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。

该结构包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of tracks** 参数设定。只有数组的前 `NumTracks` 个元素是实际航迹。 |

航迹结构的字段如航迹结构所示。每条航迹的状态形式遵循 **Motion model for tracking** 参数中指定的形式。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable all tracks output**。

## 参数

#### Tracker Configuration

### **Tracker identifier** — 唯一跟踪器标识符 `0`（默认）| 非负整数

将唯一跟踪器标识符指定为非负整数。此参数作为跟踪器输出中的 `SourceIndex` 传递，用于区分多跟踪器系统中来自不同跟踪器的航迹。要将航迹输出用作 Track-To-Track Fuser 模块的输入，必须将此属性指定为正整数。

**示例：** `1`

### **Maximum number of tracks** — 最大航迹数量 `100`（默认）| 正整数

模块可以维护的最大航迹数量，指定为正整数。

### **Maximum number of sensors** — 最大传感器数量 `20`（默认）| 正整数

将可连接到跟踪器的最大传感器数量指定为正整数。`MaxNumSensors` 必须大于或等于用于更新该模块的所有传感器数据中 `SensorIndex` 的最大值。

**数据类型：** `single` | `double`

### **Sensor configurations** — 跟踪传感器的配置 `struct('SensorIndex',1,'IsValidTime',true,'SensorLimits',[-180 180; 0 100])`（默认）| 结构体 | 结构体数组

将跟踪传感器的配置指定为结构体或结构体数组。此参数向跟踪器提供跟踪传感器配置信息，例如传感器检测限制和传感器分辨率。您必须为每个结构体指定以下字段：

| 字段名称 | 格式 |
| --- | --- |
| `SensorIndex` | 传感器的唯一标识符，指定为正整数。 |
| `IsValidTime` | 指示是否应使用传感器数据来更新航迹，指定为 `true` 或 `false`。 |
| `SensorTransformParameters` | 传感器变换函数的参数，指定为 *p* 元素测量参数结构体数组。*p* 是传感器数量。每个结构体应包含与测量函数（例如 `cvmeas` 函数）中使用的测量参数同名的字段。第一个结构体必须描述从自主系统到传感器坐标系的变换。后续结构体描述从自主系统到跟踪坐标系的变换。如果只提供一个结构体，跟踪器假定跟踪在自主系统的坐标系中执行。 |
| `SensorLimits` | 传感器检测限制，指定为 2×2 矩阵。第一行指定方位角的下限和上限，单位为度。第二行指定检测范围的下限和上限，单位为米。 |

每个结构体允许的其他字段名称对应于 `trackingSensorConfiguration` 对象的属性名称。跟踪器会忽略 `FilterInitializationFcn`、`SensorTransformFcn` 和 `MaxNumDetsPerObject` 字段，即使您在结构体中指定了它们。

在选择 **Update sensor configurations with time** 参数后，您可以通过 **Sensor configurations** 输入端口更新配置。

### **Update sensor configurations with time** — 随时间更新传感器配置 `off`（默认）| `on`

选择此参数以启用 **Sensor Configurations** 输入端口。这使您能够在仿真期间更新跟踪传感器配置。

### **Track state parameters** — 航迹状态参考系的参数 结构体

将航迹状态参考系的参数指定为结构体。该模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义该模块报告航迹时所使用的参考系，以及所生成航迹的其他所需属性。

例如，您可以使用包含以下字段的结构体来定义一个矩形参考系，其原点位置相对于场景坐标系为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

您可以通过选择 **Update track state parameters with time** 参数，经由 **State Parameters** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **Update track state parameters with time** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数以启用通过 **State Parameters** 输入端口输入航迹状态参数的端口。

### **Enable GPU computation** — 启用 GPU 计算 `off`（默认）| `on`

选择此参数以启用 GPU 来估计动态网格地图。启用 GPU 计算需要 Parallel Computing Toolbox™。

### **X-dimension of grid** — 网格 X 维度 `100`（默认）| 正标量

以正标量指定局部坐标系中网格的 X 维度，单位为米。

### **Y-dimension of grid** — 网格 Y 维度 `100`（默认）| 正标量

以正标量指定局部坐标系中网格的 Y 维度，单位为米。

### **Resolution of grid** — 网格分辨率 `1`（默认）| 正标量

以正标量指定网格的分辨率。分辨率表示网格在 X 方向和 Y 方向上每米的单元格数。

### **Grid origin** — 网格原点 `[-50 -50]`（默认）| 正标量

以双元素标量向量指定局部坐标系中网格的原点，单位为米。

### **Simulate using** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。

#### Particle Filtering

### **Motion model for tracking** — 用于跟踪的运动模型 `constant-velocity`（默认）| `constant-acceleration` | `constant-turnrate`

选择用于跟踪的运动模型为 `constant-velocity`、`constant-acceleration` 或 `constant-turnrate`。

每种运动模型的粒子状态和目标状态为：

| 运动模型 | 粒子状态 | 目标状态 |
| --- | --- | --- |
| `constant-velocity` | `[x; vx; y; vy]` | `[x; vx; y; vy; yaw; L; W]` |
| `constant-acceleration` | `[x; vx; ax; y; vy; ay]` | `[x; vx; ax; y; vy; ay; yaw; L; W]` |
| `constant-turn-rate` | `[x; vx; y; vy; w]` | `[x; vx; y; vy; w; yaw; L; W]` |

其中：

- `x` — 目标在局部跟踪坐标系 X 方向上的位置（m）
- `y` — 目标在局部跟踪坐标系 Y 方向上的位置（m）
- `vx` — 目标在局部跟踪坐标系 X 方向上的速度（m/s）
- `vy` — 目标在局部跟踪坐标系 Y 方向上的速度（m/s）
- `ax` — 目标在局部跟踪坐标系 X 方向上的加速度（m/s2）
- `ay` — 目标在局部跟踪坐标系 Y 方向上的加速度（m/s2）
- `w` — 目标在局部跟踪坐标系中的偏航角速度（deg/s）
- `yaw` — 目标在局部跟踪坐标系中的偏航角（deg）
- `L` — 目标长度（m）
- `W` — 目标宽度（m）

### **Minimum and maximum velocity of objects (m/s)** — 目标的最小和最大速度（m/s）`[-10 10; -10 10]`（默认）| 2×2 标量矩阵

以 2×2 标量矩阵指定目标的最小和最大速度，单位为 m/s。第一行指定 X 方向上的速度下限和上限，第二行指定 Y 方向上的速度下限和上限。跟踪器使用这些限制通过均匀分布在网格中采样新粒子。

### **Enable additive process noise** — 启用加性过程噪声 `false`（默认）| `true`

选择此参数以将过程噪声建模为加性。选中后，过程噪声直接添加到状态向量中。否则，噪声将纳入运动模型中。

### **过程噪声协方差矩阵** — 过程噪声协方差矩阵 `eye(2)`（默认）| *N*×*N* 矩阵

将过程噪声协方差指定为 *N*×*N* 矩阵。该参数指定粒子位置和目标几何中心的过程噪声。

- 如果选择 **Enable additive process noise** 参数，则过程噪声直接添加到预测模型中。在这种情况下，*N* 等于 **Motion model for tracking** 参数中粒子状态的维度。
- 如果不选择 **Enable additive process noise** 参数，则根据所选运动模型定义过程噪声。该模型将过程噪声添加到高阶项，例如 `constant-velocity` 模型的加速度。

  | `MotionModel` | 加速度项数 | 项的含义 |
  | --- | --- | --- |
  | `constant-velocity` | `2` | x 和 y 方向的加速度 |
  | `constant-acceleration` | `2` | x 和 y 方向的加加速度 |
  | `constant-turn-rate` | `3` | x 和 y 方向的加速度，以及角加速度 |

**示例：** `[1.0 0.05; 0.05 2]`

### **持久粒子数** — 持久粒子数 `1e5`（默认）| 正整数

将每个网格的持久粒子数指定为正整数。较高的粒子数可以提高估计质量，但会增加计算成本。

### **每步新生粒子数** — 每步新生粒子数 `1e4`（默认）| 正标量

将每个时间步的新生（初始化）粒子数指定为正整数。跟踪器通过使用预测和更新后的占用置信质量之间的不匹配以及 **Probability of birth in a cell per step** 参数来确定这些新生粒子的位置。该参数的合理值约为 **Number of persistent particles** 参数所指定粒子数的 10%。

### **每步单元内出生概率** — 每步单元内出生概率 `0.01`（默认）| 范围 `[0, 1)` 内的标量

将每步单元内目标出生概率指定为范围 `[0, 1)` 内的标量。出生概率控制单元内生成新粒子的概率。

**示例：** `1e-4`

### **单位时间内目标死亡率** — 单位时间内目标死亡率 `1e-3`（默认）| 正标量

将单位时间内目标死亡率指定为正标量。死亡率表示粒子或目标在每个时间步后消失的可能性。死亡率（*P*d）影响分量在连续时间步中的生存概率（*P*s），如下所示：

Ps=(1−Pd)ΔT

其中 *Δ**T* 是时间步数。

**示例：** `1e-4`

### **自由空间预测置信度** — 自由空间预测置信度 `0.8`（默认）| 标量

将自由空间预测置信度指定为标量。在跟踪器的预测阶段，该参数将单元处于“自由”（未占用）状态的置信质量降低为：

mk|k−1(F)=αΔTmk−1(F)

其中 *k* 是时间步索引，*m* 是置信质量，*α* 是表示自由空间预测置信度的因子，*Δ**T* 是时间步。

### **随机数生成** — 随机数种子生成方法 `Repeatable`（默认）| `Not repeatable` | `Specify seed`

选择随机数种子生成方法为 `Repeatable`、`Not repeatable` 或 `Specify seed`。

- `Repeatable` — 该模块每次使用相同的随机种子。
- `Not repeatable` — 该模块每次使用不同的随机种子。
- `Specify seed` — 使用 **Initial Seed** 参数为该模块指定随机种子。

### **初始种子** — 随机化初始种子 `0`（默认）| 非负整数

将该模块中用于随机化的初始种子指定为非负整数。

#### 依赖关系

要启用此参数，请将 **Random number generation** 参数选择为 `Specify seed`。

#### 航迹管理

### **Clustering method for new object extraction** — 新目标提取的聚类方法 `DBSCAN`（默认）| `Custom`

指定用于新目标提取的聚类方法，可选 `DBSCAN` 或 `Custom`。

- `DBSCAN` — 使用基于密度的带噪声应用空间聚类（DBSCAN）算法对未分配的动态网格单元进行聚类。您可以通过指定 **Threshold for DBSCAN clustering** 和 **Minimum number of cells per cluster for DBSCAN** 参数来配置 DBSCAN 算法。
- `Custom` — 使用在 **Name of 'Custom' clustering function** 参数中指定的自定义聚类函数对未分配的动态网格单元进行聚类。

### **Threshold for DBSCAN clustering** — DBSCAN 聚类的阈值 `5`（默认）| 正标量

将 DBSCAN 聚类的阈值指定为正标量。

#### 依赖关系

要启用此参数，请将 **Clustering method for new object extraction** 参数选择为 `DBSCAN`。

### **Minimum number of cells per cluster for DBSCAN** — DBSCAN 每个聚类的最小单元数 `2`（默认）| 正整数

将 DBSCAN 每个聚类的最小单元数指定为正整数。此参数影响 DBSCAN 算法中一个点是否为核心点。

#### 依赖关系

要启用此参数，请将 **Clustering method for new object extraction** 参数选择为 `DBSCAN`。

### **Name of 'Custom' clustering function** — 自定义聚类函数的名称 函数名

将用于对未分配网格单元进行聚类的自定义函数名称指定为函数名。该函数必须支持以下签名：

```
function indices = myFunction(dynamicGridCells)
```

其中 `dynamicGridCells` 是一个结构体，用于定义初始化航迹的一组网格单元。它必须包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `Width` | 单元的宽度，指定为正标量。 |
| `GridIndices` | 网格单元的索引，指定为 *N*×2 数组，其中 *N* 是未分配单元的数量。第一个元素指定 x 方向的网格索引，第二个元素指定 y 方向的网格索引。 |
| `State` | 网格单元的状态，指定为 *P*×*N* 的标量数组，其中 *P* 是状态的维度，*N* 是未分配单元的数量。 |
| `StateCovariance` | 网格单元的状态协方差，指定为 *P*×*P*×*N* 的标量数组，其中 *P* 是状态的维度，*N* 是未分配单元的数量。 |
| `OccupancyMass` | 单元的占用置信质量，指定为 *N* 元素向量，其中 *N* 是未分配单元的数量。 |
| `FreeMass` | 单元的自由置信质量，指定为 *N* 元素向量，其中 *N* 是未分配单元的数量。 |

自定义函数必须返回 `indices`，其为 *N* 元素索引向量，用于定义每个动态网格单元的聚类索引。

#### 依赖关系

要启用此参数，请将 **Clustering method for new object extraction** 参数选择为 `Custom`。

### **Function to initialize tracks from grid cell sets** — 用于从网格单元集合初始化航迹的函数 `trackerGridRFS.defaultTrackInitialization`（默认）| 函数名

指定用于初始化新航迹的函数名称。初始化函数从一组动态网格单元中初始化一条航迹。

默认初始化函数合并来自各单元的高斯估计，以描述目标的状态。目标的朝向与其平均速度的方向对齐。在定义了朝向的情况下，利用单元的几何属性提取目标的长度和宽度。该模块使用线性近似计算长度、宽度和朝向估计的不确定性。

如果选择使用自己的初始化函数，该函数必须支持以下签名：

```
function track = myFunction(dynamicGridCells)
```

其中 `dynamicGridCells` 是一个结构体，定义了一组用于初始化航迹的网格单元。它具有以下字段：

| 字段 | 描述 |
| --- | --- |
| `Width` | 单元的宽度，指定为正标量。 |
| `GridIndices` | 网格单元的索引，指定为 *N*×2 数组，其中 *N* 是未分配单元的数量。第一个元素指定 x 方向的网格索引，第二个元素指定 y 方向的网格索引。 |
| `State` | 网格单元的状态，指定为 *P*×*N* 的标量数组，其中 *P* 是状态的维度，*N* 是未分配单元的数量。 |
| `StateCovariance` | 网格单元的状态协方差，指定为 *P*×*P*×*N* 的标量数组，其中 *P* 是状态的维度，*N* 是未分配单元的数量。 |
| `OccupancyMass` | 单元的占用置信质量，指定为 *N* 元素向量，其中 *N* 是未分配单元的数量。 |
| `FreeMass` | 单元的自由置信质量，指定为 *N* 元素向量，其中 *N* 是未分配单元的数量。 |

自定义函数必须将 `track` 返回为 `objectTrack` 对象，或返回一个结构体，其字段名与 `objectTrack` 对象的属性名相对应。状态的维度必须与 **Motion model for tracking** 参数中指定的状态维度相同。

**示例：** `myFunction`

### **用于更新现有航迹的函数** — 用于更新现有航迹的函数 `trackerGridRFS.defaultTrackUpdate`（默认）| 函数名

指定用于通过航迹关联的动态网格单元集合来更新现有航迹的函数名称。

默认更新函数使用与航迹关联的动态网格单元的新估计来更新航迹的 `State` 和 `StateCovariance` 字段。更新过程类似于 **用于从网格单元集合初始化航迹的函数** 参数的初始化过程。跟踪器不对状态和状态协方差应用滤波。

如果选择自定义更新函数，该函数必须支持以下签名：

```
function updatedTrack = TrackUpdateFcn(predictedTrack,dynamicGridCells)
```

其中：

- `predictedTrack` 是目标的预测航迹，指定为 `objectTrack` 对象。
- `dynamicGridCells` 是定义与航迹关联的一组动态网格单元的结构体。该结构体具有以下字段：

  | 字段 | 描述 |
  | --- | --- |
  | `Width` | 单元的宽度，指定为正标量。 |
  | `GridIndices` | 网格单元的索引，指定为 *N*×2 数组，其中 *N* 是未分配单元的数量。第一个元素指定 x 方向的网格索引，第二个元素指定 y 方向的网格索引。 |
  | `State` | 网格单元的状态，指定为 *P*×*N* 的标量数组，其中 *P* 是状态的维度，*N* 是未分配单元的数量。 |
  | `StateCovariance` | 网格单元的状态协方差，指定为 *P*×*P*×*N* 的标量数组，其中 *P* 是状态的维度，*N* 是未分配单元的数量。 |
  | `OccupancyMass` | 单元的被占据置信质量，指定为 *N* 元素向量，其中 *N* 是未分配单元的数量。 |
  | `FreeMass` | 单元的空闲置信质量，指定为 *N* 元素向量，其中 *N* 是未分配单元的数量。 |
- `updatedTrack` 是更新后的航迹，返回为 `objectTrack` 对象或具有与 `objectTrack` 对象属性名称对应字段名的结构体。

**示例：** `TrackUpdateFcn`

### **将动态网格单元分配给航迹的阈值** — 将动态网格单元分配给航迹的阈值 `30`（默认）| 正标量

指定将动态网格单元分配给航迹的阈值，指定为正标量。只有当动态网格单元到航迹的距离（由负对数似然表示）小于此参数的值时，该动态网格单元才能关联到航迹。

- 如果动态单元未被分配到应分配到的航迹，则增大阈值。
- 如果动态单元被分配到不应分配到的航迹，则减小阈值。

**示例：** `18.1`

### **确认阈值 [M N]** — 航迹确认阈值 `[2 3]`（默认）| 1×2 正整数向量

指定航迹确认阈值，指定为 1×2 正整数向量 `[M N]`。如果在最近 `N` 次更新中至少有 `M` 次更新分配到了动态网格单元，则航迹被确认。

### **删除阈值 [P Q]** — 航迹删除阈值 `[5 5]`（默认）| 1×2 正整数向量

指定航迹删除阈值，指定为 1×2 正整数向量 `[P Q]`。如果在最近 `Q` 次更新中至少有 `P` 次更新未分配到任何动态网格单元，则航迹被删除。

**示例：** `0.01`

**数据类型：** `single` | `double`

#### 可视化

### **启用动态网格地图可视化** — 启用动态网格地图可视化 `on`（默认）| `off`

选择此参数以启用动态网格地图可视化。如果当前存在坐标轴，模块将在当前坐标轴上显示动态地图。否则，模块将创建一个坐标轴来显示地图。

### **Plot velocity** — 启用速度绘图 `off`（默认）| `on`

选择此参数以在动态网格地图上启用速度绘图。

### **Fast update** — 启用从上一地图更新 `on`（默认）| `off`

选择此参数以启用从上一地图更新。选中时，该模块通过轻量级更新图中上一地图来绘制地图。否则，该模块每次在图上绘制新地图。

### **Invert colors** — 启用反转颜色 `off`（默认）| `on`

选择此参数以在地图上启用反转颜色。选中时，该模块将空白区域绘制为白色，将占用区域绘制为黑色。否则，该模块将空白区域绘制为黑色，将占用区域绘制为白色。

#### 端口设置

### **Prediction time source** — 预测时间来源 `Input port`（默认）| `Auto`

将预测时间的来源指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **Enable tentative tracks output** — 启用暂定航迹输出端口 `off`（默认）| `on`

选择此参数以通过 **Tentative Tracks** 输出端口启用暂定航迹的输出。

### **Enable all tracks output** — 启用所有航迹输出端口 `off`（默认）| `on`

选择此参数以通过 **All Tracks** 输出端口启用所有航迹的输出。

### **Source of output bus name** — 输出航迹总线名称的来源 `Auto`（默认）| `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 该模块自动创建输出航迹总线名称。
- `Property` — 通过 **Specify an output bus name** 参数指定输出航迹总线名称。

## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 网格地图的可视化不支持代码生成。

## 版本历史

**在 R2021b 中引入**

### R2023a：Simulink 总线不显示在工作区中

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

使用随机有限集方法的基于网格的多目标跟踪器

Grid-Based Multi Object Tracker 是一种跟踪器，能够处理 2-D 环境中来自多个传感器的多个目标的检测。该跟踪器使用高分辨率传感器数据（如点云和雷达检测）跟踪自主系统周围的动态对象。该跟踪器使用基于随机有限集 (RFS) 的方法，结合 Dempster-Shafer 近似 [1]，来估计网格单元的动态特性。为了从网格中提取对象，该跟踪器使用单元到航迹关联方案 [2]。有关更多详细信息，请参阅算法。
