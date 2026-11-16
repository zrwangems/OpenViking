---
type: simulink-block
title: 'Read Image'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'readimageros1'
documentation_source_path: 'ref/readimageros1.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Image

## 端口

### 输入

### **Msg** — ROS `sensor_msgs/Image` or `sensor_msgs/CompressedImage` message nonvirtual bus

ROS `sensor_msgs/Image` 或
`sensor_msgs/CompressedImage` 消息，指定为非虚拟总线。您可以使用 Subscribe 模块从活动 ROS 网络获取消息。

**数据类型：** `bus`
### 输出

### **Image** — Extracted image signal *M*-by-*N*-by-3 matrix | *M*-by-*N* matrix

从 ROS 消息中提取的图像信号，对于彩色图像返回为 *M*×*N*×3 矩阵，对于灰度图像返回为 *M*×*N* 矩阵。该矩阵包含来自 ROS 消息 `Data` 属性的像素数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **AlphaChannel** — Alpha channel for image *M*-by-*N* matrix

图像的 Alpha 通道，返回为
*M*×*N* 矩阵。该矩阵与图像输出具有相同的高度和宽度。每个元素的值在 `[0,1]` 范围内，表示对应像素的不透明度，值为 `0` 时表示完全透明。

**注意**

对于 `CompressedImage` 消息，如果启用了 `Show Alpha output port`，则 alpha 通道返回全零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **ErrorCode** — Error code for image conversion scalar

图像转换的错误代码，返回为标量。错误代码值为：

- `0` — 成功转换了图像消息。
- `1` — 图像编码不正确。检查传入消息编码是否与 **Image Encoding** 参数匹配。
- `2` — 图像消息的维度超过 **Maximum Image Size** 参数中指定的限制。
- `3` — 图像消息的 `Data` 字段被截断。请参阅 Manage Array Sizes for ROS Messages in Simulink 以增加数组的最大长度。
- `4` — 图像解压缩失败。

**数据类型：** `uint8`

## 参数

### **Maximum Image Size** — Maximum image size `[2000 2000]` (default) | two-element vector

最大图像大小，指定为二元素 `[height width]` 向量。

点击 **Configure using ROS**，使用 ROS 网络上的活动话题自动设置此参数。您必须连接到 ROS 网络。

### **Image Encoding** — Image encoding `rgb8` (default) | `rgba8` | ...

输入 **ImageMsg** 的图像编码。选择与消息的 `Encoding` 属性匹配的受支持编码类型。有关编码类型的详细信息，请参阅 `rosReadImage`。

### **Show Alpha output port** — Toggle AlphaChannel port off (default) | on

如果您的编码支持 Alpha 通道，则切换 Alpha 通道输出端口。

#### 依赖关系

只有某些编码类型支持 alpha 通道。**Image Encoding** 参数决定此参数是否出现在模块掩码中。

### **Show ErrorCode output port** — Toggle ErrorCode port on (default) | off

切换 **ErrorCode** 端口以监控错误。

### **Output variable-size signals** — Toggle variable-size signal output off (default) | on

切换可变大小信号输出。仅当预期图像大小随时间变化时，才应使用可变大小信号。有关可变大小信号的详细信息，请参阅 Variable-Size Signal Basics (Simulink)。

## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 涉及 `sensor_msgs/CompressedImage` 消息工作流的模型的代码生成和部署需要安装有效版本的 OpenCV 和 `cv_bridge` 包。

  对于涉及 `sensor_msgs/Image` 消息工作流的模型的代码生成和部署，不需要安装 OpenCV 和 `cv_bridge`。
- 对于涉及 `sensor_msgs/CompressedImage` 消息工作流的模型，不支持本地主机部署。
- 不支持 Bayer 编码。

## 版本历史

**在 R2019b 中引入**

## 描述

从 ROS Image 消息中提取图像

Read Image 模块从 ROS `sensor_msgs/Image` 或 `sensor_msgs/CompressedImage` 消息中提取图像。您可以选择实时 ROS 网络上活动话题的 ROS 消息参数，也可以单独指定消息参数。ROS 消息指定为非虚拟总线。使用 Subscribe 模块输出从 ROS 网络接收消息，并将该消息输入到 Read Image 模块。

**注意**

从网络读取 ROS 图像消息时，消息的 `Data` 属性可能超过 Simulink® 中设置的最大数组长度。要增加模型中所有消息类型的最大数组长度，请在 **Simulation** 选项卡下的 **Prepare** 部分中，选择 **ROS Toolbox**  > **Variable Size Messages**。取消选中 **Use default limits for this message type**，然后在 **Maximum length** 列中，根据图像中的像素数增加长度。
