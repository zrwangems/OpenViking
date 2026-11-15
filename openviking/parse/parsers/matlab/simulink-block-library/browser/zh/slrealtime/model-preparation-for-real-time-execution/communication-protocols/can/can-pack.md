---
type: simulink-block
title: 'CAN Pack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / CAN'
documentation_page: 'canpack'
documentation_source_path: 'io_ref/canpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Pack

## 端口

### 输入

### **Data** — CAN 消息信号输入 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

CAN Pack 模块默认有一个输入端口。模块输入的数量是动态的，取决于您为模块指定的信号数量。例如，如果您的消息有四个信号，该模块可以有四个输入端口。

该模块支持以下输入信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持 fixed-point 数据类型。

**提示**

即使您有一个没有信号的零长度消息，仍必须向输入端口提供虚拟数据，以便定义采样时间。在这种情况下，数据值本身会被忽略。

### **CAN Msg ID** — CAN 消息标识符 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

CAN Msg ID 输入端口允许您动态指定 CAN 消息标识符。仅当选中 **Specify CAN identifier from input port** 参数时，该端口才存在。有关详细信息，请参阅 Dynamically Change CAN IDs by CAN Pack Block Input Ports (Vehicle Network Toolbox)。

### 输出

### **CAN Msg** — CAN 消息输出 `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

该模块有一个输出端口，CAN Msg。CAN Pack 模块获取指定的输入信号，并将它们打包成一条 CAN 消息。输出数据类型由 **Output as bus** 参数设置决定。

## 参数

### **Data input as** — 选择您的数据信号 `raw data`（默认） | `manually specified signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：将数据输入为 uint8 向量数组。如果选择此选项，您仅指定消息字段。所有其他信号参数字段均不可用。此选项在您的模块上仅打开一个输入端口。

  转换公式为：

      raw_value = (physical_value - Offset) / Factor

  其中 `physical_value` 是信号的原始值，`raw_value` 是打包后的信号值。
- `manually specified signals`：允许您指定数据信号定义。如果选择此选项，请使用 **Signals** 表创建您的信号。模块输入的数量取决于您指定的信号数量。
- `CANdb specified signals`：允许您指定包含消息和信号定义的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块输入的数量取决于所选消息在 CANdb 文件中指定的信号数量。
- `ARXML specified signals`：允许您指定用于信号定义的 ARXML 文件。这会禁用一些远程选项。从 ARXML 文件读取数据后，您可以切换到 `manually specified signals` 以进一步修改该表。

  有关详细信息，请参阅 ARXML File Support for CAN in Simulink (Vehicle Network Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** `string` | `character vector` |
| **值：** `'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` | `'ARXML specified signals'` |
| **默认值：** `'raw data'` |

### **Database file** — ARXML 或 CAN 数据库文件 character vector

如果您的 **Data is input as** 参数指定为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。单击 **Browse** 以在您的系统中查找数据库文件。数据库文件中指定的消息列表会填充对话框的 **Message** 部分。数据库文件还会为所选消息填充 **Signals** 表。

包含非字母数字字符（例如等号、& 符号等）的文件名不是有效的数据库文件名。您可以在数据库名称中使用句点。在使用数据库文件之前，请重命名它们，使其不包含非字母数字字符。

#### 编程用法

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **Message list** — CAN 消息列表 array of character vectors

如果您在 **Data is input as** 字段中指定数据库，并在 **Database file** 字段中指定数据库文件，则此选项可用。选择消息以在 **Signals** 表中显示信号详细信息。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **Name** — CAN 消息名称 `CAN Msg`（默认） | character vector

为您的 CAN 消息指定名称。默认值为 `CAN Msg`。如果您选择输入原始数据或手动指定信号，则此选项可用。如果您选择使用来自数据库文件的信号，则此选项不可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **Identifier type** — CAN 标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

指定您的 CAN 消息标识符是 `Standard` 还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11 位标识符，扩展标识符是 29 位标识符。如果您选择输入原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**Identifier type** 会从数据库继承类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认值：** `'Standard (11-bit identifier)'` |

### **CAN Identifier** — CAN 消息 ID `0`（默认） | `0` 到 `536870911`

指定您的 CAN 消息 ID。对于标准标识符，此数字必须是 0 到 2047 之间的非负整数；对于扩展标识符，必须是 0 到 536870911 之间的非负整数。您还可以使用 `hex2dec` 函数指定十六进制值。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'536870911'` |

### **Specify CAN identifier from input port** — CAN 消息 ID 值 `off`（默认） | `on`

选中后，您可以通过在模块的输入端口上指定值来动态控制 CAN 标识符（CAN ID）。选择此选项会添加一个名为 CAN Msg ID 的输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `CANIDInput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Length (bytes)** — CAN 消息长度 `8`（默认） | `0` 到 `8`

指定您的 CAN 消息长度，范围为 0 到 8 字节。如果您使用数据库指定的信号作为数据输入，数据库文件会定义您的消息长度。如果不是，此字段默认为 `8`。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'8'` |
| **默认值：** `'8'` |

### **Remote frame** — CAN 消息作为远程帧 `off`（默认） | `on`

将 CAN 消息指定为远程帧。

#### 编程用法

|  |
| --- |
| **模块参数：** `Remote` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Output as bus** — CAN 消息作为总线 `off`（默认） | `on`

选择此选项可让模块将 CAN 消息输出为 Simulink 总线信号。有关 Simulink 总线对象的详细信息，请参阅 Composite Interfaces。

#### 编程用法

|  |
| --- |
| **模块参数：** `BusOutput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Add signal** — 添加 CAN 信号

向信号表添加一个新信号。

#### 编程用法

无

### **Delete signal** — 删除 CAN 信号

从信号表中删除所选信号。

#### 编程用法

无

### **Signals** — 信号表 table

如果您选择手动指定信号或使用数据库文件定义信号，则会出现此表。

如果您使用的是数据库文件，文件中的数据会填充此表，并且您无法编辑这些字段。要编辑信号信息，请切换到手动指定的信号。

如果您已选择手动指定信号，请在此表中创建您的信号。您创建的每个信号都具有以下值：

**Name**
:   为您的信号指定描述性名称。您模型中的 Simulink 模块会显示此名称。默认值为 `Signal [row number]`。

**Start bit**
:   指定数据的起始位。起始位是从消息数据开头开始计数的最低有效位。起始位必须是 0 到 63 之间的整数。

**Length (bits)**
:   指定信号在消息中占用的位数。长度必须是 1 到 64 之间的整数。

**Byte order**
:   选择以下任一选项：

    - `LE`：其中字节顺序为 little-endian 格式（Intel®）。在此格式中，您从最低有效位到最高有效位对位进行计数。例如，如果您以 little-endian 格式打包一个字节的数据，起始位为 20，则数据位表类似于此图。

      **从最低有效位到最高地址计数的 Little-Endian 字节顺序**
    - `BE`：其中字节顺序为 big-endian 格式（Motorola®）。在此格式中，您从最低有效位到最高有效位对位进行计数。例如，如果您以 big-endian 格式打包一个字节的数据，起始位为 20，则数据位表类似于此图。

      **从最低有效位到最低地址计数的 Big-Endian 字节顺序**

**Data type**
:   指定信号如何解释分配位中的数据。从以下选项中选择：

    - `signed`（默认）
    - `unsigned`
    - `single`
    - `double`

**Multiplex type**
:   指定模块在每个时间步如何将信号打包到 CAN 消息中：

    - `Standard`：
      该信号在每个时间步都会被打包。
    - `Multiplexor`：会打包 `Multiplexor` 信号，即模式信号。每条消息只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果运行时 `Multiplexor` 信号（模式信号）的值与此信号配置的 **Multiplex value** 匹配，则会打包该信号。

    例如，一条消息具有以下这些信号，其类型和值如下。

    | 信号名称 | 复用类型 | 复用值 |
    | --- | --- | --- |
    | Signal-A | Standard | 不适用 |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | 不适用 |

    在此示例中：

    - 该模块在每个时间步都会打包 Signal-A（Standard 信号）和 Signal-D（Multiplexor 信号）。
    - 如果在某个时间步 Signal-D 的值为 1，则该模块在该时间步会将 Signal-B 与 Signal-A 和 Signal-D 一起打包。
    - 如果在某个时间步 Signal-D 的值为 0，则该模块在该时间步会将 Signal-C 与 Signal-A 和 Signal-D 一起打包。
    - 如果 Signal-D 的值不是 1 或 0，则该模块在该时间步不会打包任一 Multiplexed 信号。

**Multiplex value**
:   仅当您已将 **Multiplex type** 选择为 `Multiplexed` 时，此选项才可用。您提供的值必须在运行时与 `Multiplexor` 信号值匹配，模块才会打包 `Multiplexed` 信号。**Multiplex value** 必须是正整数或零。

**Factor**
:   指定要应用的 **Factor** 值，以将物理值（信号值）转换为消息中打包的原始值。有关详细信息，请参阅 **Data input as** 参数转换公式。

**Offset**
:   指定要应用的 **Offset** 值，以将物理值（信号值）转换为消息中打包的原始值。有关详细信息，请参阅 **Data input as** 参数转换公式。

**Min**、**Max**
:   定义信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库中读取。对于 **manually specified signals**，您可以指定信号的最小和最大物理值。默认情况下，这些设置不会裁剪超过设置的信号值。

#### 编程用法

|  |
| --- |
| **模块参数：** `SignalInfo` |
| **类型：** `string` | `character vector` |

## 所属库

Vehicle Network Toolbox / CAN Communication C2000 Microcontroller Blockset / Target Communication Embedded Coder / Embedded Targets / Host Communication Simulink Real-Time / CAN / CAN MSG blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

### R2025a：更新的参数：ARXML 支持

为支持 ARXML 文件定义，以下参数已更新：

- **Data input as** — 新增选项 `ARXML specified signals`。
- **CANdb file** — 在模块封装中已重命名为 **Database file**。其编程名称仍为 `CANdbFile`。

### R2024b：新参数：Specify CAN identifier from input port

**Specify CAN identifier from input port** 参数添加了一个输入端口 **CAN Msg ID**，以支持动态指定 CAN 标识符。

## 描述

将各个信号打包为 CAN 消息

CAN Pack 模块在仿真期间按指定间隔将信号数据加载到 CAN 消息中。

要使用此模块，您必须拥有 Simulink® 软件的许可证。

CAN Pack 模块支持：

- Simulink accelerator 和 rapid accelerator 模式。您可以加速 Simulink 模型的执行。有关详细信息，请参阅 Acceleration。
- 模型引用。您的模型可以将其他 Simulink 模型作为模块化组件包含在内。有关详细信息，请参阅 Model References。

**提示**

- 此模块可用于编码最多 8 字节的 J1939 参数组信号。但是，要处理 J1939 消息，最好使用 J1939 Communication 模块库中的模块，而不是此模块。
  请参阅 J1939。
