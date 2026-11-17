---
type: simulink-block
title: 'UDP Receive'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'udpreceive'
documentation_source_path: 'udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口
```yaml
ports:
- name: Data
  summary: 接收的数据 向量 | 矩阵 | 数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Status
  summary: 新数据可用 0（默认） | 1
  direction: output
  data_types: Boolean
```

### 输出

### **Data** — 接收的数据 向量 | 矩阵 | 数组

模块从远程地址接收的数据，以向量、矩阵或数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Status** — 新数据可用 `0`（默认） | `1`

新数据可用状态，以逻辑值 `1`（`true`）或 `0`（`false`）返回。如果此端口返回 `1`，则表示有新数据可供读取。

#### 依赖关系

要启用此端口，请取消选中 **Enable blocking mode** 参数。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Local address
  summary: 本地主机名或 IP 地址 0.0.0.0（默认） | 本地主机名或 IP 地址
  group: ''
  block_parameter: LocalAddress
  type: 字符向量、字符串
- name: Local port
  summary: 用于绑定的本地主机端口 -1（默认） | 本地主机端口
  group: ''
  block_parameter: LocalPort
  type: 字符向量、字符串
- name: Enable local port sharing
  summary: 允许其他 UDP 套接字绑定到同一本地端口 off（默认） | on
  group: ''
  block_parameter: EnablePortSharing
  type: 字符向量、字符串
  values: '''on'' | ''off'''
- name: Remote address
  summary: 远程主机名或地址 localhost（默认） | 远程主机名或 IP 地址
  group: ''
  block_parameter: Host
  type: 字符向量、字符串
- name: Remote port
  summary: 远程主机端口 9090（默认） | 远程主机端口
  group: ''
  block_parameter: Port
  type: 字符向量、字符串
  values: 1 到 65,535
- name: Verify address and port connectivity
  summary: 远程机器连接验证按钮
  group: ''
- name: Output latest data
  summary: 接收最新数据 off（默认） | on
  group: ''
  block_parameter: GetLatestData
  type: 字符向量、字符串
  values: '''on'' | ''off'''
- name: Data size
  summary: 读取的值的数量 [1, 1]（默认）| 数值数组
  group: ''
  block_parameter: DataSize
  type: 字符向量、字符串
  values: 向量
  default: '''[ 1, 1 ]'''
- name: Source Data type
  summary: 输出数据类型 uint8（默认）| single | double | int8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | ASCII
  group: ''
  block_parameter: DataType
  type: 字符向量、字符串
  values: '''single'' | ''double'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' |
    ''uint64'' | ''ASCII'''
  default: '''uint8'''
- name: ASCII format string
  summary: 字符串数据的格式 %f（默认）| 数值转换说明符
  group: ''
  block_parameter: ASCIIFormatting
  type: 字符向量、字符串
  values: '''%d'' | ''%i'' | ''%ld'' | ''%li'' | ''%u'' | %o'' | ''%x'' | ''%lu'' | ''%lo'' | ''%lx'' | ''%f'' | ''%e'' |
    ''%g'''
  default: '''%f'''
- name: Terminator
  summary: 终止符 LF（默认）| CR | CR/LF | LF/CR | Custom terminator
  group: ''
  block_parameter: Terminator
  type: 字符向量、字符串
  values: '''CR'' | ''LF'' | ''CR/LF'' | ''LF/CR'' | ''Custom terminator'''
  default: '''LF'''
- name: Custom Terminator
  summary: 自定义终止符数值数组 | 从 0 到 255 的整数
  group: ''
  block_parameter: CustomTerminator
  type: 字符向量、字符串
  values: 整数数组
  default: '''10'''
- name: Byte order
  summary: 字节的顺序 big-endian（默认） | little-endian
  group: ''
  block_parameter: ByteOrder
  type: 字符向量、字符串
  values: '''little-endian'' | ''big-endian'''
  default: '''big-endian'''
- name: Enable blocking mode
  summary: 仿真在接收数据时等待 on（默认） | off
  group: ''
  block_parameter: EnableBlockingMode
  type: 字符向量、字符串
  values: '''on'' | ''off'''
  default: '''on'''
- name: Timeout
  summary: 完成操作所允许的时间 10（默认） | 正标量
  group: ''
  block_parameter: Timeout
  type: 字符向量、字符串
  values: 正标量
  default: '''10'''
- name: 模块采样时间
  summary: 采样时间 0.01（默认）| 正数值
  group: ''
  block_parameter: SampleTime
  type: 字符向量、字符串
  values: 正数值
```

### **Local address** — 本地主机名或 IP 地址 0.0.0.0（默认） | 本地主机名或 IP 地址

本地主机的主机名、点分十进制 IP 地址或 Web 服务器。此模块同时支持 IPV4 和 IPV6 地址格式。

#### 编程使用

|  |
| --- |
| **模块参数：** `LocalAddress` |
| **类型：** 字符向量、字符串 |

### **Local port** — 用于绑定的本地主机端口 -1（默认） | 本地主机端口

用于 UDP 绑定的本地主机端口，指定为 1 到 65,535 之间的数字。如果未指定值，则会自动分配一个值。

您也可以将此参数的值指定为现有的工作区变量。

#### 编程使用

|  |
| --- |
| **模块参数：** `LocalPort` |
| **类型：** 字符向量、字符串 |

### **Enable local port sharing** — 允许其他 UDP 套接字绑定到同一本地端口 `off`（默认） | `on`

启用本地端口共享的参数。如果您希望允许其他 UDP 套接字绑定到同一本地端口，请选中此参数。

UDP 端口可被其他应用程序共享，以允许多个应用程序监听该端口上的 UDP 数据报。您可以将此模块绑定到特定的 **Local port**，并在另一个应用程序中将 UDP 套接字绑定到相同的本地端口号，这样两者都可以接收 UDP 广播数据。

#### 编程使用

|  |
| --- |
| **模块参数：** `EnablePortSharing` |
| **类型：** 字符向量、字符串 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

### **Remote address** — 远程主机名或地址 `localhost`（默认） | 远程主机名或 IP 地址

您要从中接收数据的远程机器或服务器的 IP 地址或名称。

#### 编程使用

|  |
| --- |
| **模块参数：** `Host` |
| **类型：** 字符向量、字符串 |

### **Remote port** — 远程主机端口 `9090`（默认） | 远程主机端口

您要连接的机器上的远程端口，指定为 1 到 65,535 之间的数字。

您也可以将此参数的值指定为现有的工作区变量。

#### 编程使用

|  |
| --- |
| **模块参数：** `Port` |
| **类型：** 字符向量、字符串 |
| **值：** 1 到 65,535 |
| **默认：** `'9090'` |

### **Verify address and port connectivity** — 远程机器连接验证按钮

点击此按钮以检查到指定远程地址和端口的连接是否有效。

### **Output latest data** — 接收最新数据 `off`（默认） | `on`

此参数允许您接收最新数据。如果您希望接收最新数据，请选中此参数。

数据通常以 FIFO 方式接收。启用后，将接收最新的可用数据包，而不是使用 FIFO 方法。

#### 编程使用

|  |
| --- |
| **模块参数：** `GetLatestData` |
| **类型：** 字符向量、字符串 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

#### 依赖关系

如果将 **Source Data type** 设置为 `ASCII`，则此参数不可用。

### **Data size** — 读取的值的数量 `[1, 1]`（默认）| 数值数组

输出数据大小，或每个仿真时间步要读取的值的数量。
此参数指定为标量或向量。
数据不包括终止符值。

您也可以将此参数的值指定为现有的工作区变量。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataSize` |
| **类型**：字符向量、字符串 |
| **值**：向量 |
| **默认值**：`'[ 1, 1 ]'` |

### **Source Data type** — 输出数据类型 `uint8`（默认）| `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `ASCII`

模块从远程地址接收的数据类型，指定为 MATLAB® 数据类型。

此数据类型必须与远程地址处数据的数据类型匹配。您不能使用此参数更改远程地址处数据的数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataType` |
| **类型**：字符向量、字符串 |
| **值**：`'single'` | `'double'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'ASCII'` |
| **默认值**：`'uint8'` |

### **ASCII format string** — 字符串数据的格式 `%f`（默认）| 数值转换说明符

接收到的字符串数据的格式。您可以使用以下转换说明符或它们的组合。

| 数值字段类型 | 转换说明符 | 详细信息 |
| --- | --- | --- |
| 有符号整数 | `%d` | 十进制 |
| `%i` | 数据中的值决定进制：  - 默认为十进制。 - 如果起始数字为 `0x` 或   `0X`，则值为十六进制（16 进制）。 - 如果起始数字为 `0`，则值为八进制   （8 进制）。 |
| `%ld` 或 `%li` | 64 位值，10、8 或 16 进制 |
| 无符号整数 | `%u` | 十进制 |
| `%o` | 8 进制（八进制） |
| `%x` | 16 进制（十六进制） |
| `%lu`、`%lo`、`%lx` | 64 位值，10、8 或 16 进制 |
| 浮点数 | `%f` | 浮点字段可以包含以下任意内容（不区分大小写）：`Inf`、`-Inf`、`NaN` 或 `-NaN`。 |
| `%e` |
| `%g` |

#### 编程使用

|  |
| --- |
| **模块参数**：`ASCIIFormatting` |
| **类型**：字符向量、字符串 |
| **值**：`'%d'` | `'%i'` | `'%ld'` | `'%li'` | `'%u'` | `%o'` | `'%x'` | `'%lu'` | `'%lo'` | `'%lx'` | `'%f'` | `'%e'` | `'%g'` |
| **默认值**：`'%f'` |

#### 依赖关系

要启用此参数，请将 **Source Data type** 设置为 `ASCII`。

### **Terminator** — 终止符 `LF`（默认）| `CR` | `CR/LF` | `LF/CR` | `Custom terminator`

指示数据块结束的终止符。仿真将终止符之前出现的任何数据视为新数据块。终止符数据不会发送到输出端口。此终止符必须与您从远程机器读取的数据中的终止符匹配。

如果选择 `Custom Terminator`，则可以指定自己的终止符值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Terminator` |
| **类型**：字符向量、字符串 |
| **值**：`'CR'` | `'LF'` | `'CR/LF'` | `'LF/CR'` | `'Custom terminator'` |
| **默认值**：`'LF'` |

#### 依赖关系

要启用此参数，请将 **Source Data type** 设置为 `ASCII`。

### **Custom Terminator** — 自定义终止符数值数组 | 从 0 到 255 的整数

自定义终止符，用于指示数据块的结束。仿真将终止符之前出现的任何数据视为新的数据块。终止符数据不会发送到输出端口。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | ASCII 字符示例 | MATLAB 命令 | 参数值 |
| --- | --- | --- | --- |
| 控制字符（转义序列） | `"LF"` (`"\n"`) | `uint8(sprintf('\n'))` | `[10]` |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"End"` | `uint8('End')` | `[69 110 100]` |

您也可以使用 ASCII 字符的十六进制表示来指定此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `CustomTerminator` |
| **类型：** 字符向量、字符串 |
| **值：** 整数数组 |
| **默认值：** `'10'` |

#### 依赖关系

要启用此参数，请将 **Terminator** 设置为 `Custom terminator`。

### **Byte order** — 字节的顺序 `big-endian`（默认） | `little-endian`

字节排列为更大数值时的顺序。如果字节顺序为 `little-endian`，则第一个字节位于接收到的 UDP 数据包中的第一个内存地址。如果字节顺序为 `big-endian`，则最后一个字节位于接收到的 UDP 数据包中的第一个内存地址。

在接收数据之前，请将字节顺序配置为与远程机器匹配的适当值。有关仪器存储字节顺序的信息，请参阅仪器文档。

#### 编程用法

|  |
| --- |
| **模块参数：** `ByteOrder` |
| **类型：** 字符向量、字符串 |
| **值：** `'little-endian'` | `'big-endian'` |
| **默认值：** `'big-endian'` |

### **Enable blocking mode** — 仿真在接收数据时等待 `on`（默认） | `off`

此参数使仿真在模块接收数据时等待。当新数据可用时，仿真从下一个时间步继续。如果您不希望读取操作导致仿真等待，请取消选择此参数。

如果启用阻塞模式，仿真将等待请求的数据变为可用。在每个时间步，模型等待的时间最多为 **Timeout** 参数指定的时间量。如果在此时间内未收到数据，模块输出值 `0`。

如果未启用阻塞模式，仿真将持续运行，并且模块有两个输出端口：**Status** 和 **Data**。**Data** 端口在每个时间步包含请求的数据集。**Status** 端口包含 0 或 1，取决于在给定时间步是否接收到新数据。

有关详细信息，请参阅 Receive and Send Blocks 中的 Enable Blocking Mode。

#### 编程用法

|  |
| --- |
| **模块参数：** `EnableBlockingMode` |
| **类型：** 字符向量、字符串 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **Timeout** — 完成操作所允许的时间 10（默认） | 正标量

模型在每个仿真时间步等待数据的时间量，以秒为单位。此值相对于真实世界时间或“挂钟”时间。

您也可以将此参数的值指定为现有的工作区变量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Timeout` |
| **类型：** 字符向量、字符串 |
| **值：** 正标量 |
| **默认值：** `'10'` |

#### 依赖关系

要启用此参数，请将 **Enable blocking mode** 设置为 `on`。

### **模块采样时间** — 采样时间 0.01（默认）| 正数值

模块在仿真期间的采样时间。这是模块在仿真期间执行的速率。有关详细信息，请参阅硬件接口模型中的时序。

您也可以将此参数的值指定为现有的工作区变量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量、字符串 |
| **值：** 正数值 |
| **默认：** `'0.01'` |
## 所属库

Instrument Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

## 描述

通过 UDP 网络从指定的远程机器接收数据

UDP Receive 模块使用 UDP 协议配置并打开到指定远程地址的接口。配置和初始化在模型执行开始时进行一次。该模块在模型运行期间以阻塞模式或非阻塞模式获取数据。

该模块没有输入端口。根据您选择阻塞模式还是非阻塞模式，它有一个或两个输出端口。如果您选择阻塞模式，该模块有一个输出端口 **Data**，对应于它接收的数据。如果您不选择阻塞模式，该模块有两个输出端口，**Data** 和 **Status**。

UDP Receive 模块非阻塞模式和阻塞模式

该模块使用先进先出（FIFO）缓冲区来接收数据。在每个时间步，**Data** 端口从缓冲区返回请求的值。在非阻塞模式下，**Status** 端口指示该模块是否已接收到新数据。如果 **Status** 端口显示 `1`，则新数据可用；如果 **Status** 端口显示 `0`，则没有新数据可用。

**注意**

您必须同时拥有 Instrument Control Toolbox™ 和 Simulink® 的许可证才能使用此模块。

### 其他支持的功能

- UDP Receive 模块支持使用 Simulink 加速器和快速加速器模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅加速（Simulink）。
- UDP Receive 模块支持使用模型引用。此功能允许您的模型将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
