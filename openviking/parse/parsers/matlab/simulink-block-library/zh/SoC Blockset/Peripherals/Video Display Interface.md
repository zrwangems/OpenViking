---
type: simulink-block
title: 'Video Display Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'videodisplayinterface'
documentation_source_path: 'ref/videodisplayinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Display Interface

## 端口
```yaml
ports:
- name: msg
  summary: SoC 消息数据向量
  direction: input
  data_types: SoCData
- name: data
  summary: 图像数据 3\height*\width* 元素向量
  direction: output
  data_types: uint8
```

### 输入

### **msg** — SoC 消息数据向量

此端口从所连接的 Video Display 模块的 **msg** 端口接收图像数据作为消息。

**数据类型：** `SoCData`
### 输出

### **data** — 图像数据 3\**height*\**width* 元素向量

该端口将解包的图像矩阵数据输出为三个 *height**width* 元素向量，其中 *height* 和 *width* 是由 `Image Size` 参数定义的图像矩阵的维度。`3` 是 RGB 通道的乘数。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `To output port`。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Output
  summary: 输出类型 To terminator（默认）| To output port
  group: ''
- name: Image size
  summary: 图像大小 160x120（默认）| 320x240 | 640x480 | 800x600 | custom
  group: ''
- name: Image size ([width, height])
  summary: 图像大小 [320, 240]（默认）| 正整数的二元素向量
  group: ''
- name: Pixel format
  summary: 像素数据格式 RGB（默认）| YCbCr 4:2:2
  group: ''
- name: Sample time
  summary: 采样时间（以秒为单位）-1（默认）| 正标量
  group: ''
```

### **Output** — 输出类型 `To terminator`（默认）| `To output port`

指定该模块是充当终止器（类似于 Terminator 模块），还是向输出端口产生数据。

### **Image size** — 图像大小 `160x120`（默认）| `320x240` | `640x480` | `800x600` | `custom`

指定由该模块的 `data` 端口以向量形式发出的图像的高度和宽度维度。指定 `custom` 以设置自定义图像维度。

### **Image size ([width, height])** — 图像大小 `[320, 240]`（默认）| 正整数的二元素向量

指定由该模块的 data 端口发出的图像矩阵的自定义高度和宽度维度。

#### 依赖关系

要启用此参数，请将 **Image size** 参数设置为 `custom`。

### **Pixel format** — 像素数据格式 `RGB`（默认）| `YCbCr 4:2:2`

指定图像数据输出编码为 `RGB` 或 `YCbCr 4:2:2` 三元组。

#### 依赖关系

要启用此参数，请将 **Image size** 参数设置为 `custom`。

### **Sample time** — 采样时间（以秒为单位）`-1`（默认）| 正标量

输入采样时间，定义接收包含视频数据的消息的速率。
## 所属库

SoC Blockset / Peripherals

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的更多信息，请参阅 Use SoC Builder to Generate SoC Design。

Embedded Coder 不为该模块生成代码。在生成的代码中，V4L2 驱动程序框架在设备上执行视频显示。相关的 Video Display 模块表示 V4L2 驱动程序。有关 V4L2 驱动程序框架的更多信息，请参阅 Video4Linux。

## 版本历史

**在 R2021a 中引入**

## 描述

模拟在设备上向视频屏幕显示图像

Video Display Interface 模块模拟视频输出设备的行为。此模块从所连接的 Video Display 模块接收图像样本作为消息，该模块模拟连接到您算法的视频驱动程序代码。
