---
type: simulink-block
title: 'Global Nearest Neighbor Multi Object Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Trackers'
documentation_page: 'globalnearestneighbormultiobjecttracker'
documentation_source_path: 'ref/globalnearestneighbormultiobjecttracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Global Nearest Neighbor Multi Object Tracker

## 端口

### 输入

### **Detections** — 检测列表 包含 MATLAB® 结构的 Simulink® 总线

检测列表，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | integer |
| `Detections` | 目标检测 | 目标检测结构的数组。这些检测中的前 `NumDetections` 个是实际检测。 |

`Detections` 的字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 测量时间 | `single` 或 `double` |
| `Measurement` | 目标测量 | `single` 或 `double` |
| `MeasurementNoise` | 测量噪声协方差矩阵 | `single` 或 `double` |
| `SensorIndex` | 传感器的唯一 ID | `single` 或 `double` |
| `ObjectClassID` | 目标分类 ID | `single` 或 `double` |
| `MeasurementParameters` | 跟踪滤波器初始化函数使用的参数 | Simulink Bus |
| `ObjectAttributes` | 传递给跟踪器的附加信息 | Simulink Bus |

有关这些字段的更详细说明，请参阅 `objectDetection`。

**注意**

目标检测结构包含一个 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用时间。该时间标签还必须大于模块上一次调用中指定的更新时间。

### **Prediction Time** — 航迹更新时间 real scalar

航迹更新时间，指定为 real scalar，单位为 seconds。跟踪器将所有航迹更新到此时间。每次调用模块时，更新时间必须始终增加。单位为 seconds。更新时间必须至少等于 **Detections** 输入端口指定的最大 `Time`。

如果未启用此端口，则由 Simulink 管理的仿真时钟确定更新时间。

#### 依赖项

要启用此端口，请在 **端口设置** 选项卡中，将 **Prediction time source** 设置为 `Input port`。

### **Cost Matrix** — 代价矩阵 real-valued *N*t-by-*N*d 矩阵

代价矩阵，指定为 real-valued *N*t-by-*N*d 矩阵，其中 *N*t 是现有航迹数，*N*d 是当前检测数。

代价矩阵的行对应于现有航迹。列对应于检测。航迹的顺序与上一次调用模块时 **All Tracks** 输出端口航迹列表中的显示顺序相同。

在对跟踪器的第一次更新中，或者如果跟踪器没有先前的航迹，则将代价矩阵的大小指定为 [0, *N*d]。计算代价时必须使较低的代价表示跟踪器将检测分配给航迹的可能性较高。要防止某些检测被分配给某些航迹，请使用 `Inf`。

如果未启用此端口，则由 **Filter initialization function** 初始化的滤波器使用距离方法计算代价矩阵。

#### 依赖项

要启用此端口，请在 **端口设置** 选项卡中，选中 **Enable cost matrix input**。

### **Detectable TrackIDs** — 可检测航迹 ID real-valued *M*-by-1 向量 | real-valued *M*-by-2 矩阵

可检测航迹 ID，指定为 real-valued *M*-by-1 向量或 *M*-by-2 矩阵。可检测航迹是传感器预期检测到的航迹。矩阵的第一列包含传感器报告为可检测的航迹 ID 列表。第二列包含该航迹的检测概率。检测概率可由传感器报告，如果未报告，则从 **Probability of detection used for track score** 参数获取。

标识符未包含在 **Detectable TrackIDs** 中的航迹被视为不可检测。出于航迹删除目的，航迹删除逻辑不会将未检测到计为“漏检”。

如果未启用此端口，则跟踪器在每次调用模块时假定所有航迹均可检测。

#### 依赖项

要启用此端口，请在 **端口设置** 选项卡中，选中 **Enable detectable track IDs Input**。

### **State Parameters** — 航迹状态参数 包含 MATLAB 结构的 Simulink 总线

航迹状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为 nonnegative integer |
| `Parameters` | 状态参数结构的数组 |

模块将 `Parameters` 字段的值用于所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义报告航迹所用的参考坐标系，或所生成航迹的其他所需属性。

例如，可以使用以下结构定义一个矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖项

要启用此端口，请在 **跟踪器配置** 选项卡中，选中 **Update track state parameters with time** 参数。

### 输出

### **Confirmed Tracks** — 确认航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of tracks** 参数设置。这些航迹中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如 Track Structure 所示。

根据航迹逻辑，满足以下条件时航迹被确认：

- History – 航迹在最近 `N` 次更新中至少收到 `M` 次检测。`M` 和 `N` 在 `History` 逻辑的 **Confirmation threshold** 中指定。
- Score – 航迹分数至少达到 `Score` 逻辑的 **Confirmation threshold** 中指定的确认阈值。

### **Tentative Tracks** — 暂定航迹 包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在被确认之前是暂定的。

航迹结构的字段如 Track Structure 所示。

#### 依赖项

要启用此端口，请在 **端口设置** 选项卡中，选中 **Enable tentative tracks output**。

### **All Tracks** — 确认航迹和暂定航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。

航迹结构的字段如 Track Structure 所示。

#### 依赖项

要启用此端口，请在 **端口设置** 选项卡中，选中 **Enable all tracks output**。

### **Info** — 用于分析航迹更新的附加信息 包含 MATLAB 结构的 Simulink 总线

用于分析航迹更新的附加信息，返回为包含 MATLAB 结构的 Simulink 总线。

下表显示了 info 结构的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `OOSMDetectionIndices` | 跟踪器当前步中乱序测量的索引 |
| `TrackIDsAtStepBeginning` | 步开始时航迹 ID |
| `CostMatrix` | 运动学分配矩阵的代价，其中 (*i*, *j*) 元素表示将航迹 *i* 分配给检测 *j* 的代价。 |
| `Assignments` | 来自分配函数的分配，返回为 integer-valued *L*-by-2 矩阵，其中 *L* 是分配数量。矩阵的第一列包含航迹 ID，第二列包含所分配检测的索引。检测索引是用于更新跟踪器的检测的数组索引。 |
| `UnassignedTracks` | 跟踪器返回的未分配航迹 ID |
| `UnassignedDetections` | 跟踪器返回的未分配检测 ID |
| `InitiatedTrackIDs` | 在该步中起始的航迹 ID |
| `DeletedTrackIDs` | 在该步中删除的航迹 ID |
| `TrackIDsAtStepEnd` | 步结束时航迹 ID |
| `MaxNumDetectionsPerCluster` | 在该步中生成的所有簇中的最大检测数量。仅当您将 **Cluster tracks and detections for assignment** 和 **Enable memory management** 参数均设置为 `on` 时，该结构才具有此字段。 |
| `MaxNumTracksPerCluster` | 在该步中生成的所有簇中的最大航迹数量。仅当您将 **Cluster tracks and detections for assignment** 和 **Enable memory management** 参数均设置为 `on` 时，该结构才具有此字段。 |
| `OOSMHandling` | 乱序测量处理的分析信息，返回为结构。仅当跟踪器的 **Out-of-sequence measurements handling** 参数指定为 `Retordiction` 时，该结构才具有此字段。 |

`OOSMHandling` 结构包含以下字段：

| 字段 | 描述 |
| --- | --- |
| `DiscardedDetections` | 被丢弃的乱序检测的索引。如果 OOSM 未被 **Maximum number of OOSM steps** 参数指定的已保存状态历史覆盖，则该 OOSM 会被丢弃。 |
| `CostMatrix` | 乱序测量的分配矩阵代价 |
| `Assignments` | 乱序检测与所维护航迹之间的分配 |
| `UnassignedDetections` | 未分配乱序检测的索引。跟踪器为未分配的乱序检测创建新航迹。 |

#### 依赖项

要启用此端口，请在 **端口设置** 选项卡中，选中 **Enable information output**。

## 参数

#### 跟踪器管理

### **Tracker identifier** — 唯一跟踪器标识符 `0`（默认）| nonnegative integer

将唯一跟踪器标识符指定为 nonnegative integer。此参数在跟踪器输出中作为 `SourceIndex` 传递，并用于区分多跟踪器系统中来自不同跟踪器的航迹。要将航迹输出用作 Track-To-Track Fuser 模块的输入，必须将此属性指定为 positive integer。

**示例：** `1`

### **Filter initialization function** — 滤波器初始化函数 `initcvekf`（默认）| function name

滤波器初始化函数，指定为有效的滤波器初始化函数的名称。跟踪器在创建新航迹时使用该滤波器初始化函数。

Sensor Fusion and Tracking Toolbox™ 提供了许多可供使用的初始化函数：

| 初始化函数 | 函数定义 |
| --- | --- |
| `initcvabf` | 初始化常速 alpha-beta 滤波器 |
| `initcaabf` | 初始化恒定加速度 alpha-beta 滤波器 |
| `initcvekf` | 初始化常速扩展卡尔曼滤波器。 |
| `initcackf` | 初始化恒定加速度容积滤波器。 |
| `initctckf` | 初始化恒定转向率容积滤波器。 |
| `initcvckf` | 初始化常速容积滤波器。 |
| `initcapf` | 初始化恒定加速度粒子滤波器。 |
| `initctpf` | 初始化恒定转向率粒子滤波器。 |
| `initcvpf` | 初始化常速粒子滤波器。 |
| `initcvkf` | 初始化常速线性卡尔曼滤波器。 |
| `initcvukf` | 初始化常速无迹卡尔曼滤波器。 |
| `initcaekf` | 初始化恒定加速度扩展卡尔曼滤波器。 |
| `initcakf` | 初始化恒定加速度线性卡尔曼滤波器。 |
| `initcaukf` | 初始化恒定加速度无迹卡尔曼滤波器。 |
| `initctekf` | 初始化恒定转向率扩展卡尔曼滤波器。 |
| `initctukf` | 初始化恒定转向率无迹卡尔曼滤波器。 |
| `initcvmscekf` | 初始化常速修正球坐标扩展卡尔曼滤波器。 |
| `initrpekf` | 初始化常速距离参数化扩展卡尔曼滤波器。 |
| `initapekf` | 初始化常速角度参数化扩展卡尔曼滤波器。 |
| `initekfimm` | 初始化跟踪 IMM 滤波器。 |

您也可以编写自己的初始化函数。该函数必须具有以下语法：

    filter = filterInitializationFcn(detection)

此函数的输入是检测报告，如由 `objectDetection` 创建的那些检测报告。此函数的输出必须是滤波器对象：`trackingKF`、`trackingEKF`、`trackingUKF`、`trackingCKF`、`trackingPF`、`trackingMSCEKF`、`trackingGSF`、`trackingIMM` 或 `trackingABF`。

为帮助您编写此函数，您可以在 MATLAB 中查看所提供的函数的详细信息。例如：

    type initcvekf

### **Maximum number of tracks** — 最大航迹数量 `200`（默认）| positive integer

模块可维护的最大航迹数量，指定为 positive integer。

### **Maximum number of sensors** — 最大传感器数量 `20`（默认）| positive integer

模块可处理的最大传感器数量，指定为 positive integer。此值应大于或等于 **Detections** 输入端口输入的最高 `SensorIndex` 值。

### **Out-of-sequence measurements handling** — 乱序测量处理 `Terminate`（默认）| `Neglect` | `Retrodiction`

乱序测量处理，指定为 `Terminate`、`Neglect` 或 `Retrodiction`。每个检测都有一个关联的时间戳 *t*d，跟踪器模块有自己的时间戳 *t*t，该时间戳在每次调用时更新。如果 *t*d < *t*t，则跟踪器模块将测量视为 OOSM。

当您将该参数指定为：

- `Terminate` — 当模块遇到乱序测量时停止运行。
- `Neglect` — 模块忽略任何乱序测量并继续运行。
- `Retrodiction` — 模块使用反演算法通过忽略 OOSM、更新现有航迹或使用 OOSM 创建新航迹来更新跟踪器。您必须在 **Filter initialization function** 参数中指定一个返回 `trackingKF`、`trackingEKF` 或 `trackingIMM` 对象的滤波器初始化函数。

如果将此参数指定为 `Retrodiction`，跟踪器按照以下步骤处理 OOSM：

- 如果 OOSM 时间戳超出跟踪器中维护的最旧校正时间戳（由 **Maximum number of OOSM steps** 参数指定），则跟踪器丢弃这些 OOSM。
- 如果 OOSM 时间戳在跟踪器维护的最旧校正时间戳范围内，则跟踪器首先将所有现有航迹反演到 OOSM 的时间。然后，跟踪器应用联合概率数据关联算法，尝试将 OOSM 关联到反演后的航迹。

  - 如果跟踪器成功将 OOSM 关联到至少一个反演后的航迹，则跟踪器通过应用反演校正算法使用这些 OOSM 更新反演后的航迹，以获得当前校正后的航迹。
  - 如果跟踪器无法将 OOSM 关联到任何反演后的航迹，则跟踪器基于该 OOSM 创建新航迹，并将该航迹预测到当前时间。

有关反演和反演校正算法的更多详细信息，请参阅 Retrodiction and Retro-Correction。要模拟乱序检测，请使用 `objectDetectionDelay`。

**注意**

- 当您选择 `Retrodiction` 时，不能使用 **Cost Matrix** 输入。

### **OOSM 最大步数** — OOSM 最大步数 `3`（默认）| positive integer

乱序量测（OOSM）的最大步数，指定为正整数。

增大此参数值需要更多内存，但允许您使用相对于模块上次更新时最后一个时间戳具有更大滞后的 OOSM 调用 tracker 模块。此外，随着滞后增大，OOSM 对航迹当前状态的影响会减弱。建议将此参数设置为 `3`。

#### 依赖关系

要启用此参数，请将 **乱序量测处理** 参数设置为 `Retrodiction`。

### **航迹状态参数** — 航迹状态参考坐标系结构的参数 | structure array

将航迹状态参考坐标系的参数指定为 structure 或 structure array。模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义报告航迹时所用的参考坐标系，或所生成航迹的其他所需属性。

例如，您可以使用以下 structure 来定义相对于 scenario frame 的矩形参考坐标系，其原点位置为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

您可以通过选择 **随时间更新航迹状态参数** 参数，经由 **State Parameters** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **随时间更新航迹状态参数** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数以启用通过 **State Parameters** 输入端口输入航迹状态参数的端口。

### **启用内存管理** — 启用内存管理 `off`（默认）| `on`

选择此参数以启用内存管理，使用 **每个传感器的最大检测数** 参数指定每个传感器在跟踪器的一次调用期间可以传递给跟踪器的最大检测数。此外，如果 **用于分配的航迹和检测聚类** 参数设置为 `on`，您还可以使用另外三个参数来指定跟踪器中某些可变大小数组的边界，以及确定跟踪器如何处理集群大小违规：

- **每个集群的最大检测数**
- **每个集群的最大航迹数**
- **处理运行时集群大小违规**

为可变大小数组指定边界允许您在生成的 C/C++ 代码中管理跟踪器的内存占用。

### **分配算法名称** — 分配算法名称 `'MatchPairs'`（默认）| `'Munkres'` | `'Jonker-Volgenant'` | `'Auction'` | `'Custom'`

分配算法，指定为 `'MatchPairs'`、`'Munkres'`、`'Jonker-Volgenant'`、`'Auction'` 或 `'Custom'`。Munkres 是唯一保证最优解的分配算法，但它也是最慢的，尤其是在检测和航迹数量很大时。其他算法不保证最优解，但对于具有 20 个或更多航迹和检测的问题可能更快。使用 `'Custom'` 定义您自己的分配函数，并在 `CustomAssignmentFcn` 属性中指定其名称。

### **'Custom' 分配函数的名称** — 自定义分配函数名称 character vector

自定义分配函数名称，指定为 character string。分配函数必须具有以下语法：

```
 [assignment,unTrs,unDets] = f(cost,costNonAssignment)
```

有关分配函数示例及其参数说明，请参阅 `assignmunkres`。

**示例：** `'mycustomfcn'`

#### 依赖关系

要启用此属性，请将 **分配算法名称** 名称设置为 `'Custom'`。

### **将检测分配给航迹的阈值** — 将检测分配给航迹的阈值 `30*[1 Inf]`（默认）| positive scalar | 1-by-2 vector of positive values

用于将检测分配给航迹的阈值（或门限阈值），指定为正标量或 [*C*1, *C*2*] 的 1×2 向量，其中 *C*1 ≤ *C*2。如果指定为标量，则指定值 *val* 将扩展为 [*val*, `Inf`]。

最初，跟踪器对所有航迹和检测之间的归一化距离执行粗略估计。跟踪器仅对粗略归一化距离小于 *C*2 的组合计算精确归一化距离。此外，仅当检测与航迹的精确归一化距离小于 *C*1 时，跟踪器才能将检测分配给航迹。有关归一化距离的说明，请参阅算法。

- 如果存在应计算用于分配但未计算的航迹和检测组合，请增大 *C*2 的值。如果代价计算耗时过长，请减小它。
- 如果存在应分配给航迹但未分配的检测，请增大 *C*1 的值。如果存在被分配给不应分配给它们的航迹（距离太远）的检测，请减小它。

**注意**

如果 *C*2 的值有限，则跟踪器中使用的跟踪滤波器所指定的状态转移函数和量测函数必须能够分别以 *M*×*N* 的状态矩阵作为输入，并输出 *N* 个预测状态和 *N* 个量测。*M* 是状态的大小。*N* 是状态数量，为任意非负整数。

### **用于分配的航迹和检测聚类** — 用于分配的航迹和检测聚类 `off`（默认）| `on`

将用于分配的航迹和检测聚类指定为：

- `off` — 跟踪器使用代价矩阵按传感器求解全局最近邻分配问题。代价矩阵的列数等于该传感器的检测数，行数等于跟踪器维护的航迹数。禁止的分配（代价大于 **将检测分配给航迹的阈值** 参数的分配）具有无限分配代价。
- `on` — 跟踪器在分离出禁止的分配（代价大于 **将检测分配给航迹的阈值** 参数的分配）后创建集群，并使用禁止的分配基于 **将检测分配给航迹的阈值** 参数形成新集群。*集群* 是一组（按传感器区分的）检测和被认为相互分配的航迹。在这种情况下，跟踪器按集群求解全局最近邻分配问题。

  当您将此属性指定为 `on` 并在 **Tracker Management** 选项卡中选择 **启用内存管理** 时，您可以使用以下三个参数来指定跟踪器中某些可变大小数组的边界，以及确定跟踪器如何处理集群大小违规：

  - **每个集群的最大检测数**
  - **每个集群的最大航迹数**
  - **处理运行时集群大小违规**

  为可变大小数组指定边界使您能够管理跟踪器的内存占用，尤其是在生成的 C/C++ 代码中。

### **仿真方式** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间。

#### 航迹逻辑

### **航迹确认和删除逻辑类型** — 确认和删除逻辑类型 `History`（默认）| `Score`

确认和删除逻辑类型，选择为 `History` 或 `Score`。

- `History` – 航迹确认和删除基于航迹在最近跟踪器更新中分配给检测的次数。
- `Score` – 航迹确认和删除基于对数似然航迹得分。得分高意味着航迹更可能有效。得分低意味着航迹更可能是虚警。

### **确认阈值 [M N]** — 历史逻辑的航迹确认阈值 `[2 3]`（默认）| real-valued 1-by-2 vector of positive integers

历史逻辑的航迹确认阈值，指定为实值 1×2 正整数向量 `[M N]`。如果航迹在最近 `N` 次更新中至少收到 `M` 次检测，则该航迹被确认。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `History`。

### **删除阈值 [P Q]** — 历史逻辑的航迹删除阈值 `[5 5]`（默认）| real-valued 1-by-2 vector of positive integers

历史逻辑的航迹删除阈值，指定为实值 1×2 正整数向量 `[P Q]`。如果已确认航迹在最近 `Q` 次跟踪器更新中未分配给任何检测达到 `P` 次，则该航迹被删除。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `History`。

### **确认阈值 [positive scalar]** — 得分逻辑的航迹确认阈值 `20`（默认）| positive scalar

得分逻辑的航迹确认阈值，指定为实值正标量。如果航迹得分至少与确认阈值一样高，则该航迹被确认。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `Score`。

### **删除阈值 [negative scalar]** — 得分逻辑的航迹删除阈值 `-7`（默认）| scalar | negative scalar

得分逻辑的航迹删除阈值，指定为负标量。如果航迹得分从最大航迹得分下降至少该阈值，则该航迹被删除。

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `Score`。

### **用于航迹得分的检测概率** — 用于航迹得分的检测概率 `0.9`（默认）| scalar in (0,1)

用于航迹得分的检测概率，指定为 (0,1) 中的正标量。

**示例：** `0.5`

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `Score`。

### **用于航迹得分的假阳性率** — 用于航迹得分的虚警概率 `1e-6`（默认）| scalar in (0,1)

用于航迹得分的虚警概率，指定为 (0,1) 中的标量。

**示例：** `1e-5`

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `Score`。

### **传感器检测单元体积** — 传感器检测单元体积 `1`（默认）| positive scalar

传感器检测单元的体积，指定为正标量。例如，如果雷达产生 4-D 量测，其中包括方位角、仰角、距离和距离变化率，则 4-D 体积由雷达角波束宽度、距离单元宽度和距离变化率单元宽度定义。体积用于在初始化和更新航迹时计算航迹得分。

**示例：** `1.5`

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `Score`。

### **每单位体积新航迹率** — 每单位体积新航迹率 `1`（默认）| positive scalar

每单位体积的新航迹率，指定为正标量。新航迹率用于在航迹初始化期间计算航迹得分。

**示例：** `2.5`

#### 依赖关系

要启用此参数，请将 **航迹确认和删除逻辑类型** 设置为 `Score`。

#### 端口设置

### **预测时间源** — 预测时间源 `Auto`（默认）| `Input port`

预测时间的源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **启用代价矩阵输入** — 启用代价矩阵输入端口 off（默认）| on

选中此复选框以启用通过 **Cost Matrix** 输入端口输入代价矩阵。

### **启用可检测航迹 ID 输入** — 启用可检测航迹 ID 输入 off（默认）| on

选中此复选框以启用 **Detectable track IDs** 输入端口。

### **启用暂定航迹输出** — 启用暂定航迹输出端口 off（默认）| on

选中此复选框以启用通过 **Tentative Tracks** 输出端口输出暂定航迹。

### **启用所有航迹输出** — 启用所有航迹输出端口 off（默认）| on

选中此复选框以启用通过 **All Tracks** 输出端口输出所有航迹。

### **启用信息输出** — 启用分析信息输出端口 off（默认）| on

选中此复选框以启用通过 **Info** 输出端口输出分析信息。

### **输出总线名称来源** — 输出航迹总线名称来源 `Auto`（默认）| `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 使用 **指定输出总线名称** 参数指定输出航迹总线名称。

### **输出信息总线名称来源** — 输出信息总线名称来源 `Auto`（默认）| `Property`

输出信息总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 使用 **指定输出总线名称** 参数指定输出信息总线名称。

#### 内存管理

### **每个传感器的最大检测数** — 每个传感器的最大检测数 `100`（默认）| positive integer

将每个传感器的最大检测数指定为正整数。此参数确定每个传感器在每次调用跟踪器时可以传递给跟踪器的最大检测数。

如果希望跟踪器为 C/C++ 代码生成建立局部变量的有效边界，请将此参数设置为有限值。如果不希望限制每个传感器的最大检测数，请将此属性设置为 `Inf`。

#### 依赖关系

要启用此参数，请在 **Tracker Management** 选项卡中选择 **启用内存管理**。

### **每个集群的最大检测数** — 每个集群的最大检测数 `5`（默认）| positive integer

将跟踪器运行时每个集群的最大检测数指定为正整数。

将此参数设置为有限值允许跟踪器限制集群大小，并减少生成的 C/C++ 代码中跟踪器的内存占用。如果不希望限制每个集群的最大检测数，请将此属性设置为 `Inf`。

如果在运行时，集群中的检测数超过此参数，则跟踪器会根据 **处理运行时集群大小违规** 参数做出反应。

#### 依赖关系

要启用此参数，请将 **用于分配的航迹和检测聚类** 指定为 `on`，并在 **Tracker Management** 选项卡中选择 **启用内存管理**。

### **每个簇的最大轨迹数** — 每个簇的最大轨迹数 `5`（默认）| 正整数

将跟踪器运行期间每个簇的最大轨迹数指定为正整数。

将此参数设置为有限值可使跟踪器限制簇大小，并减少生成的 C/C++ 代码中跟踪器的内存占用。如果不希望限制每个簇的最大检测数，请将此属性设置为 `Inf`。

如果在运行期间，一个簇中的轨迹数超过此参数，则跟踪器会根据 **处理运行时簇大小违规** 参数做出反应。

#### 依赖关系

要启用此参数，请将 **为分配而聚类轨迹和检测** 指定为 `on`，并在 **跟踪器管理** 选项卡中选择 **启用内存管理**。

### **处理运行时簇大小违规** — 处理运行时簇大小违规 `Auto`（默认）| `Property`

将运行时簇大小违规的处理方式指定为以下选项之一：

- `Teminate` — 如果在运行期间任何簇违反 **每个簇的最大检测数** 和 **每个簇的最大轨迹数** 参数指定的簇边界，则跟踪器会报告错误。
- `Split and warn` — 跟踪器使用次优方法将违反大小限制的簇拆分为较小的簇。跟踪器还会报告警告以指示该违规。
- `Split` — 跟踪器使用次优方法将违反大小限制的簇拆分为较小的簇。跟踪器不报告警告。

在次优方法中，跟踪器分离出与其他轨迹或检测的关联似然最小的检测或轨迹，直到满足簇边界。这些分离出的检测或轨迹可以形成一个或多个新簇，具体取决于它们彼此的关联似然以及 **将检测分配给轨迹的阈值** 参数。

#### 依赖关系

要启用此参数，请将 **为分配而聚类轨迹和检测** 指定为 `on`，并在 **跟踪器管理** 选项卡中选择 **启用内存管理**。

## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法说明和限制：

- 该模块支持 *严格单精度* 代码生成，但有以下限制：

  - 必须将分配算法指定为 `'Jonker-Volgenant'`。
  - 必须将滤波器初始化函数指定为返回配置为单精度的 `trackingEKF`、`trackingUKF`、`trackingCKF` 或 `trackingIMM` 对象。

  有关详细信息，请参阅使用严格单精度和非动态内存分配生成代码。

- 跟踪器支持 *非动态内存分配* 代码生成，但有以下限制：

  - 必须将分配算法指定为 `'Jonker-Volgenant'` 或 `'MatchPairs'`。
  - 必须将滤波器初始化函数指定为返回 `trackingEKF`、`trackingUKF`、`trackingCKF` 或 `trackingIMM` 对象。

  有关详细信息，请参阅使用严格单精度和非动态内存分配生成代码。

  启用非动态内存分配代码生成后，请考虑使用以下参数为跟踪器中的局部变量设置边界：

  - **启用内存管理**
  - **为分配而聚类轨迹和检测**
  - **每个传感器的最大检测数**
  - **每个簇的最大检测数**
  - **每个簇的最大轨迹数**
  - **处理运行时簇大小违规**

- 在代码生成中，如果检测输入指定为 `double` 精度，则轨迹输出的 `NumTracks` 字段将返回为 `double` 变量。如果检测输入指定为 `single` 精度，则轨迹输出的 `NumTracks` 字段将返回为 `uint32` 变量。

## 版本历史

**在 R2019b 中引入**

### R2023a: Simulink 总线不在工作区中显示

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

使用 GNN 分配的多传感器、多目标跟踪器

Global Nearest Neighbor Multi Object Tracker 模块能够处理来自多个传感器的多个目标的检测，非常类似于 `trackerGNN` System object™。该跟踪器基于全局最近邻 (GNN) 分配算法初始化、确认、预测、校正和删除轨迹。该跟踪器为每个轨迹估计状态向量和状态向量协方差矩阵。每个检测最多分配给一个轨迹。如果检测无法分配给任何轨迹，跟踪器将初始化一个新轨迹。

任何新轨迹都从暂定状态开始。如果有足够的检测分配给暂定轨迹，其状态将变为已确认。如果检测已经具有已知分类（返回轨迹的 `ObjectClassID` 字段非零），则该轨迹会立即确认。当轨迹被确认后，跟踪器认为该轨迹表示一个物理对象。如果在可指定数量的更新内没有检测分配给该轨迹，则删除该轨迹。
