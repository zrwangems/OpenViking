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
```yaml
ports:
- name: ctrlIn
  summary: 与像素流关联的控制信号 pixelcontrol 总线
  direction: input
  data_types: bus
- name: activePixels
  summary: 活动视频帧每一行中的像素数 标量
  direction: output
  data_types: double
- name: activeLines
  summary: 活动视频帧中的行数 标量
  direction: output
  data_types: double
- name: totalPixels
  summary: 每一行中的像素数（包括水平消隐间隔） 标量
  direction: output
  data_types: double
- name: totalLines
  summary: 帧中的行数（包括垂直消隐间隔） 标量
  direction: output
  data_types: double
- name: horizBlank
  summary: 帧的行之间的非活动像素数 标量
  direction: output
  data_types: double
- name: vertBlank
  summary: 帧之间的非活动行数 标量
  direction: output
  data_types: double
```

### 输入

### **ctrlIn** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。
这些信号描述像素的有效性及其在帧中的位置。有关更多信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`
### 输出

### **activePixels** — 活动视频帧每一行中的像素数 标量

活动视频帧每一行中的像素数，以标量形式返回。
该值通过计数 `hStart` 和
`hEnd` 之间的有效像素来测量。请参阅图中的标记 `1`。

**数据类型：** `double`

### **activeLines** — 活动视频帧中的行数 标量

活动视频帧中的行数，以标量形式返回。该值通过计数
`vStart` 和 `vEnd` 之间的 `hStart` 脉冲来测量。请参阅图中的标记
`2`。

**数据类型：** `double`

### **totalPixels** — 每一行中的像素数（包括水平消隐间隔） 标量

每一行中的像素数（包括水平消隐间隔），
以标量形式返回。该值通过计数两个 `hStart` 脉冲之间的有效像素数来测量。请参阅图中的标记 `3`。

**数据类型：** `double`

### **totalLines** — 帧中的行数（包括垂直消隐间隔） 标量

帧中的行数（包括垂直消隐间隔），以标量形式返回。该值通过计数两个
`vEnd` 脉冲之间的有效像素数，再除以 `totalPixels` 来测量。请参阅
图中的标记 `4`。

**数据类型：** `double`

### **horizBlank** — 帧的行之间的非活动像素数 标量

帧的行之间的非活动像素数，以标量形式返回。该
值通过计数 `hEnd` 与下一个 `hStart` 之间的无效周期来测量。请参阅图中的标记 `5`。

**数据类型：** `double`

### **vertBlank** — 帧之间的非活动行数 标量

帧之间的非活动行数，以标量形式返回。该值通过
计数 `vEnd` 与下一个 `vStart` 之间的无效周期，减去 `horizBlank`，然后
除以 `totalPixels` 来测量。请参阅图中的标记 `6`。

**数据类型：** `double`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Vision HDL Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2016b 中引入**

## 描述

测量像素控制总线输入的时序

Measure Timing 模块测量视频流的时序参数。
此模块仅用于 Simulink® 仿真，不支持 HDL 代码生成。

Vision HDL Toolbox™ 流式像素协议实现了视频系统的时序，包括帧之间的非活动间隔。这些非活动间隔称为*消隐间隔*。许多 Vision HDL Toolbox 模块要求最小消隐间隔。有关详细信息，请参阅 Configure Blanking Intervals。您可以使用此模块的时序参数测量结果来检查您的视频流是否满足这些要求。如果您操作视频流的控制信号，可以使用此模块验证生成的信号。

为了确定每帧的参数，该模块测量总线上控制信号之间的时间步。

显示控制信号之间六项时间测量的 Logic Analyzer 波形

- `1` — 每行有效像素数
- `2` — 每帧有效行数（计数
  `hStart` 脉冲）
- `3` — 每行总像素数
- `4` — 每帧总行数（周期数除以每行总像素数）
- `5` — 水平消隐
- `6` — 垂直消隐（周期数减去水平消隐，
  再除以每行总像素数）

有关像素控制总线和视频帧尺寸的详细信息，请参阅 Streaming Pixel Interface。

**注意**

来自第一个仿真帧的测量结果是不正确的，因为某些参数需要帧之间的测量。在使用结果之前，请至少仿真两帧。
