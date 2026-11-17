---
type: simulink-block
title: 'CAN Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN Communication'
documentation_page: 'canconfiguration'
documentation_source_path: 'ug/canconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Configuration

## 端口

R2025b 中未记录。

## 参数

### **Device** — CAN 设备和通道列表选项

从列表中选择要使用的 CAN 设备及该设备上的通道。使用此设备发送和接收报文。设备驱动程序决定默认总线速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Device` |
| **类型：** 字符向量、字符串 |

### **Bus speed** — CAN 总线位速率整数

为所选设备设置 `BusSpeed` 属性，单位为每秒位数。默认总线速度是所选设备分配的默认值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BusSpeed` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Manually configure bit parameters** — 允许指定各个位参数 关（默认） | 开

**注意**

此选项仅适用于支持的供应商。

选中此复选框可允许手动指定位参数。位参数设置包括：**Synchronization jump width**、**Time segment 1**、**Time segment 2** 和 **Number of samples**。有关这些参数的详细信息，请参阅 Bit Timing。如果未选择此选项，设备将根据总线速度设置自动分配位参数。

**提示**

除非您的 CAN 连接有特定的时序要求，否则请使用默认位参数设置。

#### 程序化使用

|  |
| --- |
| **模块参数：** `EnableBitParameters` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |
|  |

### **Synchronization jump width** — 允许的最大时间调整量 整数

指定重新同步时位时间调整的最大限制。指定的值必须是一个正整数，表示位时间量子段的数量。如果未指定值，所选总线速度设置将决定默认值。要更改此值，请先选中 **Enable bit parameters manually** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SJW` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Time segment 1** — 采样点之前的时间量子数 整数

指定采样点之前的位时间量子数。指定的值必须是一个正整数。通常，调整此值时会相应地对 **Time segment 2** 进行反向调整，以使其总和保持不变。如果未指定值，所选总线速度设置将决定默认值。要更改此值，请先选中 **Enable bit parameters manually** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TSEG1` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Time segment 2** — 采样点之后的时间量子数 整数

指定采样点之后的位时间量子数。指定的值必须是一个正整数。通常，调整此值时会相应地对 **Time segment 1** 进行反向调整，以使其总和保持不变。如果未指定值，所选总线速度设置将决定默认值。要更改此值，请先选中 **Enable bit parameters manually** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TSEG2` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Number of samples** — 每位的采样数 整数

指定每位的采样数。指定的值必须是一个正整数。如果未指定值，所选总线速度设置将决定默认值。要更改此值，请先选中 **Enable bit parameters manually** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NSamples` |
| **类型：** 字符向量、字符串 |
| **值：** 整数 |

### **Verify bit parameter settings validity** — 检查设置的有效性

如果您已手动设置位参数设置，请点击此按钮以查看您的设置是否有效。该模块会运行检查，以确认您的总线速度和位参数值的组合是否构成 CAN 设备的有效组合。如果当前组合无效，验证将失败并显示错误消息。此按钮仅在选中 **Enable bit parameters manually** 复选框时处于活动状态。

#### 编程使用

无

### **Acknowledge mode** — 控制 CAN 总线上的通道活动 `Normal`（默认）| `Silent`

指定通道处于 `Normal` 还是 `Silent` 模式。默认情况下，**Acknowledge mode** 为 `Normal`。在此模式下，通道可以正常接收和发送消息，并在网络上执行其他任务，例如确认消息和创建错误帧。要在不影响网络状态或行为的情况下观察网络上的所有消息活动并执行分析，请选择 `Silent`。在 `Silent` 模式下，通道只能接收消息，不能发送。

#### 编程使用

|  |
| --- |
| **模块参数**：`AckMode` |
| **类型**：character vector, string |
| **值**：`'Normal'` | `'Silent'` |
| **默认值**：`'Normal'` |

## 所属库

Vehicle Network Toolbox / CAN Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

与 CAN Receive 和 CAN Transmit 模块一起使用时，CAN Configuration 模块支持代码生成，但可移植性有限，仅能在主机上运行。

## 版本历史

**在 R2009a 中引入**

## 描述

为指定的 CAN 设备配置参数

CAN Configuration 模块为 CAN 设备配置参数，您可以使用该设备发送和接收消息。

在配置其他 CAN 模块之前，请先指定 CAN 设备的配置。

对于模型中发送和接收消息的每个设备，使用一个 CAN Configuration 模块进行配置。如果您使用 CAN Receive 或 CAN Transmit 模块在设备上接收和发送消息，则您的模型需要为指定设备提供相应的 CAN Configuration 模块。

**注意**

您需要同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证才能使用此模块。

### 其他支持的功能

CAN Configuration 模块支持使用 Simulink 加速和快速加速模式。使用此功能，您可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅 Acceleration (Simulink)。
