---
type: simulink-block
title: 'Joint Probabilistic Data Association Multi Object Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'jointprobabilisticdataassociationmultiobjecttracker'
documentation_source_path: 'ref/jointprobabilisticdataassociationmultiobjecttracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Joint Probabilistic Data Association Multi Object Tracker

## 端口

### 输入

### **Detections** — 检测列表 包含 MATLAB® 结构的 Simulink® 总线

检测列表，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | 整数 |
| `Detections` | 目标检测 | `objectDetection` 结构体数组。这些检测中的前 `NumDetections` 个为实际检测。 |

检测的字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 测量时间 | `Single` 或 `Double` |
| `Measurement` | 目标测量值 | `Single` 或 `Double` |
| `MeasurementNoise` | 测量噪声协方差矩阵 | `Single` 或 `Double` |
| `SensorIndex` | 传感器的唯一 ID | `Single` 或 `Double` |
| `ObjectClassID` | 目标分类 ID | `Single` 或 `Double` |
| `MeasurementParameters` | 跟踪滤波器初始化函数使用的参数 | Simulink 总线 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 | Simulink 总线 |

有关这些字段的更详细说明，请参阅 `objectDetection`。

**注意**

目标检测结构包含一个 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用时刻的时间。该时间标签还必须大于模块上一次调用时指定的更新时间。

### **Prediction Time** — 航迹更新时间 实数标量

航迹更新时间，指定为以秒为单位的实数标量。跟踪器将所有航迹更新到该时间。每次调用模块时，更新时间必须始终递增。更新时间必须至少与 **Detections** 输入端口指定的最大 `Time` 一样大。

如果该端口未启用，则由 Simulink 管理的仿真时钟决定更新时间。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上，将 **Prediction time source** 设置为 `Input port`。

### **Cost Matrix** — 代价矩阵 实值 *N*t×*N*d 矩阵

代价矩阵，指定为实值 *N*t×*N*d 矩阵，其中 *N*t 是现有航迹的数量，*N*d 是当前检测的数量。

代价矩阵的行对应现有航迹。列对应检测。航迹的排序与模块上一次调用时 **All Tracks** 输出端口输出的航迹列表中的顺序一致。

在跟踪器的首次更新时，或者如果跟踪器没有先前的航迹，则将代价矩阵的大小指定为 [0, *N*d]。代价的计算方式必须使得较低的代价表示跟踪器将检测分配给航迹的可能性更高。要阻止某些检测被分配给某些航迹，请使用 `Inf`。

如果该端口未启用，则由 **Filter initialization function** 初始化的滤波器使用距离方法计算代价矩阵。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上，选中 **Enable cost matrix input**。

### **Detectable TrackIDs** — 可检测航迹 ID 实值 *M*×1 向量 | 实值 *M*×2 矩阵

可检测航迹 ID，指定为实值 *M*×1 向量或 *M*×2 矩阵。可检测航迹是传感器期望检测到的航迹。矩阵的第一列包含传感器报告为可检测的航迹 ID 列表。可选的第二列使您能够为每个航迹添加检测概率。

标识符未包含在 **Detectable TrackIDs** 中的航迹被视为不可检测。航迹删除逻辑不会将未检测到的情况计为航迹删除目的中的“漏检”。

如果该端口未启用，则跟踪器在每次调用模块时假定所有航迹都是可检测的。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上，选中 **Enable detectable track IDs Input**。

### **State Parameters** — 跟踪状态参数 包含 MATLAB 结构的 Simulink 总线

跟踪状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构体数组 |

该模块使用 `Parameters` 字段的值作为所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹上报的参考坐标系或所生成航迹的其他所需属性。

例如，您可以使用以下结构来定义一个矩形参考坐标系，其原点位置为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒（相对于场景坐标系）。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **Tracker Configuration** 选项卡中，选择 **Update track state parameters with time** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如航迹结构所示。

根据航迹逻辑，航迹在以下情况下被确认：

- History – 航迹在最近 `N` 次更新中至少收到 `M` 次检测。`M` 和 `N` 在 `History` 逻辑的 **Confirmation threshold** 中指定。
- Integrated – 航迹存在的积分概率高于 `Integrated` 逻辑的 **Confirmation threshold** 中指定的确认阈值。

### **Tentative Tracks** — 暂定航迹 包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在被确认之前为暂定航迹。

航迹结构的字段如航迹结构所示。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable tentative tracks output**。

### **All Tracks** — 确认和暂定航迹 包含 MATLAB 结构的 Simulink 总线

确认和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。

航迹结构的字段如航迹结构所示。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable all tracks output**。

### **Info** — 用于分析航迹更新的附加信息 Simulink 总线，包含 MATLAB 结构体

用于分析航迹更新的附加信息，以包含 MATLAB 结构体的 Simulink 总线形式返回。

下表显示了 info 结构体的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `OOSMDetectionIndices` | 跟踪器当前步中乱序量测的索引 |
| `TrackIDsAtStepBeginning` | 步开始时的航迹 ID。 |
| `CostMatrix` | 运动学分配矩阵的代价，其中 (*i*, *j*) 元素表示将航迹 *i* 分配给检测 *j* 的代价。 |
| `Clusters` | 聚类报告的元胞数组。有关更多详细信息，请参阅 Feasible Joint Events。 |
| `InitiatedTrackIDs` | 在该步中起始的航迹 ID。 |
| `DeletedTrackIDs` | 在该步中删除的航迹 ID。 |
| `TrackIDsAtStepEnd` | 步结束时的航迹 ID。 |
| `MaxNumDetectionsPerCluster` | 在该步中生成的所有聚类中检测的最大数量。仅当您将 **Enable memory management** 参数设置为 `on` 时，该结构体才具有此字段。 |
| `MaxNumTracksPerCluster` | 在该步中生成的所有聚类中航迹的最大数量。仅当您将 **Enable memory management** 参数设置为 `on` 时，该结构体才具有此字段。 |
| `OOSMHandling` | 乱序量测处理的分析信息，以结构体形式返回。仅当 `Out-of-sequence measurement handling` 参数指定为 `Retordiction` 时，该结构体才具有此字段。 |

`Clusters` 字段可以包含多个聚类报告。每个聚类报告是一个结构体，包含：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `DetectionIndices` | 聚类检测的索引。 |
| `TrackIDs` | 聚类航迹的航迹 ID。 |
| `ValidationMatrix` | 聚类的确认矩阵。有关更多详细信息，请参阅 Feasible Joint Events。 |
| `SensorIndex` | 聚类检测的源传感器索引。 |
| `TimeStamp` | 聚类检测的平均时间戳。 |
| `MarginalProbabilities` | 边缘后验联合关联概率矩阵。 |

`OOSMHandling` 结构体包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `DiscardedDetections` | 被丢弃的乱序检测的索引。如果某个 OOSM 未被 **Maximum number of OOSM steps** 参数指定的已保存状态历史所覆盖，则该 OOSM 被丢弃。 |
| `CostMatrix` | 乱序检测的分配矩阵的代价。 |
| `Clusters` | 仅与乱序检测相关的聚类。 |
| `UnassignedDetections` | 未分配的乱序检测的索引。跟踪器为未分配的乱序检测创建新航迹。 |

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上，选择 **Enable information output**。

## 参数

#### Tracker Management

### **Tracker identifier** — 唯一跟踪器标识符 `0`（默认）| 非负整数

将唯一跟踪器标识符指定为非负整数。此参数作为跟踪器输出中的 `SourceIndex` 传递，并在多跟踪器系统中区分来自不同跟踪器的航迹。您必须将此属性指定为正整数，才能将航迹输出用作 Track-To-Track Fuser 模块的输入。

**Example:** `1`

### **滤波器初始化函数** — 滤波器初始化函数 `initcvekf`（默认）| 函数名

滤波器初始化函数，指定为有效滤波器初始化函数的函数名。跟踪器在创建新航迹时使用该滤波器初始化函数。

Sensor Fusion and Tracking Toolbox™ 提供了许多初始化函数：

| 初始化函数 | 函数定义 |
| --- | --- |
| `initcvkf` | 初始化匀速线性卡尔曼滤波器。 |
| `initcakf` | 初始化匀加速线性卡尔曼滤波器。 |
| `initcvabf` | 初始化匀速 alpha-beta 滤波器 |
| `initcaabf` | 初始化匀加速 alpha-beta 滤波器 |
| `initcvekf` | 初始化匀速扩展卡尔曼滤波器。 |
| `initcaekf` | 初始化匀加速扩展卡尔曼滤波器。 |
| `initrpekf` | 初始化匀速距离参数化扩展卡尔曼滤波器。 |
| `initapekf` | 初始化匀速角度参数化扩展卡尔曼滤波器。 |
| `initctekf` | 初始化匀转弯速率扩展卡尔曼滤波器。 |
| `initcackf` | 初始化匀加速容积滤波器。 |
| `initctckf` | 初始化匀转弯速率容积滤波器。 |
| `initcvckf` | 初始化匀速容积滤波器。 |
| `initcvukf` | 初始化匀速无迹卡尔曼滤波器。 |
| `initcaukf` | 初始化匀加速无迹卡尔曼滤波器。 |
| `initctukf` | 初始化匀转弯速率无迹卡尔曼滤波器。 |
| `initcvmscekf` | 在修正球坐标系中初始化匀速扩展卡尔曼滤波器。 |
| `initekfimm` | 初始化跟踪 IMM 滤波器。 |

您也可以使用以下语法编写自己的初始化函数：

```
filter = filterInitializationFcn(detection)
```

该函数的输入是由 `objectDetection` 创建的检测报告。该函数的输出必须是滤波器对象：`trackingKF`、`trackingEKF`、`trackingUKF`、`trackingCKF`、`trackingGSF`、`trackingIMM`、`trackingMSCEKF` 或 `trackingABF`。

有关编写此函数的指导，请使用 `type` 命令查看内置 MATLAB 函数的详细信息。例如：

```
type initcvekf
```

**注意**

该模块不接受 Sensor Fusion and Tracking Toolbox 中的所有滤波器初始化函数。Sensor Fusion and Tracking Toolbox 中可用的滤波器初始化函数的完整列表在 Estimation Filters 的 **Initialization** 部分中给出。

### **k-best JPDA 的 k 值** — k-best JPDA 的 k 值 `inf`（默认）| 正整数

k-best JPDA 的 k 值，指定为正整数。此参数定义每个聚类的航迹与检测关联的最大可行联合事件数。将此属性设置为有限值使您能够运行 k-best JPDA 跟踪器，该跟踪器每个聚类最多生成 k 个事件。

### **可行联合事件生成函数名** — 可行联合事件生成函数名 `jpdaEvents`（默认）| 函数名

可行联合事件生成函数名，指定为可行联合事件生成函数的名称。生成函数从航迹与检测之间的关联似然矩阵生成可行联合事件矩阵。有关详细信息，请参阅 `jpdaEvents`

要编写自己的生成函数，必须使用此语法。

```
[FJE,FJEProbs] = myfunction(likelihoodMatrix,k)
```

此函数的输入和输出参数必须与 `jpdaEvents` 中的参数相同。

您可以使用 `type` 命令查看 `jpdaEvents` 的详细信息。

```
type jpdaEvents
```

**示例：**
`myfunction`

### **最大航迹数** — 最大航迹数 `100`（默认）| 正整数

该模块可以维护的最大航迹数，指定为正整数。

### **Maximum number of sensors** — 最大传感器数量 `20`（默认）| 正整数

该模块可处理的最大传感器数量，指定为正整数。该值应大于或等于在 **Detections** 输入端口输入的最高 `SensorIndex` 值。

### **Absolute tolerance between time stamps of detections** — 检测时间戳之间的绝对容差 `20`（默认）| 正整数

同一传感器的检测之间的绝对时间容差，指定为正标量。该模块期望来自一个传感器的检测具有相同的时间戳。但是，如果某个传感器的检测之间的时间戳差异在此参数指定的容差范围内，则将基于这些检测的平均时间使用这些检测来更新航迹估计。

### **Out-of-sequence measurements handling** — 乱序测量处理 `Terminate`（默认）| `Neglect` | `Retrodiction`

乱序测量处理，指定为 `Terminate`、`Neglect` 或 `Retrodiction`。每个检测都有一个关联的时间戳 *t*d，而跟踪器模块有自己的时间戳 *t*t，该时间戳在每次调用时更新。如果 *t*d < *t*t，跟踪器模块将该测量视为 OOSM。

当您将该参数指定为：

- `Terminate` — 当遇到乱序测量时，该模块停止运行。
- `Neglect` — 该模块忽略任何乱序测量并继续运行。
- `Retrodiction` — 该模块使用反推算法来更新跟踪器，方式是忽略 OOSM、更新现有航迹，或使用 OOSM 创建新航迹。您必须在 **Filter initialization function** 参数中指定一个返回 `trackingKF`、`trackingEKF` 或 `trackingIMM` 对象的滤波器初始化函数。

如果您将该参数指定为 `Retrodiction`，跟踪器将按照以下步骤处理 OOSM：

- 如果 OOSM 时间戳超出跟踪器中维护的最旧校正时间戳（由 **Maximum number of OOSM steps** 参数指定），则跟踪器丢弃这些 OOSM。
- 如果 OOSM 时间戳在跟踪器维护的最旧校正时间戳范围内，则跟踪器首先将所有现有航迹反推到这些 OOSM 的时间。然后，跟踪器应用联合概率数据关联算法，尝试将这些 OOSM 与反推后的航迹关联起来。

  - 如果跟踪器成功将 OOSM 与至少一条反推后的航迹关联起来，则跟踪器使用这些 OOSM 更新反推后的航迹，方法是应用反校正算法以获得当前的校正航迹。
  - 如果跟踪器无法将某个 OOSM 与任何反推后的航迹关联起来，则跟踪器基于该 OOSM 创建一条新航迹，并将该航迹预测到当前时间。

有关基于 JPDA 的反推的更多详细信息，请参阅 JPDA-Based Retrodiction and Retro-Correction。要模拟乱序检测，请使用 `objectDetectionDelay`。

**注意**

- 当您选择 `Retrodiction` 时，不能使用 Cost Matrix 输入。
- 随着近距离移动的目标数量增加，使用反推带来的收益会降低。
- 跟踪器要求所有共享相同 `SensorIndex` 的输入检测，其 `Time` 差异都受 **Absolute tolerance between time stamps of detections** 参数约束。因此，当您将 **Out-of-sequence measurements handling** 参数设置为 `Neglect` 时，必须确保在运行跟踪器时，乱序检测的时间戳严格小于前一时间戳。

### **Maximum number of OOSM steps** — 最大 OOSM 步数 `3`（默认）| 正整数

最大乱序量测（OOSM）步数，指定为正整数。

增大此参数的值需要更多内存，但允许您使用相对于模块上次更新时的时间戳具有更大滞后的 OOSM 调用跟踪器模块。此外，随着滞后增大，OOSM 对航迹当前状态的影响会减弱。此参数的推荐值为 `3`。

#### 依赖关系

要启用此参数，请将 **Out-of-sequence measurements handling** 参数设置为 `Retrodiction`。

### **Track state parameters** — 航迹状态参考坐标系参数 结构体 | 结构体数组

将航迹状态参考坐标系的参数指定为结构体或结构体数组。模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹报告所在的参考坐标系，或所生成航迹的其他所需属性。

例如，您可以使用以下结构体定义一个矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒。

| Field Name | Value |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

您可以通过选择 **Update track state parameters with time** 参数，经由 **State Parameters** 输入端口更新航迹状态参数。

**Data Types:** `struct`

### **Update track state parameters with time** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数以启用通过 **State Parameters** 输入端口输入航迹状态参数的输入端口。

### **Enable memory management** — 启用内存管理 `off`（默认）| `on`

选择此参数以在跟踪器中启用内存管理。选择后，您可以使用 **Memory Management** 选项卡中的以下四个参数来指定跟踪器中某些可变大小数组的边界，并确定跟踪器如何处理簇大小违规：

- **Maximum number of detections per sensor**
- **Maximum number of detections per cluster**
- **Maximum number of tracks per cluster**
- **Handle run-time violation of cluster size**

为可变大小数组指定边界允许您在生成的 C/C++ 代码中管理跟踪器的内存占用。

### **Simulate using** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将复用该 C 代码。此选项需要额外的启动时间。

#### Assignment

### **用于将检测分配给航迹的阈值** — 用于将检测分配给航迹的阈值 `30*[1 Inf]`（默认）| 正标量 | 1×2 正值向量

用于将检测分配给航迹的阈值（或门限阈值），指定为正标量或 1×2 向量
[*C*1*,C*2]，
其中 *C*1 ≤
*C*2。如果指定为标量，则指定的
值 *val* 会扩展为 [*val*,
`Inf`]。

最初，跟踪器对所有航迹与检测之间的归一化距离执行粗略估计。跟踪器仅对粗略归一化距离小于
*C*2 的组合计算精确的
归一化距离。此外，只有当检测与航迹之间的精确归一化距离小于
*C*1 时，跟踪器才能将检测分配给航迹。有关归一化距离的说明，请参见算法。

- 如果存在应计算用于分配但未计算的航迹与检测组合，则增大 *C*2 的值。
  如果代价计算耗时过长，则减小该值。
- 如果存在应分配给航迹但未分配的检测，则增大 *C*1 的值。
  如果存在被分配到不应分配给它们的航迹（距离过远）的检测，则减小该值。

**注意**

如果 *C*2 的值是有限值，则跟踪器中使用的跟踪滤波器所指定的状态
转移函数和测量函数必须能够分别接受 *M*×*N*
状态矩阵作为输入，并输出 *N* 个预测状态和
*N* 个测量。*M* 是状态的大小。*N*（状态数量）是任意非负
整数。

### **用于初始化航迹的阈值** — 用于初始化航迹的阈值 `0`（默认）| 范围 [0, 1] 内的标量

用于初始化新航迹的概率阈值，指定为范围 [0, 1] 内的标量。如果
将检测与任何现有航迹关联的概率都小于 `InitializationThreshold`，则将该检测
用于初始化新航迹。这允许位于航迹确认门限内但关联概率低于初始化
阈值的检测生成新航迹。

**示例：** `0.1`

### **检测概率** — 检测概率 `0.9`（默认）| 范围 [0, 1] 内的标量

检测概率，指定为范围 [0, 1] 内的标量。此属性
用于在初始化和更新航迹时计算关联的边缘后验概率以及
航迹存在概率。

### **杂波测量的空间密度** — 杂波测量的空间密度 `1e-5`（默认）| 正标量

杂波测量的空间密度，指定为正标量。杂波
密度描述每单位体积中预期出现的假阳性检测数量。它
用作泊松杂波模型的参数。当 **航迹确认和删除逻辑类型** 设置为
`'Integrated'` 时，此参数也用于计算
航迹存在的初始概率。

#### 航迹逻辑

### **航迹确认和删除逻辑类型** — 确认和删除逻辑类型 `History`（默认）| `Integrated`

确认和删除逻辑类型，选择为：

- `History` – 航迹确认和删除基于
  在最近的跟踪器更新中航迹被分配给检测的次数。
- `Integrated` – 航迹确认和删除基于
  航迹存在概率，该概率在分配
  函数中进行积分。

### **确认阈值 [M N]** — 历史逻辑的航迹确认阈值 `[2, 3]`（默认）| 正整数的实值 1×2 向量

历史逻辑的航迹确认阈值，指定为正整数的实值 1×2
向量 `[M N]`。如果航迹在最近 `N`
次更新中接收到至少 `M` 次检测，则该航迹被确认。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `'History'`。

### **删除阈值 [P Q]** — 历史逻辑的航迹删除阈值 `[5, 5]`（默认）| 正整数的实值 1×2 向量

历史逻辑的航迹删除阈值，指定为正整数的实值 1×2 向量 `[P Q]`。如果在最近 `Q` 次跟踪器更新中的 `P` 次更新里，某条已确认航迹未被分配给任何似然大于 **注册 'hit' 或 'miss' 的阈值** 参数的检测，则该航迹被删除。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `'History'`。

### **注册 'hit' 或 'miss' 的阈值** — 注册 'Hit' 或 'Miss' 的阈值 `0.2`（默认）| 范围 [0, 1] 内的标量

注册 'hit' 或 'miss' 的阈值，指定为范围 [0, 1] 内的标量。如果分配的边缘概率之和低于 `HitMissThreshold`，则航迹历史逻辑注册一个 'miss'，航迹将进行惯性推算。否则，航迹历史逻辑注册一个 'hit'。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `'History'`。

### **确认阈值 [概率]** — 积分逻辑的航迹确认阈值 `0.95`（默认）| 正标量

积分逻辑的航迹确认阈值，指定为实值正标量。如果航迹的存在概率大于或等于确认阈值，则该航迹被确认。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `'Integrated'`。

### **删除阈值 [概率]** — 积分逻辑的航迹删除阈值 `0.1`（默认）| 正标量

积分逻辑的航迹删除阈值，指定为正标量。如果航迹的存在概率降至该阈值以下，则该航迹被删除。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `'Integrated'`。

### **新目标的空间密度** — 新目标的空间密度 `1e-5`（默认）| 正标量

新目标的空间密度，指定为正标量。新目标密度描述测量空间中每单位体积的预期新航迹数。它用于在航迹初始化期间计算航迹存在概率。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `'Integrated'`。

### **真实目标消亡的时间速率** — 真实目标消亡的时间速率 `0.01`（默认）| 范围 [0, 1] 内的标量

真实目标消亡的时间速率，指定为范围 [0, 1] 内的标量。此参数描述真实目标消失的概率。它与航迹存在概率（*PTE*）的传播相关：

PTE(t+δt)=(1−DeathRate)δtPTE(t)

其中 *DeathRate* 是真实目标消亡的时间速率，*δt* 是自上次更新时间 *t* 以来的时间间隔。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `'Integrated'`。

#### 端口设置

### **预测时间源** — 预测时间的来源 `Auto`（默认）| `Input port`

预测时间的来源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **启用代价矩阵输入** — 启用代价矩阵的输入端口 off（默认）| on

选中此复选框以通过 **Cost Matrix** 输入端口启用代价矩阵的输入。

### **启用可检测航迹 ID 输入** — 启用可检测航迹 ID 输入 off（默认）| on

选中此复选框以启用 **Detectable track IDs** 输入端口。

### **Enable tentative tracks output** — 启用暂定航迹输出端口 off（默认）| on

选中此复选框可通过 **Tentative Tracks** 输出端口启用暂定航迹的输出。

### **Enable all tracks output** — 启用所有航迹输出端口 off（默认）| on

选中此复选框可通过 **All Tracks** 输出端口启用所有航迹的输出。

### **Enable information output** — 启用分析信息输出端口 off（默认）| on

选中此复选框可通过 **Info** 输出端口启用分析信息的输出端口。

### **Source of output bus name** — 输出航迹总线名称的来源 `Auto`（默认）| `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 使用 **Specify an output bus name** 参数指定输出航迹总线名称。

### **Source of output info bus name** — 输出信息总线名称的来源 `Auto`（默认）| `Property`

输出信息总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 使用 **Specify an output bus name** 参数指定输出信息总线名称。

#### 内存管理

### **Maximum number of detections per sensor** — 每个传感器的最大检测数 `100`（默认）| 正整数

将每个传感器的最大检测数指定为正整数。此参数决定每个传感器在跟踪器的一次调用期间可以传递给跟踪器的最大检测数。

如果希望跟踪器为 C/C++ 代码生成建立局部变量的有效边界，请将此参数设置为有限值。如果不希望限制每个传感器的最大检测数，请将此属性设置为 `Inf`。

#### 依赖关系

要启用此参数，请在 **Tracker Management** 选项卡中选择 **Enable Memory Management**。

### **Maximum number of detections per cluster** — 每个聚类的最大检测数 `5`（默认）| 正整数

将跟踪器运行期间每个聚类的最大检测数指定为正整数。

将此参数设置为有限值可使跟踪器限制聚类大小，并减少生成的 C/C++ 代码中跟踪器的内存占用。如果不希望限制每个聚类的最大检测数，请将此属性设置为 `Inf`。

如果在运行期间，某个聚类中的检测数超过此参数，跟踪器将根据 **Handle run-time violation of cluster size** 参数做出反应。

#### 依赖关系

要启用此参数，请在 **Tracker Management** 选项卡中选择 **Enable Memory Management**。

### **Maximum number of tracks per cluster** — 每个聚类的最大航迹数 `5`（默认）| 正整数

将跟踪器运行期间每个聚类的最大航迹数指定为正整数。

将此参数设置为有限值可使跟踪器限制聚类大小，并减少生成的 C/C++ 代码中跟踪器的内存占用。如果不希望限制每个聚类的最大检测数，请将此属性设置为 `Inf`。

如果在运行期间，某个聚类中的航迹数超过此参数，跟踪器将根据 **Handle run-time violation of cluster size** 参数做出反应。

#### 依赖关系

要启用此参数，请在 **Tracker Management** 选项卡中选择 **Enable Memory Management**。

### **Handle run-time violation of cluster size** — 处理簇大小的运行时违规 `Auto`（默认）| `Property`

将簇大小的运行时违规处理指定为以下选项之一：

- `Teminate` — 如果 **Maximum number of detections per cluster** 和 **Maximum number of tracks per cluster** 参数中指定的任一簇边界在运行时被违反，跟踪器将报告错误。
- `Split and warn` — 跟踪器使用次优方法将违反大小的簇拆分为更小的簇。跟踪器还会报告警告以指示违规。
- `Split` — 跟踪器使用次优方法将违反大小的簇拆分为更小的簇，并且不报告任何警告。

在次优方法中，跟踪器分离出与其他航迹或检测关联可能性最小的检测或航迹，直到满足簇边界。这些被分离出的检测或航迹可以形成一个或多个新簇，取决于它们彼此之间的关联可能性以及 **Threshold for assigning detections to tracks** 参数。

#### 依赖关系

要启用此参数，请在 **Tracker Management** 选项卡中选择 **Enable Memory Management**。

## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 该模块支持*严格单精度*代码生成，但有以下限制：

  - 您必须将 **Value of k for k-best JPDA** 参数指定为有限正整数。
  - 您必须指定滤波器初始化函数返回配置为单精度的 `trackingEKF`、`trackingUKF`、`trackingCKF` 或 `trackingIMM` 对象。

  有关详细信息，请参阅 Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation。
- 该模块支持*非动态内存分配*代码生成，但有以下限制：

  - 您必须将 **Value of k for k-best JPDA** 参数指定为有限正整数。
  - 您必须指定滤波器初始化函数返回 `trackingEKF`、`trackingUKF`、`trackingCKF` 或 `trackingIMM` 对象。

  有关详细信息，请参阅 Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation。

  启用非动态内存分配代码生成后，请考虑使用以下参数为跟踪器中的局部变量设置边界：

  - **Enable memory management**
  - **Maximum number of detections per sensor**
  - **Maximum number of detections per cluster**
  - **Maximum number of tracks per cluster**
  - **Handle run-time violation of cluster size**
- 在代码生成中，如果检测输入以 `double` 精度指定，则航迹输出的 `NumTracks` 字段将作为 `double` 变量返回。如果检测输入以 `single` 精度指定，则航迹输出的 `NumTracks` 字段将作为 `uint32` 变量返回。

## 版本历史

**在 R2019b 中引入**

### R2023a: Simulink buses do not show in workspace

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

联合概率数据关联跟踪器

联合概率数据关联多目标跟踪器模块能够处理来自多个传感器的多个目标的检测。该跟踪器使用联合概率数据关联将检测分配给每个航迹。跟踪器采用软分配方式，其中多个检测可以对每个航迹有贡献。跟踪器执行航迹的初始化、确认、校正、预测（执行惯性跟踪）和删除。跟踪器估计每个航迹的状态向量和状态估计误差协方差矩阵。每个检测至少被分配给一个航迹。如果检测无法分配给任何现有航迹，跟踪器将创建一个新航迹。

您可以通过指定 **Type of track confirmation and deletion logic** 和 **Value of k for k-best JPDA** 参数来启用不同的 JPDA 跟踪模式。

- 将 **Type of track confirmation and deletion logic** 参数设置为 `'Integrated'` 以启用联合集成数据关联（JIPDA）跟踪器，其中航迹确认和删除基于航迹存在概率。
- 将 **Value of k for k-best JPDA** 参数设置为有限整数以启用 k-best 联合集成数据关联（k-best JPDA）跟踪器，该跟踪器为每个聚类生成最多 k 个事件。

任何新航迹都以*暂定*状态开始。如果有足够的检测分配给暂定航迹，其状态将变为*已确认*。如果检测已经具有已知分类（返回航迹的 `ObjectClassID` 字段非零），则相应航迹立即被确认。当航迹被确认后，跟踪器认为该航迹代表一个物理对象。如果在指定数量的更新内没有检测分配给该航迹，则该航迹被删除。
