---
type: simulink-block
title: 'SDL Video Display'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'sdlvideodisplay'
documentation_source_path: 'nvidia/ref/sdlvideodisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# SDL Video Display

## 端口

### 输入

### **R** — 输入视频流矩阵的红色分量

输入端口，用于指定每个像素的红色分量。

#### 依赖关系

仅当您从**像素格式**中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **G** — 输入视频流矩阵的绿色分量

输入端口，用于指定每个像素的绿色分量。

#### 依赖关系

仅当您从**像素格式**中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **B** — 输入视频流矩阵的蓝色分量

输入端口，用于指定每个像素的蓝色分量。

#### 依赖关系

仅当您从**像素格式**中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **Y** — 输入视频流矩阵的亮度分量

输入端口，用于指定每个像素的亮度分量。

#### 依赖关系

仅当您从**像素格式**中选择 `YCbCr
4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

### **Cb** — 输入视频流矩阵的蓝色差分量

输入端口，用于指定每个像素的蓝色差分量。

#### 依赖关系

仅当您从**像素格式**中选择 `YCbCr
4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

### **Cr** — 输入视频流矩阵的红色差分量

输入端口，用于指定每个像素的红色差分量。

#### 依赖关系

仅当您从**像素格式**中选择 `YCbCr
4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

## 参数

### **像素格式** — 输入视频流格式 `RGB`（默认）| `YCbCr 4:2:2`

指定输入视频流的格式：`YCbCr 4:2:2`
或 `RGB`。

`YCbCr 4:2:2` 使用三个通道表示每个像素的彩色图像数据：

- Y 是亮度分量（本质上是灰度信号）。
- Cb 是蓝色差色度分量。
- Cr 是红色差色度分量。

Cb 和 Cr 的采样率为 Y 的一半。因此，如果 Y 的维度为 M\*N，则 Cb 和 Cr 的维度各为 (M/2) × N。

`RGB` 使用三个 8 位值表示每个像素的红色、绿色和蓝色分量。

#### 编程用法

|  |
| --- |
| **模块参数：** `pixelFormat` |
| **类型：** 字符向量 |
| **值：** `'RGB'`|`'YCbCr 4:2:2'` |
| **默认值：**  `'RGB'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

在连接到 NVIDIA 目标的显示器上显示视频

使用 Simple DirectMedia Layer (SDL) 多媒体库显示视频数据。一个
Simulink® 模型只能包含一个 SDL Video Display 模块。

此模块接收 `YCbCr 4:2:2` 或
`RGB` 格式的平面视频数据。

在目标上安装 Simple DirectMedia Layer (SDL) 库。有关详细信息，
请参阅 NVIDIA 板卡代码生成的前提条件。
