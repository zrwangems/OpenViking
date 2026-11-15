---
type: simulink-block
title: 'Function Element'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'functionelement'
---

# Function Element

Specify function to be called via exporting function port

## 中文

指定要通过导出函数端口调用的函数

### 库

Simulink / Ports & Subsystems

### 说明

Function Element 模块允许由另一个被引用模型中的函数调用方调用某个被引用模型中的 Simulink® 函数。当 Function Element 模块放置在由 Model 模块引用的模型的根层级时，会在 Model 模块中创建一个导出函数端口。当导出函数端口连接到另一个 Model 模块的调用函数端口时，该另一个 Model 模块中的函数调用方可以通过这些 Model 模块各自的函数端口发出函数调用并接收返回值。

Simulink 画布显示 2 个带有函数端口的被引用模型以及连接它们的线。

Simulink 画布显示 Function Element 模块和 Simulink Function 模块。

通过使用多个 Function Element 模块，可以通过单个导出函数端口调用某个被引用模型中的多个 Simulink 函数。使用同一端口的所有 Function Element 模块共享一个对话框。一个模型可以有多个导出函数端口。

Function Element 模块必须放置在指定为 export-function 模型的模型的根层级。请参阅 Export-Function Models Overview。对于每个 Function Element 模块，还应在该模型的根层级放置一个端口作用域的 Simulink Function 模块，用于定义要通过 Function Element 模块调用的函数。

### 端口

#### 输入

#### **Port\_1** — 外部端口函数的完整或部分输出

连接一个函数，以传递到父模型的对应外部输出端口。

### 参数

要编辑与 Function Element 模块关联的元素，请在 Simulink Editor 中编辑模块标签。

要编辑端口属性，请使用 Property Inspector。在 Simulink Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

#### 模块标签

#### **Port name** — 导出函数端口的名称 `server`（默认）| 端口名称

指定一个尚未被另一个端口使用的端口名称。该名称会作为父 Model 模块上的端口标签显示。该名称还会显示在模块旁边。多个模块可以访问同一端口。

在要通过该端口调用的端口作用域 Simulink Function 模块内的 Trigger 模块的 **Scope to port** 参数中，使用相同的端口名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PortName` |
| **值：** | `'server'`（默认）| 带引号的端口名称 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element", PortName="serverPort")`

#### **Element** — 可选的函数元素规范 `f1`（默认）| 元素路径

要指定模块选择的元素，请在 Simulink Editor 中编辑模块标签的第二个文本字段。

每个元素只能由一个模块访问。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Element` |
| **值：** | `'f1'`（默认）| 带引号的元素路径 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element", Element="f3")`

#### Port 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

有关端口名称的信息，请参阅 **Port name**。

#### **Port number** — 端口在父模块上的位置 `1`（默认）| 实整数

指定与该模块对应的端口在父 Model 模块上出现的顺序。

- 如果添加一个会创建另一个端口的模块，端口号是下一个可用的编号。
- 删除与某个端口关联的所有模块会删除该端口。软件会将其他端口重新编号为连续编号，并且不会跳过任何编号。
- 指定一个超过端口数量的端口号会为该编号以及任何被跳过的连续编号创建端口。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `'1'`（默认）| 带引号的实整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element", Port="5")`

#### Signal 选项卡

要切换选项卡是否可见，请点击 Show attributes 或 Hide attributes。

当您指定端口数据类型时，端口名称旁边会出现一个括号注释。要完整显示指定的数据类型，请点击属性摘要。

*在 R2025a 之前：要指定端口数据类型，请在树中暂停在端口名称上。然后，点击 Specify attributes。或者，在可用时，点击属性摘要。*

#### **Data type** — 端口数据类型 `Inherit: auto`（默认）| `Bus: <object name>` | `ValueType: <object name>`

端口数据类型可以继承或指定。

- `Inherit: auto` — 继承的数据类型。
- `Bus: <object name>` — 使用前面带有 `Bus:` 的 `Simulink.ServiceBus` 对象的名称。例如，指定 `Bus: myServiceInterface`。
- `ValueType: <object name>` — 使用前面带有 `ValueType:` 的 `Simulink.ValueType` 对象的名称。例如，指定 `ValueType: windVelocity`。`Simulink.ValueType` 对象的数据类型必须是 `Simulink.ServiceBus` 对象。

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
- 要编辑端口名称，请双击端口名称。或者，在 **Port** 选项卡上，指定 **Port name**。
- 要更改模块颜色，请点击 Set color of blocks associated with selected elements，然后选择标准颜色或指定自定义颜色。
- 要使用 Type Editor 创建 `Simulink.Bus` 对象，请在 **Signal** 选项卡上，点击 Open Type Editor。

#### R2024a：将模块拖到新位置时可选择新选项

当您按下 **Ctrl** 并将 Function Element 模块拖到新位置时，会看到更清晰的选项：

- **New Port** — 创建一个端口。
- **New Element** — 当拖动的模块表示端口的一个元素而不是整个端口时，向该端口添加一个元素。

在以前版本中，会看到两个选项：

- **Create New Port** — 创建一个端口。
- **Use Existing Port** — 当拖动的模块表示端口的一个元素而不是整个端口时，向该端口添加一个元素。否则，创建一个端口。

#### R2024a：添加或复制模块会创建端口

这些操作现在会一致地创建端口：

- 双击画布。然后，开始键入 `Function Element`，并从菜单中选择该模块。
- 复制并粘贴 Function Element 模块。

在以前版本中，这些操作会创建端口或向端口添加元素。

## Libraries

Simulink / Ports & Subsystems

## Description

The Function Element block allows a Simulink® function in a referenced model to be called by a function caller in
another referenced model. The Function Element block, when placed at the
root level of a model referenced by a Model block, creates an exporting
function port in the Model block. When the exporting function port is
connected to an invoking function port of another Model block, a function
caller in that other Model block can issue function calls and receive
return values through the respective function ports of the Model
blocks.

Simulink canvas showing 2 referenced models with function ports and a line connecting them.

Simulink canvas showing Function Element block and Simulink Function block.

By using multiple Function Element blocks, multiple Simulink functions in a referenced model can be called through a single exporting
function port. All Function Element blocks that use the same port share a
dialog box. A model can have more than one exporting function port.

A Function Element block must be placed at the root level of model
designated as an export-function model. See Export-Function Models Overview.
For each Function Element block, a port-scoped Simulink
Function block should also be placed at the root level of the model,
defining the function to be called through the Function Element
block.

## Ports

### Input

### **Port\_1** — Full or partial output for external port function

Connect a function to pass to the corresponding external output port
of the parent model.

## Parameters

To edit the element associated with a
Function Element
block, in the Simulink Editor, edit the block label.

To edit port attributes, use the Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of exporting function port `server` (default) | port name

Specify a port name that is not already in use by another port. The
name appears as a port label on the parent Model block.
The name also appears next to the block. Multiple blocks can access the
same port.

Use the same port name in the **Scope to port**
parameter of the Trigger block inside the port-scoped
Simulink Function block to be called through the
port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `'server'` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element",
PortName="serverPort")`

### **Element** — Optional function element specification `f1` (default) | element path

To specify the element that the block selects, in the Simulink Editor, edit the second text field of the block
label.

Only one block can access each element.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Element` |
| **Values:** | `'f1'` (default) | element path in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element",
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

**Example:** `set_param("mymodel/Function Element",
Port="5")`

### Signal Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify the port data type, a parenthetical appears next to the port name. To
display the specified data type in full, click the attribute summary.

*Before R2025a: To specify the port data type, pause on the
port name in the tree. Then, click Specify attributes. Alternatively, when available, click the
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
block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — When the dragged block represents
  an element of the port and not the full port, add an element to the
  port.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — When the dragged block
  represents an element of the port and not the full port, add an element
  to the port. Otherwise, create a port.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `Function
  Element`, and select the block from the menu.
- Copy and paste a Function Element block.

In previous releases, these actions create a port or add an element to a
port.
