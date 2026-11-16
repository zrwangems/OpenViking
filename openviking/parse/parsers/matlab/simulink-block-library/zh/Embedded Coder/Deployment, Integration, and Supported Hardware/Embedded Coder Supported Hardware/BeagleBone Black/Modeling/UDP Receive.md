---
type: simulink-block
title: 'UDP Receive'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'udpreceive'
documentation_source_path: 'beaglebone/ref/udpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# UDP Receive

## 端口

### 输出

### **Message** — 接收的数据向量

UDP Receive 模块接收的数据，以在 **Data type for Message** 中指定的数据类型的一维向量返回。如果选择 **Message is complex**，则该模块将接收到的消息视为复数数据。

如果数据包在传输过程中被丢弃，且接收方未收到该数据包，则接收到的数据输出为空。

在清除 **Output variable-size signal** 参数之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
**复数支持：** Yes

### **Length** — 数据包长度标量

接收到的数据包长度，以标量返回。此值由 **Maximum length for Message** 参数的值确定。

#### 依赖关系

- 要启用此端口，请清除 **Output variable-size signal** 参数。

**数据类型：** `uint16`

## 参数

### **Local IP port** — IP 端口号 25000（默认值）| [1, 65535] 范围内的标量

指定用于接收 UDP 数据包的 IP 端口号。此参数在生成的代码中可调，但在仿真期间不可调。

在 Linux® 上，要将 IP 端口号设置为低于 1024，请以 root 权限运行 MATLAB®。例如，在 Linux 命令行中，输入 `sudo matlab`。

### **Remote IP address ('0.0.0.0' to accept all)** — 接受数据包的 IP 地址 '0.0.0.0'（默认值）| IP 地址

指定从中接受 UDP 数据包的 IP 地址。指定特定 IP 地址以阻止来自其他地址的 UDP 数据包。要接受来自任何 IP 地址的数据包，请指定 `'0.0.0.0'`。

### **Receive buffer size (bytes)** — 接收 UDP 数据包的缓冲区大小 8192（默认值）| [1, 67108864] 范围内的标量

指定接收 UDP 数据包的缓冲区大小，以 bytes 为单位。使缓冲区足够大，以避免缓冲区溢出导致的数据丢失。

### **Maximum length for Message** — 输出数据的最大长度 255（默认值）| 标量

指定数据输出向量的最大长度，以向量元素为单位。将此参数设置为等于或大于 UDP 数据包数据大小的值。系统会截断超过此长度的数据。

如果禁用 **Output variable-size signal**，则模块输出为由此参数指定的长度。

### **Data type for Message** — 消息的数据类型 `uint8`（默认值）| `single` | `double` | `int8` | `int16` | `int32` | `uint16` | `uint32` | `boolean`

指定消息输出中向量元素的数据类型。使数据类型与用于创建 UDP 数据包的数据输入相匹配。

### **Message is complex** — 消息数据的复数性 off（默认值）| on

指定模块是否将消息作为复数数据接收。选择此参数以将消息作为复数数据接收。如果接收到的消息是实数数据，则清除此参数。

### **Output variable-size signal** — 长度可变的消息输出 on（默认值）| off

指定您的模型是否支持长度可变的信号。如果您的模型支持长度可变的信号，请选择此参数。在这种情况下：

- 输出向量的长度可变，具体取决于 UDP 数据包中的数据量。
- 该模块从单个未标记的输出发出数据向量。

如果您的模型不支持长度可变的信号，请清除此参数。在这种情况下：

- 该模块发出固定长度输出，其长度与 **Maximum length for Message** 指定的长度相同。
- 如果 UDP 数据包包含的数据少于固定长度输出，则差值部分包含无效数据。
- 该模块从 **Message** 输出发出数据向量。
- 该模块从 **Length** 输出发出有效数据的长度。

如果禁用此参数，则模块发出由 **Maximum length for Message** 指定长度的输出。

### **Blocking time (seconds)** — 等待 UDP 数据包的时间 `0`（默认值）| 非负标量

指定每个采样中等待 UDP 数据包的持续时间，然后将控制权返回给调度器。

### **Sample time (seconds)** — 调用模块的频率 `0.01`（默认值）| 标量

指定调度器调用 UDP Receive 模块的频率，以 seconds 为单位。输入大于零的值。在实时操作中，将此参数设置为较小的值可降低 UDP 消息丢失的可能性。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2014b 中引入**

## 描述

通过 IP 网络接收 UDP 数据包

UDP Receive 模块从 IP 网络端口接收 UDP 数据包，并将其保存到其缓冲区中。在每个采样中，模块输出将单个 UDP 数据包的内容作为数据向量发出。

**注意**

您的防病毒软件或防火墙可能会阻止 UDP 流量。请配置软件以允许来自特定 IP 端口号的流量。
