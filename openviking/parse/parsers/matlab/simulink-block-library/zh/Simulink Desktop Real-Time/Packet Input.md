---
type: simulink-block
title: 'Packet Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'packetinput'
documentation_source_path: 'ref/packetinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Packet Input

## 端口

### 输出

### **Output Data** — 从通信通道接收的数据向量

从通信通道接收的数据值，以未格式化的二进制数据形式表示。对于 CAN 或 Virtual CAN 设备，此端口支持：

- `CAN_MESSAGE` 数据类型
- `CAN_MESSAGE_BUS` 数据类型
- CAN FD 模式下的 `CAN_FD_MESSAGE_BUS` 数据类型

### **Data Ready** — 数据就绪端口（可选） `1` | `0`

如果模块有新数据可用，此端口输出 `1`，否则输出 `0`。

#### 依赖关系

当您选中 **Show “Data Ready” port** 时，此端口可见。

### **Data Error** — 数据错误端口（可选） `1` | `0`

如果发生数据错误，此端口输出 `1`，否则输出 `0`。

#### 依赖关系

当您选中 **Show “Data Error” port** 时，此端口可见。

### **Timestamp** — 数据包时间戳端口（可选） double

此端口显示 CAN 消息数据包的时间戳。

#### 依赖关系

当您选中 **Show packet timestamp port** 时，此端口可见。

### **Missed Ticks** — 丢失节拍计数（可选） double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖关系

当您选中 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`

## 参数

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示支持的板卡制造商列表。当您选择制造商时，软件显示该制造商可用的板卡列表。当您选择板卡时，软件将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡驱动支持的更多信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖关系

当您在已注册板卡列表中选择一个板卡时，**Delete current board** 和 **Board setup** 按钮变为可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框以设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请点击 **Delete current board**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **Sample time** — 模块的采样时间 `0.1`（默认） | double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将模型与实时时钟同步。

如果您使用的是定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认）| 整数

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。即使模型错过了一些节拍，也允许模型赶上。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowMissedTicks` |

### **Yield CPU when waiting** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时授予其他程序更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`YieldWhenWaiting` |

### **Packet identifier** — 数据包的标识符 `1`（默认）| 向量

输入要处理的数据包的 ID。如果您的协议没有数据包 ID，则此参数被禁用。

#### 编程使用

|  |
| --- |
| **模块参数**：`PacketID` |

### **Extended identifier** — 数据包的扩展标识符（仅限 CAN 板） `'off'`（默认）| `'on'`

如果 **Packet identifier** 是扩展标识符，则选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`PacketID` |

### **Input packet size** — 每个输入数据包包含的字节数 `32`（默认）| 整数

输入每个输入数据包中预期的字节数。此数字必须与 **Block output data types** 中的类型规范所需的字节数匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`PacketSize` |

### **Block output data types** — 数据包中数据的输出类型和分组 `'4*double'`（默认）| 字符向量 | 字符向量元胞数组

一个或多个字符向量，用于指定每个数据包中的数据如何为应用程序输入进行类型化和分组。Packet Input 模块为 **Block output data types** 中的每个字符向量都有一个对应的输出端口。更改字符向量的数量会更改输出端口的数量。

每个字符向量的格式为 [`n*`]`datatype`。字符向量描述的数据具有由 `datatype` 指定的类型和由 `n` 指定的宽度。如果未指定 `n`，则宽度为 `1`。例如，`'double'` 表示一个 `double` 值，`'4*int8'` 表示四个 `int8` 值的向量。您也可以键入 `'CAN_MESSAGE'` 来指定单个 `CAN_MESSAGE` 值。

通过提供此类字符向量的元胞数组，您可以将输入数据包转换为所需的类型，并打包成向量。例如，指定 `{'int16','int16','double'}` 会创建三个端口。第一个和第二个各输出一个 `int16` 值，第三个输出一个 `double`。指定 `{'2*int16','double'}` 会创建两个端口：一个包含两个 `int16` 值的向量，以及一个标量 `double`。

该模块将超出范围的值强制为该数据类型的最大值。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataTypes` |

### **Input packet field byte order** — 从设备获取的数据包的字节序 `Little Endian`（默认）| `Big Endian`

从列表中选择：

- `Little Endian`（默认）— 以小端格式发送多字节值。
- `Big Endian` — 以大端格式发送多字节值。

#### 编程用法

|  |
| --- |
| **模块参数：** `ByteOrder` |

### **显示 “Data Ready” 端口** — 添加端口 `Data Ready`，当数据可用时发出 `1` 信号 `'off'`（默认）| `'on'`

当您选中此复选框时，模块将显示输出端口 `Data Ready`。当模块有新数据可用时，此端口发出 `1` 信号，否则发出 `0`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowReady` |

### **显示 “Data Error” 端口** — 添加端口 `Data Error`，如果发生错误则发出 `1` 信号 `'off'`（默认）| `'on'`

当您选中此复选框时，模块将显示输出端口 `Data Error`。当发生数据错误时，此端口发出 `1` 信号，否则发出 `0`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowError` |

### **显示数据包时间戳端口** — 添加端口 `Timestamp`，输出 CAN 消息时间戳 `'off'`（默认）| `'on'`

当您选中此复选框时，模块将显示输出端口 `Timestamp`。此端口显示 CAN 消息数据包的时间戳。如果您的协议没有数据包时间戳，模块将忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowTimestamp` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

### R2024b：更新带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink® Desktop Real-Time™ 模块端口将显示标签。

### R2024a：对 Packet I/O 模块应用 UDP 多播支持

要对 Packet Input 模块应用 UDP 多播支持，请安装 UDP 设备并通过 **Standard Devices UDP Protocol** 对话框启用多播操作。

### R2020b：CAN 和 CAN FD 消息总线数据类型

对于 CAN 或 Virtual CAN 设备，Packet Input 模块和 Packet Output 模块在 CAN 模式下提供对 `CAN_MESSAGE_BUS` 数据类型的支持，在 CAN FD 模式下提供对 `CAN_FD_MESSAGE_BUS` 数据类型的支持。

### R2019b：Packet Input 和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备

Packet Input 模块和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备。

### R2019a：RS-232 串行端口驱动支持 macOS

Packet Input 模块、Packet Output 模块、Stream Input 模块和 Stream Output 模块的串行端口驱动支持 macOS 系统。在之前的版本中，这些模块的串行端口驱动仅支持 Windows® 系统。

## 描述

从通信通道读取二进制数据或 CAN 消息

Packet Input 模块从端口或文件读取未格式化的二进制数据。将 Packet Input 模块添加到模型后，双击该模块以设置其参数。

驱动必须是以下之一：

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**
- **Kvaser** > **CAN Device**
- **PEAK-System** > **CAN Device**
- **Vector** > **CAN Device**
- **MathWorks** > **virtual CAN**（需要 Vehicle Network Toolbox™）

### UDP 协议设备配置

当您安装 UDP 设备时，使用 **Standard Devices UDP Protocol** 对话框配置以下配置参数：

- **Local UDP port address**，十进制格式
- **Remote host name or IP address**
- **Remote UDP port address**，十进制格式
- **Receive multicast messages** 启用或禁用

使用 Standard Device UDP Protocol 对话框配置 UDP 连接
