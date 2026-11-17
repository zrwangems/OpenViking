---
type: simulink-block
title: 'Singular Value Plot'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Linear Analysis Plots'
documentation_page: 'singularvalueplot'
documentation_source_path: 'ug/singularvalueplot.html'
language: zh-CN
chinese_source: worker-translation
---

# Singular Value Plot

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

下表汇总了 Singular Value Plot 模块参数，可通过模块参数对话框访问。

| 任务 | | 参数 |
| --- | --- | --- |
| 配置线性化。 | 指定输入和输出（I/O）。 | 在 **Linearizations** 选项卡中： - Linearization inputs/outputs。 - 点击模型中的信号以选择它。 |
| 指定设置。 | 在 **Linearizations** 选项卡中： - Linearize on。 - Snapshot times。 - Trigger type。 |
| 指定算法选项。 | 在 **Linearizations** 选项卡的 **Algorithm Options** 中： - Enable zero-crossing detection。 - Use exact delays。 - Linear system sample time。 - Sample time rate conversion method。 - Prewarp frequency (rad/s)。 |
| 为线性系统 I/O 和状态名称指定标签。 | 在 **Linearizations** 选项卡的 **Labels** 中： - Use full block names。 - Use bus signal names。 |
| 绘制线性系统。 | | **Show Plot** |
| （可选）为断言指定奇异值边界。 | | 在 **Bounds** 选项卡中： - Include upper singular   value bound in assertion。 - Include lower singular   value bound in assertion。 |
| 指定断言选项（仅当您为线性系统指定边界时）。 | | 在 **Assertion** 选项卡中： - Enable assertion。 - Simulation callback when assertion fails (optional)。 - Stop simulation when assertion fails。 - Output assertion signal。 |
| 将线性系统保存到 MATLAB 工作区。 | | 在 **Logging** 选项卡中将数据保存到工作区。 |
| 双击模块时显示绘图窗口而不是模块参数对话框。 | | Show plot on block open。 |

### Linearization inputs/outputs

定义非线性 Simulink 模型中要线性化的部分的线性化输入和输出。

如果您已在 Simulink 模型中定义线性化输入和输出，该模块会自动检测这些点，并将它们显示在 **Linearization inputs/outputs** 区域中。可随时点击  以使用模型中的 I/O 更新 **Linearization inputs/outputs** 表。要添加其他分析点：

1. 点击 。

   对话框将展开，显示 **Click a signal in the model to select it** 区域和一个新的  按钮。
2. 在 Simulink Editor 中选择一个或多个信号。

   所选信号将显示在 **Click a signal in the model to select it** 区域中的 **Model signal** 下。
3. （可选）对于总线，展开总线信号以选择单个元素。

   **提示**

   对于大型总线或其他大型信号列表，您可以在 **Filter by name** 编辑框中输入搜索文本来过滤元素名称。名称匹配区分大小写。此外，您还可以输入 MATLAB 正则表达式。

   要修改过滤选项，请点击 。要隐藏过滤选项，请点击 。

    Filtering Options

   - Enable regular expression
   - Show filtered results as a flat list
4. 点击  将所选信号添加到 **Linearization inputs/outputs** 表中。

   要从 **Linearization inputs/outputs** 表中删除信号，请选择该信号并点击 。

   **提示**

   要查找 **Linearization inputs/outputs** 表中某个信号在 Simulink 模型中对应的位置，请在表中选择该信号并点击 。

该表显示有关所选信号的以下信息：

|  |  |
| --- | --- |
| **Block : Port : Bus Element** | 与输入/输出关联的模块名称。模块名称旁边的数字是所选总线信号所在端口的端口号。最后一项是所选总线元素名称。 |
| **Configuration** | 线性化点的类型： - `Open-loop Input` — 指定回路开环后的线性化输入点。 - `Open-loop Output` — 指定回路开环前的线性化输出点。 - `Loop Transfer` — 指定回路开环前的输出点，后跟一个输入。 - `Input Perturbation` — 指定信号的加性输入。 - `Output Measurement` — 在信号处进行测量。 - `Loop Break` — 指定回路开环。 - `Sensitivity` — 指定加性输入，后跟输出测量。 - `Complementary Sensitivity` — 指定输出，后跟加性输入。 |

**注意**

如果您在未指定输入或输出的情况下仿真模型，软件不会计算线性系统。相反，您会在 MATLAB 命令提示符处看到一条警告消息。

**设置**

**无默认值**

**命令行信息**

使用 `getlinio` 和 `setlinio` 指定线性化输入和输出。

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 在模型中点击信号以将其选中

启用 Simulink 模型中的信号选择。仅在您点击  时出现。

当此选项出现时，您还会看到以下更改：

- 一个新的  按钮。

  用于将所选信号作为线性化输入或输出添加到 **Linearization inputs/outputs** 表中。有关详细信息，请参阅 **Linearization inputs/outputs**。
-  变为 。

  用于折叠 **Click a signal in the model to select it** 区域。

**设置**

**无默认值**

**命令行信息**

使用 `getlinio` 和 `setlinio` 命令选择信号作为线性化输入和输出。

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Enable regular expression

启用使用 MATLAB 正则表达式过滤信号名称。例如，在 **Filter by name** 编辑框中输入 `t$` 会显示所有名称以小写 `t` 结尾的信号（及其直接父级）。有关详细信息，请参阅 Regular Expressions。

**设置**

**默认值：** On

On
:   允许使用 MATLAB 正则表达式过滤信号名称。

Off
:   禁用使用 MATLAB 正则表达式过滤信号名称。过滤会将你在 **Filter by name** 编辑框中输入的文本视为字面字符向量。

**依赖关系**

选择 **Filter by name** 编辑框右侧的 **Options** 按钮
() 会启用此参数。

### Show filtered results as a flat list

使用扁平列表格式显示过滤后的信号列表，基于 **Filter by name** 编辑框中的搜索文本。扁平列表格式使用点表示法来反映总线信号的层次结构。以下是过滤后的嵌套总线信号集合的扁平列表格式示例。

**设置**

**默认值：** Off

On
:   使用扁平列表格式显示过滤后的信号列表，使用点表示法指示总线层次结构，而不是使用树格式。

Off
:   使用树格式显示过滤后的总线层次结构。

**依赖关系**

选择 **Filter by name** 编辑框右侧的 **Options** 按钮
() 会启用此参数。

### Linearize on

在仿真期间何时计算线性系统。

**设置**

**默认值：** `Simulation
snapshots`

`Simulation snapshots`
:   特定仿真时间，在 **Snapshot times** 中指定。

    在以下情况下使用：

    - 知道模型处于稳态工作点的一个或多个时间
    - 想要在特定时间计算线性系统

`External trigger`
:   基于触发的仿真事件。在 **Trigger type** 中指定触发类型。

    当仿真期间生成的信号指示稳态工作点时使用。

    选择此选项会向模块添加一个触发端口。使用此端口将模块连接到触发信号。

    例如，对于飞机模型，你可能希望在燃油质量是最大燃油质量的一部分时计算线性系统。在这种情况下，将此条件建模为外部触发。

**依赖关系**

- 将此参数设置为 `Simulation
  snapshots` 会启用 **Snapshot times**。
- 将此参数设置为 `External trigger` 会启用 **Trigger
  type**。

**命令行信息**

|  |
| --- |
| **Parameter:** `LinearizeAt` |
| **类型**：character vector |
| **Value:** `'SnapshotTimes'` | `'ExternalTrigger'` |
| **默认值**：`'SnapshotTimes'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Snapshot times

一个或多个仿真时间。在这些时间计算线性系统。

**设置**

**默认值：** 0

- 对于不同的仿真时间，输入该时间。在以下情况下使用：

  - 想要在特定时间绘制线性系统
  - 知道模型达到稳态工作点的近似时间
- 对于多个仿真时间，输入一个向量。当你想要在多个时间计算并绘制线性系统时使用。

Snapshot times 必须小于或等于 Simulink 模型中指定的仿真时间。

**依赖关系**

在 **Linearize on** 中选择 `Simulation snapshots` 会启用此参数。

**命令行信息**

|  |
| --- |
| **Parameter:** `SnapshotTimes` |
| **类型**：character vector |
| **Value:** `0` | positive real number | vector of positive real numbers |
| **默认值**：`0` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Trigger type

用于计算线性系统的外部触发器的触发类型。

**设置**

**默认值：** `Rising
edge`

`Rising edge`
：外部触发信号的上升沿。

`Falling edge`
：外部触发信号的下降沿。

**依赖关系**

在 **Linearize on** 中选择 `External trigger` 会启用此参数。

**命令行信息**

|  |
| --- |
| **参数：** `TriggerType` |
| **类型：** 字符向量 |
| **值：** `'rising'` | `'falling'` |
| **默认值：** `'rising'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Enable zero-crossing detection

启用零交叉检测，以确保软件在以下仿真时间计算线性系统特性：

- 在 **Snapshot times** 中指定的精确快照时间。

  如下图所示，当启用零交叉检测时，变步长 Simulink 求解器会在快照时间 `Tsnap` 对模型进行仿真。`Tsnap` 可能位于求解器自动选择的仿真时间步 `Tn-1` 和 `Tn` 之间。
- 在 **Trigger
  type** 中指定的检测到外部触发器的精确时间。

  如下图所示，当启用零交叉检测时，变步长 Simulink 求解器会在检测到触发信号的时间 `Ttrig` 对模型进行仿真。`Ttrig` 可能位于求解器自动选择的仿真时间步 `Tn-1` 和 `Tn` 之间。

有关零交叉检测的详细信息，请参阅 *Simulink User Guide* 中的 Zero-Crossing Detection。

**设置**

**默认值：** On

On
：在精确快照时间或检测到触发信号的精确时间计算线性系统特性。

    如果 Simulink 求解器为固定步长，则忽略此设置。

Off
：在变步长求解器选择的仿真时间步计算线性系统特性。软件可能不会在精确快照时间或检测到触发信号的精确时间计算线性系统。

**命令行信息**

|  |
| --- |
| **参数：** `ZeroCross` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Use exact delays

如何在线性模型中表示时间延迟。

如果模型中的模块具有时间延迟，请使用此选项。

**设置**

**默认值：** Off

On
：返回具有精确延迟表示的线性模型。

Off
：返回具有延迟 Padé 近似的线性模型，如您的 Transport Delay 和 Variable
    Transport Delay 模块中所指定。

**命令行信息**

|  |
| --- |
| **参数：** `UseExactDelayModel` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 线性系统采样时间

仿真期间计算的线性系统采样时间。

使用此参数可以：

- 从连续时间系统计算具有特定采样时间的离散时间系统
- 以不同的采样时间对离散时间系统进行重采样
- 从离散时间系统计算连续时间系统

当从连续时间系统计算离散时间系统（反之亦然）时，软件使用**采样时间速率转换方法**中指定的转换方法。

**设置**

**默认值：** `auto`

`auto`。按如下方式计算采样时间：
:   - 对于连续时间模型，为 0。
    - 对于具有不同采样时间模块的模型（多速率模型），为采样时间的最小公倍数。例如，如果混合使用采样时间为 0、0.2 和 0.3 的连续时间模块和离散时间模块，则线性模型的采样时间为 0.6。

正有限值。用于计算：
:   - 从连续时间系统计算离散时间线性系统。
    - 从具有不同采样时间的另一个离散时间系统计算离散时间线性系统

`0`
:   用于从离散时间模型计算连续时间线性系统。

**命令行信息**

|  |
| --- |
| **参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** `'auto'` | 正有限值 | `'0'` |
| **默认值：** `'auto'` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 采样时间速率转换方法

用于转换单速率或多速率模型的采样时间的方法。

仅当 **Linear system sample time** 的值不是 `auto` 时，才使用此参数。

**设置**

**默认值：** `Zero-Order Hold`

`Zero-Order Hold`
：零阶保持，其中假设控制输入在采样时间 `Ts` 内分段恒定。有关详细信息，请参阅 Zero-Order Hold。

此方法通常在时域中表现更好。

`Tustin (bilinear)`
：不带频率预畸变的双线性（Tustin）近似。软件会将分数时间延迟舍入到采样时间的最近倍数。有关详细信息，请参阅 Tustin Approximation。

此方法通常在频域中表现更好。

`Tustin with Prewarping`
：带频率预畸变的双线性（Tustin）近似。还需在 **Prewarp frequency (rad/s)** 中指定预畸变频率。有关详细信息，请参阅 Tustin Approximation。

此方法通常在频域中表现更好。使用此方法可确保在感兴趣的频率区域内匹配。

`Upsampling when possible, Zero-Order Hold otherwise`
：在可能时对离散时间系统进行上采样，否则使用 `Zero-Order Hold`。

仅当将离散时间系统转换为新的更快采样时间，且该采样时间是原系统采样时间的整数倍时，才能进行上采样。

`Upsampling when possible, Tustin otherwise`
：在可能时对离散时间系统进行上采样，否则使用 `Tustin (bilinear)`。

仅当将离散时间系统转换为新的更快采样时间，且该采样时间是原系统采样时间的整数倍时，才能进行上采样。

`Upsampling when possible, Tustin with Prewarping otherwise`
：在可能时对离散时间系统进行上采样，否则使用 `Tustin with Prewarping`。此外，还需在 **Prewarp frequency (rad/s)** 中指定预畸变频率。

仅当将离散时间系统转换为新的更快采样时间，且该采样时间是原系统采样时间的整数倍时，才能进行上采样。

**依赖关系**

选择以下任一选项：

- `Tustin with Prewarping`
- `Upsampling when possible, Tustin with Prewarping otherwise`

会启用 **Prewarp frequency (rad/s)**。

**命令行信息**

|  |
| --- |
| **Parameter:** `RateConversionMethod` |
| **类型**：character vector |
| **Value:** `'zoh'` | `'tustin'` | `'prewarp'`| `'upsampling_zoh'`| `'upsampling_tustin'`| `'upsampling_prewarp'` |
| **默认值**：`'zoh'` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Prewarp frequency (rad/s)

Tustin 方法的预畸变频率，以弧度/秒为单位指定。

**设置**

**默认值：** 10

正标量值，小于重采样前后的奈奎斯特频率。值 `0` 对应于不带频率预畸变的标准 Tustin 方法。

**依赖关系**

在 **Sample time rate conversion method** 中选择以下任一选项

- `Tustin with Prewarping`
- `Upsampling when possible, Tustin with Prewarping otherwise`

会启用此参数。

**命令行信息**

|  |
| --- |
| **Parameter:** `PreWarpFreq` |
| **类型**：character vector |
| **Value:** `10` | positive scalar value |
| **默认值**：`10` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 使用完整模块名称

状态、输入和输出名称在仿真期间计算的线性系统中如何显示。

线性系统是一个状态空间对象，系统状态和输入/输出名称显示在以下状态空间对象属性中：

| 输入、输出或状态名称 | 出现在哪个状态空间对象属性中 |
| --- | --- |
| 线性化输入名称 | `InputName` |
| 线性化输出名称 | `OutputName` |
| 状态名称 | `StateName` |

**设置**

**默认：** Off

On
:   显示状态和输入/输出名称及其在模型层级中的路径。例如，在 Plot Linear System Characteristics of a Chemical Reactor 示例中使用的 `scdcstr` 模型里，`CSTR` 子系统内 `Integrator1` 模块中的一个状态会以完整路径显示为 `scdcstr/CSTR/Integrator1`。

Off
:   仅显示状态和输入/输出名称。当信号名称唯一且您知道信号在 Simulink 模型中的位置时，请使用此选项。例如，`CSTR` 子系统内 `Integrator1` 模块中的一个状态会显示为 `Integrator1`。

**命令行信息**

|  |
| --- |
| **参数：** `UseFullBlockNameLabels` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 使用总线信号名称

在仿真期间计算的线性系统中，如何标记与总线上的线性化输入和输出相关联的信号（仅当您选择整个总线作为 I/O 点时适用）。

不建议选择整个总线信号。相反，请选择单个总线元素。

当您的模型包含 mux/bus 混合时，不能使用此参数。

**设置**

**默认：** Off

On
:   使用各个总线元素的信号名称。

    当输入和输出位于以下模块的输出端时，会显示总线信号名称：

    - 包含 bus object 的根级 inport 模块
    - Bus creator 模块
    - 其源可追溯到以下模块之一的 Subsystem 模块：

      - Bus creator 模块的输出
      - 仅通过虚拟或非虚拟子系统边界传递的根级 inport 模块

Off
:   使用总线信号通道编号。

**命令行信息**

|  |
| --- |
| **参数：** `UseBusSignalLabels` |
| **类型：** character vector |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 在断言中包含奇异值上界

在仿真期间检查奇异值是否满足 **Frequencies (rad/sec)** 和 **Magnitude (dB)** 中指定的上界。如果奇异值违反上界，软件会在仿真期间显示警告。

仅当 **Assertion** 选项卡中的 **Enable assertion** 被选中时，此参数才用于断言。

您可以为线性系统指定多个奇异值上界。这些边界也会显示在奇异值图上。如果清除 **Enable assertion**，这些边界不会用于断言，但仍会继续显示在图上。

**设置**

**默认：**

- 对于 Singular Value Plot 模块为 Off。
- 对于 Check Singular Value Characteristics 模块为 On。

On
:   在仿真期间检查奇异值是否满足指定的上界。

Off
:   在仿真期间不检查奇异值是否满足指定的上界。

**提示**

- 清除此参数会禁用奇异值上界，软件将停止在仿真期间检查是否满足这些边界。边界段在图上也会变灰。
- 如果您同时指定了奇异值上界和下界，但只想将下界用于断言，请清除此参数。
- 如果只想在图上查看边界，请清除 **Enable assertion**。

**命令行信息**

|  |
| --- |
| **Parameter:** `EnableUpperBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` for Singular Value Plot block, `'on'` for Check Singular Value Characteristics block. |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Frequencies (rad/sec)

一个或多个奇异值上界段的频率，以弧度/秒为单位指定。

在 **Magnitude (dB)** 中指定对应的幅值。

**设置**

**默认：**

|  |
| --- |
| 奇异值绘图模块的 `[]` |
| 检查奇异值特性模块的 `[0.1 100]` |

必须指定为起始频率和终止频率：

- 对于具有一条边的单个边界，指定为正有限数
- 对于具有多条边的单个边界，指定为正有限数矩阵

  例如，键入 [0.1 1;1 10] 表示频率 [0.1 1] 和 [1 10] 处的两条边。
- 对于多个边界，指定为正有限数矩阵的元胞数组。

**提示**

- 要断言与这些频率对应的幅值得到满足，请同时选择 **Include upper singular value bound in assertion** 和 **Enable assertion**。
- 您可以从绘图窗口添加或修改频率：

  - 要添加新频率，请右键点击图，然后选择 **Bounds** > **New Bound**。在 **Design requirement type** 中选择 `Upper gain limit`，并在 **Frequency** 列中指定频率。在 **Magnitude** 列中指定对应的幅值。
  - 要修改频率，请拖动边界段。或者，右键点击该段，然后选择 **Bounds** > **Edit Bound**。在 **Frequency** 列中指定新的频率。

  在仿真模型之前，您必须点击 **Update Block**。

**命令行信息**

|  |
| --- |
| **Parameter:** `UpperBoundFrequencies` |
| **类型**：character vector |
| **值：** `[]` | `[0.1 100]` | 正有限数 | 正有限数矩阵 | 包含正有限数的矩阵元胞数组。必须在单引号（`''`）内指定。 |
| **默认值**：`'[]'` for Singular Value Plot block, `'[0.1 100]'` for Check Singular Value Characteristics block. |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Magnitudes (dB)

一个或多个上奇异值边界段的幅值，以分贝为单位指定。

在 **Frequencies (rad/sec)** 中指定对应的频率。

**设置**

**默认值：**

|  |
| --- |
| Singular Value Plot 模块为 `[]` |
| Check Singular Value Characteristics 模块为 `[0 0]` |

必须指定为起始和结束幅值：

- 对于具有一条边的单个边界，使用有限数
- 对于具有多条边的单个边界，使用有限数矩阵

  例如，键入 [0 0; 10 10] 表示两条边，幅值分别为 [0 0] 和 [10
  10]。
- 对于多个边界，使用由有限数矩阵组成的元胞数组

**提示**

- 要断言幅值得到满足，请同时选择 **Include upper singular
  value bound in assertion** 和 **Enable assertion**。
- 您可以从绘图窗口添加或修改幅值：

  - 要添加新幅值，请右键点击绘图，然后选择 **Bounds** > **New Bound**。在
    **Design requirement type** 中选择 `Upper gain limit`，并在
    **Magnitude** 列中指定幅值。在
    **Frequency** 列中指定对应的频率。
  - 要修改幅值，请拖动边界段。或者，右键点击
    该段，然后选择 **Bounds** > **Edit Bound**。在 **Magnitude**
    列中指定新的幅值。

  在仿真模型之前，必须点击 **Update Block**。

**命令行信息**

|  |
| --- |
| **Parameter:** `UpperBoundMagnitudes` |
| **类型**：character vector |
| **Value:** `[]` | `[0 0]` | finite number | matrix of finite numbers | cell array of matrices with finite numbers。必须在单引号 (`''`) 内指定。 |
| **默认值**：Singular Value Plot 模块为 `'[]'`，Check Singular Value Characteristics 模块为 `'[0 0]'`。 |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Include lower singular value bound in assertion

检查奇异值在仿真期间是否满足在 **Frequencies
(rad/sec)** 和 **Magnitude
(dB)** 中指定的下界。如果奇异值违反下界，软件将显示警告。

仅当选择了 **Assertion** 选项卡中的 **Enable
assertion** 时，此参数才用于断言。

您可以在线性系统上指定多个下奇异值边界。这些边界也会显示在奇异值图上。如果清除 **Enable assertion**，
这些边界不会用于断言，但仍会继续显示在图上。

**设置**

**默认值：** Off

On
:   在仿真期间检查奇异值是否满足指定的下界。

Off
:   在仿真期间不检查奇异值是否满足指定的下界。

**提示**

- 清除此参数会禁用上界，软件将停止在仿真期间检查
  边界是否得到满足。边界段也会在绘图窗口中变灰。
- 如果您同时指定了下奇异值边界和上奇异值边界，
  但只想将上界用于断言，请清除此参数。
- 如果只想在图上查看边界，请清除 **Enable assertion**。

**命令行信息**

|  |
| --- |
| **Parameter:** `EnableLowerBound` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Frequencies (rad/sec)

一个或多个下奇异值边界段的频率，以弧度/秒为单位指定。

在 **Magnitude (dB)** 中指定对应的幅值。

**设置**

**默认值**
`[]`

必须指定为起始和结束频率：

- 对于具有一条边的单个边界，为正有限数
- 对于具有多条边的单个边界，为正有限数矩阵

  例如，键入 [0.01 0.1;0.1 1] 以指定两条边，频率分别为 [0.01
  0.1] 和 [0.1 1]。
- 对于多个边界，为正有限数矩阵的元胞数组。

**提示**

- 要断言与频率对应的幅值边界得到满足，请同时选择 **Include lower singular
  value bound in assertion** 和 **Enable assertion**。
- 您可以从绘图窗口添加或修改频率：

  - 要添加新频率，请右键单击绘图，然后选择 **Bounds** > **New Bound**。在
    **Design requirement type** 中选择 `Lower gain limit`，并在
    **Frequency** 列中指定频率。在
    **Magnitude** 列中指定对应的幅值。
  - 要修改频率，请拖动边界段。或者，右键单击
    该段，然后选择 **Bounds** > **Edit Bound**。在 **Frequency**
    列中指定新的频率。

  在仿真模型之前，您必须点击 **Update Block**。

**命令行信息**

|  |
| --- |
| **Parameter:** `LowerBoundFrequencies` |
| **类型**：character vector |
| **值：** `[]` | 正有限数 | 正有限数矩阵 | 包含正有限数的矩阵元胞数组。必须在单引号（`''`）内指定。 |
| **默认值**：`'[]'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Magnitudes (dB)

一个或多个下奇异值边界段的幅值，以分贝为单位指定。

在 **Frequencies (rad/sec)** 中指定对应的频率。

**设置**

**默认值**
`[]`

必须指定为起始和结束幅值：

- 对于具有一条边的单个边界，为有限数
- 对于具有多条边的单个边界，为有限数矩阵

  例如，键入 [0 0; 10 10] 以指定两条边，幅值分别为 [0 0] 和 [10
  10]。
- 对于多个边界，为有限数矩阵的元胞数组

**提示**

- 要断言幅值得到满足，请同时选择 **Include lower singular
  value bound in assertion** 和 **Enable assertion**。
- 您可以从绘图窗口添加或修改幅值：

  - 要添加新幅值，请右键单击绘图，然后选择 **Bounds** > **New Bound**。在
    **Design requirement type** 中选择 `Lower gain limit`，并在
    **Magnitude** 列中指定幅值。在
    **Frequency** 列中指定对应的频率。
  - 要修改幅值，请拖动边界段。或者，右键单击
    该段，然后选择 **Bounds** > **Edit Bound**。在 **Magnitude**
    列中指定新的幅值。

  在仿真模型之前，您必须点击 **Update Block**。

**命令行信息**

|  |
| --- |
| **Parameter:** `LowerBoundFrequencies` |
| **类型**：character vector |
| **值：** `[]` | 有限数 | 有限数矩阵 | 包含有限数的矩阵元胞数组。必须在单引号（`''`）内指定。 |
| **默认值**：`'[]'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Save data to workspace

将一个或多个线性系统保存，以便执行进一步的线性分析或控制系统设计。

保存的数据位于一个结构中，其字段包括：

- `time` — 计算线性系统时的仿真时间。
- `values` — 表示线性系统的状态空间模型。如果在多个仿真时间计算线性系统，则 `values` 是状态空间模型的数组。
- `operatingPoints` — 与 `values` 中每个线性系统对应的工作点。仅当选中 **Save operating points for each linearization** 时，此字段才存在。

保存的数据结构的位置取决于 Simulink 模型的配置：

- 如果 Simulink 模型未配置为将仿真输出保存为单个对象，则该数据结构是 MATLAB 工作区中的一个变量。
- 如果 Simulink 模型配置为将仿真输出保存为单个对象，则该数据结构是 `Simulink.SimulationOutput` 对象中包含已记录仿真数据的一个字段。

  要将模型配置为将仿真输出保存为单个对象，请在 Simulink 编辑器的 **Modeling** 选项卡上，点击 **Model Settings**。然后，在 Configuration Parameters 对话框中，选择 **Single simulation output** 参数。

有关 Simulink 中数据记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

**Settings**

**默认值**：Off

On
:   保存计算得到的线性系统。

Off
:   不保存计算得到的线性系统。

**Dependencies**

此参数启用 **Variable name**。

**命令行信息**

|  |
| --- |
| **Parameter:** `SaveToWorkspace` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

**See Also**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Variable name

存储仿真期间计算的一个或多个线性系统的数据结构名称。

保存的数据结构的位置取决于 Simulink 模型的配置：

- 如果 Simulink 模型未配置为将仿真输出保存为单个对象，则该数据结构是 MATLAB 工作区中的一个变量。
- 如果 Simulink 模型配置为将仿真输出保存为单个对象，则该数据结构是 `Simulink.SimulationOutput` 对象中包含已记录仿真数据的一个字段。

该名称必须在所有数据记录模型模块（例如 Linear Analysis Plot 模块、Model Verification 模块、Scope 模块、To Workspace 模块）以及仿真返回变量（例如 time、states 和 outputs）所使用的变量名中唯一。

有关 Simulink 中数据记录的详细信息，请参阅 Save Simulation Data 和 `Simulink.SimulationOutput` 参考页。

**Settings**

**默认值**：sys

Character vector。

**Dependencies**

**Save
data to workspace** 启用此参数。

**命令行信息**

|  |
| --- |
| **Parameter:** `SaveName` |
| **类型**：character vector |
| **Value:** `sys` | any character vector。必须用单引号（`''`）指定。 |
| **默认值**：`'sys'` |

**See Also**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 为每个线性化保存工作点

将线性系统保存到工作区以进行进一步分析或控制设计时，同时保存与每个线性化对应的操作点。使用此选项会向存储已保存线性系统的数据结构中添加一个名为 `operatingPoints` 的字段。

**设置**

**默认值：** Off

On
:   保存操作点。

Off
:   不保存操作点。

**依赖关系**

**Save data to workspace** 启用此参数。

**命令行信息**

|  |
| --- |
| **Parameter:** `SaveOperatingPoint` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Enable assertion

启用模块以检查在仿真期间是否满足 **Bounds** 选项卡中为断言指定并包含的边界。如果不满足某个边界，则断言失败。MATLAB 命令提示符处会出现一条报告断言失败的警告。

如果断言失败，您可以选择指定该模块：

- 执行在 **Simulation callback when assertion fails (optional)** 中指定的 MATLAB 表达式。
- 通过选择 **Stop simulation when assertion fails** 停止仿真并将该模块置于焦点。

对于 Linear Analysis Plots 模块，此参数不起作用，因为默认情况下不包含任何边界。如果要将 Linear Analysis Plots 模块用于断言，请在 **Bounds** 选项卡中指定并包含边界。

清除此参数会禁用断言；也就是说，该模块不再检查是否满足指定的边界。模块图标也会更新以指示断言已禁用。

在 Simulink 模型中，在 Configuration Parameters 对话框中，**Model Verification block enabling** 参数允许您启用或禁用模型中的所有模型验证模块，而不管模块中此选项的设置如何。

**设置**

**默认值：** On

On
:   检查在仿真期间是否满足 **Bounds** 选项卡中为断言包含的边界。如果违反边界，MATLAB 命令提示符处会显示一条报告断言失败的警告。

Off
:   不检查在仿真期间是否满足为断言包含的边界。

**依赖关系**

此参数启用：

- **断言失败时的仿真回调（可选）**
- **断言失败时停止仿真**

**命令行信息**

|  |
| --- |
| **Parameter:** `enabled` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'on'` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 断言失败时的仿真回调（可选）

断言失败时要执行的 MATLAB 表达式。

由于该表达式在 MATLAB 工作区中求值，请在该工作区中定义表达式中使用的所有变量。

**设置**

**无默认值**

一个 MATLAB 表达式。

**依赖关系**

**Enable assertion** 启用此参数。

**命令行信息**

|  |
| --- |
| **Parameter:** `callback` |
| **类型**：character vector |
| **Value:** `''` | MATLAB expression |
| **默认值**：`''` |

**另请参阅**

在仿真期间绘制 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 断言失败时停止仿真

当仿真过程中违反 **Bounds** 选项卡中指定的边界时（即断言失败），停止仿真。

如果从 Simulink Editor 运行仿真，将打开 Simulation Diagnostics 窗口以显示错误消息。同时，模型中发生边界违反的模块会被高亮显示。

**设置**

**默认：** Off

On
:   如果违反 **Bounds** 选项卡中指定的边界，则停止仿真。

Off
:   如果违反边界，则在 MATLAB 命令提示符处显示警告消息并继续仿真。

**提示**

- 由于选择此选项会在断言失败时立即停止仿真，因此仿真后期可能发生的断言失败不会被报告。如果您希望报告*所有*断言失败，请不要选择此选项。

**依赖关系**

**Enable assertion** 启用此参数。

**命令行信息**

|  |
| --- |
| **Parameter:** `stopWhenAssertionFail` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 输出断言信号

输出一个布尔信号，在每个时间步为：

- 如果断言成功，即所有边界均满足，则为 True（`1`）
- 如果断言失败，即违反边界，则为 False（`1`）。

仅当在 Simulink 模型中，在 Configuration Parameters 对话框中选择 **Implement
logic signals as Boolean data** 参数时，输出信号数据类型才为 Boolean。否则，输出信号的数据类型为 double。

选择此参数会向模块添加一个输出端口，您可以将其连接到模型中的任何模块。

**设置**

**默认：**Off

On
:   输出布尔信号以指示断言状态。向模块添加一个端口。

Off
:   不输出布尔信号以指示断言状态。

**提示**

- 使用此参数设计复杂的断言逻辑。有关示例，请参阅 Verify Model Using Simulink Control Design and Simulink Verification Blocks。

**命令行信息**

|  |
| --- |
| **Parameter:** `export` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### 模块打开时显示绘图

当您在 Simulink 模型中双击该模块时，打开绘图窗口而不是 Block Parameters 对话框。

如果您希望在绘图窗口中打开并执行任务（例如添加或修改边界），而不是在 Block Parameters 对话框中，请使用此参数。如果您想从绘图窗口访问模块参数，请选择 **Edit** 或点击 。

有关绘图的更多信息，请参阅 Show Plot。

**设置**

**默认：** Off

On
:   双击模块时打开绘图窗口。

Off
:   双击模块时打开 Block Parameters 对话框。

**命令行信息**

|  |
| --- |
| **Parameter:** `LaunchViewOnOpen` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

**另请参阅**

Plot
仿真期间 Simulink 模型的线性特性

在默认仿真快照时间验证模型

### Show Plot

打开绘图窗口。

使用绘图查看：

- 仿真期间计算的系统特性和信号

  必须在仿真模型之前点击此按钮，才能查看系统特性或信号。

  可以通过右键点击绘图并选择 **Characteristics** 来显示其他特性，例如峰值响应时间。
- 边界

  可以在 Block Parameters 对话框的 **Bounds** 选项卡中指定边界，或右键点击绘图并选择 **Bounds** > **New Bound**。有关可以指定的边界类型的详细信息，请参阅各个参考页。

  可以通过拖动边界段或右键点击绘图并选择 **Bounds** > **Edit Bound** 来修改边界。在仿真模型之前，点击 **Update Block** 以更新模块参数中的边界值。

在绘图窗口中执行的典型任务包括：

- 通过点击 或选择 **Edit** 打开 Block Parameters 对话框。
- 通过点击 或选择 **View** > **Highlight Simulink Block** 查找绘图窗口对应的模块。此操作会使模型窗口处于活动状态并高亮显示该模块。
- 通过点击 仿真模型。此操作还会对指定线性化输入和输出之间的模型部分进行线性化。
- 通过点击 在线性系统特性图上添加图例。

**Note**

要优化模型响应以满足 **Bounds** 选项卡中指定的设计要求，请在绘图窗口中选择 **Tools** > **Response Optimization** 打开 Response Optimizer。仅当安装了 Simulink
Design Optimization™ 软件时，此选项才可用。

### Response Optimization

打开 Response Optimizer，以优化模型响应以满足 **Bounds** 选项卡中指定的设计要求。

仅当安装了 Simulink
Design Optimization 软件时，此按钮才可用。

**See Also**

- Design Optimization to Meet Step Response Requirements (GUI) (Simulink Design Optimization)
- Design Optimization to Meet Time-Domain and Frequency-Domain Requirements (GUI) (Simulink Design Optimization)
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

## 描述

从非线性 Simulink 模型近似的线性系统的奇异值图

此模块与 Check Singular Value Characteristics 模块相同，只是 **Bounds** 选项卡中的默认参数设置不同。

从非线性 Simulink 模型计算线性系统，并在奇异值图上绘制该线性系统。

在仿真期间，软件对模型中指定的线性化输入和输出之间的部分进行线性化，并绘制该线性系统的奇异值。

Simulink 模型可以是连续时间、离散时间或多速率模型，并且可以具有时间延迟。线性系统可以是单输入单输出（SISO）或多输入多输出（MIMO）。对于 MIMO 系统，该模块显示所有输入/输出组合的图。

您可以指定分段线性、频率相关的奇异值上下界，并在图上查看它们。您还可以在仿真期间检查这些界是否满足：

- 如果所有界均满足，该模块不执行任何操作。
- 如果某个界未满足，该模块将断言，并且 MATLAB® 命令窗口中出现警告消息。您还可以指定该模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并将该模块置于焦点。

在仿真期间，该模块还可以输出逻辑断言信号。

- 如果所有界均满足，该信号为 true（`1`）。
- 如果任何界未满足，该信号为 false（`0`）。

对于 MIMO 系统，这些界适用于针对所有输入/输出组合计算的线性系统的奇异值。

您可以添加多个 Singular Value Plot 模块，以计算并绘制模型各个部分的奇异值。

您可以将线性系统保存为 MATLAB 工作区中的变量。

该模块不支持代码生成，并且只能在 `Normal` 仿真模式下使用。
