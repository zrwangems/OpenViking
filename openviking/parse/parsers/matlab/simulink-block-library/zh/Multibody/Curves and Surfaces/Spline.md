---
type: simulink-block
title: 'Spline'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'spline'
documentation_source_path: 'ref/spline.html'
language: zh-CN
chinese_source: worker-translation
---

# Spline

## 端口
```yaml
ports:
- name: R
  summary: 参考坐标系 frame
  direction: unspecified
- name: G
  summary: 样条曲线表示几何
  direction: unspecified
```

### Frame

### **R** — 参考坐标系 frame

样条曲线参考坐标系。将此 frame 端口连接到另一个模块，以指定样条曲线在模型中的位置和方向。

### Geometry

### **G** — 样条曲线表示几何

与二维或三维连续样条曲线表示相关联的几何数据。它向与其连接的其他模块（例如 Point on Curve Constraint 模块）提供样条曲线规格。
## 参数
```yaml
parameters:
- name: Interpolation Points
  summary: 用于指定样条曲线的插值点坐标 [6 -2 9; -6 5 -4; -6 -7 9; 6 0 -4; -3 6 9; -3 -8 -4] m（默认）| *N*×2 矩阵 | *N*×3 矩阵
  group: ''
- name: End Conditions
  summary: 曲线端点的处理方式 Periodic (Closed)（默认）| Natural (Open)
  group: ''
- name: Type
  summary: 样条可视化设置 From Geometry（默认）| Marker | None
  group: ''
- name: Visual Properties
  summary: 颜色和不透明度的参数化 Simple（默认）| Advanced
  group: ''
- name: Diffuse Color
  summary: 真彩色，格式为 [R,G,B,A] [0.0 0.0 0.0]（默认）| 三元素向量 | 四元素向量
  group: ''
- name: Opacity
  summary: 图形不透明度 1.0（默认）| 0 到 1 范围内的标量
  group: ''
- name: Specular Color
  summary: 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: ''
- name: Ambient Color
  summary: 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: ''
- name: Emissive Color
  summary: 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量
  group: ''
- name: Shininess
  summary: 高光锐度 75（默认）| 取值范围约束为 0–128 的标量
  group: ''
- name: Shape
  summary: 图形标记的形状 Sphere（默认）| Cube | Frame
  group: ''
- name: Size
  summary: 标记的宽度（以像素为单位）10 pixels（默认）| 标量
  group: ''
```

### **Interpolation Points** — 用于指定样条曲线的插值点坐标 [6 -2 9; -6 5 -4; -6 -7 9; 6 0 -4; -3 6 9; -3 -8 -4] m（默认）| *N*×2 矩阵 | *N*×3 矩阵

包含用于定义样条曲线的插值点坐标的矩阵。使用 *N*×2 矩阵指定二维样条，使用 *N*×2 矩阵指定三维样条。矩阵的每一行指定一个插值点相对于 Spline 模块参考坐标系的笛卡尔坐标。如果矩阵包含任何重复行，则会发生错误。

#### 提示

您可以使用 `unique` 函数从输入矩阵中删除重复行。

### **End Conditions** — 曲线端点的处理方式 `Periodic (Closed)`（默认）| `Natural (Open)`

样条曲线的端点条件。`Periodic (Closed)` 端点条件对应于闭合曲线。对于此条件，模块用连续曲线连接第一个和最后一个数据点。`Natural (Open)` 端点条件对应于开放曲线。

样条曲线是由首尾相连的三阶多项式段组成的分段函数。曲线的构建使得相邻多项式段在共享端点处具有相同的一阶和二阶导数。

#### 图形

### **Type** — 样条可视化设置 `From Geometry`（默认）| `Marker` | `None`

此样条的可视化设置。使用默认设置 `From Geometry` 显示样条。选择 `Marker` 显示图形标记，例如球体或坐标系。选择 `None` 禁用此样条的可视化。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Diffuse Color** — 真彩色，格式为 [R,G,B,A] [0.0 0.0 0.0]（默认）| 三元素向量 | 四元素向量

在直接白光下的真彩色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素指定 0–1 范围内的颜色不透明度。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量为 0 对应于完全透明，标量为 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

镜面反射产生的光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。此参数改变镜面高光的颜色，镜面高光是由于光源的光线反射而在渲染实体上形成的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

环境光是指并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射以至于不再来自任何特定方向的光组成。您可以调整此参数来改变渲染实体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

发射颜色是不来自任何外部光源的颜色，因此看起来是由实体本身发出的。当实体具有发射颜色时，即使没有外部光源，也可以看到该实体。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 取值范围约束为 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大光泽度值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Shape** — 图形标记的形状 `Sphere`（默认）| `Cube` | `Frame`

图形标记的几何形状。Multibody Explorer 使用所选形状显示标记。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记的宽度（以像素为单位）10 `pixels`（默认）| 标量

标记的宽度（以像素为单位）。此宽度不随缩放级别缩放。请注意，标记的视觉大小部分取决于屏幕分辨率，较高分辨率下每单位长度包含更多像素，因此产生的图标更小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。
## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

三次插值平面曲线或空间曲线

此 Spline 模块基于指定点之间的三次插值创建连续样条曲线。该曲线可以是二维的，例如平面凸轮轮廓，也可以是三维的，例如过山车轨道。样条的维度取决于坐标矩阵的维度。一个 *N*×2 矩阵指定 *xy* 平面中的二维曲线。一个 *N*×3 矩阵指定三维曲线。所有坐标均在模块的局部参考坐标系中解析。此外，根据指定的端点条件，曲线可以是开放的或闭合的。

二维样条曲线示例
