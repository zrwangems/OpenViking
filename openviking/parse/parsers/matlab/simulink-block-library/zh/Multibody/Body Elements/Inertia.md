---
type: simulink-block
title: 'Inertia'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'inertia'
documentation_source_path: 'ref/inertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Inertia

## 端口
```yaml
ports:
- name: R
  summary: 参考坐标系 frame
  direction: unspecified
```

### Frame

### **R** — 参考坐标系 frame

惯性单元的局部参考坐标系。连接到 frame 线或 frame 端口以定义惯性的相对位置和方向。
## 参数
```yaml
parameters:
- name: Type
  summary: 要使用的惯性参数化方式 Point Mass（默认）| Custom
  group: Inertia
- name: Mass
  summary: 实体单元的总质量 1 kg（默认）| 带质量单位的标量
  group: Inertia
- name: 'Custom: Center of Mass'
  summary: 质心坐标 [0 0 0] m（默认）| 带长度单位的三元素向量
  group: Inertia
- name: 'Custom: Moments of Inertia'
  summary: 惯性张量的对角元素 [1 1 1] kg*m^2（默认）| 带质量\*长度^2 单位的三元素向量
  group: Inertia
- name: 'Custom: Products of Inertia'
  summary: 惯性张量的非对角元素 [0 0 0] kg*m^2（默认）| 带质量\*长度^2 单位的三元素向量
  group: Inertia
- name: Type
  summary: 用于惯性可视化显示的图形 Marker（默认）| None
  group: Graphic
- name: Shape
  summary: 用于表示惯性的标记形状 Inertia Icon（默认）| Sphere | Cube | Frame
  group: Graphic
- name: Size
  summary: 标记的宽度（以像素为单位）20 pixels（默认）| 标量
  group: Graphic
- name: Visual Properties
  summary: 颜色和不透明度的参数化方式 Simple（默认）| Advanced
  group: Graphic
- name: Diffuse Color
  summary: 漫反射产生的光颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: Opacity
  summary: 图形不透明度 1.0（默认）| 取值范围为 0 到 1 的标量
  group: Graphic
- name: Specular Color
  summary: 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: Ambient Color
  summary: 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: Emissive Color
  summary: 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量
  group: Graphic
- name: Shininess
  summary: 标记的光泽度 75（默认）| 取值范围为 1 到 128 的标量
  group: Graphic
```

### Inertia

### **Type** — 要使用的惯性参数化方式 `Point Mass`（默认）| `Custom`

要使用的惯性参数化方式。选择 `Point
Mass` 表示无转动惯量的质量。
选择 `Custom` 表示具有转动惯量的分布质量。

### **Mass** — 实体单元的总质量 `1 kg`（默认）| 带质量单位的标量

要赋予实体单元的总质量。此参数可以为正值或负值。使用负值来捕获复合体（由多个实体和惯性组成）中空隙或空腔的效果，同时注意确保该物体的质量总体上为正值。

### **Custom: Center of Mass** — 质心坐标 `[0 0 0] m`（默认）| 带长度单位的三元素向量

质心相对于模块参考坐标系的 [x y z] 坐标。仅在均匀引力场中，质心与重心重合。

### **Custom: Moments of Inertia** — 惯性张量的对角元素 `[1 1 1] kg*m^2`（默认）| 带质量\*长度^2 单位的三元素向量

三元素向量，包含相对于原点位于质心且坐标轴平行于模块参考坐标系的坐标系所指定的 [Ixx Iyy
Izz] 惯性矩。惯性矩是惯性张量的对角元素

(IxxIyyIzz)，

其中：

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

### **Custom: Products of Inertia** — 惯性张量的非对角元素 `[0 0 0] kg*m^2`（默认）| 带质量\*长度^2 单位的三元素向量

三元素向量，包含相对于原点位于质心且坐标轴平行于模块参考坐标系的坐标系所指定的 [Iyz Izx Ixy]
惯性积。惯性积是惯性张量的非对角元素

(IxyIzxIxyIyzIzxIyz)，

其中：

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

### Graphic

### **Type** — 用于惯性可视化显示的图形 `Marker`（默认）| `None`

用于惯性可视化显示的图形类型，指定为 `Marker` 或 `None`。
将此参数设置为 `Marker` 以将惯性表示为标记，将此参数设置为
`None` 以在模型可视化中隐藏惯性。

### **Shape** — 用于表示惯性的标记形状 `Inertia Icon`（默认）| `Sphere` | `Cube` | `Frame`

标记的形状，指定为 `Inertia
Icon`、`Sphere`、
`Cube` 或
`Frame`。标记的运动反映惯性本身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Marker`。

### **Size** — 标记的宽度（以像素为单位）20 `pixels`（默认）| 标量

标记的宽度（以像素为单位），指定为标量。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，较高分辨率下每单位长度包含更多像素，因此产生的图标更小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Marker`。

### **Visual Properties** — 颜色和不透明度的参数化方式 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化方式。选择
`Simple` 以指定 **Diffuse
Color** 和 **Opacity**。选择
`Advanced` 以指定更多视觉属性，例如 **Specular Color**、
**Ambient Color**、**Emissive
Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Marker`。

### **Diffuse Color** — 漫反射产生的光颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

漫反射产生的光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Opacity** — 图形不透明度 1.0（默认）| 取值范围为 0 到 1 的标量

图形不透明度，指定为取值范围为 0 到 1 的标量。标量为 0 对应于完全透明，标量为 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

镜面反射产生的光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

环境光是指并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射、以至于不再来自任何特定方向的光组成。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

发射颜色是不来自任何外部光源的颜色，因此看起来是由标记自身发出的。当标记具有发射颜色时，即使没有外部光源，也可以看到该标记。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 标记的光泽度 75（默认）| 取值范围为 1 到 128 的标量

标记的光泽度，指定为取值范围为 0 到 128 的标量。此参数影响标记镜面反射的锐利程度。高光泽度的标记具有类似镜面的外观，低光泽度的标记具有更低光泽或缎面的外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker`
2. **Visual Properties** 为 `Advanced`
## 所属库

Simscape / Multibody / Body Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

具有固定惯性属性的质量单元

Inertia 模块向所连接的坐标系添加一个具有固定惯性属性的质点或分布质量。质量类型（质点或分布质量）取决于为模块选择的参数化方式。选择 `Point Mass` 假定质量集中于一点，因此不具有转动惯量。选择 `Custom` 假定质量在空间中分布，允许其具有非零惯性矩、惯性积以及质心坐标（后者相对于模块的参考坐标系）。

选择标记提供了一种在模型可视化中识别惯性的方法。可视化（默认情况下）在仿真开始时或框图更新时在 Multibody Explorer 中打开。使用标记可相对于模型其余部分跟踪惯性的运动。有多种标记形状可用——惯性图标、球体、立方体、坐标系——每种都具有可配置的尺寸。若要从模型可视化中消除惯性（同时保留其对模型动力学的影响），模块提供了 `None` 选项。
