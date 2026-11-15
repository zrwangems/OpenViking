---
type: simulink-block
title: 'Python Code'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'pythoncode'
language: zh-CN
chinese_source: worker-translation
---

# Python Code



将原生 Python 代码集成到 Simulink 模型中

## 库

Simulink / User-Defined Functions

## 描述

Python Code 模块将原生 Python® 代码集成到 Simulink® 模型中。使用此模块可导入外部代码，并通过指定模块接口以及为模块初始化、输出和终止编写 Python 代码，来自定义代码的集成。

Python Code 模块支持初始化持久数据。持久数据可以包括 Python 类对象。使用存储 Python 对象的持久变量，以在时间步之间保留状态值。

有关使用此模块集成 Python 代码的步骤，请参阅使用 Python Code 模块将 Python 代码集成到 Simulink 中。

**注意**

必须在系统中安装兼容版本的 Python 才能使用此模块。这可能涉及在 Linux 和 Mac 上安装相应的 Python 开发头文件。必须将 MATLAB 中的 Python 的 `ExecutionMode` 设置为 `InProcess`。有关详细信息，请参阅配置系统以使用 Python。

Python Code 不支持在 Dataflow Subsystem 内进行仿真。当放置在 For Each Subsystem 内时，也不支持在快速加速模式下进行仿真

## 端口

### 输入

### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

输入端口数量由模块参数对话框中的 **端口和参数** 表内定义的具有 `Input` 作用域的符号数量决定。除非通过编辑模块对话框的 **符号** 表中的 **标签** 字段来更改，否则每个输入端口标签都与 `Input` 符号的名称相同。

Python Code 不支持将总线数组作为输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus` | `fixedpoint`
### 输出

### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

输出端口数量由模块参数对话框中的 **符号** 表内定义的具有 `Output` 作用域的符号数量决定。除非通过编辑模块对话框的 **符号** 表中的 **标签** 字段来更改，否则每个输出端口标签都与 `Output` 符号的名称相同。

Python Code 不支持将总线数组作为输出。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus` | `fixedpoint`

## 参数

### **端口和参数符号** — 符号和符号属性表

Python 代码中使用的符号和符号属性，指定为表。必须在表中输入每个符号的以下属性：

- **名称** — 代码中的符号名称。

  指定的每个符号都表示一个 Python 对象。**名称** 字段用作赋予该 Python 对象的名称。
- **作用域** — 符号的作用域。可用的作用域包括：

  - `Input` — 模块的输入。
  - `Output` — 模块的输出。
  - `Parameter` — 出现在模块参数掩码上的模块参数。参数名称由符号的 **标签** 定义。
  - `Persistent` — 持久模块数据，在仿真期间从一个时间步到下一个时间步保留其值。配置了持久变量的 Python Code 模块不支持连续采样时间和仿真回退。

    可以通过定义具有 `Persistent` 作用域的符号，并将 `PythonObject` 用作该符号的 **类型**，在代码段或时间步之间共享任意 Python 对象。
- **标签** — 符号的标签。对于具有 `Input` 或 `Output` 作用域的符号，标签在模块上显示为端口名称。对于具有 `Parameter` 作用域的符号，标签显示在模块参数掩码上。不能为 `Persistent` 作用域的符号定义标签。
- **类型** — 符号的数据类型。从下拉列表中选择数据类型，或指定自定义数据类型。`PythonObject` 类型只能为作用域为 `Persistent` 的符号设置。
- **大小** — 符号数据的大小。可以使用大小表达式定义输出的大小，或使用 `-1` 继承大小。
- **端口** — 符号的端口索引。对于 `Input` 或 `Output` 符号，**端口** 指定模块上对应于该符号的一个或多个端口的端口索引。对于 `Parameter` 符号，**端口** 指定该符号在模块参数掩码中出现的顺序。

#### 编程用法

|  |
| --- |
| **模块参数：** `SymbolSpec` |
| **类型：** `SymbolSpec` 对象 |
| **值：** `SymbolSpec` 对象 |
| **默认值：** `Symbol` 对象的空数组 |

### **采样时间** — 采样周期 `-1` (默认) | 标量 | 向量

采样周期，以秒为单位指定。请参阅采样时间类型和指定采样时间。如果模块定义了持久符号，则不能指定连续采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: 字符串标量或字符向量 |
| **默认值**: `"-1"` |

### **输出** — 输出代码 无默认值

模块在仿真期间每个时间步执行的输出代码，指定为字符向量或字符串标量。例如，使用此参数调用外部 Python 代码中的函数，修改结果，并执行操作以将结果传递给其他模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `Python code` |
| **默认值：** `""` |

### **启动** — 初始化代码 无默认值

模块在仿真开始时执行一次的初始化代码。例如，使用此参数初始化持久符号。

#### 编程用法

|  |
| --- |
| **模块参数：** `StartCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `Python code` |
| **默认值：** `""` |

### **终止** — 终止代码 无默认值

模块在仿真结束时执行一次的终止代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `TerminateCode` |
| **类型：** 字符向量或字符串标量 |
| **值：** `""` | `Python code` |
| **默认值：** `""` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `busa` | `doublea` | `fixedpointa` | `integera` | `singlea` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成对 Python CAPI 的调用，以执行 Python 代码。生成的代码必须与 Python 开发头文件一起构建，并链接到 Python 解释器。

## 版本历史

**在 R2025a 中引入**
