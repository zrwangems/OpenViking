---
type: simulink-block
title: 'Video Test Sink'
family: 'soc'
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
```yaml
ports:
- name: rdData
  summary: 输入视频流数据向量
  direction: input
  data_types: uint8
- name: rdCtrlIn
  summary: 输入控制总线 总线
  direction: input
  data_types: pixelcontrol
- name: rdCtrlOut
  summary: 输出控制总线 总线
  direction: output
  data_types: StreamVideoS2MBusObj
```

### 输入

### **rdData** — 输入视频流数据向量

来自数据源的输入视频流数据。此值必须为向量。

**数据类型：** `uint8`

### **rdCtrlIn** — 输入控制总线 总线

来自数据源的输入控制总线，指定为总线。此控制总线包含以下信号：

- `hStart` — 帧的某一行水平线中的第一个像素
- `hEnd` — 帧的某一行水平线中的最后一个像素
- `vStart` — 帧的第一（顶部）行中的第一个像素
- `vEnd` — 帧的最后（底部）行中的最后一个像素
- `valid` — 指示 **rdData** 输入端口上的输入像素数据有效

**数据类型：** `pixelcontrol`
### 输出

### **rdCtrlOut** — 输出控制总线 总线

输出到数据源的控制总线，用于指示该模块已准备好接收视频流数据。此控制总线包含一个 ready 信号。

**数据类型：** `StreamVideoS2MBusObj`
## 参数
```yaml
parameters:
- name: Frame size
  summary: 帧尺寸 160x120p（默认）| ...
  group: ''
- name: Color space
  summary: 颜色空间 YCbCr422（默认）| RGB | YOnly
  group: ''
- name: Reorder input frame
  summary: 输入帧重排序 off（默认）| on
  group: ''
- name: Save data in workspace
  summary: 将数据保存到工作区 off（默认）| on
  group: ''
- name: Variable name
  summary: 工作区变量名称 simOut（默认）| 任何 MATLAB 支持的变量名称
  group: ''
- name: View input
  summary: 在 MATLAB 中显示输入 off（默认）| on
  group: ''
```

### **Frame size** — 帧尺寸 `160x120p`（默认）| ...

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

**Frame size** 值必须与数据源的值相同。

### **Color space** — 颜色空间 `YCbCr422`（默认）| `RGB` | `YOnly`

选择颜色空间的类型为 `YCbCr422`、`RGB` 或 `YOnly`。**Color space** 值必须与数据源的值相同。

### **Reorder input frame** — 输入帧重排序 `off`（默认）| `on`

选择此选项可对输入像素进行重排序。流式像素格式的顺序为从左到右遍历每一行，然后向下到下一行，即*行主序*。然而，某些矩阵运算使用*列主序*，即从上到下，然后向右到下一列。根据您的设计对像素的处理方式，您可能需要重新排序像素以正确显示。

### **Save data in workspace** — 将数据保存到工作区 `off`（默认）| `on`

选择此参数可将输入视频流数据保存到 MATLAB® 工作区。

### **Variable name** — 工作区变量名称 `simOut`（默认）| 任何 MATLAB 支持的变量名称

指定保存输入视频流数据的工作区。此参数可以是任何 MATLAB 支持的变量名称。

#### 依赖关系

要启用此参数，请选择 **Save data in workspace** 参数。

### **View input** — 在 MATLAB 中显示输入 `off`（默认）| `on`

选择此参数可在 MATLAB 查看器中查看输入视频流数据。
## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

R2025b 中未记录。

## 扩展功能

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

接收连续视频流数据

Video Test Sink 模块从基于高级可扩展接口 AXI4 的视频流数据接口模块接收连续视频流数据。您可以将此模块用作测试接收模块，用于仿真基于 AXI4 的视频流数据应用。

该模块接收视频流数据以及控制总线，并输出控制总线。
