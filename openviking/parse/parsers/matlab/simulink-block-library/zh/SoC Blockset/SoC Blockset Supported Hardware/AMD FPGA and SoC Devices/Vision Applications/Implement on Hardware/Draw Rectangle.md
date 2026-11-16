---
type: simulink-block
title: 'Draw Rectangle'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Implement on Hardware'
documentation_page: 'drawrectangle'
documentation_source_path: 'ref/drawrectangle.html'
language: zh-CN
chinese_source: worker-translation
---

# Draw Rectangle

## 端口

### 输入

### **points** — 矩形坐标和尺寸 N×4 矩阵

将矩形坐标指定为形如 `[x
y
width
height]` 的 *N*×4 矩阵，其中 *N* 是要绘制的矩形数量，*x*
*y* 是每个矩形左上角的坐标，*width*
*height* 是每个矩形的水平和垂直尺寸。

**数据类型:** `uint32`

### **valid** — 启用帧标注 `Boolean`

当此输入为 `true` (`1`) 时，模块会修改内存中找到的所有帧。您的设计应提供 **points** 值，并在视频帧在内存中可用后将 **valid** 设置为 `true`。

**数据类型:** `Boolean`

## 参数

### **Color** — 矩形边界线的颜色 `Green`（默认） | `Red` | `Blue` | `Black` | `White`

矩形边界线的颜色，指定为 `Green`、`Red`、`Blue`、`Black` 或 `White`。

### **Thickness** — 矩形边界线的厚度 3（默认） | scalar

矩形边界线的厚度，指定为 pixels 的数量。

## 所属库

在 YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware 示例中查找此模块

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

将矩形绘制到存储在外部存储器中的视频帧上

Draw Rectangle 模块将矩形叠加到存储在外部存储器中的视频帧上。例如，您可以使用此模块显示识别对象周围的边界框。该模块使用处理器-FPGA 接口和此参考设计的存储器映射来读取和修改帧中的指定像素。

每个模型只能使用此模块一次。您的设计应提供 **points** 值，并在视频帧在内存中可用后将 **valid** 设置为 `true`。YOLO v2 Vehicle Detector with Live Camera Input on Zynq-Based Hardware (Vision HDL Toolbox) 示例展示了如何在面向 ARM® 处理器的后处理模型中使用此模块。
