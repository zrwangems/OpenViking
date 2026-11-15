---
type: simulink-block
title: 'HTTP Client'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'httpclient'
documentation_source_path: 'supportpkg/raspberrypi_ref/httpclient.html'
language: zh-CN
chinese_source: worker-translation
---

# HTTP Client

## 端口

### 输入

### **URL** — 服务器的 URL 字符向量

在此端口以 `uint8` 向量输入的形式指定服务器的 URL。

**提示**

如果使用 String 库模块创建 URL，请使用 String to ASCII 模块将字符串转换为 `uint8` 向量。

**数据类型:** `uint8`

### **Payload** — 请求负载字符向量

在此端口指定希望 Raspberry Pi 硬件作为 HTTP 请求的一部分发送到远程服务器的数据。

#### 依赖项

- 要启用此端口，请选择 **Request has payload input**。

**数据类型:** `uint8`

### 输出

### **Status** — HTTP 请求的状态 `0` | `1` | `2`

此端口输出发送到远程服务器的 HTTP 请求的状态。

- `0` — 表示向服务器发送请求失败。
- `1` — 表示 Raspberry Pi 硬件已成功向服务器发送请求。
- `2` — 表示无效请求。该模块会等待向服务器发出下一个 HTTP 请求。

**数据类型:** `uint8`

### **Error** — 来自服务器的错误消息字符向量

此端口输出与所有通信失败相关的来自服务器的错误消息。如果 **Status** 端口输出 `0` 或 `2`，则 **Error** 端口输出相应的错误消息。

#### 依赖项

- 要启用此端口，请清除 **Request has response output**。

**数据类型:** `uint8`

### **Response** — 来自服务器的响应消息字符向量

此端口输出与所有成功 HTTP 请求相关的来自服务器的响应消息。如果 **Status** 端口输出 `0`，则 **Error** 端口输出错误消息。如果 **Status** 端口输出 `1`，则 **Response** 端口输出响应消息。

#### 依赖项

- 要启用此端口，请选择 **Request has response output**。

**数据类型:** `uint8`

### **Data Size** — 来自服务器的响应数据大小标量

此端口输出从服务器接收的响应消息数据的大小。

#### 依赖项

- 要启用此端口，请选择 **Request has response output**。

**数据类型:** `int32`

## 参数

### 主要

### **Request Method** — HTTP 请求方法 `GET` (默认) | `POST` | `PUT`

选择 HTTP 请求方法。

- `GET` — 此方法从指定资源请求数据。
- `POST` — 此方法向服务器发送数据以创建资源。
- `PUT` — 此方法向服务器发送数据以更新资源。

### **Update Interval (seconds)** — HTTP 请求之间的间隔 `2` (默认) | 正整数

指定后续 HTTP 请求之间等待的秒数。

### **Request has payload input** — 请求中的负载输入 `off` (默认) | `on`

如果 HTTP 请求包含 JSON 或文本格式的负载数据，请选择此选项。

### **Content Type** — 输入负载内容类型 `application/json` (默认) | `text/plain`

选择 HTTP 请求中负载输入的内容类型。如果选择 POST 或 PUT 请求方法，客户端会根据数据直接向服务器发送内容类型信息。

#### 依赖项

- 要启用此参数，请选择 **Request has payload input**。

### **Request has response output** — 响应中的负载输出 `off` (默认) | `on`

如果来自服务器的 HTTP 响应包含负载数据，请选择此选项。

### **Maximum length of the output Message** — 输出数据的最大长度 `256` (默认) | 正整数

输入预期负载数据的最大长度。

#### 依赖项

- 要启用此参数，请选择 **Request has response output**。

### **Accept** — 输出数据的格式 `application/json` (默认) | `text/plain`

选择输出负载数据的格式。

#### 依赖项

- 要启用此参数，请选择 **Request has response output**。

### **Print diagnostic messages** — 在串口上打印诊断消息 `off` (默认) | `on`

选择此选项以在 Raspberry Pi 串口上为每个 HTTP 请求打印诊断消息。

### 高级

### **Number of custom headers** — HTTP 请求头 `0` (默认) | `1` | `2` | `3`

选择自定义 HTTP 请求头的数量。可以自定义一个包含一个或多个键值对的请求头，以提供有关请求的更多信息。值 `0` 表示 HTTP 请求没有自定义请求头。类似地，值 `2` 表示 HTTP 请求有两个自定义请求头。

### **Key** — HTTP 请求头键字符向量

指定 HTTP 请求头的键。模块对话框中的 **Key** 参数框数量取决于在 **Number of custom headers** 参数中指定的请求头数量。例如，如果将 **Number of custom headers** 设置为 `2`，则该模块会生成两个 **Key** 参数。

#### 依赖项

- 要启用此参数，请将 **Number of custom headers** 设置为 `1`、`2` 或 `3`。

### **Value** — HTTP 请求头值字符向量

指定自定义 HTTP 请求头键的值。模块对话框中的 **Value** 参数框数量取决于在 **Number of custom headers** 参数中指定的请求头数量。例如，如果将 **Number of custom headers** 设置为 `3`，则该模块会生成三个 **Value** 参数。

#### 依赖项

- 要启用此参数，请将 **Number of custom headers** 设置为 `1`、`2` 或 `3`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

通过 URL 连接从 HTTP 服务器发送和接收数据

使用 HTTP Client 模块通过 HTTP 协议从远程服务器发送和接收数据。可以以文本或 JSON 格式发送数据。Raspberry Pi® 硬件充当客户端，并可通过统一资源定位符 (URL) 连接向远程服务器发送 HTTP 请求。该模块支持 HTTP GET、POST 和 PUT 方法。
