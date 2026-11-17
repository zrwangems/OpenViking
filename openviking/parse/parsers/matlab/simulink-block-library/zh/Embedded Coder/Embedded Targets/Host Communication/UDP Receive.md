---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
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

UDP 数据包，指定为数据向量，从 IP 网络端口接收。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Local IP port** — IP 端口号 25000（默认）| 范围 [1, 65535] 内的标量

指定用于接收 UDP 数据包的 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为低于 1024，请以 root 权限运行 MATLAB。例如，在 Linux 命令行中输入：

```
sudo matlab
```

### **Remote IP address ('0.0.0.0' to accept all)** — 接受数据包的来源 IP 地址 '0.0.0.0'（默认）| IP 地址

指定接受 UDP 数据包的来源 IP 地址。指定特定的 IP 地址以阻止来自其他地址的 UDP 数据包。要接受来自任何 IP 地址的数据包，请指定 `'0.0.0.0'`。

### **Receive buffer size (bytes)** — 接收 UDP 数据包的缓冲区大小 8192（默认）| 范围 [1, 67108864] 内的标量

指定接收 UDP 数据包的缓冲区大小（以字节为单位）。使缓冲区足够大，以避免缓冲区溢出导致的数据丢失。

### **Maximum length for Message** — 输出数据的最大长度 255（默认）| 标量

指定数据输出向量的最大长度（以向量元素为单位）。将此参数设置为等于或大于 UDP 数据包数据大小的值。系统会截断超过此长度的数据。

#### 参数依赖关系

如果禁用 **Output variable-size signal**，模块输出为此参数指定的长度。

### **Data type for Message** — 消息的数据类型 uint8（默认）| single | double | int8 | int16 | int32 | int64 | uint16 | uint32 | uint64 | boolean | fixed point | enumerated | bus

指定消息输出中向量元素的数据类型。将数据类型与用于创建 UDP 数据包的数据输入相匹配。

### **Message is complex** — 消息数据复数性 off（默认）| on

指定模块是否将消息作为复数数据接收。选择此参数以将消息作为复数数据接收。如果接收的消息为实数数据，则清除此参数。

### **Output variable-size signal** — 长度可变的消息输出 on（默认）| off

指定模型是否支持可变长度信号。如果模型支持可变长度信号，请选择此参数。在这种情况下：

- 输出向量的长度可变，取决于 UDP 数据包中的数据量。
- 模块从单个未标记的输出发出数据向量。

如果模型不支持可变长度信号，请清除此参数。在这种情况下：

- 模块发出固定长度的输出，其长度与 **Maximum length for Message** 指定的长度相同。
- 如果 UDP 数据包包含的数据少于固定长度输出，则差异部分包含无效数据。
- 模块从 **Message** 输出发出数据向量。
- 模块从 **Length** 输出发出有效数据的长度。
- **Data type for Length** 参数被启用。

#### 参数依赖关系

如果禁用此参数，模块发出的输出为 **Maximum length for Message** 指定的长度。

### **Blocking time (seconds)** — 等待 UDP 数据包的秒数 inf（默认）| 标量

对于每个采样，指定在将控制权返回给调度器之前等待 UDP 数据包的秒数。要无限期等待，请指定 `inf`。

**注意**

此参数仅适用于 Embedded Coder® UDP Receive 模块。

### **Sample time (seconds)** — 调用模块的频率 0.01（默认）| 标量

指定调度器调用 UDP Receive 模块的频率（以秒为单位）。输入大于零的值。在实时操作中，将此参数设置为较小的值可降低 UDP 消息丢失的可能性。

## 所属库

Embedded Coder / Embedded Targets / Host Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

接收 UDP 数据包

UDP Receive 模块从 IP 网络端口接收 UDP 数据包并将其保存到缓冲区。由于 UDP 传输协议的特性，接收方不保证能接收到您使用 UDP Send 模块发送的所有数据包。在每个采样中，模块将单个 UDP 数据包的内容作为数据向量输出。

模块接收 UDP 数据包的本地 IP 端口号在生成的代码中可调。此模块生成的代码依赖于预构建的 `.dll` 文件。您可以在 MATLAB® 环境之外运行此代码或重新部署它，但必须考虑额外的 `.dll` 文件。`packNGo` 函数创建一个 ZIP 文件，其中包含运行或重新构建此代码所需的各部分。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB (DSP System Toolbox)。
