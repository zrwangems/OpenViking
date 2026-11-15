---
type: simulink-block
title: 'Video Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'videodisplay'
documentation_source_path: 'supportpkg/android_ref/videodisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Display

## 端口

### 输入

### **R** — 图像的红色分量数值矩阵

图像的红色分量，指定为数值矩阵。此矩阵的大小必须与输入 **G** 和 **B** 相同。

**数据类型：** `uint8`

### **G** — 图像的绿色分量数值矩阵

图像的绿色分量，指定为数值矩阵。此矩阵的大小必须与输入 **R** 和 **B** 相同。

**数据类型：** `uint8`

### **B** — 图像的蓝色分量数值矩阵

图像的蓝色分量，指定为数值矩阵。此矩阵的大小必须与输入 **R** 和 **G** 相同。

**数据类型：** `uint8`

## 参数

R2025b 中未记录。

## 所属库

Simulink Support Package for Android Devices / Audio & Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

在设备屏幕上显示视频

使用 Video Display 模块，通过输入图像的红色、蓝色和绿色分量值，在设备屏幕上显示视频。所有三个输入端口 **R**、**G** 和 **B** 的维度必须相等。
