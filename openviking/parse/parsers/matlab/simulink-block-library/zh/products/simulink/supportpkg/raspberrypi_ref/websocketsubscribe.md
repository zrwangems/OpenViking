---
type: simulink-block
title: 'Websocket Subscribe'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'websocketsubscribe'
documentation_source_path: 'supportpkg/raspberrypi_ref/websocketsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# Websocket Subscribe

## 端口

### 输出

### **Out** — 接收的数据行向量

WebSocket 服务器接收的数据，指定为行向量。

该模块提供一个选项，最多可添加 10 个 **Out** 端口以获取信号数据，其中每个信号都是一个 *N*×1 向量。*N* 是信号中的数据点数。

**示例：** `[1.5,3]`

#### 依赖关系

要启用该端口，请在 **Number of outputs** 参数中指定输出信号的总数。指定 **Number of outputs** 后，模块会生成相同数量的输出端口。例如，如果将 **Number of outputs** 指定为 `4`，则模块会生成四个输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — 接收数据的有效性标量

该模块输出状态，指示所接收数据的有效性。

状态为：

- `1`：有效数据
- `0`：接收的数据为空或 JSON 格式无效
- `-1`：数据字段数量不匹配

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Server IP address** — WebSocket 服务器的 IP 地址 `127.0.0.1`（默认）| 任意 IP 地址

托管 JSON 数据的 WebSocket 服务器的 IP 地址。

### **Server Port** — WebSocket 服务器上的端口号 `9000`（默认）| 任意端口号

托管 JSON 数据的 WebSocket 服务器上的端口号。

**注意**

为避免任何资源冲突，Simulink® 模型中所有 WebSocket Subscribe 模块的 **Server IP address** 和 **Server Port** 参数必须唯一。

### **Specify output info via** — 获取 JSON 数据属性的来源 `Mask Dialog`（默认）| `JSON file`

使用模块参数对话框或从 JSON 文件指定数据的属性。

- `Mask Dialog` –– 使用模块参数对话框指定信号数据总数。模块生成的输出端口数量等于所指定的信号总数。还必须使用对话框指定每个信号的数据大小和数据类型。
- `JSON file` –– 如果有一个包含信号数据的 JSON 文件，请单击 **Browse** 按钮上传该文件。成功上传文件后，模块生成的输出端口数量等于指定文件中的数据信号数量。每个信号的数据大小和数据类型从该文件继承。

### **Number of outputs** — 输出信号总数 `1`（默认）| `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

指定 WebSocket 服务器接收的输出信号总数。在此参数中指定值后，模块生成的输出端口数量等于此参数中指定的值。例如，如果将 **Number of outputs** 指定为 `4`，则模块会生成四个输出端口。

#### 依赖关系

要启用该参数，请将 **Specify output info via** 参数设置为 `Mask Dialog`。

### **Data Size** — 数据点总数 `1`（默认）

指定输出信号中的数据点总数。

#### 依赖关系

要启用该参数，请将 **Specify output info via** 参数设置为 `Mask Dialog`。

### **Data Type** — 输出信号的数据类型 `double`（默认）| `single` | `uint32` | `int32` | `uint16` | `int16` | `uint8` | `int8` | `Boolean`

输出信号的数据类型。

#### 依赖关系

要启用该参数，请将 **Specify output info via** 参数设置为 `Mask Dialog`。

### **JSON File Path** — JSON 文件的路径 有效的 JSON 文件路径

单击 **Browse** 按钮选择包含信号数据的 JSON 文件。成功上传 JSON 文件后，模块生成的输出端口数量等于指定文件中的数据信号数量。每个信号的数据大小和数据类型从该文件继承。

#### 依赖关系

要启用该参数，请将 **Specify output info via** 参数设置为 `JSON file`。

### **Sample time** — 从 WebSocket 服务器接收数据的时间间隔 `0.1`（默认）| `-1` | 任意正整数

指定模块从 WebSocket 服务器接收数据的频率。将 **Sample time** 指定为 `-1` 时，模块会根据该模块在模型中的上下文继承其采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020a 中引入**

## 描述

订阅 WebSocket 服务器接收的 JSON 数据

WebSocket Subscribe 模块订阅由 IP 地址和端口标识的 WebSocket 服务器接收的数据。接收的数据必须为 JavaScript Object Notation (JSON) 格式，WebSocket 客户端可以解释该格式以操作数据。

### WebSocket JSON 数据

此图显示具有唯一模块标签的 JSON 格式信号。

WebSocket JSON 数据
