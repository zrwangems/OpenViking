---
type: simulink-block
title: 'Send Service Response'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'sendserviceresponseros2'
documentation_source_path: 'ref/sendserviceresponseros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Send Service Response

## 端口
```yaml
ports:
- name: Resp
  summary: 要发送给客户端的服务响应消息，非虚拟总线
  direction: input
```

### 输入

### **Resp** — 要发送给客户端的服务响应消息，非虚拟总线

要发送给服务客户端的服务响应消息，指定为非虚拟总线。响应消息类型基于配对的 Receive Service request 模块中指定的服务类型。
## 参数
```yaml
parameters:
- name: Name
  summary: 服务名称 只读：字符向量
  group: ''
- name: Type
  summary: 服务类型 只读：字符向量
  group: ''
- name: Paired Receive Request Block
  summary: 配对的 Receive Service Request 模块的路径 模块路径
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Name** — 服务名称 只读：字符向量

此参数为只读。

服务名称，指定为字符向量。这是服务服务器的名称，客户端随后可以使用该名称进行连接并发送服务请求。

#### 依赖关系

服务名称与配对的 Receive Service request 模块中指定的名称相同。

### **Type** — 服务类型 只读：字符向量

此参数为只读。

服务类型，指定为字符向量。每个服务名称都有对应的类型。点击 **Select** 按钮可从支持的 ROS 2 服务类型完整列表中进行选择。

如果您使用的是自定义服务类型，请先使用 `ros2genmsg` 函数构建关联的服务定义。然后，您可以使用 **Select** 按钮指定自定义服务类型。

#### 依赖关系

服务类型与配对的 Receive Service request 模块中指定的类型相同。

### **Paired Receive Request Block** — 配对的 Receive Service Request 模块的路径 模块路径

与此 Send Service Response 模块配对的 Receive Service Request 模块的路径。要首次创建配对的 Receive Service Request，请点击 `Create paired Receive Request block`。

创建配对的 Receive Service Request 模块后，点击该路径将显示并高亮模型中的 Receive Service Request 模块。

#### 提示

- 为正确实现服务服务器，请仅使用 `Click to create paired Receive Request block` 来创建与此 Send Service Response 模块关联的 Receive Service Request。不要从库中添加 Send Service Response 模块。
## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 生成的服务服务器遵循基于速率的执行方式，而非事件驱动的执行方式。

## 版本历史

**在 R2024a 中引入**

## 描述

向 ROS 2 服务客户端发送服务响应

在同一模型中使用 Receive Service Request 模块和 Send Service Response 模块，以在 Simulink® 中实现 ROS 2 服务服务器。Send Service Response 模块使您能够在处理客户端发送的服务请求后，向服务客户端发送服务响应消息。要配置服务参数并接收服务请求，您必须首先创建配对的 Receive Service Request 模块，并在 Receive Service Request 模块封装中指定所有参数。然后，您可以在模型中处理传入的服务请求，构造适当的响应，然后使用 Send Service Response 将服务响应返回给客户端。服务服务器与 Simulink 模型的节点相关联。

**注意**

对于您在模型中添加的每个 Send Service Response 模块，您必须仅通过点击模块封装中的 **Click to create paired Receive Request block** 来创建配对的 Receive Service Request 模块。
