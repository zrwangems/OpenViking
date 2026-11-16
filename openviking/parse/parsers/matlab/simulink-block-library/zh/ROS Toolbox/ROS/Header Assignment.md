---
type: simulink-block
title: 'Header Assignment'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'headerassignment'
documentation_source_path: 'ref/headerassignment.html'
language: zh-CN
chinese_source: worker-translation
---

# Header Assignment

## 端口

### 输入

### **InputMsg** — 要更新的 ROS 消息，nonvirtual bus

具有 `std_msgs/Header` 字段的 ROS 消息，指定为
nonvirtual bus。

**数据类型：** `bus`
### 输出

### **OutputMsg** — 带有已更新 header 的 ROS 消息，nonvirtual bus

带有已更新 header 的 ROS 消息，以 nonvirtual bus 形式返回。

**数据类型：** `bus`

## 参数

### **Set Frame ID** — 指定与消息数据关联的帧 `off`（默认） | `on`

选择此参数可指定与消息数据关联的帧。在选中此参数时启用的文本框中指定 frame ID。该模块使用指定的帧填充 ROS 消息 header 的 `frame_id` 字段。

**示例：** `base_link`

### **Set Timestamp** — 在 header 中设置时间戳 `off`（默认） | `on`

选择此参数可将 header 的 `stamp` 值设置为当前 ROS 系统时间。要使用发布在 `/clock` 主题上的自定义时间而不是 ROS 系统时间，请将 `use_sim_time` ROS 参数设置为 `true`。

### **Header field name** — 指定 Header 字段名称 `Use the default Header field name`（默认） | `Specify your own`

将 Header 字段的名称指定为以下之一：

- `Use the default Header field name` — 该模块将 ROS 消息中 header 字段的名称设置为默认值 `Header`。
- `Specify your own` — 启用一个文本框，您可以在其中为 ROS 消息中的 header 字段指定自定义名称。

**示例：** `my_custom_header`

## 所属库

ROS Toolbox / ROS

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

更新 ROS 消息 header 的字段

Header Assignment 模块更新 ROS 消息的 header 字段中的值。当 ROS 消息包含类型为 `std_msgs/Header` 的 header 字段时，您可以使用此模块更新其 header 字段中的 `frame_id` 和 `stamp` 值。在每个采样命中期间，该模块会更新 header 中的 `frame_id` 和 `stamp` 字段。时间戳的精度取决于求解器的步长。较小的步长会产生更精确的时间戳。
