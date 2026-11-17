---
type: simulink-block
title: 'Counter Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'counterinput'
documentation_source_path: 'ref/counterinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Counter Input

## 端口
```yaml
ports:
- name: Counter Data
  summary: 从输入通道向量读取的计数器数据
  direction: output
  data_types: single | double | int8 | uint8 | int16 | uint16 | int32 | uint32
- name: Missed Ticks
  summary: 丢失的滴答计数（可选）double
  direction: output
  data_types: double
```

### 输出

### **Counter Data** — 从输入通道向量读取的计数器数据

表示计数器状态的数据。输出值的数据类型取决于板卡的能力。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Missed Ticks** — 丢失的滴答计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器滴答数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖

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
  summary: 模型可以落后于内核的定时器滴答数 10（默认） | integer
  group: ''
  block_parameter: MaxMissedTicks
- name: Show “Missed Ticks” port
  summary: 将错过的节拍数发送到端口 Missed Ticks 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowMissedTicks
- name: Yield CPU when waiting
  summary: 内核等待硬件时让出 CPU 'off'（默认）| 'on'
  group: ''
  block_parameter: YieldWhenWaiting
- name: Input channels
  summary: 选择计数器输入通道 1（默认）| 向量
  group: ''
  block_parameter: Channels
- name: Reset after read
  summary: 计数器复位策略 never（默认）| always | level | rising edge | falling edge | either edge
  group: ''
  block_parameter: ResetMode
- name: Clock input source
  summary: 使计数器递增的时钟输入 input pin rising edge（默认）| input pin falling edge | internal clock
  group: ''
  block_parameter: CounterEdge
- name: Gate input functionality
  summary: 计数器门输入引脚 none（默认）| enable when high | enable when low | start on rising edge | start on falling edge | reset on
    rising edge | reset on falling edge | latch on rising edge | latch on falling edge | latch & reset on rising edge | latch
    & reset on falling edge | enable when high, latch & reset on edge | enable when low, latch & reset on edge 的动作
  group: ''
  block_parameter: CounterGate
- name: Output data type
  summary: 模块输出的数据类型 double（默认）| single | int8 | uint8 | int16 | uint16 | int32 | uint32
  group: ''
  block_parameter: DataType
```

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示支持的板卡制造商列表。当您选择某个制造商时，软件显示该制造商可用的板卡列表。当您选择某个板卡时，软件将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡驱动支持的更多信息，请参阅 Hardware Support from Simulink Desktop Real-Time。

#### 依赖

当您在已注册板卡列表中选择某个板卡时，**Delete current board** 和 **Board setup** 按钮变为可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮将不再可用。

#### 编程使用

|  |
| --- |
| **模块参数**：`DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框来设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖

要激活此参数，请在已注册板卡列表中选择一个板卡。

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

### **Maximum missed ticks** — 模型可以落后于内核的定时器滴答数 `10`（默认） | integer

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器滴答数。当模型落后此数量或更少的定时器滴答时，软件假定该滞后是暂时的。即使模型丢失了一些滴答，它也允许模型追赶。当模型落后超过此数量时，软件报告错误并停止仿真。

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

### **Yield CPU when waiting** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时，为其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`YieldWhenWaiting` |

### **Input channels** — 选择计数器输入通道 `1`（默认）| 向量

输入一个通道向量，用于选择此板上正在使用的计数器输入通道。该向量可以是任何有效的 MATLAB® 向量形式。

例如，要选择板上的前四个计数器输入通道，请输入：

```
[1,2,3,4]
```

或

```
[1:4]
```

#### 编程使用

|  |
| --- |
| **模块参数**：`Channels` |

### **Reset after read** — 计数器复位策略 `never`（默认）| `always` | `level` | `rising edge` | `falling edge` | `either edge`

确定软件在读取计数器值后是否将其复位为零。从列表中选择以下选项之一：

- `never` —
  读取后不复位。
- `always` —
  读取后始终复位。
- `level` — 如果模块输入非零，则读取后复位。向 Counter Input 模块添加一个输入。
- `rising edge` — 如果在最后两次连续读取之间，模块输入从零变为非零，则读取后复位。向 Counter Input 模块添加一个输入。
- `falling edge` — 如果在最后两次连续读取之间，模块输入从非零变为零，则读取后复位。向 Counter Input 模块添加一个输入。
- `either edge` — 如果在最后两次连续读取之间，模块输入从零变为非零或从非零变为零，则读取后复位。向 Counter Input 模块添加一个输入。

#### 编程使用

|  |
| --- |
| **模块参数**：`ResetMode` |

### **Clock input source** — 使计数器递增的时钟输入 `input pin rising edge`（默认）| `input pin falling edge` | `internal clock`

确定用于使计数器递增的时钟输入源。从列表中选择：

- `input pin rising edge` —
  时钟边沿从低到高的跳变
- `input pin falling edge` —
  时钟边沿从高到低的跳变
- `internal clock` —
  内部时基

  如果将 **Gate input functionality** 参数设置为 `enable when high, latch & reset on edge`，或 `enable when low, latch & reset on edge`，则可以以内部时基为单位测量正脉冲或负脉冲长度。可以将此组合与 National Instruments™ 驱动程序一起用于脉冲宽度测量。

并非所有计数器芯片都支持选择输入边沿。在这种情况下，列表中仅显示受支持的选项。

#### 编程使用

|  |
| --- |
| **模块参数**：`CounterEdge` |

### **Gate input functionality** — 计数器门输入引脚 `none`（默认）| `enable when high` | `enable when low` | `start on rising edge` | `start on falling edge` | `reset on rising edge` | `reset on falling edge` | `latch on rising edge` | `latch on falling edge` | `latch & reset on rising edge` | `latch & reset on falling edge` | `enable when high, latch & reset on edge` | `enable when low, latch & reset on edge` 的动作

定义计数器门输入引脚的动作。从列表中选择：

- `none` —
  无条件启用计数，忽略门输入。
- `enable when high` —
  当门输入为低电平时禁用计数，当门输入为高电平时启用计数。
- `enable when low`  —
  当门输入为高电平时禁用计数，当门输入为低电平时启用计数。
- `start on rising edge` —
  在发生低到高门跳变之前禁用计数。
- `start on falling edge` —
  在发生高到低门跳变之前禁用计数。
- `reset on rising edge` —
  当发生低到高门跳变时，将计数器重置为零。
- `reset on falling edge` —
  当发生高到低门跳变时，将计数器重置为零。
- `latch on rising edge` —
  当发生低到高门跳变时，将计数值存储到寄存器中。返回寄存器内容。
- `latch on falling edge` —
  当发生高到低门跳变时，将计数值存储到寄存器中。返回寄存器内容。
- `latch & reset on rising edge` —
  当发生低到高门跳变时，将计数值存储到寄存器中，然后将计数器重置为零。返回寄存器内容。
- `latch & reset on falling edge` —
  当发生高到低门跳变时，将计数值存储到寄存器中，然后将计数器重置为零。返回寄存器内容。
- `enable when high, latch & reset on
  edge` — 当门输入为低电平时禁用计数。
  当发生低到高门跳变时开始计数。当门输入为高电平时计数。当发生高到低门跳变时，将计数值存储到寄存器中，然后将计数器
  重置为零。返回寄存器内容。

  如果将 **Clock input source** 参数
  设置为 `internal clock`，则可以以内部时基为单位测量正
  脉冲长度。您可以将此组合与大多数 National Instruments 驱动程序一起用于脉冲宽度
  测量。
- `enable when low, latch & reset on
  edge` — 当门输入为高电平时禁用计数。
  当发生高到低门跳变时开始计数。当门输入为低电平时计数。当发生低到高门跳变时，将计数值存储到寄存器中，然后将计数器
  重置为零。返回寄存器内容。

  如果将 **Clock input source** 参数
  设置为 `internal clock`，则可以以内部时基为单位测量负
  脉冲长度。您可以将此组合与 National Instruments 驱动程序一起用于脉冲宽度
  测量。

并非所有计数器芯片
都支持所有门输入模式。
列表中仅显示支持的模式。

#### 编程使用

|  |
| --- |
| **模块参数**：`CounterGate` |

### **Output data type** — 模块输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

从列表中选择模块输出到模型的数据类型。有效值
取决于板卡的能力。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataType` |
## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2024b：更新为带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks"
port**）时，这些 Simulink
Desktop Real-Time™ 模块端口会显示标签。

## 描述

从一个或多个计数器输入通道读取

Counter Input 模块连接并从特定的计数器输入通道读取数据到您的 Simulink® 模型中。在将 Counter Input 模块添加到模型后，您可以输入其 I/O 驱动程序的参数。
