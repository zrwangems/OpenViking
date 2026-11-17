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
```yaml
ports:
- name: Ego Vehicle
  summary: 自车姿态 Simulink 总线，包含 MATLAB® 结构体
  direction: input
- name: Actors
  summary: 场景参与者姿态 Simulink 总线，包含 MATLAB 结构体
  direction: output
- name: Lane Boundaries
  summary: 场景车道边界 Simulink 总线，包含 MATLAB 结构体
  direction: output
- name: Ego Vehicle Pose
  summary: 自车姿态 Simulink 总线，包含 MATLAB 结构体
  direction: output
- name: Ego Vehicle State
  summary: 自车状态 Simulink 总线，包含 MATLAB 结构体
  direction: output
```

### 输入

### **Ego Vehicle** — 自车姿态 Simulink 总线，包含 MATLAB® 结构体

自车姿态，指定为包含 MATLAB 结构体的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | 参与者位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

当您将参与者从自车坐标转换为世界坐标以用于 3D 仿真环境时，输出自车姿态。例如，参见 Visualize Sensor Data from Unreal Engine Simulation Environment。

#### 依赖

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Source of ego vehicle** 参数设置为 `Input port`。
### 输出

### **Actors** — 场景参与者姿态 Simulink 总线，包含 MATLAB 结构体

场景参与者姿态，返回为包含 MATLAB 结构体的 Simulink 总线。

该结构体包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `Actors` | 参与者姿态 | 长度为 `NumActors` 的参与者姿态结构体数组 |

`Actors` 中的每个参与者姿态结构体包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | 参与者位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

自车的姿态从 `Actors` 数组中排除。

要从该模块返回参与者姿态，您必须运行整个驾驶场景仿真直至完成。

### **Lane Boundaries** — 场景车道边界 Simulink 总线，包含 MATLAB 结构体

场景车道边界，返回为包含 MATLAB 结构体的 Simulink 总线。

该结构体包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumLaneBoundaries` | 车道边界数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `LaneBoundaries` | 车道边界，从相对于自车的最左侧车道开始。 | 长度为 `NumLaneBoundaries` 的车道边界结构体数组 |

`LaneBoundaries` 中的每个车道边界结构体包含以下字段。

|  |  |
| --- | --- |
| **字段** | **描述** |
| `Coordinates` | 车道边界坐标，指定为实值 *N*×3 矩阵，其中 *N* 是车道边界坐标的数量。车道边界坐标定义了沿道路中心、距自车指定纵向距离处的边界点位置。 - 在 MATLAB 中，使用 `laneBoundaries` 函数的 `'XDistance'` 名称-值对组参数指定这些距离。 - 在 Simulink 中，使用 Scenario Reader 模块的 **Distances from ego vehicle for computing boundaries (m)** 参数或 Simulation 3D Vision Detection Generator 模块的 **Distance from parent for computing lane boundaries** 参数指定这些距离。 此矩阵还包含距自车零距离处的边界坐标。这些坐标位于自车原点的左侧和右侧，自车原点位于后轴中心下方。单位为米。 |
| `Curvature` | `Coordinates` 矩阵每一行处的车道边界曲率，指定为实值 *N*×1 向量。*N* 是车道边界坐标的数量。单位为弧度每米。 |
| `CurvatureDerivative` | `Coordinates` 矩阵每一行处的车道边界曲率导数，指定为实值 *N*×1 向量。*N* 是车道边界坐标的数量。单位为弧度每平方米。 |
| `HeadingAngle` | 初始车道边界航向角，指定为实值标量。车道边界的航向角相对于自车航向。单位为度。 |
| `LateralOffset` | 自车位置相对于车道边界的横向偏移，指定为实值标量。自车左侧车道边界的偏移为正。自车右侧的偏移为负。单位为米。在此图中，自车距左侧车道偏移 1.5 米，距右侧车道偏移 2.1 米。 行驶车道中的自车 |
| `BoundaryType` | 车道边界标线类型，指定为以下值之一： - `'Unmarked'` — 不存在物理车道标线 - `'Solid'` — 单条不间断线 - `'Dashed'` — 单条虚线车道标线 - `'DoubleSolid'` — 两条不间断线 - `'DoubleDashed'` — 两条虚线 - `'SolidDashed'` — 左侧实线，右侧虚线 - `'DashedSolid'` — 左侧虚线，右侧实线 |
| `Strength` | 车道边界标线的饱和度强度，指定为 0 到 1 之间的实值标量。值 `0` 对应于颜色完全不饱和的标线。标线为灰色。值 `1` 对应于颜色完全饱和的标线。 |
| `Width` | 车道边界宽度，指定为正实值标量。在双线车道标线中，两条线及线间间隔使用相同的宽度。单位为米。 |
| `Length` | 虚线中虚线的长度，指定为正实值标量。在双线车道标线中，两条线使用相同的长度。 |
| `Space` | 虚线中虚线之间的间隔长度，指定为正实值标量。在虚线双线车道标线中，两条线使用相同的间隔。 |

返回的车道边界结构体数量取决于 **Lane boundaries to output** 参数值。

#### 依赖

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `Ego lane boundaries` 或 `All lane boundaries`。

### **Ego Vehicle Pose** — 自车姿态 Simulink 总线，包含 MATLAB 结构体

自车姿态，返回为包含 MATLAB 结构体的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆前轴位置，指定为 [*x* *y* *z*] 形式的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | 参与者位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |

#### 依赖

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Source of ego vehicle** 参数设置为 `Scenario`。
3. 选中 **Output ego vehicle pose** 参数。

### **Ego Vehicle State** — 自车状态 Simulink 总线，包含 MATLAB 结构体

自车状态，返回为包含 MATLAB 结构体的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `Position` | 参与者位置，指定为 [*x* *y* *z*] 形式的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为 [*v**x* *v**y* *v**z*] 形式的实值向量。单位为米每秒。 |
| `Orientation` | 参与者的朝向，指定为 [`roll pitch yaw`] 角度的实值向量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为 [*ω**x* *ω**y* *ω**z*] 形式的实值向量。单位为度每秒。 |
| `Acceleration` | 参与者在 *x*、*y* 和 *z* 方向上的加速度 (*a*)，指定为 [*a**x* *a**y* *a**z*] 形式的实值向量。单位为米每二次方秒。 |

#### 依赖

要启用此端口，请按以下顺序设置这些参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Source of ego vehicle** 参数设置为 `Scenario`。
3. 选中 **Output ego vehicle state** 参数。
## 参数
```yaml
parameters:
- name: Source of driving scenario
  summary: 驾驶场景来源 From file（默认）| From workspace
  group: ''
- name: Driving Scenario Designer file name
  summary: 场景文件名 EgoVehicleGoesStraight.mat（默认）| MATLAB 搜索路径上的场景文件 | 场景文件路径
  group: ''
- name: MATLAB or model workspace variable name
  summary: 场景变量名 scenario（默认）| drivingScenario 对象变量名
  group: ''
- name: Coordinate system of actors output
  summary: 参与者输出的坐标系 Vehicle coordinates（默认）| World coordinates
  group: ''
- name: Source of ego vehicle
  summary: 自车来源 Scenario（默认）| Input port
  group: ''
- name: Ego vehicle ActorID
  summary: 自车的参与者 ID 1（默认）| 正整数
  group: ''
- name: Output ego vehicle pose
  summary: 输出自车位姿 off（默认）| on
  group: ''
- name: Output ego vehicle state
  summary: 输出自车状态 off（默认）| on
  group: ''
- name: Ego vehicle follows ground
  summary: 使自车朝向跟随路面 off（默认）| on
  group: ''
- name: Sample time (s)
  summary: 仿真采样时间 0.1（默认）| 正实数标量
  group: ''
- name: Lane boundaries to output
  summary: 要输出的车道边界 None（默认）| Ego vehicle lane boundaries | All lane boundaries
  group: ''
- name: Distances from ego vehicle for computing boundaries (m)
  summary: 用于计算边界的距自车距离 linspace(-150,150,101)（默认）| *N* 元素实值向量
  group: ''
- name: Location of boundaries on lane markings
  summary: 车道边界位置 Center of lane markings（默认）| Inner edge of lane markings
  group: ''
- name: Source of actors bus name
  summary: 参与者位姿总线名称的来源 Auto（默认）| Property
  group: ''
- name: Actors bus name
  summary: 参与者位姿总线名称 有效总线名称
  group: ''
- name: Source of maximum number of actors
  summary: 最大参与者数量的来源 Scenario（默认）| Property
  group: ''
- name: Maximum number of actors
  summary: 最大参与者数量 100（默认）| 正整数
  group: ''
- name: Source of lane boundaries bus name
  summary: 车道边界总线名称的来源 Auto（默认）| Property
  group: ''
- name: Lane boundaries bus name
  summary: 车道边界总线名称 有效总线名称
  group: ''
- name: Source of maximum number of lane boundaries
  summary: 最大车道边界数量的来源 Scenario（默认）| Property
  group: ''
- name: Maximum number of lane boundaries
  summary: 最大车道边界数量 10（默认）| 正整数
  group: ''
- name: Source of ego vehicle pose bus name
  summary: 自车位姿总线名称的来源 Auto（默认）| Property
  group: ''
- name: Ego vehicle pose bus name
  summary: 自车位姿总线名称 有效总线名称
  group: ''
- name: Source of ego vehicle state bus name
  summary: 自车状态总线名称的来源 Auto（默认）| Property
  group: ''
- name: Ego vehicle state bus name
  summary: 自车状态总线名称 有效总线名称
  group: ''
- name: Show coordinate labels
  summary: 显示输入和输出的坐标系 on（默认）| off
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

#### 场景

### **Source of driving scenario** — 驾驶场景来源 `From file`（默认）| `From workspace`

驾驶场景来源，指定为以下选项之一：

- `From file` — 在 **Driving Scenario Designer file name** 参数中，指定从 Driving Scenario Designer 应用程序保存的场景文件的名称。
- `From workspace` — 在 **MATLAB or model workspace variable name** 参数中，指定包含 `drivingScenario` 对象的 MATLAB 或模型工作区变量的名称。

### **Driving Scenario Designer file name** — 场景文件名 `EgoVehicleGoesStraight.mat`（默认）| MATLAB 搜索路径上的场景文件 | 场景文件路径

场景文件名，指定为 MATLAB 搜索路径上的场景文件或场景文件的完整路径。场景文件必须是从 Driving Scenario Designer 应用程序保存的 MAT 文件。如果 **Source of ego vehicle** 参数设置为 `Scenario`，则场景必须包含自车。否则，该模块在仿真期间返回错误。

如果指定的场景文件包含传感器，该模块会忽略它们。要将场景中的传感器包含在模型中，请参见提示。

默认场景文件显示一辆自车在笔直的双车道道路上向北行驶，另一辆车在对面车道向南行驶。

要将场景文件添加到 MATLAB 搜索路径，请使用 `addpath` 函数。例如，以下代码将包含预构建 Euro NCAP® 场景的文件夹集添加到 MATLAB 搜索路径。

```
path = fullfile(matlabroot,'toolbox','shared','drivingscenario', ...
'PrebuiltScenarios','EuroNCAP');
addpath(genpath(path))
```

然后，在 **Driving Scenario Designer file name** 参数中，您可以指定位于这些文件夹中的任何场景的名称，而无需指定完整文件路径。例如：`AEB_PedestrianChild_Nearside_50width.mat`。

在模型中使用完场景后，您可以使用 `rmpath` 函数从 MATLAB 搜索路径中删除任何添加的文件夹。

```
rmpath(genpath(path))
```

#### 依赖

要启用此参数，请将 **Source of driving scenario** 参数设置为 `From file`。

### **MATLAB or model workspace variable name** — 场景变量名 `scenario`（默认）| `drivingScenario` 对象变量名

场景变量名，指定为包含有效 `drivingScenario` 对象的 MATLAB 或模型工作区变量的名称。如果同名场景变量同时出现在 MATLAB 和模型工作区中，该模块使用模型工作区中定义的变量。

如果 **Source of ego vehicle** 参数设置为 `Scenario`，则 `drivingScenario` 对象必须包含自车。要指定对象中哪个参与者是自车，请在 **Ego vehicle ActorID** 参数中指定该参与者的 `ActorID` 属性值。

默认变量名 `scenario` 是从 Driving Scenario Designer 应用程序导出的 MATLAB 函数所生成的 `drivingScenario` 对象的默认名称。默认情况下，此变量不包含在 MATLAB 或模型工作区中。

#### 依赖

要启用此参数，请将 **Source of driving scenario** 参数设置为 `From workspace`。

### **Coordinate system of actors output** — 参与者输出的坐标系 `Vehicle coordinates`（默认）| `World coordinates`

输出参与者的坐标系，指定为以下值之一：

- `Vehicle coordinates` — 坐标相对于自车定义。当您的场景只有一个自车时，选择此值。
- `World coordinates` — 坐标相对于驾驶场景定义。在包含多个自车的多智能体场景中选择此值。如果选择此值，则不支持使用 Bird's-Eye Scope 进行模型可视化。

有关车辆坐标系和世界坐标系的更多详细信息，请参见 Coordinate Systems in Automated Driving Toolbox。

### **Source of ego vehicle** — 自车来源 `Scenario`（默认）| `Input port`

自车来源，指定为以下选项之一：

- `Scenario` — 使用由 **Driving Scenario Designer file name** 或 **MATLAB or model workspace variable name** 参数指定的场景中定义的自车。自车的位姿从 **Actors** 输出端口中排除。参与者位置位于车辆坐标系中，这意味着它们相对于场景中自车的世界坐标位置。

  选择此选项可测试开环 ADAS 算法，其中自车行为是预定义的，并且不随场景推进而变化。有关示例，请参阅 Test Open-Loop ADAS Algorithm Using Driving Scenario。
- `Input port` — 使用 **Ego Vehicle** 输入端口指定自车。自车的位姿不包含在 **Actors** 输出端口中。

  使用此选项时，模型中的自车必须包含世界坐标系中的起始位置。所有其他参与者位姿均位于车辆坐标系中，并相对于自车定位。有关具有已定义位置信息的自车示例，请参阅 Lane Keeping Assist with Lane Detection。在定义自车的起始位置时，请考虑使用场景中已定义的位置。通过使用该位置，如果你将 **Source of ego vehicle** 设置为 `Scenario`，然后再设置回 `Input port`，则无需手动更改起始位置。

  选择此选项可测试闭环 ADAS 算法，其中自车会随着场景推进而对变化做出反应。有关示例，请参阅 Test Closed-Loop ADAS Algorithm Using Driving Scenario。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。

### **Ego vehicle ActorID** — 自车的参与者 ID `1`（默认）| 正整数

自车的参与者 ID，指定为正整数。使用此参数可通过从 `drivingScenario` 对象读取的自车进行仿真。

- 当 **Source of ego vehicle** 设置为 `Scenario` 时，将此参数设置为存储在指定 `drivingScenario` 对象的 `Actors` 属性中的 `ActorID` 值。要检查有效的 `ActorID` 值，请使用以下语法，其中 `scenario` 是 `drivingScenario` 变量名的名称。

  ```
  actorIDs = [scenario.Actors.ActorID]
  ```
- 当 **Source of ego vehicle** 设置为 `Input Port` 时，必须将此参数设置为该模块 **Ego Vehicle** 输入端口处的 `ActorID` 值。

#### 依赖关系

要启用此参数，请按以下顺序设置这些参数：

1. 将 **Source of driving scenario** 参数设置为 `From workspace`。
2. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。

### **Output ego vehicle pose** — 输出自车位姿 `off`（默认）| `on`

选择此参数可在 **Ego Vehicle Pose** 端口输出自车的位姿。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`，并将 **Source of ego vehicle** 参数设置为 `Scenario`。

### **Output ego vehicle state** — 输出自车状态 `off`（默认）| `on`

选择此参数可在 **Ego Vehicle State** 端口输出自车的状态。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`，并将 **Source of ego vehicle** 参数设置为 `Scenario`。

要输出自车状态，你必须使用驾驶场景 API 中的 `smoothTrajectory` 函数创建自车轨迹，或在 Driving Scenario Designer 应用中选择 **Use smooth, jerk-limited trajectory** 参数。

### **Ego vehicle follows ground** — 使自车朝向跟随路面 `off`（默认）| `on`

选择此参数可使自车朝向跟随路面的高程。该模块会更新自车的高程、横滚、俯仰和偏航，并相对于更新后的自车坐标输出参与者和车道边界。该模块不会更新自车的速度或角速度。

在路网高程变化的闭环仿真中使用此参数。

**Note**

在高程和倾斜角不同的道路交汇处，更新后的自车值可能不准确。

在开环仿真中，当 **Source of ego vehicle** 设置为 `Scenario` 时，自车会跟随驾驶场景中指定的高程。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 设置为 `Vehicle coordinates`，并将 **Source of ego vehicle** 设置为 `Input port`。

### **Sample time (s)** — 仿真采样时间 `0.1`（默认）| 正实数标量

仿真采样时间，以秒为单位，指定为正实数标量。不支持继承采样时间和连续采样时间。此采样时间与 Driving Scenario Designer 应用和 `drivingScenario` 对象在仿真期间使用的采样时间分开。

#### Lanes

### **Lane boundaries to output** — 要输出的车道边界 `None`（默认）| `Ego vehicle lane boundaries` | `All lane boundaries`

要输出的车道边界，指定为以下选项之一：

- `None` — 不输出任何车道边界。
- `Ego vehicle lane boundaries` — 输出自车的左侧和右侧车道边界。
- `All lane boundaries` — 输出自车所行驶道路的所有车道边界。

如果选择 `Ego vehicle lane boundaries` 或 `All lane boundaries`，则该模块会在 **Lane Boundaries** 输出端口中返回车道边界。

#### 依赖关系

要启用此参数，请将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。

### **Distances from ego vehicle for computing boundaries (m)** — 用于计算边界的距自车距离 `linspace(-150,150,101)`（默认）| *N* 元素实值向量

用于计算车道边界的距自车距离，指定为 *N* 元素实值向量。*N* 是距离值的数量。当从后视摄像头检测车道时，指定负距离。当前视摄像头检测车道时，指定正距离。单位为米。

默认情况下，该模块计算从自车后方 150 米到自车前方 150 米范围内的 101 个车道边界。这些距离以 3 米为间隔线性分布。

**Example:** `1:0.1:10` 在自车前方 1 到 10 米范围内每 0.1 米计算一个车道边界。

#### 依赖关系

要启用此参数，请将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。

### **Location of boundaries on lane markings** — 车道边界位置 `Center of lane markings`（默认）| `Inner edge of lane markings`

车道边界在车道标线上的位置，指定为此表中的一个选项。

| Lane Boundary Location | Description | Example |
| --- | --- | --- |
| `Center of lane markings` | 车道边界以车道标线为中心。 | 一条三车道道路有四条车道边界：每条车道标线一条。 具有四条车道边界的三车道道路 |
| `Inner edge of lane markings` | 车道边界放置在车道标线的内侧边缘。 | 一条三车道道路有六条车道边界：每条车道两条。 具有六条车道边界的三车道道路 |

#### 依赖关系

要启用此参数，请将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。

#### Port Settings

### **Source of actors bus name** — 参与者位姿总线名称的来源 `Auto`（默认）| `Property`

**Actors** 输出端口中返回的参与者位姿总线名称的来源，指定为以下选项之一：

- `Auto` — 该模块自动创建参与者位姿总线名称。
- `Property` — 使用 **Actors bus name** 参数指定参与者位姿总线名称。

### **Actors bus name** — 参与者位姿总线名称 有效总线名称

**Actors** 输出端口中返回的参与者位姿总线名称，指定为有效总线名称。

#### 依赖关系

要启用此参数，请将 **Source of actors bus name** 设置为 `Property`。

### **Source of maximum number of actors** — 最大参与者数量的来源 `Scenario`（默认）| `Property`

驾驶场景中可具有的最大参与者数量的来源，指定为以下选项之一：

- `Scenario` — 该模块将最大参与者数量设置为驾驶场景中的参与者数量。此值等于 **Actors** 输出端口返回的总线的 `NumActors` 字段。当你更改输入场景时，最大参与者数量会更新以匹配新的 `NumActors` 值。
- `Property` — 使用 **Maximum number of actors** 参数指定最大参与者数量。当你希望在参与者数量变化的场景之间复用同一参与者总线时，例如从引用模型输出参与者时，请选择此选项。

### **Maximum number of actors** — 最大参与者数量 `100`（默认）| 正整数

场景中可具有的最大参与者数量，指定为正整数。

#### 依赖关系

要启用此参数，请将 **Source of maximum number of actors** 参数设置为 `Property`。

### **Source of lane boundaries bus name** — 车道边界总线名称的来源 `Auto`（默认）| `Property`

**Lane Boundaries** 输出端口中返回的车道边界总线名称的来源，指定为以下选项之一：

- `Auto` — 该模块自动创建车道边界总线名称。
- `Property` — 使用 **Lane boundaries bus name** 参数指定车道边界总线名称。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。

### **Lane boundaries bus name** — 车道边界总线名称 有效总线名称

**Lane Boundaries** 输出端口中返回的车道边界总线名称，指定为有效总线名称。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `Ego vehicle lane boundaries` 或 `All lane boundaries`。
3. 将 **Source of lane boundaries bus name** 参数设置为 `Property`。

### **Source of maximum number of lane boundaries** — 最大车道边界数量的来源 `Scenario`（默认）| `Property`

驾驶场景中可具有的最大车道边界数量的来源，指定为以下选项之一：

- `Scenario` — 该模块将最大车道边界数量设置为驾驶场景中的车道边界数量。此值等于 **Lane Boundaries** 输出端口返回的总线的 `NumLaneBoundaries` 字段。当你更改输入场景时，最大车道边界数量会更新以匹配新的 `NumLaneBoundaries` 值。
- `Property` — 使用 **Maximum number of lane boundaries** 参数指定最大车道边界数量。当你希望在车道边界数量变化的场景之间复用同一车道边界总线时，例如从引用模型输出车道边界时，请选择此选项。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `All lane boundaries`。

### **Maximum number of lane boundaries** — 最大车道边界数量 `10`（默认）| 正整数

场景中可具有的最大车道边界数量，指定为正整数。

#### 依赖关系

要启用此参数：

1. 将 **Coordinate system of actors output** 参数设置为 `Vehicle coordinates`。
2. 将 **Lane boundaries to output** 参数设置为 `All lane boundaries`。
3. 将 **Source of maximum number of lane boundaries** 参数设置为 `Property`。

### **Source of ego vehicle pose bus name** — 自车位姿总线名称的来源 `Auto`（默认）| `Property`

**Ego Vehicle Pose** 输出端口中返回的自车位姿总线名称的来源，指定为以下选项之一：

- `Auto` — 该模块自动创建自车位姿总线名称。
- `Property` — 使用 **Ego vehicle pose bus name** 参数指定自车位姿总线名称。

#### 依赖关系

要启用此参数，请选择 **Output ego vehicle pose** 参数。

### **Ego vehicle pose bus name** — 自车位姿总线名称 有效总线名称

**Ego Vehicle Pose** 输出端口中返回的自车位姿总线名称，指定为有效总线名称。

#### 依赖关系

要启用此参数，请选择 **Output ego vehicle pose** 参数，并将 **Source of ego vehicle pose bus name** 参数设置为 `Property`。

### **Source of ego vehicle state bus name** — 自车状态总线名称的来源 `Auto`（默认）| `Property`

**Ego Vehicle State** 输出端口中返回的自车状态总线名称的来源，指定为以下选项之一：

- `Auto` — 该模块自动创建自车状态总线名称。
- `Property` — 使用 **Ego vehicle state bus name** 参数指定自车状态总线名称。

#### 依赖关系

要启用此参数，请选择 **Output ego vehicle state** 参数。

### **Ego vehicle state bus name** — 自车状态总线名称 有效总线名称

**Ego Vehicle State** 输出端口中返回的自车状态总线名称，指定为有效总线名称。

#### 依赖关系

要启用此参数，请选择 **Output ego vehicle state** 参数，并将 **Source of ego vehicle state bus name** 参数设置为 `Property`。

### **Show coordinate labels** — 显示输入和输出的坐标系 `on`（默认）| `off`

选择此参数可在模块图中显示 Scenario Reader 模块上模块输入和输出的坐标系。

- **Ego Vehicle** 输入和输出始终位于世界坐标系中。
- **Lane Boundaries** 输出始终位于车辆坐标系中。
- 你可以根据 **Coordinate system of actors output** 参数的选择，以车辆坐标系或世界坐标系返回 **Actors** 输出。

#### 仿真

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，你可以调试该模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不更改，C 代码就会在后续仿真中复用。此选项需要额外的启动时间。
## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 当模型处于快速加速模式时，Scenario Reader 模块不会根据仿真之间对驾驶场景所做的更改自动重新生成代码。要重新生成这些更改，请手动删除上次仿真生成的 Simulink 项目文件夹 `slprj`。然后，重新运行仿真。或者，更改模式或通过将 **Simulate using** 参数设置为 `Interpreted execution` 来禁用代码生成。
- **Driving Scenario Designer file name** 和 **MATLAB or model workspace variable name** 参数是字符向量。代码生成中字符编码 (Simulink) 中描述的限制适用于这些参数。

## 版本历史

**在 R2019a 中引入**

## 描述

将驾驶场景读入模型

Scenario Reader 模块从使用 Driving Scenario Designer 应用创建的场景文件或从 `drivingScenario` 对象中读取道路和参与者。该模块输出参与者在自车坐标系或场景世界坐标系中的位姿。您还可以输出车道边界，或输出自车位姿以用于 3D 仿真环境。该模块还允许输出自车状态，其中包括加速度测量值，以供传感器模型使用。

要从输出的参与者位姿和车道边界生成目标和车道边界检测，请将位姿和边界输出传递给传感器模块。使用这些传感器生成的合成检测来测试传感器融合算法、跟踪算法和其他自动驾驶辅助系统 (ADAS) 算法的性能。要可视化这些算法的性能，请使用 Bird's-Eye Scope。

您可以从场景中读取自车，或将模型中定义的自车指定为 Scenario Reader 模块的输入。使用此选项可以测试闭环车辆控制器算法，例如自动紧急制动 (AEB)、车道保持辅助 (LKA) 或自适应巡航控制 (ACC)。
