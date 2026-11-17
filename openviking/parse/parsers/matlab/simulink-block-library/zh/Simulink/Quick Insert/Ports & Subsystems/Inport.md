---
type: simulink-block
title: 'Inport'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Commonly Used Blocks'
documentation_page: 'inport'
documentation_source_path: 'slref/inport.html'
language: zh-CN
chinese_source: worker-translation
---

# Inport

## 端口

### 输出

### **Port\_1** — 输入信号 标量 | 向量

通过输入端口流入系统的输入信号。

您可以在子系统内使用 Inport 模块以结构体或任何其他格式提供定点数据。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## 参数

### 主要

### **端口号** — 端口在父模块上的位置 `1`（默认）| 实数整数

指定与该模块对应的端口在父子系统或模型模块上出现的顺序。

- 如果添加一个创建另一个端口的模块，端口号将是下一个可用的编号。
- 删除与某个端口关联的所有模块会删除该端口。其他端口将重新编号，使其连续且不跳过任何编号。
- 指定一个超过端口数量的端口号将为该编号以及任何被跳过的连续编号创建端口。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `"1"`（默认）| 带引号的实数整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Subsystem1/PortBlock",Port="5")`

### **图标显示** — 图标显示 `端口号`（默认）| `信号名称` | `端口号和信号名称`

指定模块图标上显示的信息。

#### 编程使用

|  |
| --- |
| **模块参数：** `IconDisplay` |
| **类型：** 字符向量 |
| **值：** `'Signal name'` | `'Port number'` | `'Port number and signal name'` |
| **默认：** `'Port number'` |

### **通过延迟外部信号锁存输入** — 通过延迟锁存信号的选项 `off`（默认）| `on`

选择此项以指定模块输出为上一时间步的输入信号值。

选择此选项使软件能够解决作为循环一部分的触发子系统之间的数据依赖关系。

Inport 模块通过显示 `<Lo>` 来指示已选择此选项。

#### 依赖关系

仅当模块表示触发子系统中的输入端口时，此参数才启用。

#### 编程使用

|  |
| --- |
| **模块参数：** `LatchByDelayingOutsideSignal` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认：** `'off'` |

### **为函数调用子系统输出的反馈信号锁存输入** — 锁存信号以防止变化 `off`（默认）| `on`

选择此项以指定模块锁存输入值并防止其在函数调用子系统执行期间发生变化。对于分支以调用多个函数调用子系统的单个函数调用，此选项可打破当一个信号从一个函数调用子系统反馈到另一个函数调用子系统时形成的循环。选择此选项可防止在包含此模块的子系统执行期间被调用的函数调用子系统的反馈信号值发生任何变化。

Inport 模块通过显示 `<Li>` 来指示已选择此选项。

#### 依赖关系

仅当模块表示函数调用子系统中的输入端口时，此选项才启用。

#### 编程使用

|  |
| --- |
| **模块参数：** `LatchInputForFeedbackSignals` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认：** `'off'` |

### **连接输入** — 打开根 Inport 映射器工具的选项按钮

要导入、可视化和将信号及总线数据映射到根级 Inport 模块，请单击此按钮。将打开根 Inport 映射器工具。

#### 依赖关系

仅当模块位于模型的根级别时，此按钮才出现。

### 信号属性

### **输出函数调用** — 产生函数调用事件的选项 `off`（默认）| `on`

指定输入信号产生函数调用事件信号。

如果当前模型在被顶层模型引用时必须接受函数调用事件信号，请选择此选项。

#### 依赖关系

- 要启用此选项，模块必须位于异步函数调用中。
- 当 **数据类型** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。

#### 编程使用

|  |
| --- |
| **模块参数**： `OutputFunctionCall` |
| **类型**： 字符向量 |
| **值**： `'off'` | `'on'` |
| **默认**： `'off'` |

### **最小值** — 最小输出值 `[]`（默认）| 标量

软件检查的输出范围的下限值。

此数字必须是有限实数双精度标量值。

软件使用此值来执行：

- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 依赖关系

当 **数据类型** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最小值。

#### 编程使用

|  |
| --- |
| **模块参数**： `OutMin` |
| **类型**： 字符向量 |
| **值**： `'[ ]'`| 标量 |
| **默认**： `'[ ]'` |

### **最大值** — 最大输出值 `[]`（默认）| 标量

软件检查的输出范围的上限值。

此数字必须是有限实数双精度标量值。

软件使用此值来执行：

- 仿真范围检查（请参阅指定信号范围）。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 依赖关系

当 **数据类型** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的最大值。

#### 编程使用

|  |
| --- |
| **模块参数**： `OutMax` |
| **类型**： 字符向量 |
| **值**： `'[ ]'`| 标量 |
| **默认**： `'[ ]'` |

### **数据类型** — 输出数据类型 `Inherit: auto`（默认）| `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | ...

指定外部输入的输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请单击“显示数据类型助手”按钮。有关详细信息，请参阅使用数据类型助手指定数据类型。

您可以指定以下任一选项：

- 继承数据类型
- 内置 Simulink® 数据类型 — 例如，指定 `single` 或 `uint8`。请参阅 Simulink 支持的数据类型。
- 定点数据类型 — 使用 `fixdt` 函数。例如，指定 `fixdt(1,16,0)`。
- 枚举数据类型 — 使用类型名称并在前面加上 `Enum:`。例如，指定 `Enum: myEnumType`。
- 总线数据类型 — 使用 `Simulink.Bus` 对象的名称并在前面加上 `Bus:`。例如，指定 `Bus: myBusObject`。
- Simulink 图像数据类型 — 如果您有 Computer Vision Toolbox™，请使用 `Simulink.ImageType` (Computer Vision Toolbox) 对象的构造函数并指定描述图像的属性。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式，分别表示图像的行、列和通道。
- 值类型 — 使用 `Simulink.ValueType` 对象的名称并在前面加上 `ValueType:`。例如，指定 `ValueType: windVelocity`。
- 自定义数据类型 — 使用指定类型的 MATLAB® 表达式。例如，您可以指定一个 `Simulink.NumericType` 对象，其 `DataTypeMode` 属性设置为 `'Fixed-point: unspecified scaling'` 以外的值。

当您指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象作为数据类型时，Inport 模块的某些参数将被忽略。例如，Inport 模块的 **Min**、**Max** 和 **Unit** 参数将被忽略。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象的相应属性。例如，假设某个模块将 **Unit** 设置为 `ft/s`。当该模块的 **数据类型** 指定一个单位为 `m/s` 的 `ValueType` 对象时，该模块将使用 `m/s` 而不是 `ft/s`。

#### 编程使用

|  |
| --- |
| **模块参数**： `OutDataTypeStr` |
| **类型**： 字符向量 |
| **值**： `'Inherit: auto'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'string'` | `'Enum: <class name>'` | `'Bus: <object name>'` | `'ValueType: <object name>'` | `'<data type expression>'` | `Simulink.ImageType(480,640,3)` |
| **默认**： `'Inherit: auto'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型的选项 `off`（默认）| `on`

选择此参数以防止定点工具覆盖您在模块上指定的输出数据类型。有关详细信息，请参阅使用锁定输出数据类型设置 (Fixed-Point Designer)。

#### 依赖关系

当 **数据类型** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。

#### 编程使用

|  |
| --- |
| **模块参数**： `LockScale` |
| **值**： `'off'` | `'on'` |
| **默认**： `'off'` |

### **输出为非虚拟总线** — 指定总线输出虚拟性的选项 `off`（默认）| `on`

指定用于加载总线数据的顶层 Inport 模块的输出是虚拟的还是非虚拟的。

- 选择此参数以指定非虚拟总线输出。
- 清除此参数以指定虚拟总线输出。

#### 提示

- 非虚拟总线中的所有信号必须具有相同的采样时间，即使关联的总线对象为某些元素指定了继承采样时间。任何会导致非虚拟总线包含不同采样率信号的操作都会生成错误。您无法为非虚拟总线加载多速率数据。有关如何将具有不同采样率的信号作为非虚拟总线传入被引用模型的详细信息，请参阅修改非虚拟总线的采样时间。

  要为总线加载多速率数据，请清除 **输出为非虚拟总线** 参数，并将 **采样时间** 参数设置为继承（`-1`）。
- 对于模型引用层次结构中的顶层模型，代码生成会创建一个 C 结构体来表示非虚拟总线输出。
- 对于被引用模型，选择此选项以在生成的代码中创建 C 结构体。否则，代码生成会为总线的每个叶元素创建一个参数。

#### 依赖关系

要启用此参数：

- 模块必须位于模型的顶层。
- **数据类型** 模块参数必须解析为 `Simulink.Bus` 对象。例如，将 **数据类型** 设置为 `Simulink.Bus` 对象或将其数据类型指定为 `Simulink.Bus` 对象的 `Simulink.ValueType` 对象。

#### 编程使用

|  |
| --- |
| **模块参数**： `BusOutputAsStruct` |
| **类型**： 字符向量 |
| **值**： `'off'` | `'on'` |
| **默认**： `'off'` |

### **单位（例如 m、m/s^2、N\*m）** — 模块输入信号的物理单位 `inherit`（默认）| `<输入单位>`

指定模块输入信号的物理单位。要指定单位，请在文本框中开始输入。输入时，参数会显示可能匹配的单位。有关支持的单位列表，请使用 `showunitslist` 函数。

要约束单位系统，请单击参数右侧的链接：

- 如果组件中存在单位系统配置模块，将打开其对话框。使用该对话框指定组件允许和不允许的单位系统。
- 如果组件中不存在单位系统配置模块，将显示模型配置参数对话框。使用该对话框指定模型允许和不允许的单位系统。

#### 依赖关系

当 **数据类型** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的单位。

#### 编程使用

|  |
| --- |
| **模块参数：** `Unit` |
| **类型：** 字符向量 |
| **值：** `'inherit'` | `'<Enter unit>'` |
| **默认：** `'inherit'` |

要在不传播的情况下指定模块输入信号的物理单位，请使用 `UnitNoProp`。

### **端口维度（-1 表示继承）** — 端口维度 `-1`（默认）| 整数 | [整数 整数]

指定输出信号的维度。

|  |  |
| --- | --- |
| `-1` | 端口可以加载任意维度信号的数据。端口从连接的信号继承维度。 |
| `N` | 端口可以加载大小为 `N` 的向量信号的数据。 |
| `[R C]` | 端口可以加载具有 `R` 行和 `C` 列的矩阵信号的数据。 |

#### 依赖关系

当 **数据类型** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度。

#### 编程使用

|  |
| --- |
| **模块参数**： `PortDimensions` |
| **类型**： 字符向量 |
| **值**： `'-1'` | 整数 | [整数 整数] |
| **默认**： `'-1'` |

### **可变大小信号** — 允许或不允许可变大小信号的选项 `Inherit`（默认）| `No` | `Yes`

指定此端口允许的信号类型。要允许可变大小和固定大小信号，请选择 `Inherit`。要仅允许可变大小信号，请选择 `Yes`。要仅允许固定大小信号，请选择 `No`。

当此端口上的信号为可变大小信号时，**端口维度** 参数指定信号的最大维度。

#### 依赖关系

当 **数据类型** 指定 `Simulink.ValueType` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象指定的维度模式。

#### 编程使用

|  |
| --- |
| **参数：** `VarSizeSig` |
| **类型：** 字符向量 |
| **值：** `'Inherit'` | `'No'` | `'Yes'` |
| **默认：** `'Inherit'` |

### **信号类型** — 输出信号类型 `auto`（默认）| `real` | `complex`

指定信号输出的复数性。要从连接到其输入的信号继承复数性，请选择 `auto`。否则，请选择实数或复数信号类型。

#### 依赖关系

当 **数据类型** 指定 `Simulink.ValueType` 或 `Simulink.Bus` 对象时，软件忽略此参数的值。软件改用 `Simulink.ValueType` 对象或 `Simulink.Bus` 对象中的 `Simulink.BusElement` 对象指定的复数性。

#### 编程使用

|  |
| --- |
| **模块参数：** `SignalType` |
| **类型：** 字符向量 |
| **值：** `'auto'` | `'real'` | `'complex'` |
| **默认：** `'auto'` |

### 执行

### **Sample time (-1 for inherited)** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅采样时间类型。

默认情况下，该模块根据其在模型中的上下文继承采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'-1'` |

### **Interpolate data** — 用于对输出数据进行线性插值的选项 `on`（默认）| `off`

当从工作区将数据加载到根级 Inport 模块时，指定该模块是否对不存在对应数据的时间步处的输出值进行线性插值和外插。

要从工作区加载离散数据：

1. 将 **Sample time** 设置为离散速率，例如 `2`。
2. 清除 **Interpolate data**。

有关更多信息，请参阅控制模型如何加载输入数据。

软件使用以下插值和外插：

- 对于第一个指定数据点和最后一个指定数据点之间的时间步——零阶保持。
- 对于第一个指定数据点之前和最后一个指定数据点之后的时间步——接地值。
- 对于可变大小信号，在第一个指定数据点之前的时间步——对于 single 或 double 数据类型记录 `NaN` 值，对于其他数据类型使用接地值。对于最后一个指定数据点之后的时间步，软件使用接地值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Interpolate` |
| **类型**：character vector |
| **值**：`'on' | 'off'` |
| **默认值**：`'on'` |

### **Events** — 用于基于流入端口的数据流触发模型分区的选项 事件触发对象的元胞数组

*自 R2022b 起*

**Events** 参数存储与端口关联的事件触发器。*事件触发器* 创建调度事件，以基于模型中特定位置的运行时活动来执行模型中的一个或多个分区。模型的调度指定响应调度事件而执行的分区以及执行优先级。要配置模型的调度，请使用 Schedule Editor。

基于速率的模型中的根级输入端口支持三种类型的事件触发器，它们响应与流入端口的数据流相关的*输入事件*而创建调度事件。您可以为每个输入事件配置一个带有一个事件触发器的输入端口。

| Input Event | Input Event Description | Event Trigger Object |
| --- | --- | --- |
| Input write | 每次输入端口值更新时发生一次 *input write* 事件。 | `simulink.event.InputWrite` |
| Input write timeout | 每次输入端口值在指定时间内未更新时发生一次 *input write timeout* 事件。 | `simulink.event.InputWriteTimeout` |
| Input write lost | 每次新的输入端口值覆盖未处理的数据时发生一次 *input write lost* 事件。 | `simulink.event.InputWriteLost` |

#### 依赖关系

仅当该模块表示基于速率的模型中的根级输入端口时，此参数才可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`EventTriggers` |
| **值**：`1`-by-`1` cell array | `2`-by-`1` cell array | `3`-by-`1` cell array |
| **默认值**：`[]` |

## 所属库

Simulink / Commonly Used Blocks Simulink / Ports & Subsystems Simulink / Sources HDL Coder / Commonly Used Blocks HDL Coder / Ports & Subsystems HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL Architecture**

此模块具有一个默认 HDL 架构。

**HDL Block Properties**

| General | |
| --- | --- |
| **BalanceDelays** | | **BalanceDelays** Setting | Description | | --- | --- | | `on` (default) | 检测 DUT 中其他路径上延迟的引入，并在 Inport 模块路径上插入匹配的延迟。 | | `off` | 禁用 DUT 子系统中输入端口上的延迟平衡，以防止 HDL Coder 在不必要时插入匹配的延迟。例如，如果 DUT 子系统中的 Inport 模块位于具有稳定输入的路径上（即输入端口处的输入信号是 DUT 外部的稳定输入信号），则在该 Inport 模块上禁用 **BalanceDelays**。 |  **Note**  此属性仅影响 DUT 级 Inport 模块。 |
| **BidirectionalPort** | | **BidirectionalPort** Setting | Description | | --- | --- | | `on` | 将端口指定为双向。 以下要求适用：  - 端口必须位于具有黑盒实现的 Subsystem 模块中。 - 双向端口与对应的顶层 DUT 子系统端口之间也不得有逻辑。  有关更多信息，请参阅 Specify Bidirectional Ports (HDL Coder)。 | | `off` (default) | 不将端口指定为双向。 | |

| Target Specification | |
| --- | --- |
| **IOInterface** | DUT 端口的目标平台接口类型，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterface` 模块属性将被忽略。  要指定有效的 `IOInterface` 设置，请使用 HDL Workflow Advisor：  1. 在 HDL Workflow Advisor 中，在 **Set Target** > **Set Target Interface** 步骤中，在 **Target platform interface table** 中，在 **Target Platform Interfaces** 列中，使用下拉列表设置目标平台接口类型。 2. 保存模型。  `IOInterface` 值将保存为端口的 HDL 模块属性。  例如，要查看 `IOInterface` 值，如果 DUT 端口的完整路径为 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED', 'IOInterface')    ``` |
| **IOInterfaceMapping** | DUT 端口的目标平台接口端口映射，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceMapping` 模块属性将被忽略。  要指定有效的 `IOInterfaceMapping` 设置，请使用 HDL Workflow Advisor：  1. 在 HDL Workflow Advisor 中，在 **Set Target** > **Set Target Interface** 步骤中，在 **Target platform interface table** 中，在 **Target Platform Interfaces** 列中，使用下拉列表设置目标平台接口类型。 2. 在 **Bit Range / Address / FPGA Pin** 列中，如果要更改默认值，请输入目标平台接口映射。 3. 保存模型。  `IOInterfaceMapping` 值将保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceMapping` 值，如果 DUT 端口的完整路径为 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceMapping')    ``` |
| **IOInterfaceOptions** | DUT 端口的目标平台接口端口映射选项，指定为字符向量。对于不是 DUT 端口的 Inport 和 Outport 模块，`IOInterfaceOptions` 模块属性将被忽略。  要指定有效的 `IOInterfaceOptions` 设置，请使用 HDL Workflow Advisor：  1. 在 HDL Workflow Advisor 中，在 **Set Target** > **Set Target Interface** 步骤中，在 **Target platform interface table** 中，在 **Target Platform Interfaces** 列中，将输入或输出端口映射到 AXI4 从属接口。 2. 在 **Interface Options** 列中，如果要更改默认初始值，请单击 **Options** 按钮并为 **RegisterInitialValue** 输入一个值。 3. 保存模型。  `IOInterfaceOptions` 值将保存为端口的 HDL 模块属性。  例如，要查看 `IOInterfaceOptions` 值，如果 DUT 端口的完整路径为 `hdlcoder_led_blinking/led_counter/LED`，请输入：  ```    hdlget_param('hdlcoder_led_blinking/led_counter/LED',...                 'IOInterfaceOptions')    ``` |

| Frame to Sample Conversion | |
| --- | --- |
| **ConvertToSamples** | | **ConvertToSamples** Setting | Description | | --- | --- | | `on` | 通过使用帧到样本转换优化，将传入的矩阵输入信号转换为样本。 要使用此属性，请启用模型配置参数 **Enable frame to sample conversion**。有关更多信息，请参阅 Enable frame to sample conversion (HDL Coder)。 | | `off` (default) | 不将传入的矩阵输入信号转换为样本。 | |

**`Simulink.ValueType` Object Support**

此模块支持 `Simulink.ValueType` 对象的代码生成。有关值类型的更多信息，请参阅 Specify Common Set of Signal Properties as Value Type。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

为子系统或外部输入创建输入端口

Inport 模块将来自系统外部的信号链接到系统中。

软件根据以下规则分配 Inport 模块端口号：

- 顶层系统或子系统中的 Inport 模块从 1 开始按顺序编号。
- 如果添加 Inport 模块，其标签为下一个可用编号。
- 如果删除 Inport 模块，其他端口号将重新编号，以确保 Inport 模块按顺序排列且不省略任何编号。
- 如果将 Inport 模块复制到系统中，除非其当前编号与系统中已有的输入端口冲突，否则其端口号不会重新编号。如果复制的 Inport 模块的端口号不连续，请对该模块重新编号。否则，在仿真模型或更新模块图时会出现错误消息。

### Inport Blocks in Top-Level Systems

您可以使用顶层系统中的 Inport 模块来：

- 使用 **Input** 参数从工作区提供外部输入。如果未提供外部输入数据，Inport 模块的输出为接地值。有关更多信息，请参阅 Load Data to Root-Level Input Ports。

  - 要使用根级输入端口为多个信号加载数据，请考虑使用 Root Inport Mapper 工具。请参阅 Map Data Using Root Inport Mapper Tool。
  - 使用 `createInputDataset` 函数创建一个 `Simulink.SimulationData.Dataset` 对象，该对象包含您指定模型中每个根级 Inport 模块对应的元素。
- 为 `linmod` 和 `trim` 分析函数提供模型扰动的手段。有关更多信息，请参阅 Linearizing Models。

### Inport Blocks in Subsystems

子系统中的 Inport 模块表示子系统的输入。到达 Subsystem 模块输入端口上的信号从该子系统中关联的 Inport 模块流出。与 Subsystem 模块上输入端口关联的 Inport 模块是其 **Port number** 参数与 Subsystem 模块上输入端口的相对位置匹配的模块。例如，**Port number** 参数为 `1` 的 Inport 模块从连接到 Subsystem 模块最顶部端口的模块获取其信号。

如果重新编号 Inport 模块的 **Port number**，该模块将连接到不同的输入端口。该模块继续从子系统外部的同一模块接收其信号。

子系统内部的 Inport 模块支持信号标签传播，但根级 Inport 模块不支持。有关更多信息，请参阅 Signal Label Propagation。

您可以直接编辑 Subsystem 模块上的端口标签。有关更多信息，请参阅 Edit Port Labels on Subsystem Blocks。

**Tip**

对于包含由许多总线元素组成的总线的模型，请考虑使用 In Bus Element 和 Out Bus Element 模块。这些模块：

- 减少模块图中的信号线复杂度和杂乱。
- 使增量更改接口更加容易。
- 允许在更接近使用点的地方访问总线元素，避免使用 Bus Selector 和 Goto 模块配置。

In Bus Element 模块的模块类型为 Inport，Out Bus Element 模块的模块类型为 Outport。

### Create Duplicate Inport Blocks

您可以创建任意数量的 Inport 模块副本。副本是原始模块的图形表示，旨在通过消除不必要的线条来简化模块图。副本具有与原始模块相同的端口号、属性和输出。

要创建 Inport 模块的副本：

1. 在模块图中，选择要复制的未连接的 Inport 模块。
2. 按住 **Ctrl** 键并拖动该模块。
3. 释放指针，然后从上下文菜单中选择 **Duplicate**。

您可以选择具有副本的 Inport 模块以高亮显示副本模块。要在打开的图或新选项卡中显示相关模块，请将光标暂停在选中后出现的省略号上。然后，从操作菜单中选择 **Related Blocks**。当多个模块对应于所选模块时，将打开相关模块列表。您可以通过在文本框中输入搜索词来筛选相关模块列表。从列表中选择相关模块后，窗口焦点将转到显示该相关模块的打开的图或新选项卡。

### Connect Buses to Root-Level Inport Blocks

如果希望模型的根级 Inport 模块产生总线，请将 **Data type** 参数设置为定义该 Inport 模块所产生总线的总线对象名称。有关更多信息，请参阅 Specify Bus Properties with Bus Objects。
