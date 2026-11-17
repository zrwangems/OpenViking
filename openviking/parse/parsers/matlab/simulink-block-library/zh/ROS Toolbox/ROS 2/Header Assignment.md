---
type: simulink-block
title: 'Header Assignment'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'headerassignmentros2'
documentation_source_path: 'ref/headerassignmentros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Header Assignment

## 端口
```yaml
ports:
- name: InputMsg
  summary: 要更新非虚拟总线的 ROS 2 消息
  direction: input
  data_types: bus
- name: OutputMsg
  summary: 带有更新后 header 非虚拟总线的 ROS 2 消息
  direction: output
  data_types: bus
```

### 输入

### **InputMsg** — 要更新非虚拟总线的 ROS 2 消息

包含 `std_msgs/header` 字段的 ROS 2 消息，指定为非虚拟总线。

**数据类型：** `bus`
### 输出

### **OutputMsg** — 带有更新后 header 非虚拟总线的 ROS 2 消息

带有更新后 header 的 ROS 2 消息，以非虚拟总线形式返回。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Set Frame ID
  summary: 指定与消息数据关联的坐标系 off（默认）| on
  group: ''
- name: Set Timestamp
  summary: 在 header 中设置时间戳 off（默认）| on
  group: ''
- name: Header field name
  summary: 指定 Header 字段名称 Use the default Header field name（默认）| Specify your own
  group: ''
```

### **Set Frame ID** — 指定与消息数据关联的坐标系 `off`（默认）| `on`

选择此参数以指定消息数据所关联的坐标系。
在选中此参数时启用的文本框中指定坐标系 ID。该模块将 ROS 2 消息 header 的 `frame_id` 字段填充为指定的坐标系。

**示例：** `base_link`

### **Set Timestamp** — 在 header 中设置时间戳 `off`（默认）| `on`

选择此参数以将 header 的 `stamp` 值设置为当前 ROS 2 系统时间。

### **Header field name** — 指定 Header 字段名称 `Use the default Header field name`（默认）| `Specify your own`

将 Header 字段的名称指定为以下之一：

- `Use the default Header field name` — 该模块将 ROS 2 消息中 header 字段的名称设置为默认值 `header`。
- `Specify your own` — 启用一个文本框，您可以在其中为 ROS 2 消息中的 header 字段指定自定义名称。

**示例：** `my_custom_header`
## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

更新 ROS 2 消息 header 的字段

Header Assignment 模块更新 ROS 2 消息 header 字段中的值。当 ROS 2 消息包含类型为 `std_msgs/header` 的 header 字段时，您可以使用此模块更新其 header 字段中的 `frame_id` 和 `stamp` 值。在每个采样命中期间，该模块更新 header 中的 `frame_id` 和 `stamp` 字段。时间戳的精度取决于求解器的步长。较小的步长可获得更精确的时间戳。
