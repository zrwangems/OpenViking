---
type: simulink-block
title: 'Other Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'otherinput'
documentation_source_path: 'ref/otherinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Other Input

## 端口

### 输出

### **Data** — 从输入通道向量读取的数据

输出值的数据类型和范围取决于板卡的能力。

**数据类型：** `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Missed Ticks** — 错过的 tick 计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器 tick 数。当模型落后超过 **最大错过 tick 数** 时，软件会报告错误并停止仿真。

#### 依赖关系

当您选中 **显示 “Missed Ticks” 端口** 时，此端口可见。

**数据类型：** `double`

## 参数

### **安装新板卡** — 注册板卡 `< no board selected >`（默认）

当您单击 **安装新板卡** 时，软件会显示支持的板卡制造商列表。当您选择某个制造商时，软件会显示该制造商提供的板卡列表。当您选择某个板卡时，软件会将该板卡添加到已注册板卡列表，并使该板卡成为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡的驱动程序支持详细信息，请参阅 Simulink Desktop Real-Time 的硬件支持。

#### 依赖关系

当您在已注册板卡列表中选择一个板卡时，**删除当前板卡** 和 **板卡设置** 按钮可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **删除当前板卡** — 删除当前板卡（按钮）

要删除当前板卡，请单击此按钮。已注册板卡列表的初始选择会变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡时，**删除当前板卡** 和 **板卡设置** 按钮将不再可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **板卡设置** — 设置板卡（按钮）

要设置板卡，请单击此按钮。

将打开一个特定于板卡的对话框以设置板卡。有关详细信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请单击 **删除当前板卡**。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **采样时间** — 模块的采样时间 `0.1`（默认）| double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块按此采样率将模型与实时时钟同步。

如果您使用固定步长求解器，请输入您在 **固定步长** 配置参数中输入的值，或该值的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大错过 tick 数** — 模型可以落后于内核的定时器 tick 数 `10`（默认）| integer

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器 tick 数。当模型落后该数量或更少的定时器 tick 时，软件假定该滞后是临时的。它允许模型追赶上来，即使模型错过了一些 tick。当模型落后超过该数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将错过的 tick 数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的 tick 数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时，为其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **输入通道** — 选择其他输入通道 `1`（默认）| vector

输入一个通道向量，用于选择您在此板卡上使用的其他输入通道。该向量可以是任何有效的 MATLAB® 向量形式。例如，要选择八个连续的模拟输入通道，请输入：

```
[1,2,3,4,5,6,7,8]
```

或

```
[1:8]
```

要选择前三个输入通道，请输入：

```
[1,2,3]
```

#### 编程用法

|  |
| --- |
| **模块参数：** `Channels` |

### **可选参数** — 指定驱动程序需要的可选参数 `0`（默认）| vector

有关所需值，请参阅制造商数据表。

#### 编程用法

|  |
| --- |
| **模块参数：** `OptParam` |

### **输出数据类型** — 模块输出的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

从列表中选择模块输出到模型的数据类型。有效值取决于板卡的能力。

#### 编程用法

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

### R2024b：对带端口名称的模块进行更新

在 R2024b 中，当您启用可选端口（例如 **显示 "Missed Ticks" 端口**）时，这些 Simulink Desktop Real-Time 模块端口会带标签显示。

## 描述

从一个或多个并非由特定模块处理的输入通道读取

Other Input 模块连接并读取需要专用驱动程序支持的硬件源，而其他 Simulink® Desktop Real-Time™ 输入模块不提供此类支持。Other Input 模块很少使用，并且仅用于少数驱动程序。有关详细信息，请参阅您打算使用的驱动程序的文档。

如果包括 Other Input 在内的所有可用模块都不能提供您所需的功能，您可以创建自己的 I/O 模块，以用于 Simulink Desktop Real-Time 应用程序。有关详细信息，请参阅在自定义 S-Function 中集成 C 代码。
