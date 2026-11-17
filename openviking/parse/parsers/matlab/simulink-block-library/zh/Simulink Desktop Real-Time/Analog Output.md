---
type: simulink-block
title: 'Analog Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'analogoutput'
documentation_source_path: 'ref/analogoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Output

## 端口

### 输入

### **Analog Data** — 要写入输出通道的数模转换器数据向量

作为 D/A 转换输入提供的源数据。输入值的数据类型和范围取决于板卡的能力。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **Missed Ticks** — 错过的节拍计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖关系

当您选择 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`

## 参数

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示支持的板卡制造商列表。当您选择某个制造商时，软件显示该制造商可用的板卡列表。当您选择某个板卡时，软件将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡的驱动程序支持的更多信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖关系

当您在已注册板卡列表中选择某个板卡时，**Delete current board** 和 **Board setup** 按钮可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择某个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮将不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框来设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择某个板卡。

要停用此参数，请点击 **Delete current board**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **Sample time** — 模块的采样时间 `0.1`（默认） | double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值，或该值的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认） | integer

在 **Connected IO** 模式下，输入您的模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。即使模型错过了一些节拍，它也允许模型赶上。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowMissedTicks` |

### **Yield CPU when waiting** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时，为其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`YieldWhenWaiting` |

### **Output channels** — 选择输出通道的通道向量 1（默认）| 向量

输入一个通道向量，用于选择您在此板上使用的模拟输出通道。该向量可以是任何有效的 MATLAB® 向量形式。例如，要选择前两个模拟输出通道，请输入：

```
[1,2]
```

或

```
[1:2]
```

#### 编程使用

|  |
| --- |
| **模块参数**：`Channels` |

### **Output range** — 为模拟输出选择输出范围 取决于板卡

从列表中，为在 **Output channels** 参数中输入的模拟输出通道选择输出范围。例如，如果板卡的输出范围为 `±5 V`，请选择 `-5 to 5 V`。

如果希望不同模拟通道的输出范围不同，请为每个不同的输出范围添加一个 I/O 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`VoltRange` |

### **Block input signal** — 发送到模块的值类型 `Volts`（默认）| `Normalized bipolar` | `Normalized unipolar` | `Raw`

从列表中，选择以下选项之一：

- `Volts` — 期望一个等于模拟输出电压的值。
- `Normalized bipolar` — 期望一个介于 `-1` 和 `+1` 之间的值，无论输出电压范围如何，该值都会转换为输出电压的完整范围。
- `Normalized unipolar` — 期望一个介于 `0` 和 `+1` 之间的值，无论输出电压范围如何，该值都会转换为输出电压的完整范围。例如，`0` 伏到 `+5` 伏以及 `−5` 伏到 `+5` 伏的模拟输出范围都会从 `0` 和 `+1` 之间的值进行转换。
- `Raw` — 期望一个从 `0` 到 `2n -1` 的值。例如，12 位 A/D 转换器期望一个介于 `0` 和 `212 -1`（`0` 到 `4095`）之间的值。此方法的优点是期望值是整数，没有舍入误差。

#### 编程使用

|  |
| --- |
| **模块参数**：`RangeMode` |

### **Initial value** — 输出通道的初始值 向量

为在 **Output channels** 参数中输入的每个模拟输出通道输入初始值。例如，如果您输入了 `[1,2]`，并且希望初始值为 `0` 伏，请输入 `[0,0]`。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialValue` |

### **Final value** — 输出通道的最终值 向量

为在 **Output channels** 参数中输入的每个模拟通道输入最终值。例如，如果您输入了 `[1,2]`，并且希望最终值为 `0` 伏，请输入 `[0,0]`。

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

**在 R2006a 之前引入**

### R2024b：更新为带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink Desktop Real-Time™ 模块端口会显示标签。

## 描述

写入一个或多个模拟输出通道

Analog Output 模块从您的 Simulink® 模型连接并写入特定的模拟输出通道。在将 Analog Output 模块添加到模型后，您可以输入其 I/O 驱动程序的参数。
