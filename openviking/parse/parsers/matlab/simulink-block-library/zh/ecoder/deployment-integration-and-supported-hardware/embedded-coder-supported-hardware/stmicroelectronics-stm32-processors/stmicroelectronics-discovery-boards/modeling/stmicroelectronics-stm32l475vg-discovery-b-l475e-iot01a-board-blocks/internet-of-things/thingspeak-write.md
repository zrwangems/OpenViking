---
type: simulink-block
title: 'ThingSpeak Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Internet of Things'
documentation_page: 'thingspeakwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/thingspeakwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# ThingSpeak Write

## 端口

### 输入

### **Var1** — 将数据发送到指定的 ThingSpeak 通道字段 标量

输入端口，模块从该端口将数据发送到您在 Fields 参数中指定的 ThingSpeak 通道字段。如果未指定字段，模块将按顺序将数据发送到通道中的所有字段。

**数据类型：** `single`

## 参数

### 主要

### **Channel ID** — 模块将数据写入到的通道 ID `65531`（默认）| `any positive integer`

指定要写入数据的 ThingSpeak 通道。

如果您不知道通道的通道 ID：

1. 使用您的 MathWorks® 账户登录 ThingSpeak。
2. 选择 **Channels** > **My Channels**。
3. 选择要写入数据的通道。
4. 点击 **Channel Settings** 选项卡。
5. 从 **Channel ID** 参数复制通道 ID。

   ThingSpeak 通道设置
6. 在模型中打开 ThingSpeak Write 模块，并将复制的 ID 粘贴到 **Channel ID** 参数中。

### **Write API key** — ThingSpeak 通道的写入 API 密钥 `ABCDEFGHIJK`（默认）

指定 ThingSpeak 通道的写入 API 密钥。从 ThingSpeak.com 中的通道获取 **Write API Key** 参数。

为目标硬件创建 ThingSpeak 通道后：

1. 在 ThingSpeak.com 网站中，选择 **Channels** > **My Channels**。
2. 在您为此目标硬件创建的通道下，点击 **Settings**。
3. 点击 **API Keys** 选项卡。
4. 从 **Write API Key** 参数复制密钥。
5. 在模型中打开 ThingSpeak Write 模块，并将 API 密钥粘贴到 **Write API key** 参数中。

### **Number of variables** — 设置要写入的变量数目 `1`（默认）| `Integer between 1 to 8`

设置要写入的变量数目。

### **Set Minimum Update Interval** — 启用最小更新间隔 `off`（默认）| `on`

启用以设置最小更新间隔。

### **Minimum update interval** — 指定最小更新间隔 `15`（默认）| `Nonnegative value`

以 seconds 为单位指定最小更新间隔时间。

### 可选

### **Send location information** — 发送位置信息的选项 `off`（默认）| `on`

启用以发送位置信息。指定 `location source` 和 `location`。

### **Location source** — 选择位置源 `Block dialog`（默认）| `Input port`

选择位置的来源。当位置源设置为：

- `Input port` - 使用连接到 **location** 模块输入的信号指定位置。
- `Block dialog` - 使用 **Location (latitude, longitude, altitude)** 参数指定位置。

在两种情况下，将位置指定为包含三个元素的元胞数组：

```
[latitude,longitude,altitude]
```

使用十进制度数表示法指定纬度和经度。使用 meters 指定海拔。例如：

- 地下最低的人类规模点，南非 Carletonville 的 TauTona Mine：
  `[-26.416111,27.4275,-3900]`
- 从海平面测量的最高点，尼泊尔境内珠穆朗玛峰的峰顶：`[27.988056,86.925278,8848]`

### **Location** — 将位置指定为包含三个元素的元胞数组 `[ 42.29971, -71.350719, 69.29 ]`（默认）| `three-element cell array`

将位置指定为包含三个元素的元胞数组：

```
[latitude,longitude,altitude]
```

#### 依赖项

要启用此参数，请将 **Location source** 参数设置为 `Block dialog`。

### **Enable field selection** — 启用以选择要发送数据的字段 `off`（默认）| `on`

如果要指定要发送数据的字段，请启用此参数。如果未启用此参数，数据将按顺序发送到字段。

### **Fields** — 模块将数据发送到的字段 `[1]`（默认）| `Array of positive integer ranging between 1 to 8`

指定模块将数据发送到的 ThingSpeak 通道字段。

#### 依赖项

要启用此参数，请选择 **Enable field selection** 参数。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32F7 Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7 Simulink Support Package for Arduino Hardware / Ethernet Shield

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

使用 ThingSpeak 将数据发布到物联网

使用此模块通过 ThingSpeak™ 将数据从您的目标硬件发布到物联网。

ThingSpeak 是一项 IoT 分析平台服务，允许您在云中聚合、可视化和分析实时数据流。您可以从设备向 ThingSpeak 发送数据，创建实时数据的即时可视化，并使用 Web 服务发送警报。借助 ThingSpeak 内的 MATLAB® 分析功能，您可以编写并执行 MATLAB 代码来执行预处理、可视化和分析。

有关如何使用 ThingSpeak 的详细信息，请参阅应用、插件或教程。
