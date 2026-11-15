---
type: simulink-block
title: 'SDL Video Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'sdlvideodisplay'
documentation_source_path: 'supportpkg/raspberrypi_ref/sdlvideodisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# SDL Video Display

## 端口

### 输入

### **R** — 输入视频矩阵的红色分量

用于指定输入视频每个像素的红色分量的输入端口。

#### 依赖关系

要启用此端口，请将 **Pixel format** 设置为 `RGB`。

**Data Types:** `uint8`

### **G** — 输入视频矩阵的绿色分量

用于指定输入视频每个像素的绿色分量的输入端口。

#### 依赖关系

要启用此端口，请将 **Pixel format** 设置为 `RGB`。

**Data Types:** `uint8`

### **B** — 输入视频矩阵的蓝色分量

用于指定输入视频每个像素的蓝色分量的输入端口。

#### 依赖关系

要启用此端口，请将 **Pixel format** 设置为 `RGB`。

**Data Types:** `uint8`

### **Y** — 输入视频矩阵的亮度分量

用于指定输入视频每个像素的亮度分量的输入端口。

#### 依赖关系

要启用此端口，请将 **Pixel format** 设置为 `YCbCr 4:2:2`。

**Data Types:** `uint8`

### **Cb** — 输入视频矩阵的蓝色差值分量

用于指定输入视频每个像素的蓝色差值分量的输入端口。

#### 依赖关系

要启用此端口，请将 **Pixel format** 设置为 `YCbCr 4:2:2`。

**Data Types:** `uint8`

### **Cr** — 输入视频矩阵的红色差值分量

用于指定输入视频每个像素的红色差值分量的输入端口。

#### 依赖关系

要启用此端口，请将 **Pixel format** 设置为 `YCbCr 4:2:2`。

**Data Types:** `uint8`

## 参数

### **Window title** — SDL Video Display 窗口的显示名称 SDL Video Display（默认） | string

显示 SDL Video Display 模块的窗口标题。

### **Pixel format** — 输入视频流格式 `RGB`（默认） | `YCbCr 4:2:2`

将输入视频流的格式指定为 `RGB` 或 `YCbCr 4:2:2`。

`RGB` 格式使用三个 8 位值表示每个像素的红色、绿色和蓝色分量。

`YCbCr 4:2:2` 使用三个通道表示每个像素的彩色图像数据：

- Y 是亮度分量（本质上是灰度信号）。
- Cb 是蓝色差值色度分量。
- Cr 是红色差值色度分量。

Cb 和 Cr 以 Y 的一半速率采样。因此，如果 Y 的维度为 M\*N，则 Cb 和 Cr 的维度分别为 (M/2) × N。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

使用 SDL 显示视频

SDL Video Display 模块使用 Simple DirectMedia Layer (SDL) 显示视频数据。此模块接受 `RGB` 或 `YCbCr 4:2:2` 格式的平面视频数据。

**注意**

- 在一个 Simulink® 模型中最多可以使用 `20` 个 SDL Video Display 模块，并将该模型部署到 Raspberry Pi® 板上。
- Simulink Online™ 不支持将 SDL Video Display 模块部署到 Raspberry Pi 4B 硬件板。
