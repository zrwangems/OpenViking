---
type: simulink-block
title: 'Digital Input'
family: 'simulink-desktop-real-time'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Simulink Desktop Real-Time'
documentation_page: 'digitalinput'
documentation_source_path: '../sldrt/ref/digitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input

## 端口

### 输出

### **Digital Data** — 从输入通道向量读取的数字数据

输出值的数据类型和范围取决于板卡的功能。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Missed Ticks** — 遗漏 tick 计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器 tick 数。当模型落后超过 **最大遗漏 tick 数** 时，软件会报告错误并停止仿真。

#### 依赖关系

当您选择 **显示 “Missed Ticks” 端口** 时，此端口可见。

**数据类型：** `double`

## 参数

### **安装新板卡** — 注册板卡 `< no board selected >`（默认）

当您点击 **安装新板卡** 时，软件会显示受支持板卡的制造商列表。当您选择某个制造商时，软件会显示该制造商提供的板卡列表。当您选择某个板卡时，软件会将该板卡添加到已注册板卡列表，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡驱动程序支持的详细信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖关系

当您在已注册板卡列表中选择某个板卡时，**删除当前板卡** 和 **板卡设置** 按钮可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **删除当前板卡** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将更改为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择某个板卡。

当您删除当前板卡后，**删除当前板卡** 和 **板卡设置** 按钮将不再可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **板卡设置** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个特定于板卡的对话框，用于设置板卡。有关详细信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择某个板卡。

要停用此参数，请点击 **删除当前板卡**。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1`（默认）| double

请输入一个以 seconds 为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块将按此采样率使模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **固定步长** 配置参数中输入的值，或该值的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大遗漏 tick 数** — 模型可落后内核的定时器 tick 数 `10`（默认）| integer

在 **Connected IO** 模式下，请输入模型可落后实时内核的定时器 tick 数。当模型落后此数量或更少的定时器 tick 时，软件认为该滞后是临时的。它允许模型追赶，即使模型错过一些 tick。当模型落后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将遗漏 tick 数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将遗漏 tick 数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时让其他程序获得更多 CPU 时间。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **输入通道** — 选择数字输入通道 `1`（默认）| 向量

请输入一个通道向量，用于选择您在此板卡上使用的数字输入通道。该向量可以是任何有效的 MATLAB® 向量形式。例如，要选择前八个数字输入通道，请输入：

```
[1,2,3,4,5,6,7,8]
```

或

```
[1:8]
```

如果您想使用前四个数字输入线路，请输入：

```
[1,2,3,4]
```

如果您有一个 8-bit 数字通道，请输入 `[1]`。如果您有两个 8-bit 数字通道，请输入 `[1 9]`，然后从 `Channel mode` 列表中选择 `Byte`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Channels` |

### **通道模式** — 表示输入线路的模式 `Bit`（默认）| `Byte`

从列表中选择以下选项之一：

- `Bit` — 返回值 `0` 或 `1`。
- `Byte` — 将八条数字线路组合成一个数字通道。返回 `0–255` 的值。

#### 编程用法

|  |
| --- |
| **模块参数：** `BitMode` |

### **输出数据类型** — 模块输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

从列表中选择模块输出到模型的数据类型。有效值取决于板卡的功能。

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

在 R2024b 中，当您启用可选端口（例如 **显示 “Missed Ticks” 端口**）时，这些 Simulink Desktop Real-Time™ 模块端口会带标签显示。

## 描述

从一个或多个数字输入通道读取

Digital Input 模块连接到特定的数字线路或通道，并从这些线路或通道读取数据到您的 Simulink® 模型中。将 Digital Input 模块添加到模型后，您可以为其 I/O 驱动程序输入参数。
