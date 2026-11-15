---
type: simulink-block
title: 'WiFi HTTP Client'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifihttpclient'
documentation_source_path: 'supportpkg/arduino_ref/wifihttpclient.html'
language: zh-CN
chinese_source: worker-translation
---

# WiFi HTTP Client

## 端口

### 输入

### **URL** — 请求 URL 的路径 character vector

模块输入服务器的 URL。

**提示**

如果您使用 String 库模块创建 URL，请使用 String to ASCII 模块将字符串转换为 `uint8` 向量。WiFi HTTP Client 模块需要将 URL 作为 `uint8` 向量输入。

**数据类型：** `uint8`

### **Payload** — 请求 payload character vector

模块输入 Arduino 硬件作为请求 payload 发送到远程服务器的数据。

#### 依赖关系

- 要启用此端口，请选择 **Request has payload input**。

**数据类型：** `uint8`
### 输出

### **Status** — HTTP 请求的状态 `0` | `1` | `2`

该端口输出向远程服务器发出的 HTTP 请求的状态。

- `0` — 表示与发送到服务器的请求相关的任何失败。
- `1` — 表示向服务器发送的请求成功。
- `2` — 表示无效响应，因为模块正在等待向服务器发出下一个 HTTP 请求。

**数据类型：** `uint8`

### **Message** — 消息数据 scalar

如果 **Status** 端口输出 `0`，则 **Message** 端口输出错误消息。

#### 依赖关系

- 要启用此端口，请清除 **Request has response output**。

**数据类型：** `uint8`

### **Response** — 来自服务器的响应消息 character vector

对于发送到服务器的每个成功 HTTP 请求，该端口输出响应消息。如果 **Status** 端口输出 `0`，则 **Response** 端口输出错误消息。如果 **Status** 端口输出 `1`，则 **Response** 端口输出响应消息。

#### 依赖关系

- 要启用此端口，请选择 **Request has response output**。

**数据类型：** `uint8`

### **Data Size** — 来自服务器的响应数据的大小 scalar

该端口输出从服务器接收的响应消息数据的大小。

#### 依赖关系

- 要启用此端口，请选择 **Request has response output**。

**数据类型：** `int32`

## 参数

### 主要

### **Request Method** — HTTP 请求方法 `GET`（默认）| `POST` | `PUT`

选择 HTTP 请求方法，以从您的 Arduino 硬件向服务器发送请求消息。

- `GET` — 此方法从指定资源请求数据。
- `POST` — 此方法将数据发送到服务器以创建或更新资源。
- `PUT` — 此方法将数据发送到服务器以创建或更新资源。

### **Update Interval (seconds)** — HTTP 请求之间的间隔 `2`（默认）| positive integer

指定后续 HTTP 请求之间等待的秒数。

### **Request has payload input** — 请求 payload 输入 `off`（默认）| `on`

如果 HTTP 请求包含以下任一格式的 payload 数据：JSON 或文本，请选择此选项。

### **Content Type** — 输入 payload 内容类型 `text/plain`（默认）| `application/json` |

选择 HTTP 请求 payload 输入的内容类型。在 POST 或 PUT 等 HTTP 请求中，客户端会告知远程服务器实际发送的数据类型。

#### 依赖关系

- 要启用此参数，请选择 **Request has payload input**。

### **Request has response output** — 响应 payload 输出 `off`（默认）| `on`

如果来自服务器的 HTTP 响应包含 payload 数据，请选择此选项。

### **Max length of the output Message** — 最大数据长度 `256`（默认）| positive integer

输入期望从服务器接收的 payload 数据响应的最大长度。

#### 依赖关系

- 要启用此参数，请选择 **Request has response output**。

### **Accept** — 输出 payload 数据类型 `application/json`（默认）| `text/plain`

选择客户端可以理解的 HTTP 响应输出 payload 数据的格式。

#### 依赖关系

- 要启用此参数，请选择 **Request has response output**。

### **Print diagnostic messages** — 在串行端口上打印诊断消息 off（默认）| on

选择此选项可在 Arduino 串行端口上为每个 HTTP 请求打印诊断消息。

### 高级

### **Number of custom headers** — HTTP 请求标头 `0`（默认）| `1` | `2` | `3`

选择自定义 HTTP 请求标头的数量。您可以自定义包含一个或多个键值对的标头，以提供有关请求的更多信息。值 `0` 表示 HTTP 请求没有自定义标头。

### **Key** — HTTP 请求标头键 clear（默认）| character vector

指定 HTTP 请求标头键属性。当您在 **Number of custom headers** 参数中指定除 `0` 以外的值时，模块会生成相同数量的标头键。例如，如果将 **Number of custom headers** 设置为 `2`，模块会生成两个 **Key** 参数。

#### 依赖关系

- 要启用此参数，请将 **Number of custom headers** 设置为 `1`、`2` 或 `3`。

### **Value** — HTTP 请求标头值 clear（默认）| character vector

指定自定义 HTTP 请求标头键的值。当您在 **Number of custom headers** 参数中指定除 `0` 以外的值时，模块会生成相同数量的标头值。例如，如果将 **Number of custom headers** 设置为 `3`，模块会生成三个 **Value** 参数。

#### 依赖关系

- 要启用此参数，请将 **Number of custom headers** 设置为 `1`、`2` 或 `3`。

## 所属库

Simulink Support Package for Arduino Hardware / WiFi

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

通过 URL 连接从 HTTP 服务器发送和接收数据

使用 WiFi HTTP Client 模块通过 HTTP 协议从远程服务器发送和接收文本等数据。Arduino® 硬件充当客户端，可以通过统一资源定位符 (URL) 连接向远程服务器发送 HTTP 请求。该模块支持 HTTP GET、POST 和 PUT 方法。

### 支持的 Arduino 开发板

- Arduino MKR1000
- Arduino MKR WIFI 1010
- Arduino Nano 33 IoT
- Arduino compatible ESP32 – WROOM board
- Arduino compatible ESP32 – WROVER board
