---
type: simulink-block
title: 'V4L2 Video Capture'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'v4l2videocapture'
documentation_source_path: 'supportpkg/raspberrypi_ref/v4l2videocapture.html'
language: zh-CN
chinese_source: worker-translation
---

# V4L2 Video Capture

## 端口

### 输出

### **R** — 像素矩阵的红色分量

该模块输出每个像素的红色分量。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **G** — 像素矩阵的绿色分量

该模块输出每个像素的绿色分量。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **B** — 像素矩阵的蓝色分量

该模块输出每个像素的蓝色分量。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **Y** — 像素矩阵的亮度分量

该模块输出每个像素的亮度分量。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cb** — 像素矩阵的蓝色差分量

该模块输出每个像素的蓝色差分量。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cr** — 像素矩阵的红色差分量

该模块输出每个像素的红色差分量。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

## 参数

### 基本

### **设备名称** — 视频设备的名称 `/dev/video0`（默认）| character array

输入视频设备的路径和名称。将受支持的 USB 视频摄像头连接到目标硬件时，Linux 内核会创建一个视频设备文件。默认情况下，Linux 内核支持所有 UVC 设备。

要查找视频设备的名称，请将硬件连接到 Raspberry Pi 板，并采用以下任一方法：

- 打开 Raspberry Pi Resource Monitor App。**设备 ID** 会填充在应用的 **外设** 部分中。
- 打开与 Raspberry Pi 硬件的命令行会话。执行以下命令：`ls -al /dev/video*`。

### **图像大小** — 图像的显示分辨率 `320x240`（默认）| `160x120` | `640x480` | `800x600` | `custom`

选择图像的显示分辨率（以 pixels 为单位）。

### **图像大小 ([width, height])** — 图像大小 [ 320, 240 ]（默认）| 正整数

输入图像的宽度（以 pixels 为单位）和高度（以 lines 为单位）。

#### 依赖关系

要启用此参数，请将 **图像大小** 设置为 `custom`。

### **像素格式** — 输出视频流的格式 `RGB`（默认）| `YCbCr 4:2:2`

将视频设备的格式设置为 `RGB` 或 `YCbCr 4:2:2`。

`RGB` 使用 8-bit 值表示像素的红、绿、蓝分量。RGB 颜色空间取决于设备。

`YCbCr 4:2:2` 使用三个通道表示每个像素的彩色图像数据：

- `Y` 是亮度分量（本质上是灰度信号）。
- `Cb` 是蓝色差色度分量。
- `Cr` 是红色差色度分量。

`Cb` 和 `Cr` 分量以 `Y` 的采样率的一半进行采样。

### **采样时间** — 设备捕获新图像的频率 `0.1`（默认）| 标量

输入视频设备的采样时间。较小的值要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。

### **沿水平轴翻转图像** — 水平翻转图像 `off`（默认）| `on`

选择该参数可沿图像的水平参考轴翻转图像。

### **沿垂直轴翻转图像** — 垂直翻转图像 `off`（默认）| `on`

选择该参数可沿图像的垂直参考轴翻转图像。

### 高级

**图像属性**

### **亮度** — 调整图像亮度 `0.5`（默认）| 正标量，范围为 [0, 1]

调整图像中的光量。

### **饱和度** — 调整图像饱和度 `0.5`（默认）| 正标量，范围为 [0, 1]

调整图像中的色彩量。

### **对比度** — 调整图像对比度 `0.5`（默认）| 标量，范围为 [0, 1]

调整图像中最暗区域和最亮区域之间的差异。

### **锐度** — 调整图像锐度 `0.5`（默认）| 标量，范围为 [0, 1]

调整锐度以突出图像中的边缘。

**设备属性**

并非所有摄像头都支持设备属性。

### **平移** — 调整摄像头平移 `0`（默认）| 标量，范围为 [-1, 1]

调整摄像头在水平平面中的视角。

### **倾斜** — 调整摄像头倾斜 `0`（默认）| 标量，范围为 [-1, 1]

调整摄像头在垂直平面中的视角。

### **缩放** — 调整摄像头缩放 `0.5`（默认）| 正标量，范围为 [0, 1]

放大或缩小摄像头。

### **启用手动对焦** — 手动对焦摄像头 `off`（默认）| `on`

选择该参数可手动调整摄像头对焦。

### **手动对焦** — 调整摄像头对焦 `0.5`（默认）| 正标量，范围为 [0, 1]

调整摄像头对焦以增强图像清晰度。

#### 依赖关系

要启用此参数，请选择 **启用手动对焦**。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2013a 中引入**

## 描述

使用 V4L2 框架从 USB 摄像头捕获视频

V4L2 Video Capture 模块使您能够使用 Video for Linux Two API (V4L2) 驱动程序框架从 USB 视频摄像头捕获实时视频。在仿真期间，该模块输出移动的彩条图像。

Raspberry Pi® 硬件上的 debian Linux® 镜像支持从符合 USB video class (UVC) 规范的 USB 摄像头进行视频捕获。除了是符合 UVC 的摄像头外，摄像头本身还应支持在 YUYV 模式下进行数据采集。

以下摄像头已使用 V4L2 Video Capture 模块进行测试，但不限于：

- Logitech QuickCam Pro 9000
- Logitech QuickCam Pro 3000
- Logitech Webcam C600
- Logitech HD Webcam C310

V4L2 Video Capture 模块支持 Raspberry Pi camera board 在以下运行于您的 Raspberry Pi 板上的 Raspbian Linux 操作系统上使用：Buster 和 Bullseye。有关如何为 Bookworm Raspbian Linux 操作系统使用 Raspberry Pi camera board 的详细信息，请参阅 Use Raspberry Pi Camera Board for Bookworm Raspbian Linux Operating System。
