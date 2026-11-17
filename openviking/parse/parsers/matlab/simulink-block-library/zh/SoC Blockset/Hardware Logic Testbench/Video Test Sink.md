---
type: simulink-block
title: 'Video Test Sink'
family: 'hardware-logic-testbench'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'videotestsink'
documentation_source_path: 'ref/videotestsink.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Test Sink

## 端口

### 输入

### **rdData** — 输入视频流数据向量

来自数据源的输入视频流数据。此值必须为向量。

**数据类型：** `uint8`

### **rdCtrlIn** — 输入控制总线 bus

来自数据源的输入控制总线，指定为 bus。此控制总线包含以下信号：

- `hStart` — 帧的水平线中的第一个像素
- `hEnd` — 帧的水平线中的最后一个像素
- `vStart` — 帧的第一条（顶部）线中的第一个像素
- `vEnd` — 帧的最后一条（底部）线中的最后一个像素
- `valid` — 指示 **rdData** 输入端口上的输入像素数据有效

**数据类型：** `pixelcontrol`

### 输出

### **rdCtrlOut** — 输出控制总线 bus

向数据源输出的控制总线，用于指示该模块已准备好接受视频流数据。此控制总线包含一个 ready 信号。

**数据类型：** `StreamVideoS2MBusObj`

## 参数

### **帧大小** — 帧尺寸 `160x120p` (default) | ...

选择帧尺寸为以下值之一：

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

**帧大小** 值必须与数据源的值相同。

### **颜色空间** — 颜色空间 `YCbCr422` (default) | `RGB` | `YOnly`

选择颜色空间类型为 `YCbCr422`、`RGB` 或 `YOnly`。**颜色空间** 值必须与数据源的值相同。

### **重排输入帧** — 输入帧重排 `off` (default) | `on`

选择此选项可重排输入像素。流式像素格式顺序为在每一行中从左到右，然后向下到下一行，即*行主序*。然而，某些矩阵运算使用*列主序*，即从上到下，然后向右到下一列。根据您的设计对像素的处理方式，您可能需要重排它们以正确显示。

### **将数据保存到工作区** — 将数据保存到工作区 `off` (default) | `on`

选择此参数可将输入视频流数据保存到 MATLAB® 工作区。

### **变量名称** — 工作区变量名称 `simOut` (default) | any MATLAB-supported variable name

指定将输入视频流数据保存到的工作区。此参数可以是任何 MATLAB 支持的变量名称。

#### 依赖关系

要启用此参数，请选择 **将数据保存到工作区** 参数。

### **查看输入** — 在 MATLAB 中显示输入 `off` (default) | `on`

选择此参数可在 MATLAB 查看器中查看输入视频流数据。

## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

接收连续视频流数据

Video Test Sink 模块从基于高级可扩展接口 AXI4 的视频流数据接口模块接收连续视频流数据。您可以将此模块用作测试接收器模块，以仿真基于 AXI4 的视频流数据应用。

该模块接收视频流数据以及一条控制总线，并输出一条控制总线。
