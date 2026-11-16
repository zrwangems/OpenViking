---
type: simulink-block
title: 'Line Segment'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'linesegment'
documentation_source_path: 'ref/linesegment.html'
language: zh-CN
chinese_source: worker-translation
---

# Line Segment

## 端口

### 坐标系

### **R** — 局部参考坐标系 frame

线段的参考坐标系。将此坐标系连接到另一个模块，以指定线段的位置和方向。
### 几何

### **G** — 几何 geometry

表示线段的几何。您可以将此端口连接到 Planar Contact Force 模块，以对线段上的接触进行建模。

## 参数

### **Length** — 线段长度 1 `m`（默认）| 正标量

线段长度，指定为正标量。该线段沿局部参考坐标系的 *x* 轴。

#### 图形

### **Type** — 可视化设置 `From Geometry`（默认）| `None`

线段的可视化设置。使用默认设置 `From Geometry` 显示线段。选择 `None` 可禁用线段的可视化。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 可指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 可指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖项

若要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Diffuse Color** — 线段颜色 [0.5 0.5 0.5]（默认）| 三元素向量 | 四元素向量

直射白光下的真实颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖项

若要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应完全透明，标量 1 对应完全不透明。

#### 依赖项

若要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 镜面反射所致的光颜色 [0.5 0.5 0.5 1.0]（默认）| 值为 0 到 1 范围内的 3×1 或 1×3 向量 | 值为 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射所致的光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数更改镜面高光的颜色，镜面高光是由于光源的光线反射而在渲染实体上出现的亮点。

#### 依赖项

若要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 值为 0 到 1 范围内的 3×1 或 1×3 向量 | 值为 0 到 1 范围内的 4×1 或 1×4 向量

环境光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光是指并不直接来自光源的一般照明水平。环境光是已经反射并再次反射多次、以至于不再来自任何特定方向的光。您可以调整此参数以更改所渲染对象的阴影颜色。

#### 依赖项

若要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 值为 0 到 1 范围内的 3×1 或 1×3 向量

自发光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部源、因此看起来由对象自身发出的颜色。当对象具有发射颜色时，即使没有外部光源，也可以看到该对象。

#### 依赖项

若要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 值限制在 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数字。增大 **Shininess** 值以获得更小但更锐利的高光。减小该值以获得更大但更平滑的高光。

#### 依赖项

若要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

线段几何

Line Segment 模块创建一条线段。该线段沿局部参考坐标系的 *x* 轴，该局部参考坐标系位于线段的中点。

线段示意图
