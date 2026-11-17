---
type: simulink-block
title: 'MAVLink Serializer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'MAVLink'
documentation_page: 'mavlinkserializer'
documentation_source_path: 'ref/mavlinkserializer.html'
language: zh-CN
chinese_source: worker-translation
---

# MAVLink Serializer

## 端口
```yaml
ports:
- name: Msg
  summary: MAVLink 数据包非虚拟总线
  direction: input
  data_types: bus
- name: Data
  summary: MAVLink 数据流向量
  direction: output
  data_types: uint8
- name: Length
  summary: 序列化数据的长度标量
  direction: output
  data_types: uint16
```

### 输入

### **Msg** — MAVLink 数据包非虚拟总线

作为非虚拟总线的 MAVLink 数据包。这是 MAVLink Blank Message 模块的输出，其中 Message ID、System ID 和 Component ID 的值已经初始化。Payload 总线中的字段可以在将其作为输入传递给 MAVLink Serializer 模块之前，使用 Bus Assignment 模块进行修改。

**数据类型：** `bus`
### 输出

### **Data** — MAVLink 数据流向量

输入 MAVLink 消息总线的序列化 MAVLink 数据。MAVLink 协议版本 2 会移除载荷中的尾随零。因此，序列化数据中载荷的长度可能小于该方言中 MAVLink 消息的最大载荷长度。在这种情况下，模块输出的序列化数据流会包含尾随零。

**数据类型：** `uint8`

### **Length** — 序列化数据的长度标量

序列化数据的真实长度，包括头部和载荷。根据序列化期间 MAVLink 载荷中移除了多少尾随零，该长度可能小于 MAVLink 消息的最大可能长度。

**数据类型：** `uint16`
## 参数
```yaml
parameters:
- name: MAVLink dialect source
  summary: 用于指定 MAVLink 消息定义的来源 Select from standard MAVLink dialects（默认）| Specify your own
  group: ''
- name: MAVLink dialect
  summary: 用于解析 MAVLink 消息的消息定义 common.xml（默认）| 字符串
  group: ''
- name: MAVLink version
  summary: MAVLink 协议版本 2（默认）| 1
  group: ''
- name: MAVLink Message type
  summary: MAVLink 消息 HEARTBEAT（默认）
  group: ''
```

### **MAVLink dialect source** — 用于指定 MAVLink 消息定义的来源 `Select from standard MAVLink dialects`（默认）| `Specify your own`

用于指定 MAVLink 消息定义 XML 名称的来源，指定为以下选项之一：

- `Select from standard MAVLink dialects` - 使用此选项可从 **MAVLink dialect** 参数中列出的 12 个常用消息定义 XML 名称中选择一个定义 XML。
- `Specify your own` - 在 **MAVLink dialect** 参数出现的文本框中输入 XML 名称。

### **MAVLink dialect** — 用于解析 MAVLink 消息的消息定义 `common.xml`（默认）| 字符串

用于解析 MAVLink 消息的 MAVLink 消息定义文件（.`xml`），指定为字符串。

如果 **MAVLink dialect source** 参数设置为 `Select from standard MAVLink dialects`，则需要从下拉列表中的可用消息定义名称中选择一个消息定义。

如果 **MAVLink dialect source** 参数设置为 `Specify your own`，则需要指定位于当前 MATLAB 路径上的消息定义文件（.`xml`），或者可以提供该 XML 文件的完整路径。

### **MAVLink version** — MAVLink 协议版本 `2`（默认）| `1`

用于序列化和反序列化 MAVLink 消息的 MAVLink 协议版本。

### **MAVLink Message type** — MAVLink 消息 `HEARTBEAT`（默认）

MAVLink 消息，指定为字符串。单击 **Select**，可从特定于您为 **MAVLink dialect** 和 **MAVLink version** 参数所选值的可用 MAVLink 消息完整列表中进行选择。

**数据类型：** `string`
## 所属库

UAV Toolbox / MAVLink

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法和限制：

- 为该模块生成的 C/C++ 代码只能部署在 Linux 目标或 Speedgoat 上。

## 版本历史

**在 R2020b 中引入**

## 描述

通过将 Simulink 非虚拟总线转换为 uint8 数据流，对 MAVLink 数据包的消息进行序列化

MAVLink Serializer 模块接受一个 Simulink® 非虚拟总线，并将其转换为 `uint8` MAVLink 数据流。该非虚拟总线表示一个 MAVLink 数据包，包含与所选 MAVLink 消息对应的 Message ID、System ID、Component ID、Sequence 和 Payload 信息。Payload 信息是 MAVLink 数据包总线内的另一个非虚拟总线。

MAVLink v2 会移除 payload 中的尾随零。因此，序列化后的 MAVLink 数据中 payload 的长度可能小于所选 MAVLink 消息类型的最大 payload 长度。

**Data** 端口输出 MAVLink 数据流，输出数据的长度为所选 MAVLink 消息的最大可能长度。如果序列化数据的长度小于最大可能长度，则会在数据流中添加尾随零。**Length** 端口输出序列化 MAVLink 数据的真实长度。
