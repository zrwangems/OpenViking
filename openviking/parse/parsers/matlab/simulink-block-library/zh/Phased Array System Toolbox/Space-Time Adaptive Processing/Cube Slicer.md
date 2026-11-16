---
type: simulink-block
title: 'Data Cube Slicer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2023b
official_category: 'Space-Time Adaptive Processing'
documentation_page: 'datacubeslicer'
documentation_source_path: 'ref/datacubeslicer.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Cube Slicer

## 端口

### 输入

### **X** — 输入数据立方体 *M*×*Q*×*N* 复值数组

输入数据立方体，指定为 *M*×*Q*×*N* 复值矩阵。

**数据类型：** `double`
**复数支持：** 是

### **Idx** — 切片平面索引 正整数

切片平面索引，指定为正整数。此索引选择用于创建二维输出的切片。

**数据类型：** `double`

### 输出

### **Port\_1** — 输出复值矩阵

折叠后的数据立方体，以复值矩阵形式返回。

- 如果将 **Output Slice** 参数设置为 `Angle-Doppler`，则该切片是恒定距离平面或快时间平面。输出维度为 *Q*×*N*。
- 如果将 **Output Slice** 参数设置为 `Range-Doppler`，则该切片是恒定角度平面。输出维度为 *M*×*N*。
- 如果将 **Output Slice** 参数设置为 `Range-angle`，则该切片是恒定多普勒平面。输出维度为 *M*×*Q*。

**数据类型：** `double`
**复数支持：** 是

## 参数

### **Output Slice** — 输出切片 `Angle-Doppler`（默认） | `Range-Doppler` | `Range-angle`

输出切片，指定为 `Angle-Doppler`、`Range-Doppler` 或 `Range-angle`。输出切片为：

| 切片平面 | 切片维度 |
| --- | --- |
| `Angle-Doppler` | *Q*×*N* |
| `Range-Doppler` | *M*×*N* |
| `Range-angle` | *M*×*Q* |

## 所属库

Phased Array System Toolbox / Space-Time Adaptive Processing

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

沿指定维度切片数据立方体

Data Cube Slicer 模块通过指定平面切片数据立方体。输入是维度为 *M*×*Q*×*N* 的数据立方体。第一个维度是距离，或快时间。第二个维度是角度，或通道。第三个维度是多普勒，或慢时间。
