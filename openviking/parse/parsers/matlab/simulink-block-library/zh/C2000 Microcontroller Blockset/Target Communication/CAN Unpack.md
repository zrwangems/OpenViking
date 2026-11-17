---
type: simulink-block
title: 'CAN Unpack'
family: 'embedded-targets'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Embedded Targets / Host Communication'
documentation_page: 'canunpack'
documentation_source_path: '../ecoder/ref/canunpack.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Unpack

## 端口

### 输入

### **CAN Msg** — CAN 报文输入 `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

此模块有一个输入端口 **CAN Msg**。模块接收指定的输入 CAN 报文，并将其信号数据解包到单独的输出中。

该模块支持以下信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持 fixed-point 数据类型。
### 输出

### **Data** — CAN 信号输出 single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | boolean

默认情况下，该模块有一个输出端口。输出端口的数量是动态的，取决于指定要模块输出的信号数量。例如，如果报文包含四个信号，则模块可以有四个输出端口。

对于手动指定或由数据库指定的信号，CAN 信号的默认输出数据类型为 double。要指定其他类型，请使用 Signal Specification 模块。这样，模块便可支持以下输出信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持 fixed-point 类型。

通过在参数的 **输出端口** 窗格中选择相应选项，可以添加其他输出端口。有关详细信息，请参阅参数 `Output identifier`、`Output timestamp`、`Output error`、`Output remote`、`Output length` 和 `Output status`。

## 参数

### **数据输出为** — 选择数据信号 `raw data`（默认值） | `manually specify signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`：以 uint8 向量数组形式输出数据。如果选择此选项，则只需指定报文字段。其他信号参数字段不可用。此选项仅在模块上打开一个输出端口。

  转换公式为：

  ```
  physical_value = raw_value * Factor + Offset
  ```

  其中，`raw_value` 是解包后的信号值，`physical_value` 是缩放后的信号值。
- `manually specified signals`：可以指定数据信号。如果选择此选项，请使用 `Signals` 表手动创建信号报文。模块上的输出端口数量取决于指定的信号数量。例如，如果指定四个信号，则模块具有四个输出端口。
- `CANdb specified signals`：可以指定包含数据信号的 CAN 数据库文件。如果选择此选项，请选择一个 CANdb 文件。模块上的输出端口数量取决于 CANdb 文件中指定的信号数量。例如，如果 CANdb 文件中选择的报文有四个信号，则模块具有四个输出端口。
- `ARXML specified signals`：允许指定用于信号定义的 ARXML 文件。这会禁用某些远程选项。从 ARXML 文件读取数据后，可以切换到 `manually specified signals`，以进一步修改该表。

  有关详细信息，请参阅 Simulink 中 CAN 的 ARXML 文件支持 (Vehicle Network Toolbox)。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** `string` | `character vector` |
| **值：** `'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` | `'ARXML specified signals'` |
| **默认值：** `'raw data'` |

### **数据库文件** — ARXML 或 CAN 数据库文件 character vector

当将 **数据输出为** 参数指定为 `CANdb specified signals` 或 `ARXML specified signals` 时，此选项可用。单击 **浏览** 以查找系统上的数据库文件。数据库文件中指定的报文和信号定义会填充对话框的 **报文** 部分。数据库文件中指定的信号会填充 **信号** 表。包含非字母数字字符（例如等号、与号等）的文件名不是有效的数据库文件名。可以在数据库名称中使用句点。使用前，请重命名包含非字母数字字符的数据库文件。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `CANdbFile` |
| **类型：** `string` | `character vector` |

### **报文列表** — CAN 报文列表 array of character vectors

当为 **数据输入为** 字段指定数据库，并在 **数据库文件** 字段中指定数据库文件时，此选项可用。可以选择要查看的报文。随后，**信号** 表会显示所选报文的详细信息。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `MsgList` |
| **类型：** `string` | `character vector` |

### **名称** — CAN 报文名称 `CAN Msg`（默认值） | character vector

为 CAN 报文指定名称。默认值为 `CAN Msg`。如果选择输出原始数据或手动指定信号，则此选项可用。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `MsgName` |
| **类型：** `string` | `character vector` |

### **标识符类型** — CAN 标识符类型 `Standard (11-bit identifier)`（默认值） | `Extended (29-bit identifier)`

指定 CAN 报文标识符是 `Standard` 类型还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11-bit 标识符，扩展标识符是 29-bit 标识符。如果选择输出原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**标识符类型** 会从数据库继承类型。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `MsgIDType` |
| **类型：** `string` | `character vector` |
| **值：** `'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认值：** `'Standard (11-bit identifier)'` |

### **CAN 标识符** — CAN 报文标识符 `0`（默认值） | `0` 至 `536870911`

指定 CAN 报文 ID。对于标准标识符，此数字必须是 0 到 2047 之间的整数；对于扩展标识符，此数字必须是 0 到 536870911 之间的整数。如果指定 `-1`，模块将解包与为该报文指定的长度相匹配的报文。还可以使用 `hex2dec` 函数指定十六进制值。如果选择输出原始数据或手动指定信号，则此选项可用。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `MsgIdentifier` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 至 `'536870911'` |

### **长度 (bytes)** — CAN 报文长度 `8`（默认值） | `0` 至 `8`

指定 CAN 报文的长度，范围为 0 到 8 bytes。如果输出数据使用数据库指定的信号，则报文长度由数据库文件定义。否则，此字段默认为 `8`。如果选择输出原始数据或手动指定信号，则此选项可用。

注意：当接收到的帧的长度与掩码或网络描述文件中指定的值不同时，该帧将被丢弃。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `MsgLength` |
| **类型：** `string` | `character vector` |
| **值：** `'0'` 至 `'8'` |
| **默认值：** `'8'` |

### **添加信号** — 添加 CAN 信号

向信号表中添加一个信号。

#### 以编程方式使用

无

### **删除信号** — 删除 CAN 信号

从信号表中删除所选信号。

#### 以编程方式使用

无

### **信号** — 信号表 table

如果选择手动指定信号或使用数据库文件定义信号，则会显示此表。

如果使用数据库文件，文件中的数据将填充此表，并且无法编辑这些字段。要编辑信号信息，请切换到 `manually specified signals`。

如果已选择手动指定信号，请在此表中手动创建信号。创建的每个信号都具有以下值：

**名称**
:   为信号指定描述性名称。模型中的 Simulink 模块会显示此名称。默认值为 `Signal [row number]`。

**起始位**
:   指定数据的起始位。起始位是从报文开始处计数的最低有效位。起始位必须是 0 到 63 之间的整数。

**长度 (bits)**
:   指定信号在报文中占用的 bits 数。长度必须是 1 到 64 之间的整数。

**字节顺序**
:   选择以下任一选项：

    - `LE`：字节顺序采用小端格式 (Intel®)。在这种格式中，从最低有效位到最高有效位进行计数。例如，如果以小端格式打包一个 byte 的数据，且起始位为 20，则数据位表如下图所示。

      **从最低有效位到最高地址计数的小端字节顺序**
    - `BE`：字节顺序采用大端格式 (Motorola®)。在这种格式中，从最低有效位到最高有效位进行计数。例如，如果以大端格式打包一个 byte 的数据，且起始位为 20，则数据位表如下图所示。

      **从最低有效位到最低地址计数的大端字节顺序**

**数据类型**
:   指定信号如何解释所分配 bits 中的数据。可选择：

    - `signed`（默认值）
    - `unsigned`
    - `single`
    - `double`

**多路复用类型**
:   指定模块在每个时间步如何从 CAN 报文中解包信号：

    - `Standard`：在每个时间步解包信号。
    - `Multiplexor`：解包 `Multiplexor` 信号或模式信号。每条报文只能指定一个 `Multiplexor` 信号。
    - `Multiplexed`：如果运行时 `Multiplexor` 信号（模式信号）的值与此信号的已配置 **多路复用值** 相匹配，则解包该信号。

    例如，一条报文包含具有以下值的四个信号。

    | 信号名称 | 多路复用类型 | 多路复用值 |
    | --- | --- | --- |
    | Signal-A | Standard | 不适用 |
    | Signal-B | Multiplexed | 1 |
    | Signal-C | Multiplexed | 0 |
    | Signal-D | Multiplexor | 不适用 |

    在此示例中：

    - 模块在每个时间步解包 Signal-A（Standard 信号）和 Signal-D（Multiplexor 信号）。
    - 如果在某个时间步 Signal-D 的值为 1，则模块在该时间步解包 Signal-B，同时解包 Signal-A 和 Signal-D。
    - 如果在某个时间步 Signal-D 的值为 0，则模块在该时间步解包 Signal-C，同时解包 Signal-A 和 Signal-D。
    - 如果 Signal-D 的值既不是 1 也不是 0，则模块在该时间步不会解包任何一个 Multiplexed 信号。

**多路复用值**
:   仅当将 **多路复用类型** 选择为 `Multiplexed` 时，此选项才可用。要使模块解包 `Multiplexed` 信号，提供的值必须与运行时 `Multiplexor` 信号的值相匹配。**多路复用值** 必须是正整数或零。

**系数**
:   指定所应用的 **系数** 值，用于将解包后的原始值转换为物理值（信号值）。有关详细信息，请参阅 **数据输入为** 参数的转换公式。

**偏移量**
:   指定所应用的 **偏移量** 值，用于将物理值（信号值）转换为解包后的原始值。有关详细信息，请参阅 **数据输入为** 参数的转换公式。

**Min**、**Max**
:   定义原始信号值的范围。默认设置分别为 `-Inf`（负无穷大）和 `Inf`。对于数据库指定的信号，这些设置从数据库中读取。对于 **manually specified signals**，可以指定信号的最小物理值和最大物理值。默认情况下，这些设置不会裁剪超出其范围的信号值。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `SignalInfo` |
| **类型：** `string` | `character vector` |

### **输出标识符** — 添加 CAN ID 输出端口 `off`（默认值）

选择此选项可输出 CAN 报文标识符。此端口的数据类型为 `uint32`。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `IDPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出时间戳** — 添加 Timestamp 输出端口 `off`（默认值） | `on`

选择此选项可输出报文时间戳。此值指示报文的接收时间，表示为自模型仿真开始以来经过的时间，单位为 seconds。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `double`。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `TimestampPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出错误** — 添加 Error 输出端口 `off`（默认值） | `on`

选择此选项可输出报文错误状态。此选项会向模块添加一个新的输出端口。此端口上的输出值为 `1` 时，表示传入报文是错误帧。输出值为 `0` 时，表示没有错误。此端口的数据类型为 `uint8`。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `ErrorPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出远程帧** — 添加 Remote 输出端口 `off`（默认值） | `on`

选择此选项可输出报文的远程帧状态。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `RemotePort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出长度** — 添加 Length 输出端口 `off`（默认值） | `on`

选择此选项可输出报文长度，单位为 bytes。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `LengthPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出状态** — 添加 Status 输出端口 `off`（默认值） | `on`

选择此选项可输出报文接收状态。如果模块接收到新报文，则状态为 `1`；否则为 `0`。此选项会向模块添加一个新的输出端口。此端口的数据类型为 `uint8`。

#### 以编程方式使用

|  |
| --- |
| **模块参数：** `StatusPort` |
| **类型：** `string` | `character vector` |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

## 所属库

Vehicle Network Toolbox / CAN Communication C2000 Microcontroller Blockset / Target Communication Embedded Coder / Embedded Targets / Host Communication Simulink Real-Time / CAN / CAN MSG blocks

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2009a 中引入**

### R2025a：更新的参数：ARXML 支持

为支持 ARXML 文件定义，更新了以下参数：

- **数据输出为** — 新增选项 `ARXML specified signals`。

- **CANdb 文件** — 在模块掩码中已重命名为 **数据库文件**。其编程名称仍为 `CANdbFile`。

## 描述

从 CAN 报文中解包各个信号

CAN Unpack 模块在每个时间步使用指定的输出参数，将 CAN 报文解包为信号数据。数据作为单独的信号输出。

要使用此模块，您还需要 Simulink® 软件的许可证。

CAN Unpack 模块支持：

- 使用 Simulink 加速模式和快速加速模式。利用此功能，您可以加快 Simulink 模型的执行速度。有关详细信息，请参阅 Acceleration。
- 使用模型引用。利用此功能，您的模型可以将其他 Simulink 模型作为模块化组件包含进来。有关详细信息，请参阅 Model References。

**提示**

- 要处理通过通道传来的每条报文，请勿在函数触发子系统中使用 CAN Unpack 模块。有关详细信息，请参阅 Speedgoat® 文档。
- 此模块可用于解码长度最大为 8 bytes 的 J1939 参数组中的信号。但是，要处理 J1939 报文，最好使用 J1939 Communication 模块库中的模块，而不是此模块。
