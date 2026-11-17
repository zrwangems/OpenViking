---
type: simulink-block
title: 'Other Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'otheroutput'
documentation_source_path: 'ref/otheroutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Other Output

## 端口
```yaml
ports:
- name: Data
  summary: 要写入输出通道的数据向量
  direction: input
  data_types: single | double | int8 | uint8 | int16 | uint16 | int32 | uint32
- name: Missed Ticks
  summary: 错过的节拍计数（可选）double
  direction: output
  data_types: double
```

### 输入

### **Data** — 要写入输出通道的数据向量

输入值的数据类型和范围取决于板卡的能力。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **Missed Ticks** — 错过的节拍计数（可选）double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件会报告错误并停止仿真。

#### 依赖

当您选中 **Show “Missed Ticks” port** 时，此端口可见。

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
  summary: 模型可以落后于内核的定时器节拍数 10（默认） | 整数
  group: ''
  block_parameter: MaxMissedTicks
- name: Show “Missed Ticks” port
  summary: 将错过的节拍数发送到端口 Missed Ticks 'off'（默认） | 'on'
  group: ''
  block_parameter: ShowMissedTicks
- name: 等待时让出 CPU
  summary: 内核等待硬件时让出 CPU 'off'（默认）| 'on'
  group: ''
  block_parameter: YieldWhenWaiting
- name: 输出通道
  summary: 选择其他输出通道的通道向量 1（默认）| 向量
  group: ''
  block_parameter: Channels
- name: 可选参数
  summary: 指定驱动程序所需的自定义参数 0（默认）| 向量
  group: ''
  block_parameter: OptParam
- name: 初始值
  summary: 指定通道在执行开始前生成的值 向量
  group: ''
  block_parameter: InitialValue
- name: 最终值
  summary: 指定通道在执行结束后生成的值 向量
  group: ''
  block_parameter: FinalValue
```

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件会显示支持的板卡制造商列表。当您选择某个制造商时，软件会显示该制造商可用的板卡列表。当您选择某个板卡时，软件会将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

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

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮将不再可用。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框来设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖

要激活此参数，请在已注册板卡列表中选择一个板卡。

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

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认） | 整数

在 **Connected IO** 模式下，输入您的模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。它允许模型追赶上来，即使模型错过了一些节拍。当模型落后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认） | `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时，为其他程序授予更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件会忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **输出通道** — 选择其他输出通道的通道向量 `1`（默认）| 向量

输入一个通道向量，用于选择您在此板上使用的其他输出通道。该向量可以是任何有效的 MATLAB® 向量形式。例如，要选择前两个其他输出通道，请输入：

```
[1,2]
```

或

```
[1:2]
```

#### 程序化使用

|  |
| --- |
| **模块参数：** `Channels` |

### **可选参数** — 指定驱动程序所需的自定义参数 `0`（默认）| 向量

有关所需的值，请参阅制造商数据手册。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OptParam` |

### **初始值** — 指定通道在执行开始前生成的值 向量

为在 **输出通道** 框中输入的每个输出通道输入初始值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialValue` |

### **最终值** — 指定通道在执行结束后生成的值 向量

为在 **输出通道** 框中输入的每个输出通道输入最终值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FinalValue` |
## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前推出**

### R2024b：更新了带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink Desktop Real-Time 模块端口会显示标签。

## 描述

写入一个或多个不由特定模块处理的输出通道

Other Output 模块连接到需要专用驱动程序支持的硬件接收器，并向其写入数据，而其他 Simulink® Desktop Real-Time™ 输出模块不提供此类支持。Other Output 模块很少使用，仅适用于少数驱动程序。有关详细信息，请参阅您打算使用的驱动程序的文档。

如果所有可用模块（包括 Other Output）都无法满足您的需求，您可以创建自己的 I/O 模块，以便与 Simulink Desktop Real-Time 应用程序配合使用。有关详细信息，请参阅 Integrate C Code in Custom S-Functions。
