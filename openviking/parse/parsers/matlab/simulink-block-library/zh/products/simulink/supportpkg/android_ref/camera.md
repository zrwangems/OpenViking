---
type: simulink-block
title: 'Camera'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'camera'
documentation_source_path: 'supportpkg/android_ref/camera.html'
language: zh-CN
chinese_source: worker-translation
---

# Camera

## 端口

在 R2025b 中未记录。

## 参数

在 R2025b 中未记录。

## 所属库

Simulink Support Package for Android Devices / Audio & Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

使用前置或后置摄像头捕获视频

从 Android™ 设备上的前置或后置摄像头捕获视频。

Camera 模块有三个输出端口：`R`、`G` 和 `B`。每个端口输出一个由 `uint8` 值组成的二维矩阵。这些矩阵共同构成来自摄像头的彩色图像。**Resolution** 参数决定矩阵维度。

**注意**

在没有硬件的仿真期间，此模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
