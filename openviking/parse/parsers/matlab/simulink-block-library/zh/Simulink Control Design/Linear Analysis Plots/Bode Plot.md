---
type: simulink-block
title: 'Bode Plot'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Linear Analysis Plots'
documentation_page: 'bodeplot'
documentation_source_path: 'ug/bodeplot.html'
language: zh-CN
chinese_source: worker-translation
---

# Bode Plot

## 端口
```yaml
ports:
- name: Trigger
  summary: 外部触发信号 标量
  direction: input
- name: z–1
  summary: 断言信号 1 | 0
  direction: output
```

### 输入

### **Trigger** — 外部触发信号 标量

使用此输入端口（由外部触发图标指示）连接外部触发信号，用于计算模型线性化。要指定要检测的触发信号类型，请使用 **Trigger type** 参数。

#### 依赖关系

要启用此端口，请将 **Linearize on** 参数设置为 `External trigger`。
### 输出

### **z–1** — 断言信号 `1` | `0`

将断言信号的值输出为逻辑值。如果违反了 **Bounds** 选项卡上指定的任何边界，则断言信号为 false（`0`）。否则，该信号为 true（`1`）。

默认情况下，输出信号的数据类型为 double。要将输出数据类型设置为 Boolean，请在 Simulink 模型中，在“配置参数”对话框中，选择 **Implement logic signals as Boolean data** 参数。此设置适用于模型中生成逻辑信号的所有模块。

您可以使用断言信号来设计复杂的断言逻辑。有关示例，请参阅 Verify Model Using Simulink Control Design and Simulink Verification Blocks。

#### 依赖关系

要启用此端口，请选择 **Output assertion signal** 参数。
## 参数
```yaml
parameters:
- name: Show Plot
  summary: 打开绘图按钮
  group: ''
- name: Show plot on block open
  summary: 打开模块时打开绘图 off（默认）| on
  group: ''
  block_parameter: LaunchViewOnOpen
  type: 字符向量
  values: '''off'' | ''on'''
- name: Response Optimization
  summary: 打开 Response Optimizer 按钮
  group: ''
- name: Linearization inputs/outputs
  summary: 指定要线性化的模型部分线性分析点
  group: 线性化
- name: Enable regular expression
  summary: 启用使用正则表达式进行信号搜索 on（默认）| off
  group: 线性化
- name: Show filtered results as a flat list
  summary: 使用平面列表显示过滤后的总线信号层级 off（默认）| on
  group: 线性化
- name: Linearize on
  summary: 何时计算线性模型 Simulation snapshots（默认）| External trigger
  group: 线性化
  block_parameter: LinearizeAt
  type: 字符向量
  values: '''SnapshotTimes'' | ''ExternalTrigger'''
  default: '''SnapshotTimes'''
- name: Snapshot times
  summary: 计算线性模型的仿真时间 0（默认）| 正实数值 | 正实数值向量
  group: 线性化
  block_parameter: SnapshotTimes
  type: 字符向量
  values: '''0'' | 正实数值 | 正实数值向量'
  default: '''0'''
- name: Trigger type
  summary: 要检测的外部触发类型 Rising edge（默认）| Falling edge
  group: 线性化
  block_parameter: TriggerType
  type: 字符向量
  values: '''rising'' | ''falling'''
  default: '''rising'''
- name: Enable zero-crossing detection
  summary: 启用过零检测 on（默认）| off
  group: 线性化
  block_parameter: ZeroCross
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Use exact delays
  summary: 在线性模型中使用精确延迟 off（默认）| on
  group: 线性化
  block_parameter: UseExactDelayModel
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Linear system sample time
  summary: 线性系统的采样时间 'auto'（默认）| 正有限值 | 0
  group: 线性化
  block_parameter: SampleTime
  type: character vector
  values: '''auto'' | positive finite value | ''0'''
  default: '''auto'''
- name: Sample time rate conversion method
  summary: 采样时间速率转换方法 Zero-Order Hold（默认）| Tustin (bilinear) | Tustin with Prewarping | ...
  group: 线性化
  block_parameter: RateConversionMethod
  type: character vector
  values: '''zoh'' | ''tustin'' | ''prewarp''| ''upsampling_zoh''| ''upsampling_tustin''| ''upsampling_prewarp'''
  default: '''zoh'''
- name: Prewarp frequency
  summary: Tustin 速率转换的预畸变频率 '10'（默认）| 正标量
  group: 线性化
  block_parameter: PreWarpFreq
  type: character vector
  values: positive scalar
  default: '''10'''
- name: Use full block names
  summary: 在状态、输入和输出名称中使用完整模块路径 off（默认）| on
  group: 线性化
  block_parameter: UseFullBlockNameLabels
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Use bus signal names
  summary: 在线性系统中使用总线信号名称 off（默认）| on
  group: 线性化
  block_parameter: UseBusSignalLabels
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Include upper magnitude bound in assertion
  summary: 检查 Bode 幅值是否违反上界 on | off
  group: Bounds
  block_parameter: EnableUpperBound
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'' for Bode Plot block, ''on'' for Check Bode Characteristics block'
- name: Frequencies
  summary: 上限幅值边界段的频率 向量 | 矩阵 | 元胞数组
  group: Bounds
  block_parameter: UpperBoundFrequencies
  type: character vector
  values: 正有限数向量 | 正有限数矩阵 | 包含正有限数的矩阵元胞数组
  default: '''[]'' for Bode Plot block, ''[10 100]'' for Check Bode Characteristics block'
- name: Magnitudes
  summary: 上限边界段的幅值 向量 | 矩阵 | 元胞数组
  group: Bounds
  block_parameter: UpperBoundFrequencies
  type: character vector
  values: 有限数向量 | 有限数矩阵 | 包含有限数的矩阵元胞数组
  default: '''[]'' for Bode Plot block, ''[-20 -20]'' for Check Bode Characteristics block'
- name: Include lower magnitude bound in assertion
  summary: 检查 Bode 幅值是否违反下限 on | off
  group: Bounds
  block_parameter: EnableLowerBound
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'' for Bode Plot block, ''on'' for Check Bode Characteristics block'
- name: Frequencies
  summary: 下限幅值段的频率 向量 | 矩阵 | 元胞数组
  group: Bounds
  block_parameter: LowerBoundFrequencies
  type: character vector
  values: 正有限数向量 | 正有限数矩阵 | 包含正有限数的矩阵元胞数组
  default: '''[]'' for Bode Plot block, ''[0.1 1]'' for Check Bode Characteristics block'
- name: Magnitudes
  summary: 下限段的幅值 向量 | 矩阵 | 元胞数组
  group: Bounds
  block_parameter: LowerBoundFrequencies
  type: character vector
  values: 有限数向量 | 有限数矩阵 | 包含有限数的矩阵元胞数组
  default: '''[]'' for Bode Plot block, ''[20 20]'' for Check Bode Characteristics block'
- name: Save data to workspace
  summary: 保存线性系统以供进一步分析 off（默认）| on
  group: Logging
  block_parameter: SaveToWorkspace
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Variable name
  summary: 用于保存线性系统的数据结构体名称 sys（默认）| 字符向量
  group: Logging
  block_parameter: SaveName
  type: character vector
  default: '''sys'''
- name: Save operating points for each linearization
  summary: 保存每次线性化的工作点 off（默认）| on
  group: Logging
  block_parameter: SaveOperatingPoints
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Enable assertion
  summary: 启用边界检查 on（默认）| off
  group: Assertion
  block_parameter: enabled
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
- name: Simulation callback when assertion fails
  summary: 当违反边界时要求值的表达式 ''（默认）| MATLAB expression
  group: Assertion
  block_parameter: callback
  type: character vector
  values: MATLAB expression
  default: ''''''
- name: Stop simulation when assertion fails
  summary: 当违反边界时停止仿真 off（默认）| on
  group: Assertion
  block_parameter: stopWhenAssertionFail
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Output assertion signal
  summary: 添加断言输出端口 off（默认）| on
  group: Assertion
  block_parameter: export
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Show Plot** — 打开绘图按钮

要查看仿真期间计算的 Bode 图，请在开始仿真之前单击此按钮。如果您在 **Bounds** 选项卡上指定了边界，它们也会显示在图上。

要在打开模块时显示绘图，请选择 **Show plot on block open** 参数。

有关使用该图的详细信息，请参阅 Using the Plot。

### **Show plot on block open** — 打开模块时打开绘图 `off`（默认）| `on`

选择此参数可在打开模块时打开绘图。然后，您可以在绘图窗口中执行诸如添加或修改边界等任务，而无需使用模块参数。要从绘图窗口访问模块参数，请选择 **Edit** 或单击“参数”图标。

有关使用该图的详细信息，请参阅 Using the Plot。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LaunchViewOnOpen` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Response Optimization** — 打开 Response Optimizer 按钮

打开 Response Optimizer 应用，以优化模型响应，使其满足 **Bounds** 选项卡上指定的设计要求。

仅当您安装了 Simulink
Design Optimization™ 软件时，此按钮才可用。

有关响应优化的详细信息，请参阅 Design Optimization to Meet Step Response Requirements (GUI) (Simulink Design Optimization) 和 Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI) (Simulink Design Optimization)。

### 线性化

要指定要线性化的模型部分和其他线性化设置，请使用 **Linearizations** 选项卡上的参数。此选项卡上的默认设置对于 Bode Plot 和 Check Bode
Characteristics 模块是相同的。

### **Linearization inputs/outputs** — 指定要线性化的模型部分线性分析点

要指定要线性化的模型部分，请从 Simulink 模型中选择信号，并将其添加为线性化输入或输出。

线性化输入和输出表

在表中，**Block:Port:Bus Element** 列显示每个信号的以下信息。

- 源模块
- 信号所连接的源模块的输出端口
- 总线元素名称（如果信号位于总线中）

在 **Configuration** 列中，从以下类型中选择线性分析点的类型。有关线性分析点的详细信息，请参阅 Specify Portion of Model to Linearize。

- `Open-loop Input` — 在环路断开后指定一个线性化输入点
- `Open-loop Output` — 在环路断开前指定一个线性化输出点
- `Loop Transfer` — 在环路断开前指定一个输出点，后跟一个输入
- `Input Perturbation` — 为信号指定一个加性输入
- `Output Measurement` — 在信号处进行测量
- `Loop Break` — 指定一个环路断开
- `Sensitivity` — 指定一个加性输入，后跟一个输出测量
- `Complementary Sensitivity` — 指定一个输出，后跟一个加性输入

**注意**

如果在未指定线性化输入或输出的情况下仿真模型，软件会在 MATLAB Command Window 中生成警告，并且不会计算线性系统。

#### 编辑线性化输入和输出

要添加线性化输入和输出：

1. 要展开信号选择区域，请点击 Plus。

   对话框将展开，显示 **Click a signal in the model to select it** 区域。
2. 在 Simulink 模型中，选择一个或多个信号。

   所选信号会出现在 **Model signal** 表中。

   已添加信号的信号表
3. （可选）对于总线信号，展开总线以选择各个元素。

   **提示**

   对于大型总线或其他大型信号列表，您可以过滤信号名称。在 **Filter by name** 框中，输入搜索文本。名称匹配区分大小写。

   要修改过滤选项，请点击 Down arrow。有关过滤选项的详细信息，请参阅 **Enable regular expression** 和 **Show filtered results as a flat list** 参数。
4. 要将所选信号添加到 **Linearization inputs/outputs** 表中，请点击 Left arrow。
5. 在 **Configuration** 列中，指定信号类型。

或者，如果您的模型中已定义线性化输入和输出，则可以通过点击 Import icon 将它们添加到 **Linearization inputs/outputs** 表中。

要从 **Linearization inputs/outputs** 表中删除信号，请选择该信号并点击 Delete icon。

要在 Simulink 模型中突出显示信号的源模块，请在 **Linearization inputs/outputs** 表中选择该信号，然后点击 Highlight icon。

### **Enable regular expression** — 启用使用正则表达式进行信号搜索 `on`（默认）| `off`

选择此选项可启用使用 MATLAB 正则表达式过滤信号名称。例如，在 **Filter by name** 文本框中输入 `t$` 会显示所有名称以小写 `t` 结尾的信号（及其直接父级）。有关详细信息，请参阅 Regular Expressions。

#### 依赖关系

要启用此参数，请点击 **Filter by name** 文本框旁边的 Down arrow。

### **Show filtered results as a flat list** — 使用平面列表显示过滤后的总线信号层级 `off`（默认）| `on`

选择此选项可以以平面列表格式显示过滤后的信号列表。平面列表格式使用点表示法来反映总线信号的层级结构。信号会根据 **Filter by name** 文本框中的文本进行过滤。

下图显示了过滤后的嵌套总线信号集的平面列表格式示例。

#### 依赖关系

要启用此参数，请点击 **Filter by name** 文本框旁边的向下箭头。

### **Linearize on** — 何时计算线性模型 `Simulation snapshots`（默认）| `External trigger`

使用此参数指定何时计算线性模型。

要在指定的仿真快照时间计算线性模型，请将此参数设置为
`Simulation snapshots`。使用
**Snapshot times** 参数指定快照时间。

在以下情况下使用仿真快照：

- 已知模型处于稳态工作点的一个或多个时间
- 想要在特定时间计算线性系统

要在基于触发的仿真事件时计算线性模型，请将此参数设置为
`External trigger`。选择此选项会向模块添加一个触发输入端口，您可以将外部触发信号连接到该端口。要指定要检测的触发类型，请使用 **Trigger type**
参数。

当仿真期间生成的信号表明模型处于感兴趣的稳态条件时，使用外部触发。例如，对于飞机模型，您可能希望在燃油质量达到最大燃油质量的给定比例时计算线性系统。

#### 编程用法

|  |
| --- |
| **模块参数：** `LinearizeAt` |
| **类型：** 字符向量 |
| **值：** `'SnapshotTimes'` | `'ExternalTrigger'` |
| **默认值：** `'SnapshotTimes'` |

### **Snapshot times** — 计算线性模型的仿真时间 `0`（默认）| 正实数值 | 正实数值向量

要在特定仿真时间（例如您已知模型达到稳态工作点的时间）计算线性系统，请指定一个或多个快照时间。要指定多个快照时间，请将此参数指定为正数值向量。

快照时间必须小于或等于 Simulink 模型中指定的仿真时间。

有关在仿真快照时间对模型进行线性化的示例，请参阅：

- Visualize Linear System at Multiple Simulation Snapshots
- 在默认仿真快照时间验证模型
- 在多个仿真快照时间验证模型

#### 依赖关系

要启用此参数，请将 **Linearize on** 参数设置为
`Simulation snapshots`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SnapshotTimes` |
| **类型：** 字符向量 |
| **值：** `'0'` | 正实数值 | 正实数值向量 |
| **默认值：** `'0'` |

### **Trigger type** — 要检测的外部触发类型 `Rising edge`（默认）| `Falling edge`

将要检测的外部触发信号中的触发指定为以下类型之一。

- `Rising edge` — 使用触发信号的上升沿；即信号从 `0` 变为
  `1` 时。
- `Falling edge` — 使用触发信号的下降沿；即信号从 `1` 变为
  `0` 时。

#### 依赖关系

要启用此参数，请将 **Linearize on** 参数设置为 `External trigger`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TriggerType` |
| **类型：** 字符向量 |
| **值：** `'rising'` | `'falling'` |
| **默认值：** `'rising'` |

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认）| `off`

选择此选项以启用过零检测。

当您将 **Linearize on** 参数设置为 `Simulation snapshots` 时，启用过零检测可确保软件在您在 **Snapshot times** 参数中指定的精确快照时间计算线性模型。

当您将 **Linearize on** 参数设置为 `External trigger` 时，启用过零检测可确保软件在检测到外部触发器的精确时间计算线性模型。要指定触发器类型，请使用 **Trigger type** 参数。

如果清除此选项，软件将在变步长 Simulink 求解器选择的仿真时间计算线性系统，这些时间可能不对应精确的快照时间或检测到触发信号的精确时间。

例如，考虑变步长求解器选择仿真时间
*T**n*–1 和
*Tn* 的情况。如下图所示，
指定的快照时间 *Tsnap* 可能
位于所选仿真时间之间。如果您启用过零检测，求解器
还会在时间 *Tsnap* 仿真模型
并在该点计算线性模型。

类似地，外部触发器可能在
*Ttrig* 时间被检测到，该时间位于所选
仿真时间之间。如果您启用过零检测，求解器还会在
时间 *Ttrig* 仿真模型并在该点计算线性
模型。

在两种情况下，如果您未启用过零检测，软件将在
*T**n*–1 或
*Tn* 计算线性模型。

有关过零检测的更多信息，请参阅 Zero-Crossing Detection。

#### 依赖关系

当您使用定步长 Simulink 求解器时，此参数将被忽略。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Use exact delays** — 在线性模型中使用精确延迟 `off`（默认）| `on`

选择此选项以计算具有精确延迟的线性模型。如果清除此选项，线性模型将使用任何延迟的 Padé 近似。

有关线性化具有延迟的模型的更多信息，请参阅 Linearize Models with Delays。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseExactDelayModel` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Linear system sample time** — 线性系统的采样时间 `'auto'`（默认）| 正有限值 | `0`

要计算具有指定采样时间的线性系统，软件使用您在 **Sample time rate
conversion method** 参数中指定的方法转换模型中的采样
时间。

您可以将采样时间设置为以下值之一。

- `auto` — 如果模型中的所有模块都是连续时间，则使用
  采样时间 `0`。否则，将采样时间设置为模型中非零采样时间的最小公倍数。
- 正有限值 — 创建具有指定采样
  时间的离散时间模型。
- `0` — 创建连续时间模型。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **Value:** `'auto'` | positive finite value | `'0'` |
| **默认值**：`'auto'` |

### **Sample time rate conversion method** — 采样时间速率转换方法 `Zero-Order Hold`（默认）| `Tustin (bilinear)` | `Tustin with Prewarping` | ...

在线性化过程中转换采样时间的方法，指定为以下值之一。

- `Zero-Order Hold` — 零阶保持，其中假设控制输入在采样时间 `Ts` 内分段恒定。此方法通常时域性能更好。
- `Tustin (bilinear)` — 不带频率预畸变的双线性（Tustin）近似。软件将分数时间延迟舍入到采样时间的最接近倍数。此方法通常频域性能更好。
- `Tustin with Prewarping` — 带频率预畸变的双线性（Tustin）近似。使用 **Prewarp frequency** 参数指定预畸变频率。此方法通常频域性能更好。使用此方法可确保在感兴趣的频率范围内匹配。
- `Upsampling when possible, Zero-Order Hold otherwise` — 在可能时对离散时间系统进行上采样；否则使用零阶保持。
- `Upsampling when possible, Tustin otherwise` — 在可能时对离散时间系统进行上采样；否则使用 Tustin 近似。
- `Upsampling when possible, Tustin with Prewarping otherwise` — 在可能时对离散时间系统进行上采样；否则使用带频率预畸变的 Tustin 近似。

仅当将离散时间系统转换为新的更快采样时间，且该采样时间是原系统采样时间的整数倍时，才能进行上采样。

有关多速率模型的速率转换和线性化的详细信息，请参阅：

- Multirate Linearization Algorithm
- Linearize Models Using Different Rate Conversion Methods
- Continuous-Discrete Conversion Methods

**注意**

如果使用 `Zero-Order Hold` 以外的速率转换方法，转换后的状态不再具有与原始状态相同的物理含义。因此，生成的 LTI 系统中的状态名称将变为 `'?'`。

#### 依赖关系

要启用此参数，请将 **Linear system sample time** 参数设置为 `auto` 以外的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`RateConversionMethod` |
| **类型**：character vector |
| **Value:** `'zoh'` | `'tustin'` | `'prewarp'`| `'upsampling_zoh'`| `'upsampling_tustin'`| `'upsampling_prewarp'` |
| **默认值**：`'zoh'` |

### **Prewarp frequency** — Tustin 速率转换的预畸变频率 `'10'`（默认）| 正标量

Tustin 速率转换的预畸变频率，以弧度/秒为单位，指定为小于重采样前后 Nyquist 频率的标量值。

#### 依赖关系

要启用此参数，请将 **Sample time rate conversion method** 参数设置为以下值之一。

- `Tustin with Prewarping`
- `Upsampling when possible, Tustin with Prewarping otherwise`

#### 编程使用

|  |
| --- |
| **模块参数**：`PreWarpFreq` |
| **类型**：character vector |
| **Value:** positive scalar |
| **默认值**：`'10'` |

### **Use full block names** — 在状态、输入和输出名称中使用完整模块路径 `off`（默认）| `on`

要使用完整模块路径显示所计算线性系统的状态、输入和输出名称，请选择此参数。例如，在 Plot Linear System Characteristics of a Chemical Reactor 示例所使用的 `scdcstr` 模型中，`CSTR` 子系统内 `Integrator1` 模块中的一个状态会以完整路径形式显示为 `scdcstr/CSTR/Integrator1`。

如果清除此参数，则仅使用状态、输入和输出的名称，当信号名称唯一且你知道它们在 Simulink 模型中的位置时，这很有用。在前面的示例中，积分器模块的状态名称显示为 `Integrator1`。

所计算的线性系统是一个状态空间对象（`ss`）。系统的状态、输入和输出名称会出现在以下状态空间对象属性中。

| 输入、输出或状态名称 | 状态空间对象属性 |
| --- | --- |
| 线性化输入名称 | `InputName` |
| 线性化输出名称 | `OutputName` |
| 状态名称 | `StateName` |

#### 编程使用

|  |
| --- |
| **模块参数**：`UseFullBlockNameLabels` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Use bus signal names** — 在线性系统中使用总线信号名称 `off`（默认）| `on`

当你选择整个总线作为线性化输入或输出时，选择此参数可在所计算的线性系统中使用各个总线元素的信号名称。如果未启用此选项，则改用总线通道编号。

**Note**

不建议选择整个总线信号。而应选择各个总线元素。

当线性化输入或输出来自以下模块之一时，会出现总线信号名称。

- 包含总线对象的根级输入端口模块
- Bus creator 模块
- 其源可追溯到 Bus creator 模块输出的子系统模块
- 其源可追溯到根级输入端口且仅穿过虚拟或非虚拟子系统边界的子系统模块

#### 依赖关系

当你的模型包含 mux/bus 混合时，不支持使用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseBusSignalLabels` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### Bounds

要为 Bode 图定义幅值边界，并指定是否检查是否违反这些边界，请使用 **Bounds** 选项卡上的参数。此选项卡上的默认设置对于 Bode Plot 和 Check Bode Characteristics 模块是不同的。

### **Include upper magnitude bound in assertion** — 检查 Bode 幅值是否违反上界 `on` | `off`

选择此参数可检查 Bode 图的幅值是否违反相应 **Magnitudes** 和 **Frequencies** 参数中指定的上界。

默认情况下，对于 Bode Plot 模块，此参数处于清除状态；对于 Check Bode Characteristics 模块，此参数处于选中状态。

#### 依赖关系

仅当你选择 **Enable assertion** 参数时，此参数才用于断言。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableUpperBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` for Bode Plot block, `'on'` for Check Bode Characteristics block |

### **Frequencies** — 上限幅值边界段的频率 向量 | 矩阵 | 元胞数组

要为 Bode 图定义上限，请以弧度/秒为单位指定每个边界段的起始和结束频率。要不指定上限，请将此参数设置为 `[]`。

默认情况下，Bode Plot 模块的频率为 `[]`，Check Bode Characteristics 模块的频率为 `[10 100]`。

要指定：

- 具有一条边的单个边界，请指定一个由正有限值组成的二元素向量。
- 具有多条边的单个边界，请指定一个 *N*×2 数组，其中 *N* 是边的数量。例如，对于频率 `[0.1 1]` 和 `[1 10]` 处的两条边，输入 `[0.1 1;1 10]`。
- 多个边界，请指定一个由矩阵组成的 *M* 元素元胞数组，其中 *M* 是边界的数量。

使用对应的 **Magnitudes** 参数设置边界的幅值。**Frequencies** 和 **Magnitudes** 参数的维度必须匹配。

您也可以在绘图窗口中添加边界段。有关详细信息，请参阅 Using the Plot。

#### 依赖关系

要在仿真期间检查是否违反幅值边界，请同时选择 **Include upper magnitude bound in assertion** 和 **Enable assertion** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperBoundFrequencies` |
| **类型**：character vector |
| **值：** 正有限数向量 | 正有限数矩阵 | 包含正有限数的矩阵元胞数组 |
| **默认值**：`'[]'` for Bode Plot block, `'[10 100]'` for Check Bode Characteristics block |

### **Magnitudes** — 上限边界段的幅值 向量 | 矩阵 | 元胞数组

要为 Bode 图定义上限，请以分贝为单位指定每个对应频率点处的幅值。要不指定上限，请将此参数设置为 `[]`。

默认情况下，Bode Plot 模块的幅值为 `[]`，Check Bode Characteristics 模块的幅值为 `[-20 -20]`。

要指定：

- 具有一条边的单个边界，请指定一个由有限幅值组成的二元素向量。
- 具有多条边的单个边界，请指定一个 *N*×2 数组，其中 *N* 是边的数量。例如，对于幅值为 `[-10 -10]` 和 `[-20 -20]` 的两条边，输入 `[-10 -10;-20 -20]`。
- 多个边界，请指定一个由矩阵组成的 *M* 元素元胞数组，其中 *M* 是边界的数量。

使用对应的 **Frequencies** 参数设置边界的频率值。**Magnitude** 和 **Frequencies** 参数的维度必须匹配。

您也可以在绘图窗口中添加边界段。有关详细信息，请参阅 Using the Plot。

#### 依赖关系

要在仿真期间检查是否违反幅值边界，请同时选择 **Include upper magnitude bound in assertion** 和 **Enable assertion** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperBoundFrequencies` |
| **类型**：character vector |
| **值：** 有限数向量 | 有限数矩阵 | 包含有限数的矩阵元胞数组 |
| **默认值**：`'[]'` for Bode Plot block, `'[-20 -20]'` for Check Bode Characteristics block |

### **Include lower magnitude bound in assertion** — 检查 Bode 幅值是否违反下限 `on` | `off`

选择此参数可检查 Bode 图的幅值是否违反对应的 **Magnitudes** 和 **Frequencies** 参数中指定的下限。

默认情况下，此参数在 Bode Plot 模块中处于清除状态，在 Check Bode Characteristics 模块中处于选中状态。

#### 依赖关系

仅当您选择 **Enable assertion** 参数时，此参数才用于断言。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableLowerBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` for Bode Plot block, `'on'` for Check Bode Characteristics block |

### **Frequencies** — 下限幅值段的频率 向量 | 矩阵 | 元胞数组

要为 Bode 图定义下限，请以弧度/秒为单位指定每个边界段的起始和结束频率。要指定无下限，请将此参数设置为 `[]`。

默认情况下，Bode Plot 模块的频率为 `[]`，Check Bode Characteristics 模块的频率为 `[0.1 1]`。

要指定：

- 具有一条边的单个边界，请指定由正有限值组成的二元素向量。
- 具有多条边的单个边界，请指定 *N*×2 数组，其中 *N* 是边的数量。例如，对于频率 `[0.1 1]` 和 `[1 10]` 处的两条边，输入 `[0.1 1;1 10]`。
- 多个边界，请指定由矩阵组成的 *M* 元素元胞数组，其中 *M* 是边界数量。

使用对应的 **Magnitudes** 参数设置边界的幅值。**Frequencies** 和 **Magnitudes** 参数的维度必须匹配。

您也可以在绘图窗口中添加边界段。有关详细信息，请参阅 Using the Plot。

#### 依赖关系

要在仿真期间检查是否违反幅值边界，请同时选择 **Include lower magnitude bound in assertion** 和 **Enable assertion** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerBoundFrequencies` |
| **类型**：character vector |
| **值：** 正有限数向量 | 正有限数矩阵 | 包含正有限数的矩阵元胞数组 |
| **默认值**：`'[]'` for Bode Plot block, `'[0.1 1]'` for Check Bode Characteristics block |

### **Magnitudes** — 下限段的幅值 向量 | 矩阵 | 元胞数组

要为 Bode 图定义下限，请以分贝为单位指定每个对应频率点处的幅值。要指定无下限，请将此参数设置为 `[]`。

默认情况下，Bode Plot 模块的幅值为 `[]`，Check Bode Characteristics 模块的幅值为 `[20 20]`。

要指定：

- 具有一条边的单个边界，请指定由有限幅值组成的二元素向量。
- 具有多条边的单个边界，请指定 *N*×2 数组，其中 *N* 是边的数量。例如，对于幅值为 `[20 20]` 和 `[40 40]` 的两条边，输入 `[20 20; 40 40]`。
- 多个边界，请指定由矩阵组成的 *M* 元素元胞数组，其中 *M* 是边界数量。

使用对应的 **Frequencies** 参数设置边界的频率值。**Magnitude** 和 **Frequencies** 参数的维度必须匹配。

您也可以在绘图窗口中添加边界段。有关详细信息，请参阅 Using the Plot。

#### 依赖关系

要在仿真期间检查是否违反幅值边界，请同时选择 **Include lower magnitude bound in assertion** 和 **Enable assertion** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerBoundFrequencies` |
| **类型**：character vector |
| **值：** 有限数向量 | 有限数矩阵 | 包含有限数的矩阵元胞数组 |
| **默认值**：`'[]'` for Bode Plot block, `'[20 20]'` for Check Bode Characteristics block |

### Logging

要控制是否保存仿真期间计算的线性化结果，请使用 **Logging** 选项卡上的参数。此选项卡上的默认设置对于 Bode Plot 和 Check Bode Characteristics 模块相同。

### **Save data to workspace** — 保存线性系统以供进一步分析 `off`（默认）| `on`

选择此参数以保存计算得到的线性系统，用于进一步分析或控制设计。数据保存在一个具有以下字段的结构体中。

- `time` — 计算线性系统时的仿真时间。
- `values` — 表示线性系统的状态空间模型。如果在多个仿真时间计算线性系统，则 `values` 是状态空间模型的数组。
- `operatingPoints` — 与 `values` 中每个线性系统对应的工作点。要启用此字段，请选择 **Save operating points for each linearization** 参数。

要指定保存的数据结构体的名称，请使用 **Variable name** 属性。

保存的数据结构体的位置取决于 Simulink 模型的配置。

- 如果模型未配置为将仿真输出保存为单个对象，则数据结构体是 MATLAB 工作区中的一个变量。
- 如果模型配置为将仿真输出保存为单个对象，则数据结构体是 `Simulink.SimulationOutput` 对象中包含记录的仿真数据的一个字段。

要将模型配置为将仿真输出保存为单个对象，请在配置参数对话框中选择 **Single simulation output** 参数。

有关 Simulink 中数据记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

#### 编程使用

|  |
| --- |
| **模块参数**：`SaveToWorkspace` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Variable name** — 用于保存线性系统的数据结构体名称 `sys`（默认）| 字符向量

指定用于存储仿真期间计算得到的线性系统的数据结构体的名称。

该名称必须在所有数据记录模型模块（如 Linear Analysis Plot 模块、Model Verification 模块、Scope 模块、To Workspace 模块）以及仿真返回变量（如 time、states 和 outputs）所使用的变量名称中唯一。

有关 Simulink 中数据记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

#### 依赖关系

要启用此参数，请选择 **Save data to workspace** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`SaveName` |
| **类型**：character vector |
| **默认值**：`'sys'` |

### **Save operating points for each linearization** — 保存每次线性化的工作点 `off`（默认）| `on`

选择此参数以保存计算每次线性化时的工作点。选择此参数会将 `operatingPoints` 字段添加到保存的数据结构体中。

#### 依赖关系

要启用此参数，请选择 **Save data to workspace** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`SaveOperatingPoints` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### Assertion

要控制当 **Bounds** 选项卡上定义的边界被违反时模块的断言行为，请使用 **Assertion** 选项卡上的参数。此选项卡上的默认设置对于 Bode Plot 和 Check Bode Characteristics 模块是相同的。

### **Enable assertion** — 启用边界检查 `on`（默认）| `off`

要在仿真期间检查是否满足 **Bounds** 选项卡上定义的边界，请选择此参数。当不满足边界时，断言失败并生成警告。

清除此参数会禁用断言；也就是说，该模块不再检查是否满足指定的边界。模块图标也会更新，以指示断言已禁用。

带有 X 的模块，表示断言已禁用。

默认情况下，在 **Bounds** 选项卡上：

- Bode Plot 模块没有定义边界。
- Check Bode Characteristics 模块有定义边界。

您可以配置 Simulink 模型以启用或禁用所有模型验证模块，并覆盖 **Enable assertion** 参数。为此，在 Simulink 模型中，在 Configuration Parameters 对话框中，指定 **Model Verification block enabling** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`enabled` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

### **Simulation callback when assertion fails** — 当违反边界时要求值的表达式 `''`（默认）| MATLAB expression

指定当违反 **Bounds** 选项卡上指定的边界时要计算的 MATLAB 表达式。表达式中使用的所有变量都必须位于 MATLAB 工作区中。

#### 依赖关系

要启用此参数，请选择 **Enable assertion** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`callback` |
| **类型**：character vector |
| **Value:** MATLAB expression |
| **默认值**：`''` |

### **Stop simulation when assertion fails** — 当违反边界时停止仿真 `off`（默认）| `on`

要在违反 **Bounds** 选项卡上指定的边界时停止仿真，请选择此参数。如果未选择此选项，则边界违例将作为警告报告在 MATLAB Command Window 中，并且仿真继续。

如果从 Simulink 模型运行仿真，当断言失败时，发生边界违例的模块会高亮显示，并且错误消息会显示在 Simulation Diagnostics 窗口中。

**Note**

由于选择此选项会在断言失败时立即停止仿真，因此不会报告仿真后期可能发生的边界违例。如果您希望报告所有边界违例，请不要选择此选项。

#### 依赖关系

要启用此参数，请选择 **Enable assertion** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`stopWhenAssertionFail` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Output assertion signal** — 添加断言输出端口 `off`（默认）| `on`

将 **z–1** 断言信号输出端口添加到该模块。此端口将断言的值输出为 Boolean 信号。当违反 **Bounds** 选项卡上定义的边界时，断言失败，并且断言信号为 `0`。否则，断言信号为 `1`。

您可以使用断言信号来设计复杂的断言逻辑。有关示例，请参见 Verify Model Using Simulink Control Design and Simulink Verification Blocks。

#### 编程使用

|  |
| --- |
| **模块参数**：`export` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink Control Design / Linear Analysis Plots Simulink Control Design / Model Verification

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

## 描述

从非线性 Simulink 模型计算得到的线性系统的 Bode 图

Bode Plot 和 Check Bode Characteristics 模块从非线性 Simulink® 模型计算线性系统，并在仿真期间在 Bode 图上绘制该线性系统。除 **Bounds** 选项卡上的默认设置外，这些模块完全相同。

- Bode Plot 不定义默认边界。
- Check Bode Characteristics 模块定义默认边界并为断言启用这些边界。

有关线性系统频域分析的详细信息，请参阅 Frequency-Domain Responses。

在仿真期间，软件对模型中指定的线性化输入和输出之间的部分进行线性化，然后绘制该线性系统的幅值和相位。您还可以将线性系统保存为 MATLAB® 工作区中的变量。

Simulink 模型可以是连续时间、离散时间或多速率模型，并且可以具有时间延迟。线性系统可以是单输入单输出 (SISO) 或多输入多输出 (MIMO)。对于 MIMO 系统，该模块显示所有输入/输出组合的图。

您可以指定分段线性的频率相关幅值上下边界，并在 Bode 图上查看它们。您还可以在仿真期间检查是否满足这些边界。

- 如果满足所有边界，该模块不执行任何操作。
- 如果未满足某个边界，该模块将进行断言，并且 MATLAB 命令窗口中会出现警告消息。您还可以指定该模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并使该模块获得焦点。

在仿真期间，该模块还可以输出逻辑断言信号。

- 如果满足所有边界，该信号为 true (`1`)。
- 如果未满足任何边界，该信号为 false (`0`)。

要计算并绘制模型各个部分的幅值和相位，您可以添加多个 Bode Plot 和 Check Bode Characteristics 模块。

这些模块不支持代码生成，并且只能在 `Normal` 仿真模式下使用。
