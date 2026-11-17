---
type: simulink-block
title: 'Serial Receive'
family: 'host-communication'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Host Communication'
documentation_page: 'serialreceive'
documentation_source_path: 'ref/serialreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Receive

## 端口

### 输出

### **Data** — 接收的数据 向量 | 矩阵 | 数组

模块从串行端口接收的数据，以向量、矩阵或数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — 新数据可用 `false` 或 `0` (默认) | `true` 或 `1`

新数据可用状态，以数值或逻辑值 `1` (`true`) 或 `0` (`false`) 返回。如果此端口返回 `1`，则有新数据可读取。

#### 依赖项

要启用此端口，请取消选择该参数。

**数据类型：** `Boolean`

## 参数

### **端口** — 串行通信端口 可用的通信端口

要从其接收数据的计算机上的串行端口。从可用端口中选一个端口，然后使用 Serial Configuration 模块配置该端口。如果尚未配置端口，运行模型时模块将返回错误。

**注意**

每个 Serial Receive 模块都必须有一个已配置的 Serial Configuration 模块。如果在仿真中使用多个串行端口，必须使用单独的 Serial Configuration 模块配置每个端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `Port` |
| **类型：** character vector, string |

### **数据类型** — 输出数据类型 `uint8` (默认) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32`

模块从串行端口接收的数据类型，指定为 MATLAB® 数值数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataType` |
| **类型：** character vector, string |
| **值：** `'uint8'` | `'single'` | `'double'` | `'int8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` |
| **默认：** `'uint8'` |

### **标头** — 标头数值数组 | 从 0 到 255 的整数（含端点）

如果选中此参数，可以指定指示数据块开始的标头。仿真会忽略标头之前出现的数据。标头数据不会发送到输出端口。默认情况下，此参数未选中，且未指定标头。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示形式。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | ASCII 字符示例 | MATLAB 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"Start"` | `uint8('Start')` | `[83 116 97 114 116]` |

您还可以使用 ASCII 字符的十六进制表示形式指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `ToggleHeader` |
| **类型：** character vector, string |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

|  |
| --- |
| **模块参数：** `Header` |
| **类型：** character vector, string |
| **值：** integer array |

### **结束标记** — 终止符 `<none>` (默认) | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

如果选中此参数，可以指定指示数据块结束的结束标记或终止符。仿真将结束标记之后出现的任何数据视为新数据块。结束标记数据不会发送到输出端口。如果要读取的串行端口数据中有结束标记，则此结束标记必须与其中的结束标记匹配。

如果选择 `Custom Terminator`，可以指定您自己的结束标记值。

#### 编程用法

|  |
| --- |
| **模块参数：** `ToggleTerminator` |
| **类型：** character vector, string |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

|  |
| --- |
| **模块参数：** `Terminator` |
| **类型：** character vector, string |
| **值：** `'<none>'` | `'CR ('\r')'` | `'LF ('\n')'` | `'CR/LF ('\r\n')'` | `'NULL ('\0')'` | `'Custom Terminator'` |
| **默认：** `'<none>'` |

### **自定义终止符** — 自定义终止符数值数组 | 从 0 到 255 的整数（含端点）

指示数据块结束的自定义终止符，在 **结束标记** 设置为 `'Custom Terminator'` 时使用。仿真将终止符之后出现的任何数据视为新数据块。终止符数据不会发送到输出端口。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示形式。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | ASCII 字符示例 | MATLAB 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"End"` | `uint8('End')` | `[69 110 100]` |

您还可以使用 ASCII 字符的十六进制表示形式指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `CustomTerminator` |
| **类型：** character vector, string |
| **值：** integer array |

### **输入格式** — 读取数据的格式 `Column major` (默认) | `Row major`

模块从串行端口接收的数据的格式，指定为 `Row major` 或 `Column major`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputFormat` |
| **类型：** character vector, string |
| **值：** `'Row major'` | `'Column major'` |
| **默认：** `'Column major'` |

### **数据大小** — 读取的值的数目 `[1 1]` (默认) | 数值数组

输出数据大小，或在每个仿真时间步应读取的值的数目。此参数指定为多维数值数组。数据大小不包括标头或终止符值。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataSize` |
| **类型：** character vector, string |
| **值：** integer array |
| **默认：** `'[1 1]'` |

### **启用阻塞模式** — 仿真在接收数据时等待 `on` (默认) | `off`

此参数使仿真在模块接收数据时等待。当新数据可用时，仿真从下一个时间步继续。如果不希望读取操作导致仿真等待，请取消选中该复选框。

如果启用阻塞模式，仿真会等待请求的数据变为可用。模型等待的时间最多为 Serial Configuration 模块中 **Timeout** 参数指定的时间。如果在仿真期间新数据未变为可用，可以通过为 **数据不可用时的操作** 参数选择 `Error` 选项来返回错误。

如果未启用阻塞模式，仿真会连续运行，且模块有两个输出端口：**Status** 和 **Data**。**Data** 端口在每个时间步包含请求的数据集。**Status** 端口包含 0 或 1，取决于在给定时间步是否接收到新数据。

#### 编程用法

|  |
| --- |
| **模块参数：** `EnableBlockingMode` |
| **类型：** character vector, string |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **数据不可用时的操作** — 数据不可用时采取的操作 `Output last received value` (默认) | `Output custom value` | `Error`

数据不可用时模块应执行的操作。可用选项包括：

- `Output last received value` — 当模块在当前时间步未接收到数据时，返回它在上一时间步接收到的值。
- `Output custom value` — 当模块未接收到当前数据时，返回任何用户定义的值。在 **自定义值** 字段中定义自定义值。
- `Error` — 当模块未接收到当前数据时，返回错误。必须选择 **启用阻塞模式** 才能使用此选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `ActionDataUnavailable` |
| **类型：** character vector, string |
| **值：** `'Output last received value'` | `'Output custom value'` | `'Error'` |
| **默认：** `'Output last received value'` |

### **自定义值** — 数据不可用时的自定义输出值 0 (默认) | 数值

模块未接收到新数据时要输出的自定义值。自定义值可以是标量，也可以等于其接收数据的大小（由 **数据大小** 参数指定）。必须选择 `Output custom value` 作为 **数据不可用时的操作** 才能设置此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `CustomValue` |
| **类型：** character vector, string |
| **值：** numeric |
| **默认：** `'0'` |

### **模块采样时间** — 采样时间 0.01 (默认) | 正数值

模块在仿真期间的采样时间。这是模块在仿真期间执行的速率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector, string |
| **值：** positive numeric |
| **默认：** `'0.01'` |

## 所属库

Instrument Control Toolbox Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块仅为主机平台（Windows®、macOS、Linux®）生成平台特定的代码。

## 版本历史

**在 R2008a 中引入**

## 描述

通过串行端口接收二进制数据

Serial Receive 模块配置并打开到指定串行端口的接口。配置和初始化在模型执行开始时进行一次。模块在模型运行期间从串行端口获取数据。一次只能使用一个 Serial Receive 模块从特定串行端口接收数据。

**注意**

在指定 Serial Receive 模块参数之前，必须使用 Serial Configuration 模块配置串行端口参数。

此模块没有输入端口。根据您选择阻塞模式还是非阻塞模式，它有一个或两个输出端口。如果选择阻塞模式，模块有一个输出端口 **Data**，对应于它接收的数据。如果未选择阻塞模式，模块有两个输出端口 **Data** 和 **Status**。

此模块使用先进先出 (FIFO) 缓冲区从串行端口接收数据。在每个时间步，**Data** 端口从缓冲区返回请求的值。在非阻塞模式下，**Status** 端口指示模块是否已接收到新数据。如果 **Status** 端口显示 `1`，则有新数据可用；如果 **Status** 端口显示 `0`，则没有新数据可用。

### 其他支持的功能

- Serial Receive 模块支持使用 Simulink® Accelerator 模式，但不支持 Rapid Accelerator。此功能可加速 Simulink 模型的执行。
- Serial Receive 模块支持使用模型引用。此功能允许您的模型将其他 Simulink 模型作为模块化组件包含在内。
- Serial Receive 模块支持 C/C++ 代码生成。此功能允许您使用 Simulink Coder™ 生成 C 和 C++ 代码。

有关这些功能的详细信息，请参阅 Simulink 文档。
