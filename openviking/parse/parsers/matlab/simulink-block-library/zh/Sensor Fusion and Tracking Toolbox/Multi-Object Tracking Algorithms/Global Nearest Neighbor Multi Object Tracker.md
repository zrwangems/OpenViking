---
type: simulink-block
title: 'Global Nearest Neighbor Multi Object Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'globalnearestneighbormultiobjecttracker'
documentation_source_path: 'ref/globalnearestneighbormultiobjecttracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Global Nearest Neighbor Multi Object Tracker

## 端口
```yaml
ports:
- name: Detections
  summary: 检测列表 Simulink® 总线，包含 MATLAB® 结构体
  direction: input
- name: Prediction Time
  summary: 航迹更新时间 实数标量
  direction: input
- name: Cost Matrix
  summary: 代价矩阵 实值 *N*t×*N*d 矩阵
  direction: input
- name: Detectable TrackIDs
  summary: 可检测航迹 ID 实值 *M*×1 向量 | 实值 *M*×2 矩阵
  direction: input
- name: State Parameters
  summary: 航迹状态参数 包含 MATLAB 结构的 Simulink 总线
  direction: input
- name: Confirmed Tracks
  summary: 确认航迹 包含 MATLAB 结构的 Simulink 总线
  direction: output
- name: Tentative Tracks
  summary: 暂定航迹 包含 MATLAB 结构的 Simulink 总线
  direction: output
- name: All Tracks
  summary: 确认和暂定航迹 包含 MATLAB 结构的 Simulink 总线
  direction: output
- name: Info
  summary: 用于分析航迹更新的附加信息 Simulink 总线，包含 MATLAB 结构体
  direction: output
```

### 输入

### **Detections** — 检测列表 Simulink® 总线，包含 MATLAB® 结构体

检测列表，指定为包含 MATLAB 结构体的 Simulink 总线。该结构体具有以下形式：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | integer |
| `Detections` | 目标检测 | 目标检测结构体数组。这些检测中的前 `NumDetections` 个为实际检测。 |

`Detections` 的字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 测量时间 | `single` 或 `double` |
| `Measurement` | 目标测量值 | `single` 或 `double` |
| `MeasurementNoise` | 测量噪声协方差矩阵 | `single` 或 `double` |
| `SensorIndex` | 传感器的唯一 ID | `single` 或 `double` |
| `ObjectClassID` | 目标分类 ID | `single` 或 `double` |
| `MeasurementParameters` | 跟踪滤波器初始化函数使用的参数 | Simulink Bus |
| `ObjectAttributes` | 传递给跟踪器的附加信息 | Simulink Bus |

有关这些字段的更详细说明，请参阅 `objectDetection`。

**注意**

目标检测结构体包含一个 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用时间。该时间标签还必须大于模块上一次调用中指定的更新时间。

### **Prediction Time** — 航迹更新时间 实数标量

航迹更新时间，指定为以秒为单位的实数标量。跟踪器将所有航迹更新到该时间。每次调用模块时，更新时间必须始终增加。单位为秒。更新时间必须至少与 **Detections** 输入端口指定的最大 `Time` 一样大。

如果未启用此端口，则由 Simulink 管理的仿真时钟确定更新时间。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，将 **Prediction time source** 设置为 `Input port`。

### **Cost Matrix** — 代价矩阵 实值 *N*t×*N*d 矩阵

代价矩阵，指定为实值 *N*t×*N*d 矩阵，其中 *N*t 是现有航迹的数量，*N*d 是当前检测的数量。

代价矩阵的行对应于现有航迹。列对应于检测。航迹按照它们在模块上一次调用时 **All Tracks** 输出端口的航迹列表中出现的顺序排列。

在跟踪器的第一次更新中，或者如果航迹没有先前的航迹，则将代价矩阵的大小指定为 [0, *N*d]。代价的计算方式必须使得较低的代价表示跟踪器将检测分配给航迹的可能性更高。要防止某些检测被分配给某些航迹，请使用 `Inf`。

如果未启用此端口，则由 **Filter initialization function** 初始化的滤波器使用距离方法计算代价矩阵。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable cost matrix input**。

### **Detectable TrackIDs** — 可检测航迹 ID 实值 *M*×1 向量 | 实值 *M*×2 矩阵

可检测航迹 ID，指定为实值 *M*×1 向量或 *M*×2 矩阵。可检测航迹是传感器期望检测到的航迹。矩阵的第一列包含传感器报告为可检测的航迹 ID 列表。第二列包含航迹的检测概率。检测概率由传感器报告，或者如果未报告，则从 **Probability of detection used for track score** 参数获取。

标识符未包含在 **Detectable TrackIDs** 中的航迹被视为不可检测。航迹删除逻辑不会将未检测到计为航迹删除目的中的“漏检”。

如果此端口未启用，则跟踪器在每次调用该模块时假定所有航迹均可检测。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable detectable track IDs Input**。

### **State Parameters** — 航迹状态参数 包含 MATLAB 结构的 Simulink 总线

航迹状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| Field | Description |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构体数组 |

该模块使用 `Parameters` 字段的值作为所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹报告的参考坐标系或所生成航迹的其他期望属性。

例如，您可以使用以下结构来定义一个矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒。

| Field Name | Value |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **Tracker Configuration** 选项卡中，选择 **Update track state parameters with time** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| Field | Description |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构体的字段如 Track Structure 中所示。

根据航迹逻辑，航迹在以下情况下被确认：

- History – 航迹在最近 `N` 次更新中至少收到 `M` 次检测。`M` 和 `N` 在 `History` 逻辑的 **Confirmation threshold** 中指定。
- Score – 航迹分数至少与 `Score` 逻辑的 **Confirmation threshold** 中指定的确认阈值一样高。

### **Tentative Tracks** — 暂定航迹 包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在被确认之前是暂定的。

航迹结构体的字段如 Track Structure 中所示。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable tentative tracks output**。

### **All Tracks** — 确认和暂定航迹 包含 MATLAB 结构的 Simulink 总线

确认和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。

航迹结构体的字段如 Track Structure 中所示。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable all tracks output**。

### **Info** — 用于分析航迹更新的附加信息 Simulink 总线，包含 MATLAB 结构体

用于分析航迹更新的附加信息，以包含 MATLAB 结构体的 Simulink 总线形式返回。

下表显示了 info 结构体的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `OOSMDetectionIndices` | 跟踪器当前步中乱序量测的索引 |
| `TrackIDsAtStepBeginning` | 步开始时的航迹 ID |
| `CostMatrix` | 运动学分配矩阵的代价，其中 (*i*, *j*) 元素表示将航迹 *i* 分配给检测 *j* 的代价。 |
| `Assignments` | 来自分配函数的分配结果，以整数值 *L*×2 矩阵返回，其中 *L* 是分配数量。矩阵的第一列包含航迹 ID，第二列包含已分配检测的索引。检测索引是用于更新跟踪器的检测的数组索引。 |
| `UnassignedTracks` | 从跟踪器返回的未分配航迹的 ID |
| `UnassignedDetections` | 从跟踪器返回的未分配检测的 ID |
| `InitiatedTrackIDs` | 在该步中起始的航迹的 ID |
| `DeletedTrackIDs` | 在该步中删除的航迹的 ID |
| `TrackIDsAtStepEnd` | 步结束时的航迹 ID |
| `MaxNumDetectionsPerCluster` | 在该步中生成的所有聚类中检测的最大数量。仅当您将 **Cluster tracks and detections for assignment** 和 **Enable memory management** 参数均设置为 `on` 时，该结构体才具有此字段。 |
| `MaxNumTracksPerCluster` | 在该步中生成的所有聚类中航迹的最大数量。仅当您将 **Cluster tracks and detections for assignment** 和 **Enable memory management** 参数均设置为 `on` 时，该结构体才具有此字段。 |
| `OOSMHandling` | 乱序量测处理的分析信息，以结构体形式返回。仅当跟踪器的 **Out-of-sequence measurements handling** 参数指定为 `Retordiction` 时，该结构体才具有此字段。 |

`OOSMHandling` 结构体包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `DiscardedDetections` | 被丢弃的乱序检测的索引。如果某个 OOSM 未被 **Maximum number of OOSM steps** 参数所指定的已保存状态历史覆盖，则该 OOSM 被丢弃。 |
| `CostMatrix` | 乱序量测的分配矩阵的代价 |
| `Assignments` | 乱序检测与已维护航迹之间的分配 |
| `UnassignedDetections` | 未分配的乱序检测的索引。跟踪器为未分配的乱序检测创建新航迹。 |

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择
**启用信息输出**。
## 参数
```yaml
parameters:
- name: Tracker identifier
  summary: 唯一跟踪器标识符 0（默认）| 非负整数
  group: ''
- name: 滤波器初始化函数
  summary: 滤波器初始化函数 initcvekf（默认）| 函数名
  group: ''
- name: 最大航迹数
  summary: 最大航迹数 200（默认）| 正整数
  group: ''
- name: 最大传感器数
  summary: 最大传感器数 20（默认）| 正整数
  group: ''
- name: 乱序测量处理
  summary: 乱序测量处理 Terminate（默认）| Neglect | Retrodiction
  group: ''
- name: 最大 OOSM 步数
  summary: 最大 OOSM 步数 3（默认）| 正整数
  group: ''
- name: 航迹状态参数
  summary: 航迹状态参考坐标系参数 结构体 | 结构体数组
  group: ''
- name: Update track state parameters with time
  summary: 使用时间更新航迹状态参数 off（默认）| on
  group: ''
- name: Enable memory management
  summary: 启用内存管理 off（默认）| on
  group: ''
- name: Assignment algorithm name
  summary: 关联算法名称 'MatchPairs'（默认）| 'Munkres' | 'Jonker-Volgenant' | 'Auction' | 'Custom'
  group: ''
- name: Name of 'Custom' assignment function
  summary: 自定义关联函数名称 字符向量
  group: ''
- name: Threshold for assigning detections to tracks
  summary: 将检测关联到航迹的阈值 30*[1 Inf]（默认）| 正标量 | 1×2 正值向量
  group: ''
- name: Cluster tracks and detections for assignment
  summary: 为关联聚类航迹和检测 off（默认）| on
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted Execution（默认）| Code Generation
  group: ''
- name: Type of track confirmation and deletion logic
  summary: 航迹确认和删除逻辑类型 History（默认）| Score
  group: ''
- name: Confirmation threshold [M N]
  summary: 历史逻辑的航迹确认阈值 [2 3]（默认）| 正整数的实值 1×2 向量
  group: ''
- name: Deletion threshold [P Q]
  summary: 历史逻辑的航迹删除阈值 [5 5]（默认）| 正整数的实值 1×2 向量
  group: ''
- name: Confirmation threshold [positive scalar]
  summary: 得分逻辑的航迹确认阈值 20（默认）| 正标量
  group: ''
- name: Deletion threshold [negative scalar]
  summary: 得分逻辑的航迹删除阈值 -7（默认）| 标量 | 负标量
  group: ''
- name: Probability of detection used for track score
  summary: 用于航迹得分的检测概率 0.9（默认）| (0,1) 范围内的标量
  group: ''
- name: Rate of false positives used for track score
  summary: 用于航迹得分的虚警概率 1e-6（默认）| (0,1) 范围内的标量
  group: ''
- name: Volume of the sensor's detection bin
  summary: 传感器检测波位的体积 1（默认）| 正标量
  group: ''
- name: Rate of new tracks per unit volume
  summary: 每单位体积的新航迹率 1（默认）| 正标量
  group: ''
- name: Prediction time source
  summary: 预测时间源 Auto（默认）| Input port
  group: ''
- name: Enable cost matrix input
  summary: 启用代价矩阵输入端口 off（默认）| on
  group: ''
- name: Enable detectable track IDs input
  summary: 启用可检测航迹 ID 输入 off（默认）| on
  group: ''
- name: Enable tentative tracks output
  summary: 启用暂定航迹输出端口 off（默认）| on
  group: ''
- name: Enable all tracks output
  summary: 启用所有航迹输出端口 off（默认）| on
  group: ''
- name: Enable information output
  summary: 启用分析信息输出端口 off（默认）| on
  group: ''
- name: 输出总线名称的来源
  summary: 输出航迹总线名称的来源 Auto（默认）| Property
  group: ''
- name: 输出信息总线名称的来源
  summary: 输出信息总线名称的来源 Auto（默认）| Property
  group: ''
- name: 每个传感器的最大检测数
  summary: 每个传感器的最大检测数 100（默认）| 正整数
  group: ''
- name: 每个聚类的最大检测数
  summary: 每个聚类的最大检测数 5（默认）| 正整数
  group: ''
- name: 每个聚类的最大航迹数
  summary: 每个聚类的最大航迹数 5（默认）| 正整数
  group: ''
- name: Handle run-time violation of cluster size
  summary: 处理簇大小的运行时违规 Auto（默认）| Property
  group: ''
```

#### Tracker Management

### **Tracker identifier** — 唯一跟踪器标识符 `0`（默认）| 非负整数

将唯一跟踪器标识符指定为非负整数。此参数作为跟踪器输出中的 `SourceIndex` 传递，用于区分多跟踪器系统中来自不同跟踪器的航迹。要将航迹输出用作 Track-To-Track Fuser 模块的输入，您必须将此属性指定为正整数。

**Example:** `1`

### **滤波器初始化函数** — 滤波器初始化函数 `initcvekf`（默认）| 函数名

滤波器初始化函数，指定为有效的滤波器初始化函数的名称。跟踪器在创建新航迹时使用该滤波器初始化函数。

Sensor Fusion and Tracking Toolbox™ 提供了许多可供使用的初始化函数：

| 初始化函数 | 函数定义 |
| --- | --- |
| `initcvabf` | 初始化常速 alpha-beta 滤波器 |
| `initcaabf` | 初始化常加速 alpha-beta 滤波器 |
| `initcvekf` | 初始化常速扩展卡尔曼滤波器。 |
| `initcackf` | 初始化常加速容积滤波器。 |
| `initctckf` | 初始化常转弯速率容积滤波器。 |
| `initcvckf` | 初始化常速容积滤波器。 |
| `initcapf` | 初始化常加速粒子滤波器。 |
| `initctpf` | 初始化常转弯速率粒子滤波器。 |
| `initcvpf` | 初始化常速粒子滤波器。 |
| `initcvkf` | 初始化常速线性卡尔曼滤波器。 |
| `initcvukf` | 初始化常速无迹卡尔曼滤波器。 |
| `initcaekf` | 初始化常加速扩展卡尔曼滤波器。 |
| `initcakf` | 初始化常加速线性卡尔曼滤波器。 |
| `initcaukf` | 初始化常加速无迹卡尔曼滤波器。 |
| `initctekf` | 初始化常转弯速率扩展卡尔曼滤波器。 |
| `initctukf` | 初始化常转弯速率无迹卡尔曼滤波器。 |
| `initcvmscekf` | 初始化常速修正球坐标扩展卡尔曼滤波器。 |
| `initrpekf` | 初始化常速距离参数化扩展卡尔曼滤波器。 |
| `initapekf` | 初始化常速角度参数化扩展卡尔曼滤波器。 |
| `initekfimm` | 初始化跟踪 IMM 滤波器。 |

您也可以编写自己的初始化函数。该函数必须具有以下语法：

```
filter = filterInitializationFcn(detection)
```

该函数的输入是由 `objectDetection` 创建的检测报告。该函数的输出必须是滤波器对象：`trackingKF`、`trackingEKF`、`trackingUKF`、`trackingCKF`、`trackingPF`、`trackingMSCEKF`、`trackingGSF`、`trackingIMM` 或 `trackingABF`。

为帮助您编写此函数，您可以在 MATLAB 中查看所提供函数的详细信息。例如：

```
type initcvekf
```

### **最大航迹数** — 最大航迹数 `200`（默认）| 正整数

该模块可以维护的最大航迹数，指定为正整数。

### **最大传感器数** — 最大传感器数 `20`（默认）| 正整数

该模块可以处理的最大传感器数，指定为正整数。该值应大于或等于 **Detections** 输入端口输入的最高 `SensorIndex` 值。

### **乱序测量处理** — 乱序测量处理 `Terminate`（默认）| `Neglect` | `Retrodiction`

乱序测量处理，指定为 `Terminate`、`Neglect` 或 `Retrodiction`。每个检测都有一个关联的时间戳 *t*d，而跟踪器模块有自己的时间戳 *t*t，该时间戳在每次调用时更新。如果 *t*d < *t*t，跟踪器模块将该测量视为 OOSM。

当您将该参数指定为：

- `Terminate` — 当模块遇到乱序测量时停止运行。
- `Neglect` — 模块忽略任何乱序测量并继续运行。
- `Retrodiction` — 模块使用反推算法通过忽略 OOSM、更新现有航迹或使用 OOSM 创建新航迹来更新跟踪器。您必须在 **滤波器初始化函数** 参数中指定一个返回 `trackingKF`、`trackingEKF` 或 `trackingIMM` 对象的滤波器初始化函数。

如果您将该参数指定为 `Retrodiction`，跟踪器按照以下步骤处理 OOSM：

- 如果 OOSM 时间戳超出跟踪器中维护的最旧校正时间戳（由 **最大 OOSM 步数** 参数指定），跟踪器丢弃这些 OOSM。
- 如果 OOSM 时间戳在跟踪器的最旧校正时间戳范围内，跟踪器首先将所有现有航迹反推到 OOSM 的时间。然后，跟踪器应用联合概率数据关联算法，尝试将 OOSM 与反推后的航迹进行关联。

  - 如果跟踪器成功将 OOSM 与至少一条反推航迹关联，则跟踪器使用 OOSM 通过应用反校正算法更新反推航迹，以获得当前的校正航迹。
  - 如果跟踪器无法将 OOSM 与任何反推航迹关联，则跟踪器基于该 OOSM 创建新航迹，并将该航迹预测到当前时间。

有关反推和反校正算法的更多详细信息，请参阅 Retrodiction and Retro-Correction。要模拟乱序检测，请使用 `objectDetectionDelay`。

**注意**

- 当您选择 `Retrodiction` 时，不能使用 **代价矩阵** 输入。

### **最大 OOSM 步数** — 最大 OOSM 步数 `3`（默认）| 正整数

最大乱序测量（OOSM）步数，指定为正整数。

增大该参数的值需要更多内存，但允许您以相对于模块上次更新时的时间戳具有更大滞后的 OOSM 调用跟踪器模块。此外，随着滞后的增加，OOSM 对航迹当前状态的影响会减小。该参数的推荐值为 `3`。

#### 依赖关系

要启用此参数，请将 **乱序测量处理** 参数设置为 `Retrodiction`。

### **航迹状态参数** — 航迹状态参考坐标系参数 结构体 | 结构体数组

将航迹状态参考坐标系的参数指定为结构体或结构体数组。模块将该参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹报告的参考坐标系或所生成航迹的其他所需属性。

例如，您可以使用以下结构体定义一个矩形参考坐标系，其原点位置为 `[10 10 0]` 米，原点速度相对于场景坐标系为 `[2 -2 0]` 米每秒。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

您可以通过选择 **随时间更新航迹状态参数** 参数，通过 **状态参数** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **Update track state parameters with time** — 使用时间更新航迹状态参数 `off`（默认）| `on`

选择此参数可通过 **State Parameters** 输入端口启用航迹状态参数的输入端口。

### **Enable memory management** — 启用内存管理 `off`（默认）| `on`

选择此参数可使用 **Maximum number of detections per sensor** 参数启用内存管理，以指定每个传感器在跟踪器的一次调用期间可以传递给跟踪器的最大检测数。此外，如果 **Cluster tracks and detections for assignment** 参数指定为 `on`，您可以使用另外三个参数来指定跟踪器中某些可变大小数组的边界，并确定跟踪器如何处理簇大小违规：

- **Maximum number of detections per cluster**
- **Maximum number of tracks per cluster**
- **Handle run-time violation of cluster size**

为可变大小数组指定边界允许您管理生成的 C/C++ 代码中跟踪器的内存占用。

### **Assignment algorithm name** — 关联算法名称 `'MatchPairs'`（默认）| `'Munkres'` | `'Jonker-Volgenant'` | `'Auction'` | `'Custom'`

关联算法，指定为 `'MatchPairs'`、`'Munkres'`、`'Jonker-Volgenant'`、`'Auction'` 或 `'Custom'`。Munkres 是唯一保证最优解的关联算法，但它也是最慢的，尤其是在检测和航迹数量较大时。其他算法不保证最优解，但对于有 20 个或更多航迹和检测的问题可能更快。使用 `'Custom'` 定义您自己的关联函数，并在 `CustomAssignmentFcn` 属性中指定其名称。

### **Name of 'Custom' assignment function** — 自定义关联函数名称 字符向量

自定义关联函数名称，指定为字符串。关联函数必须具有以下语法：

```
 [assignment,unTrs,unDets] = f(cost,costNonAssignment)
```

有关关联函数的示例及其参数的说明，请参阅 `assignmunkres`。

**示例：** `'mycustomfcn'`

#### 依赖关系

要启用此属性，请将 **Assignment algorithm name** 名称设置为 `'Custom'`。

### **Threshold for assigning detections to tracks** — 将检测关联到航迹的阈值 `30*[1 Inf]`（默认）| 正标量 | 1×2 正值向量

将检测关联到航迹的阈值（或门限阈值），指定为正标量或 1×2 向量
[*C*1*,C*2]，
其中 *C*1 ≤
*C*2。如果指定为标量，则指定值 *val* 将扩展为 [*val*,
`Inf`]。

最初，跟踪器对所有航迹和检测之间的归一化距离执行粗略估计。跟踪器仅对粗略归一化距离小于 *C*2 的组合计算精确归一化距离。此外，跟踪器仅在其精确归一化距离小于 *C*1 时才能将检测关联到航迹。有关归一化距离的说明，请参阅算法。

- 如果存在应计算用于关联但未计算的航迹和检测组合，请增大 *C*2 的值。如果代价计算耗时过多，请减小该值。
- 如果存在应关联到航迹但未关联的检测，请增大 *C*1 的值。如果存在被关联到不应关联的航迹（距离太远）的检测，请减小该值。

**注意**

如果 *C*2 的值是有限的，则在跟踪器中所使用的跟踪滤波器中指定的状态转移函数和测量函数必须能够分别接受 *M*×*N* 的状态矩阵作为输入，并输出 *N* 个预测状态和 *N* 个测量。*M* 是状态的大小。*N*（状态的数量）是任意非负整数。

### **Cluster tracks and detections for assignment** — 为关联聚类航迹和检测 `off`（默认）| `on`

指定为关联聚类航迹和检测的方式如下：

- `off` — 跟踪器使用代价矩阵为每个传感器求解全局最近邻关联问题。代价矩阵的列数等于该传感器的检测数，行数等于跟踪器维护的航迹数。禁止关联（代价大于 **Threshold for assigning detections to tracks** 参数的关联）具有无穷大的关联代价。
- `on` — 跟踪器在分离出禁止关联（代价大于 **Threshold for assigning detections to tracks** 参数的关联）后创建一个聚类，并使用禁止关联基于 **Threshold for assigning detections to tracks** 参数形成新的聚类。*聚类*是一组（每个传感器的）检测和被认为相互关联的航迹的集合。在这种情况下，跟踪器为每个聚类求解全局最近邻关联问题。

  当您将此属性指定为 `on` 并在 **Tracker Management** 选项卡中选择 **Enable memory management** 时，您可以使用以下三个参数为跟踪器中某些可变大小的数组指定边界，并确定跟踪器如何处理聚类大小违规：

  - **Maximum number of detections per cluster**
  - **Maximum number of tracks per cluster**
  - **Handle run-time violation of cluster size**

  为可变大小数组指定边界使您能够管理跟踪器的内存占用，尤其是在生成的 C/C++ 代码中。

### **Simulate using** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。

#### Track Logic

### **Type of track confirmation and deletion logic** — 航迹确认和删除逻辑类型 `History`（默认）| `Score`

航迹确认和删除逻辑类型，选择为 `History` 或 `Score`。

- `History` – 航迹确认和删除基于航迹在最近跟踪器更新中被关联到检测的次数。
- `Score` – 航迹确认和删除基于对数似然航迹得分。高分意味着航迹更可能是有效的。低分意味着航迹更可能是虚警。

### **Confirmation threshold [M N]** — 历史逻辑的航迹确认阈值 `[2 3]`（默认）| 正整数的实值 1×2 向量

历史逻辑的航迹确认阈值，指定为正整数的实值 1×2 向量 `[M N]`。如果航迹在最近 `N` 次更新中接收到至少 `M` 次检测，则该航迹被确认。

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `History`。

### **Deletion threshold [P Q]** — 历史逻辑的航迹删除阈值 `[5 5]`（默认）| 正整数的实值 1×2 向量

历史逻辑的航迹删除阈值，指定为正整数的实值 1×2 向量 `[P Q]`。如果已确认的航迹在最近 `Q` 次跟踪器更新中未被关联到任何检测达到 `P` 次，则该航迹被删除。

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `History`。

### **Confirmation threshold [positive scalar]** — 得分逻辑的航迹确认阈值 `20`（默认）| 正标量

得分逻辑的航迹确认阈值，指定为实值正标量。如果航迹的得分至少与确认阈值一样高，则该航迹被确认。

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `Score`。

### **Deletion threshold [negative scalar]** — 得分逻辑的航迹删除阈值 `-7`（默认）| 标量 | 负标量

得分逻辑的航迹删除阈值，指定为负标量。如果航迹的得分从最大航迹得分下降至少该阈值，则该航迹被删除。

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `Score`。

### **Probability of detection used for track score** — 用于航迹得分的检测概率 `0.9`（默认）| (0,1) 范围内的标量

用于航迹得分的检测概率，指定为 (0,1) 范围内的正标量。

**示例：** `0.5`

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `Score`。

### **Rate of false positives used for track score** — 用于航迹得分的虚警概率 `1e-6`（默认）| (0,1) 范围内的标量

用于航迹得分的虚警概率，指定为 (0,1) 范围内的标量。

**示例：** `1e-5`

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `Score`。

### **Volume of the sensor's detection bin** — 传感器检测波位的体积 `1`（默认）| 正标量

传感器检测波位的体积，指定为正标量。例如，如果雷达产生 4-D 测量值，其中包括方位角、俯仰角、距离和距离变化率，则 4-D 体积由雷达角波束宽度、距离波位宽度和距离变化率波位宽度定义。在初始化和更新航迹时，体积用于计算航迹得分。

**示例：** `1.5`

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `Score`。

### **Rate of new tracks per unit volume** — 每单位体积的新航迹率 `1`（默认）| 正标量

每单位体积的新航迹率，指定为正标量。新航迹率用于在航迹初始化期间计算航迹得分。

**示例：** `2.5`

#### 依赖关系

要启用此参数，请将 **Type of track confirmation and deletion logic** 设置为 `Score`。

#### 端口设置

### **Prediction time source** — 预测时间源 `Auto`（默认）| `Input port`

预测时间源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **Enable cost matrix input** — 启用代价矩阵输入端口 off（默认）| on

选中此复选框以启用通过 **Cost Matrix** 输入端口输入代价矩阵。

### **Enable detectable track IDs input** — 启用可检测航迹 ID 输入 off（默认）| on

选中此复选框以启用 **Detectable track IDs** 输入端口。

### **Enable tentative tracks output** — 启用暂定航迹输出端口 off（默认）| on

选中此复选框以启用通过 **Tentative Tracks** 输出端口输出暂定航迹。

### **Enable all tracks output** — 启用所有航迹输出端口 off（默认）| on

选中此复选框以启用通过 **All Tracks** 输出端口输出所有航迹。

### **Enable information output** — 启用分析信息输出端口 off（默认）| on

选中此复选框以启用通过 **Info** 输出端口输出分析信息。

### **输出总线名称的来源** — 输出航迹总线名称的来源 `Auto`（默认）| `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 通过 **指定输出总线名称** 参数指定输出航迹总线名称。

### **输出信息总线名称的来源** — 输出信息总线名称的来源 `Auto`（默认）| `Property`

输出信息总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 通过 **指定输出总线名称** 参数指定输出信息总线名称。

#### 内存管理

### **每个传感器的最大检测数** — 每个传感器的最大检测数 `100`（默认）| 正整数

将每个传感器的最大检测数指定为正整数。此参数决定每个传感器在每次调用跟踪器时可以向跟踪器传递的最大检测数。

如果希望跟踪器为 C/C++ 代码生成建立局部变量的高效边界，请将此参数设置为有限值。如果不希望限制每个传感器的最大检测数，请将此属性设置为 `Inf`。

#### 依赖关系

要启用此参数，请在 **跟踪器管理** 选项卡中选择 **启用内存管理**。

### **每个聚类的最大检测数** — 每个聚类的最大检测数 `5`（默认）| 正整数

将跟踪器运行期间每个聚类的最大检测数指定为正整数。

将此参数设置为有限值可使跟踪器限制聚类大小，并减少生成的 C/C++ 代码中跟踪器的内存占用。如果不希望限制每个聚类的最大检测数，请将此属性设置为 `Inf`。

如果在运行期间某个聚类中的检测数超过此参数，跟踪器将根据 **处理聚类大小的运行时违规** 参数作出反应。

#### 依赖关系

要启用此参数，请将 **用于分配的聚类航迹和检测** 指定为 `on`，并在 **跟踪器管理** 选项卡中选择 **启用内存管理**。

### **每个聚类的最大航迹数** — 每个聚类的最大航迹数 `5`（默认）| 正整数

将跟踪器运行期间每个聚类的最大航迹数指定为正整数。

将此参数设置为有限值可使跟踪器限制聚类大小，并减少生成的 C/C++ 代码中跟踪器的内存占用。如果不希望限制每个聚类的最大检测数，请将此属性设置为 `Inf`。

如果在运行期间某个聚类中的航迹数超过此参数，跟踪器将根据 **处理聚类大小的运行时违规** 参数作出反应。

#### 依赖关系

要启用此参数，请将 **用于分配的聚类航迹和检测** 指定为 `on`，并在 **跟踪器管理** 选项卡中选择 **启用内存管理**。

### **Handle run-time violation of cluster size** — 处理簇大小的运行时违规 `Auto`（默认）| `Property`

将簇大小的运行时违规处理方式指定为以下选项之一：

- `Teminate` — 如果在运行期间任何簇违反了 **Maximum number of detections per cluster** 和 **Maximum number of tracks per cluster** 参数中指定的簇边界，跟踪器将报告错误。
- `Split and warn` — 跟踪器使用次优方法将违反大小的簇拆分为更小的簇。跟踪器还会报告警告以指示该违规。
- `Split` — 跟踪器使用次优方法将违反大小的簇拆分为更小的簇。跟踪器不报告警告。

在次优方法中，跟踪器分离出与其他航迹或检测的关联似然最小的检测或航迹，直到满足簇边界。这些被分离出的检测或航迹可以形成一个或多个新簇，取决于它们彼此之间的关联似然以及 **Threshold for assigning detections to tracks** 参数。

#### 依赖关系

要启用此参数，请将 **Cluster tracks and detections for assignment** 指定为 `on`，并在 **Tracker Management** 选项卡中选择 **Enable Memory Management**。
## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 该模块支持*严格单精度*代码生成，但有以下限制：

  - 您必须将分配算法指定为 `'Jonker-Volgenant'`。
  - 您必须指定滤波器初始化函数返回配置为单精度的 `trackingEKF`、`trackingUKF`、`trackingCKF` 或 `trackingIMM` 对象。

  有关详细信息，请参阅 Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation。
- 跟踪器支持*非动态内存分配*代码生成，但有以下限制：

  - 您必须将分配算法指定为 `'Jonker-Volgenant'` 或 `'MatchPairs'`。
  - 您必须指定滤波器初始化函数返回 `trackingEKF`、`trackingUKF`、`trackingCKF` 或 `trackingIMM` 对象。

  有关详细信息，请参阅 Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation。

  启用非动态内存分配代码生成后，请考虑使用以下参数来设置跟踪器中局部变量的边界：

  - **Enable memory management**
  - **对航迹和检测进行聚类以用于分配**
  - **Maximum number of detections per sensor**
  - **Maximum number of detections per cluster**
  - **Maximum number of tracks per cluster**
  - **Handle run-time violation of cluster size**
- 在代码生成中，如果检测输入以 `double` 精度指定，则航迹输出的 `NumTracks` 字段将作为 `double` 变量返回。如果检测输入以 `single` 精度指定，则航迹输出的 `NumTracks` 字段将作为 `uint32` 变量返回。

## 版本历史

**在 R2019b 中引入**

### R2023a: Simulink buses do not show in workspace

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

使用 GNN 关联的多传感器、多目标跟踪器

Global Nearest Neighbor Multi Object Tracker 模块能够处理来自多个传感器的多个目标的检测，与 `trackerGNN` System object™ 非常相似。该跟踪器基于全局最近邻（GNN）关联算法对航迹进行初始化、确认、预测、校正和删除。跟踪器为每条航迹估计状态向量和状态向量协方差矩阵。每个检测最多分配给一条航迹。如果检测无法分配给任何航迹，跟踪器将初始化一条新航迹。

任何新航迹都从试探状态开始。如果有足够的检测分配给某条试探航迹，其状态将变为已确认。如果检测已经具有已知分类（返回航迹的 `ObjectClassID` 字段非零），则该航迹立即被确认。当航迹被确认后，跟踪器认为该航迹代表一个物理对象。如果在可指定次数的更新内没有检测分配给该航迹，则该航迹被删除。
