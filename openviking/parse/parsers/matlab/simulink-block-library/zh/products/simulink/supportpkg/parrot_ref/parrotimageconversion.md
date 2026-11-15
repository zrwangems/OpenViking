---
type: simulink-block
title: 'PARROT Image Conversion'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'parrotimageconversion'
documentation_source_path: 'supportpkg/parrot_ref/parrotimageconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# PARROT Image Conversion

## 端口

### 输入

### **Port\_1** — Y1UY2V 格式的图像 4x9600 数组

输入图像从 Parrot minidrone 的下视摄像头获取，并表示为一个 4-by-9600 数组。
此输入采用 Y1UY2V 格式编码。

**数据类型：** `uint8`

### 输出

### **Y** — 转换为 YUV 格式时图像的亮度 120x160 数组

**数据类型：** `uint8`

### **U** — 转换为 YUV 格式时图像的 U 色度 120x160 数组

**数据类型：** `uint8`

### **V** — 转换为 YUV 格式时图像的 V 色度 120x160 数组

**数据类型：** `uint8`

### **R** — 转换为 RGB 格式时图像中的红色 120x160 数组

**数据类型：** `uint8`

### **G** — 转换为 RGB 格式时图像中的绿色 120x160 数组

**数据类型：** `uint8`

### **B** — 转换为 RGB 格式时图像中的蓝色 120x160 数组

**数据类型：** `uint8`

## 参数

### **Output color space** — 选择用于转换的颜色空间 `YUV`（默认）| `RGB`

选择颜色空间（YUV 或 RGB），以将图像从编码的 Y1UY2V 格式转换。

当将此参数设置为 `YUV` 时，Y、U 和 V 分量可作为单独的输出端口使用。

当将此参数设置为 `RGB` 时，R、G 和 B 分量可作为单独的输出端口使用。

## 所属库

Simulink Support Package for Parrot Minidrones

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

将编码的 Y1UY2V 图像格式转换为 YUV 或 RGB 格式

PARROT Image Conversion 模块将采用 Y1UY2V 格式编码的图像（该图像来自 Parrot® minidrone 的下视摄像头）转换为 YUV 或 RGB 格式。该模块分离颜色分量，并将它们作为输出提供。
