---
type: simulink-block
title: 'Linear Step Response Plot'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Linear Analysis Plots'
documentation_page: 'linearstepresponseplot'
documentation_source_path: 'ug/linearstepresponseplot.html'
language: zh-CN
chinese_source: worker-translation
---

# Linear Step Response Plot

## 端口

### 输入

### **Trigger** — 外部触发信号 标量

使用此输入端口（由外部触发图标指示）连接外部触发信号，用于计算模型线性化。要指定要检测的触发信号类型，请使用 **Trigger type** 参数。

#### 依赖关系

要启用此端口，请将 **Linearize on** 参数设置为 `External trigger`。
### 输出

### **z–1** — 断言信号 `1` | `0`

将断言信号的值作为逻辑值输出。如果违反了 **Bounds** 选项卡上指定的任何边界，则断言信号为 false（`0`）。否则，该信号为 true（`1`）。

默认情况下，输出信号的数据类型为 double。要将输出数据类型设置为 Boolean，请在 Simulink 模型中，在“配置参数”对话框中，选择 **Implement logic signals as Boolean data** 参数。此设置适用于模型中生成逻辑信号的所有模块。

您可以使用断言信号来设计复杂的断言逻辑。有关示例，请参阅 Verify Model Using Simulink Control Design and Simulink Verification Blocks。

#### 依赖关系

要启用此端口，请选择 **Output assertion signal** 参数。

## 参数

### **Show Plot** — 打开绘图按钮

要查看仿真期间计算的增益裕度和相位裕度，请在开始仿真之前点击此按钮。如果您在 **Bounds** 选项卡上指定了边界，这些边界也会显示在绘图上。

要在打开模块时显示绘图，请选择 **Show plot on block open** 参数。

有关使用绘图的详细信息，请参阅 Using the Plot。

### **Show plot on block open** — 打开模块时打开绘图 `off`（默认）| `on`

选择此参数可在打开模块时打开绘图。然后，您可以在绘图窗口中执行诸如添加或修改边界等任务，而无需使用模块参数。要从绘图窗口访问模块参数，请选择 **Edit** 或点击 Parameter 图标。

有关使用绘图的详细信息，请参阅 Using the Plot。

#### 编程使用

|  |
| --- |
| **模块参数**：`LaunchViewOnOpen` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### **Response Optimization** — 打开 Response Optimizer 按钮

打开 Response Optimizer 应用，以优化模型响应，使其满足 **Bounds** 选项卡上指定的设计要求。

仅当您安装了 Simulink
Design Optimization™ 软件时，此按钮才可用。

有关响应优化的详细信息，请参阅 Design Optimization to Meet Step Response Requirements (GUI) (Simulink Design Optimization) 和 Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI) (Simulink Design Optimization)。

### Linearizations

要指定要线性化的模型部分和其他线性化设置，请使用 **Linearizations** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块是相同的。

### **Linearization inputs/outputs** — 指定要线性化的模型部分线性分析点

要指定要线性化的模型部分，请从 Simulink 模型中选择信号，并将它们添加为线性化输入或输出。

线性化输入和输出表

在表中，**Block:Port:Bus Element** 列显示每个信号的以下信息。

- 源模块
- 信号所连接的源模块的输出端口
- 总线元素名称（如果信号位于总线中）

在 **Configuration** 列中，从以下类型中选择线性分析点的类型。有关线性分析点的详细信息，请参阅 Specify Portion of Model to Linearize。

- `Open-loop Input` — 在环路断开点之后指定一个线性化输入点
- `Open-loop Output` — 在环路断开点之前指定一个线性化输出点
- `Loop Transfer` — 在环路断开点之前指定一个输出点，后跟一个输入
- `Input Perturbation` — 为信号指定一个加性输入
- `Output Measurement` — 在信号处进行测量
- `Loop Break` — 指定一个环路断开点
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
3. （可选）对于总线信号，展开总线以选择单个元素。

   **提示**

   对于大型总线或其他大型信号列表，您可以过滤信号名称。在 **Filter by name** 框中，输入搜索文本。名称匹配区分大小写。

   要修改过滤选项，请点击 Down arrow。有关过滤选项的详细信息，请参阅 **Enable regular expression** 和 **Show filtered results as a flat list** 参数。
4. 要将所选信号添加到 **Linearization inputs/outputs** 表中，请点击 Left arrow。
5. 在 **Configuration** 列中，指定信号类型。

或者，如果您的模型中已定义线性化输入和输出，您可以通过点击 Import icon 将它们添加到 **Linearization inputs/outputs** 表中。

要从 **Linearization inputs/outputs** 表中删除信号，请选择该信号并点击 Delete icon。

要在 Simulink 模型中高亮显示信号的源模块，请在 **Linearization inputs/outputs** 表中选择该信号，然后点击 Highlight icon。

### **Enable regular expression** — 启用使用正则表达式搜索信号 `on`（默认）| `off`

选择此选项可启用使用 MATLAB 正则表达式过滤信号名称。例如，在 **Filter by name** 文本框中输入 `t$` 会显示所有名称以小写 `t` 结尾的信号（及其直接父级）。有关详细信息，请参阅 Regular Expressions。

#### 依赖关系

要启用此参数，请点击 **Filter by name** 文本框旁边的 Down arrow。

### **Show filtered results as a flat list** — 使用平面列表显示过滤后的总线信号层级 `off`（默认）| `on`

选择此选项可以平面列表格式显示过滤后的信号列表。平面列表格式使用点表示法来反映总线信号的层级结构。信号会根据 **Filter by name** 文本框中的文本进行过滤。

下图显示了过滤后的一组嵌套总线信号的平面列表格式示例。

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

#### 编程使用

|  |
| --- |
| **模块参数**：`LinearizeAt` |
| **类型**：character vector |
| **Value:** `'SnapshotTimes'` | `'ExternalTrigger'` |
| **默认值**：`'SnapshotTimes'` |

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

#### 编程使用

|  |
| --- |
| **模块参数**：`SnapshotTimes` |
| **类型**：character vector |
| **值：** `'0'` | 正实数值 | 正实数值向量 |
| **默认值**：`'0'` |

### **Trigger type** — 要检测的外部触发类型 `Rising edge`（默认）| `Falling edge`

将要检测的外部触发信号中的触发指定为以下类型之一。

- `Rising edge` — 使用触发信号的上升沿；即信号从 `0` 变为
  `1` 时。
- `Falling edge` — 使用触发信号的下降沿；即信号从 `1` 变为
  `0` 时。

#### 依赖关系

要启用此参数，请将 **Linearize on** 参数设置为 `External trigger`。

#### 编程使用

|  |
| --- |
| **模块参数**：`TriggerType` |
| **类型**：character vector |
| **Value:** `'rising'` | `'falling'` |
| **默认值**：`'rising'` |

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

有关线性化带延迟模型的更多信息，请参阅 Linearize Models with Delays。

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

### **Sample time rate conversion method** — 速率转换方法 `Zero-Order Hold`（默认）| `Tustin (bilinear)` | `Tustin with Prewarping` | ...

在线性化过程中转换采样时间的方法，指定为以下值之一。

- `Zero-Order Hold` — 零阶保持，其中假设控制输入在采样时间 `Ts` 内分段恒定。此方法通常时域性能更好。
- `Tustin (bilinear)` — 不带频率预畸变的双线性（Tustin）近似。软件将分数时间延迟舍入到采样时间的最接近倍数。此方法通常频域性能更好。
- `Tustin with Prewarping` — 带频率预畸变的双线性（Tustin）近似。使用 **Prewarp frequency** 参数指定预畸变频率。此方法通常频域性能更好。使用此方法可确保在感兴趣的频率范围内匹配。
- `Upsampling when possible, Zero-Order Hold otherwise` — 在可能时对离散时间系统进行上采样；否则使用零阶保持。
- `Upsampling when possible, Tustin otherwise` — 在可能时对离散时间系统进行上采样；否则使用 Tustin 近似。
- `Upsampling when possible, Tustin with Prewarping otherwise` — 在可能时对离散时间系统进行上采样；否则使用带频率预畸变的 Tustin 近似。

仅当将离散时间系统转换为新的更快采样时间，且该采样时间是原始系统采样时间的整数倍时，才能进行上采样。

有关多速率模型的速率转换和线性化的更多信息，请参阅：

- Multirate Linearization Algorithm
- Linearize Models Using Different Rate Conversion Methods
- Continuous-Discrete Conversion Methods

**注意**

如果使用 `Zero-Order Hold` 以外的速率转换方法，转换后的状态不再具有与原始状态相同的物理含义。因此，生成的 LTI 系统中的状态名称将变为 `'?'`。

#### 依赖关系

要启用此参数，请将 **Linear system sample time** 参数设置为 `auto` 以外的值。

#### 编程用法

|  |
| --- |
| **模块参数：** `RateConversionMethod` |
| **类型：** 字符向量 |
| **值：** `'zoh'` | `'tustin'` | `'prewarp'`| `'upsampling_zoh'`| `'upsampling_tustin'`| `'upsampling_prewarp'` |
| **默认：** `'zoh'` |

### **Prewarp frequency** — Tustin 速率转换的预畸变频率 `'10'`（默认）| 正标量

Tustin 速率转换的预畸变频率，以弧度/秒为单位，指定为小于重采样前后奈奎斯特频率的标量值。

#### 依赖关系

要启用此参数，请将 **Sample time rate conversion method** 参数设置为以下值之一。

- `Tustin with Prewarping`
- `Upsampling when possible, Tustin with Prewarping otherwise`

#### 编程用法

|  |
| --- |
| **模块参数：** `PreWarpFreq` |
| **类型：** 字符向量 |
| **值：** 正标量 |
| **默认：** `'10'` |

### **Use full block names** — 在状态、输入和输出名称中使用完整模块路径 `off`（默认）| `on`

要使用完整模块路径显示所计算线性系统的状态、输入和输出名称，请选择此参数。例如，在 Plot Linear System Characteristics of a Chemical Reactor 示例中使用的 `scdcstr` 模型里，`CSTR` 子系统内 `Integrator1` 模块中的一个状态会以完整路径显示为 `scdcstr/CSTR/Integrator1`。

如果清除此参数，则仅使用状态、输入和输出的名称，当信号名称唯一且您知道它们在 Simulink 模型中的位置时，这很有用。在前面的示例中，积分器模块的状态名称显示为 `Integrator1`。

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

当您选择整个总线作为线性化输入或输出时，请选择此参数以在所计算的线性系统中使用各个总线元素的信号名称。如果未启用此选项，则改用总线通道编号。

**Note**

不建议选择整个总线信号。而应选择各个总线元素。

当线性化输入或输出来自以下模块之一时，会出现总线信号名称。

- 包含总线对象的根级输入端口模块
- Bus creator 模块
- 其源可追溯到 Bus creator 模块输出的子系统模块
- 其源可追溯到根级输入端口且仅穿过虚拟或非虚拟子系统边界的子系统模块

#### 依赖关系

当您的模型包含 mux/bus 混合时，不支持使用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseBusSignalLabels` |
| **类型**：character vector |
| **Value:** `'off'` | `'on'` |
| **默认值**：`'off'` |

### Bounds

要定义阶跃响应特性的边界，并指定是否检查这些边界是否被违反，请使用 **Bounds** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块是不同的。

### **Include step response bound in assertion** — 检查阶跃响应是否违反特性边界 `on` | `off`

选择此参数以检查阶跃响应特性是否违反 **Bounds** 选项卡上指定的边界。

默认情况下，对于 Linear Step Response Plot 模块，此参数被清除；对于 Check Linear Step Response Characteristics 模块，此参数被选中。

#### 依赖关系

仅当您选择 **Enable assertion** 参数时，此参数才用于断言。

#### 编程使用

|  |
| --- |
| **模块参数**：`EnableStepResponseBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` for Linear Step Response Plot block, `'on'` for Check Linear Step Response Characteristics block |

### **Final value** — 响应阶跃输入的输出信号最终值 有限实数标量

为了计算 **Bounds** 选项卡上的其他阶跃响应特性，模块使用输出信号响应阶跃输入的预期最终值。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FinalValue` |
| **类型：** 字符向量 |
| **值：** 有限实数标量 |
| **默认值：** 线性阶跃响应绘图模块为 `'[]'`，检查线性阶跃响应特性模块为 `'1'` |

### **上升时间** — 上升时间上界 有限正标量

阶跃响应达到最终值某一百分比所需时间的上界，以秒为单位。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定最终值的百分比，请使用 **% 上升** 参数。

默认情况下，此参数对于线性阶跃响应绘图模块为 `[]`，对于检查线性阶跃响应特性模块为 `5`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RiseTime` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认值：** 线性阶跃响应绘图模块为 `'[]'`，检查线性阶跃响应特性模块为 `'5'` |

### **% 上升** — 用于计算上升时间的最终值百分比 小于 (100 - % 稳定) 的正标量

用于定义上升时间上界的最终值百分比。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定上升时间上界，请使用 **上升时间** 参数。

默认情况下，此参数对于线性阶跃响应绘图模块为 `[]`，对于检查线性阶跃响应特性模块为 `80`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PercentRise` |
| **类型：** 字符向量 |
| **值：** 小于 (100 - % 稳定) 的正标量 |
| **默认值：** 线性阶跃响应绘图模块为 `'[]'`，检查线性阶跃响应特性模块为 `'80'` |

### **稳定时间** — 稳定时间上界 大于上升时间的有限标量

阶跃响应在最终值附近指定范围内稳定所需时间的上界，以秒为单位。此稳定范围定义为最终值加上或减去最终值的指定稳定百分比。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定稳定百分比，请使用 **% 稳定** 参数。

默认情况下，此参数对于线性阶跃响应绘图模块为 `[]`，对于检查线性阶跃响应特性模块为 `7`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** 字符向量 |
| **值：** 大于上升时间的有限标量 |
| **默认值：** 线性阶跃响应绘图模块为 `'[]'`，检查线性阶跃响应特性模块为 `'7'` |

### **% 稳定** — 用于计算稳定范围的最终值百分比 小于 (100 - % 上升) 的正标量

用于定义稳定范围边界的最终值百分比。稳定范围定义为最终值加上或减去最终值的指定稳定百分比。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定稳定时间上界，请使用 **稳定时间** 参数。

默认情况下，此参数对于线性阶跃响应绘图模块为 `[]`，对于检查线性阶跃响应特性模块为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PercentSettling` |
| **类型：** 字符向量 |
| **值：** 小于 (100 - % 稳定) 的正标量 |
| **默认值：** 线性阶跃响应绘图模块为 `'[]'`，检查线性阶跃响应特性模块为 `'1'` |

### **% 超调** — 超调上界 介于 0 和 100 之间的标量

阶跃响应可以超过最终值的量，定义为最终值的百分比。要指定最终值，请使用 **最终值** 参数。

默认情况下，此参数对于线性阶跃响应绘图模块为 `[]`，对于检查线性阶跃响应特性模块为 `10`。

#### 编程用法

|  |
| --- |
| **模块参数：** `PercentOvershoot` |
| **类型：** 字符向量 |
| **值：** 0 到 100 之间的标量 |
| **默认值：** Linear Step Response Plot 模块为 `'[]'`，Check Linear Step Response Characteristics 模块为 `'10'` |

### **% Undershoot** — 下冲的上界，0 到 100 之间的标量

阶跃响应可以低于初始值的量，定义为最终值的百分比。要指定最终值，请使用 **Final value** 参数。

默认情况下，Linear Step Response Plot 模块的此参数为 `[]`，Check Linear Step Response Characteristics 模块的此参数为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `PercentUndershoot` |
| **类型：** 字符向量 |
| **值：** 0 到 100 之间的标量 |
| **默认值：** Linear Step Response Plot 模块为 `'[]'`，Check Linear Step Response Characteristics 模块为 `'1'` |

### 记录

要控制是否保存在仿真期间计算的线性化结果，请使用 **Logging** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块是相同的。

### **Save data to workspace** — 保存线性系统以供进一步分析 `off`（默认）| `on`

选择此参数可保存计算得到的线性系统，以供进一步分析或控制设计使用。数据保存在具有以下字段的结构体中。

- `time` — 计算线性系统时的仿真时间。
- `values` — 表示线性系统的状态空间模型。如果在多个仿真时间计算线性系统，则 `values` 是状态空间模型的数组。
- `operatingPoints` — 与 `values` 中每个线性系统对应的工作点。要启用此字段，请选择 **Save operating points for each linearization** 参数。

要指定所保存数据结构的名称，请使用 **Variable name** 属性。

所保存数据结构的位置取决于 Simulink 模型的配置。

- 如果模型未配置为将仿真输出保存为单个对象，则该数据结构是 MATLAB 工作区中的一个变量。
- 如果模型配置为将仿真输出保存为单个对象，则该数据结构是 `Simulink.SimulationOutput` 对象中包含所记录仿真数据的一个字段。

要将模型配置为将仿真输出保存为单个对象，请在配置参数对话框中选择 **Single simulation output** 参数。

有关 Simulink 中数据记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

#### 编程用法

|  |
| --- |
| **模块参数：** `SaveToWorkspace` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Variable name** — 用于保存线性系统的数据结构名称 `sys`（默认）| 字符向量

指定用于存储仿真期间计算得到的线性系统的数据结构名称。

该名称必须在所有数据记录模型模块所使用的变量名称中唯一，例如 Linear Analysis Plot 模块、Model Verification 模块、Scope 模块、To Workspace 模块，以及诸如 time、states 和 outputs 等仿真返回变量。

有关 Simulink 中数据记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

#### 依赖关系

要启用此参数，请选择 **Save data to workspace** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `SaveName` |
| **类型：** 字符向量 |
| **默认值：** `'sys'` |

### **Save operating points for each linearization** — 保存每次线性化的工作点 `off`（默认）| `on`

选择此参数可保存计算每次线性化时的工作点。选择此参数会将 `operatingPoints` 字段添加到所保存的数据结构中。

#### 依赖关系

要启用此参数，请选择 **Save data to workspace** 参数。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `SaveOperatingPoints` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 断言

要控制当违反 **Bounds** 选项卡上定义的边界时模块的断言行为，请使用 **Assertion** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块是相同的。

### **Enable assertion** — 启用边界检查 `on`（默认）| `off`

要在仿真期间检查是否满足 **Bounds** 选项卡上定义的边界，请选择此参数。当不满足某个边界时，断言失败并生成警告。

清除此参数将禁用断言；也就是说，模块不再检查是否满足指定的边界。模块图标也会更新以指示断言已禁用。

带有 X 的模块表示断言已禁用。

默认情况下，在 **Bounds** 选项卡上：

- Linear Step Response Plot 模块没有定义边界。
- Check Linear Step Response Characteristics 模块有定义边界。

您可以配置 Simulink 模型以启用或禁用所有模型验证模块，并覆盖 **Enable assertion** 参数。为此，在 Simulink 模型中，在“配置参数”对话框中，指定 **Model Verification block enabling** 参数。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `enabled` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Simulation callback when assertion fails** — 当违反边界时要求值的表达式 `''`（默认）| MATLAB 表达式

指定当违反 **Bounds** 选项卡上指定的边界时要求值的 MATLAB 表达式。表达式中使用的所有变量都必须位于 MATLAB 工作区中。

#### 依赖关系

要启用此参数，请选择 **Enable assertion** 参数。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `callback` |
| **类型：** 字符向量 |
| **值：** MATLAB 表达式 |
| **默认值：** `''` |

### **Stop simulation when assertion fails** — 当违反边界时停止仿真 `off`（默认）| `on`

要在违反 **Bounds** 选项卡上指定的边界时停止仿真，请选择此参数。如果未选择此选项，则边界违反将作为警告报告在 MATLAB 命令窗口中，并且仿真继续。

如果从 Simulink 模型运行仿真，当断言失败时，发生边界违反的模块将高亮显示，并且错误消息将显示在“仿真诊断”窗口中。

**注意**

由于选择此选项会在断言失败时立即停止仿真，因此不会报告仿真期间稍后可能发生的边界违反。如果您希望报告所有边界违反，请不要选择此选项。

#### 依赖关系

要启用此参数，请选择 **Enable assertion** 参数。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `stopWhenAssertionFail` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Output assertion signal** — 添加断言输出端口 `off`（默认）| `on`

将 **z–1** 断言信号输出端口添加到模块。此端口将断言的值输出为布尔信号。当违反 **Bounds** 选项卡上定义的边界时，断言失败，断言信号为 `0`。否则，断言信号为 `1`。

您可以使用断言信号来设计复杂的断言逻辑。有关示例，请参阅 Verify Model Using Simulink Control Design and Simulink Verification Blocks。

#### 编程用法

|  |
| --- |
| **模块参数：** `export` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

## 所属库

Simulink Control Design / Linear Analysis Plots Simulink Control Design / Model Verification

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

## 描述

从非线性 Simulink 模型计算线性系统的阶跃响应

Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块从非线性 Simulink® 模型计算线性系统，并在仿真期间绘制该线性系统的阶跃响应。这两个模块除 **Bounds** 选项卡上的默认设置外完全相同。

- Linear Step Response Plot 不定义默认边界。
- Check Linear Step Response Characteristics 模块定义默认边界并为断言启用这些边界。

有关线性系统时域分析的详细信息，请参阅 Time-Domain Responses。

在仿真期间，软件对模型中指定的线性化输入和输出之间的部分进行线性化，然后绘制该线性系统的阶跃响应。您还可以将线性系统保存为 MATLAB® 工作区中的变量。

Simulink 模型可以是连续时间或离散时间，也可以是多速率模型，并且可以具有时间延迟。由于在此模块中只能指定一对线性化输入/输出，因此线性系统为单输入单输出（SISO）。

您可以指定阶跃响应边界并在图上查看它们。您还可以在仿真期间检查是否满足这些边界：

- 如果满足所有边界，模块不执行任何操作。
- 如果不满足某个边界，模块将触发断言，并在 MATLAB 命令窗口中显示警告消息。您还可以指定模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并使该模块获得焦点。

在仿真期间，模块还可以输出逻辑断言信号。

- 如果满足所有边界，信号为 true（`1`）。
- 如果任何边界不满足，信号为 false（`0`）。

要计算并绘制模型各个部分的阶跃响应，您可以添加多个 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块。

这些模块不支持代码生成，并且只能在 `Normal` 仿真模式下使用。
