---
type: simulink-block
title: 'Video Test Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'videotestsource'
documentation_source_path: 'ref/videotestsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Test Source

## 端口

### 输入

### **wrCtrlIn** — 输入控制总线 bus

来自数据消费者的控制总线，用于指示数据消费者已准备好接受视频流数据。该控制总线包含一个 ready 信号。

**数据类型：** `StreamVideoS2MBusObj`
### 输出

### **wrData** — 输出视频流数据向量

向数据消费者输出视频流数据。该值以向量形式返回。

**数据类型：** `uint8`

### **wrCtrlOut** — 输出控制总线 bus

向数据消费者输出的控制总线，以 bus 形式返回。该控制总线包含以下控制信号：

- `hStart` — 一帧中水平行的第一个像素
- `hEnd` — 一帧中水平行的最后一个像素
- `vStart` — 一帧中第一（顶部）行的第一个像素
- `vEnd` — 一帧中最后（底部）行的最后一个像素
- `valid` — 指示 **wrData** 输出端口上的输出像素数据是否有效

**数据类型：** `pixelcontrol`

## 参数

### **Frame size** — 帧尺寸 `160x120p`（默认）| ...

选择帧尺寸为以下值之一：

- `480p SDTV (720x480p)`
- `576p SDTV (720x576p)`
- `720p HDTV (1280x720p)`
- `1080p HDTV (1920x1080p)`
- `160x120p`
- `320x240p`
- `640x480p`
- `800x600p`
- `1024x768p`
- `1280x768p`
- `1280x1024p`
- `1360x768p`
- `1366x768p`
- `1400x1050p`
- `1600x1200p`
- `1680x1050p`
- `1920x1200p`

### **Video source** — 选择视频源类型 `Video file`（默认）| `Color bar` | `Ramp`

选择视频源类型为 `Video file`、`Color bar` 或 `Ramp`。

### **Input file name** — 选择输入视频文件 `handshake_left.avi`（默认）| 任何支持的视频文件格式

通过点击 **Browse** 按钮并导航到视频文件位置来选择输入视频文件。

#### 依赖关系

要启用此参数，请将 **Video source** 参数设置为 `Video file`。

### **Color space** — 色彩空间 `YCbCr422`（默认）| `RGB` | `YOnly`

选择色彩空间类型为 `YCbCr422`、`RGB` 或 `YOnly`。

### **Reorder output frame** — 输出帧重排序 `off`（默认）| `on`

选择此选项可将输出像素重排序为*列主序*。流式像素格式顺序为从左到右遍历每一行，然后向下到下一行，即*行主序*。然而，某些矩阵运算使用*列主序*，即从上到下，然后向右到下一列。

### **Frame sample time** — 帧采样时间 `1/60`（默认）| 正标量

将帧采样时间指定为正标量。默认值 `1/60` 中的分母表示每秒帧数。

## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

R2025b 中未记录。

## 扩展功能

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

生成连续视频流数据

Video Test Source 模块向基于高级可扩展接口 AXI4 的视频流数据接口模块生成连续视频流数据。您可以将此模块用作测试源模块，用于仿真基于 AXI4 的视频流数据应用。

该模块接受一个控制总线，并输出视频流数据以及一个控制总线。
