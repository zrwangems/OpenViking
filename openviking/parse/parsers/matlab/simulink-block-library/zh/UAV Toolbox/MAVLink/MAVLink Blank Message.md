---
type: simulink-block
title: 'MAVLink Blank Message'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'MAVLink'
documentation_page: 'mavlinkblankmessage'
documentation_source_path: 'ref/mavlinkblankmessage.html'
language: zh-CN
chinese_source: worker-translation
---

# MAVLink Blank Message

## 端口
```yaml
ports:
- name: Msg
  summary: MAVLink 数据包非虚拟总线
  direction: output
  data_types: bus
```

### 输出

### **Msg** — MAVLink 数据包非虚拟总线

MAVLink 数据包，以 Simulink 非虚拟总线形式返回。该总线包含以下字段：
Message ID、System ID、Component ID、Sequence 和 Payload。Payload 是另一个
非虚拟总线，对应于您在 **MAVLink message type** 参数中选择的 MAVLink 消息类型。Message ID 初始化为
所选 MAVLink 消息 ID 的数值。System ID 和 Component
ID 初始化为对应的 **System ID** 和
**Component ID** 参数。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: MAVLink dialect source
  summary: 用于指定 MAVLink 消息定义的源 Select from standard MAVLink dialects（默认）| Specify your own
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
- name: System ID
  summary: 发送方的系统 ID 1（默认）
  group: ''
- name: Component ID
  summary: 发送方的组件 ID 1（默认）
  group: ''
- name: Sample time
  summary: 输出之间的间隔 inf（默认）| 标量
  group: ''
```

### **MAVLink dialect source** — 用于指定 MAVLink 消息定义的源 `Select from standard MAVLink dialects`（默认）| `Specify your own`

用于指定 MAVLink 消息定义 XML 名称的源，指定为以下选项之一：

- `Select from standard MAVLink dialects` - 使用此选项可在
  **MAVLink dialect** 参数中列出的 12 个常用消息定义 XML 名称中选择一个定义 XML。
- `Specify your own` - 在 **MAVLink dialect** 参数出现的文本框中输入 XML 名称。

### **MAVLink dialect** — 用于解析 MAVLink 消息的消息定义 `common.xml`（默认）| 字符串

用于解析 MAVLink 消息的 MAVLink 消息定义文件（.`xml`），指定为字符串。

如果 **MAVLink dialect source** 参数设置为
`Select from standard MAVLink dialects`，您需要从下拉列表中的可用消息定义名称中选择一个消息定义。

如果 **MAVLink dialect source** 参数设置为
`Specify your own`，您需要指定位于当前 MATLAB 路径上的消息
定义文件（.`xml`），或者您可以提供该 XML 文件的完整路径。

### **MAVLink version** — MAVLink 协议版本 `2`（默认）| `1`

用于序列化和反序列化 MAVLink 消息的 MAVLink 协议版本。

### **MAVLink Message type** — MAVLink 消息 `HEARTBEAT`（默认）

MAVLink 消息，指定为字符串。点击 **Select** 可从完整的可用 MAVLink 消息列表中进行选择，该列表取决于您为 **MAVLink dialect** 和 **MAVLink
version** 参数选择的值。

**数据类型：** `string`

### **System ID** — 发送方的系统 ID `1`（默认）

MAVLink 系统 ID，指定为 1 到 255 之间的正整数。MAVLink
协议最多仅支持 255 个系统。每个 UAV 都有自己的系统 ID，但多个
UAV 可被视为一个系统。

**数据类型：** `uint8`

### **Component ID** — 发送方的组件 ID `1`（默认）

MAVLink 组件 ID，指定为 1 到 255 之间的正整数。

**数据类型：** `uint8`

### **Sample time** — 输出之间的间隔 `inf`（默认）| 标量

默认值（`inf`）表示模块输出永不改变。如果您使用此值，仿真和代码生成会更快，
因为无需重新计算模块输出。对于其他值，模块在每个 Sample time 间隔输出
一个新的空白消息。

有关详细信息，请参阅 Specify Sample Time (Simulink) (Simulink)。

**数据类型：** `uint8`
## 所属库

UAV Toolbox / MAVLink

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法和限制：

- 为模块生成的 C/C++ 代码只能部署在 Linux 目标或
  Speedgoat 上。

## 版本历史

**在 R2020b 中引入**

## 描述

通过指定载荷信息和 MAVLink 消息类型创建空白 MAVLink 消息总线

MAVLink Blank Message 模块基于指定的 Message ID、System ID、Component ID、Sequence、载荷信息和 MAVLink 消息类型，创建一个表示 MAVLink 数据包的 Simulink® 非虚拟总线。

载荷信息是 MAVLink 数据包总线内的另一个非虚拟总线。该模块为 MAVLink 数据包及相应消息创建可与 MAVLink Serializer 和 MAVLink Deserializer 模块配合使用的 Simulink 总线。在每个采样命中时，该模块为指定消息类型的载荷输出空白或零信号。

总线中除 Message ID、System ID 和 Component ID 之外的所有元素均初始化为 `0`。唯一的例外是 `common.xml` 方言中 HEARTBEAT 消息的 `mavlink_version` 字段，该字段初始化为 `3`。
