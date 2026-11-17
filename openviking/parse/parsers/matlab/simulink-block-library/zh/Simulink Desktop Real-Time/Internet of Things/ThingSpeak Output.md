---
type: simulink-block
title: 'ThingSpeak Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Internet of Things'
documentation_page: 'thingspeakoutput'
documentation_source_path: 'ref/thingspeakoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Output

## 端口

### 输入

### **Data** — 要写入通道的数据 numeric

要写入 ThingSpeak 通道的标量数值数据。

**示例：** `3.14159`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Channel number** — 正在访问的 ThingSpeak 通道 只读：`0`（默认）| numeric

此参数为只读。

要选择通道，请点击 **Configure channel parameters** 按钮。在 Network Services ThingSpeak 对话框中，设置 **Channel ID** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvAddress` |

### **Configure channel parameters** — 选择并配置要访问的通道（按钮）

要配置通道，请点击此按钮。将显示一个对话框，其中包含通道参数设置。

要接受更改，请点击 **OK**。要测试更改，请点击 **Test**。要将设置恢复为之前的值，请点击 **Revert**。要不更改设置直接退出对话框，请点击 **Cancel**。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvName` |
| **模块参数**：`DrvOptions` |

### **ThingSpeak server** — 用于数据传输的服务器 `api.thingspeak.com`（默认）| character vector

默认值是公共 ThingSpeak 服务器的标准地址。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvName` |
| **模块参数**：`DrvOptions` |

### **Channel ID** — 唯一通道 `0`（默认）| numeric

在可用通道中选择一个唯一通道。

不能在同一模型中对同一 ThingSpeak 通道进行读取和写入。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvOptions` |

### **Write API key** — 用于写入通道的访问密钥 character vector

默认情况下，此密钥是公共服务器 api.thingspeak.com 上该通道的 API 密钥。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvOptions` |

### **Update period (secs)** — 写入更新周期，以秒为单位 `20`（默认）| numeric

对通道进行连续写入之间的时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvOptions` |

### **View channel web page** — 访问通道网页（按钮）

要访问 **Channel number** 的网页，请点击 **View channel web page**。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvOptions` |

### **Sample time** — 模块采样时间 `0.1`（默认）| double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块按此采样率将您的模型与实时时钟同步。

如果您使用固定步长求解器，请输入与 **Fixed step size** 配置参数相同的值，或该值的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |

### **Maximum missed ticks** — 模型可以落后内核的定时器节拍数 `10`（默认）| integer

在 **Connected IO** 模式下，输入模型可以落后实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是临时的。即使模型错过了一些节拍，也允许模型赶上。当模型落后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowMissedTicks` |

### **Yield CPU when waiting** — 当内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时，为其他程序授予更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **Output fields** — 定义要写入的数据部分 `1`（默认）| `[1–8]`

每个通道最多可写入 `1–8` 个字段。使用此参数可忽略特定于实现的信息，仅传输应用程序所需的字段。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ChannelFields` |

### **Initial value** — 传输的第一个值 []（默认）| `[integer]`

传输一个初始值，例如初始状态值或初始化命令。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialValue` |

### **Final value** — 传输的最后一个值 []（默认）| `[integer]`

传输一个最终值，例如最终状态值或收尾命令。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FinalValue` |

## 所属库

Simulink Desktop Real-Time / Internet of Things

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

### R2024b：更新为带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink® Desktop Real-Time™ 模块端口会显示标签。

## 描述

将输出字段写入 ThingSpeak 通道

ThingSpeak Output 模块将数值数据写入 `1−8` 个 ThingSpeak™ 通道。

默认情况下，此模块使用公共 ThingSpeak 服务器 `api.thingspeak.com`。要配置 ThingSpeak 通道，请点击 **Configure channel parameters**。

要访问 **Channel number** 的网页，请点击 **View channel web page**。

此模块不会将 ThingSpeak 时间戳与仿真时间同步。例如，假设该模块的采样时间设置为 `0.1` 秒，且通道更新周期为 `20` 秒。该模块在特定仿真时间 *T* 传输数据，但 ThingSpeak 仅在 `20` 更新周期时写入数据并为其添加时间戳。
