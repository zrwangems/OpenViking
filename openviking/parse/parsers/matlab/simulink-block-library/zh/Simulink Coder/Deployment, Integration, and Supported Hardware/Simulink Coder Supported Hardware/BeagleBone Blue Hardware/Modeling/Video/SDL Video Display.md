---
type: simulink-block
title: 'SDL Video Display'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Video'
documentation_page: 'sdlvideodisplay'
documentation_source_path: 'beagleboneblue/ref/sdlvideodisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# SDL Video Display

## 端口

### 输入

### **R** — 像素矩阵的红色分量

用于指定每个像素红色分量的输入端口。

#### 依赖项

仅当从 **Pixel format** 中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **G** — 像素矩阵的绿色分量

用于指定每个像素绿色分量的输入端口。

#### 依赖项

仅当从 **Pixel format** 中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **B** — 像素矩阵的蓝色分量

用于指定每个像素蓝色分量的输入端口。

#### 依赖项

仅当从 **Pixel format** 中选择 `RGB` 时，此端口才会出现。

**数据类型：** `uint8`

### **Y** — 像素矩阵的亮度分量

用于指定每个像素亮度分量的输入端口。

#### 依赖项

仅当从 **Pixel format** 中选择 `YCbCr 4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

### **Cb** — 像素矩阵的蓝色差分量

用于指定每个像素蓝色差分量的输入端口。

#### 依赖项

仅当从 **Pixel format** 中选择 `YCbCr 4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

### **Cr** — 像素矩阵的红色差分量

用于指定每个像素红色差分量的输入端口。

#### 依赖项

仅当从 **Pixel format** 中选择 `YCbCr 4:2:2` 时，此端口才会出现。

**数据类型：** `uint8`

## 参数

### **Pixel format** — 输入视频流的格式 RGB（默认） | YCbCr 4:2:2

指定输入视频流的格式：`YCbCr 4:2:2` 或 `RGB`。

`YCbCr 4:2:2` 使用三个通道为每个像素表示彩色图像数据：

- Y 是亮度分量（本质上是一种灰度信号）。
- Cb 是蓝色差色度分量。
- Cr 是红色差色度分量。

Cb 和 Cr 以 Y 的一半速率采样。因此，如果 Y 的维度为 M\*N，则 Cb 和 Cr 的维度各自为 (M/2) × N。

`RGB` 使用三个 8 位值表示每个像素的红色、绿色和蓝色分量。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Video

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

使用 SDL 显示视频

使用 Simple Directmedia Layer (SDL) 多媒体库显示视频数据。一个 Simulink® 模型只能包含一个 SDL Video Display 模块。

此模块接收 YCbCr 4:2:2 或 RGB 格式的平面视频数据。
