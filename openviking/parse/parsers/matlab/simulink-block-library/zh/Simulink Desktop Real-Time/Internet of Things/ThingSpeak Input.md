---
type: simulink-block
title: 'ThingSpeak Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Internet of Things'
documentation_page: 'thingspeakinput'
documentation_source_path: 'ref/thingspeakinput.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Input

## 端口

### 输出

### **Data** — 从通道读取的数据 numeric

从 ThingSpeak 通道读取的标量 numeric 数据。

**示例：** `3.14159`

#### 依赖关系

**输出数据类型** 参数的设置决定端口数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **通道编号** — 正在访问的 ThingSpeak 通道 只读：`0`（默认）| numeric

此参数为只读。

要选择通道，请点击 **配置通道参数** 按钮。在 Network Services ThingSpeak 对话框中，设置 **通道 ID** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvAddress` |

### **配置通道参数** — 选择并配置要访问的通道（按钮）

要配置通道，请点击此按钮。对话框将显示通道参数设置。

要接受更改，请点击 **确定**。要测试更改，请点击 **测试**。要将设置恢复为先前值，请点击 **还原**。要在不更改设置的情况下退出对话框，请点击 **取消**。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvName` |
| **模块参数：** `DrvOptions` |

### **ThingSpeak 服务器** — 用于数据传输的服务器 `api.thingspeak.com`（默认）| character vector

默认值是公共 ThingSpeak 服务器的标准地址。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvName` |
| **模块参数：** `DrvOptions` |

### **通道 ID** — 唯一通道 `12397`（默认）| numeric

从可用通道中选择一个唯一通道。

在同一模型中，不能通过同一个 ThingSpeak 通道进行读取和写入。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvOptions` |

### **读取 API 密钥** — 用于从通道读取的访问密钥 character vector

默认情况下，此密钥是公共服务器 api.thingspeak.com 上该通道的 API 密钥。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvOptions` |

### **更新周期 (secs)** — 读取更新周期，以 seconds 为单位 `20`（默认）| numeric

通过该通道连续读取之间的时间。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvOptions` |

### **查看通道网页** — 访问通道的网页（按钮）

要访问 **通道编号** 的网页，请点击 **查看通道网页**。

#### 编程使用

|  |
| --- |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1`（默认）| double

输入一个值（以 seconds 为单位），表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用固定步长求解器，请输入您在 **固定步长** 配置参数中输入的值，或该值的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大错过 ticks** — 您的模型可以落后内核的计时器 ticks 数 `10`（默认）| integer

在 **Connected IO** 模式下，输入您的模型可以落后实时内核的计时器 ticks 数。当模型落后此数量或更少的计时器 ticks 时，软件假定该滞后是临时的。即使模型错过一些 ticks，也允许模型赶上。当模型落后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将错过的 ticks 数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的 ticks 数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时为其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **要读取的通道字段** — 定义要读取通道的哪些部分 `1`（默认）| `[1–8]`

您可以从每个通道读取 `1–8` 个字段。使用此参数可忽略特定于实现的信息，并仅接收您的应用所需的字段。

#### 编程使用

|  |
| --- |
| **模块参数：** `ChannelFields` |

### **输出数据类型** — 定义输出端口的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `<data type expression>`

定义输出端口的数据类型。

要打开数据类型助手，请点击 **>>** 按钮。要关闭数据类型助手，请点击 **<<** 按钮。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataTypeStr` |

### **模式** — 定义类型的方法 `Built in`（默认）| `Expression`

使用内置类型，例如 `double`，或由数据类型表达式定义的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `OptParam` |

### **类型** — 数据类型选择器 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

可用于构造数据类型表达式的内置类型集。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataTypeStr` |

### **数据类型覆盖** — 信号类型不匹配时的策略 `inherit`（默认）| `off`

- `inherit` — 端口继承其所连接信号的类型。
- `off` — 端口将信号数据类型设置为此模块定义的类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataTypeStr` |

## 所属库

Simulink Desktop Real-Time / Internet of Things

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017b 中引入**

### R2024b：对具有端口名称的模块进行更新

在 R2024b 中，当您启用可选端口（例如 **显示 "Missed Ticks" 端口**）时，这些 Simulink® Desktop Real-Time™ 模块端口会带标签显示。

## 描述

从 ThingSpeak 通道读取输入字段

ThingSpeak Input 模块从 ThingSpeak™ 通道读取 numeric 数据。

默认情况下，此模块使用公共 ThingSpeak 服务器 `api.thingspeak.com`。要配置 ThingSpeak 通道，请点击 **配置通道参数**。

要访问 **通道编号** 的网页，请点击 **查看通道网页**。

此模块不会将 ThingSpeak 时间戳与仿真时间同步。例如，假设模块的采样时间设置为 `0.1` s，通道更新周期为 `20` s。传感器在时间 *T* 获取新数据并将其传输到 ThingSpeak 服务器，服务器会为该数据提供时间戳。如果新数据在 `20` s 更新周期过去之前到达，则新数据会丢失。该模块每 `0.1` s 运行一次，并且仅每 `20` s 获取一次新数据。其余时间，该模块获取的是旧数据。
