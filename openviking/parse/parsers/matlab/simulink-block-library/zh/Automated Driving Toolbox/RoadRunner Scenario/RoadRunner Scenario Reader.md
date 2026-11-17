---
type: simulink-block
title: 'RoadRunner Scenario Reader'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'RoadRunner Scenario'
documentation_page: 'roadrunnerscenarioreader'
documentation_source_path: 'ref/roadrunnerscenarioreader.html'
language: zh-CN
chinese_source: worker-translation
---

# RoadRunner Scenario Reader

## 端口

### 输入

### **Port\_1** — 参与者 ID 标量

指定需要其父级或子级信息的参与者的 ID。

要将 ID 转换为 `uint64` 数据类型，您可以将 Constant (Simulink) 模块的 **Constant value** 参数设置为 `uint64(ID)`，其中 `ID` 是参与者 ID，或者使用 Data Type Conversion (Simulink) 模块。

#### 依赖关系

要启用此端口，请将 **Filter** 参数设置为 `Actor ID (provided by input)`。

**数据类型：** `uint64`
### 输出

### **Message** — 来自场景的状态信息 Simulink 消息

来自场景的状态信息，以 Simulink 消息形式返回。要从 Simulink 消息中提取数据，请将 RoadRunner Scenario Reader 模块连接到 Receive (Simulink) 模块。

## 参数

### **Topic Category** — 主题类别 `Actor`（默认）| `Action` | `Sensor` | `Event`

主题类别，指定为以下值之一：

- `Actor` — 从场景中读取参与者数据
- `Action` — 从场景中读取动作数据
- `Sensor` — 从场景中读取传感器数据
- `Event` — 从场景中读取事件数据

### **Actor Type** — 场景中的参与者类型 `All Types`（默认）| `Vehicle` | `Traffic Signal` | `Traffic Signal Controller`

场景中的参与者类型，指定为 `All Types`、`Vehicle`、`Traffic Signal` 或 `Traffic Signal Controller`。`Vehicle` 类型包含参与者的额外车轮信息。

`Traffic Signal` 类型表示交通信号参与者，而 `Traffic Signal Controller` 类型表示将交叉口的所有交通信号参与者连接在一起的交通信号控制器实体。

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Actor`。

### **Action Type** — 动作类型 `Path Following`（默认）| `Change Parameter` | `Lane Change` | `Lateral Offset` | `Longitudinal Distance` | `Speed Change` | `User Defined`

可从场景中读取的动作类型，指定为以下值之一：

| 字段名称 | 描述 |
| --- | --- |
| `Change Parameter` | 从场景中读取用户创建的参数。有关详细信息，请参阅 Change Parameter。 |
| `Lateral Offset` | 从场景中读取横向偏移动作数据。有关详细信息，请参阅 Lateral Offset。 |
| `Path Following` | 从场景中读取路径跟随动作数据。有关详细信息，请参阅 Path Following。 |
| `Speed Change` | 从场景中读取速度变化动作数据。有关详细信息，请参阅 Speed Change。 |
| `Lane Change` | 从场景中读取车道变换动作数据。有关详细信息，请参阅 Lane Change。 |
| `Longitudinal Distance` | 从场景中读取纵向距离动作数据。有关详细信息，请参阅 Longitudinal Distance。 |
| `User Defined` | 从场景中读取用户定义动作的自定义参数。有关详细信息，请参阅 User Defined。 |

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Action`。

### **Sensor View** — 从场景真值导出的传感器数据 `Target Poses`（默认）| `Target Poses For Host` | `Lane Boundaries` | `Target Poses And Lane Boundaries`

从场景真值导出的传感器数据，指定为以下选项之一：

- `Target Poses` — 模块输出传感器范围内目标在宿主车辆坐标系中的位姿。有关输出目标位姿的总线结构，请参阅 `targetPoses` 函数的输出参数描述。
- `Target Poses For Host` — 模块输出所有目标在宿主车辆坐标系中的位姿。有关输出目标位姿的总线结构，请参阅 `targetPoses` 函数的输出参数描述。
- `Lane Boundaries` — 模块输出传感器范围内车道边界在宿主车辆坐标系中的信息。有关输出车道边界的总线结构，请参阅 `laneBoundaries` 函数的输出参数描述。
- `Target Poses And Lane Boundaries` — 模块输出传感器范围内车道边界和目标在宿主车辆坐标系中的位姿。

宿主车辆坐标系的原点是宿主车辆的几何中心。

您可以将上述输出直接发送到传感器检测生成器模块并获取检测结果。

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Sensor`。

### **Event Type** — 事件类型 `User-Defined`

要从场景中读取的事件类型。

所读取的事件必须映射到 RoadRunner Scenario 模块中相应的总线对象。

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Event`。

### **Topic** — 参与者数据，或通过传感器视图捕获的车道边界数据 `Actor Specifications` | `Actor Pose` | `Actor Pose (Driving Scenario compatible)` | `Actor Lane Location` | `Vehicle Specifications` | ...

参与者数据，或通过传感器视图捕获的车道边界。

**Topic** 参数可以包含各种选项集，如下表所示，具体取决于其他字段的配置。

如果以下两个字段配置均为真，则 **Topic** 参数包含下表所述的选项：

- **Topic Category** 设置为 `Actor`。
- **Actor Type** 设置为 `All Types`。

| 选项 | 描述 |
| --- | --- |
| `Actor Specifications`（默认） | 与参与者关联的静态属性，例如参与者 ID、参与者名称和边界框。有关详细信息，请参阅 Actor Specifications。 |
| `Actor Pose` | 与参与者关联的动态数据，例如位姿、速度和角速度。对于 RoadRunner 中包含或创建的车辆资产，参与者原点是参与者的几何中心。有关详细信息，请参阅 Actor Pose。 |
| `Actor Pose (Driving Scenario compatible)` | 与参与者关联的动态数据，例如参与者 ID、位置、速度、横滚角、俯仰角、偏航角和角速度。对于 RoadRunner 中包含或创建的车辆资产，参与者原点是其后轴中心下方地面上的点。有关详细信息，请参阅 Actor Pose (Driving Scenario compatible)。 |
| `Actor Lane Location` | 与参与者车道位置关联的动态数据。有关详细信息，请参阅 Actor Lane Location。 |

如果以下两个字段配置均为真，则 **Topic** 参数包含下表所述的选项：

- **Topic Category** 设置为 `Actor`。
- **Actor Type** 设置为 `Vehicle`。

| 选项 | 描述 |
| --- | --- |
| `Vehicle Specifications`（默认） | 与车辆关联的静态属性，例如油漆颜色和车轮规格。有关详细信息，请参阅 Vehicle Specifications。 |
| `Vehicle Pose` | 与参与者关联的动态数据，例如车轮位姿。有关详细信息，请参阅 Vehicle Pose。 |

如果以下两个字段配置均为真，则 **Topic** 参数包含下表所述的选项：

- **Topic Category** 设置为 `Actor`。
- **Actor Type** 设置为 `Traffic Signal`。

| 选项 | 描述 |
| --- | --- |
| `Traffic Signal Specifications`（默认） | 交通信号参与者的静态规格。有关详细信息，请参阅 Traffic Signal Specifications Topic。 |
| `Traffic Signal Runtime` | 交通信号参与者的运行时信息。有关详细信息，请参阅 Traffic Signal Runtime Topic。 |

如果以下两个字段配置均为真，则 **Topic** 参数包含下表所述的选项：

- **Topic Category** 设置为 `Actor`。
- **Actor Type** 设置为 `Traffic Signal Controller`。

| 选项 | 描述 |
| --- | --- |
| `Traffic Signal Controller Specifications`（默认） | 交通信号控制器的静态规格。有关详细信息，请参阅 Traffic Signal Controller Specifications Topic。 |
| `Traffic Signal Controller Runtime` | 交通信号控制器的运行时信息。有关详细信息，请参阅 Traffic Signal Controller Runtime Topic。 |

如果以下两个字段配置均为真，则 **Topic** 参数包含下表所述的选项：

- **Topic Category** 设置为 `Sensor`。
- **Sensor View** 设置为 `Lane Boundaries`。

| 选项 | 描述 |
| --- | --- |
| `Ego-Lane`（默认） | 宿主车辆参与者所行驶车道的边界 |
| `Ego and Adjacent Lanes` | 相邻左车道和右车道的边界，以及宿主车辆参与者所行驶车道的边界 |
| `All Lanes` | 道路上所有车道的边界 |

### **Filter** — 筛选条件 `Self`（默认）| `None` | `Actor ID (provided by input)`

相关主题数据的筛选条件，指定为以下选项之一：

| 选项 | 描述 |
| --- | --- |
| `None` | 输出场景中所有参与者的数据。当您将 **Filter** 设置为 `None` 时，模块会为仿真中的每个参与者输出一条消息。消息携带数据，包括参与者 ID。您可以将消息存储在 Queue (Simulink) 模块中。然后，您可以使用例如 MATLAB System 模块来处理这些消息。有关详细信息，请参阅 Process Message Payload Using MATLAB System Block (Simulink)。当 Filter 选择为 None 时，RoadRunner Scenario Reader 模块输出关联参与者的消息。Queue 模块存储消息，MATLAB Function 模块处理消息。 |
| `Self` | 输出与 Simulink 模型行为关联的参与者的数据。 |
| `Actor ID (provided by input)` | 输出特定参与者的数据。选择此选项会暴露输入端口 **Port\_1**，您可以通过该端口提供参与者 ID。例如，您可以将 Constant 模块连接到 **Port\_1**，以提供表示场景中参与者 ID 的固定值。 |

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Actor` 或 `Action`。

### **Additional Relationship** — 与筛选实体的关系 `None`（默认）| `Parent` | `Children`

与筛选实体的关系，指定为以下选项之一：

- `None` — 不选择。RoadRunner Scenario reader 模块输出与根据 **Filter** 参数筛选的实体关联的数据。
- `Parent` — 筛选实体的父参与者。RoadRunner Scenario reader 模块输出与根据 **Filter** 参数筛选的实体的父级关联的数据。
- `Children` — 筛选实体的子参与者。RoadRunner Scenario reader 模块输出与根据 **Filter** 参数筛选的实体的子级关联的数据。

例如，选择 `Actor ID (provided by input)` 作为筛选条件以暴露输入端口 **Port\_1**。将一个输出值为 `uint64(2)` 的 Constant 模块连接到该输入端口。如果您从 **Additional Relationship** 字段中选择 `Parent`，则 RoadRunner Scenario Reader 模块输出与 ID 为 `2` 的参与者的父级关联的数据。

**注意**

您还可以使用 **Additional Relationship** 参数来输出有关父参与者或子参与者动作的信息。

#### 依赖关系

要启用此参数，请将 **Filter** 设置为 `Actor ID (provided by input)` 或 `Self`。

### **Sensor ID** — 传感器的唯一索引 `1`（默认）| 正整数

传感器的唯一索引，指定为正整数。`Sensor ID` 必须与相应传感器模型检测生成器模块的 **Unique identifier of sensor** 参数相对应。

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Sensor`，并将 **Sensor View** 设置为 `Target Poses`、`Lane Boundaries` 或 `Target Poses And Lane Boundaries`。

### **Sample Time** — 仿真的采样时间 正实数标量

仿真的采样时间，以秒为单位，指定为正实数标量。

### **Event Name** — 事件名称 字符串

要从场景中读取的用户定义事件的名称。

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Event`，并将 **Event Type** 设置为 `User-Defined`。

## 所属库

Automated Driving Toolbox / RoadRunner Scenario

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

### R2025a：获取交通信号和交通信号控制器信息

通过将 **Topic Category** 参数设置为 `Actor`，并将 **Actor Type** 设置为 `Traffic Signal` 或 `Traffic Signal Controller`，获取交通信号和交通信号控制器信息。

然后，您可以通过更改 **Topic** 参数来输出指定交通信号或交通信号控制器的静态或运行时规格。

### R2025a：获取与父参与者或子参与者关联的参与者或动作信息

通过将 **Topic Category** 参数设置为 `Actor` 或 `Action`，并将 **Filter** 设置为 `Actor ID (provided by input)`，获取与特定参与者的父参与者或子参与者关联的参与者或动作信息。设置这些参数值会暴露输入端口 **Port\_1**。根据您的需求，将 **Additional Relationship** 参数设置为 `Parent` 或 `Children`。

### R2023a：适用于所有参与者的 `LaneLocation` 主题

从 R2023a 开始，当您使用 RoadRunner Scenario Reader 模块访问 `Vehicle Pose` 时，不再支持 `MapLocation` 及其总线定义 `BusVehicleMaplocation`。要读取参与者位置，请使用新的专用主题 `Actor Lane Location`。此更改允许您访问 RoadRunner Scenario 仿真中任何参与者关联的位置数据。

## 描述

从 RoadRunner 场景中读取所选主题

RoadRunner Scenario Reader 模块从 `RoadRunner` 场景中读取所选主题。您可以将 **Topic Category** 参数设置为 `Actor`、`Action`、`Sensor` 或 `Event`。模块以消息形式输出数据。

当您选择 `Actor` 主题时，模块输出与参与者关联的数据，例如 `Actor Specifications` 和 `Actor Pose`。当您选择 `Action` 主题时，模块输出诸如 `Speed Change` 和 `Lane Change` 之类的数据。模块返回上一时间步的仿真状态。您可以根据与 Simulink® 参与者模型关联的参与者来筛选数据。

当您选择 `Sensor` 主题时，模块输出与指定 `Sensor ID` 的传感器关联的数据。您可以通过指定 `Target Poses` 或 `Lane Boundaries` 来选择模块必须输出的传感器数据类型。当您选择 `Event` 主题时，模块输出为 **Event name** 参数指定的用户定义事件的数据。
