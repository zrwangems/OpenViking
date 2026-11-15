---
type: simulink-block
title: 'Pixel Processing'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'pixelprocessing'
documentation_source_path: 'slref/pixelprocessing.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixel Processing

## 端口

在 R2025b 中未记录。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

Pixel Processing Subsystem 的控制模块

Pixel Processing 模块用作 Pixel Processing Subsystem 模块的控制模块。Pixel Processing Subsystem 模块遍历三维输入矩阵。在每个迭代步骤中，该子系统处理输入矩阵的一个 1-by-1-by-*`n`* 子集，其中 *`n`* 是输入矩阵第三维的大小。该子系统输出一个二维矩阵，其前两维与输入矩阵相同。
