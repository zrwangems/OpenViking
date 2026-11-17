---
type: simulink-block
title: 'Generalized Optimal Subpattern Assignment Metric'
family: 'track-metrics'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Track Metrics'
documentation_page: 'generalizedoptimalsubpatternassignmentmetric'
documentation_source_path: 'ref/generalizedoptimalsubpatternassignmentmetric.html'
language: zh-CN
chinese_source: worker-translation
---

# Generalized Optimal Subpattern Assignment Metric

## 端口

### 输入

### **Tracks** — 包含 MATLAB® 结构的航迹列表 Simulink® 总线

航迹列表，指定为包含 MATLAB 结构的 Simulink 总线。

如果在 **Port Setting** 选项卡上将 **Track bus** 参数指定为 `objectTrack`，则结构必须使用以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构数组 |

每个航迹结构必须包含 `TrackID` 和 `State` 字段。此外，如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则每个结构必须包含 `StateCovariance` 字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符，指定为非负整数。 |
| `State` | 更新时刻的状态向量值，指定为 *N* 元向量，其中 *N* 是状态的维数。 |
| `StateCovariance` | 不确定度协方差矩阵，指定为 *N*×*N* 矩阵，其中 *N* 是状态的维数。 |

如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则结构必须包含 `StateCovariance` 字段。

如果将 **Track bus** 参数指定为 `custom`，则可以使用自己的航迹总线格式。在这种情况下，必须使用 **Track extractor function** 参数定义航迹提取器函数。该函数必须使用以下语法：

    tracks = trackExtractorFcn(trackInputFromBus)

其中 `trackInputFromBus` 是来自航迹总线的输入，`tracks` 必须返回为包含 `TrackID` 和 `State` 字段的结构体数组。

### **Truths** — 包含 MATLAB® 结构的真值列表 Simulink® 总线

真值列表，指定为包含 MATLAB 结构的 Simulink 总线。

如果在 **Port Setting** 选项卡上将 **Truth bus** 参数指定为 `Platform`，则结构必须使用以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumPlatforms` | 真值平台数量 |
| `Platforms` | 真值平台结构数组 |

每个平台结构具有以下字段：

| 字段 | 定义 |
| --- | --- |
| `PlatformID` | 用于区分平台的唯一标识符，指定为非负整数。 |
| `Position` | 平台的位置，指定为 *M* 元向量，其中 *M* 是位置状态的维数。例如，对于 3-D 位置，*M* = 3。 |
| `Velocity` | 平台的速度，指定为 *M* 元向量，其中 *M* 是速度状态的维数。例如，对于 3-D 速度，*M* = 3。 |

如果将 **Truth bus** 参数指定为 `Actor`，则结构必须使用以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumActors` | 真值 actor 数量 |
| `Actors` | 真值 actor 结构数组 |

每个 actor 结构具有以下字段：

| 字段 | 定义 |
| --- | --- |
| `ActorID` | 用于区分 actor 的唯一标识符，指定为非负整数。 |
| `Position` | actor 的位置，指定为 *M* 元向量，其中 *M* 是位置状态的维数。例如，对于 3-D 位置，*M* = 3。 |
| `Velocity` | actor 的速度，指定为 *M* 元向量，其中 *M* 是速度状态的维数。例如，对于 3-D 速度，*M* = 3。 |

如果将 **Truth bus** 参数指定为 `custom`，则可以定义自己的真值总线格式。在这种情况下，必须使用 **Truth extractor function** 参数定义真值提取器函数。该函数必须使用以下语法：

     truths = truthExtractorFcn(truthInputFromBus)

其中 `truthInputFromBus` 是来自真值总线的输入，`truths` 必须返回为包含 `PlatformID`、`Position` 和 `Velocity` 字段的结构体数组。

### **Assignments** — 已知分配 *K*-by-2 非负整数矩阵

已知分配，指定为 *K*-by-2 非负整数矩阵。*K* 是分配对的数量。第一列元素是航迹 ID，第二列元素是真值 ID。同一行中的 ID 相互分配。如果某个航迹或真值未分配，请将同一行元素指定为 `0`。

分配必须是航迹与真值之间的唯一分配。冗余或虚假航迹应通过将其分配给 "0" `TruthID` 来视为未分配航迹。

#### 依赖项

要启用此端口，请在 **Port Setting** 选项卡上选择 **Assignments**。

### 输出

### **GOSPA Metric** — 包含切换误差分量的 GOSPA 度量，非负实数标量

包含切换误差分量的 GOSPA 度量，返回为非负实数标量。

### **GOSPA Metric Without Switching** — 不包含切换误差分量的 GOSPA 度量，非负实数标量

不包含切换误差分量的 GOSPA 度量，返回为非负实数标量。

**示例：** 8.5

#### 依赖项

要启用此端口，请在 **Port Setting** 选项卡上选择 **GOSPA metric without switching error component**。

### **Switching Error** — 切换误差分量，非负实数标量

切换误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖项

要启用此端口，请在 **Port Setting** 选项卡上选择 **Switching error**。

### **Localization Error** — 定位误差分量，非负实数标量

定位误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖项

要启用此端口，请在 **Port Setting** 选项卡上选择 **Localization error**。

### **Missed Target Error** — 漏检目标误差分量，非负实数标量

漏检目标误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖项

要启用此端口，请在 **Port Setting** 选项卡上选择 **Missed target error**。

### **False Track Error** — 虚假航迹误差分量，非负实数标量

虚假航迹误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖项

要启用此端口，请在 **Port Setting** 选项卡上选择 **False track error**。

## 参数

#### 属性

### **Cutoff distance** — 航迹与真值之间截断距离的阈值 `30` (default) | real positive scalar

航迹与真值之间截断距离的阈值，指定为正实数标量。如果航迹与所分配真值之间的计算距离高于该阈值，则度量中并入的实际距离会减小到该阈值。

**示例：** `40`

### **Order** — GOSPA 度量的阶数 `2` (default) | positive integer

GOSPA 度量的阶数，指定为正整数。

**示例：** `10`

### **Alpha** — GOSPA 度量的 Alpha 参数 `2` (default) | positive scalar in range [0, 2]

GOSPA 度量的 Alpha 参数，指定为范围 [0, 2] 内的正标量。

**示例：** `1`

### **Distance type** — 距离类型 `posnees` (default) | `velnees` | `posabserr` | `velabserr` | `custom`

距离类型，指定为 `posnees`、`velnees`、`posabserr` 或 `velabserr`。距离类型指定用于距离计算的物理量：

- `posnees` – 航迹位置的归一化估计误差平方 (NEES)
- `velnees` – 航迹速度的 NEES 误差
- `posabserr` – 航迹位置的绝对误差
- `velabserr` – 航迹速度的绝对误差
- `custom` – 自定义距离误差

如果将其指定为 `custom`，还必须在此 **Custom distance function** 参数中指定距离函数。

### **Custom distance function** — 自定义距离函数 function handle

自定义距离函数，指定为函数句柄。该函数必须支持以下语法：

    d = myCustomFcn(Track,Truth)

其中 `Track` 是航迹信息的结构体，`Truth` 是真值信息的结构体，`d` 是真值与航迹之间的距离。有关如何组织航迹信息的示例，请参见 `objectTrack`。

**示例：** `@myCustomFcn`

#### 依赖项

要启用此属性，请将 **Distance type** 参数设置为 `custom`。

### **Motion model** — 期望的平台运动模型 `constvel` (default) | `constacc` | `constturn` | `singer`

期望的平台运动模型，指定为 `constvel`、`constacc`、`constturn` 或 `singer`。此属性选择由 **Tracks** 输入端口使用的运动模型。

运动模型期望航迹结构的 `State` 字段具有包含以下值的列向量：

- `constvel` — 位置在元素 [1 3 5] 中，速度在元素 [2 4 6] 中。
- `constacc` — 位置在元素 [1 4 7] 中，速度在元素 [2 5 8] 中，加速度在元素 [3 6 9] 中。
- `constturn` — 位置在元素 [1 3 6] 中，速度在元素 [2 4 7] 中，偏航角速度在元素 5 中。
- `singer` — 位置在元素 [1 4 7] 中，速度在元素 [2 5 8] 中，加速度在元素 [3 6 9] 中。

航迹结构输入的 `StateCovariance` 字段必须在与航迹结构的 `State` 字段的位置、速度和转弯率对应的行和列中包含位置、速度和转弯率协方差。

### **Switching penalty** — 分配切换的惩罚 `0` (default) | nonnegative real scalar

分配切换的惩罚，指定为非负实数标量。

**示例：** `2`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code Generation`

从以下选项中选择仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不更改，后续仿真会重用该 C 代码。此选项需要额外的启动时间。

#### 端口设置

### **Assignments** — 启用分配输入 `off` (default) | `on`

选择此参数可通过 **Assignments** 输入端口启用已知分配输入。

### **GOSPA metric without switching error** — 启用不包含切换误差的 GOSPA 度量输出 `off` (default) | `on`

选择此参数可通过 **GOSPA Metric Without Switching** 输出端口启用不包含切换误差分量的 GOSPA 度量输出。

### **Switching error** — 启用切换误差分量输出 `off` (default) | `on`

选择此参数可通过 **Switching Error** 输出端口启用切换误差分量输出。

### **Localization error** — 启用定位误差分量输出 `off` (default) | `on`

选择此参数可通过 **Localization Error** 输出端口启用定位误差分量输出。

### **Missed target error** — 启用漏检目标误差分量输出 `off` (default) | `on`

选择此参数可通过 **Missed Target Error** 输出端口启用漏检目标误差分量输出。

### **False track error** — 启用虚假航迹误差分量输出 `off` (default) | `on`

选择此参数可通过 **False Track Error** 输出端口启用虚假航迹误差分量输出。

### **Track bus** — 航迹总线选择 `objectTrack` (default) | `custom`

航迹总线选择，指定为 `objectTrack` 或 `custom`。有关每个选择的更多详细信息，请参见 **Tracks** 输入端口的描述。

### **Truth bus** — 真值总线选择 `Platform` (default) | `Actor` | `custom`

真值总线选择，指定为 `Platform`、`Actor` 或 `custom`。有关每个选择的更多详细信息，请参见 **Truths** 输入端口的描述。

### **Track extractor function** — 航迹提取器函数 function handle

航迹提取器函数，指定为函数句柄。该函数必须支持以下语法：

    tracks = trackExtractorFcn(trackInputFromBus)

其中 `trackInputFromBus` 是来自航迹总线的输入，`tracks` 必须返回为包含 `TrackID` 和 `State` 字段的结构体数组。如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则结构体必须包含 `StateCovariance` 字段。

**示例：** `@myCustomFcn`

#### 依赖项

要启用此属性，请将 **Track bus** 参数设置为 `custom`。

### **Truth extractor function** — 真值提取器函数 function handle

真值提取器函数，指定为函数句柄。该函数必须支持以下语法：

     truths = truthExtractorFcn(truthInputFromBus)

其中 `truthInputFromBus` 是来自航迹总线的输入，`truths` 必须返回为包含 `PlatformID`、`Position` 和 `Velocity` 字段名的结构体数组。

**示例：** `@myCustomFcn`

#### 依赖项

要启用此属性，请将 **Truth bus** 参数设置为 `custom`。

## 所属库

Sensor Fusion and Tracking Toolbox / Track Metrics

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2023a：Simulink 总线不在工作区中显示

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

计算 Generalized Optimal Subpattern Assignment Metric

Generalized Optimal Subpattern Assignment Metric 模块通过计算航迹与已知真值之间的广义最优子模式分配（GOSPA）度量，评估跟踪算法的性能。该度量由切换误差、定位误差、漏检目标误差和虚假航迹误差分量组成。您还可以选择每个单独的误差分量作为模块输出。
