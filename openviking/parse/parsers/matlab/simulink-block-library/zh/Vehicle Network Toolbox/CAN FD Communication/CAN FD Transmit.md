---
type: simulink-block
title: 'CAN FD Transmit'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN FD Communication'
documentation_page: 'canfdtransmit'
documentation_source_path: 'ug/canfdtransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN FD Transmit

## 端口

### 输入

### **CAN Msg** — 要发送的 CAN FD 消息 `CAN_FD_MESSAGE_BUS`

要发送的 CAN FD 消息，由 CAN FD Pack 模块打包，作为类型为 `CAN_FD_MESSAGE_BUS` 的 Simulink 信号总线输入。

**数据类型：** `CAN_FD_MESSAGE_BUS`

## 参数

**提示**

在配置 CAN FD Transmit 模块参数之前，请先在模型中配置 CAN FD Configuration 模块。

### **Device** — CAN FD 设备和通道列表选项

选择用于向网络发送 CAN FD 消息的 CAN 设备和通道。此列表显示系统中安装的所有设备。它显示供应商名称、设备名称和通道 ID。默认值为系统上第一个可用的设备。

注意：使用 PEAK-System 设备时，多个已启用子系统中的 CAN FD Transmit 模块可能会跳过某些消息。如果可能，请将已启用子系统替换为不同类型的条件子系统，例如 if-action、switch-case-action 或 triggered 子系统；或者重新设计模型，使所有 CAN FD Transmit 模块都包含在单个已启用子系统中。

#### 编程使用

|  |
| --- |
| **模块参数：** `Device` |
| **类型：** 字符向量、字符串 |

以下参数定义发送选项。

### **On data change** — 数据变化时启用基于事件的发送 `off`（默认）| `on`

启用基于事件的发送后，仅在检测到消息数据发生变化的时间步发送消息。当输入数据与给定消息 ID 的最近一次发送匹配时，不会重新发送该消息。

事件发送和周期性发送可以同时启用并协同工作。如果两者均未选择，则默认行为是在每个时间步发送当前输入。

#### 编程使用

|  |
| --- |
| **模块参数：** `EnableEventTransmit` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Periodic** — 启用周期性发送 `off`（默认）| `on`

选择此选项可按照指定的消息周期在配置的通道上启用消息的周期性发送。该周期参考实时时间，与 Simulink 模型时间步大小（基本采样时间）或模块执行采样时间无关。这等效于 MATLAB 函数 `transmitPeriodic`。

周期性发送是非缓冲操作。当时间周期到达时，仅发送 CAN FD Transmit 模块输入端存在的最后一条 CAN 消息或最后一组消息。

#### 编程使用

|  |
| --- |
| **模块参数：** `EnablePerioicTransmit` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Transmit Options: Message period (in seconds)** — 消息发送速率周期 `1.000`（默认）| 正数值标量

指定以秒为单位的周期。此值用于在指定周期内发送消息。默认情况下，此值为 `1.000` 秒。

#### 编程使用

|  |
| --- |
| **模块参数：** `MessagePeriod` |
| **类型：** 字符向量、字符串 |
| **值：** double |
| **默认：** `'1.000'` |

## 所属库

Vehicle Network Toolbox / CAN FD Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块生成的代码可移植性有限，仅在主机计算机上运行。请参阅代码生成。

## 版本历史

**在 R2018a 中引入**

## 描述

将 CAN FD 报文发送到选定的 CAN FD 设备

CAN FD Transmit 模块使用指定的 CAN 设备向 CAN 网络发送报文。CAN FD Transmit 模块可以在给定的时间步内发送单条报文或报文数组。要从信号总线发送报文数组，请使用 Bus Creator (Simulink) 或 Vector Concatenate, Matrix Concatenate (Simulink) 模块。

**注意**

使用此模块需要同时拥有 Vehicle Network Toolbox™ 和 Simulink® 软件的许可证。

CAN FD Transmit 模块有一个输入端口。此端口接受使用 CAN FD Pack 模块打包的 CAN 报文。它没有输出端口。

CAN 是一种对等网络，因此在物理总线上发送报文时，至少需要存在另一个节点才能正确确认该报文。如果没有其他节点，发送将作为错误帧失败，并且设备将持续重试发送。

### 其他支持的功能

CAN FD Transmit 模块支持使用 Simulink 加速器模式。使用此功能，您可以加速 Simulink 模型的执行。有关详细信息，请参阅 Acceleration (Simulink)。

CAN FD Transmit 模块支持结合使用代码生成和 packNGo 函数，以将所需的源代码和依赖的共享库打包。

### 代码生成

Vehicle Network Toolbox Simulink 模块允许您生成代码，使包含这些模块的模型能够在加速器、快速加速器、外部和部署模式下运行。

**使用 Simulink Coder 进行代码生成**

您可以结合使用 Vehicle Network Toolbox、Simulink Coder™ 和 Embedded Coder® 软件在主机端生成代码，用于实现您的模型。有关代码生成的详细信息，请参阅 Generated Code Compilation (Simulink Coder)。

**共享库依赖项**

该模块生成的代码可移植性有限。该模块使用预编译的共享库（如 DLL）来支持特定类型设备的 I/O。使用此模块，您可以使用 Simulink Coder 支持的 `packNGo` 函数来设置和管理模型的构建信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖的共享库打包到一个 zip 文件中进行部署。目标系统上不需要安装 MATLAB®，但目标系统需要受 MATLAB 支持。

要设置 `packNGo`：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要构建的当前模型。构建模型会创建一个与模型名称相同的 zip 文件。您可以将此 zip 文件移动到另一台机器上，并在那里构建 zip 文件中的源代码，以创建一个可以独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码可使用 C 和 C++ 编译器编译。有关详细信息，请参阅 Code Compilation Customization (Simulink Coder)。

**注意**

在 Linux® 平台上，您需要将解压库的文件夹添加到环境变量 `LD_LIBRARY_PATH` 中。
