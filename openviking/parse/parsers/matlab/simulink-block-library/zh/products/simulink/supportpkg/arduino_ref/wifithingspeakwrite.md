---
type: simulink-block
title: 'WiFi ThingSpeak Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifithingspeakwrite'
documentation_source_path: 'supportpkg/arduino_ref/wifithingspeakwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi ThingSpeak Write

## 端口

### 输入

### **fieldn** — 发布到 ThingSpeak 通道第 n 个 field 的数据 [`1` x *N*] 向量，其中 *N* 的范围为 [`1` 到 `8`]

该模块在每一时间步将读取的数据发布到 ThingSpeak 通道中的第 n 个 field。模块输入处的数据通道数取决于您在 **Fields to write** 参数中输入的字段数。例如，如果您将 **Fields to write** 参数设置为 [`1 4 5`]，则该模块启用三个输入端口，端口名称为 **field1**、**field4** 和 **field5**。

#### 依赖项

- 要启用此端口，请在 **Optional** 选项卡上选择 **Send location information**，并将 **Location source** 参数设置为 `Input port`。

**数据类型：** `single`

### **location** — 发送位置数据三元素数值向量

该模块以 [*latitude*、*longitude*、*altitude*] 形式的三元素数值向量发送位置数据。

#### 依赖项

- 要启用此端口，请在 **Optional** 选项卡上选择 **Send location information**，并将 **Location source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`

## 参数

### 主要

### **Channel ID** — ThingSpeak 通道 ID `12397`（默认）| 正整数

输入该模块从中读取数据的 ThingSpeak 通道的唯一标识号。

按照以下步骤查找 ThingSpeak 通道标识号。

1. 使用您的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要从中读取数据的通道。
4. 单击 **Channel Settings** 选项卡，然后从 **Channel ID** 参数中复制通道 ID。

   ThingSpeak 通道设置
5. 在模型中打开 ThingSpeak Read 模块，并将复制的 ID 粘贴到 **Channel ID** 参数中。

### **Write API key** — ThingSpeak 通道的写入 API 密钥 无默认值（默认）| 字符向量

输入 ThingSpeak 通道的 16 位写入 API 密钥。

按照以下步骤了解您的 ThingSpeak 通道的 API 密钥。

1. 使用您的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取写入 API 密钥的通道。
4. 单击 **API Keys** 选项卡，然后从 **Read API Keys** 参数中复制密钥。Arduino ThingSpeak Write API 密钥
5. 在模型中打开 ThingSpeak Read 模块，并将复制的 API 密钥粘贴到 **Read API key** 参数中。

### **Fields to write** — 要写入数据的 ThingSpeak 通道 Field `1`（默认）| [`1` x *N*] 向量，其中 *N* 的范围为 [`1` 到 `8`]

输入该模块将数据写入的 ThingSpeak 通道的 field。例如，如果您将此参数设置为 [`1 2 3`]，则该模块将数据写入三个 field，并具有三个输入端口 `field1`、`field2` 和 `field3`。如果您将此参数设置为 `1`，则该模块仅将数据写入一个 field，并具有一个输入端口 `field1`。

### **Update interval (seconds)** — 数据更新间隔 `60`（默认）| 非负整数

指定在 ThingSpeak 通道上更新输入数据的时间间隔。

### **Print diagnostic messages** — 将 ThingSpeak 服务器响应保存到日志文件 off（默认）| on

选择此参数可将每个写入请求的 ThingSpeak 服务器响应保存到日志文件。日志文件的名称格式为 `<model_name>.log`。

### 可选

### **Send location information** — 发送位置信息 off（默认）| on

选择此参数可将位置信息发送到 ThingSpeak 通道。

### **Location source** — 位置数据的来源 `Block dialog`（默认）| `Input port`

将位置数据的来源选择为以下之一：

- `Block dialog` — 使用 **Location (latitude, longitude, altitude)** 参数指定位置。
- `Input port` — 使用 **location** 输入端口指定位置。

使用 decimal degrees 表示法指定 *latitude* 和 *longitude*，并使用 meters 指定 *altitude*。例如：

- 地下最低的人类规模点，位于南非 Carletonville 的 TauTona Mine，为 [`-26.416111,27.4275,-3900`]。
- 从海平面测量的最高点，位于尼泊尔珠穆朗玛峰峰顶，为 [`27.988056,86.925278,8848`]。

### **Location (latitude, longitude, altitude)** — 位置信息 [`42.29971`, `-71.350719`, `69.29`]（默认）| 三元素数值向量

输入位置信息，形式为 [*latitude*、*longitude*、*altitude*] 的三元素数值向量，以将位置信息发送到 ThingSpeak 通道。

#### 依赖项

- 要启用此参数，请将 **Location source** 设置为 `Block dialog`。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2015b 中引入**

## 描述

使用 ThingSpeak 在无线网络上发布数据到物联网

使用 ThingSpeak Write 模块，通过 ThingSpeak™ 将 Arduino® 板上的输入数据在无线网络上发布到物联网 (IoT)。

ThingSpeak 是一个开源 IoT 平台，具有 MATLAB® 分析功能，允许您将传感器数据收集并存储在云中，并开发 IoT 应用程序。ThingSpeak IoT 平台提供的应用程序允许您在 MATLAB 中分析和可视化数据，然后基于数据执行操作。有关如何使用 ThingSpeak 的更多信息，请参阅 ThingSpeak Apps, Plugins, and Tutorials。

### 支持的硬件

此表列出了 Arduino 板为 WiFi ThingSpeak Write 模块支持的硬件属性。

| 目标硬件 | 接收限制（Number of Bytes） |
| --- | --- |
| Wi-Fi® Shield | 64 bytes |
| Arduino MKR1000, Arduino MKR Wi-Fi 1010, Arduino Nano 33 IoT, Arduino compatible ESP32 – WROOM, Arduino compatible ESP32 – WROVER | 1400 bytes |

**注意**

使用 ESP8266 芯片进行 Wi-Fi 连接不支持在 Arduino 板上部署 WiFi ThingSpeak Write 模块。
