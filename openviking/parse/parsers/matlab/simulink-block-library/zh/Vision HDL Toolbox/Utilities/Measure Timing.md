---
type: simulink-block
title: 'Measure Timing'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'measuretiming'
documentation_source_path: 'ref/measuretiming.html'
language: zh-CN
chinese_source: worker-translation
---

# Measure Timing

## 端口

### 输入

### **ctrlIn** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

**数据类型：** `bus`

### 输出

### **activePixels** — 有效视频帧每行中的像素数（标量）

有效视频帧每行中的像素数，以标量形式返回。该值通过计数 `hStart` 和 `hEnd` 之间的有效像素来测量。请参见图中的标记 `1`。

**数据类型：** `double`

### **activeLines** — 有效视频帧中的行数（标量）

有效视频帧中的行数，以标量形式返回。该值通过计数 `vStart` 和 `vEnd` 之间的 `hStart` 脉冲来测量。请参见图中的标记 `2`。

**数据类型：** `double`

### **totalPixels** — 每行中的像素数，包括水平消隐间隔（标量）

每行中的像素数，包括水平消隐间隔，以标量形式返回。该值通过计数两个 `hStart` 脉冲之间的有效像素数来测量。请参见图中的标记 `3`。

**数据类型：** `double`

### **totalLines** — 帧中的行数，包括垂直消隐间隔（标量）

帧中的行数，包括垂直消隐间隔，以标量形式返回。该值通过计数两个 `vEnd` 脉冲之间的有效像素数，再除以 `totalPixels` 来测量。请参见图中的标记 `4`。

**数据类型：** `double`

### **horizBlank** — 帧的行之间非活动像素数（标量）

帧的行之间非活动像素数，以标量形式返回。该值通过计数 `hEnd` 与下一个 `hStart` 之间的无效周期来测量。请参见图中的标记 `5`。

**数据类型：** `double`

### **vertBlank** — 帧之间非活动行数（标量）

帧之间非活动行数，以标量形式返回。该值通过计数 `vEnd` 与下一个 `vStart` 之间的无效周期，减去 `horizBlank`，然后除以 `totalPixels` 来测量。请参见图中的标记 `6`。

**数据类型：** `double`

## 参数

未在 R2025b 中记录。

## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 C/C++ 代码生成，适用于 Simulink 加速模式和快速加速模式以及 DPI 组件生成。

### HDL 代码生成：使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于在生成 HDL 代码的子系统中提供仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2016b 中引入**

## 描述

测量像素控制总线输入的时序

Measure Timing 模块测量视频流的时序参数。此模块仅用于 Simulink® 仿真，不支持 HDL 代码生成。

Vision HDL Toolbox™ 流式像素协议实现了视频系统的时序，包括帧之间的非活动间隔。这些非活动间隔称为*消隐间隔*。许多 Vision HDL Toolbox 模块要求最小消隐间隔。有关详细信息，请参阅配置消隐间隔。可以使用此模块的时序参数测量值来检查视频流是否满足这些要求。如果修改了视频流的控制信号，可以使用此模块验证生成的信号。

为了确定每帧的参数，该模块测量总线上控制信号之间的时间步长。

Logic Analyzer 波形，显示控制信号之间的六项时间测量

- `1` — 每行有效像素数
- `2` — 每帧有效行数（对 `hStart` 脉冲进行计数）
- `3` — 每行总像素数
- `4` — 每帧总行数（周期数除以每行总像素数）
- `5` — 水平消隐
- `6` — 垂直消隐（周期数减去水平消隐，再除以每行总像素数）

有关像素控制总线和视频帧尺寸的详细信息，请参阅流式像素接口。

**注意**

由于某些参数需要测量帧之间的值，第一个仿真帧的测量结果不正确。使用结果之前，请至少仿真两帧。
