---
type: simulink-block
title: 'Camera'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'nvidiacamera'
documentation_source_path: 'nvidia/ref/nvidiacamera.html'
language: zh-CN
chinese_source: worker-translation
---

# Camera

## 端口

### 输出

### **R** — 输出视频流矩阵的红色分量

此端口输出每个像素的红色分量。

**数据类型：** `uint8`

### **G** — 输出视频流矩阵的绿色分量

此端口输出每个像素的绿色分量。

**数据类型：** `uint8`

### **B** — 输出视频流矩阵的蓝色分量

此端口输出每个像素的蓝色分量。

**数据类型：** `uint8`

## 参数

### **Name** — 已连接视频设备的名称 `My Camera`（默认）

输入视频设备的路径和名称。

当您将支持的 USB 或 CSI 视频摄像头连接到目标硬件时，Linux® 内核会创建一个视频设备文件。要查看视频设备文件列表，请与目标硬件打开命令行会话，并输入：`ls -al
/dev/video*`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CameraName` |
| **类型：** character vector |
| **值：** `valid name`| |
| **默认值：**  `'My Camera'` |

### **Image size** — 显示分辨率 `[320, 240]`（默认） | `[width, height]`

指定要捕获图像的显示分辨率，以 pixels 为单位。

#### 编程用法

|  |
| --- |
| **模块参数：** `ImageSize` |
| **类型：** character vector |
| **值：** `[width, height]`| |
| **默认值：**  `'[320, 240]'` |

### **Sample time** — 捕获新图像的频率 `0.1`（默认） | scalar | `vector`

选择视频设备的采样时间。

较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'0.1'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从连接到 NVIDIA 目标的 USB 或 CSI 摄像头捕获视频

从 USB 或 CSI 摄像头捕获实时视频。输出采用行主序格式。在仿真期间，模型输出移动的 colorbar 图像。

在目标上安装 GStreamer 库、V4L2 库和 V4L2 实用程序。还必须安装这些库的开发包。有关详细信息，请参阅 Prerequisites for Generating Code for NVIDIA Boards
