---
type: simulink-block
title: 'Video Capture'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Video'
documentation_page: 'videocapture'
documentation_source_path: 'ref/videocapture.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Capture

## 端口

### 输入

### **msg** — 来自视频采集接口的标量数据消息

此消息端口接收来自连接的 Video Capture Interface 模块的数据消息。当 Task Manager 模块触发包含 Video Capture 模块的任务时，这些消息会进行处理。有关消息的详细信息，请参阅消息。

**数据类型：** `SoCData`
### 输出

### ***`Color`*** — 图像的 *height*-by-*width* 矩阵的颜色分量

此端口输出该 *`Color`* 分量的 *height*-by-*width* 矩阵，其中维度是图像的尺寸。**图像大小** 参数指定 *height* 和 *width* 维度。

#### 依赖关系

**像素格式** 参数将颜色分量格式设置为 `RGB` 或 `YCbCr
4:2:2`。

**数据类型：** `uint8`

## 参数

### **图像大小** — 图像大小 `160x120` (默认) | `320x240` | `640x480` | `800x600` | `custom`

指定此模块的颜色通道端口输出的图像矩阵的 *height* 和 *width* 维度。指定 `custom` 以设置自定义图像维度。

### **图像大小 ([width, height])** — 图像大小 `[320, 240]` (默认) | `2` 元素正整数向量

指定颜色通道端口输出的图像矩阵的自定义 *height*-by-*width* 维度。

#### 依赖关系

要启用此参数，请将 **图像大小** 参数设置为 `custom`。

### **像素格式** — 像素数据的格式 `RGB` (默认) | `YCbCr 4:2:2`

将图像数据编码指定为 `RGB` 或 `YCbCr 4:2:2` 三元组。

### **采样时间** — 以 seconds 为单位的采样时间 `-1` (默认) | 正标量

如果在定时器驱动任务中使用，请输入 Task Manager 模块中定义的任务的采样时间。如果在事件驱动任务中使用，请输入 `-1`。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 要为您的设计自动生成 C 代码，
  并在 SoC 设备上执行，请使用 SoC Builder 工具。
  有关为 SoC 设计生成代码的详细信息，请参阅使用 SoC Builder 生成 SoC 设计。
- 要为您的 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® 和 SoC Blockset™ Support Package for Embedded Linux® Devices。
- 要使用此模块，必须将 **硬件板** 设置为
  `Embedded Linux Board`。然后可以按照说明
  配置该板。有关详细信息，请参阅创建 Embedded Linux 设备配置。

当部署到支持的硬件板时，此模块使用 V4L2 驱动框架
从视频捕获设备（如摄像头）捕获图像。要指定视频捕获
设备和事件触发器，请使用 Hardware Mapping 工具。有关
V4L2 驱动框架的详细信息，请参阅 Video4Linux。

## 版本历史

**在 R2021a 中引入**

## 描述

从输入视频设备捕获视频并发送到算法

Video Capture 模块模拟驱动代码的行为，该代码从硬件板上的视频设备（如摄像头）捕获图像。此模块的输入必须连接到 Video Capture Interface 模块，该模块模拟硬件板上的物理视频源设备。将此模块放在任务内，并将其连接到算法，以便在任务每次执行时处理图像。有关任务的详细信息，请参阅定时器驱动任务和事件驱动任务。
