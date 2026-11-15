---
type: simulink-block
title: 'RTSP Video Stream Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'rtspvideostreamreceive'
documentation_source_path: 'supportpkg/raspberrypi_ref/rtspvideostreamreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# RTSP Video Stream Receive

## 端口

### 输出

### **Status** — 流视频的状态标量

该端口在从发送端接收视频时输出 RTSP Video Stream Receive 模块的状态。

- `0` — 表示通过网络成功读取视频流。
- `1` — 表示来自发送端的流中断，进而导致 RTSP Video Stream Receive 模块无法从发送端读取任何进一步的数据。
- `2` — 表示需要用户干预才能修复的流错误，例如 Raspberry Pi® 硬件无法从发送端接收数据。
- `3` — 表示可能由于流 URL 或图像属性配置错误而发生的 GStreamer 管道创建错误。
- `4` — 表示阻止模块进一步执行的致命错误，例如内部程序故障。

**数据类型：** `int32`

### **R** — 输出视频矩阵的红色分量

RGB 视频的红色通道信号，指定为 *M*×*N* 的 pixels 网格。这里，
*M* 是红色分量的行数，*N* 是红色分量的列数。

#### 依赖关系

- 要启用此端口，请将 **Image format** 设置为
  `RGB`。

**数据类型：** `uint8`

### **G** — 输出视频矩阵的绿色分量

RGB 视频的绿色通道信号，指定为 *M*×*N* 的 pixels 网格。这里，
*M* 是绿色分量的行数，*N* 是绿色分量的列数。

#### 依赖关系

- 要启用此端口，请将 **Image format** 设置为
  `RGB`。

**数据类型：** `uint8`

### **B** — 输出视频矩阵的蓝色分量

RGB 视频的蓝色通道信号，指定为 *M*×*N* 的 pixels 网格。这里，
*M* 是蓝色分量的行数，*N* 是蓝色分量的列数。

#### 依赖关系

- 要启用此端口，请将 **Image format** 设置为
  `RGB`。

**数据类型：** `uint8`

### **Y** — 输出视频矩阵的亮度分量

视频的亮度分量，指定为 *M*×*N* 的 pixels 网格。这里，
*M* 是亮度分量的行数，*N* 是亮度分量的列数。

#### 依赖关系

- 要启用此端口，请将 **Image format** 设置为
  `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cb** — 输出视频矩阵的蓝色差色度分量

视频的蓝色差色度分量，指定为 *M*×*N* 的 pixels 网格。这里，
*M* 是蓝色差色度分量的行数，*N* 是蓝色差色度分量的列数。

#### 依赖关系

- 要启用此端口，请将 **Image format** 设置为
  `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cr** — 输出视频矩阵的红色差色度分量

视频的红色差色度分量，指定为 *M*×*N* 的 pixels 网格。这里，
*M* 是红色差色度分量的行数，*N* 是红色差色度分量的列数。

#### 依赖关系

- 要启用此端口，请将 **Image format** 设置为
  `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **I** — 灰度输出视频矩阵

灰度视频，指定为 *M*×*N* 的 pixels 网格。这里，*M* 是灰度视频的行数，*N* 是灰度视频的列数。

#### 依赖关系

- 要启用此端口，请将 **Image format** 设置为
  `Grayscale`。

**数据类型：** `uint8`

## 参数

### **RTSP URL** — RTSP 流 URL `rtsp://127.0.0.1:8554/stream01`（默认） | char | string

按以下格式指定用于接收视频流的唯一 RTSP URL：
`rtsp://<raspberrypi IP address>/<mount point
identifier>`

### **Image format** — 输出视频流格式 `RGB`（默认） | `YCbCr 4:2:2` | `Grayscale`

指定输出视频流的格式。

**提示**

要在设备上查看彩色视频，请将此参数设置为 `YCbCr
4:2:2`。由于此格式需要更少的带宽，您可以在不明显影响视频质量的情况下流式传输视频。

### **Image size** — 视频帧的图像分辨率 `640x480`（默认） | `160x120` | `320x240` | `800x600` | `1280x720` | `custom`

指定视频帧的图像分辨率，以 pixels 为单位。

### **Image size ([width, height])** — 自定义图像分辨率 `[640, 480]`（默认） | [`width`, `height`]

指定输出图像的自定义分辨率，以 pixels 为单位。

#### 依赖关系

- 要启用此参数，请将 **Image size** 设置为
  `custom`。

### **Video compression** — 视频流的解码格式 `H264`（默认） | `JPEG`

选择实时流协议（RTSP）视频流的解码格式。

### **Sample time** — 模块输出图像帧的时间频率 `0.1`（默认） | 标量

指定模块从视频流输出图像帧的频率。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

通过实时流协议从网络接收视频

使用 RTSP Video Stream Receive 模块从网络上的流媒体源接收实时流协议（RTSP）视频流。您可以使用 RTSP Video Stream Transmit 模块或任何其他 RTSP 流媒体设备创建通过网络流式传输视频的源。该模块输出灰度、RGB 或 YCbCr 视频。该模块可以使用 H264 或 JPEG 视频编码标准解码视频流。

**注意**

要为该模块生成 C/C++ 代码，您必须拥有 Embedded Coder® 许可证。
