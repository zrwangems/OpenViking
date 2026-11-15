---
type: simulink-block
title: 'Function-Call Split'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'functioncallsplit'
---

# Function-Call Split

Provide junction for splitting function-call line

## 中文

提供联接点以用于拆分函数调用信号线

### 所属库

Simulink / Ports & Subsystems

### 描述

Function-Call Split 模块允许对函数调用信号线进行拆分，再把拆分后的分支信号连接到多个函数调用子系统或函数调用模型。

对于 Function-Call Split 模块所连接的各个输出端口，带有圆点标记的输出端口所连接的函数调用子系统或函数调用模型会先执行，而其他输出端口所连接的子系统或模型会在其后执行。如果子系统或模型之间的数据依赖关系不支持指定的执行顺序，Function-Call Split 模块会返回错误。要避免此错误，请考虑在数据依赖关系循环涉及的函数调用子系统或模型的一个或多个 Inport 模块上选择**针对函数调用子系统输出的反馈信号锁存输入**参数。选择此选项会延迟对应的函数调用，从而消除数据依赖关系循环。

要显示连接到给定函数调用信号分支的函数调用子系统的执行顺序，请在 Simulink 编辑器的**调试**选项卡上，选择**叠加信息**并点击**执行顺序**。Simulink 画布上将打开一个窗格，显示**执行顺序模块列表**。在该列表中，函数调用子系统的执行顺序以 [`n`]←[`m`] `subsystem block name` 形式表示，其中：

- `n` 表示子系统的执行顺序。
- `m` 表示生成函数调用信号的模块的执行顺序。
- `subsystem block name` 表示函数调用子系统的名称。

Function-Call Split 模块支持信号标签传播。

以下模型显示如何应用**针对函数调用子系统输出的反馈信号锁存输入**参数以解决 Function-Call Split 模块导致的数据依赖关系错误。通过在 `f1` 子系统的 Inport 模块中启用此参数，Function-Call Split 模块将忽略信号 b 的数据依赖关系。此模块将打破子系统 `f1` 和 `g1` 之间的数据依赖关系循环。该模型可确保先调用 f1 来执行，再执行 g1。对于给定的执行步，子系统 `f1` 使用在上一个执行步中计算的 `g1` 输出。

### 端口

#### 输入

#### **Function Call** — 函数调用信号线 标量

Function-Call Generator 模块、S-Function 模块、Hit Crossing 模块或 Stateflow® 图可以提供函数调用事件。
#### 输出

#### **Function Call** — 函数调用信号 标量

连接到函数调用子系统或函数调用模型的函数调用信号线。

### 参数

#### **图标形状** — 选择模块图标形状 **不同** (默认) | **舍入**

选择模块图标形状。

##### 设置

**不同**
:   矩形模块图标。

**舍入**
:   圆形模块图标。

##### 编程用法

|  |
| --- |
| **模块参数**：`IconShape` |
| **类型**：字符向量 |
| **值**：`'distinctive'` | `'round'` |
| **默认值：**`'distinctive'` |

#### **输出端口数量** — 指定输出端口数量 `2` (默认) | 整数

指定函数调用信号输出端口的数量。

##### 设置

`2`
:   两个函数调用输出端口。

整数
:   整数

##### 编程用法

|  |
| --- |
| **模块参数**：`NumOutputPorts` |
| **类型**：字符向量 |
| **值**：`'2'` | `'<integer>'` |
| **默认值**：`'2'` |

#### **输出端口布局** — 选择输出端口的顺序 **默认** (默认) | **反向**

选择函数调用输出端口的顺序，确定哪个端口先提供函数调用信号。

##### 设置

**默认**
:   位于顶部的端口先提供函数调用。

**反向**
:   位于底部的端口先提供函数调用。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutputPortLayout` |
| **类型**：字符向量 |
| **值**：`'default'` | `'reverse'` |
| **默认值：**`'default'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2010a 中推出**

## Libraries

Simulink / Ports & Subsystems

## Description

The Function-Call Split block allows a function-call line to branch and
connect to several function-call subsystems or function-call models.

The function-call subsystem or function-call model connected to the output port of the
Function-Call Split block that is marked with a dot executes before
the subsystems or models connected to other output ports. If data dependencies between
subsystems or models do not support the specified execution order, the
Function-Call Split block returns an error. To eliminate this error,
consider selecting the **Latch input for feedback signals of function-call
subsystem outputs** parameter on one or more Inport blocks
of the function-call subsystems or models involved in a data-dependency loop. Selecting
this option delays the corresponding function-call, thereby eliminating the
data-dependency loop.

To display the execution order of function-call subsystems connected to branches of a
given function-call signal, in the Simulink Editor, on the **Debug**
tab, select **Information Overlays** and click **Execution
Order**. A pane opens on the Simulink canvas that represents the
**Execution Order Block List**. In the list, the execution order of
the function-call subsystems is represented in the form
[`n`]←[`m`] `subsystem block
name`, where:

- `n` indicates the execution order of the
  subsystem.
- `m` indicates the execution order of the block that
  generates the function-call signal.
- `subsystem block name` indicates the name of the
  function-call subsystem.

The Function-Call Split block supports Signal Label Propagation.

The following model shows how to apply the **Latch input for feedback signals
of function-call subsystem outputs** parameter to work around a
data-dependency error caused by a Function-Call Split block. By turning
this parameter on in the `f1` subsystem's Inport block,
the Function-Call Split block ignores the data dependency of signal b.
The block breaks the loop of data dependencies between subsystems `f1`
and `g1`. The model achieves the behavior of consistently calling f1 to
execute before g1. For a given execution step, subsystem `f1` uses the
`g1` output computed at the previous execution step.

## Ports

### Input

### **Function Call** — Function-call line scalar

A Function-Call Generator block, an
S-Function block, a Hit Crossing
block, or a Stateflow® chart can provide function-call events.
### Output

### **Function Call** — Function-call signal scalar

Function-call line connected to a function-call subsystem or
function-call model.

## Parameters

### **Icon shape** — Select block icon shape `distinctive` (default) | `round`

Select block icon shape.

#### Settings

`distinctive`
:   Rectangular block icon.

`round`
:   Circular block icon.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IconShape` |
| **Type**: character vector |
| **Values**: `'distinctive'` | `'round'` |
| **Default**: `'distinctive'` |

### **Number of output ports** — Specify number of output ports `2` (default) | integer

Specify the number of function-call signal output ports.

#### Settings

`2`
:   Two function-call output ports.

integer
:   Integer number

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumOutputPorts` |
| **Type**: character vector |
| **Values**: `'2'` | `'<integer>'` |
| **Default**: `'2'` |

### **Output port layout** — Select order of output ports `default` (default) | `reverse`

Select the order of function-call output ports with respect to which port
provides a function-call first.

#### Settings

`default`
:   Top port provides function-call first.

`reverse`
:   Bottom port provides function-call first.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputPortLayout` |
| **Type**: character vector |
| **Values**: `'default'` | `'reverse'` |
| **Default**: `'default'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2010a**
