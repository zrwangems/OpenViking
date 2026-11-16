---
type: simulink-block
title: 'Scenario Reader'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'scenarioreader'
documentation_source_path: 'ref/scenarioreader.html'
language: zh-CN
chinese_source: worker-translation
---

# Scenario Reader

## 端口

### 输入

### **Ego Vehicle** — 本车姿态，包含 MATLAB® structure 的 Simulink bus

本车姿态，指定为包含 MATLAB structure 的 Simulink bus。

该结构必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位是 meters。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位是 meters。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位是 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位是 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位是 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位是 degrees。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位是 degrees per second。 |

当您将参与者从本车坐标转换为世界坐标以用于 3D 仿真环境时，输出本车姿态。例如，请参阅 Visualize Sensor Data from Unreal Engine Simulation Environment。

#### 依赖关系

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Source of ego vehicle** 参数设置为 `Input port`。

### 输出

### **Actors** — 场景参与者姿态，包含 MATLAB structure 的 Simulink bus

场景参与者姿态，返回为包含 MATLAB structure 的 Simulink bus。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real-valued scalar |
| `Actors` | 参与者姿态 | 长度为 `NumActors` 的参与者姿态结构数组 |

`Actors` 中的每个参与者姿态结构包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位是 meters。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位是 meters。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位是 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位是 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位是 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位是 degrees。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位是 degrees per second。 |

本车姿态从 `Actors` 数组中排除。

要从模块返回参与者姿态，必须将整个驾驶场景仿真运行至完成。

### **Lane Boundaries** — 场景车道边界，包含 MATLAB structure 的 Simulink bus

场景车道边界，返回为包含 MATLAB structure 的 Simulink bus。

该结构包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumLaneBoundaries` | 车道边界数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real scalar |
| `LaneBoundaries` | 相对于本车从最左侧车道开始的车道边界。 | 长度为 `NumLaneBoundaries` 的车道边界结构数组 |

`LaneBoundaries` 中的每个车道边界结构包含以下字段。

|  |  |
| --- | --- |
| **字段** | **描述** |
| `Coordinates` | 车道边界坐标，指定为 real-valued *N*×3 矩阵，其中 *N* 是车道边界坐标的数量。车道边界坐标定义了沿着道路中心、距本车指定纵向距离处的边界点位置。 - 在 MATLAB 中，使用 `laneBoundaries` 函数的 `'XDistance'` 名称-值对参数指定这些距离。 - 在 Simulink 中，使用 Scenario Reader 模块的 **Distances from ego vehicle for computing boundaries (m)** 参数或 Simulation 3D Vision Detection Generator 模块的 **Distance from parent for computing lane boundaries** 参数指定这些距离。 此矩阵还包括距本车零距离处的边界坐标。这些坐标位于本车原点的左侧和右侧，本车原点位于后轴中心下方。单位是 meters。 |
| `Curvature` | `Coordinates` 矩阵每一行处的车道边界曲率，指定为 real-valued *N*×1 向量。*N* 是车道边界坐标的数量。单位是 radians per meter。 |
| `CurvatureDerivative` | `Coordinates` 矩阵每一行处的车道边界曲率的导数，指定为 real-valued *N*×1 向量。*N* 是车道边界坐标的数量。单位是 radians per square meter。 |
| `HeadingAngle` | 初始车道边界航向角，指定为 real scalar。车道边界的航向角相对于本车航向。单位是 degrees。 |
| `LateralOffset` | 本车位置相对于车道边界的横向偏移，指定为 real scalar。本车左侧的车道边界偏移为正。本车右侧的车道边界偏移为负。单位是 meters。在此图中，本车距左侧车道偏移 1.5 meters，距右侧车道偏移 2.1 meters。 本车在行驶车道中 |
| `BoundaryType` | 车道边界标记的类型，指定为以下值之一： - `'Unmarked'` — 不存在物理车道标记 - `'Solid'` — 单条不间断线 - `'Dashed'` — 单条虚线车道标记 - `'DoubleSolid'` — 两条不间断线 - `'DoubleDashed'` — 两条虚线 - `'SolidDashed'` — 左侧实线和右侧虚线 - `'DashedSolid'` — 左侧虚线和右侧实线 |
| `Strength` | 车道边界标记的饱和度强度，指定为 0 到 1 之间的 real scalar。值 `0` 对应于颜色完全不饱和的标记。标记为灰色。值 `1` 对应于颜色完全饱和的标记。 |
| `Width` | 车道边界宽度，指定为 positive real scalar。在双线车道标记中，两条线以及线之间的空间使用相同的宽度。单位是 meters。 |
| `Length` | 虚线中虚线的长度，指定为 positive real scalar。在双线车道标记中，两条线使用相同的长度。 |
| `Space` | 虚线中虚线之间的空间长度，指定为 positive real scalar。在虚线双线车道标记中，两条线使用相同的空间。 |

返回的车道边界结构数量取决于 **Lane boundaries to output** 参数值。

#### 依赖关系

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `Ego lane boundaries` 或 `All lane boundaries`。

### **Ego Vehicle Pose** — 本车姿态，包含 MATLAB structure 的 Simulink bus

本车姿态，返回为包含 MATLAB structure 的 Simulink bus。

该结构必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位是 meters。 **注意** 如果驾驶场景不包含至少一辆车辆的前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位是 meters。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位是 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位是 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位是 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位是 degrees。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位是 degrees per second。 |

#### 依赖关系

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Source of ego vehicle** 参数设置为 `Scenario`。
3. 选中 **Output ego vehicle pose** 参数。

### **Ego Vehicle State** — 本车状态，包含 MATLAB structure 的 Simulink bus

本车状态，返回为包含 MATLAB structure 的 Simulink bus。

该结构必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位是 meters。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位是 meters per second。 |
| `Orientation` | 参与者的方向，指定为 [`roll pitch yaw`] 角度的 real-valued vector。单位是 degrees。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位是 degrees per second。 |
| `Acceleration` | 参与者在 *x*、*y* 和 *z* 方向上的加速度 (*a*)，指定为形式为 [*a**x* *a**y* *a**z*] 的 real-valued vector。单位是 meters per second squared。 |

#### 依赖关系

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Source of ego vehicle** 参数设置为 `Scenario`。
3. 选中 **Output ego vehicle state** 参数。

## 参数

#### 场景

### **Source of driving scenario** — 驾驶场景来源 `From file` (default) | `From workspace`

驾驶场景来源，指定为以下选项之一：

- `From file` — 在 **Driving Scenario Designer file name** 参数中，指定从 Driving Scenario Designer 应用保存的场景文件的名称。
- `From workspace` — 在 **MATLAB or model workspace variable name** 参数中，指定包含 `drivingScenario` 对象的 MATLAB 或模型工作区变量的名称。

### **Driving Scenario Designer file name** — 场景文件名 `EgoVehicleGoesStraight.mat` (default) | MATLAB 搜索路径上的场景文件 | 场景文件的路径

场景文件名，指定为 MATLAB 搜索路径上的场景文件或场景文件的完整路径。场景文件必须是从 Driving Scenario Designer 应用保存的 MAT 文件。如果 **Source of ego vehicle** 参数设置为 `Scenario`，则场景必须包含本车。否则，模块在仿真期间返回错误。

如果指定的场景文件包含传感器，模块会忽略它们。要在模型中包含场景中的传感器，请参阅提示。

默认场景文件显示一辆本车在笔直的双车道道路上向北行驶，另一辆车在对面车道向南行驶。

要将场景文件添加到 MATLAB 搜索路径，请使用 `addpath` 函数。例如，以下代码将包含预构建 Euro NCAP® 场景的文件夹集添加到 MATLAB 搜索路径。

```
path = fullfile(matlabroot,'toolbox','shared','drivingscenario', ...
'PrebuiltScenarios','EuroNCAP');
addpath(genpath(path))
```

然后，在 **Driving Scenario Designer file name** 参数中，您可以指定这些文件夹中任何场景的名称，而无需指定完整文件路径。例如：`AEB_PedestrianChild_Nearside_50width.mat`。

在模型中使用完场景后，您可以使用 `rmpath` 函数从 MATLAB 搜索路径中删除任何添加的文件夹。

```
rmpath(genpath(path))
```

#### 依赖关系

要启用此参数，请将 **Source of driving scenario** 参数设置为 `From file`。

### **MATLAB or model workspace variable name** — 场景变量名 `scenario` (default) | `drivingScenario` 对象变量名

场景变量名，指定为包含有效 `drivingScenario` 对象的 MATLAB 或模型工作区变量的名称。如果同名的场景变量同时存在于 MATLAB 和模型工作区中，模块使用模型工作区中定义的变量。

如果 **Source of ego vehicle** 参数设置为 `Scenario`，则 `drivingScenario` 对象必须包含本车。要指定对象中哪个参与者是本车，请在 **Ego vehicle ActorID** 参数中指定该参与者的 `ActorID` 属性值。

默认变量名 `scenario` 是由 Driving Scenario Designer 应用导出的 MATLAB 函数生成的 `drivingScenario` 对象的默认名称。默认情况下，此变量不包含在 MATLAB 或模型工作区中。

#### 依赖关系

要启用此参数，请将 **Source of driving scenario** 参数设置为 `From workspace`。

### **Coordinate system of actors output** — 参与者输出的坐标系 `Vehicle coordinates` (default) | `World coordinates`

输出参与者的坐标系，指定为以下值之一：

- `Vehicle coordinates` — 坐标相对于本车定义。当您的场景只有一个本车时，选择此值。
- `World coordinates` — 坐标相对于驾驶场景定义。在包含多个本车的多智能体场景中，选择此值。如果选择此值，则不支持使用 Bird's-Eye Scope 进行模型可视化。

有关本车和世界坐标系的更多详细信息，请参阅 Coordinate Systems in Automated Driving Toolbox。

### **Source of ego vehicle** — 本车来源 `Scenario` (default) | `Input port`

本车来源，指定为以下选项之一：

- `Scenario` — 使用由 **Driving Scenario Designer file name** 或 **MATLAB or model workspace variable name** 参数指定的场景中定义的本车。本车姿态从 **Actors** 输出端口中排除。参与者位置采用本车坐标，这意味着它们相对于场景中本车的世界坐标位置。

  选择此选项以测试开环 ADAS 算法，其中本车行为是预定义的，并且不随场景推进而改变。有关示例，请参阅 Test Open-Loop ADAS Algorithm Using Driving Scenario。
- `Input port` — 使用 **Ego Vehicle** 输入端口指定本车。本车姿态不包含在 **Actors** 输出端口中。

  使用此选项时，模型中的本车必须包含世界坐标中的起始位置。所有其他参与者姿态均采用本车坐标，并相对于本车定位。有关具有已定义位置信息的本车示例，请参阅 Lane Keeping Assist with Lane Detection。在定义本车的起始位置时，请考虑使用场景中已定义的位置。通过使用此位置，如果您将 **Source of ego vehicle** 设置为 `Scenario`，然后再设置回 `Input port`，则无需手动更改起始位置。

  选择此选项以测试闭环 ADAS 算法，其中本车随场景推进而对变化做出反应。有关示例，请参阅 Test Closed-Loop ADAS Algorithm Using Driving Scenario。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。

### **Ego vehicle ActorID** — 本车的参与者 ID `1` (default) | positive integer

本车的参与者 ID，指定为 positive integer。使用此参数以使用从 `drivingScenario` 对象读取的本车进行仿真。

- 当 **Source of ego vehicle** 设置为 `Scenario` 时，将此参数设置为存储在指定 `drivingScenario` 对象的 `Actors` 属性中的 `ActorID` 值。要检查有效的 `ActorID` 值，请使用以下语法，其中 `scenario` 是 `drivingScenario` 变量名。

  ```
  actorIDs = [scenario.Actors.ActorID]
  ```
- 当 **Source of ego vehicle** 设置为 `Input Port` 时，必须将此参数设置为模块的 **Ego Vehicle** 输入端口处的 `ActorID` 值。

#### 依赖关系

要启用此参数，请按以下顺序设置这些参数：

1. 将 **Source of driving scenario** 参数设置为 `From workspace`。
2. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。

### **Output ego vehicle pose** — 输出本车姿态 `off` (default) | `on`

选中此参数以在 **Ego Vehicle Pose** 端口输出本车姿态。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`，并将 **Source of ego vehicle** 参数设置为 `Scenario`。

### **Output ego vehicle state** — 输出本车状态 `off` (default) | `on`

选中此参数以在 **Ego Vehicle State** 端口输出本车状态。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`，并将 **Source of ego vehicle** 参数设置为 `Scenario`。

要输出本车状态，必须使用驾驶场景 API 中的 `smoothTrajectory` 函数创建本车轨迹，或在 Driving Scenario Designer 应用中选择 **Use smooth, jerk-limited trajectory** 参数。

### **Ego vehicle follows ground** — 使本车定向以跟随路面 `off` (default) | `on`

选中此参数以使本车定向以跟随路面的高程。模块更新本车的高程、横滚、俯仰和偏航，并输出相对于更新后的本车坐标的参与者和车道边界。模块不更新本车的速度或角速度。

在道路网络高程变化的闭环仿真中使用此参数。

**注意**

在高程和倾斜角不同的道路交汇处，更新后的本车值可能不准确。

在开环仿真中，当 **Source of ego vehicle** 设置为 `Scenario` 时，本车跟随驾驶场景中指定的高程。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 设置为 `Vehicle coordinates`，并将 **Source of ego vehicle** 设置为 `Input port`。

### **Sample time (s)** — 仿真采样时间 `0.1` (default) | positive real scalar

仿真采样时间，以秒为单位，指定为 positive real scalar。不支持继承和连续采样时间。此采样时间与 Driving Scenario Designer 应用和 `drivingScenario` 对象在仿真期间使用的采样时间分开。

#### 车道

### **Lane boundaries to output** — 要输出的车道边界 `None` (default) | `Ego vehicle lane boundaries` | `All lane boundaries`

要输出的车道边界，指定为以下选项之一：

- `None` — 不输出任何车道边界。
- `Ego vehicle lane boundaries` — 输出本车的左侧和右侧车道边界。
- `All lane boundaries` — 输出本车所行驶道路的所有车道边界。

如果选择 `Ego vehicle lane boundaries` 或 `All lane boundaries`，则模块在 **Lane Boundaries** 输出端口中返回车道边界。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。

### **Distances from ego vehicle for computing boundaries (m)** — 从本车计算车道边界的距离 `linspace(-150,150,101)` (default) | *N* 元素 real-valued vector

从本车计算车道边界的距离，指定为 *N* 元素 real-valued vector。*N* 是距离值的数量。当从后向摄像头检测车道时，指定负距离。当前向摄像头检测车道时，指定正距离。单位是 meters。

默认情况下，模块计算从本车后方 150 meters 到本车前方 150 meters 范围内的 101 条车道边界。这些距离线性间隔 3 meters。

**示例：** `1:0.1:10` 在本车前方 1 到 10 meters 范围内每 0.1 meters 计算一条车道边界。

#### 依赖关系

要启用此参数，请将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。

### **Location of boundaries on lane markings** — 车道边界位置 `Center of lane markings` (default) | `Inner edge of lane markings`

车道标记上的车道边界位置，指定为此表中的一个选项。

| 车道边界位置 | 描述 | 示例 |
| --- | --- | --- |
| `Center of lane markings` | 车道边界以车道标记为中心。 | 一条三车道道路有四条车道边界：每条车道标记一条。 具有四条车道边界的三车道道路 |
| `Inner edge of lane markings` | 车道边界放置在车道标记的内边缘。 | 一条三车道道路有六条车道边界：每条车道两条。 具有六条车道边界的三车道道路 |

#### 依赖关系

要启用此参数，请将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。

#### 端口设置

### **Source of actors bus name** — 参与者姿态总线名称来源 `Auto` (default) | `Property`

**Actors** 输出端口中返回的参与者姿态总线的名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建参与者姿态总线名称。
- `Property` — 使用 **Actors bus name** 参数指定参与者姿态总线名称。

### **Actors bus name** — 参与者姿态总线名称 valid bus name

**Actors** 输出端口中返回的参与者姿态总线的名称，指定为 valid bus name。

#### 依赖关系

要启用此参数，请将 **Source of actors bus name** 设置为 `Property`。

### **Source of maximum number of actors** — 最大参与者数量来源 `Scenario` (default) | `Property`

驾驶场景中可拥有的最大参与者数量的来源，指定为以下选项之一：

- `Scenario` — 模块将最大参与者数量设置为驾驶场景中的参与者数量。此值等于 **Actors** 输出端口返回的总线的 `NumActors` 字段。当您更改输入场景时，最大参与者数量会更新以匹配新的 `NumActors` 值。
- `Property` — 使用 **Maximum number of actors** 参数指定最大参与者数量。当您希望在具有不同参与者数量的场景中重用同一参与者总线时（例如从引用模型输出参与者时），选择此选项。

### **Maximum number of actors** — 最大参与者数量 `100` (default) | positive integer

场景中可拥有的最大参与者数量，指定为 positive integer。

#### 依赖关系

要启用此参数，请将 **Source of maximum number of actors** 参数设置为 `Property`。

### **Source of lane boundaries bus name** — 车道边界总线名称来源 `Auto` (default) | `Property`

**Lane Boundaries** 输出端口中返回的车道边界总线的名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建车道边界总线名称。
- `Property` — 使用 **Lane boundaries bus name** 参数指定车道边界总线名称。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。

### **Lane boundaries bus name** — 车道边界总线名称 valid bus name

**Lane Boundaries** 输出端口中返回的车道边界总线的名称，指定为 valid bus name。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。
3. 将 **Source of lane boundaries bus name** 参数设置为 `Property`。

### **Source of maximum number of lane boundaries** — 最大车道边界数量来源 `Scenario` (default) | `Property`

驾驶场景中可拥有的最大车道边界数量的来源，指定为以下选项之一：

- `Scenario` — 模块将最大车道边界数量设置为驾驶场景中的车道边界数量。此值等于 **Lane Boundaries** 输出端口返回的总线的 `NumLaneBoundaries` 字段。当您更改输入场景时，最大车道边界数量会更新以匹配新的 `NumLaneBoundaries` 值。
- `Property` — 使用 **Maximum number of lane boundaries** 参数指定最大车道边界数量。当您希望在具有不同车道边界数量的场景中重用同一车道边界总线时（例如从引用模型输出车道边界时），选择此选项。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `All lane boundaries`。

### **Maximum number of lane boundaries** — 最大车道边界数量 `10` (default) | positive integer

场景中可拥有的最大车道边界数量，指定为 positive integer。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `All lane boundaries`。
3. 将 **Source of maximum number of lane boundaries** 参数设置为 `Property`。

### **Source of ego vehicle pose bus name** — 本车姿态总线名称来源 `Auto` (default) | `Property`

**Ego Vehicle Pose** 输出端口中返回的本车姿态总线的名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建本车姿态总线名称。
- `Property` — 使用 **Ego vehicle pose bus name** 参数指定本车姿态总线名称。

#### 依赖关系

要启用此参数，请选中 **Output ego vehicle pose** 参数。

### **Ego vehicle pose bus name** — 本车姿态总线名称 valid bus name

**Ego Vehicle Pose** 输出端口中返回的本车姿态总线的名称，指定为 valid bus name。

#### 依赖关系

要启用此参数，请选中 **Output ego vehicle pose** 参数，并将 **Source of ego vehicle pose bus name** 参数设置为 `Property`。

### **Source of ego vehicle state bus name** — 本车状态总线名称来源 `Auto` (default) | `Property`

**Ego Vehicle State** 输出端口中返回的本车状态总线的名称来源，指定为以下选项之一：

- `Auto` — 模块自动创建本车状态总线名称。
- `Property` — 使用 **Ego vehicle state bus name** 参数指定本车状态总线名称。

#### 依赖关系

要启用此参数，请选中 **Output ego vehicle state** 参数。

### **Ego vehicle state bus name** — 本车状态总线名称 valid bus name

**Ego Vehicle State** 输出端口中返回的本车状态总线的名称，指定为 valid bus name。

#### 依赖关系

要启用此参数，请选中 **Output ego vehicle state** 参数，并将 **Source of ego vehicle state bus name** 参数设置为 `Property`。

### **Show coordinate labels** — 显示输入和输出的坐标系 `on` (default) | `off`

选中此参数以在框图中的 Scenario Reader 模块上显示模块输入和输出的坐标系。

- **Ego Vehicle** 输入和输出始终采用世界坐标。
- **Lane Boundaries** 输出始终采用本车坐标。
- 您可以根据 **Coordinate system of actors output** 参数的选择，以本车坐标或世界坐标返回 **Actors** 输出。

#### 仿真

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。第一次运行仿真时，Simulink 为模块生成 C/C++ 代码。只要模型不更改，C 代码将重用于后续仿真。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 当模型处于快速加速器模式时，Scenario Reader 模块不会根据仿真之间对驾驶场景所做的更改自动重新生成代码。要重新生成这些更改，请手动删除上次仿真生成的 Simulink 项目文件夹 `slprj`。然后，重新运行仿真。或者，更改模式，或通过将 **Simulate using** 参数设置为 `Interpreted execution` 来禁用代码生成。
- **Driving Scenario Designer file name** 和 **MATLAB or model workspace variable name** 参数是字符向量。Encoding of Characters in Code Generation (Simulink) 中描述的限制适用于这些参数。

## 版本历史

**在 R2019a 中引入**

## 描述

将驾驶场景读入模型

Scenario Reader 模块从使用 Driving Scenario Designer 应用创建的场景文件或从 `drivingScenario` 对象中读取道路和参与者。模块输出参与者在本车坐标系或场景世界坐标系中的姿态。您还可以输出车道边界或输出本车姿态以用于 3D 仿真环境。模块还允许输出本车状态，其中包括加速度测量值，以用于传感器模型。

要从输出的参与者姿态和车道边界生成对象和车道边界检测，请将姿态和边界输出传递给传感器模块。使用这些传感器生成的合成检测来测试传感器融合算法、跟踪算法和其他高级驾驶辅助系统 (ADAS) 算法的性能。要可视化这些算法的性能，请使用 Bird's-Eye Scope。

您可以从场景中读取本车，或将模型中定义的本车指定为 Scenario Reader 模块的输入。使用此选项测试闭环车辆控制器算法，例如自动紧急制动 (AEB)、车道保持辅助 (LKA) 或自适应巡航控制 (ACC)。
