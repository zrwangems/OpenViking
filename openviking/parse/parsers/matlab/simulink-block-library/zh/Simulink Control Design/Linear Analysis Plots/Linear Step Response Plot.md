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

### **Trigger** — 外部触发信号标量

使用此输入端口（由 External trigger 图标指示）连接外部触发信号，用于计算模型线性化。要指定要检测的触发信号类型，请使用 **Trigger type** 参数。

#### 依赖关系

要启用此端口，请将 **Linearize on** 参数设置为 `External trigger`。

### 输出

### **z–1** — 断言信号 `1` | `0`

以逻辑值输出断言信号的值。如果违反 **Bounds** 选项卡上指定的任何边界，则断言信号为 false（`0`）。否则，此信号为 true（`1`）。

默认情况下，输出信号的数据类型为 double。要将输出数据类型设置为 Boolean，请在 Simulink 模型中，在 Configuration Parameters 对话框中，选择 **Implement logic signals as Boolean data** 参数。此设置适用于模型中生成逻辑信号的所有模块。

您可以使用断言信号设计复杂的断言逻辑。有关示例，请参见 Verify Model Using Simulink Control Design and Simulink Verification Blocks。

#### 依赖关系

要启用此端口，请选择 **Output assertion signal** 参数。

## 参数

### **Show Plot** — 打开绘图按钮

要查看仿真期间计算的增益裕度和相位裕度，请在开始仿真前点击此按钮。如果您在 **Bounds** 选项卡上指定了边界，它们也会显示在绘图上。

要在打开模块时显示绘图，请选择 **Show plot on block open** 参数。

有关使用绘图的详细信息，请参见 Using the Plot。

### **Show plot on block open** — 打开模块时打开绘图 `off`（默认） | `on`

选择此参数以在打开模块时打开绘图。然后，您可以在绘图窗口中执行添加或修改边界等任务，而无需使用模块参数。要从绘图窗口访问模块参数，请选择 **Edit** 或点击 Parameter 图标。

有关使用绘图的详细信息，请参见 Using the Plot。

#### 编程使用

|  |
| --- |
| **模块参数：** `LaunchViewOnOpen` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Response Optimization** — 打开 Response Optimizer 按钮

打开 Response Optimizer 应用，以优化模型响应，从而满足 **Bounds** 选项卡上指定的设计要求。

仅当安装了 Simulink Design Optimization™ 软件时，此按钮才可用。

有关响应优化的详细信息，请参见 Design Optimization to Meet Step Response Requirements (GUI) (Simulink Design Optimization) 和 Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI) (Simulink Design Optimization)。

### 线性化

要指定要线性化的模型部分和其他线性化设置，请使用 **Linearizations** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块相同。

### **Linearization inputs/outputs** — 指定要线性化的模型部分线性分析点

要指定要线性化的模型部分，请从 Simulink 模型中选择信号，并将它们添加为线性化输入或输出。

线性化输入和输出表

在表中，**Block:Port:Bus Element** 列显示每个信号的以下信息。

- 源模块
- 信号连接到的源模块的输出端口
- 总线元素名称（如果信号位于总线中）

在 **Configuration** 列中，从以下类型中选择线性分析点的类型。有关线性分析点的详细信息，请参见 Specify Portion of Model to Linearize。

- `Open-loop Input` — 指定环路打开后的线性化输入点
- `Open-loop Output` — 指定环路打开前的线性化输出点
- `Loop Transfer` — 指定环路打开前的输出点，后跟一个输入
- `Input Perturbation` — 指定信号上的加性输入
- `Output Measurement` — 在信号处进行测量
- `Loop Break` — 指定环路打开
- `Sensitivity` — 指定加性输入，后跟输出测量
- `Complementary Sensitivity` — 指定输出，后跟加性输入

**注意**

如果在未指定线性化输入或输出的情况下仿真模型，软件会在 MATLAB Command Window 中生成警告，并且不会计算线性系统。

#### 编辑线性化输入和输出

要添加线性化输入和输出：

1. 要展开信号选择区域，请点击 Plus。

   对话框将展开以显示 **Click a signal in the model to select it** 区域。
2. 在 Simulink 模型中，选择一个或多个信号。

   所选信号会出现在 **Model signal** 表中。

   添加信号后的信号表
3. （可选）对于总线信号，展开总线以选择各个元素。

   **提示**

   对于大型总线或其他大型信号列表，您可以过滤信号名称。在 **Filter by name** 框中，输入搜索文本。名称匹配区分大小写。

   要修改过滤选项，请点击 Down arrow。有关过滤选项的详细信息，请参见 **Enable regular expression** 和 **Show filtered results as a flat list** 参数。
4. 要将所选信号添加到 **Linearization inputs/outputs** 表，请点击 Left arrow。
5. 在 **Configuration** 列中，指定信号类型。

或者，如果您的模型中定义了线性化输入和输出，则可以通过点击 Import 图标将它们添加到 **Linearization inputs/outputs** 表。

要从 **Linearization inputs/outputs** 表中删除信号，请选择该信号并点击 Delete 图标。

要在 Simulink 模型中突出显示信号的源模块，请在 **Linearization inputs/outputs** 表中选择该信号，然后点击 Highlight 图标。

### **Enable regular expression** — 启用使用正则表达式搜索信号 `on`（默认） | `off`

选择此选项以启用使用 MATLAB 正则表达式过滤信号名称。例如，在 **Filter by name** 文本框中输入 `t$` 会显示名称以小写 `t` 结尾的所有信号（及其直接父级）。有关详细信息，请参见 Regular Expressions。

#### 依赖关系

要启用此参数，请点击 **Filter by name** 文本框旁边的 Down arrow。

### **Show filtered results as a flat list** — 使用扁平列表显示过滤后的总线信号层级 `off`（默认） | `on`

选择此选项以扁平列表格式显示过滤后的信号列表。扁平列表格式使用点表示法反映总线信号的层级。信号根据 **Filter by name** 文本框中的文本进行过滤。

下图显示了过滤后的嵌套总线信号集的扁平列表格式示例。

#### 依赖关系

要启用此参数，请点击 **Filter by name** 文本框旁边的 Down arrow。

### **Linearize on** — 何时计算线性模型 `Simulation snapshots`（默认） | `External trigger`

使用此参数指定希望何时计算线性模型。

要在指定的仿真快照时间计算线性模型，请将此参数设置为 `Simulation snapshots`。使用 **Snapshot times** 参数指定快照时间。

在以下情况下使用仿真快照：

- 您知道模型处于稳态工作点的一个或多个时间
- 您希望在特定时间计算线性系统

要在基于触发的仿真事件时计算线性模型，请将此参数设置为 `External trigger`。选择此选项会向模块添加一个触发输入端口，您可以将外部触发信号连接到该端口。要指定要检测的触发类型，请使用 **Trigger type** 参数。

当仿真期间生成的信号指示模型处于感兴趣的稳态条件时，使用外部触发。例如，对于飞机模型，您可能希望在燃油质量达到最大燃油质量的给定比例时计算线性系统。

#### 编程使用

|  |
| --- |
| **模块参数：** `LinearizeAt` |
| **类型：** character vector |
| **值：** `'SnapshotTimes'` | `'ExternalTrigger'` |
| **默认值：** `'SnapshotTimes'` |

### **Snapshot times** — 计算线性模型时的仿真时间 `0`（默认） | positive real value | vector of positive real values

要在特定仿真时间（例如您知道模型达到稳态工作点的时间）计算线性系统，请指定一个或多个快照时间。要指定多个快照时间，请将此参数指定为正值的向量。

快照时间必须小于或等于 Simulink 模型中指定的仿真时间。

有关在仿真快照时间对模型进行线性化的示例，请参见：

- Visualize Linear System at Multiple Simulation Snapshots
- Verify Model at Default Simulation Snapshot Time
- Verify Model at Multiple Simulation Snapshots

#### 依赖关系

要启用此参数，请将 **Linearize on** 参数设置为 `Simulation snapshots`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SnapshotTimes` |
| **类型：** character vector |
| **值：** `'0'` | positive real value | vector of positive real values |
| **默认值：** `'0'` |

### **Trigger type** — 要检测的外部触发类型 `Rising edge`（默认） | `Falling edge`

指定要在外部触发信号中检测的触发类型为以下类型之一。

- `Rising edge` — 使用触发信号的上升沿；即信号从 `0` 变为 `1` 时。
- `Falling edge` — 使用触发信号的下降沿；即信号从 `1` 变为 `0` 时。

#### 依赖关系

要启用此参数，请将 **Linearize on** 参数设置为 `External trigger`。

#### 编程使用

|  |
| --- |
| **模块参数：** `TriggerType` |
| **类型：** character vector |
| **值：** `'rising'` | `'falling'` |
| **默认值：** `'rising'` |

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认） | `off`

选择此选项以启用过零检测。

当您将 **Linearize on** 参数设置为 `Simulation snapshots` 时，启用过零检测可确保软件在 **Snapshot times** 参数中指定的精确快照时间计算线性模型。

当您将 **Linearize on** 参数设置为 `External trigger` 时，启用过零检测可确保软件在检测到外部触发的精确时间计算线性模型。要指定触发类型，请使用 **Trigger type** 参数。

如果清除此选项，软件将在变步长 Simulink 求解器选择的仿真时间计算线性系统，这可能不对应于精确的快照时间或检测到触发信号的精确时间。

例如，考虑变步长求解器选择仿真时间
*T**n*–1 和
*Tn* 的情况。如下图所示，
指定的快照时间 *Tsnap* 可以位于所选仿真时间之间。如果启用过零检测，求解器还会在时间 *Tsnap* 仿真模型，并在该点计算线性模型。

类似地，外部触发可以在位于所选仿真时间之间的时间
*Ttrig* 被检测到。如果启用过零检测，求解器还会在时间 *Ttrig* 仿真模型，并在该点计算线性模型。

在这两种情况下，如果未启用过零检测，软件会在
*T**n*–1 或
*Tn* 处计算线性模型。

有关过零检测的详细信息，请参见 Zero-Crossing Detection。

#### 依赖关系

当您使用定步长 Simulink 求解器时，将忽略此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `ZeroCross` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Use exact delays** — 在线性模型中使用精确延迟 `off`（默认） | `on`

选择此选项以计算具有精确延迟的线性模型。如果清除此选项，线性模型将对任何延迟使用 Padé 近似。

有关对带延迟模型进行线性化的详细信息，请参见 Linearize Models with Delays。

#### 编程使用

|  |
| --- |
| **模块参数：** `UseExactDelayModel` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Linear system sample time** — 线性系统的采样时间 `'auto'`（默认） | positive finite value | `0`

要计算具有指定采样时间的线性系统，软件会使用您在 **Sample time rate conversion method** 参数中指定的方法转换模型中的采样时间。

您可以将采样时间设置为以下值之一。

- `auto` — 如果模型中的所有模块都是连续时间，则使用采样时间 `0`。否则，将采样时间设置为模型中非零采样时间的最小公倍数。
- Positive finite value — 创建具有指定采样时间的离散时间模型。
- `0` — 创建连续时间模型。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** `'auto'` | positive finite value | `'0'` |
| **默认值：** `'auto'` |

### **Sample time rate conversion method** — 采样时间速率转换方法 `Zero-Order Hold`（默认） | `Tustin (bilinear)` | `Tustin with Prewarping` | ...

线性化期间用于转换采样时间的方法，指定为以下值之一。

- `Zero-Order Hold` — 零阶保持，其中控制输入假定在采样时间 `Ts` 内分段常数。此方法通常在时域中表现更好。
- `Tustin (bilinear)` — 不带频率预扭曲的双线性（Tustin）近似。软件会将小数时间延迟舍入到采样时间的最接近倍数。此方法通常在频域中表现更好。
- `Tustin with Prewarping` — 带频率预扭曲的双线性（Tustin）近似。使用 **Prewarp frequency** 参数指定预扭曲频率。此方法通常在频域中表现更好。使用此方法可确保在感兴趣的频率区域内匹配。
- `Upsampling when possible, Zero-Order Hold otherwise` — 在可能时对离散时间系统进行上采样；否则，使用零阶保持。
- `Upsampling when possible, Tustin otherwise` — 在可能时对离散时间系统进行上采样；否则，使用 Tustin 近似。
- `Upsampling when possible, Tustin with Prewarping otherwise` — 在可能时对离散时间系统进行上采样；否则，使用带频率预扭曲的 Tustin 近似。

仅当您将离散时间系统转换为新的更快的采样时间，且该采样时间是原始系统采样时间的整数倍时，才可以进行上采样。

有关多速率模型的速率转换和线性化的详细信息，请参见：

- Multirate Linearization Algorithm
- Linearize Models Using Different Rate Conversion Methods
- Continuous-Discrete Conversion Methods

**注意**

如果您使用 `Zero-Order Hold` 以外的速率转换方法，则转换后的状态不再具有与原始状态相同的物理含义。因此，生成的 LTI 系统中的状态名称会变为 `'?'`。

#### 依赖关系

要启用此参数，请将 **Linear system sample time** 参数设置为 `auto` 以外的值。

#### 编程使用

|  |
| --- |
| **模块参数：** `RateConversionMethod` |
| **类型：** character vector |
| **值：** `'zoh'` | `'tustin'` | `'prewarp'`| `'upsampling_zoh'`| `'upsampling_tustin'`| `'upsampling_prewarp'` |
| **默认值：** `'zoh'` |

### **预扭曲频率** — 用于 Tustin 速率转换的预扭曲频率 `'10'`（默认）| positive scalar

用于 Tustin 速率转换的预扭曲频率，以 radians per second 为单位，指定为小于重采样前后 Nyquist 频率的标量值。

#### 依赖项

要启用此参数，请将 **采样时间速率转换方法** 参数设置为以下值之一。

- `Tustin with Prewarping`
- `Upsampling when possible, Tustin with Prewarping otherwise`

#### 程序化使用

|  |
| --- |
| **模块参数：** `PreWarpFreq` |
| **类型：** character vector |
| **值：** positive scalar |
| **默认值：** `'10'` |

### **使用完整模块名称** — 在状态、输入和输出名称中使用完整模块路径 `off`（默认）| `on`

要使用计算得到的线性系统的完整模块路径显示其状态、输入和输出名称，请选择此参数。例如，在 Plot Linear System Characteristics of a Chemical Reactor 示例中使用的 `scdcstr` 模型里，`CSTR` 子系统的 `Integrator1` 模块中的一个状态以完整路径显示为 `scdcstr/CSTR/Integrator1`。

如果清除此参数，则仅使用状态、输入和输出的名称，这在信号名称唯一且您知道它们在 Simulink 模型中的位置时很有用。在前述示例中，积分器模块的状态名称显示为 `Integrator1`。

计算得到的线性系统是状态空间对象（`ss`）。该系统的状态、输入和输出名称出现在以下状态空间对象属性中。

| 输入、输出或状态名称 | State-Space Object Property |
| --- | --- |
| 线性化输入名称 | `InputName` |
| 线性化输出名称 | `OutputName` |
| 状态名称 | `StateName` |

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseFullBlockNameLabels` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **使用总线信号名称** — 在线性系统中使用总线信号名称 `off`（默认）| `on`

当您选择整个总线作为线性化输入或输出时，选择此参数以在计算得到的线性系统中使用各个总线元素的信号名称。如果不启用此选项，则改用总线通道编号。

**注意**

不建议选择整个总线信号。而应选择单个总线元素。

当线性化输入或输出来自以下模块之一时，总线信号名称会出现。

- 包含总线对象的根级 inport 模块
- Bus creator 模块
- 其源可追溯到 Bus creator 模块的输出的 Subsystem 模块
- 其源仅穿过 virtual 或 nonvirtual 子系统边界追溯到根级 inport 的 Subsystem 模块

#### 依赖项

当您的模型包含 mux/bus 混合时，不支持使用此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseBusSignalLabels` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 边界

要定义阶跃响应特性的边界并指定是否检查这些边界的违反情况，请使用 **边界** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块不同。

### **在断言中包含阶跃响应边界** — 检查阶跃响应是否违反特性边界 `on` | `off`

选择此参数以检查阶跃响应特性是否违反在 **边界** 选项卡上指定的边界。

默认情况下，对于 Linear Step Response Plot 模块，清除此参数；对于 Check Linear Step Response Characteristics 模块，选择此参数。

#### 依赖项

仅当您选择 **启用断言** 参数时，此参数才用于断言。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EnableStepResponseBound` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'off'`，对于 Check Linear Step Response Characteristics 模块为 `'on'` |

### **最终值** — 阶跃输入响应中输出信号的最终值 finite real scalar

为了计算 **边界** 选项卡上的其他阶跃响应特性，模块使用输出信号对阶跃输入的预期最终值。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FinalValue` |
| **类型：** character vector |
| **值：** finite real scalar |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'[]'`，对于 Check Linear Step Response Characteristics 模块为 `'1'` |

### **上升时间** — 上升时间的上界 finite positive scalar

阶跃响应达到最终值某一百分比所需时间的上界，单位为 seconds。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定最终值的百分比，请使用 **% 上升** 参数。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `5`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RiseTime` |
| **类型：** character vector |
| **值：** finite positive scalar |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'[]'`，对于 Check Linear Step Response Characteristics 模块为 `'5'` |

### **% 上升** — 用于计算上升时间的最终值百分比 positive scalar less than (100 - % Settling)

用于定义上升时间边界的最终值百分比。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定上升时间边界，请使用 **上升时间** 参数。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `80`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PercentRise` |
| **类型：** character vector |
| **值：** positive scalar less than (100 - % Settling) |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'[]'`，对于 Check Linear Step Response Characteristics 模块为 `'80'` |

### **稳定时间** — 稳定时间的上界 finite scalar greater than rise time

阶跃响应在最终值周围指定范围内稳定所需时间的上界，单位为 seconds。此稳定范围定义为最终值加上或减去最终值的指定稳定百分比。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定稳定百分比，请使用 **% 稳定** 参数。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `7`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** character vector |
| **值：** finite scalar greater than rise time |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'[]'`，对于 Check Linear Step Response Characteristics 模块为 `'7'` |

### **% 稳定** — 用于计算稳定范围的最终值百分比 positive scalar less than (100 - % Rise)

用于定义稳定范围边界的最终值百分比。稳定范围定义为最终值加上或减去最终值的指定稳定百分比。

- 要指定最终值，请使用 **最终值** 参数。
- 要指定稳定时间边界，请使用 **稳定时间** 参数。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PercentSettling` |
| **类型：** character vector |
| **值：** positive scalar less than (100 - % Settling) |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'[]'`，对于 Check Linear Step Response Characteristics 模块为 `'1'` |

### **% 超调量** — 超调量的上界 scalar between 0 and 100

阶跃响应可超过最终值的量，定义为最终值的百分比。要指定最终值，请使用 **最终值** 参数。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `10`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PercentOvershoot` |
| **类型：** character vector |
| **值：** scalar between 0 and 100 |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'[]'`，对于 Check Linear Step Response Characteristics 模块为 `'10'` |

### **% 下冲量** — 下冲量的上界 scalar between 0 and 100

阶跃响应可下冲初始值的量，定义为最终值的百分比。要指定最终值，请使用 **最终值** 参数。

默认情况下，对于 Linear Step Response Plot 模块，此参数为 `[]`；对于 Check Linear Step Response Characteristics 模块，此参数为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PercentUndershoot` |
| **类型：** character vector |
| **值：** scalar between 0 and 100 |
| **默认值：** 对于 Linear Step Response Plot 模块为 `'[]'`，对于 Check Linear Step Response Characteristics 模块为 `'1'` |

### 日志记录

要控制是否保存在仿真期间计算得到的线性化结果，请使用 **日志记录** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块相同。

### **将数据保存到工作区** — 保存线性系统以供进一步分析 `off`（默认）| `on`

选择此参数以保存计算得到的线性系统，以供进一步分析或控制设计。数据保存在一个具有以下字段的 structure 中。

- `time` — 计算线性系统时的仿真时间。
- `values` — 表示线性系统的状态空间模型。如果线性系统在多个仿真时间计算，`values` 是状态空间模型的数组。
- `operatingPoints` — 与 `values` 中每个线性系统对应的工作点。要启用此字段，请选择 **为每个线性化保存工作点** 参数。

要指定保存的数据结构的名称，请使用 **变量名称** 属性。

保存的数据结构的位置取决于 Simulink 模型的配置。

- 如果模型未配置为将仿真输出保存为单个对象，则数据结构是 MATLAB 工作区中的变量。
- 如果模型配置为将仿真输出保存为单个对象，则数据结构是包含记录的仿真数据的 `Simulink.SimulationOutput` 对象中的字段。

要将模型配置为将仿真输出保存在单个对象中，请在 **配置参数** 对话框中，选择 **单个仿真输出** 参数。

有关 Simulink 中数据日志记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaveToWorkspace` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **变量名称** — 用于保存线性系统的数据结构名称 `sys`（默认）| character vector

指定用于存储仿真期间计算得到的线性系统的数据结构的名称。

该名称在所有数据日志记录模块（例如 Linear Analysis Plot 模块、Model Verification 模块、Scope 模块、To Workspace 模块）以及仿真返回变量（例如 time、states 和 outputs）所使用的变量名称中必须唯一。

有关 Simulink 中数据日志记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

#### 依赖项

要启用此参数，请选择 **将数据保存到工作区** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaveName` |
| **类型：** character vector |
| **默认值：** `'sys'` |

### **为每个线性化保存工作点** — 保存线性化对应的工作点 `off`（默认）| `on`

选择此参数以保存计算每个线性化时的工作点。选择此参数会将 `operatingPoints` 字段添加到保存的数据结构中。

#### 依赖项

要启用此参数，请选择 **将数据保存到工作区** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SaveOperatingPoints` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### 断言

要控制当违反 **边界** 选项卡上定义的边界时模块的断言行为，请使用 **断言** 选项卡上的参数。此选项卡上的默认设置对于 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块相同。

### **启用断言** — 启用边界检查 `on`（默认）| `off`

要检查在仿真期间是否满足 **边界** 选项卡上定义的边界，请选择此参数。当某个边界未满足时，断言失败并生成警告。

清除此参数将禁用断言；也就是说，模块不再检查是否满足指定的边界。模块图标也会更新以指示断言已禁用。

带有 X 的模块，指示断言已禁用。

默认情况下，在 **边界** 选项卡上：

- Linear Step Response Plot 模块没有定义的边界。
- Check Linear Step Response Characteristics 模块有定义的边界。

您可以配置 Simulink 模型以启用或禁用所有模型验证模块，并覆盖 **启用断言** 参数。为此，在 Simulink 模型中，在 **配置参数** 对话框中，指定 **模型验证模块启用** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `enabled` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **断言失败时的仿真回调** — 当违反边界时要求值的表达式 `''`（默认）| MATLAB expression

指定当违反 **边界** 选项卡上指定的边界时要计算的 MATLAB 表达式。表达式中使用的所有变量都必须位于 MATLAB 工作区中。

#### 依赖项

要启用此参数，请选择 **启用断言** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `callback` |
| **类型：** character vector |
| **值：** MATLAB expression |
| **默认值：** `''` |

### **断言失败时停止仿真** — 当违反边界时停止仿真 `off`（默认）| `on`

要在违反 **边界** 选项卡上指定的边界时停止仿真，请选择此参数。如果不选择此选项，边界违反将作为警告报告在 MATLAB 命令窗口中，并且仿真继续。

如果从 Simulink 模型运行仿真，当断言失败时，发生边界违反的模块会高亮显示，并在 **仿真诊断** 窗口中显示错误消息。

**注意**

由于选择此选项会在断言失败时立即停止仿真，因此不会报告仿真期间稍后可能发生的边界违反。如果希望报告所有边界违反，请不要选择此选项。

#### 依赖项

要启用此参数，请选择 **启用断言** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `stopWhenAssertionFail` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出断言信号** — 添加断言输出端口 `off`（默认） | `on`

将 **z–1** 断言信号输出端口添加到模块。此端口将断言的值作为 Boolean 信号输出。当违反 **边界** 选项卡上定义的边界时，断言失败，断言信号为 `0`。否则，断言信号为 `1`。

您可以使用断言信号来设计复杂的断言逻辑。有关示例，请参阅使用 Simulink Control Design 和 Simulink Verification Blocks 验证模型。

#### 编程用法

|  |
| --- |
| **模块参数：** `export` |
| **类型：** character vector |
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

从非线性 Simulink 模型计算得到的线性系统的阶跃响应

Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块从非线性 Simulink® 模型计算线性系统，并在仿真期间绘制该线性系统的阶跃响应。除 **边界** 选项卡上的默认设置外，这些模块完全相同。

- Linear Step Response Plot 不定义默认边界。
- Check Linear Step Response Characteristics 模块定义默认边界，并为断言启用这些边界。

有关线性系统时域分析的详细信息，请参阅时域响应。

在仿真期间，软件对模型中指定的线性化输入和输出之间的部分进行线性化，然后绘制该线性系统的阶跃响应。您还可以将线性系统保存为 MATLAB® 工作区中的变量。

Simulink 模型可以是连续时间或离散时间，也可以是多速率，并且可以具有时间延迟。由于在此模块中只能指定一个线性化输入/输出对，因此线性系统为单输入单输出 (SISO)。

您可以指定阶跃响应边界，并在图上查看这些边界。您还可以在仿真期间检查是否满足这些边界：

- 如果满足所有边界，则模块不执行任何操作。
- 如果未满足某个边界，则模块执行断言，并且 MATLAB 命令窗口中会出现警告消息。您还可以指定模块执行以下操作：

  - 计算 MATLAB 表达式。
  - 停止仿真并使该模块获得焦点。

在仿真期间，模块还可以输出逻辑断言信号。

- 如果满足所有边界，则信号为 true (`1`)。
- 如果任一边界未满足，则信号为 false (`0`)。

要计算并绘制模型各个部分的阶跃响应，您可以添加多个 Linear Step Response Plot 和 Check Linear Step Response Characteristics 模块。

这些模块不支持代码生成，并且只能在 `Normal` 仿真模式下使用。
