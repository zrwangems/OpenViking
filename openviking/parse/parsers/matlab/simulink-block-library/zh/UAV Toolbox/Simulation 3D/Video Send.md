---
type: simulink-block
title: 'Video Send'
family: 'simulation-3d'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'videosend'
documentation_source_path: 'ref/videosend.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Send

## 端口

### 输入

### **Image** — 要流式传输的 RGB 或灰度图像信号 *M*-by-*N*-by-*3* 矩阵 | *M*-by-*N* 矩阵

要流式传输的 RGB 或灰度图像信号，分别指定为 *M*-by-*N*-by-*3* 矩阵或 *M*-by-*N* 矩阵。

#### 依赖项

`Image Signal` 参数必须设置为 `One multidimensional signal`。

**数据类型：** `uint8` | `uint16`

### **R** — 要流式传输的 RGB 图像的红色通道信号 *M*-by-*N* 矩阵。

要流式传输的 RGB 图像的红色通道信号，指定为 `M-by-N` 矩阵。

#### 依赖项

`Image Signal` 参数必须设置为 `Separate color signals`。

**数据类型：** `uint8`

### **G** — 要流式传输的 RGB 图像的绿色通道信号 *M*-by-*N* 矩阵

要流式传输的 RGB 图像的绿色通道信号，指定为 `M-by-N` 矩阵。

#### 依赖项

`Image Signal` 参数必须设置为 `Separate color signals`。

**数据类型：** `uint8`

### **B** — 要流式传输的 RGB 图像的蓝色通道信号 *M*-by-*N* 矩阵

要流式传输的 RGB 图像的蓝色通道信号，指定为 `M-by-N` 矩阵。

#### 依赖项

`Image Signal` 参数必须设置为 `Separate color signals`。

**数据类型：** `uint8`

## 参数

#### 视频参数

### **Format** — 输入视频流信号格式 `RGB`（默认） | `Grayscale` | `Grayscale (16-bit)`

将输入视频流信号格式指定为以下项之一：

- `RGB` - RGB 图像（每个颜色通道 8-bit）。
- `Grayscale` - 灰度图像（8-bit）。
- `Grayscale (16-bit)` - 灰度图像（16-bit）。

### **Image signal** — RGB 图像输入信号的性质 `One multidimensional signal`（默认） | `Separate color signals`

将 RGB 图像输入信号的性质指定为以下项之一：

- `One multidimensional signal` - 用于具有 R、G 和 B 颜色通道的 *M*-by-*N*-by-*3* 彩色视频信号的一个输入端口。
- `Separate color signals` - 用于 R、G 和 B 通道的三个单独输入端口。每个端口接受一个 *M*-by-*N* 矩阵。

#### 依赖项

`Format` 参数必须设置为 `RGB`。

### **Compression** — 视频流的压缩格式 `JPEG`（默认） | `VP8` | `VP9`

将视频流的压缩格式指定为以下项之一：

- `JPEG` - 使用 jpeg GStreamer 插件。

  - 这使用以下 GStreamer pipeline：

    ```
    video/x-raw,format=I420 ! jpegenc quality=<Quality> idct-method=1 ! rtpjpegpay ! udpsink sync=false host=<Remote address> port=<Remote port>
    ```
- `VP8` - 使用 vpx GStreamer 插件。

  - 这使用以下 GStreamer pipeline：

    ```
    vp8enc deadline=<Max frame time*1000> bits-per-pixel=0.0434 target-bitrate=0 threads=8 lag-in-frames=0 ! rtpvp8pay ! udpsink sync=false host=<Remote address> port=<Remote port>
    ```
- `VP9` - 使用 vpx GStreamer 插件。

  - 这使用以下 GStreamer pipeline：

    ```
    vp9enc deadline=<Max frame time*1000> bits-per-pixel=0.0434 target-bitrate=0 threads=8 lag-in-frames=0 ! rtpvp9pay ! udpsink sync=false host=<Remote address> port=<Remote port>
    ```

### **Quality** — 视频流的质量 85（默认） | `0`-`100`

将 JPEG 视频流的质量指定为 positive scalar。此参数控制视频流的编码速度和压缩率。较高的质量值会提高图像质量，但会占用更高的网络带宽。对于低带宽网络连接，请指定较低的值。

#### 依赖项

`Compression` 参数必须设置为 `JPEG`。

### **Max frame time (ms)** — 每帧的最大时间 30（默认） | non-negative integer

将 VP8 或 VP9 视频流的最大帧时间指定为 positive integer，以 milliseconds 为单位。此参数控制编解码器用于编码图像的最大处理时间。根据输入 `Image` 的帧率设置此参数。一个良好的起始值为 `1000/fps`，其中 `fps` 是输入视频信号的采样率。如果希望编码器按所需时间进行编码，请设置为 0，这会提高质量，但会增加压缩所需的时间。

#### 依赖项

`Compression` 参数必须设置为 `VP8` 或 `VP9`。

#### 连接参数

### **Remote address** — 远程 IP 地址 127.0.0.1（默认） | character vector

将模块向其发送消息的远程设备的 IP 地址或主机名指定为 character vector。

### **Remote port** — 远程 IP 端口 5004（默认） | 0-65535

指定模块向其发送消息的远程设备的 IP 端口。流式传输视频时，此模块会选择第一个可用的本地 UDP 端口，与您指定的远程端口无关。

## 所属库

UAV Toolbox / Simulation 3D

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

将视频流发送到远程硬件

Video Send 模块将视频流从 Simulink® 发送到指定的远程设备。对于硬件在环仿真应用，您可以将从 Unreal Engine® 场景收集的灰度和 RGB 图像以及深度和激光雷达点云数据发送到远程设备。您还可以指定视频流的压缩和质量。要流式传输视频，此模块会选择第一个可用的本地 UDP 端口，与您指定的远程端口无关。此模块使用 Gstreamer 框架处理数据流式传输。
