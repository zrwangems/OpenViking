---
type: simulink-block
title: 'Interleave'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'interleave'
documentation_source_path: 'ref/interleave.html'
language: zh-CN
chinese_source: worker-translation
---

# Interleave

## 端口

### 输入

### **Cb** — 蓝色色度帧矩阵

蓝色色度帧，指定为矩阵。该矩阵表示 YCbCr 4:2:2 格式图像的蓝色色度分量。该矩阵包含对应 Y 帧的一半值。

### **Cr** — 红色色度帧矩阵

红色色度帧，指定为矩阵。该矩阵表示 YCbCr 4:2:2 格式图像的红色色度分量。该矩阵包含对应 Y 帧的一半值。
### 输出

### **CbCr** — 交织视频帧矩阵

交织视频帧，以矩阵形式返回。其大小为输入矩阵的两倍，并包含交织的 Cb 和 Cr 像素值。

## 参数

在 R2025b 中未记录。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / PicoZed SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC702 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

将分离的 Cb 和 Cr 分量转换为交织的 CbCr 帧

Interleave 模块接受分离的 Cb 和 Cr 帧分量。输出是由交织的 Cb 和 Cr 数据组成的帧。当在带有 HDMI FMC 卡的 FPGA 上以 YCbCr 4:2:2 格式为目标时，使用此模块为从帧到像素流的转换做准备。

**注意**

此模块不支持 HDL 代码生成，并且不能在 FPGA 用户逻辑内使用此模块。

YCbCr 4:2:2 格式的 FPGA 数据路径由 Y 分量和时间交织的 CbCr 分量组成。面向 FPGA 上用户逻辑的像素流子系统必须具有这两个输入和输出端口。从板卡捕获的 YCbCr 视频数据作为三个分量帧进入 Simulink®。Cb 和 Cr 帧的水平尺寸是 Y 分量尺寸的一半。对于像素流设计，在转换为像素流之前，通过组合 Cb 和 Cr 帧来重新创建交织的 CbCr 分量。当将帧转换为像素流时，对第三个分量使用虚拟数据（复制交织的 CbCr 帧）。请参阅 YCbCr 4:2:2 HDL Pixel-Streaming Algorithm 模板中的 Frame to Pixels for YCbCr 4:2:2 模块以及示例模型。
