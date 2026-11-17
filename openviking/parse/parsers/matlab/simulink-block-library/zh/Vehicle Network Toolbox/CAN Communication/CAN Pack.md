---
type: simulink-block
title: 'CAN Pack'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN Communication'
documentation_page: 'canpack'
documentation_source_path: 'ug/canpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Pack

## 端口

### 输入

### **Data** — CAN 消息信号输入 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

默认情况下，CAN Pack 模块有一个输入端口。模块输入的数量是动态的，取决于您为模块指定的信号数量。例如，如果您的消息有四个信号，则该模块可以有四个输入端口。

该模块支持以下输入信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点数据类型。

**提示**

即使您有一个没有信号的零长度消息，您仍然必须向输入端口提供虚拟数据，以便定义采样时间。在这种情况下，数据值本身会被忽略。

### **CAN Msg ID** — CAN 消息标识符 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

CAN Msg ID 输入端口允许您动态指定 CAN 消息标识符。仅当选中 **Specify CAN identifier from input port** 参数时，此端口才存在。有关详细信息，请参阅 Dynamically Change CAN IDs by CAN Pack Block Input Ports。
### 输出

### **CAN Msg** — CAN 消息输出 `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

该模块有一个输出端口，即 CAN Msg。CAN Pack 模块获取指定的输入信号并将其打包为 CAN 消息。输出数据类型由 **Output as bus** 参数设置决定。

## 参数

### **Data input as** — 选择您的数据信号 `raw data`（默认）| `manually specified signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：将数据作为 uint8 向量数组输入。如果选择此选项，您只需指定消息字段。所有其他信号参数字段均不可用。此选项仅在您的模块上打开一个输入端口。

  转换公式为：

  ```
  raw_value = (physical_value - Offset) / Factor
  ```

  其中 `physical_value` 是信号的原始值，`raw_value` 是打包后的信号值。
- `manually specified signals`：允许您指定数据信号定义。如果选择此选项，请使用 **Signals** 表创建信号。模块输入的数量取决于您指定的信号数量。
- `CANdb specified signals`：允许您指定包含消息和信号定义的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块输入的数量取决于 CANdb 文件中为所选消息指定的信号数量。
- `ARXML specified signals`：允许您指定用于信号定义的 ARXML 文件。这会禁用某些远程选项。从 ARXML 文件读取数据后，您可以切换到 `manually specified signals` 以进一步修改该表。

  有关详细信息，请参阅 ARXML File Support for CAN in Simulink。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataFormat` |
| **类型**：`string` | `character vector` |
| **值**：`'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` | `'ARXML specified signals'` |
| **默认值**：`'raw data'` |

### **Database file** — ARXML 或 CAN 数据库文件 character vector

如果您将 **Data is input as** 参数指定为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。点击 **Browse** 以在您的系统上查找数据库文件。数据库文件中指定的消息列表将填充对话框的 **Message** 部分。数据库文件还会为所选消息填充 **Signals** 表。

包含非字母数字字符（如等号、& 符号等）的文件名不是有效的数据库文件名。您可以在数据库名称中使用句点。在使用数据库文件之前，请使用非字母数字字符重命名它们。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **消息列表** — CAN 消息列表字符向量数组

如果在 **数据输入方式** 字段中指定数据库，并在 **数据库文件** 字段中指定数据库文件，则此选项可用。选择要显示信号详细信息的消息，详细信息将显示在 **信号** 表中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **名称** — CAN 消息名称 `CAN Msg`（默认）| 字符向量

为您的 CAN 消息指定名称。默认值为 `CAN Msg`。如果您选择输入原始数据或手动指定信号，则此选项可用。如果您选择使用数据库文件中的信号，则此选项不可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **标识符类型** — CAN 标识符类型 `Standard (11-bit identifier)`（默认）| `Extended (29-bit identifier)`

指定您的 CAN 消息标识符是 `Standard` 还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11 位标识符，扩展标识符是 29 位标识符。如果您选择输入原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**标识符类型** 从数据库继承类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认：** `'Standard (11-bit identifier)'` |

### **CAN 标识符** — CAN 消息 ID `0`（默认）| `0` 到 `536870911`

指定您的 CAN 消息 ID。对于标准标识符，此数字必须是 0 到 2047 之间的正整数；对于扩展标识符，必须是 0 到 536870911 之间的正整数。您也可以使用 `hex2dec` 函数指定十六进制值。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'536870911'` |

### **从输入端口指定 CAN 标识符** — CAN 消息 ID 值 `off`（默认）| `on`

选中后，您可以通过模块上的输入端口指定值来动态控制 CAN 标识符（CAN ID）。选择此选项会添加一个名为 CAN Msg ID 的输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CANIDInput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **长度（字节）** — CAN 消息长度 `8`（默认）| `0` 到 `8`

指定您的 CAN 消息长度，范围为 0 到 8 字节。如果您使用数据库指定的信号作为数据输入，则数据库文件定义消息的长度。如果不是，此字段默认为 `8`。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 到 `'8'` |
| **默认：** `'8'` |

### **远程帧** — CAN 消息作为远程帧 `off`（默认）| `on`

将 CAN 消息指定为远程帧。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Remote` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **输出为总线** — CAN 消息作为总线 `off`（默认）| `on`

选择此选项使模块将 CAN 消息输出为 Simulink 总线信号。有关 Simulink 总线对象的更多信息，请参阅 Composite Interfaces (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BusOutput` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Add signal** — 添加 CAN 信号

向信号表中添加一个新信号。

#### 程序化使用

无

### **Delete signal** — 删除 CAN 信号

从信号表中移除所选信号。

#### 程序化使用

无

### **Signals** — Signals 表 表

如果您选择手动指定信号或使用数据库文件定义信号，则会显示此表。

如果您使用数据库文件，文件中的数据会填充此表，您无法编辑这些字段。要编辑信号信息，请切换到手动指定信号。

如果您已选择手动指定信号，请在此表中创建信号。您创建的每个信号都具有以下值：

**Name**
:   为您的信号指定一个描述性名称。模型中的 Simulink 模块会显示此名称。默认值为
    `Signal [row number]`。

**Start bit**
:   指定数据的起始位。起始位是从消息数据起始位置开始计数的最低有效位。起始位必须是
    0 到 63 之间的整数。

**Length (bits)**
:   指定信号在消息中占用的位数。长度必须是
    1 到 64 之间的整数。

**Byte order**
:   选择以下任一选项：

    - `LE`：字节顺序为小端格式
      (Intel®)。在此格式中，您从最低有效位计数到最高有效位。例如，如果您以小端格式打包一个字节的数据，起始位为
      20，则数据位表类似于下图。

      **从最低有效位到最高地址计数的小端字节顺序**
    - `BE`：字节顺序为大端格式
      (Motorola®)。在此格式中，您从最低有效位计数到最高有效位。例如，如果您以大端格式打包一个字节的数据，起始位为
      20，则数据位表类似于下图。

      **从最低有效位到最低地址计数的大端字节顺序**

    有关详细信息，请参阅 CAN Frame Structure, Byte Order, and Bit Counting。

**数据类型**
:   指定信号如何解释所分配位中的数据。选择：

    - `signed`（默认）
    - `unsigned`
    - `single`
    - `double`

**Multiplex type**
:   指定模块在每个时间步如何将信号打包到 CAN 消息中：

    - `Standard`：
      该信号在每个时间步都会被打包。
    - `Multiplexor`：打包
      `Multiplexor` 信号，即模式信号。
      每条消息只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果运行时
      `Multiplexor` 信号（模式信号）的值与该信号配置的 **Multiplex value** 匹配，则打包该信号。

    例如，一条消息具有以下信号，其类型和值如下。

    | Signal Name | Multiplex Type | Multiplex Value |
    | --- | --- | --- |
    | Signal-A | Standard | Not applicable |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | Not applicable |

    在此示例中：

    - 模块在每个时间步都会打包 Signal-A（Standard 信号）和 Signal-D（Multiplexor
      信号）。
    - 如果在某个特定时间步 Signal-D 的值为 1，则模块在该时间步会将 Signal-B 与 Signal-A 和 Signal-D 一起打包。
    - 如果在某个特定时间步 Signal-D 的值为 0，则模块在该时间步会将 Signal-C 与 Signal-A 和 Signal-D 一起打包。
    - 如果 Signal-D 的值不是 1 或 0，则模块在该时间步不会打包任何一个
      Multiplexed 信号。

**Multiplex value**
:   仅当您将 **Multiplex
    type** 选择为 `Multiplexed` 时，此选项才可用。您提供的值必须在运行时与
    `Multiplexor` 信号值匹配，模块才会打包该 `Multiplexed` 信号。
    **Multiplex value** 必须为正整数或零。

**Factor**
:   指定要应用的 **Factor** 值，以将物理值（信号值）转换为打包在报文中的原始值。有关详细信息，请参阅 **Data input as** 参数转换公式。

**Offset**
:   指定要应用的 **Offset** 值，以将物理值（信号值）转换为打包在报文中的原始值。有关详细信息，请参阅 **Data input as** 参数转换公式。

**Min**、**Max**
:   定义信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库中读取。对于**手动指定的信号**，您可以指定信号的最小和最大物理值。默认情况下，这些设置不会裁剪超出设置的信号值。

#### 编程使用

|  |
| --- |
| **模块参数**：`SignalInfo` |
| **类型**：`string` | `character vector` |

## 所属库

Vehicle Network Toolbox / CAN Communication C2000 Microcontroller Blockset / Target Communication Embedded Coder / Embedded Targets / Host Communication Simulink Real-Time / CAN / CAN MSG blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

### R2025a: Updated parameters: ARXML support

为支持 ARXML 文件定义，以下参数已更新：

- **Data input as** — 新增选项 `ARXML specified
  signals`。

- **CANdb file** — 在模块掩码中已重命名为 **Database
  file**。其程序化名称仍为
  `CANdbFile`。

### R2024b：新参数：从输入端口指定 CAN 标识符

参数 **Specify CAN identifier from input port** 新增了一个
输入端口 **CAN Msg ID**，以支持动态指定 CAN 标识符。

## 描述

将各个信号打包为 CAN 报文

CAN Pack 模块在仿真期间按指定间隔将信号数据加载到 CAN 报文中。

要使用此模块，您必须拥有 Simulink® 软件的许可证。

CAN Pack 模块支持：

- Simulink 加速和快速加速模式。您可以加速 Simulink 模型的执行。有关详细信息，请参阅 Acceleration (Simulink)。
- 模型引用。您的模型可以将其他 Simulink 模型作为模块化组件包含在内。有关详细信息，请参阅 Model References (Simulink)。

**Tip**

- 此模块可用于编码最多 8 字节的 J1939 参数组信号。但是，要处理 J1939 报文，最好使用 J1939 Communication 模块库中的模块，而不是此模块。请参阅
  J1939 Communication。
