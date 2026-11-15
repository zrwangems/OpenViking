---
type: simulink-block
title: 'ThingSpeak Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Internet of Things'
documentation_page: 'thingspeakwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/thingspeakwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Write

## 端口

### 输入

### **varn** — 发布到 ThingSpeak 通道第 n 个变量的数据 [`1` x *N*] 向量，其中 *N* 的范围为 `1` 到 `8`

该模块在每个时间步将从此端口读取的数据发布到 ThingSpeak 通道上的第 n 个变量。模块输入的数据通道数取决于你在 **Number of variables to send** 参数中选择的变量数。例如，如果你将 **Number of variables to send** 参数设置为 `3`，该模块将启用三个输入端口，名称分别为 **var1**、**var2** 和 **var3**。

**数据类型：** `single`

### **location** — 发送位置数据 三元素数值向量

以 [*latitude*, *longitude*, *altitude*] 形式的三元素数值向量指定位置数据。然后该模块将位置数据发布到 ThingSpeak。

#### 依赖关系

要启用此端口，请在 **Optional** 选项卡上，选择 **Send location information**，并将 **Location source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`

## 参数

### 主要

### **Write API key** — ThingSpeak 通道的写入 API 密钥 字符向量

输入 ThingSpeak 通道的 16 位写入 API 密钥。

按照以下步骤获取你的 ThingSpeak 通道的 API 密钥：

1. 使用你的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取读取 API 密钥的通道。
4. 单击 **API Keys** 选项卡，然后从 **Write API Key** 参数中复制密钥。

   Raspberry Pi ThingSpeak Write API Key
5. 在你的模型中打开 ThingSpeak Read 模块，并将复制的 API 密钥粘贴到 **Write API key** 参数中。

### **Number of variables to send** — 要发布数据的 ThingSpeak 变量数 `1` (默认) | `2` | `3` | `4` | `5` | `6` | `7` | `8`

选择要从模块发布数据的 ThingSpeak 变量数。

### **Update interval** — 数据更新间隔 `60` (默认) | 非负标量

指定在 ThingSpeak 通道上更新输入数据的时间间隔。

### **Print diagnostic messages** — 将 ThingSpeak 服务器响应保存到日志文件 off (默认) | on

选择此参数以针对每个写入请求将来自 ThingSpeak 服务器的响应保存到日志文件。日志文件的名称格式为 `<model_name>.log`。

### 可选

### **Send location information** — 发送位置信息 off (默认) | on

选择此参数以将位置信息发送到 ThingSpeak 通道。

### **Coordinate source** — 位置数据来源 `Block dialog` (默认) | `Input port`

将位置数据的来源选择为以下之一：

- `Block dialog` — 使用 **Location (latitude, longitude, altitude)** 参数指定位置。
- `Input port` — 使用 **location** 输入端口指定位置。

使用十进制度数表示法指定 *latitude* 和 *longitude*，并使用 meters 指定 *altitude*。例如：

- 地下最低的人类规模点，位于南非 Carletonville 的 TauTona 矿，是 [`-26.416111,27.4275,-3900`]。
- 从海平面测量的最高点，位于尼泊尔珠穆朗玛峰的峰顶，是 [`27.988056,86.925278,8848`]。

### **Coordinates (latitude, longitude, altitude)** — 位置信息 [`42.29971`, `-71.350719`, `69.29`] (默认) | 三元素数值向量

以 [*latitude*, *longitude*, *altitude*] 形式的三元素数值向量输入位置信息，以将位置信息发布到 ThingSpeak 通道。

#### 依赖关系

要启用此参数，请将 **Coordinate source** 设置为 `Block dialog`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Internet Of Things

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

使用 ThingSpeak 将数据发布到物联网

ThingSpeak Write 模块使用 ThingSpeak™ 将来自目标硬件的输入数据发布到物联网 (IoT)。

ThingSpeak 是一个开放式 IoT 平台，具有 MATLAB® 分析功能，允许你收集并将传感器数据存储在云中，并开发 IoT 应用程序。ThingSpeak IoT 平台提供了一些应用程序，允许你在 MATLAB 中分析和可视化数据，然后基于数据采取行动。有关如何使用 ThingSpeak 的详细信息，请参阅 ThingSpeak Apps, Plugins, and Tutorials。
