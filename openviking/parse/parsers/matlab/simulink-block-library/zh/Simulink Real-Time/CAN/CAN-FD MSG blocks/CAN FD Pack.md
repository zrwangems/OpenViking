---
type: simulink-block
title: 'CAN FD Pack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'CAN / CAN-FD MSG blocks'
documentation_page: 'canfdpack'
documentation_source_path: 'io_ref/canfdpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN FD Pack

## 端口
```yaml
ports:
- name: Data
  summary: CAN FD 消息信号输入 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean
  direction: input
- name: CAN Msg ID
  summary: CAN 消息标识符 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
  direction: input
- name: Msg
  summary: CAN FD 消息输出 CAN_FD_MESSAGE_BUS
  direction: output
```

### 输入

### **Data** — CAN FD 消息信号输入 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

CAN FD Pack 模块默认有一个输入端口。模块输入的数量是动态的，取决于您为模块指定的信号数量。例如，如果您的消息有四个信号，则该模块可以有四个输入端口。

该模块支持以下输入信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点数据类型。

**提示**

即使您有一个没有信号的零长度消息，您仍然必须为输入端口提供虚拟数据，以便定义采样时间。在这种情况下，数据值本身会被忽略。

### **CAN Msg ID** — CAN 消息标识符 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

CAN Msg ID 输入端口允许您动态指定 CAN 消息标识符。仅当选中 **Specify CAN identifier from input port** 参数时，此端口才存在。有关详细信息，请参阅 Dynamically Change CAN IDs by CAN Pack Block Input Ports (Vehicle Network Toolbox)。

### 输出

### **Msg** — CAN FD 消息输出 `CAN_FD_MESSAGE_BUS`

该模块有一个输出端口 Msg。CAN FD Pack 模块获取指定的输入信号并将其打包为 CAN FD 消息，以 Simulink `CAN_FD_MESSAGE_BUS` 信号的形式输出。有关 Simulink 总线对象的详细信息，请参阅 Composite Interfaces。
## 参数
```yaml
parameters:
- name: Data input as
  summary: 选择您的数据信号 raw data（默认）| manually specified signals | CANdb specified signals | ARXML specified signals
  group: ''
  block_parameter: DataFormat
  type: string | character vector
  values: '''raw data'' | ''manually specified signals'' | ''CANdb specified signals'' ''ARXML specified signals'''
  default: '''raw data'''
- name: Database file
  summary: ARXML 或 CAN 数据库文件 character vector
  group: ''
  block_parameter: CANdbFile
  type: string | character vector
- name: Message list
  summary: CAN 消息列表字符向量数组
  group: ''
  block_parameter: MsgList
  type: string | character vector
- name: Name
  summary: CAN FD 消息名称 CAN Msg（默认）| 字符向量
  group: ''
  block_parameter: MsgName
  type: string | character vector
- name: Protocol mode
  summary: CAN FD 消息协议 CAN FD（默认）| CAN
  group: ''
  block_parameter: ProtocolMode
  type: string | character vector
  values: '''CAN FD'' | ''CAN'''
- name: Identifier type
  summary: CAN 标识符类型 Standard (11-bit identifier)（默认）| Extended (29-bit identifier)
  group: ''
  block_parameter: MsgIDType
  type: string | character vector
  values: '''Standard (11-bit identifier)'' | ''Extended (29-bit identifier)'''
- name: Identifier
  summary: 消息标识符 0（默认）| 0 .. 536870911
  group: ''
  block_parameter: MsgIdentifier
  type: string | character vector
  values: '''0'' 到 ''536870911'''
- name: Specify CAN identifier from input port
  summary: CAN 消息 ID 值 off（默认）| on
  group: ''
  block_parameter: CANIDInput
  type: string | character vector
  values: '''off'' | ''on'''
- name: Length (bytes)
  summary: CAN FD 消息长度 8（默认）| 0 到 64
  group: ''
  block_parameter: MsgLength
  type: string | character vector
  values: '''0'' 到 ''8''、''12''、''16''、''20''、''24''、''32''、''48''、''64'''
- name: Remote frame
  summary: CAN 消息作为远程帧 off（默认）| on
  group: ''
  block_parameter: Remote
  type: string | character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Bit Rate Switch (BRS)
  summary: 启用位速率切换 off（默认）| on
  group: ''
  block_parameter: BRSSwitch
  type: string | character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Add signal
  summary: 添加 CAN FD 信号
  group: ''
- name: Delete signal
  summary: 删除 CAN FD 信号
  group: ''
- name: Signals
  summary: 信号表
  group: ''
  block_parameter: SignalInfo
  type: string | character vector
```

### **Data input as** — 选择您的数据信号 `raw data`（默认）| `manually specified signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：以 uint8 向量数组形式输入数据。如果选择此选项，您只需指定消息字段。所有其他信号参数字段均不可用。此选项在您的模块上仅打开一个输入端口。

  转换公式为：

  ```
  raw_value = (physical_value - Offset) / Factor
  ```

  其中 `physical_value` 是信号的原始值，`raw_value` 是打包后的信号值。
- `manually specified signals`：允许您指定数据信号定义。如果选择此选项，请使用 **Signals** 表创建信号。模块输入的数量取决于您指定的信号数量。
- `CANdb specified signals`：允许您指定包含消息和信号定义的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块输入的数量取决于 CANdb 文件中为所选消息指定的信号数量。
- `ARXML specified signals`：允许您指定用于信号定义的 ARXML 文件。这会禁用某些远程选项。从 ARXML 文件读取数据后，您可以切换到 `manually specified signals` 以进一步修改表格。

  有关详细信息，请参阅 ARXML File Support for CAN in Simulink (Vehicle Network Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataFormat` |
| **类型**：`string` | `character vector` |
| **值**：`'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` `'ARXML specified signals'` |
| **默认值**：`'raw data'` |

### **Database file** — ARXML 或 CAN 数据库文件 character vector

如果您将 **Data is input as** 参数指定为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。单击 **Browse** 以在您的系统上查找数据库文件。数据库文件中指定的消息列表将填充对话框的 **Message** 部分。数据库文件还会为所选消息填充 **Signals** 表。包含非字母数字字符（如等号、& 符号等）的文件名不是有效的数据库文件名。您可以在数据库名称中使用句点。在使用数据库文件之前，请使用非字母数字字符重命名它们。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **Message list** — CAN 消息列表字符向量数组

如果在 **Data is input as** 字段中指定数据库，并且在 **Database file** 字段中指定数据库文件，则此选项可用。选择消息以在 **Signals** 表中显示信号详细信息。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **Name** — CAN FD 消息名称 `CAN Msg`（默认）| 字符向量

指定 CAN FD 消息的名称。默认值为 `CAN Msg`。如果选择输入原始数据或手动指定信号，则此选项可用。如果选择使用数据库文件中的信号，则此选项不可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **Protocol mode** — CAN FD 消息协议 `CAN FD`（默认）| `CAN`

指定消息协议模式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProtocolMode` |
| **类型：** `string` | `character vector` |
| **值：** `'CAN FD'` | `'CAN'` |
| **默认：** `'CAN FD'` |

### **Identifier type** — CAN 标识符类型 `Standard (11-bit identifier)`（默认）| `Extended (29-bit identifier)`

指定 CAN 消息标识符是 `Standard` 还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11 位标识符，扩展标识符是 29 位标识符。如果选择输入原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**Identifier type** 从数据库继承类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认：** `'Standard (11-bit identifier)'` |

### **Identifier** — 消息标识符 `0`（默认）| `0 .. 536870911`

指定消息 ID。对于标准标识符，此数字必须是 0 到 2047 的正整数；对于扩展标识符，此数字必须是 0 到 536870911 的正整数。也可以使用 `hex2dec` 函数指定十六进制值。如果选择输入原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'536870911'` |

### **Specify CAN identifier from input port** — CAN 消息 ID 值 `off`（默认）| `on`

选中后，可以通过模块上的输入端口指定值来动态控制 CAN 标识符（CAN ID）。选择此选项会添加一个名为 CAN Msg ID 的输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CANIDInput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Length (bytes)** — CAN FD 消息长度 `8`（默认）| `0` 到 `64`

指定消息的长度。对于 CAN 消息，该值可以为 0 到 8 字节；对于 CAN FD，该值可以为 0 到 8、12、16、20、24、32、48 或 64 字节。如果使用数据库指定的信号作为数据输入，则数据库文件定义消息的长度。如果选择输入原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'8'`、`'12'`、`'16'`、`'20'`、`'24'`、`'32'`、`'48'`、`'64'` |
| **默认：** `'8'` |

### **Remote frame** — CAN 消息作为远程帧 `off`（默认）| `on`

（在 CAN FD 协议模式下禁用。）将 CAN 消息指定为远程帧。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Remote` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Bit Rate Switch (BRS)** — 启用位速率切换 `off`（默认）| `on`

（在 CAN 协议模式下禁用。）启用位速率切换。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BRSSwitch` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Add signal** — 添加 CAN FD 信号

向信号表中添加一个信号。

#### 程序化使用

无

### **Delete signal** — 删除 CAN FD 信号

从信号表中移除所选信号。

#### 程序化使用

无

### **Signals** — 信号表

当您选择手动指定信号或使用数据库文件定义信号时，将显示此表。

如果您使用数据库文件，文件中的数据将填充此表，您无法编辑这些字段。要编辑信号信息，请切换到手动指定信号。

如果您已选择手动指定信号，请在此表中创建信号。您创建的每个信号都具有以下值：

**Name**
:   为信号指定一个描述性名称。模型中的 Simulink 模块将显示此名称。默认值为
    `Signal [row number]`。

**Start bit**
:   指定数据的起始位。起始位是从消息数据起始处开始计数的最低有效位。对于 CAN，起始位必须是 0 到 63 的整数，对于 CAN FD 为 0 到 511，且在消息的位数范围内。（请注意，消息长度以字节为单位指定。）

**Length (bits)**
:   指定信号在消息中占用的位数。长度必须是 1 到 64 的整数。一条消息中所有信号长度的总和受消息长度的位数限制；也就是说，所有信号必须累积地适应消息的长度。（请注意，消息长度以字节为单位指定，信号长度以位为单位指定。）

**Byte order**
:   选择以下任一选项：

    - `LE`：字节顺序为小端格式（Intel®）。在此格式中，您从最低有效位计数到最高有效位。例如，如果您以小端格式打包一个字节的数据，起始位为 20，则数据位表类似于下图。

      **从小端字节序的最低有效位计数到最高地址**
    - `BE`：字节顺序为大端格式（Motorola®）。在此格式中，您从最低有效位计数到最高有效位。例如，如果您以大端格式打包一个字节的数据，起始位为 20，则数据位表类似于下图。

      **从大端字节序的最低有效位计数到最低地址**

**数据类型**
:   指定信号如何解释所分配位中的数据。选择：

    - `signed`（默认）
    - `unsigned`
    - `single`
    - `double`

      注意：如果您有一个 `double` 信号未与消息字节边界精确对齐，要使用 Embedded Coder® 生成代码，您必须在配置参数对话框的 **Hardware Implementation** 窗格中的 **Device Details** 下勾选 **Support long long**。

**Multiplex type**
:   指定模块在每个时间步如何将信号打包到消息中：

    - `Standard`：信号在每个时间步被打包。
    - `Multiplexor`：打包 `Multiplexor` 信号，即模式信号。
      每条消息只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果运行时 `Multiplexor` 信号（模式信号）的值与此信号配置的 **Multiplex value** 匹配，则打包该信号。

    例如，一条消息有四个信号，其类型和值如下。

    | 信号名称 | 多路复用类型 | 多路复用值 |
    | --- | --- | --- |
    | Signal-A | Standard | 不适用 |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | 不适用 |

    在此示例中：

- 该模块在每个时间步中打包 Signal-A（标准信号）和 Signal-D（多路复用器信号）。
- 如果在某个特定时间步中 Signal-D 的值为 1，则该模块在该时间步中将 Signal-B 与 Signal-A 和 Signal-D 一起打包。
- 如果在某个特定时间步中 Signal-D 的值为 0，则该模块在该时间步中将 Signal-C 与 Signal-A 和 Signal-D 一起打包。
- 如果 Signal-D 的值不是 1 或 0，则该模块在该时间步中不打包任何一个多路复用信号。

**Multiplex value**
:   仅当您将 **Multiplex type** 选择为 `Multiplexed` 时，此选项才可用。您在此处提供的值必须在运行时与 `Multiplexor` 信号值匹配，模块才会打包 `Multiplexed` 信号。**Multiplex value** 必须为正整数或零。

**Factor**
:   指定要应用的 **Factor** 值，以将物理值（信号值）转换为打包在报文中的原始值。请参阅 **Data input as** 参数转换公式，以了解物理值如何转换为打包到报文中的原始值。

**Offset**
:   指定要应用的 **Offset** 值，以将物理值（信号值）转换为打包在报文中的原始值。请参阅 **Data input as** 参数转换公式，以了解物理值如何转换为打包到报文中的原始值。

**Min**、**Max**
:   定义信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库文件中读取。对于 **manually specified signals**，您可以指定信号的最小和最大物理值。默认情况下，这些设置不会裁剪超过它们的信号值。

#### 编程使用

|  |
| --- |
| **模块参数**：`SignalInfo` |
| **类型**：`string` | `character vector` |
## 所属库

Vehicle Network Toolbox / CAN FD Communication C2000 Microcontroller Blockset / Target Communication Simulink Real-Time / CAN / CAN-FD MSG blocks

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2025a: Updated parameters: ARXML support

为支持 ARXML 文件定义，以下参数已更新：

- **数据输入方式** — 新增选项 `ARXML specified
  signals`.

- **CANdb file** — Has been renamed to **Database
  file** 在模块掩码中。其程序化名称保持不变
  `CANdbFile`.

### R2024b：新参数：从输入端口指定 CAN 标识符

参数 **从输入端口指定 CAN 标识符** 新增了一个
输入端口 **CAN Msg ID**，以支持动态指定 CAN 标识符。

## 描述

将各个信号打包为 CAN FD 总线报文

CAN FD Pack 模块在指定间隔内将信号数据加载到报文中
simulation.

要使用此模块，您还需要 Simulink® 软件的许可证。

CAN FD Pack 模块支持：

- 使用 Simulink 加速模式。使用此功能，您可以加快
  Simulink 模型的执行速度。有关详细信息，请参阅加速。

**Tip**

- 要处理 J1939 报文，请使用 J1939 通信模块库中的模块
  而不是此模块。请参阅 J1939。
