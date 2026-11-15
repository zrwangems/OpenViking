---
type: simulink-block
title: 'MQTT Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Internet of Things'
documentation_page: 'mqttsubscribe'
documentation_source_path: 'supportpkg/raspberrypi_ref/mqttsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Subscribe

## 端口

### 输出

### **IsNew** — 新消息指示符 `0` (默认) | `1`

如果客户端自上一个时间步以来接收到新消息，则 **IsNew** 端口输出 `1`。否则，该端口输出 `0`。

**数据类型：** `Boolean`

### **Message** — 接收到的消息 `0` (默认)

从 MQTT broker 接收到的消息，指定为 *N*×1 向量。*N* 是由 **Message length (N)** 参数指定的消息长度。

**数据类型：** `double`

### **Topic** — 消息的主题 `topic/level/#` (默认)

与接收消息的主题名称对应的 ASCII 值。例如，如果接收消息的主题为 `model/data`，则该端口将主题输出为 `109 111 100 101 108 47 100 97 116 97`。

要将 ASCII 值转换为字母数字等效值，请将 ASCII to String 模块连接到 **Topic** 端口的输出。有关主题及其结构的信息，请参阅 MQTT 中的主题。

**注意**

主题最多可以有 128 个字符。

#### 依赖关系

仅当 Block Parameters 对话框中指定的 **Topic** 参数值包含通配符条目时，**Topic** 端口才可用。有关通配符的信息，请参阅 MQTT 主题中的通配符。

**数据类型：** `uint8`

## 参数

### **Topic** — 用于订阅的主题 `topic/level` (默认) | 任何有效主题名称

指定客户端订阅的主题。有关主题及其结构的信息，请参阅 MQTT 中的主题。

### **QoS** — QoS 级别 `0` (默认) | `1` | `2`

服务质量 (QoS) 定义了 MQTT 中消息传递过程的可靠性。MQTT 为消息传递提供三个 QoS 级别：QoS 0、QoS 1 和 QoS 2。您使用的 MQTT broker 可能不支持所有三个 QoS 级别。例如，ThingSpeak™ MQTT 仅支持 QoS 0。

从列表中选择一个 QoS 级别：

- `0`：MQTT broker 将消息发送到客户端。客户端不发送接收确认。
- `1`：MQTT broker 至少将消息发送到客户端一次。如果 broker 未收到来自客户端的确认，则重新发送消息。
- `2`：MQTT broker 将消息恰好一次发送到客户端。broker 和客户端交换确认，以确保消息仅接收一次。

有关 QoS 级别的详细信息，请参阅 MQTT 中的 QoS 级别。

### **Message length (N)** — 要接收的消息长度 `1` (默认) | 1 到 64（含）之间的整数

指定要从 MQTT broker 接收的消息长度。如果接收到的消息长度大于 **Message length (N)** 中指定的长度，则模块仅输出接收消息的前 *N* 个字符。如果接收到的消息长度小于 **Message length (N)** 中指定的长度，则模块向接收到的消息追加零。

### **Output the last received message** — 在 Message 端口上查看最后接收消息的选项 `off` (默认) | `on`

选中此选项时，最后接收到的消息将显示在 **Message** 输出端口上。

- 当 **isNew** 输出端口为高电平时，新消息将显示在 **Message** 输出端口上。
- 当 **isNew** 输出端口为低电平时，在上一个采样时间接收到的消息将显示在 **Message** 输出端口上。

清除此选项时，为指定主题接收到的消息按先进先出顺序形成队列，并相应地显示在 **Message** 输出端口中。

### **Sample time** — 检查来自 MQTT broker 的消息的频率 `1` (默认) | `-1` | 任何正整数

指定订阅者检查来自 broker 的新消息的频率。当将 **Sample time** 指定为 `-1` 时，模块将根据模块在模型中的上下文继承其采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Internet Of Things

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

接收来自 MQTT broker 的指定主题消息

MQTT Subscribe 模块从消息队列遥测传输 (MQTT) broker 接收指定主题的消息。

该模块有三个输出端口：**IsNew**、**Message** 和 **Topic**。在每个时间步，模块检查指定主题上是否有新消息可用。如果有新消息可用，模块将接收该消息。**Message** 端口输出新消息。如果没有新消息可用，**Message** 输出最后接收到的消息。**Topic** 端口输出所接收消息的主题。模块图标上的字符串 **topic/level/#** 由 **Topic** 参数指定。

有关 MQTT 的详细信息，请参阅发布 MQTT 消息和订阅消息主题。

**注意**

MQTT Subscribe 模块仅支持通过 TCP/IP 套接字使用 MQTT。
