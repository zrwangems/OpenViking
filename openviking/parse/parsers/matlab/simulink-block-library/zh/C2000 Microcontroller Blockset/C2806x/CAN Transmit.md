---
type: simulink-block
title: 'CAN Transmit'
family: 'vnt'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'CAN Communication'
documentation_page: 'cantransmit'
documentation_source_path: '../vnt/ug/cantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Transmit

## 端口
```yaml
ports:
- name: CAN Msg
  summary: 要传输的 CAN 消息，即打包的 CAN 消息
  direction: input
  data_types: CAN_MESSAGE | bus
```

### 输入

### **CAN Msg** — 要传输的 CAN 消息，即打包的 CAN 消息

由 CAN Pack 模块打包的 CAN 消息，以 CAN\_MESSAGE 或 Simulink 信号总线的形式输入。

**数据类型：** `CAN_MESSAGE` | `bus`
## 参数
```yaml
parameters:
- name: Device
  summary: CAN 设备和通道列表选项
  group: ''
  block_parameter: Device
  type: character vector, string
- name: 'Transmit Options: On data change'
  summary: 在数据更改时启用基于事件的传输 'off'（默认）| 'on'
  group: ''
  block_parameter: EnableEventTransmit
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: 'Transmit Options: Periodic'
  summary: 启用周期性传输 'off'（默认）| 'on'
  group: ''
  block_parameter: EnablePerioicTransmit
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: 'Transmit Options: Message period'
  summary: 报文传输周期 1.000（默认）| 正数值标量
  group: ''
  block_parameter: MessagePeriod
  type: character vector, string
  values: double
  default: '''1.000'''
```

### **Device** — CAN 设备和通道列表选项

选择用于向网络传输 CAN 消息的 CAN 设备和通道。选项列表显示系统上安装的所有设备，其中包含供应商名称、设备名称和通道 ID。默认为系统上的第一个可用设备。

注意：使用 PEAK-System 设备时，多个使能子系统中的 CAN Transmit 模块可能会跳过某些消息。如果可能，请将使能子系统替换为其他类型的条件子系统，例如 if-action、switch-case-action 或触发子系统；或者重新设计模型，使所有 CAN Transmit 模块都包含在单个使能子系统中。

#### 编程使用

|  |
| --- |
| **模块参数：** `Device` |
| **类型：** character vector, string |

### **Transmit Options: On data change** — 在数据更改时启用基于事件的传输 `'off'`（默认）| `'on'`

启用基于事件的传输后，仅在检测到消息数据发生更改的时间步传输消息。对于给定的消息 ID，当输入数据与最近一次传输的数据相同时，不会重新传输该消息。

基于事件的传输和周期性传输可以同时启用并协同工作。如果两者均未选中，则默认行为是在每个时间步传输当前输入。

#### 编程使用

|  |
| --- |
| **模块参数：** `EnableEventTransmit` |
| **类型：** character vector, string |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Transmit Options: Periodic** — 启用周期性传输 `'off'`（默认）| `'on'`

选择此选项可按指定的报文周期，在配置的通道上启用报文的周期性传输。该周期以实际时间为基准，不受 Simulink 模型时间步长（基础采样时间）或模块执行采样时间的影响。这相当于 MATLAB 函数 `transmitPeriodic`。

周期性传输是一种非缓冲操作。当周期时刻到来时，仅发送 CAN Transmit 模块输入端当前的最新一条 CAN 报文或最新一组多路复用报文。

#### 编程用法

|  |
| --- |
| **模块参数：** `EnablePerioicTransmit` |
| **类型：** character vector, string |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Transmit Options: Message period** — 报文传输周期 `1.000`（默认）| 正数值标量

指定报文传输周期，单位为 seconds。该值用于按指定周期传输报文。默认情况下，此值为 `1.000` seconds。

#### 编程用法

|  |
| --- |
| **模块参数：** `MessagePeriod` |
| **类型：** character vector, string |
| **值：** double |
| **默认值：** `'1.000'` |
## 所属库

Vehicle Network Toolbox / CAN Communication

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块生成的代码可移植性有限，只能在主机上运行。请参阅代码生成。

## 版本历史

**在 R2009a 中引入**

## 描述

将 CAN 报文传输到所选 CAN 设备

CAN Transmit 模块使用指定的 CAN 设备向 CAN 网络传输报文。CAN Transmit 模块可以在给定时间步内传输单条报文或报文数组。要传输报文数组，请使用 Simulink® 模块库中的 mux (Simulink)（多路复用）模块。

**注意**

使用此模块需要同时具有 Vehicle Network Toolbox™ 和 Simulink 软件的许可证。

CAN Transmit 模块有一个输入端口。此端口接受使用 CAN Pack 模块打包的 CAN 报文。该模块没有输出端口。

CAN 是对等网络，因此在物理总线上传输报文时，必须至少存在另一个节点才能正确确认该报文。如果没有另一个节点，传输将以错误帧的形式失败，并且设备会不断重试传输。

### 其他支持的功能

CAN Transmit 模块支持使用 Simulink 加速模式。使用此功能，可以加快 Simulink 模型的执行速度。有关此功能的更多信息，请参阅 Acceleration (Simulink)。

CAN Transmit 模块支持结合使用代码生成和 packNGo 函数，将所需的源代码和依赖的共享库归集在一起。

### 代码生成

Vehicle Network Toolbox 的 Simulink 模块支持您生成代码，使包含这些模块的模型能够在加速器、快速加速器、外部和部署模式下运行。

**使用 Simulink Coder 生成代码**

您可以结合使用 Vehicle Network Toolbox、Simulink Coder™ 和 Embedded Coder® 软件，在主机端生成可用于实现模型的代码。有关代码生成的详细信息，请参阅生成的代码编译 (Simulink Coder)。

**共享库依赖项**

该模块生成的代码可移植性有限。该模块使用预编译的共享库（如 DLL）来支持特定类型设备的 I/O。使用此模块时，您可以使用 Simulink Coder 支持的 `packNGo` 函数来设置和管理模型的构建信息。`packNGo` (Simulink Coder) 函数允许您将模型代码和依赖的共享库打包成 zip 文件，以便部署。目标系统上不需要安装 MATLAB®，但目标系统必须受 MATLAB 支持。

要设置 `packNGo`：

```
set_param(gcs,'PostCodeGenCommand','packNGo(buildInfo)');
```

在此示例中，`gcs` 是您要构建的当前模型。构建模型会创建一个与模型名称相同的 zip 文件。您可以将此 zip 文件移动到另一台计算机，并在该计算机上构建 zip 文件中的源代码，以创建一个可独立于 MATLAB 和 Simulink 运行的可执行文件。生成的代码支持使用 C 和 C++ 编译器进行编译。有关详细信息，请参阅代码编译自定义 (Simulink Coder)。

**注意**

在 Linux® 平台上，您需要将这些库的解压目录添加到环境变量 `LD_LIBRARY_PATH` 中。
