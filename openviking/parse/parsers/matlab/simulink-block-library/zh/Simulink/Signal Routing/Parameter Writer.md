---
type: simulink-block
title: 'Parameter Writer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Signal Routing'
documentation_page: 'parameterwriter'
documentation_source_path: 'slref/parameterwriter.html'
language: zh-CN
chinese_source: worker-translation
---

# Parameter Writer



写入模块参数或变量

## 库

Simulink / Signal Routing

## 说明

Parameter Writer 模块通过写入以下之一来更改模块参数值：

- 仿真期间可调谐的模块参数
- 属于引用某个模型的 Model 模块的实例参数
- 封装子系统参数
- 模型工作区变量
- 基础工作区变量
- 在 `Simulink.data.Dictionary` 中创建的变量

具有可由 Parameter Writer 模块写入的参数的模块称为 *参数所有者模块*。为了让 Parameter Writer 模块找到参数所有者模块支持的参数，必须启用这些支持的参数。

将 Parameter Writer 模块与 Initialize Function、Reinitialize Function 和 Reset Function 模块一起使用，以响应事件。例如，某个事件可以是读取硬件传感器的值，然后基于传感器值更新模块参数。有关使用 Parameter Writer 模块的详细信息，请参阅 Initialize and Reset Parameter Values。

对于封装子系统中的 Parameter Writer 模块，Parameter Writer 模块和对应的参数所有者模块必须具有相同的直接父级封装子系统。

否则，Parameter Writer 模块必须与以下之一位于同一封装中：

- 其参数由 Parameter Writer 模块直接写入的模块，可以是内置模块，例如 Gain 模块、Model 模块、封装子系统模块，或用户定义函数模块，例如 S-Function 模块
- 其参数通过工作区变量间接写入的模块

建议在条件执行子系统内使用 Parameter Writer 模块，以提高仿真性能。有关使用条件执行子系统的详细信息，请参阅 Conditionally Executed Subsystems and Models。

要使用 Parameter Writer 模块写入基础工作区变量、模型工作区变量、在 `Simulink.data.Dictionary` 中创建的变量、封装参数或 Model 模块实例参数，这些变量和参数必须由参数所有者模块或具有运行时可调谐参数的 C MEX S-function 使用。

当 Parameter Writer 模块将数据类型不是 `double`（默认数据类型）的值写入封装参数时，必须使用与 Parameter Writer 模块写入值相同数据类型的值初始化封装参数。要初始化封装参数，请双击该模块以打开封装对话框，指定封装参数的数据类型和值。或者，要以编程方式初始化封装参数，请将 **MaskValues** 参数与 `set_param` 函数一起使用。有关详细信息，请参阅 Control Masks Programmatically。

在所示示例中，Parameter Writer 模块将数据类型为 `single` 的值写入封装子系统内 Gain 模块的模块参数。封装参数初始化为 1，数据类型为 `single`。

当 Parameter Writer 模块将数据类型不是 double 的数据写入封装子系统内参数时的封装参数值设置

当 Parameter Writer 模块写入存储类设置为 `Model default` 的实例参数时，代码生成器在为该参数生成代码时会使用 **Model parameter arguments** 的默认配置。请参阅 Specify Instance-Specific Parameter Values for Reusable Referenced Model (Simulink Coder)。

**注意**

创建包含 Parameter Writer 模块的库模块时，还必须在该库模块中包含对应的参数所有者模块。除了使用 Create Custom Library 中所述工作流创建的自定义库模块之外，Simulink® 还会将使用 Subsystem Reference 模块创建的模型组件视为单模块库。

### 识别参数所有者模块

你可以通过 `IsParamOwnerBlock` 模块参数的值确定某个模块是否是支持的参数所有者模块。使用 `get_param` 函数，并传入模块名称或句柄 `blk` 以及 `IsParamOwnerBlock` 模块参数。

    get_param(blk,'IsParamOwnerBlock')

如果该模块是支持的参数所有者模块，该函数返回 `'on'`；否则返回 `'off'`。

Parameter Writer 模块与该模块所写入值的参数所有者模块构成一组相关模块。你可以选择 Parameter Writer 模块以突出显示相关的参数所有者模块，反之亦然。突出显示相关模块时，当前模型中包含该相关模块的模块也会突出显示。例如，当 Initialize Function 模块包含与所选模块相关的 Parameter Writer 模块时，该 Initialize Function 模块会突出显示。在模型画布中突出显示的模块也会在小地图中突出显示。

要在打开的图或新选项卡中显示相关模块，请在选择后出现的省略号上暂停。然后，从操作栏中选择 **Related Blocks** 按钮。窗口焦点将转到显示相关模块的已打开图或新选项卡。

## 端口

### 输入

### **In** — 参数值 标量 | 向量

由该模块写入的参数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Validate parameter** — 在正常模式仿真期间验证参数的选项 `on`（默认） | `off`

*自 R2023a 起*

为此模块局部启用参数验证。

为 Parameter Writer 模块禁用参数验证后，该模块的正常模式仿真会更快。

#### 提示

要为 Parameter Writer 模块全局启用或禁用参数验证，请使用 **Parameter Writer block validation** 配置参数。

#### 依赖关系

要禁用此模块的参数验证，该模块不得直接或间接更改 Model 模块实例参数的值。例如，该模块不得更改用于指定 Model 模块实例参数值的变量或封装参数的值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `IsParameterValidationOn` |
| **值：** | `'on'` (default) | `'off'` |

**示例：** `set_param(gcb,'IsParameterValidationOn','off')`

### **Destination** — 写入变量和参数的选项 `Block parameter`（默认） | `Model workspace variable` | `Base workspace variable`

*自 R2024a 起*

写入模块参数、模型工作区变量、基础工作区变量，或你在 `Simulink.data.Dictionary` 中创建的变量。选择以下选项之一：

- `Block parameter` — 写入模块参数。
- `Model workspace variable` — 写入模型工作区中的变量。
- `Base workspace variable` — 写入基础工作区中的变量，或你在 `Simulink.data.Dictionary` 中创建的变量。

**注意**

- **Destination** 参数取代 **Access model workspace parameter** 参数。
- 你可以使用放置在条件执行子系统内或 Initialize Function 模块、Reinitialize Function 模块、Reset Function 模块中的 Parameter Writer 模块，在仿真或生成代码执行期间切换活动变体。根据变体控制变量的位置设置 **Destination** 参数，并选择 **Validate parameter**。有关详细信息，请参阅 Variant Subsystem。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Destination` |
| **值：** | `'Block parameter'` (default) | `'Model workspace variable'` | `'Base workspace variable'` |

**示例：** `set_param(gcb, Destination="Block parameter")`

### **Workspace variable name** — 工作区变量的名称 无默认值

指定此模块写入其值的工作区变量的名称。

**注意**

**Workspace variable name** 参数取代现有的 **Model workspace parameter name** 参数。*（自 R2023b 起）*

#### 依赖关系

要启用此参数，请从 **Destination** 参数选项中选择 `Model workspace variable` 或 `Base workspace variable`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WorkspaceVariableName` |
| **值：** | `''` (default) | character vector | string scalar |

**示例：** `set_param(gcb,'WorkspaceVariableName','var')`

### **Parameter owner block** — 参数所有者模块的模块路径和模块参数名称 无默认值

指定参数所有者模块的模块路径，以及此模块写入其值的参数名称。

**Parameter Owner Selector Tree** 以分层树列表形式提供可写参数。展开通往参数所有者模块的路径上的节点。然后，选择参数所有者模块下的参数。

#### 提示

如果参数所有者模块的名称包含斜杠 (`/`)，则该斜杠在 Parameter Writer 模块参数中显示为两个斜杠 (`//`)。此表示法将模块名称本身的斜杠与用于分隔模型层级中不同级别名称的斜杠区分开。

#### 依赖关系

要启用此参数，请从 **Destination** 参数列表中选择 `Block parameter` 选项。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

首先，使用 `ParameterOwnerBlock` 参数指定参数所有者模块的模块路径。

|  |  |
| --- | --- |
| **参数：** | `ParameterOwnerBlock` |
| **值：** | `''` (default) | character vector | string scalar |
| **数据类型：** | `char` | `string` |

**示例：** `set_param(gcb,'ParameterOwnerBlock','mymodel/Gain1')`

然后，使用 `ParameterName` 参数指定参数所有者模块的模块参数的编程名称。

|  |  |
| --- | --- |
| **参数：** | `ParameterName` |
| **值：** | `''` (default) | character vector | string scalar |

**示例：** `set_param(gcb,'ParameterName','Gain')`

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

### R2024a：写入基础工作区变量和数据字典中的变量

现在，除了模型工作区变量和模块参数之外，你还可以使用此模块写入基础工作区变量以及你在数据字典中创建的变量。使用 **Destination** 参数指定要写入变量还是模块参数。在 R2024a 之前，你只能使用此模块写入模型工作区变量或模块参数。

### R2023b：写入不可见的封装子系统参数

无论封装对话框是否显示该参数，Parameter Writer 模块都可以写入已启用的封装子系统参数。

### R2023a：在正常模式仿真期间禁用参数验证

（可选）为 Parameter Writer 模块禁用正常模式仿真期间发生的参数验证。为 Parameter Writer 模块禁用参数验证后，该模块的正常模式仿真会更快。

要为 Parameter Writer 模块局部启用或禁用参数验证，请使用 **Validate parameter** 模块参数。

要为 Parameter Writer 模块全局启用或禁用参数验证，请使用 **Parameter Writer block validation** 配置参数。
