---
type: simulink-block
title: 'Change Operating Points'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'changeoperatingpoints'
documentation_source_path: 'ug/changeoperatingpoints.html'
language: zh-CN
chinese_source: worker-translation
---

# Change Operating Points

## 端口

### 输入

### **systeminputs\_in** — 系统输入数组

指定工作点处输入电平的值。

当模块在快照模式下运行时，模块会直接将此输入传递到 **systeminputs\_out** 端口。

### **enable/disable** — 启用和禁用更改工作点 标量

指定一个信号以启用（`1`）或禁用（`0`）模块操作。

### **autotuning times** — 启动自整定的时间向量 向量

指定启动自整定的时间向量。该向量每个索引处的值是该索引对应工作点的自整定启动时间。使用 **Autotuning time span (sec)** 参数指定实验的持续时间。

#### 依赖关系

要启用此端口，请使用此配置。

- 将 **Operating mode** 设置为 `Import operating points`。
- 选中 **Use block for autotuning**。
- 将 **Method for starting autotuning** 设置为 `External time vector`。

### **next OP** — 下一个工作点 标量

指定切换到下一个工作点的自定义逻辑。

#### 依赖关系

要启用此端口，请使用此配置。

- 将 **Operating mode** 设置为 `Import operating points`。
- 将 **Transition method** 设置为 `External trigger`。

### **y** — 被控对象输出 标量 | 向量

将被控对象的输出连接到此端口。模块使用此信号确定系统的当前工作状态。

#### 依赖关系

要启用此端口，请使用此配置。

- 将 **Operating mode** 设置为 `Import operating points`。
- 选中 **Use block for autotuning**。
- 将 **Method for starting autotuning** 设置为 `Time after reaching steady-state`。

### **enable autotuning** — 启用或禁用自整定 标量

使用此端口手动指定一个标量标志以启用（`1`）或禁用（`0`）自整定过程。

#### 依赖关系

要启用此端口，请使用此配置。

- 将 **Operating mode** 设置为 `Import operating points`。
- 选中 **Use block for autotuning** 和 **Add enable/disable port for autotuning**。

### **snapshot trigger** — 快照触发器 向量

指定基于时间或基于事件的快照触发器，您希望在这些触发点提取模型的工作点。

当 **Snapshot mode** 为 **Time-based** 时，指定您希望快照工作点数据的时间值。例如，要在 3、5 和 7 秒时进行快照，请使用向量 `[3,5,7]` 作为此端口的输入。

当 **Snapshot mode** 为 **Event-based** 时，模块在输入信号的上升沿对工作点数据进行快照。

#### 依赖关系

要启用此端口，请将 **Operating mode** 设置为 `Snapshot operating points`，并使用以下配置之一。

- 将 **Snapshot mode** 设置为 **Time-based** 并选中 **Use external source**。
- 将 **Snapshot mode** 设置为 **Event-based**。
### 输出

### **systeminputs\_out** — 工作点输出总线

用于将系统移动到切换后工作点的参考信号。

### **start\_stop** — 启动和停止自整定的信号 标量

用于通过 Closed-Loop PID Autotuner 模块启动和停止自整定过程的信号。生成的信号取决于附加参数，例如自整定方法和稳态设置。

#### 依赖关系

要启用此端口，请将 **Operating mode** 设置为 `Import operating points` 并选中 **Use block for autotuning**。

## 参数

### Import operating point 选项卡

### **Operating mode** — 用于获取工作点数据的模式 `Import operating points`（默认）| `Snapshot operating points`

指定获取工作点数据的模式。

- `Import operating points` — 通过手动编辑模块对话框中的表格或导入 `OperatingPoint` 对象来指定预定义的工作点数据。

  在此模式下，您可以使用该模块实现简化的工作流程，在运行范围内对增益调度 PID 控制器进行自动整定。
- `Snapshot operating points` — 在仿真过程中于指定时间或事件处快照工作点。

#### 编程使用

|  |
| --- |
| **模块参数**：`OperatingMode` |
| **类型**：string |
| **值**：`"Import operating points"` | `"Snapshot operating points"` |
| **默认值**：`"Import operating points"` |

### **Input method** — 工作点数据的输入方法 **Manually edit table**（默认）| **Automatically fill Table**

指定工作点数据的输入方法。

- **Manually edit table** — 在模块对话框中手动指定工作点数据。
- **Automatically fill table** — 使用 `OperatingPoint` 对象导入工作点数据。通常，您可以使用 `operpoint` 和 `findop` 等函数，或 Steady State Manager 和 Model Linearizer 应用来获取工作点。您也可以导入使用此模块的快照模式获取的工作点数据。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Import operating points`。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputMethod` |
| **类型**：string |
| **值**：`"Manually edit table"` | `"Automatically fill table"` |
| **默认值**：`"Manually Edit Table"` |

### **Number of inputs** — 模型输入的数量 `3`（默认）| 正标量

指定模型中的输入数量。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Import operating points`，并将 **Input method** 设置为 **Manually edit table**。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumSystemInputs` |
| **类型**：string |
| **值**：带引号的正标量 |
| **默认值**：`"3"` |

### **Workspace** — 用于导入工作点数据的工作区 `Base workspace`（默认）| `Model workspace` | `Data dictionary`

指定要从中导入工作点数据的工作区。指定的工作区必须包含与 **Operating point variable** 中的值同名的 `OperatingPoint` 对象。

- `Base workspace` — 从基础 MATLAB® 工作区导入数据。
- `Model workspace` — 从当前模型工作区导入数据。
- `Data dictionary` — 从 Simulink® 数据字典导入数据。

此外，要导入模块在快照模式下生成的工作点数据，请点击 **Save to Workspace** 按钮并指定工作点结构的名称。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Import operating points`，并将 **Input method** 设置为 **Automatically fill table**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ImportWorkspace` |
| **类型**：string |
| **值**：`"Data dictionary"` | `"Base workspace"` | `"Model workspace"` |
| **默认值**：`"Data dictionary"` |

### **Data dictionary name** — 数据字典名称 `myDataDictionary.sldd`（默认）| 字符串

指定要从中读取工作点数据的数据字典的名称。`OperatingPoint` 对象必须存储在字典的 `Other Data` 部分中。有关详细信息，请参阅 What Is a Data Dictionary?。

#### 依赖关系

要启用此参数，请设置以下参数。

- **Operating mode** 设置为 `Import operating points`
- **Input method** 设置为 **Automatically fill table**
- **Workspace** 设置为 `Data dictionary`

#### 编程使用

|  |
| --- |
| **模块参数**：`DataDictionaryName` |
| **类型**：string |
| **默认值**：`"myDataDictionary.sldd"` |

### **Operating point variable** — 工作点变量名称 `myOperatingPoint`（默认）| 字符串

指定工作点变量的名称。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Import operating points`，并将 **Input method** 设置为 **Automatically fill table**。

#### 编程用法

|  |
| --- |
| **模块参数：** `OperatingPointVariable` |
| **类型：** 字符串 |
| **默认值：** `"myOperatingPoint"` |

### **Snapshot mode** — 工作点快照模式 **Time-based**（默认）| **Event-based**

指定用于获取工作点数据的快照模式。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Snapshot operating points`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SnapshotMode` |
| **类型：** 字符串 |
| **值：** `"Time-based"` | `"Event-based"` |
| **默认值：** `"Time-based"` |

### **Snapshot times (sec)** — 仿真快照时间 `[0 1 2]`（默认）| 标量 | 向量

指定用于提取模型工作点的仿真快照时间。使用标量表示单个快照，或使用向量表示多个快照。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Snapshot operating points`，并将 **Snapshot mode** 设置为 **Time-based**。

#### 编程用法

|  |
| --- |
| **模块参数：** `SnapshotTimes` |
| **类型：** 字符串 |
| **值：** 带引号的标量或向量 |
| **默认值：** `"[1 2 3]"` |

### **Use external source** — 使用输入端口获取快照时间 `off`（默认）| `on`

将仿真快照时间指定为模块输入。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Snapshot operating points`，并将 **Snapshot mode** 设置为 **Time-based**。

#### 编程用法

|  |
| --- |
| **模块参数：** `SnapshotTimesExternalSource` |
| **类型：** 字符串 |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Sample time (-1 for inherited)** — 采样时间 `-1`（默认）| 正标量

指定采样时间。

#### 依赖关系

要启用此参数，请将 **Operating mode** 设置为 `Snapshot operating points`，并将 **Snapshot mode** 设置为 **Time-based**。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符串 |
| **值：** 带引号的正标量 | "–1" |
| **默认值：** `"–1"` |

### **Operating point definitions** — 工作点数据 多个表条目

工作点数据，指定为多个表条目。

当 **Input Method** 为 **Manually edit table** 时，使用表的 **Value** 列手动指定工作点的索引、快照时间和输入水平对应的数据。

当 **Input Method** 为 **Automatically fill table** 时，**Value** 会根据导入的工作点显示工作点的值。

要在快照模式下获取数据后填充表的条目，请点击 **Save to Table**。

#### 依赖关系

要为此表的 **Value** 列启用手动数据输入，请将 **Operating mode** 设置为 `Import operating points`，并将 **Input method** 设置为 **Manually edit table**。

#### 编程用法

|  |
| --- |
| **模块参数：** `OperatingPointTable` |
| **类型：** 字符串 |
| **值：** 带引号的元胞数组 |
| **默认值：** `"{'Indicies','[1 2 3]';'Times (sec)','[0 1 2]';'SystemInput_1','[1 1 1]';'SystemInput_2','[2 2 2]';'SystemInput_3','[3 3 3]'}"` |

### **Bus name** — 总线对象名称 `scdPlantOPsBusObject`（默认）| 字符串

为模块创建的 `Simulink.Bus` 对象指定名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `BusName` |
| **类型：** 字符串 |
| **值：** 字符串 |
| **默认值：** `"scdPlantOPsBusObject"` |

### **Specify bus name** — 指定总线名称 `off`（默认）| `on`

手动为对象指定总线名称。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SpecifyBusName` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **数据类型** — 浮点精度 `Double`（默认）| `Single`

根据仿真环境或硬件要求指定浮点精度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BlockDataType` |
| **类型：** string |
| **值：** `"Double"` | `"Single"` |
| **默认值：** `"Double"` |

### 更改工作点设置选项卡

### **使用模块进行自动调优** — 使用模块进行 PID 自动调优工作流 `on`（默认）| `off`

将模块用于增益调度 PID 自动调优工作流。启用此选项时，模块会在 **start\_stop** 输出端口生成信号。使用 **start\_stop** 信号通过 Closed-Loop PID Autotuner 模块启动和停止自动调优过程。生成的信号取决于其他参数，例如自动调优方法和稳态设置。

#### 依赖关系

要启用此参数，请将 **操作模式** 设置为 `Import operating points`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `UseAutotuning` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"on"` |

### **启动自动调优的方法** — 启动自动调优的方法 `External time vector`（默认）| `Time after reaching steady-state`

指定启动 PID 自动调优的方法。

- `External time vector` — 使用 **autotuning times** 输入端口指定时间向量。该向量每个索引处的值是该索引对应工作点的自动调优启动时间。使用 **自动调优时间跨度（秒）** 参数指定实验持续时间。
- `Time after reaching steady-state` — 当模型输出达到稳态时启动自动调优。使用 **稳定时间上界**、**稳定时间下界** 和 **稳定时间间隔** 参数定义每个工作点的稳态判据。

#### 依赖关系

要启用此参数，请将 **操作模式** 设置为 `Import operating points` 并选择 **使用模块进行自动调优**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AutotuningTriggerMethod` |
| **类型：** string |
| **值：** `"External time vector"` | `"Time after reaching steady-state"` |
| **默认值：** `"External time vector"` |

### **为自动调优添加使能/禁用端口** — 为自动调优添加使能/禁用端口 `off`（默认）| `on`

向模块添加 **enable autotuning** 输入端口。使用此端口手动指定标量标志以启用（`1`）或禁用（`0`）自动调优过程。

#### 依赖关系

要启用此参数，请将 **操作模式** 设置为 `Import operating points` 并选择 **使用模块进行自动调优**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AddEnableDisableAutotuning` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"on"` |

### **自动调优时间跨度（秒）** — 自动调优实验持续时间 `10`（默认）| 正标量 | 向量

指定自动调优实验的持续时间。必须让实验运行足够长的时间，以便算法收集足够的数据来良好估计被控对象频率响应。实验运行时间不足可能导致结果不准确。有关详细信息，请参阅 Closed-Loop PID Autotuner 模块的 **start/stop** 输入端口。

- 要对所有工作点以相同持续时间运行自动调优实验，请指定一个正标量值。
- 要对每个工作点以不同持续时间运行实验，请指定一个正值向量。每个持续时间值对应于该向量该索引处的工作点。

#### 依赖关系

要启用此参数，请将 **操作模式** 设置为 `Import operating points` 并选择 **使用模块进行自动调优**。

#### 编程用法

|  |
| --- |
| **模块参数：** `AutotuningExperimentLength` |
| **类型：** string |
| **值：** 带引号的正标量或向量 |
| **默认值：** `"10"` |

### **达到稳态后开始自整定的采样数** — 延迟开始自整定 `2`（默认）| 正标量

指定在模型达到稳态后，模块延迟开始自整定过程的采样数。

#### 依赖关系

要启用此参数，请使用此配置。

- 将 **Operating mode** 设置为
  `Import operating
  points`。
- 选中 **Use block for
  autotuning**。
- 将 **Method for starting autotuning** 设置为
  `Time after reaching
  steady-state`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumAutotuningDelaySamples` |
| **类型：** string |
| **值：** 带引号的正标量 |
| **默认值：** `"2"` |

### **Transition method** — 工作点过渡方法 `Internal time vector (from operating point table)`（默认）| `Time after reaching steady-state` | `Time after completing autotuning` | `External trigger`

指定工作点过渡方法。

- `Internal time vector (from operating point
  table)` — 根据工作点数据的时间向量中的值更改工作点。
- `Time after reaching steady-state` —
  在模型输出达到为该工作点定义的稳态条件后更改工作点。
- `Time after completing autotuning` —
  在该工作点的自整定时间跨度过去后更改工作点。
- `External trigger` — 根据在 **next
  OP** 模块输入端口处指定的自定义逻辑更改工作点。

#### 依赖关系

要启用此参数，请将 **Operating mode**
设置为 `Import operating points`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TransitionMethod` |
| **类型：** string |
| **值：** `"Internal time vector (from operating point table)"` | `"Time after reaching steady-state"` | `"Time after completing autotuning"` | `"External trigger"` |
| **默认值：** `"Internal time vector (from operating point table)"` |

### **Change operating point algorithm** — 工作点过渡算法 `Step`（默认）| `Ramp`

指定从一个工作点过渡到另一个工作点的算法。

- `Step` — 使用阶跃信号在两个工作电平之间进行阶跃切换。
- `Ramp` — 使用斜坡信号在两个工作电平之间作为恒定增加或减少的信号进行过渡。

#### 依赖关系

要启用此参数，请将 **Operating mode**
设置为 `Import operating points`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ChangeOPAlgorithm` |
| **类型：** string |
| **值** `"Step"` | `"Ramp"` |
| **默认值：** `"Step"` |

### **Rising slew rate (/sec)** — 输入增加时的导数限值 `1`（默认）| 标量 | 向量

指定输入信号上升速率的限值。

#### 依赖关系

要启用此参数，请将 **Operating mode**
设置为 `Import operating points`，并将
**Change operating point algorithm** 设置为
`Ramp`。

#### 编程用法

|  |
| --- |
| **模块参数：** `RampSlewUpRate` |
| **类型：** string |
| **值：** 带引号的标量或向量 |
| **默认值：** `"1"` |

### **Falling slew rate (/sec)** — 输入减少时的导数限值 `-1`（默认）| 标量 | 向量

指定输入信号下降速率的下限。

#### 依赖关系

要启用此参数，请将 **Operating mode**
设置为 `Import operating points`，并将
**Change operating point algorithm** 设置为
`Ramp`。

#### 编程用法

|  |
| --- |
| **模块参数：** `RampSlewLoRate` |
| **类型：** string |
| **值：** 带引号的标量或向量 |
| **默认值：** `"–1"` |

### **达到稳态后过渡的采样数** — 过渡到工作点的延迟 `2`（默认）| 非负标量

指定在模型达到稳态后，模块延迟过渡到下一个工作点的采样数。

#### 依赖关系

要启用此参数，请将**运行模式**设置为 `Import operating points`，并将**过渡方法**设置为 `Time after reaching steady-state`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumTransitionDelaySamples` |
| **类型：** string |
| **值：** 带引号的非负标量 |
| **默认：** `"2"` |

### **完成自动调优后过渡的采样数** — 过渡到工作点的延迟 `2`（默认）| 非负标量

指定在自动调优实验完成后，模块延迟过渡到下一个工作点的采样数。

#### 依赖关系

要启用此参数，请将**运行模式**设置为 `Import operating points`，并将**过渡方法**设置为 `Time after completing autotuning`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumSamplesAutotuningTranstion` |
| **类型：** string |
| **值：** 带引号的非负标量 |
| **默认：** `"2"` |

### **调节时间上界** — 调节时间的上界 `[1.1 2.1 3.1]`（默认）| 向量

指定用于确定工作点调节时间和稳态的运行值上界。

此向量的每个值对应于该索引处工作点值的上界。

#### 依赖关系

要启用此参数，请将**运行模式**设置为 `Import operating points`，并将**过渡方法**设置为 `Time after reaching steady-state`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTimeUpper` |
| **类型：** string |
| **值：** 带引号的标量或向量 |
| **默认：** `"[1.1 2.1 3.1]"` |

### **调节时间下界** — 调节时间的下界 `[0.9 1.9 2.9]`（默认）| 向量

指定用于确定工作点调节时间和稳态的运行值下界。

此向量的每个值对应于该索引处工作点值的下界。

#### 依赖关系

要启用此参数，请将**运行模式**设置为 `Import operating points`，并将**过渡方法**设置为 `Time after reaching steady-state`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTimeLower` |
| **类型：** string |
| **值：** 带引号的标量或向量 |
| **默认：** `"[0.9 1.9 2.9]"` |

### **调节时间间隔** — 调节时间间隔 `5`（默认）| 标量 | 向量

指定运行条件保持稳态的时间间隔。

使用向量可为不同工作点指定不同的时间间隔。

#### 依赖关系

要启用此参数，请将**运行模式**设置为 `Import operating points`，并将**过渡方法**设置为 `Time after reaching steady-state`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTimeInterval` |
| **类型：** string |
| **值：** 带引号的标量或向量 |
| **默认：** `"5"` |

## 所属库

Simulink Control Design / Autotuning

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Change Operating Points 模块仅在**运行模式**为 `Import operating points` 时支持代码生成。

## 版本历史

**在 R2023b 中引入**

## 描述

在仿真期间切换工作点

Change Operating Points 模块允许您在仿真期间管理和切换工作点。您可以按以下配置之一使用该模块：

- 从工作区导入预定义的工作数据，并在仿真期间在工作范围之间切换。
- 在仿真期间的指定时间或事件自动快照，以获取指定范围内的作点数据。例如，对于电机模型，您可以在以下时刻进行快照：

  - 3、5 和 7 s（基于时间）。
  - 2000、5000 和 8000 rpm（基于事件）。

当您拥有预定义的工作点数据时，可以在增益调度控制器整定工作流中使用此模块。此模块有助于生成参考信号，使您的被控对象从一个工作点移动到另一个工作点。否则，请先对工作点进行快照，然后将数据用于增益调度工作流。

通常，整定增益调度控制器是一个复杂的过程。它需要您在每個工作点运行多次仿真以进行整定，并提供在该工作点存储 PID 增益的逻辑。使用此模块以及 PID Gains Store and Update 和 PID Gain Scheduler 模块，有助于您实现一个简化的流程，在一次运行中在某个工作范围内自动整定增益调度 PID 控制器。为此，请使用此工作流。

1. 使用 Change Operating Points 模块在仿真期间在预定义或快照工作点数据之间切换。
2. 使用 Closed-Loop PID Autotuner 在工作点执行自动整定。
3. 使用 PID Gains Store and Update 模块将对应于该工作点的 PID 增益存储在数组中。
4. 使用 PID Gain Scheduler 模块从数组执行基于查找表的增益调度。

从高层次来看，您可以使用这些模块实现增益调度工作流，如下图所示。

增益调度系统图，包含 Closed-Loop PID Autotuner、PID Controller、Change Operating Points、Gain Scheduler 和 PID Gains Store and Update 模块。
