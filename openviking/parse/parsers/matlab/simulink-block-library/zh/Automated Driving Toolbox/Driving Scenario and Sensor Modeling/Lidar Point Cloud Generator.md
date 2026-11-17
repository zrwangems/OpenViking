---
type: simulink-block
title: 'Lidar Point Cloud Generator'
family: 'driving-scenario-and-sensor-modeling'
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

### 输入

### **Actors** — 场景参与者位姿，包含 MATLAB® 结构体的 Simulink 总线

自车坐标系中的场景参与者位姿，指定为包含 MATLAB 结构体的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实数值标量 |
| `Actors` | 参与者位姿 | 长度为 `NumActors` 的参与者位姿结构体数组 |

`Actors` 中的每个参与者位姿结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | 参与者位置，指定为 [*x* *y* *z*] 形式的实数值向量。单位为 meters。 |
| `Velocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实数值向量。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为实数值标量。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为实数值标量。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为实数值标量。单位为 degrees。 |
| `AngularVelocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实数值向量。单位为 degrees per second。 |

#### 依赖关系

该模块必须位于使用 Scenario Reader 模块仿真驾驶场景的模型中。

### **Ego Vehicle** — 自车位姿，包含 MATLAB 结构体的 Simulink 总线

自车位姿，指定为包含 MATLAB 结构体的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：*  `FrontAxlePosition` | 车辆的前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为 meters。  **注意**  如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | 参与者位置，指定为 [*x* *y* *z*] 形式的实数值向量。单位为 meters。 |
| `Velocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实数值向量。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为实数值标量。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为实数值标量。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为实数值标量。单位为 degrees。 |
| `AngularVelocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实数值向量。单位为 degrees per second。 |

您可以从 Scenario Reader 模块输出自车位姿。在模型中使用的 Scenario Reader 模块中，选择 **输出自车位姿** 参数。

#### 依赖关系

该模块必须位于使用 Scenario Reader 模块仿真驾驶场景的模型中。

### 输出

### **Point Cloud** — 点云数据，*m*-by-*n*-by-3 的正实数值 [*x*, *y*, *z*] 点数组

点云数据，返回为 *m*-by-*n*-by 3 的正实数值 [*x*, *y*, *z*] 点数组。*m* 是点云中仰角（垂直）通道的数量。*n* 是点云中方位角（水平）通道的数量。*m* 和 *n* 定义点云中的点数，如下式所示：

m×n=VFOVVRES×HFOVHRES

- *V*FOV 是激光雷达的垂直视场，单位为 degrees，由 **激光雷达的仰角限值 (deg)** 参数指定。
- *V*RES 是激光雷达的垂直角分辨率，单位为 degrees，由 **激光雷达的仰角分辨率 (deg)** 参数指定。
- *H*FOV 是激光雷达的水平视场，单位为 degrees，由 **激光雷达的方位角限值 (deg)** 参数指定。
- *H*RES 是激光雷达的水平角分辨率，单位为 degrees，由 **激光雷达的方位角分辨率 (deg)** 参数指定。

数组中的每个 *m*-by-*n* 条目指定自车坐标系中检测点的 *x*-、*y*- 和 *z*-坐标。如果激光雷达在给定坐标处未检测到点，则 *x*、*y* 和 *z* 返回为 `NaN`。

默认情况下，Lidar Point Cloud Generator 模块会在生成的点云中包含道路数据。该模块从与 Lidar Point Cloud Generator 模块位于同一模型中的 Scenario Reader 模块获取世界坐标系中的道路数据。Lidar Point Cloud Generator 模块根据道路数据以及 **Ego Vehicle** 输入端口处的自车位姿，计算自车坐标系中的道路网格。Lidar Point Cloud Generator 模块的 **最大检测范围 (m)** 参数确定道路网格的范围。要将道路数据从点云中排除，请清除 **在生成的点云中包含道路** 参数。

## 参数

### 参数

#### 传感器标识

### **传感器的唯一标识符** — 唯一传感器标识符 `1`（默认） | 正整数

唯一传感器标识符，指定为正整数。传感器标识符用于区分多传感器系统中来自不同传感器的检测。如果模型包含多个具有相同传感器标识符的传感器模块，则 Bird's-Eye Scope 会显示错误。

### **传感器更新之间的所需间隔 (s)** — 传感器更新之间所需的时间间隔 `0.1`（默认） | 正标量

传感器更新之间所需的时间间隔，指定为正标量。此参数的值必须是 **Actors** 输入端口数据间隔的整数倍。在更新间隔之间从传感器请求的更新不包含任何检测。单位为 seconds。

#### 传感器外参

### **传感器的 (x,y) 位置 (m)** — 激光雷达传感器中心的位置 `[1.5 0]`（默认） | 实数值 1-by-2 向量

激光雷达传感器中心的位置，指定为实数值 1-by-2 向量。**传感器的 (x,y) 位置 (m)** 和 **传感器的高度 (m)** 参数定义激光雷达传感器相对于自车坐标系的坐标。默认值对应于安装在轿车车顶前缘中心的激光雷达传感器。单位为 meters。

### **传感器的高度 (m)** — 激光雷达传感器的高度 `1.6`（默认） | 正标量

激光雷达传感器高于地平面的高度，指定为正标量。**传感器的 (x,y) 位置 (m)** 和 **传感器的高度 (m)** 参数定义激光雷达传感器相对于自车坐标系的坐标。默认值对应于安装在轿车车顶前缘中心的激光雷达传感器。单位为 meters。

### **安装在自车上的传感器的偏航角 (deg)** — 激光雷达传感器的偏航角 `0`（默认） | 实数值标量

激光雷达传感器的偏航角，指定为实数值标量。*偏航角* 是自车中心线与激光雷达传感器测距轴之间的角度。当您沿自车坐标系的 *z* 轴正方向观察时，正偏航角对应于顺时针旋转。单位为 degrees。

### **安装在自车上的传感器的俯仰角 (deg)** — 激光雷达传感器的俯仰角 `0`（默认） | 实数值标量

激光雷达传感器的俯仰角，指定为实数值标量。*俯仰角* 是激光雷达传感器的测距轴与自车坐标系的 *xy* 平面之间的角度。当您沿自车坐标系的 *y* 轴正方向观察时，正俯仰角对应于顺时针旋转。单位为 degrees。

### **安装在自车上的传感器的横滚角 (deg)** — 激光雷达传感器的横滚角 `0`（默认） | 实数值标量

激光雷达传感器的横滚角，指定为实数值标量。*横滚角* 是激光雷达传感器的测距轴绕自车坐标系的 *x* 轴旋转的角度。当您沿自车坐标系的 *x* 轴正方向观察时，正横滚角对应于顺时针旋转。单位为 degrees。

#### 点云报告

### **用于报告点云的坐标系** — 所报告检测的坐标系 `Ego Cartesian`（默认） | `Sensor Cartesian`

所报告检测的坐标系，指定为以下值之一：

- `Ego Cartesian` — 检测在自车笛卡尔坐标系中报告。
- `Sensor Cartesian` — 检测在传感器笛卡尔坐标系中报告。

### **在生成的点云中包含自车** — 在点云中包含自车 `on`（默认） | `off`

选择此参数可在生成的点云中包含自车。

### **自车的 ActorID** — 自车的 `ActorID` 值 `1`（默认） | 正整数

自车的 `ActorID` 值，指定为正整数。`ActorID` 是参与者的唯一标识符。此参数必须是输入 **Actor** 总线中的有效 `ActorID`。

#### 依赖关系

要启用此参数，请选择 **在生成的点云中包含自车** 参数。

### **在生成的点云中包含道路** — 在点云中包含道路 `on`（默认） | `off`

选择此参数可在生成的点云中包含道路。

### **参与者配置文件来源** — 参与者配置文件的来源 `From Scenario Reader block`（默认） | `From workspace`

参与者配置文件的来源，这些配置文件是驾驶场景中所有参与者的物理特性和雷达特性，指定为以下选项之一：

- `From Scenario Reader block` — 该模块从 Scenario Reader 模块或 RoadRunner Scenario Reader 模块指定的场景中获取参与者配置文件。
- `From workspace` — 该模块从 **MATLAB 或模型工作区变量名称** 参数指定的 MATLAB 或模型工作区变量中获取参与者配置文件。

### **MATLAB 或模型工作区变量名称** — 参与者配置文件的变量名 `actor_profiles`（默认） | 有效变量名

参与者配置文件的变量名，指定为包含参与者配置文件的 MATLAB 或模型工作区变量的名称。

参与者配置文件是驾驶场景中所有参与者的物理特性和雷达特性，指定为结构体或结构体数组。

- 如果参与者配置文件变量包含单个结构体，则输入 **Actors** 总线中指定的所有参与者都使用此配置文件。
- 如果参与者配置文件变量是结构体数组，则输入 **Actors** 总线中指定的每个参与者都必须具有唯一的参与者配置文件。

要为驾驶场景生成结构体数组，请使用 `actorProfiles` 函数。下表显示了有效的结构体字段。如果未指定某个字段，则这些字段将设置为其默认值。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| `ClassID` | 分类标识符，指定为非负整数。`0` 表示未知或未分配类别的对象。 |
| `Length` | 参与者的长度，指定为正实数值标量。单位为 meters。 |
| `Width` | 参与者的宽度，指定为正实数值标量。单位为 meters。 |
| `Height` | 参与者的高度，指定为正实数值标量。单位为 meters。 |
| `OriginOffset` | 参与者的旋转中心相对于其几何中心的偏移，指定为 [*x*, *y*, *z*] 形式的实数值向量。旋转中心（即原点）位于参与者的底部中心。对于车辆，旋转中心是后轴中心下方地面上的点。单位为 meters。 |
| `MeshVertices` | 参与者的网格顶点，指定为 *n*-by-*3* 实数值顶点矩阵。矩阵中的每一行定义 3-D 空间中的一个点。 |
| `MeshFaces` | 参与者的网格面，指定为 *m*-by-*3* 整数矩阵。`MeshFaces` 的每一行表示一个由顶点 ID（即顶点的行号）定义的三角形。 |
| `RCSPattern` | 参与者的雷达截面积 (RCS) 方向图，指定为 `numel(RCSElevationAngles)`-by-`numel(RCSAzimuthAngles)` 实数值矩阵。单位为 decibels per square meter。 |
| `RCSAzimuthAngles` | 对应于 `RCSPattern` 行的方位角，指定为范围 [–180, 180] 内的值向量。单位为 degrees。 |
| `RCSElevationAngles` | 对应于 `RCSPattern` 行的仰角，指定为范围 [–90, 90] 内的值向量。单位为 degrees。 |

有关结构体字段的完整定义，请参阅 `actor` 和 `vehicle` 函数。

#### 依赖关系

要启用此参数，请将 **参与者配置文件来源** 参数设置为 `From workspace`。

### 测量

#### 设置

### **最大检测范围 (m)** — 最大检测范围 `120`（默认） | 正标量

激光雷达传感器的最大检测范围，指定为正标量。传感器无法检测超出此范围的参与者。此参数还决定道路网格的范围。单位为 meters。

### **距离精度 (m)** — 距离测量的精度 `0.002`（默认） | 正标量

距离测量的精度，指定为正标量。单位为 meters。

### **激光雷达的方位角分辨率 (deg)** — 激光雷达传感器的方位角分辨率 `0.16`（默认） | 正标量

激光雷达传感器的方位角分辨率，指定为正标量。方位角分辨率定义激光雷达能够区分两个目标的最小方位角间隔。单位为 degrees。

### **激光雷达的仰角分辨率 (deg)** — 激光雷达传感器的仰角分辨率 `1.25`（默认） | 正标量

激光雷达传感器的仰角分辨率，指定为正标量。仰角分辨率定义激光雷达能够区分两个目标的最小仰角间隔。单位为 degrees。

### **激光雷达的方位角限值 (deg)** — 激光雷达传感器的方位角限值 `[-180 180]`（默认） | [*min*, *max*] 形式的 1-by-2 实数值向量

激光雷达传感器的方位角限值，指定为 [*min*, *max*] 形式的 1-by-2 实数值向量。单位为 degrees。

### **激光雷达的仰角限值 (deg)** — 激光雷达传感器的仰角限值 `[-20 20]`（默认） | [*min*, *max*] 形式的 1-by-2 实数值向量

激光雷达传感器的仰角限值，指定为 [*min*, *max*] 形式的 1-by-2 实数值向量。单位为 degrees。

### **向测量添加噪声** — 向测量添加噪声 `on`（默认） | `off`

选择此参数可向激光雷达传感器测量添加噪声。清除此参数时，测量不包含噪声。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2020b 中引入**

### R2024a：与 RoadRunner Scenario 仿真一起使用时，不需要使用 `addSensors` 函数注册传感器模型

从 R2024a 开始，Simulink 会自动实例化一个 `SensorSimulation` 对象，并将模型中定义的传感器添加到 RoadRunner 场景。因此，不需要使用 `addSensors` 函数手动注册 Lidar Point Cloud Generator 模块。有关新工作流的详细信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。

在 R2024a 之前的版本中，必须使用 `addSensors` 函数手动将该模块注册为传感器模型。有关详细信息，请参阅“使用 `addSensors` 函数手动添加传感器对于 Simulink 模型不是必需的”。

## 描述

为驾驶场景或 RoadRunner Scenario 生成激光雷达点云数据

Lidar Point Cloud Generator 模块根据安装在自车上的激光雷达传感器所采集的激光雷达测量生成点云。

该模块从驾驶场景中的仿真道路和参与者位姿推导点云，并以等于传感器更新间隔的间隔生成点云。默认情况下，检测以自车坐标系为参考。该模块可以使用统计模型按指定的距离精度仿真添加的噪声。该模块还提供参数，以将自车和道路从生成的点云中排除。

您可以在 Driving Scenario 和 RoadRunner Scenario 仿真中将该模块与车辆参与者一起使用。在 RoadRunner Scenario 仿真中与参与者一起使用时，该模块不需要任何输入。有关详细信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。

激光雷达根据场景中道路和参与者的网格表示生成点云数据。*网格* 是由面和顶点组成的对象的 3-D 几何。

使用 Lidar Point Cloud Generator 创建的激光雷达传感器模型使用硬件加速光线追踪，以在点云中生成高度逼真且准确的对象表示。光线追踪允许对激光雷达传感器发射的光线与场景中对象表面之间的交互进行精确建模。此外，光线追踪会考虑表面纹理和角度等因素，从而增强输出点云数据的逼真度和准确性。该传感器模型还可以向检测添加随机噪声。

使用 Driving Scenario Designer 应用构建场景和传感器模型时，导出到 Simulink® 的激光雷达传感器会输出为 Lidar Point Cloud Generator 模块。

**提示**

在配置为驾驶场景仿真的模型中，Scenario Reader 模块必须在 Lidar Point Cloud Generator 模块之前执行。这样，驾驶场景数据才会由 Lidar Point Cloud Generator 模块正确处理。要检查模块执行顺序，请右键点击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Scenario Reader — `0`
- Lidar Point Cloud Generator — `1`
