---
type: simulink-block
title: 'Packet Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'packetoutput'
documentation_source_path: 'ref/packetoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Packet Output

## 端口

### 输入

### **Input Data** — 要写入通信通道的 vector 数据

作为未格式化的二进制数据发送到通信通道的数据值。对于 CAN 或 Virtual CAN 设备，此端口支持：

- `CAN_MESSAGE` datatype
- `CAN_MESSAGE_BUS` datatype
- `CAN_FD_MESSAGE_BUS` datatype in CAN FD 模式

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **Data Ready** — 数据就绪端口（可选） `1` | `0`

如果模块准备好接受新数据，此端口发出 `1` 信号，否则发出 `0` 信号。

#### 依赖关系

当你选择 **显示 “Data Ready” 端口** 时，此端口可见。

### **Data Error** — 数据错误端口（可选） `1` | `0`

如果发生数据错误，此端口发出 `1` 信号，否则发出 `0` 信号。

#### 依赖关系

当你选择 **显示 “Data Error” 端口** 时，此端口可见。

### **Missed Ticks** — 丢失 tick 计数（可选） double

在 **Connected IO** 模式下，返回模型落后于实时内核的 timer ticks 数。当模型落后超过 **最大丢失 ticks** 时，软件会报告错误并停止仿真。

#### 依赖关系

当你选择 **显示 “Missed Ticks” 端口** 时，此端口可见。

**数据类型：** `double`

## 参数

### **安装新板** — 注册板 `< no board selected >` (default)

当你点击 **安装新板** 时，软件显示支持的板的制造商列表。当你选择某个制造商时，软件显示该制造商提供的板列表。当你选择某个板时，软件会将该板添加到已注册板列表，并使该板成为当前板。

默认情况下，已注册板列表中的初始选择为 `< no board selected >`。

有关 I/O 板的驱动程序支持的详细信息，请参阅 Hardware Support from Simulink Desktop Real-Time。

#### 依赖关系

当你在已注册板列表中选择一个板时，**删除当前板** 和 **板设置** 按钮可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **删除当前板** — 删除当前板（按钮）

要删除当前板，请点击此按钮。已注册板列表的初始选择将变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板列表中选择一个板。

当你删除当前板时，**删除当前板** 和 **板设置** 按钮将不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **板设置** — 设置板（按钮）

要设置板，请点击此按钮。

将打开一个特定于板的对话框来设置板。有关详细信息，请参阅板制造商文档。

#### 依赖关系

要激活此参数，请在已注册板列表中选择一个板。

要停用此参数，请点击 **删除当前板**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1` (default) | double

输入一个以 seconds 为单位的值，表示你希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将模型与实时时钟同步。

如果你使用的是固定步长求解器，请输入你在 **固定步长** 配置参数中输入的值，或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大丢失 ticks** — 模型可以落后内核的 timer ticks 数 `10` (default) | integer

在 **Connected IO** 模式下，输入模型可以落后于实时内核的 timer ticks 数。当模型落后此数量或更少的 timer ticks 时，软件假定该滞后是临时的。它允许模型赶上，即使模型丢失了一些 ticks。当模型落后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将丢失 ticks 数发送到端口 `Missed Ticks` `'off'` (default) | `'on'`

在 **Connected IO** 模式下，选中此复选框以将丢失 ticks 数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 当内核等待硬件时让出 CPU `'off'` (default) | `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时向其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **数据包标识符** — 数据包的标识符 `1` (default) | vector

输入要处理的数据包的 ID。如果你的协议没有数据包 ID，则此参数被禁用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PacketID` |

### **扩展标识符** — 数据包的扩展标识符（仅 CAN 板） `'off'` (default) | `'on'`

如果 **数据包标识符** 是扩展标识符，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PacketID` |

### **输出数据包大小** — 每个输入数据包包含的 bytes 数 `32` (default) | integer

输入每个输入数据包期望的 bytes 数。此数字必须与 **输出数据包数据类型** 中的类型规范所需的 bytes 数匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PacketSize` |

### **输出数据包字段数据类型** — 发送到设备的数据包中数据的输出类型和分组 `'4*double'` (default) | character vector | cell array of character vector

一个或多个 character vector，用于指定应用程序提供的数据如何格式化为数据包。Packet Output 模块具有与 **输出数据包字段数据类型** 中每个 character vector 对应的输入端口。更改 character vector 的数量会更改端口的数量。

每个 character vector 的格式为
[`n*`]`datatype`。
该 character vector 描述的数据具有由 `datatype` 指定的类型和由 `n` 指定的宽度。如果未指定 `n`，则宽度为 `1`。例如，`'double'` 表示一个 `double` 值，`'4*int8'` 表示四个 `int8` 值的 vector。你还可以键入 `'CAN_MESSAGE'` 来指定单个 `CAN_MESSAGE` 值。

输入到 Packet Output 模块每个端口的信号可以是该数据类型的 scalar 或 vector。每个端口的 character vector 指定其信号输出到设备时要使用的类型。如果某个端口的 character vector 与该端口输入信号的类型匹配，则信号值会原样出现在输出数据包中。

你还可以在输出时执行类型转换。例如，假设输入是四元素 `int16` vector，character vector 为 `'4*int8'`。这四个整数在写入数据包之前会转换为 `int8`。结果数据在输出数据包中占用 4 bytes。

模块会将超出范围的值强制转换为该数据类型的最大值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataTypes` |

### **输出数据包字段字节顺序** — 发送到设备的数据包的字节顺序 `Little Endian` (default) | `Big Endian`

从列表中选择：

- `Little Endian` (default)
  — 以 little-endian 格式接收多字节值。
- `Big Endian` — 以 big-endian 格式接收多字节值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ByteOrder` |

### **显示 “Data Ready” 端口** — 添加端口 `Data Ready`，该端口在模块可以接受新数据时发出 `1` 信号 `'off'` (default) | `'on'`

当你选中此复选框时，模块会显示输出端口 `Data Ready`。此输出端口在模块准备好接受新数据时发出 `1` 信号，否则发出 `0` 信号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowReady` |

### **显示 “Data Error” 端口** — 添加端口 `Data Error`，如果发生错误则发出 `1` 信号 `'off'` (default) | `'on'`

当你选中此复选框时，模块会显示输出端口 `Data Error`。此端口在发生数据错误时发出 `1` 信号，否则发出 `0` 信号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowError` |

### **初始值** — 仿真开始时发送的数据 vector

可选。输入一个 vector，其元素数与所有端口的输入信号宽度之和相同。仿真开始时，在仿真期间发送的其他数据之前发送指定的数据。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialValue` |

### **最终值** — 仿真结束时发送的数据 vector

可选。输入一个 vector，其元素数与所有端口的输入信号宽度之和相同。仿真结束时，在仿真期间发送的其他数据之后发送指定的数据。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FinalValue` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2007b 中引入**

### R2024b：更新为具有端口名称的模块

在 R2024b 中，当你启用可选端口（例如 **显示 "Missed Ticks" 端口**）时，这些 Simulink® Desktop Real-Time™ 模块端口会显示标签。

### R2020b：CAN 和 CAN FD 消息总线数据类型

对于 CAN 或 Virtual CAN 设备，Packet Input 模块和 Packet Output 模块在 CAN 模式下提供对 `CAN_MESSAGE_BUS` 数据类型的支持，并在 CAN FD 模式下提供对 `CAN_FD_MESSAGE_BUS` 数据类型的支持。

### R2019b：Packet Input 和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备

Packet Input 模块和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备。

### R2019a：RS-232 串行端口驱动程序支持 macOS

Packet Input 模块、Packet Output 模块、Stream Input 模块和 Stream Output 模块的串行端口驱动程序支持 macOS 系统。在以前的版本中，这些模块的串行端口驱动程序仅支持 Windows® 系统。

## 描述

将二进制数据或 CAN 消息写入通信通道

Packet Output 模块连接到端口、文件或 CAN 设备，并将未格式化的二进制数据写入其中。将 Packet Output 模块添加到模型后，双击该模块以设置其参数。

驱动程序必须是以下之一：

- **标准设备** > **文件**
- **标准设备** > **串行端口**
- **标准设备** > **TCP 协议**
- **标准设备** > **UDP 协议**
- **Kvaser** > **CAN 设备**
- **PEAK-System** > **CAN 设备**
- **Vector** > **CAN 设备**
- **MathWorks** > **virtual CAN** (requires Vehicle Network Toolbox™)

安装 UDP 设备时，请在标准设备 UDP 协议对话框中以十进制格式输入端口地址。

任何串行输出端口都可以发送采样率高达 500 Hz 的数据。要为某些输出串行端口启用高达 10 kHz 的更快的采样率，请点击 **安装新板**，选择 **标准设备** > **串行端口**，然后选择 **直接端口访问**。

该模块并非对所有类型的串行输出硬件都支持此选项。
