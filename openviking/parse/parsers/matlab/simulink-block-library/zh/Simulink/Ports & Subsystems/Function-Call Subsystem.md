---
type: simulink-block
title: 'Function-Call Subsystem'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functioncallsubsystem'
documentation_source_path: 'slref/functioncallsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Function-Call Subsystem

## 端口
```yaml
ports:
- name: In
  summary: 到 Subsystem 模块的信号输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus | image
- name: Function Call
  summary: 到 Subsystem 模块的函数调用输入 标量
  direction: input
- name: Out
  summary: 来自 Subsystem 模块的信号输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus | image
```

### 输入

### **In** — 到 Subsystem 模块的信号输入 标量 | 向量 | 矩阵

到 Subsystem 模块的信号输入，指定为标量、向量或矩阵。在 Subsystem 模块中放置一个 Inport 模块会向该模块添加一个外部输入端口。端口标签与 Inport 模块的名称匹配。

使用 Inport 模块从局部环境接收信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **Function Call** — 到 Subsystem 模块的函数调用输入 标量

Subsystem 模块中的 Trigger 模块会向该模块添加一个外部输入端口。**Trigger type** 为 `function-call` 会使该模块成为接受函数调用事件的 Function-Call 端口模块。
### 输出

### **Out** — 来自 Subsystem 模块的信号输出 标量 | 向量 | 矩阵

来自 Subsystem 模块的信号输出，以标量、向量或矩阵形式返回。在 Subsystem 模块中放置一个 Outport 模块会向该模块添加一个外部输出端口。端口标签与 Outport 模块的名称匹配。

使用 Outport 模块向局部环境发送信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
## 参数
```yaml
parameters:
- name: Show port labels
  summary: 端口标签的显示选项 FromPortIcon（默认）| FromPortBlockName | SignalName | none
  group: 主要
  block_parameter: ShowPortLabels
  values: '''FromPortIcon''（默认）| ''FromPortBlockName'' | ''SignalName'' | ''none'''
- name: Read/Write permissions
  summary: 对子系统内容的访问级别 ReadWrite（默认）| ReadOnly | NoReadOrWrite
  group: 主要
  block_parameter: Permissions
  values: '''ReadWrite''（默认）| ''ReadOnly'' | ''NoReadOrWrite'''
- name: Name of error callback function
  summary: 发生错误时要调用的函数名称 无默认值
  group: 主要
  block_parameter: ErrorFcn
  values: '''''（默认）| 带引号的函数名称'
- name: Permit hierarchical resolution
  summary: 工作区变量名称的解析 All（默认）| ExplicitOnly | None
  group: 主要
  block_parameter: PermitHierarchicalResolution
  values: '''All''（默认）| ''ExplicitOnly'' | ''None'''
- name: Show subsystem reinitialize ports
  summary: 显示重新初始化事件端口的选项 off（默认）| on
  group: 主要
  block_parameter: ShowSubsystemReinitializePorts
  values: '''off''（默认）| ''on'''
- name: Function packaging
  summary: 代码格式 Auto | Inline | Nonreusable function | Reusable function
  group: 代码生成
  block_parameter: RTWSystemCode
  values: '''Auto'' | ''Inline'' | ''Nonreusable function'' | ''Reusable function'''
- name: Function name options
  summary: 如何命名生成的函数 Auto | Use subsystem name | User specified
  group: 代码生成
  block_parameter: RTWFcnNameOpts
  values: '''Auto'' | ''Use subsystem name'' | ''User specified'''
- name: Function name
  summary: 子系统代码的函数名称 无默认值
  group: 代码生成
  block_parameter: RTWFcnName
  values: '''''（默认）| 带引号的函数名称'
- name: File name options
  summary: 如何命名生成的文件 Auto | Use subsystem name | Use function name | User specified
  group: 代码生成
  block_parameter: RTWFileNameOpts
  values: '''Auto'' | ''Use subsystem name'' | ''Use function name'' | ''User specified'''
- name: File name (no extension)
  summary: 生成文件的名称 无默认值
  group: 代码生成
  block_parameter: RTWFileName
  values: '''''（默认） | 带引号的文件名'
- name: Function interface
  summary: 如何使用生成函数的参数 void_void（默认） | Allow arguments (Optimized) | Allow arguments (Match graphical interface)
  group: 代码生成
  block_parameter: FunctionInterfaceSpec
  values: '''void_void''（默认） | ''Allow arguments (Optimized)'' | ''Allow arguments (Match graphical interface)'''
- name: Function with separate data
  summary: 控制子系统代码生成 off（默认） | on
  group: 代码生成
  block_parameter: FunctionWithSeparateData
  values: '''off''（默认） | ''on'''
- name: Memory section for initialize/terminate functions
  summary: 如何应用内存段 Inherit from model（默认） | Default | 模型内存段
  group: 代码生成
  block_parameter: RTWMemSecFuncInitTerm
  values: '''Inherit from model''（默认） | ''Default'' | 带引号的模型内存段'
- name: Memory section for execution functions
  summary: 如何应用内存段 Inherit from model（默认） | Default | 模型内存段
  group: 代码生成
  block_parameter: RTWMemSecFuncExecute
  values: '''Inherit from model''（默认） | ''Default'' | 带引号的模型内存段'
- name: Memory section for constants
  summary: 如何应用内存段 Inherit from model（默认） | Default | 模型内存段
  group: 代码生成
  block_parameter: RTWMemSecDataConstants
  values: '''Inherit from model''（默认） | ''Default'' | 带引号的模型内存段'
- name: Memory section for internal data
  summary: 如何应用内存段 Inherit from model（默认） | Default | 模型内存段
  group: 代码生成
  block_parameter: RTWMemSecDataInternal
  values: '''Inherit from model''（默认） | ''Default'' | 带引号的模型内存段'
- name: Memory section for parameters
  summary: 如何应用内存段 Inherit from model（默认） | Default | 模型内存段
  group: 代码生成
  block_parameter: RTWMemSecDataParameters
  values: '''Inherit from model''（默认） | ''Default'' | 带引号的模型内存段'
- name: Subsystem file name
  summary: 被引用子系统的文件名 无默认值
  group: Subsystem Reference
  block_parameter: ReferencedSubsystem
  values: '''''（默认） | 带引号的子系统文件名'
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 中，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Show port labels** — 端口标签的显示选项 `FromPortIcon`（默认）| `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称；如果模块名称为默认名称，则显示端口号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到该端口的信号已命名，则在 Subsystem 模块上显示该信号名称。否则，显示对应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅 Edit Port Labels on Subsystem Blocks。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ShowPortLabels` |
| **值**：| `'FromPortIcon'`（默认）| `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — 对子系统内容的访问级别 `ReadWrite`（默认）| `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开子系统，但不允许修改。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，也可以创建和修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

如果您尝试查看 **Read/Write permissions** 参数设置为 `NoReadOrWrite` 的子系统内容，您不会收到任何响应。例如，当双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Permissions` |
| **值**：| `'ReadWrite'`（默认）| `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — 发生错误时要调用的函数名称 无默认值

输入当软件执行子系统期间发生错误时要调用的函数名称。

软件会向该函数传递两个参数：子系统的句柄以及指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件会显示一般错误消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ErrorFcn` |
| **值**：| `''`（默认）| 带引号的函数名称 |
| **Data Types:** | `char` | `string` |

### **Permit hierarchical resolution** — 工作区变量名称的解析 `All`（默认）| `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅 Symbol Resolution 和 Symbol Resolution Process。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在对应模块的位置）、信号以及标记为“must resolve”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PermitHierarchicalResolution` |
| **值**：| `'All'`（默认）| `'ExplicitOnly'` | `'None'` |

### **Show subsystem reinitialize ports** — 显示重新初始化事件端口的选项 `off`（默认）| `on`

选择此参数以显示重新初始化事件端口。清除此参数以移除这些端口。

#### 依赖关系

要启用此参数，请选择 **Treat as atomic unit**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ShowSubsystemReinitializePorts` |
| **值**：| `'off'`（默认）| `'on'` |

### 代码生成

Code Generation 选项卡上的参数需要 Simulink Coder™ 或 Embedded Coder® 许可证。

### **Function packaging** — 代码格式 `Auto` | `Inline` | `Nonreusable function` | `Reusable function`

选择要为原子（非虚拟）子系统生成的代码格式。

- `Auto` — 软件根据模型中存在的子系统类型和实例数量为您选择最佳格式。
- `Inline` — 软件无条件地内联该子系统。
- `Nonreusable function` — 如果 **Filename options** 设置为 `Auto`，软件会在模型文件中打包单独的函数。如果 **File name options** 设置为 `Use subsystem name`、`Use function name` 或使用不同文件名的 `User specified`，软件会在单独的文件中打包单独的函数。

  使用此设置的子系统生成的函数可能带有参数，具体取决于 Function interface 参数设置。您可以使用 Function name 和 File name (no extension) 参数分别命名生成的函数和文件。这些函数不可重入。
- `Reusable function` — 软件生成带参数的函数，当模型包含子系统的多个实例时，允许重用子系统代码。

  此选项还会生成带参数的函数，当模型引用层次结构在多个被引用模型中包含子系统的多个实例时，允许在生成的代码中重用子系统代码。在这种情况下，子系统必须位于库中。

有关详细信息，请参阅：

- 为单个子系统生成代码和可执行文件 (Simulink Coder)
- Generate Inlined Subsystem Code (Simulink Coder)
- 将子系统代码生成为单独的函数和文件 (Simulink Coder)
- 从跨模型共享的库子系统生成可重用代码 (Simulink Coder)

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Reusable function`。

#### 提示

- 当您希望将子系统的多个实例表示为一个可重用函数时，可以将每个实例指定为 `Auto` 或 `Reusable function`。最好只使用其中一种，因为同时使用两者会创建两个可重用函数，每种指定各一个。这些选择的结果仅在无法重用时才有所不同。选择 `Auto` 不允许控制子系统代码的函数名或文件名。
- `Reusable function` 和 `Auto` 选项都会尝试确定是否存在子系统的多个实例以及代码是否可以重用。每个选项行为之间的区别在于，当无法重用时：

  - `Auto` 会生成内联代码，或者如果情况禁止内联，则为每个子系统实例生成单独的函数。
  - `Reusable function` 会为模型中的每个子系统实例生成一个带参数的单独函数。
- 如果您在生成的代码处于源代码控制下时选择 `Reusable function`，请将 **File name options** 设置为 `Use subsystem name`、`Use function name` 或 `User specified`。否则，每当您修改模型时，代码文件的名称都会更改，这会妨碍对文件进行源代码控制。
- 如果您选择的选项不是 `Auto` 或 `Inline`，并且模型配置参数为 **States**，则代码生成器会生成单独的输出和更新方法。代码生成器不会考虑 **Combine output and update methods for code generation and simulation** 规范。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证才能进行代码生成。
- 要启用此参数，请选择 **Treat as atomic unit**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWSystemCode` |
| **值**：| `'Auto'` | `'Inline'` | `'Nonreusable function'` | `'Reusable function'` |

### **Function name options** — 如何命名生成的函数 `Auto` | `Use subsystem name` | `User specified`

选择软件如何命名它为子系统生成的函数。

如果您拥有 Embedded Coder 许可证，可以使用 Configuration Parameter **Code Generation** > **Identifiers** 窗格上的选项控制函数名称。

- `Auto` — 使用默认命名约定 `model_subsystem()` 分配唯一函数名称，其中 *`model`* 是模型名称，*`subsystem`* 是子系统名称；当代码被重用时，则是相同子系统的名称。

  如果您为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，则为了生成该子系统的可重用代码，**Function name options** 必须设置为 `Auto`。
- `Use subsystem name` — 使用子系统名称作为函数名称。默认情况下，函数名称使用命名约定 `model_subsystem`。

  当子系统位于库模块中且子系统参数 Function packaging 设置为 `Reusable function` 时，如果您设置 `Use subsystem name` 选项，代码生成器会使用库模块的名称作为子系统函数名称和文件名。
- `User specified` — 启用 **Function name** 字段。输入任何合法的 C 或 C++ 函数名称，该名称必须唯一。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use subsystem name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnNameOpts` |
| **值**：| `'Auto'` | `'Use subsystem name'` | `'User specified'` |

### **Function name** — 子系统代码的函数名称 无默认值

为子系统代码指定唯一、合法的 C 或 C++ 函数名称。

如果您想为函数指定特定名称，而不是允许 Simulink Coder 代码生成器分配其自己的自动生成名称或使用子系统名称，请使用此参数。有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function name options** 设置为 `User specified`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RTWFcnName` |
| **值**：| `''`（默认）| 带引号的函数名称 |
| **Data Types:** | `char` | `string` |

### **File name options** — 如何命名生成的文件 `Auto` | `Use subsystem name` | `Use function name` | `User specified`

选择软件如何命名它为子系统生成的函数所在的单独文件。

- `Auto` — 根据子系统的配置以及模型中的实例数量，`Auto` 会产生不同的结果。

  - 如果代码生成器*不*为子系统生成单独的文件，则子系统代码会生成在由子系统父系统生成的代码模块中。如果子系统父系统是模型本身，则子系统代码会生成在 `model.c` 或 `model.cpp` 中。
  - 如果您为 **Function packaging** 参数选择 `Reusable function`，并且生成的代码处于源代码控制下，请考虑指定 `Auto` 以外的 **File name options** 值。这可以防止生成的文件名因无关的模型修改而更改，这对于使用源代码控制管理配置来说是个问题。
  - 如果您为 **Function packaging** 参数选择 `Reusable function`，并且模型引用层次结构包含可重用子系统的多个实例，则为了生成该子系统的可重用代码，**File name options** 必须设置为 `Auto`。
- `Use subsystem name` — 代码生成器生成单独的文件，使用子系统（或库模块）名称作为文件名。

  当 **File name options** 设置为 `Use subsystem name` 时，如果模型包含 Model 模块，或者正在为该模型生成模型引用目标，则子系统文件名会被改编。在这些情况下，子系统文件名由子系统名称加上模型名称前缀组成。
- `Use function name` — 代码生成器使用由 **Function name options** 指定的函数名称作为文件名。
- `User specified` — 此选项启用 **File name (no extension)** 文本输入字段。代码生成器使用您输入的名称作为文件名。输入任何文件名，但不要包含 `.c` 或 `.cpp`（或任何其他）扩展名。此文件名不必唯一。

  虽然子系统源文件名不必唯一，但您必须避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

默认值取决于模块配置。例如，Subsystem 模块的默认值为 `Auto`。CodeReuseSubsystem 模块的默认值为 `Use function name`。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileNameOpts` |
| **值：** | `'Auto'` | `'Use subsystem name'` | `'Use function name'` | `'User specified'` |

### **File name (no extension)** — 生成文件的名称 无默认值

您指定的文件名不必唯一。但是，请避免使用会导致循环依赖的非唯一名称。例如，`sys_a.h` 包含 `sys_b.h`，`sys_b.h` 包含 `sys_c.h`，而 `sys_c.h` 包含 `sys_a.h`。

有关详细信息，请参阅 Generate Subsystem Code as Separate Function and Files (Simulink Coder)。

#### 依赖关系

- 此参数需要 Simulink Coder 许可证。
- 要启用此参数，请将 **File name options** 设置为 `User specified`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWFileName` |
| **值：** | `''`（默认） | 带引号的文件名 |
| **数据类型：** | `char` | `string` |

### **Function interface** — 如何使用生成函数的参数 `void_void`（默认） | `Allow arguments (Optimized)` | `Allow arguments (Match graphical interface)`

选择如何使用生成函数的参数。

- `void_void` — 生成不带参数的函数，并将数据作为全局变量传递。例如：

  ```
  void subsystem_function(void)
  ```
- `Allow arguments (Optimized)` — 生成使用参数而不是将数据作为全局变量传递的函数。此规范可减少全局 RAM。此选项可能会减小代码大小并提高执行速度，并使代码生成器能够应用额外的优化。例如：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1)
  ```

  在某些情况下，生成优化代码时，代码生成器可能不会生成带参数的函数。
- `Allow arguments (Match graphical interface)` — 生成使用与 Subsystem 图形模块接口匹配的参数的函数接口。生成的函数接口是可预测的，不会发生变化。可预测的接口对于调试和测试代码以及与外部应用程序集成非常有用。例如，如果模型有两个 Inport 模块和两个 Outport 模块，则生成的函数接口为：

  ```
  void subsystem_function(real_T rtu_In1, real_T rtu_In2,
                          real_T *rty_Out1, real_T *rty_Out2)
  ```

有关详细信息，请参阅：

- Reduce Global Variables in Nonreusable Subsystem Functions (Embedded Coder)
- 生成可预测的函数接口以匹配图形模块接口 (Embedded Coder)
- 为非虚拟子系统生成模块化函数代码 (Embedded Coder)

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionInterfaceSpec` |
| **值：** | `'void_void'`（默认） | `'Allow arguments (Optimized)'` | `'Allow arguments (Match graphical interface)'` |

### **Function with separate data** — 控制子系统代码生成 `off`（默认） | `on`

生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。

- `off` — 不生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。
- `on` — 生成子系统函数代码，其中原子子系统的内部数据与其父模型分离，并由该子系统拥有。子系统数据结构独立于父模型数据结构声明。具有独立数据的子系统拥有自己的模块 I/O 和 `DWork` 数据结构。因此，子系统生成的代码更易于跟踪和测试。数据分离还倾向于减小整个模型中全局数据结构的最大大小，因为它们被拆分为多个数据结构。

有关如何为原子子系统生成模块化函数代码的详细信息，请参阅 Generate Modular Function Code for Nonvirtual Subsystems (Embedded Coder)。

有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionWithSeparateData` |
| **值：** | `'off'`（默认） | `'on'` |

### **Memory section for initialize/terminate functions** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统初始化和终止函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值取决于您为模型配置设置了哪些内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncInitTerm` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **Memory section for execution functions** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择 Embedded Coder 如何将内存段应用于子系统执行函数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 可能的值取决于您为模型配置设置了哪些内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder) 和 Model Configuration Parameters: Code Generation (Simulink Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 或 `Reusable function`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecFuncExecute` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **Memory section for constants** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统常量。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于您为模型配置设置了哪些内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataConstants` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **Memory section for internal data** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统内部数据。

- `Inherit from model` — 将根模型内存段应用于子系统数据。
- `Default` — 不将内存段应用于子系统数据，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于您为模型配置设置了哪些内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataInternal` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### **Memory section for parameters** — 如何应用内存段 `Inherit from model`（默认） | `Default` | 模型内存段

选择软件如何将内存段应用于子系统参数。

- `Inherit from model` — 将根模型内存段应用于子系统函数代码。
- `Default` — 不将内存段应用于子系统系统代码，覆盖任何模型级规范。
- 将其中一个模型内存段应用于子系统。

#### 提示

- 您指定的内存段应用于生成代码中相应的全局数据结构。有关为原子子系统生成的全局数据结构的基本信息，请参阅 Standard Data Structures (Simulink Coder)。
- 可能的值取决于您为模型配置设置了哪些内存段包（如果有）。请参阅 Control Data and Function Placement in Memory by Inserting Pragmas (Embedded Coder)。
- 如果您尚未为模型配置包，则 `Inherit from model` 是唯一可用的值。否则，列表包括 `Default` 和模型包包含的所有内存段。
- 这些选项可用于覆盖给定子系统的模型内存段设置。有关如何将内存段应用于原子子系统的详细信息，请参阅 Override Default Memory Placement for Subsystem Functions and Data (Embedded Coder)。

#### 依赖关系

- 此参数需要 Embedded Coder 许可证和基于 ERT 的系统目标文件。
- 要启用此参数，请将 **Function packaging** 设置为 `Nonreusable function` 并选择 **Function with separate data** 参数。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RTWMemSecDataParameters` |
| **值：** | `'Inherit from model'`（默认） | `'Default'` | 带引号的模型内存段 |

### Subsystem Reference

### **Subsystem file name** — 被引用子系统的文件名 无默认值

指定要引用的子系统文件。有关子系统引用的信息，请参阅 Create and Use Referenced Subsystems in Models。

#### 依赖关系

要访问此参数，请在 **Subsystem Reference** 部分中点击 **Convert**。

有关如何将子系统转换为被引用子系统的详细信息，请参阅 Convert Subsystem to a Referenced Subsystem。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ReferencedSubsystem` |
| **值：** | `''`（默认） | 带引号的子系统文件名 |
| **数据类型：** | `char` | `string` |
## 所属库

Simulink / Ports & Subsystems

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

实际的代码生成支持取决于模块实现。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2006a 之前引入**

## 描述

执行由外部函数调用输入控制的子系统

Function-Call Subsystem 模块是一个 Subsystem 模块，已预配置为创建子系统的起点，该子系统在函数调用输入端口接收到函数调用事件时执行。Stateflow® 图、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块可以提供函数调用事件。请参阅使用函数调用子系统。

Function-Call Subsystem 模块的内容。

使用 Function-Call Subsystem 模块可以：

- 调度模型组件的执行顺序。
- 控制模型组件的执行速率。

Simulink® 会忽略在 Function-Call Subsystem 模块上设置的任何优先级，但您可以在连接到该子系统函数调用端口的模块上设置优先级。函数调用端口可以从 Stateflow 图、MATLAB Function 模块、Function-Call Generator 模块、S-Function 模块或 Hit Crossing 模块接收函数调用事件。
