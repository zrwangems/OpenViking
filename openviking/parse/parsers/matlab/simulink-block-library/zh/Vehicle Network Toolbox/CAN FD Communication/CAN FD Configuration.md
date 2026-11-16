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
chinese_source: official
---

# CAN FD Configuration

## 端口

R2025b 官方文档未提供。

## 参数

### **设备** — CAN 设备和通道 列表选项

从列表中选择 CAN FD 设备和要在该设备上使用的通道。使用此设备传输和/或接收报文。设备驱动确定默认总线速度。

#### 编程用法

|  |
| --- |
| **模块参数：**`Device` |
| **类型：**字符向量、字符串 |

### **仲裁总线速度** — 仲裁比特率 数值

设置所选设备的仲裁总线速度，以每秒位数为单位。默认速度由所选设备分配。

#### 编程用法

|  |
| --- |
| **模块参数：**`ArbitrationBusSpeed` |
| **类型：**字符向量、字符串 |
| **值：**整数 |

### **数据总线速度** — 数据比特率 数值

设置所选设备的数据总线速度，以每秒位数为单位。默认速度由所选设备分配。

#### 编程用法

|  |
| --- |
| **模块参数：**`DataBusSpeed` |
| **类型：**字符向量、字符串 |
| **值：**整数 |

### **总线频率** — PEAK-System 总线速率 数值

（仅限 PEAK-System。）设置总线频率，以兆赫为单位。

#### 编程用法

|  |
| --- |
| **模块参数：**`BusFrequency` |
| **类型：**字符向量、字符串 |
| **值：**数值 |

### **仲裁/数据比特率预分频器** — 比特率预分频器 整数

（仅限 PEAK-System。）为仲裁和数据比特率设置单独的比特率预分频器值。

#### 编程用法

|  |
| --- |
| **模块参数：**`ArbitrationPrescaler`、`DataPrescaler` |
| **类型：**字符向量、字符串 |
| **值：**整数 |

对于 Vector 和 PEAK-System 设备，接下来的三个参数有两组设置，分别用于对数据总线速度和仲裁总线速度的位参数进行手动设置。有关这些参数的详细信息，请参阅 位定时。

### **同步跳转宽度** — 允许的最大时间调整量 整数

指定重新同步时位时间调整量的最大限制。指定的值必须为正整数，表示位时间量子段的数量。如果未指定值，则由所选的总线速度设置来确定默认值。

#### 编程用法

|  |
| --- |
| **模块参数：**`ArbitrationSJW`、`DataSJW` |
| **类型：**字符向量、字符串 |
| **值：**整数 |

### **时间段 1** — 采样前的时间量子数量 整数

指定采样点之前的位时间量子数量。指定的值必须是正整数。通常，此值的调整是通过对**时间段 2** 进行对应的反向调整来实现的，因此其总和保持不变。如果未指定值，则由所选的总线速度设置来确定默认值。

#### 编程用法

|  |
| --- |
| **模块参数：**`ArbitrationTSEG1`、`DataTSEG1` |
| **类型：**字符向量、字符串 |
| **值：**整数 |

### **时间段 2** — 采样后的时间量子数量 整数

指定采样点后的位时间量子数量。指定的值必须是正整数。通常，此值的调整是通过对**时间段 1** 进行对应的反向调整来实现的，因此其总和保持不变。如果未指定值，则由所选的总线速度设置来确定默认值。

#### 编程用法

|  |
| --- |
| **模块参数：**`ArbitrationTSEG2`、`DataTSEG2` |
| **类型：**字符向量、字符串 |
| **值：**整数 |

### **验证位参数设置的有效性** — 检查设置的有效性

如果您更改了位参数设置，点击此按钮可查看您的设置是否有效。该模块会运行检查，以查看总线速度设置和位参数值的组合是否形成了设备的有效值。如果新的位参数值未形成有效组合，则验证将失败并显示错误报文。

#### 编程用法

无

### **确认模式** — 控制 CAN 总线上的通道活动 `Normal` (默认) | `Silent`

指定通道是处于普通模式 (Normal) 还是静默模式 (Silent)。默认情况下，**确认模式**为 `Normal`。在此模式下，通道既可以正常接收和传输报文，也可以在网络上执行其他任务，例如确认报文和创建错误帧。要观察网络上的所有报文活动并执行分析，而不影响网络状态或行为，请选择 `Silent`。在 Silent 模式下，您只能接收报文而不能传输报文。

#### 编程用法

|  |
| --- |
| **模块参数：**`AckMode` |
| **类型：**字符向量、字符串 |
| **值：**`'Normal'` | `'Silent'` |
| **默认值：**`'Normal'` |

## 所属库

Vehicle Network Toolbox / CAN FD Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

当与 CAN FD Receive 和 CAN FD Transmit 模块结合使用时，CAN FD Configuration 模块支持代码生成，但可移植性有限，只能在主机上运行。

## 版本历史

**在 R2018a 中推出**

## 描述

配置指定 CAN FD 设备的参数

CAN FD Configuration 模块配置可用于传输和接收报文的 CAN FD 设备的参数。

在配置其他 CAN FD 模块之前，请先指定 CAN FD 设备的配置。

使用一个 CAN FD Configuration 模块对模型中发送和接收报文的每个设备进行配置。如果使用 CAN FD Receive 或 CAN FD Transmit 模块来接收和发送设备上的报文，则模型会检查对于指定设备是否存在对应的 CAN FD Configuration 模块。

**注意**

您需要 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证才能使用此模块。

### 其他支持的功能

CAN FD Configuration 模块支持使用 Simulink 加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关详细信息，请参阅加速 (Simulink)。
