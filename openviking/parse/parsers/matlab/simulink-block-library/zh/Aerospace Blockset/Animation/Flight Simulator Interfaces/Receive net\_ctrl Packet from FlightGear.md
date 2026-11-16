---
type: simulink-block
title: 'Receive net_ctrl Packet from FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'receivenet_ctrlpacketfromflightgear'
documentation_source_path: 'receivenet_ctrlpacketfromflightgear.html'
language: zh-CN
chinese_source: worker-translation
---

# Receive net_ctrl Packet from FlightGear

## 端口

### 输出

### **net\_ctrl** — 来自 FlightGear 的控制信息 744-by-1 向量

来自 FlightGear 的控制信息，以 744-by-1 向量形式返回。

**数据类型：** `uint8`

### **Rx bytes** — 接收到的 FlightGear 数据包大小 `0` | `744`

接收到的 FlightGear 数据包大小，指定为标量。

- 0，如果未接收到数据
- 数据包大小（744），以字节为单位。

#### 依赖项

此端口由 **启用已接收标志端口** 复选框启用。

**数据类型：** `double`

## 参数

### **源 IP 地址** — 源 IP 地址 `127.0.0.1`（默认） | 标量

输入有效的 IP 地址作为点分十进制字符串。此 IP 地址必须是运行 FlightGear 的计算机的地址，例如 `10.10.10.3`。

您还可以使用一个 MATLAB 表达式，该表达式以 character vector 形式返回有效 IP 地址。如果 FlightGear 在本地计算机上运行，请保留默认值 `127.0.0.1`（localhost）。

要确定源 IP 地址，您可以使用以下几种方法之一，例如：

- 对于本地计算机（localhost），使用 127.0.0.1。
- 从 Windows® `cmd.exe`（或 Linux® shell）提示符 ping 另一台计算机：

  ```
  C:\> ping andyspc

  Pinging andyspc [144.213.175.92] with 32 bytes of data:

  Reply from 144.213.175.92: bytes=32 time=30ms TTL=253
  Reply from 144.213.175.92: bytes=32 time=20ms TTL=253
  Reply from 144.213.175.92: bytes=32 time=20ms TTL=253
  Reply from 144.213.175.92: bytes=32 time=20ms TTL=253

  Ping statistics for 144.213.175.92:
      Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
  Approximate round trip times in milli-seconds:
      Minimum = 20ms, Maximum =  30ms, Average =  22ms
  ```
- 在 Windows 机器上，输入 `ipconfig` 并使用返回的 IP 地址：

  ```
  H:\>ipconfig

  Windows IP Configuration

  Ethernet adapter Local Area Connection:

          Connection-specific DNS Suffix  . :
          IP Address. . . . . . . . . . . . : 192.168.42.178
          Subnet Mask . . . . . . . . . . . : 255.255.255.0
          Default Gateway . . . . . . . . . : 192.168.42.254
  ```

#### 程序化使用

|  |
| --- |
| **模块参数**: `ReceiveAddress` |
| **类型**: character vector |
| **值**: 标量 |
| **默认值**: `'127.0.0.1'` |

### **源端口** — 源端口 5505（默认）

此模块接受数据的 UDP 端口。发送方将数据发送到此参数指定的端口。此值必须与 Generate Run Script 模块的 **源端口** 参数匹配。它必须是计算机上其他应用程序未使用的唯一端口号。站点 `https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers` 列出了常见的 UDP 端口号。要识别计算机上已在使用的 UDP 端口号，请输入：

```
netstat -a -p UDP
```

#### 程序化使用

|  |
| --- |
| **模块参数**: `ReceivePort` |
| **类型**: character vector |
| **值**: 标量 |
| **默认值**: `'5505'` |

### **采样时间** — 采样时间 1/30（默认） | 标量

指定采样时间（继承时为 -1）。

#### 程序化使用

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: character vector |
| **值**: 标量 |
| **默认值**: `'1/30'` |

### **启用已接收标志端口** — 启用已接收标志输出端口 `off`（默认） | `on`

启用已接收标志输出端口。使用此复选框确定是否已接收到 FlightGear 网络数据包。

#### 依赖项

选中此复选框将启用 **Rx bytes** 端口。

#### 程序化使用

|  |
| --- |
| **模块参数**: `packetFlag` |
| **类型**: character vector |
| **值：**`'off' | 'on'` |
| **默认值**: `'off'` |

## 所属库

Aerospace Blockset / Animation / Flight Simulator Interfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2012a 中引入**

## 描述

从 FlightGear 接收 net_ctrl 数据包

Receive net\_ctrl Packet from FlightGear 模块接收来自 FlightGear 模拟器中 Simulink® 模型的仿真、或来自 FlightGear 会话的网络控制和环境数据包 `net_ctrl`。此数据包与特定版本的 FlightGear 飞行模拟器兼容。此模块支持 FlightGear `net_ctrl` 数据包支持的所有信号。此模块将信号排列为多个组。对于属于非活动信号组的数据包值，此模块插入零。

Aerospace Blockset™ 产品支持从 v2.6 开始的 FlightGear 版本。如果您使用早于 2.6 的 FlightGear 版本，模型会显示来自 Simulink Upgrade Advisor 的通知。请考虑使用 Upgrade Advisor 升级您的 FlightGear 版本。有关详细信息，请参阅支持的 FlightGear 版本。

如果您在 Rapid Accelerator 模式下运行包含此模块的模型，此模块会产生零（`0`）并且不会生成可部署代码。在 Accelerator 模式下，此模块按预期工作。

有关信号和信号组的详细信息，请参阅输出。
