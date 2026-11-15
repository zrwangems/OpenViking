---
type: simulink-block
title: 'WiFi TCP/IP Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifitcpipreceive'
documentation_source_path: 'supportpkg/arduino_ref/wifitcpipreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi TCP/IP Receive

## 端口

### 输出

### **Data** — 输出数据向量

在每个时步，端口输出数据，其向量大小由 **Data size (N)** 参数指定。数据以 little-endian 格式接收。
要将其转换为 big-endian 格式，请执行以下任一操作：

- 将 Byte Reversal 模块紧跟在 WiFi TCP/IP Receive 模块之后放置。
- 在 MATLAB Function 模块中应用 `swapbytes` 函数，并将该模块紧跟在 WiFi TCP/IP Receive 模块之后放置。

有关详细信息，请参阅阻塞模式和非阻塞模式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — 在给定时步接收到请求的数据 `1` | `0`

在每个时步，当接收到的数据长度大于或等于 **Data size (N)** 参数指定的长度时，端口输出
`1`。否则，输出 `0`，表示未接收到新数据。

有关详细信息，请参阅阻塞模式和非阻塞模式。

**数据类型：** `int8`

## 参数

#### 主选项卡

### **Connection mode** — 将模块设置为服务器或客户端 `Server`（默认）| `Client`

将模块设置为 TCP/IP 服务器或客户端。

当您将此参数设置为 `Server` 时，必须提供
**Local IP port**。本地端口充当 TCP/IP
服务器上的侦听端口。

当您将此参数设置为 `Client` 时，必须提供
**Remote IP address** 以及要从其接收数据的 TCP/IP 服务器上的 **Remote IP port**。在部署包含客户端 WiFi TCP/IP Receive 模块的模型之前，请确保服务器已启动并正在运行。

### **Local IP port** — 接收主机上用于接收数据的 IP 端口 `25000`（默认）| [1 to 65,535]

此本地端口号充当 TCP/IP
服务器上的侦听端口。将本地端口号与发送主机的远程端口号匹配。

#### 依赖关系

此参数仅在您将 **Connection
mode** 参数设置为 `Server` 时显示。

### **Remote IP address** — 从其接收数据的服务器的远程 IP 地址 `192.168.1.2`（默认）| 任何有效的 IP 地址

指定从其接收数据的服务器的 IP 地址。

#### 依赖关系

此参数仅在您将 **Connection
mode** 参数设置为 `Client` 时显示。

### **Remote IP port** — 从其接收数据的服务器上的远程 IP 端口 `25000`（默认）| [1 to 65,535]

指定从其接收数据的服务器上的端口号。

#### 依赖关系

此参数仅在您将 **Connection
mode** 设置为 `Client` 时显示。

### **Data type** — 接收数据的数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

指定模块从发送主机接收的数据类型。每个元素的大小取决于其数据类型。

### **Data size (N)** — 接收数据中的字节数 `1`（默认）| 任意正整数

每个时步要接收的字节数。

该模块在每个时步可以接收的最大字节数如下表所示。

| 目标硬件 | ESP8266 | WiFi Shield | MKR1000 |
| --- | --- | --- | --- |
| 最大接收字节数 | 40 | 64 | 1400 |

### **Sample time** — 模块从发送主机读取数据的时间间隔 `0.1`（默认）| `-1` | 任意非负值

当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。当硬件为 ESP8266 时，允许的最小采样时间为
`0.01` seconds。否则，为 `0.000001` seconds（1
microsecond）。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off（默认）| on

- 当您选择此选项时，读取操作在阻塞模式下运行。在等待请求的数据可用时，读取操作会被阻塞。等待数据时，**Status** 端口显示上一个时步的相同值。当数据可用时，**Data** 端口输出数据字节，并且 **Status** 端口变为 `1`。

  如果目标硬件在计划开始下一次读取操作时仍在等待数据可用，则会发生任务超限。

  要修复超限：

  - 使用 **Sample time** 参数增大时间步。
  - 使用 **Data size (N)** 参数减少请求的数据长度。
- 当您清除此选项时，读取操作在非阻塞模式下运行。读取数据时，如果数据不可用，**Data** 端口输出由 **Data size (N)** 参数指定大小的向量，并用零填充。**Status** 端口输出 `0`。在此模式下，模块不会等待请求的数据可用。

### **Timeout in seconds** — 等待直到接收到数据的时间 `0.1`（默认）| (0, 2^32/1000]

指定模块在每个时步等待数据的时间量。如果发生超时，读取操作将中止。

**注意**

在 External 模式下仿真模型时，建议将 **Timeout
in seconds** 指定为小于 `3` seconds。

#### 依赖关系

此参数仅在您选择 **Wait
until data received** 参数时显示。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

通过无线网络上的 TCP/IP 网络从远程主机接收数据

WiFi TCP/IP Receive 模块通过无线网络从远程主机或其他硬件接收数据。当您将 **Connection mode** 设置为
`Server` 时，必须提供 **Local IP port**。
**Local IP port** 充当 TCP/IP 服务器上的侦听端口。当您将
**Connection mode** 设置为 `Client` 时，必须提供要接收数据的 TCP/IP
服务器的 **Remote IP address** 和 **Remote IP port**。

该模块以阻塞模式或非阻塞模式接收数据。该模块有两个输出端口：**Data** 和
**Status**。**Data** 端口在每个时步输出请求的数据。**Status** 端口指示在指定时步是否接收到新数据。

您可以在 Arduino® 板上以 Connected IO 模式运行包含 WiFi TCP/IP Receive 模块的 Simulink® 模型。

**注意**

Connected IO 模式不支持 ESP32 和 ESP8266 板。

有关模块的固定端口和分配引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

**注意**

如果您在使用 TCP 与计算机通信时遇到问题，防病毒或防火墙软件可能正在阻止 TCP 流量。如果是这样，请将该软件配置为允许特定 IP 端口号的流量。

### 支持的硬件

您只能将 WiFi TCP/IP Receive 模块与以下硬件一起使用：

- ESP8266
- WiFi Shield
- MKR1000
- MKR WIFI 1010
- Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
