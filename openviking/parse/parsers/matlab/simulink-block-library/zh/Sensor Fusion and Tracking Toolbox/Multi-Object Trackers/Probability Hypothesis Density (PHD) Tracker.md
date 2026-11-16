---
type: simulink-block
title: 'Probability Hypothesis Density (PHD) Tracker'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Trackers'
documentation_page: 'probabilityhypothesisdensityphdtracker'
documentation_source_path: 'ref/probabilityhypothesisdensityphdtracker.html'
language: zh-CN
chinese_source: worker-translation
---

# Probability Hypothesis Density (PHD) Tracker

## 端口

### 输入

### **Detections** — 检测列表，包含 MATLAB® 结构的 Simulink® 总线

检测列表，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumDetections` | 检测数量 | Integer. |
| `Detections` | 目标检测 | 目标检测结构体数组。这些检测中的前 `NumDetections` 个是实际检测。 |

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

目标检测结构体包含 `Time` 字段。每个目标检测的时间标签必须小于或等于模块当前调用时的时间。该时间标签还必须大于模块上一次调用时指定的更新时间。

### **Prediction Time** — 航迹更新时间，实数标量

航迹更新时间，指定为以 seconds 为单位的实数标量。跟踪器将所有航迹更新到此时间。每次调用模块时，更新时间必须增加。单位为 seconds。更新时间必须至少与 **Detections** 输入端口处指定的最大 `Time` 一样大。

如果未启用此端口，则由 Simulink 管理的仿真时钟确定更新时间。

#### 依赖关系

要启用此端口，请在 **端口设置**选项卡中，将 **预测时间源** 设置为 `Input port`。

### **Sensor Configurations** — 跟踪传感器的配置，包含 MATLAB 结构的 Simulink 总线

跟踪传感器的配置，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 | 类型 |
| --- | --- | --- |
| `NumConfigurations` | 传感器配置数量 | Integer. |
| `Configurations` | 传感器配置 | 传感器配置结构体数组。这些配置中的前 `NumConfigurations` 个是实际配置。字段名称和定义必须分别对应于 `trackingSensorConfiguration` 对象属性的名称和值。 如果在跟踪系统中使用 Radar Data Generator (Radar Toolbox) 模块，则可以直接使用该 Radar Data Generator (Radar Toolbox) 模块的 **Configuration** 输出来指定此值。 |

#### 依赖关系

要启用此端口，请在 **跟踪器**选项卡中，选择 **随时间更新传感器配置** 参数。

### **State Parameters** — 航迹状态参数，包含 MATLAB 结构的 Simulink 总线

航迹状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构体数组 |

模块使用 `Parameters` 字段的值作为所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义报告航迹时所用的参考系，或所生成航迹的其他所需属性。

例如，可以使用以下结构来定义一个矩形参考系，其原点位置相对于场景坐标系为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **跟踪器配置**选项卡中，选择 **随时间更新航迹状态参数** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹，包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构体数组，其长度由 **最大航迹数** 参数设置。这些航迹中的前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如 Track Structure 中所示。

### **Tentative Tracks** — 暂定航迹，包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在被确认之前为暂定航迹。此端口的输出形式与 **Confirmed Tracks** 端口的输出相同。

#### 依赖关系

要启用此端口，请在 **端口设置**选项卡中，选择 **启用暂定航迹输出**。

### **All Tracks** — 确认航迹和暂定航迹，包含 MATLAB 结构的 Simulink 总线

确认航迹和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。此端口的输出形式与 **Confirmed Tracks** 端口的输出相同。

#### 依赖关系

要启用此端口，请在 **端口设置**选项卡中，选择 **启用所有航迹输出**。

### **Info** — 用于分析航迹更新的附加信息，包含 MATLAB 结构的 Simulink 总线

用于分析航迹更新的附加信息，返回为包含 MATLAB 结构的 Simulink 总线。

下表列出了 info 结构体的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `CorrectionOrder` | 用于状态估计校正的传感器顺序，返回为 `SensorIndex` 值的行向量。例如，[1 3 2 4]。 |
| `TrackIDsAtStepBeginning` | 步开始时的航迹 ID。 |
| `DeletedTrackIDs` | 在该步期间删除的航迹 ID。 |
| `TrackIDsAtStepEnd` | 步结束时的航迹 ID。 |
| `SensorAnalysisInfo` | 传感器分析信息的元胞数组。 |

`SensorAnalysisInfo` 字段可以包含多个传感器信息报告。每个报告是一个结构体，包含以下字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `SensorIndex` | 传感器索引。 |
| `DetectionCells` | 检测单元，返回为逻辑矩阵。矩阵的每一列表示一个检测单元。在每一列中，如果第 *i* 个元素为 1，则第 *i* 个检测属于该列所表示的检测单元。 |
| `DetectionLikelihoods` | 密度函数中的分量与检测单元之间的关联似然，返回为 *N*×*P* 矩阵。*N* 是密度函数中的分量数，*P* 是检测单元数。 |
| `IsBirthCells` | 指示 `DetectionCells` 中列出的检测单元是否产生新航迹，返回为 1×*P* 逻辑向量，其中 *P* 是检测单元数。 |
| `NumPartitions` | 划分数量。 |
| `DetectionProbability` | 现有航迹被传感器检测到的概率，返回为 1×*N* 行向量，其中 *N* 是密度函数中的分量数。 |
| `LabelsBeforeCorrection` | 校正前密度函数中分量的标签，返回为 1×*M*b 行向量。*M*b 是校正前跟踪器中维护的分量数。向量的每个元素是一个 `TrackID`。例如，[1 1 2 0 0]。注意，多个分量可以共享同一个 `TrackID`。 |
| `LabelsAfterCorrection` | 校正后密度函数中分量的标签，返回为 1×*M*a 行向量。*M*a 是校正后跟踪器中维护的分量数。向量的每个元素是一个 `TrackID`。例如，[1 1 1 2 2 0 0]。注意，多个分量可以共享同一个 `TrackID`。 |
| `WeightsBeforeCorrection` | 校正前密度函数中分量的权重，返回为 1×*M*b 行向量。*M*b 是校正前跟踪器中维护的分量数。向量的每个元素是 `LabelsBeforeCorrection` 中对应分量的权重。例如，[0.1 0.5 0.7 0.3 0.2]。 |
| `WeightsAfterCorrection` | 校正后密度函数中分量的权重，返回为 1×*M*a 行向量。*M*a 是校正后跟踪器中维护的分量数。向量的每个元素是 `LabelsAfterCorrection` 中对应分量的权重。例如，[0.1 0.4 0.2 0.6 0.3 0.2 0.2]。 |

#### 依赖关系

要启用此端口，请在 **端口设置**选项卡中，选择 **启用信息输出**。

## 参数

#### 跟踪器配置

### **跟踪器标识符** — 唯一跟踪器标识符 `0`（默认）| 非负整数

将唯一跟踪器标识符指定为非负整数。此参数作为跟踪器输出中的 `SourceIndex` 传递，并用于区分多跟踪器系统中来自不同跟踪器的航迹。要将航迹输出用作 Track-To-Track Fuser 模块的输入，必须将此属性指定为正整数。

**示例：** `1`

### **检测划分函数** — 将检测划分为检测单元的函数 `partitionDetections`（默认）| 函数名称

用于将检测划分为检测单元的函数，指定为函数名称。当每个传感器可以对每个目标报告多个检测时，必须使用划分函数。划分函数报告来自一个传感器的检测的所有可能划分。在每个划分中，检测被分离为互斥的检测单元，假设每个检测单元属于一个扩展目标。

您也可以指定自己的检测划分函数。有关编写此函数的指导，可以使用 `type` 命令检查默认划分函数 `partitionDetections` 的详细信息：

`type partitionDetections`

**示例：**
`myfunction`

### **分配阈值** — 用于选择检测以初始化分量的阈值 `25`（默认）| 正实数标量

用于选择检测以初始化分量的阈值，指定为正标量。在校正期间，跟踪器计算现有航迹与检测单元之间的关联似然。如果某个检测单元与所有现有航迹的关联似然（由负对数似然给出）高于该阈值（这意味着该检测单元与现有航迹的关联似然较低），则该检测单元用于在自适应新生密度中初始化新分量。

**示例：** `18.1`

**数据类型：** `single` | `double`

### **最大传感器数** — 最大传感器数 `20`（默认）| 正整数

可连接到跟踪器的最大传感器数，指定为正整数。`MaxNumSensors` 必须大于或等于用于更新模块的所有检测中找到的最大 `SensorIndex` 值。

**数据类型：** `single` | `double`

### **最大航迹数** — 最大航迹数 `1000`（默认）| 正整数

跟踪器可以维护的最大航迹数，指定为正整数。

**数据类型：** `single` | `double`

### **最大分量数** — 最大分量数 `1000`（默认）| 正整数

跟踪器可以维护的最大分量数，指定为正整数。

**数据类型：** `single` | `double`

### **传感器配置** — 跟踪传感器的配置 `struct('SensorIndex',1,'IsValidTime',true)`（默认）| 结构体 | 结构体数组

跟踪传感器的配置，指定为结构体或结构体数组。此参数向跟踪器提供跟踪传感器配置信息，例如传感器检测限制和传感器分辨率。每个结构体允许的字段名称与 `trackingSensorConfiguration` 对象的属性名称相同。如果将结构体的 `MaxDetsPerObject` 字段设置为 `1`，则跟踪器仅创建一个划分，使得每个目标最多可以分配一个检测。

可以通过选择 **随时间更新传感器配置** 参数，经由 **Sensor configurations** 输入端口更新配置。

### **随时间更新传感器配置** — 随时间更新传感器配置 `off`（默认）| `on`

选择此参数可通过 **Sensor Configurations** 输入端口启用跟踪传感器配置的输入端口。

### **航迹状态参数** — 航迹状态参考系的参数 结构体 | 结构体数组

将航迹状态参考系的参数指定为结构体或结构体数组。模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义报告航迹时所用的参考系，或所生成航迹的其他所需属性。

例如，可以使用以下结构来定义一个矩形参考系，其原点位置相对于场景坐标系为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

可以通过选择 **随时间更新航迹状态参数** 参数，经由 **State Parameters** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **随时间更新航迹状态参数** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数可通过 **State Parameters** 输入端口启用航迹状态参数的输入端口。

### **仿真使用** — 要运行的仿真类型 `Interpreted Execution`（默认）| `Code Generation`

从以下选项中选择要运行的仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间。

#### 航迹管理

### **新目标出生率** — 密度中新目标的出生率 `1e-3`（默认）| 正实数标量

密度中新目标的出生率，指定为正实数标量。出生率表示每单位时间在密度中新增目标的预期数量。新生密度通过跟踪器所用传感器配置的 `FilterInitializationFcn` 创建。通常，跟踪器通过两种方式向密度函数添加分量：

1. 预测新生密度 — 当 `FilterInitializationFcn` 函数在不带输入的情况下调用时，会初始化此密度。
2. 自适应新生密度 — 当 `FilterInitializationFcn` 函数在带检测输入的情况下调用时，会初始化此密度。跟踪器根据检测与目标当前估计的关联对数似然来选择检测。

**新目标出生率** 参数的值表示每个时间步的预测新生密度与自适应新生密度之和。

**示例：** `0.01`

**数据类型：** `single` | `double`

### **分量死亡率** — 密度中分量的死亡率 `1e-6` (默认) | 正实数标量

密度中分量的死亡率，指定为正实数标量。死亡率表示一个分量在一个时间步后在密度中消失的速率。此方程说明了死亡率
(*P*d) 如何与分量在连续时间步之间的生存概率
(*P*s) 相关：

Ps=(1−Pd)ΔT

其中 *Δ**T* 是时间步长。

**示例：** `1e-4`

**数据类型：** `single` | `double`

### **初始化暂定航迹的阈值** — 初始化暂定航迹的阈值 `0.5` (默认) | 正实数标量

初始化暂定航迹的阈值，指定为正实数标量。如果分量的权重高于该阈值，则该分量被标记为 `'Tentative'` 航迹，并分配一个 `TrackID`。

**示例：** `0.45`

**数据类型：** `single` | `double`

### **航迹确认阈值** — 航迹确认阈值 `0.8` (默认) | 正实数标量

航迹确认阈值，指定为正实数标量。在 PHD 跟踪器中，一条航迹可以具有多个共享同一 `TrackID` 的分量。如果暂定航迹各分量的权重和高于确认阈值，则航迹状态标记为 `'Confirmed'`。

**示例：** `0.85`

**数据类型：** `single` | `double`

### **航迹删除阈值** — 分量删除阈值 `1e-3` (默认) | 正实数标量

分量删除阈值，指定为正实数标量。在 PHD 跟踪器中，如果分量的权重低于删除阈值，则删除该分量。

**示例：** `0.01`

**数据类型：** `single` | `double`

### **分量合并阈值** — 分量合并阈值 `25` (默认) | 正实数标量

分量合并阈值，指定为正实数标量。在 PHD 跟踪器中，如果具有相同 `TrackID` 的分量之间的 Kullback-Leibler 距离小于合并阈值，则将这些分量合并为一个分量。新分量的合并权重等于合并前各分量的权重之和。此外，如果合并权重高于 **标签管理阈值** 参数中指定的第一个阈值，则将合并权重截断为第一个阈值。请注意，`TrackID` 为 `0` 的分量也可以彼此合并。

**示例：** 30

**数据类型：** `single` | `double`

### **标签管理阈值** — 标签管理阈值 `[1.1 1 0.8]` (默认) | 1×3 正值向量

标签阈值，指定为按降序排列的 1×3 正值向量，[*C*1,
*C*2,
*C*3]。基于此参数，跟踪器使用以下规则管理密度中的分量：

1. 任何高于第一个阈值 *C*1 的分量，其权重都会降至 *C*1。
2. 对于具有相同 `TrackID` 的所有分量，如果这些分量中的最大权重大于 *C*2，则保留具有最大权重的分量以保留 `TrackID`，而删除所有其他分量。
3. 对于具有相同 `TrackID` 的所有分量，如果最大权重与所有这些分量的权重和之比大于 *C*3，则保留具有最大权重的分量以保留 `TrackID`，而删除所有其他分量。
4. 如果条件 2 和条件 3 均不满足，则具有最大权重的分量保留 `TrackID`，而所有其他分量的标签设置为 `0`。发生这种情况时，意味着某些分量可能表示其他对象。此过程保留了这些未保留分量将来再次被提取的可能性。

#### 端口设置

### **预测时间来源** — 预测时间来源 `Auto` (默认) | `Input port`

预测时间来源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **启用暂定航迹输出** — 启用暂定航迹的输出端口 `off` (默认) | `on`

选中此参数以通过 **Tentative Tracks** 输出端口启用暂定航迹的输出。

### **启用所有航迹输出** — 启用所有航迹的输出端口 `off` (默认) | `on`

选中此参数以通过 **All Tracks** 输出端口启用所有航迹的输出。

### **启用信息输出** — 启用分析信息的输出端口 `off` (默认) | `on`

选中此参数以通过 **Info** 输出端口启用分析信息的输出。

### **输出总线名称来源** — 输出航迹总线名称来源 `Auto` (默认) | `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 使用 **指定输出总线名称** 参数指定输出航迹总线名称。

### **输出信息总线名称来源** — 输出信息总线名称来源 `Auto` (默认) | `Property`

输出信息总线名称的来源，指定为：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 使用 **指定输出信息总线名称** 参数指定输出信息总线名称。

#### 依赖项

要启用此参数，请在 **端口设置** 选项卡上，选择 **启用信息输出**。

## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 在代码生成中，如果检测输入指定为 `double` 精度，则航迹输出的 `NumTracks` 字段将作为 `double` 变量返回。如果检测输入指定为 `single` 精度，则航迹输出的 `NumTracks` 字段将作为 `uint32` 变量返回。

- 跟踪器支持 *严格单精度* 代码生成，但存在以下限制：

  - 必须在每个跟踪传感器配置结构中将滤波器初始化函数指定为单精度。
  - 每个跟踪传感器配置结构中指定的滤波器必须使用支持单精度的运动模型和测量模型。

  有关 *严格单精度* 代码生成的详细信息，请参阅使用严格单精度和非动态内存分配生成代码。
- 跟踪器支持 *非动态内存分配* 代码生成，但存在以下限制：

  - 必须在每个跟踪传感器配置结构中将 `MaxNumDetections` 和 `MaxNumDetsPerObject` 字段指定为有限整数。
  - 必须将 **最大分量数** 参数指定为有限整数。
  - 必须将 **最大航迹数** 参数指定为有限整数。

  有关 *非动态内存分配* 代码生成的详细信息，请参阅使用严格单精度和非动态内存分配生成代码。

## 版本历史

**在 R2021a 中引入**

### R2023a：Simulink 总线不显示在工作区中

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

多传感器、多目标 PHD 跟踪器

Probability Hypothesis Density (PHD) Tracker 模块创建并管理多传感器环境中静止和运动对象的航迹。该跟踪器使用多目标概率假设密度滤波器来估计点目标和扩展目标的状态。PHD 由概率密度函数的加权和表示，并提取 PHD 中的峰值来表示可能的目标。有关更多详细信息，请参阅算法。
