---
type: simulink-block
title: 'Optimal Subpattern Assignment Metric'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Visualization and Analytics'
documentation_page: 'optimalsubpatternassignmentmetric'
documentation_source_path: 'ref/optimalsubpatternassignmentmetric.html'
language: zh-CN
chinese_source: worker-translation
---

# Optimal Subpattern Assignment Metric

## 端口

### 输入

### **Tracks** — 轨迹列表，包含 MATLAB 结构体的 Simulink® 总线

轨迹列表，指定为包含 MATLAB 结构体的 Simulink 总线。

如果在 **端口设置** 选项卡上将 **Track bus** 参数指定为 `objectTrack`，则该结构体必须使用以下形式：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 轨迹数量 |
| `Tracks` | 轨迹结构体数组 |

每个轨迹结构体必须包含 `TrackID` 和 `State` 字段。此外，如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则每个结构体必须包含 `StateCovariance` 字段。

| 字段 | 定义 |
| --- | --- |
| `TrackID` | 用于区分多个轨迹的唯一轨迹标识符，指定为非负整数。 |
| `State` | 更新时刻状态向量的值，指定为 *N* 元素向量，其中 *N* 是状态的维度。 |
| `StateCovariance` | 不确定性协方差矩阵，指定为 *N*×*N* 矩阵，其中 *N* 是状态的维度。 |

如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则该结构体必须包含 `StateCovariance` 字段。

如果将 **Track bus** 参数指定为 `custom`，则可以使用自己的轨迹总线格式。在这种情况下，必须使用 **Track extractor function** 参数定义轨迹提取函数。该函数必须使用以下语法：

```
tracks = trackExtractorFcn(trackInputFromBus)
```

其中 `trackInputFromBus` 是来自轨迹总线的输入，`tracks` 必须返回为具有 `TrackID` 和 `State` 字段的结构体数组。

### **Truths** — 真值列表，包含 MATLAB 结构体的 Simulink 总线

真值列表，指定为包含 MATLAB 结构体的 Simulink 总线。

如果在 **端口设置** 选项卡上将 **Truth bus** 参数指定为 `Platform`，则该结构体必须使用以下形式：

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

如果将 **Truth bus** 参数指定为 `Actor`，则该结构体必须使用以下形式：

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

其中 `truthInputFromBus` 是来自轨迹总线的输入，`truths` 必须返回为具有 `PlatformID`、`Position` 和 `Velocity` 字段名的结构体数组。

### **Assignments** — 已知分配 *K*×2 非负整数矩阵

已知分配，指定为非负整数的 *K*×2 矩阵。*K* 是分配对的数量。第一列元素是轨迹 ID，第二列元素是真值 ID。一行中的两个 ID 相互分配。如果某个轨迹或真值未分配，请在该行的另一个元素中指定 `0`。

轨迹与真值之间的分配必须唯一。冗余或虚假轨迹应通过将其分配给 "`0`" `TruthID` 来视为未分配轨迹。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上选择 **Assignments**。

### 输出

### **OSPA Metric** — OSPA 度量 非负实数标量

OSPA 度量，返回为非负实数标量。根据 **Metric** 和 **Labeling error** 参数的值，该模块可以输出传统 OSPA、带标签 OSPA (LOSPA) 或 OSPA(2)。

| **Metric** 参数值 | **Labeling error** 参数值 | 度量 |
| --- | --- | --- |
| `OSPA` | `0` | OSPA |
| `OSPA` | 正标量 | LOSPA |
| `OSPA(2)` | 不适用 | OSPA(2) |

**示例：** 10.1

### **Localization Error** — 定位误差分量 非负实数标量

定位误差分量，返回为非负实数标量。

**示例：** 8.5

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上选择 **Localization error**。

### **Cardinality Error** — 基数误差分量 非负实数标量

基数误差分量，返回为非负实数标量。

**示例：** 6

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上选择 **Cardinality error**。

### **Labeling Error** — 标签误差分量 非负实数标量

标签误差分量，返回为非负实数标量。

**示例：** 7.5

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上选择 **Labeling error**。

## 参数

#### 属性

### **Metric** — 度量选项 `OPSA` (default) | `OSPA(2)`

度量选项，指定为 `OSPA` 或 `OSPA(2)`。

- `OSPA` — 默认计算传统 OSPA 度量，或者在额外将 **Labeling error** 参数指定为正值后计算带标签 OSPA 度量。
- `OSPA(2)` — 计算 OSPA(2) 度量，该度量评估累积跟踪性能。选择此选项会启用以下用于配置度量的参数：

  - **Window length**
  - **Window sum order (q)**
  - **Window weights**
  - **Window weight exponent (r)**
  - **Custom window weights**

  选择此选项还会禁用两个用于评估标签误差分量的参数：

  - **Assignments**
  - **Labeling error**

### **Cutoff distance** — 轨迹与真值之间截断距离的阈值 `30` (default) | 正实数标量

轨迹与真值之间截断距离的阈值，指定为正实数标量。如果轨迹与分配的真值之间计算出的距离高于阈值，则纳入度量中的实际距离会减小到该阈值。

**示例：** `40`

### **Order** — OSPA 度量的阶数 `2` (default) | 正整数

OSPA 度量的阶数，指定为正整数。

**示例：**
`3`

### **Distance type** — 距离类型 `posnees` (default) | `velnees` | `posabserr` | `velabserr` | `custom`

距离类型，指定为 `posnees`、`velnees`、`posabserr` 或 `velabserr`。距离类型指定用于距离计算的物理量：

- `posnees` – 轨迹位置的归一化估计误差平方 (NEES)
- `velnees` – 轨迹速度的 NEES 误差
- `posabserr` – 轨迹位置的绝对误差
- `velabserr` – 轨迹速度的绝对误差
- `custom` – 自定义距离误差

如果选择 `custom`，还必须在 **Custom distance function** 参数中指定距离函数。

### **Custom distance function** — 自定义距离函数，函数句柄

自定义距离函数，指定为函数句柄。该函数必须支持以下语法：

```
d = myCustomFcn(Track,Truth)
```

其中 `Track` 是轨迹信息结构体，`Truth` 是真值信息结构体，`d` 是真值与轨迹之间的距离。有关如何组织轨迹信息的示例，请参阅 `objectTrack`。

**示例：**
`@myCustomFcn`

#### 依赖关系

要启用此属性，请将 **Distance type** 参数设置为 `custom`。

### **Motion model** — 所需平台运动模型 `constvel` (default) | `constacc` | `constturn` | `singer`

所需平台运动模型，指定为 `constvel`、`constacc`、`constturn` 或 `singer`。此属性选择 **Tracks** 输入端口使用的运动模型。

这些运动模型要求轨迹结构的 `State` 字段具有包含以下值的列向量：

- `constvel` — 位置位于元素 [1 3 5] 中，速度位于元素 [2 4 6] 中。
- `constacc` — 位置位于元素 [1 4 7] 中，速度位于元素 [2 5 8] 中，加速度位于元素 [3 6 9] 中。
- `constturn` — 位置位于元素 [1 3 6] 中，速度位于元素 [2 4 7] 中，偏航角速度位于元素 5 中。
- `singer` — 位置位于元素 [1 4 7] 中，速度位于元素 [2 5 8] 中，加速度位于元素 [3 6 9] 中。

轨迹结构体输入的 `StateCovariance` 字段必须在与轨迹结构体 `State` 字段的位置、速度和转向率对应的行和列中包含位置、速度和转向率协方差。

### **Labeling error** — 错误分配的惩罚 `0` (default) | 非负标量

轨迹到真值错误分配的惩罚，指定为非负标量。该函数根据从 **Assignments** 输入端口提供的已知分配输入来判断分配是否正确。如果未将分配作为输入提供，则假定最后一个已知分配是正确的。

**示例：**
`5`

#### 依赖关系

要启用此参数，请将 **Metric** 参数设置为 `OSPA`。

### **Window length** — OSPA(2) 度量的滑动窗口长度 `100` (default) | 正整数

OSPA(2) 度量的滑动窗口长度，指定为正整数。窗口长度定义用于评估度量的从前一时刻到当前时刻的时间步数。有关更多详细信息，请参阅 OSPA(2) 度量。

#### 依赖关系

要启用此参数，请将 **Metric** 参数设置为 `OSPA(2)`。

**数据类型：** `single` | `double`

### **Window sum order (q)** — 轨迹和真值历史的加权求和阶数 `2` (default) | 正标量

轨迹和真值历史的加权求和阶数，指定为正标量。有关更多详细信息，请参阅 OSPA(2) 度量。

#### 依赖关系

要启用此参数，请将 **Metric** 参数设置为 `OSPA(2)`。

**数据类型：** `single` | `double`

### **Window weights** — 窗口权重选项 `auto` (default) | `custom`

窗口权重选项，指定为 `auto` 或 `custom`。

- `auto` — 使用 OSPA(2) 度量中给出的算法自动生成窗口权重。
- `custom` — 使用 **Custom window weights** 参数自定义窗口权重。

#### 依赖关系

要启用此参数，请将 **Metric** 参数设置为 `OSPA(2)`。

**数据类型：** `single` | `double`

### **Window weight exponent (r)** — 自动权重计算的指数 `1` (default) | 非负标量

自动权重计算的指数，指定为非负标量。指数值 *r* 为 `0` 表示窗口中的权重相等。*r* 值越高，对最近数据赋予的权重越大。有关更多详细信息，请参阅 OSPA(2) 度量。

#### 依赖关系

要启用此参数，请将 **Window weights** 参数设置为 `auto`。

**数据类型：** `single` | `double`

### **Custom window weights** — 时间窗口中的自定义权重 *N* 元素非负值向量

时间窗口中的自定义权重，指定为非负值的 *N* 元素向量，其中 *N* 是在 **Window length** 参数中指定的窗口长度。

#### 依赖关系

要启用此参数，请将 **Window weights** 参数设置为 `custom`。

**数据类型：** `single` | `double`

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code Generation`

从以下选项中选择仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间。

#### 端口设置

### **Assignments** — 启用分配输入 `off` (default) | `on`

选择此参数可通过 **Assignments** 输入端口启用已知分配的输入。

#### 依赖关系

要启用此参数，请将 **Metric** 参数设置为 `OSPA`。

### **Localization error** — 启用定位误差分量输出 `off` (default) | `on`

选择此参数可通过 **Localization Error** 输出端口启用定位误差分量的输出。

### **Cardinality error** — 启用基数误差分量输出 `off` (default) | `on`

选择此参数可通过 **Cardinality Error** 输出端口启用基数误差分量的输出。

### **Labeling error** — 启用标签误差分量输出 `off` (default) | `on`

选择此参数可通过 **Labeling Error** 输出端口启用标签误差分量的输出。

#### 依赖关系

要启用此参数，请将 **Metric** 参数设置为 `OSPA`。

### **Track bus** — 轨迹总线选择 `objectTrack` (default) | `custom`

轨迹总线选择，指定为 `objectTrack` 或 `custom`。有关每个选择的更多详细信息，请参阅 **Tracks** 输入端口的描述。

### **Truth bus** — 真值总线选择 `Platform` (default) | `Actor` | `custom`

真值总线选择，指定为 `Platform`、`Actor` 或 `custom`。有关每个选择的更多详细信息，请参阅 **Truths** 输入端口的描述。

### **Track extractor function** — 轨迹提取函数，函数句柄

轨迹提取函数，指定为函数句柄。该函数必须支持以下语法：

```
tracks = trackExtractorFcn(trackInputFromBus)
```

其中 `trackInputFromBus` 是来自轨迹总线的输入，`tracks` 必须返回为具有 `TrackID` 和 `State` 字段的结构体数组。如果在 **Distance type** 参数中指定基于 NEES 的距离（`posnees` 或 `velnees`），则该结构体必须包含 `StateCovariance` 字段。

**示例：**  `@myCustomFcn`

#### 依赖关系

要启用此属性，请将 **Track bus** 参数设置为 `custom`。

### **Truth extractor function** — 真值提取函数，函数句柄

真值提取函数，指定为函数句柄。该函数必须支持以下语法：

```
 truths = truthExtractorFcn(truthInputFromBus)
```

其中 `truthInputFromBus` 是来自轨迹总线的输入，`truths` 必须返回为具有 `PlatformID`、`Position` 和 `Velocity` 字段名的结构体数组。

**示例：**
`@myCustomFcn`

#### 依赖关系

要启用此属性，请将 **Truth bus** 参数设置为 `custom`。

## 所属库

Sensor Fusion and Tracking Toolbox / Track Metrics

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2023a: Simulink 总线不在工作区中显示

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

计算 Optimal Subpattern Assignment Metric

Optimal Subpattern Assignment Metric 模块计算一组航迹与已知真值之间的最优子模式分配度量。您可以通过配置以下参数来启用不同类型的 OSPA 度量：

- 传统 OSPA — 将 **Metric** 参数指定为 `OSPA`，并在 **Properties** 选项卡上将 **Labeling error** 参数指定为 `0`。传统 OSPA 度量评估瞬时跟踪性能，包含两个分量：

  - 定位误差分量 — 考虑已分配航迹与真值之间的状态估计误差。
  - 基数误差分量— 考虑未分配航迹和真值的数量。
- 带标签的 OSPA — 将 **Metric** 参数指定为 `OSPA`，并在 **Properties** 选项卡上将 **Labeling error** 参数指定为一个正标量。带标签的 OSPA (LOSPA) 度量评估瞬时跟踪性能，并包含对不正确分配的惩罚，包含三个分量：

  - 定位误差分量 — 考虑已分配航迹与真值之间的状态估计误差。
  - 基数误差分量— 考虑未分配航迹和真值的数量。
  - 标签错误分量 — 考虑不正确分配的误差。
- OSPA(2) — 将 **Metric** 参数指定为 `OSPA(2)`。OSPA(2) 度量评估一段时间内的累积跟踪性能。

您可以从该模块中分别输出每个分量。有关该算法的更多详细信息，请参阅算法和参考文献。
