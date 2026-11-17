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
| *在 R2024b 中：* `FrontAxlePosition` | 车辆的前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构不包含此字段。 |
| `Position` | 参与者的位置，指定为形式为 [*x* *y* *z*] 的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的实值向量。单位为米每秒。 |
| `Roll` | 参与者的横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者的俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者的偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的实值向量。单位为度每秒。 |
### 输出

### **Detections** — 目标检测 包含 MATLAB 结构的 Simulink 总线

目标检测，返回为包含 MATLAB 结构的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器（例如 Multi-Object Tracker 模块），并生成航迹。

该结构必须包含以下字段。

| 属性 | 描述 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 到最近目标的距离测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数使用的参数 |

下表描述了 `ObjectAttributes` 属性中的附加信息。

**`ObjectAttributes`**

| 属性 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的参与者的标识符 `ActorID`。对于虚警，此值为负数。 |
| `PointOnTarget` | 传感器用于计算距离测量的被检测目标上的点的坐标。它位于车辆坐标系中。使用此值可在 Bird's-Eye Scope 应用中可视化检测。 |

对于 `MeasurementParameters`，测量值相对于父坐标系。父坐标系为自车车身。

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 指示用于报告测量值的坐标系的枚举类型。`Frame` 始终设置为 `'spherical'`，对于 Ultrasonic Detection Generator，检测以球坐标报告。 |
| `OriginPosition` | 传感器原点相对于父坐标系原点的三维向量偏移。 |
| `OriginVelocity` | 传感器坐标系相对于父坐标系的速度。 |
| `IsParentToChild` | 逻辑标量，指示 `Orientation` 是否执行从父坐标系到子坐标系的坐标系旋转。当 `IsParentToChild` 为 false 时，`Orientation` 执行从子坐标系到父坐标系的坐标系旋转。 |
| `HasAzimuth` | 指示测量值是否包含方位角分量。 |
| `HasRange` | 指示测量值是否包含距离分量。对于 Ultrasonic Detection Generator 始终为 `true`。 |
| `HasElevation` | 指示测量值是否包含俯仰角分量。对于 Ultrasonic Detection Generator 始终为 `false`。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。对于 Ultrasonic Detection Generator 始终为 `false`。 |
| `FieldOfView` | 包含传感器方位角和俯仰角视场值的二维向量。 |

## 参数

### 参数

#### 传感器标识

### **Unique identifier of sensor** — 传感器唯一标识符 `0`（默认）| 正整数

将传感器唯一标识符指定为正整数。使用此参数可区分多传感器系统中来自不同传感器的检测或航迹。为每个传感器指定唯一值。如果您未将 **Unique identifier of sensor** 从默认值 `0` 更新，则雷达将在仿真开始时返回错误。

#### 传感器安装

### **Translation [ X, Y, Z ] relative to ego origin (m)** — 传感器在自车上的位置 (m) `[3.4, 0, 0.2]`（默认）| 形式为 [*x* *y* *z*] 的 1×3 实值向量

将自车车身坐标系中的传感器位置指定为形式为 [*x* *y* *z*] 的 1×3 实值向量，单位为米。此参数定义传感器相对于自车原点沿 *x* 轴、*y* 轴和 *z* 轴的坐标，其中：

- *x* 轴从车辆向前指向。
- *y* 轴指向车辆左侧。
- *z* 轴从地面向上指向。

默认值对应于安装在轿车前格栅中心的雷达。

有关自车坐标系的更多详细信息，请参阅 Coordinate Systems in Automated Driving Toolbox。

### **Rotation [Yaw, Pitch, Roll] relative to ego's frame (deg)** — 雷达的安装旋转角度 `[0 0 0]`（默认）| 形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量

将雷达的安装旋转角度指定为形式为 [*z*yaw *y*pitch *x*roll] 的 1×3 实值向量，单位为度。此参数定义传感器相对于自车车身坐标系绕 *z* 轴、*y* 轴和 *x* 轴的内旋欧拉角旋转，其中：

- *z*yaw，即 *偏航角*，使传感器绕自车的 *z* 轴旋转。
- *y*pitch，即 *俯仰角*，使传感器绕自车的 *y* 轴旋转。此旋转相对于由 *z*yaw 旋转产生的传感器位置。
- *x*roll，即 *横滚角*，使传感器绕自车的 *x* 轴旋转。此旋转相对于由 *z*yaw 和 *y*pitch 旋转产生的传感器位置。

当分别沿 *z* 轴、*y* 轴和 *x* 轴的正方向观察时，这些角度为顺时针正方向。如果您从鸟瞰视角可视化传感器数据，则偏航角为逆时针正方向，因为您沿 *z* 轴的负方向（从地面向上指向）查看数据。

有关此坐标系的更多详细信息，请参阅 Coordinate Systems in Automated Driving Toolbox。

#### 传感器配置

### **Field of view [horizontalFOV, verticalFOV] (deg)** — 超声波传感器的角度视场 `[70 35]`（默认）| 形式为 `[horizontalFOV verticalFOV]` 的 1×2 正实值向量

超声波传感器的角度视场，指定为形式为 `[horizontalFOV verticalFOV]` 的 1×2 正实值向量。视场定义传感器所跨越的总角度范围。您必须将水平视场 `horizontalFOV` 指定在 (0, 360] 范围内，将俯仰角视场 `verticalFOV` 指定在 (0, 180] 范围内。垂直视场范围较窄，以避免来自地面的检测。单位为度。

### **Detection ranges [minDetOnlyRange, minDistRange, maxDistRange] (m)** — 超声波传感器的检测距离向量 (m) `[0.03 0.15 5.5]`（默认）| 形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量

超声波传感器的检测距离向量，指定为形式为 `[minDetOnlyRange minDistRange maxDistRange]` 的 1×3 非负实值向量，其中 `minDetOnlyRange < minDistRange < maxDistRange`。单位为米。这些值决定超声波传感器返回的检测和距离值。

- 当被检测目标位于 `minDistRange` 和 `maxDistRange` 之间的距离时，传感器返回正距离值。
- 当被检测目标位于 `minDetOnlyRange` 和 `minDistRange` 之间的距离时，传感器检测到目标，但无法确定距离并返回值 `0`。
- 当目标位于 `minDetOnlyRange` 以下或 `maxDistRange` 以上的距离时，传感器返回空元胞数组。

### **Update rate (Hz)** — 传感器更新率 `10`（默认）| 正实标量

将传感器更新率指定为正实标量，单位为赫兹。更新率的倒数必须是仿真时间间隔的整数倍。雷达按此倒数定义的间隔生成新报告。在更新间隔之间请求的任何传感器更新不包含检测或航迹。

#### 端口设置

### **Source of output bus name** — 输出总线名称的来源 `Auto`（默认）| `Property`

输出总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建总线名称。
- `Property` — 使用 **Specify an output bus name** 参数指定总线名称。

### **Specify an output bus name** — 输出总线名称 `BusDrivingRadarDataGenerator`（默认）| 有效总线名称

指定在 **Actors** 输出端口中返回的参与者位姿总线的名称。

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

### 参与者配置文件

### **Target profiles definition** — 指定目标配置文件的方法 `Parameters`（默认）| `MATLAB expression` | `From Scenario Reader block`

将指定目标配置文件（即驾驶场景中所有目标的物理和雷达特性）的方法指定为以下选项之一：

- `Parameters` — 当您选择此选项时，模块从 **Target Profiles** 选项卡上启用的参数获取目标配置文件。
- `MATLAB expression` — 模块从 **MATLAB expression for target profiles** 参数指定的 MATLAB 表达式获取参与者配置文件。
- `From Scenario Reader block` — 模块从 Scenario Reader 模块或 RoadRunner Scenario Reader 模块指定的场景获取参与者配置文件。

### **MATLAB expression for target profiles** — 目标配置文件的 MATLAB 表达式 MATLAB 结构 | MATLAB 结构数组 | 有效 MATLAB 表达式

将参与者配置文件的 MATLAB 表达式指定为 MATLAB 结构、MATLAB 结构数组或生成此类结构或结构数组的有效 MATLAB 表达式。

如果您的 Scenario Reader 模块从 `drivingScenario` 对象读取数据，要直接从该对象获取参与者配置文件，请将此表达式设置为对该对象调用 `actorProfiles` 函数。例如：`actorProfiles(scenario)`。

默认目标配置文件表达式生成一个 MATLAB 结构，其形式如下：

```
struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4, ...
'OriginOffset',[-1.35 0 0],'RCSPattern',[10 10;10 10], ...
'RCSAzimuthAngles',[-180 180],'RCSElevationAngles',[-90 90])
```

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `MATLAB expression`。

### **Unique identifier for actors** — 场景定义的参与者标识符 `[]`（默认）| 正整数 | 长度为 *L* 的唯一正整数向量

将场景定义的参与者标识符指定为正整数或长度为 *L* 的唯一正整数向量。*L* 必须等于输入到 **Actors** 输入端口的参与者数量。向量元素必须与参与者的 `ActorID` 值匹配。您可以将 **Unique identifier for actors** 指定为 `[]`。在这种情况下，相同的参与者配置文件参数适用于所有参与者。

**示例：** `[1 2]`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **User-defined integer to classify actors** — 用户定义的分分类标识符 `0`（默认）| 整数 | 长度为 *L* 的整数向量

将用户定义的分分类标识符指定为整数或长度为 *L* 的整数向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为单个整数，其值适用于所有参与者。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Length of actors' cuboids (m)** — 参与者长方体的长度 `4.7`（默认）| 正实标量 | 长度为 *L* 的正值向量

将参与者长方体的长度指定为正实标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为正实标量，其值适用于所有参与者。单位为米。

**示例：** `6.3`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Width of actors' cuboids (m)** — 参与者长方体的宽度 `1.8`（默认）| 正实标量 | 长度为 *L* 的正值向量

将参与者长方体的宽度指定为正实标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为正实标量，其值适用于所有参与者。单位为米。

**示例：** `4.7`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Height of actors' cuboids (m)** — 参与者长方体的高度 `1.4`（默认）| 正实标量 | 长度为 *L* 的正值向量

将参与者长方体的高度指定为正实标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，您必须将此参数指定为正实标量，其值适用于所有参与者。单位为米。

**示例：** `2.0`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

### **Rotational center of actors from bottom center (m)** — 执行器旋转中心 `{[-1.35, 0, 0]}`（默认）| 长度为 *L* 的元胞数组，包含实值 1×3 向量

将执行器的旋转中心指定为长度为 *L* 的元胞数组，包含实值 1×3 向量。每个向量表示执行器旋转中心相对于执行器底部中心的偏移量。对于车辆，该偏移量对应于后轴中心下方地面上的点。当 **Unique identifier for actors** 为向量时，此参数为向量元胞数组，其元胞与 **Unique identifier for actors** 中的执行器一一对应。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为包含一个偏移向量的单元素元胞数组，其值适用于所有执行器。单位为米。

**示例：** `{[-1.35, 0.2, 0.3]}`

#### 依赖关系

要启用此参数，请将 **Target profiles definition** 参数设置为 `Parameters`。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从驾驶场景或 RoadRunner Scenario 生成超声波传感器检测

Ultrasonic Detection Generator 模块生成安装在自车上的超声波传感器对目标的检测。使用此模块可从包含执行器和轨迹的驾驶场景生成传感器数据，您可以从 Scenario Reader 模块读取这些数据。

在等于传感器更新间隔的时间间隔内，该模块输出从传感器到检测目标最近点的距离。该模块还提供参数来指定场景中对象的尺寸和属性。为了使用 Bird's-Eye Scope 应用可视化超声波检测，该模块还输出检测对象上最近点的三维坐标。

您可以将该模块与 Driving Scenario 和 RoadRunner Scenario 仿真中的车辆执行器一起使用。

您可以使用 Ultrasonic Detection Generator 为 Multi-Object Tracker 模块创建输入。在使用 Driving Scenario Designer 应用构建场景和传感器模型时，导出到 Simulink® 的超声波传感器将输出为 Ultrasonic Detection Generator 模块。
