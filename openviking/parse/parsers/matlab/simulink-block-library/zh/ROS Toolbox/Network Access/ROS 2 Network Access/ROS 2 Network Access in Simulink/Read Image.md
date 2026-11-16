---
type: simulink-block
title: 'Read Image'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'readimageros2'
documentation_source_path: 'ref/readimageros2.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Image

## 端口

### 输入

### **Msg** — ROS 2 `sensor_msgs/Image` 或 `sensor_msgs/CompressedImage` 消息非虚拟总线

ROS 2 `sensor_msgs/Image` 或
`sensor_msgs/CompressedImage` 消息，指定为非虚拟总线。您可以使用 Subscribe 模块从活动的 ROS 2 网络获取消息。

**数据类型：** `bus`
### 输出

### **Image** — 提取的图像信号 *M*×*N*×3 矩阵 | *M*×*N* 矩阵

从 ROS 2 消息中提取的图像信号，对于彩色图像返回为
*M*×*N*×3 矩阵，对于灰度图像返回为
*M*×*N* 矩阵。该矩阵包含来自 ROS 2
消息 `Data` 属性的像素数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **AlphaChannel** — 图像的 Alpha 通道 *M*×*N* 矩阵

图像的 Alpha 通道，返回为
*M*×*N* 矩阵。该矩阵与图像输出具有相同的高度和宽度。每个元素的值在
`[0,1]` 范围内，表示对应像素的不透明度，值为
`0` 表示完全透明。

**注意**

对于 `CompressedImage` 消息，如果启用了 `Show Alpha output port`，则 alpha 通道返回全零。

#### 依赖项

启用 `Show Alpha output port` 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **ErrorCode** — 图像转换的错误代码 标量

图像转换的错误代码，返回为标量。错误代码值如下：

- `0` — 成功转换了图像消息。
- `1` — 图像编码不正确。检查传入消息的编码是否与 **图像编码**
  参数匹配。
- `2` — 图像消息的维度超过
  **最大图像大小** 参数中指定的限制。
- `3` — 图像消息的 `Data`
  字段被截断。请参阅在 Simulink 中管理 ROS 消息的数组大小
  以增加数组的最大长度。
- `4` — 图像解压缩失败。

**数据类型：** `uint8`

## 参数

### **最大图像大小** — 最大图像大小 `[2000 2000]`（默认）| 二元素向量

最大图像大小，指定为二元素 `[height width]`
向量。

选择 **使用 ROS 2 配置...** 以使用 ROS 2 网络上的活动话题自动设置此参数。您必须连接到 ROS
2 网络。

### **图像编码** — 图像编码 `rgb8`（默认）| `rgba8` | ...

输入 **ImageMsg** 的图像编码。选择与消息的 `Encoding` 属性匹配的
编码类型。有关编码类型的详细信息，请参阅 `rosReadImage`。

### **显示 Alpha 输出端口** — AlphaChannel 端口开关 `off`（默认）| `on`

如果所选编码类型支持 alpha 通道，则打开或关闭 alpha 通道输出端口。

#### 依赖项

要启用此参数，请将 **图像编码**
参数设置为支持 alpha 通道的编码类型。

### **显示 ErrorCode 输出端口** — 切换 ErrorCode 端口 `on`（默认）| `off`

打开或关闭 **ErrorCode** 端口，以监视
错误。

### **输出可变大小信号** — 可变大小信号输出开关 `off`（默认）| `on`

切换是否输出可变大小信号。仅当您预期图像大小会随时间变化时，才使用可变大小信号。有关可变大小
信号的详细信息，请参阅可变大小信号基础知识 (Simulink)。

## 所属库

ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 涉及
  `sensor_msgs/CompressedImage` 消息工作流的模型进行代码生成和部署时，需要安装
  有效版本的 OpenCV 和 `cv_bridge` 包。

  对于涉及
  `sensor_msgs/Image` 消息工作流的模型进行代码生成和部署，不需要安装 OpenCV
  和 `cv_bridge`。

- 涉及
  `sensor_msgs/CompressedImage` 消息工作流的模型不支持本地主机部署。
- 不支持 Bayer 编码。

## 版本历史

**在 R2021b 中引入**

## 描述

从 ROS 2 Image 消息中提取图像

Read Image 模块从 ROS
2 `sensor_msgs/Image` 或 `sensor_msgs/CompressedImage`
消息中提取图像。您可以选择实时 ROS 2 网络上活动话题的消息参数，也可以
单独指定消息参数。ROS 2 消息被指定为非虚拟
总线。使用 Subscribe 模块输出
从 ROS 2 网络接收消息，并将该消息输入到 Read
Image 模块。

**注意**

当从网络读取 ROS 2 图像消息时，消息的 `Data` 属性
可能超过 Simulink® 中设置的最大数组长度。请按照以下步骤增加模型中所有消息
类型的最大数组长度：

1. 通过选择 **应用** 选项卡下的 **Robot Operating System
   (ROS)** 应用来启用 ROS 选项，并适当配置 ROS
   网络参数。
2. 在 **仿真** 选项卡下的
   **准备** 部分中，选择 **ROS Toolbox** > **可变大小消息**。
3. 取消选中 **使用此消息类型的默认限制**，然后在
   **最大长度** 列中，根据
   图像中的像素数增加长度。
