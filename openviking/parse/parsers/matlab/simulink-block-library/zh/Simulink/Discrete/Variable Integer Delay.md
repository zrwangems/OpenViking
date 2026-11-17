---
type: simulink-block
title: 'Variable Integer Delay'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'variableintegerdelay'
documentation_source_path: 'slref/variableintegerdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Integer Delay

## 端口

### 输入

### **u** — 数据输入信号 标量 | 向量

根据参数设置进行延迟的输入数据信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **d** — 延迟长度 标量

从输入端口继承的延迟长度。当您将 **Delay length: Source** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Enable** — 外部使能信号 标量

使能或禁用模块执行的外部使能信号。要创建此端口，请选择 **Show enable port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **External reset** — 外部复位信号 标量

将模块执行复位到初始条件的外部信号。要创建此端口，请选择 **External reset** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **x0** — 初始条件 标量 | 向量

从输入端口继承的初始条件。当您将 **Initial Condition: Source** 参数选择为 `Input port` 时启用。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号，即输入信号延迟由 **Delay length** 参数指定的时间长度。输出信号的初始值取决于多种条件。请参阅初始模块输出。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### 主要

### **Delay length** — 延迟长度 `Dialog`（默认）| `Input port`

指定是直接在对话框上输入延迟长度（固定延迟），还是从输入端口继承延迟（可变延迟）。

- 如果将 **Source** 设置为 `Dialog`，请在 **Value** 下的编辑字段中输入延迟长度。
- 如果将 **Source** 设置为 `Input port`，请验证上游信号为 `d` 输入端口提供延迟长度。您还可以通过指定 **Upper limit** 参数来指定其最大值。

将标量延迟长度指定为实数非负整数。对话框中超出范围或非整数的值（固定延迟）会返回错误。来自输入端口的超出范围的值（可变延迟）会将其强制转换到范围内。来自输入端口的非整数值（可变延迟）会将其截断为整数。

#### 编程使用

|  |
| --- |
| **模块参数**：`DelayLengthSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Input port'` | |
| **默认值**：`'Dialog'` |

|  |
| --- |
| **模块参数**：`DelayLength` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'2'` |

|  |
| --- |
| **模块参数**：`DelayLengthUpperLimit` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'100'` |

### **Initial condition** — 初始条件 `Dialog`（默认）| `Input port`

指定是直接在对话框上输入初始条件，还是从输入端口继承初始条件。

- 如果将 **Source** 设置为 `Dialog`，请在 **Value** 下的编辑字段中输入初始条件。
- 如果将 **Source** 设置为 `Input port`，请验证上游信号为 `x0` 输入端口提供初始条件。

Simulink® 使用舍入到最近操作和饱和，将 **Initial condition** 的数据类型离线转换为输入信号 `u` 的数据类型。

**注意**

当在 **State Attributes** 窗格上选择 **State name must resolve to Simulink signal object** 时，模块会将信号对象的初始值复制到 **Initial condition** 参数。但是，当 **Initial condition** 的源为 `Input port` 时，模块会忽略信号对象的初始值。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialConditionSource` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Input port'` | |
| **默认值**：`'Dialog'` |

|  |
| --- |
| **模块参数**：`InitialCondition` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'0.0'` |

### **Input processing** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)`（默认）| `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独的通道（基于采样的处理）。

使用 **Input processing** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：character vector |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **Use circular buffer for state** — 用于存储状态的循环缓冲区 `off`（默认）| `on`

选择以在仿真和代码生成中使用循环缓冲区存储状态。否则，数组缓冲区存储状态。

当延迟长度较大时，使用循环缓冲区可以提高执行速度。对于数组缓冲区，复制操作的数量随着延迟长度的增加而增加。对于循环缓冲区，复制操作的数量在延迟长度增加时保持不变。

如果以下条件之一为真，则始终使用数组缓冲区存储状态，因为循环缓冲区不会提高执行速度：

- 对于基于采样的信号，延迟长度为 1。
- 对于基于帧的信号，延迟长度不大于帧大小。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseCircularBuffer` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Prevent direct feedthrough** — 防止直接馈通 `off`（默认）| `on`

选择以将延迟长度从零增加到 **Input processing** 模式的下限：

- 对于基于采样的信号，将最小延迟长度增加到 1。
- 对于基于帧的信号，将最小延迟长度增加到帧长度。

选择此复选框可防止从输入端口 `u` 到输出端口的直接馈通。但是，此复选框无法防止从初始条件端口 `x0` 到输出端口的直接馈通。

#### 依赖关系

要启用此参数，请将 **Delay length: Source** 设置为 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PreventDirectFeedthrough` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Remove delay length check in generated code** — 移除延迟长度超出范围检查 `off`（默认）| `on`

选择以移除检查延迟长度是否超出范围的代码。

| 复选框 | 结果 | 使用时机 |
| --- | --- | --- |
| 选中 | 生成的代码不包含检查延迟长度是否超出范围的条件语句。 | 为了提高代码效率 |
| 清除 | 生成的代码包含检查延迟长度是否超出范围的条件语句。 | 用于安全关键型应用 |

#### 依赖关系

要启用此参数，请将 **Delay length: Source** 设置为 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数**：`RemoveDelayLengthCheckInGeneratedCode` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Diagnostic for delay length** — 延迟长度的诊断检查 `None`（默认）| `Warning` | `Error`

指定当输入 `d` 小于下限或大于 **Delay length: Upper limit** 时是否生成警告或错误。下限取决于 **Prevent direct feedthrough** 的设置。

- 如果清除该复选框，则下限为零。
- 如果选中该复选框，则对于基于采样的信号，下限为 1；对于基于帧的信号，下限为帧长度。

诊断选项包括：

- `None` — Simulink 软件不采取任何操作。
- `Warning` — Simulink 软件显示警告并继续仿真。
- `Error` — Simulink 软件终止仿真并显示错误。

#### 依赖关系

要启用此参数，请将 **Delay length: Source** 设置为 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数**：`DiagnosticForDelayLength` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

### **Show enable port** — 创建使能端口 `off`（默认）| `on`

选择以使用使能端口控制此模块的执行。当此端口的输入为非零时，模块被视为已启用；当输入为 `0` 时，模块被视为已禁用。输入的值在模块执行的同一时间步进行检查。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowEnablePort` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **External reset** — 外部状态复位 `None`（默认）| `Rising` | `Falling` | `Either` | `Level` | `Level hold`

指定用于将状态复位到初始条件的触发事件。

| 复位模式 | 行为 |
| --- | --- |
| `None` | 不复位 |
| `Rising` | 在上升沿复位 |
| `Falling` | 在下降沿复位 |
| `Either` | 在上升沿或下降沿复位 |
| `Level` | 在以下任一情况下复位：  - 当复位信号在当前时间步为非零时 - 当复位信号值从上一时间步的非零变为当前时间步的零时 |
| `Level hold` | 当复位信号在当前时间步为非零时复位 |

#### 编程使用

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：character vector |
| **值**：`'None'` | `'Rising'` | `'Falling'` | `'Either'` | `'Level'` | `'Level hold'` |
| **默认值**：`'None'` |

### **Sample time (-1 for inherited)** — 采样时间命中之间的离散间隔 `-1`（默认）| `scalar`

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。此模块支持离散采样时间，但不支持连续采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **Value**: real scalar |
| **默认值**：`'-1'` |

### 状态属性

### **State name** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **Apply** 时，此参数会启用 **State name must resolve to Simulink signal object**。

有关详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateName` |
| **类型**：character vector |
| **值**：unique name |
| **默认值**：`''` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选择此复选框以要求状态名称解析为 Simulink 信号对象。

#### 依赖关系

要启用此参数，请为 **State name** 指定一个值。仅当您将模型配置参数 **Signal resolution** 设置为 `None` 以外的值时，此参数才会出现。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

有关 HDL 代码生成的信息，请参阅 Delay 页面上的 HDL Code Generation。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2012b 中引入**

## 描述

按可变采样周期延迟输入信号

Variable Integer Delay 模块是 Delay 模块的变体，其延迟长度的源默认设置为 `Input port`。
