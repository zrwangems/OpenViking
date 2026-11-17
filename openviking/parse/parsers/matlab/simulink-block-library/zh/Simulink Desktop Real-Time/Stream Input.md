---
type: simulink-block
title: 'Stream Input'
family: 'simulink-desktop-real-time'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Simulink Desktop Real-Time'
documentation_page: 'streaminput'
documentation_source_path: 'ref/streaminput.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Input

## 端口

### 输出

### **Output Data** — 从通信通道接收的数据 numeric vector | string

从通信通道接收的数据值，采用格式化 ASCII 数据形式，并根据 **格式字符串** 解码。

### **Data Ready** — 数据就绪端口（可选） `1` | `0`

当模块有新数据可用时，此端口输出 `1`，否则输出 `0`。

#### 依赖关系

当您选择 **显示 “Data Ready” 端口** 时，此端口可见。

### **Data Error** — 数据错误端口（可选） `1` | `0`

当发生数据错误时，此端口输出 `1`，否则输出 `0`。

#### 依赖关系

当您选择 **显示 “Data Error” 端口** 时，此端口可见。

### **Missed Ticks** — 错过的 tick 计数（可选） double

在 **Connected IO** 模式下，返回模型滞后于实时内核的定时器 tick 数。当模型滞后超过 **最大错过 tick 数** 时，软件会报告错误并停止仿真。

#### 依赖关系

当您选择 **显示 “Missed Ticks” 端口** 时，此端口可见。

**数据类型：** `double`

## 参数

### **安装新板卡** — 注册板卡 `< no board selected >`（默认）

当您点击 **安装新板卡** 时，软件会显示支持的板卡制造商列表。当您选择某个制造商时，软件会显示该制造商提供的板卡列表。当您选择某个板卡时，软件会将该板卡添加到已注册板卡列表，并使该板卡成为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `<
no board selected >`。

有关 I/O 板卡驱动支持的更多信息，请参见 Hardware Support from Simulink Desktop Real-Time。

#### 依赖关系

当您在已注册板卡列表中选择某个板卡时，**删除当前板卡** 和 **板卡设置** 按钮可用。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **删除当前板卡** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `<
no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡后，**删除当前板卡** 和 **板卡设置** 按钮将不再可用。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **板卡设置** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开特定于板卡的对话框以设置板卡。有关更多信息，请参见板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请点击 **删除当前板卡**。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1`（默认） | double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块按此采样率将模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **固定步长** 配置参数中输入的值，或该值的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大错过 tick 数** — 模型可滞后于内核的定时器 tick 数 `10`（默认） | integer

在 **Connected IO** 模式下，输入模型可滞后于实时内核的定时器 tick 数。当模型滞后此数量或更少的定时器 tick 时，软件认为该滞后是临时的。即使模型错过一些 tick，也允许模型追赶。当模型滞后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将错过的 tick 数发送到端口 `Missed Ticks` `'off'`（默认） | `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的 tick 数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 内核等待硬件时让出 CPU `'off'`（默认） | `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时向其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **模块输出数据类型** — 发送到模块输出的数据类型和分组 `'double'`（默认） | character vector | cell array of character vector

一个 character vector 或一个 character vector 的 cell array。模块的输出端口数量等于 character vector 的数量。每个向量按名称指定一种数据类型，并可选择指定输出向量中该数据类型的项数。例如，`'double'` 表示一个 `double` 值，`'4*int8'` 表示四个 `int8` 值。

输出端口上提供的值根据 **模块输出数据类型** character vector 进行分组和类型化。例如，如果 **模块输出数据类型** 为 `{'2*int8','3*double'}`，则模块输出：

- 在输出端口 `1` 上 — 一个宽度为 `2` 的 `int8` 向量
- 在输出端口 `2` 上 — 一个宽度为 `3` 的 `double` 向量

#### 编程使用

|  |
| --- |
| **模块参数：** `DataTypes` |

### **格式字符串** — 从流中读取的数据项的格式 `'%f'`（默认） | character vector

一种与 C 库 I/O 例程（如 `scanf`）所用格式相同的规范。格式字符串描述要接收的数据。格式字符串中的元素数量必须等于 **模块输出数据类型** 中指定的数据项数量。如果说明符为 `%s` 或 `%c`（用于字符串），则创建的 string 类型输出端口仅生成 string 信号。此输出端口的 `Block output data types` 参数值必须为 `"1"`，因为字符串只能是标量。

例如，假设 **模块输出数据类型** 为 `{'2*int8','3*double'}`，**格式字符串** 为 `'%d %d %f %f %f'`。模块读取两个整数和三个 double 的 ASCII 表示。模块将结果值提供给应用程序，位于：

- 输出端口 `1` — 一个宽度为 `2` 的 `int8` 向量
- 输出端口 `2` — 一个宽度为 `3` 的 `double` 向量

如果为 **模块输出数据类型** 中的某个值指定的数据类型与 **格式字符串** 中对应元素的类型不同，则会发生类型转换。模块按 **格式字符串** 的指定读取数据，将数据转换为与 **模块输出数据类型** 匹配，并将数据通过模块输出端口提供给应用程序。

#### 编程使用

|  |
| --- |
| **模块参数：** `FormatString` |

### **消息终止** — 指定消息结束 `{'\r', '\n'}`（默认） | character vector | cell array of character vector | integer

一个 character vector、character vector 的 cell array 或一个数字。如果该值是一个 character vector，则接收到该字符序列会终止数据输入。如果该值是一个 cell array，则 cell array 中的任何 character vector 都会终止数据输入。如果该值是一个数字，则在读取指定数量的字符后终止数据输入。

#### 编程使用

|  |
| --- |
| **模块参数：** `Terminator` |

### **显示 “Data Ready” 端口** — 添加端口 `Data Ready`，当数据可用时发出 `1` 信号 `'off'`（默认） | `'on'`

当您选中此复选框时，模块将使输出端口 `Data Ready` 可见。当模块有新数据可用时，此端口发出 `1` 信号，否则发出 `0`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowReady` |

### **显示 “Data Error” 端口** — 添加端口 `Data Error`，如果发生错误则发出 `1` 信号 `'off'`（默认） | `'on'`

当您选中此复选框时，模块将使输出端口 `Data Error` 可见。当发生数据错误时，此端口发出 `1` 信号，否则发出 `0`。

#### 编程使用

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

**R2007b 中引入**

### R2024b：更新为具有端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **显示 "Missed Ticks"
端口**）时，这些 Simulink®
Desktop Real-Time™ 模块端口会带标签显示。

### R2019b：Stream Input 和 Stream Output 模块支持 String 信号

Stream Input 模块和 Stream Output 模块支持 Simulink string 信号。

### R2019a：RS-232 串行端口驱动程序支持 macOS

Packet Input 模块、Packet
Output 模块、Stream Input 模块和 Stream
Output 模块的串行端口驱动程序支持 macOS 系统。在之前的版本中，这些模块的串行端口驱动程序仅支持 Windows® 系统。

### R2018a：Stream Input 和 Stream Output 的 TCP 和 UDP 协议支持

Stream Input 模块和 Stream Output 模块的 TCP 协议和 UDP 协议驱动程序可从 Standard Devices 列表中获得。在 **安装新板卡** 按钮中，选择 **Standard Devices** > **TCP Protocol** 或选择 **Standard Devices** > **UDP Protocol**。

## 描述

从通信通道读取格式化 ASCII 数据

Stream Input 模块从端口或文件读取格式化 ASCII 数据。将 Stream Input 模块添加到模型后，双击 Stream Input 模块以打开 Block Parameters: Stream Input 对话框。

驱动程序必须是以下之一：

- **Standard Devices** > **File**
- **Standard Devices** > **Serial Port**
- **Standard Devices** > **TCP Protocol**
- **Standard Devices** > **UDP Protocol**

根据需要指定参数值，然后点击 **OK** 或 **Apply**。安装 UDP 设备时，请在 Standard Devices UDP Protocol 对话框中以十进制格式输入端口地址。
