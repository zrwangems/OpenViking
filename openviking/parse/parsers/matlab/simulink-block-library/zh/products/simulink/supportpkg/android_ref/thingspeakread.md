---
type: simulink-block
title: 'ThingSpeak Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'thingspeakread'
documentation_source_path: 'supportpkg/android_ref/thingspeakread.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Read

## 端口

### 输出

### **Field1** — 从 ThingSpeak 通道的指定字段读取的数据（标量）

在每个时间步，该端口输出从 **Field Number** 参数中指定的字段读取的数据。如果接收到的数据为 null，则该端口输出 `0`。

**数据类型：** `single`

### **Status** — 每个读取请求的 ThingSpeak 服务器响应（标量）

该端口在每个时间步输出读取请求的 ThingSpeak 服务器响应。该响应以 HTTP 状态码形式接收。HTTP 状态码 `200` 表示读取请求已成功完成。有关 HTTP 状态码的详细信息，请参阅 `matlab.net.http.StatusCode`。

如果接收到的数据为 null，则该端口输出 `0`。

**数据类型：** `single`

## 参数

### **Channel ID** — 模块从中读取数据的通道 ID `12397`（默认）| 任意正整数

指定模块从中读取数据的通道 ID。

如果您不知道通道的通道 ID：

1. 使用您的 MathWorks® Account 登录
   ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要从中读取数据的通道。
4. 点击 **Channel Settings** 选项卡。
5. 从 **Channel ID** 参数复制通道 ID。
6. 在模型中打开 ThingSpeak Read 模块，并将复制的
   ID 粘贴到 **Channel ID** 参数。

### **Channel Access** — 通道的共享设置 `Public`（默认）| `Private`

指定您的通道是私有还是公共。

如果您不知道通道的共享设置：

1. 使用您的 MathWorks Account 登录
   ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取共享状态的通道。
4. 点击 **Sharing** 选项卡。使用该选项卡中选择的选项
   设置 **Channel Access**。

   - **Keep channel view private**：将 **Channel Access** 设置为 `Private`。只有您可以查看通道数据。
   - **Share channel view with everyone**：将 **Channel Access** 设置为 `Public`。浏览 ThingSpeak 网站的任何人都可以查看通道数据。
   - **Share channel view only with the following users**：将 **Channel Access** 设置为 `Private`。有权访问共享通道的用户只能看到通道的私有视图；他们不能添加通道、查看警报或查看许可证信息。

### **Read API Key** — 用于从私有或共享通道读取数据的密钥 `ABCDEFGHIJK`（默认）| 任何有效的 Read API Key

当您使用 ThingSpeak API 或 MATLAB 代码从通道读取数据时，您需要相应的读取权限。16 位 API 密钥允许您从私有或共享通道读取数据。您不需要 API 密钥即可从公共 ThingSpeak 通道读取。

如果您不知道通道的读取 API 密钥：

1. 使用您的 The MathWorks® Account 登录
   ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取读取 API 密钥的通道。
4. 点击 **API Keys** 选项卡。
5. 从 **Read API Keys** 参数复制密钥。
6. 在模型中打开 ThingSpeak Read 模块，并将复制的
   API 密钥粘贴到 **Read API Key** 参数。

#### 依赖项

仅当您将 **Channel Access** 参数设置为 `Private` 时，才会显示 **Read API Key** 参数。

### **Field Number** — 模块从中读取数据的字段 `1`（默认）| 1 到 8 之间的任意整数

选择模块从中读取数据的 ThingSpeak 通道字段。

### **Sample time** — 模块从 ThingSpeak 通道读取数据的时间间隔 `60`（默认）| `-1` | 任意非负值

指定此模块从 ThingSpeak 通道读取数据的频率。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取存储在 ThingSpeak 通道中的数据

ThingSpeak Read 模块从 ThingSpeak.com 网站上的 ThingSpeak™ 通道读取数据。

ThingSpeak 是一个开放的物联网 (IoT) 平台，具有 MATLAB® 分析功能，允许您在云端收集和存储传感器数据并开发 IoT 应用程序。ThingSpeak IoT 平台提供的应用程序允许您在 MATLAB 中分析和可视化数据，然后根据数据采取行动。对于与连接、通道 ID、字段和成功日志相关的错误，请参阅 Android® 设备上生成的应用程序中的 **Log** 选项卡。
