---
type: simulink-block
title: 'Call Service'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Access in MATLAB'
documentation_page: 'callserviceros1'
documentation_source_path: 'ref/callserviceros1.html'
language: zh-CN
chinese_source: worker-translation
---

# Call Service

## 端口

### 输入

### **Req** — 请求消息 nonvirtual bus

请求消息，指定为 nonvirtual bus。请求消息类型对应于您的服务类型。要生成一个空请求消息总线并用数据填充，请使用 Blank Message 模块。

**数据类型：** `bus`
### 输出

### **Resp** — 响应消息 nonvirtual bus

响应消息，作为 nonvirtual bus 返回。响应基于输入 **Req** 消息。响应消息类型对应于您的服务类型。要生成一个空响应消息总线并用数据填充，请使用 Blank Message 模块。

**数据类型：** `bus`

### **ErrorCode** — 服务调用的错误条件 integer

服务调用的错误条件，指定为 integer。每个 integer 对应于服务连接的不同错误条件或服务调用的状态。如果发生错误条件，**Resp** 输出最后一条响应消息，或者如果之前未收到响应，则输出空白消息。

| 错误代码 | 条件 |
| --- | --- |
| `0` | 服务响应已成功获取，并可在 `Resp` 输出中使用。 |
| `1` | 未在指定的 `Connection timeout` 内建立连接。 |
| `2` | 未收到来自服务器的响应。 |
| `3` | 服务调用因未知原因失败。 |

#### 依赖关系

当 **Show ErrorCode output port** 复选框为 `on` 时，此输出启用。

**数据类型：** `uint8`

## 参数

### **Source** — 指定服务名称的来源 `Select from ROS network` | `Specify your own`

指定服务名称的来源：

- `Select from ROS network`
  — 使用 **Select** 选择服务名称。**Name** 和 **Type** 参数将自动设置。您必须连接到 ROS 网络。
- `Specify your own`
  — 在 **Name** 中输入服务名称，并在 **Type** 中指定其服务类型。您必须完全匹配服务名称。

### **Name** — 服务名称 character vector

服务名称，指定为 character vector。服务名称必须与 ROS 服务服务器上可用的服务名称匹配。要查看 ROS 网络中的有效服务列表，请参阅 `rosservice`。

### **Type** — 服务类型 character vector

服务类型，指定为 character vector。每个服务名称都有对应的类型。

### **Connection timeout** — 服务服务器连接超时 `5`（默认值） | positive numeric scalar

服务服务器连接超时，指定为 positive numeric scalar，单位为 seconds。如果在此时间内无法与 ROS 服务服务器建立连接，则 **ErrorCode** 输出 1。

### **Keep persistent connection** — 保持与服务服务器的连接 `off`（默认值） | `on`

选中此复选框以保持与 ROS 服务服务器的持久连接。当为 `off` 时，每次将请求消息输入到 **Req** 时，该模块都会创建一个服务客户端。

### **Show ErrorCode output port** — 启用错误代码输出端口 `on`（默认值） | `off`

选中此复选框以输出 **ErrorCode** 输出。如果发生错误条件，**Resp** 输出最后一条响应消息，或者如果之前未收到响应，则输出空白消息。

## 所属库

ROS Toolbox / ROS

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

在 ROS 网络中调用服务

Call Service 模块接收 ROS 服务请求消息，将其发送到 ROS 服务服务器，并等待响应。使用 `rosinit` 连接到 ROS 网络。在使用此模块之前，应在网络中的某处设置 ROS 服务器。使用 `rosservice` 检查 ROS 网络中可用的服务。使用 `rossvcserver` 在 MATLAB® 中设置服务服务器。

在模块掩码中指定 ROS 服务的名称和服务类型。如果已连接到 ROS 网络，可以从可用服务列表中选择。您可以使用 Blank Message 模块创建空白服务请求或响应消息，并用数据填充。
