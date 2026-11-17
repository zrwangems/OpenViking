---
type: simulink-block
title: 'Lidar Sensor'
family: 'lidar'
product_id: 'lidar'
product_name: 'Lidar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'lidarsensor'
documentation_source_path: 'ref/lidarsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Lidar Sensor

## 端口

### 输入

### **ActorPoses** — 参与者位姿 包含 MATLAB® 结构的 Simulink 总线

参与者位姿，指定为包含 MATLAB 结构的 Simulink 总线。该结构必须包含以下两个字段。

1. 场景中参与者的目标位姿，指定为 *L* 元素的结构体数组。每个结构体对应一个参与者。*L* 是所使用的参与者数量。

   您可以使用 `actorPoses`（Automated Driving Toolbox）函数以编程方式生成此结构体。您也可以手动创建这些结构体。每个结构体必须包含以下字段。

   | 字段 | 描述 | 值 |
   | --- | --- | --- |
   | `ActorID` | 参与者的唯一标识符。 | 正标量 |
   | `Position` | 参与者相对于自车坐标系的位置，单位为米。 | 形式为 [`x y z`] 的三元素向量 |
   | `Velocity` | 参与者沿 *x*、*y* 和 *z* 方向的速度 (*V*)，单位为米每秒。 | 形式为 [`Vx Vy Vz`] 的三元素向量 |
   | `Roll` | 参与者的横滚角，单位为度。 | 数值标量 |
   | `Pitch` | 参与者的俯仰角，单位为度。 | 数值标量 |
   | `Yaw` | 参与者的偏航角，单位为度。 | 数值标量 |
   | `AngularVelocity` | 参与者沿 *x*、*y* 和 *z* 方向的角速度 (*ω*)，单位为度每秒。 | 形式为 [`ωx ωy ωz`] 的三元素向量 |
2. 用于生成新点云的仿真时间，指定为正标量。

您可以从 Scenario Reader（Automated Driving Toolbox）模块输出场景参与者位姿。
### 输出

### **IsValid** — 有效仿真时间 `0` | `1`

有效仿真时间，返回为逻辑值 `0`（`false`）或 `1`（`true`）。对于在 **Required interval between sensor updates (s)** 参数指定的更新间隔之间请求的更新，此值为 `0`。

**数据类型：** `Boolean`

### **Location** — 点的位置值 *M*×*N*×3 矩阵

点云中点的位置值，返回为 *M*×*N*×3 矩阵。*M*、*N* 分别为组织化点云中的行数和列数。

### **Intensity** — 点的强度值 *M*×*N* 矩阵

点云中点的强度值，返回为 *M*×*N* 矩阵。*M*、*N* 分别为组织化点云中的行数和列数。

### **Clusters** — 参与者的分类数据 *M*×*N*×3 数组

场景中参与者的分类数据，返回为 *M*×*N*×3 数组。*M*、*N* 分别为组织化点云中的行数和列数。数组的第一个维度包含 `ActorID`，第二个维度包含目标参与者的 `ClassID`，第三个维度包含表示 **Material attribute information in JSON format** 索引的材质 ID。

## 参数

### 参数

#### 传感器标识

### **Unique identifier of sensor** — 唯一传感器标识符 `1`（默认）| 正整数

传感器的唯一标识符，指定为正整数。在多传感器系统中，此索引用于区分不同的传感器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Required interval between sensor updates (s)** — 传感器更新之间的所需时间间隔 `0.1`（默认）| 正标量

两次连续传感器更新之间的时间间隔，指定为正标量。模块按此参数指定的间隔生成新检测。该值必须是仿真时间的整数倍。在更新间隔之间从传感器请求的更新不包含任何检测。单位为秒。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Sensor model to choose typical values** — 传感器模型名称 `Custom`（默认）| `HDL64E` | `HDL32E` | `VLP16` | `VLP32C` | `VLS128` | `PuckLITE` | `PuckHiRes` | `OS0-32` | `OS0-64` | `OS0-128` | `OS1Gen1-32` | `OS1Gen1-64` | `OS1Gen1-128` | `OS1Gen2-32` | `OS1Gen2-64` | `OS1Gen2-128` | `OS2-32` | `OS2-64` | `OS2-128`

*自 R2024a 起*

指定传感器模型的名称。有关支持的传感器模型的信息，请参阅 Supported Sensors。此参数根据指定的传感器设置默认仰角值。要应用自定义仰角，请将此参数设置为 `Custom`，并使用 **Elevation angles (deg)** 参数。

#### 依赖关系

当您未将此参数设置为 `Custom` 时，该模块会禁用以下参数：

- **Use elevation angles**
- **Elevation angles (deg)**
- **Elevation limits (deg)**
- **Elevation resolution (deg)**

#### 传感器安装

### **Position [X Y Height] (m)** — 传感器中心位置 `[1.5 0 1.6]`（默认）| 形式为 [*X* *Y* *Height*] 的三元素向量

传感器中心位置，指定为形式为 [*X* *Y* *Height*] 的三元素向量。*X* 和 *Y* 的值表示传感器中心相对于自车坐标系 *X* 轴和 *Y* 轴的位置。*Height* 是传感器离地高度。默认值定义了安装在轿车车顶前缘的激光雷达传感器。单位为米。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Orientation [Roll Pitch Yaw] (deg)** — 传感器方向 `[0 0 0]`（默认）| 三元素向量

传感器方向，指定为形式为 [*Roll* *Pitch* *Yaw*] 的三元素向量。这些值相对于自车坐标系。单位为度。

- *Roll* — 横滚角是绕前后轴（即自车坐标系的 *x* 轴）旋转的角度。正横滚角对应于沿 *x* 轴正方向观察时的顺时针旋转。
- *Pitch* — 俯仰角是绕左右轴（即自车坐标系的 *y* 轴）旋转的角度。正横滚角对应于沿 *y* 轴正方向观察时的顺时针旋转。
- *Yaw* — 偏航角是绕垂直轴（即自车坐标系的 *z* 轴）旋转的角度。正横滚角对应于沿 *z* 轴正方向观察时的顺时针旋转。当从上方观察车辆时，此旋转表现为逆时针方向。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### 参与者配置文件

### **MATLAB or Model workspace Actor profiles variable name** — actor profiles 的变量名称 `actor_profiles`（默认）| 有效变量名

actor profiles 的变量名称，指定为包含 actor profiles 的 MATLAB 或模型工作区变量的名称。

Actor profiles 是场景中 actors 的物理特征，
指定为结构体或 *L* 元素结构体数组。
*L* 是场景中 actors 的数量。

如果 actor profiles 变量具有单个结构体，则在 **ActorPoses** 输入端口指定的所有 actors 使用相同的 profile。

要为您的驾驶场景 `drivingScenario`（Automated Driving Toolbox）生成 actor profile 结构体数组，请使用 `actorProfiles`（Automated Driving Toolbox）函数。您也可以手动创建这些结构体。
此表显示了有效的结构体字段。

| 字段 | 描述 | 值 |
| --- | --- | --- |
| `ActorID` | actor 的唯一标识符。在具有多个 actors 的场景中，此值将不同的 actors 彼此区分开来。 | 正整数 |
| `ClassID` | actor 的用户定义分类 ID。 | `ClassID` | 类名称 | | --- | --- | | `1` | Car | | `2` | Truck | | `3` | Bicycle | | `4` | Pedestrian | | `5` | Jersey Barrier | | `6` | Guardrail | | 正标量 |
| `Length` | actor 的长度，以米为单位。 | 正标量 |
| `Width` | actor 的宽度，以米为单位。 | 正标量 |
| `Height` | actor 的高度，以米为单位。 | 正标量 |
| `OriginOffset` | actor 的旋转中心相对于其几何中心的偏移。旋转中心（即原点）位于 actor 的底部中心。对于车辆，旋转中心是后轴中心下方地面上的点。 | 形式为 `[x y z]` 的三元素向量。单位为米。 |
| `MeshVertices` | 网格表示中 actor 的顶点。 | *N*×3 数值矩阵，其中每一行定义 3-D 空间中的一个顶点。 |
| `MeshFaces` | 网格表示中 actor 的面。 | *M*×3 整数矩阵，其中每一行表示由顶点 ID 定义的三角形，顶点 ID 是 `MeshVertices` 的行号。 |
| `MeshTargetReflectances` | actor 每个三角形面的材料反射率。 | *M*×1 数值向量，其中 *M* 是 actor 的三角形面数。每个值必须在 `[0, 1]` 范围内。 |

有关这些结构体字段的更多信息，请参阅 `actor`（Automated Driving Toolbox）和 `vehicle`（Automated Driving Toolbox）函数。

### **ActorID of the host vehicle** — 自车的 Actor ID `1`（默认）| 正整数

自车的 `ActorID` 值，指定为正整数。`ActorID` 是 actor 的唯一标识符。此参数必须是在 **ActorPoses** 输入端口指定的有效 `ActorID`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### 点云报告

### **Coordinate system to report point cloud data** — 报告检测结果的坐标系 `World`（默认）| `Sensor` | `Host`

*自 R2024b 起*

报告检测结果的坐标系，指定为以下值之一：

- `Sensor` — 模块在传感器坐标系中报告检测结果。
- `Host` — 模块在宿主 actor 的坐标系中报告检测结果。
- `World` — 模块在世界坐标系中报告检测结果。

### 传感器视场

#### 设置

### **Maximum detection range of sensor (m)** — 最大检测范围 `120`（默认）| 正标量

传感器的最大检测范围，指定为正标量。传感器无法扫描超出此范围的点。单位为米。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Azimuth limits (deg)** — 激光雷达传感器的方位角限制 `[-180 180]`（默认）| 二元素向量

激光雷达传感器的方位角限制，指定为 [*min*
*max*] 形式的二元素向量。值必须在 `[-180,
180]` 范围内，*max* 必须大于 *min*。
单位为度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Azimuth resolution (deg)** — 激光雷达传感器的方位角分辨率 `0.16`（默认）| 正标量

激光雷达传感器的方位角分辨率，指定为正标量。单位为度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Use elevation angles** — 使用自定义仰角 `off`（默认）| `on`

选择此参数以使用自定义仰角。

#### 依赖关系

- 要启用此参数，请将 **Set model to choose typical
  values** 参数设置为 `Custom`。
- 选择此参数时，模块将禁用 **Elevation
  limits (deg)** 和 **Elevation resolution (deg)**
  参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Elevation angles (deg)** — 激光雷达传感器的仰角 *N* 元素实值向量

激光雷达传感器的自定义仰角，指定为
*N* 元素实值向量。*N* 是仰角通道数。向量元素必须按递增顺序排列。单位为
度。

#### 依赖关系

要启用此参数：

- 将 **Set model to choose typical values** 参数
  设置为 `Custom`。
- 选择 **Use elevation angles** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Elevation limits (deg)** — 激光雷达传感器的仰角限制 `[-20 20]`（默认）| [*min*, *max*] 形式的二元素向量

激光雷达传感器的仰角限制，指定为
[*min*
*max*] 形式的二元素向量。值必须在 `[-180,
180]` 范围内，*max* 必须大于 *min*。
单位为度。

#### 依赖关系

要启用此参数：

- 将 **Set model to choose typical values** 参数
  设置为 `Custom`。
- 清除 **Use elevation angles** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Elevation resolution (deg)** — 激光雷达传感器的仰角分辨率 `1.25`（默认）| 正标量

激光雷达传感器的仰角分辨率，指定为以度为单位的正标量。

#### 依赖关系

要启用此参数：

- 将 **Set model to choose typical values** 参数
  设置为 `Custom`。
- 清除 **Use elevation angles** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### Advance Settings

#### Noise Simulation

### **Add noise to measurements** — 向测量添加噪声 `on`（默认）| `off`

选择此参数时，模块使用 **Range accuracy (m)** 参数作为一个
标准差，向点云中的每个点添加随机高斯噪声。否则，数据没有噪声。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Range accuracy (m)** — 传感器距离测量的精度 `0.002`（默认）| 正标量

传感器距离测量的精度，指定为正标量。单位为
米。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### Weather Simulation

### **Fog visibility in meters** — 雾中可见距离 `1000`（默认）| 正标量

雾中可见距离，指定为正标量，单位为米。此参数的值不得大于 1000。较高的值表示较好的能见度和较低的雾影响。默认值 `1000` 表示清晰能见度，或无雾。

**注意**

当您同时指定 **Fog visibility in meters** 和 **Rainrate in mm/hour** 参数时，该模块仅模拟雾天天气。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rainrate in mm/hour** — 降雨速率 `0`（默认）| 正标量

降雨速率，指定为正标量，单位为毫米每小时。此参数的值不得大于 200。增大此值会增加降雨对生成点云的影响。默认值为 `0`，表示无降雨。

**注意**

当您同时指定 **Fog visibility in meters** 和 **Rainrate in mm/hour** 参数时，该模块仅模拟雾天天气。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### 运动畸变

### **Simulate Motion Distortion** — 模拟运动畸变 `off`（默认）| `on`

*自 R2024a 起*

选择此参数以模拟由于自车运动导致的点云数据畸变。

### **Laser firing time (s)** — 激光雷达传感器中激光器的发射时间 `[]`（默认）| 正标量 | 正数值向量

*自 R2024a 起*

指定激光雷达传感器中激光器的发射时间。要为传感器中的所有激光器指定相同的发射时间，请使用正标量。否则请使用正数值向量。向量的长度必须与 **Elevation angles (deg)** 参数的长度匹配。

如果您未选择 **Use elevation angles** 参数，则向量的长度必须与 **Elevation limits (deg)** 和 **Elevation resolution (deg)** 参数一致。例如，如果您将 **Elevation limits (deg)** 参数设置为 `[-20 20]`，并将 **Elevation resolution (deg)** 参数设置为 `1.25`，则 **Laser firing time (s)** 向量的长度必须与向量 `[-20:1.25:20]` 的长度匹配。

#### 依赖关系

要启用此参数，请选择 **Simulate Motion Distortion** 参数。

**数据类型：** `single` | `double`

### 场景材质属性

### **Material attribute information in JSON format** — JSON 格式的材质属性信息 字符串标量 | 字符向量

*自 R2024b 起*

选择此参数以查看或编辑 JSON 格式的目标材质属性信息。有关材质属性的更多信息，请参阅 `MaterialAttributes` 属性。

#### 依赖关系

- 要启用此参数，请选择 **Edit JSON text to add, remove, or modify material attributes**。

### **Edit JSON text to add, remove, or modify material attributes** — 编辑 JSON 文本以添加、删除或修改材质属性 `off`（默认）| `on`

*自 R2024b 起*

选择此参数以启用编辑以 JSON 格式存储的材质属性信息。

### 输出端口设置

### **Output intensity port** — 输出点的强度值 `on`（默认）| `off`

选择此参数以启用 **Intensity** 输出端口。

### **Output clusters port** — 输出点的分割值 `on`（默认）| `off`

选择此参数以启用 **Clusters** 输出端口。

## 所属库

Lidar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

### R2024b: 使用 RoadRunner Scenario 中的目标材质信息

现在，您可以使用 RoadRunner Scenario 中目标参与者的材质信息，通过 **Scene Material Attributes** 选项卡中的参数生成点云数据。**Clusters** 输出端口也包含材质 ID 信息。

### R2024b: 指定坐标系以报告点云数据

使用 **Coordinate system to report point cloud data** 参数为输出点云指定 `World`、`Host` 或 `Sensor` 类型的坐标系。

### R2024a: 指定传感器模型

现在，您可以使用 **Sensor model to choose typical values** 参数指定传感器模型的类型。该参数根据指定的传感器设置默认仰角值。

### R2024a: 模拟运动畸变

现在，您可以使用 **Simulate Motion Distortion** 和 **Laser firing time (s)** 参数模拟运动畸变。

### R2024a: 在 RoadRunner Scenario 中向车辆参与者添加激光雷达传感器

现在，您可以使用在 Simulink 中定义的激光雷达传感器模型，在 RoadRunner 场景中生成点云数据。当与 RoadRunner Scenario 仿真中的参与者一起使用时，该模块不需要任何输入。

## 描述

为场景生成激光雷达点云数据

Lidar Sensor 模块根据安装在自车上的激光雷达传感器记录的测量值生成点云数据。生成的数据位于自车坐标系中。

要为场景生成点云数据，您可以使用此模块配置传感器和参与者位姿。该模块还输出生成点的强度和分割值。

此外，您可以使用此模块来

- 配置激光雷达传感器参数，例如范围、方位角和仰角。
- 向点云中的点添加随机高斯噪声。
- 模拟雾和雨等天气条件。

您可以使用 `drivingScenario`（Automated Driving Toolbox）对象创建包含参与者和轨迹的场景，使用 Scenario Reader（Automated Driving Toolbox）模块将此数据导入 Simulink®，然后使用 Lidar Sensor 模块为场景生成点云数据。

您还可以在 RoadRunner Scenario 仿真中将该模块与车辆参与者一起使用。当与 RoadRunner Scenario 仿真中的参与者一起使用时，该模块不需要任何输入。有关详细信息，请参阅 Integrate Lidar Sensor Model into RoadRunner Scenario 和 Cosimulate with Unreal Engine。*（自 R2024a 起）*

使用 Lidar Sensor 模块创建的激光雷达传感器模型使用硬件加速光线追踪来生成点云中高度逼真且准确的对象表示。光线追踪允许精确建模激光雷达传感器发出的光线与场景中对象表面之间的交互。此外，光线追踪还考虑表面纹理和角度等因素，从而增强输出点云数据的真实感和准确性。

**提示**

在配置为驾驶场景仿真的模型中，Scenario Reader 模块必须在 Lidar Sensor 模块之前执行。这样，Lidar Sensor 模块才能正确处理驾驶场景数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Scenario Reader — `0`
- Lidar Sensor — `1`

。
