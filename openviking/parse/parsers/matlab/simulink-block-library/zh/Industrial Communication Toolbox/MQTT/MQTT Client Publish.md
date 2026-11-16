---
type: simulink-block
title: 'MQTT Client Publish'
family: 'icomm'
product_id: 'icomm'
product_name: 'Industrial Communication Toolbox'
documentation_release: R2025b
official_category: 'MQTT'
documentation_page: 'mqttclientpublish'
documentation_source_path: 'ug/mqttclientpublish.html'
language: zh-CN
chinese_source: worker-translation
---

# MQTT Client Publish

## 端口

### 输入

### **Topic\_*`x`*** — 要发布到 MQTT 主题的消息 double

要发布到 MQTT 主题的消息。输入端口数量对应于在“要发布的主题”参数中添加的主题数量。当输入数据发生变化时，模块将消息发布到主题。您可以使用“仅在输入数据更改时发布”参数切换此设置。

#### 依赖项

要启用此端口，请在 **要发布的主题** 参数中指定一个或多个主题。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string`

## 参数

### **客户端** — 选择 MQTT 客户端下拉列表

选择要与模块关联的 MQTT 客户端。选择客户端后，模块将更新 **Broker 地址** 参数。

- 要使用 **MQTT** 窗格添加客户端，请点击 **配置客户端**。有关详细信息，请参阅在 Simulink 中配置 MQTT 客户端。
- 要更新客户端列表并显示最新的 MQTT 客户端，请点击 **刷新**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ClientList` |
| **值：** | MQTT 客户端名称 |
| **数据类型：** | `character vector` | `string` |

### **要发布的主题** — MQTT 主题列表表格

添加要发布的主题。

- 要添加主题，请点击 **添加**。此操作会在 **要发布的主题** 表格中添加一行，其中 `QoS` 和 `Retain` 分别设置为默认值 `0` 和 `off`。您必须在 `Topic name` 列中指定客户端要发布到的主题名称。每次点击 **添加** 时，模块都会在 **要发布的主题** 表格中添加新行，并将序列号递增 1。

  - `Sl`
    `no`：此字段不可编辑，用于指定主题的序列号。序列号决定模块在输入端口接收信号的顺序。
  - `Topic name`：这是一个可编辑文本字段，用于指定主题名称。此字段还定义输入端口的名称。
  - `QoS`：此字段指定消息传递的服务质量 (QoS)。您可以将此字段设置为下拉列表中的某个值：

    - `0`：至多一次且不超过一次地传递消息
    - `1`：至少一次且不少于一次地传递消息
    - `2`：恰好一次地传递消息，不多不少
  - `Retain`：此字段指定 broker 是否为新订阅该主题的订阅者保留消息。选中此复选框可保留消息。
- 要删除主题，请选择主题并点击 **删除**。

**注意**

以 `$` 字符开头的主题名称不支持用于发布消息。这些主题专供服务器端实现使用，客户端不应使用它们。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TopicsTable` |
| **值：** | MQTT 主题名称和信息 |
| **数据类型：** | `character vector` | `string` |

### **仅在输入数据更改时发布** — 确定何时发布消息 on（默认） | off

当您选择此参数时，模块仅在输入数据发生变化时向主题发布消息。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `PublishOnDataChange` |
| **值：** | on（默认） | off |
| **数据类型：** | `character vector` | `string` |

### **模块采样时间** — 读取操作的采样时间 -1（默认） | 非负标量

以 seconds 为单位定义模块的采样时间。模块在指定的采样时间同步地将消息发布到 MQTT 主题。有关详细信息，请参阅指定采样时间 (Simulink)。

#### 程序化使用

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

**R2025a 中引入**

## 描述

将消息发布到 MQTT 主题

MQTT Client Publish 模块将消息发布到一个或多个 MQTT 主题。

每个输入端口将消息发布到 **要发布的主题** 参数中指定的对应 MQTT 主题。

**注意**

使用此模块需要 Industrial Communication Toolbox™ 和 Simulink® 许可证。

**注意**

必须将 MQTT Client Publish 模块与一个 MQTT Client 关联。您可以使用模型的“配置参数”对话框中的 **MQTT** 窗格创建客户端以连接到 MQTT broker。必须在模型中至少添加一个 MQTT Client Subscribe 或 MQTT Client Publish 模块才能启用此窗格。有关详细信息，请参阅在 Simulink 中配置 MQTT 客户端。
