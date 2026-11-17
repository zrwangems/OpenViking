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
```yaml
ports:
- name: Input Data
  summary: 要写入通信通道的数据 vector
  direction: input
  data_types: single | double | int8 | uint8 | int16 | uint16 | int32 | uint32
- name: Data Ready
  summary: 数据就绪端口（可选） 1 | 0
  direction: output
- name: Data Error
  summary: 数据错误端口（可选） 1 | 0
  direction: output
- name: Missed Ticks
  summary: 错过的节拍计数（可选） double
  direction: output
  data_types: double
```

### 输入

### **Input Data** — 要写入通信通道的数据 vector

作为无格式二进制数据发送到通信通道的数据值。对于 CAN 或 Virtual CAN 设备，此端口支持：

- `CAN_MESSAGE` 数据类型
- `CAN_MESSAGE_BUS` 数据类型
- CAN FD 模式下的 `CAN_FD_MESSAGE_BUS` 数据类型

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **Data Ready** — 数据就绪端口（可选） `1` | `0`

如果模块已准备好接受新数据，此端口发出 `1` 信号，否则发出 `0`。

#### 依赖关系

当您选择 **Show “Data Ready” port** 时，此端口可见。

### **Data Error** — 数据错误端口（可选） `1` | `0`

如果发生数据错误，此端口发出 `1` 信号，否则发出 `0`。

#### 依赖关系

当您选择 **Show “Data Error” port** 时，此端口可见。

### **Missed Ticks** — 错过的节拍计数（可选） double

在 **Connected IO** 模式下，返回您的模型滞后于实时内核的定时器节拍数。当模型滞后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖关系

当您选择 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Install new board
  summary: 注册板卡 < no board selected >（默认）
  group: ''
  block_parameter: DrvName
- name: Delete current board
  summary: 删除当前板卡（按钮）
  group: ''
  block_parameter: DrvName
- name: Board setup
  summary: 设置板卡（按钮）
  group: ''
  block_parameter: DrvOptions
- name: Sample time
  summary: 模块的采样时间 0.1（默认） | double
  group: ''
  block_parameter: SampleTime
- name: Maximum missed ticks
  summary: 模型可以落后于内核的定时器节拍数 10（默认）| 整数
  group: ''
  block_parameter: MaxMissedTicks
- name: Show “Missed Ticks” port
  summary: 将错过的节拍数发送到端口 Missed Ticks 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowMissedTicks
- name: Yield CPU when waiting
  summary: 在内核等待硬件时让出 CPU 'off'（默认）| 'on'
  group: ''
  block_parameter: YieldWhenWaiting
- name: Packet identifier
  summary: 数据包的标识符 1（默认）| 向量
  group: ''
  block_parameter: PacketID
- name: Extended identifier
  summary: 数据包的扩展标识符（仅限 CAN 板） 'off'（默认）| 'on'
  group: ''
  block_parameter: PacketID
- name: Output packet size
  summary: 每个输入数据包包含的字节数 32（默认）| 整数
  group: ''
  block_parameter: PacketSize
- name: Output packet field data types
  summary: 发送到设备的数据包中数据的输出类型和分组 '4*double'（默认）| 字符向量 | 字符向量元胞数组
  group: ''
  block_parameter: DataTypes
- name: Output packet field byte order
  summary: 发送到设备的报文字节序 Little Endian（默认）| Big Endian
  group: ''
  block_parameter: ByteOrder
- name: Show “Data Ready” port
  summary: 添加端口 Data Ready，当模块可以接受新数据时发出 1 信号 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowReady
- name: Show “Data Error” port
  summary: 添加端口 Data Error，如果发生错误则发出 1 信号 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowError
- name: Initial value
  summary: 仿真开始时发送的数据 向量
  group: ''
  block_parameter: InitialValue
- name: Final value
  summary: 仿真结束时发送的数据 向量
  group: ''
  block_parameter: FinalValue
```

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示支持的板卡制造商列表。当您选择某个制造商时，软件显示该制造商可用的板卡列表。当您选择某个板卡时，软件将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡驱动支持的更多信息，请参阅 Simulink Desktop Real-Time 的 Hardware Support。

#### 依赖关系

当您在已注册板卡列表中选择某个板卡时，**Delete current board** 和 **Board setup** 按钮变为可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择某个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮将不再可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框以设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择某个板卡。

要停用此参数，请点击 **Delete current board**。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvAddress` |
| **模块参数**：`DrvOptions` |

### **Sample time** — 模块的采样时间 `0.1`（默认） | double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值，或该值的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认）| 整数

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。即使模型错过了一些节拍，也允许模型追赶。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **Yield CPU when waiting** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时授予其他程序更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **Packet identifier** — 数据包的标识符 `1`（默认）| 向量

输入要处理的数据包的 ID。如果您的协议没有数据包 ID，则此参数被禁用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PacketID` |

### **Extended identifier** — 数据包的扩展标识符（仅限 CAN 板） `'off'`（默认）| `'on'`

如果 **Packet identifier** 是扩展标识符，则选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PacketID` |

### **Output packet size** — 每个输入数据包包含的字节数 `32`（默认）| 整数

输入每个输入数据包中预期的字节数。此数字必须与 **Output packet data types** 中的类型规范所需的字节数匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `PacketSize` |

### **Output packet field data types** — 发送到设备的数据包中数据的输出类型和分组 `'4*double'`（默认）| 字符向量 | 字符向量元胞数组

一个或多个字符向量，用于指定应用程序提供的数据如何格式化为数据包。Packet Output 模块为 **Output packet field data types** 中的每个字符向量都有一个对应的输入端口。更改字符向量的数量会更改端口的数量。

每个字符向量的格式为 [`n*`]`datatype`。字符向量描述的数据具有由 `datatype` 指定的类型和由 `n` 指定的宽度。如果未指定 `n`，则宽度为 `1`。例如，`'double'` 表示一个 `double` 值，`'4*int8'` 表示四个 `int8` 值的向量。您也可以键入 `'CAN_MESSAGE'` 来指定单个 `CAN_MESSAGE` 值。

输入到 Packet Output 模块每个端口的信号可以是该数据类型的标量或向量。每个端口的字符向量指定其信号输出到设备时要使用的类型。如果某个端口的字符向量与该端口输入的信号类型匹配，则信号值将原样出现在输出数据包中。

您还可以对输出执行类型转换。例如，假设输入是一个四元素 `int16` 向量，字符向量为 `'4*int8'`。这四个整数在写入数据包之前被转换为 `int8`。结果数据在输出数据包中占用 4 个字节。

该模块将超出范围的值强制为该数据类型的最大值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataTypes` |

### **Output packet field byte order** — 发送到设备的报文字节序 `Little Endian`（默认）| `Big Endian`

从列表中选择：

- `Little Endian`（默认）
  — 以小端格式接收多字节值。
- `Big Endian` — 以大端格式接收多字节值。

#### 编程使用

|  |
| --- |
| **模块参数**：`ByteOrder` |

### **Show “Data Ready” port** — 添加端口 `Data Ready`，当模块可以接受新数据时发出 `1` 信号 `'off'`（默认）| `'on'`

当您选中此复选框时，模块将显示输出端口 `Data Ready`。当模块准备好接受新数据时，此输出端口发出 `1` 信号，否则发出 `0` 信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowReady` |

### **Show “Data Error” port** — 添加端口 `Data Error`，如果发生错误则发出 `1` 信号 `'off'`（默认）| `'on'`

当您选中此复选框时，模块将显示输出端口 `Data Error`。当发生数据错误时，此端口发出 `1` 信号，否则发出 `0` 信号。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowError` |

### **Initial value** — 仿真开始时发送的数据 向量

可选。输入一个向量，其元素数量等于所有端口上输入信号宽度之和。当仿真开始时，在仿真期间发送的其他数据之前发送指定的数据。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialValue` |

### **Final value** — 仿真结束时发送的数据 向量

可选。输入一个向量，其元素数量等于所有端口上输入信号宽度之和。当仿真结束时，在仿真期间发送的其他数据之后发送指定的数据。

#### 编程使用

|  |
| --- |
| **模块参数**：`FinalValue` |
## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

### R2024b：更新具有端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink® Desktop Real-Time™ 模块端口会带有标签显示。

### R2020b：CAN 和 CAN FD 消息总线数据类型

对于 CAN 或 Virtual CAN 设备，Packet Input 模块和 Packet Output 模块在 CAN 模式下提供对 `CAN_MESSAGE_BUS` 数据类型的支持，在 CAN FD 模式下提供对 `CAN_FD_MESSAGE_BUS` 数据类型的支持。

### R2019b：Packet Input 和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备

Packet Input 模块和 Packet Output 模块支持 PEAK-System 和 Kvaser CAN 设备。

### R2019a：RS-232 串行端口驱动程序支持 macOS

Packet Input 模块、Packet Output 模块、Stream Input 模块和 Stream Output 模块的串口驱动程序支持 macOS 系统。在之前的版本中，这些模块的串口驱动程序仅支持 Windows® 系统。

## 描述

将二进制数据或 CAN 报文写入通信通道

Packet Output 模块连接到端口、文件或 CAN 设备，并向其写入未格式化的二进制数据。将 Packet Output 模块添加到模型后，双击该模块以设置其参数。

驱动程序必须为以下之一：

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**
- **Kvaser** > **CAN Device**
- **PEAK-System** > **CAN Device**
- **Vector** > **CAN Device**
- **MathWorks** > **virtual CAN**（需要 Vehicle Network Toolbox™）

安装 UDP 设备时，请在 Standard Devices UDP Protocol 对话框中以十进制格式输入端口地址。

任何串行输出端口都可以发送采样率高达 500 Hz 的数据。要为某些输出串行端口启用高达 10 kHz 的更快采样率，请点击 **Install new board**，选择 **Standard Devices** > **Serial Port**，然后选择 **Direct port access**。

该模块并非对所有类型的串行输出硬件都支持此选项。
