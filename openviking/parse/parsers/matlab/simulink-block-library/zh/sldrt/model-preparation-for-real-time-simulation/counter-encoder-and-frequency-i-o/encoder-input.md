---
type: simulink-block
title: 'Encoder Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Simulation / Counter, Encoder, and Frequency I/O'
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

### **Missed Ticks** — 丢失节拍计数（可选）double

在 **Connected IO** 模式下，返回您的模型滞后于实时内核的定时器节拍数。当模型滞后超过 **最大丢失节拍数** 时，软件会报告错误并停止仿真。

#### 依赖关系

当您选择 **显示 “Missed Ticks” 端口** 时，此端口可见。

**数据类型：** `double`

## 参数

### **安装新板卡** — 注册板卡 `< no board selected >`（默认）

当您点击 **安装新板卡** 时，软件会显示支持的板卡制造商的列表。当您选择某个制造商时，软件会显示该制造商提供的板卡列表。当您选择某个板卡时，软件会将该板卡添加到已注册板卡列表中，并使该板卡成为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡的驱动程序支持的更多信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖关系

当您在已注册板卡列表中选择一个板卡时，**删除当前板卡**和**板卡设置**按钮可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **删除当前板卡** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将更改为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

删除当前板卡后，**删除当前板卡**和**板卡设置**按钮将不再可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **板卡设置** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个特定于板卡的对话框以设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请点击 **删除当前板卡**。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1`（默认）| double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您作为 **固定步长** 配置参数输入的值，或该值的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大丢失节拍数** — 您的模型可以滞后于内核的定时器节拍数 `10`（默认）| 整数

在 **Connected IO** 模式下，输入您的模型可以滞后于实时内核的定时器节拍数。当模型滞后此数量或更少的定时器节拍时，软件假定该滞后是临时的。它允许模型赶上，即使模型丢失了一些节拍。当模型滞后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将丢失节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将丢失节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时为其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **输入通道** — 选择编码器输入通道 `1`（默认）| 向量

输入一个通道向量，用于选择您在此板卡上使用的编码器输入通道。该向量可以是任何有效的 MATLAB® 向量形式。每个向量元素按板卡上通道的编号顺序对应于所选硬件板卡上的一个通道。例如，要选择前四个编码器输入通道，请输入：

```
[1,2,3,4]
```

或

```
[1:4]
```

#### 编程用法

|  |
| --- |
| **模块参数：** `Channels` |

### **正交模式** — 为以光学方式检测运动的幅度和方向，选择编码器条纹边沿 `quadruple`（默认）| `double` | `single` | `two-pulse`

编码器使用两组相位偏移的条纹，以光学方式检测运动的幅度和方向。此参数指定编码器对哪些编码器条纹边沿进行计数。从列表中选择：

- `quadruple`（默认）—
  对两组条纹的上升沿和下降沿进行计数。
- `double` — 对两组条纹的上升沿进行计数。
- `single` — 对一组条纹的上升沿进行计数。
- `two-pulse` — 对来自两脉冲编码器输入的上升沿进行计数，其中通道 A 输入使计数递增，通道 B 输入使计数递减。此选项在选择了 NI-62xx 或 NI-63xx 板卡时可用。

quadruple 模式每转产生的脉冲数比 single 模式多四倍。因此，quadruple 更准确。除非其他参数另有要求，否则请使用 quadruple 模式。

#### 编程用法

|  |
| --- |
| **模块参数：** `QuadMode` |

### **复位输入功能** — 选择复位引脚的模式 `reset`（默认）| `gate` | `rising edge index` | `falling edge index`

编码器接口芯片除了编码器输入外，还有一个复位引脚。通常，您将该引脚连接到编码器的索引输出。但是，您可以将其连接到任何信号，也可以完全不连接。此参数指定该引脚的功能。从列表中选择：

- `reset`（默认）—
  对编码器计数进行电平复位。
- `gate` — 启用编码器计数。
- `rising edge index` —
  在上升沿复位编码器计数。
- `falling edge index` —
  在下降沿复位编码器计数。

#### 编程用法

|  |
| --- |
| **模块参数：** `IndexPulse` |

### **输入滤波器时钟频率** — 低通滤波器的截止频率 (Hz) `Inf`（默认）| 标量

编码器接口芯片包含一个低通滤波器，用于滤除高频，芯片将这些高频视为噪声。此参数是该滤波器的截止频率 (Hz)。您指定的截止频率会舍入到芯片支持的最接近频率。

如果编码器移动缓慢且存在高频噪声，请使用滤波器消除噪声。滤波器工作时，芯片不会将噪声计为编码器脉冲。如果编码器移动很快，滤波器可能会滤除高频脉冲，包括您想要计数的脉冲。在这种情况下，请考虑通过将截止频率设置为 `Inf` 来禁用滤波器。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputFilter` |

### **输出数据类型** — 模块输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

从列表中选择模块输出到模型的数据类型。有效值取决于板卡的能力。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataType` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 之前引入**

### R2024b：更新带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **显示 "Missed Ticks" 端口**）时，这些 Simulink Desktop Real-Time™ 模块端口会显示标签。

### R2024a：Encoder Input 模块 two-pulse 输入支持

Encoder Input 模块的 Quadrature mode 参数支持在使用 National Instruments™ 62xx 或 63xx I/O 板卡时选择 two-pulse 模式。

### R2018a：Encoder Input 模块针对 NI PCIe-6351 的复位

Encoder Input 模块新增了一个选项，用于为 National Instruments PCI-62xx 和 PCI-63xx 板卡驱动程序选择索引脉冲的编码器相位

## 描述

从一个或多个增量式编码器输入通道读取

Encoder Input 模块连接到特定编码器输入通道，并将其读入您的 Simulink® 模型。将 Encoder Input 模块添加到模型后，您可以输入其 I/O 驱动程序的参数。
