---
type: simulink-block
title: 'Write Image'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'writeimageblock'
documentation_source_path: 'ref/writeimageblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Write Image

## 端口

### 输入

### **Image** — 输入图像信号 *M*-by-*N*-by-3 矩阵 | *M*-by-*N* 矩阵

图像像素数据，对于彩色图像指定为 *M*-by-*N*-by-3 矩阵，对于灰度图像指定为 *M*-by-*N* 矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### **AlphaChannel** — 输入图像的 Alpha 通道 *M*-by-*N* 矩阵

图像的 Alpha 通道，指定为 *M*-by-*N* 矩阵。此矩阵与图像输入具有相同的高度和宽度。每个元素的取值范围为 `[0,1]`，表示对应像素的不透明度，值为 `0` 时表示完全透明。

#### 依赖关系

所选的图像编码必须支持 alpha 通道。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16`

### 输出

### **Msg** — ROS 或 ROS 2 图像消息 nonvirtual bus

ROS 或 ROS 2 图像消息，返回为 nonvirtual bus。您可以使用 ROS Publish 或 ROS 2 Publish 模块，将该消息分别发布到活动的 ROS 或 ROS 2 网络。

**数据类型：** `bus`

## 参数

### **Image Encoding** — 图像编码 `rgb8`（默认） | `rgba8` | ...

输入 **Image** 的图像编码，指定为支持的选项之一。有关编码类型的详细信息，请参阅 `rosReadImage`。

## 所属库

ROS Toolbox / ROS ROS Toolbox / ROS 2

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

将图像数据写入 ROS 或 ROS 2 消息

Write Image 模块将图像数据写入 ROS 或 ROS 2 图像消息。您可以指定输出图像消息的编码。使用 ROS Publish 或 ROS 2 Publish 模块将输出图像消息发布到网络上的活动主题。
