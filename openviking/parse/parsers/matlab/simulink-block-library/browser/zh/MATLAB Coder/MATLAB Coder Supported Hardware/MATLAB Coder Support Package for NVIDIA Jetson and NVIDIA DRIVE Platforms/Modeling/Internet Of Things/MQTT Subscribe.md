---
type: simulink-block
title: 'MQTT Subscribe'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Internet Of Things'
documentation_page: 'mqttsubscribe'
documentation_source_path: 'nvidia/ref/mqttsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Subscribe

## 端口

### 输出

### **IsNew** — 新消息指示 `0` (默认) | `1`

如果客户端自上一个时间步以来收到新消息，则 **IsNew** 端口输出 `1`。否则，该端口输出 `0`。

**数据类型：** `Boolean`

### **Message** — 接收到的消息 `0` (默认)

从 MQTT broker 接收到的消息，指定为 *N*×1 向量。*N* 是 **消息长度 (N)** 参数指定的消息长度。

**数据类型：** `double`

### **Topic** — 消息的主题 `topic/level/#` (默认)

与所接收消息的主题名称对应的 ASCII 值。例如，如果所接收消息的主题为 `model/data`，则该端口输出的主题为 `109 111 100 101 108 47 100 97 116 97`。

要将 ASCII 值转换为字母数字等效形式，请将 ASCII to String (Simulink) 模块连接到 **Topic** 端口的输出。有关主题及其结构的信息，请参阅 MQTT 中的主题。

**注意**

一个主题最多可以包含 128 个字符。

#### 依赖关系

仅当在“模块参数”对话框中指定的 **Topic** 参数值包含通配符条目时，**Topic** 端口才可用。有关通配符的信息，请参阅 MQTT 主题中的通配符。

**数据类型：** `uint8`

## 参数

### **Topic** — 用于订阅的主题 `topic/level` (默认) | 有效主题名称

指定客户端订阅的主题。有关主题及其结构的信息，请参阅 MQTT 中的主题。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Topic` |
| **类型：** character vector |
| **值：** `'topic/level'`|`valid topic name` |
| **默认值：**  `'topic/level'` |

### **QoS** — QoS 级别 `0` (默认) | `1` | `2`

服务质量 (QoS) 定义了 MQTT 中消息传递过程的可靠性。MQTT 提供三种消息传递 QoS 级别：QoS 0、QoS 1 和 QoS 2。您使用的 MQTT broker 可能不支持三种 QoS 级别。例如，ThingSpeak™ MQTT 仅支持 QoS 0。

从列表中选择一个 QoS 级别：

- `0` (At most once)：MQTT broker 将消息发送给客户端。客户端不发送收到确认。
- `1` (At least once)：MQTT broker 至少将消息发送给客户端一次。如果 broker 未收到来自客户端的确认，则会重新发送该消息。
- `2` (Exactly once)：MQTT broker 将消息恰好发送给客户端一次。broker 和客户端交换确认，以便该消息仅被接收一次。

有关 QoS 级别的详细信息，请参阅 MQTT 中的 QoS 级别。

#### 程序化使用

|  |
| --- |
| **模块参数：** `QoS` |
| **类型：** character vector |
| **值：** `'0'`|`'1'`|`'2'` |
| **默认值：**  `'0'` |

### **消息长度 (N)** — 要接收的消息长度 `1` (默认) | 1 到 64 之间的整数（含 1 和 64）

指定要从 MQTT broker 接收的消息长度。如果接收到的消息长度大于 **消息长度 (N)** 中指定的长度，则模块仅输出所接收消息的前 *N* 个字符。如果接收到的消息长度小于 **消息长度 (N)** 中指定的长度，则模块会在所接收消息后追加零。

### **输出最后接收到的消息** — 在 Message 端口上查看最后接收到的消息的选项 `off` (默认) | `on`

当您选择此选项时，最后接收到的消息会显示在 **Message** 输出端口上。

- 当 **isNew** 输出端口为高时，新消息显示在 **Message** 输出端口上。
- 当 **isNew** 输出端口为低时，在上一采样时间接收到的消息显示在 **Message** 输出端口上。

当您清除此选项时，为指定主题接收到的消息按先进先出顺序形成队列，并且这些消息相应地显示在 **Message** 输出端口上。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputMessage` |
| **类型：** character vector |
| **值：** `'off'`|`'on'` |
| **默认值：**  `off` |

### **采样时间** — 新消息的采样率 `1` (默认) | `-1` | 正整数

指定订阅者检查来自 broker 的新消息的频率。当您将 **采样时间** 指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Internet Of Things

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

接收来自 MQTT broker 的指定主题的消息

MQTT Subscribe 模块接收来自 MQ Telemetry Transport (MQTT) broker 的指定主题的消息。

在每个时间步，模块检查指定主题上是否有新消息可用。如果有新消息可用，模块接收该消息。**Message** 端口输出新消息。如果没有新消息可用，**Message** 输出最后接收到的消息。**Topic** 端口输出所接收消息的主题。模块图标上的字符串 **topic/level/#** 由 **Topic** 参数指定。

有关 MQTT 的详细信息，请参阅 MQTT 简介。

**注意**

MQTT Subscribe 模块仅支持通过 TCP/IP 套接字的 MQTT。
