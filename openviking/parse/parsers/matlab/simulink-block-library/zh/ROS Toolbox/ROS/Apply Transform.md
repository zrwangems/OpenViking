---
type: simulink-block
title: 'Apply Transform'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'applytransformblock'
documentation_source_path: 'ref/applytransformblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Apply Transform

## 端口

### 输入

### **TFMsg** — ROS 或 ROS 2 `geometry_msgs/TransformStamped` 消息非虚拟总线

ROS 或 ROS 2 `geometry_msgs/TransformStamped` 消息，指定为非虚拟总线。

### **Entity** — ROS 或 ROS 2 实体消息非虚拟总线

ROS 或 ROS 2 实体消息，指定为非虚拟总线。

### 输出

### **TFEntity** — 变换后的 ROS 或 ROS 2 实体消息非虚拟总线

变换后的 ROS 或 ROS 2 实体消息，返回为非虚拟总线。输出 `TFEntity` 消息与输入 `Entity` 消息具有相同的消息类型。

## 参数

### **Entity message type** — 输入实体消息的类型 `geometry_msgs/QuaternionStamped`（默认）| `geometry_msgs/Vector3Stamped` | `geometry_msgs/PointStamped` | `geometry_msgs/PoseStamped`

输入实体消息的类型，指定为以下选项之一：

- `geometry_msgs/PointStamped`
- `geometry_msgs/PoseStamped`
- `geometry_msgs/QuaternionStamped`
- `geometry_msgs/Vector3Stamped`

## 所属库

ROS Toolbox / ROS ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

将输入 ROS 或 ROS 2 消息变换到目标坐标系

Apply Transform 模块根据输入 `gemonetry_msgs/TransformStamped` 消息中指定的齐次变换值，将输入 ROS 或 ROS 2 实体消息变换到目标坐标系。Apply Transform 模块支持以下输入实体消息类型：

- `geometry_msgs/PointStamped`
- `geometry_msgs/PoseStamped`
- `geometry_msgs/QuaternionStamped`
- `geometry_msgs/Vector3Stamped`

要将实体消息变换到目标坐标系，该模块使用左乘约定对实体消息应用前向变换。
