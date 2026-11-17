---
type: simulink-block
title: 'Function Element Call'
family: 'ports-subsystems'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functionelementcall'
documentation_source_path: 'slref/functionelementcall.html'
language: zh-CN
chinese_source: worker-translation
---

# Function Element Call

## 端口

### 输出

### **Port\_1** — 从外部端口函数中选择的输入

从父模型的相应外部输入端口中选择一个函数。

## 参数

要编辑与 Function Element Call 模块关联的元素，请在 Simulink Editor 中编辑模块标签。

要编辑端口属性，请使用属性检查器。在 Simulink 工具条中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### 模块标签

### **端口名称** — 调用函数端口的名称 `client`（默认）| 端口名称

指定一个尚未被模型中的另一个模块或端口使用的端口名称。该名称会作为端口标签显示在父 Model 模块上。该名称也会显示在模块旁边。
多个模块可以访问同一端口。

使用相同的端口名称，以点表示法限定通过该端口发出函数调用的 Function Caller 模块的 **函数原型** 参数中的函数名称。

```
[OutArg1,OutArg2,...] = PortName.FunctionElementName(InArg1,InArg2,...)
```

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PortName` |
| **值：** | `'client'`（默认）| 带引号的端口名称 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element Call", PortName="clientPort")`

### **元素** — 可选的函数元素规范 `f1`（默认）| 元素路径

要指定该模块选择的元素，请在 Simulink Editor 中编辑模块标签的第二个文本字段。

多个模块可以访问同一元素。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Element` |
| **值：** | `'f1'`（默认）| 带引号的元素路径 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element Call", Element="f3")`

### 端口选项卡

要切换选项卡是否可见，请点击显示属性或隐藏属性。

有关端口名称的信息，请参阅 **端口名称**。

### **端口号** — 端口在父模块上的位置 `1`（默认）| 实数整数

指定对应于该模块的端口在父 Model 模块上出现的顺序。

- 如果添加一个会创建另一个端口的模块，则端口号是下一个可用编号。
- 删除与某个端口关联的所有模块会删除该端口。软件会重新编号其他端口使其连续，并且不会跳过任何编号。
- 指定超过端口数的端口号会为该编号以及任何跳过的连续编号创建端口。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `'1'`（默认）| 带引号的实数整数 |
| **数据类型：** | `char` | `string` |

**示例：** `set_param("mymodel/Function Element Call", Port="5")`

### 信号选项卡

要切换选项卡是否可见，请点击显示属性或隐藏属性。

指定端口数据类型后，端口名称旁边会出现一个括注。要完整显示指定的数据类型，请点击属性摘要。

*R2025a 之前：要指定端口数据类型，请将鼠标悬停在树中的端口名称上。然后，点击指定属性。或者，在可用时，点击属性摘要。*

### **数据类型** — 端口数据类型 `Inherit: auto`（默认）| `Bus: <object name>` | `ValueType: <object name>`

端口数据类型可以是继承的或指定的。

- `Inherit: auto` — 继承的数据类型。
- `Bus: <object name>` — 使用前面带有 `Bus:` 的 `Simulink.ServiceBus` 对象名称。例如，指定 `Bus: myServiceInterface`。
- `ValueType: <object name>` — 使用前面带有 `ValueType:` 的 `Simulink.ValueType` 对象名称。例如，指定 `ValueType: windVelocity`。`Simulink.ValueType` 对象的数据类型必须是 `Simulink.ServiceBus` 对象。

#### 提示

- 要编辑 `Simulink.ServiceBus` 或 `Simulink.ValueType` 对象，请点击打开类型编辑器。
- 要创建 `Simulink.ServiceBus` 或 `Simulink.ValueType` 对象，请使用架构数据编辑器或接口编辑器 (System Composer)。

#### 以编程方式使用

要通过编程方式设置端口数据类型，请使用 `set_param` 函数。将端口指定为模型名称、正斜杠和端口名称。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `"Inherit: auto"`（默认）| `"Bus: <object name>"` | `"ValueType: <object name>"` |

**示例：** `set_param("mymodel/client", OutDataTypeStr="Bus: ServiceInterface")`

## 所属库

Simulink / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2025a：更轻松地指定端口属性

现在可以更轻松地指定端口属性。

- 要切换端口属性的显示，请点击显示属性或隐藏属性。端口属性现在显示在 **端口** 和 **信号** 选项卡上。显示属性或隐藏属性按钮取代了以前版本中将鼠标悬停在端口名称上时出现的按钮。
- 要编辑端口名称，请双击端口的名称。或者，在 **端口** 选项卡上，指定 **端口名称**。
- 要更改模块颜色，请点击设置与所选元素关联的模块的颜色，然后选择标准颜色或指定自定义颜色。
- 要使用类型编辑器创建 `Simulink.Bus` 对象，请在 **信号** 选项卡上，点击打开类型编辑器。

### R2024a：将模块拖动到新位置时可选择新选项

当您按下 **Ctrl** 并将 Function Element Call 模块拖动到新位置时，会收到更清晰的选项：

- **新端口** — 创建端口。
- **新元素** — 向端口添加元素。
- **复制** — 创建 Function Element Call 模块的副本。

在以前的版本中，您会收到两个选项：

- **创建新端口** — 创建端口。
- **使用现有端口** — 创建 Function Element Call 模块的副本。

### R2024a：添加或复制模块会创建端口

这些操作现在会一致地创建端口：

- 双击画布。然后，开始键入 `Function Element Call`，并从菜单中选择该模块。
- 复制并粘贴 Function Element Call 模块。

在以前的版本中，这些操作会创建端口、向端口添加元素或复制模块。

## 描述

指定要通过调用函数端口发出的函数调用

Function Element Call 模块允许被引用模型中的 Function Caller 模块调用另一个被引用模型中的 Simulink® 函数。当 Function Element Call 模块放置在由 Model 模块引用的模型的根级别时，它会在 Model 模块中创建一个调用函数端口。当该调用函数端口连接到另一个 Model 模块的导出函数端口时，Model 模块中的 Function Caller 模块可以向该另一个 Model 模块中的 Simulink 函数发出函数调用，并通过 Model 模块各自的函数端口接收返回值。

显示 2 个带有函数端口的被引用模型以及连接它们的线的 Simulink 画布。

显示 Function Element Call 模块和 Function-Call Subsystem 模块，且子系统内有一个 Function Caller 模块的 Simulink 画布。

通过使用多个 Function Element Call 模块，被引用模型中的多个 Function Caller 模块可以通过单个调用函数端口发出函数调用。所有使用同一端口的 Function Element Call 模块共享一个对话框。一个模型可以具有多个调用函数端口。

Function Element Call 模块必须放置在指定为导出函数模型的模型的根级别。请参阅导出函数模型概述。
对于每个 Function Element Call 模块，还应在模型的根级别放置一个 Function-Call Subsystem 模块，并在该子系统内放置一个 Function Caller 模块，以指定要通过 Function Element Call 模块调用的函数。
