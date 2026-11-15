---
type: simulink-block
title: 'Video Display'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Video'
documentation_page: 'videodisplay'
documentation_source_path: 'ref/videodisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Display

## 端口

### 输入

### ***`Color`*** — 图像 *height*-by-*width* 大小矩阵的颜色分量

指定一个 *height*-by-*width* 矩阵，其中维度是图像的大小。

#### 依赖项

使用 **Pixel format** 参数将颜色分量格式指定为 `RGB` 或 `YCbCr 4:2:2`。

**数据类型：** `uint8`
### 输出

### **msg** — 到视频显示接口的数据消息标量

此端口将包含图像数据的数据消息输出到连接的 Video Display Interface 模块。有关消息的详细信息，请参阅消息。

**数据类型：** `SoCData`

## 参数

### **Pixel format** — 像素数据格式 `RGB`（默认）| `YCbCr 4:2:2`

将输入图像数据编码指定为 `RGB` 或 `YCbCr 4:2:2` 三元组。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 若要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。有关为 SoC 设计生成代码的详细信息，请参阅使用 SoC Builder 生成 SoC 设计。
- 若要为您的 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® 和 SoC Blockset™ Support Package for Embedded Linux® Devices。
- 若要使用此模块，必须将 **Hardware Board** 设置为 `Embedded Linux Board`。然后，您可以按照说明配置开发板。有关详细信息，请参阅创建 Embedded Linux 设备配置。

当部署到受支持的硬件板时，此模块使用 V4L2 驱动程序框架从视频捕获设备（如摄像头）捕获图像。若要指定视频捕获设备和事件触发器，请使用 Hardware Mapping 工具。有关 V4L2 驱动程序框架的详细信息，请参阅 Video4Linux。

## 版本历史

**在 R2021a 中引入**

## 描述

将来自算法的图像样本显示到输出视频设备

Video Display 模块模拟驱动程序代码的行为，该代码将图像显示到硬件板上的视频输出（例如 LCD 屏幕）。此模块的输出必须连接到 Video Display Interface 模块，该模块模拟硬件板上的物理显示屏。将此模块放在任务内，并连接到算法，以便在每次任务执行时输出图像。有关任务的详细信息，请参阅定时器驱动任务和事件驱动任务。
