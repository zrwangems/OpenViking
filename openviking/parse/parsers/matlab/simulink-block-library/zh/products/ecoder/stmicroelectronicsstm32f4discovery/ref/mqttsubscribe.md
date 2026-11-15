---
type: simulink-block
title: 'MQTT Subscribe'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Internet of Things'
documentation_page: 'mqttsubscribe'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/mqttsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Subscribe

## 端口

### 输出

### **IsNew** — 新消息指示符 `0`（默认） | `1`

如果客户端自上一个时间步以来收到新消息，则 **IsNew** 端口输出 `1`。否则，该端口输出 `0`。

**数据类型：** `Boolean`

### **Message** — 接收到的消息 `0`（默认）

从 MQTT 代理接收到的消息，指定为 *N*×1 向量。*N* 是由 **消息长度 (N)** 参数指定的消息长度。

**数据类型：** `double`

### **Topic** — 消息的主题 `topic/level/#`（默认）

与接收到的消息的主题名称对应的 ASCII 值。例如，如果接收到的消息的主题为 `model/data`，则该端口将主题输出为 `109 111 100 101 108 47 100 97 116 97`。

要将 ASCII 值转换为字母数字等价形式，请将 ASCII to String 模块连接到 **Topic** 端口的输出。有关主题及其结构的信息，请参阅 MQTT 中的主题。

**注意**

一个主题最多可以包含 128 个字符。

#### 依赖关系

仅当在模块参数对话框中指定的 **Topic** 参数值包含通配符条目时，**Topic** 端口才可用。有关通配符的信息，请参阅 MQTT 主题中的通配符。

**数据类型：** `uint8`

## 参数

### **Topic** — 用于订阅的主题 `topic/level`（默认） | 有效主题名称

指定客户端订阅的主题。有关主题及其结构的信息，请参阅 MQTT 中的主题。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Topic` |
| **类型：** character vector |
| **值：** `'topic/level'`|`valid topic name` |
| **默认值：**  `'topic/level'` |

### **QoS** — QoS 级别 `0`（默认） | `1` | `2`

服务质量 (QoS) 定义 MQTT 中消息传递过程的可靠性。MQTT 为消息传递提供三个 QoS 级别：QoS 0、QoS 1 和 QoS 2。您使用的 MQTT 代理可能不支持三个 QoS 级别。例如，ThingSpeak™ MQTT 仅支持 QoS 0。

从列表中选择 QoS 级别：

- `0`（至多一次）：MQTT 代理将消息发送到客户端。客户端不发送接收确认。
- `1`（至少一次）：MQTT 代理至少将消息发送到客户端一次。如果代理未收到来自客户端的确认，则会重新发送消息。
- `2`（恰好一次）：MQTT 代理恰好将消息发送到客户端一次。代理和客户端交换确认，以便消息仅接收一次。

有关 QoS 级别的详细信息，请参阅 MQTT 中的 QoS 级别。

#### 程序化使用

|  |
| --- |
| **模块参数：** `QoS` |
| **类型：** character vector |
| **值：** `'0'`|`'1'`|`'2'` |
| **默认值：**  `'0'` |

### **消息长度 (N)** — 要接收的消息长度 `10`（默认） | 1 到 64（含）之间的整数

指定要从 MQTT 代理接收的消息长度。如果接收到的消息长度大于 **消息长度 (N)** 中指定的长度，则该模块仅输出接收到的消息的前 *N* 个字符。如果接收到的消息长度小于 **消息长度 (N)** 中指定的长度，则该模块会在接收到的消息后追加零。

#### 程序化使用

|  |
| --- |
| **模块参数：** `MessageLength` |
| **类型：** character vector |
| **值：** `'1'`|`integer between 1 and 64 inclusive` |
| **默认值：**  `'1'` |

### **采样时间** — 新消息的采样率 `1`（默认） | `-1` | 正整数

指定订阅者检查来自代理的新消息的频率。当您将 **采样时间** 指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sampletime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'0.1'` |

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

从 MQTT 代理接收指定主题的消息

MQTT Subscribe 模块从 MQ Telemetry Transport (MQTT) 代理接收指定主题的消息。

在每个时间步，该模块检查指定主题上是否有新消息可用。如果有新消息可用，则该模块接收该消息。**Message** 端口输出新消息。如果没有新消息可用，则 **Message** 输出最后接收到的消息。**Topic** 端口输出接收到的消息的主题。模块图标上的字符串 **topic/level/#** 由 **Topic** 参数指定。

有关 MQTT 的详细信息，请参阅 MQTT 简介。

**注意**

MQTT Subscribe 模块仅支持通过 TCP/IP 套接字的 MQTT。
