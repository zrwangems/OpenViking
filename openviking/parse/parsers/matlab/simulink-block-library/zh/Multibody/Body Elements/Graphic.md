---
type: simulink-block
title: 'Graphic'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'graphic'
documentation_source_path: 'ref/graphic.html'
language: zh-CN
chinese_source: worker-translation
---

# Graphic

## 端口

### Frame

### **R** — 参考坐标系 frame

图形标记的局部参考坐标系。连接到 frame line 或 frame port，以定义标记的相对位置和方向。

## 参数

### **Shape** — 可视化期间要显示的标记形状 `Sphere`（默认） | `Cube` | `Frame`

模型中可视化时要显示的标记形状，指定为 `Sphere`、`Cube` 或 `Frame`。标记的运动反映模块所连接到的 frame 的运动。

### **Size** — 标记的宽度（以 pixels 为单位） 10 `pixels`（默认） | scalar

标记的宽度，以 pixels 为单位，指定为 scalar。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，较高分辨率每单位长度容纳更多像素，因此产生更小的图标。

### Visual Properties

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认） | `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

### **Diffuse Color** — 漫反射产生的光颜色 [0.5 0.5 0.5]（默认） | 3×1 或 1×3 向量，值在 0 到 1 范围内 | 4×1 或 1×4 向量，值在 0 到 1 范围内

漫反射产生的光颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

### **Opacity** — 图形不透明度 1.0（默认） | 0 到 1 范围内的 scalar

图形不透明度，指定为 0 到 1 范围内的 scalar。scalar 0 对应完全透明，scalar 1 对应完全不透明。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Simple`。

### **Specular Color** — 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0]（默认） | 3×1 或 1×3 向量，值在 0 到 1 范围内 | 4×1 或 1×4 向量，值在 0 到 1 范围内

镜面反射产生的光颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认） | 3×1 或 1×3 向量，值在 0 到 1 范围内 | 4×1 或 1×4 向量，值在 0 到 1 范围内

环境光颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光指不直接来自光源的一般照明水平。环境光由已经反射和再反射多次、从而不再来自任何特定方向的光组成。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认） | 3×1 或 1×3 向量，值在 0 到 1 范围内

自发光产生的颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部源的颜色，因此似乎由标记自身发射。当标记具有发射颜色时，即使没有外部光源，也可以看到该标记。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

### **Shininess** — 标记的光泽度 75（默认） | 1 到 128 范围内的 scalar

标记的光泽度，指定为 0 到 128 范围内的 scalar。此参数影响标记镜面反射的锐度。高光泽度的标记具有类似镜面的外观，低光泽度的标记具有更低光泽或缎面外观。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

## 所属库

Simscape / Multibody / Body Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

具有图形属性的标记

Graphic 模块向附加的 frame 添加一个简单标记。该标记具有简单的几何形状、颜色，且无惯量。您可以使用此模块在 Multibody Explorer 可视化窗格中突出显示感兴趣的 frame。图形标记对模型动力学没有影响。

**图形标记几何形状**
