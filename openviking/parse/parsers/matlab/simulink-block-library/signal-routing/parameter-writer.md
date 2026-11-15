---
type: simulink-block
title: 'Parameter Writer'
family: signal-routing
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'parameterwriter'
---

# Parameter Writer

Write to block parameter or variable

## 中文

写入模块参数或变量

### 库

Simulink / Signal Routing

### 说明

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

#### 识别参数所有者模块

你可以通过 `IsParamOwnerBlock` 模块参数的值确定某个模块是否是支持的参数所有者模块。使用 `get_param` 函数，并传入模块名称或句柄 `blk` 以及 `IsParamOwnerBlock` 模块参数。

    get_param(blk,'IsParamOwnerBlock')

如果该模块是支持的参数所有者模块，该函数返回 `'on'`；否则返回 `'off'`。

Parameter Writer 模块与该模块所写入值的参数所有者模块构成一组相关模块。你可以选择 Parameter Writer 模块以突出显示相关的参数所有者模块，反之亦然。突出显示相关模块时，当前模型中包含该相关模块的模块也会突出显示。例如，当 Initialize Function 模块包含与所选模块相关的 Parameter Writer 模块时，该 Initialize Function 模块会突出显示。在模型画布中突出显示的模块也会在小地图中突出显示。

要在打开的图或新选项卡中显示相关模块，请在选择后出现的省略号上暂停。然后，从操作栏中选择 **Related Blocks** 按钮。窗口焦点将转到显示相关模块的已打开图或新选项卡。

### 端口

#### 输入

#### **In** — 参数值 标量 | 向量

由该模块写入的参数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 参数

#### **Validate parameter** — 在正常模式仿真期间验证参数的选项 `on`（默认） | `off`

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

#### **Destination** — 写入变量和参数的选项 `Block parameter`（默认） | `Model workspace variable` | `Base workspace variable`

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

#### **Workspace variable name** — 工作区变量的名称 无默认值

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

#### **Parameter owner block** — 参数所有者模块的模块路径和模块参数名称 无默认值

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

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 版本历史

#### R2024a：写入基础工作区变量和数据字典中的变量

现在，除了模型工作区变量和模块参数之外，你还可以使用此模块写入基础工作区变量以及你在数据字典中创建的变量。使用 **Destination** 参数指定要写入变量还是模块参数。在 R2024a 之前，你只能使用此模块写入模型工作区变量或模块参数。

#### R2023b：写入不可见的封装子系统参数

无论封装对话框是否显示该参数，Parameter Writer 模块都可以写入已启用的封装子系统参数。

#### R2023a：在正常模式仿真期间禁用参数验证

（可选）为 Parameter Writer 模块禁用正常模式仿真期间发生的参数验证。为 Parameter Writer 模块禁用参数验证后，该模块的正常模式仿真会更快。

要为 Parameter Writer 模块局部启用或禁用参数验证，请使用 **Validate parameter** 模块参数。

要为 Parameter Writer 模块全局启用或禁用参数验证，请使用 **Parameter Writer block validation** 配置参数。

## Libraries

Simulink / Signal Routing

## Description

The Parameter Writer block changes block parameter values by writing to
one of the following:

- A parameter of a block that is tunable during simulation
- An instance parameter that belongs to a Model block that references a
  model
- A masked subsystem parameter
- A model workspace variable
- A base workspace variable
- A variable created in `Simulink.data.Dictionary`

A block with a parameter that can be written by a Parameter Writer block is
called a *parameter owner block*. For the Parameter
Writer block to find the supported parameters of a parameter owner block,
the supported parameters must be enabled.

Use the Parameter Writer block with the Initialize
Function, Reinitialize Function, and Reset
Function blocks to respond to events. For example, an event could be reading
the value from a hardware sensor and then updating a block parameter based on the sensor
value. For more information about using the Parameter Writer block, see
Initialize and Reset Parameter
Values.

For a Parameter Writer block in a masked subsystem, the
Parameter Writer block and corresponding parameter owner block must
have the same immediate parent masked subsystem.

Otherwise, a Parameter Writer block must be in the same mask as either:

- The block whose parameter is directly written by the Parameter
  Writer block, which could be a built-in block such as a
  Gain block, a Model block, a masked
  subsystem block, or a User-Defined Functions block such as an
  S-Function block
- The block whose parameter is indirectly written through a workspace
  variable

It is recommended to use the Parameter Writer block inside a conditionally
executed subsystem to improve the simulation performance. For more information about
using conditionally executed subsystems, see Conditionally Executed Subsystems and Models.

To write to a base or model workspace variable, a variable created in
`Simulink.data.Dictionary`, mask parameter, or Model
block instance parameter with a Parameter Writer block, the variables and
the parameters must be used by a parameter owner block or C MEX S-function with run-time
tunable parameters.

When a Parameter Writer block writes values with data type other than
`double` (the default data type) to a mask parameter, you must
initialize the mask parameter with a value of the same data type as the value written by
the Parameter Writer block. To initialize the mask parameter,
double-click the block to open the mask dialog box, specify the data type and value of
the mask parameter. Alternatively, to initialize mask parameter programmatically, use
**MaskValues** parameter with `set_param`
function. For more information, see Control Masks Programmatically.

In this example shown, a Parameter Writer block writes a value with data type
`single` to a Gain  block parameter inside a masked
subsystem. The mask parameter is initialized to 1 with data type
`single`.

Mask parameter value setting when Parameter Writer block writes data with datatype other then double to a parameter inside a masked subsystem

When a Parameter Writer block writes to an instance parameter with storage
class set to `Model default`, the code generator uses the
default configuration for **Model parameter arguments** when generating
code for the parameter. See Specify Instance-Specific Parameter Values for Reusable Referenced Model (Simulink Coder).

**Note**

When you create a library block with a Parameter Writer block, you
must also include the corresponding parameter owner block in the library block. In
addition to custom library blocks created using the workflow mentioned in Create Custom Library, Simulink® treats model components created using Subsystem Reference block as a one-block library.

### Identify Parameter Owner Blocks

You can determine whether a block is a supported parameter owner block by the value of
the `IsParamOwnerBlock` block parameter. Use the
`get_param` function with the block name or handle,
`blk`, and the `IsParamOwnerBlock` block
parameter.

```
get_param(blk,'IsParamOwnerBlock')
```

The function returns `'on'` if the block is a supported parameter owner
block and `'off'` otherwise.

A Parameter Writer block and the parameter owner block of the value that
the block writes constitute a set of related blocks. You can select a Parameter
Writer block to highlight the related parameter owner block or vice versa. When a
related block is highlighted, blocks in the current model that contain the related block are
also highlighted. For example, an Initialize Function block is highlighted
when it contains a Parameter Writer block that is related to the selected
block. The blocks that are highlighted in the model canvas are also highlighted in the
miniature map.

To show a related block in an open diagram or new tab, pause on the ellipsis that appears
after selection. Then, select the **Related Blocks** button
 from the action bar. Window focus goes to the
open diagram or new tab that shows the related block.

## Ports

### Input

### **In** — Parameter value scalar | vector

Parameter value written by the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Validate parameter** — Option to validate parameter during normal mode simulation `on` (default) | `off`

*Since R2023a*

Locally enable parameter validation for this block.

When parameter validation is disabled for a Paramer Writer block,
normal mode simulation of the block is faster.

#### Tips

To globally enable or disable parameter validation for Parameter
Writer blocks, use the **Parameter Writer
block validation** configuration parameter.

#### Dependencies

To disable parameter validation for this block, the block must not directly or
indirectly change the value of a Model block instance
parameter. For example, the block must not change the value of variable
or mask parameter that specifies the value of a Model
block instance parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `IsParameterValidationOn` |
| **Values:** | `'on'` (default) | `'off'` |

**Example:** `set_param(gcb,'IsParameterValidationOn','off')`

### **Destination** — Option to write to variables and parameters `Block parameter` (default) | `Model workspace variable` | `Base workspace variable`

*Since R2024a*

Write to block parameters, model workspace variables, base workspace variables, or
variables you create in `Simulink.data.Dictionary`.
Select one of these options:

- `Block parameter` — Write to block
  parameters.
- `Model workspace variable` — Write to
  variables in the model workspace.
- `Base workspace variable` — Write to
  variables in the base workspace or variables you create in
  `Simulink.data.Dictionary`.

**Note**

- The **Destination** parameter replaces
  the **Access model workspace parameter**
  parameter.
- You can switch the active variant during simulation or
  execution of the generated code by using the Parameter Writer block placed inside a
  conditionally executed subsystem or in an Initialize
  Function block, a Reinitialize Function block, a Reset
  Function block. Set the
  **Destination** parameter based on the
  location of your variant control variable and select the
  **Validate parameter**. For more
  information see Variant
  Subsystem.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Destination` |
| **Values:** | `'Block parameter'` (default) | `'Model workspace variable'` | `'Base workspace variable'` |

**Example:** `set_param(gcb, Destination="Block parameter")`

### **Workspace variable name** — Name of the workspace variable no default

Specify the name of the workspace variable whose value this block writes.

**Note**

The **Workspace
variable name** parameter replaces the existing
**Model workspace parameter name**
parameter. *(since R2023b)*

#### Dependencies

To enable this parameter, select the `Model workspace
variable` or `Base workspace
variable` from the **Destination**
parameter options.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WorkspaceVariableName` |
| **Values:** | `''` (default) | character vector | string scalar |

**Example:** `set_param(gcb,'WorkspaceVariableName','var')`

### **Parameter owner block** — Block path of parameter owner block and name of block parameter no default

Specify the block path of the parameter owner block and the name of the parameter
whose value this block writes.

The **Parameter Owner Selector Tree** provides the writable
parameters in a hierarchical tree list. Expand the nodes on the path to the parameter
owner block. Then, select the parameter under the parameter owner block.

#### Tips

If the name of a parameter owner block contains a slash (`/`),
the slash appears as two slashes (`//`) in the Parameter
Writer block parameters. This notation distinguishes the slash in the block
name itself from slashes that separate names at different levels of the model
hierarchy.

#### Dependencies

To enable this parameter, select the `Block parameter` option
from the **Destination** parameter list.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

First, specify the block path of a parameter owner block using the
`ParameterOwnerBlock`
parameter.

|  |  |
| --- | --- |
| **Parameter:** | `ParameterOwnerBlock` |
| **Values:** | `''` (default) | character vector | string scalar |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'ParameterOwnerBlock','mymodel/Gain1')`

Then, specify the programmatic name of a block parameter of the parameter owner
block using the `ParameterName`
parameter.

|  |  |
| --- | --- |
| **Parameter:** | `ParameterName` |
| **Values:** | `''` (default) | character vector | string scalar |

**Example:** `set_param(gcb,'ParameterName','Gain')`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

### R2024a: Write to base workspace variable and variables in data dictionary

You can now use this block to write to base workspace variables and variables you create in
a data dictionary in addition to model workspace variables and block parameters. Use
the **Destination** parameter to specify whether you want to
write to a variable or a block parameter. Before R2024a, you could use this block to
write to model workspace variables or block parameters only.

### R2023b: Write to invisible masked subsystem parameters

A Parameter Writer block can write to a masked subsystem parameter that is enabled regardless of whether the mask dialog box displays the parameter.

### R2023a: Disable parameter validation during normal mode simulation

Optionally, disable parameter validation that occurs during normal mode simulation for
Parameter Writer blocks. When parameter validation is disabled for a
Parameter Writer block, normal mode simulation of the block is
faster.

To locally enable or disable parameter validation for a Parameter Writer
block, use the **Validate parameter** block parameter.

To globally enable or disable parameter validation for Parameter Writer
blocks, use the **Parameter Writer block
validation** configuration parameter.
