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

### **Topic\_*`x`*** — 来自已订阅主题的当前消息 向量

从已订阅的 MQTT 主题读取的消息。输出端口的数量对应于您在“要订阅的主题”参数中添加的主题数量。该模块在指定的采样时间输出所有已订阅主题的消息。该模块会在此端口保持上一条消息，直到有新消息可用。

#### 依赖关系

要启用此端口，请在**要订阅的主题**参数中指定一个或多个主题。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string`

### **IsNew** — 指示读取的消息是否为新的标志 `0` | `1` | 逻辑值向量

此端口返回逻辑值 `1`，表示读取的消息是新的。当该模块读取多条消息时，该端口返回一个逻辑值向量。例如，如果该模块订阅了三个主题，并且 **IsNew** 端口返回向量 [ 0, 0, 1]，则输出表示从第三个主题读取的消息是新的。

#### 依赖关系

要启用此端口，请在**要订阅的主题**参数中指定一个或多个主题。

**数据类型：** `Boolean`

## 参数

### **Client** — 选择 MQTT 客户端 下拉列表

选择要与该模块关联的 MQTT 客户端。选择客户端后，该模块会更新 **Broker address** 参数。

- 要使用 **MQTT** 窗格添加客户端，请点击 **Configure clients**。有关详细信息，请参阅 Configure MQTT Client in Simulink。
- 要更新客户端列表并显示最新的 MQTT 客户端，请点击 **Refresh**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ClientList` |
| **值：** | MQTT 客户端名称 |
| **数据类型：** | `character vector` | `string` |

### **Topics to subscribe** — MQTT 主题列表表格

添加要订阅的主题。

- 要添加主题，请点击 **Add**。此操作会在 **Topics to subscribe** 表格中添加一行，其中 `Output data type` 和 `QoS` 分别设置为默认值 `double` 和 `0`。您必须在 `Topic name` 列中指定客户端要订阅的主题名称。每次点击 **Add** 时，模块会在 **Topics to subscribe** 表格中添加一个新行，并将序号递增 1。

  - `Sl`
    `no`：此字段不可编辑，用于指定主题的序号。序号决定了模块在输出端口输出信号的顺序。
  - `Topic name`：这是一个可编辑的文本字段，用于指定主题的名称。此字段还定义了输出端口的名称。
  - `Output data type`：此字段指定模块输出的数据类型。您可以将此字段设置为下拉列表中的以下值之一：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`、`single`、`double` 或 `string`。模块将从对应主题读取的消息解析为所选数据类型。
  - `QoS`：此字段指定消息传递的服务质量（QoS）。您可以将此字段设置为下拉列表中的以下值之一：

    - `0`：最多传递一次消息，不会更多
    - `1`：至少传递一次消息，不会更少
    - `2`：恰好传递一次消息，不会更多也不会更少
- 要删除主题，请选择主题并点击 **Delete**。

**注意**

- MQTT Client Subscribe 模块不支持包含通配符的主题名称。
- 当您将此模块的 `Output data type` 设置为 `string` 时，必须将 Simulink 配置为使用固定步长离散求解器。要配置求解器，请打开配置参数对话框，导航到 **Solver** 窗格的 **Solver selection** 部分，然后将 **Type** 设置为 `Fixed-step`，将 **Solver** 设置为 `discrete`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TopicsTable` |
| **值：** | MQTT 主题名称和信息 |
| **数据类型：** | `character vector` | `string` |

### **Block sample time** — 读取操作的采样时间 -1（默认）| 非负标量

以秒为单位定义模块的采样时间。模块在指定的采样时间同步地从 MQTT 主题读取消息。有关详细信息，请参阅 Specify Sample Time (Simulink)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

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

从订阅的 MQTT 主题读取消息

MQTT Client Subscribe 模块订阅在 **Topics to subscribe** 参数中指定的 MQTT 主题。该模块从这些主题读取消息，并在相应的输出端口返回消息。读取操作在指定的采样时间同步进行。

**IsNew** 端口根据订阅主题的数量输出一个布尔值或布尔值向量。这些布尔值指示相应主题中是否有新消息可用。

**注意**

您需要 Industrial Communication Toolbox™ 和 Simulink® 许可证才能使用此模块。

**注意**

您必须将 MQTT Client Subscribe 模块与一个 MQTT Client 关联。您可以使用模型的 Configuration Parameters 对话框中的 **MQTT** 窗格创建客户端以连接到 MQTT broker。您必须在模型中添加至少一个 MQTT Client Subscribe 或 MQTT Client Publish 模块才能启用此窗格。有关详细信息，请参阅 Configure MQTT Client in Simulink。
