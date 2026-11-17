---
type: simulink-block
title: 'Multi-Object Tracker'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'multiobjecttracker'
documentation_source_path: 'ref/multiobjecttracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Multi-Object Tracker

## 端口

### 输入

### **Detections** — 包含 MATLAB® 结构的检测列表 Simulink 总线

检测列表，指定为包含 MATLAB 结构的 Simulink 总线。请参阅 Group Signals or Messages into Virtual Buses (Simulink)。该结构的形式为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | 整数 |
| `IsValidTime` | 当在模块调用间隔之间的时刻请求更新时为 False | 布尔值 |
| `Detections` | 目标检测 | 目标检测结构体数组。这些检测中的前 `NumDetections` 个为实际检测。 |

目标检测结构体的定义可在 Driving Radar Data Generator 和 Vision Detection Generator 模块的 **Detections** 输出端口描述中找到。

**注意**

目标检测结构体包含一个 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用的时间。该时间标签还必须大于模块上一次调用中指定的更新时间。

### **Prediction Time** — 航迹更新时间 实数标量

航迹更新时间，指定为实数标量。多目标跟踪器将所有航迹更新到此时间。每次调用模块时，更新时间必须始终递增。单位为秒。

**注意**

目标检测结构体包含一个 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用的时间。该时间标签还必须大于模块上一次调用中的更新时间。

#### 依赖关系

要启用此端口，请将 **Prediction time source** 设置为 `Input port`。

### **Cost Matrix** — 代价矩阵 实值 *N*t×*N*d 矩阵

代价矩阵，指定为实值 *N*t×*N*d 矩阵，其中 *N*t 是现有航迹的数量，*N*d 是当前检测的数量。

代价矩阵的行对应现有航迹。列对应检测。航迹的排列顺序与模块上一次调用时 **All Tracks** 输出端口中航迹列表中的顺序相同。

在多目标跟踪器的首次更新时，或者如果航迹没有先前的航迹，则将代价矩阵的大小指定为 [0, *N*d]。代价的计算方式必须使得较低的代价表示多目标跟踪器将检测分配给航迹的可能性更高。要阻止某些检测被分配给某些航迹，请使用 `Inf`。

#### 依赖关系

要启用此端口，请选中 **Enable cost matrix input**。

### **Detectable Track IDs** — 可检测航迹 ID 实值 *M*×1 向量 | 实值 *M*×2 矩阵

可检测航迹 ID，指定为实值 *M*×1 向量或 *M*×2 矩阵。可检测航迹是传感器期望检测到的航迹。矩阵的第一列包含传感器报告为可检测的航迹 ID 列表。可选的第二列包含航迹的检测概率。

标识符未包含在 **Detectable Track IDs** 中的航迹被视为不可检测。航迹删除逻辑不会将未检测到计为航迹删除目的中的“漏检”。

如果未启用此端口，则跟踪器在每次调用模块时假定所有航迹都是可检测的。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中选中 **Enable detectable track IDs Input**。

### **State Parameters** — 航迹状态参数 包含 MATLAB 结构的 Simulink 总线

航迹状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构体数组 |

模块将 `Parameters` 字段的值用于所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹报告的参考坐标系，或所生成航迹的其他期望属性。

例如，您可以使用以下结构来定义一个矩形参考坐标系，其原点位置在 `[10 10 0]` 米处，原点速度相对于场景坐标系为 `[2 -2 0]` 米每秒。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **Tracker Configuration** 选项卡中选中 **Update track state parameters with time** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

下表显示了结构体字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

下表显示了每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为秒。 |
| `Age` | 航迹更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1×*K* 逻辑数组。*K* 是记录的最新航迹逻辑状态的数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回为 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

航迹在以下情况下被确认：

- 在航迹初始化后的前 *N* 次更新中，至少有 *M* 个检测被分配给该航迹。要指定 *M* 和 *N* 的值，请使用 **M and N for the M-out-of-N confirmation** 参数。
- 启动该航迹的检测的 `ObjectClassID` 大于零。

### **Tentative Tracks** — 暂定航迹 包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。航迹在被确认之前为暂定航迹。

下表显示了结构体字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

下表显示了每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为秒。 |
| `Age` | 航迹更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1×*K* 逻辑数组。*K* 是记录的最新航迹逻辑状态的数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回为 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

#### 依赖关系

要启用此端口，请选中 **Enable tentative tracks output**。

### **All Tracks** — 所有航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。请参阅 Create Nonvirtual Buses (Simulink)。

下表显示了结构体字段。

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

下表显示了每个航迹结构体的字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符。 |
| `BranchID` | 用于区分多个航迹分支的唯一航迹分支标识符。 |
| `SourceIndex` | 用于在多跟踪器环境中区分跟踪源的唯一源索引。 |
| `UpdateTime` | 航迹更新的时间。单位为秒。 |
| `Age` | 航迹更新的次数。 |
| `State` | 更新时刻的状态向量值。 |
| `StateCovariance` | 不确定性协方差矩阵。 |
| `ObjectClassID` | 表示目标分类的整数值。值 `0` 表示未知分类。非零分类仅适用于确认航迹。 |
| `TrackLogic` | 确认和删除逻辑类型。对于雷达传感器，此值始终为 `'History'`，表示基于历史的逻辑。 |
| `TrackLogicState` | 航迹逻辑类型的当前状态，返回为 1×*K* 逻辑数组。*K* 是记录的最新航迹逻辑状态的数量。在数组中，`1` 表示命中，`0` 表示未命中。 |
| `IsConfirmed` | 确认状态。如果航迹被确认为真实目标，则此字段为 `true`。 |
| `IsCoasted` | 滑行状态。如果航迹在没有新检测的情况下更新，则此字段为 `true`。 |
| `IsSelfReported` | 指示航迹是否由跟踪器报告。此字段用于航迹融合环境。默认返回为 `true`。 |
| `ObjectAttributes` | 关于航迹的附加信息。 |

有关这些字段的更多详细信息，请参阅 `objectTrack`。

#### 依赖关系

要启用此端口，请选中 **Enable all tracks output**。

## 参数

### 跟踪器管理

### **Tracker identifier** — 唯一跟踪器标识符 `0`（默认）| 非负整数

唯一跟踪器标识符，指定为非负整数。此参数用作输出中的 `SourceIndex`，用于在多跟踪器系统中区分来自不同跟踪器的航迹。您必须将此属性指定为正整数，才能将航迹输出用作航迹融合器的输入。

**示例：** `1`

### **Filter initialization function name** — 卡尔曼滤波器初始化函数 `initcvkf`（默认）| 函数名

卡尔曼滤波器初始化函数，指定为函数名。工具箱提供了多个初始化函数。有关初始化函数的示例，请参阅 `initcvekf`。

### **Threshold for assigning detections to tracks** — 检测分配阈值 `30.0`（默认）| 正实数标量

检测分配阈值，指定为正实数标量。要将检测分配给航迹，检测到航迹的归一化距离必须小于分配阈值。如果某些检测仍未分配给希望分配的航迹，则增大阈值。如果某些检测被分配给错误的航迹，则减小阈值。

### **M and N for the M-out-of-N confirmation** — 航迹创建的确认参数 `[2,3]`（默认）| 正整数二元向量

航迹创建的确认参数，指定为正整数二元向量 `[M,N]`。当在航迹初始化后的前 `N` 次更新中至少有 `M` 个检测被分配给该航迹时，该航迹被确认。`M` 必须小于或等于 `N`。

- 设置 `N` 时，请考虑您希望跟踪器在确认航迹之前更新的次数。例如，如果跟踪器每 0.05 秒更新一次，并且您允许 0.5 秒来做出确认决策，则设置 `N` = 10。
- 设置 `M` 时，请考虑传感器的目标检测概率。检测概率取决于遮挡或杂波等因素。当航迹未能被确认时，您可以减小 `M`；当过多虚假检测被分配给航迹时，您可以增大 `M`。

**示例：** `[3,5]`

### **P and R for the P-out-of-R deletion** — 航迹删除阈值 `[5 5]`（默认）| 实值 1×2 正整数向量

历史逻辑的航迹删除阈值，指定为实值 1×2 正整数向量 `[P R]`。如果确认航迹在最近 `R` 次跟踪器更新中有 `P` 次未分配给任何检测，则该航迹被删除。

### **Maximum number of tracks** — 最大航迹数量 `200`（默认）| 正整数

模块可以处理的最大航迹数量，指定为正整数。

### **Maximum number of sensors** — 最大传感器数量 20（默认）| 正整数

模块可以处理的最大传感器数量，指定为正整数。此值应大于或等于 **Detections** 输入端口中所用的最高 `SensorIndex` 值。

### **Out-of-sequence measurements handling** — 乱序测量处理 `Terminate`（默认）| `neglect`

乱序测量处理，指定为 `Terminate` 或 `neglect`。每个检测都有一个关联的时间戳 *t*d，跟踪器模块有自己的时间戳 *t*t，该时间戳在每次调用时更新。如果 *t*d < *t*t，跟踪器模块将测量视为 OOSM。

当该参数指定为：

- `Terminate` — 当模块遇到任何乱序测量时停止运行。
- `Neglect` — 模块忽略任何乱序测量并继续运行。

### **Track state parameters** — 航迹状态参考坐标系结构的参数 | 结构体数组

将航迹状态参考坐标系的参数指定为结构体或结构体数组。该模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹上报时所处的参考坐标系，或所生成航迹的其他所需属性。

例如，您可以使用以下结构体定义一个矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

您可以通过选择 **Update track state parameters with time** 参数，经由 **State Parameters** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **Update track state parameters with time** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数以启用通过 **State Parameters** 输入端口输入航迹状态参数。

### 输入和输出

### **Prediction time source** — 预测时间来源 `Input port`（默认）| `Auto`

预测时间来源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟决定更新时间。

**示例：** `Auto`

### **Enable cost matrix input** — 启用代价矩阵输入端口 `off`（默认）| `on`

选中此复选框以启用通过 **Cost Matrix** 输入端口输入代价矩阵。

### **Enable detectable track IDs input** — 启用可检测航迹 ID 输入 `off`（默认）| `on`

选中此复选框以启用 **Detectable Track IDs** 输入端口。

### **Source of output bus name** — 输出总线名称来源 `Auto`（默认）| `Property`

输出总线名称来源，指定为 `Auto` 或 `Property`。

- 如果选择 `Auto`，模块会自动创建总线名称。
- 如果选择 `Property`，请使用 **Specify an output bus name** 参数指定总线名称。

### **Specify an output bus name** — 输出总线名称 无默认值

#### 依赖关系

要启用此参数，请将 **Source of output bus name** 参数设置为 `Property`。

### **Enable tentative tracks output** — 启用暂定航迹输出端口 `off`（默认）| `on`

选中此复选框以启用通过 **Tentative Tracks** 输出端口输出暂定航迹。

### **Enable all tracks output** — 启用所有航迹输出端口 `off`（默认）| `on`

选中此复选框以启用通过 **All Tracks** 输出端口输出所有航迹。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C/C++ 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C/C++ 代码。只要模型不变，C 代码将在后续仿真中复用。此选项需要额外的启动时间。

## 所属库

Automated Driving Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 当模块中指定的滤波器初始化函数返回 `trackingEKF` 或 `trackingUKF`（Sensor Fusion and Tracking Toolbox）对象时，该模块支持静态内存分配代码生成。
- 在代码生成中，如果检测输入以 `double` 精度指定，则航迹输出的 `NumTracks` 字段以 `double` 变量返回。如果检测输入以 `single` 精度指定，则航迹输出的 `NumTracks` 字段以 `uint32` 变量返回。

## 版本历史

**在 R2017b 中引入**

## 描述

创建并管理多个对象的航迹

Multi-Object Tracker 模块对运动对象的航迹进行初始化、确认、预测、校正和删除。多对象跟踪器的输入是由 Driving Radar Data Generator 和 Vision Detection Generator 模块生成的检测报告。多对象跟踪器接受来自多个传感器的检测，并使用全局最近邻（GNN）准则将其分配给航迹。每个检测被分配给一条单独的航迹。如果检测无法分配给任何航迹，多对象跟踪器将创建一条新航迹。

新航迹以*暂定*状态开始。如果有足够的检测分配给暂定航迹，其状态将变为*已确认*。当航迹被确认后，多对象跟踪器认为该航迹代表一个物理对象。如果在可指定次数的更新内没有检测添加到该航迹，则该航迹将被删除。

多对象跟踪器还使用卡尔曼滤波器估计每条航迹的状态向量和状态向量协方差矩阵。这些状态向量用于预测航迹在每一帧中的位置，并确定每个检测分配给每条航迹的可能性。
