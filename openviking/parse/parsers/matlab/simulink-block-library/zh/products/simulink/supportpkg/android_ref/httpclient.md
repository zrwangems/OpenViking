---
type: simulink-block
title: 'HTTP Client'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'httpclient'
documentation_source_path: 'supportpkg/android_ref/httpclient.html'
language: zh-CN
chinese_source: worker-translation
---

# HTTP Client

## 端口

### 输入

### **URL** — 请求 URL 的路径 character vector

该模块输入服务器的 URL。

**提示**

如果使用 String 库模块创建 URL，请使用 String to ASCII 模块将字符串转换为 `uint8` 向量。HTTP Client 模块需要将 URL 作为 `uint8` 向量输入。

**数据类型：** `uint8`

### **Payload** — 请求负载 character vector

该模块输入 Android 设备作为请求负载发送到远程服务器的数据。

#### 依赖关系

- 要启用此端口，请选择 **请求具有负载输入**，并将其设置为以下任一参数：

  - `application/json`
  - `text/plain`

**数据类型：** `uint8`

### **R** — 图像矩阵的红色分量

该模块输入图像的红色分量。该矩阵与输入 **G** 和 **B** 的大小相同。

#### 依赖关系

- 要启用此端口，请选择 **请求具有负载输入**，并将其设置为 `image/jpeg`。

**数据类型：** `uint8`

### **G** — 图像矩阵的绿色分量

该模块输入图像的绿色分量。该矩阵与输入 **R** 和 **B** 的大小相同。

#### 依赖关系

- 要启用此端口，请选择 **请求具有负载输入**，并将其设置为 `image/jpeg`。

**数据类型：** `uint8`

### **B** — 图像矩阵的蓝色分量

该模块输入图像的蓝色分量。该矩阵与输入 **R** 和 **G** 的大小相同。

#### 依赖关系

- 要启用此端口，请选择 **请求具有负载输入**，并将其设置为 `image/jpeg`。

**数据类型：** `uint8`

### 输出

### **Status** — HTTP 请求的状态 `0` | `1` | `2`

该端口输出 HTTP 请求的状态，即对远程服务器请求的状态。

- `0` — 表示与发送到服务器的请求相关的任何失败。
- `1` — 表示发送到服务器的请求成功。
- `2` — 表示响应无效，因为模块等待向服务器发出下一个 HTTP 请求。

**数据类型：** `uint8`

### **Message** — 消息数据 scalar

如果 **Status** 端口输出 `0`，则 **Message** 端口输出错误消息。

#### 依赖关系

- 要启用此端口，请清除 **请求具有响应输出**。

**数据类型：** `uint8`

### **Response** — 来自服务器的响应消息 character vector

对于每个成功发送到服务器的 HTTP 请求，该端口输出响应消息。如果 **Status** 端口输出 `0`，则 **Response** 端口输出错误消息。如果 **Status** 端口输出 `1`，则 **Response** 端口输出响应消息。

#### 依赖关系

- 要启用此端口，请选择 **请求具有响应输出**。

**数据类型：** `uint8`

### **Data Size** — 来自服务器的响应数据大小 scalar

该端口输出从服务器接收的响应消息数据的大小。

#### 依赖关系

- 要启用此端口，请选择 **请求具有响应输出**。

**数据类型：** `int32`

## 参数

### 主要

### **请求方法** — HTTP 请求方法 `GET`（默认）| `POST` | `PUT`

选择从 Android 设备向服务器发送请求消息时使用的 HTTP 请求方法。

- `GET` — 此方法从指定资源请求数据。
- `POST` — 此方法向服务器发送数据以创建或更新资源。
- `PUT` — 此方法向服务器发送数据以创建或更新资源。

### **更新间隔** — HTTP 请求之间的间隔 `2`（默认）| positive integer

指定后续 HTTP 请求之间等待的秒数。

### **请求具有负载输入** — 请求负载输入 `off`（默认）| `on`

如果 HTTP 请求包含以下任一格式的负载数据，请选择此选项：JSON、文本或图像。

### **内容类型** — 输入负载内容类型 `application/json`（默认）| `text/plain` | `image/jpeg`

选择 HTTP 请求的负载输入的内容类型。在 POST 或 PUT 等 HTTP 请求中，客户端会告知远程服务器实际发送的数据类型。

#### 依赖关系

- 要启用此参数，请选择 **请求具有负载输入**。

### **请求具有响应输出** — 响应负载输出 `off`（默认）| `on`

如果来自服务器的 HTTP 响应包含负载数据，请选择此选项。

### **输出消息的最大长度** — 最大数据长度 `256`（默认）| positive integer

输入预期从服务器接收的负载数据响应的最大长度。

#### 依赖关系

- 要启用此参数，请选择 **请求具有响应输出**。

### **Accept** — 输出负载数据类型 `application/json`（默认）| `text/plain`

选择客户端可以理解的 HTTP 响应输出负载数据的格式。

#### 依赖关系

- 要启用此参数，请选择 **请求具有响应输出**。

### 高级

### **自定义标头数量** — HTTP 请求标头 `0`（默认）| `1` | `2` | `3`

选择自定义 HTTP 请求标头的数量。您可以自定义一个包含一个或多个键值对的标头，以提供有关请求的更多信息。值 `0` 表示 HTTP 请求没有自定义标头。

### **Key** — HTTP 请求标头键 clear（默认）| character vector

指定 HTTP 请求标头键属性。当在 **自定义标头数量** 参数中指定非 `0` 的值时，模块会生成相同数量的标头键。例如，如果将 **自定义标头数量** 设置为 `2`，模块会生成两个 **Key** 参数。

#### 依赖关系

- 要启用此参数，请将 **自定义标头数量** 设置为 `1`、`2` 或 `3`。

### **Value** — HTTP 请求标头值 clear（默认）| character vector

指定自定义 HTTP 请求标头键的值。当在 **自定义标头数量** 参数中指定非 `0` 的值时，模块会生成相同数量的标头值。例如，如果将 **自定义标头数量** 设置为 `3`，模块会生成三个 **Value** 参数。

#### 依赖关系

- 要启用此参数，请将 **自定义标头数量** 设置为 `1`、`2` 或 `3`。

## 所属库

Simulink Support Package for Android Devices / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

通过 URL 连接从 HTTP 服务器发送和接收数据

使用 HTTP Client 模块通过 HTTP 协议从远程服务器发送和接收文本等数据。还可以使用该模块将图像发送到远程服务器。Android® 设备作为客户端，可以通过统一资源定位符 (URL) 连接向远程服务器发送 HTTP 请求。该模块支持 HTTP GET、POST 和 PUT 方法。

**注意**

在 Simulink® 模型中只能使用一个 HTTP Client 模块，并将该模型部署到 Android 设备上。
