---
type: simulink-block
title: 'SDL Video Display'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'sdlvideodisplay'
documentation_source_path: 'beaglebone/ref/sdlvideodisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# SDL Video Display

## 端口

### 输入

### **R** — 输入视频矩阵的红色分量

输入端口，用于指定输入视频中每个像素的红色分量。

#### 依赖项

- 要启用此端口，请将 **像素格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **G** — 输入视频矩阵的绿色分量

输入端口，用于指定输入视频中每个像素的绿色分量。

#### 依赖项

- 要启用此端口，请将 **像素格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **B** — 输入视频矩阵的蓝色分量

输入端口，用于指定输入视频中每个像素的蓝色分量。

#### 依赖项

- 要启用此端口，请将 **像素格式** 设置为 `RGB`。

**数据类型：** `uint8`

### **Y** — 输入视频矩阵的亮度分量

输入端口，用于指定输入视频中每个像素的亮度分量。

#### 依赖项

- 要启用此端口，请将 **像素格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cb** — 输入视频矩阵的蓝色差分量

输入端口，用于指定输入视频中每个像素的蓝色差分量。

#### 依赖项

- 要启用此端口，请将 **像素格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

### **Cr** — 输入视频矩阵的红色差分量

输入端口，用于指定输入视频中每个像素的红色差分量。

#### 依赖项

- 要启用此端口，请将 **像素格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `uint8`

## 参数

### **像素格式** — 输入视频流格式 `RGB`（默认） | `YCbCr 4:2:2`

将输入视频流的格式指定为 `RGB` 或 `YCbCr 4:2:2`。

`RGB` 格式使用三个 8-bit 值来表示每个像素的红色、绿色和蓝色分量。

`YCbCr 4:2:2` 使用三个通道来表示每个像素的彩色图像数据：

- Y 是亮度分量（本质上为灰度信号）。
- Cb 是蓝色差色度分量。
- Cr 是红色差色度分量。

Cb 和 Cr 的采样率为 Y 的一半。因此，如果 Y 的维度为 M\*N，则 Cb 和 Cr 的维度分别为 (M/2) × N。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

使用 SDL 显示视频

SDL Video Display 模块使用 Simple DirectMedia Layer (SDL) 显示视频数据。此模块接受 `RGB` 或 `YCbCr 4:2:2` 格式的平面视频数据。
