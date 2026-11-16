---
type: simulink-block
title: 'CAN Transmit'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'CAN and CAN FD Communication / Communication in Simulink / CAN'
documentation_page: 'cantransmit'
documentation_source_path: 'ug/cantransmit.html'
language: zh-CN
chinese_source: official
---

# CAN Transmit

## 端口

### 输入

### **CAN Msg** — 要传输的 CAN 报文 打包的 CAN 报文

由 CAN Pack 模块打包的 CAN 报文，以 CAN\_MESSAGE 或 Simulink 信号总线形式输入。

**数据类型:** `CAN_MESSAGE` | `bus`

## 参数

### **设备** — CAN 设备和通道 列表选项

选择用于将 CAN 报文传输到网络的 CAN 设备和通道。选项列表显示系统上安装的所有设备。它显示供应商名称、设备名称和通道 ID。默认值为系统上第一个可用的设备。

注意：使用 PEAK-System 设备时，多个使能子系统中的 CAN Transmit 模块可能会跳过某些报文。请尽可能将使能子系统替换为不同类型的条件子系统，例如 if-action、switch-case-action 或触发子系统；或重新设计您的模型，以便所有 CAN Transmit 模块都包含在一个使能子系统中。

#### 编程用法

|  |
| --- |
| **模块参数：**`Device` |
| **类型：**字符向量、字符串 |

### **传输选项：数据更改时** — 当数据发生变化时启用基于事件的传输 `'off'` (默认) | `'on'`

当启用基于事件的传输时，仅在检测到报文数据变化的那些时间步传输报文。当输入数据与给定报文 ID 的最近传输相匹配时，不会重新传输报文。

事件传输和周期性传输可以同时启用，共同工作。如果两者都没有选择，默认行为是在每个时间步传输当前输入。

#### 编程用法

|  |
| --- |
| **模块参数：**`EnableEventTransmit` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

### **传输选项：周期性** — 启用周期性传输 `'off'` (默认) | `'on'`

选择此选项可在配置的通道上以指定的报文周期定期传输报文。无论 Simulink 模型时间步大小（基础采样时间）或模块执行采样时间如何，周期均基于真实时间。这相当于 MATLAB 函数 `transmitPeriodic` 的功能。

周期性传输是非缓冲操作。出现一个时间周期时，仅该周期内 CAN Transmit 模块输入上的最后一条 CAN 报文或一组复路报文会被发送。

#### 编程用法

|  |
| --- |
| **模块参数：**`EnablePerioicTransmit` |
| **类型：**字符向量、字符串 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

### **传输选项：报文周期** — 报文传输速率周期 `1.000` (默认) | 正数值标量

以秒为单位指定报文传输周期。此值用于以指定的周期传输报文。默认情况下，此值为 `1.000` 秒。

#### 编程用法

|  |
| --- |
| **模块参数：**`MessagePeriod` |
| **类型：**字符向量、字符串 |
| **值：**双精度值 |
| **默认值：**`'1.000'` |

## 所属库

Vehicle Network Toolbox / CAN Communication

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

此模块生成的代码可移植性有限，只能在主机上运行。请参阅代码生成。

## 版本历史

**在 R2009a 中推出**

## 描述

将 CAN 报文传输到所选 CAN 设备

CAN Transmit 模块使用指定的 CAN 设备将报文传输到 CAN 网络。CAN Transmit 模块可以在给定时间步内传输单个报文或报文数组。要传输报文数组，请使用 Simulink® 模块库中的 mux (Simulink)（多路复用）模块。

**注意**

您需要 Vehicle Network Toolbox™ 和 Simulink 软件的许可证才能使用此模块。

CAN Transmit 模块有一个输入端口。此端口接受使用 CAN Pack 模块打包的 CAN 报文。它没有输出端口。

CAN 是 P2P 网络，因此在物理总线上发送报文时，必须至少存在一个其他节点，才能正确地确认报文。如果没有其他节点，传输会被视为错误帧而失败，随后设备将不断重试传输。

### 其他支持的功能

CAN Transmit 模块支持使用 Simulink 加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关此功能的详细信息，请参阅加速 (Simulink)。

CAN Transmit 模块支持使用代码生成和 packNGo 函数将所需的源代码和依赖共享库打包。

### 代码生成

Vehicle Network Toolbox 提供的 Simulink 模块支持您生成代码，使包含这些模块的模型可在加速、快速加速、外部和已部署模式下运行。

**使用 Simulink Coder 进行代码生成**

您可以将 Vehicle Network Toolbox、Simulink Coder™ 和 Embedded Coder® 软件结合使用，以在您用来实现模型的主机端生成代码。有关代码生成的详细信息，请参阅生成代码编译 (Simulink Coder)。

**共享库依赖关系**

这些模块生成的代码可移植性有限。它使用预编译的共享库（如 DLL）来支持特定类型设备的 I/O。使用此模块，您可以使用 Simulink Coder 支持的 `packNGo` 函数来设置和管理模型的编译信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖共享库打包到一个 zip 文件中进行部署。您不需要在目标系统上安装 MATLAB®，但需要 MATLAB 支持目标系统。

要设置 `packNGo`，请执行以下代码：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要编译的当前模型。编译模型会创建一个与模型同名的 zip 文件。您可以将此 zip 文件移至另一台机器，并在该机器中编译 zip 文件中的源代码以创建可独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码使用 C 和 C++ 编译器进行编译。有关详细信息，请参阅代码编译自定义 (Simulink Coder)。

**注意**

在 Linux® 平台上，您需要将用于解压缩库的文件夹添加到环境变量 `LD_LIBRARY_PATH`。
