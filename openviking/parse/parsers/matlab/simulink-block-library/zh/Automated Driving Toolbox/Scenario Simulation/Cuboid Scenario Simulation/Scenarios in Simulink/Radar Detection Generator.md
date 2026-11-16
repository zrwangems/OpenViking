---
type: simulink-block
title: 'Radar Detection Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Cuboid Scenario Simulation / Scenarios in Simulink'
documentation_page: 'radardetectiongenerator'
documentation_source_path: 'ref/radardetectiongenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Radar Detection Generator

## 端口

### 输入

### **Actors** — 场景参与者位姿 Simulink 总线，包含 MATLAB® 结构体

自车坐标系中的场景参与者位姿，指定为包含 MATLAB 结构体的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | 非负整数 |
| `Time` | 当前仿真时间 | 实值标量 |
| `Actors` | 参与者位姿 | 长度为 `NumActors` 的参与者位姿结构体数组 |

`Actors` 中的每个参与者位姿结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为正整数。 |
| *在 R2024b 中：* `FrontAxlePosition` | 车辆前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位为米。 **注意** 如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` 结构体不包含此字段。 |
| `Position` | 参与者位置，指定为形式为 [*x* *y* *z*] 的实值向量。单位为米。 |
| `Velocity` | 参与者在 *x*、*y* 和 *z* 方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的实值向量。单位为米每秒。 |
| `Roll` | 参与者横滚角，指定为实值标量。单位为度。 |
| `Pitch` | 参与者俯仰角，指定为实值标量。单位为度。 |
| `Yaw` | 参与者偏航角，指定为实值标量。单位为度。 |
| `AngularVelocity` | 参与者在 *x*、*y* 和 *z* 方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的实值向量。单位为度每秒。 |

### 输出

### **Detections** — 检测 Simulink 总线，包含 MATLAB 结构体

目标检测，返回为包含 MATLAB 结构体的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

您可以将来自这些传感器和其他传感器的目标检测传递给跟踪器，例如 Multi-Object Tracker 模块，并生成航迹。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时刻请求更新时为 false | Boolean |
| `Detections` | 目标检测 | 长度为 **Maximum number of reported detections** 参数所设置值的目标检测结构体数组。其中只有 `NumDetections` 个是实际检测。 |

每个目标检测结构体包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量值 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数所使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

- 对于笛卡尔坐标，`Measurement` 和 `MeasurementNoise` 按 **Coordinate system used to report detections** 参数指定的坐标系报告。
- 对于球坐标，`Measurement` 和 `MeasurementNoise` 按基于传感器笛卡尔坐标系的球坐标系报告。

**测量与测量噪声**

| **用于报告检测的坐标系** | 测量与测量噪声坐标 |
| --- | --- |
| `'Ego Cartesian'` | **对 **Enable range rate measurements** 的坐标依赖**  | **Enable range rate measurements** | 坐标 | | --- | --- | | true | `[x;y;z;vx;vy;vz]` | | false | `[x;y;z]` | |
| `'Sensor Cartesian'` |
| `'Sensor spherical'` | **对 **Enable elevation angle measurements** 和 **Enable range rate measurements** 的坐标依赖**  | **Enable range rate measurements** | **Enable elevation angle measurements** | 坐标 | | --- | --- | --- | | true | true | `[az;el;rng;rr]` | | true | false | `[az;rng;rr]` | | false | true | `[az;el;rng]` | | false | false | `[az;rng]` | |

**`MeasurementParameters`**

| 参数 | 定义 |
| --- | --- |
| `Frame` | 指示用于报告测量的坐标系的枚举类型。当 `Frame` 设置为 `'rectangular'` 时，检测按笛卡尔坐标报告。当 `Frame` 设置为 `'spherical'` 时，检测按球坐标报告。 |
| `OriginPosition` | 传感器原点相对于自车原点的 3-D 向量偏移。该向量派生自 `radarDetectionGenerator` 中指定的 `SensorLocation` 和 `Height` 属性。 |
| `Orientation` | 雷达传感器坐标系相对于自车坐标系的姿态。该姿态派生自 `radarDetectionGenerator` 的 `Yaw`、`Pitch` 和 `Roll` 属性。 |
| `HasVelocity` | 指示测量值是否包含速度或距离变化率分量。 |
| `HasElevation` | 指示测量值是否包含俯仰角分量。 |

每个检测的 `ObjectAttributes` 属性是一个包含以下字段的结构体。

| 字段 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的参与者标识符 `ActorID`。对于虚警，此值为负数。 |
| `SNR` | 检测的信噪比。单位为 dB。 |

## 参数

### 参数

#### 传感器标识

### **Unique identifier of sensor** — 唯一传感器标识符 1 (默认) | positive integer

唯一传感器标识符，指定为正整数。传感器标识符用于区分多传感器系统中来自不同传感器的检测。如果模型包含多个具有相同传感器标识符的传感器模块，Bird's-Eye Scope 将显示错误。

**示例：** `5`

### **Required interval between sensor updates (s)** — 所需时间间隔 `0.1` (默认) | positive real scalar

传感器更新之间所需的时间间隔，指定为正实数标量。此参数的值必须是 **Actors** 输入端口数据间隔的整数倍。在更新间隔之间从传感器请求的更新不包含检测。单位为秒。

#### 传感器外参

### **Sensor's (x,y) position (m)** — 雷达传感器中心的位置 `[3.4 0]` (默认) | real-valued 1-by-2 vector

雷达传感器中心的位置，指定为实值 1×2 向量。**Sensor's (x,y) position (m)** 和 **Sensor's height (m)** 参数定义雷达传感器相对于自车坐标系的坐标。默认值对应于安装在轿车前格栅中心的雷达。单位为米。

### **Sensor's height (m)** — 雷达传感器离地平面高度 `0.2` (默认) | positive real scalar

雷达传感器离地平面高度，指定为正实数标量。该高度相对于车辆地平面定义。**Sensor's (x,y) position (m)** 和 **Sensor's height (m)** 参数定义雷达传感器相对于自车坐标系的坐标。默认值对应于安装在轿车前格栅中心的雷达。单位为米。

**示例：** `0.25`

### **Yaw angle of sensor mounted on ego vehicle (deg)** — 传感器偏航角 `0` (默认) | real scalar

雷达传感器的偏航角，指定为实标量。偏航角是自车中心线与雷达传感器距离轴之间的角度。正偏航角对应于沿自车坐标系 *z* 轴正方向观察时的顺时针旋转。单位为度。

**示例：** `-4.0`

### **Pitch angle of sensor mounted on ego vehicle (deg)** — 传感器俯仰角 `0` (默认) | real scalar

传感器俯仰角，指定为实标量。俯仰角是雷达传感器距离轴与自车坐标系 *x-y* 平面之间的角度。正俯仰角对应于沿自车坐标系 *y* 轴正方向观察时的顺时针旋转。单位为度。

**示例：** `3.0`

### **Roll angle of sensor mounted on ego vehicle (deg)** — 传感器横滚角 `0` (默认) | real scalar

雷达传感器的横滚角，指定为实标量。横滚角是雷达距离轴围绕自车坐标系 *x* 轴旋转的角度。正横滚角对应于沿坐标系 *x* 轴正方向观察时的顺时针旋转。单位为度。

#### 端口设置

### **Source of output bus name** — 输出总线名称来源 `Auto` (默认) | `Property`

输出总线名称来源，指定为 `Auto` 或 `Property`。如果选择 `Auto`，模块将自动创建总线名称。如果选择 `Property`，请使用 **Specify an output bus name** 参数指定总线名称。

**示例：** `Property`

### **Specify an output bus name** — 输出总线名称 no default

输出总线名称。

#### 依赖项

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

#### 检测报告

### **Maximum number of reported detections** — 报告的检测最大数量 `50` (默认) | positive integer

传感器报告的检测最大数量，指定为正整数。检测按距传感器距离递增的顺序报告，直到达到最大数量。

**示例：** `100`

### **Coordinate system used to report detections** — 报告检测使用的坐标系 `Ego Cartesian` (默认) | `Sensor Cartesian` | `Sensor Spherical`

报告检测使用的坐标系，指定为以下值之一：

- `Ego Cartesian` — 检测在自车笛卡尔坐标系中报告。
- `Sensor Cartesian` — 检测在传感器笛卡尔坐标系中报告。
- `Sensor spherical` — 检测在球坐标系中报告。该坐标系以雷达为中心，并与雷达在自车上的姿态对齐。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间。

### 测量

#### 精度设置

### **Azimuthal resolution of radar (deg)** — 雷达方位角分辨率 `4.0` (默认) | positive real scalar

雷达的方位角分辨率，指定为正实数标量。方位角分辨率定义雷达能够区分两个目标的最小方位角间隔。方位角分辨率通常为雷达方位角波束宽度的 3dB 下降点。单位为度。

**示例：** `6.5`

### **Elevation resolution of radar (deg)** — 雷达俯仰角分辨率 `10.0` (默认) | positive real scalar

雷达的俯仰角分辨率，指定为正实数标量。俯仰角分辨率定义雷达能够区分两个目标的最小俯仰角间隔。俯仰角分辨率通常为雷达俯仰角波束宽度的 3dB 下降点。单位为度。

**示例：** `3.5`

#### 依赖项

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **Range resolution of radar (m)** — 雷达距离分辨率 `2.5` (默认) | positive real scalar

雷达的距离分辨率，指定为正实数标量。距离分辨率定义雷达能够区分两个目标的最小距离间隔。单位为米。

**示例：** `5.0`

### **Range rate resolution of radar (m/s)** — 雷达距离变化率分辨率 `0.5` (默认) | positive real scalar

雷达的距离变化率分辨率，指定为正实数标量。距离变化率分辨率定义雷达能够区分两个目标的最小距离变化率间隔。单位为米每秒。

**示例：** `0.75`

#### 依赖项

要启用此参数，请选中 **Enable range rate measurements** 复选框。

#### 偏差设置

### **Fractional azimuthal bias component of radar** — 方位角偏差分数 `0.1` (默认) | nonnegative real scalar

雷达的方位角偏差分数，指定为非负实数标量。方位角偏差表示为 **Azimuthal resolution of radar (deg)** 参数中指定的方位角分辨率的一部分。单位为无量纲。

**示例：** 0.3

### **Fractional elevation bias component of radar** — 俯仰角偏差分数 `0.1` (默认) | nonnegative real scalar

雷达的俯仰角偏差分数，指定为非负实数标量。俯仰角偏差表示为 **Elevation resolution of radar (deg)** 参数中指定的俯仰角分辨率的一部分。单位为无量纲。

**示例：** 0.2

#### 依赖项

要启用此参数，请选中 **Enable elevation angle measurements** 复选框。

### **Fractional range bias component of radar** — 距离偏差分数 `0.05` (默认) | nonnegative real scalar

雷达的距离偏差分数，指定为非负实数标量。距离偏差表示为 **Range resolution of radar (m)** 参数中指定的距离分辨率的一部分。单位为无量纲。

**示例：** `0.15`

### **Fractional range rate bias component of radar** — 雷达距离变化率偏差分数 `0.05` (默认) | nonnegative real scalar

雷达的距离变化率偏差分数，指定为非负实数标量。距离变化率偏差表示为 **Range rate resolution of radar (m)** 参数中指定的距离变化率分辨率的一部分。单位为无量纲。

**示例：** `0.2`

#### 依赖项

要启用此参数，请选中 **Enable range rate measurements** 复选框。

#### 检测器设置

### **Total angular field of view for radar (deg)** — 雷达传感器视场 `[20 5]` (默认) | real-valued 1-by-2 vector of positive values

雷达传感器视场，指定为正值实值 1×2 向量，`[azfov elfov]`。视场定义传感器覆盖的角度范围。每个分量必须位于区间 (0,180] 内。雷达视场外的目标不会被检测到。单位为度。

**示例：** `[14 7]`

### **Maximum detection range (m)** — 最大检测距离 `150` (默认) | positive real scalar

最大检测距离，指定为正实数标量。雷达无法检测超过此距离的目标。单位为米。

**示例：** `250`

### **Minimum and maximum range rates that can be reported** — 可报告的最小和最大检测距离变化率 `[-100 100]` (默认) | real-valued 1-by-2 vector

可报告的最小和最大检测距离变化率，指定为实值 1×2 向量。雷达无法检测此距离变化率区间之外的目标。单位为米每秒。

**示例：** `[-200 200]`

#### 依赖项

要启用此参数，请选中 **Enable range rate measurements** 复选框。

### **Detection probability** — 检测目标的概率 `0.9` (默认) | positive real scalar less than or equal to 1

检测目标的概率，指定为小于或等于 1 的正实数标量。此量定义在 **Range where detection probability is achieved (m)** 参数指定的参考检测距离处，检测具有 **Radar cross section at which detection probability is achieved (dBsm)** 参数所指定雷达散射截面的目标的概率。

**示例：** `0.95`

### **Rate at which false alarms are reported** — 虚警率 `1e-6` (默认) | positive real scalar

雷达分辨率单元内的虚警率，指定为范围 [10–7, 10–3] 内的正实数标量。单位为无量纲。

**示例：** `1e-5`

### **Range where detection probability is achieved (m):** — 达到检测概率的参考距离 `100` (默认) | positive real scalar

给定检测概率的参考距离，指定为正实数标量。参考距离是指具有 **Radar cross section at which detection probability is achieved (dBsm)** 所指定雷达散射截面的目标被检测到的概率为 **Detection probability** 所指定值时的距离。单位为米。

**示例：** `150`

### **Radar cross section at which detection probability is achieved (dBsm)** — 达到检测概率的参考雷达散射截面 `0.0` (默认) | nonnegative real scalar

给定检测概率的参考雷达散射截面 (RCS)，指定为非负实数标量。参考 RCS 是目标被检测到的概率为 **Detection probability** 所指定值时的值。单位为 dBsm。

**示例：** `2.0`

#### 测量设置

### **Enable elevation angle measurements** — 启用雷达测量俯仰角 `off` (默认) | `on`

选中此复选框可建模能够测量目标俯仰角的雷达。

### **Enable range rate measurements** — 启用雷达测量距离变化率 `on` (默认) | `off` | `on`

选中此复选框可建模能够测量目标距离变化率的雷达。

### **Add noise to measurements** — 启用向雷达传感器测量添加噪声 `on` (默认) | `off`

选中此复选框可向雷达传感器测量添加噪声。否则，测量无噪声。每个检测的 `MeasurementNoise` 属性始终会计算，并且不受 **Add noise to measurements** 参数所指定值的影响。通过将此复选框保留为 `off`，您可以将传感器的真值测量传递给 Multi-Object Tracker 模块。

### **Enable false detections** — 启用创建虚警雷达检测 `on` (默认) | `off`

选中此复选框可启用报告虚警雷达测量。否则，仅报告实际检测。

### **Enable occlusion** — 启用视线遮挡 `on` (默认) | `off`

选中此参数可启用视线遮挡，此时雷达仅从具有直接视线的对象生成检测。

#### 随机数生成器设置

### **Select method to specify initial seed** — 指定随机数生成器种子的方法 `Repeatable` (默认) | `Specify seed` | `Not repeatable`

设置随机数生成器种子的方法，指定为表中的选项之一。

| 选项 | 描述 |
| --- | --- |
| `Repeatable` | 模块为首次仿真生成随机初始种子，并在所有后续仿真中重用此种子。选择此参数可从统计传感器模型生成可重复结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 使用 **Specify seed** 参数指定您自己的随机初始种子以获得可重复结果。 |
| `Not repeatable` | 模块在每次仿真运行后生成新的随机初始种子。选择此参数可从统计传感器模型生成不可重复结果。 |

### **Initial seed** — 随机数生成器种子 `0` (默认) | nonnegative integer less than 2^32

随机数生成器种子，指定为小于 2^32 的非负整数。

**示例：** `2001`

#### 依赖项

要启用此参数，请将 `Random Number Generator Settings` 参数设置为 `Specify seed`。

### 参与者配置文件

### **Select method to specify actor profiles** — 指定参与者配置文件的方法 `From Scenario Reader block` (默认) | `Parameters` | `MATLAB expression`

指定参与者配置文件的方法，参与者配置文件是驾驶场景中所有参与者的物理和雷达特性，指定为以下选项之一：

- `From Scenario Reader block` — 模块从 Scenario Reader 模块或 RoadRunner Scenario Reader 模块指定的场景获取参与者配置文件。
- `Parameters` — 模块从 **Actor Profiles** 选项卡上启用的参数获取参与者配置文件。
- `MATLAB expression` — 模块从 **MATLAB expression for actor profiles** 参数指定的 MATLAB 表达式获取参与者配置文件。

### **MATLAB expression for actor profiles** — 参与者配置文件的 MATLAB 表达式 `struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4,'OriginOffset',[-1.35,0,0])` (默认) | MATLAB structure | MATLAB structure array | valid MATLAB expression

参与者配置文件的 MATLAB 表达式，指定为 MATLAB 结构体、MATLAB 结构体数组或生成此类结构体或结构体数组的有效 MATLAB 表达式。

如果您的 Scenario Reader 模块从 `drivingScenario` 对象读取数据，要直接从该对象获取参与者配置文件，请将此表达式设置为对该对象调用 `actorProfiles` 函数。例如：`actorProfiles(scenario)`。

**示例：** `struct('ClassID',5,'Length',5.0,'Width',2,'Height',2,'OriginOffset',[-1.55,0,0])`

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `MATLAB expression`。

### **Unique identifier for actors** — 场景定义的参与者标识符 `[]` (默认) | positive integer | length-*L* vector of unique positive integers

场景定义的参与者标识符，指定为正整数或长度为 *L* 的唯一正整数向量。*L* 必须等于输入到 **Actor** 输入端口的参与者数量。向量元素必须与参与者的 `ActorID` 值匹配。您可以将 **Unique identifier for actors** 指定为 `[]`。在这种情况下，相同的参与者配置文件参数适用于所有参与者。

**示例：** `[1,2]`

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **User-defined integer to classify actors** — 用户定义的参与者分类标识符 `0` (默认) | integer | length-*L* vector of integers

用户定义的分类标识符，指定为整数或长度为 *L* 的整数向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为单个整数，其值适用于所有参与者。

**示例：** `2`

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **Length of actors cuboids (m)** — 长方体长度 `4.7` (默认) | positive real scalar | length-*L* vector of positive values

长方体长度，指定为正实数标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为正实数标量，其值适用于所有参与者。单位为米。

**示例：** 6.3

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **Width of actors cuboids (m)** — 长方体宽度 `4.7` (默认) | positive real scalar | length-*L* vector of positive values

长方体宽度，指定为正实数标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为正实数标量，其值适用于所有参与者。单位为米。

**示例：** 4.7

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **Height of actors cuboids (m)** — 长方体高度 `4.7` (默认) | positive real scalar | length-*L* vector of positive values

长方体高度，指定为正实数标量或长度为 *L* 的正值向量。当 **Unique identifier for actors** 为向量时，此参数为相同长度的向量，其元素与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为正实数标量，其值适用于所有参与者。单位为米。

**示例：** `2.0`

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **Rotational center of actors from bottom center (m)** — 参与者旋转中心 { [ -1.35, 0, 0 ] } (默认) | length-*L* cell array of real-valued 1-by-3 vectors

参与者的旋转中心，指定为长度为 *L* 的实值 1×3 向量元胞数组。每个向量表示参与者旋转中心相对于参与者底部中心的偏移。对于车辆，该偏移对应于后轴中心下方地面上的点。当 **Unique identifier for actors** 为向量时，此参数为向量元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为包含一个元素的元胞数组，其中包含适用于所有参与者的偏移向量。单位为米。

**示例：** [ -1.35, .2, .3 ]

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **Radar cross section pattern (dBsm)** — 雷达散射截面 `{[10,10;10,10]}` (默认) | real-valued *Q*-by-*P* matrix | length-*L* cell array of real-valued *Q*-by-*P* matrices

参与者的雷达散射截面 (RCS)，指定为实值 *Q*×*P* 矩阵或长度为 *L* 的实值 *Q*×*P* 矩阵元胞数组。*Q* 是 **Elevation angles defining RCSPattern (deg)** 参数中对应元胞指定的俯仰角数量。*P* 是 **Azimuth angles defining RCSPattern (deg)** 属性中对应元胞指定的方位角数量。当 **Unique identifier for actors** 为向量时，此参数为矩阵元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。*Q* 和 *P* 可以在元胞数组中变化。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为包含一个元素的元胞数组，其中包含适用于所有参与者的矩阵。单位为 dBsm。

**示例：** [10 14 10; 9 13 9]

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **Azimuth angles defining RCSPattern (deg)** — 雷达散射截面方向图的方位角 `{[-180 180]}` (默认) | length-*L* cell array of real-valued *P*-length vectors

雷达散射截面方向图的方位角，指定为长度为 *L* 的实值 *P* 长度向量元胞数组。每个向量表示 **Radar cross section pattern (dBsm)** 中指定的雷达散射截面的 *P* 列的方位角。当 **Unique identifier for actors** 为向量时，此参数为向量元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。*P* 可以在元胞数组中变化。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为包含一个元素的元胞数组，其中包含适用于所有参与者的向量。单位为度。方位角位于 -180° 到 180° 范围内，并且必须严格递增。

当 **Radar cross section pattern (dBsm)** 的元胞中指定的雷达散射截面都具有相同维度时，只需指定包含一个元素的元胞数组，其中包含方位角向量。

**示例：** `[-90:90]`

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

### **Elevation angles defining RCSPattern (deg)** — 雷达散射截面方向图的俯仰角 `{[-90 90]}` (默认) | length-*L* cell array of real-valued *Q*-length vectors

雷达散射截面方向图的俯仰角，指定为长度为 *L* 的实值 *Q* 长度向量元胞数组。每个向量表示 **Radar cross section pattern (dBsm)** 中指定的雷达散射截面的 *Q* 列的俯仰角。当 **Unique identifier for actors** 为向量时，此参数为向量元胞数组，其元胞与 **Unique identifier for actors** 中的参与者一一对应。*Q* 可以在元胞数组中变化。当 **Unique identifier for actors** 为空 `[]` 时，必须将此参数指定为包含一个元素的元胞数组，其中包含适用于所有参与者的向量。单位为度。俯仰角位于 -90° 到 90° 范围内，并且必须严格递增。

当 **Radar cross section pattern (dBsm)** 的元胞中指定的雷达散射截面都具有相同维度时，只需指定包含一个元素的元胞数组，其中包含俯仰角向量。

**示例：** `[-25:25]`

#### 依赖项

要启用此参数，请将 **Select method to specify actor profiles** 参数设置为 `Parameters`。

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2021a: `radarDetectionGenerator` System object 和 Radar Detection Generator 模块不推荐使用

除非您需要 C/C++ 代码生成，否则不推荐使用 `radarDetectionGenerator` System object™ 和 Radar Detection Generator 模块。请分别改用 `drivingRadarDataGenerator` System object 和 Driving Radar Data Generator。这些新的雷达传感器提供了用于建模雷达传感器的附加属性，包括生成航迹和聚类检测的能力。

目前没有计划移除 `radarDetectionGenerator` System object 或 Radar Detection Generator 模块。使用这些功能的 MATLAB 代码和 Simulink 模型将继续运行。您仍然可以将 `radarDetectionGenerator` 对象导入 Driving Scenario Designer 应用。但是，该应用会更新导入传感器的参数，以反映 `drivingRadarDataGenerator` 对象的参数。此外，当您将包含 `radarDetectionGenerator` 传感器的场景导出到 MATLAB 代码或 Simulink 模型时，该应用会分别将该传感器导出为 `drivingRadarDataGenerator` 对象或 Driving Radar Data Generator 模块。

**更新代码**

在 MATLAB 代码中，将所有 `radarDetectionGenerator` 实例替换为 `drivingRadarDataGenerator`。此外，使用表中所示的等效 `drivingRadarDataGenerator` 属性更新所有 `radarDetectionGenerator` 属性。表中未列出的属性要么仅特定于 `drivingRadarDataGenerator`，要么在两个对象中相同。

| `radarDetectionGenerator` 属性 | 等效的 `drivingRadarDataGenerator` 属性 |
| --- | --- |
| `UpdateInterval` | `UpdateRate` |
| `SensorLocation`  `Height` | `MountingLocation` |
| `Yaw`  `Pitch`  `Roll` | `MountingAngles` |
| `MaxRange` | `RangeLimits` |
| `MaxNumDetectionsSource` | `MaxNumReportsSource` |
| `MaxNumDetections` | `MaxNumReports` |
| `ActorProfiles` | `Profiles` |

此表展示了创建 `drivingRadarDataGenerator` 对象而不是 `radarDetectionGenerator` 对象的示例代码。

| 不推荐用法 | 推荐替代方案 |
| --- | --- |
| ```     radar = radarDetectionGenerator( ...         'SensorLocation',[-1 0], ...         'Height',0.2, ...         'Yaw',180, ...         'Pitch',0, ...         'Roll',0, ...         'MaxRange',50); ``` | ```     radar = drivingRadarDataGenerator( ...         'MountingLocation',[-1 0 0.2], ...         'MountingAngles',[180 0 0], ...         'RangeLimits',[0 50]); ``` |

要在每个仿真时间步根据目标位姿生成检测，请将 `dets = radarDetectionGenerator(targets,time)` 语法替换为 `dets = drivingRadarDataGenerator(targets,time)`。

**更新模型**

在 Simulink 模型中，将所有 Radar Detection Generator 模块替换为 Driving Radar Data Generator 模块。在 Driving Radar Data Generator 模块中，按照更新代码部分中更新 `drivingRadarDataGenerator` 属性值的方式更新参数值。

如果您的模型包含单独的检测聚类模块，则可以将其移除，因为 Driving Radar Data Generator 模块默认对检测进行聚类。

例如，在此模型中，Sensor Simulation 子系统将来自 Radar Detection Generator 模块的串联检测输出到单独的检测聚类模块。

一个 Simulink 模型，其中雷达检测被输入到检测聚类模块

在此模型中，Sensor Simulation 子系统将来自 Driving Radar Data Generator 模块的串联、聚类检测直接输出到模型管线的下一部分。

一个不含检测聚类模块的 Simulink 模型

## 描述

根据雷达测量创建检测对象

Radar Detection Generator 模块根据安装在自车上的雷达传感器所获取的雷达测量生成检测。检测派生自仿真的参与者位姿，并按等于传感器更新间隔的间隔生成。默认情况下，检测参考自车坐标系。该生成器可以仿真添加了随机噪声的真实检测，也可以生成虚警检测。统计模型生成测量噪声、真实检测和误报。统计模型生成的随机数由 **Measurements** 选项卡上的随机数生成器设置控制。您可以使用 Radar Detection Generator 为 Multi-Object Tracker 模块创建输入。使用 Driving Scenario Designer 应用构建场景和传感器模型时，导出到 Simulink® 的雷达传感器会输出为 Radar Detection Generator 模块。
