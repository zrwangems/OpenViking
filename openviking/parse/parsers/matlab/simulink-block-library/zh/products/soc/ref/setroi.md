---
type: simulink-block
title: 'Set ROI'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Implement on Hardware'
documentation_page: 'setroi'
documentation_source_path: 'ref/setroi.html'
language: zh-CN
chinese_source: worker-translation
---

# Set ROI

## 端口

### 输入

### **StartPos** — ROI 左上角的坐标 N×2 矩阵

将 ROI 的坐标指定为形式为 `[x
y]` 的 *N*×2 矩阵，其中 *N* 是 ROI 的数量，*x* 和 *y* 是每个矩形左上角的坐标。

**数据类型：** `single` | `double` | `uint32`

### **ROI** — 感兴趣区域矩阵的替换像素值

将替换像素值指定为 *N*×*width*×*height* 的矩阵。所有 ROI 必须具有相同大小。

**数据类型：** `single` | `double` | `uint32`

### **valid** — 启用帧标注 `Boolean`

当此输入为 `true` (`1`) 时，该模块修改内存中找到的所有帧。你的设计应提供 **StartPos** 和 **ROI** 值，并且一旦视频帧在内存中可用，就将 **valid** 设置为 `true`。

**数据类型：** `Boolean`

## 参数

### **Use row-major format** — 以行优先顺序读取和修改帧缓冲区 on（默认）| off

此模块假定帧在内存中按行优先顺序存储。如果你的设计按列优先顺序存储帧，请清除此复选框。

## 所属库

在 YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware 示例中找到此模块

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

在存储于外部存储器中的视频帧的指定区域上绘制

Set ROI 模块覆盖存储于外部存储器中的视频帧的一个或多个矩形区域。例如，你可以使用此模块在识别出的对象上显示分数标签。该模块使用处理器-FPGA 接口和此参考设计的存储器映射来读取和修改帧中的指定像素。

每个模型只能使用此模块一次。你的设计应提供 ROI 坐标和替换值，并且一旦视频帧在内存中可用，就将 **valid** 设置为 `true`。YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware (Vision HDL Toolbox) 示例展示了如何在面向 ARM® 处理器的后处理模型中使用此模块。
