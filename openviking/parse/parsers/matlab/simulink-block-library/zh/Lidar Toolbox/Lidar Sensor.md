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

### **ActorPoses** — 包含 MATLAB® 结构的参与者位姿 Simulink 总线

参与者位姿，指定为包含 MATLAB 结构的 Simulink 总线。该结构必须包含以下两个字段。

1. 场景中参与者的目标位姿，指定为 *L* 元素的结构体数组。每个结构体对应一个参与者。*L* 是使用的参与者数量。

   您可以使用 `actorPoses` (Automated Driving Toolbox) 函数以编程方式生成此结构。您也可以手动创建这些结构。每个结构必须包含以下字段。

   | 字段 | 描述 | 值 |
   | --- | --- | --- |
   | `ActorID` | 参与者的唯一标识符。 | Positive scalar |
   | `Position` | 参与者相对于自车坐标系的位置，单位为 meters。 | Three-element vector of the form [`x y z`] |
   | `Velocity` | 参与者的速度 (*V*)，单位为 meters per second，沿 *x*、*y* 和 *z* 方向。 | Three-element vector of the form [`Vx Vy Vz`] |
   | `Roll` | 参与者的横滚角，单位为 degrees。 | Numeric scalar |
   | `Pitch` | 参与者的俯仰角，单位为 degrees。 | Numeric scalar |
   | `Yaw` | 参与者的偏航角，单位为 degrees。 | Numeric scalar |
   | `AngularVelocity` | 参与者的角速度 (*ω*)，单位为 degrees per second，沿 *x*、*y* 和 *z* 方向。 | Three-element vector of the form [`ωx ωy ωz`] |
2. 用于生成新点云的仿真时间，指定为 positive scalar。

您可以从 Scenario Reader (Automated Driving Toolbox) 模块输出场景参与者位姿。
### 输出

### **IsValid** — 有效的仿真时间 `0` | `1`

有效的仿真时间，以逻辑值 `0`（`false`）或 `1`（`true`）返回。对于在 **传感器更新之间所需间隔 (s)** 参数指定的更新间隔之间请求的更新，此值为 `0`。

**数据类型：** `Boolean`

### **Location** — 点的位置值 *M*-by-*N*-by-3 matrix

点云中点的位置值，以 *M*-by-*N*-by-3 matrix 返回。*M*、*N* 分别为有序点云中的行数和列数。

### **Intensity** — 点的强度值 *M*-by-*N* matrix

点云中点的强度值，以 *M*-by-*N* matrix 返回。*M*、*N* 分别为有序点云中的行数和列数。

### **Clusters** — 参与者的分类数据 *M*-by-*N*-by-3 array

场景中参与者的分类数据，以 *M*-by-*N*-by-3 array 返回。*M*、*N* 分别为有序点云中的行数和列数。数组的第一维包含 `ActorID`s，第二维包含目标参与者的 `ClassID`s，第三维包含材质 ID，这些 ID 表示 **JSON 格式的材质属性信息** 的索引。

## 参数

### 参数

#### 传感器标识

### **传感器的唯一标识符** — 唯一的传感器标识符 `1`（默认）| positive integer

传感器的唯一标识符，指定为 positive integer。在多传感器系统中，此索引用于区分不同的传感器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **传感器更新之间所需间隔 (s)** — 传感器更新之间所需的时间间隔 `0.1`（默认）| positive scalar

两个连续传感器更新之间的时间间隔，指定为 positive scalar。模块按此参数指定的间隔生成新检测。该值必须是仿真时间的整数倍。在更新间隔之间从传感器请求的更新不包含任何检测。单位为 seconds。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **用于选择典型值的传感器模型** — 传感器模型的名称 `Custom`（默认）| `HDL64E` | `HDL32E` | `VLP16` | `VLP32C` | `VLS128` | `PuckLITE` | `PuckHiRes` | `OS0-32` | `OS0-64` | `OS0-128` | `OS1Gen1-32` | `OS1Gen1-64` | `OS1Gen1-128` | `OS1Gen2-32` | `OS1Gen2-64` | `OS1Gen2-128` | `OS2-32` | `OS2-64` | `OS2-128`

*自 R2024a 起*

指定传感器模型的名称。有关支持的传感器模型的信息，请参阅支持的传感器。此参数根据指定的传感器设置默认仰角值。要应用自定义仰角，请将此参数设置为 `Custom`，并使用 **仰角 (deg)** 参数。

#### 依赖关系

当您未将此参数设置为 `Custom` 时，模块会禁用以下参数：

- **使用仰角**
- **仰角 (deg)**
- **仰角限制 (deg)**
- **仰角分辨率 (deg)**

#### 传感器安装

### **位置 [X Y Height] (m)** — 传感器中心位置 `[1.5 0 1.6]`（默认）| three-element vector of form [*X* *Y* *Height*]

传感器中心位置，指定为 three-element vector of the form [*X* *Y* *Height*]。*X* 和 *Y* 的值表示传感器中心相对于自车坐标系 *X* 轴和 *Y* 轴的位置。*Height* 是传感器离地高度。默认值定义了安装在轿车车顶前缘的 lidar 传感器。单位为 meters。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **方向 [Roll Pitch Yaw] (deg)** — 传感器方向 `[0 0 0]`（默认）| three-element vector

传感器方向，指定为 three-element vector of the form，[*Roll* *Pitch* *Yaw*]。这些值相对于自车坐标系。单位为 degrees。

- *Roll* — 横滚角是围绕前后轴（即自车坐标系的 *x* 轴）旋转的角度。正横滚角对应于沿 *x* 轴正方向观察时的顺时针旋转。
- *Pitch* — 俯仰角是围绕左右轴（即自车坐标系的 *y* 轴）旋转的角度。正俯仰角对应于沿 *y* 轴正方向观察时的顺时针旋转。
- *Yaw* — 偏航角是围绕垂直轴（即自车坐标系的 *z* 轴）旋转的角度。正偏航角对应于沿 *z* 轴正方向观察时的顺时针旋转。当从上方观察车辆时，此旋转看起来是逆时针方向。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### 参与者配置文件

### **MATLAB 或模型工作区参与者配置文件变量名** — 参与者配置文件的变量名 `actor_profiles`（默认）| 有效的变量名

参与者配置文件的变量名，指定为包含参与者配置文件的 MATLAB 或模型工作区变量的名称。

参与者配置文件是场景中参与者的物理特征，指定为结构体或 *L* 元素的结构体数组。*L* 是场景中参与者的数量。

如果参与者配置文件变量具有单个结构体，则在 **ActorPoses** 输入端口指定的所有参与者都使用相同的配置文件。

要为您的驾驶场景 `drivingScenario` (Automated Driving Toolbox) 生成参与者配置文件结构体数组，请使用 `actorProfiles` (Automated Driving Toolbox) 函数。您也可以手动创建这些结构体。下表显示了有效的结构体字段。

| 字段 | 描述 | 值 |
| --- | --- | --- |
| `ActorID` | 参与者的唯一标识符。在具有多个参与者的场景中，此值用于区分不同的参与者。 | Positive integer |
| `ClassID` | 参与者的用户定义分类 ID。  | `ClassID` | 类别名称 | | --- | --- | | `1` | Car | | `2` | Truck | | `3` | Bicycle | | `4` | Pedestrian | | `5` | Jersey Barrier | | `6` | Guardrail | | Positive scalar |
| `Length` | 参与者的长度，单位为 meters。 | Positive scalar |
| `Width` | 参与者的宽度，单位为 meters。 | Positive scalar |
| `Height` | 参与者的高度，单位为 meters。 | Positive scalar |
| `OriginOffset` | 参与者的旋转中心相对于其几何中心的偏移。旋转中心（或原点）位于参与者的底部中心。对于车辆，旋转中心是后轴中心下方地面上的点。 | A three-element vector of the form `[x y z]`. Units are in meters. |
| `MeshVertices` | 网格表示中参与者的顶点。 | *N*-by-3 numeric matrix，其中每一行定义 3-D 空间中的一个顶点。 |
| `MeshFaces` | 网格表示中参与者的面。 | *M*-by-3 integer matrix，其中每一行表示一个由顶点 ID 定义的三角形，这些 ID 是 `MeshVertices` 的行号。 |
| `MeshTargetReflectances` | 参与者每个三角形面的材质反射率。 | *M*-by-1 numeric vector，其中 *M* 是参与者的三角形面数量。每个值必须在范围 `[0, 1]` 内。 |

有关这些结构体字段的详细信息，请参阅 `actor` (Automated Driving Toolbox) 和 `vehicle` (Automated Driving Toolbox) 函数。

### **主车的 ActorID** — 自车的 Actor ID `1`（默认）| positive integer

自车的 `ActorID` 值，指定为 positive integer。`ActorID` 是参与者的唯一标识符。此参数必须是 **ActorPoses** 输入端口指定的有效 `ActorID`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### 点云报告

### **用于报告点云数据的坐标系** — 报告的检测所在的坐标系 `World`（默认）| `Sensor` | `Host`

*自 R2024b 起*

报告的检测所在的坐标系，指定为以下值之一：

- `Sensor` — 模块在传感器坐标系中报告检测。
- `Host` — 模块在主车参与者的坐标系中报告检测。
- `World` — 模块在世界坐标系中报告检测。

### 传感器视场

#### 设置

### **传感器的最大检测范围 (m)** — 最大检测范围 `120`（默认）| positive scalar

传感器的最大检测范围，指定为 positive scalar。传感器无法扫描超出此范围的点。单位为 meters。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **方位角限制 (deg)** — lidar 传感器的方位角限制 `[-180 180]`（默认）| two-element vector

lidar 传感器的方位角限制，指定为 two-element vector of the form [*min* *max*]。值必须在范围 `[-180, 180]` 内，*max* 必须大于 *min*。单位为 degrees。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **方位角分辨率 (deg)** — lidar 传感器的方位角分辨率 `0.16`（默认）| positive scalar

lidar 传感器的方位角分辨率，指定为 positive scalar。单位为 degrees。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **使用仰角** — 使用自定义仰角 `off`（默认）| `on`

选择此参数以使用自定义仰角。

#### 依赖关系

- 要启用此参数，请将 **用于选择典型值的传感器模型** 参数设置为 `Custom`。
- 当您选择此参数时，模块会禁用 **仰角限制 (deg)** 和 **仰角分辨率 (deg)** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **仰角 (deg)** — lidar 传感器的仰角 *N*-element real-valued vector

lidar 传感器的自定义仰角，指定为 *N*-element real-valued vector。*N* 是仰角通道的数量。向量中的元素必须按递增顺序排列。单位为 degrees。

#### 依赖关系

要启用此参数：

- 将 **用于选择典型值的传感器模型** 参数设置为 `Custom`。
- 选择 **使用仰角** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **仰角限制 (deg)** — lidar 传感器的仰角限制 `[-20 20]`（默认）| two element vector of form [*min*, *max*]

lidar 传感器的仰角限制，指定为 two-element vector of the form [*min* *max*]。值必须在范围 `[-180, 180]` 内，*max* 必须大于 *min*。单位为 degrees。

#### 依赖关系

要启用此参数：

- 将 **用于选择典型值的传感器模型** 参数设置为 `Custom`。
- 清除 **使用仰角** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **仰角分辨率 (deg)** — lidar 传感器的仰角分辨率 `1.25`（默认）| positive scalar

lidar 传感器的仰角分辨率，指定为以 degrees 为单位的 positive scalar。

#### 依赖关系

要启用此参数：

- 将 **用于选择典型值的传感器模型** 参数设置为 `Custom`。
- 清除 **使用仰角** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### 高级设置

#### 噪声仿真

### **向测量添加噪声** — 向测量添加噪声 `on`（默认）| `off`

当您选择此参数时，模块会使用 **距离精度 (m)** 参数作为一个标准差，向点云中的每个点添加随机高斯噪声。否则，数据没有噪声。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **距离精度 (m)** — 传感器距离测量的精度 `0.002`（默认）| positive scalar

传感器距离测量的精度，指定为 positive scalar。单位为 meters。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### 天气仿真

### **雾能见度 (meters)** — 雾中的可见距离 `1000`（默认）| positive scalar

雾中的可见距离，指定为以 meters 为单位的 positive scalar。此参数的值不得大于 1000。值越高表示能见度越好，雾的影响越小。默认值 `1000` 表示能见度清晰，即无雾。

**注意**

当您同时指定 **雾能见度 (meters)** 和 **降雨率 (mm/hour)** 参数时，模块仅仿真雾天天气。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **降雨率 (mm/hour)** — 降雨速率 `0`（默认）| positive scalar

降雨速率，指定为以 millimeter per hour 为单位的 positive scalar。此参数的值不得大于 200。增大此值会增加降雨对生成的点云的影响。默认值为 `0`，表示无降雨。

**注意**

当您同时指定 **雾能见度 (meters)** 和 **降雨率 (mm/hour)** 参数时，模块仅仿真雾天天气。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### 运动畸变

### **仿真运动畸变** — 仿真运动畸变 `off`（默认）| `on`

*自 R2024a 起*

选择此参数以仿真由自车运动引起的点云数据畸变。

### **激光发射时间 (s)** — 激光雷达传感器中激光器的发射时间 `[]`（默认）| 正标量 | 正数值向量

*自 R2024a 起*

指定激光雷达传感器中激光器的发射时间。要为传感器中的所有激光器指定相同的发射时间，请使用正标量。否则，请使用正数值向量。该向量的长度必须与 **仰角 (deg)** 参数的长度匹配。

如果未选择 **使用仰角** 参数，则该向量的长度必须与 **仰角限制 (deg)** 和 **仰角分辨率 (deg)** 参数一致。例如，如果将 **仰角限制 (deg)** 参数设置为 `[-20 20]`，并将 **仰角分辨率 (deg)** 参数设置为 `1.25`，则 **激光发射时间 (s)** 向量的长度必须与向量 `[-20:1.25:20]` 的长度匹配。

#### 依赖关系

要启用此参数，请选择 **模拟运动畸变** 参数。

**数据类型：** `single` | `double`

### 场景材质属性

### **JSON 格式的材质属性信息** — JSON 格式的材质属性信息 字符串标量 | 字符向量

*自 R2024b 起*

选择此参数可查看或编辑 JSON 格式的目标材质属性信息。有关材质属性的详细信息，请参阅 `MaterialAttributes` 属性。

#### 依赖关系

- 要启用此参数，请选择 **编辑 JSON 文本以添加、删除或修改材质属性**。

### **编辑 JSON 文本以添加、删除或修改材质属性** — 编辑 JSON 文本以添加、删除或修改材质属性 `off`（默认）| `on`

*自 R2024b 起*

选择此参数可启用编辑以 JSON 格式存储的材质属性信息。

### 输出端口设置

### **输出强度端口** — 点的输出强度值 `on`（默认）| `off`

选择此参数可启用 **Intensity** 输出端口。

### **输出聚类端口** — 点的输出分割值 `on`（默认）| `off`

选择此参数可启用 **Clusters** 输出端口。

## 所属库

Lidar Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2023a 中引入**

### R2024b：使用来自 RoadRunner Scenario 的目标材质信息

现在，您可以使用 **场景材质属性** 选项卡中的参数，利用 RoadRunner Scenario 中目标参与者的材质信息生成点云数据。**Clusters** 输出端口还包含材质 ID 信息。

### R2024b：指定用于报告点云数据的坐标系

使用 **用于报告点云数据的坐标系** 参数为输出点云指定 `World`、`Host` 或 `Sensor` 类型的坐标系。

### R2024a：指定传感器模型

现在，您可以使用 **用于选择典型值的传感器模型** 参数指定传感器模型的类型。此参数根据指定的传感器设置默认仰角值。

### R2024a：模拟运动畸变

现在，您可以使用 **模拟运动畸变** 和 **激光发射时间 (s)** 参数模拟运动畸变。

### R2024a：将激光雷达传感器添加到 RoadRunner Scenario 中的车辆参与者

现在，您可以使用 Simulink 中定义的激光雷达传感器模型在 RoadRunner 场景中生成点云数据。当在 RoadRunner Scenario 仿真中与参与者一起使用时，该模块不需要任何输入。

## 描述

为场景生成激光雷达点云数据

Lidar Sensor 模块根据安装在自车上的激光雷达传感器记录的测量值生成点云数据。生成的数据位于自车坐标系中。

要为场景生成点云数据，您可以使用此模块配置传感器和参与者位姿。该模块还输出生成点的强度和分割值。

此外，您还可以使用此模块执行以下操作：

- 配置激光雷达传感器参数，例如范围、方位角和仰角。
- 向点云中的点添加随机高斯噪声。
- 模拟雾和雨等天气条件。

您可以使用 `drivingScenario`（Automated Driving Toolbox）对象创建包含参与者和轨迹的场景，使用 Scenario Reader (Automated Driving Toolbox) 模块将此数据导入 Simulink®，然后使用 Lidar Sensor 模块为该场景生成点云数据。

您还可以在 RoadRunner Scenario 仿真中将该模块与车辆参与者一起使用。当在 RoadRunner Scenario 仿真中与参与者一起使用时，该模块不需要任何输入。有关详细信息，请参阅 Integrate Lidar Sensor Model into RoadRunner Scenario and Cosimulate with Unreal Engine。*(自 R2024a 起)*

使用 Lidar Sensor 模块创建的激光雷达传感器模型使用硬件加速光线追踪，以在点云中生成高度逼真且准确的对象表示。光线追踪允许精确对激光雷达传感器发射的光线与场景中对象表面之间的相互作用进行建模。此外，光线追踪会考虑表面纹理和角度等因素，从而提高输出点云数据的逼真度和准确性。

**提示**

在针对驾驶场景仿真配置的模型中，Scenario Reader 模块必须在 Lidar Sensor 模块之前执行。这样，Lidar Sensor 模块才能正确处理驾驶场景数据。要检查模块执行顺序，请右键点击这些模块并选择 **属性**。在 **常规** 选项卡上，确认以下 **优先级** 设置：

- Scenario Reader — `0`
- Lidar Sensor — `1`

。
