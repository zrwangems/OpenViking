---
type: simulink-block
title: 'Servo Output'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'servooutput'
documentation_source_path: 'ref/servooutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Servo Output

## 端口

### 输入

### **Servo Data** — 要写入输出通道的舵机数据 double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean

舵机位置（角度）。轴位置的最小值和最大值随 **Block input signal**（单位）参数值而变化：

| 模块输入信号 | 最小舵机数据 | 最大舵机数据 |
| --- | --- | --- |
| Degrees（默认） | `0` | `180` |
| Radians | `0` | `pi` |
| Normalized bipolar | `-1` | `1` |
| Normalized unipolar | `0` | `1` |

**示例：**  90

**数据类型：** `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **Missed Ticks** — 错过的 tick 计数（可选） double

在 **Connected IO** 模式下，返回模型落后于实时内核的定时器 tick 数。当模型落后超过 **Maximum missed ticks** 时，软件报告错误并停止仿真。

#### 依赖

当您选中 **Show “Missed Ticks” port** 时，此端口可见。

**数据类型：** `double`

## 参数

### **Install new board** — 注册板卡 `< no board selected >`（默认）

当您点击 **Install new board** 时，软件显示支持的板卡制造商列表。当您选择某个制造商时，软件显示该制造商可用的板卡列表。当您选择某个板卡时，软件将该板卡添加到已注册板卡列表中，并将该板卡设为当前板卡。

默认情况下，已注册板卡列表中的初始选择为 `< no board selected >`。

有关 I/O 板卡的驱动程序支持的详细信息，请参阅 Hardware Support from Simulink Desktop Real-Time。

#### 依赖

当您在已注册板卡列表中选择某个板卡时，**Delete current board** 和 **Board setup** 按钮可用。

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

将打开一个板卡特定的对话框来设置板卡。有关详细信息，请参阅板卡制造商文档。

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

如果您使用的是定步长求解器，请输入您在 **Fixed step size** 配置参数中输入的值或该值的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |

### **Maximum missed ticks** — 模型可以落后于内核的定时器 tick 数 `10`（默认） | integer

在 **Connected IO** 模式下，输入模型可以落后于实时内核的定时器 tick 数。当模型落后此数量或更少的定时器 tick 时，软件假定该滞后是暂时的。它允许模型追赶，即使模型错过了一些 tick。当模型落后超过此数量时，软件报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示“Missed Ticks”端口** — 将错过的节拍数发送到端口 `Missed Ticks` `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可将错过的节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 内核等待硬件时让出 CPU `'off'`（默认）| `'on'`

在 **Connected IO** 模式下，选中此复选框可在内核等待硬件响应时，将更多 CPU 时间让给其他程序。

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

### **模块输入信号** — 模块输入信号的单位 `Degrees`（默认）| `Radians` | `Normalized bipolar` | `Normalized unipolar`

选择用于指定舵机位置的模块输入信号的单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RangeMode` |

### **最小脉冲持续时间** — 控制脉冲的持续时间 500e-6（默认）

选择对应于最小舵机角度的控制脉冲持续时间。由于并非所有舵机都相同，此参数允许您将输入信号校准到实际舵机角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MinPulseDuration` |

### **最大脉冲持续时间** — 控制脉冲的持续时间 2500e-6（默认）

选择对应于最大舵机角度的控制脉冲持续时间。由于并非所有舵机都相同，此参数允许您将输入信号校准到实际舵机角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MaxPulseDuration` |

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

**在 R2018b 中引入**

### R2024b：更新了带端口名称的模块

在 R2024b 中，当您启用可选端口（例如 **显示“Missed Ticks”端口**）时，这些 Simulink® Desktop Real-Time™ 模块端口会显示标签。

## 描述

写入标准舵机输出通道

Servo Output 模块设置标准舵机电机的轴位置。

要旋转舵机轴，请向模块输入发送值。

向模块输入发送超出范围的值与发送最小或最大输入值具有相同的效果。

模块输入继承上游模块的数据类型。
