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

图形标记的局部参考坐标系。连接到 frame 线或 frame 端口，以定义标记的相对位置和方向。

## 参数

### **Shape** — 可视化期间显示的标记形状 `Sphere`（默认）| `Cube` | `Frame`

在模型可视化中显示的标记形状，指定为 `Sphere`、`Cube` 或 `Frame`。标记的运动反映与模块连接的 frame 的运动。

### **Size** — 标记的宽度（以像素为单位） 10 `pixels`（默认）| 标量

标记的宽度（以像素为单位），指定为标量。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，较高分辨率每单位长度包含更多像素，因此会产生较小的图标。

### Visual Properties

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

### **Diffuse Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

漫反射光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应于完全透明，标量 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Simple`。

### **Specular Color** — 镜面反射光的颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

环境光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光是指并非直接来自光源的一般照明水平。环境光由已经反射并再次反射多次、以至于不再来自任何特定方向的光组成。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

由自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

自发光颜色是不来自任何外部光源的颜色，因此看起来是由标记自身发出的。当标记具有自发光颜色时，即使没有外部光源，也可以看到该标记。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

### **Shininess** — 标记的光泽度 75（默认）| 取值范围为 1 到 128 的标量

标记的光泽度，指定为取值范围为 0 到 128 的标量。此参数影响标记镜面反射的锐利程度。光泽度高的标记具有类似镜面的外观，光泽度低的标记具有更低光泽或缎面外观。

#### 依赖关系

要启用此参数，请将 **Visual Properties** 设置为 `Advanced`。

## 所属库

Simscape / Multibody / Body Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

具有图形属性的标记

Graphic 模块向所连接的坐标系添加一个简单标记。该标记具有简单的几何形状、颜色，并且没有惯性。您可以使用此模块在 Multibody Explorer 可视化窗格中突出显示感兴趣的坐标系。该图形标记对模型动力学没有影响。

**Graphic Marker Geometries**
