---
type: simulink-block
title: 'CAN FD Pack'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Blocks for Embedded Targets'
documentation_page: 'canfdpack'
documentation_source_path: 'ref/canfdpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN FD Pack

## 端口

### 输入

### **Data** — CAN FD 消息信号输入 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

CAN FD Pack 模块默认有一个输入端口。模块输入的数量是动态的，取决于您为模块指定的信号数量。例如，如果您的消息有四个信号，则该模块可以有四个输入端口。

该模块支持以下输入信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点数据类型。

**提示**

即使您有一个没有信号的零长度消息，为了定义采样时间，您仍然必须向输入端口提供虚拟数据。在这种情况下，数据值本身会被忽略。

### **CAN Msg ID** — CAN 消息标识符 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

CAN Msg ID 输入端口允许您动态指定 CAN 消息标识符。仅当选中 **从输入端口指定 CAN 标识符** 参数时，此端口才存在。有关详细信息，请参阅 Dynamically Change CAN IDs by CAN Pack Block Input Ports (Vehicle Network Toolbox)。

### 输出

### **Msg** — CAN FD 消息输出 `CAN_FD_MESSAGE_BUS`

该模块有一个输出端口 Msg。CAN FD Pack 模块获取指定的输入信号，并将它们打包成一条 CAN FD 消息，作为 Simulink `CAN_FD_MESSAGE_BUS` 信号输出。有关 Simulink 总线对象的详细信息，请参阅 Composite Interfaces。

## 参数

### **数据输入形式** — 选择您的数据信号 `raw data` (default) | `manually specified signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：将输入数据作为 uint8 向量数组。如果选择此选项，您只需指定消息字段。所有其他信号参数字段均不可用。此选项仅在您的模块上打开一个输入端口。

  转换公式为：

  ```
  raw_value = (physical_value - Offset) / Factor
  ```

  其中 `physical_value` 是信号的原始值，`raw_value` 是打包后的信号值。
- `manually specified signals`：允许您指定数据信号定义。如果选择此选项，请使用 **信号** 表创建信号。模块输入的数量取决于您指定的信号数量。
- `CANdb specified signals`：允许您指定包含消息和信号定义的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块输入的数量取决于 CANdb 文件中为所选消息指定的信号数量。
- `ARXML specified signals`：允许您指定用于信号定义的 ARXML 文件。这会禁用一些远程选项。从 ARXML 文件读取数据后，您可以切换到 `manually specified signals` 以进一步修改表。

  有关详细信息，请参阅 ARXML File Support for CAN in Simulink (Vehicle Network Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** `string` | `character vector` |
| **值：** `'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` `'ARXML specified signals'` |
| **默认值：** `'raw data'` |

### **数据库文件** — ARXML 或 CAN 数据库文件 character vector

如果将 **数据输入为** 参数指定为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。单击 **浏览** 以在您的系统上查找数据库文件。数据库文件中指定的消息列表会填充对话框的 **消息** 部分。数据库文件还会为所选消息填充 **信号** 表。包含非字母数字字符（例如等号、& 符号等）的文件名不是有效的数据库文件名。您可以在数据库名称中使用句点。在使用数据库文件之前，请使用非字母数字字符重命名它们。

#### 编程使用

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **消息列表** — CAN 消息列表 array of character vectors

如果您在 **数据输入为** 字段中指定数据库，并在 **数据库文件** 字段中指定数据库文件，则此选项可用。选择消息以在 **信号** 表中显示信号详细信息。

#### 编程使用

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **名称** — CAN FD 消息名称 `CAN Msg` (default) | character vector

指定 CAN FD 消息的名称。默认值为 `CAN Msg`。如果您选择输入原始数据或手动指定信号，则此选项可用。如果您选择使用数据库文件中的信号，则此选项不可用。

#### 编程使用

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **协议模式** — CAN FD 消息协议 `CAN FD` (default) | `CAN`

指定消息协议模式。

#### 编程使用

|  |
| --- |
| **模块参数：** `ProtocolMode` |
| **类型：** `string` | `character vector` |
| **值：** `'CAN FD'` | `'CAN'` |
| **默认值：** `'CAN FD'` |

### **标识符类型** — CAN 标识符类型 `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

指定您的 CAN 消息标识符是 `Standard` 还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11 位标识符，扩展标识符是 29 位标识符。如果您选择输入原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**标识符类型** 从数据库继承该类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认值：** `'Standard (11-bit identifier)'` |

### **标识符** — 消息标识符 `0` (default) | `0 .. 536870911`

指定您的消息 ID。对于标准标识符，此数字必须是 0 到 2047 的整数；对于扩展标识符，必须是 0 到 536870911 的整数。您还可以使用 `hex2dec` 函数指定十六进制值。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程使用

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` to `'536870911'` |

### **从输入端口指定 CAN 标识符** — CAN 消息 ID 值 `off` (default) | `on`

选中后，您可以通过在模块的输入端口上指定值来动态控制 CAN 标识符 (CAN ID)。选择此选项会添加一个名为 CAN Msg ID 的输入端口。

#### 编程使用

|  |
| --- |
| **模块参数：** `CANIDInput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **长度 (bytes)** — CAN FD 消息长度 `8` (default) | `0` to `64`

指定消息的长度。对于 CAN 消息，该值可以为 0 到 8 bytes；对于 CAN FD，该值可以为 0 到 8、12、16、20、24、32、48 或 64 bytes。如果您使用数据库指定的信号作为数据输入，则数据库文件定义消息的长度。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程使用

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` to `'8'`, `'12'`, `'16'`, `'20'`, `'24'`, `'32'`, `'48'`, `'64'` |
| **默认值：** `'8'` |

### **远程帧** — CAN 消息作为远程帧 `off` (default) | `on`

（对于 CAN FD 协议模式禁用。）将 CAN 消息指定为远程帧。

#### 编程使用

|  |
| --- |
| **模块参数：** `Remote` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **位速率切换 (BRS)** — 启用位速率切换 `off` (default) | `on`

（对于 CAN 协议模式禁用。）启用位速率切换。

#### 编程使用

|  |
| --- |
| **模块参数：** `BRSSwitch` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **添加信号** — 添加 CAN FD 信号

向信号表中添加一个信号。

#### 编程使用

无

### **删除信号** — 删除 CAN FD 信号

从信号表中移除所选信号。

#### 编程使用

无

### **信号** — 信号表 table

如果您选择手动指定信号或使用数据库文件定义信号，则会出现此表。

如果您使用的是数据库文件，文件中的数据会填充此表，并且您无法编辑字段。要编辑信号信息，请切换到手动指定信号。

如果您已选择手动指定信号，请在此表中创建信号。您创建的每个信号都有以下值：

**名称**
:   为您的信号指定一个描述性名称。模型中的 Simulink 模块会显示此名称。默认值为 `Signal [row number]`。

**起始位**
:   指定数据的起始位。起始位是从消息数据开头算起的最低有效位。对于 CAN，起始位必须是 0 到 63 的整数；对于 CAN FD，必须是 0 到 511 的整数，且位于消息的位数范围内。（请注意，消息长度以 bytes 为单位指定。）

**长度 (bits)**
:   指定信号在消息中占用的位数。长度必须是 1 到 64 的整数。一条消息中所有信号长度之和受消息长度中的位数限制；也就是说，所有信号必须累计适配在消息长度内。（请注意，消息长度以 bytes 为单位指定，信号长度以 bits 为单位。）

**字节序**
:   选择以下任一选项：

    - `LE`：字节序为 little-endian 格式（Intel®）。在此格式中，您从最低有效位计数到最高有效位。例如，如果您以 little-endian 格式打包一个字节的数据，起始位为 20，则数据位表类似于此图。

      **小端字节序：从最低有效位计数到最高地址**
    - `BE`：字节序为 big-endian 格式（Motorola®）。在此格式中，您从最低有效位计数到最高有效位。例如，如果您以 big-endian 格式打包一个字节的数据，起始位为 20，则数据位表类似于此图。

      **大端字节序：从最低有效位计数到最低地址**

**数据类型**
:   指定信号如何解释分配位中的数据。选择：

    - `signed` (default)
    - `unsigned`
    - `single`
    - `double`

      注意：如果您有一个 `double` 信号未与消息字节边界精确对齐，要使用 Embedded Coder® 生成代码，您必须在配置参数对话框的 **硬件实现** 窗格中的 **设备详细信息** 下选中 **支持 long long**。

**多路复用类型**
:   指定模块在每个时间步如何将信号打包到消息中：

    - `Standard`：信号在每个时间步都会被打包。
    - `Multiplexor`：打包 `Multiplexor` 信号或模式信号。每条消息只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果运行时 `Multiplexor` 信号（模式信号）的值与此信号配置的 **多路复用值** 匹配，则打包该信号。

    例如，一条消息有四个信号，其类型和值如下。

    | 信号名称 | 多路复用类型 | 多路复用值 |
    | --- | --- | --- |
    | Signal-A | Standard | 不适用 |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | 不适用 |

    在此示例中：

    - 模块在每个时间步都会打包 Signal-A（Standard 信号）和 Signal-D（Multiplexor 信号）。
    - 如果在特定时间步 Signal-D 的值为 1，则模块在该时间步会将 Signal-B 与 Signal-A 和 Signal-D 一起打包。
    - 如果在特定时间步 Signal-D 的值为 0，则模块在该时间步会将 Signal-C 与 Signal-A 和 Signal-D 一起打包。
    - 如果 Signal-D 的值不是 1 或 0，则模块在该时间步不会打包任一 Multiplexed 信号。

**多路复用值**
:   仅当您将 **多路复用类型** 选择为 `Multiplexed` 时，此选项才可用。您在此处提供的值必须在运行时与 `Multiplexor` 信号值匹配，模块才会打包 `Multiplexed` 信号。**多路复用值** 必须是正整数或零。

**Factor**
:   指定要应用的 **Factor** 值，以将物理值（信号值）转换为打包在消息中的原始值。请参阅 **数据输入形式** 参数转换公式，以了解如何将物理值转换为打包到消息中的原始值。

**Offset**
:   指定要应用的 **Offset** 值，以将物理值（信号值）转换为打包在消息中的原始值。请参阅 **数据输入形式** 参数转换公式，以了解如何将物理值转换为打包到消息中的原始值。

**最小值**、**最大值**
:   定义信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库文件读取。对于 **manually specified signals**，您可以指定信号的最小和最大物理值。默认情况下，这些设置不会裁剪超过它们的信号值。

#### 编程使用

|  |
| --- |
| **模块参数：** `SignalInfo` |
| **类型：** `string` | `character vector` |

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

- **数据输入形式** — 新增选项 `ARXML specified signals`。

- **CANdb 文件** — 在模块掩码中已重命名为 **数据库文件**。其编程名称仍为 `CANdbFile`。

### R2024b：新参数：从输入端口指定 CAN 标识符

参数 **从输入端口指定 CAN 标识符** 添加了一个输入端口 **CAN Msg ID**，以支持动态指定 CAN 标识符。

## 描述

将各个信号打包为 CAN FD 总线消息

CAN FD Pack 模块在仿真期间按指定间隔将信号数据加载到消息中。

要使用此模块，您还需要 Simulink® 软件的许可证。

CAN FD Pack 模块支持：

- 使用 Simulink 加速模式。使用此功能，您可以加速 Simulink 模型的执行。有关详细信息，请参阅 Acceleration。

**提示**

- 要处理 J1939 消息，请使用 J1939 Communication 模块库中的模块，而不是此模块。
