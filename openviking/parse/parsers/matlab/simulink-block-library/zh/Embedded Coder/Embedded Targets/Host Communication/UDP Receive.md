---
type: simulink-block
title: 'UDP Receive'
family: 'embedded-targets'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Embedded Targets / Host Communication'
documentation_page: 'udpreceive'
documentation_source_path: 'ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Port\_1** — UDP 数据包向量

UDP 数据包，指定为从 IP 网络端口接收的数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **本地 IP 端口** — IP 端口号 25000（默认）| [1, 65535] 范围内的标量

指定接收 UDP 数据包所用的 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为低于 1024，请以 root 权限运行 MATLAB。例如，在 Linux 命令行中，输入：

    sudo matlab

### **远程 IP 地址（'0.0.0.0' 表示接受所有）** — 接受数据包的 IP 地址 '0.0.0.0'（默认）| IP 地址

指定接受 UDP 数据包的 IP 地址。指定特定 IP 地址以阻止来自其他地址的 UDP 数据包。要接受来自任何 IP 地址的数据包，请指定 `'0.0.0.0'`。

### **接收缓冲区大小 (bytes)** — 接收 UDP 数据包的缓冲区大小 8192（默认）| [1, 67108864] 范围内的标量

指定接收 UDP 数据包的缓冲区大小，以 bytes 为单位。使缓冲区足够大，以避免缓冲区溢出导致的数据丢失。

### **Message 的最大长度** — 输出数据的最大长度 255（默认）| 标量

指定数据输出向量的最大长度，以向量元素为单位。将此参数设置为等于或大于 UDP 数据包数据大小的值。系统会截断超过此长度的数据。

#### 参数依赖关系

如果禁用 **输出可变大小信号**，则模块输出的长度由该参数指定。

### **Message 的数据类型** — 消息的数据类型 uint8（默认）| single | double | int8 | int16 | int32 | int64 | uint16 | uint32 | uint64 | boolean | fixed point | enumerated | bus

指定消息输出中向量元素的数据类型。将数据类型与用于创建 UDP 数据包的数据输入匹配。

### **Message 为复数** — Message 数据的复数性 off（默认）| on

指定模块是否将消息作为复数数据接收。选择此参数以将消息作为复数数据接收。如果接收的消息是实数数据，则清除此参数。

### **输出可变大小信号** — Message 输出长度可变 on（默认）| off

指定模型是否支持长度可变的信号。如果模型支持长度可变的信号，则选择此参数。在这种情况下：

- 输出向量的长度可变，取决于 UDP 数据包中的数据量。
- 模块从单个未标记的输出端口输出数据向量。

如果模型不支持长度可变的信号，则清除此参数。在这种情况下：

- 模块输出固定长度输出，其长度与 **Message 的最大长度** 指定的长度相同。
- 如果 UDP 数据包包含的数据少于固定长度输出，则差值部分包含无效数据。
- 模块从 **Message** 输出端口输出数据向量。
- 模块从 **Length** 输出端口输出有效数据的长度。
- **Length 的数据类型** 参数启用。

#### 参数依赖关系

如果禁用此参数，模块输出的长度由 **Message 的最大长度** 指定。

### **阻塞时间 (seconds)** — 等待 UDP 数据包的秒数 inf（默认）| 标量

对于每个采样，指定在将控制权返回给调度器之前等待 UDP 数据包的秒数。要无限期等待，请指定 `inf`。

**注意**

此参数仅适用于 Embedded Coder® UDP Receive 模块。

### **采样时间 (seconds)** — 调用模块的频率 0.01（默认）| 标量

指定调度器调用 UDP Receive 模块的频率，以 seconds 为单位。输入大于零的值。在实时操作中，将此参数设置为较小的值可降低丢弃 UDP 消息的可能性。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

接收 UDP 数据包

UDP Receive 模块从 IP 网络端口接收 UDP 数据包，并将其保存到其缓冲区。由于 UDP 传输协议的性质，接收方不能保证接收到你使用 UDP Send 模块发送的所有数据包。在每个采样中，模块将单个 UDP 数据包的内容作为数据向量输出。

模块接收 UDP 数据包所用的本地 IP 端口号在生成的代码中可调。此模块生成的代码依赖预构建的 `.dll` 文件。你可以在 MATLAB® 环境之外运行此代码或重新部署它，但必须考虑额外的 `.dll` 文件。`packNGo` 函数会创建一个 ZIP 文件，其中包含运行或重新构建此代码所需的各部分。有关更多详细信息，请参阅如何在 MATLAB 外部运行生成的可执行文件 (DSP System Toolbox)。
