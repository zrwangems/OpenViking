---
type: simulink-block
title: 'Video Capture Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'videocaptureinterface'
documentation_source_path: 'ref/videocaptureinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Capture Interface

## 端口
```yaml
ports:
- name: data
  summary: 图像数据 3*MN* 长度向量
  direction: input
  data_types: uint8
- name: event
  summary: 任务事件信号 标量
  direction: output
  data_types: rteEvent
- name: msg
  summary: SoC 消息数据 标量
  direction: output
  data_types: SoCData
```

### 输入

### **data** — 图像数据 `3`*M**N* 长度向量

指定一个 `3`*M**N* 长度向量作为展开的图像矩阵。

#### 依赖关系

要启用此端口，请将 **Input** 参数设置为 `From input port`。

**数据类型：** `uint8`
### 输出

### **event** — 任务事件信号 标量

此端口在每个新图像事件时发送一条消息。此输出连接到 Task Manager 模块的输入，以在接收到新图像后执行关联的事件驱动任务。

#### 依赖关系

要启用此端口，请选择 **Show event port** 参数。

**数据类型：** `rteEvent`

### **msg** — SoC 消息数据 标量

此端口将包含图像数据的消息输出到连接的 Video Capture 模块。

**数据类型：** `SoCData`
## 参数
```yaml
parameters:
- name: Input
  summary: 仿真视频数据的来源 From dialog（默认）| From input port | From timeseries object
  group: ''
- name: Value
  summary: 要导入的图像 uint8(floor(rand(1,3*160*120)*255))（默认）| 3*MN* 元素向量
  group: ''
- name: Object name
  summary: Timeseries 对象名称 []（默认）| MATLAB 工作区变量
  group: ''
- name: Sample time
  summary: 采样时间（秒） -1（默认）| 正标量
  group: ''
- name: Show event port
  summary: 启用任务事件端口的选项 off（默认）| on
  group: ''
```

### **Input** — 仿真视频数据的来源 `From dialog`（默认）| `From input port` | `From timeseries object`

指定仿真图像数据的来源。

### **Value** — 要导入的图像 `uint8(floor(rand(1,3*160*120)*255))`（默认）| 3*M**N* 元素向量

将仿真图像指定为向量。该向量被转换为三个 *M*×*N* 矩阵，分别表示图像源的色彩通道。

### **Object name** — Timeseries 对象名称 []（默认）| MATLAB 工作区变量

将视频源指定为 MATLAB® 工作区中的 timeseries 对象。

### **Sample time** — 采样时间（秒） `-1`（默认）| 正标量

输入采样时间，定义输出包含视频数据的消息的速率。

### **Show event port** — 启用任务事件端口的选项 `off`（默认）| `on`

选择此参数以启用事件端口，当连接到 Task Manager 模块时，可以执行事件驱动任务。
## 所属库

SoC Blockset / Peripherals

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的更多信息，请参阅 Use SoC Builder to Generate SoC Design。

Embedded Coder 不为该模块生成代码。在生成的代码中，V4L2 驱动框架在设备上执行视频捕获。相关的 Video Capture 模块代表 V4L2 驱动。有关 V4L2 驱动框架的更多信息，请参阅 Video4Linux。

## 版本历史

**在 R2021a 中引入**

## 描述

仿真从硬件上的视频流捕获图像

Video Capture Interface 模块仿真视频输入设备的行为。该模块将捕获的图像以消息形式发送给连接的 Video Capture 模块，可用于算法中。该模块还可以发出事件，当连接到 Task Manager 模块时，可以触发包含 Video Capture 模块的任务。
