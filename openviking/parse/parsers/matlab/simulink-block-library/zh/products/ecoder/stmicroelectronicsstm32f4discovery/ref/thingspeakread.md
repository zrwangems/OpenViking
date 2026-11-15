---
type: simulink-block
title: 'ThingSpeak Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'thingspeakread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/thingspeakread.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Read

## 端口

### 输出

### **Data** — 从 ThingSpeak 通道的指定字段读取的数据 标量

在每个时间步，该端口输出从 **Field Number** 参数中指定的字段读取的数据。

**数据类型：** `single`

### **Status** — 每个读取请求的状态 标量

该端口输出下表中所述的每个读取请求的状态：

**返回状态码**

| **Status** | 描述 |
| --- | --- |
| 200 | OK 或成功 |
| -301 | 无法连接到 ThingSpeak |
| -303 | 无响应/无法解析来自 ThingSpeak 的响应 |

#### 依赖关系

仅当您选择 **Output Status** 参数时，此端口才会出现。

**数据类型：** `single`

## 参数

### **Channel ID** — 模块从中读取数据的通道 ID `65531`（默认） | `positive integer`

指定模块从中读取数据的通道 ID。

如果您不知道通道的通道 ID：

1. 使用您的 MathWorks® 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要从中读取数据的通道。
4. 单击 **Channel Settings** 选项卡。
5. 从 **Channel ID** 参数复制通道 ID。
6. 在您的模型中打开 ThingSpeak Read 模块，并将复制的 ID 粘贴到 **Channel ID** 参数。

### **Channel access** — 通道的共享设置 `Public`（默认） | `Private`

指定您的通道是私有还是公共。

如果您不知道通道的共享设置：

1. 使用您的 MathWorks® 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要获取共享状态的通道。
4. 单击 **Sharing** 选项卡。使用该选项卡中选择的选项设置 **Channel Access**。

   - **Keep channel view private**：将 **Channel Access** 设置为 `Private`。只有您能够查看通道数据。
   - **Share channel view with everyone**：将 **Channel Access** 设置为 `Public`。任何浏览 ThingSpeak 网站的人都可以查看通道数据。
   - **Share channel view only with the following users**：将 **Channel Access** 设置为 `Private`。有权访问共享通道的用户只能看到通道的私有视图；他们无法添加通道、查看警报或查看许可证信息。

### **Field number** — 模块从中读取数据的字段 `1`（默认） | 1 到 8 之间的整数

选择模块从中读取数据的 ThingSpeak 通道字段。

### **Output Status** — 启用输出状态 `off`（默认） | `on`

当您选择 **Output Status** 参数时，模块会配置一个输出端口 **Status**。该端口输出状态消息。

### **Sample time** — 模块读取数据的时间间隔 `20`（默认） | `-1` | `nonnegative integer`

指定模块从 ThingSpeak 通道读取数据的频率。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7 Simulink Support Package for Arduino Hardware / Ethernet Shield

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

读取存储在 ThingSpeak 通道中的数据

ThingSpeak Read 模块从 ThingSpeak.com 网站上的 ThingSpeak™ 通道读取数据。

ThingSpeak 是一项 IoT 分析平台服务，允许您在云中聚合、可视化和分析实时数据流。您可以从您的设备向 ThingSpeak 发送数据，创建实时数据的即时可视化，并使用 Web 服务发送警报。借助 ThingSpeak 内的 MATLAB® 分析功能，您可以编写并执行 MATLAB 代码以执行预处理、可视化和分析。

有关如何使用 ThingSpeak 的更多信息，请参阅 Apps、Plugins 或 Tutorials。
