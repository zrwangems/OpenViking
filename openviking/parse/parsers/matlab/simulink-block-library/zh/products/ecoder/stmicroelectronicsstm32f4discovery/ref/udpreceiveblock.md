---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Network'
documentation_page: 'udpreceiveblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/udpreceiveblock.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Data** — 从 UDP 主机接收的输出 UDP 数据包向量

在每个采样时间，端口将接收到的数据包内容输出为数据向量，其大小为您在 **数据大小 (N)** 参数中指定的大小。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Status** — 确定在给定时步是否接收到请求的数据（标量）

在每个采样时间，当接收到的数据长度大于或等于 **数据大小 (N)** 参数中指定的长度时，端口输出 `0`。值 `0` 表示在给定时步接收到了请求的数据。否则，它输出一个非零值，表示没有新数据可用。

有关更多信息，请参阅接收 UDP 数据包。

#### 依赖关系

要启用此端口，请选择 **输出错误状态** 参数。

**数据类型：** `uint16`

## 参数

### **远程 IP 地址（0.0.0.0 表示接受所有）** — 模块从其接收 UDP 数据包的 IP 地址 `0.0.0.0`（默认）

指定模块从其接收数据包的远程主机的 IP 地址。要从所有发送主机接收数据包，请指定 `0.0.0.0`。

### **本地 IP 端口** — 接收 UDP 主机上的 IP 端口 `25010`（默认） | `Any integer between 1 and 65535`

指定您要从中接收数据包的应用程序的端口号。将本地端口号与发送主机的远程端口号匹配。

### **等待直到接收到数据** — 等待直到请求的数据可用 `off`（默认） | `on`

- `on` — 选择此参数时，读操作在 **阻塞模式** 下运行。读操作会被阻塞，直到请求的数据可用。如果数据可用，`Data` 端口输出数据。如果数据不可用，`Data` 端口等待数据。

  如果目标硬件在计划开始下一次读操作时仍在等待数据可用，则会发生任务超限。

  要修复超限：

  - 通过 **采样时间** 参数增大时间步长。
  - 通过 **数据大小 (N)** 参数减少请求的数据长度。
- `off` — 清除此参数时，读操作在 **非阻塞模式** 下运行。读取数据时，如果数据不可用，`Data` 端口包含上一个时间步接收到的数据包。在此模式下，模块不会等待请求的数据可用。

### **数据类型** — UDP 数据包中元素的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择模块从发送主机接收元素时使用的数据类型。每个元素的大小取决于其数据类型。

### **数据大小 (N)** — 每个 UDP 数据包中的数据元素数量 `1`（默认） | `scalar`

指定您要在每个数据包中接收的元素数量。数据大小必须是标量值。

### **输出错误状态** — 在数据传输期间显示错误状态的选项 `off`（默认） | `on`

选择此参数以在数据传输期间显示错误状态。

当您选择输出错误状态参数时，模块会配置一个输出端口。该模块上的端口标记为 Status，表示模块在输出端口输出读操作的状态。

### **采样时间** — 此模块从发送 UDP 主机读取数据包的频率 `-1`（默认）

当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

从 UDP 主机接收 UDP 数据包

UDP Receive 模块从 UDP 主机接收 UDP 数据包。将该模块用于无状态和无连接的数据传输。

在每个采样中，模块将 UDP 数据包的内容输出为 **(Nx1)** 数组。

模块通过 **本地 IP 端口** 参数中指定的端口号，从 **远程 IP 地址（0.0.0.0 表示接受所有）** 参数中指定的 IP 地址接收数据包。要从所有发送主机接收数据包，请将远程 IP 地址指定为 `0.0.0.0`。将 **本地 IP 端口** 参数中指定的端口号与发送主机的远程端口号匹配。

您可以选择以阻塞或非阻塞模式接收 UDP 数据包。

**注意**

- 确保在 STM32CubeMX 项目中配置以太网选项。有关更多信息，请参阅《在 STM32CubeMX 中为基于 STM32 处理器的板配置以太网选项》。
- 如果您在使用 UDP 与计算机通信时遇到问题，请检查是否有防病毒或防火墙软件阻止 UDP 流量。如果是这样，请尝试配置该软件，以允许特定 IP 端口号的流量。
