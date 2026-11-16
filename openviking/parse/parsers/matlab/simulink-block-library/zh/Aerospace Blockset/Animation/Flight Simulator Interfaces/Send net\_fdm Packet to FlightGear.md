---
type: simulink-block
title: 'Send net_fdm Packet to FlightGear'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'sendnet_fdmpackettoflightgear'
documentation_source_path: 'sendnet_fdmpackettoflightgear.html'
language: zh-CN
chinese_source: worker-translation
---

# Send net_fdm Packet to FlightGear

## 端口

### 输入

### **net\_fdm** — FlightGear `net_fdm` 数据包标量

FlightGear `net_fdm` 数据包，指定为标量。

**数据类型：** `uint8`

## 参数

### **目标 IP 地址** — 远程计算机的目标 IP 地址 `127.0.0.1`（默认）| 标量

目标 IP 地址，指定为标量。

您可以使用多种方法之一来确定目标 IP 地址，例如：

- 使用 127.0.0.1 表示本地计算机
- 从 Windows® `cmd.exe`（或 UNIX® shell）提示符 ping 另一台计算机：

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
- 在 Windows 计算机上，键入 `ipconfig` 并使用返回的 *`IP Address`*：

  ```
  H:\>ipconfig

  Windows IP Configuration

  Ethernet adapter Local Area Connection:

          Connection-specific DNS Suffix  . :
          IP Address. . . . . . . . . . . . : 192.168.42.178
          Subnet Mask . . . . . . . . . . . : 255.255.255.0
          Default Gateway . . . . . . . . . : 192.168.42.254
  ```

#### 编程使用

|  |
| --- |
| **模块参数**：`DestinationIpAddress` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`127.0.0.1` |

### **目标端口** — 远程计算机的目标端口 5502（默认）| 标量

目标端口，指定为标量

#### 编程使用

|  |
| --- |
| **模块参数**：`DestinationPort` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`5502` |

### **采样时间** — 采样时间 `1/30`（默认）| 标量

采样时间（-1 表示继承），指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：标量 |
| **默认值**：`1/30` |

## 所属库

Aerospace Blockset / Animation / Flight Simulator Interfaces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

为 FlightGear 会话将 net_fdm 数据包传输到目标 IP 地址和端口

Send net\_fdm Packet to FlightGear 模块将 `net_fdm` 数据包传输到当前计算机或网络上的远程计算机上的 FlightGear。该数据包使用 Pack net\_fdm Packet for FlightGear 模块构建。目标端口应为未使用的端口，您可以在使用 FlightGear 命令行标志启动 FlightGear 时使用该端口：

```
--fdm=network,localhost,5501,5502,5503
```

此模块不生成可部署代码。
