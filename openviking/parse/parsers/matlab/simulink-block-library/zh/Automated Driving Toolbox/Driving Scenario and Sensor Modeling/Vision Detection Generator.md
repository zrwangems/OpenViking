---
type: simulink-block
title: 'Vision Detection Generator'
family: 'driving-scenario-and-sensor-modeling'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'visiondetectiongenerator'
documentation_source_path: 'ref/visiondetectiongenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Vision Detection Generator

## 端口

### 输入

### **Actors** — 场景参与者位姿，包含 MATLAB® structure 的 Simulink 总线

自车坐标系中的场景参与者位姿，指定为包含 MATLAB structure 的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumActors` | 参与者数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real-valued scalar |
| `Actors` | 参与者位姿 | `NumActors`-length array of actor pose structures |

`Actors` 中的每个参与者位姿结构体必须包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `ActorID` | 场景定义的参与者标识符，指定为 positive integer。 |
| *In R2024b:*  `FrontAxlePosition` | 车辆前轴位置，指定为形式为 [*x* *y* *z*] 的三元素行向量。单位为 meters。  **注意**  如果驾驶场景中至少有一辆车不包含前轴轨迹，则 `ActorPoses` structure 不包含此字段。 |
| `Position` | 参与者位置，指定为形式为 [*x* *y* *z*] 的 real-valued vector。单位为 meters。 |
| `Velocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的速度 (*v*)，指定为形式为 [*v**x* *v**y* *v**z*] 的 real-valued vector。单位为 meters per second。 |
| `Roll` | 参与者的横滚角，指定为 real-valued scalar。单位为 degrees。 |
| `Pitch` | 参与者的俯仰角，指定为 real-valued scalar。单位为 degrees。 |
| `Yaw` | 参与者的偏航角，指定为 real-valued scalar。单位为 degrees。 |
| `AngularVelocity` | 参与者在 *x*-、*y*- 和 *z*-方向上的角速度 (*ω*)，指定为形式为 [*ω**x* *ω**y* *ω**z*] 的 real-valued vector。单位为 degrees per second。 |

#### 依赖关系

要启用此输入端口，请将 **传感器生成的检测类型** 参数设置为 `Objects only`、`Lanes with occlusion` 或 `Lanes and objects`。

### **Lane Boundaries** — 车道边界，包含 MATLAB structure 的 Simulink 总线

自车坐标系中的车道边界，指定为包含 MATLAB structure 的 Simulink 总线。

该结构体必须包含以下字段。

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumLaneBoundaries` | 车道边界数量 | Nonnegative integer |
| `Time` | 当前仿真时间 | Real scalar |
| `LaneBoundaries` | 从自车最左侧车道开始的车道边界。 | `NumLaneBoundaries`-length array of lane boundary structures |

`LaneBoundaries` 中的每个车道边界结构体必须包含以下字段。

|  |  |
| --- | --- |
| **字段** | **描述** |
| `Coordinates` | 车道边界坐标，指定为 real-valued *N*-by-3 matrix，其中 *N* 是车道边界坐标的数量。车道边界坐标定义边界上各点的位置，这些点位于沿道路中心线距自车指定纵向距离处。  - 在 MATLAB 中，通过 `laneBoundaries` 函数的 `'XDistance'` 名称-值对组参数指定这些距离。 - 在 Simulink 中，通过 Scenario Reader 模块的 **Distances from ego vehicle for computing boundaries (m)** 参数或 Simulation 3D Vision Detection Generator 模块的 **Distance from parent for computing lane boundaries** 参数指定这些距离。  此矩阵还包括距自车零距离处的边界坐标。这些坐标位于自车原点的左侧和右侧，自车原点位于后轴中心下方。单位为 meters。 |
| `Curvature` | `Coordinates` 矩阵每一行处的车道边界曲率，指定为 real-valued *N*-by-1 vector。*N* 是车道边界坐标的数量。单位为 radians per meter。 |
| `CurvatureDerivative` | `Coordinates` 矩阵每一行处的车道边界曲率导数，指定为 real-valued *N*-by-1 vector。*N* 是车道边界坐标的数量。单位为 radians per square meter。 |
| `HeadingAngle` | 初始车道边界航向角，指定为 real scalar。车道边界的航向角相对于自车航向。单位为 degrees。 |
| `LateralOffset` | 自车位置相对于车道边界的横向偏移，指定为 real scalar。自车左侧车道边界的偏移为正。自车右侧车道边界的偏移为负。单位为 meters。在此图像中，自车距左侧车道偏移 1.5 meters，距右侧车道偏移 2.1 meters。  自车在行驶车道中 |
| `BoundaryType` | 车道边界标记类型，指定为以下值之一：  - `'Unmarked'` — 不存在物理车道标记 - `'Solid'`  — 单条不间断线 - `'Dashed'` — 单条虚线车道标记 - `'DoubleSolid'` — 两条不间断线 - `'DoubleDashed'` — 两条虚线 - `'SolidDashed'` — 左侧为实线，右侧为虚线 - `'DashedSolid'` — 左侧为虚线，右侧为实线 |
| `Strength` | 车道边界标记的饱和度强度，指定为 0 到 1 范围内的 real scalar。值 `0` 对应于颜色完全不饱和的标记。该标记为灰色。值 `1` 对应于颜色完全饱和的标记。 |
| `Width` | 车道边界宽度，指定为 positive real scalar。在双线车道标记中，两条线以及线间空间使用相同的宽度。单位为 meters。 |
| `Length` | 虚线中虚线的长度，指定为 positive real scalar。在双线车道标记中，两条线使用相同的长度。 |
| `Space` | 虚线中虚线之间的间隔长度，指定为 positive real scalar。在虚线双线车道标记中，两条线使用相同的间隔。 |

#### 依赖关系

要启用此输入端口，请将 **传感器生成的检测类型** 参数设置为 `Lanes only`、`Lanes only`、`Lanes with occlusion` 或 `Lanes and objects`。
### 输出

### **Object Detections** — 目标检测，包含 MATLAB structure 的 Simulink 总线

目标检测，返回为包含 MATLAB structure 的 Simulink 总线。有关总线的更多详细信息，请参阅 Create Nonvirtual Buses (Simulink)。

您可以将这些传感器和其他传感器的目标检测传递给跟踪器（例如 Multi-Object Tracker 模块），并生成航迹。

检测结构体具有以下形式：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | Integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | Boolean |
| `Detections` | 目标检测 | 目标检测结构体数组，长度由 **报告的最大检测数** 参数设置。只有 `NumDetections` 个这些检测是实际检测。 |

目标检测结构体包含以下属性。

| 属性 | 定义 |
| --- | --- |
| `Time` | 测量时间 |
| `Measurement` | 目标测量 |
| `MeasurementNoise` | 测量噪声协方差矩阵 |
| `SensorIndex` | 传感器的唯一 ID |
| `ObjectClassID` | 目标分类 |
| `MeasurementParameters` | 非线性卡尔曼跟踪滤波器初始化函数所使用的参数 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 |

`Measurement` 字段报告测量在 **用于报告检测的坐标系** 所指定坐标系中的位置和速度。此字段是形式为 [*x*; *y*; *z*; *vx*; *vy*; *vz*] 的 real-valued column vector。单位为 meters per second。

`MeasurementNoise` 字段是 6-by-6 matrix，用于报告 `Measurement` 字段中每个坐标的测量噪声协方差。

`MeasurementParameters` 字段是包含以下字段的结构体。

| 参数 | 定义 |
| --- | --- |
| `Frame` | 枚举类型，指示用于报告测量的坐标框架。Vision Detection Generator 模块在自车和传感器笛卡尔坐标系中报告检测，二者均为直角坐标框架。因此，对于此模块，`Frame` 始终设置为 `'rectangular'`。 |
| `OriginPosition` | 传感器原点相对于自车原点的 3-D 向量偏移。该向量由模块的 **传感器的 (x,y) 位置 (m)** 和 **传感器高度 (m)** 参数导出。 |
| `Orientation` | 视觉传感器坐标系相对于自车坐标系的姿态。该姿态由模块的 **安装在自车上的传感器偏航角 (deg)**、**安装在自车上的传感器俯仰角 (deg)** 和 **安装在自车上的传感器横滚角 (deg)** 参数导出。 |
| `HasVelocity` | 指示测量是否包含速度。 |

每个检测的 `ObjectAttributes` 属性是包含以下字段的结构体。

| 字段 | 定义 |
| --- | --- |
| `TargetIndex` | 生成该检测的参与者的标识符 `ActorID`。对于误报，此值为负数。 |

#### 依赖关系

要启用此输出端口，请将 **传感器生成的检测类型** 参数设置为 `Objects only`、`Lanes with occlusion` 或 `Lanes and objects`。

### **Lane Detections** — 车道边界检测，包含 MATLAB structure 的 Simulink 总线

车道边界检测，返回为包含 MATLAB structure 的 Simulink 总线。该结构体包含以下字段：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 车道检测时间 | Real scalar |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 false | Boolean |
| `SensorIndex` | 传感器的唯一标识符 | Positive integer |
| `NumLaneBoundaries` | 车道边界检测数量 | Nonnegative integer |
| `LaneBoundaries` | 车道边界检测 | `clothoidLaneBoundary` 对象数组 |

#### 依赖关系

要启用此输出端口，请将 **传感器生成的检测类型** 参数设置为 `Lanes only`、`Lanes with occlusion` 或 `Lanes and objects`。

## 参数

### 参数

#### 传感器标识

### **传感器唯一标识符** — 唯一传感器标识符 `1`（默认） | positive integer

唯一传感器标识符，指定为 positive integer。传感器标识符用于区分多传感器系统中来自不同传感器的检测。如果模型包含多个具有相同传感器标识符的传感器模块，Bird's-Eye Scope 将显示错误。

**示例：** `5`

### **传感器生成的检测类型** — 选择检测类型 `Objects only`（默认） | `Lanes only` | `Lanes with occlusion` | `Lanes and objects`

传感器生成的检测类型，指定为 `Objects only`、`Lanes only`、`Lanes with occlusion` 或 `Lanes and objects`。

- 当设置为 `Objects only` 时，不使用道路信息来遮挡参与者。
- 当设置为 `Lanes only` 时，不使用参与者信息来检测车道。
- 当设置为 `Lanes with occlusion` 时，相机视场中的参与者可能会削弱传感器检测车道的能力。
- 当设置为 `Lanes and objects` 时，传感器既生成目标检测，也生成带遮挡的车道检测。

### **传感器更新之间所需时间间隔 (s)** — 所需时间间隔 `0.1`（默认） | positive real scalar

传感器更新之间所需时间间隔，指定为 positive real scalar。此参数的值必须是 **Actors** 输入端口数据间隔的整数倍。在更新间隔之间从传感器请求的更新不包含检测。单位为 seconds。

### **车道检测更新之间所需时间间隔 (s)** — 车道检测更新之间的时间间隔 `0.1`（默认） | positive real scalar

车道检测更新之间所需时间间隔，指定为 positive real scalar。视觉检测生成器按固定时间间隔调用。视觉检测器按此参数定义的间隔生成新的车道检测，该间隔必须是仿真时间间隔的整数倍。在更新间隔之间从传感器请求的更新不包含车道检测。单位为 seconds。

#### 传感器外参

### **传感器的 (x,y) 位置 (m)** — 视觉传感器中心的位置 `[3.4 0]`（默认） | real-valued 1-by-2 vector

视觉传感器中心的位置，指定为 real-valued 1-by-2 vector。**传感器的 (x,y) 位置 (m)** 和 **传感器高度 (m)** 参数定义视觉传感器相对于自车坐标系的坐标。默认值对应于安装在轿车仪表板上的前向视觉传感器。单位为 meters。

### **传感器高度 (m)** — 视觉传感器离地平面高度 `0.2`（默认） | positive real scalar

视觉传感器离地平面高度，指定为 positive real scalar。高度相对于车辆地平面定义。**传感器的 (x,y) 位置 (m)** 和 **传感器高度 (m)** 参数定义视觉传感器相对于自车坐标系的坐标。默认值对应于安装在轿车仪表板上的前向视觉传感器。单位为 meters。

**示例：** `0.25`

### **安装在自车上的传感器偏航角 (deg)** — 传感器偏航角 `0`（默认） | real scalar

视觉传感器偏航角，指定为 real scalar。偏航角是自车中心线与相机光轴之间的角度。当沿自车坐标系的 *z*-轴正方向观察时，正偏航角对应于顺时针旋转。单位为 degrees。

**示例：** `-4.0`

### **安装在自车上的传感器俯仰角 (deg)** — 传感器俯仰角 `0`（默认） | real scalar

传感器俯仰角，指定为 real scalar。俯仰角是相机光轴与自车坐标系 *x-y* 平面之间的角度。当沿自车坐标系的 *y*-轴正方向观察时，正俯仰角对应于顺时针旋转。单位为 degrees。

**示例：** `3.0`

### **安装在自车上的传感器横滚角 (deg)** — 传感器横滚角 `0`（默认） | real scalar

视觉传感器横滚角，指定为 real scalar。横滚角是相机光轴绕自车坐标系 *x*-轴的旋转角度。当沿坐标系 *x*-轴正方向观察时，正横滚角对应于顺时针旋转。单位为 degrees。

#### 输出端口设置

### **目标总线名称的来源** — 目标总线名称的来源 `Auto`（默认） | `Property`

目标总线名称的来源，指定为 `Auto` 或 `Property`。如果选择 `Auto`，模块会自动创建总线名称。如果选择 `Property`，请使用 **目标总线名称** 参数指定总线名称。

**示例：** `Property`

### **输出车道总线名称的来源** — 车道总线名称的来源 `Auto`（默认） | `Property`

输出车道总线名称的来源，指定为 `Auto` 或 `Property`。如果选择 `Auto`，模块会自动创建总线名称。如果选择 `Property`，请使用 **目标总线名称** 参数指定总线名称。

**示例：** `Property`

### **目标总线名称** — 目标总线名称 valid bus name

目标总线名称，指定为有效总线名称。

**示例：** `objectbus`

#### 依赖关系

要启用此参数，请将 **目标总线名称的来源** 参数设置为 `Property`。

### **指定输出车道总线名称** — 输出车道总线名称 valid bus name

输出车道总线名称，指定为有效总线名称。

**示例：** `lanebus`

#### 依赖关系

要启用此参数，请将 **输出车道总线名称的来源** 参数设置为 `Property`。

#### 检测报告

### **报告的最大检测数** — 报告的最大检测数 `50`（默认） | positive integer

传感器报告的最大检测数，指定为 positive integer。检测按距传感器的距离递增顺序报告，直到达到最大数量。

**示例：** `100`

#### 依赖关系

要启用此参数，请将 **传感器生成的检测类型** 参数设置为 `Objects only` 或 `Lanes and objects`。

### **报告的最大车道数** — 报告的最大车道数 `30`（默认） | positive integer

报告的最大车道数，指定为 positive integer。

**示例：** `100`

#### 依赖关系

要启用此参数，请将 **传感器生成的检测类型** 参数设置为 `Lanes only`、`Lanes with occlusion` 或 `Lanes and objects`。

### **用于报告检测的坐标系** — 报告检测的坐标系 `Ego Cartesian`（默认） | `Sensor Cartesian`

报告检测的坐标系，指定为以下值之一：

- `Ego Cartesian` — 检测在自车笛卡尔坐标系中报告。
- `Sensor Cartesian`— 检测在传感器笛卡尔坐标系中报告。

#### 仿真

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间。

### 测量

#### 设置

### **最大检测距离 (m)** — 最大检测距离 `150`（默认） | positive real scalar

最大检测距离，指定为 positive real scalar。视觉传感器无法检测超出此距离的目标。单位为 meters。

**示例：** `250`

#### 目标检测器设置

### **边界框精度 (pixels)** — 边界框精度 `5`（默认） | positive real scalar

边界框精度，指定为 positive real scalar。此量定义检测器将边界框与目标匹配的精度。单位为 pixels。

**示例：** `9`

### **平滑滤波器噪声强度 (m/s^2)** — 用于滤波位置和速度测量的噪声强度 `5`（默认） | positive real scalar

用于滤波位置和速度测量的噪声强度，指定为 positive real scalar。噪声强度定义视觉传感器中内部匀速卡尔曼滤波器过程噪声的标准差。该滤波器使用分段常值白噪声加速度模型对过程噪声建模。噪声强度通常为目标预期最大加速度量级。单位为 meters per second squared。

**示例：** `2`

### **可检测的最大目标速度 (m/s)** — 最大可检测目标速度 `100`（默认） | nonnegative real scalar

最大可检测目标速度，指定为 nonnegative real scalar。单位为 meters per second。

**示例：** `20`

### **检测器允许的最大遮挡** — 检测器允许的最大遮挡 `0.5`（默认） | real scalar in the range [0 1)

目标允许的最大遮挡，指定为 [0 1) 范围内的 real scalar。*Occlusion* 是目标总表面积中传感器不可见的部分所占比例。值 1 表示目标被完全遮挡。单位：dimensionless。

**示例：** `0.2`

### **目标的最小可检测图像大小** — 目标的最小高度和宽度 `[15,15]`（默认） | 1-by-2 vector of positive values

视觉传感器在图像中检测到目标的最小高度和宽度，指定为 `[minHeight,minWidth]` positive values 向量。目标的 2-D 投影高度必须大于或等于 `minHeight`。目标的投影宽度必须大于或等于 `minWidth`。单位为 pixels。

**示例：** `[25 20]`

### **检测到目标的概率** — 检测概率 `0.9`（默认） | positive real scalar less than or equal to 1

检测到目标的概率，指定为小于或等于 1 的 positive real scalar。此量定义传感器检测到可检测目标的概率。*Detectable object* 是满足最小可检测大小、最大距离、最大速度和最大允许遮挡约束的目标。

**示例：** `0.95`

### **每幅图像的误报数** — 视觉传感器每幅图像生成的误检测数 `0.1`（默认） | nonnegative real scalar

视觉传感器每幅图像生成的误检测数，指定为 nonnegative real scalar。

**示例：** `1.0`

#### 车道检测器设置

### **图像中车道的最小大小 (pixels)** — 车道最大大小 `[20,3]`（默认） | 1-by-2 real-valued vector

在考虑曲率后，传感器可检测的相机图像中投影车道标记的最小大小，指定为 1-by-2 real-valued vector `[minHeight minWidth]`。车道标记必须超过这两个值才能被检测到。单位为 pixels。

#### 依赖关系

要启用此参数，请将 **传感器生成的检测类型** 参数设置为 `Lanes only`、`Lanes only` 或 `Lanes and objects`。

### **车道边界精度 (pixels)** — 车道边界精度 `3`（默认） | positive real scalar

车道边界精度，指定为 positive real scalar。此参数定义车道传感器放置车道边界的精度。单位为 pixels。

**示例：** `2.5`

#### 依赖关系

要启用此参数，请将 **传感器生成的检测类型** 参数设置为 `Lanes only`、`Lanes only` 或 `Lanes and objects`。

#### 随机数生成器设置

### **向测量添加噪声** — 启用向视觉传感器测量添加噪声 `on`（默认） | `off`

选择此参数可向视觉传感器测量添加噪声。否则，测量无噪声。每个检测的 `MeasurementNoise` 属性始终会被计算，并且不受您为 **向测量添加噪声** 参数指定的值影响。

### **选择指定初始种子的方法** — 指定随机数生成器种子的方法 `Repeatable`（默认） | `Specify seed` | `Not repeatable`

设置随机数生成器种子的方法，指定为表中的选项之一。

| 选项 | 描述 |
| --- | --- |
| `Repeatable` | 模块在首次仿真时生成随机初始种子，并在所有后续仿真中重用此种子。选择此参数以从统计传感器模型生成可重复结果。要更改此初始种子，请在 MATLAB 命令提示符下输入：`clear all`。 |
| `Specify seed` | 使用 **初始种子** 参数指定您自己的随机初始种子以获得可重复结果。 |
| `Not repeatable` | 模块在每次仿真运行后生成新的随机初始种子。选择此参数以从统计传感器模型生成不可重复结果。 |

### **初始种子** — 随机数生成器种子 `0`（默认） | nonnegative integer less than 232

随机数生成器种子，指定为小于 232 的 nonnegative integer。

**示例：** `2001`

#### 依赖关系

要启用此参数，请将 **随机数生成器设置** 参数设置为 `Specify seed`。

### 参与者配置文件

### **选择指定参与者配置文件的方法** — 指定参与者配置文件的方法 `From Scenario Reader block`（默认） | `Parameters` | `MATLAB expression`

指定参与者配置文件的方法，这些配置文件是驾驶场景中所有参与者的物理特性和雷达特性，指定为以下选项之一：

- `From Scenario Reader block` — 模块从 Scenario Reader 模块或 RoadRunner Scenario Reader 模块指定的场景中获取参与者配置文件。
- `Parameters` — 模块从 **Actor Profiles** 选项卡上启用的参数中获取参与者配置文件。
- `MATLAB expression` — 模块从 **参与者配置文件的 MATLAB 表达式** 参数指定的 MATLAB 表达式中获取参与者配置文件。

### **参与者配置文件的 MATLAB 表达式** — 参与者配置文件的 MATLAB 表达式 `struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4,'OriginOffset',[-1.35,0,0])`（默认） | MATLAB structure | MATLAB structure array | valid MATLAB expression

参与者配置文件的 MATLAB 表达式，指定为 MATLAB structure、MATLAB structure array，或生成此类结构体或结构体数组的有效 MATLAB 表达式。

如果您的 Scenario Reader 模块从 `drivingScenario` 对象读取数据，要直接从此对象获取参与者配置文件，请将此表达式设置为对该对象调用 `actorProfiles` 函数。例如：`actorProfiles(scenario)`。

**示例：** `struct('ClassID',5,'Length',5.0,'Width',2,'Height',2,'OriginOffset',[-1.55,0,0])`

#### 依赖关系

要启用此参数，请将 **选择指定参与者配置文件的方法** 参数设置为 `MATLAB expression`。

### **参与者的唯一标识符** — 场景定义的参与者标识符 `[]`（默认） | positive integer | length-*L* vector of unique positive integers

场景定义的参与者标识符，指定为 positive integer 或 length-*L* vector of unique positive integers。*L* 必须等于输入到 **Actors** 输入端口的参与者数量。向量元素必须与参与者的 `ActorID` 值匹配。您可以将 **参与者的唯一标识符** 指定为 `[]`。在这种情况下，相同的参与者配置文件参数适用于所有参与者。

**示例：** `[1,2]`

#### 依赖关系

要启用此参数，请将 **选择指定参与者配置文件的方法** 参数设置为 `Parameters`。

### **用于对参与者分类的用户定义整数** — 用户定义的分类标识符 `0`（默认） | integer | length-*L* vector of integers

用户定义的分类标识符，指定为 integer 或 length-*L* vector of integers。当 **参与者的唯一标识符** 是向量时，此参数是长度相同的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为单个整数，其值适用于所有参与者。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **选择指定参与者配置文件的方法** 参数设置为 `Parameters`。

### **参与者长方体长度 (m)** — 长方体长度 `4.7`（默认） | positive real scalar | length-*L* vector of positive values

长方体长度，指定为 positive real scalar 或 length-*L* vector of positive values。当 **参与者的唯一标识符** 是向量时，此参数是长度相同的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为 positive real scalar，其值适用于所有参与者。单位为 meters。

**示例：** 6.3

#### 依赖关系

要启用此参数，请将 **选择指定参与者配置文件的方法** 参数设置为 `Parameters`。

### **参与者长方体宽度 (m)** — 长方体宽度 `4.7`（默认） | positive real scalar | length-*L* vector of positive values

长方体宽度，指定为 positive real scalar 或 length-*L* vector of positive values。当 **参与者的唯一标识符** 是向量时，此参数是长度相同的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为 positive real scalar，其值适用于所有参与者。单位为 meters。

**示例：** 4.7

#### 依赖关系

要启用此参数，请将 **选择指定参与者配置文件的方法** 参数设置为 `Parameters`。

### **参与者长方体高度 (m)** — 长方体高度 `4.7`（默认） | positive real scalar | length-*L* vector of positive values

长方体高度，指定为 positive real scalar 或 length-*L* vector of positive values。当 **参与者的唯一标识符** 是向量时，此参数是长度相同的向量，其元素与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为 positive real scalar，其值适用于所有参与者。单位为 meters。

**示例：** `2.0`

#### 依赖关系

要启用此参数，请将 **选择指定参与者配置文件的方法** 参数设置为 `Parameters`。

### **参与者从底部中心起的旋转中心 (m)** — 参与者的旋转中心 { [ -1.35, 0, 0 ] }（默认） | length-*L* cell array of real-valued 1-by-3 vectors

参与者的旋转中心，指定为 length-*L* cell array of real-valued 1-by-3 vectors。每个向量表示参与者旋转中心相对于参与者底部中心的偏移。对于车辆，该偏移对应于后轴中心下方地面上的点。当 **参与者的唯一标识符** 是向量时，此参数是向量元胞数组，其元胞与 **参与者的唯一标识符** 中的参与者一一对应。当 **参与者的唯一标识符** 为空 `[]` 时，必须将此参数指定为包含一个元素的元胞数组，其中包含适用于所有参与者的偏移向量。单位为 meters。

**示例：** [ -1.35, .2, .3 ]

#### 依赖关系

要启用此参数，请将 **选择指定参与者配置文件的方法** 参数设置为 `Parameters`。

### 相机内参

### **焦距 (pixels)** — 相机焦距 `[800,800]`（默认） | two-element real-valued vector

相机焦距，以 pixels 为单位，指定为 two-element real-valued vector。另请参阅 `cameraIntrinsics` 的 `FocalLength` 属性。

**示例：** `[480,320]`

### **相机光学中心 (pixels)** — 相机光学中心 `[320,240]`（默认） | two-element real-valued vector

相机光学中心，以 pixels 为单位，指定为 two-element real-valued vector。另请参阅 `cameraIntrinsics` 的 `PrincipalPoint` 属性。

**示例：** `[480,320]`

### **相机生成的图像大小 (pixels)** — 相机生成的图像大小 `[480,640]`（默认） | two-element vector of positive integers

相机生成的图像大小，以 pixels 为单位，指定为 two-element vector of positive integers。另请参阅 `cameraIntrinsics` 的 `ImageSize` 属性。

**示例：** `[240,320]`

### **径向畸变系数** — 径向畸变系数 `[0,0]`（默认） | two-element real-valued vector | three-element real-valued vector

径向畸变系数，指定为 two-element 或 three-element real-valued vector。有关设置这些系数的详细信息，请参阅 `cameraIntrinsics` 的 `RadialDistortion` 属性。

**示例：** `[1,1]`

### **切向畸变系数** — 切向畸变系数 `[0,0]`（默认） | two-element real-valued vector

切向畸变系数，指定为 two-element real-valued vector。有关设置这些系数的详细信息，请参阅 `cameraIntrinsics` 的 `TangentialDistortion` 属性。

**示例：** `[1,1]`

### **相机轴倾斜** — 相机轴倾斜角 `0`（默认） | real scalar

相机轴倾斜角，指定为 real scalar。另请参阅 `cameraIntrinsics` 的 `Skew` 属性。

**示例：** `0.1`

## 所属库

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 对于驾驶场景工作流，Vision Detection Generator 模块支持：

  - Rapid accelerator mode simulation。
  - 使用 Simulink Coder™ 以及面向 Simulink Real-Time™ 目标的独立部署。
- 对于 RoadRunner Scenario 工作流，Vision Detection Generator 模块支持使用 ready-to-run packages 进行独立部署。有关为您的 Simulink 模型生成 ready-to-run packages 的更多信息，请参阅 Publish Ready-to-Run Actor Behaviors for Reuse and Simulation Performance。

## 版本历史

**在 R2017b 中引入**

### R2024a：与 RoadRunner Scenario 仿真一起使用时，不需要使用 `addSensors` 函数注册传感器模型

从 R2024a 开始，Simulink 会自动实例化 `SensorSimulation` 对象，并将模型中定义的传感器添加到 RoadRunner scenario。因此，不需要使用 `addSensors` 函数手动注册 Vision Detection Generator 模块。有关新工作流的更多信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。

在 R2024a 之前的版本中，您必须使用 `addSensors` 函数手动将该模块注册为传感器模型。有关更多信息，请参阅 Adding sensors manually using `addSensors` function is not required for Simulink models。

### R2023a：Simulink 总线不显示在工作区中

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

从驾驶场景或 RoadRunner Scenario 中的视觉测量中检测目标和车道

Vision Detection Generator 模块根据安装在自车上的视觉传感器所采集的相机测量生成检测。

该模块根据仿真的参与者位姿推导检测，并按等于传感器更新间隔的间隔生成这些检测。默认情况下，检测参考自车坐标系。该模块可以仿真添加了随机噪声的真实检测，也可以生成误报检测。统计模型生成测量噪声、真实检测和误报。要控制统计模型生成的随机数，请使用模块 **Measurements** 选项卡上的随机数生成器设置。

您可以将该模块与 Driving Scenario 和 RoadRunner Scenario 仿真中的车辆参与者一起使用。有关更多信息，请参阅 Add Sensors to RoadRunner Scenario Using Simulink 示例。

您可以使用 Vision Detection Generator 为 Multi-Object Tracker 模块创建输入。使用 Driving Scenario Designer 应用构建场景和传感器模型时，导出到 Simulink® 的相机传感器会输出为 Vision Detection Generator 模块。
