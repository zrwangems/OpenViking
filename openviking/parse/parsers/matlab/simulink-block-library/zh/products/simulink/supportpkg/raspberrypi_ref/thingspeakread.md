---
type: simulink-block
title: 'ThingSpeak Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Internet of Things'
documentation_page: 'thingspeakread'
documentation_source_path: 'supportpkg/raspberrypi_ref/thingspeakread.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Read

## 端口

### 输出

### **Field1** — 从 ThingSpeak 通道的指定字段读取的数据（标量）

在每个时间步，该端口输出从 **Field Number** 参数指定的字段读取的数据。

**数据类型：** `single`

### **Status** — 每个读取请求的 ThingSpeak 服务器响应（标量）

在每个时间步，该端口输出读取请求的 ThingSpeak 服务器响应。该响应以 HTTP 状态码形式接收。HTTP 状态码 `200` 表示读取请求已成功完成。有关 HTTP 状态码的更多信息，请参阅 `matlab.net.http.StatusCode`。

**数据类型：** `single`

## 参数

### **Channel ID** — 模块从中读取数据的通道 ID `12345`（默认）| 任意正整数

指定模块从中读取数据的通道 ID。

如果您不知道通道的通道 ID：

1. 使用您的 MathWorks® 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要从中读取数据的通道。
4. 单击 **Channel Settings** 选项卡。
5. 从 **Channel ID** 参数复制通道 ID。

   ThingSpeak 通道设置
6. 在模型中打开 ThingSpeak Read 模块，并将复制的 ID 粘贴到 **Channel ID** 参数中。

### **Channel Access** — 通道的共享设置 `Public`（默认）| `Private`

指定您的通道是私有还是公共。

如果您不知道通道的共享设置：

1. 使用您的 MathWorks 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取共享状态的通道。
4. 单击 **Sharing** 选项卡。使用该选项卡中选择的选项来设置 **Channel Access**。

   - **Keep channel view private**：将 **Channel Access** 设置为 `Private`。只有您可以查看通道数据。
   - **Share channel view with everyone**：将 **Channel Access** 设置为 `Public`。任何浏览 ThingSpeak 网站的人都可以查看通道数据。
   - **Share channel view only with the following users**：将 **Channel Access** 设置为 `Private`。有权访问共享通道的用户只能看到通道的私有视图；他们不能添加通道、查看警报或查看许可证信息。

   ThingSpeak 共享设置

### **Read API Key** — 从私有或共享通道读取数据的密钥 `ABCDEFGHIJK`（默认）| 任何有效的 Read API Key

当您使用 ThingSpeak API 或 MATLAB 代码从通道读取数据时，需要相应的读取权限。16 位 API 密钥允许您从私有通道或共享通道读取数据。从公共 ThingSpeak 通道读取数据不需要 API 密钥。

如果您不知道通道的读取 API 密钥：

1. 使用您的 The MathWorks® 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取读取 API 密钥的通道。
4. 单击 **API Keys** 选项卡。
5. 从 **Read API Keys** 参数复制密钥。

   ThingSpeak Read API Key
6. 在模型中打开 ThingSpeak Read 模块，并将复制的 API 密钥粘贴到 **Read API Key** 参数中。

#### 依赖项

仅当您将 **Channel Access** 参数设置为 `Private` 时，**Read API Key** 参数才会显示。

### **Field Number** — 模块从中读取数据的字段 `1`（默认）| 1 到 8 之间的任意整数

选择模块从中读取数据的 ThingSpeak 通道字段。

### **Print diagnostic messages** — 将 ThingSpeak 服务器响应保存到日志文件 off（默认）

选择此选项以将每个读取请求的 ThingSpeak 服务器响应保存到日志文件。日志文件的名称是模型名称后跟 `.log`。

### **Sample time** — 模块从 ThingSpeak 通道读取数据的时间间隔 `60`（默认）| `-1` | 任意非负值

指定此模块从 ThingSpeak 通道读取数据的频率。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Internet Of Things

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

读取存储在 ThingSpeak 通道中的数据

ThingSpeak Read 模块从 ThingSpeak.com 网站上的 ThingSpeak™ 通道读取数据。

ThingSpeak 是一个开放式 IoT 平台，具有 MATLAB® 分析功能，允许您在云中收集和存储传感器数据并开发 IoT 应用。ThingSpeak IoT 平台提供的应用程序允许您在 MATLAB 中分析和可视化数据，然后根据数据采取行动。有关如何使用 ThingSpeak 的更多信息，请参阅 ThingSpeak 应用、插件和教程。
