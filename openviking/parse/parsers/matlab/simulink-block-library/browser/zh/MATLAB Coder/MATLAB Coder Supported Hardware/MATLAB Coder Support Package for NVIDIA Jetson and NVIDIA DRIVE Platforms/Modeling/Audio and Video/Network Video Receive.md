---
type: simulink-block
title: 'Network Video Receive'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'networkvideoreceive'
documentation_source_path: 'nvidia/ref/networkvideoreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Network Video Receive

## 端口

### 输出

### **Image** — 图像信号矩阵

此端口输出每个像素的图像信号。

#### 依赖项

当你在模块参数窗口中选择 `RGB` 作为 **格式**，并选择 `One multidimensional signal` 作为 **图像信号**，或者选择 `Grayscale` 作为 **格式** 时，会出现此端口。

**数据类型：** `uint8` | `uint16`

### **R** — 输出视频流矩阵的红色分量

此端口输出每个像素的红色分量。

#### 依赖项

仅当你在模块参数窗口中选择 `RGB` 作为 **格式**，并选择 `Separate color signal` 作为 **图像信号** 时，才会出现此端口。

**数据类型：** `uint8`

### **G** — 输出视频流矩阵的绿色分量

此端口输出每个像素的绿色分量。

#### 依赖项

仅当你在模块参数窗口中选择 `RGB` 作为 **格式**，并选择 `Separate color signal` 作为 **图像信号** 时，才会出现此端口。

**数据类型：** `uint8`

### **B** — 输出视频流矩阵的蓝色分量

此端口输出每个像素的蓝色分量。

#### 依赖项

仅当你在模块参数窗口中选择 `RGB` 作为 **格式**，并选择 `Separate color signal` 作为 **图像信号** 时，才会出现此端口。

**数据类型：** `uint8`

## 参数

### 视频参数

### **视频源** — 视频流源 `Network stream` (默认) | `Network device`

指定视频流的源。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VideoSource` |
| **类型：** character vector |
| **值：** `'Network stream'`|`'Network device'` |
| **默认值：**  `'Network stream'` |

### **图像大小** — 图像分辨率 `[320, 240]` (默认) | `[width, height]`

指定要捕获的图像分辨率，以 pixels 为单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ImageSize` |
| **类型：** character vector |
| **值：** `[width, height]`| |
| **默认值：**  `'[320, 240]'` |

### **格式** — 视频流格式 `Grayscale (16-bit)` | `Grayscale` | `RGB`

指定视频流的格式。格式选项基于 **视频源** 的设置值。

|  | Network stream | Network device |
| --- | --- | --- |
| 可用的流格式 | `'Grayscale (16-bit)'` (默认) | `'Grayscale'` |
| `'Grayscale'` | `'RGB'` (默认) |
| `'RGB'` | - |
| 模块参数名称 | `'ImageFormat'` | `'DeviceImageFormat'` |

#### 程序化使用

|  |
| --- |
| **模块参数：** `ImageFormat`|`DeviceImageFormat` |
| **类型：** character vector |
| **值：** `'RGB'`|`'Grayscale'`|`'Grayscale (16-bit)'` |

### **图像信号** — 输出信号格式 `One multidimensional signal` (默认) | `Separate color signal`

指定如何输出 RGB 彩色视频信号。如果选择 `One multidimensional signal`，模块会在 `Image` 端口输出一个 M-by-N-by-P 彩色视频信号，其中 P 是颜色平面数。如果选择 `Separate color signal`，模块上会出现额外的端口。每个端口输出 RGB 视频流的一个 M-by-N 平面。

#### 依赖项

要启用此参数，请将 **格式** 设置为 `RGB`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ImageSignal` |
| **类型：** character vector |
| **值：** `'One multidimensional signal'`|`'Separate color signal'`| |
| **默认值：**  `'One multidimensional signal'` |

### **压缩** — 视频压缩算法 `JPEG` | `VP8` | `VP9` | `H264` | `H265` | `None (uncompressed)`

选择用于解码 RTP 视频流的压缩算法类型。压缩选项基于 **视频源** 的设置值。

|  | Network stream | Network device |
| --- | --- | --- |
| 可用的压缩算法 | `'JPEG'` (默认) | `'H264'` (默认) |
| `'VP8'` | `'H265'` |
| `'VP9'` | - |
| `'H264'` | - |
| `'H265'` | - |
| `'None (uncompressed)'` | - |
| 模块参数名称 | `'Decoder'` | `'VideoDeviceDecoder'` |

**注意**

选择 `H265` 解码器时，接收器必须在发送器启动视频流之前启动。这是因为解码数据所需的元数据在流开始时发出。或者，你可以配置发送器在流中按间隔插入此元数据。例如，使用 GStreamer 时，使用以下命令，

    gst-launch-1.0 -v videotestsrc is-live=true ! video/x-raw,
    framerate=100/1,width=320,height=240 ! videoconvert
    ! x265enc tune=zerolatency ! h265parse config-interval=2
    ! rtph265pay ! udpsink host=127.0.0.1 port=3000

#### 程序化使用

|  |
| --- |
| **模块参数：** `Decoder` | `VideoDeviceDecoder` |
| **类型：** character vector |
| **值：** `'JPEG'`|`'VP8'`|`'VP9'`|`'H264'`|`'H265'`|`'None (uncompressed)'` |

### **启用硬件加速** — 使用图形硬件进行解码 `on` (默认) | off

选择此参数可启用 NVIDIA® 目标上的图形硬件进行解码。

**注意**

启用硬件加速时，如果发送器和接收器的分辨率规格不同，图像分辨率会自动缩放。如果禁用硬件加速，自动缩放也会被禁用。在这种情况下，发送器和接收器的图像分辨率规格必须相同。

如果视频帧大小不是 16 的倍数，硬件加速器库会填充所接收视频帧的边界，以输出请求的大小。如果不希望出现此行为，请禁用硬件加速。

### 连接参数

### **端口** — NVIDIA 板上用于接收数据的端口 `3000` | 范围 `[1,65535]` 内的正整数

指定你希望从中接收视频数据包的端口号。将本地端口号与发送主机的远程端口号匹配。

#### 依赖项

要启用此参数，请将 **视频源** 设置为 `Network stream`。

### **RTSP URL** — IP 摄像机的 RTSP URL `char` | `string`

IP 摄像机的 RTSP URL，指定为 character vector。

#### 依赖项

要启用此参数，请将 **视频源** 设置为 `Network device`。

### **采样时间** — 捕获新图像的频率 `0.1` (默认) | scalar | `vector`

选择视频设备的采样时间。

较小的值要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'0.1'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

从网络 RTP 或 IP 摄像机 RTSP 流接收视频

从网络 RTP 或 IP 摄像机 RTSP 流接收视频。在硬件上运行时，该模块输出来自网络或 IP 摄像机的视频。
