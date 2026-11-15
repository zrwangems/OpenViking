---
type: simulink-block
title: 'WebSocket Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'websocketsubscribe'
documentation_source_path: 'supportpkg/arduino_ref/websocketsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# WebSocket Subscribe

## 端口

### 输出

### **Status** — 接收数据的有效性（标量）

该模块输出状态，用于指示接收数据的有效性。

状态为：

- `1`：有效数据
- `0`：接收数据为空或 JSON 格式无效

**数据类型：** `int8`

### **Out** — 接收数据行向量

WebSocket 服务器接收的数据，指定为行向量。

该模块提供选项，最多可添加 10 个 **Out** 端口以获取信号数据，其中每个信号为一个 *N*×1 向量。*N* 是信号中的数据点数。

**示例：** `[1.5,3]`

#### 依赖关系

要启用该端口，请在 **Number of Outputs** 参数中指定输出信号总数。指定 **Number of Outputs** 后，该模块会生成相同数量的输出端口。例如，如果将 **Number of Outputs** 指定为 `4`，则该模块会生成四个输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Port** — WebSocket 服务器上的端口号 `9000`（默认） | 任意端口号

承载 JSON 数据的 WebSocket 服务器上的端口号。

### **Specify Output Info via** — 获取 JSON 数据属性的来源 `Mask Dialog`（默认） | `JSON file`

使用模块参数对话框或从 JSON 文件获取数据的属性。

- `Mask Dialog` –– 使用模块参数对话框指定信号数据总数。该模块生成的输出端口数量等于指定的信号总数。还必须使用该对话框指定每个信号的数据大小和数据类型。
- `JSON file` –– 如果有一个包含信号数据的 JSON 文件，请单击 **Browse** 按钮上传该文件。成功上传文件后，该模块生成的输出端口数量等于指定文件中的数据信号数量。每个信号的数据大小和数据类型继承自该文件。

### **Number of Outputs** — 输出信号总数 `1`（默认） | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

WebSocket 服务器接收的输出信号总数。在此参数中指定值时，该模块生成的输出端口数量等于此参数中指定的值。例如，如果将 **Number of Outputs** 指定为 `4`，则该模块会生成四个输出端口。

#### 依赖关系

要启用该参数，请将 **Specify Output Info via** 参数设置为 `Mask Dialog`。

### **Data Size** — 数据点总数 `1`（默认）

输出信号中的数据点总数。

#### 依赖关系

要启用该参数，请将 **Specify Output Info via** 参数设置为 `Mask Dialog`。

### **Data Type** — 输出信号的数据类型 `double`（默认） | `single` | `uint32` | `int32` | `uint16` | `int16` | `uint8` | `int8` | `Boolean`

输出信号的数据类型。

#### 依赖关系

要启用该参数，请将 **Specify Output Info via** 参数设置为 `Mask Dialog`。

### **Sample time** — 从 WebSocket 服务器接收数据的时间间隔 `0.1`（默认） | `-1` | 任意正整数

指定该模块从 WebSocket 服务器接收数据的频率。将 **Sample time** 指定为 `-1` 时，该模块会根据模型内该模块的上下文继承其采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

订阅 WebSocket 服务器接收的 JSON 数据

WebSocket Subscribe 模块订阅由 IP 地址和端口标识的 WebSocket 服务器接收的数据。接收的数据必须采用 JavaScript Object Notation (JSON) 格式，WebSocket 客户端可解释该格式以操作数据。

### 支持的 Arduino 开发板

- Arduino® MKR1000
- Arduino MKR WIFI 1010
- Arduino Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board

### WebSocket JSON 数据

下图显示了 JSON 格式的信号。

WebSocket Subscribe JSON 格式
