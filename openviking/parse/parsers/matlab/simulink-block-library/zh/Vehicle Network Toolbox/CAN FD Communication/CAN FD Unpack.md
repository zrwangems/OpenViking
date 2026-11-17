---
type: simulink-block
title: 'CAN FD Unpack'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN FD Communication'
documentation_page: 'canfdunpack'
documentation_source_path: 'ug/canfdunpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN FD Unpack

## 端口

### 输入

### **Msg** — CAN FD 报文输入 `CAN_FD_MESSAGE_BUS`

此模块有一个输入端口 Msg。CAN FD Unpack 模块接收指定的输入 CAN 报文，并将其信号数据解包到单独的输出端口。

该模块支持以下输入信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点数据类型。

### 输出

### **Data** — CAN 报文输出 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

CAN FD Unpack 模块默认有一个输出端口。数据输出端口的数量是动态的，取决于您为模块指定输出的信号数量。例如，如果您的模块有四个信号，则它有四个输出端口，以信号名称标记。

对于手动指定或数据库指定的信号，默认输出信号数据类型为 double。要指定其他类型，请使用 Signal Specification (Simulink) 模块。这允许该模块支持以下输出信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点类型。

可以通过参数 **Output ports** 窗格中的选项添加额外的输出端口。

## 参数

### **Data to output as** — 选择您的数据信号 `raw data`（默认）| `manually specify signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：将数据输出为 uint8 向量数组。如果选择此选项，则只需指定报文字段。其他信号参数字段不可用。此选项在模块上仅打开一个输出端口。

  转换公式为：

  ```
  physical_value = raw_value * Factor + Offset
  ```

  其中 `raw_value` 是解包后的信号值，`physical_value` 是缩放后的信号值。
- `manually specified signals`：您可以指定数据信号。如果选择此选项，请使用 `Signals` 表手动创建信号报文。模块上的输出端口数量取决于您指定的信号数量。例如，如果指定四个信号，则模块有四个输出端口。
- `CANdb specified signals`：您可以指定包含数据信号的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块上的输出端口数量取决于 CANdb 文件中指定的信号数量。例如，如果 CANdb 文件中选定的报文有四个信号，则模块有四个输出端口。
- `ARXML specified signals`：允许您指定 ARXML 文件用于信号定义。这会禁用某些远程选项。从 ARXML 文件读取数据后，您可以切换到 `manually specified signals` 以进一步修改表格。

  有关详细信息，请参阅 ARXML File Support for CAN in Simulink。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataFormat` |
| **类型**：`string` | `character vector` |
| **值**：`'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` `'ARXML specified signals'` |
| **默认值**：`'raw data'` |

### **Database file** — ARXML 或 CAN 数据库文件 字符向量

如果您将 **Data to output as** 参数指定为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。点击 **Browse** 在您的系统上查找数据库文件。数据库文件中指定的报文和信号定义将填充对话框的 **Message** 部分。数据库文件中指定的信号将填充 **Signals** 表。包含非字母数字字符（如等号、& 符号等）的文件名不是有效的数据库文件名。您可以在数据库名称中使用句点。在使用包含非字母数字字符的数据库文件之前，请先重命名它们。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **消息列表** — 字符向量数组的消息列表

如果你为 **数据输入方式** 字段指定了数据库，并且在 **数据库文件** 字段中指定了数据库文件，则此选项可用。你可以选择要查看的消息。随后，**信号** 表会显示所选消息的详细信息。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **名称** — 消息名称 `CAN Msg`（默认）| 字符向量

为你的消息指定一个名称。默认值为 `Msg`。如果你选择输出原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **标识符类型** — 标识符类型 `Standard (11-bit identifier)`（默认）| `Extended (29-bit identifier)`

指定你的消息标识符是 `Standard` 还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11 位标识符，扩展标识符是 29 位标识符。如果你选择输出原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**标识符类型** 会从数据库继承类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认：** `'Standard (11-bit identifier)'` |

### **标识符** — 消息标识符 `0`（默认）| `0 .. 536870911`

指定你的消息 ID。对于标准标识符，此数字必须是 0 到 2047 之间的整数；对于扩展标识符，必须是 0 到 536870911 之间的整数。如果你指定 `–1`，该模块会解包与为消息指定的长度匹配的消息。你也可以使用 `hex2dec` 函数指定十六进制值。如果你选择输出原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'536870911'` |

### **长度（字节）** — CAN 消息长度 `8`（默认）| `0 .. 8`

指定消息的长度。对于 CAN 消息，该值可以为 0-8 字节；对于 CAN FD，该值可以为 0-8、12、16、20、24、32、48 或 64 字节。如果你使用数据库指定的信号作为输出数据，则数据库文件会定义消息的长度。如果你选择输出原始数据或手动指定信号，则此选项可用。

注意：当接收到长度与掩码或网络描述文件中指定的值不同的帧时，该帧会被丢弃。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'8'`、`'12'`、`'16'`、`'20'`、`'24'`、`'32'`、`'48'`、`'64'` |
| **默认：** `'8'` |

### **添加信号** — 添加 CAN 信号

向信号表中添加一个信号。

#### 程序化使用

无

### **删除信号** — 移除 CAN 信号

从信号表中移除所选信号。

#### 程序化使用

无

### **Signals** — 信号表

如果选择手动指定信号或使用数据库文件定义信号，则会显示此表。

如果使用数据库文件，文件中的数据会填充此表，且无法编辑这些字段。要编辑信号信息，请切换到指定信号。

如果已选择手动指定信号，请在此表中手动创建信号。创建的每个信号都具有以下值：

**Name**
:   为信号指定一个描述性名称。模型中的 Simulink 模块会显示此名称。默认值为
    `Signal [row number]`。

**Start bit**
:   指定数据的起始位。起始位是从消息数据起始位置算起的最低有效位。对于 CAN，起始位必须是 0 到 63 的整数；对于 CAN FD，必须是 0 到 511 的整数，且位于消息的位数范围内。（请注意，消息长度以字节为单位指定。）

**Length (bits)**
:   指定信号在消息中占用的位数。长度必须是 1 到 64 的整数。一条消息中所有信号长度的总和受消息长度位数的限制；也就是说，所有信号必须累计适配在消息长度范围内。（请注意，消息长度以字节为单位指定，信号长度以位为单位指定。）

**Byte order**
:   选择以下任一选项：

    - `LE`：字节顺序为小端格式
      (Intel®)。在此格式中，从最低有效位计数到最高有效位，并在跨越字节边界时继续到下一个更高字节。例如，如果以小端格式打包一个字节的数据，起始位为 20，则数据位表类似于下图。

      **从最低有效位到最高地址计数的小端字节顺序**
    - `BE`：字节顺序为大端格式
      (Motorola®)。在此格式中，从最低有效位计数到最高有效位，并在跨越字节边界时继续到下一个更低字节。例如，如果以大端格式打包一个字节的数据，起始位为 20，则数据位表类似于下图。

      **从最低有效位到最低地址计数的大端字节顺序**

    有关详细信息，请参阅 CAN Frame Structure, Byte Order, and Bit Counting。

**数据类型**
:   指定信号如何解释所分配位中的数据。选择：

    - `signed`（默认）
    - `unsigned`
    - `single`
    - `double`

      注意：如果有一个 `double` 信号未与消息字节边界精确对齐，要使用 Embedded Coder® 生成代码，必须在 Configuration Parameters 对话框的 **Hardware Implementation** 窗格中的 **Device Details** 下选中 **Support long long**。

**Multiplex type**
:   指定模块在每个时间步如何从消息中解包信号：

    - `Standard`：在每个时间步解包该信号。
    - `Multiplexor`：解包 `Multiplexor` 信号，即模式信号。每条消息只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果运行时 `Multiplexor` 信号（模式信号）的值与该信号配置的 **Multiplex value** 匹配，则解包该信号。

    例如，一条消息有四个信号，其值如下。

    | Signal Name | Multiplex Type | Multiplex Value |
    | --- | --- | --- |
    | Signal-A | Standard | Not applicable |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | Not applicable |

    在此示例中：

- 该模块在每个时间步解包 Signal-A（标准信号）和 Signal-D（多路复用信号）。
- 如果在某个时间步 Signal-D 的值为 1，则该模块在该时间步解包 Signal-B 以及 Signal-A 和 Signal-D。
- 如果在某个时间步 Signal-D 的值为 0，则该模块在该时间步解包 Signal-C 以及 Signal-A 和 Signal-D。
- 如果 Signal-D 的值不是 1 或 0，则该模块在该时间步不解包任何一个多路复用信号。

**Multiplex value**
:   仅当您将 **Multiplex type** 选择为 `Multiplexed` 时，此选项才可用。您在此处提供的值必须在运行时与 `Multiplexor` 信号值匹配，模块才能解包 `Multiplexed` 信号。**Multiplex value** 必须为正整数或零。

**Factor**
:   指定用于将解包后的原始值转换为物理值（信号值）的 **Factor** 值。有关详细信息，请参阅 **Data input as** 参数转换公式。

**Offset**
:   指定用于将物理值（信号值）转换为解包后的原始值的 **Offset** 值。有关详细信息，请参阅 **Data input as** 参数转换公式。

**Min**、**Max**
:   定义原始信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库中读取。对于 **manually specified signals**，您可以指定信号的最小和最大物理值。默认情况下，这些设置不会裁剪超过其范围的信号值。

#### 编程使用

|  |
| --- |
| **模块参数**：`SignalInfo` |
| **类型**：`string` | `character vector` |

### **Output identifier** — 添加 CAN ID 输出端口 `off`（默认）| `on`

选择此选项可输出 CAN 报文标识符。此端口的数据类型为 `uint32`。

#### 编程使用

|  |
| --- |
| **模块参数**：`IDPort` |
| **类型**：`string` | `character vector` |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Output timestamp** — 添加 Timestamp 输出端口 `off`（默认）| `on`

选择此选项可输出报文时间戳。该值表示报文的接收时间，以模型仿真开始以来经过的秒数来衡量。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `double`。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimestampPort` |
| **类型**：`string` | `character vector` |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Output error** — 添加 Error 输出端口 `off`（默认）| `on`

选择此选项可输出报文错误状态。此选项会向模块添加一个新的输出端口。此端口上的输出值 `1` 表示传入报文是错误帧。如果输出值为 `0`，则没有错误。此端口的数据类型为 `uint8`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ErrorPort` |
| **类型**：`string` | `character vector` |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Output remote** — 添加 Remote 输出端口 `off`（默认）| `on`

选择此选项可输出报文远程帧状态。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 编程使用

|  |
| --- |
| **模块参数**：`RemotePort` |
| **类型**：`string` | `character vector` |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Output length** — 添加 Length 输出端口 `off`（默认）| `on`

选择此选项可输出报文的长度（以字节为单位）。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LengthPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出状态** — 添加状态输出端口 `off`（默认）| `on`

选择此选项以输出消息接收状态。如果模块接收到新消息，状态为 `1`；如果未接收到，状态为 `0`。此选项会向模块添加一个新的输出端口。该端口的数据类型为 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StatusPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出位速率切换（BRS）** — 添加 BRS 输出端口 `off`（默认）| `on`

（对 CAN 协议禁用。）选择此选项以输出消息位速率切换。此选项会向模块添加一个新的输出端口，用于指示是否设置了 CAN FD 消息位速率切换。该端口的数据类型为 `boolean`，指示消息数据阶段的位速率是比仲裁阶段的位速率更快（`true`）还是相同（`false`）。

有关 BRS 的更多信息，请参阅 CAN FD - The basic idea。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BRSPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出错误状态指示器（ESI）** — 添加 ESI 输出端口 `off`（默认）| `on`

（对 CAN 协议禁用。）选择此选项以输出消息错误状态。此选项会向模块添加一个新的输出端口。该端口的数据类型为 `boolean`，指示是否设置了 CAN FD 消息错误状态指示器标志。

有关 ESI 的更多信息，请参阅 CAN FD - The basic idea。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ESIPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出数据长度代码（DLC）** — 添加 DLC 输出端口 `off`（默认）| `on`

（对 CAN 协议禁用。）选择此选项以输出消息数据长度。此选项会向模块添加一个新的输出端口。该端口的数据类型为 `double`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DLCPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

## 所属库

Vehicle Network Toolbox / CAN FD Communication C2000 Microcontroller Blockset / Target Communication Simulink Real-Time / CAN / CAN-FD MSG blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2025a：更新的参数：ARXML 支持

为支持 ARXML 文件定义，以下参数已更新：

- **Data to output as** — 新增选项 `ARXML specified signals`。

- **CANdb file** — 在模块掩码中已重命名为 **Database file**。其程序化名称仍为 `CANdbFile`。

## 描述

从 CAN FD 消息中解包各个信号

CAN FD Unpack 模块在每个时间步使用指定的输出参数将 CAN FD 消息解包为信号数据。数据以各个信号的形式输出。

要使用此模块，您还需要 Simulink® 软件的许可证。

CAN FD Unpack 模块支持：

- Simulink 加速模式。您可以加速 Simulink 模型的执行。有关更多信息，请参阅 Acceleration (Simulink)。

**提示**

- 要处理通过通道传来的每条消息，请勿在函数触发子系统中使用 CAN FD Unpack 模块。有关更多信息，请参阅 Speedgoat® 文档。
- 要处理 J1939 消息，请使用 J1939 Communication 模块库中的模块，而不是此模块。请参阅 J1939 Communication。
