---
type: simulink-block
title: 'Function Element Call'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'functionelementcall'
---

# Function Element Call

Specify function call to be issued via invoking function port

## 中文

指定要经由调用函数端口发出的函数调用

### 库

Simulink / Ports & Subsystems

### 说明

Function Element Call 模块允许被引用模型中的 Function Caller 模块调用另一个被引用模型中的 Simulink® 函数。当 Function Element Call 模块放置在由 Model 模块引用的模型的根层级时，它会在 Model 模块中创建一个调用函数端口。当调用函数端口连接到另一个 Model 模块的导出函数端口时，该 Model 模块中的 Function Caller 模块可以向该另一个 Model 模块中的 Simulink 函数发出函数调用，并通过这些 Model 模块各自的函数端口接收返回值。

Simulink 画布显示 2 个带有函数端口的被引用模型以及连接它们的线。

Simulink 画布显示 Function Element Call 模块和 Function-Call Subsystem 模块，其中 Function Caller 模块位于该子系统内。

通过使用多个 Function Element Call 模块，被引用模型中的多个 Function Caller 模块可以通过单个调用函数端口发出函数调用。所有使用同一端口的 Function Element Call 模块共享一个对话框。一个模型可以具有多个调用函数端口。

Function Element Call 模块必须放置在指定为导出函数模型的模型的根层级。请参阅 Export-Function Models Overview。对于每个 Function Element Call 模块，还应在模型的根层级放置一个 Function-Call Subsystem 模块，并在该子系统内放置一个 Function Caller 模块，以指定要通过 Function Element Call 模块调用的函数。

### 端口

#### 输出

#### **Port\_1** — 从外部端口函数选择的输入

从父模型的对应外部输入端口中选择一个函数。

### 参数

要编辑与 Function Element Call 模块关联的元素，请在 Simulink 编辑器中编辑模块标签。

要编辑端口属性，请使用 Property Inspector。在 Simulink Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

#### 模块标签

#### **Port name** — 调用函数端口的名称 `client`（默认）| 端口名称

指定一个尚未被模型内其他模块或端口使用的端口名称。该名称作为端口标签显示在父 Model 模块上。该名称也显示在模块旁边。多个模块可以访问同一端口。

使用相同的端口名称，以点表示法限定通过该端口发出函数调用的 Function Caller 模块的 **Function prototype** 参数中的函数名称。

    [OutArg1,OutArg2,...] = PortName.FunctionElementName(InArg1,InArg2,...)

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PortName` |
| **值：** | `'client'`（默认）| 带引号的端口名称 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element Call", PortName="clientPort")`

#### **Element** — 可选的函数元素规格 `f1`（默认）| 元素路径

要指定模块选择的元素，请在 Simulink 编辑器中编辑模块标签的第二个文本字段。

多个模块可以访问同一元素。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Element` |
| **值：** | `'f1'`（默认）| 带引号的元素路径 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element Call", Element="f3")`

#### Port 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

有关端口名称的信息，请参阅 **Port name**。

#### **Port number** — 端口在父模块上的位置 `1`（默认）| 实数整数

指定与该模块对应的端口在父 Model 模块上出现的顺序。

- 如果添加一个会创建另一个端口的模块，端口编号为下一个可用编号。
- 删除与某个端口关联的所有模块会删除该端口。软件会重新将其他端口编号为连续编号，不跳过任何编号。
- 指定一个超过端口数量的端口编号会为该编号以及任何跳过的连续编号创建端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `'1'`（默认）| 带引号的实数整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element Call", Port="5")`

#### Signal 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

指定端口数据类型时，端口名称旁边会出现一个括号说明。要完整显示指定的数据类型，请点击属性摘要。

*R2025a 之前：要指定端口数据类型，请暂停在树中的端口名称上。然后，点击 Specify attributes。或者，在可用时，点击属性摘要。*

#### **Data type** — 端口数据类型 `Inherit: auto`（默认）| `Bus: <object name>` | `ValueType: <object name>`

端口数据类型可以继承或指定。

- `Inherit: auto` — 继承的数据类型。
- `Bus: <object name>` — 使用 `Simulink.ServiceBus` 对象的名称，并在前面加上 `Bus:`。例如，指定 `Bus: myServiceInterface`。
- `ValueType: <object name>` — 使用 `Simulink.ValueType` 对象的名称，并在前面加上 `ValueType:`。例如，指定 `ValueType: windVelocity`。`Simulink.ValueType` 对象的数据类型必须是 `Simulink.ServiceBus` 对象。

#### 提示

- 要编辑 `Simulink.ServiceBus` 或 `Simulink.ValueType` 对象，请点击 Open Type Editor。
- 要创建 `Simulink.ServiceBus` 或 `Simulink.ValueType` 对象，请使用 Architectural Data Editor 或 Interface Editor (System Composer)。

#### 编程用法

要以编程方式设置端口数据类型，请使用 `set_param` 函数。将端口指定为模型名称、正斜杠和端口名称。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"`（默认）| `"Bus: <object name>"` | `"ValueType: <object name>"` |

**示例：** `set_param("mymodel/client", OutDataTypeStr="Bus: ServiceInterface")`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 版本历史

**在 R2022a 中引入**

#### R2025a：更轻松地指定端口属性

现在可以更轻松地指定端口属性。

- 要切换端口属性的显示，请点击 Show attributes 或 Hide attributes。端口属性现在显示在 **Port** 和 **Signal** 选项卡上。Show attributes 或 Hide attributes 按钮取代了以前版本中暂停在端口名称上时出现的按钮。
- 要编辑端口名称，请双击端口的名称。或者，在 **Port** 选项卡上，指定 **Port name**。
- 要更改模块颜色，请点击 Set color of blocks associated with selected elements，并选择标准颜色或指定自定义颜色。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请在 **Signal** 选项卡上点击 Open Type Editor。

#### R2024a：将模块拖到新位置时可选择新选项

当您按下 **Ctrl** 并将 Function Element Call 模块拖到新位置时，会看到更清晰的选项：

- **New Port** — 创建一个端口。
- **New Element** — 向端口添加一个元素。
- **Duplicate** — 创建 Function Element Call 模块的副本。

在以前的版本中，会看到两个选项：

- **Create New Port** — 创建一个端口。
- **Use Existing Port** — 创建 Function Element Call 模块的副本。

#### R2024a：添加或复制模块会创建端口

这些操作现在会一致地创建端口：

- 双击画布。然后，开始键入 `Function Element Call`，并从菜单中选择该模块。
- 复制并粘贴 Function Element Call 模块。

在以前的版本中，这些操作会创建端口、向端口添加元素或复制模块。

## Libraries

Simulink / Ports & Subsystems

## Description

The Function Element Call block allows a Function Caller block
in a referenced model to call a Simulink® function in another referenced model. The Function Element
Call block, when placed at the root level of a model referenced by a
Model block, creates an invoking function port in the
Model block. When the invoking function port is connected to an
exporting function port of another Model block, a Function
Caller block in the Model block can issue function calls to
Simulink functions in that other Model block and receive return
values through the respective function ports of the Model blocks.

Simulink canvas showing 2 referenced models with function ports and a line connecting them.

Simulink canvas showing Function Element Call block and Function-Call Subsystem block, with a Function Caller block inside the subsystem.

By using multiple Function Element Call blocks, multiple Function
Caller blocks in a referenced model can issue function calls through a
single invoking function port. All Function Element Call blocks that use
the same port share a dialog box. A model can have more than one invoking function
port.

A Function Element Call block must be placed at the root level of model
designated as an export-function model. See Export-Function Models Overview.
For each Function Element Call block, a Function-Call
Subsystem block should also be placed at the root level of the model, and a
Function Caller block should be placed inside the subsystem,
designating the function to call through the Function Element Call
block.

## Ports

### Output

### **Port\_1** — Selected input from external port function

Select a function from the corresponding external input port of the
parent model.

## Parameters

To edit the element associated with a
Function Element Call
block, in the Simulink Editor, edit the block label.

To edit port attributes, use the Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of invoking function port `client` (default) | port name

Specify a port name that is not already in use by another block or
port within the model. The name appears as a port label on the parent
Model block. The name also appears next to the block.
Multiple blocks can access the same port.

Use the same port name to qualify, with dot notation, the function name in the
**Function prototype** parameter of the
Function Caller block issuing function calls through
the
port.

```
[OutArg1,OutArg2,...] = PortName.FunctionElementName(InArg1,InArg2,...)
```

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `'client'` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element Call",
PortName="clientPort")`

### **Element** — Optional function element specification `f1` (default) | element path

To specify the element that the block selects, in the Simulink Editor, edit the second text field of the block
label.

Multiple blocks can access the same element.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Element` |
| **Values:** | `'f1'` (default) | element path in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element Call",
Element="f3")`

### Port Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

For information about the port name, see **Port
name**.

### **Port number** — Position of port on parent block `1` (default) | real integer

Specify the order in which the port that corresponds to the block
appears on the parent Model block.

- If you add a block that creates another port, the port
  number is the next available number.
- Deleting all blocks associated with a port deletes the
  port. The software renumbers other ports to be sequential
  and does not skip any numbers.
- Specifying a port number that exceeds the number of ports
  creates a port for that number and for any skipped
  sequential numbers.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Port` |
| **Values:** | `'1'` (default) | real integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element Call",
Port="5")`

### Signal Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify the port data type, a parenthetical appears next to the port
name. To display the specified data type in full, click the attribute
summary.

*Before R2025a: To specify the port data type, pause on the port
name in the tree. Then, click Specify attributes. Alternatively, when available, click the
attribute summary.*

### **Data type** — Port data type `Inherit: auto` (default) | `Bus: <object name>` | `ValueType: <object name>`

The port data type can be inherited or specified.

- `Inherit: auto` — Inherited data
  type.
- `Bus: <object name>` — Use the
  name of the `Simulink.ServiceBus` object preceded
  by `Bus:`. For example, specify
  `Bus: myServiceInterface`.
- `ValueType: <object name>`  — Use
  the name of the `Simulink.ValueType` object
  preceded by `ValueType:`. For example, specify
  `ValueType: windVelocity`. The data
  type of the `Simulink.ValueType` object must be a
  `Simulink.ServiceBus` object.

#### Tips

- To edit a `Simulink.ServiceBus` or
  `Simulink.ValueType` object, click Open Type Editor.
- To create a `Simulink.ServiceBus` or
  `Simulink.ValueType` object, use the
  Architectural Data Editor or Interface Editor (System Composer).

#### Programmatic Use

To programmatically set the port data type, use the `set_param`
function. Specify the port as the model name, a forward slash,
and the port name.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `"Inherit: auto"` (default) | `"Bus: <object name>"` | `"ValueType: <object name>"` |

**Example:** `set_param("mymodel/client",
OutDataTypeStr="Bus:
ServiceInterface")`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2025a: Specify port attributes more easily

You can now specify port attributes more easily.

- To toggle the display of port attributes, click Show attributes or Hide attributes. Port attributes now appear on the
  **Port** and **Signal**
  tabs. The Show attributes or Hide attributes button replaces the button that appears
  when you pause on the port name in a previous release.
- To edit the port name, double-click the name of the port. Alternatively,
  on the **Port** tab, specify **Port
  name**.
- To change block colors, click Set color of blocks associated with selected elements and select a standard color or specify a
  custom color.
- To create a `Simulink.Bus` object using the Type
  Editor, on the **Signal** tab, click Open Type Editor.

### R2024a: Select new options when dragging block to new location

When you press **Ctrl** and drag a Function Element
Call block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — Add an element to the
  port.
- **Duplicate** — Create a duplicate Function
  Element Call block.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — Create a duplicate
  Function Element Call block.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `Function Element
  Call`, and select the block from the menu.
- Copy and paste a Function Element Call block.

In previous releases, these actions create a port, add an element to a port, or
duplicate a block.
