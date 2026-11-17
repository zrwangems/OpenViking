---
type: simulink-block
title: 'Disk'
family: 'curves-and-surfaces'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'disk'
documentation_source_path: 'ref/disk.html'
language: zh-CN
chinese_source: worker-translation
---

# Disk

## 端口

### 坐标系

### **R** — 参考坐标系 frame

圆盘参考坐标系。将此坐标系连接到另一个模块，以指定圆盘的位置和方向。
### 几何

### **G** — 几何 geometry

表示圆盘的几何。将此端口连接到 Spatial Contact Force 模块，以对圆盘上的接触进行建模。

## 参数

### **Radius** — 圆盘半径 1 `m`（默认）| 正整数

圆盘的半径，指定为带长度单位的正整数。

### 图形

### **Type** — 圆盘的视觉表示 `From Geometry`（默认）| `None`

圆盘的视觉表示。将此参数设置为 `From Geometry` 可显示圆盘的视觉表示。将此参数设置为 `None` 可在模型可视化中隐藏该圆盘。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 可指定漫反射颜色和不透明度。选择 `Advanced` 可指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Diffuse Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

漫反射光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

漫反射颜色反映渲染对象的主色，并提供阴影，使渲染对象具有三维外观。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Opacity** — 渲染对象的不透明度 1.0（默认）| 范围 0 到 1 内的标量

渲染对象的不透明度，指定为范围 0 到 1 内的标量。标量 0 对应于完全透明，标量 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为
   `Simple`

### **Specular Color** — 镜面反射光的颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

镜面高光是渲染对象上因光源光线反射而产生的亮斑。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为
   `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

环境光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

此属性指定不直接来自光源的一般照明水平。使用此属性可更改渲染对象的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为
   `Advanced`

### **Emissive Color** — 自发光颜色 [0 0 0 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

自发光引起的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为
   `Advanced`

### **Shininess** — 渲染对象的光泽度 75（默认）| 范围 0 到 128 内的标量

渲染对象的光泽度，指定为范围 0 到 128 内的标量。此属性会影响渲染对象镜面反射的锐度。高光泽度的对象具有类似镜面的外观，低光泽度的对象具有更低光泽或缎面外观。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为
   `Advanced`

## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

用于接触建模的 Disk

Disk 模块创建一个 2-D 圆形圆盘，可用于对接触问题进行建模。您可以对圆盘与许多其他几何体之间的接触进行建模，包括无限平面、brick、圆柱体、椭球体、球体或凸包。

Disk 模块有两个端口。**R** 端口对应于与圆盘几何原点重合的参考坐标系，圆盘位于参考坐标系的 *xy* 平面内。**G** 端口是表示圆盘几何的几何端口。

圆盘示意图

要指定圆盘的大小，请使用 **Radius** 参数。
