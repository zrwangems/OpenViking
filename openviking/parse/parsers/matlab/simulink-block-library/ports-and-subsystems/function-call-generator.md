---
type: simulink-block
title: 'Function-Call Generator'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'functioncallgenerator'
---

# Function-Call Generator

Provide function-call events to control execution of subsystem or model

## 中文

提供函数调用事件来控制子系统或模型的执行

### 所属库

Simulink / Ports & Subsystems

### 描述

Function-Call Generator 模块提供函数调用事件，用于以您在**采样时间**参数中指定的速率执行函数调用子系统或函数调用模型。函数调用子系统或函数调用模型是包含 Trigger 模块的子系统或模型，其**触发器类型**参数设置为**函数调用**。

要以迭代方式在每个时间步中多次执行每个函数调用子系统或函数调用模型，请使用**迭代次数**参数。

要以指定的顺序执行多个函数调用子系统或函数调用模型，请结合使用 Function-Call Split 模块和 Function-Call Generator 模块。有关示例，请参阅 Function-Call Split。

要间歇地（意味着不是在每个时间步）执行函数调用子系统或函数调用模型，请选择**显示使能端口**参数。然后，您可以使用使能端口的输入来控制模块何时输出函数调用事件。实际上，您可以根据需要打开和关闭模块。

**注意**

从 R2025a 开始，Function-Call Generator 模块不再作为封装链接模块运行。要以编程方式在模型中定位此模块，请使用命令 `find_system('BlockType','FunctionCallGenerator')`。当从其他版本更新到 R2025a 时，建议修复任何与 Simulink® 库的链接已断开的 Function-Call Generator 模块。否则，该模块将不会更新，并会在更新后的模型中继续作为封装模块运行。此模块的封装行为将在以后的版本中删除。有关识别模型中断开的库链接的详细信息，请参阅显示库链接。

对于 R2025a 之前的版本，要以编程方式在模型中定位此模块，请使用命令 `find_system('MaskType','Function-Call Generator')`。

### 端口

#### 输入

#### **Enable** — 控制信号输入 标量

仅当此端口的输入为正数时，此模块才输出函数调用事件。

##### 依赖关系

要启用此端口，请选中**显示使能端口**复选框。
#### 输出

#### **Function Call** — 函数调用事件输出 标量 | 向量

将函数调用事件发送到函数调用子系统或函数调用模型的函数调用输入端口。

### 参数

#### **采样时间** — 指定时间间隔 `1` (默认) | 标量 | 向量 | `-1`

指定函数调用子系统或含调用模型的函数调用事件之间的时间间隔。如果子系统或模型的实际调用速率与此参数指定的时间间隔不同，Simulink 将显示错误。

默认情况下，该模块使用的时间间隔为 `1`。要设置不同时间间隔，请根据采样时间的类型中的表输入有效的采样时间，或指定 `-1` 从模型中继承时间间隔。

##### 依赖关系

要启用此参数，请清除**显示使能端口**复选框。如果选择**显示使能端口**，采样时间将自动设置为 `-1`（继承）。

##### 编程用法

|  |
| --- |
| **模块参数**：`sample_time` |
| **类型**：字符向量 |
| **值**：`'1'` | 标量表达式 | 向量表达式 | `'-1'` |
| **默认值**：`'1'` |

#### **迭代次数** — 指定在每个时间步中提供函数调用的次数 `1` (默认) | 整数

此参数的值可以是向量，向量的每个元素指定执行函数调用子系统或模型的次数。如果指定向量，则该模块输出函数调用事件的向量，该向量可以使用 Demux 模块拆分成单个函数调用事件，并用于驱动多个函数调用子系统或模型。

假设您将**迭代次数**指定为 `[3 2]`，并将此模块的输出连接到 Demux 模块，后者又连接到两个函数调用子系统的控制端口。在本例中，第一个函数调用子系统在每个时间步执行三次，第二个函数调用子系统在每个时间步执行两次。

但是，如果您将此模块的输出连接到单个函数调用子系统或模型，则函数调用子系统或模型在每时间步执行的总次数等于向量元素值的总和。因此，在上面的示例中，将**迭代次数**指定为 `[3 2]` 并将此模块的输出连接到单个函数调用子系统，会导致函数调用子系统在每个时间步执行五次。

##### 设置

`1`
:   在每个时间步期间提供一次函数调用。

整数
:   有符号或无符号整数。在每个时间步提供指定数量的函数调用。

##### 编程用法

|  |
| --- |
| **模块参数**：`numberOfIterations` |
| **类型**：字符向量 |
| **值**：`'1'` | 用引号引起来的整数 | 用引号引起来的整数向量 |
| **默认值**：`'1'` |

#### **不允许宽输出** — 防止输出信号的隐式扩展 `off` (默认) | `on`

除非选择此参数，否则此模块的输出将扩展为向量，以在必要时驱动连接到它的模块。例如，如果**迭代次数**设置为 `2`，并且未选择**不允许宽输出**，并且此模块的输出连接到 Demux 模块，此模块又连接到三个单独的函数调用子系统，则每个函数调用子系统在每个时间步接收两个函数调用事件。如果此模块的输出连接到具有多个事件的 Stateflow® 图，也会出现类似的结果。如果在这些情况下选择**不允许宽输出**，则软件会生成错误。

选择此参数可防止隐式扩展输出信号。

清除此参数可允许在适当时隐式扩展输出信号。

##### 编程用法

|  |
| --- |
| **模块参数**：`DisallowWideOutput` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

#### **显示使能端口** — 添加控制信号的输入端口 `off` (默认) | `on`

选择此参数可向模块添加控制信号输入端口。仅当控制信号输入端口的值为正数时，该模块才输出函数调用事件。

清除此参数可删除控制信号输入端口。该模块在每个时间步输出函数调用事件。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowEnablePort` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2006a 之前推出**

#### R2025a: Function-Call Generator 模块不再作为链接封装模块运行

Function-Call Generator 模块现在作为内置模块运行。对于 R2025a 之前的版本，该模块作为封装链接模块运行。此模块行为的更改使模块在仿真期间执行速度更快。

## Libraries

Simulink / Ports & Subsystems

## Description

The Function-Call Generator block provides function-call events that
execute a function-call subsystem or function-call model at the rate you specify with
the **Sample time** parameter. A function-call subsystem or
function-call model is a subsystem or model containing a Trigger block
with its **Trigger type** parameter set to
`function-call`.

To iteratively execute each function-call subsystem or function-call model multiple
times at each time step, use the **Number of iterations**
parameter.

To execute multiple function-call subsystems or function-call models in a specified
order, use the Function-Call Generator block with a Function-Call
Split block. For an example, see Function-Call Split.

To execute a function-call subsystem or function-call model intermittently, meaning
not at every time step, select the **Show enable port** parameter. You
can then use the input at the enable port to control when the block outputs
function-call events. In effect, you can turn the block on and off as needed.

**Note**

Starting in R2025a, the Function-Call Generator block no longer
behaves as a masked, linked block. To locate this block in a model programmatically,
use the command `find_system('BlockType','FunctionCallGenerator')`.
When you update from another release to R2025a, it is recommended that you fix any
Function-Call Generator block whose link to a Simulink® library is broken. Otherwise, the block will not be updated, and it
will continue to behave as a masked block in the updated model. The mask behavior of
this block will be removed in a future release. For more information about
identifying broken library links in a model, see Display Library Links.

For versions prior to R2025a, to locate this block in a model programmatically,
use the command `find_system('MaskType','Function-Call
Generator')`.

## Ports

### Input

### **Enable** — Control signal input scalar

The block outputs function-call events only when the input at this
port is a positive number.

#### Dependencies

To enable this port, select the **Show enable
port** check box.
### Output

### **Function Call** — Function-call event output scalar | vector

Sends function-call events to the function-call input port of a
function-call subsystem or function-call model.

## Parameters

### **Sample time** — Specify time interval `1` (default) | scalar | vector | `-1`

Specify the time interval between function-call events to a function-call
subsystem or function-call model. If the actual calling rate for the
subsystem or model differs from the time interval this parameter specifies,
Simulink displays an error.

By default, the block uses a time interval of `1`. To set
a different interval, enter a valid sample time based on the table in Types of Sample Time, or
specify `-1` to inherit the time interval from the
model.

#### Dependencies

To enable this parameter, clear the **Show enable
port** check box. If you select **Show enable
port**, sample time is automatically set to
`-1` (inherited).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sample_time` |
| **Type**: character vector |
| **Values**: `'1'` | scalar expression | vector expression | `'-1'` |
| **Default**: `'1'` |

### **Number of iterations** — Specify number of times to provide a function-call at each time step `1` (default) | integer

The value of this parameter can be a vector, where each element of the
vector specifies a number of times to execute a function-call subsystem or
model. If a vector is specified, then the block outputs a vector of
function-call events, which can be split into individual function-call
events using a Demux block and used to drive
multiple function-call subsystems or models.

Suppose that you specify **Number of iterations** to be
`[3 2]` and connect the output of this block to a
Demux block, which is connected to the control ports of
two function-call subsystems. In this case, the first function-call
subsystem executes three times at each time step, and the second
function-call subsystem executes two times at each time step.

If, however, you connect the output of this block to a single
function-call subsystem or model, the total number of times that the
function-call subsystem or model executes per time step is equal to the sum
of the vector element values. So in the example above, specifying
**Number of iterations** to be `[3 2]`
and connecting the output of this block to a single function-call subsystem
results in the function-call subsystem executing five times at each time
step.

#### Settings

`1`
:   Provide function-call once during each time step.

integer
:   Signed or unsigned integer number. Provide the specified
    number of function calls at each time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `numberOfIterations` |
| **Type**: character vector |
| **Values**: `'1'` | integer in quotes | vector of integers in quotes |
| **Default**: `'1'` |

### **Disallow wide output** — Prevent implicit expansion of output signal `off` (default) | `on`

Unless this parameter is
selected,
the output of this block is expanded into a vector, if necessary, to drive
the blocks to which it is connected. For example, if **Number of
iterations** is set to `2` and
**Disallow wide output** is not selected, and the
output of this block is connected to a Demux block, which is
in turn connected to three separate function-call subsystems, then each
function-call subsystem receives two function-call events at each time step.
A similar result occurs if the output of this block is connected to a
Stateflow® chart with multiple events. If **Disallow wide
output** is selected in these situations, the software produces
an error.

Select this parameter to prevent implicit expansion of the output
signal.

Clear this parameter to allow implicit expansion of the output signal when
appropriate.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DisallowWideOutput` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Show enable port** — Add input port for control signal `off` (default) | `on`

Select this parameter to add a control signal input port to the block. The
block outputs function-call events only when the value at the control signal
input port is a positive number.

Clear this parameter to remove the control signal input port. The block
outputs function-call events at every time step.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowEnablePort` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** |  |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2025a: Function-Call Generator block no longer behaves as linked, masked block

The Function-Call Generator block now behaves as a built-in block.
For versions prior to R2025a, the block behaves as a masked, linked block. This
change in block behavior enables the block to execute faster during
simulation.
