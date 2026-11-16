---
type: simulink-block
title: 'Track-Oriented Multi-Hypothesis Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'trackorientedmultihypothesistracker'
documentation_source_path: 'ref/trackorientedmultihypothesistracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Track-Oriented Multi-Hypothesis Tracker

## 端口

### 输入

### **Detections** — 检测列表，包含 MATLAB® 结构的 Simulink® 总线

检测列表，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数 | Integer |
| `Detections` | 目标检测 | `objectDetection` 结构的数组。这些检测中的前 `NumDetections` 个是实际检测。 |

检测结构的字段如下：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 测量时间 | `Single` or `Double` |
| `Measurement` | 目标测量 | `Single` or `Double` |
| `MeasurementNoise` | 测量噪声协方差矩阵 | `Single` or `Double` |
| `SensorIndex` | 传感器的唯一 ID | `Single` or `Double` |
| `ObjectClassID` | 目标分类 ID | `Single` or `Double` |
| `MeasurementParameters` | 跟踪滤波器的初始化函数所使用的参数 | Simulink Bus |
| `ObjectAttributes` | 传递给跟踪器的附加信息 | Simulink Bus |

有关这些字段的更详细说明，请参阅 `objectDetection`。

**注意**

目标检测结构包含一个 `Time` 字段。每个目标检测的时间标签必须小于或等于该模块当前调用时的时间。时间标签还必须大于该模块上一次调用时指定的更新时间。

### **Prediction Time** — 航迹更新时间 real scalar

航迹更新时间，指定为以 seconds 为单位的 real scalar。跟踪器将所有航迹更新到该时间。每次调用该模块时，更新时间必须始终增加。更新时间必须至少与 **Detections** 输入端口中所指定的最大 `Time` 一样大。

如果未启用该端口，则由 Simulink 管理的仿真时钟确定更新时间。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，将 **预测时间源** 设置为 `Input port`。

### **Cost Matrix** — 代价矩阵，实值 *N*×*M* 矩阵

代价矩阵，指定为实值 *N*×*M* 矩阵，其中 *N* 是分支数，*M* 是当前检测数。

代价矩阵的行必须与分支列表的顺序相同。分支按照它们在该模块上一次调用时 **All Branches** 输出端口的分支列表中出现的顺序排序。列对应于检测。

在对跟踪器的第一次更新中，或者如果跟踪器没有先前的航迹，则将代价矩阵的大小指定为 [0, *N*]。计算代价时必须使较低的代价表示跟踪器将检测分配给航迹的可能性较高。要阻止某些检测分配给某些航迹，请使用 `Inf`。

如果未启用此端口，则由 **滤波器初始化函数** 初始化的滤波器使用距离方法计算代价矩阵。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用代价矩阵输入**。

### **Detectable BranchIDs** — 可检测分支 ID，实值 *M*×1 向量 | 实值 *M*×2 矩阵

可检测分支 ID，指定为实值 *M*×1 向量或 *M*×2 矩阵。可检测分支是传感器预期检测到的分支。矩阵的第一列包含传感器报告为可检测的分支 ID 列表。可选的第二列使您能够为每个分支添加检测概率。分支列在该模块上一次调用的 **All Branches** 输出中。

其标识符未包含在 **Detectable BranchIDs** 中的航迹被视为不可检测。航迹删除逻辑不会将未检测到计为用于航迹删除目的的“漏检”。

如果未启用此端口，则跟踪器在该模块的每次调用时都假定所有航迹均可检测。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用可检测分支 ID 输入**。

### **State Parameters** — 航迹状态参数，包含 MATLAB 结构的 Simulink 总线

航迹状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构的数组 |

该模块将 `Parameters` 字段的值用于所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义报告航迹时所用的参考坐标系，或所生成航迹的其他所需属性。

例如，您可以使用以下结构来定义一个矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **跟踪器配置** 选项卡中，选择 **随时间更新航迹状态参数** 参数。

### 输出

### **Confirmed Tracks** — 确认航迹，包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数 |
| `Tracks` | 航迹结构数组，其长度由 **最大航迹数** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如“航迹结构”中所示。

如果航迹满足 **航迹逻辑** 选项卡下 **确认阈值** 参数中指定的阈值，则该航迹被确认。

### **Tentative Tracks** — 暂定航迹，包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在被确认之前为暂定航迹。

航迹结构的字段如“航迹结构”中所示。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用暂定航迹输出**。

### **All Tracks** — 确认航迹和暂定航迹，包含 MATLAB 结构的 Simulink 总线

确认航迹和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。

航迹结构的字段如“航迹结构”中所示。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用所有航迹输出**。

### **Info** — 用于分析航迹更新的附加信息，包含 MATLAB 结构的 Simulink 总线

用于分析航迹更新的附加信息，返回为包含 MATLAB 结构的 Simulink 总线。

下表显示了 info 结构的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `OOSMDetectionIndices` | 乱序测量的索引 |
| `BranchIDsAtStepBeginning` | 更新开始时的分支 ID。 |
| `CostMatrix` | 运动学分配矩阵的代价，其中 (*i*, *j*) 元素表示将航迹 *i* 分配给检测 *j* 的代价。 |
| `Assignments` | 从 `assignTOMHT` 函数返回的分配。 |
| `UnassignedTracks` | 跟踪器返回的未分配分支 ID。 |
| `UnassignedDetections` | 跟踪器返回的未分配检测 ID。 |
| `InitialBranchHistory` | 分支后且剪枝前的分支历史。 |
| `InitialBranchScores` | 剪枝前的分支得分。 |
| `KeptBranchHistory` | 初始剪枝后的分支历史。 |
| `KeptBranchScores` | 初始剪枝后的分支得分。 |
| `Clusters` | 将分支映射到聚类的逻辑数组。如果分支在其历史中共享检测，或者直接或通过其他分支属于同一航迹，则它们属于同一聚类。 |
| `TrackIncompatibility` | 分支不兼容矩阵。如果第 *i* 个和第 *j* 个分支在其历史中共享检测或属于同一航迹，则 `(i,j)` 元素为 true。 |
| `GlobalHypotheses` | 将分支映射到全局假设的逻辑矩阵。兼容的分支可以属于同一假设。 |
| `GlobalHypScores` | 全局假设的总得分。 |
| `PrunedBranches` | `pruneTrackBranches` 函数确定为要剪枝的分支的逻辑数组。 |
| `GlobalBranchProbabilities` | 每个分支在全局假设中存在的全局概率。 |
| `BranchesDeletedByPruning` | 被跟踪器删除的分支。 |
| `BranchIDsAtStepEnd` | 更新结束时的分支 ID。 |

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用信息输出**。

### **All Branches** — 所有分支，包含 MATLAB 结构的 Simulink 总线

所有分支，返回为包含 MATLAB 结构的 Simulink 总线。

分支结构的字段与航迹结构相同。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用所有分支输出**。

## 参数

#### 跟踪器管理

### **跟踪器标识符** — 唯一跟踪器标识符 `0`（默认）| 非负整数

唯一跟踪器标识符，指定为非负整数。此参数在跟踪器输出中作为 `SourceIndex` 传递，并区分多跟踪器系统中来自不同跟踪器的航迹。要将航迹输出用作 `trackFuser` 对象的输入，必须将此属性指定为正整数。

**示例：** `1`

### **滤波器初始化函数** — 滤波器初始化函数 `@initcvekf`（默认）| 函数名

滤波器初始化函数，指定为滤波器初始化函数的名称。跟踪器在创建新航迹时使用滤波器初始化函数。

Sensor Fusion and Tracking Toolbox™ 提供了许多与该模块兼容的初始化函数。

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

此函数的输入是检测报告，类似于由 `objectDetection` 对象创建的检测报告。此函数的输出必须是滤波器对象：`trackingKF`、`trackingEKF`、`trackingUKF`、`trackingCKF`、`trackingPF`、`trackingMSCEKF`、`trackingGSF`、`trackingIMM` 或 `trackingABF`。

为指导您编写此函数，您可以在 MATLAB 中查看受支持函数的详细信息。例如：

```
type initcvekf
```

### **将检测分配给航迹的阈值** — 将检测分配给航迹的阈值 `30*[0.3 0.7 1 Inf]`（默认）| 正标量 | 1×3 正值向量 | 1×4 正值向量

将检测分配给航迹的阈值，指定为正标量、由非递减正值组成的 1×3 向量 [*C*1,*C*2,*C*3]，或由非递减正值组成的 1×4 向量 [*C*1,*C*2,*C*3,*C*4]。如果指定为标量，则指定值 *val* 将扩展为 [0.3,0.7,1,`Inf`]\**val*。如果指定为 [*C*1,*C*2,*C*3]，则将扩展为 [*C*1,*C*2,*C*3,`Inf`]。

这些阈值控制 (1) 将检测分配给航迹，(2) 从检测创建新分支，以及 (3) 从未分配航迹创建新分支。阈值必须满足：*C*1 <= *C*2 <= *C*3 <= *C*4。

- *C*1 定义了一个距离，使得如果航迹分配到的检测距离小于 *C*1，则该航迹不再被视为未分配，并且不会创建未分配航迹分支。
- *C*2 定义了一个距离，使得如果检测已分配给距离小于 *C*2 的航迹，则该检测不再被视为未分配，并且不会创建新航迹分支。
- *C*3 定义了将检测分配给航迹的最大距离。
- *C*4 定义了要执行精确归一化代价计算的航迹和检测组合。最初，跟踪器对所有航迹和检测之间的归一化距离执行粗略估计。跟踪器仅对粗略归一化距离小于 *C*4 的组合计算精确归一化距离。

有关归一化距离的说明，请参阅算法。

- 如果存在应分配给航迹但未分配的检测，则增大 *C*3 的值。如果存在被分配给不应分配给它们的航迹（距离太远）的检测，则减小该值。
- 增大 *C*1 和 *C*2 的值有助于控制所创建的航迹分支数。但是，这样做会减少每个航迹拥有的分支（假设）数。
- 如果存在应为分配进行计算但未计算的航迹和检测组合，则增大 *C*4 的值。如果代价计算耗时过长，则减小该值。

**注意**

如果 *C*4 的值是有限的，则跟踪器中使用的跟踪滤波器所指定的状态转移函数和测量函数必须能够分别接受 *M*×*N* 的状态矩阵作为输入，并输出 *N* 个预测状态和 *N* 个测量。*M* 是状态的大小。*N* 是状态数，为任意非负整数。

**数据类型：** `single` | `double`

### **最大航迹数** — 最大航迹数 `100`（默认）| 正整数

该模块可以维护的最大航迹数，指定为正整数。

### **最大传感器数** — 最大传感器数 `20`（默认）| 正整数

可以连接到跟踪器的最大传感器数，指定为正整数。`MaxNumSensors` 必须大于或等于用于更新跟踪器的所有检测中找到的 `SensorIndex` 的最大值。`SensorIndex` 是 `objectDetection` 对象的一个属性。该模块的 `MaxNumSensors` 属性决定每个输出航迹可以拥有多少组 `ObjectAttributes` 字段。

### **乱序测量处理** — 乱序测量处理 `Terminate` (默认) | `neglect`

乱序测量处理，指定为 `Terminate` 或 `neglect`。每个检测都有一个与之关联的时间戳，*t*d，而跟踪器模块有自己的时间戳，*t*t，该时间戳在每次调用时更新。如果 *t*d < *t*t，跟踪器模块将测量视为 OOSM。

当该参数指定为：

- `Terminate` — 当遇到任何乱序测量时，模块停止运行。
- `Neglect` — 模块忽略任何乱序测量并继续运行。

若要模拟乱序检测，请使用 `objectDetectionDelay`。

### **航迹状态参数** — 航迹状态参考系结构的参数 | structure array

将航迹状态参考系的参数指定为结构体或结构体数组。模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义报告航迹时所用的参考系，或所生成航迹的其他所需属性。

例如，可以使用以下结构体定义一个矩形参考系，其原点位置相对于场景坐标系为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

通过选择 **Update track state parameters with time** 参数，您可以通过 **State Parameters** 输入端口更新航迹状态参数。

**数据类型:** `struct`

### **随时间更新航迹状态参数** — 随时间更新航迹状态参数 `off` (默认) | `on`

选择此参数可通过 **State Parameters** 输入端口启用航迹状态参数的输入端口。

### **航迹输出方法** — 航迹输出方法 `'Tracks'` (默认) | `'Hypothesis'` | `'Clusters'`

航迹输出方法，指定为 `'Tracks'`、`'Hypothesis'` 或 `'Clusters'`。

- `'Tracks'` – 基于每条航迹的航迹分支输出每条航迹的质心。
- `'Hypothesis'` – 输出处于特定假设中的分支。如果选择此选项，请使用 `HypothesesToOutput` 属性列出要输出的假设。
- `'Clusters'` – 输出每个聚类的质心。与 `'Tracks'` 输出类似，但包含一个聚类内的所有航迹。

**数据类型:** `char`

### **仿真方式** — 要运行的仿真类型 `Interpreted Execution` (默认) | `Code Generation`

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间。

#### 假设管理

### **要维护的最大假设数** — 要维护的最大假设数 `5` (默认) | 正整数

跟踪器在每一步维护的全局分配假设的最大数量，指定为正整数。如果假设数量大于该属性值，跟踪器会修剪似然较低的假设及其关联分支，直到假设数量达到该属性值。较大的值会增加计算负载。

**示例:** `10`

**数据类型:** `single` | `double`

### **每条航迹的最大航迹分支数** — 每条航迹的最大航迹分支数 `3` (默认) | 正整数

每条航迹允许的最大航迹分支数，指定为正整数。较大的值会增加计算负载。

**数据类型:** `single` | `double`

### **分支历史中维护的最大扫描数** — 分支历史中维护的最大扫描数 `4` (默认) | 正整数

分支历史中维护的最大扫描数，指定为正整数。航迹历史扫描数通常为 2 到 6。较大的值会增加计算负载。

**数据类型:** `single` | `double`

### **保留分支所需的最小概率** — 保留分支所需的最小概率 `.001` (默认) | 正标量

保留航迹分支所需的最小概率，指定为小于 1 的正标量。任何概率低于指定概率的航迹都会被修剪。典型值为 0.001 到 0.005。

**示例:** `.003`

**数据类型:** `single` | `double`

### **N-scan 修剪方法** — N-scan 修剪方法 `'None'` (默认) | `'Hypothesis'`

N-scan 修剪方法，指定为 `'None'` 或 `'Hypothesis'`。在 N-scan 修剪中，如果同一航迹的分支在 N 次扫描历史中与同一航迹最可能的分支矛盾，则这些分支会被修剪（删除）。最可能分支的定义方式有以下两种：

- `'None'` – 不执行 N-scan 修剪。
- `'Hypothesis'` – 所选分支位于最可能的假设中。

**示例:** `'Hypothesis'`

#### 航迹逻辑

### **确认阈值 [正标量]** — 确认航迹所需的最低分数 `20` (默认) | 正标量

确认航迹所需的最低分数，指定为正标量。任何分数高于此阈值的航迹都会被确认。

**示例:** `12`

**数据类型:** `single` | `double`

### **删除阈值 [负标量]** — 航迹删除的最大分数下降 `-7` (默认) | 标量

航迹被删除前的最大分数下降，指定为标量。任何分数从最高分数下降超过此参数的航迹都会被删除。删除阈值受虚警概率影响。

**示例:** `-1`

**数据类型:** `single` | `double`

### **用于航迹分数的检测概率** — 用于航迹分数的检测概率 `0.9` (默认) | 0 到 1 之间的正标量

检测概率，指定为 0 到 1 之间的正标量。此属性用于计算航迹分数。

**示例:** `0.5`

**数据类型:** `single` | `double`

### **用于航迹分数的误报率** — 用于航迹分数的虚警概率 `1e-6` (默认) | 标量

虚警概率，指定为标量。此属性用于计算航迹分数。

**示例:** `1e-5`

**数据类型:** `single` | `double`

### **传感器检测单元的体积** — 传感器测量单元的体积 `1` (默认) | 正标量

传感器测量单元的体积，指定为正标量。例如，如果雷达生成 4-D 测量，其中包括方位角、俯仰角、距离和距离变化率，则 4-D 体积由雷达角波束宽度、距离单元宽度和距离变化率单元宽度定义。在初始化和更新航迹时，体积用于计算航迹分数。

**示例:** `1.5`

**数据类型:** `single` | `double`

### **单位体积的新航迹率** — 单位体积的新航迹率 `1` (默认) | 正标量

单位体积的新航迹率，指定为正标量。该参数用于在航迹初始化期间计算航迹分数。

**示例:** `2.5`

**数据类型:** `single` | `double`

#### 端口设置

### **预测时间源** — 预测时间的来源 `Auto` (默认) | `Input port`

预测时间的来源，指定为 `Input port` 或 `Auto`。选择 `Input port` 可通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **启用代价矩阵输入** — 启用代价矩阵输入端口 off (默认) | on

选择此参数可通过 **Cost Matrix** 输入端口启用代价矩阵输入。

### **启用可检测分支 ID 输入** — 启用可检测分支 ID 输入 off (默认) | on

选择此参数以启用 **Detectable branch IDs** 输入端口。

### **启用暂定航迹输出** — 启用暂定航迹输出端口 off (默认) | on

选择此参数以通过 **Tentative Tracks** 输出端口启用暂定航迹输出。

### **启用所有航迹输出** — 启用所有航迹输出端口 off (默认) | on

选择此参数以通过 **All Tracks** 输出端口启用所有航迹输出。

### **启用信息输出** — 启用分析信息输出端口 off (默认) | on

选择此参数以通过 **Info** 输出端口启用分析信息输出端口。

### **启用所有分支输出** — 启用所有分支输出端口 off (默认) | on

选择此参数以通过 **All Branches** 输出端口启用所有分支输出。

### **输出总线名称的来源** — 输出航迹总线名称的来源 `Auto` (默认) | `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 使用 **Specify an output bus name** 参数指定输出航迹总线名称。

### **输出信息总线名称的来源** — 输出信息总线名称的来源 `Auto` (默认) | `Property`

输出信息总线名称的来源，指定为：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 使用 **Specify an output info bus name** 参数指定输出信息总线名称。

#### 依赖项

要启用此参数，请在 **Port Setting** 选项卡上选择 **Enable information output**。

## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 在代码生成中，如果检测输入以 `double` 精度指定，则航迹输出的 `NumTracks` 字段以 `double` 变量返回。如果检测输入以 `single` 精度指定，则航迹输出的 `NumTracks` 字段以 `uint32` 变量返回。

## 版本历史

**在 R2020a 中引入**

### R2023a: Simulink 总线不再显示在工作区中

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

Track-Oriented Multi-Hypothesis Tracker

Track-Oriented Multi-Hypothesis Tracker 模块处理来自多个传感器的多目标检测。跟踪器模块会初始化、确认、预测、校正和删除航迹。跟踪器模块的输入是由 `objectDetection`、`fusionRadarSensor`、`irSensor` 或 `sonarSensor` 对象生成的检测报告。跟踪器模块估计每条航迹的状态向量和状态向量协方差矩阵。跟踪器基于面向航迹的多假设方法分配检测。

任何新航迹都从 *暂定* 状态开始。如果有足够的检测分配给暂定航迹，其状态将变为 *已确认*。如果检测已经具有已知分类（返回航迹的 `ObjectClassID` 字段非零），则该航迹会立即被确认。当航迹被确认后，多目标跟踪器会将该航迹视为代表一个物理对象。如果在可指定次数的更新内没有检测分配给该航迹，则该航迹会被删除。有关跟踪器工作原理的概述，请参阅算法。
