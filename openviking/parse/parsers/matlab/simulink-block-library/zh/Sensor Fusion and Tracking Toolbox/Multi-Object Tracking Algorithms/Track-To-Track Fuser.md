---
type: simulink-block
title: 'Track-To-Track Fuser'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multi-Object Tracking Algorithms'
documentation_page: 'tracktotrackfuser'
documentation_source_path: 'ref/tracktotrackfuser.html'
language: zh-CN
chinese_source: worker-translation
---

# Track-To-Track Fuser

## 端口

### 输入

### **Tracks** — 航迹列表 包含 MATLAB® 结构的 Simulink 总线

航迹列表，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构体数组 |

航迹结构体的字段如航迹结构中所示。

### **Prediction Time** — 航迹更新时间 实数标量

航迹更新时间，指定为以秒为单位的实数标量。融合器将所有航迹更新到该时间。每次调用该模块时，更新时间必须递增。更新时间必须至少与 **Tracks** 输入端口中所指定的最大 `UpdateTime` 一样大。

如果未启用此端口，则由 Simulink 管理的仿真时钟确定更新时间。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上，将 **Prediction time source** 设置为 `Input port`。

### **Source Configurations** — 源配置列表 包含 MATLAB 结构的 Simulink 总线

源配置列表，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumConfigurations` | 非默认源配置的数量。该字段值必须小于 **Maximum number of source configurations** 参数中指定的值。 |
| `Configurations` | 源配置结构体数组。 |

源配置结构体的字段为：

| 字段名称 | 描述 |
| --- | --- |
| `SourceIndex` | 源系统的唯一索引，指定为正整数。 |
| `IsInternalSource` | 指示源是否为融合器内部源，指定为 `true` 或 `false`。内部源是指即使航迹不是自报告的，融合器也直接融合其航迹的源。例如，如果融合器位于车辆级别，则安装在相关车辆上的跟踪雷达被视为内部源，而报告融合航迹的另一辆车被视为外部源。 |
| `IsInitializingCentralTracks` | 指示源是否可以在融合器中初始化中央航迹，指定为 `true` 或 `false`。中央航迹是在融合器中维护的航迹。 |
| `LocalToCentralTransformFcn` | 将航迹从局部状态空间变换到中央状态空间的函数，指定为包含变换函数名称的字符串或字符向量。 |
| `CentralToLocalTransformFcn` | 将航迹从中央状态空间变换到局部状态空间的函数，指定为包含变换函数名称的字符串或字符向量。 |

#### 依赖关系

要启用此端口，请在 **Fuser Management** 选项卡上，选中 **Update source configurations with time** 参数。

### **State Parameters** — 航迹状态参数 包含 MATLAB 结构的 Simulink 总线

航迹状态参数，指定为包含 MATLAB 结构的 Simulink 总线。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构体数组 |

该模块将 `Parameters` 字段的值用于所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹报告所在的参考坐标系或所生成航迹的其他所需属性。

例如，您可以使用以下结构来定义一个矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **Tracker Configuration** 选项卡中，选中 **Update track state parameters with time** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹，返回为包含 MATLAB 结构的 Simulink 总线。该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of central tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如 Track Structure 中所示。

如果航迹满足 **Tracks** 选项卡上 **Confirmation threshold** 参数中指定的阈值，则该航迹被确认。

### **Tentative Tracks** — 暂定航迹 包含 MATLAB 结构的 Simulink 总线

暂定航迹，返回为包含 MATLAB 结构的 Simulink 总线。航迹在被确认之前是暂定的。

该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of central tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如 Track Structure 中所示。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择
**Enable tentative tracks output**。

### **All Tracks** — 确认航迹和暂定航迹 包含 MATLAB 结构的 Simulink 总线

确认航迹和暂定航迹的组合列表，返回为包含 MATLAB 结构的 Simulink 总线。

该结构的形式如下：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构数组，其长度由 **Maximum number of central tracks** 参数设定。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段如 Track Structure 中所示。

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择
**Enable all tracks output**。

### **Info** — 用于分析航迹更新的附加信息 包含 MATLAB 结构的 Simulink 总线

用于分析航迹更新的附加信息，返回为包含 MATLAB 结构的 Simulink 总线。

下表显示了 info 结构的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `BranchIDsAtStepBeginning` | 更新开始时的分支 ID。 |
| `CostMatrix` | 分配矩阵的代价。 |
| `Assignments` | 从 `assignTOMHT` 函数返回的分配。 |
| `UnassignedTracks` | 从跟踪器返回的未分配分支的 ID。 |
| `UnassignedDetections` | 从跟踪器返回的未分配检测的 ID。 |
| `InitialBranchHistory` | 分支后、剪枝前的分支历史。 |
| `InitialBranchScores` | 剪枝前的分支得分。 |
| `KeptBranchHistory` | 初始剪枝后的分支历史。 |
| `KeptBranchScores` | 初始剪枝后的分支得分。 |
| `Clusters` | 将分支映射到聚类的逻辑数组。如果分支在其历史中共享检测，或者直接或通过其他分支属于同一航迹，则这些分支属于同一聚类。 |
| `TrackIncompatibility` | 分支不兼容矩阵。如果第 *i* 个和第 *j* 个分支在其历史中共享检测或属于同一航迹，则 `(i,j)` 元素为 `true`。 |
| `GlobalHypotheses` | 将分支映射到全局假设的逻辑矩阵。兼容的分支可以属于同一假设。 |
| `GlobalHypScores` | 全局假设的总得分。 |
| `PrunedBranches` | `pruneTrackBranches` 函数确定要剪枝的分支的逻辑数组。 |
| `GlobalBranchProbabilities` | 每个分支在全局假设中存在的全局概率。 |
| `BranchesDeletedByPruning` | 被跟踪器删除的分支。 |
| `BranchIDsAtStepEnd` | 更新结束时的分支 ID。 |

#### 依赖关系

要启用此端口，请在 **Port Setting** 选项卡上选择
**启用信息输出**。

## 参数

#### Fuser Management

### **Fuser Index** — 跟踪融合器的唯一索引 `1`（默认）| 正整数

融合器的唯一索引，指定为正整数。使用此属性可在多融合器环境中区分不同的融合器。

**示例：**
`2`

### **Assignment algorithm name** — 关联算法 `MatchPairs`（默认）| `Munkres` | `Jonker-Volgenant` | `Auction` | `Custom`

关联算法，指定为 `MatchPairs`、`Munkres`、`Jonker-Volgenant`、`Auction` 或 `Custom`。Munkres 是唯一能保证最优解的关联算法，但它也是最慢的，尤其是在检测和航迹数量较大时。其他算法不保证最优解，但对于具有 20 个或更多航迹和检测的问题可能更快。使用 `Custom` 可定义您自己的关联函数，并在 **Name of 'Custom' assignment function** 参数中指定其名称。

**数据类型：** `char`

### **Name of 'Custom' assignment function** — 'Custom' 关联函数的名称 函数名

'Custom' 关联函数的名称，指定为函数名。关联函数必须具有以下语法：

```
 [assignments,unassignedCentral,unassignedLocal] = myfun(cost,costNonAssignment)
```

有关关联函数的示例及其参数的说明，请参阅 `assignmunkres`。

**示例：** `myfun`

#### 依赖关系

要启用此属性，请将 **Assignment algorithm name** 参数设置为 `Custom`。

### **Threshold for assigning source to central tracks** — 将源航迹关联到中心航迹的阈值 `[1 Inf]*30.0`（默认）| 正标量 | 1×2 正数值向量

将源航迹关联到中心航迹的阈值，指定为正标量或形式为 [*C*1 *C*2] 的 1×2 向量，其中 *C*1 ≤ *C*2。如果指定为标量，则指定值 *val* 将扩展为 [*val* `Inf`]。

最初，融合器对所有源航迹和中心航迹之间的归一化距离执行粗略估计。融合器仅对粗略归一化距离小于 *C*2 的源航迹和中心航迹组合计算精确归一化距离。此外，融合器仅在其精确归一化距离小于 *C*1 时才能将局部航迹关联到中心航迹。有关归一化距离的说明，请参阅算法。

**提示**

- 如果存在应计算关联但未被计算的源航迹和中心航迹组合，请增大 *C*2 的值。如果计算耗时过长，请减小该值。
- 如果存在应关联到中心航迹但未被关联的源航迹，请增大 *C*1 的值。如果存在被关联到不应关联的中心航迹（距离太远）的局部航迹，请减小该值。

### **Maximum number of central tracks** — 中心航迹的最大数量 `100`（默认）| 正整数

跟踪器可维护的中心航迹的最大数量，指定为正整数。

### **Maximum number of source configurations** — 源配置的最大数量 `20`（默认）| 正整数

融合器可维护的源配置的最大数量，指定为正整数。

### **源配置** — 源系统的配置 `struct('SourceIndex',1)`（默认）| 源配置结构体数组

源系统的配置，指定为源配置结构体数组。源配置结构体的字段包括：

| 字段名 | 描述 |
| --- | --- |
| `SourceIndex` | 源系统的唯一索引，指定为正整数。 |
| `IsInternalSource` | 指示源是否为融合器内部源，指定为 `true` 或 `false`。内部源是指融合器直接融合其航迹的源，即使这些航迹不是自报告的。例如，如果融合器位于车辆级别，则安装在相关车辆上的跟踪雷达被视为内部源，而另一辆报告融合航迹的车辆被视为外部源。 |
| `IsInitializingCentralTracks` | 指示源是否可以在融合器中初始化中央航迹，指定为 `true` 或 `false`。中央航迹是在融合器中维护的航迹。 |
| `LocalToCentralTransformFcn` | 将航迹从局部状态空间变换到中央状态空间的函数，指定为包含变换函数名称的字符串或字符向量。 |
| `CentralToLocalTransformFcn` | 将航迹从中央状态空间变换到局部状态空间的函数，指定为包含变换函数名称的字符串或字符向量。 |

### **随时间更新源配置** — 随时间更新源配置 `off`（默认）| `on`

选择此参数以启用通过 **源配置** 输入端口输入源配置。

### **航迹状态参数** — 航迹状态参考系的参数 结构体 | 结构体数组

将航迹状态参考系的参数指定为结构体或结构体数组。该模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数来定义航迹报告所在的参考系或所生成航迹的其他所需属性。

例如，您可以使用以下结构体定义一个矩形参考系，其原点位置相对于场景坐标系为 `[10 10 0]` 米，原点速度为 `[2 -2 0]` 米每秒。

| 字段名 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

您可以通过选择 **随时间更新航迹状态参数** 参数，通过 **状态参数** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **随时间更新航迹状态参数** — 随时间更新航迹状态参数 `off`（默认）| `on`

选择此参数以启用通过 **状态参数** 输入端口输入航迹状态参数的输入端口。

### **仿真方式** — 要运行的仿真类型 `解释执行`（默认）| `代码生成`

从以下选项中选择仿真类型：

- `解释执行` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `解释执行` 模式下，您可以调试模块的源代码。
- `代码生成` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。

#### 航迹

### **Confirmation threshold [M N]** — 中心航迹确认阈值 `[2 3]`（默认）| 正整数 | 正整数的实值 1×2 向量

中心航迹确认阈值，指定为正整数 *M*，或正整数的实值 1×2 向量 [*M* *N*]。如果在最近 *N* 次更新中，中心航迹至少被分配到局部航迹 *M* 次，则该中心航迹被确认。如果指定为正整数 *M*，则确认阈值扩展为 [*M* *M*]。

### **Deletion threshold [P Q]** — 中心航迹删除阈值 `[5 5]`（默认）| 正整数 | 正整数的实值 1×2 向量

中心航迹删除阈值，指定为正整数 *P*，或正整数的 1×2 向量 [*P* *Q*]，其中 *P* *≤* *Q*。如果在最近 *Q* 次更新中，航迹至少未被分配到局部航迹 *P* 次，则该中心航迹被删除。如果指定为正整数 *P*，则确认阈值扩展为 [*P* *P*]。

### **Central track state size** — 中心航迹状态大小 `6`（默认）| 正整数

中心航迹状态大小，指定为正整数。

### **Central track object attributes** — 中心航迹对象属性 `struct`（默认）| 结构体

中心航迹对象属性，指定为结构体。跟踪器将此参数的值传递给航迹输出的 `ObjectAttributes` 字段。

### **State transition function** — 状态转移函数 `constvel`（默认）| 函数名

状态转移函数，指定为函数名。此函数基于时间步 *k*–1 的状态计算时间步 *k* 的状态。

- 如果 **Tracks** 选项卡上的 **Enable additive process noise** 参数已启用，则该函数必须使用以下语法：

  ```
  x(k) = f(x(k-1),dt)
  ```

  其中：

  - `x(k)` — 时间 `k` 的估计状态，指定为向量或矩阵。如果指定为矩阵，则矩阵的每一列表示一个状态向量。
  - `dt` — 预测的时间步。
- 如果 **Tracks** 选项卡上的 **Enable additive process noise** 参数未启用，则该函数必须使用以下语法：

  ```
  x(k) = f(x(k-1),w(k-1),dt)
  ```

  其中：

  - `x(k)` — 时间 `k` 的估计状态，指定为向量或矩阵。如果指定为矩阵，则矩阵的每一列表示一个状态向量。
  - `w(k)` — 时间 `k` 的过程噪声。
  - `dt` — 预测的时间步。

**示例：** `@constacc`

### **State transition Jacobian function** — 状态转移雅可比函数函数名称

状态转移函数的雅可比，指定为函数名称。如果未指定，则通过数值计算雅可比，这可能会增加处理时间并降低数值精度。如果指定，该函数必须支持以下两种语法之一：

- 如果 **Tracks** 选项卡上的 **Enable additive process noise** 参数已启用，则该函数必须使用以下语法：

  ```
  Jx(k) = statejacobianfcn(x(k),dt)
  ```

  其中：

  - `x(k)` — 时刻 `k` 的估计状态，指定为 *M*×1 的实数值向量。
  - `dt` — 预测的时间步长。
  - `Jx(k)` — 状态转移函数关于状态的雅可比 `df/dx`，在 `x(k)` 处求值。雅可比以 *M*×*M* 矩阵形式返回。
- 如果 **Tracks** 选项卡上的 **Enable additive process noise** 参数未启用，则该函数必须使用以下语法：

  ```
  [Jx(k),Jw(k)] = statejacobianfcn(x(k),w(k),dt)
  ```

  其中：

  - `x(k)` — 时刻 `k` 的（估计）状态，指定为 *M*×1 的实数值向量。
  - `w(k)` — 时刻 `k` 的过程噪声，指定为 *W*×1 的实数值向量。
  - `dt` — 预测的时间步长。
  - `Jx(k)` — 状态转移函数关于状态的雅可比 `df/dx`，在 `x(k)` 处求值。雅可比以 *M*×*M* 矩阵形式返回。
  - `Jw(k)` — 状态转移函数关于过程噪声的雅可比 `df/dw`，在 `x(k)` 和 `w(k)` 处求值。雅可比以 *M*×*W* 矩阵形式返回。

**示例：** `@constaccjac`

### **Process noise matrix** — 过程噪声矩阵 `eye(3)`（默认）| 正实标量 | 正定矩阵

过程噪声协方差矩阵，指定为正实标量或正定矩阵。

- 当 **Tracks** 选项卡上的 **Enable additive process noise** 参数已启用时，将过程噪声协方差指定为正实标量或正定 *M*×*M* 矩阵。*M* 是状态向量的维度。当指定为标量时，该矩阵为 *M*×*M* 对角矩阵，每个对角元素等于该标量。
- 当 **Tracks** 选项卡上的 **Enable additive process noise** 参数未启用时，将过程噪声协方差指定为 *W*×*W* 矩阵。*W* 是过程噪声向量的维度。

**示例：** `[1.0 0.05; 0.05 2`]

### **Enable additive process noise** — 启用加性过程噪声 `off`（默认）| `on`

启用加性过程噪声，指定为 `on` 或 `off`。当为 `on` 时，过程噪声被添加到状态向量。否则，噪声被纳入状态转移函数。

#### Fusion

### **State fusion function** — 状态融合函数 `Cross`（默认）| `Intersection` | `Custom`

状态融合函数，指定为以下选项之一：

- `Cross` — 使用互协方差融合算法
- `Intersection` — 使用协方差交集融合算法
- `Custom` — 允许您使用 **Name of 'Custom' fusion function** 参数指定自定义融合函数

使用 **State fusion parameters source** 参数指定状态融合算法使用的附加参数。

### **Name of 'Custom' fusion function** — 自定义关联函数的名称 函数名

自定义关联函数的名称，指定为字符串或函数名。

状态融合函数必须支持以下语法之一：

```
[fusedState,fusedCov] = f(trackState,trackCov)
[fusedState,fusedCov] = f(trackState,trackCov,fuseParams)
```

其中：

- `trackState` 指定为 *N*×*M* 矩阵。*N* 是航迹状态的维度，*M* 是航迹数量。
- `trackCov` 指定为 *N*×*N*×*M* 矩阵。*N* 是航迹状态的维度，*M* 是航迹数量。
- `fuseParams` 是在 **State fusion parameters source** 参数中定义的可选参数。
- `fusedState` 返回为 *N*×1 向量。
- `fusedCov` 返回为 *N*×*N* 矩阵。

#### 依赖关系

要启用此属性，请将 **State fusion function** 参数设置为 `Custom`。

### **State fusion parameters source** — 状态融合参数源 `Auto`（默认）| `Property`

状态融合参数源，指定为以下选项之一：

- `Auto` — 模块为每种状态融合算法使用默认值融合参数。有关更多详细信息，请参阅 **Cross covariance factor**、**Optimize covariance based on** 和 **State fusion custom algorithm parameters**。
- `Property` — 使用以下参数设置状态融合参数

  - 当 **State fusion function** 选择为 `Cross` 时，使用 **Cross covariance factor** 参数。
  - 当 **State fusion function** 选择为 `Intersection` 时，使用 **Optimize covariance based on** 参数。
  - 当 **State fusion function** 选择为 `Custom` 时，使用 **State fusion custom algorithm parameters** 参数。

### **Cross covariance factor** — 互协方差因子 `0.4`（默认）| (0,1) 范围内的标量

互协方差因子，指定为 (0,1) 范围内的标量。有关更多详细信息，请参阅 `fusexcov`。

### **Optimize covariance based on** — 交集算法准则 `det`（默认）| `trace`

交集算法准则，指定为 `det` 或 `trace`。有关更多详细信息，请参阅 `fusecovint`。

### **State fusion custom algorithm parameters** — 状态融合自定义算法参数 MATLAB 变量

状态融合自定义算法参数，可以指定为任意变量类型，只要它与自定义状态融合函数的可选 `fuseParams` 输入的设置相匹配，该输入在 **Name of 'Custom' assignment function** 参数中指定。

### **Fuse only confirmed source tracks** — 仅融合已确认的源航迹 `on`（默认）| `off`

仅融合已确认的源航迹，指定为 `on` 或 `off`。如果要融合所有源航迹而不考虑其确认状态，请将此参数设置为 `off`。

### **Fuse coasted source tracks** — 仅融合已确认的源航迹 `off`（默认）| `on`

融合滑行源航迹，指定为 `off` 或 `on`。如果要融合滑行源航迹，请将此参数设置为 `on`。如果只想融合未滑行的源航迹，请将其设置为 `off`。

#### Port Setting

### **Prediction time source** — 预测时间源 `Auto`（默认）| `Input port`

预测时间源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以通过 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **Enable tentative tracks output** — 启用暂定航迹输出端口 `off`（默认）| `on`

选择此参数以通过 **Tentative Tracks** 输出端口启用暂定航迹的输出。

### **Enable all tracks output** — 启用所有航迹输出端口 `off`（默认）| `on`

选择此参数以通过 **All Tracks** 输出端口启用所有航迹的输出。

### **Enable information output** — 启用分析信息的输出端口 `off`（默认）| `on`

选择此参数可通过 **Info** 输出端口启用分析信息的输出端口。

### **Source of output bus name** — 输出航迹总线名称的来源 `Auto`（默认）| `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 通过 **Specify an output bus name** 参数指定输出航迹总线名称。

### **Source of output info bus name** — 输出信息总线名称的来源 `Auto`（默认）| `Property`

输出信息总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 通过 **Fuser info bus name** 参数指定输出信息总线名称。

## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2023a：Simulink 总线不显示在工作区中

从 R2023a 起，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

航迹对航迹融合

Track-to-Track Fuser Simulink® 模块是一种多源、多目标、航迹级融合器，它使用全局最近邻（GNN）关联来维护关于其所融合航迹的单一假设。该模块的输入是来自已经跟踪多个目标的源的航迹，例如多目标跟踪器模块或其他航迹对航迹融合器模块。输入航迹称为*源航迹*或*局部航迹*，而融合器中维护的航迹称为*中心航迹*。
