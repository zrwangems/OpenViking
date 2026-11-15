---
type: simulink-block
title: 'ThingSpeak Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'thingspeakwrite'
documentation_source_path: 'supportpkg/android_ref/thingspeakwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Write

## 端口

### 输入

### **fieldn** — 发布到 ThingSpeak 通道第 n 个变量的数据 [`1` x *N*] 向量，其中 *N* 的范围为 `1` 到 `8`

模块在每个时间步将从该端口读取的数据发布到 ThingSpeak 通道上的第 n 个变量。模块输入处的数据通道数取决于您在 **Number of fields** 参数中选择的变量数。例如，如果将 **Number of fields** 参数设置为 `3`，则模块会启用三个名称为 `field1`、`field2` 和 `field3` 的输入端口。

**数据类型：** `single`

### **location** — 发送位置数据三元素数值向量

将位置数据指定为 [*latitude*, *longitude*, *altitude*] 形式的三元素数值向量。然后，模块将位置数据发布到 ThingSpeak。

#### 依赖关系

要启用此端口，请在 **可选** 选项卡上选择 **Send location information**，并将 **Location source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`

## 参数

### 主要

### **Channel ID** — ThingSpeak 通道 ID `12397`（默认）| 正整数

输入模块从中发布数据的 ThingSpeak 通道的唯一标识号。

按照以下步骤获取 ThingSpeak 通道标识号。

1. 使用您的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择该通道以获取写入 API 密钥。
4. 单击 **Channel Settings** 选项卡，然后从 **Channel ID** 参数复制通道 ID。ThingSpeak Channel ID
5. 在模型中打开 ThingSpeak Write 模块，并将复制的 ID 粘贴到 **Channel ID** 参数中。

### **Write API key** — ThingSpeak 通道的写入 API 密钥字符向量

输入 ThingSpeak 通道的 16 位写入 API 密钥。

按照以下步骤获取您的 ThingSpeak 通道的 API 密钥：

1. 使用您的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择该通道以获取 ThingSpeak 写入 API 密钥。
4. 单击 **API Keys** 选项卡，然后从 **Write API Keys** 参数复制密钥。ThingSpeak Write API Key
5. 在模型中打开 ThingSpeak Write 模块，并将复制的 API 密钥粘贴到 **Write API key** 参数中。

### **Number of fields** — 要发布数据的 ThingSpeak 字段数 `1`（默认）| `2` | `3` | `4` | `5` | `6` | `7` | `8`

选择模块将数据写入的 ThingSpeak 通道字段。例如，如果将此参数设置为 `3`，则模块有三个输入端口 `field1`、`field2` 和 `field3`。如果将此参数设置为 `1`，则模块只有一个输入端口 `field1`。

### **Update interval (seconds)** — 数据更新间隔 `60`（默认）| 非负标量

指定在 ThingSpeak 通道上更新输入数据的时间间隔。

### 可选

### **Send location information** — 发送位置信息 off（默认）| on

选择此参数以将位置信息发送到 ThingSpeak 通道。

### **Location source** — 位置数据的来源 `Block dialog`（默认）| `Input port`

将位置数据的来源选择为以下之一：

- `Block dialog` — 使用 **Location (latitude, longitude, altitude)** 参数指定位置。
- `Input port` — 使用 **location** 输入端口指定位置。

使用十进制度数表示法指定 *latitude* 和 *longitude*，使用米指定 *altitude*。例如：

- 地下可供人类到达的最低点，南非 Carletonville 的 TauTona Mine，为 [`-26.416111,27.4275,-3900`]。
- 从海平面测量的最高点，尼泊尔珠穆朗玛峰的峰顶，为 [`27.988056,86.925278,8848`]。

### **Location (latitude, longitude, altitude)** — 位置信息 [`42.29971`, `-71.350719`, `69.29`]（默认）| 三元素数值向量

将位置信息输入为 [*latitude*, *longitude*, *altitude*] 形式的三元素数值向量，以将位置信息发布到 ThingSpeak 通道。

#### 依赖关系

要启用此参数，请将 **Location source** 设置为 `Block dialog`。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

使用 ThingSpeak 将数据发布到物联网

ThingSpeak Write 模块使用 ThingSpeak™ 将目标硬件的数据发布到物联网 (IoT)。

ThingSpeak 是一个开放式 IoT 平台，具有 MATLAB® 分析功能，允许您在云中收集和存储传感器数据并开发 IoT 应用程序。ThingSpeak IoT 平台提供的应用程序允许您在 MATLAB 中分析和可视化数据，然后对数据采取措施。有关如何使用 ThingSpeak 的详细信息，请参阅 ThingSpeak Apps, Plugins, and Tutorials。
