---
type: simulink-block
title: 'CAN Unpack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / CAN'
documentation_page: 'canunpack'
documentation_source_path: 'io_ref/canunpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Unpack

## 端口

### 输入

### **CAN Msg** — CAN 消息输入 `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

此模块有一个输入端口，**CAN Msg**。该模块获取指定的输入 CAN 消息，并将其信号数据解包到单独的输出。

该模块支持以下信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点数据类型。

### 输出

### **Data** — CAN 信号输出 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

默认情况下，该模块有一个输出端口。输出端口的数量是动态的，取决于您指定该模块输出的信号数量。例如，如果您的消息有四个信号，该模块可以有四个输出端口。

对于手动指定或由数据库指定的信号，CAN 信号的默认输出数据类型是 double。要指定其他类型，请使用 Signal Specification 模块。这允许该模块支持以下输出信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点类型。

可以通过在参数 **Output ports** 窗格中选择选项来添加其他输出端口。有关详细信息，请参阅参数 `Output identifier`、`Output timestamp`、`Output error`、`Output remote`、`Output length` 和 `Output status`。

## 参数

### **输出数据为** — 选择您的数据信号 `raw data`（默认）| `manually specify signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：将数据输出为 uint8 向量数组。如果选择此选项，您只需指定消息字段。其他信号参数字段不可用。此选项仅在您的模块上打开一个输出端口。

  转换公式为：

  `physical_value = raw_value * Factor + Offset`

  其中 `raw_value` 是解包后的信号值，`physical_value` 是缩放后的信号值。
- `manually specified signals`：您可以指定数据信号。如果选择此选项，请使用 `Signals` 表手动创建您的信号消息。模块上的输出端口数量取决于您指定的信号数量。例如，如果指定四个信号，您的模块有四个输出端口。
- `CANdb specified signals`：您可以指定包含数据信号的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块上的输出端口数量取决于 CANdb 文件中指定的信号数量。例如，如果 CANdb 文件中选定的消息有四个信号，您的模块有四个输出端口。
- `ARXML specified signals`：允许您为信号定义指定一个 ARXML 文件。这会禁用某些远程选项。从 ARXML 文件读取数据后，您可以切换到 `manually specified signals` 以进一步修改表。

  有关详细信息，请参阅 Simulink 中的 CAN 的 ARXML 文件支持（Vehicle Network Toolbox）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** `string` | `character vector` |
| **值：** `'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` | `'ARXML specified signals'` |
| **默认：** `'raw data'` |

### **数据库文件** — ARXML 或 CAN 数据库文件 character vector

如果指定 **输出数据为** 参数为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。单击 **Browse** 以在您的系统上查找数据库文件。数据库文件中指定的消息和信号定义将填充对话框的 **Message** 部分。数据库文件中指定的信号将填充 **Signals** 表。包含非字母数字字符（例如等号、& 等）的文件名不是有效的数据库文件名。您可以在数据库名称中使用句点。在使用前，请重命名包含非字母数字字符的数据库文件。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **消息列表** — CAN 消息列表 array of character vectors

如果您为 **数据输入为** 字段指定数据库，并在 **数据库文件** 字段中指定数据库文件，则此选项可用。您可以选择要查看的消息。然后 **Signals** 表会显示所选消息的详细信息。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **名称** — CAN 消息名称 `CAN Msg`（默认）| character vector

指定您的 CAN 消息的名称。默认值为 `CAN Msg`。如果您选择输出原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **标识符类型** — CAN 标识符类型 `Standard (11-bit identifier)`（默认）| `Extended (29-bit identifier)`

指定您的 CAN 消息标识符是 `Standard` 还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11 位标识符，扩展标识符是 29 位标识符。如果您选择输出原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**标识符类型** 从数据库继承类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认：** `'Standard (11-bit identifier)'` |

### **CAN 标识符** — CAN 消息标识符 `0`（默认）| `0` 到 `536870911`

指定您的 CAN 消息 ID。对于标准标识符，此数字必须是 0 到 2047 的整数；对于扩展标识符，必须是 0 到 536870911 的整数。如果指定 `-1`，该模块会解包与消息指定长度匹配的消息。您还可以使用 `hex2dec` 函数指定十六进制值。如果您选择输出原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'536870911'` |

### **长度 (bytes)** — CAN 消息长度 `8`（默认）| `0` 到 `8`

指定您的 CAN 消息长度，范围为 0 到 8 bytes。如果您对输出数据使用数据库指定的信号，则数据库文件定义消息长度。否则，此字段默认为 `8`。如果您选择输出原始数据或手动指定信号，则此选项可用。

注意：当收到的帧长度与掩码或网络描述文件中指定的值不同时，该帧会被丢弃。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'8'` |
| **默认：** `'8'` |

### **添加信号** — 添加 CAN 信号

将信号添加到信号表。

#### 程序化使用

无

### **删除信号** — 移除 CAN 信号

从信号表中移除所选信号。

#### 程序化使用

无

### **Signals** — 信号表 table

如果您选择手动指定信号或使用数据库文件定义信号，则会显示此表。

如果您正在使用数据库文件，文件中的数据将填充此表，您无法编辑这些字段。要编辑信号信息，请切换到指定信号。

如果您已选择手动指定信号，请在此表中手动创建您的信号。您创建的每个信号都具有以下值：

**名称**
:   为您的信号指定一个描述性名称。模型中的 Simulink 模块显示此名称。默认值为 `Signal [row number]`。

**起始位**
:   指定数据的起始位。起始位是从消息开头开始计数的最低有效位。起始位必须是 0 到 63 的整数。

**长度 (bits)**
:   指定信号在消息中占用的位数。长度必须是 1 到 64 的整数。

**字节顺序**
:   选择以下任一选项：

    - `LE`：其中字节顺序为 little-endian 格式（Intel®）。在此格式中，您从最低有效位计数到最高有效位。例如，如果以 little-endian 格式打包一个字节的数据，起始位为 20，则数据位表类似于下图。

      **从最低有效位到最高地址计数的 Little-Endian 字节顺序**
    - `BE`：其中字节顺序为 big-endian 格式（Motorola®）。在此格式中，您从最低有效位计数到最高有效位。例如，如果以 big-endian 格式打包一个字节的数据，起始位为 20，则数据位表类似于下图。

      **从最低有效位到最低地址计数的 Big-Endian 字节顺序**

**数据类型**
:   指定信号如何解释分配位中的数据。从以下选项中选择：

    - `signed`（默认）
    - `unsigned`
    - `single`
    - `double`

**多路复用类型**
:   指定模块在每个时间步如何从 CAN 消息中解包信号：

    - `Standard`：该信号在每个时间步都会被解包。
    - `Multiplexor`：解包 `Multiplexor` 信号或模式信号。每条消息只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果在运行时 `Multiplexor` 信号（模式信号）的值与此信号配置的 **多路复用值** 匹配，则解包该信号。

    例如，一条消息有四个信号，其值如下。

    | 信号名称 | 多路复用类型 | 多路复用值 |
    | --- | --- | --- |
    | Signal-A | Standard | 不适用 |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | 不适用 |

    在此示例中：

    - 该模块在每个时间步解包 Signal-A（Standard 信号）和 Signal-D（Multiplexor 信号）。
    - 如果在特定时间步 Signal-D 的值为 1，则该模块在该时间步解包 Signal-B 以及 Signal-A 和 Signal-D。
    - 如果在特定时间步 Signal-D 的值为 0，则该模块在该时间步解包 Signal-C 以及 Signal-A 和 Signal-D。
    - 如果 Signal-D 的值不是 1 或 0，则该模块在该时间步不解包任何 Multiplexed 信号。

**多路复用值**
:   仅当您已将 **多路复用类型** 选择为 `Multiplexed` 时，此选项才可用。您提供的值必须在运行时与 `Multiplexor` 信号值匹配，模块才会解包 `Multiplexed` 信号。**多路复用值** 必须是正整数或零。

**Factor**
:   指定用于将解包后的原始值转换为物理值（信号值）的 **Factor** 值。有关详细信息，请参阅 **数据输入为** 参数转换公式。

**Offset**
:   指定用于将物理值（信号值）转换为解包后的原始值的 **Offset** 值。有关详细信息，请参阅 **数据输入为** 参数转换公式。

**Min**、**Max**
:   定义原始信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库读取。对于 **manually specified signals**，您可以指定信号的最小和最大物理值。默认情况下，这些设置不会裁剪超过它们的信号值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SignalInfo` |
| **类型：** `string` | `character vector` |

### **输出标识符** — 添加 CAN ID 输出端口 `off`（默认）

选择此选项以输出 CAN 消息标识符。此端口的数据类型为 `uint32`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IDPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **输出时间戳** — 添加 Timestamp 输出端口 `off`（默认）| `on`

选择此选项以输出消息时间戳。此值指示消息的接收时间，以自模型仿真开始以来经过的秒数度量。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `double`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TimestampPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **输出错误** — 添加 Error 输出端口 `off`（默认）| `on`

选择此选项以输出消息错误状态。此选项会向模块添加一个新的输出端口。此端口上输出值 `1` 表示传入消息是错误帧。如果输出值为 `0`，则没有错误。此端口的数据类型为 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ErrorPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **输出远程** — 添加 Remote 输出端口 `off`（默认）| `on`

选择此选项以输出消息远程帧状态。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RemotePort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **输出长度** — 添加 Length 输出端口 `off`（默认）| `on`

选择此选项以输出消息长度（以 bytes 为单位）。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LengthPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **输出状态** — 添加 Status 输出端口 `off`（默认）| `on`

选择此选项以输出消息接收状态。如果模块收到新消息，则状态为 `1`；如果未收到，则为 `0`。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StatusPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

## 所属库

Vehicle Network Toolbox / CAN Communication C2000 Microcontroller Blockset / Target Communication Embedded Coder / Embedded Targets / Host Communication Simulink Real-Time / CAN / CAN MSG blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

### R2025a: 更新参数：ARXML 支持

为支持 ARXML 文件定义，以下参数已更新：

- **输出数据为** — 具有新选项 `ARXML specified signals`。

- **CANdb file** — 在模块封装中已重命名为 **数据库文件**。其程序化名称仍为 `CANdbFile`。

## 描述

从 CAN 消息中解包单个信号

CAN Unpack 模块在每个时间步使用指定的输出参数将一条 CAN 消息解包为信号数据。数据作为单个信号输出。

要使用此模块，您还需要 Simulink® 软件的许可证。

CAN Unpack 模块支持：

- 使用 Simulink 加速模式和快速加速模式。使用此功能，您可以加速
  Simulink 模型的执行。有关详细信息，请参阅 Acceleration。
- 使用模型引用。使用此功能，您的模型可以将其他
  Simulink 模型作为模块化组件包含在内。有关详细信息，请参阅 Model References。

**提示**

- 要处理通过通道传入的每条消息，请不要在函数触发子系统中使用 CAN
  Unpack 模块。有关详细信息，请参阅
  Speedgoat® 文档。
- 此模块可用于解码最多 8
  bytes 的 J1939 参数组信号。但是，要处理 J1939 消息，最好使用
  J1939 Communication 模块库中的模块，而不是此模块。
  请参阅 J1939。
