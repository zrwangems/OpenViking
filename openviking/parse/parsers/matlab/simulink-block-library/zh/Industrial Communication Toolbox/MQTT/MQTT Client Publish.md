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

要发布到 MQTT 主题的消息。输入端口数量与您在“要发布的主题”参数中添加的主题数量相对应。当输入数据发生变化时，模块将消息发布到主题。您可以使用“仅在输入数据变化时发布”参数切换此设置。

#### 依赖关系

要启用此端口，请在 **要发布的主题** 参数中指定一个或多个主题。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string`

## 参数

### **Client** — 选择 MQTT 客户端 下拉列表

选择要与模块关联的 MQTT 客户端。选择客户端后，模块会更新 **Broker 地址** 参数。

- 要使用 **MQTT** 窗格添加客户端，请点击 **配置客户端**。有关详细信息，请参阅 Configure MQTT Client in Simulink。
- 要更新客户端列表并显示最新的 MQTT 客户端，请点击 **刷新**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ClientList` |
| **值：** | MQTT 客户端名称 |
| **数据类型：** | `character vector` | `string` |

### **Topics to publish** — MQTT 主题列表 表格

添加要发布的主题。

- 要添加主题，请点击 **添加**。此操作会在 **要发布的主题** 表格中添加一行，其中 `QoS` 和 `Retain` 分别设置为默认值 `0` 和 `off`。您必须在 `Topic name` 列中指定客户端要发布到的主题名称。每次点击 **添加** 时，模块会在 **要发布的主题** 表格中添加新行，并将序号递增 1。

  - `Sl`
    `no`：此字段不可编辑，用于指定主题的序号。序号决定了模块在输入端口接收信号的顺序。
  - `Topic name`：这是一个可编辑文本字段，用于指定主题的名称。此字段还定义了输入端口的名称。
  - `QoS`：此字段指定消息传递的服务质量 (QoS)。您可以将此字段设置为下拉列表中的以下值之一：

    - `0`：最多传递一次消息，不会更多
    - `1`：至少传递一次消息，不会更少
    - `2`：恰好传递一次消息，不会更多也不会更少
  - `Retain`：此字段指定代理是否为该主题的新订阅者保留消息。选中此复选框以保留消息。
- 要删除主题，请选择主题并点击 **删除**。

**注意**

不支持发布以 `$` 字符开头的主题名称。这些主题专供服务器端实现使用，客户端不应使用。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TopicsTable` |
| **值：** | MQTT 主题名称和信息 |
| **数据类型：** | `character vector` | `string` |

### **Publish only on input data change** — 确定何时发布消息 on（默认）| off

当您选择此参数时，模块仅在输入数据发生变化时将消息发布到主题。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `PublishOnDataChange` |
| **值：** | on（默认）| off |
| **数据类型：** | `character vector` | `string` |

### **模块采样时间** — 读取操作的采样时间 -1（默认）| 非负标量

以秒为单位定义模块的采样时间。模块在指定的采样时间同步向 MQTT 主题发布消息。有关详细信息，请参阅指定采样时间（Simulink）。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`（Simulink）函数。

要以程序化方式获取模块参数值，请使用 `get_param`（Simulink）函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | -1（默认）| 非负标量 |
| **数据类型：** | `double` |

## 所属库

Industrial Communication Toolbox / MQTT

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

向 MQTT 主题发布消息

MQTT Client Publish 模块向一个或多个 MQTT 主题发布消息。

每个输入端口向 **Topics to publish** 参数中指定的对应 MQTT 主题发布消息。

**注意**

您需要 Industrial Communication Toolbox™ 和 Simulink® 许可证才能使用此模块。

**注意**

您必须将 MQTT Client Publish 模块与一个 MQTT Client 关联。您可以使用模型的配置参数对话框中的 **MQTT** 窗格创建客户端以连接到 MQTT broker。您必须在模型中添加至少一个 MQTT Client Subscribe 或 MQTT Client Publish 模块才能启用此窗格。有关详细信息，请参阅在 Simulink 中配置 MQTT Client。
