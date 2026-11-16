---
type: simulink-block
title: 'MQTT Client Subscribe'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'MQTT'
documentation_page: 'mqttclientsubscribe'
documentation_source_path: 'ug/mqttclientsubscribe.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Client Subscribe

## 端口

### 输出

### **Topic\_*`x`*** — 来自订阅主题的当前消息向量

从订阅的 MQTT 主题读取的消息。输出端口数对应于您在 **要订阅的主题** 参数中添加的主题数。模块在指定的采样时间输出所有已订阅主题的消息。模块在此端口保持上一条消息，直到有新消息可用。

#### 依赖关系

要启用此端口，请在 **要订阅的主题** 参数中指定一个或多个主题。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string`

### **IsNew** — 指示读取的消息是否为新消息的标志 `0` | `1` | logical 向量

此端口返回 logical `1` 以指示读取的消息是新消息。当模块读取多条消息时，此端口返回 logical 值向量。例如，如果模块订阅了三个主题，并且 **IsNew** 端口返回向量 [ 0, 0, 1]，则输出指示从第三个主题读取的消息是新消息。

#### 依赖关系

要启用此端口，请在 **要订阅的主题** 参数中指定一个或多个主题。

**数据类型：** `Boolean`

## 参数

### **客户端** — 选择 MQTT 客户端下拉列表

选择要与该模块关联的 MQTT 客户端。选择客户端后，模块会更新 **代理地址** 参数。

- 要使用 **MQTT** 窗格添加客户端，请点击 **配置客户端**。有关详细信息，请参阅在 Simulink 中配置 MQTT 客户端。
- 要更新客户端列表并显示最新的 MQTT 客户端，请点击 **刷新**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ClientList` |
| **值：** | MQTT 客户端名称 |
| **数据类型：** | `character vector` | `string` |

### **要订阅的主题** — MQTT 主题列表表格

添加要订阅的主题。

- 要添加主题，请点击 **添加**。此操作会在 **要订阅的主题** 表中添加一行，其中 `Output data type` 和 `QoS` 分别设置为默认值 `double` 和 `0`。您必须在 `Topic name` 列中指定客户端要订阅的主题名称。每次点击 **添加**，模块都会在 **要订阅的主题** 表中添加新行，并将序列号递增 1。

  - `Sl`
    `no`：此字段不可编辑，用于指定主题的序列号。序列号决定模块在输出端口输出信号的顺序。
  - `Topic name`：这是一个可编辑文本字段，用于指定主题名称。此字段还定义输出端口的名称。
  - `Output data type`：此字段指定模块输出的数据类型。您可以将此字段设置为下拉列表中的以下值之一：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`single`、`double` 或 `string`。模块将从相应主题读取的消息解析为所选数据类型。
  - `QoS`：此字段指定消息传递的服务质量 (QoS)。您可以将此字段设置为下拉列表中的以下值之一：

    - `0`：至多传递一次消息，且不会更多
    - `1`：至少传递一次消息，且不会更少
    - `2`：恰好传递一次消息，不多不少
- 要删除主题，请选择这些主题并点击 **删除**。

**注意**

- MQTT Client Subscribe 模块不支持包含通配符的主题名称。
- 当您将该模块的 `Output data type` 设置为 `string` 时，必须将 Simulink 配置为使用 fixed-step discrete 求解器。要配置求解器，请打开配置参数对话框，导航到 **求解器** 窗格的 **求解器选择** 部分，并将 **类型** 设置为 `Fixed-step`，将 **求解器** 设置为 `discrete`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TopicsTable` |
| **值：** | MQTT 主题名称和信息 |
| **数据类型：** | `character vector` | `string` |

### **模块采样时间** — 读取操作的采样时间 -1（默认） | 非负标量

以秒为单位定义模块的采样时间。模块在指定的采样时间同步地从 MQTT 主题读取消息。有关详细信息，请参阅指定采样时间 (Simulink)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | -1（默认） | 非负标量 |
| **数据类型：** | `double` |

## 所属库

Industrial Communication Toolbox / MQTT

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2025a 中引入**

## 描述

从订阅的 MQTT 主题读取消息

MQTT Client Subscribe 模块订阅在 **要订阅的主题** 参数中指定的 MQTT 主题。模块从这些主题读取消息，并在对应的输出端口返回这些消息。读取操作在指定的采样时间同步进行。

**IsNew** 端口输出 Boolean 值或 Boolean 值向量，具体取决于订阅主题的数量。这些 Boolean 值指示对应主题中是否有新消息可用。

**注意**

使用此模块需要 Industrial Communication Toolbox™ 和 Simulink® 许可证。

**注意**

必须将 MQTT Client Subscribe 模块与 MQTT Client 关联。您可以使用模型配置参数对话框中的 **MQTT** 窗格创建要连接到 MQTT broker 的客户端。必须在模型中添加至少一个 MQTT Client Subscribe 或 MQTT Client Publish 模块，才能启用此窗格。有关详细信息，请参阅在 Simulink 中配置 MQTT 客户端。
