---
type: simulink-block
title: 'Function-Call Generator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functioncallgenerator'
documentation_source_path: 'slref/functioncallgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Function-Call Generator

## 端口

### 输入

### **Enable** — 控制信号输入 标量

仅当此端口处的输入为正数时，模块才输出函数调用事件。

#### 依赖关系

要启用此端口，请选中 **Show enable port** 复选框。
### 输出

### **Function Call** — 函数调用事件输出 标量 | 向量

向函数调用子系统或函数调用模型的函数调用输入端口发送函数调用事件。

## 参数

### **Sample time** — 指定时间间隔 `1`（默认）| 标量 | 向量 | `-1`

指定向函数调用子系统或函数调用模型发送函数调用事件之间的时间间隔。如果子系统或模型的实际调用速率与此参数指定的时间间隔不同，Simulink 会显示错误。

默认情况下，模块使用时间间隔 `1`。要设置不同的间隔，请根据采样时间类型表中的说明输入有效的采样时间，或指定 `-1` 以从模型继承时间间隔。

#### 依赖关系

要启用此参数，请清除 **Show enable port** 复选框。如果选中 **Show enable port**，采样时间会自动设置为 `-1`（继承）。

#### 编程用法

|  |
| --- |
| **模块参数**：`sample_time` |
| **类型**：字符向量 |
| **值**：`'1'` | 标量表达式 | 向量表达式 | `'-1'` |
| **默认值**：`'1'` |

### **Number of iterations** — 指定每个时间步提供函数调用的次数 `1`（默认）| 整数

此参数的值可以是向量，其中向量的每个元素指定执行函数调用子系统或模型的次数。如果指定了向量，则模块输出函数调用事件的向量，可以使用 Demux 模块将其拆分为单独的函数调用事件，并用于驱动多个函数调用子系统或模型。

假设将 **Number of iterations** 指定为 `[3 2]`，并将此模块的输出连接到 Demux 模块，该模块又连接到两个函数调用子系统的控制端口。在这种情况下，第一个函数调用子系统在每个时间步执行三次，第二个函数调用子系统在每个时间步执行两次。

但是，如果将此模块的输出连接到单个函数调用子系统或模型，则函数调用子系统或模型在每个时间步执行的总次数等于向量元素值之和。因此在上面的示例中，将 **Number of iterations** 指定为 `[3 2]` 并将此模块的输出连接到单个函数调用子系统，会导致函数调用子系统在每个时间步执行五次。

#### 设置

`1`
:   在每个时间步提供一次函数调用。

整数
:   有符号或无符号整数。在每个时间步提供指定次数的函数调用。

#### 编程用法

|  |
| --- |
| **模块参数**：`numberOfIterations` |
| **类型**：字符向量 |
| **值**：`'1'` | 带引号的整数 | 带引号的整数向量 |
| **默认值**：`'1'` |

### **Disallow wide output** — 防止输出信号的隐式扩展 `off`（默认）| `on`

除非选中此参数，否则此模块的输出会在必要时扩展为向量，以驱动与其连接的模块。例如，如果 **Number of iterations** 设置为 `2` 且未选中 **Disallow wide output**，并且此模块的输出连接到 Demux 模块，该模块又依次连接到三个独立的函数调用子系统，则每个函数调用子系统在每个时间步接收两个函数调用事件。如果此模块的输出连接到具有多个事件的 Stateflow® 图，也会出现类似的结果。在这些情况下，如果选中 **Disallow wide output**，软件会产生错误。

选中此参数以防止输出信号的隐式扩展。

清除此参数以在适当时允许输出信号的隐式扩展。

#### 编程用法

|  |
| --- |
| **模块参数**：`DisallowWideOutput` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Show enable port** — 添加控制信号输入端口 `off`（默认）| `on`

选中此参数以向模块添加控制信号输入端口。仅当控制信号输入端口处的值为正数时，模块才输出函数调用事件。

清除此参数以移除控制信号输入端口。模块在每个时间步输出函数调用事件。

#### 编程用法

|  |
| --- |
| **模块参数**：`ShowEnablePort` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

### R2025a：Function-Call Generator 模块不再表现为链接的掩码模块

Function-Call Generator 模块现在表现为内置模块。对于 R2025a 之前的版本，该模块表现为掩码的链接模块。此模块行为的更改使模块在仿真期间能够更快地执行。

## 描述

提供函数调用事件以控制子系统或模型的执行

Function-Call Generator 模块提供函数调用事件，以使用 **Sample time** 参数指定的速率执行函数调用子系统或函数调用模型。函数调用子系统或函数调用模型是包含 Trigger 模块的子系统或模型，其 **Trigger type** 参数设置为 `function-call`。

要在每个时间步多次迭代执行每个函数调用子系统或函数调用模型，请使用 **Number of iterations** 参数。

要按指定顺序执行多个函数调用子系统或函数调用模型，请将 Function-Call Generator 模块与 Function-Call Split 模块一起使用。有关示例，请参阅 Function-Call Split。

要间歇性地执行函数调用子系统或函数调用模型（即不在每个时间步执行），请选中 **Show enable port** 参数。然后可以使用使能端口处的输入来控制模块何时输出函数调用事件。实际上，您可以根据需要打开和关闭模块。

**注意**

从 R2025a 开始，Function-Call Generator 模块不再表现为掩码的链接模块。要以编程方式在模型中定位此模块，请使用命令 `find_system('BlockType','FunctionCallGenerator')`。当从其他版本更新到 R2025a 时，建议修复任何到 Simulink® 库的链接已损坏的 Function-Call Generator 模块。否则，该模块将不会被更新，并且在更新后的模型中将继续表现为掩码模块。此模块的掩码行为将在未来版本中移除。有关识别模型中损坏的库链接的详细信息，请参阅 Display Library Links。

对于 R2025a 之前的版本，要以编程方式在模型中定位此模块，请使用命令 `find_system('MaskType','Function-Call Generator')`。
