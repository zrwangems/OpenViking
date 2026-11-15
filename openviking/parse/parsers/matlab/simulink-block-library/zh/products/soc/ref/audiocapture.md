---
type: simulink-block
title: 'Audio Capture'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Audio'
documentation_page: 'audiocapture'
documentation_source_path: 'ref/audiocapture.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Capture

## 端口

### 输入

### **msg** — 来自音频捕获接口的数据消息 标量

此消息端口接收来自已连接的 Audio Capture Interface 模块的数据消息。当 Task Manager 模块触发包含 Audio Capture 模块的任务时，这些消息会进行处理。有关消息的详细信息，请参阅消息。

**数据类型：** `SoCData`

### 输出

### **data** — 来自捕获音频的数据帧 *M*-元素向量 | *M*×*C* 矩阵

当模块接收单个音频通道时，data 是从模拟硬件音频源接收的 *M* 元素音频数据帧。**每帧采样数** 参数定义音频数据的样本数 *M*。当模块接收多个音频通道时，音频数据是 *M*×*C* 矩阵，其中 *C* 由 **通道数** 参数指定。

**数据类型：** `int8` | `int16` | `int32`

## 参数

### **数据类型** — 音频设备的数据类型 `int16`（默认） | `int8` | `int32`

指定音频捕获设备的数据类型。

### **通道数** — 数据通道数 `2`（默认） | 正整数

指定从音频设备接收的音频通道数 *C*。此数字应与 Audio Capture Interface 模块中的 **通道数** 参数匹配。

### **每帧采样数** — 从音频设备读取的数据向量大小 `4410`（默认） | 正整数标量

指定接收的音频数据的每帧样本数 *M*。

### **采样时间** — 以 seconds 为单位的采样时间 `-1`（默认） | 正标量

如果在定时器驱动的任务中使用，请输入 Task Manager 模块中定义的任务的采样时间。如果在事件驱动的任务中使用，请输入 `-1`。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 — 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。有关为 SoC 设计生成代码的详细信息，请参阅使用 SoC Builder 生成 SoC 设计。
- 要为您的 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® 和 SoC Blockset™ Support Package for Embedded Linux® Devices。
- 要使用此模块，必须将 **硬件板卡** 设置为 `Embedded Linux Board`。然后您可以按照说明配置板卡。有关详细信息，请参阅创建 Embedded Linux 设备配置。

当部署到支持的硬件板卡时，此模块使用 V4L2 驱动程序框架从视频捕获设备（如摄像头）捕获图像。要指定视频捕获设备和事件触发器，请使用 Hardware Mapping 工具。有关 V4L2 驱动程序框架的详细信息，请参阅 Video4Linux。

## 版本历史

**在 R2021a 中引入**

## 描述

从输入音频设备捕获音频样本并发送到算法

Audio Capture 模块模拟在硬件板卡上捕获音频流样本的驱动程序代码的行为。此模块的输入必须连接到 Audio Capture Interface 模块，后者模拟硬件板卡上的物理音频设备。将此模块放在任务内，并连接到算法，以便在任务每次执行时处理一帧音频样本。有关任务的详细信息，请参阅定时器驱动任务和事件驱动任务。
