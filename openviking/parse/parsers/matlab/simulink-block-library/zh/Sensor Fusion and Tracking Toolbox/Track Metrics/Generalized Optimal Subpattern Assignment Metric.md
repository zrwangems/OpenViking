---
type: simulink-block
title: 'Generalized Optimal Subpattern Assignment Metric'
family: 'fusion'
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
```yaml
ports:
- name: Tracks
  summary: 航迹列表 Simulink® 总线，包含 MATLAB® 结构体
  direction: input
- name: Truths
  summary: 真值列表 Simulink 总线，包含 MATLAB 结构体
  direction: input
- name: Assignments
  summary: 已知分配 *K*×2 非负整数矩阵
  direction: input
- name: GOSPA Metric
  summary: 包含切换误差分量的 GOSPA 度量 非负实数标量
  direction: output
- name: GOSPA Metric Without Switching
  summary: 不包含切换误差分量的 GOSPA 度量 非负实数标量
  direction: output
- name: Switching Error
  summary: 切换误差分量 非负实数标量
  direction: output
- name: Localization Error
  summary: 定位误差分量 非负实数标量
  direction: output
- name: Missed Target Error
  summary: 漏检目标误差分量 非负实数标量
  direction: output
- name: False Track Error
  summary: 虚假航迹误差分量 非负实数标量
  direction: output
```

### 输入

### **Tracks** — 航迹列表 Simulink® 总线，包含 MATLAB® 结构体

航迹列表，指定为包含 MATLAB 结构体的 Simulink 总线。

如果将 **Port Setting** 选项卡上的 **Track bus** 参数指定为 `objectTrack`，则结构体必须使用以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组 |

每个航迹结构体必须包含 `TrackID` 和 `State` 字段。此外，如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则每个结构体必须包含 `StateCovariance` 字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个航迹的唯一航迹标识符，指定为非负整数。 |
| `State` | 更新时刻的状态向量值，指定为 *N* 元素向量，其中 *N* 是状态的维度。 |
| `StateCovariance` | 不确定性协方差矩阵，指定为 *N*×*N* 矩阵，其中 *N* 是状态的维度。 |

如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则结构体必须包含 `StateCovariance` 字段。

如果将 **Track bus** 参数指定为 `custom`，则可以使用自己的航迹总线格式。在这种情况下，必须使用 **Track extractor function** 参数定义航迹提取函数。该函数必须使用以下语法：

```
tracks = trackExtractorFcn(trackInputFromBus)
```

其中 `trackInputFromBus` 是来自航迹总线的输入，`tracks` 必须返回为包含 `TrackID` 和 `State` 字段的结构体数组。

### **Truths** — 真值列表 Simulink 总线，包含 MATLAB 结构体

真值列表，指定为包含 MATLAB 结构体的 Simulink 总线。

如果将 **Port Setting** 选项卡上的 **Truth bus** 参数指定为 `Platform`，则结构体必须使用以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumPlatforms` | 真值平台数量 |
| `Platforms` | 真值平台结构体数组 |

每个平台结构体具有以下字段：

| 字段 | 定义 |
| --- | --- |
| `PlatformID` | 用于区分平台的唯一标识符，指定为非负整数。 |
| `Position` | 平台的位置，指定为 *M* 元素向量，其中 *M* 是位置状态的维度。例如，对于 3-D 位置，*M* = 3。 |
| `Velocity` | 平台的速度，指定为 *M* 元素向量，其中 *M* 是速度状态的维度。例如，对于 3-D 速度，*M* = 3。 |

如果将 **Truth bus** 参数指定为 `Actor`，则结构体必须使用以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumActors` | 真值 actor 数量 |
| `Actors` | 真值 actor 结构体数组 |

每个 actor 结构体具有以下字段：

| 字段 | 定义 |
| --- | --- |
| `ActorID` | 用于区分 actor 的唯一标识符，指定为非负整数。 |
| `Position` | actor 的位置，指定为 *M* 元素向量，其中 *M* 是位置状态的维度。例如，对于 3-D 位置，*M* = 3。 |
| `Velocity` | actor 的速度，指定为 *M* 元素向量，其中 *M* 是速度状态的维度。例如，对于 3-D 速度，*M* = 3。 |

如果将 **Truth bus** 参数指定为 `custom`，则可以定义自己的真值总线格式。在这种情况下，必须使用 **Truth extractor function** 参数定义真值提取函数。该函数必须使用以下语法：

```
 truths = truthExtractorFcn(truthInputFromBus)
```

其中 `truthInputFromBus` 是来自真值总线的输入，`truths` 必须返回为包含 `PlatformID`、`Position` 和 `Velocity` 字段的结构体数组。

### **Assignments** — 已知分配 *K*×2 非负整数矩阵

已知分配，指定为 *K*×2 的非负整数矩阵。*K* 是分配对的数量。第一列元素是航迹 ID，第二列元素是真值 ID。同一行中的 ID 相互分配。如果某个航迹或真值未被分配，则在同一行元素中指定 `0`。

分配必须是航迹与真值之间的唯一分配。冗余或虚假航迹应通过将其分配给“0” `TruthID` 来视为未分配航迹。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择 **Assignments**。
### 输出

### **GOSPA Metric** — 包含切换误差分量的 GOSPA 度量 非负实数标量

包含切换误差分量的 GOSPA 度量，返回为非负实数标量。

### **GOSPA Metric Without Switching** — 不包含切换误差分量的 GOSPA 度量 非负实数标量

不包含切换误差分量的 GOSPA 度量，返回为非负实数标量。

**示例：** 8.5

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择 **GOSPA metric without switching error component**。

### **Switching Error** — 切换误差分量 非负实数标量

切换误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择 **Switching error**。

### **Localization Error** — 定位误差分量 非负实数标量

定位误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择 **Localization error**。

### **Missed Target Error** — 漏检目标误差分量 非负实数标量

漏检目标误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择 **Missed target error**。

### **False Track Error** — 虚假航迹误差分量 非负实数标量

虚假航迹误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择 **False track error**。
## 参数
```yaml
parameters:
- name: Cutoff distance
  summary: 航迹与真值之间截断距离的阈值 30（默认）| 正实数标量
  group: ''
- name: Order
  summary: GOSPA 度量的阶数 2（默认）| 正整数
  group: ''
- name: Alpha
  summary: GOSPA 度量的 Alpha 参数 2（默认）| 范围 [0, 2] 内的正标量
  group: ''
- name: Distance type
  summary: 距离类型 posnees（默认）| velnees | posabserr | velabserr | custom
  group: ''
- name: Custom distance function
  summary: 自定义距离函数函数句柄
  group: ''
- name: Motion model
  summary: 期望的平台运动模型 constvel（默认）| constacc | constturn | singer
  group: ''
- name: Switching penalty
  summary: 分配切换的惩罚 0（默认）| 非负实数标量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code Generation
  group: ''
- name: Assignments
  summary: 启用分配输入 off（默认）| on
  group: ''
- name: GOSPA metric without switching error
  summary: 启用不含切换误差的 GOSPA 度量输出 off（默认）| on
  group: ''
- name: Switching error
  summary: 启用切换误差分量输出 off（默认）| on
  group: ''
- name: Localization error
  summary: 启用定位误差分量输出 off（默认）| on
  group: ''
- name: Missed target error
  summary: 启用漏检目标误差分量输出 off（默认）| on
  group: ''
- name: False track error
  summary: 启用虚假航迹误差分量输出 off（默认）| on
  group: ''
- name: Track bus
  summary: 航迹总线选择 objectTrack（默认）| custom
  group: ''
- name: Truth bus
  summary: 真值总线选择 Platform（默认）| Actor | custom
  group: ''
- name: Track extractor function
  summary: 航迹提取函数 函数句柄
  group: ''
- name: Truth extractor function
  summary: 真值提取函数 函数句柄
  group: ''
```

#### 属性

### **Cutoff distance** — 航迹与真值之间截断距离的阈值 `30`（默认）| 正实数标量

航迹与真值之间截断距离的阈值，指定为正实数标量。如果计算得到的航迹与所分配真值之间的距离高于该阈值，则纳入度量中的实际距离将减小到该阈值。

**示例：** `40`

### **Order** — GOSPA 度量的阶数 `2`（默认）| 正整数

GOSPA 度量的阶数，指定为正整数。

**示例：**
`10`

### **Alpha** — GOSPA 度量的 Alpha 参数 `2`（默认）| 范围 [0, 2] 内的正标量

GOSPA 度量的 Alpha 参数，指定为范围 [0, 2] 内的正标量。

**示例：**
`1`

### **Distance type** — 距离类型 `posnees`（默认）| `velnees` | `posabserr` | `velabserr` | `custom`

距离类型，指定为 `posnees`、`velnees`、`posabserr` 或 `velabserr`。距离类型指定用于距离计算的物理量：

- `posnees` – 航迹位置的归一化估计误差平方（NEES）
- `velnees` – 航迹速度的 NEES 误差
- `posabserr` – 航迹位置的绝对误差
- `velabserr` – 航迹速度的绝对误差
- `custom` – 自定义距离误差

如果将其指定为 `custom`，还必须在 **Custom distance function** 参数中指定距离函数。

### **Custom distance function** — 自定义距离函数函数句柄

自定义距离函数，指定为函数句柄。该函数必须支持以下语法：

```
d = myCustomFcn(Track,Truth)
```

其中，
`Track` 是航迹信息的结构体，
`Truth` 是真值信息的结构体，`d`
是真值与航迹之间的距离。有关如何组织航迹信息的示例，请参阅 `objectTrack`。

**示例：**
`@myCustomFcn`

#### 依赖关系

要启用此属性，请将 **Distance type** 参数设置为
`custom`。

### **Motion model** — 期望的平台运动模型 `constvel`（默认）| `constacc` | `constturn` | `singer`

期望的平台运动模型，指定为 `constvel`、
`constacc`、`constturn` 或
`singer`。此属性选择 **Tracks** 输入端口所使用的运动模型。

这些运动模型期望航迹结构体的 `State` 字段具有包含以下值的列向量：

- `constvel` — 位置位于元素 [1 3 5]，速度位于
  元素 [2 4 6]。
- `constacc` — 位置位于元素 [1 4 7]，速度位于
  元素 [2 5 8]，加速度位于元素 [3 6 9]。
- `constturn` — 位置位于元素 [1 3 6]，速度位于
  元素 [2 4 7]，偏航角速率位于元素 5。
- `singer` — 位置位于元素 [1 4 7]，速度位于
  元素 [2 5 8]，加速度位于元素 [3 6 9]。

航迹结构体输入的 `StateCovariance` 字段
必须具有与航迹结构体 `State`
字段的位置、速度和转向速率相对应的行和列中的位置、速度和转向速率协方差。

### **Switching penalty** — 分配切换的惩罚 `0`（默认）| 非负实数标量

分配切换的惩罚，指定为非负实数标量。

**示例：**
`2`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code Generation`

从以下选项中选择仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。

#### 端口设置

### **Assignments** — 启用分配输入 `off`（默认）| `on`

选择此参数可通过
**Assignments** 输入端口输入已知分配。

### **GOSPA metric without switching error** — 启用不含切换误差的 GOSPA 度量输出 `off`（默认）| `on`

选择此参数可通过
**GOSPA Metric Without Switching** 输出端口输出不含切换误差分量的 GOSPA 度量。

### **Switching error** — 启用切换误差分量输出 `off`（默认）| `on`

选择此参数可通过
**Switching Error** 输出端口输出切换误差分量。

### **Localization error** — 启用定位误差分量输出 `off`（默认）| `on`

选择此参数可通过
**Localization Error** 输出端口输出定位误差分量。

### **Missed target error** — 启用漏检目标误差分量输出 `off`（默认）| `on`

选择此参数可通过
**Missed Target Error** 输出端口输出漏检目标误差分量。

### **False track error** — 启用虚假航迹误差分量输出 `off`（默认）| `on`

选择此参数可通过
**False Track Error** 输出端口输出虚假航迹误差分量。

### **Track bus** — 航迹总线选择 `objectTrack`（默认）| `custom`

航迹总线选择，指定为 `objectTrack` 或
`custom`。有关每种选择的更多详细信息，请参阅 **Tracks**
输入端口的相关描述。

### **Truth bus** — 真值总线选择 `Platform`（默认）| `Actor` | `custom`

真值总线选择，指定为 `Platform`、
`Actor` 或 `custom`。有关每种选择的更多详细信息，请参阅
**Truths** 输入端口的相关描述。

### **Track extractor function** — 航迹提取函数 函数句柄

航迹提取函数，指定为函数句柄。该函数必须支持以下
语法：

```
tracks = trackExtractorFcn(trackInputFromBus)
```

其中
`trackInputFromBus` 是来自航迹总线的输入，
`tracks` 必须返回一个结构体数组，其中包含
`TrackID` 和 `State` 字段。如果在
**Distance type** 参数中指定基于 NEES 的距离（`posnees` 或
`velnees`），则该结构体必须包含
`StateCovariance` 字段。

**示例：**  `@myCustomFcn`

#### 依赖关系

要启用此属性，请将 **Track bus** 参数设置为 `custom`。

### **Truth extractor function** — 真值提取函数 函数句柄

真值提取函数，指定为函数句柄。该函数必须支持
以下
语法：

```
 truths = truthExtractorFcn(truthInputFromBus)
```

其中
`truthInputFromBus` 是来自航迹总线的输入，
`truths` 必须返回一个结构体数组，其中包含
`PlatformID`、`Position` 和
`Velocity` 作为字段名称。

**示例：**
`@myCustomFcn`

#### 依赖关系

要启用此属性，请将 **Truth bus** 参数设置为
`custom`。
## 所属库

Sensor Fusion and Tracking Toolbox / Track Metrics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2023a：Simulink 总线不显示在工作区中

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

计算广义最优子模式分配度量

广义最优子模式分配度量模块通过计算航迹与
已知真值之间的广义最优子模式分配（GOSPA）度量来评估跟踪算法的性能。该度量由切换误差、定位误差、漏检
目标误差和虚假航迹误差分量组成。您还可以选择每个单独的误差
分量作为模块输出。
