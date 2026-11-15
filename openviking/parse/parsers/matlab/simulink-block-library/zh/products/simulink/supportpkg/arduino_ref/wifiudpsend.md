---
type: simulink-block
title: 'WiFi UDP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifiudpsend'
documentation_source_path: 'supportpkg/arduino_ref/wifiudpsend.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi UDP Send

## 端口

### 输入

### **Port\_1** — 输入数据向量

该模块接受 *N*×1 数组形式的数据。该模块通过无线网络将此数据发送到接收主机。数据以小端格式发送。要将其转换为大端格式，请执行以下任一操作：

- 将 Byte Reversal 模块紧放在 WiFi UDP Send 模块之前。
- 在 MATLAB Function 模块中应用 `swapbytes` 函数，并将该模块紧放在 WiFi UDP Send 模块之前。

该模块在每个时间步可以发送的最大字节数如下表所示。

| 目标硬件 | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| 最大发送字节数 | 2048 | 64 | 1400 |

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

## 参数

### **Remote IP address** — 数据发送到的主机的远程 IP 地址 `192.168.1.2`（默认）| 任何有效 IP 地址

指定数据发送到的主机的远程 IP 地址。要向所有接收主机广播数据，请指定 `255.255.255.255`。

### **Remote IP Port** — 数据发送到的主机上的远程 IP 端口 `50002`（默认）| [1 到 65,535]

指定数据发送到的主机上应用程序的端口号。将远程端口号与接收主机上的本地端口号匹配。

### **Local IP Port** — 发送主机上从其发送数据的 IP 端口 `50001`（默认）| [1 到 65,535]

指定目标上从其发送数据的应用程序的端口号。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

通过无线网络向 UDP 主机发送数据

WiFi UDP Send 模块通过无线网络向 UDP 主机发送数据。该模块从 **Local IP Port** 参数指定的端口号发送数据。在 **Remote IP address** 和 **Remote IP Port** 参数中指定接收主机的 IP 地址和端口号。

您可以在 Arduino® 板上以 Connected IO 模式运行包含 WiFi UDP Send 模块的 Simulink® 模型。

有关该模块的固定端口和已分配引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

**注意**

如果您在使用 UDP 与计算机通信时遇到问题，防病毒或防火墙软件可能正在阻止 UDP 流量。如果是这样，请配置该软件以允许特定 IP 端口号的流量。

### 支持的硬件

您只能将 WiFi UDP Send 模块与以下硬件一起使用：

- ESP8266
- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
