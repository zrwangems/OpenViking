---
type: simulink-block
title: 'Model'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'model'
documentation_source_path: 'slref/model.html'
language: zh-CN
chinese_source: worker-translation
---

# Model

## 端口

### 输入

### **Port\_1** — 与被引用模型的根级模块对应的输入 标量 | 向量 | 矩阵 | 数组 | 总线

Model 模块为其引用的模型的每个输入端口都有一个输入端口。被引用模型的输入端口由 Inport 和 In Bus Element 模块定义。Model 模块端口的名称与所引用模型中对应端口的名称一致。Model 模块每个端口的输入信号、消息或函数调用必须对所引用模型中的对应端口有效。有关详细信息，请参阅 Define Model Reference Interfaces。

#### 提示

- 被引用模型中的信号属性独立于 Model 模块的上下文。例如，信号维度和数据类型不会跨越 Model 模块边界传播。要在被引用模型中定义信号属性，请为根级 Inport 和 In Bus Element 模块定义模块参数。
- 连接到输入端口的函数调用会传入被引用模型。要基于函数调用有条件地执行被引用模型，请参阅 **Function Call**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持：** 是
### 输出

### **Port\_1** — 与被引用模型的根级模块对应的输出 标量 | 向量 | 矩阵 | 数组 | 总线

Model 模块为其引用的模型的每个输出端口都有一个输出端口。被引用模型的输出端口由 Outport 和 Out Bus Element 模块定义。Model 模块上端口的名称与所引用模型中对应端口的名称一致。Model 模块的输出信号和消息是连接到被引用模型中 Outport 和 Out Bus Element 模块的信号和消息。请参阅 Define Model Reference Interfaces。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持：** 是
### 控制

#### 条件执行

### **Enable** — 启用被引用模型的控制信号 标量 | 向量 | 矩阵

使能端口出现在 Model 模块的顶部。端口标签是表示使能信号的图标。

Model 模块上的使能端口

连接到该端口的控制信号决定何时执行被引用模型。有关详细信息，请参阅 Conditionally Execute Referenced Models。

#### 依赖关系

要启用此端口，请在被引用模型的顶层添加一个 Enable 模块。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Trigger** — 触发被引用模型的控制信号 标量 | 向量 | 矩阵

触发端口出现在 Model 模块的顶部。端口标签是表示触发信号的图标。

Model 模块上的触发端口

连接到该端口的控制信号决定何时执行被引用模型。有关详细信息，请参阅 Conditionally Execute Referenced Models。

#### 依赖关系

要启用此端口，请在被引用模型的顶层添加一个 Trigger 模块，并将其 **Trigger type** 设置为 `rising`、`falling` 或 `either`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Function Call** — 函数调用事件的控制信号 标量

函数调用端口出现在 Model 模块的顶部。端口标签将被引用模型的名称显示为函数。

Model 模块上的函数调用端口

连接到该端口的函数调用控制信号决定何时执行被引用模型。有关详细信息，请参阅 Conditionally Execute Referenced Models。

#### 依赖关系

要启用此端口，请在被引用模型的顶层添加一个 Trigger 模块，并将其 **Trigger type** 设置为 `function-call`。

#### 模型事件仿真

### **initialize** — 模型初始化事件的控制信号 标量

初始化事件端口提供一个函数调用控制信号，用于触发模型初始化事件，从而初始化被引用模型的状态。

被引用模型可以包含与模型初始化事件对应的 Initialize Function 模块。有关详细信息，请参阅 Using Initialize, Reinitialize, Reset, and Terminate Functions。

#### 依赖关系

要启用此端口，请选择 **Show model initialize port**。

### **reset** — 模型重置事件的控制信号 标量

重置事件端口提供一个函数调用控制信号，用于触发模型重置事件，从而重置被引用模型的状态。

被引用模型必须包含与每个模型重置事件对应的 Reset Function 模块。有关详细信息，请参阅 Using Initialize, Reinitialize, Reset, and Terminate Functions。

要指定端口名称，请使用 Reset Function 模块中 Event Listener 模块的 **Event name** 参数。

#### 依赖关系

要启用此类端口，请选择 **Show model reset ports**。

### **reinit** — 模型重新初始化事件的控制信号 标量

重新初始化事件端口提供一个函数调用控制信号，用于触发模型重新初始化事件，从而重新初始化被引用模型的状态。

被引用模型必须包含与每个模型重新初始化事件对应的 Reinitialize Function 模块。有关详细信息，请参阅 Using Initialize, Reinitialize, Reset, and Terminate Functions。

要指定端口名称，请使用 Reinitialize Function 模块中 Event Listener 模块的 **Event name** 参数。

#### 依赖关系

要启用此类端口，请选择 **Show model reinitialize ports**。

### **terminate** — 模型终止事件的控制信号 标量

终止事件端口提供一个函数调用控制信号，用于触发模型终止事件，从而读取并保存被引用模型的状态。

被引用模型可以包含与模型终止事件对应的 Terminate Function 模块。有关详细信息，请参阅 Using Initialize, Reinitialize, Reset, and Terminate Functions。

#### 依赖关系

要启用此端口，请选择 **Show model terminate port**。

### **D** — 调度周期性事件的控制信号 标量

周期性事件端口提供函数调用控制信号，用于指定何时执行模型。有关示例，请参阅 Test Rate-Based Model Simulation Using Function-Call Generators。

每个端口标签显示有关周期性事件的信息，例如对应 Inport 模块的采样时间。例如，此图像中的 Model 模块显示周期性事件端口，并引用一个具有两个离散速率（0.01 和 0.1）的模型。

Model 模块具有标记为 D1[0.01] 和 D2[0.1] 的端口。

#### 依赖关系

要启用此类端口，请将 **Schedule rates with** 设置为 `Ports`。

## 参数

要以交互方式修改 Model 模块参数，请选择 Model 模块。然后，在 Simulink 工具条的 **Model Block** 选项卡上，点击 **Block Parameters**。

### 主要

指定 Model 模块的基本信息。

### **Model name** — 被引用模型的文件名 无默认值

指定被引用模型的文件名。文件名必须是有效的 MATLAB® 模型标识符，如 Choose Valid Model File Names 中所定义。文件扩展名是可选的。

要选择要引用的模型，请点击 **Browse**。要查看指定的模型，请点击 **Open Model**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ModelNameDialog` |
| **值：** | `''`（默认） | 带引号的文件名 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,ModelNameDialog="mymodel.slx")`

要以编程方式获取模块参数值，请使用 `get_param` 函数。

您可以查询不同格式的被引用模型名称：

- `ModelFile` — 带文件扩展名的模型名称。当您未指定文件扩展名时，软件在 MATLAB 路径上找到的第一个匹配项决定文件扩展名。
- `ModelNameDialog` — 带或不带文件扩展名的模型名称，取决于您是否指定了文件扩展名。
- `ModelName` — 不带文件扩展名的模型名称。如果您为 `ModelName` 指定了带文件扩展名的模型名称，软件将通过设置 `ModelNameDialog` 和 `ModelFile` 来保留文件扩展名。

### **Simulation mode** — 模型引用的仿真模式 `Normal`（默认） | `Accelerator` | `Software-in-the-loop (SIL)` | `Processor-in-the-loop (PIL)`

指定 Model 模块的仿真模式。Model 模块的仿真模式可以与其被引用模型以及模型层次结构中其他模型的仿真模式不同。

- `Normal` — 以解释方式执行被引用模型，就像被引用模型是直接在父模型中实现的原子子系统一样。
- `Accelerator` — 为被引用模型创建 MEX 文件。然后，通过运行 S-function 来执行被引用模型。
- `Software-in-the-loop (SIL)` — 此选项需要 Embedded Coder® 许可证。根据 **Code interface** 参数设置生成生产代码。该代码为主机平台编译并执行。
- `Processor-in-the-loop (PIL)` — 此选项需要 Embedded Coder 许可证。根据 **Code Interface** 参数设置生成生产代码。该代码为目标平台编译并执行。目标连接 API 实现支持在 PIL 仿真期间每个时间步在主机和目标之间交换数据。

Model 模块的角指示 Model 模块的仿真模式。对于普通模式，角具有空三角形。对于加速器模式，角三角形被填充。对于 SIL 和 PIL 模式，角被填充，并且模块图标上显示 `(SIL)` 或 `(PIL)` 字样。

尽管您可以为模型指定任何仿真模式，但当您引用该模型时，Model 模块指定被引用模型实例的仿真模式。父模型的仿真模式可以覆盖 Model 模块的仿真模式。

有关详细信息，请参阅 Choose Simulation Modes for Model Hierarchies。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SimulationMode` |
| **值：** | `"Normal"`（默认） | `"Accelerator"` | `"Software-in-the-loop (SIL)"` | `"Processor-in-the-loop (PIL)"` |

**示例：** `set_param(gcb,SimulationMode="Accelerator")`

### **Code interface** — 从顶层模型或被引用模型生成代码的选项 `Model reference`（默认） | `Top model`

指定对于 SIL 和 PIL 仿真模式，是从顶层模型还是从被引用模型生成代码。要将生成的代码作为使用被引用模型的更大应用程序的一部分进行部署，请指定 `Model reference`。要将生成的代码作为独立应用程序进行部署，请指定 `Top model`。

- `Model reference` — 代码从作为模型层次结构一部分的被引用模型生成。代码生成使用类似于此命令的命令，该命令为名为 `ModelName` 的模型生成代码。

  ```
  slbuild("ModelName","ModelReferenceCoderTarget")
  ```
- `Top model` — 代码从具有独立代码接口的顶层模型生成。代码生成使用类似于此命令的命令，该命令为名为 `ModelName` 的模型生成代码。

  ```
  slbuild("ModelName")
  ```

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Software-in-the-loop (SIL)` 或 `Processor-in-the-loop (PIL)`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CodeInterface` |
| **值：** | `"Model reference"`（默认） | `"Top model"` |

**示例：** `set_param(gcb,CodeInterface="Top
model")`

### 模型事件仿真

控制被引用模型何时执行和更改状态。

### **Show model initialize port** — 显示初始化事件端口的选项 `off`（默认） | `on`

选择此参数以显示初始化事件端口。清除此参数以移除该端口。

#### 依赖关系

要启用此参数，请引用一个未配置为条件执行的模型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowModelInitializePort` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,ShowModelInitializePort="on")`

### **Show model reinitialize ports** — 显示重新初始化事件端口的选项 `off`（默认） | `on`

选择此参数以显示重新初始化事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请引用一个未配置为条件执行且包含 Reinitialize Function 模块的模型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowModelReinitializePorts` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,ShowModelReinitializePorts="on")`

### **Show model reset ports** — 显示重置事件端口的选项 `off`（默认） | `on`

选择此参数以显示重置事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请引用一个未配置为条件执行且包含 Reset Function 模块的模型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowModelResetPorts` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,ShowModelResetPorts="on")`

### **Show model terminate port** — 显示终止事件端口的选项 `off`（默认） | `on`

选择此参数以显示终止事件端口。清除此参数以移除该端口。

#### 依赖关系

要启用此参数，请引用一个未配置为条件执行的模型。然后，选择 **Show model initialize port**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShowModelTerminatePort` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,ShowModelTerminatePort="on")`

### **Schedule rates** — 调度周期性事件的选项 `off`（默认） | `on`

使用周期性事件控制被引用模型的执行。

根据 **Schedule rates with** 参数的值，选择此参数将在 Model 模块上显示周期性事件端口，或创建用于 Schedule Editor 的分区。当 **Schedule rates with** 参数不可见时，其默认值（`Ports`）适用。

清除此参数将隐藏周期性事件端口，并且不会创建分区。

#### 依赖关系

要启用此参数，请引用一个具有离散采样时间、未配置为条件执行且不是导出函数模型的模型。当父模型基于速率且被引用模型是导出函数模型时，**Schedule rates** 会自动选中。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ScheduleRates` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,ScheduleRates="on")`

### **Schedule rates with** — 用于创建分区或周期事件端口的选项 `Ports`（默认） | `Schedule Editor`

创建端口或分区。

- `Ports` — 为被引用模型中的离散速率显示周期事件端口。

  要手动指定端口速率，请使用 `set_param` 函数将 Model 模块的 `AutoFillPortDiscreteRates` 参数设置为 `"off"`。然后，使用 `PortDiscreteRates` 参数指定端口速率。
- `Schedule Editor` — 为被引用模型创建分区，以便与 Schedule Editor 一起使用。

#### 依赖关系

要启用此参数：

- 父模型不能是导出函数模型。
- 父模型不能使用固定步长求解器和单任务模式。
- 选择 **Schedule rates**。当父模型基于速率且被引用模型是导出函数模型时，**Schedule rates** 会自动选中。
- 清除 **Show model initialize port**、**Show model reset ports** 和 **Show model reinitialize ports**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ScheduleRatesWith` |
| **值：** | `"Ports"`（默认） | `"Schedule Editor"` |

**示例：** `set_param(gcb,ScheduleRatesWith="Schedule Editor")`

### 实例参数

为模型参数指定实例特定的值。

### **Instance parameters** — 显示实例参数并为被引用模型指定值 数值 | 工作区变量 | 数学表达式 | 结构体或结构体字段

显示实例参数并指定实例特定的值。*实例参数*是在被引用模型中配置为对模型的每个实例使用不同值的模块参数。

要指定实例特定的值，请使用表中的 **Value** 列。要指定参数值可以由父模型覆盖，请选中 **Argument** 复选框。有关在被引用模型中配置实例参数并在 Model 模块中指定实例特定值的详细信息，请参阅 Configure Instance-Specific Values for Block Parameters in a Referenced Model。

更改实例特定的值时，可以使用部分结构体，该结构体的字段仅对应于要更改其值的实例参数。未包含在部分结构体中的实例参数保留其值。在结构体中，包含实例参数名称和值，指定为字符向量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParameterArgumentNames` |
| **值：** | 以逗号分隔的带引号的参数名称 |

|  |  |
| --- | --- |
| **参数：** | `InstanceParameters` |
| **值：** | 包含 `Name`、`Value`、`Path` 和 `Argument` 字段的结构体 |
| **数据类型：** | `struct` |

有关如何设置这些编程参数的示例，请参阅 Parameterize a Referenced Model Programmatically。

要获取 Model 模块的实例参数名称和值，请使用 `get_param` 函数查询 `InstanceParameters` 或 `ParameterArgumentValues`。不要使用 `ParameterArgumentValues` 来设置实例特定的值。

#### 依赖关系

要启用此参数，被引用模型必须在模型工作区中具有配置为模型参数的 MATLAB 变量或 `Simulink.Parameter` 对象。要将变量或对象配置为模型参数，请选中 **Argument** 属性。

### 求解器

通过组合被引用模型的配置参数和每个引用该模型的 Model 模块的模块参数，将被引用模型配置为使用局部求解器。

#### 被引用模型配置参数

### **Use local solver** — 使用局部求解器求解被引用模型的选项 链接到被引用模型配置参数

此参数提供一个超链接，用于打开该模块所引用模型的配置参数对话框。在配置参数对话框中，选中或清除被引用模型的 **Use local solver when referencing model** 参数。

当您选中 **Use local solver when referencing model** 时，软件使用局部求解器将被引用模型中实现的系统作为独立的微分方程组进行求解。在仿真期间，局部求解器计算被引用模型中连续状态的值以及被引用模型内部模块的输出值。

使用局部求解器可以促进系统组合和集成。使用局部求解器时，您可以在系统级仿真中使用与单独设计和测试每个模型时相同的求解器和步长来求解被引用模型。使用局部求解器还可以减少在将模型集成到更大系统时需要对被引用模型配置参数进行的配置调整次数。

对于某些系统，使用局部求解器可以通过以下方式提高仿真性能：

- 选择更适合求解被引用模型中系统的求解器
- 对不同组件使用不同的步长，以减少组件间动态范围较大的系统中冗余计算的次数。

有关详细信息，请参阅 Use Local Solvers in Referenced Models。

### **Solver** — 选择局部求解器的选项 链接到被引用模型配置参数

此参数提供一个超链接，用于打开该模块所引用模型的配置参数对话框。在配置参数对话框中，为被引用模型的 **Solver** 参数选择一个值。使用局部求解器时，被引用模型的 **Solver** 参数指定用作局部求解器的求解器。

在某些系统中，使用不同的局部求解器可以提高仿真性能。例如，当系统不是刚性的但被引用模型实现的组件是刚性的时，使用刚性局部求解器可以提高仿真系统时的性能。

顶层求解器可以是变步长或固定步长求解器。局部求解器可以是变步长*（自 R2025a 起）*或固定步长求解器。

有关详细信息，请参阅 Use Local Solvers in Referenced Models。

#### 依赖关系

要启用此参数，请在此模块所引用模型的配置参数中选中 **Use local solver when referencing model**。

### **Fixed step** — 为固定步长局部求解器指定步长的选项 链接到被引用模型配置参数

此参数提供一个超链接，用于打开该模块所引用模型的配置参数对话框。在配置参数对话框中，为被引用模型的 **Fixed-step size (fundamental sample time)** 参数指定值，以指定局部求解器的步长。您为局部求解器指定的步长不会在被引用模型或父模型中注册为离散速率。

局部步长可以大于、小于或等于父求解器步长。但是，*通信步长*决定了局部求解器和父求解器何时交换数据，它约束了局部步长的可能值。

- 局部步长必须小于或等于通信步长。
- 当局部步长小于通信步长时，局部步长必须是通信步长的整数除数。

  例如，当通信步长为 0.1 秒时，局部求解器可以是 0.1 秒、0.05 秒、0.025 秒等整数除数。

*在 R2024a 之前：当父求解器是固定步长求解器时，局部求解器步长必须是父求解器步长的整数倍。*

有关详细信息，请参阅 Use Local Solvers in Referenced Models。

#### 依赖关系

要启用此参数，请在此模块所引用模型的配置参数中：

- 选中 **Use local solver when referencing model**。
- 将 **Type** 设置为 `Fixed-step`。

#### Model 模块参数

### **Communication step size** — 局部求解器与父求解器之间通信的离散间隔 正标量双精度值

*通信步长*指定局部求解器和父求解器交换数据的速率。通信步长在父模型中注册为 Model 模块的离散采样时间。

默认情况下，通信步长为继承（`-1`），由软件确定。

- 固定步长局部求解器 — 继承的通信步长为局部步长。
- 变步长局部求解器*（自 R2025a 起）* — 继承的通信步长取决于多种条件。

  - 当被引用模型具有离散速率时，继承的通信步长是这些速率的最大公约数。
  - 当被引用模型没有离散速率且局部最大步长有限时，继承的通信步长为局部最大步长。
  - 当被引用模型没有离散速率且局部最大步长和仿真停止时间均为无穷大时，继承的通信步长为 `0.2`。
  - 当被引用模型没有离散速率、局部最大步长为无穷大且仿真停止时间有限时，继承的通信步长为仿真时间的 2%。

当您显式指定通信步长时，指定的值必须满足以下所有约束：

- 通信步长必须：

  - 大于或等于局部和父最小步长
  - 在适用时，是局部和父固定步长的整数倍
  - 大于或等于被引用模型中最快的离散速率
- 被引用模型中的每个离散速率必须能被通信步长整除。

当局部步长大于父步长时，请将通信步长指定为继承（`-1`）或等于局部步长。例如，如果父步长为 1 秒，局部步长为 2 秒，请将通信步长指定为 `-1`（继承）或 `2`。将通信步长指定为更大的值（如 `4`）可能会降低精度而不会带来任何性能提升。

对于变步长局部求解器*（自 R2025a 起）*：

- 当通信步长小于局部最大步长时，局部求解器的步长不会超过通信步长。
- 在通信步长的命中时间之间的间隔内，局部求解器根据被引用模型中连续状态的动态特性和您为局部求解器指定的容差值来确定每个局部步长的大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CommunicationStepSize` |
| **值：** | `-1`（默认） | 正标量双精度值 |
| **数据类型：** | `double` |

**示例：** `set_param(gcb,CommunicationStepSize="0.5")`

### **Input signal handling** — 局部求解器输入的外推方法 `Auto`（默认） | `Zero-order hold`

局部求解器通过外推来自父求解器的连续导数或输入信号值来计算连续状态值和模块输出值。此参数指定局部求解器用于将连续导数或输入信号值外推到局部仿真时间的方法。

- `Auto` — 软件根据所选求解器、模型结构以及局部步长与父求解器步长的比较来确定外推方法。

  局部求解器在以下情况下使用零阶保持将输入信号值外推到局部仿真时间：

  - 您选择隐式求解器，如 `ode1be` 或 `ode14x`。
  - 被引用模型没有输入端口。
  - 局部步长小于父步长。

  否则，局部求解器使用适合所选求解器的外推算法将连续导数外推到局部仿真时间。外推算法通常提高仿真结果的精度，但比零阶保持外推的计算量更大。

  *在 R2024a 之前：软件仅根据所选求解器来确定如何外推连续导数或输入信号值，且局部步长始终大于或等于父求解器步长。*
- `Zero-Order Hold` — 局部求解器使用零阶保持将输入信号值外推到局部仿真时间。局部仿真时间处的每个输入信号值等于父求解器在最近通信步长处为该信号计算的值。

  在以下任何情况下，考虑使用 `Zero-order hold` 输入处理：

  - 当使用 `Zero-order hold` 输入处理时仿真结果可接受且性能是关注点时
  - 当输入端口值不影响连续状态计算时
  - 当导数的很大一部分基于状态本身时，例如来自模型中的反馈环路
  - 为提高给定步长下局部求解器的稳定性

局部求解器在局部求解器推进阶段独立传播时间，该阶段发生在父求解器执行 Model 模块的更新方法时。由于更新方法在父求解器仿真循环中先于推进方法执行：

- 局部求解器推进发生在父求解器推进之前。
- 局部求解器在仿真时间上领先于父求解器。

为了计算被引用模型内部的连续状态值和模块输出值，局部求解器将连续导数或输入信号的值外推到局部仿真时间。有关详细信息，请参阅 Use Local Solvers in Referenced Models。

当您使用变步长局部求解器*（自 R2025a 起）*时，仅支持 `Zero-order hold` 输入和输出信号处理。

#### 依赖关系

要启用此参数，请在此模块所引用模型的模型配置参数中选中 **Use local solver when referencing model**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InputSignalHandling` |
| **值：** | `"Auto"`（默认） | `"Zero-order hold"` |

**示例：** `set_param(gcb,InputSignalHandling="Zero-order hold")`

### **输出信号处理** — 局部求解器输出的插值方法 `Auto`（默认）| `Use solver interpolant` | `Zero-order hold`

局部求解器可能需要在父求解器仿真时刻为模型引用接口上的输出信号提供值。为了提供输出信号值，局部求解器会对影响输出信号值的连续状态值进行插值，或者对输出信号值本身进行插值。此参数指定局部求解器如何对连续状态或输出信号值进行插值。

- `Auto` — 软件根据局部步长与通信步长的比较结果来确定插值方法。*（自 R2024a 起）*

  - 当局部步长小于通信步长时，局部求解器使用零阶保持将输出信号值插值到父求解器仿真时刻。
  - 当局部步长大于或等于通信步长时，局部求解器使用局部求解器插值函数将连续状态值插值到父求解器仿真时刻。然后，局部求解器使用插值后的连续状态值计算父求解器仿真时刻的输出信号值。
- `Use solver interpolant` — 局部求解器使用局部求解器插值函数将连续状态值插值到父求解器仿真时刻。仅当局部步长大于或等于父求解器步长时，才支持此选项。
- `Zero-order hold` — 局部求解器使用零阶保持将输出信号值插值到父求解器仿真时刻。

使用求解器插值函数进行插值通常可以提高精度，但也会增加计算复杂度。零阶保持输出处理可降低计算复杂度，但也会降低精度。

局部求解器在局部求解器推进阶段独立传播时间，该阶段发生在父求解器执行 Model 模块的更新方法时。由于在父求解器的仿真循环中，更新方法在推进方法之前执行：

- 局部求解器推进发生在父求解器推进之前。
- 局部求解器在仿真时间上领先于父求解器。

为了计算提供给父求解器的输出信号值，局部求解器会将 Model 模块输出方法中使用的连续状态值或输出信号值插值到父求解器仿真时刻。有关详细信息，请参阅 Use Local Solvers in Referenced Models。

当您使用变步长局部求解器时*（自 R2025a 起）*，仅支持 `Zero-order hold` 输入和输出信号处理。

#### 依赖关系

要启用此参数，请在此模块所引用模型的模型配置参数中选择 **Use local solver when referencing model**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputSignalHandling` |
| **值：** | `"Auto"`（默认）| `"Use solver interpolant"` | `"Zero-order Hold"` |

**示例：** `set_param(gcb,OutputSignalHandling="Zero-order
Hold")`

## 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。有关使用 Model 模块进行 HDL 代码生成以及最佳实践和限制的详细信息，请参阅 Model Referencing for HDL Code Generation (HDL Coder)。

另请参阅 Generate Black Box Interface for Referenced Model (HDL Coder) 和 Generate Parameterized Code for Referenced Models (HDL Coder)。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `ModelReference`（默认） | 当您希望从引用的模型及任何嵌套模型生成代码时，请使用 `ModelReference` 实现。有关详细信息，请参阅 Model Referencing for HDL Code Generation (HDL Coder)。 |
| `BlackBox` | 使用 `BlackBox` 实现为旧有或外部 HDL 代码实例化 HDL 封装或黑盒接口。如果指定黑盒接口，HDL Coder 不会尝试为引用的模型生成 HDL 代码。有关详细信息，请参阅 Generate Black Box Interface for Referenced Model (HDL Coder)。 |

**黑盒接口自定义**

对于 `BlackBox` 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

|  |  |
| --- | --- |
| **BalanceDelays** | 检测在一条路径上引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。另请参阅 BalanceDelays (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ReferenceModelPrefix** | 在生成代码中插入的引用模型前缀。代码生成器将此前缀应用于子模型文件名和 HDL 标识符。默认前缀为 `modelname_`，其中 `modelname` 是引用模型的名称。**注意**  - 如果指定空前缀，代码生成器不会为子模型文件名添加前缀。这可能会因模型之间的命名冲突而导致 HDL 编译错误。 - 如果将引用模型用作 DUT，代码生成器会忽略您指定的前缀。 |
| **SharingFactor** | 映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 被时间复用以转换为串行标量数据路径的并行数据路径或向量数量。默认值为 0，表示实现完全并行的数据路径。另请参阅 Streaming (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2006a 之前引入**

### R2025a：变步长局部求解器

您现在可以将引用的模型配置为使用变步长局部求解器。以前，仅支持定步长局部求解器。

当您使用变步长局部求解器时，Model 模块的 **Communication step size** 参数指定父求解器和局部求解器何时交换数据。在通信步长的命中时间之间的间隔内，变步长局部求解器根据引用模型中连续状态的动态特性和您为局部求解器指定的容差值来确定每个局部步长的大小。

当您使用变步长局部求解器时，仅支持 `Zero-order hold` 输入和输出信号处理。

有关详细信息，请参阅 Use Local Solvers in Referenced Models。

### R2024b：改进了使用局部求解器的模型引用输出端口的采样时间传播

引用配置为使用局部求解器的模型的 Model 模块现在会在局部求解器使用零阶保持输出信号处理时，将离散采样时间传播到模块输出端口。Model 模块的 **Communication step size** 参数定义了传播到模块输出端口的离散采样时间。在以前的版本中，Model 模块将引用模型中端口的采样时间传播到模块输出端口。

此采样时间传播的更改：

- 简化了父求解器和局部求解器之间的交互
- 更清晰地反映了零阶保持输出信号处理在父模型上下文中的效果
- 减少了父求解器复位的次数

在某些情况下，采样时间传播的更改会导致有关采样时间差异或冲突的警告。例如，当现在具有离散采样时间的 Model 模块输出端口驱动另一个模型引用的输入端口时，如果引用模型中输入端口的采样时间与顶层模型中输入信号的采样时间不匹配，软件会发出警告。有关详细信息，请参阅 Improve Simulation Performance Using Performance Advisor。

在大多数情况下，此更改不会影响数值结果，只会导致顶层模型中 Model 模块输出信号的记录数据点更少或不同。下表总结了此更改对不同局部求解器配置的影响。

| 局部求解器步长 | **Output signal handling** 参数值 | 采样时间传播更改的影响 |
| --- | --- | --- |
| 局部求解器步长小于通信步长 | `Zero-order hold` | Model 模块输出端口具有由模块的 **Communication step size** 参数定义的离散采样时间。采样时间的更改不会影响仿真的数值结果，但可能导致顶层模型中 Model 模块输出信号的记录数据点不同或更少。 |
| `Auto`  *仅支持零阶保持输出信号处理。* |
| 局部求解器步长等于通信步长 | `Auto` | 采样时间传播无变化。 |
| `Use solver interpolant` |
| `Zero-order hold` | Model 模块输出端口具有由模块的 **Communication step size** 参数定义的离散采样时间。采样时间的更改可能导致顶层模型中 Model 模块输出信号的记录数据点不同或更少。在极少数情况下，采样时间的更改可能由于以下原因影响数值结果：  - 对不依赖于引用模型中连续状态的输出信号应用零阶保持 - 执行更少的父求解器复位 |

### R2024a：对具有更快动态特性的组件使用局部求解器

您可以通过指定小于父求解器步长的局部步长，对具有更快动态特性的系统组件使用局部求解器。新的 **Communication step size** 参数指定父求解器和局部求解器之间通信的离散速率。通信步长在父模型中注册为离散速率，而不是局部求解器步长。

### R2024a：新的默认 **Output signal handling** 参数值以及当 **Input signal handling** 参数值为 `Auto` 时的改进行为

**Output signal handling** 参数的默认值是新的值 `Auto`。当 **Output signal handling** 参数值为 `Auto` 时，软件根据局部步长与通信步长的比较结果来确定用于将连续状态或输入信号值插值到父求解器仿真时刻的方法。在以前的版本中，局部步长必须大于或等于父求解器步长，并且 `Auto` 选项不存在。

当 **Input signal handling** 参数值为 `Auto` 时，软件现在根据模型结构以及局部步长与通信步长的比较结果来确定如何将连续导数或输入信号值外推到局部仿真时刻。在以前的版本中，软件在选择插值方法时不考虑模型结构。比较局部步长与通信步长也不相关，因为 **Communication step size** 参数不存在。

### R2024a：对包含具有环绕状态的模块的模型使用局部求解器

您可以将包含一个或多个具有环绕状态的模块的模型配置为在模型层次结构中引用时使用局部求解器。环绕状态可以提高具有周期性状态值的系统的数值稳定性，并允许状态值环绕到周期起点而无需重置求解器，从而避免降低仿真性能。

例如，您可以将车轮的角位置建模为始终介于 0 和 2*π* 之间的值。当车轮旋转超过角位置 2*π* 时，角位置环绕回 0，而不是持续增加。

### R2023b：无需进入引用模型即可创建 Model 模块端口

从 R2023b 开始，您可以像在 Subsystem 模块上一样，无需进入引用模型即可在 Model 模块上创建端口。

要创建端口，请将指针暂停在 Model 模块的四个边缘中的任意一个上。当指针变为十字形时，单击。新端口会出现在您单击的边缘上，并以蓝色高亮显示。将指针暂停在新端口上。在展开的操作菜单中，选择要创建的端口类型。

要删除现有端口，请选择该端口并按 **Delete**。要删除多个端口，请按 **Shift** 并选择这些端口。然后按 **Delete**。

有关创建 Model 模块端口的详细信息，请参阅 Add Ports to Model Reference Interface。

### R2023a：在模型层次结构中的任意位置对模型引用使用局部求解器

模型层次结构中任意位置的 Model 模块都可以使用局部求解器，包括使用局部求解器的引用模型内部的 Model 模块。

### R2022b：对加速器和快速加速器仿真支持局部求解器

加速器和快速加速器模式支持仿真使用局部求解器的模型引用层次结构。

### R2022a: 在引用模型中使用局部求解器

当被另一个模型引用时，您可以将引用模型配置为使用局部求解器。局部求解器将引用模型作为独立的微分方程系统进行求解。

使用局部求解器可以促进系统组合与集成。当您使用局部求解器时，可以使用与单独设计和测试每个模型时相同的求解器和步长，在系统级仿真中求解引用模型。使用局部求解器还可以减少在将模型集成到更大系统时，需要对引用模型中的配置参数进行的配置调整量。

对于某些系统，使用局部求解器可以通过允许您选择更适合求解引用模型中系统的求解器，或通过减少组件之间动态范围广泛的系统中的冗余计算次数，来提高仿真性能。

这些限制适用于引用一个或多个配置为使用局部求解器的模型的模型层次结构：

- 只有从顶层模型引用的模型才能使用局部求解器。
- 局部求解器仅支持普通模式仿真。
- 父求解器可以是变步长或固定步长求解器。局部求解器必须是固定步长求解器。
- 当父求解器为固定步长求解器时，局部求解器步长必须大于顶层求解器步长。

有关详细信息，请参阅 Use Local Solvers in Referenced Models。

### R2019a: 不再支持在 Model 模块中指定变体模型

从 R2019a 开始，不再支持在 Model 模块中指定变体模型。Model Variants 模块（一种预配置用于指定变体模型的 Model 模块）也不再受支持。加载包含这些模块的模型会将其转换为 Variant Subsystem 模块，其中包含代表变体选项的 Model 模块。

Variant Subsystem 模块提供以下优势：

- 您可以将 Model 模块和 Subsystem 模块混合作为变体选项。
- 您可以指定具有不同输入和输出端口数量的变体。

Variant Subsystem 模块参数 **Analyze all choices during update diagram and generate preprocessor conditionals** 的行为与 Model 模块参数 **Generate preprocessor conditionals** 不同。Variant Subsystem 模块参数不会仅编译活动变体以进行仿真和更新图，而是编译所有变体。

如果您有使用 Model 模块参数处理变体的脚本，则必须将其更新为使用 Variant Subsystem 模块参数。

## 描述

引用另一个模型以创建模型层次结构

Model 模块引用指定的模型。它显示与引用模型的顶层输入和输出端口相对应的输入和输出端口。这些端口允许您将引用模型连接到父模型中的其他模块。

要确定 Model 模块是否比具有类似功能的其他模块更适合您的目标，请参阅 Explore Types of Model Components 和 Compare Capabilities of Model Components。

有关如何使用 Model 模块引用模型的说明，请参阅 Reference Existing Models。

默认情况下，Model 模块显示引用模型内容的表示。有关详细信息，请参阅 Preview Content of Model Components。要查看引用模型的内容，请双击 Model 模块。

如果您拥有 Simulink®
Coder™ 许可证，您可以通过保护模型来隐藏引用模型的实现细节。要保护模型，请参阅 Protect Models to Conceal Contents (Simulink Coder)。要引用受保护的模型，请参阅 Reference Protected Models from Third Parties。
