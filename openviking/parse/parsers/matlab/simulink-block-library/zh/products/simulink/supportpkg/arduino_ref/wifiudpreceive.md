---
type: simulink-block
title: 'WiFi UDP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifiudpreceive'
documentation_source_path: 'supportpkg/arduino_ref/wifiudpreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi UDP Receive

## 端口

### 输出

### **Data** — 输出数据向量

在每个采样时间，端口输出由 **数据大小 (N)** 参数指定大小的向量形式的数据。数据以小端格式接收。要将其转换为大端格式，请执行以下任一操作：

- 将 Byte Reversal 模块紧接放在 WiFi UDP Receive 模块之后。
- 在 MATLAB Function 模块中应用 `swapbytes` 函数，并将该模块紧接放在 WiFi UDP Receive 模块之后。

有关详细信息，请参阅接收数据的输出。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **Size** — 接收到的数据字节数标量

在每个采样时间，端口输出接收数据中的字节数。有关详细信息，请参阅接收数据的输出。

**数据类型：** `uint16`

## 参数

### **本地 IP 端口** — 接收主机上从其接收数据的 IP 端口 `50001`（默认） | [1 到 65,535]

指定要接收数据的应用程序的端口号。将本地端口号与发送主机上的远程端口号匹配。

### **数据类型** — 接收数据的数据类型 `uint8`（默认） | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定模块从发送主机接收的数据类型。每个元素的大小取决于其数据类型。

### **数据大小 (N)** — 接收数据中的字节数 `1`（默认） | 任意正整数

每个采样时间接收的字节数。

此模块在每个采样时间可接收的最大字节数如下表所示。

| 目标硬件 | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| 最大接收字节数 | 40 | 64 | 1400 |

### **采样时间** — 模块从发送主机读取数据的时间间隔 `0.1`（默认） | `-1` | 任意非负值

当将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。当硬件为 ESP8266 时，允许的最小采样时间为 `0.01` seconds。否则，为 `0.000001` seconds (1 microsecond)。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

从无线网络上的 UDP 主机接收数据

WiFi UDP Receive 模块从无线网络上的 UDP 主机接收数据。在每个采样时间，该模块输出由 **数据大小 (N)** 参数指定大小的向量形式的数据。该模块在 **本地 IP 端口** 参数指定的端口号上接收数据。将 **本地 IP 端口** 参数指定的端口号与发送主机上的远程端口号匹配。

**注意**

如果您在使用 UDP 与计算机通信时遇到问题，防病毒或防火墙软件可能正在阻止 UDP 流量。如果是这样，请配置该软件以允许特定 IP 端口号的流量。

您可以在 Arduino® 开发板上以 Connected IO 模式运行包含 WiFi UDP Receive 模块的 Simulink® 模型。

有关该模块的固定端口和分配引脚的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

### 支持的硬件

您只能将 WiFi UDP Receive 模块与以下硬件一起使用：

- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
