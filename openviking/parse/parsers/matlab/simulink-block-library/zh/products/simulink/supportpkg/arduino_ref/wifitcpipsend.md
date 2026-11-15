---
type: simulink-block
title: 'WiFi TCP/IP Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifitcpipsend'
documentation_source_path: 'supportpkg/arduino_ref/wifitcpipsend.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi TCP/IP Send

## 端口

### 输入

### **Port\_1** — 输入数据向量

该模块接受 *N*×1 数组形式的数据。该模块通过 TCP/IP 网络将此数据发送到接收主机。数据以小端格式发送。要将其转换为大端格式，请执行以下任一操作：

- 将 Byte Reversal 模块紧放在 WiFi TCP/IP Send 模块之前。
- 在 MATLAB Function 模块中应用 `swapbytes` 函数，并将该模块紧放在 WiFi TCP/IP Send 模块之前。

该模块在每个时间步可发送的最大字节数如下表所示。

| 目标硬件 | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| 最大发送字节数 | 2048 | 64 | 1400 |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认）| `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供 **Local IP Port**。该本地端口充当 TCP/IP 服务器上的侦听端口。

当您将此参数设置为 `Client` 时，必须提供 **Remote IP address** 以及要将数据发送到的 TCP/IP 服务器上的 **Remote IP port**。在部署包含客户端 WiFi TCP/IP Send 模块的模型之前，请确保服务器已启动并正在运行。

### **Local IP port** — 发送主机上从其发送数据的 IP 端口 `25000`（默认）| [1 到 65,535]

指定从其发送数据的应用程序的端口号。此本地端口充当 TCP/IP 服务器上的侦听端口。

#### 依赖关系

仅当将 **Connection mode** 参数设置为 `Server` 时，此参数才会出现。

### **Remote IP address** — 要将数据发送到的服务器的远程 IP 地址 `192.168.1.2`（默认）| 任何有效 IP 地址

指定要将数据发送到的服务器的远程 IP 地址。

#### 依赖关系

仅当将 **Connection mode** 参数设置为 `Client` 时，此参数才会出现。

### **Remote IP port** — 要将数据发送到的服务器上的远程 IP 端口 `25000`（默认）| [1 到 65,535]

指定要将数据发送到的接收服务器上的端口号。

#### 依赖关系

仅当将 **Connection mode** 参数设置为 `Client` 时，此参数才会出现。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

通过无线网络经 TCP/IP 网络将数据发送到远程主机

WiFi TCP/IP Send 模块通过无线网络将数据发送到远程主机或其他硬件板。您可以将该模块的 **Connection mode** 设置为 `Server` 或 `Client`。当您将 **Connection mode** 设置为 `Client` 时，必须提供要将数据发送到的服务器的 **Server IP Address** 和 **Server IP Port**。当您将 **Connection mode** 设置为 `Server` 时，必须提供 **Local IP Port**。此 **Local IP Port** 充当 TCP/IP 服务器上的侦听端口。

您可以在 Arduino® 板上以 Connected IO 模式运行包含 WiFi TCP/IP Send 模块的 Simulink® 模型。

**注意**

Connected IO 模式下不支持 ESP32 和 ESP8266 板。

有关该模块的固定端口和分配引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

**注意**

如果您在使用 TCP 与计算机通信时遇到问题，防病毒或防火墙软件可能正在阻止 TCP 流量。如果是这样，请将该软件配置为允许特定 IP 端口号的流量。

### 支持的硬件

WiFi TCP/IP Send 模块只能用于以下硬件：

- ESP8266
- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
