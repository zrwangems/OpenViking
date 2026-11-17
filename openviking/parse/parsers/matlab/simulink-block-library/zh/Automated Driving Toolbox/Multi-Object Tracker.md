---
type: simulink-block
title: 'Multi-Object Tracker'
family: 'automated-driving-toolbox'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Automated Driving Toolbox'
documentation_page: 'multiobjecttracker'
documentation_source_path: 'ref/multiobjecttracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Multi-Object Tracker

## 端口

### 输入

### **Detections** — 检测列表，包含 MATLAB® 结构的 Simulink 总线

检测列表，指定为包含 MATLAB 结构的 Simulink 总线。请参阅 Group Signals or Messages into Virtual Buses (Simulink)。该结构的形式如下：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | integer |
| `IsValidTime` | 当在模块调用间隔之间的时间请求更新时为 False | Boolean |
| `Detections` | 目标检测 | Array of object detection structures. The first `NumDetections` of these detections are actual detections. |

目标检测结构体的定义可在 Driving Radar Data Generator 和 Vision Detection Generator 模块的 **Detections** 输出端口描述中找到。

**注意**

目标检测结构体包含 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用时间。该时间标签还必须大于模块上一次调用中指定的更新时间。

### **Prediction Time** — 航迹更新时间 real scalar

航迹更新时间，指定为 real scalar。多目标跟踪器将所有航迹更新到此时间。每次调用模块时，更新时间必须始终增加。单位为 seconds。

**注意**

目标检测结构体包含 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用时间。该时间标签还必须大于模块上一次调用中的更新时间。

#### 依赖关系

要启用此端口，请将 **Prediction time source** 设置为 `Input port`。

### **Cost Matrix** — 成本矩阵 real-valued *N*t-by-*N*d matrix

成本矩阵，指定为 real-valued *N*t-by-*N*d matrix，其中 *N*t 是现有航迹数，*N*d 是当前检测数。

成本矩阵的行对应现有航迹。列对应检测。航迹按照它们在上一次调用模块时 **All Tracks** 输出端口的航迹列表中的出现顺序排列。

在对多目标跟踪器的第一次更新中，或者如果航迹没有先前的航迹，则将成本矩阵的大小指定为 [0, *N*d]。必须计算成本，使得较低的成本表示多目标跟踪器将检测分配给航迹的可能性更高。为防止某些检测被分配给某些航迹，请使用 `Inf`。

#### 依赖关系

要启用此端口，请选择 **Enable cost matrix input**。

### **Detectable Track IDs** — 可检测航迹 ID real-valued *M*-by-1 vector | real-valued *M*-by-2 matrix

可检测航迹 ID，指定为 real-valued *M*-by-1 vector 或 *M*-by-2 matrix。可检测航迹是传感器期望检测到的航迹。矩阵的第一列包含传感器报告为可检测的航迹 ID 列表。可选的第二列包含该航迹的检测概率。

标识符未包含在 **Detectable Track IDs** 中的航迹被视为不可检测。航迹删除逻辑不会因航迹删除目的而将未检测计为“漏检”。

如果未启用此端口，则跟踪器在每次调用模块时假定所有航迹均可检测。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable detectable track IDs Input**。

### **State Parameters** — 航迹状态参数，包含 MATLAB 结构的 Simulink 总线

航迹状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为 nonnegative integer |
| `Parameters` | 状态参数结构体数组 |

模块将 `Parameters` 字段的值用于所生成航迹的 `StateParameters` 字段。可以使用这些参数定义报告航迹时所用的参考帧，或所生成航迹的其他所需属性。

例如，可以使用以下结构定义一个矩形参考帧，其原点位置相对于场景帧为 `[10 10 0]` meters，原点速度相对于场景帧为 `[2 -2 0]` meters per second。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **Tracker Configuration** 选项卡中，选择 **Update track state parameters with time** 参数。

### 输出

### **Confirmed Tracks** — 确认航迹，包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

此表显示结构字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

此表显示每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为 seconds。 |
| `Age` | 航迹已更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数。值 `0` 表示未知分类。非零分类仅适用于确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1-by-*K* logical array。*K* 是记录的最新航迹逻辑状态数。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

如果满足以下条件，则航迹被确认：

- 在航迹初始化后的前 *N* 次更新期间，至少有 *M* 个检测分配给该航迹。要指定值 *M* 和 *N*，请使用 **M and N for the M-out-of-N confirmation** 参数。
- 启动该航迹的检测具有大于零的 `ObjectClassID`。

### **Tentative Tracks** — 试探航迹，包含 MATLAB 结构的 Simulink 总线

试探航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。航迹在被确认之前是试探航迹。

此表显示结构字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

此表显示每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为 seconds。 |
| `Age` | 航迹已更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数。值 `0` 表示未知分类。非零分类仅适用于确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1-by-*K* logical array。*K* 是记录的最新航迹逻辑状态数。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

#### 依赖关系

要启用此端口，请选择 **Enable tentative tracks output**。

### **All Tracks** — 所有航迹，包含 MATLAB 结构的 Simulink 总线

确认航迹和试探航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

此表显示结构字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

此表显示每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为 seconds。 |
| `Age` | 航迹已更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数。值 `0` 表示未知分类。非零分类仅适用于确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1-by-*K* logical array。*K* 是记录的最新航迹逻辑状态数。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

#### 依赖关系

要启用此端口，请选择 **Enable all tracks output**。

## 参数

### 跟踪器管理

### **Tracker identifier** — 唯一跟踪器标识符 `0`（默认）| nonnegative integer

唯一跟踪器标识符，指定为 nonnegative integer。此参数用作输出中的 `SourceIndex`，并在多跟踪器系统中区分来自不同跟踪器的航迹。必须将此属性指定为 positive integer，才能将航迹输出用作航迹融合器的输入。

**示例：** `1`

### **Filter initialization function name** — Kalman 滤波器初始化函数 `initcvkf`（默认）| function name

Kalman 滤波器初始化函数，指定为函数名。工具箱提供若干初始化函数。有关初始化函数的示例，请参阅 `initcvekf`。

### **Threshold for assigning detections to tracks** — 检测分配阈值 `30.0`（默认）| positive real scalar

检测分配阈值，指定为 positive real scalar。要将检测分配给航迹，检测到航迹的归一化距离必须小于分配阈值。如果某些检测仍未分配给希望分配的航迹，则增大阈值。如果某些检测被分配给错误的航迹，则减小阈值。

### **M and N for the M-out-of-N confirmation** — 用于创建航迹的确认参数 `[2,3]`（默认）| two-element vector of positive integers

用于创建航迹的确认参数，指定为 two-element vector of positive integers，`[M,N]`。当在航迹初始化后的前 `N` 次更新期间，至少有 `M` 个检测分配给该航迹时，该航迹被确认。`M` 必须小于或等于 `N`。

- 设置 `N` 时，请考虑希望跟踪器在确认航迹之前更新的次数。例如，如果跟踪器每 0.05 seconds 更新一次，并且允许 0.5 seconds 做出确认决定，则设置 `N` = 10。
- 设置 `M` 时，请考虑传感器的目标检测概率。检测概率取决于遮挡或杂波等因素。当航迹无法被确认时，可以减少 `M`；当过多虚假检测被分配给航迹时，可以增加 `M`。

**示例：** `[3,5]`

### **P and R for the P-out-of-R deletion** — 航迹删除阈值 `[5 5]`（默认）| real-valued 1-by-2 vector of positive integers

用于历史逻辑的航迹删除阈值，指定为 real-valued 1-by-2 vector of positive integers `[P R]`。如果确认航迹在最近 `R` 次跟踪器更新中未分配给任何检测 `P` 次，则该航迹被删除。

### **Maximum number of tracks** — 航迹最大数量 `200`（默认）| positive integer

模块可以处理的航迹最大数量，指定为 positive integer。

### **Maximum number of sensors** — 传感器最大数量 20（默认）| positive integer

模块可以处理的传感器最大数量，指定为 positive integer。此值应大于或等于 **Detections** 输入端口中所用的最高 `SensorIndex` 值。

### **Out-of-sequence measurements handling** — 乱序测量处理 `Terminate`（默认）| `neglect`

乱序测量处理，指定为 `Terminate` 或 `neglect`。每个检测都有一个与之关联的时间戳，*t*d，而跟踪器模块有自己的时间戳，*t*t，该时间戳在每次调用时更新。如果 *t*d < *t*t，则跟踪器模块将测量视为 OOSM。

当参数指定为：

- `Terminate` — 当遇到任何乱序测量时，模块停止运行。
- `Neglect` — 模块忽略任何乱序测量并继续运行。

### **Track state parameters** — 航迹状态参考帧的参数 structure | structure array

将航迹状态参考帧的参数指定为 structure 或 structure array。模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。可以使用这些参数定义报告航迹时所用的参考帧，或所生成航迹的其他所需属性。

例如，可以使用以下结构定义一个矩形参考帧，其原点位置相对于场景帧为 `[10 10 0]` meters，原点速度相对于场景帧为 `[2 -2 0]` meters per second。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

可以通过选择 **Update track state parameters with time** 参数，通过 **State Parameters** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **Update track state parameters with time** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数以通过 **State Parameters** 输入端口启用航迹状态参数输入端口。

### 输入和输出

### **Prediction time source** — 预测时间的来源 `Input port`（默认）| `Auto`

预测时间的来源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

**示例：** `Auto`

### **Enable cost matrix input** — 启用成本矩阵输入端口 `off`（默认）| `on`

选中此复选框以通过 **Cost Matrix** 输入端口启用成本矩阵输入。

### **Enable detectable track IDs input** — 启用可检测航迹 ID 输入 `off`（默认）| `on`

选中此复选框以启用 **Detectable Track IDs** 输入端口。

### **Source of output bus name** — 输出总线名称的来源 `Auto`（默认）| `Property`

输出总线名称的来源，指定为 `Auto` 或 `Property`。

- 如果选择 `Auto`，模块会自动创建总线名称。
- 如果选择 `Property`，请使用 **Specify an output bus name** 参数指定总线名称。

### **Specify an output bus name** — 输出总线名称 无默认值

#### 依赖关系

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

### **Enable tentative tracks output** — 启用试探航迹输出端口 `off`（默认）| `on`

选中此复选框以通过 **Tentative Tracks** 输出端口启用试探航迹输出。

### **Enable all tracks output** — 启用所有航迹输出端口 `off`（默认）| `on`

选中此复选框以通过 **All Tracks** 输出端口启用所有航迹输出。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不变，C 代码会复用于后续仿真。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 当模块中指定的滤波器初始化函数返回 `trackingEKF` 或 `trackingUKF` (Sensor Fusion and Tracking Toolbox) 对象时，模块支持静态内存分配代码生成。
- 在代码生成中，如果检测输入以 `double` 精度指定，则航迹输出的 `NumTracks` 字段返回为 `double` 变量。如果检测输入以 `single` 精度指定，则航迹输出的 `NumTracks` 字段返回为 `uint32` 变量。

## 版本历史

**在 R2017b 中引入**

## 描述

创建并管理多个目标的航迹

Multi-Object Tracker 模块初始化、确认、预测、校正和删除移动目标的航迹。多目标跟踪器的输入是由 Driving Radar Data Generator 和 Vision Detection Generator 模块生成的检测报告。多目标跟踪器接受来自多个传感器的检测，并使用全局最近邻 (GNN) 准则将它们分配给航迹。每个检测被分配给一个单独的航迹。如果检测无法分配给任何航迹，则多目标跟踪器会创建新航迹。

新航迹以 *试探* 状态开始。如果有足够的检测分配给试探航迹，其状态将变为 *确认*。当航迹被确认时，多目标跟踪器认为该航迹表示一个物理目标。如果在可指定次数的更新内没有向航迹添加检测，则该航迹被删除。

多目标跟踪器还使用 Kalman 滤波器估计每个航迹的状态向量和状态向量协方差矩阵。这些状态向量用于预测每个帧中航迹的位置，并确定每个检测被分配给每个航迹的可能性。
