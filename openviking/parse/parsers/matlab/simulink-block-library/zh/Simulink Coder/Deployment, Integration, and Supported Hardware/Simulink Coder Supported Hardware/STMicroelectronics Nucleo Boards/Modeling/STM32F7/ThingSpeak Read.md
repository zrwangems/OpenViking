---
type: simulink-block
title: 'ThingSpeak Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32F7'
documentation_page: 'thingspeakread'
documentation_source_path: 'nucleo/ref/thingspeakread.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Read

## 端口

### 输出

### **Data** — 从 ThingSpeak 通道指定字段读取的数据 scalar

在每个时间步，该端口输出从 **字段编号** 参数指定的字段读取的数据。

**数据类型：** `single`

### **Status** — 每个读取请求的状态 scalar

该端口输出下表中所述的每个读取请求的状态：

**返回状态码**

| **Status** | 描述 |
| --- | --- |
| 200 | OK 或成功 |
| -301 | 无法连接到 ThingSpeak |
| -303 | 无法解析来自 ThingSpeak 的响应 |
| -304 | 服务器在超时时间内无响应 |

#### 依赖关系

仅当您选择 **输出状态** 参数时，此端口才会出现。

**数据类型：** `single`

### **Received length** — 接收到的 ASCII vector 的实际长度 vector

Received length 端口输出字段的接收到的 ASCII vector 的实际长度。

#### 依赖关系

仅当您选择 **接收字段长度** 参数时，此端口才会出现。

**数据类型：** `uint8`

## 参数

### **通道 ID** — 块从中读取数据的通道 ID `65531` （默认） | `positive integer`

指定块从中读取数据的通道 ID。

如果您不知道通道的通道 ID：

1. 使用您的 MathWorks® 账户登录 ThingSpeak。
2. 选择 **通道** > **我的通道**。
3. 选择要从中读取数据的通道。
4. 单击 **通道设置** 选项卡。
5. 从 **通道 ID** 参数复制通道 ID。
6. 在模型中打开 ThingSpeak Read 模块，并将复制的 ID 粘贴到 **通道 ID** 参数中。

### **通道访问** — 通道的共享设置 `Public` （默认） | `Private`

指定您的通道是私有还是公共。

如果您不知道通道的共享设置：

1. 使用您的 MathWorks 账户登录 ThingSpeak。
2. 选择 **通道** > **我的通道**。
3. 选择要获取共享状态的通道。
4. 单击 **共享** 选项卡。使用该选项卡中选择的选项来设置 **通道访问**。

   - **保持通道视图为私有**：将 **通道访问** 设置为 `Private`。只有您可以查看通道数据。
   - **与所有人共享通道视图**：将 **通道访问** 设置为 `Public`。任何浏览 ThingSpeak 网站的人都可以查看通道数据。
   - **仅与以下用户共享通道视图**：将 **通道访问** 设置为 `Private`。有权访问共享通道的用户只能看到通道的私有视图；他们不能添加通道、查看警报或查看许可证信息。

### **字段编号** — 块从中读取数据的字段 `1` （默认） | `integer between 1 and 8`

选择块从中读取数据的 ThingSpeak 通道字段。

### **输出类型** — 选择 ThingSpeak 读取输出类型 `Numeric data (single)` （默认） | `ASCII (uint8)`

当您选择输出类型为 **Numeric data (single)** 时，模块输出所选字段数据的 `Scalar single` 值。

当您选择输出类型为 **ASCII vector (uint8)** 时，模块输出所选字段数据的 `ASCII vector`。

### **输出长度** — 指定 ThingSpeak 读取输出长度 `1` （默认） | `Any positive integer`

指定 ThingSpeak Read 模块的输出长度。

#### 依赖关系

要启用 **输出长度** 参数，请将 **输出类型** 设置为 `ASCII vector (uint8)`。

### **接收字段长度** — 选择接收字段长度 `off` （默认） | `on`

当您选择 **接收字段长度** 参数时，模块会配置一个输出端口 **Received Length**。该端口输出字段的接收到的 ASCII vector 的实际长度。

#### 依赖关系

要启用 **接收字段长度** 参数，请将 **输出类型** 设置为 `ASCII vector (uint8)`。

### **输出状态** — 启用输出状态 `off` （默认） | `on`

当您选择 **输出状态** 参数时，模块会配置一个输出端口 **Status**。该端口输出状态消息。

### **采样时间** — 块读取数据的时间间隔 `20` （默认） | `-1` | `nonnegative integer`

指定块从 ThingSpeak 通道读取数据的频率。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

读取存储在 ThingSpeak 通道中的数据

ThingSpeak Read 模块从 ThingSpeak.com 网站上的 ThingSpeak™ 通道读取数据。硬件必须连接到 Internet。该模块输出 Scalar single 和 ASCII Vector 数据。

ThingSpeak 是一项 IoT 分析平台服务，允许您在云中聚合、可视化和分析实时数据流。您可以从设备向 ThingSpeak 发送数据，创建实时数据的即时可视化，并使用 Web 服务发送警报。借助 ThingSpeak 内部的 MATLAB® 分析功能，您可以编写并执行 MATLAB 代码来执行预处理、可视化和分析。

有关如何使用 ThingSpeak 的详细信息，请参阅应用、插件或教程。
