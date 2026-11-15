---
type: simulink-block
title: 'WiFi ThingSpeak Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifithingspeakread'
documentation_source_path: 'supportpkg/arduino_ref/wifithingspeakread.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi ThingSpeak Read

## 端口

### 输出

### **fieldn** — 从 ThingSpeak 通道的第 n 个字段读取的数据 [`1` x *N*] 向量，其中 *N* 的范围为 [`1` 到 `8`]

模块在每个时间步输出从 ThingSpeak 通道中第 n 个字段读取的数据。模块输出端的数据通道数取决于您在 **Fields to read** 参数中输入的字段数。例如，如果将 **Fields to read** 参数设置为 [`1 4 5`]，则模块会启用三个输出端口，端口名称为 **field1**、**field4** 和 **field5**。如果从通道接收到的数据为 null，则模块输出 `0`。

**数据类型：** `single`

### **status** — 每个读取请求的 ThingSpeak 服务器响应 标量

模块在每个时间步输出读取请求的 ThingSpeak 服务器响应。该响应以 HTTP 状态代码的形式接收。HTTP 状态代码 `200` 表示读取请求已成功完成。有关 HTTP 状态代码的详细信息，请参阅 `matlab.net.http.StatusCode`。

如果接收到的数据为 null，则该端口输出 `0`。

**示例：** HTTP 状态代码 `200` 表示读取请求已成功完成。而 HTTP 状态代码 `204` 表示在数据通道上接收到的数据为 null。

**数据类型：** `single`

## 参数

### **Channel ID** — 模块从中读取数据的通道 ID `12397` (默认) | 任何正整数

指定模块从中读取数据的通道 ID。

如果您不知道通道的通道 ID：

1. 使用您的 MathWorks® 账户登录到 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要从中读取数据的通道。
4. 单击 **Channel Settings** 选项卡。
5. 从 **Channel ID** 参数复制通道 ID。
6. 在模型中打开 ThingSpeak Read 模块，并将复制的 ID 粘贴到 **Channel ID** 参数中。

### **Channel access** — 通道的共享设置 `Public` (默认) | `Private`

指定您的通道是私有还是公共。

如果您不知道通道的共享设置：

1. 使用您的 MathWorks 账户登录到 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取共享状态的通道。
4. 单击 **Sharing** 选项卡。使用该选项卡中选择的选项设置 **Channel Access**。

   - **Keep channel view private**：将 **Channel Access** 设置为 `Private`。只有您可以查看通道数据。
   - **Share channel view with everyone**：将 **Channel Access** 设置为 `Public`。浏览 ThingSpeak 网站的任何人都可以查看通道数据。
   - **Share channel view only with the following users**：将 **Channel Access** 设置为 `Private`。有权访问共享通道的用户只能查看通道的私有视图；他们不能添加通道、查看提醒或查看许可证信息。

### **Read API key** — 用于从私有或共享通道读取数据的密钥 `ABCDEFGHIJK` (默认) | 任何有效的 Read API Key

当您使用 ThingSpeak API 或 MATLAB® 代码从通道读取数据时，需要相应的读取权限。16 位 API 密钥允许您从私有或共享通道读取数据。从公共 ThingSpeak 通道读取数据不需要 API 密钥。

如果您不知道通道的读取 API 密钥：

1. 使用您的 The MathWorks® 账户登录到 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取读取 API 密钥的通道。
4. 单击 **API Keys** 选项卡。
5. 从 **Read API Keys** 参数复制密钥。
6. 在模型中打开 ThingSpeak Read 模块，并将复制的 API 密钥粘贴到 **Read API Key** 参数中。

#### 依赖关系

- 要启用此参数，请将 **Channel access** 设置为 `Private`。

### **Fields to read** — 要读取数据的 ThingSpeak 通道字段 `1` (默认) | [`1` x *N*] 向量，其中 *N* 的范围为 [`1` 到 `8`]

输入模块从中读取数据的 ThingSpeak 通道的字段。例如，如果将此参数设置为 [`1 2 3`]，则模块从三个字段读取数据，并具有三个输出端口 `field1`、`field2` 和 `field3`。如果将此参数设置为 `1`，则模块仅从一个字段读取数据，并具有一个输出端口 `field1`。

### **Print diagnostic messages** — 将 ThingSpeak 服务器响应保存到日志文件 off (默认) | on

选择此参数可将每个读取请求的 ThingSpeak 服务器响应保存到日志文件。日志文件的名称格式为 `<model_name>.log`。

### **Sample time** — 模块从 ThingSpeak 通道读取数据的时间间隔 `60` (默认) | `-1` | 任何非负值

指定此模块从 ThingSpeak 通道读取数据的频率。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

读取存储在无线网络上的 ThingSpeak 通道中的数据

使用 WiFi ThingSpeak Read 模块，通过无线网络上的 ThingSpeak™ 从物联网网站检索数据，并将数据下载到您的 Arduino® 板。

ThingSpeak 是一个可用于物联网的应用平台。您可以围绕传感器收集的数据构建应用。ThingSpeak 包括实时数据收集、数据处理、可视化、应用和插件。

您可以通过选择 Print diagnostic messages 选项来查看 ThingSpeak 服务器对数据下载请求的响应。当您使用外部模式，或使用端口 0 的 Serial Transmit 或 Serial Receive 模块时，此选项无效。

有关如何使用 ThingSpeak 的详细信息，请参阅 ThingSpeak 应用、插件和教程。

### 支持的硬件

此表列出了 Arduino 板为 WiFi ThingSpeak Read 模块支持的硬件属性。

| 目标硬件 | 接收限制（字节数） |
| --- | --- |
| Wi-Fi® Shield | 64 bytes |
| Arduino MKR1000, Arduino MKR Wi-Fi 1010, Arduino Nano 33 IoT, Arduino compatible ESP32 – WROOM, Arduino compatible ESP32 – WROVER | 1400 bytes |

**注意**

将 ESP8266 芯片用于 Wi-Fi 连接时，不支持在 Arduino 板上部署 WiFi ThingSpeak Read 模块。
