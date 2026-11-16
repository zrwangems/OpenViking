---
type: simulink-block
title: 'ROS Write Point Cloud, ROS 2 Write Point Cloud'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'writepointcloudblock'
documentation_source_path: 'ref/writepointcloudblock.html'
language: zh-CN
chinese_source: worker-translation
---

# ROS Write Point Cloud, ROS 2 Write Point Cloud

## 端口

### 输入

### **XYZ** — XYZ 坐标矩阵 | 数组

点云数据中每个点的 *x-*、*y-* 和 *z-* 坐标，指定为 *N*×3 矩阵或 *h*×*w*×3 数组。*N* 是点云中的点数。*h* 和 *w* 是图像的高度和宽度，以像素为单位。

**数据类型：** `single`

### **RGB** — 每个点的 RGB 值矩阵 | 数组

点云数据中每个点的 RGB 值，指定为 *N*×3 矩阵或 *h*×*w*×3 数组。*N* 是点云中的点数。*h* 和 *w* 是图像的高度和宽度，以像素为单位。RGB 值指定红色、绿色和蓝色颜色强度，范围为 `[0,1]`。

#### 依赖关系

所选颜色字段必须支持 rgb 值。

**数据类型：** `double`

### **Alpha** — 输入图像的 Alpha 通道 *N*×1 向量 | *h*×*w* 矩阵

图像的 Alpha 通道，指定为 *N*×1 向量或 *h*×*w* 矩阵。每个元素的值在 `[0,1]` 范围内，表示对应像素的不透明度，值 `0` 表示完全透明。

#### 依赖关系

所选颜色字段必须支持 alpha 通道。

**数据类型：** `double`

### **Intensity** — 每个点的强度值矩阵 | 数组

点云数据中每个点的强度值，指定为 *N*×3 矩阵或 *h*×*w*×3 数组。*N* 是点云中的点数。*h* 和 *w* 是图像的高度和宽度，以像素为单位。

#### 依赖关系

必须选择 **写入 Intensity 字段** 参数。

**数据类型：** `single` | `double`
### 输出

### **Msg** — ROS 或 ROS 2 点云消息非虚拟总线

ROS 或 ROS 2 点云消息，返回为非虚拟总线。你可以使用 ROS Publish 或 ROS 2 Publish 模块分别将消息发布到活动的 ROS 或 ROS 2 网络。

**数据类型：** `bus`

## 参数

### **选择颜色字段** — 点云图像的颜色字段 `none`（默认） | `rgb` | `rgba`

点云图像的颜色字段，指定为支持的选项之一。选择适当的选项以指定与点云图像对应的颜色和 alpha 值。

### **写入 Intensity 字段** — 写入强度值 off（默认） | on

选择是否将强度值写入输出消息。

## 所属库

ROS Toolbox / ROS ROS Toolbox / ROS 2

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2022a 中引入**

## 描述

将点云数据写入 ROS 或 ROS 2 消息

Write Point Cloud 模块将点云数据写入 ROS 或 ROS 2 点云消息。你可以为点云图像指定适当的颜色编码，并将相应的颜色和 alpha 值写入输出消息。你还可以将强度值写入输出消息。使用 ROS Publish 或 ROS 2 Publish 模块将输出图像消息发布到网络上的活动话题。
