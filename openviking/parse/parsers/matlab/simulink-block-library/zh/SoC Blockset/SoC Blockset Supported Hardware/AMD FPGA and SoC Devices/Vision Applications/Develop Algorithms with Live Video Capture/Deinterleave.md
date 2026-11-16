---
type: simulink-block
title: 'Deinterleave'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'deinterleave'
documentation_source_path: 'ref/deinterleave.html'
language: zh-CN
chinese_source: worker-translation
---

# Deinterleave

## 端口

### 输入

### **CbCr** — 交织视频帧矩阵

交织视频帧，指定为矩阵。该矩阵表示 YCbCr 4:2:2 格式图像的色度分量。它包含交织的 Cb 和 Cr 像素值。
### 输出

### **Cb** — 蓝色色度帧矩阵

蓝色色度帧，以矩阵形式返回。该矩阵的大小为输入矩阵的一半。

### **Cr** — 红色色度帧矩阵

红色色度帧，以矩阵形式返回。该矩阵的大小为输入矩阵的一半。

## 参数

R2025b 中未记录。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / PicoZed SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC702 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

将交织的 CbCr 帧转换为独立分量

Deinterleave 模块接受由交织的 Cb 和 Cr 值组成的输入视频帧。输出是独立的 Cb 和 Cr 帧。使用此模块可将来自 HDMI FMC 卡的交织帧转换为独立的 Cb 和 Cr 帧分量，以连接到 Computer Vision Toolbox™ 模块。Cb 和 Cr 输出分量的帧大小是相关联的 Y 分量的一半。

**注意**

此模块不支持 HDL 代码生成，并且不能在 FPGA 用户逻辑内使用此模块。

YCbCr 4:2:2 格式的 FPGA 数据路径由 Y 分量和时间交织的 CbCr 分量组成。面向 FPGA 上用户逻辑的像素流子系统必须具有这两个输入和输出端口。当将像素流转换为帧时，对第三个分量使用虚拟数据（复制 CbCr 分量）。生成的帧具有 3 个全尺寸分量。要连接到 Computer Vision Toolbox 模块，请丢弃重复分量，并将交织帧分离为半尺寸的 Cb 和 Cr 分量帧。请参见 YCbCr 4:2:2 HDL Pixel-Streaming Algorithm 模板中的 Pixels to Frame for YCbCr 4:2:2 模块，以及示例模型。
