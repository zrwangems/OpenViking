---
type: simulink-block
title: 'V4L2 Video Capture'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Video'
documentation_page: 'v4l2videocapture'
documentation_source_path: 'beagleboneblue/ref/v4l2videocapture.html'
language: zh-CN
chinese_source: worker-translation
---

# V4L2 Video Capture

## 端口

### 输出

### **R** — 像素矩阵的红色分量

此端口输出每个像素的红色分量。

#### 依赖项

仅当您从 **Pixel format** 中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **G** — 像素矩阵的绿色分量

此端口输出每个像素的绿色分量。

#### 依赖项

仅当您从 **Pixel format** 中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **B** — 像素矩阵的蓝色分量

此端口输出每个像素的蓝色分量。

#### 依赖项

仅当您从 **Pixel format** 中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **Y** — 像素矩阵的亮度分量

此端口输出每个像素的亮度分量。

#### 依赖项

仅当您从 **Pixel format** 中选择 `YCbCr 4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

### **Cb** — 像素矩阵的蓝色差分量

此端口输出每个像素的蓝色差分量。

#### 依赖项

仅当您从 **Pixel format** 中选择 `YCbCr 4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

### **Cr** — 像素矩阵的红色差分量

此端口输出每个像素的红色差分量。

#### 依赖项

仅当您从 **Pixel format** 中选择 `YCbCr 4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

## 参数

### **Device name** — 已连接视频设备的名称 `'/dev/video0'`（默认）

输入视频设备的路径和名称。

当您将受支持的 USB 视频摄像头连接到目标硬件时，Linux 内核会创建一个视频设备文件。默认情况下，Linux 内核支持所有 USB video class (UVC) 设备。

要查看视频设备文件列表，请打开与目标硬件的命令行会话，并输入：`ls -al /dev/video*`。

### **Image size** — 显示分辨率 320x240（默认）| 160x120 | Custom

指定要捕获的图像的显示分辨率，以像素为单位。

### **Image size ([width, height])** — 要捕获的图像大小 `[640,480]`（默认）

指定要捕获的图像的宽度（以像素为单位）和高度（以行为单位）。

#### 依赖项

仅当您从 **Image Size** 中选择 `Custom` 时，此参数才会出现。

### **Pixel format** — 输出视频流的格式 RGB（默认）

选择视频设备的视频格式：`RGB` 或 `YCbCr 4:2:2`。

`RGB` 使用 8 位值表示像素的红色、绿色和蓝色分量。RGB 颜色空间取决于设备。

`YCbCr 4:2:2` 使用三个通道来表示每个像素的彩色图像数据：

- `Y` 是亮度分量（本质上是一种灰度信号）。
- `Cb` 是蓝色差色度分量。
- `Cr` 是红色差色度分量。

Cb 和 Cr 分量的采样率是 Y 的一半。

### **Sample time** — 捕获新图像的频率 `1/10`（默认）

选择视频设备的采样时间。

较小的值要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Video

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

使用 V4L2 从 USB 摄像头捕获视频

使用 V4L2（Video for Linux Two API）驱动程序框架从 USB 视频摄像头捕获实时视频。输出采用行主序格式。在仿真期间，模型输出移动的色条图像。

目标硬件上使用的 Ubuntu® Linux® 镜像支持从列为 Universal Video Class (UVC) 的 USB 摄像头进行视频捕获。除了是 UVC 类摄像头外，摄像头本身还必须支持 YUYV 模式下的数据采集。

以下摄像头已经过测试：

- Logitech QuickCam Pro 9000
- Logitech QuickCam Pro 3000
- Logitech Webcam C600
- Logitech HD Webcam C310
