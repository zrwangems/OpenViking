---
type: simulink-block
title: 'RTSP Video Stream Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'rtspvideostreamtransmit'
documentation_source_path: 'supportpkg/raspberrypi_ref/rtspvideostreamtransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# RTSP Video Stream Transmit

## 端口

### 输入

### **R** — 输入视频矩阵的红色分量

要流式传输的 RGB 视频的红色通道信号，指定为 *M*×*N* 的像素网格。
此处，*M* 是行数，*N* 是红色分量的列数。

#### 依赖关系

要启用此端口，请将 **输入图像格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **G** — 输入视频矩阵的绿色分量

要流式传输的 RGB 视频的绿色通道信号，指定为 *M*×*N* 的像素网格。
此处，*M* 是行数，*N* 是绿色分量的列数。

#### 依赖关系

要启用此端口，请将 **输入图像格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **B** — 输入视频矩阵的蓝色分量

要流式传输的 RGB 视频的蓝色通道信号，指定为 *M*×*N* 的像素网格。
此处，*M* 是行数，*N* 是蓝色分量的列数。

#### 依赖关系

要启用此端口，请将 **输入图像格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **Y** — 输入视频矩阵的亮度分量

要流式传输的输入视频的亮度分量，指定为 *M*×*N* 的像素网格。
此处，*M* 是行数，*N* 是亮度分量的列数。

#### 依赖关系

要启用此端口，请将 **输入图像格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cb** — 输入视频矩阵的蓝色差色度分量

要流式传输的输入视频的蓝色差色度分量，指定为 *M*×*N* 的像素网格。
此处，*M* 是行数，*N* 是蓝色差色度分量的列数。

#### 依赖关系

要启用此端口，请将 **输入图像格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cr** — 输入视频矩阵的红色差色度分量

要流式传输的输入视频的红色差色度分量，指定为 *M*×*N* 的像素网格。
此处，*M* 是行数，*N* 是红色差色度分量的列数。

#### 依赖关系

要启用此端口，请将 **输入图像格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **I** — 灰度输入视频矩阵

要流式传输的灰度输入视频信号，指定为 *M*×*N* 的像素网格。
此处，*M* 是行数，*N* 是灰度输入视频的列数。

#### 依赖关系

要启用此端口，请将 **输入图像格式** 设置为 `Grayscale`。

**数据类型：** `uint8`

## 参数

### 视频参数

### **输入图像格式** — 输入视频流格式 `RGB` (默认) | `YCbCr 4:2:2` | `Grayscale`

指定输入视频流的格式。

**提示**

要在设备上查看彩色视频，请将此参数设置为 `YCbCr 4:2:2`。由于此格式需要的带宽较少，您可以流式传输视频而不会显著影响视频质量。

### **输出分辨率** — 图像分辨率 `Specify` (默认) | `Inherit from input image`

选择输出图像分辨率。

- `Specify` — 在 **图像大小 ([width, height])** 参数中手动指定输入图像分辨率。使用此选项，您可以增大或减小输出视频流的分辨率。当您指定更高分辨率时，Simulink 模型的执行速度会降低。
- `Inherit from input image` — 模块继承输入图像的分辨率。

### **图像大小 ([width, height])** — 图像分辨率 `[640, 480]` (默认) | [`width`, `height`]

以像素为单位指定输入图像的分辨率。

#### 依赖关系

要启用此参数，请将 **输出分辨率** 设置为 `Specify`。

### **视频流编码** — 视频流编码格式 `H264` (默认) | `JPEG`

选择实时流协议 (RTSP) 视频流的编码格式。

### **帧率 (in fps)** — 输入视频的帧率 `24` (默认) | positive integer

以帧/秒为单位指定输入视频信号的帧率。

### RTSP 流连接参数

### **端口号** — 用于流式传输视频的 Raspberry Pi 板端口 `8554` (默认) | positive integer，范围为 [`1`,`65535`]

指定要从中流式传输视频的 Raspberry Pi 硬件端口号。

### **挂载点** — 视频标识符 `stream01` (默认) | char | string

指定唯一标识符，以便为视频流创建 RTSP URL。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

通过实时流协议将视频流传输到网络

使用 RTSP Video Stream Transmit 模块，通过实时流协议 (RTSP) 将视频流传输到网络。您可以在网络上流式传输灰度、RGB 或 YCbCr 视频，并在连接到同一网络的设备上查看它。您还可以使用 H264 或 JPEG 标准对视频流进行编码。

**注意**

- 在 Simulink® 模型中使用此模块时，请至少使用 256 MB 的 Raspberry Pi® GPU 内存，以避免使用 RTSP 协议时视频馈送出现任何质量下降。
- 要为该模块生成 C/C++ 代码，您必须具有 Embedded Coder® 许可证。
