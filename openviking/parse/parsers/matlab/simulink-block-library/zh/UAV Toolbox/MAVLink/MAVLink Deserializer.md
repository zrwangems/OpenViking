---
type: simulink-block
title: 'MAVLink Deserializer'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'MAVLink'
documentation_page: 'mavlinkdeserializer'
documentation_source_path: 'ref/mavlinkdeserializer.html'
language: zh-CN
chinese_source: worker-translation
---

# MAVLink Deserializer

## 端口

### 输入

### **Data** — MAVLink 数据流向量

包含序列化 MAVLink 数据包的 `uint8` 字节流。字节流通常通过通信通道接收，例如 UDP、TCP 或 Serial。在每个采样时间，通信通道接收数据并返回一个包含一个或多个 MAVLink 数据包的字节流。该字节流也可以跨多个采样时间分部分返回一个 MAVLink 数据包。此输入端口接受可变长度信号。

**数据类型：** `uint8`

### **Length** — Data 输入端口处有效 MAVLink 数据的长度 标量

可选输入端口，用于包含有效 MAVLink 数据的长度。要启用此端口，请选择 **输入数据流长度可用** 参数。当您知道数据流中有效 MAVLink 数据的准确长度时，请使用此选项。

当您有一个通信通道接收外设，其输出包含尾随零的部分接收数据时，此选项很有用。此类外设还会输出实际接收到的有效数据字节数长度。您可以将外设的长度输出直接连接到 MAVLink Deserializer 模块的 **Length** 输入端口，以便输入字节流中的尾随零不影响解码逻辑。

**数据类型：** `uint16`

### 输出

### **IsNew** — 新消息指示符 `0` | `1`

新 MAVLink 消息指示符，以逻辑值形式返回。值 `1` 表示自该模块上次接收采样以来有新消息可用。此输出可用于触发子系统处理从 MAVLink Deserializer 模块接收到的新消息。

**数据类型：** `Boolean`

### **Msg** — MAVLink 数据包非虚拟总线

MAVLink 数据包，以非虚拟总线形式返回。MAVLink 数据包中 Payload 的类型是与 **MAVLink 消息类型** 参数中指定的 MAVLink 消息对应的 Simulink 总线。该模块在接收到您指定消息名称的消息之前输出空白消息。**Msg** 端口输出此新消息。如果新消息不可用，则输出最后接收到的 MAVLink 消息。如果自仿真开始以来尚未接收到消息，**Msg** 端口输出空白 MAVLink 消息。

**数据类型：** `bus`

## 参数

#### 主要

### **MAVLink 方言源** — 用于指定 MAVLink 消息定义的源 `Select from standard MAVLink dialects` (默认) | `Specify your own`

用于指定 MAVLink 消息定义 XML 名称的源，指定为以下之一：

- `Select from standard MAVLink dialects` - 使用此选项可在 **MAVLink 方言** 参数中列出的 12 个常用消息定义 XML 名称中选择一个定义 XML。
- `Specify your own` - 在 **MAVLink 方言** 参数出现的文本框中输入 XML 名称。

### **MAVLink 方言** — 要为 MAVLink 消息解析的消息定义 `common.xml` (默认) | string

要为 MAVLink 消息解析的 MAVLink 消息定义文件（.`xml`），指定为字符串。

如果 **MAVLink 方言源** 参数设置为 `Select from standard MAVLink dialects`，则需要从下拉列表中的可用消息定义名称中选择一个消息定义。

如果参数 **MAVLink 方言源** 设置为 `Specify your own`，则需要指定当前 MATLAB 路径上的消息定义文件（.`xml`），或者可以提供 XML 文件的完整路径。

### **MAVLink 版本** — MAVLink 协议版本 `2` (默认) | `1`

该模块用于序列化和反序列化 MAVLink 消息的 MAVLink 协议版本。

### **MAVLink 消息类型** — MAVLink 消息 `HEARTBEAT` (默认)

MAVLink 消息，指定为字符串。单击 **选择** 可从可用 MAVLink 消息的完整列表中选择。该列表根据您为 **MAVLink 方言** 和 **MAVLink 版本** 参数选择的值而变化。

**数据类型：** `string`

#### 高级

### **输入数据流长度可用** — 输入字节流中有效 MAVLink 数据的长度已知 `off` (默认) | `on`

当您选择此选项时，MAVLink Deserializer 模块会提供一个名为 **Length** 的附加输入端口。此输入端口可用于传递输入字节流中 MAVLink 数据的实际长度（如果已知）。输入字节流会按此长度进行裁剪。

当您有一个通信通道接收外设，其输出包含尾随零的部分接收数据时，此选项很有用。此类外设还会输出实际接收到的有效数据字节数长度。您可以将外设的长度输出直接连接到 MAVLink Deserializer 模块的 **Length** 输入端口，以便输入字节流中的尾随零不影响解码逻辑。

### **按 System ID 过滤输出 MAVLink 消息** — 按 System ID 过滤接收到的消息 `off` (默认) | `on`

选择此选项可针对 **System ID** 参数中提到的 System ID 值过滤接收到的 MAVLink 消息。此选项可帮助您同时按 System ID 和 Component ID 过滤接收到的消息。

### **System ID** — System ID 值 `1` (默认) | `[0,255]` 范围内的标量

指定在过滤解码后的 MAVLink 消息时要使用的 System ID 值。该模块输出接收到的 MAVLink 消息，其 System ID 与指定值匹配，并且其 Message ID 与 MAVLink 消息匹配（在 **MAVLink 消息类型** 参数中选择）。

#### 依赖关系

要启用此参数，请选择 **按 System ID 过滤输出 MAVLink 消息**。

### **按 Component ID 过滤输出 MAVLink 消息** — 按 System ID 和 Component ID 过滤接收到的消息 `off` (默认) | `on`

选择此选项可针对分别在 **System ID** 和 **Component ID** 参数中提到的 System ID 和 Component ID 过滤接收到的 MAVLink 消息。

#### 依赖关系

仅当您选择 **按 System ID 过滤输出 MAVLink 消息** 参数时，此参数才会出现。

### **Component ID** — Component ID 值 `1` (默认) | [`0,255`]

指定在过滤解码后的 MAVLink 消息时要使用的 Component ID 值。该模块输出那些接收到的 MAVLink 消息，其 System ID 和 Component ID 值分别与 **System ID** 和 **Component ID** 参数中指定的值匹配，并且其 Message ID 与 MAVLink 消息匹配（在 **MAVLink 消息类型** 参数中选择）。

#### 依赖关系

要启用此参数，请选择 **按 Component ID 过滤输出 MAVLink 消息**。

### **在输出中排队 MAVLink 消息** — 启用接收到的 MAVLink 消息排队 `off` (默认) | `on`

选择此选项可使用先进先出模式输出消息。如果您不选择此选项，MAVLink Deserializer 模块将在每个仿真步输出针对所选 **MAVLink 消息类型** 的最新接收到的 MAVLink 消息（如果选择了那些参数，则还具有匹配的 System ID 和 Component ID）。如果在某个仿真步中接收到多个匹配给定参数的消息，则最新消息作为输出传递，其余消息被丢弃。您可以通过选择此选项来反转此行为。

当您选择此参数时，MAVLink Deserializer 模块在每个仿真步的行为为：

- 该模块将匹配所选 MAVLink 消息类型（以及如果选择了那些参数，则匹配 System ID 和 Component ID）的解码后 MAVLink 消息存储在队列中。如果在接收到的消息中没有匹配所需参数的消息，则不会排队任何消息。
- 如果队列不为空，则首先将队列中的第一条消息作为输出发送，并且 **IsNew** 端口上的信号设置为 `1`。

选择 **在输出中排队 MAVLink 消息** 参数会使 **要排队的消息数** 参数可见。您可以通过设置此参数的值来固定队列大小。

### **要排队的消息数** — MAVLink 消息队列大小 `50` (默认) | (`0,65535`] 范围内的标量

指定用于存储匹配所需参数的接收到的 MAVLink 消息的队列大小。

#### 依赖关系

要启用此参数，请选择 **在输出中排队 MAVLink 消息**。

## 所属库

UAV Toolbox / MAVLink

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法和限制：

- 为该模块生成的 C/C++ 代码只能部署在 Linux 目标或 Speedgoat 上。

## 版本历史

**在 R2020b 中引入**

## 描述

将序列化的 uint8 MAVLink 数据流转换为 Simulink 非虚拟总线

MAVLink Deserializer 模块接收 `uint8` 缓冲区，并解码缓冲区中的 MAVLink 消息。一旦该模块接收到所选 MAVLink 消息类型的 MAVLink 消息，该模块会输出一个 Simulink® 非虚拟总线，表示一个 MAVLink 数据包，其中包含与所选 MAVLink 消息类型对应的 Message ID、System ID、Component ID、Sequence 和 Payload 信息。

在每个仿真步，该模块解码输入 `uint8` 缓冲区，并检索解码后接收到的 MAVLink 消息。如果已接收到所选 MAVLink 消息类型的新消息，则该模块从接收到的消息列表中检索该消息，并将其转换为 Simulink 非虚拟总线信号。

该模块中的 MAVLink 解码逻辑会处理从通信通道部分接收到 MAVLink 数据包的情况。MAVLink Deserializer 模块内部存储当前解析状态，并在通过通信通道接收到新缓冲区时从前一步恢复解码。如果已接收到完整的 MAVLink 数据包，并且接收到的校验和与针对接收字节计算出的校验和匹配，则这表明已接收到一条 MAVLink 消息。存储解析状态可确保该模块能够解码分多部分接收到的 MAVLink 数据包。

默认情况下，该模块输出所选 MAVLink 消息类型的最新接收到的 MAVLink 消息（如果已接收到）。可以通过选择 **在输出中排队消息** 参数来更改此行为。在这种情况下，所需类型的所有接收到的 MAVLink 消息都会排队，并且在每个仿真步，该模块输出最旧的消息。
