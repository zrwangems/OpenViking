---
type: simulink-block
title: 'V4L2 Video Capture'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'v4l2videocapture'
documentation_source_path: 'beaglebone/ref/v4l2videocapture.html'
language: zh-CN
chinese_source: worker-translation
---

# V4L2 Video Capture

## 端口

### 输出

### **R** — 像素矩阵的红色分量

该模块输出每个像素的红色分量。

#### 依赖项

- 要启用此端口，请将 **Pixel format** 设置为
  `RGB`。

**数据类型：** `uint8`

### **G** — 像素矩阵的绿色分量

该模块输出每个像素的绿色分量。

#### 依赖项

- 要启用此端口，请将 **Pixel format** 设置为
  `RGB`。

**数据类型：** `uint8`

### **B** — 像素矩阵的蓝色分量

该模块输出每个像素的蓝色分量。

#### 依赖项

- 要启用此端口，请将 **Pixel format** 设置为
  `RGB`。

**数据类型：** `uint8`

### **Y** — 像素矩阵的亮度分量

该模块输出每个像素的亮度分量。

#### 依赖项

- 要启用此端口，请将 **Pixel format** 设置为
  `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cb** — 像素矩阵的蓝色差分量

该模块输出每个像素的蓝色差分量。

#### 依赖项

- 要启用此端口，请将 **Pixel format** 设置为
  `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cr** — 像素矩阵的红色差分量

该模块输出每个像素的红色差分量。

#### 依赖项

- 要启用此端口，请将 **Pixel format** 设置为
  `YCbCr 4:2:2`。

**数据类型：** `uint8`

## 参数

### **Device name** — 视频设备的名称 `'/dev/video0'`（默认）| character array

输入视频设备的路径和名称。当您将受支持的 USB 视频摄像头连接到目标硬件时，Linux 内核会创建视频设备文件。默认情况下，Linux 内核支持所有 UVC 设备。

要查看视频设备文件列表，请打开与开发板的命令行会话，然后输入：`ls -al /dev/video*`。

### **Image size** — 图像的显示分辨率 `320x240`（默认）| `160x120` | `640x480` | `800x600` | `custom`

选择图像的显示分辨率（以 pixels 为单位）。

### **Image size ([width, height])** — 图像大小 640x480（默认）| positive integer

输入图像的宽度（以 pixels 为单位）和高度（以 lines 为单位）。

#### 依赖项

要启用此参数，请将 **Image size** 设置为 `custom`。

### **Pixel format** — 输出视频流的格式 `RGB`（默认）| `YCbCr 4:2:2`

将视频设备的格式设置为 `RGB` 或 `YCbCr 4:2:2`。

`RGB` 使用 8-bit 值表示像素的红色、绿色和蓝色分量。RGB 颜色空间取决于设备。

`YCbCr 4:2:2` 使用三个通道表示每个像素的彩色图像数据：

- `Y` 是亮度分量（本质上是一个灰度信号）。
- `Cb` 是蓝色差色度分量。
- `Cr` 是红色差色度分量。

`Cb` 和 `Cr` 分量以 `Y` 采样率的一半进行采样。

### **Sample time** — 设备捕获新图像的频率 `0.1`（默认）| scalar

输入视频设备的采样时间。较小的值要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

使用 V4L2 框架从 USB 摄像头捕获视频

V4L2 Video Capture 模块使您能够使用 Video for Linux Two API (V4L2) 驱动程序框架从 USB 视频摄像头捕获实时视频。在仿真期间，该模块输出移动彩条图像。

Raspberry Pi® 硬件上的 debian Linux® 镜像支持从符合 USB video class (UVC) 规范的 USB 摄像头进行视频捕获。除了是符合 UVC 的摄像头外，摄像头本身还应支持以 YUYV 模式进行数据采集。

以下摄像头已使用 V4L2 Video Capture 模块进行测试，但不限于：

- Logitech QuickCam Pro 9000
- Logitech QuickCam Pro 3000
- Logitech Webcam C600
- Logitech HD Webcam C310

有时，当您将 USB 网络摄像头连接到正在运行的 BeagleBone® Black 硬件时，BeagleBone Black 硬件无法识别该 USB 网络摄像头。要验证 BeagleBone Black 硬件是否识别该 USB 网络摄像头，请在 Command Window 中输入：

    bbone = beaglebone_black;
    system(bbone,'ls -al /dev/videox')

如果开发板识别出该 USB 摄像头，此命令会返回与该 USB 摄像头关联的视频设备名称。否则，重新启动 BeagleBone Black 硬件。重新启动后，如果 BeagleBone Black 硬件仍无法识别该 USB 网络摄像头，则可能该网络摄像头不是受支持的设备。请尝试使用其他 USB 网络摄像头。
