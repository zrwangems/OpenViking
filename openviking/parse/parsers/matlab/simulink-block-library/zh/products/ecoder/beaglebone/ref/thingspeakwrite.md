---
type: simulink-block
title: 'ThingSpeak Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'thingspeakwrite'
documentation_source_path: 'beaglebone/ref/thingspeakwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Write

## 端口

### 输入

### **varn** — 发布到 ThingSpeak 通道第 n 个变量的数据 [`1` x *N*] 向量，其中 *N* 的范围为 `1` 到 `8`

该模块在每个时间步将数据发布到 ThingSpeak 通道中的第 n 个变量。模块输入端的数据通道数量取决于您在 **要发送的变量数量** 参数中选择的变量数量。例如，如果您将 **要发送的变量数量** 参数设置为 `3`，则该模块会启用三个输入端口，端口名称为 **var1**、**var2** 和 **var3**。

**数据类型：** `single`

### **location** — 发送位置数据三元素数值向量

该模块发送指定为 [*latitude*, *longitude*, *altitude*] 形式的三元素数值向量的位置数据。

#### 依赖项

- 要启用此端口，请在 **可选** 选项卡上选择 **发送位置信息**，并将 **坐标源** 参数设置为 `Input port`。

**数据类型：** `single` | `double`

## 参数

### 主要

### **更新 URL** — 从 ThingSpeak 网站添加 URL https://api.thingspeak.com/update (默认) | char vector

在 ThingSpeak.com 中从 **通过 POST 或 GET 发送数据到** 参数输入 URL。要了解该 URL：

1. 在 ThingSpeak.com 网站中，选择 **频道** > **我的频道**。
2. 在您为此目标硬件创建的通道下，单击 **设置**。
3. 单击 **数据导入/导出** 选项卡。
4. 从 **通过 POST 或 GET 发送数据到** 参数复制 URL。
5. 在您的 Simulink® 模型中打开 ThingSpeak Write 模块，并将 URL 粘贴到 **更新 URL** 参数中。

### **写入 API 密钥** — ThingSpeak 通道的写入 API 密钥 无默认值 (默认) | character vector

输入 ThingSpeak 通道的 16 位写入 API 密钥。

按照以下步骤了解您的 ThingSpeak 通道的 API 密钥。

1. 使用您的 MATLAB 账户登录到 ThingSpeak。
2. 选择 **频道** > **我的频道**。
3. 选择要获取写入 API 密钥的通道。
4. 单击 **API 密钥** 选项卡，并从 **写入 API 密钥** 参数中复制密钥。写入 API 密钥
5. 在您的模型中打开 ThingSpeak Write 模块，并将复制的 API 密钥粘贴到 **写入 API 密钥** 参数中。

### **要发送的变量数量** — 要发布数据的 ThingSpeak 变量数量 `1` (默认) | `2` | `3` | `4` | `5` | `6` | `7` | `8`

选择要从模块发布数据的 ThingSpeak 变量数量。

### **更新间隔 (seconds)** — 数据更新间隔 `60` (默认) | 非负标量

指定输入数据在 ThingSpeak 通道上更新的时间间隔。

### **打印诊断消息** — 将 ThingSpeak 服务器响应保存到日志文件 Off (默认) | On

选择此参数可将每个写入请求的 ThingSpeak 服务器响应保存到日志文件。日志文件的名称格式为 `<model_name>.log`。

### 可选

### **发送位置信息** — 发送位置信息 Off (默认) | On

选择此参数可将位置信息发送到 ThingSpeak 通道。

### **坐标源** — 位置数据的来源 `Block dialog` (默认) | `Input port`

选择位置数据的来源。

- `Block dialog` — 使用 **位置 (latitude, longitude, altitude)** 参数指定位置。
- `Input port` — 使用 **location** 输入端口指定位置。

使用十进制度数表示法指定 *latitude* 和 *longitude*，而使用 meters 指定 *altitude*。例如，

- 地下最低的人类规模点，位于南非 Carletonville 的 TauTona Mine，为 [`-26.416111,27.4275,-3900`]。
- 从海平面测量的最高点，尼泊尔珠穆朗玛峰峰顶，为 [`27.988056,86.925278,8848`]。

### **坐标 (latitude, longitude, altitude)** — 位置信息 [`42.29971`, `-71.350719`, `69.29`] (默认) | 三元素数值向量

以 [*latitude*, *longitude*, *altitude*] 形式的三元素数值向量输入位置信息，以更新 ThingSpeak 通道。

#### 依赖项

- 要启用此参数，请将 **坐标源** 设置为 `Block dialog`。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

使用 ThingSpeak 将数据发布到物联网

ThingSpeak Write 模块使用 ThingSpeak™ 将来自目标硬件的输入数据发布到物联网 (IoT)。

ThingSpeak 是一个开放的物联网 (IoT) 平台，具有 MATLAB® 分析功能，允许您在云中收集和存储传感器数据，并开发 IoT 应用。ThingSpeak IoT 平台提供的应用允许您在 MATLAB 中分析和可视化数据，然后根据数据采取行动。有关如何使用 ThingSpeak 的详细信息，请参阅 ThingSpeak 应用、插件和教程。
