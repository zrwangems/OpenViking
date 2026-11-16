---
type: simulink-block
title: 'Video Capture USB'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'videocaptureusb'
documentation_source_path: 'ref/videocaptureusb.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Capture USB

## 端口

### 输出

### **Y, Cb, Cr** — 输入视频帧矩阵的颜色分量

该模块为输入视频的每个颜色分量返回一个矩阵。**Y** 矩阵的维度与帧大小匹配。**Cb** 和 **Cr** 矩阵的维度为 *height*-by-`width/2`，因为 4:2:2 格式会为帧中的每个像素交替 **Cb** 和 **Cr** 值。

#### 依赖关系

要启用这些端口，请将 **Pixel format** 设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **R, G, B** — 输入视频帧矩阵的颜色分量

该模块为输入视频的每个颜色分量返回一个矩阵。每个矩阵的维度与帧大小匹配。

#### 依赖关系

要启用这些端口，请将 **Pixel format** 设置为 `RGB`，并将 **Image signal** 设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Image** — 彩色输入视频帧矩阵

该模块返回一个 3-by-*height*-by-*width* 矩阵，其中 *height* 和 *width* 与帧大小匹配。

#### 依赖关系

要启用此端口，请将 **Pixel format** 设置为 `RGB`，并将 **Image signal** 设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **IP address** — SoC 设备的地址 192.168.1.101（默认）

连接到您的主机的 SoC 设备的以太网地址。

### **Video source** — 视频流来源 *detected UVC camera name* | `USB 3.0 Basler Camera` | `Test pattern generator`

通过 FPGA 逻辑和 ARM® 处理器的视频流可以从 SoC 设备的 USB 端口输入视频开始，也可以从测试图案生成器 (TPG) 生成的视频开始。使用 **Scan** 按钮检测连接到您 SoC 设备 USB 端口的一个或多个相机。下拉菜单会更新为检测到的相机名称。

- *detected UVC camera name* — 连接到 SoC 设备上 USB 输入端口的相机。**Frame size** 参数菜单会更新，以匹配检测到的相机可用的分辨率。
- `USB 3.0 Basler Camera` — 连接到 SoC 设备上 USB 输入端口的相机。**Frame size** 参数菜单会更新为受支持分辨率的列表。
- `Test pattern generator` — 板载 TPG。SD 卡上的 TPG 会按请求的分辨率创建输入帧。在 **Test pattern** 参数中选择固定彩条图案或移动球。当您选择 TPG 时，不需要相机连接到 SoC 设备上的 USB 端口。

### **Test pattern** — 板载视频源 `SMPTE color bars` | `Moving ball`

SD 卡上的测试图案生成器会按请求的分辨率创建输入帧。

- `SMPTE color bars` —

  当您将 Test pattern 设置为 SMPTE color bars 时捕获的彩条测试图案。
- `Moving ball` —

  当您将 Test pattern 设置为 Moving ball 时捕获的彩条测试图案。

### **Frame size** — 输入视频的分辨率 *detected from camera* | `320x240p` | `640x480p` | `1280x720p` | `1920x1080p`

从检测到的相机上可用的受支持分辨率中进行选择。

要使用大于 2k 分辨率的帧大小，您必须将 FPGA 参考设计配置为使用 2-pixel-per-clock streaming。设置期间加载的默认参考设计使用 2-pixel-per-clock streaming。您可以在 HDL Workflow Advisor 的 Step 1.2 中配置每个时钟的像素数。有关详细信息，请参阅 Target FPGA on Zynq Hardware。

对于 Basler USB 3.0 相机或测试图案生成器，以下分辨率可用：

- `320x240p`
- `640x480p`
- `1280x720p`
- `1920x1080p`

### **Frame rate** — 连续图像显示的速率（每秒帧数）*calculated from resolution*

该模块根据检测到的相机可用的受支持分辨率计算可用帧率。对于低于 1080p 的分辨率，该模块可以达到最高 120 fps。

该模块将捕获视频帧的 Simulink 采样时间设置为 1/**Frame rate**。

### **Host pixel format** — 导入到 Simulink 的像素流的格式 `YCbCr 4:2:2`（默认） | `RGB`

将像素流的格式指定为以下值之一。

- `RGB` — 每个像素三个 8 bit 颜色分量，即总共每像素 24 bits。
- `YCbCr 4:2:2`（默认） — 也称为 YUYV。一个 8 bit Y 分量和一个交错的 8 bit CbCr 分量。有效像素大小为 16 bits。该模块在 **Y**、**Cb** 和 **Cr** 输出端口上返回分量帧。

### **DUT pixel format** — 用户逻辑中像素流的格式 `YCbCr 4:2:2`（默认） | `RGB`

将像素流的格式指定为以下值之一。

- `RGB` — 每个像素三个 8 bit 颜色分量，即总共每像素 24 bits。
- `YCbCr 4:2:2`（默认） — 也称为 YUYV。一个 8 bit Y 分量和一个交错的 8 bit CbCr 分量。有效像素大小为 16 bits。该模块在 **Y**、**Cb** 和 **Cr** 输出端口上返回分量帧。

### **Bypass FPGA user logic** — 将输入帧直接发送到主机 `off`（默认） | `on`

选择此参数以绕过 FPGA 的用户逻辑部分，并将输入视频帧直接发送到主机。

### **Image signal** — RGB 输出流格式 `Separate color signals`（默认） | `One multidimensional signal`

将 RGB 输出流格式指定为以下值之一。

- `Separate color signals` — 该模块为每个颜色分量返回单独的 *height*-by-*width* 矩阵。在这种情况下，该模块具有 **R**、**G** 和 **B** 输出端口。
- `One multidimensional signal` — 该模块返回单个 3-by-*height*-by-*width* 矩阵。在这种情况下，该模块具有 **Image** 输出端口。

#### 依赖关系

要启用此参数，请将 **Pixel format** 设置为 `RGB`。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106 SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

从基于 Zynq 的硬件上的一个或多个 USB 相机导入实时视频帧

Video Capture USB 模块从具有一个或多个 USB 视频设备类 (UVC) 相机或 Basler USB 3.0 相机的基于 Zynq® 的板捕获视频帧，并将这些帧导入到您的 Simulink® 模型中。参考设计使用包含 USB 相机接口、数据路径多路复用器、视频格式转换和视频测试图案生成器 (TPG) 的映像对 FPGA 进行编程。您可以从 Video Capture USB 模块控制这些数据路径和转换选项。
