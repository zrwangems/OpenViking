---
type: simulink-block
title: 'Infinite Plane'
family: 'curves-and-surfaces'
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

### 坐标系

### **R** — 参考坐标系 frame

无限平面参考坐标系。将此坐标系连接到另一个模块，以指定无限平面的位置和方向。
### 几何

### **G** — 几何 frame

表示由此模块定义的平面的几何。将此端口连接到 Spatial Contact Force 模块，以对与支持的几何体进行接触建模。

## 参数

### 图形

### **Type** — 平面的可视表示 `Rectangle` (default) | `None`

平面的可视表示。将此参数设置为 `Rectangle` 可将无限平面的可视表示显示为带虚线边界的矩形。将此参数设置为 `None` 可从模型可视化中移除该平面。

### **Width (X)** — 平面可视表示的宽度 1 `m` (default) | 正整数

平面的可视表示的宽度。请注意，实际平面具有无限大小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Rectangle`。

### **Height (Y)** — 平面可视表示的高度 1 `m` (default) | 正整数

平面的可视表示的高度。请注意，实际平面具有无限大小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Rectangle`。

### **Visual Properties** — 用于颜色和不透明度的参数化 `Simple` (default) | `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 可指定漫反射颜色和不透明度。选择 `Advanced` 可指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Rectangle`。

### **Diffuse Color** — 图形颜色 [0.5 0.5 0.5] (default) | 三元素向量 | 四元素向量

直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Simple`

### **Opacity** — 图形不透明度 0.25 (default) | 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应完全透明，标量 1 对应完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 高光颜色 [0.5 0.5 0.5 1.0] (default) | 三元素向量 | 四元素向量

镜面高光的颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 阴影颜色 [0.15 0.15 0.15 1.0] (default) | 三元素向量 | 四元素向量

漫射环境光中阴影区域的颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0] (default) | 三元素向量 | 四元素向量

由于自发光而产生的图形颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75 (default) | 1 到 128 范围内的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数字。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Rectangle`
2. **Visual Properties** 为 `Advanced`

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

Infinite Plane 模块创建一个无限平面，可用于对接触问题进行建模。您可以对平面与各种类型的几何体之间的接触进行建模。有关支持的几何体，请参阅“支持的几何体”。此外，Infinite Plane 模块支持 Custom Tire Force and Torque 以及 Magic Formula Tire Force and Torque 模块。

必须使用平面的正法向侧进行接触，其方向由坐标系的蓝色轴指示。否则，接触部分将穿过平面被弹射到正侧。

Infinite Plane

Infinite Plane 模块在平面接触建模中很有用。例如，与 Brick Solid 模块相比，Infinite Plane 模块在建模地平面时有效得多。

Infinite Plane 示例
