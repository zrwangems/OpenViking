---
type: simulink-block
title: 'MQTT Publish'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Internet of Things'
documentation_page: 'mqttpublish'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/mqttpublish.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Publish

## 端口

### 输入

### **Message** — 要发布的消息向量

要发布到 MQTT broker 的消息，指定为向量。

**示例：**
`[0,3]`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Status** — 来自 MQTT broker 的状态代码标量

由 MQTT broker 针对发布请求发出的状态代码。如果 broker 接受该消息进行发布，该端口输出 `0`。非零输出表示 broker 已拒绝该消息。消息可能因各种原因被拒绝，例如用户名或密码不正确，或协议版本不可接受。有关来自 MQTT broker 的状态代码的详细信息，请参阅 LWIP 错误代码。

**数据类型：** `int8`

## 参数

### **Broker Service** — MQTT broker 服务提供商 `ThingSpeak`（默认）| other

选择接收、过滤并向客户端发送消息的 MQTT broker 服务提供商。

- `ThingSpeak` — 指定此选项时，对您通道的 MQTT 访问由 ThingSpeak™ MQTT broker 处理。要创建 MQTT 设备，请按照创建 ThingSpeak MQTT 设备 (ThingSpeak) 中的步骤操作。
- `Other` — 当对您通道的 MQTT 访问由其他 MQTT 公共 broker（例如 HiveMQ®、Mosquitto™ 等）处理时，指定此选项。

配置与 MQTT 中相同的 MQTT broker 属性。

#### 编程用法

|  |
| --- |
| **模块参数：** `Broker Service` |
| **类型：** character vector |
| **取值：** `'ThingSpeak'`|`Others` |
| **默认值：**  `'ThingSpeak'` |

### **Topic** — 消息的主题 `Channels/<channelID>publish`（默认）| valid channel

指定要在其上发布消息的主题。主题最多可包含 128 个字符。有关主题及其结构的信息，请参阅 MQTT 中的主题。

#### 编程用法

|  |
| --- |
| **模块参数：** `Topic` |
| **类型：** character vector |
| **取值：** `Channels/<channelID>publish`|`valid channel` |
| **默认值：**  `Channels/<channelID>publish` |

### **QoS** — QoS 级别 `0`（默认）| `1` | `2`

服务质量 (QoS) 定义了 MQTT 中消息传递过程的可靠性。MQTT 为消息传递提供三个 QoS 级别：QoS 0、QoS 1 和 QoS 2。您使用的 MQTT broker 可能不支持这三个 QoS 级别。例如，ThingSpeak MQTT 仅支持 QoS 0。

从列表中选择 QoS 级别：

- `0`（至多一次）：发布者向 MQTT broker 发送一次消息。broker 不发送接收确认。
- `1`（至少一次）：发布者至少向 MQTT broker 发送一次消息。如果发布者未收到来自 broker 的确认，则会重新发送消息。
- `2`（恰好一次）：发布者向 MQTT broker 恰好发送一次消息。发布者和 broker 交换确认，以确保消息仅接收一次。

有关 QoS 级别的详细信息，请参阅 MQTT 中的 QoS 级别。

#### 编程用法

|  |
| --- |
| **模块参数：** `QoS` |
| **类型：** character vector |
| **取值：** `'0'`|`'1'`|`'2'` |
| **默认值：**  `'0'` |

### **Retain message** — 向新订阅者发送消息的选项 `off`（默认）| `on`

**Retain message** 参数控制如何处理新订阅：

- `on` –– 当对某个主题进行新订阅时，broker 会在其数据库中识别出具有匹配主题名称的消息，并立即发送该消息。

  **注意**

  MQTT broker 仅保留发布在某个主题上的最后一条已知消息。
- `off` –– 当对某个主题进行新订阅时，订阅者必须等待发布者发送下一条消息。

  **注意**

  例如，ThingSpeak MQTT 不支持 Retain message。

#### 依赖关系

要启用此参数，请将 **Broker Service** 设置为 **Other**。

#### 编程用法

|  |
| --- |
| **模块参数：** `RetainMsg` |
| **类型：** character vector |
| **取值：** `'off'`|`'on'` |
| **默认值：**  `off` |

### **Update interval (seconds)** — 发布消息的速率 `60`（默认）| `scalar`

输入向 MQTT broker 发布消息的时间间隔（秒）。

#### 编程用法

|  |
| --- |
| **模块参数：** `Update interval (seconds)` |
| **类型：** character vector |
| **取值：** `'60'`|`'on'` |
| **默认值：**  `60` |

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**R2024a 中引入**

## 描述

将消息发布到指定主题上的 MQTT broker

MQTT Publish 模块将来自您的硬件（发布者）的消息发布到指定主题上的消息队列遥测传输 (MQTT) broker。

**Message** 端口接收要发布到 broker 的消息。**Status** 端口输出发布请求的状态。模块图标上的字符串 **topic/level** 由 **Topic** 参数指定。

有关 MQTT 的详细信息，请参阅 MQTT 简介。

**注意**

MQTT Publish 模块仅支持通过 TCP/IP 套接字使用 MQTT。
