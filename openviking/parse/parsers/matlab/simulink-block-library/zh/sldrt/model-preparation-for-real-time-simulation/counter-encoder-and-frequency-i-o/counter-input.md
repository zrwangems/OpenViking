---
type: simulink-block
title: 'Counter Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Simulation / Counter, Encoder, and Frequency I/O'
documentation_page: 'counterinput'
documentation_source_path: 'ref/counterinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Counter Input

## 端口

### 输出

### **Counter Data** — 从输入通道向量读取的计数器数据

表示计数器状态的数据。输出值的数据类型取决于板卡的能力。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Missed Ticks** — 丢失节拍计数（可选）double

在 **Connected IO** 模式下，返回您的模型滞后于实时内核的定时器节拍数。当模型滞后超过 **最大丢失节拍数** 时，软件报告错误并停止仿真。

#### 依赖关系

当您选择 **显示 “Missed Ticks” 端口** 时，此端口可见。

**数据类型：** `double`

## 参数

### **安装新板卡** — 注册板卡 `< no board selected >`（默认）

当您点击 **安装新板卡** 时，软件显示受支持板卡制造商的列表。当您选择制造商时，软件显示该制造商提供的板卡列表。当您选择板卡时，软件将该板卡添加到已注册板卡列表中，并使该板卡成为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡的驱动程序支持的详细信息，请参阅 Hardware Support from Simulink Desktop Real-Time。

#### 依赖关系

当您在已注册板卡列表中选择一个板卡时，**删除当前板卡** 和 **板卡设置** 按钮可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **删除当前板卡** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡时，**删除当前板卡** 和 **板卡设置** 按钮将不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **板卡设置** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个特定于板卡的对话框以设置板卡。有关详细信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请点击 **删除当前板卡**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1`（默认）| double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块按此采样率将您的模型与实时时钟同步。

如果您使用的是定步长求解器，请输入您在 **固定步长** 配置参数中输入的值，或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大丢失节拍数** — 您的模型可以滞后于内核的定时器节拍数 `10`（默认）| integer

在 **Connected IO** 模式下，输入您的模型可以滞后于实时内核的定时器节拍数。当模型滞后此数量或更少的定时器节拍时，软件假定该滞后是临时的。即使模型丢失一些节拍，它也会允许模型赶上。当模型滞后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将丢失节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以将丢失节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 当内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时向其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **输入通道** — 选择计数器输入通道 `1`（默认）| vector

输入一个通道向量，用于选择您在此板卡上使用的计数器输入通道。该向量可以是任何有效的 MATLAB® 向量形式。

例如，要选择板卡上的前四个计数器输入通道，请输入：

```
[1,2,3,4]
```

或

```
[1:4]
```

#### 程序化使用

|  |
| --- |
| **模块参数：** `Channels` |

### **读取后复位** — 计数器复位策略 `never`（默认）| `always` | `level` | `rising edge` | `falling edge` | `either edge`

确定软件在读取计数器值后是否将其复位为零。从列表中选择以下选项之一：

- `never` —
  读取后不复位。
- `always` —
  读取后始终复位。
- `level` — 如果模块输入非零，则在读取后复位。向 Counter Input 模块添加一个输入。
- `rising edge` — 如果模块输入在最后两次连续读取之间从零变为非零，则在读取后复位。向 Counter Input 模块添加一个输入。
- `falling edge` — 如果模块输入在最后两次连续读取之间从非零变为零，则在读取后复位。向 Counter Input 模块添加一个输入。
- `either edge` — 如果模块输入在最后两次连续读取之间从零变为非零或从非零变为零，则在读取后复位。向 Counter Input 模块添加一个输入。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ResetMode` |

### **时钟输入源** — 递增计数器的时钟输入 `input pin rising edge`（默认）| `input pin falling edge` | `internal clock`

确定用于递增计数器的时钟输入源。从列表中选择：

- `input pin rising edge` —
  时钟边沿从低到高的跳变
- `input pin falling edge` —
  时钟边沿从高到低的跳变
- `internal clock` —
  内部时基

  如果您将 **门输入功能** 参数设置为 `enable when high, latch & reset on edge`，或 `enable when low, latch & reset on edge`，则可以以内部时基为单位测量正脉冲或负脉冲长度。您可以将此组合与 National Instruments™ 驱动程序一起用于脉冲宽度测量。

并非所有计数器芯片都支持选择输入边沿。在这种情况下，列表中仅显示受支持的选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CounterEdge` |

### **门输入功能** — 计数器门输入引脚的操作 `none`（默认）| `enable when high` | `enable when low` | `start on rising edge` | `start on falling edge` | `reset on rising edge` | `reset on falling edge` | `latch on rising edge` | `latch on falling edge` | `latch & reset on rising edge` | `latch & reset on falling edge` | `enable when high, latch & reset on edge` | `enable when low, latch & reset on edge`

定义计数器门输入引脚的操作。从列表中选择：

- `none` —
  无条件启用计数，忽略门输入。
- `enable when high` —
  当门输入为低时禁用计数，当门输入为高时启用计数。
- `enable when low`  —
  当门输入为高时禁用计数，当门输入为低时启用计数。
- `start on rising edge` —
  禁用计数，直到发生低到高的门跳变。
- `start on falling edge` —
  禁用计数，直到发生高到低的门跳变。
- `reset on rising edge` —
  当发生低到高的门跳变时，将计数器复位为零。
- `reset on falling edge` —
  当发生高到低的门跳变时，将计数器复位为零。
- `latch on rising edge` —
  当发生低到高的门跳变时，将计数存储到寄存器中。返回寄存器内容。
- `latch on falling edge` —
  当发生高到低的门跳变时，将计数存储到寄存器中。返回寄存器内容。
- `latch & reset on rising edge` —
  当发生低到高的门跳变时，将计数存储到寄存器中，然后将计数器复位为零。返回寄存器内容。
- `latch & reset on falling edge` —
  当发生高到低的门跳变时，将计数存储到寄存器中，然后将计数器复位为零。返回寄存器内容。
- `enable when high, latch & reset on
  edge` — 当门输入为低时禁用计数。
  当发生低到高的门跳变时开始计数。当门输入为高时计数。当发生高到低的门跳变时，将计数存储到寄存器中，然后将计数器复位为零。返回寄存器内容。

  如果您将 **时钟输入源** 参数设置为 `internal clock`，则可以以内部时基为单位测量正脉冲长度。您可以将此组合与大多数 National Instruments 驱动程序一起用于脉冲宽度测量。
- `enable when low, latch & reset on
  edge` — 当门输入为高时禁用计数。
  当发生高到低的门跳变时开始计数。当门输入为低时计数。当发生低到高的门跳变时，将计数存储到寄存器中，然后将计数器复位为零。返回寄存器内容。

  如果您将 **时钟输入源** 参数设置为 `internal clock`，则可以以内部时基为单位测量负脉冲长度。您可以将此组合与 National Instruments 驱动程序一起用于脉冲宽度测量。

并非所有计数器芯片都支持所有门输入模式。列表中仅显示受支持的模式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `CounterGate` |

### **输出数据类型** — 模块输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

从列表中选择模块输出到模型的数据类型。有效值取决于板卡的能力。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataType` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2024b：对带端口名称的模块的更新

在 R2024b 中，当您启用可选端口（例如 **显示 "Missed Ticks" 端口**）时，这些 Simulink Desktop Real-Time™ 模块端口会显示标签。

## 描述

从一个或多个计数器输入通道读取

Counter Input 模块连接到特定的计数器输入通道，并将数据读入您的 Simulink® 模型。将 Counter Input 模块添加到模型后，您可以输入其 I/O 驱动程序的参数。
