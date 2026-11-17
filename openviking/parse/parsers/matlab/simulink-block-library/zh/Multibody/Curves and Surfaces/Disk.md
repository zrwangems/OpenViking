---
type: simulink-block
title: 'Disk'
family: 'sm'
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
```yaml
ports:
- name: R
  summary: 参考坐标系 frame
  direction: unspecified
- name: G
  summary: 几何体 geometry
  direction: unspecified
```

### Frame

### **R** — 参考坐标系 frame

圆盘的参考坐标系。将此坐标系连接到另一个模块以指定圆盘的位置和方向。
### Geometry

### **G** — 几何体 geometry

表示圆盘的几何体。将此端口连接到 Spatial Contact Force 模块以对圆盘上的接触进行建模。
## 参数
```yaml
parameters:
- name: Radius
  summary: 圆盘半径 1 m（默认）| 正整数
  group: ''
- name: Type
  summary: 圆盘的视觉表示 From Geometry（默认）| None
  group: Graphic
- name: Visual Properties
  summary: 颜色和不透明度的参数化方式 Simple（默认）| Advanced
  group: Graphic
- name: Diffuse Color
  summary: 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量
  group: Graphic
- name: Opacity
  summary: 渲染对象的不透明度 1.0（默认）| 0 到 1 范围内的标量
  group: Graphic
- name: Specular Color
  summary: 镜面反射光的颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量
  group: Graphic
- name: Ambient Color
  summary: 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量
  group: Graphic
- name: Emissive Color
  summary: 自发光颜色 [0 0 0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: Shininess
  summary: 渲染对象的光泽度 75（默认）| 取值范围为 0 到 128 的标量
  group: Graphic
```

### **Radius** — 圆盘半径 1 `m`（默认）| 正整数

圆盘的半径，指定为带长度单位的正整数。

### Graphic

### **Type** — 圆盘的视觉表示 `From Geometry`（默认）| `None`

圆盘的视觉表示。将此参数设置为 `From
Geometry` 以显示圆盘的视觉表示。将此参数设置为 `None` 以在模型可视化中隐藏圆盘。

### **Visual Properties** — 颜色和不透明度的参数化方式 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化方式。选择
`Simple` 以指定漫反射颜色和不透明度。选择
`Advanced` 以指定更多视觉属性，例如
**Specular Color**、**Ambient Color**、
**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From
Geometry`。

### **Diffuse Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

漫反射光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A]
向量。该向量可以是行向量或列向量。
可选的第四个元素指定颜色不透明度。省略不透明度元素
等同于指定值 1。

漫反射颜色反映渲染对象的主色，并提供
着色效果，使渲染对象呈现三维外观。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From
Geometry`。

### **Opacity** — 渲染对象的不透明度 1.0（默认）| 0 到 1 范围内的标量

渲染对象的不透明度，指定为 0 到 1 范围内的标量。标量
0 对应于完全透明，标量 1 对应于
完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为
   `Simple`

### **Specular Color** — 镜面反射光的颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或
[R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度
元素等同于指定值 1。

镜面高光是渲染对象上由于
光源光线反射而产生的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为
   `Advanced`

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

环境光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。
该向量可以是行向量或列向量。可选的
第四个元素指定颜色不透明度。省略不透明度元素等同于
指定值 1。

此属性指定并非直接来自光源的一般照明
水平。使用此属性可更改渲染对象的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为
   `Advanced`

### **Emissive Color** — 自发光颜色 [0 0 0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

由自发光产生的颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，其取值范围为 0 到 1。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 渲染对象的光泽度 75（默认）| 取值范围为 0 到 128 的标量

渲染对象的光泽度，指定为取值范围为 0 到 128 的标量。此属性影响渲染对象镜面反射的锐利程度。光泽度高的对象具有类似镜面的外观，光泽度低的对象则具有更低光泽或缎面的外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`
## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

用于接触建模的圆盘

Disk 模块创建一个二维圆盘，可用于对接触问题进行建模。您可以对圆盘与许多其他几何体之间的接触进行建模，包括无限平面、长方体、圆柱体、椭球体、球体或凸包。

Disk 模块有两个端口。**R** 端口对应于与圆盘几何体原点重合的参考坐标系，圆盘位于该参考坐标系的 *xy* 平面上。**G** 端口是表示圆盘几何体的几何体端口。

圆盘示意图

要指定圆盘的大小，请使用 **Radius** 参数。
