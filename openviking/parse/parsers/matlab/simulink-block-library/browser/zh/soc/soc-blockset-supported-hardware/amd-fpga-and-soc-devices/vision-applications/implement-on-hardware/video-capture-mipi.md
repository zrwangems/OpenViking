---
type: simulink-block
title: 'Video Capture MIPI'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'videocapturemipi'
documentation_source_path: 'ref/videocapturemipi.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Capture MIPI

## 端口

### 输出

### **R, G, B** — 输入视频帧矩阵的颜色分量

该模块为输入视频的每个颜色分量返回一个矩阵。每个矩阵的维度与帧大小匹配。

#### 依赖关系

要启用这些端口，请将 **像素格式** 设置为 `RGB`，并将 **图像信号** 设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Image** — 彩色输入视频帧矩阵

该模块返回一个 3×*height*×*width* 矩阵，其中 *height* 和 *width* 与帧大小匹配。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `RGB`，并将 **图像信号** 设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **视频源** — 视频流的来源 `IMX274 sensor`

视频流来自 IMX274 摄像头板。设置 **帧大小** 参数以匹配所连接摄像头的分辨率。

### **帧大小** — 输入视频的分辨率 `1280x720p`（默认）| `1920x1080p`

选择 720p HDTV 格式（`1280x720p`）或 1080p HDTV 格式（`1920x1080p`）。

### **帧率** — 连续图像显示的速率（帧/秒）`120 fps`（默认）| `60 fps`

该模块将捕获视频帧的 Simulink 采样时间设置为 1/**帧率**。

帧大小 `1920x1080p` 仅支持 `60 fps`。

### **像素格式** — 像素流的格式 `RGB`

`RGB` 像素流格式为每个像素返回三个 8 位颜色分量，即每个像素总共 24 位。您还可以选择该模块返回一个多维信号还是三个单独的颜色信号。有关详细信息，请参阅 **图像信号** 参数。

### **图像信号** — RGB 输出流格式 `Separate color signals`（默认）| `One multidimensional signal`

将 RGB 输出流格式指定为以下值之一。

- `Separate color signals` — 该模块为每个颜色分量返回单独的 *height*×*width* 矩阵。在这种情况下，该模块具有 **R**、**G** 和 **B** 输出端口。
- `One multidimensional signal` — 该模块返回单个 3×*height*×*width* 矩阵。在这种情况下，该模块具有一个 **Image** 输出端口。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从基于 Zynq 的硬件上的 MIPI CSI-2 卡导入实时视频帧

Video Capture MIPI 模块从连接到基于 Zynq® 的板卡的 IMX274 FMC MIPI® CSI-2® 卡捕获视频帧，并将这些帧导入到您的 Simulink® 模型中。参考设计使用一个映像对 FPGA 进行编程，该映像对来自传感器的视频输入进行去马赛克和伽马校正，并允许从 Simulink 捕获视频。您可以从 Video Capture MIPI 模块控制帧大小和 Simulink 视频信号格式选项。

FPGA 映像还包含一个称为 FPGA 用户逻辑的 IP 核，您可以使用 HDL Workflow Advisor 从您的设计生成该 IP 核。该模块在 FPGA 用户逻辑之后捕获输入视频。

在 FPGA 上，视频数据采用 AXI4-Stream Video 格式。当您将视频导入 Simulink 时，该流会转换为基于帧的视频。

`MIPI Receive path` 参考设计要求整个数据路径使用相同的视频分辨率和颜色格式。您定位到 FPGA 用户逻辑的设计不得修改数据的帧大小或格式。
