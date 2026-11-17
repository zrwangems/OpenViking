---
type: simulink-block
title: 'Encoder Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'encoderinput'
documentation_source_path: 'ref/encoderinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder Input

## 端口

### 输出

### **Encoder Data** — 从输入通道向量读取的编码器数据

表示编码器状态的数据。输出值的数据类型和范围取决于板卡的能力。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Missed Ticks** — 丢失的 tick 计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器 tick 数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖

当您选择 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`

## 参数

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示支持的板卡制造商列表。当您选择某个制造商时，软件显示该制造商可用的板卡列表。当您选择某个板卡时，软件将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡驱动支持的更多信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖

当您在已注册板卡列表中选择某个板卡时，**Delete current board** 和 **Board setup** 按钮变为可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖

要激活此参数，请在已注册板卡列表中选择某个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮将不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框来设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖

要激活此参数，请在已注册板卡列表中选择某个板卡。

要停用此参数，请点击 **Delete current board**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **Sample time** — 模块的采样时间 `0.1`（默认） | double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值，或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器 tick 数 `10`（默认） | integer

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器 tick 数。当模型落后此数量或更少的定时器 tick 时，软件假定该滞后是暂时的。即使模型丢失了一些 tick，也允许模型追赶。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **Yield CPU when waiting** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时授予其他程序更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **Input channels** — 选择编码器输入通道 `1`（默认）| 向量

输入一个通道向量，用于选择您在此板上使用的编码器输入通道。该向量可以是任何有效的 MATLAB® 向量形式。每个向量元素按板上通道编号的顺序对应于所选硬件板上的一个通道。例如，要选择前四个编码器输入通道，请输入：

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

### **Quadrature mode** — 以光学方式检测运动的幅度和方向，选择编码器条纹边沿 `quadruple`（默认）| `double` | `single` | `two-pulse`

编码器使用两组相位偏移的条纹，以光学方式检测运动的幅度和方向。此参数指定编码器对哪些编码器条纹边沿进行计数。从列表中选择：

- `quadruple`（默认）— 对来自两组条纹的上升沿和下降沿进行计数。
- `double` — 对来自两组条纹的上升沿进行计数。
- `single` — 对来自一组条纹的上升沿进行计数。
- `two-pulse` — 对来自两脉冲编码器输入的上升沿进行计数，通道 A 输入使计数递增，通道 B 输入使计数递减。此选项在选择了 NI-62xx 或 NI-63xx 板时可用。

四倍模式每转产生的脉冲数是单倍模式的四倍。因此，四倍模式更精确。除非其他参数另有要求，否则请使用四倍模式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `QuadMode` |

### **Reset input function** — 选择复位引脚的模式 `reset`（默认）| `gate` | `rising edge index` | `falling edge index`

编码器接口芯片除编码器输入外还有一个复位引脚。通常，您将此引脚连接到编码器的索引输出。但是，您也可以将其连接到任何信号，或者不连接。此参数指定此引脚的功能。从列表中选择：

- `reset`（默认）— 编码器计数的电平复位。
- `gate` — 使能编码器计数。
- `rising edge index` — 在上升沿复位编码器计数。
- `falling edge index` — 在下降沿复位编码器计数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `IndexPulse` |

### **Input filter clock frequency** — 低通滤波器的截止频率 (Hz) `Inf`（默认）| 标量

编码器接口芯片包含一个低通滤波器，用于滤除芯片视为噪声的高频信号。此参数是该滤波器的截止频率 (Hz)。您指定的截止频率会舍入到芯片支持的最接近频率。

如果编码器移动缓慢且存在高频噪声，请使用滤波器消除噪声。滤波器工作时，芯片不会将噪声计为编码器脉冲。如果编码器移动较快，滤波器可能会滤除高频脉冲，包括您想要计数的脉冲。在这种情况下，请考虑通过将截止频率设置为 `Inf` 来禁用滤波器。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputFilter` |

### **输出数据类型** — 模块输出 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` 的数据类型

从列表中选择模块输出到模型的数据类型。有效值取决于板卡的能力。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataType` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2024b：更新带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink Desktop Real-Time™ 模块端口会带标签显示。

### R2024a：Encoder Input 模块双脉冲输入支持

在使用 National Instruments™ 62xx 或 63xx I/O 板时，Encoder Input 模块的 Quadrature mode 参数支持选择双脉冲模式。

### R2018a：针对 NI PCIe-6351 的 Encoder Input 模块复位

Encoder Input 模块新增了一个选项，可为 National Instruments PCI-62xx 和 PCI-63xx 板卡驱动选择索引脉冲的编码器相位

## 描述

从一个或多个增量式编码器输入通道读取

Encoder Input 模块连接并从特定编码器输入通道读取数据到您的 Simulink® 模型中。在将 Encoder Input 模块添加到模型后，您可以输入其 I/O 驱动程序的参数。
