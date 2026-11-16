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

R2025b 中未提供文档。

## 参数

**分辨率**
:   选择设备上摄像头的位置以及图像的大小。

    - `Front` 使用与显示屏位于同一侧的摄像头。
    - `Back` 使用与显示屏位于相对一侧的摄像头。

    要获取特定于设备的分辨率列表，请连接已配置的设备，然后点击**刷新**按钮。要配置设备，请按照硬件设置过程中提供的说明进行操作。

    图像大小会显著影响摄像头生成数据的速率。例如，以 `1920x1080` 捕获视频时产生的数据量几乎是以 `720x486` 捕获视频时的六倍。

**采样时间**
:   指定模块读取传感器的频率。

    较小的值要求处理器在更短的时间内完成相同数量的指令，这可能会导致任务溢出。

## 所属库

Simulink Support Package for Android Devices / Audio & Video

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2014a 中引入**

## 描述

使用前置或后置摄像头捕获视频

从 Android™ 设备上的前置或后置摄像头捕获视频。

Camera 模块有三个输出端口：`R`、`G` 和 `B`。每个端口输出一个由 `uint8` 值组成的二维矩阵。这些矩阵共同构成摄像头捕获的彩色图像。**分辨率**参数决定矩阵的大小。

**注意**

在没有硬件的情况下进行仿真时，此模块输出零值。请参阅“模块在仿真中产生零值或不执行任何操作”。
