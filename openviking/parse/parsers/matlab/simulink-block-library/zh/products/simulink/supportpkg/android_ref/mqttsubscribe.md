---
type: simulink-block
title: 'MQTT Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'mqttsubscribe'
documentation_source_path: 'supportpkg/android_ref/mqttsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Subscribe

## 端口

### 输出

### **Data Length** — 数据长度（标量）（默认）

该端口输出从 MQTT 代理接收到的数据的实际长度。

**数据类型：** `int32`

### **Data** — 从 MQTT 代理接收的数据标量

该模块将从 MQTT 代理接收到的数据输出为 ASCII 字符数组。

**数据类型：** `uint8`

## 参数

### **主题** — 要订阅的主题 `channels/<channelID>/subscribe`（默认） | 任何有效的主题名称

指定客户端订阅的主题。主题最多可包含 128 个字符。有关主题及其结构的信息，请参阅 MQTT 中的主题。

### **输出消息的最大长度** — 从 MQTT 代理读取的数据的最大长度 `256`（默认） | `positive integer`

指定每个采样时间要接收的数据的最大长度。

### **采样时间** — 检查来自 MQTT 代理的消息的频率 `1`（默认） | `-1` | 标量

指定客户端检查来自代理的新消息的频率。当您将采样时间指定为 `-1` 时，该模块将根据模块在模型中的上下文继承其采样时间。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

订阅 MQTT 主题并从代理接收消息

使用 MQTT Subscribe 模块在指定主题上从消息队列遥测传输 (MQTT) 代理接收消息。
