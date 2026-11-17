---
type: simulink-block
title: 'Analog Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'analoginput'
documentation_source_path: 'ref/analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

### 输出

### **Analog Data** — 从输入通道向量读取的模数转换器数据

模拟信号进行 A/D 转换的结果。输出值的数据类型和范围取决于板卡的能力。

**数据类型：** `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Missed Ticks** — 错过的节拍计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖

当您选择 **Show "Missed Ticks" port** 时，此端口可见。

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

### **Sample time** — 模块的采样时间 `0.1`（默认）| double

输入一个以秒为单位的值，表示您希望模块执行和与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值，或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认）| integer

在 **Connected IO** 模式下，输入您的模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。它允许模型追赶，即使模型错过了一些节拍。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示“Missed Ticks”端口** — 将错过的 tick 数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的 tick 数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowMissedTicks` |

### **等待时让出 CPU** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时，为其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`YieldWhenWaiting` |

### **输入通道** — 选择模拟输入通道 `1`（默认）| 向量

输入一个通道向量，用于选择您在此板上使用的模拟输入通道。该向量可以是任何有效的 MATLAB® 向量形式。例如，要选择八个连续的模拟输入通道，请输入：

```
[1,2,3,4,5,6,7,8]
```

或

```
[1:8]
```

要选择前三个模拟输入通道，请输入：

```
[1,2,3]
```

#### 编程使用

|  |
| --- |
| **模块参数**：`Channels` |

### **输入范围** — 模拟输入的输入范围，取决于板卡

从列表中，为您在 **输入通道** 参数中输入的模拟输入通道选择输入范围。例如，如果板卡的输入范围为 `±5 V`，请选择 `-5 to 5 V`。

如果您希望不同的模拟通道使用不同的输入范围，请为每个不同的输入范围添加一个 I/O 模块。有效值取决于板卡的能力。

#### 编程使用

|  |
| --- |
| **模块参数**：`VoltRange` |

### **模块输出信号** — 模块返回的值类型 `Volts`（默认）| `Normalized bipolar` | `Normalized unipolar` | `Raw`

从列表中，选择以下选项之一：

- `Volts` — 返回等于模拟电压的值。
- `Normalized bipolar` — 无论输入电压范围如何，都返回 -`1` 到 `+1` 的满量程值。
- `Normalized unipolar` — 无论输入电压范围如何，都返回 `0` 到 `+1` 的满量程值。例如，`0` 伏到 `+5` 伏以及 `−5` 伏到 `+5` 伏的模拟输入范围都会转换为 `0` 到 `+1`。
- `Raw` — 返回从 `0` 到 `2n -1` 的值。例如，12 位 A/D 转换器返回从 `0` 到 `212 -1`（`0` 到 `4095`）的值。此方法的优点是返回值为整数，没有舍入误差。

#### 编程使用

|  |
| --- |
| **模块参数**：`RangeMode` |

### **输出数据类型** — 模块输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

从列表中，选择模块输出到模型的数据类型。有效值取决于板卡的能力。

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

在 R2024b 中，当您启用可选端口（例如 **显示“Missed Ticks”端口**）时，这些 Simulink Desktop Real-Time™ 模块端口会带标签显示。

## 描述

从一个或多个模拟输入通道读取

Analog Input 模块连接并从您的 Simulink® 模型中的特定模拟输入通道读取。将 Analog Input 模块添加到模型后，您可以输入其 I/O 驱动程序的参数。
