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
```yaml
ports:
- name: Msg
  summary: ROS sensor_msgs/Image 或 sensor_msgs/CompressedImage 消息非虚拟总线
  direction: input
  data_types: bus
- name: Image
  summary: 提取的图像信号 *M*×*N*×3 矩阵 | *M*×*N* 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16
- name: AlphaChannel
  summary: 图像的 Alpha 通道 *M*×*N* 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16
- name: ErrorCode
  summary: 图像转换的错误代码 标量
  direction: output
  data_types: uint8
```

### 输入

### **Msg** — ROS `sensor_msgs/Image` 或 `sensor_msgs/CompressedImage` 消息非虚拟总线

ROS `sensor_msgs/Image` 或
`sensor_msgs/CompressedImage` 消息，指定为非虚拟总线。您可以使用 Subscribe 模块从活动 ROS 网络获取消息。

**数据类型：** `bus`
### 输出

### **Image** — 提取的图像信号 *M*×*N*×3 矩阵 | *M*×*N* 矩阵

从 ROS 消息中提取的图像信号，彩色图像返回为 *M*×*N*×3 矩阵，灰度图像返回为 *M*×*N* 矩阵。该矩阵包含来自 ROS 消息 `Data` 属性的像素数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **AlphaChannel** — 图像的 Alpha 通道 *M*×*N* 矩阵

图像的 Alpha 通道，返回为
*M*×*N* 矩阵。该矩阵与图像输出的高度和宽度相同。每个元素的值在 `[0,1]` 范围内，表示对应像素的不透明度，值为 `0` 表示完全透明。

**注意**

对于 `CompressedImage` 消息，如果启用了 `Show Alpha output
port`，Alpha 通道将返回全零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **ErrorCode** — 图像转换的错误代码 标量

图像转换的错误代码，返回为标量。错误代码值如下：

- `0` — 成功转换图像消息。
- `1` — 图像编码不正确。请检查传入消息的编码是否与 **Image Encoding** 参数匹配。
- `2` — 图像消息的尺寸超过了 **Maximum Image Size** 参数中指定的限制。
- `3` — 图像消息的 `Data` 字段被截断。请参阅 Manage Array Sizes for ROS Messages in Simulink 以增加数组的最大长度。
- `4` — 图像解压缩失败。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Maximum Image Size
  summary: 最大图像尺寸 [2000 2000]（默认）| 二元素向量
  group: ''
- name: Image Encoding
  summary: 图像编码 rgb8（默认）| rgba8 | ...
  group: ''
- name: Show Alpha output port
  summary: 切换 AlphaChannel 端口 关闭（默认）| 开启
  group: ''
- name: Show ErrorCode output port
  summary: 切换 ErrorCode 端口 开启（默认）| 关闭
  group: ''
- name: Output variable-size signals
  summary: 切换可变大小信号输出 关闭（默认）| 开启
  group: ''
```

### **Maximum Image Size** — 最大图像尺寸 `[2000 2000]`（默认）| 二元素向量

最大图像尺寸，指定为二元素 `[height width]` 向量。

点击 **Configure using ROS** 可使用 ROS 网络上的活动话题自动设置此参数。您必须连接到 ROS 网络。

### **Image Encoding** — 图像编码 `rgb8`（默认）| `rgba8` | ...

输入 **ImageMsg** 的图像编码。
选择与消息的 `Encoding` 属性匹配的受支持编码类型。有关编码类型的更多信息，请参阅 `rosReadImage`。

### **Show Alpha output port** — 切换 AlphaChannel 端口 关闭（默认）| 开启

如果您的编码支持 Alpha 通道，则切换 Alpha 通道输出端口。

#### 依赖关系

只有某些编码类型支持 Alpha 通道。**Image Encoding** 参数决定此参数是否出现在模块掩码中。

### **Show ErrorCode output port** — 切换 ErrorCode 端口 开启（默认）| 关闭

切换 **ErrorCode** 端口以监控错误。

### **Output variable-size signals** — 切换可变大小信号输出 关闭（默认）| 开启

切换可变大小信号输出。仅当预期图像大小随时间变化时才应使用可变大小信号。有关可变大小信号的更多信息，请参阅 Variable-Size Signal Basics (Simulink)。
## 所属库

ROS Toolbox / ROS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

用法说明和限制：

- 涉及 `sensor_msgs/CompressedImage` 消息工作流的模型代码生成和部署需要安装有效版本的 OpenCV 和 `cv_bridge` 包。

  对于涉及 `sensor_msgs/Image` 消息工作流的模型代码生成和部署，不需要安装 OpenCV 和 `cv_bridge`。
- 涉及 `sensor_msgs/CompressedImage` 消息工作流的模型不支持本地主机部署。
- 不支持 Bayer 编码。

## 版本历史

**在 R2019b 中引入**

## 描述

从 ROS Image 消息中提取图像

Read Image 模块从 ROS `sensor_msgs/Image` 或 `sensor_msgs/CompressedImage` 消息中提取图像。您可以选择实时 ROS 网络上活动话题的 ROS 消息参数，也可以单独指定消息参数。ROS 消息被指定为非虚拟总线。使用 Subscribe 模块输出从 ROS 网络接收消息，并将该消息输入到 Read Image 模块。

**注意**

当从网络读取 ROS 图像消息时，消息的 `Data` 属性可能超过 Simulink® 中设置的最大数组长度。要增加模型中所有消息类型的最大数组长度，请在 **Simulation** 选项卡下的 **Prepare** 部分中，选择 **ROS Toolbox** > **Variable Size Messages**。取消选中 **Use default limits for this message type**，然后在 **Maximum length** 列中，根据图像中的像素数增加长度。
