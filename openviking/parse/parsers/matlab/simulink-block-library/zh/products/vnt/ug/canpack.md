---
type: simulink-block
title: 'CAN Pack'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN and CAN FD Communication / Communication in Simulink / CAN'
documentation_page: 'canpack'
documentation_source_path: 'ug/canpack.html'
language: zh-CN
chinese_source: official
---

# CAN Pack

## 端口

### 输入

### **Data** — CAN 报文信号输入 单精度值 | 双精度值 | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | 布尔值

CAN Pack 模块默认有一个输入端口。模块输入的数量是动态的，取决于您为模块指定的信号数量。例如，如果您的报文有四个信号，则该模块可以有四个输入端口。

该模块支持以下输入信号数据类型：single、double、int8、int16、int32、int64、uint8、uint16、uint32、uint64 和 boolean。该模块不支持定点数据类型。

**提示**

即使您有不包含信号的零长度报文，您仍必须向输入端口提供虚拟数据以便定义采样时间。在这种情况下，数据值本身会被忽略。

### **CAN Msg ID** — CAN 报文标识符 单精度值 | 双精度值 | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64

CAN Msg ID 输入端口允许您动态指定 CAN 报文标识符。仅当选择**从输入端口指定 CAN 标识符**参数时，此端口才存在。有关详细信息，请参阅通过 CAN Pack 模块输入端口动态更改 CAN ID。
### 输出

### **CAN Msg** — CAN 报文输出 `CAN_MESSAGE` | `CAN_MESSAGE_BUS`

该模块有一个输出端口 CAN Msg。CAN Pack 模块接受指定的输入信号并将其打包为一个 CAN 报文。输出数据类型由**作为总线输出**参数设置确定。

## 参数

### **数据输入为** — 选择您的数据信号： `raw data` (默认) | `manually specified signals` | `CANdb specified signals` | `ARXML specified signals`

- `raw data`:以 uint8 向量数组形式输入数据。如果选择此选项，则只需指定报文字段。所有其他信号参数字段都不可用。此选项仅在模块上打开一个输入端口。

  转换公式为：

  ```
  raw_value = (physical_value - Offset) / Factor
  ```

  其中 `physical_value` 是信号的原始值，`raw_value` 是打包的信号值。
- `manually specified signals`:允许您指定数据信号定义。如果选择此选项，请使用**信号**表创建信号。模块输入的数量取决于您指定的信号数量。
- `CANdb specified signals`:允许您指定包含报文和信号定义的 CAN 数据库文件。如果选择此选项，请选择 CANdb 文件。模块输入的数量取决于 CANdb 文件中为所选报文指定的信号数量。
- `ARXML specified signals`:允许您为信号定义指定 ARXML 文件。这将禁用一些远程选项。从 ARXML 文件中读取数据后，您可以切换到 `manually specified signals` 来进一步修改该表。

  有关详细信息，请参阅Simulink 中对 CAN 的 ARXML 文件支持。

#### 编程用法

|  |
| --- |
| **模块参数：**`DataFormat` |
| **类型：**`string` | `character vector` |
| **值：**`'raw data'` | `'manually specified signals'` | `'CANdb specified signals'` | `'ARXML specified signals'` |
| **默认值：**`'raw data'` |

### **数据库文件** — ARXML 或 CAN 数据库文件 字符向量

如果您将**数据输入为**参数指定为 `CANdb specified signals` 或 `ARXML specified signals`，则此选项可用。点击**浏览**以在您的系统上找到数据库文件。数据库文件中指定的报文列表将填充对话框的**报文**部分。数据库文件还会填充所选报文的**信号**表。

包含非字母数字字符（如等号、& 符号等）的文件名不是有效的数据库文件名。您可以在数据库名称中使用句点。在使用数据库文件之前，请重命名那些带有非字母数字字符的名称。

#### 编程用法

|  |
| --- |
| **模块参数：**`CANdbFile` |
| **类型：**`string` | `character vector` |

### **报文列表** — CAN 报文列表 字符向量数组

如果您在**数据输入为**字段中指定数据库，并在**数据库文件**字段中指定数据库文件，则此选项可用。选择要在**信号**表中显示信号详细信息的报文。

#### 编程用法

|  |
| --- |
| **模块参数：**`MsgList` |
| **类型：**`string` | `character vector` |

### **名称** — CAN 报文名称 `CAN Msg` (默认) | 字符向量

指定 CAN 报文的名称。默认值为 `CAN Msg`。如果您选择输入原始数据或手动指定信号，则此选项可用。如果您选择使用来自数据库文件的信号，则此选项不可用。

#### 编程用法

|  |
| --- |
| **模块参数：**`MsgName` |
| **类型：**`string` | `character vector` |

### **标识符类型** — CAN 标识符类型 `Standard (11-bit identifier)` (默认) | `Extended (29-bit identifier)`

指定 CAN 报文标识符是 `Standard` 还是 `Extended` 类型。默认值为 `Standard`。标准标识符是 11 位标识符，扩展标识符是 29 位标识符。如果您选择输入原始数据或手动指定信号，则此选项可用。对于数据库指定的信号，**标识符类型**从数据库继承类型。

#### 编程用法

|  |
| --- |
| **模块参数：**`MsgIDType` |
| **类型：**`string` | `character vector` |
| **值：**`'Standard (11-bit identifier)'` | `'Extended (29-bit identifier)'` |
| **默认值：**`'Standard (11-bit identifier)'` |

### **CAN 标识符** — CAN 报文 ID `0` (默认) | `0` 到 `536870911`

指定 CAN 报文 ID。对于标准标识符，此数字必须是 0 到 2047 之间的正整数，对于扩展标识符，此数字必须是 0 到 536870911 之间的正整数。您还可以使用 `hex2dec` 函数指定十六进制值。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程用法

|  |
| --- |
| **模块参数：**`MsgIdentifier` |
| **类型：**`string` | `character vector` |
| **值：**`'0'` 到 `'536870911'` |

### **从输入端口指定 CAN 标识符** — CAN 报文 ID 值 `off` (默认) | `on`

当选中时，可以通过模块上的输入端口指定值来动态控制 CAN 标识符 (CAN ID)。选择此选项会添加名为 CAN Msg ID 的输入端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`CANIDInput` |
| **类型：**`string` | `character vector` |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

### **长度(字节)** — CAN 报文长度 `8` (默认) | `0` 到 `8`

指定 CAN 报文的长度，范围为 0 到 8 个字节。如果您使用数据库指定的信号作为数据输入，数据库文件定义您的报文长度。如果不是，则该字段默认为 `8`。如果您选择输入原始数据或手动指定信号，则此选项可用。

#### 编程用法

|  |
| --- |
| **模块参数：**`MsgLength` |
| **类型：**`string` | `character vector` |
| **值：**`'0'` 到 `'8'` |
| **默认值：**`'8'` |

### **远程帧** — CAN 报文作为远程帧 `off` (默认) | `on`

将 CAN 报文指定为远程帧。

#### 编程用法

|  |
| --- |
| **模块参数：**`Remote` |
| **类型：**`string` | `character vector` |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

### **作为总线输出** — CAN 报文作为总线 `off` (默认) | `on`

选择此选项可使模块将 CAN 报文作为 Simulink 总线信号输出。有关 Simulink 总线对象的详细信息，请参阅合成接口 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：**`BusOutput` |
| **类型：**`string` | `character vector` |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

### **添加信号** — 添加 CAN 信号

向信号表中添加一个新信号。

#### 编程用法

无

### **删除信号** — 删除 CAN 信号

从信号表中删除所选信号。

#### 编程用法

无

### **信号** — 信号表 表

如果您选择手动指定信号或使用数据库文件定义信号，则会出现此表。

如果您使用的是数据库文件，则文件中的数据会填充此表，您不能编辑字段。要编辑信号信息，请切换到手动指定的信号。

如果您已选择手动指定信号，请在此表中创建信号。您创建的每个信号都具有以下值：

**名称**
:   为信号指定说明性名称。模型中的 Simulink 模块将显示此名称。默认值为 `Signal [row number]`。

**开始位**
:   指定数据的开始位。开始位是从报文数据的开头计数的最低有效位。开始位必须是 0 到 63 之间的整数。

**长度(位)**
:   指定信号在报文中占用的位数。长度必须是 1 到 64 之间的整数。

**字节顺序**
:   选择以下任一选项：

    - `LE`:其中字节顺序为 little-endian 格式 (Intel®)。在这种格式中，从最低有效位到最高有效位进行计数。例如，如果以 little-endian 格式打包数据的一个字节，并且开始位为 20，则数据位表类似于下图所示。

      **从最低有效位到最高地址计数的 Little-Endian 字节顺序**
    - `BE`:其中字节顺序为 big-endian 格式 (Motorola®)。在这种格式中，从最低有效位到最高有效位进行计数。例如，如果以 big-endian 格式打包数据的一个字节，并且开始位为 20，则数据位表类似于下图所示。

      **从最低有效位到最低地址计数的 Big-Endian 字节顺序**

    有关详细信息，请参阅 CAN 帧结构、字节顺序和位计数。

**数据类型**
:   指定信号如何解释分配的位中的数据。从下列各项中选择：

    - `signed`（默认值）
    - `unsigned`
    - `single`
    - `double`

**多路复用类型**
:   指定模块在每个时间步将信号打包到 CAN 报文中的方式：

    - `Standard`:在每个时间步打包信号。
    - **多路复用器**：打包**多路复用器**信号，即模式信号。对每条报文，只能指定一个**多路复用器**信号。
    - **多路复用**：如果在运行时**多路复用器**信号（模式信号）的值与为此信号配置的**多路复用值**匹配，则打包信号。

    例如，一条报文包含下列具有以下类型和值的信号。

    | 信号名称 | 多路复用类型 | 多路复用值 |
    | --- | --- | --- |
    | Signal-A | 标准 | 不适用 |
    | Signal-B | 多路复用 | 1 |
    | Signal-C | 多路复用 | 0 |
    | Signal-D | 多路复用器 | 不适用 |

    在此示例中：

    - 模块在每个时间步中打包 Signal-A（标准信号）和 Signal-D（多路复用器信号）。
    - 如果 Signal-D 的值在特定时间步为 1，则模块在该时间步中将 Signal-B 与 Signal-A 和 Signal-D 一起打包。
    - 如果 Signal-D 的值在特定时间步为 0，则模块在该时间步中将 Signal-C 与 Signal-A 和 Signal-D 一起打包。
    - 如果 Signal-D 的值不是 1 或 0，则模块不会在该时间步中打包任一复用信号。

**多路复用值**
:   仅当您选择的**多路复用类型** 为 `Multiplexed` 时，此选项才可用。您提供的值必须与运行时的**多路复用器**信号值匹配，模块才会打包**多路复用**信号。**多路复用值**必须是正整数或零。

**因子**
:   指定将物理值（信号值）转换为报文中打包的原始值时要应用的**因子**值。有关详细信息，请查看**数据输入为**参数转换公式。

**偏移量**
:   指定将物理值（信号值）转换为报文中打包的原始值时要应用的**偏移量**值。有关详细信息，请查看**数据输入为**参数转换公式。

**最小值**、**最大值**
:   定义一个信号值范围。默认设置分别为 `-Inf`（负无穷）和 `Inf`。对于数据库指定的信号，从数据库中读取这些设置。对于**手动指定的信号**，您可以指定信号的最小和最大物理值。默认情况下，这些设置不会对超过设置的信号值进行裁剪。

#### 编程用法

|  |
| --- |
| **模块参数：**`SignalInfo` |
| **类型：**`string` | `character vector` |

## 所属库

Vehicle Network Toolbox / CAN Communication C2000 Microcontroller Blockset / Target Communication Embedded Coder / Embedded Targets / Host Communication Simulink Real-Time / CAN / CAN MSG blocks

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2009a 中推出**

### R2025a: 已更新参数：ARXML 支持

为了支持 ARXML 文件定义，以下参数已更新：

- **数据输入为** - 有新选项 `ARXML specified signals`。

- **CANdb 文件** - 在模块封装中已重命名为**数据库文件**。其编程名称仍为 `CANdbFile`。

### R2024b: 新参数：从输入端口指定 CAN 标识符

参数**从输入端口指定 CAN 标识符**会添加一个输入端口 **CAN Msg ID** 以支持 CAN 标识符的动态指定。

## 描述

将单个信号打包到 CAN 报文中

CAN Pack 模块在仿真期间以指定的间隔将信号数据加载到一条 CAN 报文中。

要使用此模块，您必须有 Simulink® 软件的许可证。

CAN Pack 模块支持：

- Simulink 加速和快速加速模式。您可以加快 Simulink 模型的执行速度。有关详细信息，请参阅加速 (Simulink)。
- 模型引用。您的模型可以包含其他 Simulink 模型作为模块化组件。有关详细信息，请参阅模型引用 (Simulink)。

**提示**

- 此模块可用于编码最多 8 个字节的 J1939 参数组的信号。但是，要使用 J1939 报文，最好使用 J1939 Communication 模块库中的模块，而不是此模块。请参阅 J1939 通信。
