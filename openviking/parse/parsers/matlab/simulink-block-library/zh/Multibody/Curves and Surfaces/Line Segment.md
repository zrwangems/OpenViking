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

### Frame

### **R** — 局部参考坐标系 frame

线段的参考坐标系。将此坐标系连接到另一个模块，以指定线段的位置和方向。
### Geometry

### **G** — 几何 geometry

表示线段的几何。您可以将此端口连接到 Planar Contact Force 模块，以对线段上的接触进行建模。

## 参数

### **Length** — 线段长度 1 `m`（默认）| 正标量

线段的长度，指定为正标量。线段沿局部参考坐标系的 *x* 轴方向。

#### 图形

### **Type** — 可视化设置 `From Geometry`（默认）| `None`

线段的可视化设置。使用默认设置 `From Geometry` 可显示线段。选择 `None` 可禁用线段的可视化。

### **Visual Properties** — 颜色和不透明度的参数化设置 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化设置。选择 `Simple` 可指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 可指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Diffuse Color** — 线段颜色 [0.5 0.5 0.5]（默认）| 三元素向量 | 四元素向量

在直接白光下的真实颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素以 0–1 的范围指定颜色不透明度。省略不透明度元素等效于指定值为 1。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量为 0 对应于完全透明，标量为 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 镜面反射光颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。此参数会改变镜面高光的颜色，镜面高光是由于光源的光反射而在渲染实体上出现的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

环境光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

环境光是指并非直接来自光源的一般照明水平。环境光是经过多次反射和再反射、以至于不再来自任何特定方向的光。您可以调整此参数以更改渲染对象的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

由自发光产生的颜色，指定为取值范围在 0 到 1 之间的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

自发光颜色是不来自任何外部光源的颜色，因此看起来是由物体自身发出的。当物体具有自发光颜色时，即使没有外部光源，该物体也能被看到。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 取值范围约束在 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

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

Line Segment 模块创建一个线段。该线段沿着位于线段中点的局部参考系的 *x* 轴方向。

线段示意图
