---
type: simulink-block
title: 'Stream Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'streaminput'
documentation_source_path: 'ref/streaminput.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Input

## 端口
```yaml
ports:
- name: 输出数据
  summary: 从通信通道接收的数据 数值向量 | 字符串
  direction: output
- name: 数据就绪
  summary: 数据就绪端口（可选） 1 | 0
  direction: output
- name: 数据错误
  summary: 数据错误端口（可选） 1 | 0
  direction: output
- name: 丢失节拍
  summary: 丢失节拍计数（可选） double
  direction: output
  data_types: double
```

### 输出

### **输出数据** — 从通信通道接收的数据 数值向量 | 字符串

从通信通道接收的数据值，以格式化 ASCII 数据形式接收，并根据 **Format string** 进行解码。

### **数据就绪** — 数据就绪端口（可选） `1` | `0`

如果模块有新数据可用，此端口输出 `1`，否则输出 `0`。

#### 依赖关系

当您选中 **Show “Data Ready” port** 时，此端口可见。

### **数据错误** — 数据错误端口（可选） `1` | `0`

如果发生数据错误，此端口输出 `1`，否则输出 `0`。

#### 依赖关系

当您选中 **Show “Data Error” port** 时，此端口可见。

### **丢失节拍** — 丢失节拍计数（可选） double

在 **Connected IO** 模式下，返回您的模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖关系

当您选中 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: 安装新板卡
  summary: 注册板卡 < no board selected >（默认）
  group: ''
  block_parameter: DrvName
- name: 删除当前板卡
  summary: 删除当前板卡（按钮）
  group: ''
  block_parameter: DrvName
- name: 板卡设置
  summary: 设置板卡（按钮）
  group: ''
  block_parameter: DrvOptions
- name: 采样时间
  summary: 模块的采样时间 0.1（默认） | double
  group: ''
  block_parameter: SampleTime
- name: 最大丢失节拍数
  summary: 您的模型可以落后于内核的定时器节拍数 10（默认） | 整数
  group: ''
  block_parameter: MaxMissedTicks
- name: 显示“Missed Ticks”端口
  summary: 将错过的节拍数发送到端口 Missed Ticks 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowMissedTicks
- name: 等待时让出 CPU
  summary: 在内核等待硬件时让出 CPU 'off'（默认）| 'on'
  group: ''
  block_parameter: YieldWhenWaiting
- name: 模块输出数据类型
  summary: 发送到模块输出的数据类型和分组 'double'（默认）| 字符向量 | 字符向量元胞数组
  group: ''
  block_parameter: DataTypes
- name: 格式字符串
  summary: 从流中读取的数据项的格式 '%f'（默认）| 字符向量
  group: ''
  block_parameter: FormatString
- name: 消息终止
  summary: 指定消息结束 {'\r', '\n'}（默认）| 字符向量 | 字符向量元胞数组 | 整数
  group: ''
  block_parameter: Terminator
- name: Show “Data Ready” port
  summary: 添加端口 Data Ready，当数据可用时发出信号 1 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowReady
- name: Show “Data Error” port
  summary: 添加端口 Data Error，如果发生错误则发出信号 1 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowError
```

### **安装新板卡** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示支持的板卡制造商列表。当您选择某个制造商时，软件显示该制造商可用的板卡列表。当您选择某个板卡时，软件将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡驱动支持的更多信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖关系

当您在已注册板卡列表中选择某个板卡时，**Delete current board** 和 **Board setup** 按钮变为可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **删除当前板卡** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮将不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **板卡设置** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框来设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请点击 **Delete current board**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1`（默认） | double

输入一个以秒为单位的值，表示您希望模块执行和与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值，或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大丢失节拍数** — 您的模型可以落后于内核的定时器节拍数 `10`（默认） | 整数

在 **Connected IO** 模式下，输入您的模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。它允许模型追赶，即使模型丢失了一些节拍。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示“Missed Ticks”端口** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时授予其他程序更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **模块输出数据类型** — 发送到模块输出的数据类型和分组 `'double'`（默认）| 字符向量 | 字符向量元胞数组

字符向量或字符向量元胞数组。模块的输出端口数量等于字符向量的数量。每个向量按名称指定一种数据类型，并可选地指定输出向量中该数据类型的数据项数量。例如，`'double'` 表示一个 `double` 值，`'4*int8'` 表示四个 `int8` 值。

输出端口上提供的值根据 **模块输出数据类型** 字符向量进行分组和类型化。例如，如果 **模块输出数据类型** 为 `{'2*int8','3*double'}`，则模块输出：

- 在输出端口 `1` 上 — 宽度为 `2` 的 `int8` 向量
- 在输出端口 `2` 上 — 宽度为 `3` 的 `double` 向量

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataTypes` |

### **格式字符串** — 从流中读取的数据项的格式 `'%f'`（默认）| 字符向量

使用与 C 库 I/O 例程（如 `scanf`）相同格式的规范。格式字符串描述要接收的数据。格式字符串中的元素数量必须等于 **模块输出数据类型** 中指定的数据项数量。如果说明符为 `%s` 或 `%c`（用于字符串），则创建的字符串类型输出端口仅产生字符串信号。此输出端口的 `Block output data types` 参数值必须为 `"1"`，因为字符串只能是标量。

例如，假设 **模块输出数据类型** 为 `{'2*int8','3*double'}`，**格式字符串** 为 `'%d %d %f %f %f'`。模块读取两个整数和三个双精度浮点数的 ASCII 表示。模块将结果值提供给应用程序：

- 输出端口 `1` — 宽度为 `2` 的 `int8` 向量
- 输出端口 `2` — 宽度为 `3` 的 `double` 向量

如果 **模块输出数据类型** 中为某个值指定的数据类型与 **格式字符串** 中对应元素的类型不同，则会发生类型转换。模块按照 **格式字符串** 的指定读取数据，将数据转换为与 **模块输出数据类型** 匹配的类型，并将数据通过模块输出端口提供给应用程序。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FormatString` |

### **消息终止** — 指定消息结束 `{'\r', '\n'}`（默认）| 字符向量 | 字符向量元胞数组 | 整数

字符向量、字符向量元胞数组或数字。如果值为字符向量，接收到此字符序列将终止数据输入。如果值为元胞数组，元胞数组中的任何字符向量都将终止数据输入。如果值为数字，则在读取指定数量的字符后终止数据输入。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Terminator` |

### **Show “Data Ready” port** — 添加端口 `Data Ready`，当数据可用时发出信号 `1` `'off'`（默认）| `'on'`

当您选中此复选框时，该模块将显示输出端口 `Data Ready`。当模块有新数据可用时，此端口发出信号 `1`，否则发出 `0`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowReady` |

### **Show “Data Error” port** — 添加端口 `Data Error`，如果发生错误则发出信号 `1` `'off'`（默认）| `'on'`

当您选中此复选框时，该模块将显示输出端口 `Data Error`。当发生数据错误时，此端口发出信号 `1`，否则发出 `0`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowError` |
## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

### R2024b：更新了带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink® Desktop Real-Time™ 模块端口会显示标签。

### R2019b：Stream Input 和 Stream Output 模块支持字符串信号

Stream Input 模块和 Stream Output 模块支持 Simulink 字符串信号。

### R2019a：RS-232 串行端口驱动程序支持 macOS

Packet Input 模块、Packet Output 模块、Stream Input 模块和 Stream Output 模块的串行端口驱动程序支持 macOS 系统。在之前的版本中，这些模块的串行端口驱动程序仅支持 Windows® 系统。

### R2018a：Stream Input 和 Stream Output 的 TCP 和 UDP 协议支持

Stream Input 模块和 Stream Output 模块的 TCP 协议和 UDP 协议驱动程序可从 Standard Devices 列表中获得。从 Install new board 按钮中，选择 **Standard Devices** > **TCP Protocol** 或选择 **Standard Devices** > **UDP Protocol**。

## 描述

从通信通道读取格式化 ASCII 数据

Stream Input 模块从端口或文件读取格式化 ASCII 数据。将 Stream Input 模块添加到模型后，双击 Stream Input 模块以打开 Block Parameters: Stream Input 对话框。

驱动程序必须是以下之一：

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**

根据需要指定参数值，然后单击 **OK** 或 **Apply**。当您安装 UDP 设备时，在 Standard Devices UDP Protocol 对话框中以十进制格式输入端口地址。
