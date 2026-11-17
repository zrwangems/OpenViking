---
type: simulink-block
title: 'Lidar Point Cloud Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'lidarpointcloudgenerator'
documentation_source_path: 'ref/lidarpointcloudgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Lidar Point Cloud Generator

## 端口
```yaml
ports:
- name: Actors
  summary: 场景参与者位姿 包含 MATLAB® 结构的 Simulink 总线
  direction: input
- name: Ego Vehicle
  summary: 自车位姿 包含 MATLAB 结构的 Simulink 总线
  direction: input
- name: Point Cloud
  summary: 点云数据 *m*×*n*×3 的正实值 [*x*, *y*, *z*] 点数组
  direction: output
```

### 输入

### **Actors** — 场景参与者位姿 包含 MATLAB® 结构的 Simulink 总线

自车坐标系中的场景参与者位姿，指定为包含 MATLAB 结构的 Simulink 总线。

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
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

#### 依赖关系

该模块必须位于使用 Scenario Reader 模块仿真驾驶场景的模型中。

### **Ego Vehicle** — 自车位姿 包含 MATLAB 结构的 Simulink 总线

自车位姿，指定为包含 MATLAB 结构的 Simulink 总线。

该结构必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

您可以从 Scenario Reader 模块输出自车位姿。在模型使用的 Scenario Reader 模块中，选择 **Output ego vehicle pose** 参数。

#### 依赖关系

该模块必须位于使用 Scenario Reader 模块仿真驾驶场景的模型中。
### 输出

### **Point Cloud** — 点云数据 *m*×*n*×3 的正实值 [*x*, *y*, *z*] 点数组

点云数据，返回为 *m*×*n*×3 的正实值 [*x*, *y*, *z*] 点数组。*m* 是点云中的仰角（垂直）通道数。*n* 是点云中的方位角（水平）通道数。*m* 和 *n* 定义点云中的点数，如下式所示：

m×n=VFOVVRES×HFOVHRES

- *V*FOV 是激光雷达的垂直视场角，以度为单位，由 **Elevation limits of lidar (deg)** 参数指定。
- *V*RES 是激光雷达的垂直角分辨率，以度为单位，由 **Elevation resolution of lidar (deg)** 参数指定。
- *H*FOV 是激光雷达的水平视场角，以度为单位，由 **Azimuthal limits of lidar (deg)** 参数指定。
- *H*RES 是激光雷达的水平角分辨率，以度为单位，由 **Azimuthal resolution of lidar (deg)** 参数指定。

数组中的每个 *m*×*n* 条目指定自车坐标系中检测到的点的 *x*、*y* 和 *z* 坐标。如果激光雷达在给定坐标处未检测到点，则 *x*、*y* 和 *z* 返回为 `NaN`。

默认情况下，Lidar Point Cloud Generator 模块在生成的点云中包含道路数据。该模块从与 Lidar Point Cloud Generator 模块位于同一模型中的 Scenario Reader 模块获取世界坐标系中的道路数据。Lidar Point Cloud Generator 模块根据道路数据和 **Ego Vehicle** 输入端口处的自车位姿，计算自车坐标系中的道路网格。Lidar Point Cloud Generator 模块的 **Maximum detection range (m)** 参数决定道路网格的范围。要从点云中排除道路数据，请清除 **Include roads in generated point cloud** 参数。
## 参数
```yaml
parameters:
- name: Unique identifier of sensor
  summary: 唯一传感器标识符 1（默认）| 正整数
  group: 参数
- name: Required interval between sensor updates (s)
  summary: 传感器更新之间的所需时间间隔 0.1（默认）| 正标量
  group: 参数
- name: Sensor's (x,y) position (m)
  summary: 激光雷达传感器中心的位置 [1.5 0]（默认）| 实值 1×2 向量
  group: 参数
- name: Sensor's height (m)
  summary: 激光雷达传感器的高度 1.6（默认）| 正标量
  group: 参数
- name: Yaw angle of sensor mounted on ego vehicle (deg)
  summary: 激光雷达传感器的偏航角 0（默认）| 实值标量
  group: 参数
- name: Pitch angle of sensor mounted on ego vehicle (deg)
  summary: 激光雷达传感器的俯仰角 0（默认）| 实值标量
  group: 参数
- name: Roll angle of sensor mounted on ego vehicle (deg)
  summary: 激光雷达传感器的横滚角 0（默认）| 实值标量
  group: 参数
- name: Coordinate system used to report point cloud
  summary: 报告检测结果的坐标系 Ego Cartesian（默认）| Sensor Cartesian
  group: 参数
- name: Include ego vehicle in generated point cloud
  summary: 在点云中包含自车 on（默认）| off
  group: 参数
- name: ActorID of ego vehicle
  summary: 自车的 ActorID 值 1（默认）| 正整数
  group: 参数
- name: Include roads in generated point cloud
  summary: 在点云中包含道路 on（默认）| off
  group: 参数
- name: Source of actor profiles
  summary: 参与者配置文件的来源 From Scenario Reader block（默认）| From workspace
  group: 参数
- name: MATLAB or model workspace variable name
  summary: 参与者配置文件的变量名 actor_profiles（默认）| 有效变量名
  group: 参数
- name: Maximum detection range (m)
  summary: 最大检测距离 120（默认）| 正标量
  group: 测量
- name: Range accuracy (m)
  summary: 距离测量的精度 0.002（默认）| 正标量
  group: 测量
- name: Azimuthal resolution of lidar (deg)
  summary: 激光雷达传感器的方位角分辨率 0.16（默认）| 正标量
  group: 测量
- name: Elevation resolution of lidar (deg)
  summary: 激光雷达传感器的仰角分辨率 1.25（默认）| 正标量
  group: 测量
- name: Azimuthal limits of lidar (deg)
  summary: 激光雷达传感器的方位角范围 [-180 180]（默认）| [*min*, *max*] 形式的 1×2 实值向量
  group: 测量
- name: Elevation limits of lidar (deg)
  summary: 激光雷达传感器的仰角范围 [-20 20]（默认）| [*min*, *max*] 形式的 1×2 实值向量
  group: 测量
- name: Add noise to measurements
  summary: 向测量添加噪声 on（默认）| off
  group: 测量
```

### 参数

#### 传感器标识

### **Unique identifier of sensor** — 唯一传感器标识符 `1`（默认）| 正整数

唯一传感器标识符，指定为正整数。传感器标识符用于区分多传感器系统中来自不同传感器的检测结果。如果模型包含多个具有相同传感器标识符的传感器模块，Bird's-Eye Scope 将显示错误。

### **Required interval between sensor updates (s)** — 传感器更新之间的所需时间间隔 `0.1`（默认）| 正标量

传感器更新之间的所需时间间隔，指定为正标量。此参数的值必须是 **Actors** 输入端口数据间隔的整数倍。在更新间隔之间请求的传感器更新不包含任何检测结果。单位为秒。

#### 传感器外参

### **Sensor's (x,y) position (m)** — 激光雷达传感器中心的位置 `[1.5 0]`（默认）| 实值 1×2 向量

激光雷达传感器中心的位置，指定为实值 1×2 向量。**Sensor's (x,y) position (m)** 和 **Sensor's height (m)** 参数定义激光雷达传感器相对于自车坐标系的坐标。默认值对应于安装在轿车上的激光雷达传感器，位于车顶前缘中心。单位为米。

### **Sensor's height (m)** — 激光雷达传感器的高度 `1.6`（默认）| 正标量

激光雷达传感器高于地平面的高度，指定为正标量。**Sensor's (x,y) position (m)** 和 **Sensor's height (m)** 参数定义激光雷达传感器相对于自车坐标系的坐标。默认值对应于安装在轿车上的激光雷达传感器，位于车顶前缘中心。单位为米。

### **Yaw angle of sensor mounted on ego vehicle (deg)** — 激光雷达传感器的偏航角 `0`（默认）| 实值标量

激光雷达传感器的偏航角，指定为实值标量。*偏航角*是自车中心线与激光雷达传感器前向轴之间的夹角。正偏航角对应于沿自车坐标系 *z* 轴正方向观察时的顺时针旋转。单位为度。

### **Pitch angle of sensor mounted on ego vehicle (deg)** — 激光雷达传感器的俯仰角 `0`（默认）| 实值标量

激光雷达传感器的俯仰角，指定为实值标量。*俯仰角*是激光雷达传感器前向轴与自车坐标系 *xy* 平面之间的夹角。正俯仰角对应于沿自车坐标系 *y* 轴正方向观察时的顺时针旋转。单位为度。

### **Roll angle of sensor mounted on ego vehicle (deg)** — 激光雷达传感器的横滚角 `0`（默认）| 实值标量

激光雷达传感器的横滚角，指定为实值标量。*横滚角*是激光雷达传感器前向轴绕自车坐标系 *x* 轴的旋转角度。正横滚角对应于沿自车坐标系 *x* 轴正方向观察时的顺时针旋转。单位为度。

#### 点云报告

### **Coordinate system used to report point cloud** — 报告检测结果的坐标系 `Ego Cartesian`（默认）| `Sensor Cartesian`

报告检测结果的坐标系，指定为以下值之一：

- `Ego Cartesian` — 检测结果在自车笛卡尔坐标系中报告。
- `Sensor Cartesian` — 检测结果在传感器笛卡尔坐标系中报告。

### **Include ego vehicle in generated point cloud** — 在点云中包含自车 `on`（默认）| `off`

选择此参数以在生成的点云中包含自车。

### **ActorID of ego vehicle** — 自车的 `ActorID` 值 `1`（默认）| 正整数

自车的 `ActorID` 值，指定为正整数。`ActorID` 是参与者的唯一标识符。此参数必须是输入 **Actor** 总线中的有效 `ActorID`。

#### 依赖关系

要启用此参数，请选择 **Include ego vehicle in generated point cloud** 参数。

### **Include roads in generated point cloud** — 在点云中包含道路 `on`（默认）| `off`

选择此参数以在生成的点云中包含道路。

### **Source of actor profiles** — 参与者配置文件的来源 `From Scenario Reader block`（默认）| `From workspace`

参与者配置文件的来源，即驾驶场景中所有参与者的物理和雷达特性，指定为以下选项之一：

- `From Scenario Reader block` — 该模块从 Scenario Reader 模块或 RoadRunner Scenario Reader 模块指定的场景中获取参与者配置文件。
- `From workspace` — 该模块从 **MATLAB or model workspace variable name** 参数指定的 MATLAB 或模型工作区变量中获取参与者配置文件。

### **MATLAB or model workspace variable name** — 参与者配置文件的变量名 `actor_profiles`（默认）| 有效变量名

参与者配置文件的变量名，指定为包含参与者配置文件的 MATLAB 或模型工作区变量的名称。

参与者配置文件是驾驶场景中所有参与者的物理和雷达特性，指定为结构体或结构体数组。

- 如果参与者配置文件变量包含单个结构体，则输入 **Actors** 总线中指定的所有参与者都使用此配置文件。
- 如果参与者配置文件变量是结构体数组，则输入 **Actors** 总线中指定的每个参与者必须具有唯一的参与者配置文件。

要为您的驾驶场景生成结构体数组，请使用 `actorProfiles` 函数。下表显示了有效的结构体字段。如果未指定字段，则字段设置为其默认值。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| `ClassID` | 分类标识符，指定为非负整数。`0` 表示未知或未分配类别的对象。 |
| `Length` | 参与者的长度，指定为正实值标量。单位为米。 |
| `Width` | 参与者的宽度，指定为正实值标量。单位为米。 |
| `Height` | 参与者的高度，指定为正实值标量。单位为米。 |
| `OriginOffset` | 参与者旋转中心相对于其几何中心的偏移，指定为 [*x*, *y*, *z*] 形式的实值向量。旋转中心（即原点）位于参与者的底部中心。对于车辆，旋转中心是后轴中心下方地面上的点。单位为米。 |
| `MeshVertices` | 参与者的网格顶点，指定为 *n*×*3* 的实值顶点矩阵。矩阵中的每一行定义三维空间中的一个点。 |
| `MeshFaces` | 参与者的网格面，指定为 *m*×*3* 的整数矩阵。`MeshFaces` 的每一行表示由顶点 ID（即顶点的行号）定义的三角形。 |
| `RCSPattern` | 参与者的雷达散射截面 (RCS) 方向图，指定为 `numel(RCSElevationAngles)`×`numel(RCSAzimuthAngles)` 的实值矩阵。单位为分贝每平方米。 |
| `RCSAzimuthAngles` | 对应于 `RCSPattern` 行的方位角，指定为范围为 [–180, 180] 的值向量。单位为度。 |
| `RCSElevationAngles` | 对应于 `RCSPattern` 行的仰角，指定为范围为 [–90, 90] 的值向量。单位为度。 |

有关结构体字段的完整定义，请参阅 `actor` 和 `vehicle` 函数。

#### 依赖关系

要启用此参数，请将 **Source of actor profiles** 参数设置为 `From workspace`。

### 测量

#### 设置

### **Maximum detection range (m)** — 最大检测距离 `120`（默认）| 正标量

激光雷达传感器的最大检测距离，指定为正标量。传感器无法检测超出此距离的参与者。此参数还决定道路网格的范围。单位为米。

### **Range accuracy (m)** — 距离测量的精度 `0.002`（默认）| 正标量

距离测量的精度，指定为正标量。单位为米。

### **Azimuthal resolution of lidar (deg)** — 激光雷达传感器的方位角分辨率 `0.16`（默认）| 正标量

激光雷达传感器的方位角分辨率，指定为正标量。方位角分辨率定义激光雷达可以区分两个目标的最小方位角间隔。单位为度。

### **Elevation resolution of lidar (deg)** — 激光雷达传感器的仰角分辨率 `1.25`（默认）| 正标量

激光雷达传感器的仰角分辨率，指定为正标量。仰角分辨率定义激光雷达可以区分两个目标的最小仰角间隔。单位为度。

### **Azimuthal limits of lidar (deg)** — 激光雷达传感器的方位角范围 `[-180 180]`（默认）| [*min*, *max*] 形式的 1×2 实值向量

激光雷达传感器的方位角范围，指定为 [*min*, *max*] 形式的 1×2 实值向量。单位为度。

### **Elevation limits of lidar (deg)** — 激光雷达传感器的仰角范围 `[-20 20]`（默认）| [*min*, *max*] 形式的 1×2 实值向量

激光雷达传感器的仰角范围，指定为 [*min*, *max*] 形式的 1×2 实值向量。单位为度。

### **Add noise to measurements** — 向测量添加噪声 `on`（默认）| `off`

选择此参数以向激光雷达传感器测量添加噪声。清除此参数时，测量不包含噪声。
## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2024a：与 RoadRunner Scenario 仿真一起使用时，无需使用 `addSensors` 函数注册传感器模型

从 R2024a 开始，Simulink 会自动实例化一个 `SensorSimulation` 对象，并将模型中定义的传感器添加到 RoadRunner 场景中。因此，不再需要使用 `addSensors` 函数手动注册 Lidar Point Cloud Generator 模块。有关新工作流的详细信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。

在 R2024a 之前的版本中，必须使用 `addSensors` 函数手动将该模块注册为传感器模型。有关详细信息，请参阅 Adding sensors manually using `addSensors` function is not required for Simulink models。

## 描述

为驾驶场景或 RoadRunner Scenario 生成激光雷达点云数据

Lidar Point Cloud Generator 模块根据安装在自车上的激光雷达传感器所采集的激光雷达测量数据生成点云。

该模块根据驾驶场景中的仿真道路和参与者位姿推导点云，并以等于传感器更新间隔的周期生成点云。默认情况下，检测结果参考自车坐标系。该模块可以使用统计模型，按指定的距离精度模拟添加的噪声。该模块还提供参数，用于从生成的点云中排除自车和道路。

您可以将该模块与 Driving Scenario 和 RoadRunner Scenario 仿真中的车辆参与者一起使用。当与 RoadRunner Scenario 仿真中的参与者一起使用时，该模块不需要任何输入。有关详细信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。

激光雷达根据场景中道路和参与者的网格表示生成点云数据。*网格*是由面和顶点组成的对象三维几何表示。

使用 Lidar Point Cloud Generator 创建的激光雷达传感器模型使用硬件加速光线追踪，以生成点云中高度逼真且准确的对象表示。光线追踪可以精确建模激光雷达传感器发出的光线与场景中对象表面之间的交互。此外，光线追踪还考虑表面纹理和角度等因素，从而增强输出点云数据的真实感和准确性。该传感器模型还可以向检测结果添加随机噪声。

使用 Driving Scenario Designer 应用构建场景和传感器模型时，导出到 Simulink® 的激光雷达传感器会输出为 Lidar Point Cloud Generator 模块。

**提示**

在配置为驾驶场景仿真的模型中，Scenario Reader 模块必须在 Lidar Point Cloud Generator 模块之前执行。这样，驾驶场景数据才能被 Lidar Point Cloud Generator 模块正确处理。要检查模块执行顺序，请右键点击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Scenario Reader — `0`
- Lidar Point Cloud Generator — `1`

。
