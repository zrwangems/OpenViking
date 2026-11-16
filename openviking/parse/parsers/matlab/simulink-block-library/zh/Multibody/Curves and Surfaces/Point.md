---
type: simulink-block
title: 'Point'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'point'
documentation_source_path: 'ref/point.html'
language: zh-CN
chinese_source: worker-translation
---

# Point

## 端口

### 坐标系

### **R** — 局部参考坐标系 frame

用于定义点的位置和方向的局部参考坐标系。
### 几何

### **G** — 几何坐标系 frame

表示此模块定义的点的几何坐标系。将此端口连接到 Spatial Contact Force 模块，以对点上的接触进行建模。

## 参数

### 图形

### **Type** — 用于点可视化的图形 `Marker`（默认）| `None`

用于可视化点的图形。将此参数指定为 `None` 以从模型可视化中消除该点。

### **Shape** — 点标记的形状 `Sphere`（默认）| `Cube` | `Frame`

用于可视化点的标记的形状。标记形状对点的接触结果没有影响。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记的宽度，以像素为单位 10 `pixels`（默认）| 标量

标记的宽度，以像素为单位。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，分辨率越高，每单位长度包含的像素越多，因此产生的图标越小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定漫反射颜色和不透明度。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Diffuse Color** — 图形颜色 [0.5 0.5 0.5]（默认）| 三元素向量 | 四元素向量

直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值为 1。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应于完全透明，标量 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 镜面反射光颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。此参数更改镜面高光的颜色，即因光源光线反射而在渲染实体上出现的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

环境光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

环境光是指不直接来自光源的一般照明水平。环境光由经过多次反射和再反射、不再来自任何特定方向的光组成。您可以调整此参数以更改渲染实体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量

自发光颜色，指定为 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

发射颜色是不来自任何外部来源的颜色，因此似乎由实体本身发射。当实体具有自发光颜色时，即使没有外部光源也可以看到该实体。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 值限制在 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2020b 中引入**

## 描述

用于接触建模的点几何

Point 模块导出一个 0-D 点几何，用于对接触问题进行建模。您可以对点与多种几何体之间的接触进行建模，例如 Body Element 库中的所有实体和凸包，以及 Curves and Surfaces 库中的无限平面。但是，您无法对一对点之间的接触进行建模，因为两个点之间没有穿透，而穿透是罚函数法所必需的。

Point

使用点几何可以通过消除不必要的几何细节来简化和加速涉及复杂几何体的接触建模。例如，在 Train Humanoid Walker 示例中，您可以使用多个点来表示机器人脚部，从而简化脚-地面接触。

机器人脚部
