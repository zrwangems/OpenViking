---
type: simulink-block
title: 'Stream Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'streamoutput'
documentation_source_path: 'ref/streamoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Output

## 端口
```yaml
ports:
- name: Input Data
  summary: 要写入通信通道的数据 数值向量 | 字符串
  direction: input
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

### **Input Data** — 要写入通信通道的数据 数值向量 | 字符串

作为 ASCII 数据发送到通信通道的数据值，
根据 **Format string** 进行编码。
### 输出

### **Data Ready** — 数据就绪端口（可选） `1` | `0`

如果模块已准备好
接受新数据，此端口输出 `1`，否则输出 `0`。

#### 依赖

当您选中 **Show “Data Ready” port** 时，
此端口可见。

### **Data Error** — 数据错误端口（可选） `1` | `0`

如果发生数据错误，此端口输出 `1`，
否则输出 `0`。

#### 依赖

当您选中 **Show “Data Error” port** 时，
此端口可见。

### **Missed Ticks** — 错过的节拍计数（可选） double

在 **Connected IO** 模式下，返回您的模型
落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed
ticks** 时，软件报告错误并停止仿真。

#### 依赖

当您选中 **Show “Missed Ticks”
port** 时，此端口可见。

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
  summary: 您的模型可以落后于内核的定时器节拍数 10（默认） | 整数
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
- name: Input port sizes
  summary: 指定端口的数量和宽度 1（默认）| 向量
  group: ''
  block_parameter: PortSizes
- name: Format string
  summary: 写入流的数据项的格式 '%g'（默认）| 字符向量
  group: ''
  block_parameter: FormatString
- name: Show “Data Ready” port
  summary: 添加端口 Data Ready，当模块可以接受新数据时发出信号 1 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowReady
- name: Show “Data Error” port
  summary: 添加端口 Data Error，如果发生错误则发出信号 1 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowError
- name: Initial string
  summary: 仿真开始时发送的数据 字符向量
  group: ''
  block_parameter: InitialValue
- name: Final string
  summary: 仿真结束时发送的数据 字符向量
  group: ''
  block_parameter: FinalValue
```

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件
显示支持的板卡制造商列表。当您选择
一个制造商时，软件显示该制造商
可用的板卡列表。当您选择一块板卡时，软件将该
板卡添加到已注册板卡列表中，并将该板卡设为当前
板卡。

默认情况下，已注册板卡列表中的初始选择为 `<
no board selected >`。

有关 I/O 板卡的驱动程序支持的更多信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖

当您在已注册板卡列表中选择一块板卡时，**Delete
current board** 和 **Board setup** 按钮
变为可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始
选择将变为 `<
no board selected >`。

#### 依赖

要激活此参数，请在已注册板卡
列表中选择一块板卡。

当您删除当前板卡后，**Delete current
board** 和 **Board setup** 按钮将
不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框来设置板卡。有关更多
信息，请参阅板卡制造商文档。

#### 依赖

要激活此参数，请在已注册板卡
列表中选择一块板卡。

要停用此参数，请点击 **Delete current
board**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **Sample time** — 模块的采样时间 `0.1`（默认） | double

输入一个以秒为单位的值，表示您
希望模块执行并与 I/O 硬件交互的频率。该
模块以此采样率将您的模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **Fixed
step size** 配置参数中输入的值或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **Maximum missed ticks** — 您的模型可以落后于内核的定时器节拍数 `10`（默认） | 整数

在 **Connected IO** 模式下，输入您的模型可以
落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器
节拍时，软件假定该滞后是暂时的。它允许模型追赶，即使
模型错过了一些节拍。当模型落后超过此数量时，软件
报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **Yield CPU when waiting** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时授予其他程序更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **Input port sizes** — 指定端口的数量和宽度 `1`（默认）| 向量

输入一个端口宽度，或端口宽度向量。元素的数量决定输入端口数量。每个端口具有由对应元素指定的宽度。例如，指定 `[3,1,2]` 表示该模块有三个输入端口：一个宽度为 `3` 的向量、一个标量和一个宽度为 `2` 的向量，总共六个元素。您只需指定宽度。

#### 编程用法

|  |
| --- |
| **模块参数：** `PortSizes` |

### **Format string** — 写入流的数据项的格式 `'%g'`（默认）| 字符向量

输入与 C 库 I/O 例程（如 `printf`）所用格式相同的规范。格式字符串描述要发送的数据。格式字符串中的格式说明符数量必须等于 **Input port sizes** 元素之和。如果格式说明符为 `%s` 或 `%c`（用于字符串），则创建的字符串类型输入端口仅接受字符串信号。此输入端口的 `Input port sizes` 参数值必须为 `"1"`，因为字符串只能是标量。

例如，假设 **Input port sizes** 为 `[3,1,2]`。则 **Format string** 为 `'%d %d %d %f %d %d'` 时输出 ASCII 表示：

- 来自第一个输入端口向量的三个整数
- 来自第二个输入端口标量的一个双精度值
- 来自第三个输入端口向量的两个整数

如果 **Format string** 中为某个值指定的数据类型与实际值的类型不同，则会发生类型转换。符合 **Format string** 的转换后数据以 ASCII 形式输出到设备。

#### 编程用法

|  |
| --- |
| **模块参数：** `FormatString` |

### **Show “Data Ready” port** — 添加端口 `Data Ready`，当模块可以接受新数据时发出信号 `1` `'off'`（默认）| `'on'`

选中此复选框时，模块将显示输出端口 `Data Ready`。此输出端口在模块准备好接受新数据时发出信号 `1`，否则发出信号 `0`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowReady` |

### **Show “Data Error” port** — 添加端口 `Data Error`，如果发生错误则发出信号 `1` `'off'`（默认）| `'on'`

选中此复选框时，模块将显示输出端口 `Data Error`。此端口在发生数据错误时发出信号 `1`，否则发出信号 `0`。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowError` |

### **Initial string** — 仿真开始时发送的数据 字符向量

可选。输入一个字符向量。仿真开始时，在仿真期间发送的其他数据之前发送指定的数据。

该字符向量可以包含任何内容。您可以使用它来初始化设备。它按指定内容原样发送，不参照 **Format string**。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialValue` |

### **Final string** — 仿真结束时发送的数据 字符向量

可选。输入一个字符向量。当仿真结束时，在仿真期间发送的其他数据之后，发送指定的数据。

该字符向量可以包含任何内容。你可以用它来关闭设备。它会按指定内容原样发送，不参考 **Format string**

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

### R2024b：更新带端口名称的模块

在 R2024b 中，当你启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink®
Desktop Real-Time™ 模块端口会带标签显示。

### R2019b：Stream Input 和 Stream Output 模块支持字符串信号

Stream Input 模块和 Stream Output 模块
支持 Simulink 字符串信号。

### R2019a：RS-232 串行端口驱动程序支持 macOS

Packet Input 模块、Packet
Output 模块、Stream Input 模块和 Stream
Output 模块的串行端口驱动程序支持 macOS 系统。在之前的版本中，这些
模块的串行端口驱动程序仅支持 Windows® 系统。

### R2018a：Stream Input 和 Stream Output 的 TCP 和 UDP 协议支持

Stream Input
模块和 Stream Output 模块的 TCP 协议和 UDP 协议驱动程序可从 Standard Devices
列表中获得。从 Install new board 按钮中，选择 **Standard Devices** > **TCP Protocol** 或选择 **Standard Devices** > **UDP Protocol**。

## 描述

将格式化 ASCII 数据写入通信通道

Stream Output 模块将格式化 ASCII 数据写入端口或文件。
将 Stream Output 模块添加到模型后，双击
Stream Output 模块以打开 Block Parameters: Stream Output
对话框。

驱动程序必须是以下之一：

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**

安装 UDP 设备时，在 Standard
Devices UDP Protocol 对话框中以十进制格式输入端口地址。

任何串行输出端口
都可以以最高 500 Hz 的采样率发送数据。要为某些输出串行端口启用最高 10 kHz 的更快采样
率，请点击 **Install
new board**，选择 **Standard Devices** > **Serial Port**，然后选择 **Direct
port access**。

该模块并非对所有
类型的串行输出硬件都支持此选项。
