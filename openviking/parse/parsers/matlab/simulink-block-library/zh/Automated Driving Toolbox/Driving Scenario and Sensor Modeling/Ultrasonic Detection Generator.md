---
type: simulink-block
title: 'Ultrasonic Detection Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'ultrasonicdetectiongenerator'
documentation_source_path: 'ref/ultrasonicdetectiongenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Ultrasonic Detection Generator

## 端口

### 输入

### **Actors** — 场景参与者位姿 Simulink bus，包含 MATLAB® structure

自车坐标中的场景参与者位姿，指定为包含 MATLAB structure 的 Simulink bus。

该 structure 必须包含以下字段。

| Field | Description | Type |
| --- | --- | --- |
| `NumActors` | 参与者数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `Actors` | 参与者位姿 | `NumActors` 长度的参与者位姿 structure 数组 |

`Actors` 中的每个参与者位姿 structure 必须包含以下字段。

| Field | Description |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位是米。 **注意** 如果驾驶场景不包含至少一个车辆的前轴轨迹，则 `ActorPoses` structure 不包含此字段。 |
| `Position` | 参与者位置，指定为形式为 [*x* *y* *z*] 的实值向量。单位是米。 |
| `Velocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的实值向量。单位是米每秒。 |
| `Roll` | 参与者横滚角，指定为实值标量。单位是度。 |
| `Pitch` | 参与者俯仰角，指定为实值标量。单位是度。 |
| `Yaw` | 参与者偏航角，指定为实值标量。单位是度。 |
| `AngularVelocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的实值向量。单位是度每秒。 |

### 输出

### **Detections** — 目标检测结果 Simulink bus，包含 MATLAB structure

目标检测结果，返回为包含 MATLAB structure 的 Simulink bus。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

您可以将来自这些传感器和其他传感器的目标检测结果传递给跟踪器，例如 Multi-Object Tracker 模块，并生成航迹。

该 structure 必须包含以下字段。

| Property | Description |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 到最近目标的距离测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性 Kalman 跟踪滤波器的初始化函数使用的参数 |

下表描述 `ObjectAttributes` 属性中的附加信息。

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | 生成该检测结果的参与者标识符 `ActorID`。对于误报，此值为负数。 |
| `PointOnTarget` | 检测目标上用于传感器计算距离测量的点的坐标。它在车辆坐标系中。使用此坐标可在 Bird's-Eye Scope 应用中可视化检测结果。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。父坐标系是自车车身。

**`MeasurementParameters`**

| Parameter | Definition |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量值的坐标系。`Frame` 始终设置为 `'spherical'`，并且对于 Ultrasonic Detection Generator，检测结果以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的 3-D 向量偏移。 |
| `OriginVelocity` | 传感器坐标系相对于父坐标系的速度。 |
| `IsParentToChild` | 逻辑标量，指示 `Orientation` 是否执行从父坐标系到子坐标系的坐标系旋转。当 `IsParentToChild` 为 false 时，`Orientation` 执行从子坐标系到父坐标系的坐标系旋转。 |
| `HasAzimuth` | 指示测量值是否包含方位角分量。 |
| `HasRange` | 指示测量值是否包含距离分量。对于 Ultrasonic Detection Generator 始终为 `true`。 |
| `HasElevation` | 指示测量值是否包含俯仰角分量。对于 Ultrasonic Detection Generator 始终为 `false`。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。对于 Ultrasonic Detection Generator 始终为 `false`。 |
| `FieldOfView` | 包含传感器方位角和俯仰角视场值的 2-D 向量。 |

## 参数

### 参数

#### 传感器标识

### **传感器的唯一标识符** — 唯一传感器标识符 `0`（默认）| 正整数

将唯一传感器标识符指定为正整数。使用此参数区分多传感器系统中来自不同传感器的检测结果或航迹。为每个传感器指定唯一值。如果不将 **传感器的唯一标识符** 从默认值 `0` 更新，则雷达会在仿真开始时返回错误。

#### 传感器安装

### **相对于自车原点的平移 [ X, Y, Z ] (m)** — 传感器在自车上的位置 (m) `[3.4, 0, 0.2]`（默认）| 形式为 [*x* *y* *z*] 的 1-by-3 实值向量

将传感器在自车车身坐标系中的位置指定为以米为单位的 1-by-3 实值向量，形式为 [*x* *y* *z*]。此参数定义传感器相对于自车原点沿 *x*-轴、*y*-轴和 *z*-轴的坐标，其中：

- *x*-轴从车辆向前指向。
- *y*-轴指向车辆左侧。
- *z*-轴从地面向上指向。

默认值对应于安装在轿车前格栅中心的雷达。

有关自车坐标系的更多详细信息，请参阅 Coordinate Systems in Automated Driving Toolbox。

### **相对于自车坐标系的旋转 [Yaw, Pitch, Roll] (deg)** — 雷达的安装旋转角 `[0 0 0]`（默认）| 形式为 [*z*yaw *y*pitch *x*roll] 的 1-by-3 实值向量

将雷达的安装旋转角指定为以度为单位的 1-by-3 实值向量，形式为 [*z*yaw *y*pitch *x*roll]。此参数定义传感器相对于自车车身坐标系绕 *z*-轴、*y*-轴和 *x*-轴的内旋 Euler 角旋转，其中：

- *z*yaw，即 *yaw angle*，使传感器绕自车的 *z*-轴旋转。
- *y*pitch，即 *pitch angle*，使传感器绕自车的 *y*-轴旋转。此旋转相对于由 *z*yaw 旋转产生的传感器位置。
- *x*roll，即 *roll angle*，使传感器绕自车的 *x*-轴旋转。此旋转相对于由 *z*yaw 和 *y*pitch 旋转产生的传感器位置。

当分别沿 *z*-轴、*y*-轴和 *x*-轴的正方向观察时，这些角度为顺时针正。如果从鸟瞰图视角可视化传感器数据，则偏航角为逆时针正，因为您沿 *z*-轴（从地面向上指向）的负方向查看数据。

有关此坐标系的更多详细信息，请参阅 Coordinate Systems in Automated Driving Toolbox。

#### 传感器配置

### **视场 [horizontalFOV, verticalFOV] (deg)** — 超声传感器的角视场 `[70 35]`（默认）| 形式为 `[horizontalFOV verticalFOV]` 的 1-by-2 正实值向量

超声传感器的角视场，指定为形式为 `[horizontalFOV verticalFOV]` 的 1-by-2 正实值向量。视场定义传感器跨越的总角度范围。必须将水平视场 `horizontalFOV` 指定在范围 (0, 360] 内，并将俯仰角视场 `verticalFOV` 指定在范围 (0, 180] 内。垂直视场范围较窄，以避免来自地面的检测。单位为度。

### **检测范围 [minDetOnlyRange, minDistRange, maxDistRange] (m)** — 超声传感器的检测范围向量 (m) `[0.03 0.15 5.5]`（默认）| 形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1-by-3 非负实值向量

超声传感器的检测范围向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1-by-3 非负实值向量，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为米。这些值确定超声传感器返回的检测结果和距离值。

- 当检测目标位于 `minDistRange` 与 `maxDistRange` 之间的距离时，传感器返回正距离值。
- 当检测目标位于 `minDetOnlyRange` 与 `minDistRange` 之间的距离时，传感器检测到目标，但无法确定距离并返回值 `0`。
- 当目标距离低于 `minDetOnlyRange` 或高于 `maxDistRange` 时，传感器返回空 cell array。

### **更新率 (Hz)** — 传感器更新率 `10`（默认）| 正实值标量

将传感器更新率指定为以赫兹为单位的正实值标量。更新率的倒数必须是仿真时间间隔的整数倍。雷达按由此倒数定义的时间间隔生成新报告。在更新间隔之间请求的任何传感器更新都不包含检测结果或航迹。

#### 端口设置

### **输出总线名称的来源** — 输出总线名称的来源 `Auto`（默认）| `Property`

输出总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建总线名称。
- `Property` — 使用 **指定输出总线名称** 参数指定总线名称。

### **指定输出总线名称** — 输出总线名称 `BusDrivingRadarDataGenerator`（默认）| 有效总线名称

指定在 **Actors** 输出端口中返回的参与者位姿总线的名称。

要启用此参数，请将 **输出总线名称的来源** 参数设置为 `Property`。

### 参与者配置文件

### **目标配置文件定义** — 指定目标配置文件的方法 `Parameters`（默认）| `MATLAB expression` | `From Scenario Reader block`

指定目标配置文件的方法，目标配置文件是驾驶场景中所有目标的物理特性和雷达特性，指定为以下选项之一：

- `Parameters` — 选择此选项时，模块从 **Target Profiles** 选项卡上启用的参数获取目标配置文件。
- `MATLAB expression` — 模块从 **目标配置文件的 MATLAB 表达式** 参数指定的 MATLAB 表达式获取参与者配置文件。
- `From Scenario Reader block` — 模块从 Scenario Reader 模块或 RoadRunner Scenario Reader 模块指定的场景获取参与者配置文件。

### **目标配置文件的 MATLAB 表达式** — 目标配置文件的 MATLAB 表达式 MATLAB structure | MATLAB structure array | 有效 MATLAB 表达式

将参与者配置文件的 MATLAB 表达式指定为 MATLAB structure、MATLAB structure array 或生成此类 structure 或 structure array 的有效 MATLAB 表达式。

如果您的 Scenario Reader 模块从 `drivingScenario` 对象读取数据，要直接从该对象获取参与者配置文件，请将此表达式设置为对该对象调用 `actorProfiles` 函数。例如：`actorProfiles(scenario)`。

默认目标配置文件表达式生成一个 MATLAB structure，其形式如下：

    struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4, ...
    'OriginOffset',[-1.35 0 0],'RCSPattern',[10 10;10 10], ...
    'RCSAzimuthAngles',[-180 180],'RCSElevationAngles',[-90 90])

#### 依赖关系

要启用此参数，请将 **目标配置文件定义** 参数设置为 `MATLAB expression`。

### **参与者的唯一标识符** — 场景定义的参与者标识符 `[]`（默认）| 正整数 | 长度为 *L* 的唯一正整数向量

将场景定义的参与者标识符指定为正整数或长度为 *L* 的唯一正整数向量。*L* 必须等于输入到 **Actors** 输入端口的参与者数量。向量元素必须与参与者的 `ActorID` 值匹配。您可以将 **参与者的唯一标识符** 指定为 `[]`。在这种情况下，相同的参与者配置文件参数应用于所有参与者。

**示例：** `[1 2]`

#### 依赖关系

要启用此参数，请将 **目标配置文件定义** 参数设置为 `Parameters`。

### **用于对参与者分类的用户定义整数** — 用户定义分类标识符 `0`（默认）| 整数 | 长度为 *L* 的整数向量

将用户定义分类标识符指定为整数或长度为 *L* 的整数向量。当 **参与者的唯一标识符** 是向量时，此参数是相同长度的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为单个整数，其值应用于所有参与者。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **目标配置文件定义** 参数设置为 `Parameters`。

### **参与者长方体的长度 (m)** — 参与者长方体的长度 `4.7`（默认）| 正实值标量 | 长度为 *L* 的正值向量

将参与者长方体的长度指定为正实值标量或长度为 *L* 的正值向量。当 **参与者的唯一标识符** 是向量时，此参数是相同长度的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为正实值标量，其值应用于所有参与者。单位为米。

**示例：** `6.3`

#### 依赖关系

要启用此参数，请将 **目标配置文件定义** 参数设置为 `Parameters`。

### **参与者长方体的宽度 (m)** — 参与者长方体的宽度 `1.8`（默认）| 正实值标量 | 长度为 *L* 的正值向量

将参与者长方体的宽度指定为正实值标量或长度为 *L* 的正值向量。当 **参与者的唯一标识符** 是向量时，此参数是相同长度的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为正实值标量，其值应用于所有参与者。单位为米。

**示例：** `4.7`

#### 依赖关系

要启用此参数，请将 **目标配置文件定义** 参数设置为 `Parameters`。

### **参与者长方体的高度 (m)** — 参与者长方体的高度 `1.4`（默认）| 正实值标量 | 长度为 *L* 的正值向量

将参与者长方体的高度指定为正实值标量或长度为 *L* 的正值向量。当 **参与者的唯一标识符** 是向量时，此参数是相同长度的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为正实值标量，其值应用于所有参与者。单位为米。

**示例：** `2.0`

#### 依赖关系

要启用此参数，请将 **目标配置文件定义** 参数设置为 `Parameters`。

### **参与者从底部中心起的旋转中心 (m)** — 参与者的旋转中心 `{[-1.35, 0, 0]}`（默认）| 长度为 *L* 的实值 1-by-3 向量 cell array

将参与者的旋转中心指定为长度为 *L* 的实值 1-by-3 向量 cell array。每个向量表示参与者旋转中心相对于参与者底部中心的偏移。对于车辆，该偏移对应后轴中心下方地面上的点。当 **参与者的唯一标识符** 是向量时，此参数是向量 cell array，其 cell 与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为包含一个元素的 cell array，其中包含应用于所有参与者的偏移向量。单位为米。

**示例：** `{[-1.35, 0.2, 0.3]}`

#### 依赖关系

要启用此参数，请将 **目标配置文件定义** 参数设置为 `Parameters`。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从驾驶场景或 RoadRunner Scenario 生成超声传感器检测结果

Ultrasonic Detection Generator 模块从安装在自车上的超声传感器生成目标检测。使用此模块可从包含参与者和轨迹的驾驶场景生成传感器数据，您可以从 Scenario Reader 模块读取该场景。

在等于传感器更新间隔的时间间隔处，模块输出从传感器到检测目标最近点的距离。此模块还提供参数，用于指定场景中对象的尺寸和属性。为了使用 Bird's-Eye Scope 应用可视化超声检测，此模块还输出检测对象上最近点的 3-D 坐标。

您可以在 Driving Scenario 和 RoadRunner Scenario 仿真中将此模块与车辆参与者一起使用。

您可以使用 Ultrasonic Detection Generator 为 Multi-Object Tracker 模块创建输入。使用 Driving Scenario Designer 应用构建场景和传感器模型时，导出到 Simulink® 的超声传感器输出为 Ultrasonic Detection Generator 模块。
