---
type: simulink-block
title: 'HDMI Rx'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'hdmirx'
documentation_source_path: 'ref/hdmirx.html'
language: zh-CN
chinese_source: worker-translation
---

# HDMI Rx

## 端口

### 输出

### **hdmiRxData** — 像素流中的单个 YCbCr 4:2:2 像素，拼接的 YCbCr 值

像素流中的单个 YCbCr 4:2:2 像素，指定为拼接 YCbCr 4:2:2 格式的标量，其中

- bits [1:8] 表示 Y。
- bits [9:16] 表示 Cb 或 Cr，在时间上
  交错。

**数据类型：** `uint16`

### **ctrl** — 伴随输出像素流的控制信号 `pixelcontrol` 总线

伴随输出像素流的控制信号，以 `pixelcontrol` (Vision HDL Toolbox) 总线形式返回。该总线包含五个 Boolean 信号，用于指示像素的有效性及其在帧内的位置。

当 **输出模式** 参数为 `Frame` 时，模块将 `pixelcontrol` 总线中的所有五个信号设置为 `true`，以指示输出数据何时有效。

**数据类型：** `bus`

## 参数

#### 主要

### **帧大小** — 视频帧大小 `160x120p`（默认） | `Pixel` | ...

从以下值中选择视频帧大小：

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

### **输出模式** — 模块的输出模式 `Frame`（默认） | `Pixel`

指定输出是按每个时钟周期一个像素进行流式传输，还是每个时钟一帧。`Pixel` 模式更好地表示硬件算法，推荐用于 FPGA 部署。`Frame` 模式可实现更快的仿真。

#### 仿真

### **输入文件名** — 输入视频文件字符向量

指定输入视频文件的完整路径。有关支持的文件类型的信息，请参阅 From Multimedia File (Computer Vision Toolbox)。

**示例：** `'handshake_left.avi'`

### **帧采样时间** — 模块采样时间 `1/60`（默认） | 正标量

模块采样时间，以 seconds 为单位，指定为正标量。默认值对应于 60 fps 的帧速率。

### **可视化输入帧** — 显示输入视频 `on`（默认） | `off`

选择此选项会启用 To Video Display (Computer Vision Toolbox) 模块以在仿真期间显示输入帧。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2019a 中引入**

## 描述

将视频流转换为 YCbCr 4:2:2 像素流

HDMI Rx 模块将原始视频数据转换为 YCbCr 4:2:2 像素流格式。它可以以像素流模式返回数据以用于硬件算法设计，或以帧模式返回数据以实现更快的仿真。当您在设计中包含此模块时，SoC Builder 工具会生成从连接到硬件板的 FMC-HDMI-CAM 卡接收视频数据所需的所有 IP 模块。模块参数均不影响硬件行为。仿真时，请指定要流式传输的视频文件。

使用此模块必须具有 Computer Vision Toolbox™。
