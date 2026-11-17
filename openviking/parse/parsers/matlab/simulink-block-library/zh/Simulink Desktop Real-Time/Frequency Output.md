---
type: simulink-block
title: 'Frequency Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'frequencyoutput'
documentation_source_path: 'ref/frequencyoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Frequency Output

## 端口
```yaml
ports:
- name: Frequency
  summary: 输出波形的频率（可选）向量
  direction: input
  data_types: single | double | int8 | uint8 | int16 | uint16 | int32 | uint32
- name: Duty Cycle
  summary: 输出波形的占空比（可选）向量
  direction: input
  data_types: single | double | int8 | uint8 | int16 | uint16 | int32 | uint32
- name: Missed Ticks
  summary: 错过的节拍计数（可选）double
  direction: output
  data_types: double
```

### 输入

### **Frequency** — 输出波形的频率（可选）向量

波形发生器的频率设置。输入值的数据类型和范围取决于板卡的能力。

#### 依赖关系

当您将 **Output signal frequency source** 设置为 `external` 时，此端口可见。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Duty Cycle** — 输出波形的占空比（可选）向量

波形发生器的占空比设置。输入值的数据类型和范围取决于板卡的能力。

#### 依赖关系

当您将 **Output signal duty source** 设置为 `external` 时，此端口可见。

**数据类型：** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **Missed Ticks** — 错过的节拍计数（可选）double

在 **Connected IO** 模式下，返回您的模型落后于实时内核的定时器节拍数。当模型落后超过 **Maximum missed ticks** 时，软件会报告错误并停止仿真。

#### 依赖关系

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
  summary: 模块的采样时间 0.1（默认）| double
  group: ''
  block_parameter: SampleTime
- name: Maximum missed ticks
  summary: 模型可以落后于内核的定时器节拍数 10（默认）| 整数
  group: ''
  block_parameter: MaxMissedTicks
- name: Show “Missed Ticks” port
  summary: 将错过的节拍数发送到端口 Missed Ticks 'off'（默认）| 'on'
  group: ''
  block_parameter: ShowMissedTicks
- name: Yield CPU when waiting
  summary: 在内核等待硬件时让出 CPU 'off'（默认）| 'on'
  group: ''
  block_parameter: YieldWhenWaiting
- name: Output channels
  summary: 选择频率输出通道向量
  group: ''
  block_parameter: Channels
- name: Output signal frequency source
  summary: 指定输出频率（Hz）的来源 external（默认）| internal
  group: ''
  block_parameter: FrequencySource
- name: Frequency
  summary: 指定输出频率（Hz）标量
  group: ''
  block_parameter: Frequency
- name: Frequency initial value
  summary: 指定板在执行开始前生成的频率 标量
  group: ''
  block_parameter: Frequency
- name: Frequency final value
  summary: 指定执行结束后板卡生成的频率 标量
  group: ''
  block_parameter: FrequencyFinalValue
- name: Output signal duty source
  summary: 指定输出信号占空比的来源 internal（默认）| external
  group: ''
  block_parameter: DutySource
- name: Duty
  summary: 指定输出信号为高电平的时间 0.5（默认）| 0–1
  group: ''
  block_parameter: Duty
- name: Duty initial value
  summary: 指定执行开始前板卡的占空比 0–1
  group: ''
  block_parameter: Duty
- name: Duty final value
  summary: 指定执行结束后板卡的占空比 0–1
  group: ''
  block_parameter: DutyFinalValue
```

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件会显示支持的板卡制造商列表。当您选择某个制造商时，软件会显示该制造商可用的板卡列表。当您选择某个板卡时，软件会将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡驱动支持的更多信息，请参阅 Simulink Desktop Real-Time 的 Hardware Support。

#### 依赖关系

当您在已注册板卡列表中选择某个板卡时，**Delete current board** 和 **Board setup** 按钮变为可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **Delete current board** — 删除当前板卡（按钮）

要删除当前板卡，请点击此按钮。已注册板卡列表的初始选择将变为 `< no board selected >`。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

当您删除当前板卡后，**Delete current board** 和 **Board setup** 按钮将不再可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvName` |

### **Board setup** — 设置板卡（按钮）

要设置板卡，请点击此按钮。

将打开一个板卡特定的对话框以设置板卡。有关更多信息，请参阅板卡制造商文档。

#### 依赖关系

要激活此参数，请在已注册板卡列表中选择一个板卡。

要停用此参数，请点击 **Delete current board**。

#### 编程用法

|  |
| --- |
| **模块参数：** `DrvAddress` |
| **模块参数：** `DrvOptions` |

### **Sample time** — 模块的采样时间 `0.1`（默认）| double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以此采样率将您的模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值，或该值的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器节拍数 `10`（默认）| 整数

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是暂时的。即使模型错过了一些节拍，也允许模型追赶。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaxMissedTicks` |

### **Show “Missed Ticks” port** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowMissedTicks` |

### **Yield CPU when waiting** — 在内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时授予其他程序更多的 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程使用

|  |
| --- |
| **模块参数**：`YieldWhenWaiting` |

### **Output channels** — 选择频率输出通道向量

输入一个通道向量，用于选择您在此板上使用的频率输出通道。该向量可以是任何有效的 MATLAB® 向量形式。例如，要选择前八个数字输出通道，请输入：

```
[1,2,3,4,5,6,7,8]
```

或

```
[1:8]
```

#### 编程使用

|  |
| --- |
| **模块参数**：`Channels` |

### **Output signal frequency source** — 指定输出频率（Hz）的来源 `external`（默认）| `internal`

选择指定要输出的频率（以 Hz 为单位）的来源。**Output signal frequency source** 可以是以下之一：

- `internal` — 一个名为 **Frequency** 的可调参数指定频率。
- `external`（默认）— 一个信号指定频率。输入端口 `Frequency` 出现在模块上以接受该信号。

  您可以为 **Frequency initial value** 和 **Frequency final value** 指定附加设置。

#### 依赖关系

如果指定 `external`（默认），端口 `Frequency` 以及参数 **Frequency initial value** 和 **Frequency final value** 可见。

如果指定 `internal`，**Frequency** 将替换 **Frequency initial value**，并且 **Frequency final value** 被禁用。

#### 编程使用

|  |
| --- |
| **模块参数**：`FrequencySource` |

### **Frequency** — 指定输出频率（Hz）标量

此参数替换 **Frequency initial value**。

#### 依赖关系

要使此参数可见，请将 **Output signal frequency source** 设置为 `internal`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Frequency` |

### **Frequency initial value** — 指定板在执行开始前生成的频率 标量

可选地指定初始频率（以赫兹为单位）。当您连接到目标时，指定的频率生效。它持续到仿真开始，此时频率信号的值生效。您可以使用此参数指定初始条件并给它们时间稳定。如果没有值出现，连接到目标对频率没有影响。

#### 依赖关系

要使此参数可见，请将 **Output signal frequency source** 设置为 `external`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Frequency` |

### **Frequency final value** — 指定执行结束后板卡生成的频率 标量

可选地指定最终频率，单位为赫兹。当仿真完成时，指定的频率生效并无限期持续。与目标断开连接不会改变频率。你可以使用此参数在仿真后将连接的设备置于中性状态。如果未出现值，则仿真结束时生效的频率在此后持续。

#### 依赖

要使此参数可见，请将 **Output signal frequency source** 设置为 `external`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyFinalValue` |

### **Output signal duty source** — 指定输出信号占空比的来源 `internal`（默认）| `external`

指定决定占空比的来源。**Output signal duty source** 可以是以下之一：

- `internal`（默认）—
  一个名为 **Duty** 的可调参数指定占空比。
- `external` — 一个信号指定占空比。输入端口 `Duty Cycle` 出现在模块上以接受该信号。

#### 依赖

如果指定 `internal`（默认），则 **Duty** 可见。**Duty final value** 不可见。

如果指定 `external`，则端口 `Duty Cycle` 出现，参数 **Duty initial value** 替换 **Duty**，并且参数 **Duty final value** 可见。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DutySource` |

### **Duty** — 指定输出信号为高电平的时间 `0.5`（默认）| `0–1`

将占空比指定为从 `0` 到 `1`（含）的十进制小数。它决定输出信号值为高电平（`1`）的时间量。例如，占空比 `0.7` 指定输出在 70% 的时间内为高电平，在 30% 的时间内为低电平。

两个占空比值具有特殊意义：

- `0` — 无论当前生效的频率规格如何，输出信号持续为低电平（`0`）。
- `1` — 无论当前生效的频率规格如何，输出信号持续为高电平（`1`）。

#### 依赖

要使此参数可见，请将 **Output signal duty source** 设置为 `internal`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Duty` |

### **Duty initial value** — 指定执行开始前板卡的占空比 `0–1`

可选地指定初始占空比。当你连接到目标时，指定的占空比生效。它持续到仿真开始。如果未出现值，则连接到目标不会对占空比产生影响。你可以指定任意占空比。通常 **Duty initial value** 为 `0` 或 `1`，强制初始输出信号持续为低电平或高电平。指定 `0` 或 `1` 会覆盖任何 **Frequency initial value** 设置。

#### 依赖

要使此参数可见，请将 **Output signal duty source** 设置为 `external`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Duty` |

### **Duty final value** — 指定执行结束后板卡的占空比 `0–1`

可选地指定最终占空比。当仿真完成时，指定的占空比生效并无限期持续。与目标断开连接不会改变占空比。如果未出现值，则仿真结束时生效的占空比在此后无限期持续。你可以指定任意占空比。通常 **Duty final value** 为 `0` 或 `1`，强制最终输出信号持续为低电平或高电平。指定 `0` 或 `1` 会覆盖任何 **Frequency final value** 设置。

#### 依赖

要使此参数可见，请将 **Output signal duty source** 设置为 `external`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DutyFinalValue` |
## 所属库

Simulink Desktop Real-Time

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2007b 中引入**

### R2024b：更新了带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink® Desktop Real-Time™ 模块端口会显示标签。

## 描述

写入一个或多个频率或 PWM 输出通道

Frequency Output 模块生成脉冲宽度调制方波并输出到模拟输出。

方波在低电平（`0`）和高电平（`1`）之间交替，具有指定的频率和占空比。

您以赫兹（Hz）为单位指定频率。

您以从 `0` 到 `1`（含）的小数形式指定占空比。占空比决定输出信号值为高电平（`1`）的时间量。

将 Frequency Output 模块添加到模型后，双击 Frequency Output 模块以打开 Block Parameters: Frequency Output 对话框。
