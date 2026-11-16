---
type: simulink-block
title: 'Serial Send'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Embedded Targets / Host Communication'
documentation_page: 'serialsend'
documentation_source_path: 'ref/serialsend.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Send

## 端口

### 输入

### **Data** — 要发送的数据值 向量 | 矩阵 | 数组

要从模块通过串行端口发送的数据值，指定为向量、矩阵或数组。在发送数据之前，请设置此模块的参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Port** — 串行通信端口，可用通信端口

您要向其发送数据的计算机上的串行端口。从可用端口中选择一个端口，然后使用 Serial Configuration 模块配置该端口。如果尚未配置端口，则运行模型时该模块会返回错误。

**注意**

每个 Serial Send 模块都必须有一个已配置的 Serial Configuration 模块。如果在仿真中使用多个串行端口，则必须使用单独的 Serial Configuration 模块配置每个端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `Port` |
| **类型：** character vector, string |

### **Header** — 标头 numeric array | integer 从 0 到 255（含）

标头，用于指示数据块的开始。Serial Send 模块在通过串行端口发送数据之前，会将标头添加到数据前面。默认情况下，不指定标头。

此参数中指定的 numeric array 是对应 ASCII 字符的 `uint8` integer 表示。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | 示例 ASCII 字符 | MATLAB 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"Start"` | `uint8('Start')` | `[83 116 97 114 116]` |

您也可以使用 ASCII 字符的十六进制表示来指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `Header` |
| **类型：** character vector, string |
| **值：** integer array |

### **Terminator** — 终止符 `<none>`（默认） | `CR ('\r')` | `LF ('\n')` | `CR/LF ('\r\n')` | `NULL ('\0')` | `Custom Terminator`

终止符，用于指示数据块的结束。Serial Send 模块在通过串行端口发送数据之前，会将终止符追加到数据末尾。

如果选择 `Custom Terminator`，则可以指定自己的终止符值。

#### 编程用法

|  |
| --- |
| **模块参数：** `Terminator` |
| **类型：** character vector, string |
| **值：** `'<none>'` | `'CR ('\r')'` | `'LF ('\n')'` | `'CR/LF ('\r\n')'` | `'NULL ('\0')'` | `'Custom Terminator'` |
| **默认值：** `'<none>'` |

### **Custom terminator** — 自定义终止符 numeric array | integer 从 0 到 255（含）

自定义终止符，用于指示数据块的结束。Serial Send 模块在通过串行端口发送数据之前，会将终止符追加到数据末尾。

此参数中指定的 numeric array 是对应 ASCII 字符的 `uint8` integer 表示。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | 示例 ASCII 字符 | MATLAB 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"End"` | `uint8('End')` | `[69 110 100]` |

您也可以使用 ASCII 字符的十六进制表示来指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `CustomTerminator` |
| **类型：** character vector, string |
| **值：** integer array |

### **Enable blocking mode** — 仿真在发送数据时等待 `on`（默认） | `off`

此参数使仿真在模块发送数据时等待。如果不希望写操作导致仿真等待，请清除该复选框。

如果启用阻塞模式，仿真将等待数据发送完成。如果未启用阻塞模式，仿真将连续运行。

#### 编程用法

|  |
| --- |
| **模块参数：** `EnableBlockingMode` |
| **类型：** character vector, string |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

## 所属库

Instrument Control Toolbox Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块仅为主机平台生成平台特定的代码（Windows®、macOS、Linux®）。

## 版本历史

**在 R2008a 中引入**

## 描述

通过串行端口发送二进制数据

Serial Send 模块配置并打开指向指定串行端口的接口。配置和初始化在模型执行开始时进行一次。该模块在模型运行时将数据从模型发送到串行端口。您可以同时使用多个 Serial Send 模块将数据发送到特定串行端口。

**注意**

在指定 Serial Send 模块参数之前，必须使用 Serial Configuration 模块配置串行端口参数。

Serial Send 模块有一个输入端口，可接受 1-D 向量和矩阵数据。此模块没有输出端口。该模块从输入端口处的信号继承数据类型。有效的数据类型为 `single`、`double`、`int8`、`uint8`、`int16`、`uin16`、`int32` 和 `uint32`。

### 其他支持的功能

- Serial Send 模块支持使用 Simulink® Accelerator mode，但不支持 Rapid Accelerator。
  此功能可加速 Simulink 模型的执行。
- Serial Send 模块支持使用模型引用。此功能允许您的模型将其他 Simulink
  模型作为模块化组件包含在内。
- Serial Send 模块支持 C/C++ 代码生成。此功能允许您使用 Simulink
  Coder™ 生成 C 和 C++ 代码。

有关这些功能的详细信息，请参阅 Simulink
文档。
