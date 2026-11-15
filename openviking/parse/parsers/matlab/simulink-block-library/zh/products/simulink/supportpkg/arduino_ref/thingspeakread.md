---
type: simulink-block
title: 'ThingSpeak Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / ThingSpeak'
documentation_page: 'thingspeakread'
documentation_source_path: 'supportpkg/arduino_ref/thingspeakread.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Read

## 端口

### 输出

### **fieldn** — 从 ThingSpeak 通道第 n 个字段读取的数据 [`1` x *N*] 向量，其中 *N* 的范围为 [`1` 到 `8`]

该模块在每个时间步输出从 ThingSpeak 通道中第 n 个字段读取的数据。模块输出端的数据通道数取决于你在 **Fields to read** 参数中输入的字段数。例如，如果你将 **Fields to read** 参数设置为 [`1 4 5`]，则该模块会启用三个输出端口，端口名称为 **field1**、**field4** 和 **field5**。如果从通道接收到的数据为 null，则该模块输出 `0`。

**数据类型：** `single`

### **status** — 每个读取请求的 ThingSpeak 服务器响应，标量

该模块在每个时间步输出针对读取请求的 ThingSpeak 服务器响应。该模块以 HTTP 状态代码的形式接收响应。有关 HTTP 状态代码的详细信息，请参阅 `matlab.net.http.StatusCode`

**示例：** HTTP 状态代码 `200` 表示读取请求已成功完成。而 HTTP 状态代码 `204` 表示数据通道上接收到的数据为 null。

**数据类型：** `int16`

## 参数

### **Channel ID** — ThingSpeak 通道 ID `12397`（默认） | 正整数

输入该模块读取数据的 ThingSpeak 通道的唯一标识号。

按以下步骤查找 ThingSpeak 通道标识号。

1. 使用你的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要从中读取数据的通道。
4. 单击 **Channel Settings** 选项卡，并从 **Channel ID** 参数中复制通道 ID。

   ThingSpeak 通道设置
5. 在模型中打开 ThingSpeak Read 模块，并将复制的 ID 粘贴到 **Channel ID** 参数中。

### **Channel access** — 对 ThingSpeak 通道的访问类型 `Public`（默认） | `Private`

选择 ThingSpeak 通道的共享访问类型。

按以下步骤查找你的 ThingSpeak 通道的共享访问设置。

1. 使用你的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要查看共享状态的通道。
4. 单击 **Sharing** 选项卡。使用该选项卡中选定的选项来设置 **Channel access**。

   - **Keep channel view private**：将 **Channel access** 设置为 `Private`。只有你可以查看通道数据。
   - **Share channel view with everyone**：将 **Channel access** 设置为 `Public`。任何浏览 ThingSpeak 网站的人都可以查看通道数据。
   - **Share channel view only with the following users**：将 **Channel access** 设置为 `Private`。有权访问共享通道的用户只能查看通道，但不能添加通道、查看警报或查看许可证信息。

   ThingSpeak 通道共享设置

### **Read API key** — 用于从私有或共享 ThingSpeak 通道读取的密钥 ABCDEFGHIJKLMNO（默认） | 有效的读取 API 密钥

输入 ThingSpeak 通道的 16 位读取 API 密钥。从公共或 ThingSpeak 通道读取数据时不需要此 API 密钥。

按以下步骤了解你的 ThingSpeak 通道的 API 密钥。

1. 使用你的 MATLAB 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取读取 API 密钥的通道。
4. 单击 **API Keys** 选项卡，并从 **Read API Keys** 参数中复制密钥。

   Arduino ThingSpeak 的 Write API Key
5. 在模型中打开 ThingSpeak Read 模块，并将复制的 API 密钥粘贴到 **Read API key** 参数中。

#### 依赖项

要启用此参数，请将 **Channel access** 设置为 `Private`。

### **Fields to read** — 要读取数据的 ThingSpeak 通道字段 `1`（默认） | [`1` x *N*] 向量，其中 *N* 的范围为 [`1` 到 `8`]

输入该模块读取数据的 ThingSpeak 通道字段。例如，如果你将此参数设置为 [`1 2 3`]，则该模块从三个字段读取数据，并具有三个输出端口 `field1`、`field2` 和 `field3`。如果你将此参数设置为 `1`，则该模块仅从一个字段读取数据，并具有一个输出端口 `field1`。

### **Print diagnostic messages** — 将 ThingSpeak 服务器响应保存到日志文件 off（默认） | on

选择此参数可将每个读取请求的 ThingSpeak 服务器响应保存到日志文件。日志文件的名称格式为 `<model_name>.log`。

### **Sample time** — 模块从 ThingSpeak 通道读取数据的时间间隔 `60`（默认） | `-1` | 非负整数

输入模块从 ThingSpeak 通道读取数据的时间间隔（以秒为单位）。当你将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Ethernet Shield

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016b 中引入**

## 描述

读取存储在 ThingSpeak 通道中的数据

ThingSpeak Read 模块从 ThingSpeak™ 通道读取数据。

ThingSpeak 是一个开源物联网 (IoT) 平台，具有 MATLAB® 分析功能，可让你在云中收集和存储传感器数据，并开发 IoT 应用程序。ThingSpeak IoT 平台提供的应用程序使你能够在 MATLAB 中分析和可视化数据，然后根据数据采取行动。有关如何使用 ThingSpeak 的详细信息，请参阅 ThingSpeak 应用、插件和教程。
