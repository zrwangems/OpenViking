---
type: simulink-block
title: 'Read Scan'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'readscanblock'
documentation_source_path: 'ref/readscanblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Scan

## 端口

### 输入

### **Msg** — ROS 或 ROS 2 激光扫描消息非虚拟总线

ROS 2 激光扫描消息，指定为非虚拟总线。您可以使用 ROS
Subscribe 或 ROS 2 Subscribe
模块从网络获取消息。

**数据类型：** `bus`
### 输出

### **Ranges** — 每个点的距离值数组

扫描中每个点的距离值，以长度为
*M* 的数组返回。

**数据类型：** `single`

### **Angles** — 每个点的角度值数组

扫描中每个点的角度值，以长度为
*M* 的数组返回。

#### 依赖关系

启用 `Show Angles output port` 参数。

**数据类型：** `single`

### **Intensities** — 每个点的强度值数组

扫描中每个点的强度值，以长度为
*M* 的数组返回。

#### 依赖关系

启用 `Show Intensities output port` 参数。

**数据类型：** `single`

### **ErrorCode** — 消息解析错误代码标量

消息解析的错误代码，以标量返回。错误代码值包括：

- `0` — 成功解析激光扫描消息。
- `1` — 激光扫描消息的 `Data` 字段被截断。

#### 依赖关系

启用 `Show ErrorCode output port` 参数。

**数据类型：** `uint8`

## 参数

### **Maximum array length** — 激光扫描数组的最大长度 `100`（默认）| 正标量

激光扫描数组的最大长度，指定为正标量。

选择 **Configure using ROS...** 以使用 ROS 或 ROS 2 网络上的活动话题自动设置此参数。您必须连接到网络。

### **Show Angles output port** — `RGB` 端口切换 `off`（默认）| `on`

选择此参数以启用 **Angles** 端口。如果
启用此参数，消息必须包含 RGB 数据，否则模块将返回错误代码。

### **Show Intensity output port** — `Intensity` 端口切换 `off`（默认）| `on`

选择此参数以启用 **Intensity** 端口。
如果启用此参数，消息必须包含强度数据，否则模块将返回错误代码。

### **Show ErrorCode output port** — `ErrorCode` 端口切换 `on`（默认）| `off`

选择此参数以启用 **ErrorCode** 端口
并监控错误。

### **Output variable-size signals** — 可变大小信号输出切换 `off`（默认）| `on`

切换是否输出可变大小信号。仅当您预期图像大小随时间变化时才使用可变大小信号。有关可变大小信号的详细信息，请参阅 Variable-Size Signal Basics (Simulink)。

## 所属库

ROS Toolbox / ROS ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

从 ROS 或 ROS 2 激光扫描消息中提取扫描数据

Read Scan 模块从 ROS 或
ROS 2 激光扫描消息中提取距离、扫描和强度数据。您可以选择实时
ROS 或 ROS 2 网络上活动话题的消息参数，或单独指定消息参数。输入消息
指定为非虚拟总线。使用 ROS Subscribe 或 ROS 2 Subscribe 模块
从网络接收消息并将消息输入到 Read Scan
模块。对于 ROS 和 ROS 2 模型，您必须使用各自 ROS 和 ROS 2
库中的模块。
