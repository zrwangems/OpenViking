---
type: simulink-block
title: 'CAN FD Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN FD Communication'
documentation_page: 'canfdconfiguration'
documentation_source_path: 'ug/canfdconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN FD Configuration

## 端口

R2025b 中未记录。

## 参数

### **Device** — CAN 设备和通道列表选项

从列表中选择 CAN FD 设备以及该设备上要使用的通道。使用此设备发送和/或接收报文。设备驱动程序决定默认总线速度。

#### 编程使用

|  |
| --- |
| **模块参数：** `Device` |
| **类型：** 字符向量、字符串 |

### **Arbitration Bus speed** — 仲裁比特率数值

设置所选设备的仲裁总线速度，单位为比特每秒。默认速度由所选设备分配。

#### 编程使用

|  |
| --- |
| **模块参数：** `ArbitrationBusSpeed` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Data Bus speed** — 数据比特率数值

设置所选设备的数据总线速度，单位为比特每秒。默认速度由所选设备分配。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataBusSpeed` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Bus frequency** — PEAK-System 总线速率数值

（仅限 PEAK-System。）设置总线频率，单位为兆赫兹。

#### 编程使用

|  |
| --- |
| **模块参数：** `BusFrequency` |
| **类型：** 字符向量、字符串 |
| **值：** 数值 |

### **Arbitration/Data bit rate prescaler** — 比特率预分频器整数

（仅限 PEAK-System。）为仲裁比特率和数据比特率分别设置比特率预分频器值。

#### 编程使用

|  |
| --- |
| **模块参数：** `ArbitrationPrescaler`、`DataPrescaler` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

对于 Vector 和 PEAK-System 设备，接下来的三个参数各有两组可用，用于手动设置数据总线和仲裁总线速度的位参数。有关这些参数的详细信息，请参阅 Bit Timing。

### **Synchronization jump width** — 最大允许时间调整整数

指定重新同步时位时间调整的最大限制。指定的值必须为正整数，表示位时间量子段的数量。如果未指定值，则由所选总线速度设置决定默认值。

#### 编程使用

|  |
| --- |
| **模块参数：** `ArbitrationSJW`、`DataSJW` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Time segment 1** — 采样点之前的位时间量子数整数

指定采样点之前的位时间量子数。指定的值必须为正整数。通常，调整此值时会相应反向调整 **Time segment 2**，以使它们的和保持不变。如果未指定值，则由所选总线速度设置决定默认值。

#### 编程使用

|  |
| --- |
| **模块参数：** `ArbitrationTSEG1`、`DataTSEG1` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Time segment 2** — 采样点之后的位时间量子数整数

指定采样点之后的位时间量子数。指定的值必须为正整数。通常，调整此值时会相应反向调整 **Time segment 1**，以使它们的和保持不变。如果未指定值，则由所选总线速度设置决定默认值。

#### 编程使用

|  |
| --- |
| **模块参数：** `ArbitrationTSEG2`、`DataTSEG2` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Verify bit parameter settings validity** — 检查设置的有效性

如果您已更改位参数设置，请点击此按钮以查看您的设置是否有效。该模块会运行检查，以确定您的总线速度设置与位参数值的组合是否构成该设备的有效值。如果新的位参数值未构成有效组合，则验证失败并显示错误消息。

#### 程序化使用

无

### **确认模式** — 控制 CAN 总线上的通道活动 `Normal`（默认）| `Silent`

指定通道处于 Normal 模式还是 Silent 模式。默认情况下，**确认模式**为 `Normal`。在此模式下，通道正常接收和发送消息，并执行网络上的其他任务，例如确认消息和创建错误帧。要在不影响网络状态或行为的情况下观察网络上的所有消息活动并执行分析，请选择 `Silent`。在 Silent 模式下，您只能接收消息，不能发送。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AckMode` |
| **类型：** 字符向量、字符串 |
| **值：** `'Normal'` | `'Silent'` |
| **默认：** `'Normal'` |

## 所属库

Vehicle Network Toolbox / CAN FD Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当与 CAN FD Receive 和 CAN FD Transmit 模块一起使用时，CAN FD Configuration 模块支持代码生成，但可移植性有限，仅能在主机上运行。

## 版本历史

**在 R2018a 中引入**

## 描述

为指定的 CAN FD 设备配置参数

CAN FD Configuration 模块为 CAN FD 设备配置参数，您可以使用该设备发送和接收消息。

在配置其他 CAN FD 模块之前，请先指定 CAN FD 设备的配置。

在模型中，为每个发送和接收消息的设备使用一个 CAN FD Configuration 模块。如果您使用 CAN FD Receive 或 CAN FD Transmit 模块在设备上接收和发送消息，您的模型会检查指定设备是否存在对应的 CAN FD Configuration 模块。

**注意**

使用此模块需要同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

### 其他支持的功能

CAN FD Configuration 模块支持使用 Simulink 加速模式。使用此功能，您可以加速 Simulink 模型的执行。有关详细信息，请参阅 Acceleration (Simulink)。
