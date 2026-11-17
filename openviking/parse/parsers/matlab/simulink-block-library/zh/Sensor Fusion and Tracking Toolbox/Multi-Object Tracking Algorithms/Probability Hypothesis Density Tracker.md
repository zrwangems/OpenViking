---
type: simulink-block
title: 'Probability Hypothesis Density (PHD) Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'probabilityhypothesisdensityphdtracker'
documentation_source_path: 'ref/probabilityhypothesisdensityphdtracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Probability Hypothesis Density (PHD) Tracker

## 端口
```yaml
ports:
- name: Detections
  summary: 检测列表 包含 MATLAB® 结构的 Simulink® 总线
  direction: input
- name: Prediction Time
  summary: 航迹更新时间 实数标量
  direction: input
- name: Sensor Configurations
  summary: 跟踪传感器的配置 包含 MATLAB 结构的 Simulink 总线
  direction: input
- name: State Parameters
  summary: 跟踪状态参数，指定为包含 MATLAB 结构的 Simulink 总线
  direction: input
- name: Confirmed Tracks
  summary: 确认航迹，包含 MATLAB 结构的 Simulink 总线
  direction: output
- name: Tentative Tracks
  summary: 暂定航迹，包含 MATLAB 结构的 Simulink 总线
  direction: output
- name: All Tracks
  summary: 确认和暂定航迹，包含 MATLAB 结构的 Simulink 总线
  direction: output
- name: Info
  summary: 用于分析航迹更新的附加信息 Simulink 总线，包含 MATLAB 结构体
  direction: output
```

### 输入

### **Detections** — 检测列表 包含 MATLAB® 结构的 Simulink® 总线

检测列表，指定为包含 MATLAB 结构的 Simulink 总线。该结构具有以下形式：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | 整数。 |
| `Detections` | 目标检测 | 目标检测结构体数组。这些检测中的前 `NumDetections` 个为实际检测。 |

`Detections` 的字段为：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `Time` | 测量时间 | `single` 或 `double` |
| `Measurement` | 目标测量值 | `single` 或 `double` |
| `MeasurementNoise` | 测量噪声协方差矩阵 | `single` 或 `double` |
| `SensorIndex` | 传感器的唯一 ID | `single` 或 `double` |
| `ObjectClassID` | 目标分类 ID | `single` 或 `double` |
| `MeasurementParameters` | 跟踪滤波器初始化函数使用的参数 | Simulink 总线 |
| `ObjectAttributes` | 传递给跟踪器的附加信息 | Simulink 总线 |

有关这些字段的更详细说明，请参阅 `objectDetection`。

**注意**

目标检测结构包含一个 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用时刻的时间。该时间标签还必须大于模块上一次调用时指定的更新时间。

### **Prediction Time** — 航迹更新时间 实数标量

航迹更新时间，指定为以秒为单位的实数标量。跟踪器将所有航迹更新到该时间。每次调用模块时，更新时间必须递增。单位为秒。更新时间必须至少与 **Detections** 输入端口指定的最大 `Time` 一样大。

如果未启用此端口，则由 Simulink 管理的仿真时钟决定更新时间。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，将 **Prediction time source** 设置为 `Input port`。

### **Sensor Configurations** — 跟踪传感器的配置 包含 MATLAB 结构的 Simulink 总线

跟踪传感器的配置，指定为包含 MATLAB 结构的 Simulink 总线。该结构具有以下形式：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumConfigurations` | 传感器配置数量 | 整数。 |
| `Configurations` | 传感器配置 | 传感器配置结构体数组。这些配置中的前 `NumConfigurations` 个为实际配置。字段名称和定义必须分别对应于 `trackingSensorConfiguration` 对象属性的名称和值。如果在跟踪系统中使用 Radar Data Generator (Radar Toolbox) 模块，则可以直接使用 Radar Data Generator (Radar Toolbox) 模块的 **Configuration** 输出来指定此值。 |

#### 依赖关系

要启用此端口，请在 **Tracker** 选项卡中，选中 **Update sensor configurations with time** 参数。

### **State Parameters** — 跟踪状态参数，指定为包含 MATLAB 结构的 Simulink 总线

跟踪状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构体数组 |

该模块使用 `Parameters` 字段的值作为所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹上报的参考坐标系，或所生成航迹的其他期望属性。

例如，您可以使用以下结构来定义一个矩形参考坐标系，其原点位置为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒（相对于场景坐标系）。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **Tracker Configuration** 选项卡中，选择 **Update track state parameters with time** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹，包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构体数组，其长度由 **Maximum number of tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如航迹结构所示。

### **Tentative Tracks** — 暂定航迹，包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在确认之前为暂定航迹。此端口的输出与 **Confirmed Tracks** 端口的输出具有相同的形式。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable tentative tracks output**。

### **All Tracks** — 确认和暂定航迹，包含 MATLAB 结构的 Simulink 总线

确认和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。此端口的输出与 **Confirmed Tracks** 端口的输出具有相同的形式。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable all tracks output**。

### **Info** — 用于分析航迹更新的附加信息 Simulink 总线，包含 MATLAB 结构体

用于分析航迹更新的附加信息，以包含 MATLAB 结构体的 Simulink 总线形式返回。

下表显示了 info 结构体的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `CorrectionOrder` | 用于状态估计校正的传感器顺序，以 `SensorIndex` 值的行向量形式返回。例如，[1 3 2 4]。 |
| `TrackIDsAtStepBeginning` | 步开始时航迹的 ID。 |
| `DeletedTrackIDs` | 步期间删除的航迹的 ID。 |
| `TrackIDsAtStepEnd` | 步结束时航迹的 ID。 |
| `SensorAnalysisInfo` | 传感器分析信息的元胞数组。 |

`SensorAnalysisInfo` 字段可以包含多个传感器信息报告。每个报告是一个包含以下字段的结构体：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `SensorIndex` | 传感器索引。 |
| `DetectionCells` | 检测单元，以逻辑矩阵形式返回。矩阵的每一列表示一个检测单元。在每一列中，如果第 *i* 个元素为 1，则第 *i* 个检测属于该列所表示的检测单元。 |
| `DetectionLikelihoods` | 密度函数中的分量与检测单元之间的关联似然，以 *N*×*P* 矩阵形式返回。*N* 是密度函数中的分量数，*P* 是检测单元数。 |
| `IsBirthCells` | 指示 `DetectionCells` 中列出的检测单元是否生成新航迹，以 1×*P* 逻辑向量形式返回，其中 *P* 是检测单元数。 |
| `NumPartitions` | 分区数。 |
| `DetectionProbability` | 现有航迹被传感器检测到的概率，以 1×*N* 行向量形式返回，其中 *N* 是密度函数中的分量数。 |
| `LabelsBeforeCorrection` | 校正前密度函数中分量的标签，以 1×*M*b 行向量形式返回。*M*b 是校正前跟踪器中维护的分量数。向量的每个元素是一个 `TrackID`。例如，[1 1 2 0 0]。注意多个分量可以共享相同的 `TrackID`。 |
| `LabelsAfterCorrection` | 校正后密度函数中分量的标签，以 1×*M*a 行向量形式返回。*M*a 是校正后跟踪器中维护的分量数。向量的每个元素是一个 `TrackID`。例如，[1 1 1 2 2 0 0]。注意多个分量可以共享相同的 `TrackID`。 |
| `WeightsBeforeCorrection` | 校正前密度函数中分量的权重，以 1×*M*b 行向量形式返回。*M*b 是校正前跟踪器中维护的分量数。向量的每个元素是 `LabelsBeforeCorrection` 中对应分量的权重。例如，[0.1 0.5 0.7 0.3 0.2]。 |
| `WeightsAfterCorrection` | 校正后密度函数中分量的权重，以 1×*M*a 行向量形式返回。*M*a 是校正后跟踪器中维护的分量数。向量的每个元素是 `LabelsAfterCorrection` 中对应分量的权重。例如，[0.1 0.4 0.2 0.6 0.3 0.2 0.2]。 |

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡中，选择 **Enable information output**。
## 参数
```yaml
parameters:
- name: Tracker identifier
  summary: 唯一跟踪器标识符 0（默认）| 非负整数
  group: ''
- name: Detection partition function
  summary: 用于将检测划分为检测单元的函数 partitionDetections（默认）| 函数名
  group: ''
- name: Assignment threshold
  summary: 用于选择检测以初始化分量的阈值 25（默认）| 正实数标量
  group: ''
- name: Maximum number of sensors
  summary: 最大传感器数量 20（默认）| 正整数
  group: ''
- name: Maximum number of tracks
  summary: 最大航迹数量 1000（默认）| 正整数
  group: ''
- name: Maximum number of components
  summary: 最大分量数量 1000（默认）| 正整数
  group: ''
- name: Sensor configurations
  summary: 跟踪传感器的配置 struct('SensorIndex',1,'IsValidTime',true)（默认）| 结构体 | 结构体数组
  group: ''
- name: Update sensor configurations with time
  summary: 随时间更新传感器配置 off（默认）| on
  group: ''
- name: Track state parameters
  summary: 航迹状态参考坐标系结构的参数 | 结构体数组
  group: ''
- name: Update track state parameters with time
  summary: 随时间更新航迹状态参数 off（默认）| on
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted Execution（默认）| Code Generation
  group: ''
- name: Birth rate of new targets
  summary: 新目标的出生率（以密度计） 1e-3（默认）| 正实数标量
  group: ''
- name: Death rate of components
  summary: 分量的消亡率（以密度计） 1e-6（默认）| 正实数标量
  group: ''
- name: Threshold for initializing tentative tracks
  summary: 初始化暂定航迹的阈值 0.5（默认）| 正实数标量
  group: ''
- name: Threshold for track confirmation
  summary: 航迹确认阈值 0.8（默认）| 正实数标量
  group: ''
- name: Threshold for track deletion
  summary: 分量删除阈值 1e-3（默认）| 正实数标量
  group: ''
- name: Threshold for components merging
  summary: 分量合并阈值 25（默认）| 正实数标量
  group: ''
- name: Thresholds for label management
  summary: 标签管理阈值 [1.1 1 0.8]（默认）| 1×3 正数值向量
  group: ''
- name: Prediction time source
  summary: 预测时间来源 Auto（默认）| Input port
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
```

#### 跟踪器配置

### **Tracker identifier** — 唯一跟踪器标识符 `0`（默认）| 非负整数

将唯一跟踪器标识符指定为非负整数。此参数作为跟踪器输出中的 `SourceIndex` 传递，用于区分多跟踪器系统中来自不同跟踪器的航迹。您必须将此属性指定为正整数，才能将航迹输出用作 Track-To-Track Fuser 模块的输入。

**示例：** `1`

### **Detection partition function** — 用于将检测划分为检测单元的函数 `partitionDetections`（默认）| 函数名

用于将检测划分为检测单元的函数，指定为函数名。
当每个传感器可以对一个目标报告多个检测时，必须使用划分函数。划分函数报告来自一个传感器的检测的所有可能划分。在每个划分中，检测被分离为互斥的检测单元，假设每个检测单元属于一个扩展目标。

你也可以指定自己的检测划分函数。有关编写此函数的指导，你可以使用 `type` 命令检查默认划分函数 `partitionDetections` 的详细信息：

```
type partitionDetections
```

**示例：**
`myfunction`

### **Assignment threshold** — 用于选择检测以初始化分量的阈值 `25`（默认）| 正实数标量

用于选择检测以初始化分量的阈值，指定为正标量。在校正期间，跟踪器计算现有航迹与检测单元之间的关联似然。如果某个检测单元与所有现有航迹的关联似然（由负对数似然给出）高于该阈值（这意味着该检测单元与现有航迹的关联似然较低），则该检测单元用于在自适应出生密度中初始化新分量。

**示例：** `18.1`

**数据类型：** `single` | `double`

### **Maximum number of sensors** — 最大传感器数量 `20`（默认）| 正整数

可连接到跟踪器的最大传感器数量，指定为正整数。`MaxNumSensors` 必须大于或等于用于更新该模块的所有检测中出现的 `SensorIndex` 的最大值。

**数据类型：** `single` | `double`

### **Maximum number of tracks** — 最大航迹数量 `1000`（默认）| 正整数

跟踪器可维护的最大航迹数量，指定为正整数。

**数据类型：** `single` | `double`

### **Maximum number of components** — 最大分量数量 `1000`（默认）| 正整数

跟踪器可维护的最大分量数量，指定为正整数。

**数据类型：** `single` | `double`

### **Sensor configurations** — 跟踪传感器的配置 `struct('SensorIndex',1,'IsValidTime',true)`（默认）| 结构体 | 结构体数组

跟踪传感器的配置，指定为结构体或结构体数组。此参数向跟踪器提供跟踪传感器配置信息，例如传感器检测限制和传感器分辨率。每个结构体允许的字段名与 `trackingSensorConfiguration` 对象的属性名相同。如果你将该结构体的 `MaxDetsPerObject` 字段设置为 `1`，则跟踪器仅创建一个划分，使得每个目标最多只能分配一个检测。

你可以通过选择 **Update sensor configurations with time** 参数，经由 **Sensor configurations** 输入端口更新配置。

### **Update sensor configurations with time** — 随时间更新传感器配置 `off`（默认）| `on`

选择此参数以启用通过 **Sensor Configurations** 输入端口输入跟踪传感器配置的输入端口。

### **Track state parameters** — 航迹状态参考坐标系结构的参数 | 结构体数组

将航迹状态参考坐标系的参数指定为结构体或结构体数组。该模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹报告的参考坐标系，或所生成航迹的其他期望属性。

例如，您可以使用以下结构体定义一个矩形参考坐标系，其原点位置为 `[10 10 0]` 米，原点速度相对于场景坐标系为 `[2 -2 0]` 米每秒。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

您可以通过选择 **Update track state parameters with time** 参数，经由 **State Parameters** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **Update track state parameters with time** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数以启用通过 **State Parameters** 输入端口输入航迹状态参数的端口。

### **Simulate using** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。

#### Track Management

### **Birth rate of new targets** — 新目标的出生率（以密度计） `1e-3`（默认）| 正实数标量

新目标的出生率（以密度计），指定为正实数标量。出生率表示每单位时间内密度中新增目标的期望数量。出生密度通过跟踪器所使用的传感器配置的 `FilterInitializationFcn` 创建。通常，跟踪器通过两种方式向密度函数添加分量：

1. 预测出生密度 — 该密度由 `FilterInitializationFcn` 函数在无输入调用时初始化。
2. 自适应出生密度 — 该密度由 `FilterInitializationFcn` 函数在带检测输入调用时初始化。跟踪器根据检测与目标当前估计的关联对数似然来选择检测。

**Birth rate of new targets** 参数的值表示每个时间步的预测出生密度和自适应出生密度之和。

**示例：** `0.01`

**数据类型：** `single` | `double`

### **Death rate of components** — 分量的消亡率（以密度计） `1e-6`（默认）| 正实数标量

分量的消亡率（以密度计），指定为正实数标量。消亡率表示一个分量在一个时间步后在密度中消失的速率。以下方程说明了消亡率（*P*d）与分量在连续时间步之间的生存概率（*P*s）之间的关系：

Ps=(1−Pd)ΔT

其中 *Δ**T* 为时间步。

**示例：** `1e-4`

**数据类型：** `single` | `double`

### **Threshold for initializing tentative tracks** — 初始化暂定航迹的阈值 `0.5`（默认）| 正实数标量

初始化暂定航迹的阈值，指定为正实数标量。如果某个分量的权重高于该阈值，则该分量被标记为 `'Tentative'` 航迹并被赋予 `TrackID`。

**示例：** `0.45`

**数据类型：** `single` | `double`

### **Threshold for track confirmation** — 航迹确认阈值 `0.8`（默认）| 正实数标量

航迹确认阈值，指定为正实数标量。在 PHD 跟踪器中，一条航迹可以有多个共享同一 `TrackID` 的分量。如果暂定航迹各分量的权重之和高于确认阈值，则该航迹状态被标记为 `'Confirmed'`。

**示例：** `0.85`

**数据类型：** `single` | `double`

### **Threshold for track deletion** — 分量删除阈值 `1e-3`（默认）| 正实数标量

分量删除阈值，指定为正实数标量。在 PHD 跟踪器中，如果某个分量的权重低于删除阈值，则该分量被删除。

**示例：** `0.01`

**数据类型：** `single` | `double`

### **Threshold for components merging** — 分量合并阈值 `25`（默认）| 正实数标量

分量合并阈值，指定为正实数标量。在 PHD 跟踪器中，如果具有相同 `TrackID` 的分量之间的 Kullback-Leibler 距离小于合并阈值，则这些分量合并为一个分量。合并后新分量的权重等于合并前各分量权重之和。此外，如果合并后的权重高于 **Thresholds for label management** 参数中指定的第一个阈值，则合并后的权重被截断为第一个阈值。注意，`TrackID` 为 `0` 的分量也可以相互合并。

**示例：** 30

**数据类型：** `single` | `double`

### **Thresholds for label management** — 标签管理阈值 `[1.1 1 0.8]`（默认）| 1×3 正数值向量

标签管理阈值，指定为递减正数值的 1×3 向量，[*C*1, *C*2, *C*3]。基于此参数，跟踪器使用以下规则管理密度中的分量：

1. 任何高于第一个阈值 *C*1 的分量权重被降低到 *C*1。
2. 对于所有具有相同 `TrackID` 的分量，如果这些分量中的最大权重大于 *C*2，则保留权重最大的分量以保留 `TrackID`，同时删除所有其他分量。
3. 对于所有具有相同 `TrackID` 的分量，如果最大权重与所有这些分量的权重之和的比值大于 *C*3，则保留权重最大的分量以保留 `TrackID`，同时删除所有其他分量。
4. 如果条件 2 和条件 3 均不满足，则权重最大的分量保留 `TrackID`，而所有其他分量的标签被设置为 `0`。发生这种情况时，意味着某些分量可能代表其他目标。此过程保留了这些未保留分量将来被再次提取的可能性。

#### 端口设置

### **Prediction time source** — 预测时间来源 `Auto`（默认）| `Input port`

预测时间来源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **Enable tentative tracks output** — 启用暂定航迹输出端口 `off`（默认）| `on`

选择此参数以通过 **Tentative Tracks** 输出端口启用暂定航迹的输出。

### **Enable all tracks output** — 启用所有航迹输出端口 `off`（默认）| `on`

选择此参数以通过 **All Tracks** 输出端口启用所有航迹的输出。

### **Enable information output** — 启用分析信息输出端口 `off`（默认）| `on`

选择此参数以通过 **Info** 输出端口启用分析信息的输出。

### **输出总线名称的来源** — 输出航迹总线名称的来源 `Auto`（默认）| `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 通过 **Specify an output bus name** 参数指定输出航迹总线名称。

### **输出信息总线名称的来源** — 输出信息总线名称的来源 `Auto`（默认）| `Property`

输出信息总线名称的来源，指定为：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 通过 **Specify an output info bus name** 参数指定输出信息总线名称。

#### 依赖关系

要启用此参数，请在 **Port Setting** 选项卡上选择 **Enable information output**。
## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 在代码生成中，如果检测输入指定为 `double` 精度，则航迹输出的 `NumTracks` 字段将作为 `double` 变量返回。如果检测输入指定为 `single` 精度，则航迹输出的 `NumTracks` 字段将作为 `uint32` 变量返回。

- 跟踪器支持*严格单精度*代码生成，但有以下限制：

  - 您必须在每个跟踪传感器配置结构体中将滤波器初始化函数指定为单精度。
  - 每个跟踪传感器配置结构体中指定的滤波器必须使用支持单精度的运动模型和测量模型。

  有关*严格单精度*代码生成的详细信息，请参阅 Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation。
- 跟踪器支持*非动态内存分配*代码生成，但有以下限制：

  - 您必须在每个跟踪传感器配置结构体中将 `MaxNumDetections` 和 `MaxNumDetsPerObject` 字段指定为有限整数。
  - 您必须将 **Maximum number of components** 参数指定为有限整数。
  - 您必须将 **Maximum number of tracks** 参数指定为有限整数。

  有关*非动态内存分配*代码生成的详细信息，请参阅 Generate Code with Strict Single-Precision and Non-Dynamic Memory Allocation。

## 版本历史

**在 R2021a 中引入**

### R2023a：Simulink 总线不再显示在工作区中

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

多传感器、多目标 PHD 跟踪器

概率假设密度（PHD）跟踪器模块在多传感器环境中创建并管理静止和移动对象的航迹。该跟踪器使用多目标概率假设密度滤波器来估计点目标和扩展对象的状态。PHD 由概率密度函数的加权和表示，并提取 PHD 中的峰值以表示可能的目标。有关更多详细信息，请参阅 Algorithms。
