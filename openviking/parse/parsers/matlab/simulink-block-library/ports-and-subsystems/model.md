---
type: simulink-block
title: 'Model'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'model'
---

# Model

Reference another model to create model hierarchy

## 中文

引用另一个模型来创建模型层次结构

### 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

### 描述

Model 模块引用指定的模型。该模块显示与引用模型顶层输入和输出端口对应的输入和输出端口。这些端口可将引用模型连接到父模型中的其他模块。

要确定 Model 模块是否比另一个具有类似功能的模块更适合您的目标，请参阅探索模型组件的类型和比较模型组件的功能。

有关如何引用包含 Model 模块的模型的说明，请参阅引用现有模型。

默认情况下，Model 模块显示引用模型内容的表示。有关详细信息，请参阅预览模型组件的内容。要查看引用模型的内容，请双击 Model 模块。

如果您拥有 Simulink® Coder™ 许可证，您可以通过保护模型来隐藏引用模型的实现细节。要保护模型，请参阅保护模型以隐藏内容 (Simulink Coder)。要引用受保护模型，请参阅引用来自第三方的受保护模型。

### 端口

#### 输入

#### **Port\_1** — 与引用模型的根级模块对应的输入 标量 | 向量 | 矩阵 | 数组 | 总线

Model 模块针对它引用的模型的每个输入端口都有一个对应的输入端口。引用模型的输入端口由 Inport 和 In Bus Element 模块定义。Model 模块端口的名称与引用模型中对应端口的名称相匹配。每个 Model 模块端口的输入信号、消息或函数调用必须对引用模型中的对应端口有效。有关详细信息，请参阅定义模型引用接口。

##### 提示

- 引用模型中的信号属性独立于 Model 模块的上下文。例如，信号维度和数据类型不会跨 Model 模块边界传播。要在引用模型中定义信号属性，请为根级 Inport 和 In Bus Element 模块定义模块参数。
- 连接到输入端口的函数调用会传入引用模型中。要根据函数调用有条件地执行引用模型，请参阅**函数调用**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持:** 是
#### 输出

#### **Port\_1** — 与引用模型的根级模块对应的输出 标量 | 向量 | 矩阵 | 数组 | 总线

Model 模块针对它引用的模型的每个输出端口都有一个对应的输出端口。引用模型的输出端口由 Outport 和 Out Bus Element 模块定义。Model 模块上端口的名称与引用模型中对应端口的名称相匹配。Model 模块的输出信号和消息是连接到引用模型中的 Outport 和 Out Bus Element 模块的信号和消息。请参阅定义模型引用接口。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持:** 是
#### 控制

##### 条件执行

#### **Enable** — 启用引用模型的控制信号 标量 | 向量 | 矩阵

使能端口显示在 Model 模块的顶部。端口标签是表示使能信号的图标。

Enable port on Model block

连接到端口的控制信号确定何时执行引用模型。有关详细信息，请参阅Conditionally Execute Referenced Models。

##### 依赖关系

要使能此端口，请将 Enable 模块添加到引用模型的顶层。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Trigger** — 触发引用模型的控制信号 标量 | 向量 | 矩阵

触发端口显示在 Model 模块的顶部。端口标签是表示触发信号的图标。

Trigger port on Model block

连接到端口的控制信号确定何时执行引用模型。有关详细信息，请参阅Conditionally Execute Referenced Models。

##### 依赖关系

要启用此端口，请将 Trigger 模块添加到引用模型的顶层，并将其**触发器类型**设置为**上升沿**、**下降沿**或**任一沿**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Function Call** — 函数调用事件的控制信号 标量

函数调用端口显示在 Model 模块的顶部。端口标签将引用模型的名称显示为函数。

Function-call port on Model block

连接到端口的函数调用控制信号确定何时执行引用模型。有关详细信息，请参阅Conditionally Execute Referenced Models。

##### 依赖关系

要启用此端口，请将 Trigger 模块添加到引用模型的顶层，并将其**触发器类型**设置为**函数调用**。

##### 模型事件仿真

#### **initialize** — 模型初始化事件的控制信号 标量

初始化事件端口提供触发模型初始化事件的函数调用控制信号，该事件会初始化引用模型的状态。

引用模型可以包含一个对应于模型初始化事件的 Initialize Function 模块。有关详细信息，请参阅使用初始化、重新初始化、重置和终止函数。

##### 依赖关系

要启用此端口，请选择**显示模型初始化端口**。

#### **reset** — 模型重置事件的控制信号 标量

重置事件端口提供触发模型重置事件的函数调用控制信号，该事件会重置引用模型的状态。

对于每个模型重置事件，引用模型必须包含一个对应的 Reset Function 模块。有关详细信息，请参阅使用初始化、重新初始化、重置和终止函数。

要指定端口名称，请使用 Reset Function 模块中 Event Listener 模块的**事件名称**参数。

##### 依赖关系

要启用这种类型的端口，请选择**显示模型重置端口**。

#### **reinit** — 模型重新初始化事件的控制信号 标量

重新初始化事件端口提供触发模型重新初始化事件的函数调用控制信号，该事件会重新初始化引用模型的状态。

对于每个模型重新初始化事件，引用模型必须包含一个对应的 Reinitialize Function 模块。有关详细信息，请参阅使用初始化、重新初始化、重置和终止函数。

要指定端口名称，请使用 Reinitialize Function 模块中 Event Listener 模块的**事件名称**参数。

##### 依赖关系

要启用这种类型的端口，请选择 **显示模型重新初始化端口**。

#### **terminate** — 模型终止事件的控制信号 标量

终止事件端口提供触发模型终止事件的函数调用控制信号，该事件会读取并保存引用模型的状态。

引用模型可以包含一个对应于模型终止事件的 Terminate Function 模块。有关详细信息，请参阅使用初始化、重新初始化、重置和终止函数。

##### 依赖关系

要启用此端口，请选择**显示模型终止端口**。

#### **D** — 用于调度周期性事件的控制信号 标量

周期性事件端口提供指定何时执行模型的函数调用控制信号。有关示例，请参阅Test Rate-Based Model Simulation Using Function-Call Generators。

每个端口标签显示关于周期性事件的信息，例如对应的 Inport 模块的采样时间。例如，此图像中的 Model 模块显示周期性事件端口并引用一个具有以下两个离散速率的模型：0.01 和 0.1。

A Model block has ports labeled D1[0.01] and D2[0.1].

##### 依赖关系

要启用这种类型的端口，请将**速率调度方式**设置为**端口**。

### 参数

要以交互方式修改 Model 模块参数，请选择 Model 模块。然后，在 Simulink 工具条的**模型模块**选项卡上，点击**模块参数**。

#### 常设

指定 Model 模块的基本信息。

#### **模型名称** — 引用模型的文件名 无默认值

指定引用模型的文件名。文件名必须为模型的有效 MATLAB® 标识符，如选择有效的模型文件名中所定义。文件扩展名是可选的。

要选择要引用的模型，请点击**浏览**。要查看指定的模型，请点击**打开模型**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ModelNameDialog` |
| **值:** | `''` (默认) | filename in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb,ModelNameDialog="mymodel.slx")`

要以编程方式获取模块参数值，请使用 `get_param` 函数。

您可以用不同格式查询引用模型的名称：

- `ModelFile` - 带文件扩展名的模型名称。如果不指定文件扩展名，则由软件在 MATLAB 路径中找到的第一个匹配项确定文件扩展名。
- `ModelNameDialog` - 带或不带文件扩展名的模型名称，具体取决于您是否指定了文件扩展名。
- `ModelName` - 不带文件扩展名的模型名称。如果为 `ModelName` 指定带文件扩展名的模型名称，则软件通过设置 `ModelNameDialog` 和 `ModelFile` 来保留文件扩展名。

#### **仿真模式** — 模型引用的仿真模式 **普通** (默认) | **加速** | **软件在环(SIL)** | **处理器在环(PIL)**

指定 Model 模块的仿真模式。Model 模块的仿真模式可以不同于其引用模型和模型层次结构中的其他模型的仿真模式。

- **普通** - 以解释方式执行引用模型，就像引用模型是在父模型中直接实现的原子子系统一样。
- **加速** - 为引用模型创建一个 MEX 文件。然后，通过运行 S-Function 来执行引用模型。
- **软件在环(SIL)** - 此选项需要 Embedded Coder® 许可证。根据**代码接口**参数设置生成生产代码。代码针对主机平台编译并在主机平台上执行。
- **处理器在环(PIL)** - 此选项需要 Embedded Coder 许可证。根据**代码接口**参数设置生成生产代码。此代码针对目标平台编译并在目标平台上执行。对于主机与目标之间的数据交换，软件提供了目标连接 API 实现，支持在 PIL 仿真的每个时间步进行此类数据交换。

Model 模块的四个角指示 Model 模块的仿真模式。对于普通模式，四个角为空心三角形。对于加速模式，四个角为实心三角形。对于 SIL 和 PIL 模式，四个角为实心三角形，且模块图标上显示有 `(SIL)` 或 `(PIL)` 字样。

虽然您可以为模型指定任何仿真模式，但当您引用该模型时，Model 模块会指定引用模型实例的仿真模式。父模型的仿真模式可以覆盖 Model 模块的仿真模式。

有关详细信息，请参阅为模型层次结构选择仿真模式。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SimulationMode` |
| **值:** | `"Normal"` (默认) | `"Accelerator"` | `"Software-in-the-loop (SIL)"` | `"Processor-in-the-loop (PIL)"` |

**示例:** `set_param(gcb,SimulationMode="Accelerator")`

#### **代码接口** — 从顶层模型或引用模型生成代码的选项 **模型引用** (默认) | **顶层模型**

指定是从顶层模型还是从引用模型为 SIL 和 PIL 仿真模式生成代码。要将生成的代码部署为使用引用模型的较大应用程序的一部分，请指定**模型引用**。要将生成的代码部署为独立应用程序，请指定**顶层模型**。

- **模型引用** - 代码是作为模型层次结构的一部分从引用模型生成的。代码生成使用类似于以下命令的命令，为名为 `ModelName` 的模型生成代码。

  ```
  slbuild("ModelName","ModelReferenceCoderTarget")
  ```
- **顶层模型** - 代码是使用独立的代码接口从顶层模型生成的。代码生成使用类似于以下命令的命令，为名为 `ModelName` 的模型生成代码。

  ```
  slbuild("ModelName")
  ```

##### 依赖关系

要启用此参数，请将**仿真模式**设置为**软件在环(SIL)** 或**处理器在环(PIL)**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `CodeInterface` |
| **值:** | `"Model reference"` (默认) | `"Top model"` |

**示例:** `set_param(gcb,CodeInterface="Top model")`

#### 模型事件仿真

控制引用模型何时执行并更改状态。

#### **显示模型初始化端口** — 显示初始化事件端口的选项 `off` (默认) | `on`

选中此参数可显示初始化事件端口。清除此参数可删除该端口。

##### 依赖关系

要启用此参数，请引用未配置为条件执行的模型。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowModelInitializePort` |
| **值:** | `"off"` (默认) | `"on"` |

**示例:** `set_param(gcb,ShowModelInitializePort="on")`

#### **显示模型重新初始化端口** — 显示重新初始化事件端口的选项 `off` (默认) | `on`

选中此参数可显示重新初始化事件端口。清除此参数可删除这些端口。

##### 依赖关系

要启用此参数，请引用未配置为条件执行且包含 Reinitialize Function 模块的模型。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowModelReinitializePorts` |
| **值:** | `"off"` (默认) | `"on"` |

**示例:** `set_param(gcb,ShowModelReinitializePorts="on")`

#### **显示模型重置端口** — 显示重置事件端口的选项 `off` (默认) | `on`

选中此参数可显示重置事件端口。清除此参数可删除这些端口。

##### 依赖关系

要启用此参数，请引用未配置为条件执行且包含 Reset Function 模块的模型。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowModelResetPorts` |
| **值:** | `"off"` (默认) | `"on"` |

**示例:** `set_param(gcb,ShowModelResetPorts="on")`

#### **显示模型终止端口** — 显示终止事件端口的选项 `off` (默认) | `on`

选中此参数可显示终止事件端口。清除此参数可删除该端口。

##### 依赖关系

要启用此参数，请引用未配置为条件执行的模型。然后，选择**显示模型初始化端口**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowModelTerminatePort` |
| **值:** | `"off"` (默认) | `"on"` |

**示例:** `set_param(gcb,ShowModelTerminatePort="on")`

#### **调度速率** — 调度周期性事件的选项 `off` (默认) | `on`

用周期性事件控制引用模型的执行。

根据**速率调度方式**参数的值，选择此参数将显示 Model 模块上的周期性事件端口，或创建分区以与调度编辑器结合使用。当**速率调度方式**参数不可见时，将应用其默认值（**端口**）。

清除此参数会隐藏周期性事件端口并且不会创建分区。

##### 依赖关系

要启用此参数，请引用一个具有离散采样时间的模型，该模型未配置为条件执行且不是导出函数模型。如果父模型是基于速率的模型，而引用模型是导出函数模型，则会自动选择**调度速率**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ScheduleRates` |
| **值:** | `"off"` (默认) | `"on"` |

**示例:** `set_param(gcb,ScheduleRates="on")`

#### **速率调度方式** — 创建分区或周期性事件端口的选项 **端口** (默认) | **调度编辑器**

创建端口或分区。

- **端口** - 显示引用模型中离散速率的周期性事件端口。

  要手动指定端口速率，请使用 `set_param` 函数将 Model 模块的 `AutoFillPortDiscreteRates` 参数设置为 `"off"`。然后，使用 `PortDiscreteRates` 参数指定端口速率。
- **调度编辑器** - 为引用模型创建分区以便与调度编辑器结合使用。

##### 依赖关系

要启用此参数，请进行如下设置：

- 父模型不能是导出函数模型。
- 父模型不能使用定步长求解器和单任务模式。
- 选择**调度速率**。如果父模型是基于速率的模型，而引用模型是导出函数模型，则会自动选择**调度速率**。
- 清除**显示模型初始化端口**、**显示模型重置端口**和**显示模型重新初始化端口**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ScheduleRatesWith` |
| **值:** | `"Ports"` (默认) | `"Schedule Editor"` |

**示例:** `set_param(gcb,ScheduleRatesWith="Schedule Editor")`

#### 实例参数

为模型参量指定特定于实例的值。

#### **实例参数** — 显示实例参数并指定引用模型的值 数字 | 工作区变量 | 数学表达式 | 结构体或结构体字段

显示实例参数并指定特定于实例的值。*实例参数*是已在引用模型中进行配置、用于对模型的每个实例使用不同值的模块参数。

要指定特定于实例的值，请使用表中的**值**列。要指定参数值可以被父模型覆盖，请选中**参量**复选框。有关在引用模型中配置实例参数以及在 Model 模块中指定特定于实例的值的详细信息，请参阅 为引用模型中的模块参数配置特定于实例的值。

更改特定于实例的值时，可以使用非完全结构体，该结构体的字段仅对应于您希望更改其值的实例参数。不包含在此非完全结构体中的实例参数保持其值不变。在结构体中包含实例参数名称和值，指定为字符向量。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ParameterArgumentNames` |
| **值:** | comma-separated parameter names in quotes |

|  |  |
| --- | --- |
| **参数:** | `InstanceParameters` |
| **值:** | structure with fields `Name`, `Value`, `Path`, and `Argument` |
| **数据类型:** | `struct` |

有关如何设置这些编程参数的示例，请参阅Parameterize a Referenced Model Programmatically。

要获取 Model 模块的实例参数名称和值，请使用 `get_param` 函数查询 `InstanceParameters` 或 `ParameterArgumentValues`。不要使用 `ParameterArgumentValues` 来设置特定于实例的值。

##### 依赖关系

要启用此参数，引用模型必须在模型工作区中具有配置为模型参量的 MATLAB 变量或 `Simulink.Parameter` 对象。要将变量或对象配置为模型参量，请选择**参量**属性。

#### 求解器

使用引用模型的配置参数和引用该模型的每个 Model 模块的模块参数的组合，将引用模型配置为使用局部求解器。

##### 引用模型配置参数

#### **使用局部求解器** — 使用局部求解器求解引用模型的选项 链接到引用模型配置参数

此参数提供超链接，该超链接可打开模块所引用的模型的“配置参数”对话框。在“配置参数”对话框中，选中或清除引用模型的**引用模型时使用局部求解器**参数。

当您选择**引用模型时使用局部求解器**时，软件将使用局部求解器求解在引用模型中作为单独的微分方程组实现的系统。在仿真期间，局部求解器计算引用模型中连续状态的值以及引用模型内模块的输出值。

使用局部求解器便于系统的组合和集成。使用局部求解器时，可以在系统级仿真中使用用于单独设计和测试每个模型的相同求解器和步长来求解引用模型。在将模型集成到更大的系统中时，使用局部求解器还可以减少需要对引用模型中的配置参数进行的配置调整次数。

对于某些系统，使用局部求解器可以提高仿真性能，因为它允许您：

- 选择更适合在引用模型中求解系统的求解器
- 对不同组件使用不同步长，以减小在各组件的动态特性明显不同的系统中冗余计算的数量。

有关详细信息，请参阅Use Local Solvers in Referenced Models。

#### **求解器** — 选择局部求解器的选项 链接到引用模型配置参数

此参数提供超链接，该超链接可打开模块所引用的模型的“配置参数”对话框。在“配置参数”对话框中，为引用模型的**求解器**参数选择值。使用局部求解器时，引用模型的**求解器**参数指定要用作局部求解器的求解器。

在某些系统中，使用不同局部求解器可以提高仿真性能。例如，如果系统为非刚性系统，但由引用模型实现的组件为刚性组件，则使用刚性局部求解器可以提高仿真系统时的性能。

顶层求解器既可以是变步长求解器，也可以是定步长求解器。局部求解器可以是变步长 *(自 R2025a 起)*或定步长求解器。

有关详细信息，请参阅Use Local Solvers in Referenced Models。

##### 依赖关系

要启用此参数，请在此模块引用的模型的配置参数中选择**引用模型时使用局部求解器**。

#### **定步长** — 为定步长局部求解器指定步长的选项 链接到引用模型配置参数

此参数提供超链接，该超链接可打开模块所引用的模型的“配置参数”对话框。在“配置参数”对话框中，指定引用模型的**定步长(基础采样时间)** 参数值以指定局部求解器的步长。在引用模型或父模型中，您为局部求解器指定的步长未注册为离散速率。

局部步长可以大于、小于或等于父求解器步长。但是，确定局部求解器和父求解器何时交换数据的*通信步长*会限制局部步长可能采用的值。

- 局部步长必须小于或等于通信步长。
- 当局部步长小于通信步长时，局部步长必须为通信步长的整数除数。

  例如，当通信步长为 0.1 秒时，局部求解器步长可以是 0.1 秒、0.05 秒、0.025 秒等整数除数。

*在 R2024a 之前的版本中: 当父求解器是定步长求解器时，局部求解器步长必须为父求解器步长的整数倍。*

有关详细信息，请参阅Use Local Solvers in Referenced Models。

##### 依赖关系

要启用此参数，请在此模块引用的模型的配置参数中：

- 选择**引用模型时使用局部求解器**。
- 将**类型**设置为**定步长**。

##### 模型模块参数

#### **通信步长** — 局部求解器和父求解器之间通信的离散间隔 双精度正标量

*通信步长*指定局部求解器和父求解器交换数据的速率。通信步长注册为父模型中 Model 模块的离散采样时间。

默认情况下，通信步长采用继承 (`-1`) 并由软件确定。

- 定步长局部求解器 - 继承的通信步长是局部步长。
- 变步长局部求解器 *(自 R2025a 起)* - 继承的通信步长取决于各种条件。

  - 当引用模型具有离散速率时，继承的通信步长是这些速率的最大公约数。
  - 当引用模型没有离散速率且局部最大步长有限时，继承的通信步长是局部最大步长。
  - 当引用模型没有离散速率且局部最大步长和仿真停止时间均为无限时，继承的通信步长为 `0.2`。
  - 当引用模型没有离散速率、局部最大步长为无限且仿真停止时间有限时，继承的通信步长为仿真时间的 2%。

当您显式指定通信步长时，您指定的值必须满足以下所有约束：

- 通信步长必须：

  - 大于或等于局部和父级最小步长
  - 在适用情况下，为局部和父级定步长的整数倍
  - 大于或等于引用模型中的最快离散速率
- 引用模型中的每个离散速率必须能被通信步长整除。

当局部步长大于父步长时，将通信步长指定为继承 (`-1`) 或等于局部步长。例如，如果父步长为 1 秒，局部步长为 2 秒，则将通信步长指定为 `-1`（继承）或 `2`。将通信步长指定为较大的值（如 `4`）可能会降低准确性，但不会带来任何性能提升。

对于变步长局部求解器 *(自 R2025a 起)*：

- 当通信步长小于局部最大步长时，局部求解器的步长不会超过通信步长。
- 在通信步长的命中时间的间隔内，局部求解器根据引用模型中连续状态的动态特性和为局部求解器指定的容差值确定每个局部步长。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `CommunicationStepSize` |
| **值:** | `-1` (默认) | positive scalar double |
| **数据类型:** | `double` |

**示例:** `set_param(gcb,CommunicationStepSize="0.5")`

#### **输入信号处理** — 局部求解器输入的外插方法 **自动** (默认) | **零阶保持**

局部求解器通过外插来自父求解器的连续导数或输入信号值来计算连续状态值和模块输出值。此参数指定局部求解器用于将连续导数或输入信号值外插至局部仿真时间的方法。

- **自动** - 软件根据所选求解器、模型结构以及局部步长与父求解器步长的比较结果来确定外插方法。

  在以下情况下，局部求解器使用零阶保持将输入信号值外插至局部仿真时间：

  - 选择了 `ode1be` 或 `ode14x` 等隐式求解器。
  - 引用模型没有输入端口。
  - 局部步长小于父步长。

  否则，局部求解器使用适用于所选求解器的外插算法将连续导数外插至局部仿真时间。外插算法通常会提高仿真结果的准确性，但计算量大于零阶保持外插。

  *在 R2024a 之前的版本中: 软件仅根据所选求解器确定如何外插连续导数或输入信号值，并且局部步长始终大于或等于父求解器步长。*
- **零阶保持** - 局部求解器使用零阶保持将输入信号值外插至局部仿真时间。局部仿真时间的每个输入信号值等于父求解器在最近的通信步中为信号计算的值。

  在以下任一情况下，考虑使用**零阶保持**输入处理：

  - 当仿真结果可接受但**零阶保持**输入处理和性能令人担忧时
  - 当输入端口值不影响连续状态计算时
  - 当导数的重要部分基于状态本身时，例如，来自模型中的反馈环
  - 需要提高在给定步长条件下的局部求解器稳定性

当父求解器对 Model 模块执行更新方法时，局部求解器在局部求解器推进阶段独立传播时间。因为在父求解器仿真循环中，更新方法在推进方法之前执行：

- 局部求解器的推进发生在父求解器推进之前。
- 在仿真时间内，局部求解器先于父求解器执行。

为了计算引用模型内的连续状态值和模块输出值，局部求解器将连续导数或输入信号值外插至局部仿真时间。有关详细信息，请参阅Use Local Solvers in Referenced Models。

使用变步长局部求解器 *(自 R2025a 起)*时，仅支持**零阶保持**输入和输出信号处理。

##### 依赖关系

要启用此参数，请在此模块引用的模型的模型配置参数中选择**引用模型时使用局部求解器**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InputSignalHandling` |
| **值:** | `"Auto"` (默认) | `"Zero-order hold"` |

**示例:** `set_param(gcb,InputSignalHandling="Zero-order hold")`

#### **输出信号处理** — 局部求解器输出的插值方法 **自动** (默认) | **使用求解器插值** | **零阶保持**

在父求解器仿真时间，局部求解器可能需要在模型引用接口上提供输出信号的值。为了提供输出信号值，局部求解器对影响输出信号值的连续状态值进行插值，或对输出信号值本身进行插值。此参数指定局部求解器如何对连续状态值或输出信号值进行插值。

- **自动** - 软件根据局部步长与通信步长的比较结果确定插值方法。 *(自 R2024a 起)*

  - 当局部步长小于通信步长时，局部求解器使用零阶保持将输出信号值插值到父求解器仿真时间。
  - 当局部步长大于或等于通信步长时，局部求解器使用局部求解器插值将连续状态值插值到父求解器仿真时间。然后，局部求解器使用经过插值的连续状态值计算父求解器仿真时间的输出信号值。
- **使用求解器插值** - 局部求解器使用局部求解器插值将连续状态值插值到父求解器仿真时间中。仅当局部步长大于或等于父求解器步长时，才支持此选项。
- **零阶保持** - 局部求解器使用零阶保持将输出信号值插值到父求解器仿真时间。

使用求解器插值通常会提高准确性，但也会增大计算复杂度。零阶保持输出处理会降低计算复杂度，但也会降低准确性。

当父求解器对 Model 模块执行更新方法时，局部求解器在局部求解器推进阶段独立传播时间。因为在父求解器的仿真循环中，更新方法先于推进方法执行：

- 局部求解器的推进发生在父求解器推进之前。
- 在仿真时间内，局部求解器先于父求解器执行。

为了计算输出信号值以提供给父求解器，局部求解器会对 Model 模块输出方法中使用的连续状态值或父求解器仿真时间的输出信号值进行插值。有关详细信息，请参阅Use Local Solvers in Referenced Models。

使用变步长局部求解器 *(自 R2025a 起)*时，仅支持**零阶保持**输入和输出信号处理。

##### 依赖关系

要启用此参数，请在此模块引用的模型的模型配置参数中选择**引用模型时使用局部求解器**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutputSignalHandling` |
| **值:** | `"Auto"` (默认) | `"Use solver interpolant"` | `"Zero-order Hold"` |

**示例:** `set_param(gcb,OutputSignalHandling="Zero-order Hold")`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `否` |
| **多维信号** | `是a` |
| **可变大小信号** | `是a` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。有关使用 Model 模块进行 HDL 代码生成以及最佳做法和限制的详细信息，请参阅 Model Referencing for HDL Code Generation (HDL Coder)。

另请参阅Generate Black Box Interface for Referenced Model (HDL Coder)和Generate Parameterized Code for Referenced Models (HDL Coder)。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **ModelReference**（默认值） | 当您要从引用模型和任何嵌套模型生成代码时，请使用 **ModelReference** 实现。有关详细信息，请参阅Model Referencing for HDL Code Generation (HDL Coder)。 |
| **BlackBox** | 使用 **BlackBox** 实现来实例化 HDL 包装器，或实例化与原有或外部 HDL 代码的黑盒接口。如果您指定黑盒接口，HDL Coder 不会尝试为引用模型生成 HDL 代码。  有关详细信息，请参阅 Generate Black Box Interface for Referenced Model (HDL Coder)。 |

**黑盒接口自定义**

对于 **BlackBox** 架构，您可以自定义端口名称并设置外部组件接口的属性。请参阅Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

**HDL 模块属性**

|  |  |
| --- | --- |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 **inherit**。另请参阅BalanceDelays (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **DistributedPipelining** | 流水线寄存器分配或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining (HDL Coder)。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为**无**。另请参阅DSPStyle (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |
| **ReferenceModelPrefix** | 要在生成代码中插入的引用模型的前缀。代码生成器将此前缀应用于子模型文件名和 HDL 标识符。默认前缀是 `modelname_`，其中 `modelname` 是引用模型的名称。  **注意**  - 如果指定空前缀，代码生成器不会向子模型文件名添加前缀。这可能导致模型间命名冲突所引发的 HDL 编译错误。 - 如果使用引用模型作为 DUT，代码生成器将忽略您指定的前缀。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源的数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |
| **StreamingFactor** | 并行数据路径或向量的数量，这些路径或向量通过时间多路复用的方式变换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅Streaming (HDL Coder)。 |

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

### 版本历史记录

**在 R2006a 之前推出**

#### R2025a: 变步长局部求解器

现在您可以将引用模型配置为使用变步长局部求解器。以前仅支持定步长局部求解器。

使用变步长局部求解器时，Model 模块的**通信步长**参数指定父求解器和局部求解器交换数据的时间。在通信步长的命中时间的间隔内，变步长局部求解器根据引用模型中连续状态的动态特性和为局部求解器指定的容差值确定每个局部步长。

使用变步长局部求解器时，仅支持**零阶保持**输入和输出信号处理。

有关详细信息，请参阅Use Local Solvers in Referenced Models。

#### R2024b: 改进了使用局部求解器的模型引用的输出端口的采样时间传播

如果局部求解器使用零阶保持输出信号处理，则引用配置为使用局部求解器的模型的 Model 模块现在会将离散采样时间传播到模块输出端口。Model 模块的**通信步长**参数定义传播到模块输出端口的离散采样时间。在以前的版本中，Model 模块将引用模型中端口的采样时间传播到模块输出端口。

对采样时间传播的这种更改会产生如下影响：

- 简化父求解器和局部求解器之间的交互
- 更清楚地反映父模型上下文中零阶保持输出信号处理的效果
- 减少父求解器重置的次数

在某些情况下，对采样时间传播的更改会导致发出有关采样时间差异或冲突的警告。例如，当现在具有离散采样时间的 Model 模块输出端口驱动另一个模型引用的输入端口时，如果引用模型中输入端口的采样时间与顶层模型中输入信号的采样时间不匹配，软件会发出警告。有关详细信息，请参阅Improve Simulation Performance Using Performance Advisor。

在大多数情况下，这种变化不会影响数值结果，只会导致 Model 模块输出信号的记录数据中出现更少或不同的点。下表总结了这种变化对不同局部求解器配置的影响。

| 局部求解器步长 | **输出信号处理**参数值 | 采样时间传播变化的影响 |
| --- | --- | --- |
| 局部求解器步长小于通信步长 | **零阶保持** | Model 模块输出端口具有由模块的**通信步长**参数定义的离散采样时间。  采样时间的变化不会影响仿真的数值结果，但会导致顶层模型中 Model 模块输出信号的记录数据中出现不同或更少的数据点。 |
| **自动**  *仅支持零阶保持输出信号处理。* |
| 局部求解器步长等于通信步长 | **自动** | 采样时间传播无变化。 |
| **使用求解器插值** |
| **零阶保持** | Model 模块输出端口具有由模块的**通信步长**参数定义的离散采样时间。  采样时间的变化会导致顶层模型中 Model 模块输出信号的记录数据中出现不同或更少的数据点。  在极少数情况下，因为以下原因，采样时间的变化会影响数值结果：  - 将零阶保持应用于不依赖引用模型中的连续状态的输出信号 - 执行更少的父求解器重置 |

#### R2024a: 使用局部求解器来求解具有更快动态特性的组件

通过指定小于父求解器步长的局部步长，可以将局部求解器用于具有更快动态特性的系统组件。新的**通信步长**参数指定父求解器和局部求解器之间通信的离散速率。通信步长在父模型中注册为离散速率，而不是局部求解器步长。

#### R2024a: 当**输入信号处理**参数值为**自动**时，新的默认**输出信号处理**参数值和改进的行为

**输出信号处理**参数的默认值为新值**自动**。当**输出信号处理**参数值为**自动**时，软件会根据局部步长与通信步长的比较结果，确定用于将连续状态值或输入信号值插值到父求解器仿真时间的方法。在以前的版本中，局部步长必须大于或等于父求解器步长，并且**自动**选项不存在。

当**输入信号处理**参数值为**自动**时，软件现在会根据模型结构以及局部步长与通信步长的比较结果，确定如何将连续导数值或输入信号值外插至局部仿真时间。在以前的版本中，软件在选择插值方法时不考虑模型结构。也不会考虑局部步长与通信步长的比较结果，因为**通信步长**参数不存在。

#### R2024a: 对包含具有绕回状态的模块的模型使用局部求解器

当在模型层次结构中引用包含一个或多个具有绕回状态的模块的模型时，可以将该模型配置为使用局部求解器。对于具有循环状态值的系统，绕回状态可以提高数值稳定性，并允许状态值绕回到循环的开始而无需重置求解器，但这可能会降低仿真性能。

例如，您可以对值始终介于 0 到 2*π* 之间的车轮角度位置进行建模。当车轮旋转超出角度位置 2*π* 时，角度位置会绕回到 0，而不是持续增加。

#### R2023b: 创建 Model 模块端口而无需进入模型

从 R2023b 开始，无需进入引用模型即可在 Model 模块上创建端口，这与在 Subsystem 模块上创建端口的方式相同。

要创建端口，请将鼠标在 Model 模块的四条边中的任一边上暂停。当指针变为十字时，点击鼠标。您点击的边上便会出现一个以蓝色突出显示的新端口。将指针在新端口上暂停。在展开的操作菜单中，选择要创建的端口类型。

要删除现有端口，请选择该端口并按 **Delete** 键。要删除多个端口，请按 **Shift** 键并选择要删除的端口。然后，按 **Delete** 键。

有关创建 Model 模块端口的详细信息，请参阅向模型引用接口添加端口。

#### R2023a: 在模型层次结构中的任何位置对模型引用使用局部求解器

处于模型层次结构中任何位置的 Model 模块都可以使用局部求解器，包括使用局部求解器的引用模型中的 Model 模块。

#### R2022b: 加速和快速加速仿真的局部求解器支持

加速和快速加速模式支持对使用局部求解器的模型引用层次结构进行仿真。

#### R2022a: 在引用模型中使用局部求解器

当一个引用模型被另一个模型引用时，可以将该引用模型配置为使用局部求解器。局部求解器将引用模型作为单独的微分方程组进行求解。

使用局部求解器便于系统的组合和集成。使用局部求解器时，可以在系统级仿真中使用用于单独设计和测试每个模型的相同求解器和步长来求解引用模型。在将模型集成到更大的系统中时，使用局部求解器还可以减少需要对引用模型中的配置参数进行的配置调整量。

某些系统允许您选择更适合在引用模型中求解系统的求解器，或减小在各组件的动态特性明显不同的系统中冗余计算的数量，从而使用局部求解器可以提高仿真性能。

引用一个或多个配置为使用局部求解器的模型的模型层次结构存在以下限制：

- 只有从顶层模型引用的模型才能使用局部求解器。
- 仅普通模式仿真支持局部求解器。
- 父求解器既可以是变步长求解器，也可以是定步长求解器。局部求解器必须为定步长求解器。
- 当父求解器是定步长求解器时，局部求解器步长必须大于顶层求解器步长。

有关详细信息，请参阅Use Local Solvers in Referenced Models。

#### R2019a: 不再支持在 Model 模块中指定变体模型

从 R2019a 开始，不再支持在 Model 模块中指定变体模型。Model Variants 模块（一种 Model 模块，预配置为指定变体模型）也不再受支持。包含这些模块的模型如被加载，则会被转换为 Variant Subsystem，其中包含表示变体选择项的 Model 模块。

Variant Subsystem 模块提供以下优势：

- 您可以将 Model 模块和 Subsystem 模块作为变体选择项来混合使用。
- 您可以指定具有不同数量的输入和输出端口的变体。

Variant Subsystem 模块参数**在更新图期间分析所有选择项并生成预处理器条件句**的行为方式不同于 Model 模块参数**生成预处理器条件句**。Variant Subsystem 模块参数会使仿真和更新图编译所有变体，而不是仅编译活动变体。

如果您的脚本使用变体的 Model 模块参数，您必须更新它们以使用 Variant Subsystem 模块参数。

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Description

The Model block references the specified model. It displays input and
output ports that correspond to the top-level input and output ports of the referenced
model. These ports allow you to connect the referenced model to other blocks in the
parent model.

To determine whether the Model block is better suited for your goal
than another block with similar functionality, see Explore Types of Model Components and Compare Capabilities of Model Components.

For instructions on how to reference a model with a Model block, see
Reference Existing Models.

By default, the Model block displays a representation of the contents
of the referenced model. For more information, see Preview Content of Model Components.
To see the contents of a referenced model, double-click the Model
block.

If you have a Simulink®
Coder™ license, you can conceal the implementation details of a referenced model
by protecting the model. To protect a model, see Protect Models to Conceal Contents (Simulink Coder). To
reference a protected model, see Reference Protected Models from Third Parties.

## Ports

### Input

### **Port\_1** — Input that corresponds to root-level blocks of referenced model scalar | vector | matrix | array | bus

The Model block has an input port for each input port
of the model it references. The input ports of referenced models are
defined by Inport and In Bus Element
blocks. The name of the Model block port matches the name
of the corresponding port in the referenced model. The input signal,
message, or function call for each Model block port must
be valid for the corresponding port in the referenced model. For more
information, see Define Model Reference Interfaces.

#### Tips

- Signal attributes in a referenced model are independent
  from the context of the Model block. For
  example, signal dimensions and data types do not propagate
  across the Model block boundary. To define
  signal attributes in a referenced model, define block
  parameters for root-level Inport and
  In Bus Element blocks.
- Function calls connected to an input port pass into the
  referenced model. To conditionally execute the referenced
  model based on a function call, see **Function Call**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output that corresponds to root-level blocks of referenced model scalar | vector | matrix | array | bus

The Model block has an output port for each output port
of the model it references. The output ports of referenced models are
defined by Outport and Out Bus Element
blocks. The name of the port on the Model block matches
the name of the corresponding port in the referenced model. The output
signals and messages of a Model block are the signals and
messages connected to the Outport and Out Bus
Element blocks in the referenced model. See Define Model Reference Interfaces.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
**Complex Number Support:** Yes
### Control

#### Conditional Execution

### **Enable** — Control signal that enables referenced model scalar | vector | matrix

The enable port appears at the top of the Model block.
The port label is an icon that represents an enable signal.

Enable port on Model block

The control signal that connects to the port determines when to
execute the referenced model. For more information, see Conditionally Execute Referenced Models.

#### Dependencies

To enable this port, add an Enable block to the
top level of the referenced model.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Trigger** — Control signal that triggers referenced model scalar | vector | matrix

The trigger port appears at the top of the Model block.
The port label is an icon that represents a trigger signal.

Trigger port on Model block

The control signal that connects to the port determines when to
execute the referenced model. For more information, see Conditionally Execute Referenced Models.

#### Dependencies

To enable this port, add a Trigger block to the
top level of the referenced model and set its **Trigger
type** to `rising`,
`falling`, or
`either`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Function Call** — Control signal for function-call event scalar

The function-call port appears at the top of the Model
block. The port label displays the name of the referenced model as a
function.

Function-call port on Model block

The function-call control signal that connects to the port determines
when to execute the referenced model. For more information, see Conditionally Execute Referenced Models.

#### Dependencies

To enable this port, add a Trigger block to the
top level of the referenced model and set its **Trigger
type** to
`function-call`.

#### Model Events Simulation

### **initialize** — Control signal for model initialize event scalar

The initialize event port provides a function-call control signal that
triggers a model initialize event, which initializes the states of the
referenced model.

The referenced model can contain an Initialize Function
block that corresponds to the model initialize event. For more
information, see Using Initialize, Reinitialize, Reset, and Terminate Functions.

#### Dependencies

To enable this port, select **Show model initialize
port**.

### **reset** — Control signal for model reset event scalar

A reset event port provides a function-call control signal that
triggers a model reset event, which resets the states of the referenced
model.

The referenced model must contain a Reset Function block
that corresponds to each model reset event. For more information, see
Using Initialize, Reinitialize, Reset, and Terminate Functions.

To specify the port name, use the **Event name**
parameter of the Event Listener block in the Reset
Function block.

#### Dependencies

To enable this type of port, select **Show model reset ports**.

### **reinit** — Control signal for model reinitialize event scalar

A reinitialize event port provides a function-call control signal that
triggers a model reinitialize event, which reinitializes the states of
the referenced model.

The referenced model must contain a Reinitialize Function block that corresponds to each model
reinitialize event. For more information, see Using Initialize, Reinitialize, Reset, and Terminate Functions.

To specify the port name, use the **Event name**
parameter of the Event Listener block in the
Reinitialize Function block.

#### Dependencies

To enable this type of port, select **Show model reinitialize ports**.

### **terminate** — Control signal for model terminate event scalar

The terminate event port provides a function-call control signal that
triggers a model terminate event, which reads and saves the states of
the referenced model.

The referenced model can contain a Terminate Function block
that corresponds to the model terminate event. For more information, see
Using Initialize, Reinitialize, Reset, and Terminate Functions.

#### Dependencies

To enable this port, select **Show model terminate
port**.

### **D** — Control signal for scheduling periodic events scalar

Periodic event ports provide function-call control signals that
specify when to execute the model. For an example, see Test Rate-Based Model Simulation Using Function-Call Generators.

Each port label displays information about the periodic event, such as
the sample time of the corresponding Inport block. For
example, the Model block in this image displays periodic
event ports and references a model with two discrete rates: 0.01 and
0.1.

A Model block has ports labeled D1[0.01] and D2[0.1].

#### Dependencies

To enable this type of port, set **Schedule rates with** to
`Ports`.

## Parameters

To interactively modify Model block parameters, select the
Model block. Then, in the Simulink Toolstrip, on the **Model Block** tab, click
**Block Parameters**.

### Main

Specify fundamental information for the Model block.

### **Model name** — File name of referenced model no default

Specify the filename of the referenced model. The filename must be a
valid MATLAB® identifier for a model, as defined in Choose Valid Model File Names. The file extension is
optional.

To select the model that you want to reference, click
**Browse**. To view the specified model, click
**Open Model**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ModelNameDialog` |
| **Values:** | `''` (default) | filename in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,ModelNameDialog="mymodel.slx")`

To get the block parameter value
programmatically, use the `get_param` function.

You can query the name of the referenced model in different formats:

- `ModelFile` — Model name with file
  extension. When you do not specify a file extension, the
  first match that the software finds on the MATLAB path determines the file extension.
- `ModelNameDialog` — Model name with
  or without file extension, depending on whether you
  specify a file extension.
- `ModelName` — Model name without file
  extension. If you specify a model name with a file
  extension for `ModelName`, the software
  retains the file extension by setting
  `ModelNameDialog` and
  `ModelFile`.

### **Simulation mode** — Simulation mode for model reference `Normal` (default) | `Accelerator` | `Software-in-the-loop (SIL)` | `Processor-in-the-loop (PIL)`

Specify the simulation mode for the Model block. The
simulation mode for the Model block can be different than
the simulation mode of its referenced model and of other models in the
model hierarchy.

- `Normal` — Execute the referenced
  model interpretively, as if the referenced model is an atomic
  subsystem implemented directly within the parent model.
- `Accelerator` — Create a MEX file for
  the referenced model. Then, execute the referenced model by
  running the S-function.
- `Software-in-the-loop (SIL)` — This
  option requires an Embedded Coder® license. Generate production code based on the
  **Code interface** parameter setting. The code is
  compiled for and executed on the host platform.
- `Processor-in-the-loop (PIL)` — This
  option requires an Embedded Coder license. Generate production code based on the
  **Code Interface** parameter setting. This
  code is compiled for and executed on the target platform. A
  target connectivity API implementation supports the exchange of
  data between the host and target at each time step during the
  PIL simulation.

The corners of the Model block indicate the simulation
mode of the Model block. For normal mode, the corners
have empty triangles. For accelerator mode, the corner triangles are
filled in. For SIL and PIL modes, the corners are filled in and the word
`(SIL)` or `(PIL)` appears on the
block icon.

Although you can specify any simulation mode for a model, when you
reference that model, the Model block specifies the
simulation mode of the referenced model instance. The simulation mode of
a parent model can override the simulation mode of a
Model block.

For more information, see Choose Simulation Modes for Model Hierarchies.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SimulationMode` |
| **Values:** | `"Normal"` (default) | `"Accelerator"` | `"Software-in-the-loop (SIL)"` | `"Processor-in-the-loop (PIL)"` |

**Example:** `set_param(gcb,SimulationMode="Accelerator")`

### **Code interface** — Option to generate code from top model or referenced model `Model reference` (default) | `Top model`

Specify whether to generate the code from the top model or the
referenced model for SIL and PIL simulation modes. To deploy the
generated code as part of a larger application that uses the referenced
model, specify `Model reference`. To deploy the
generated code as a standalone application, specify `Top
model`.

- `Model reference` — The code is
  generated from the referenced model as part of a model
  hierarchy. Code generation uses a command similar to this
  command, which generates code for a model named
  `ModelName`.

  ```
  slbuild("ModelName","ModelReferenceCoderTarget")
  ```
- `Top model` — The code is generated
  from the top model with the standalone code interface. Code
  generation uses a command similar to this command, which
  generates code for a model named
  `ModelName`.

  ```
  slbuild("ModelName")
  ```

#### Dependencies

To enable this parameter, set **Simulation mode** to either
`Software-in-the-loop (SIL)` or
`Processor-in-the-loop (PIL)`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CodeInterface` |
| **Values:** | `"Model reference"` (default) | `"Top model"` |

**Example:** `set_param(gcb,CodeInterface="Top
model")`

### Model Events Simulation

Control when the referenced model executes and changes states.

### **Show model initialize port** — Option to display initialize event port `off` (default) | `on`

Select this parameter to display the initialize event port. Clear this
parameter to remove the port.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelInitializePort` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelInitializePort="on")`

### **Show model reinitialize ports** — Option to display reinitialize event ports `off` (default) | `on`

Select this parameter to display the reinitialize event ports. Clear
this parameter to remove the ports.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution and contains a Reinitialize Function block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelReinitializePorts` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelReinitializePorts="on")`

### **Show model reset ports** — Option to display reset event ports `off` (default) | `on`

Select this parameter to display the reset event ports. Clear this
parameter to remove the ports.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution and contains a Reset Function
block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelResetPorts` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelResetPorts="on")`

### **Show model terminate port** — Option to display terminate event port `off` (default) | `on`

Select this parameter to display the terminate event port. Clear this
parameter to remove the port.

#### Dependencies

To enable this parameter, reference a model that is not configured
for conditional execution. Then, select **Show model initialize port**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowModelTerminatePort` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ShowModelTerminatePort="on")`

### **Schedule rates** — Option to schedule periodic events `off` (default) | `on`

Control the execution of the referenced model with periodic
events.

Depending on the value of the **Schedule rates with** parameter, selecting this parameter
will either display the periodic event ports on the Model
block or create partitions to use with the Schedule Editor. When the **Schedule rates
with** parameter is not visible, its default value
(`Ports`) applies.

Clearing this parameter hides the periodic event ports and does not
create partitions.

#### Dependencies

To enable this parameter, reference a model with discrete sample
times that is not configured for conditional execution and is not an
export-function model. When the parent model is rate based and the
referenced model is an export-function model, **Schedule
rates** is automatically selected.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ScheduleRates` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb,ScheduleRates="on")`

### **Schedule rates with** — Option to create partitions or periodic event ports `Ports` (default) | `Schedule Editor`

Create ports or partitions.

- `Ports` — Display periodic event
  ports for discrete rates in the referenced model.

  To manually specify port rates, use the `set_param`
  function to set the `AutoFillPortDiscreteRates`
  parameter of the Model block to
  `"off"`. Then, specify the port rates with
  the `PortDiscreteRates` parameter.
- `Schedule Editor` — Create partitions
  for the referenced model to use with the Schedule Editor.

#### Dependencies

To enable this parameter:

- The parent model must not be an export-function
  model.
- The parent model must not use a fixed-step solver and
  single-tasking mode.
- Select **Schedule rates**. When the parent model
  is rate based and the referenced model is an
  export-function model, **Schedule
  rates** is automatically selected.
- Clear **Show model initialize port**, **Show model reset ports**, and **Show model reinitialize ports**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ScheduleRatesWith` |
| **Values:** | `"Ports"` (default) | `"Schedule Editor"` |

**Example:** `set_param(gcb,ScheduleRatesWith="Schedule
Editor")`

### Instance Parameters

Specify instance-specific values for model arguments.

### **Instance parameters** — Display instance parameters and specify values for referenced model number | workspace variable | mathematical expression | structure or structure field

Display instance parameters and specify instance-specific values.
*Instance parameters* are block parameters that
have been configured in the referenced model to use a different value
for each instance of the model.

To specify instance-specific values, use the
**Value** column in the table. To specify that a
parameter value can be overridden by the parent model, select the
**Argument** check
box. For more
information about configuring instance parameters in a referenced model
and specifying instance-specific values at the Model
block, see Configure Instance-Specific Values for Block Parameters in a Referenced Model.

When changing instance-specific values, you can use a partial
structure that has fields that correspond to only the instance
parameters whose values you want to change. Instance parameters not
included in the partial structure retain their values. In the structure,
include the instance parameter names and values, specified as character
vectors.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ParameterArgumentNames` |
| **Values:** | comma-separated parameter names in quotes |

|  |  |
| --- | --- |
| **Parameter:** | `InstanceParameters` |
| **Values:** | structure with fields `Name`, `Value`, `Path`, and `Argument` |
| **Data Types:** | `struct` |

For an example of how to set these programmatic parameters, see
Parameterize a Referenced Model Programmatically.

To get the instance parameter names and values for a
Model block, query
`InstanceParameters` or
`ParameterArgumentValues` with the `get_param` function.
Do not use `ParameterArgumentValues` to set the
instance-specific
values.

#### Dependencies

To enable this parameter, the referenced model must have
MATLAB variables or `Simulink.Parameter`
objects in the model workspace that are configured as model
arguments. To configure a variable or object as a model argument,
select the **Argument** property.

### Solver

Configure a referenced model to use a local solver by using a combination of the
configuration parameters for the referenced model and the block parameters for each
Model block that references the model.

#### Referenced Model Configuration Parameters

### **Use local solver** — Option to use local solver to solve referenced model link to referenced model configuration parameter

This parameter provides a hyperlink that opens the Configuration
Parameters dialog box for the model referenced by the block. In the
Configuration Parameters dialog box, select or clear the **Use local solver when referencing model** parameter of
the referenced model.

When you select **Use local solver when referencing
model**, the software uses a local solver to solve the
system implemented in the referenced model as a separate system of
differential equations. During simulation, the local solver computes the
values of continuous states in the referenced model and the output
values for the blocks inside the referenced model.

Using a local solver can facilitate system composition and
integration. When you use local solvers, you can solve referenced models
in system-level simulations using the same solver and step size used to
design and test each model in isolation. Using local solvers can also
reduce the number of configuration adjustments you need to make to
configuration parameters in referenced models while integrating the
model into a larger system.

For some systems, using a local solver can improve simulation
performance by allowing you to:

- Choose a solver that is more appropriate to solve the
  system in the referenced model
- Use different step sizes for different components to
  reduce the number of redundant calculations in systems that
  have a wide range of dynamics among components.

For more information, see Use Local Solvers in Referenced Models.

### **Solver** — Option to select local solver link to referenced model configuration parameter

This parameter provides a hyperlink that opens the Configuration
Parameters dialog box for the model referenced by the block. In the
Configuration Parameters dialog box, select a value for the **Solver** parameter
of the referenced model. When you use a local solver, the
**Solver** parameter of the referenced model
specifies the solver to use as the local solver.

In some systems, using a different local solver can improve simulation
performance. For example, when the system is not stiff but the component
implemented by the referenced model is stiff, using a stiff local solver
can improve performance when simulating the system.

The top solver can be a variable-step or fixed-step solver. The local
solver can be a variable-step *(since R2025a)* or
fixed-step solver.

For more information, see Use Local Solvers in Referenced Models.

#### Dependencies

To enable this parameter, select **Use local solver when referencing model** in the
configuration parameters for the model referenced by this
block.

### **Fixed step** — Option to specify step size for fixed-step local solver link to referenced model configuration parameter

This parameter provides a hyperlink that opens the Configuration
Parameters dialog box for the model referenced by the block. In the
Configuration Parameters dialog box, specify the value for the
**Fixed-step size (fundamental
sample time)** parameter of the referenced model to
specify the step size for the local solver. The step size you specify
for the local solver is not registered as a discrete rate in either the
referenced model or the parent model.

The local step size can be greater than, less than, or equal to the
parent solver step size. However, the *communication step
size*, which determines when the local and parent solvers
exchange data, constrains possible values for the local step size.

- The local step size must be less than or equal to the
  communication step size.
- When the local step size is smaller than the communication
  step size, the local step size must be an integer divisor of
  the communication step size.

  For example, when the communication step size is 0.1
  seconds, the local solver can be an integer divisor such as
  0.1 seconds, 0.05 seconds, 0.025 seconds, and so on.

*Before R2024a: When the parent solver is a
fixed-step solver, the local solver step size must be an integer
multiple of the parent solver step size.*

For more information, see Use Local Solvers in Referenced Models.

#### Dependencies

To enable this parameter, in the configuration parameters for the
model referenced by this block:

- Select **Use local solver when referencing
  model**.
- Set **Type** to
  `Fixed-step`.

#### Model Block Parameters

### **Communication step size** — Discrete interval of communication between local solver and parent solver positive scalar double

The *communication step size* specifies the rate
at which the local and parent solvers exchange data. The communication
step size is registered as a discrete sample time of the
Model block in the parent model.

By default, the communication step size is inherited
(`-1`) and determined by the software.

- Fixed-step local solver — The inherited communication step
  size is the local step size.
- Variable-step local
  solver *(since R2025a)* — The inherited communication step size
  depends on various criteria.

  - When the referenced model has discrete rates, the
    inherited communication step size is the greatest common
    divisor of these rates.
  - When the referenced model has no discrete rates and
    the local maximum step size is finite, the inherited
    communication step size is the local maximum step size.
  - When the referenced model has no discrete rates and
    both the local maximum step size and the simulation stop
    time are infinite, the inherited communication step size
    is `0.2`.
  - When the referenced model has no discrete rates, the
    local maximum step size is infinite, and the simulation
    stop time is finite, the inherited communication step
    size is 2% of the simulation time.

When you explicitly specify the communication step size, the value you
specify must satisfy all of these constraints:

- The communication step size must be:

  - Greater than or equal to both the local and
    parent minimum step sizes
  - An integer multiple of both the local and
    parent fixed step sizes, when applicable
  - Greater than or equal to the fastest discrete
    rate in the referenced model
- Every discrete rate in the referenced model must be evenly
  divisible by the communication step size.

When the local step size is larger than the parent step size, specify
the communication step size as inherited (`-1`) or
equal to the local step size. For example, if the parent step size is 1
second and the local step size is 2 seconds, specify the communication
step size as `-1` (inherited) or `2`.
Specifying the communication step size as a larger value, such as
`4`, could reduce accuracy without providing any
performance improvement.

For a variable-step local solver *(since R2025a)*:

- When the communication step size is smaller than the local
  maximum step size, the local solver does not step farther
  than the communication step size.
- Within the interval between hit times for the
  communication step size, the local solver determines the
  size of each local step based on the dynamics of the
  continuous states in the referenced model and the tolerance
  values you specify for the local solver.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CommunicationStepSize` |
| **Values:** | `-1` (default) | positive scalar double |
| **Data Types:** | `double` |

**Example:** `set_param(gcb,CommunicationStepSize="0.5")`

### **Input signal handling** — Extrapolation method for local solver inputs `Auto` (default) | `Zero-order hold`

The local solver computes continuous state values and block output
values by extrapolating continuous derivative or input signal values
that come from the parent solver. This parameter specifies the method
the local solver uses to extrapolate continuous derivative or input
signal values to the local simulation time.

- `Auto` — The software determines the
  extrapolation method based on the selected solver, the model
  structure, and how the local step size compares to the parent
  solver step size.

  The local solver extrapolates input signal values to the local
  simulation time using a zero-order hold when:

  - You select an implicit solver, such as
    `ode1be` or
    `ode14x`.
  - The referenced model has no input ports.
  - The local step size is smaller than the parent
    step size.

  Otherwise, the local solver extrapolates continuous
  derivatives to the local simulation time using an extrapolation
  algorithm that is appropriate for the selected solver. The
  extrapolation algorithms generally improve the accuracy of
  simulation results but are more computationally intensive than
  the zero-order hold extrapolation.

  *Before R2024a: The software determines
  how to extrapolate continuous derivative or input signal values
  based only on the selected solver, and the local step size is
  always greater than or equal to the parent solver step
  size.*
- `Zero-Order Hold` — The local solver
  extrapolates input signal values to the local simulation time
  using a zero-order hold. Each input signal value at the local
  simulation time is equal to the value the parent solver
  calculated for the signal at the most recent communication
  step.

  Consider using `Zero-order hold`
  input handling in any of these situations:

  - When simulation results are acceptable with
    `Zero-order hold` input
    handling and performance is a concern
  - When input port values do not affect continuous
    state computations
  - When a significant part of the derivative is based
    on the state itself, for example, from feedback
    loops in the model
  - To improve local solver stability for a given step
    size

The local solver propagates time independently during the local solver
advance phase that occurs when the parent solver executes the update
method for the Model block. Because the update method
executes before the advance method in the parent solver simulation loop:

- The local solver advance occurs before the parent solver
  advance.
- The local solver gets ahead of the parent solver in
  simulation time.

To compute the continuous state values and block output values inside
the referenced model, the local solver extrapolates the values for
continuous derivatives or input signals to the local simulation time.
For more information, see Use Local Solvers in Referenced Models.

When you use a variable-step local
solver *(since R2025a)*, only `Zero-order hold`
input and output signal handling are supported.

#### Dependencies

To enable this parameter, select **Use local solver when referencing model** in the
model configuration parameters for the model referenced by this
block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InputSignalHandling` |
| **Values:** | `"Auto"` (default) | `"Zero-order hold"` |

**Example:** `set_param(gcb,InputSignalHandling="Zero-order
hold")`

### **Output signal handling** — Interpolation method for outputs from local solver `Auto` (default) | `Use solver interpolant` | `Zero-order hold`

The local solver might need to provide values for output signals on
the model reference interface at the parent solver simulation time. To
provide the output signal values, the local solver interpolates
continuous state values that affect the output signal values or
interpolates the output signal values themselves. This parameter
specifies how the local solver interpolates the continuous state or
output signal values.

- `Auto` — The software determines
  the interpolation method based on how the local step size
  compares to the communication step size. *(since R2024a)*

  - When the local step size is smaller than the
    communication step size, the local solver interpolates
    the output signal values to the parent solver simulation
    time using a zero-order hold.
  - When the local step size is greater than or equal to
    the communication step size, the local solver
    interpolates continuous state values to the parent
    solver simulation time using the local solver
    interpolant. The local solver then computes the output
    signal values for the parent solver simulation time
    using the interpolated continuous state values.
- `Use solver interpolant` — The local
  solver interpolates continuous state values to the parent solver
  simulation time using the local solver interpolant. This option
  is supported only when the local step size is greater than or
  equal to the parent solver step size.
- `Zero-order hold` — The local solver
  interpolates output signal values to the parent solver
  simulation time using a zero-order hold.

Using the solver interpolant for interpolation generally increases
accuracy but also increases computational complexity. Zero-order hold
output handling reduces computational complexity but also reduces
accuracy.

The local solver propagates time independently during the local solver
advance phase that occurs when the parent solver executes the update
method for the Model block. Because the update method
executes before the advance method in the simulation loop for the parent solver:

- The local solver advance occurs before the parent solver
  advance.
- The local solver gets ahead of the parent solver in
  simulation time.

To compute output signal values to provide to the parent solver, the
local solver interpolates either the values of continuous states that
are used in the Model block output method or the output
signal values to the parent solver simulation time. For more
information, see Use Local Solvers in Referenced Models.

When you use a variable-step local
solver *(since R2025a)*, only `Zero-order hold`
input and output signal handling are supported.

#### Dependencies

To enable this parameter, select **Use local solver when referencing model** in the
model configuration parameters for the model referenced by this
block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputSignalHandling` |
| **Values:** | `"Auto"` (default) | `"Use solver interpolant"` | `"Zero-order Hold"` |

**Example:** `set_param(gcb,OutputSignalHandling="Zero-order
Hold")`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic. For more information about using the
Model block for HDL code generation and best practices and
limitations, see Model Referencing for HDL Code Generation (HDL Coder).

See also Generate Black Box Interface for Referenced Model (HDL Coder) and Generate Parameterized Code for Referenced Models (HDL Coder).

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `ModelReference` (default) | When you want to generate code from a referenced model and any nested models, use the `ModelReference` implementation. For more information, see Model Referencing for HDL Code Generation (HDL Coder). |
| `BlackBox` | Use the `BlackBox` implementation to instantiate an HDL wrapper, or black box interface, for legacy or external HDL code. If you specify a black box interface, HDL Coder does not attempt to generate HDL code for the referenced model.  For more information, see Generate Black Box Interface for Referenced Model (HDL Coder). |

**Black Box Interface Customization**

For the `BlackBox` architecture, you
can customize port names and set attributes of the external component
interface. See Customize Black Box or HDL Cosimulation Interface (HDL Coder).

**HDL Block Properties**

|  |  |
| --- | --- |
| **BalanceDelays** | Detects introduction of new delays along one path and inserts matching delays on the other paths. The default is `inherit`. See also BalanceDelays (HDL Coder). |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **DistributedPipelining** | Pipeline register distribution, or register retiming. The default is `inherit`. See also DistributedPipelining (HDL Coder). |
| **DSPStyle** | Synthesis attributes for multiplier mapping. The default is `none`. See also DSPStyle (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |
| **ReferenceModelPrefix** | Prefix of the referenced model to insert in the generated code. The code generator applies this prefix to submodel file names and HDL identifiers. The default prefix is `modelname_` where `modelname` is the name of the referenced model.  **Note**  - If you specify an empty prefix, the code generator   does not add a prefix to submodel file names. This can cause HDL compilation   errors due to naming collisions between the models. - If you use the referenced model as the DUT, the code   generator ignores the prefix that you specify. |
| **SharingFactor** | Number of functionally equivalent resources to map to a single shared resource. The default is 0. See also Resource Sharing (HDL Coder). |
| **StreamingFactor** | Number of parallel data paths, or vectors, that are time multiplexed to transform into serial, scalar data paths. The default is 0, which implements fully parallel data paths. See also Streaming (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced before R2006a**

### R2025a: Variable-step local solver

You can now configure a referenced model to use a variable-step local solver.
Previously, only fixed-step local solvers were supported.

When you use a variable-step local solver, the **Communication step
size** parameter of the Model block specifies when the
parent and local solvers exchange data. Within the interval between hit times for
the communication step size, the variable-step local solver determines the size of
each local step based on the dynamics of the continuous states in the referenced
model and the tolerance values you specify for the local solver.

When you use a variable-step local solver, only `Zero-order
hold` input and output signal handling are supported.

For more information, see Use Local Solvers in Referenced Models.

### R2024b: Improved sample time propagation for output ports of model references that use local solvers

Model blocks that reference models configured to use local solvers
now propagate a discrete sample time to the block output ports if the local solver
uses zero-order hold output signal handling. The **Communication step
size** parameter of the Model block defines the discrete
sample time propagated to the block output ports. In previous releases, the
Model block propagated the sample time of the port in the
referenced model to the block output ports.

This change to sample time propagation:

- Simplifies the interactions between the parent solver and local
  solver
- More clearly reflects the effect of the zero-order hold output signal
  handling in the context of the parent model
- Reduces the number of parent solver resets

In some cases, the change to sample time propagation causes warnings about sample
time discrepancies or collisions. For example, when a Model block
output port that now has a discrete sample time drives the input port of another
model reference, the software issues a warning if the sample time of the input port
in the referenced model does not match the sample time of the input signal in the
top model. For more information, see Improve Simulation Performance Using Performance Advisor.

In most cases, this change does not affect numerical results and only results in
fewer or different points in logged data for the Model block output
signals. The table summarizes the impact of this change for different local solver
configurations.

| Local Solver Step Size | **Output signal handling** Parameter Value | Effect of Sample Time Propagation Change |
| --- | --- | --- |
| Local solver step size less than communication step size | `Zero-order hold` | Model block output ports have a discrete sample time defined by the **Communication step size** parameter of the block.  The change in sample time does not affect the numerical results of the simulation but can result in different or fewer data points in logged data for Model block output signals in the top model. |
| `Auto`  *Only zero-order hold output signal handling is supported.* |
| Local solver step size equal to communication step size | `Auto` | No change to sample time propagation. |
| `Use solver interpolant` |
| `Zero-order hold` | Model block output ports have a discrete sample time defined by the **Communication step size** parameter of the block.  The change in sample time can result in different or fewer data points in logged data for Model block output signals in the top model.  In rare cases, the change in sample time can affect numerical results as a result of:  - Applying the zero-order hold to output signals   that do not depend on continuous states in the   referenced model - Performing fewer parent solver resets |

### R2024a: Use local solver for components with faster dynamics

You can use local solvers for system components with faster dynamics by specifying
a local step size that is smaller than the parent solver step size. The new
**Communication step size** parameter specifies the discrete
rate for communication between the parent and local solver. The communication step
size is registered as a discrete rate in the parent model instead of the local
solver step size.

### R2024a: New default **Output signal handling** parameter value and improved behavior when **Input signal handling** parameter value is `Auto`

The default value of the **Output signal handling** parameter is
the new value `Auto`. When the **Output signal
handling** parameter value is `Auto`, the
software determines the method to use to interpolate continuous state or input
signal values to the parent solver simulation time based on how the local step size
compares to the communication step size. In previous releases, the local step size
had to be greater than or equal to the parent solver step size, and the
`Auto` option did not exist.

When the **Input signal handling** parameter value is
`Auto`, the software now determines how to extrapolate
continuous derivative or input signal values to the local simulation time based on
the model structure and how the local step size compares to the communication step
size. In previous releases, the software did not consider the model structure when
selecting the interpolation method. Considering how the local step size compares to
the communication step size was also not relevant because the
**Communication step size** parameter did not exist.

### R2024a: Use local solver for model that contains blocks with wrapped states

You can configure a model that contains one or more blocks with wrapped states to
use a local solver when referenced in a model hierarchy. Wrapping states can improve
numerical stability for systems with cyclical state values and allows the state
value to wrap to the start of the cycle without resetting the solver, which can slow
simulation performance.

For example, you can model the angular position of a wheel as having a value that
is always between 0 and 2*π*. When the wheel rotates beyond an
angular position of 2*π*, the angular position wraps back to 0
rather than continually increasing.

### R2023b: Create Model block ports without entering referenced model

Starting in R2023b, you can create ports on Model blocks without
entering the referenced model the same way you can on a Subsystem
block.

To create a port, pause on any of the four edges of the Model
block. When your pointer turns into a cross, click. A new port appears on the edge
you clicked, highlighted in blue. Pause your pointer on the new port. In the action
menu that expands, select the type of port you want to create.

To delete an existing port, select the port and press **Delete**. To
delete multiple ports, press **Shift** and select the ports. Then,
press **Delete**.

For more information about creating Model block ports, see Add Ports to Model Reference Interface.

### R2023a: Use local solver for model reference at any location in model hierarchy

Model blocks at any location in a model hierarchy can use a local
solver, including Model blocks inside referenced models that use
local solvers.

### R2022b: Local solver support for accelerator and rapid accelerator simulation

Accelerator and rapid accelerator mode support simulating model reference
hierarchies that use local solvers.

### R2022a: Use local solvers in referenced models

You can configure a referenced model to use a local solver when referenced by
another model. The local solver solves the referenced model as a separate system of
differential equations.

Using a local solver can facilitate system composition and integration. When you
use local solvers, you can solve referenced models in system-level simulations using
the same solver and step size used to design and test each model in isolation. Using
local solvers can also reduce the amount of configuration adjustments you need to
make to configuration parameters in referenced models while integrating the model
into a larger system.

For some systems, using a local solver can improve simulation performance by
allowing you to choose a solver that is more appropriate to solve the system in the
referenced model or by reducing the number of redundant calculations in systems that
have a wide range of dynamics among components.

These limitations apply for model hierarchies that reference one or more models
configured to use a local solver:

- Only models referenced from the top model can use local
  solvers.
- Local solvers are supported for only normal mode simulations.
- The parent solver can be a variable-step or fixed-step solver. The
  local solver must be a fixed-step solver.
- When the parent solver is a fixed-step solver, the local solver step
  size must be larger than the top solver step size.

For more information, see Use Local Solvers in Referenced Models.

### R2019a: Specifying variant models in Model blocks is no longer supported

Starting in R2019a, specifying variant models in Model blocks is no
longer supported. The Model Variants block, which was a
Model block preconfigured to specify variant models, is also no
longer supported. Loading a model that contains these blocks converts them to
Variant Subsystem blocks that contain Model blocks
that represent the variant choices.

Variant Subsystem blocks provide these advantages:

- You can mix Model blocks and Subsystem
  blocks as variant choices.
- You can specify variants that have different numbers of input and output
  ports.

The Variant Subsystem block parameter **Analyze all choices
during update diagram and generate preprocessor conditionals** behaves
differently from the Model block parameter **Generate
preprocessor conditionals**. Instead of causing simulation and update
diagram to compile the active variant only, the Variant Subsystem
block parameter compiles all variants.

If you have scripts that use Model block parameters for variants,
you must update them to use Variant Subsystem block
parameters.
