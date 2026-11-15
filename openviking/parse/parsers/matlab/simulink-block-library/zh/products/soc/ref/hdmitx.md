---
type: simulink-block
title: 'HDMI Tx'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'hdmitx'
documentation_source_path: 'ref/hdmitx.html'
language: zh-CN
chinese_source: worker-translation
---

# HDMI Tx

## 端口

### 输入

### **hdmiTxData** — 像素流中的单个 YCbCr 4:2:2 像素，以拼接 YCbCr 值表示

像素流中的单个 YCbCr 4:2:2 像素，指定为拼接 YCbCr 4:2:2 格式的标量，其中

- bits [1:8] 表示 Y。
- bits [9:16] 表示 Cb 或 Cr，在时间上交错。

**数据类型：** `uint16`

### **ctrl** — 伴随输入像素流的控制信号 `pixelcontrol` 总线

伴随输入像素流的控制信号，指定为 `pixelcontrol`（Vision HDL Toolbox）总线。该总线包含五个布尔信号，用于指示像素的有效性及其在帧内的位置。

当 **Input mode** 参数为 `Frame` 时，该模块将 `pixelcontrol` 总线中的全部五个信号设置为 `true`，以指示输出数据何时有效。

**数据类型：** `bus`
### 输出

### **frame** — 输出帧数据向量

输出帧数据，以 YCbCr 4:2:2 格式的向量返回。

#### 依赖关系

要启用此端口，请选择 **Frame output** 参数。

**数据类型：** `uint8`

### **valid** — 伴随输出帧数据的控制信号标量

伴随输出帧数据的控制信号，以标量返回。

此端口是一个控制信号，用于指示 **frame** 输出端口何时有效。当 **frame** 输出端口上有数据可用时，该模块将此值设置为 `1`。

#### 依赖关系

要启用此端口，请选择 **Frame output** 参数。

**数据类型：** `Boolean`

## 参数

### **Frame size** — 视频帧大小 `160x120p`（默认）| ...

选择视频帧大小作为以下值之一：

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

### **Input mode** — 视频输入格式 `Frame`（默认）| `Pixel`

指定输入是每个时钟周期流式传输一个像素，还是每个时钟传输一帧。`Pixel` 模式更好地表示硬件算法，推荐用于 FPGA 部署。`Frame` 模式可实现更快的仿真。

### **Visualize output frame** — 显示输出视频 `on`（默认）| `off`

选择此参数以启用 To Video Display（Computer Vision Toolbox）模块，在仿真期间显示输出帧。

### **Frame output** — 帧输出 `off`（默认）| `on`

选择此参数以启用输出端口 **frame** 和 **valid**。使用这些端口，您可以从此模块访问视频帧数据，并将其导出到任何文件或工作区变量。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2019a 中引入**

## 描述

将 YCbCr 4:2:2 像素流转换为视频帧

HDMI Tx 模块将 YCbCr 4:2:2 格式的像素流转换为原始视频数据，以便在仿真期间显示。它可以以像素流模式返回数据，用于硬件算法设计；或以帧模式返回数据，以实现更快的仿真。当您将此模块包含在设计中时，SoC Builder 工具会生成将视频数据传输到连接到硬件板的 FMC-HDMI-CAM 卡所需的所有 IP 模块。所有模块参数均不影响硬件行为。

您必须拥有 Computer Vision Toolbox™ 才能使用此模块。
