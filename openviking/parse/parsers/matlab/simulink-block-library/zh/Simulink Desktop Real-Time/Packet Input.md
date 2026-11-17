---
type: simulink-block
title: 'Packet Input'
family: 'simulink-desktop-real-time'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Simulink Desktop Real-Time'
documentation_page: 'packetinput'
documentation_source_path: 'ref/packetinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Packet Input

## 端口

### 输出

### **Output Data** — 从通信通道接收的数据向量

作为未格式化二进制数据从通信通道接收的数据值。对于 CAN 或 Virtual CAN 设备，此端口支持：

- `CAN_MESSAGE` 数据类型
- `CAN_MESSAGE_BUS` 数据类型
- CAN FD 模式下的 `CAN_FD_MESSAGE_BUS` 数据类型

### **Data Ready** — 数据就绪端口（可选） `1` | `0`

如果模块有新数据可用，此端口发出 `1` 信号，否则发出 `0`。

#### 依赖项

当您选择 **Show “Data Ready” port** 时，此端口可见。

### **Data Error** — 数据错误端口（可选） `1` | `0`

如果发生数据错误，此端口发出 `1` 信号，否则发出 `0`。

#### 依赖项

当您选择 **Show “Data Error” port** 时，此端口可见。

### **Timestamp** — 包时间戳端口（可选） double

此端口显示 CAN 消息包的时间戳。

#### 依赖项

当您选择 **Show packet timestamp port** 时，此端口可见。

### **Missed Ticks** — 丢失 tick 计数（可选） double

在 **Connected IO** 模式下，返回您的模型落后于实时内核的 timer ticks 数。当模型落后超过 **Maximum missed ticks** 时，软件会报告错误并停止仿真。

#### 依赖项

当您选择 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`

## 参数

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示受支持板卡的制造商列表。当您选择制造商时，软件显示该制造商提供的板卡列表。当您选择板卡时，软件将该板卡添加到已注册板卡列表，并使该板卡成为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡的驱动程序支持的详细信息，请参阅 Hardware Support from Simulink Desktop Real-Time。

#### 依赖项

当您在已注册板卡列表中选择一个板卡时，**Delete current board** 和 **Board setup** 按钮可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择变为 `< no board selected >`。

#### 依赖项

要激活此参数，请在已注册板卡列表中选择一个板卡。

删除当前板卡后，**Delete current board** 和 **Board setup** 按钮不再可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开板卡特定的对话框以设置板卡。有关详细信息，请参阅板卡制造商文档。

#### 依赖项

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请点击 **Delete current board**。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **Sample time** — 模块的采样时间 `0.1`（默认） | double

输入一个以 seconds 为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用固定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值，或该值的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

### **Maximum missed ticks** — 您的模型可以落后于内核的 timer ticks 数 `10`（默认） | integer

在 **Connected IO** 模式下，输入您的模型可以落后于实时内核的 timer ticks 数。当模型落后此数量或更少的 timer ticks 时，软件假定该滞后是暂时的。它允许模型追上，即使模型丢失一些 ticks。当模型落后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将丢失 ticks 数发送到端口 `Missed Ticks` `'off'`（默认） | `'on'`

在 **Connected IO** 模式下，选中此复选框以将丢失 ticks 数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **Yield CPU when waiting** — 当内核等待硬件时让出 CPU `'off'`（默认） | `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时授予其他程序更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **Packet identifier** — 包的标识符 `1`（默认） | vector

输入要处理的包的 ID。如果您的协议没有包 ID，则此参数被禁用。

#### 编程用法

|  |
| --- |
| **模块参数：** `PacketID` |

### **Extended identifier** — 包的扩展标识符（仅 CAN 板卡） `'off'`（默认） | `'on'`

如果 **Packet identifier** 是扩展标识符，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `PacketID` |

### **Input packet size** — 每个输入包包含的 bytes 数 `32`（默认） | integer

输入每个输入包中预期的 bytes 数。此数字必须与 **Block output data types** 中的类型规范所需的 bytes 数匹配。

#### 编程用法

|  |
| --- |
| **模块参数：** `PacketSize` |

### **Block output data types** — 来自包的数据的输出类型和分组 `'4*double'`（默认） | character vector | cell array of character vector

一个或多个 character vector，用于指定每个包中的数据如何类型化并分组以输入到应用程序。Packet Input 模块有一个输出端口，对应于 **Block output data types** 中的每个 character vector。更改 character vector 的数量会更改输出端口的数量。

每个 character vector 的格式为 [`n*`]`datatype`。该 character vector 描述的数据具有由 `datatype` 指定的类型和由 `n` 指定的宽度。如果未指定 `n`，则宽度为 `1`。例如，`'double'` 表示一个 `double` 值，`'4*int8'` 表示四个 `int8` 值的向量。您还可以键入 `'CAN_MESSAGE'` 来指定单个 `CAN_MESSAGE` 值。

通过提供此类 character vector 的 cell array，您可以将输入包转换为所需类型，并打包成向量。例如，指定 `{'int16','int16','double'}` 会创建三个端口。第一个和第二个各输出一个 `int16` 值，第三个输出一个 `double`。指定 `{'2*int16','double'}` 会创建两个端口：一个包含两个 `int16` 值的向量，以及一个标量 `double`。

该模块将超出范围的值强制转换为该数据类型的最大值。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataTypes` |

### **Input packet field byte order** — 从设备获取的包的字节顺序 `Little Endian`（默认） | `Big Endian`

从列表中选择：

- `Little Endian`（默认）— 以 little-endian 格式发送多字节值。
- `Big Endian` — 以 big-endian 格式发送多字节值。

#### 编程用法

|  |
| --- |
| **模块参数：** `ByteOrder` |

### **Show “Data Ready” port** — 添加端口 `Data Ready`，当数据可用时发出 `1` 信号 `'off'`（默认） | `'on'`

当您选中此复选框时，模块使输出端口 `Data Ready` 可见。当模块有新数据可用时，此端口发出 `1` 信号，否则发出 `0`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowReady` |

### **Show “Data Error” port** — 添加端口 `Data Error`，如果发生错误则发出 `1` 信号 `'off'`（默认） | `'on'`

当您选中此复选框时，模块使输出端口 `Data Error` 可见。当发生数据错误时，此端口发出 `1` 信号，否则发出 `0`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowError` |

### **Show packet timestamp port** — 添加端口 `Timestamp`，用于输出 CAN 消息时间戳 `'off'`（默认） | `'on'`

当您选中此复选框时，模块使输出端口 `Timestamp` 可见。此端口显示 CAN 消息包的时间戳。如果您的协议没有包时间戳，模块将忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowTimestamp` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

### R2024b：对具有端口名称的模块的更新

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink® Desktop Real-Time™ 模块端口会显示标签。

### R2024a：对 Packet I/O 模块应用 UDP 组播支持

要为 Packet Input 模块应用 UDP 组播支持，请安装 UDP 设备，并使用 **Standard Devices UDP Protocol** 对话框启用组播操作。

### R2020b：CAN 和 CAN FD 消息总线数据类型

对于 CAN 或 Virtual CAN 设备，Packet Input 模块和 Packet Output 模块在 CAN 模式下支持 `CAN_MESSAGE_BUS` 数据类型，在 CAN FD 模式下支持 `CAN_FD_MESSAGE_BUS` 数据类型。

### R2019b：Packet Input 和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备

Packet Input 模块和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备。

### R2019a：RS-232 串行端口驱动程序对 macOS 的支持

Packet Input 模块、Packet Output 模块、Stream Input 模块和 Stream Output 模块的串行端口驱动程序支持 macOS 系统。在以前的版本中，这些模块的串行端口驱动程序仅支持 Windows® 系统。

## 描述

从通信通道读取二进制数据或 CAN 消息

Packet Input 模块从端口或文件读取未格式化的二进制数据。将 Packet Input 模块添加到模型后，双击该模块以设置其参数。

驱动程序必须是以下之一：

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**
- **Kvaser** > **CAN Device**
- **PEAK-System** > **CAN Device**
- **Vector** > **CAN Device**
- **MathWorks** > **virtual CAN**（需要 Vehicle Network Toolbox™）

### UDP Protocol 设备的配置

安装 UDP 设备时，使用 **Standard Devices UDP Protocol** 对话框配置以下配置参数：

- **Local UDP port address**，采用十进制格式
- **Remote host name or IP address**
- **Remote UDP port address**，采用十进制格式
- **Receive multicast messages**，启用或禁用

使用 Standard Device UDP Protocol 对话框配置 UDP 连接
