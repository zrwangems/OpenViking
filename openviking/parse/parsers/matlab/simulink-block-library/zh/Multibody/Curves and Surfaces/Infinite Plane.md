---
type: simulink-block
title: 'Infinite Plane'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'infiniteplane'
documentation_source_path: 'ref/infiniteplane.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Plane

## 端口

### Frame

### **R** — 参考坐标系 frame

无限平面参考坐标系。将此坐标系连接到另一个模块，以指定无限平面的位置和方向。
### Geometry

### **G** — 几何坐标系 frame

表示此模块所定义平面的几何体。将此端口连接到 Spatial Contact Force 模块，以对与受支持几何体的接触进行建模。

## 参数

### Graphic

### **Type** — 平面的视觉表示 `Rectangle`（默认）| `None`

平面的视觉表示。将此参数设置为 `Rectangle`，以将无限平面的视觉表示显示为带虚线边界的矩形。将此参数设置为 `None`，以从模型可视化中消除该平面。

### **Width (X)** — 平面视觉表示的宽度 1 `m`（默认）| 正整数

平面视觉表示的宽度。请注意，实际平面具有无限尺寸。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Rectangle`。

### **Height (Y)** — 平面视觉表示的高度 1 `m`（默认）| 正整数

平面视觉表示的高度。请注意，实际平面具有无限尺寸。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Rectangle`。

### **Visual Properties** — 颜色和不透明度的参数化方式 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化方式。选择 `Simple` 以指定漫反射颜色和不透明度。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Rectangle`。

### **Diffuse Color** — 图形颜色 [0.5 0.5 0.5]（默认）| 三元素向量 | 四元素向量

图形在直接白光下的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 以 0–1 的范围指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Simple`

### **Opacity** — 图形不透明度 0.25（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量为 0 对应于完全透明，标量为 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 高光颜色 [0.5 0.5 0.5 1.0]（默认）| 三元素向量 | 四元素向量

镜面高光的颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 阴影颜色 [0.15 0.15 0.15 1.0]（默认）| 三元素向量 | 四元素向量

漫反射环境光中阴影区域的颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 三元素向量 | 四元素向量

由于自发光而产生的图形颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 1 到 128 范围内的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为
   `Advanced`

## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

用于接触建模的无限平面

Infinite Plane 模块创建一个无限平面，可用于对接触问题进行建模。您可以对该平面与各种类型的几何体之间的接触进行建模。有关支持的几何体，请参阅支持的几何体。此外，Infinite Plane 模块支持 Custom Tire Force and Torque 和 Magic Formula Tire Force and Torque 模块。

您必须使用平面的正法线侧进行接触，即坐标系蓝色轴所指示的方向。否则，接触部件将通过平面被弹出到正侧。

Infinite Plane

Infinite Plane 模块在平面接触建模中非常有用。例如，在建模地平面时，Infinite Plane 模块比 Brick Solid 模块有效得多。

Infinite Plane 示例
