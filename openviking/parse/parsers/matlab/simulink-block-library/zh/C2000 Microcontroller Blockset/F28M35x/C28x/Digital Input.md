---
type: simulink-block
title: 'Digital Input'
family: 'sldrt'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'digitalinput'
documentation_source_path: '../sldrt/ref/digitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input

## 端口

### 输出

### **Digital Data** — 从输入通道读取的数字数据 向量

输出值的数据类型和范围取决于板卡的能力。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Missed Ticks** — 错过的节拍计数（可选） double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖

当您选中 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`

## 参数

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

将打开一个板卡特定的对话框以设置板卡。有关更多信息，请参阅板卡制造商文档。

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

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认） | integer

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是临时的。它允许模型追赶，即使模型错过了一些节拍。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认） | `'on'`

在 **Connected IO** 模式下，选中此复选框以将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowMissedTicks` |

### **Yield CPU when waiting** — 在内核等待硬件时让出 CPU `'off'`（默认） | `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时授予其他程序更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`YieldWhenWaiting` |

### **Input channels** — 选择数字输入通道 `1`（默认） | vector

输入一个通道向量，用于选择您在此板卡上使用的数字输入通道。该向量可以是任何有效的 MATLAB® 向量形式。例如，要选择前八个数字输入通道，请输入：

```
[1,2,3,4,5,6,7,8]
```

或

```
[1:8]
```

如果您想使用前四条数字输入线路，请输入：

```
[1,2,3,4]
```

如果您有一个 8 位数字通道，请输入 `[1]`。如果您有两个 8 位数字通道，请输入 `[1 9]`，然后从 `Channel mode` 列表中选择 `Byte`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Channels` |

### **Channel mode** — 表示输入线路的模式 `Bit`（默认） | `Byte`

从列表中选择以下选项之一：

- `Bit` — 返回 `0` 或 `1` 的值。
- `Byte` — 将八条数字线路组合为一个数字通道。返回 `0–255` 的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`BitMode` |

### **Output data type** — 模块输出的数据类型 `double`（默认） | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

从列表中选择模块输出到模型的数据类型。有效值取决于板卡的能力。

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

### R2024b: 更新了带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink Desktop Real-Time™ 模块端口会显示标签。

## 描述

从一个或多个数字输入通道读取

Digital Input 模块连接并读取特定的数字线路或通道到您的 Simulink® 模型中。在将 Digital Input 模块添加到模型后，您可以输入其 I/O 驱动程序的参数。
