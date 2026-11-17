---
type: simulink-block
title: 'CAN Pack'
family: 'embedded-targets'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Embedded Targets / Host Communication'
documentation_page: 'canpack'
documentation_source_path: '../ecoder/ref/canpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Pack

## 端口

### 输入

### **Data** — CAN 消息信号输入 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

CAN Pack 模块默认具有一个输入端口。模块输入的数量是动态的，取决于您为模块指定的信号数量。例如，如果消息包含四个信号，则该模块可以具有四个输入端口。

该模块支持以下输入信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点数据类型。

**提示**

即使您有一条不含任何信号的零长度消息，仍必须向输入端口提供虚拟数据，以便定义采样时间。在这种情况下，数据值本身会被忽略。

### **CAN Msg ID** — CAN 消息标识符 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

CAN Msg ID 输入端口允许您动态指定 CAN 消息标识符。仅当选中 **从输入端口指定 CAN 标识符** 参数时，此端口才存在。有关详细信息，请参阅通过 CAN Pack 模块输入端口动态更改 CAN ID (Vehicle Network Toolbox)。

### 输出

### **CAN Msg** — CAN 消息输出 `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

此模块具有一个输出端口 CAN Msg。CAN Pack 模块接受指定的输入信号，并将其打包为 CAN 消息。输出数据类型由 **作为总线输出** 参数设置决定。

## 参数

### **数据输入方式** — 选择数据信号 `raw data` (默认) | `manually specified signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：以 uint8 向量数组形式输入数据。如果选择此选项，则只需指定消息字段。所有其他信号参数字段均不可用。此选项仅在模块上打开一个输入端口。

  转换公式为：

  ```
  raw_value = (physical_value - Offset) / Factor
  ```

  其中，`physical_value` 是信号的原始值，`raw_value` 是打包后的信号值。
- `manually specified signals`：允许您指定数据信号定义。如果选择此选项，请使用 **信号** 表创建信号。模块输入的数量取决于您指定的信号数量。
- `CANdb specified signals`：允许您指定包含消息和信号定义的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块输入的数量取决于 CANdb 文件中为所选消息指定的信号数量。
- `ARXML specified signals`：允许您指定用于信号定义的 ARXML 文件。这会禁用一些远程选项。从 ARXML 文件读取数据后，您可以切换到 `manually specified signals`，以进一步修改该表。

  有关详细信息，请参阅 Simulink 中对 CAN 的 ARXML 文件支持 (Vehicle Network Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** `string` | `character vector` |
| **值：** `'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` | `'ARXML specified signals'` |
| **默认值：** `'raw data'` |

### **数据库文件** — ARXML 或 CAN 数据库文件 character vector

如果将 **数据输入方式** 参数指定为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。点击 **浏览** 以在系统上查找数据库文件。数据库文件中指定的消息列表将填充对话框的 **消息** 部分。数据库文件还会为所选消息填充 **信号** 表。

包含非字母数字字符（例如等号、与号等）的文件名不是有效的数据库文件名。数据库名称中可以使用句点。在使用数据库文件之前，请对名称中含有非字母数字字符的文件进行重命名。

#### 编程用法

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **消息列表** — CAN 消息列表 character vector 数组

如果您在 **数据输入方式** 字段中指定了数据库，并在 **数据库文件** 字段中指定了数据库文件，则此选项可用。选择要在 **信号** 表中显示其信号详细信息的消息。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **名称** — CAN 消息名称 `CAN Msg` (默认) | character vector

指定 CAN 消息的名称。默认值为 `CAN Msg`。如果您选择输入原始数据或手动指定信号，则此选项可用。如果您选择使用数据库文件中的信号，则此选项不可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **标识符类型** — CAN 标识符类型 `Standard (11-bit identifier)` (默认) | `Extended (29-bit identifier)`

指定 CAN 消息标识符是 `Standard` 类型还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11-bit 标识符，扩展标识符是 29-bit 标识符。如果您选择输入原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**标识符类型** 从数据库继承该类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认值：** `'Standard (11-bit identifier)'` |

### **CAN 标识符** — CAN 消息 ID `0` (默认) | `0` 到 `536870911`

指定 CAN 消息 ID。对于标准标识符，该数值必须是 0 到 2047 范围内的正整数；对于扩展标识符，该数值必须是 0 到 536870911 范围内的正整数。您还可以使用 `hex2dec` 函数指定十六进制值。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'536870911'` |

### **从输入端口指定 CAN 标识符** — CAN 消息 ID 值 `off` (默认) | `on`

选中后，您可以通过模块上的输入端口指定值，从而动态控制 CAN 标识符 (CAN ID)。选择此选项会添加一个名为 CAN Msg ID 的输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `CANIDInput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **长度 (bytes)** — CAN 消息长度 `8` (默认) | `0` 到 `8`

指定 CAN 消息的长度，范围为 0 到 8 bytes。如果数据输入使用数据库指定的信号，则数据库文件会定义消息长度。否则，此字段默认为 `8`。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'8'` |
| **默认值：** `'8'` |

### **远程帧** — 将 CAN 消息作为远程帧 `off` (默认) | `on`

将 CAN 消息指定为远程帧。

#### 编程用法

|  |
| --- |
| **模块参数：** `Remote` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **作为总线输出** — 将 CAN 消息作为总线 `off` (默认) | `on`

选择此选项可使模块将 CAN 消息作为 Simulink 总线信号输出。有关 Simulink 总线对象的详细信息，请参阅复合接口。

#### 编程用法

|  |
| --- |
| **模块参数：** `BusOutput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **添加信号** — 添加 CAN 信号

向信号表中添加新信号。

#### 编程用法

无

### **删除信号** — 删除 CAN 信号

从信号表中删除所选信号。

#### 编程用法

无

### **信号** — 信号表 table

如果您选择手动指定信号或使用数据库文件定义信号，则会显示此表。

如果您使用数据库文件，文件中的数据将填充此表，并且您无法编辑这些字段。要编辑信号信息，请切换到 `manually specified signals`。

如果您已选择手动指定信号，请在此表中创建信号。您创建的每个信号都具有以下值：

**名称**
:   为信号指定描述性名称。模型中的 Simulink 模块会显示此名称。默认值为 `Signal [row number]`。

**起始位**
:   指定数据的起始位。起始位是从消息数据起始位置开始计数的最低有效位。起始位必须是 0 到 63 范围内的整数。

**长度 (bits)**
:   指定信号在消息中占用的位数。长度必须是 1 到 64 范围内的整数。

**字节顺序**
:   选择以下任一选项：

    - `LE`：字节顺序采用小端格式 (Intel®)。在这种格式中，从最低有效位到最高有效位对位进行计数。例如，如果以小端格式打包一个 byte 的数据，且起始位为 20，则数据位表类似于此图。

      **从最低有效位到最高地址计数的小端字节顺序**
    - `BE`：字节顺序采用大端格式 (Motorola®)。在这种格式中，从最低有效位到最高有效位对位进行计数。例如，如果以大端格式打包一个 byte 的数据，且起始位为 20，则数据位表类似于此图。

      **从最低有效位到最低地址计数的大端字节顺序**

**数据类型**
:   指定信号如何解释已分配位中的数据。可从以下选项中选择：

    - `signed` (默认)
    - `unsigned`
    - `single`
    - `double`

**多路复用类型**
:   指定模块如何在每个时间步长将信号打包到 CAN 消息中：

    - `Standard`：在每个时间步长打包该信号。
    - `Multiplexor`：打包 `Multiplexor` 信号（即模式信号）。每条消息只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果运行时 `Multiplexor` 信号（模式信号）的值与此信号配置的 **多路复用值** 匹配，则打包该信号。

    例如，一条消息具有以下类型和值的信号。

    | 信号名称 | 多路复用类型 | 多路复用值 |
    | --- | --- | --- |
    | Signal-A | Standard | 不适用 |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | 不适用 |

    在此示例中：

    - 模块在每个时间步长都打包 Signal-A（Standard 信号）和 Signal-D（Multiplexor 信号）。
    - 如果 Signal-D 的值在特定时间步长为 1，则模块会在该时间步长将 Signal-B 与 Signal-A 和 Signal-D 一起打包。
    - 如果 Signal-D 的值在特定时间步长为 0，则模块会在该时间步长将 Signal-C 与 Signal-A 和 Signal-D 一起打包。
    - 如果 Signal-D 的值既不是 1 也不是 0，则模块不会在该时间步长打包任何一个 Multiplexed 信号。

**多路复用值**
:   仅当您将 **多路复用类型** 选择为 `Multiplexed` 时，此选项才可用。模块要打包 `Multiplexed` 信号，您提供的值必须与运行时 `Multiplexor` 信号的值匹配。**多路复用值** 必须是正整数或零。

**Factor**
:   指定要应用的 **Factor** 值，以将物理值（信号值）转换为打包在消息中的原始值。有关详细信息，请参阅 **数据输入方式** 参数的转换公式。

**Offset**
:   指定要应用的 **Offset** 值，以将物理值（信号值）转换为打包在消息中的原始值。有关详细信息，请参阅 **数据输入方式** 参数的转换公式。

**Min**、**Max**
:   定义信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库中读取。对于 **manually specified signals**，您可以指定信号的最小物理值和最大物理值。默认情况下，这些设置不会对超出设置范围的信号值进行限幅。

#### 编程用法

|  |
| --- |
| **模块参数：** `SignalInfo` |
| **类型：** `string` | `character vector` |

## 所属库

Vehicle Network Toolbox / CAN Communication C2000 Microcontroller Blockset / Target Communication Embedded Coder / Embedded Targets / Host Communication Simulink Real-Time / CAN / CAN MSG blocks

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中推出**

### R2025a: 更新了参数：ARXML 支持

为支持 ARXML 文件定义，更新了以下参数：

- **数据输入方式** — 新增选项 `ARXML specified signals`。

- **CANdb 文件** — 在模块封装中已重命名为 **数据库文件**。其编程名称仍为 `CANdbFile`。

### R2024b: 新参数：从输入端口指定 CAN 标识符

**从输入端口指定 CAN 标识符** 参数添加了输入端口 **CAN Msg ID**，以支持动态指定 CAN 标识符。

## 描述

将各个信号打包到 CAN 消息中

CAN Pack 模块在仿真期间按指定时间间隔将信号数据加载到 CAN 消息中。

要使用此模块，您必须具有 Simulink® 软件的许可证。

CAN Pack 模块支持：

- Simulink 加速模式和快速加速模式。您可以加快 Simulink 模型的执行速度。有关详细信息，请参阅加速。
- 模型引用。您的模型可以将其他 Simulink 模型作为模块化组件包含在内。有关详细信息，请参阅模型引用。

**提示**

- 此模块可用于对长度不超过 8 bytes 的 J1939 参数组中的信号进行编码。但是，处理 J1939 消息时，最好使用 J1939 Communication 模块库中的模块，而不是此模块。
