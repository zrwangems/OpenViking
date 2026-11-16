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

### **Tracks** — 航迹列表，包含 MATLAB® structure 的 Simulink bus

航迹列表，指定为包含 MATLAB structure 的 Simulink bus。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量 |
| `Tracks` | 航迹结构的数组 |

航迹结构的字段见航迹结构部分。

### **Prediction Time** — 航迹更新时间 real scalar

航迹更新时间，指定为以 seconds 为单位的 real scalar。融合器将所有航迹更新到该时间。每次调用模块时，更新时间必须增大。更新时间必须至少等于 **Tracks** 输入端口中指定的最大 `UpdateTime`。

如果未启用此端口，则由 Simulink 管理的仿真时钟确定更新时间。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，将 **预测时间源** 设置为 `Input port`。

### **Source Configurations** — 源配置列表，包含 MATLAB structure 的 Simulink bus

源配置列表，指定为包含 MATLAB structure 的 Simulink bus。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumConfigurations` | 非默认源配置的数量。该字段值必须小于 **源配置的最大数量** 参数中指定的值。 |
| `Configurations` | 源配置结构的数组。 |

源配置结构的字段为：

| 字段名称 | 描述 |
| --- | --- |
| `SourceIndex` | 源系统的唯一索引，指定为正整数。 |
| `IsInternalSource` | 指示源是否在融合器内部，指定为 `true` 或 `false`。内部源是融合器直接融合其航迹的源，即使这些航迹不是自报告的。例如，如果融合器位于车辆级别，则安装在相关车辆上的跟踪雷达被视为内部源，而报告融合航迹的另一辆车被视为外部源。 |
| `IsInitializingCentralTracks` | 指示源是否可以在融合器中初始化中心航迹，指定为 `true` 或 `false`。中心航迹是在融合器中维护的航迹。 |
| `LocalToCentralTransformFcn` | 用于将航迹从局部状态空间变换到中心状态空间的函数，指定为包含变换函数名称的 string 或 character vector。 |
| `CentralToLocalTransformFcn` | 用于将航迹从中心状态空间变换到局部状态空间的函数，指定为包含变换函数名称的 string 或 character vector。 |

#### 依赖关系

要启用此端口，请在 **融合器管理** 选项卡上，选择 **随时间更新源配置** 参数。

### **State Parameters** — 航迹状态参数，包含 MATLAB structure 的 Simulink bus

航迹状态参数，指定为包含 MATLAB structure 的 Simulink bus。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumParameters` | 非默认状态参数的数量，指定为非负整数 |
| `Parameters` | 状态参数结构的数组 |

模块使用 `Parameters` 字段的值作为所生成航迹的 `StateParameters` 字段。您可以使用这些参数定义报告航迹时所处的参考坐标系，或所生成航迹的其他所需属性。

例如，您可以使用以下结构定义矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

#### 依赖关系

要启用此端口，请在 **跟踪器配置** 选项卡中，选择 **随时间更新航迹状态参数** 参数。
### 输出

### **Confirmed Tracks** — 确认航迹，包含 MATLAB structure 的 Simulink bus

确认航迹，返回为包含 MATLAB structure 的 Simulink bus。该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构的数组，其长度由 **中心航迹的最大数量** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段见航迹结构部分。

如果航迹满足 **航迹** 选项卡上 **确认阈值** 参数中指定的阈值，则该航迹被确认。

### **Tentative Tracks** — 暂定航迹，包含 MATLAB structure 的 Simulink bus

暂定航迹，返回为包含 MATLAB structure 的 Simulink bus。航迹在被确认之前是暂定航迹。

该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构的数组，其长度由 **中心航迹的最大数量** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段见航迹结构部分。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用暂定航迹输出**。

### **All Tracks** — 确认和暂定航迹，包含 MATLAB structure 的 Simulink bus

确认航迹和暂定航迹的组合列表，返回为包含 MATLAB structure 的 Simulink bus。

该结构的形式为：

| 字段 | 描述 |
| --- | --- |
| `NumTracks` | 航迹数量。 |
| `Tracks` | 航迹结构的数组，其长度由 **中心航迹的最大数量** 参数设置。其中只有前 `NumTracks` 个是实际航迹。 |

航迹结构的字段见航迹结构部分。

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用所有航迹输出**。

### **Info** — 用于分析航迹更新的附加信息，包含 MATLAB structure 的 Simulink bus

用于分析航迹更新的附加信息，返回为包含 MATLAB structure 的 Simulink bus。

下表显示 info 结构的字段：

|  |  |
| --- | --- |
| **字段** | **描述** |
| `BranchIDsAtStepBeginning` | 更新开始时的分支 ID。 |
| `CostMatrix` | 分配矩阵的代价。 |
| `Assignments` | 从 `assignTOMHT` 函数返回的分配。 |
| `UnassignedTracks` | 跟踪器返回的未分配分支的 ID。 |
| `UnassignedDetections` | 跟踪器返回的未分配检测的 ID。 |
| `InitialBranchHistory` | 分支后、修剪前的分支历史。 |
| `InitialBranchScores` | 修剪前的分支得分。 |
| `KeptBranchHistory` | 初始修剪后的分支历史。 |
| `KeptBranchScores` | 初始修剪后的分支得分。 |
| `Clusters` | 将分支映射到聚类的逻辑数组。如果分支在其历史中共享检测，或直接或通过其他分支属于同一航迹，则它们属于同一聚类。 |
| `TrackIncompatibility` | 分支不兼容性矩阵。如果第 *i* 个和第 *j* 个分支在其历史中共享检测或属于同一航迹，则 `(i,j)` 元素为 `true`。 |
| `GlobalHypotheses` | 将分支映射到全局假设的逻辑矩阵。兼容的分支可以属于同一假设。 |
| `GlobalHypScores` | 全局假设的总得分。 |
| `PrunedBranches` | `pruneTrackBranches` 函数决定修剪的分支的逻辑数组。 |
| `GlobalBranchProbabilities` | 每个分支存在于全局假设中的全局概率。 |
| `BranchesDeletedByPruning` | 跟踪器删除的分支。 |
| `BranchIDsAtStepEnd` | 更新结束时的分支 ID。 |

#### 依赖关系

要启用此端口，请在 **端口设置** 选项卡上，选择 **启用信息输出**。

## 参数

#### 融合器管理

### **融合器索引** — 航迹融合器的唯一索引 `1` (default) | 正整数

融合器的唯一索引，指定为正整数。在多融合器环境中，使用此属性区分不同的融合器。

**示例：**
`2`

### **分配算法名称** — 分配算法 `MatchPairs` (default) | `Munkres` | `Jonker-Volgenant` | `Auction` | `Custom`

分配算法，指定为 `MatchPairs`、`Munkres`、`Jonker-Volgenant`、`Auction` 或 `Custom`。Munkres 是唯一保证最优解的分配算法，但也是最慢的，尤其是在检测和航迹数量很大时。其他算法不保证最优解，但对于具有 20 个或更多航迹和检测的问题可能更快。使用 `Custom` 定义您自己的分配函数，并在 **'Custom' 分配函数的名称** 参数中指定其名称。

**数据类型：** `char`

### **'Custom' 分配函数的名称** — 'Custom' 分配函数的名称，函数名称

'Custom' 分配函数的名称，指定为函数名称。分配函数必须具有以下语法：

    [assignments,unassignedCentral,unassignedLocal] = myfun(cost,costNonAssignment)

有关分配函数的示例及其参数说明，请参阅 `assignmunkres`。

**示例：** `myfun`

#### 依赖关系

要启用此属性，请将 **分配算法名称** 参数设置为 `Custom`。

### **将源分配到中心航迹的阈值** — 将源分配到中心航迹的阈值 `[1 Inf]*30.0` (default) | 正标量 | 正值的 1-by-2 向量

将源分配到中心航迹的阈值，指定为正标量或形式为 [*C*1 *C*2] 的 1-by-2 向量，其中 *C*1 ≤ *C*2。如果指定为标量，则指定值 *val* 会扩展为 [*val* `Inf`]。

最初，融合器对所有源航迹和中心航迹之间的归一化距离执行粗略估计。融合器仅对粗略归一化距离小于 *C*2 的源和中心组合计算精确归一化距离。此外，仅当局部航迹与中心航迹的精确归一化距离小于 *C*1 时，融合器才能将局部航迹分配到中心航迹。有关归一化距离的说明，请参阅算法。

**提示**

- 如果存在应计算以进行分配但未计算的源航迹和中心航迹组合，请增大 *C*2 的值。如果计算耗时过长，请减小该值。
- 如果存在应分配到中心航迹但未分配的源航迹，请增大 *C*1 的值。如果存在被分配到不应分配到的中心航迹（距离太远）的局部航迹，请减小该值。

### **中心航迹的最大数量** — 中心航迹的最大数量 `100` (default) | 正整数

跟踪器可以维护的中心航迹的最大数量，指定为正整数。

### **源配置的最大数量** — 源配置的最大数量 `20` (default) | 正整数

融合器可以维护的源配置的最大数量，指定为正整数。

### **源配置** — 源系统的配置 `struct('SourceIndex',1)` (default) | 源配置结构数组

源系统的配置，指定为源配置结构的数组。源配置结构的字段为：

| 字段名称 | 描述 |
| --- | --- |
| `SourceIndex` | 源系统的唯一索引，指定为正整数。 |
| `IsInternalSource` | 指示源是否在融合器内部，指定为 `true` 或 `false`。内部源是融合器直接融合其航迹的源，即使这些航迹不是自报告的。例如，如果融合器位于车辆级别，则安装在相关车辆上的跟踪雷达被视为内部源，而报告融合航迹的另一辆车被视为外部源。 |
| `IsInitializingCentralTracks` | 指示源是否可以在融合器中初始化中心航迹，指定为 `true` 或 `false`。中心航迹是在融合器中维护的航迹。 |
| `LocalToCentralTransformFcn` | 用于将航迹从局部状态空间变换到中心状态空间的函数，指定为包含变换函数名称的 string 或 character vector。 |
| `CentralToLocalTransformFcn` | 用于将航迹从中心状态空间变换到局部状态空间的函数，指定为包含变换函数名称的 string 或 character vector。 |

### **随时间更新源配置** — 随时间更新源配置 `off` (default) | `on`

选择此参数可通过 **Source configurations** 输入端口输入源配置。

### **航迹状态参数** — 航迹状态参考坐标系的参数 structure | structure array

将航迹状态参考坐标系的参数指定为 structure 或 structure array。模块将此参数的值传递给所生成航迹的 `StateParameters` 字段。您可以使用这些参数定义报告航迹时所处的参考坐标系，或所生成航迹的其他所需属性。

例如，您可以使用以下结构定义矩形参考坐标系，其原点位置相对于场景坐标系为 `[10 10 0]` meters，原点速度为 `[2 -2 0]` meters per second。

| 字段名称 | 值 |
| --- | --- |
| `Frame` | `"Rectangular"` |
| `Position` | `[10 10 0]` |
| `Velocity` | `[2 -2 0]` |

通过选择 **随时间更新航迹状态参数** 参数，您可以通过 **State Parameters** 输入端口更新航迹状态参数。

**数据类型：** `struct`

### **随时间更新航迹状态参数** — 随时间更新航迹状态参数 `off` (default) | `on`

选择此参数可通过 **State Parameters** 输入端口启用航迹状态参数的输入端口。

### **仿真使用** — 要运行的仿真类型 `Interpreted execution` (default) | `Code Generation`

从以下选项中选择仿真类型：

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间。

#### 航迹

### **确认阈值 [M N]** — 中心航迹确认阈值 `[2 3]` (default) | 正整数 | 实数值的 1-by-2 正整数向量

中心航迹确认阈值，指定为正整数 *M*，或实数值的 1-by-2 正整数向量 [*M* *N*]。如果中心航迹在最近 *N* 次更新中至少 *M* 次分配到局部航迹，则该中心航迹被确认。如果指定为正整数 *M*，则确认阈值扩展为 [*M* *M*]。

### **删除阈值 [P Q]** — 中心航迹删除阈值 `[5 5]` (default) | 正整数 | 实数值的 1-by-2 正整数向量

中心航迹删除阈值，指定为正整数 *P*，或 1-by-2 正整数向量 [*P* *Q*]，其中 *P* ≤ *Q*。如果航迹在最近 *Q* 次更新中未至少 *P* 次分配到局部航迹，则该中心航迹被删除。如果指定为正整数 *P*，则删除阈值扩展为 [*P* *P*]。

### **中心航迹状态大小** — 中心航迹状态大小 `6` (default) | 正整数

中心航迹状态大小，指定为正整数。

### **中心航迹对象属性** — 中心航迹对象属性 `struct` (默认值) | structure

中心航迹对象属性，指定为结构体。跟踪器将此参数的值传递到航迹输出的 `ObjectAttributes` 字段。

### **状态转移函数** — 状态转移函数 `constvel` (默认值) | 函数名称

状态转移函数，指定为函数名称。此函数基于时间步 *k*–1 的状态计算时间步 *k* 的状态。

- 如果 **Tracks** 选项卡上的 **启用加性过程噪声** 参数已启用，则该函数必须使用以下语法：

  ```
  x(k) = f(x(k-1),dt)
  ```

  其中：

  - `x(k)` — 时间 `k` 的估计状态，指定为向量或矩阵。如果指定为矩阵，则矩阵的每一列表示一个状态向量。
  - `dt` — 用于预测的时间步。
- 如果 **Tracks** 选项卡上的 **启用加性过程噪声** 参数未启用，则该函数必须使用以下语法：

  ```
  x(k) = f(x(k-1),w(k-1),dt)
  ```

  其中：

  - `x(k)` — 时间 `k` 的估计状态，指定为向量或矩阵。如果指定为矩阵，则矩阵的每一列表示一个状态向量。
  - `w(k)` — 时间 `k` 的过程噪声。
  - `dt` — 用于预测的时间步。

**示例：** `@constacc`

### **状态转移雅可比函数** — 状态转移雅可比函数 函数名称

状态转移函数的雅可比，指定为函数名称。如果未指定，则雅可比数值计算，这可能会增加处理时间和数值不准确度。如果指定，则该函数必须支持以下两种语法之一：

- 如果 **Tracks** 选项卡上的 **启用加性过程噪声** 参数已启用，则该函数必须使用以下语法：

  ```
  Jx(k) = statejacobianfcn(x(k),dt)
  ```

  其中：

  - `x(k)` — 时间 `k` 的估计状态，指定为 *M*-by-1 实数值向量。
  - `dt` — 用于预测的时间步。
  - `Jx(k)` — 状态转移函数关于状态的雅可比 `df/dx`，在 `x(k)` 处计算。雅可比以 *M*-by-*M* 矩阵形式返回。
- 如果 **Tracks** 选项卡上的 **启用加性过程噪声** 参数未启用，则该函数必须使用以下语法：

  ```
  [Jx(k),Jw(k)] = statejacobianfcn(x(k),w(k),dt)
  ```

  其中：

  - `x(k)` — 时间 `k` 的（估计）状态，指定为 *M*-by-1 实数值向量。
  - `w(k)` — 时间 `k` 的过程噪声，指定为 *W*-by-1 实数值向量。
  - `dt` — 用于预测的时间步。
  - `Jx(k)` — 状态转移函数关于状态的雅可比 `df/dx`，在 `x(k)` 处计算。雅可比以 *M*-by-*M* 矩阵形式返回。
  - `Jw(k)` — 状态转移函数关于过程噪声的雅可比 `df/dw`，在 `x(k)` 和 `w(k)` 处计算。雅可比以 *M*-by-*W* 矩阵形式返回。

**示例：** `@constaccjac`

### **过程噪声矩阵** — 过程噪声矩阵 `eye(3)` (默认值) | 正实数标量 | 正定矩阵

过程噪声协方差矩阵，指定为正实数标量或正定矩阵。

- 当 **Tracks** 选项卡上的 **启用加性过程噪声** 参数已启用时，将过程噪声协方差指定为正实数标量或正定 *M*-by-*M* 矩阵。*M* 是状态向量的维度。当指定为标量时，矩阵是 *M*-by-*M* 对角矩阵，每个对角元素等于该标量。
- 当 **Tracks** 选项卡上的 **启用加性过程噪声** 参数未启用时，将过程噪声协方差指定为 *W*-by-*W* 矩阵。*W* 是过程噪声向量的维度。

**示例：** `[1.0 0.05; 0.05 2`]

### **启用加性过程噪声** — 启用加性过程噪声 `off` (默认值) | `on`

启用加性过程噪声，指定为 `on` 或 `off`。当其为 `on` 时，过程噪声会添加到状态向量。否则，噪声会并入状态转移函数。

#### 融合

### **状态融合函数** — 状态融合函数 `Cross` (默认值) | `Intersection` | `Custom`

状态融合函数，指定为以下选项之一：

- `Cross` — 使用交叉协方差融合算法
- `Intersection` — 使用协方差交集融合算法
- `Custom` — 允许您使用 **“Custom”融合函数的名称** 参数指定自定义融合函数

使用 **状态融合参数来源** 参数指定状态融合算法使用的附加参数。

### **“Custom”融合函数的名称** — 自定义分配函数的名称 函数名称

自定义分配函数的名称，指定为字符串或函数名称。

状态融合函数必须支持以下语法之一：

```
[fusedState,fusedCov] = f(trackState,trackCov)
[fusedState,fusedCov] = f(trackState,trackCov,fuseParams)
```

其中：

- `trackState` 指定为 *N*-by-*M* 矩阵。*N* 是航迹状态的维度，*M* 是航迹数。
- `trackCov` 指定为 *N*-by-*N*-by-*M* 矩阵。*N* 是航迹状态的维度，*M* 是航迹数。
- `fuseParams` 是 **状态融合参数来源** 参数中定义的可选参数。
- `fusedState` 以 *N*-by-1 向量形式返回。
- `fusedCov` 以 *N*-by-*N* 矩阵形式返回。

#### 依赖关系

要启用此属性，请将 **状态融合函数** 参数设置为 `Custom`。

### **状态融合参数来源** — 状态融合参数来源 `Auto` (默认值) | `Property`

状态融合参数来源，指定为以下选项之一：

- `Auto` — 模块为每个状态融合算法使用默认值融合参数。有关更多详细信息，请参阅 **交叉协方差因子**、**优化协方差的依据** 和 **状态融合自定义算法参数**。
- `Property` — 使用以下项设置状态融合参数

  - 当 **状态融合函数** 选择为 `Cross` 时，使用 **交叉协方差因子** 参数。
  - 当 **状态融合函数** 选择为 `Intersection` 时，使用 **优化协方差的依据** 参数。
  - 当 **状态融合函数** 选择为 `Custom` 时，使用 **状态融合自定义算法参数** 参数。

### **交叉协方差因子** — 交叉协方差因子 `0.4` (默认值) | 范围 (0,1) 内的标量

交叉协方差因子，指定为范围 (0,1) 内的标量。有关更多详细信息，请参阅 `fusexcov`。

### **优化协方差的依据** — 交集算法准则 `det` (默认值) | `trace`

交集算法准则，指定为 `det` 或 `trace`。有关更多详细信息，请参阅 `fusecovint`。

### **状态融合自定义算法参数** — 状态融合自定义算法参数 MATLAB 变量

状态融合自定义算法参数，以任意变量类型指定，只要它与自定义状态融合函数的可选 `fuseParams` 输入的设置匹配（在 **“Custom”分配函数的名称** 参数中指定）。

### **仅融合已确认的源航迹** — 仅融合已确认的源航迹 `on` (默认值) | `off`

仅融合已确认的源航迹，指定为 `on` 或 `off`。如果要融合所有源航迹而不考虑其确认状态，请将此参数设置为 `off`。

### **融合滑行源航迹** — 融合滑行源航迹 `off` (默认值) | `on`

融合滑行源航迹，指定为 `off` 或 `on`。如果要融合滑行源航迹，请将此参数设置为 `on`。如果只想融合未滑行的源航迹，请将其设置为 `off`。

#### 端口设置

### **预测时间来源** — 预测时间的来源 `Auto` (默认值) | `Input port`

预测时间来源，指定为 `Input port` 或 `Auto`。选择 `Input port` 以使用 **Prediction Time** 输入端口输入更新时间。否则，由 Simulink 管理的仿真时钟确定更新时间。

### **启用暂定航迹输出** — 启用暂定航迹的输出端口 `off` (默认值) | `on`

选择此参数以通过 **Tentative Tracks** 输出端口启用暂定航迹的输出。

### **启用所有航迹输出** — 启用所有航迹的输出端口 `off` (默认值) | `on`

选择此参数以通过 **All Tracks** 输出端口启用所有航迹的输出。

### **启用信息输出** — 启用分析信息的输出端口 `off` (默认值) | `on`

选择此参数以启用分析信息的输出端口，即 **Info** 输出端口。

### **输出总线名称的来源** — 输出航迹总线名称的来源 `Auto` (默认值) | `Property`

输出航迹总线名称的来源，指定为：

- `Auto` — 模块自动创建输出航迹总线名称。
- `Property` — 使用 **指定输出总线名称** 参数指定输出航迹总线名称。

### **输出信息总线名称的来源** — 输出信息总线名称的来源 `Auto` (默认值) | `Property`

输出信息总线名称的来源，指定为以下选项之一：

- `Auto` — 模块自动创建输出信息总线名称。
- `Property` — 使用 **融合器信息总线名称** 参数指定输出信息总线名称。

## 所属库

Sensor Fusion and Tracking Toolbox / Multi-Object Tracking Algorithms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2023a：Simulink 总线不在工作区中显示

从 R2023a 开始，此模块创建的 Simulink 总线不再显示在 MATLAB 工作区中。

## 描述

航迹到航迹融合

Track-to-Track Fuser Simulink® 模块是一种多源、多目标、航迹级融合器，它使用全局最近邻 (GNN) 关联来维护关于其所融合航迹的单一假设。该模块的输入是来自已跟踪多个对象的源的航迹，例如多目标跟踪器模块或其他 track-to-track fuser 模块。输入航迹称为 *源航迹* 或 *本地航迹*，而融合器中维护的航迹称为 *中心航迹*。
