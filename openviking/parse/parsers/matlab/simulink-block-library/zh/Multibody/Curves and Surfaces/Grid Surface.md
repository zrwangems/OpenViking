---
type: simulink-block
title: 'Grid Surface'
family: 'curves-and-surfaces'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Curves and Surfaces'
documentation_page: 'gridsurface'
documentation_source_path: 'ref/gridsurface.html'
language: zh-CN
chinese_source: worker-translation
---

# Grid Surface

## 端口

### 坐标系

### **R** — 局部参考坐标系 frame

网格曲面参考坐标系。将此 frame 连接到另一个模块，以指定网格曲面的位置和方向。
### 几何体

### **G** — 几何体 geometry

表示由该模块定义的网格曲面的几何体。将此端口连接到 Spatial Contact Force 模块，以对与受支持几何体的接触进行建模。

## 参数

### **X Grid Vector** — 沿 *x* 方向的坐标 [0 1 2 3] `m` (默认) | *1-by-m* vector

网格曲面沿 *x* 方向的坐标，指定为 real *1-by-m* vector。*m* 必须大于 2，且 vector 元素必须严格单调递增。此 vector 对应于 **Z Heights** 参数中指定矩阵的行。

x grid vector 与 z height matrix 之间关系的图示

### **Y Grid Vector** — 沿 *y* 方向的坐标 [0 1 2 3] `m` (默认) | *1-by-n* vector

网格曲面沿 *y* 方向的坐标，指定为 real *1-by-n* vector。*n* 必须大于 2，且 vector 元素必须严格单调递增。此 vector 对应于 **Z Heights** 参数中指定矩阵的列。

y grid vector 与 z height matrix 之间关系的图示

### **Z Heights** — 网格点的高程 [0 0 .5 .5; 0 0 .5 .5; 0 0 0 0; 0 0 0 0] `m` (默认) | *m-by-n* matrix

网格曲面中网格点的高程，指定为 real *m-by-n* matrix。*m* 和 *n* 分别是 **X Grid Vector** 和 **Y Grid Vector** 参数向量的长度。

### 图形

### **Type** — 网格曲面的可视化表示 `From Geometry` (默认) | `None`

网格曲面的可视化表示。将此参数设置为 `From Geometry` 可显示网格曲面的可视化表示。将此参数设置为 `None` 可在模型可视化中隐藏网格曲面。

### **Visual Properties** — 颜色和不透明度的参数化设置 `Simple` (默认) | `Advanced`

用于指定视觉属性的参数化设置。选择 `Simple` 可指定漫反射颜色和不透明度。选择 `Advanced` 可指定更多视觉属性，如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Diffuse Color** — 图形颜色 [0.5 0.5 0.5] (默认) | three-element vector | four-element vector

在直接白光下图形的颜色，指定为 0–1 尺度上的 [R G B] 或 [R G B A] vector。可选的第四个元素 (A) 指定 0–1 尺度上的颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Opacity** — 图形不透明度 1.0 (默认) | scalar in the range of 0 to 1

图形不透明度，指定为 0 到 1 范围内的 scalar。scalar 为 0 对应于完全透明，scalar 为 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Simple`

### **Specular Color** — 高光颜色 [0.5 0.5 0.5 1.0] (默认) | three-element vector | four-element vector

镜面高光的颜色，指定为 0–1 尺度上的 [R,G,B] 或 [R,G,B,A] vector。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Ambient Color** — 阴影颜色 [0.15 0.15 0.15 1.0] (默认) | three-element vector | four-element vector

漫射环境光中阴影区域的颜色，指定为 0–1 尺度上的 [R,G,B] 或 [R,G,B,A] vector。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0] (默认) | three-element vector | four-element vector

因自发光而产生的图形颜色，指定为 0–1 尺度上的 [R,G,B] 或 [R,G,B,A] vector。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Shininess** — 高光锐度 75 (默认) | scalar in the range of 1 to 128

镜面光反射的锐度，指定为 0–128 尺度上的 scalar 数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

用于接触建模的网格曲面

Grid Surface 模块创建一个笛卡尔网格曲面，您可以使用它对接触问题进行建模。您可以对网格曲面与各种类型的几何体之间的接触进行建模。有关受支持的几何体，请参阅 Supported Geometries。此外，Grid Surface 模块支持 Custom Tire Force and Torque 和 Magic Formula Tire Force and Torque 模块。

必须使用网格曲面的正法向侧进行接触，即参考坐标系的正 *z* 轴所指向的一侧。否则，模块会将接触部件穿过曲面弹出到正侧。

网格曲面正法向侧的图示

网格曲面具有与 MATLAB® 中 `ndgrid` 函数生成的网格类似的格式。要对网格曲面建模，请使用 X Grid Vector 和 Y Grid Vector 参数指定网格曲面在 *x* 和 *y* 方向上的坐标，然后使用 Z Heights 参数指定网格点在 *z* 方向上的高程。您可以使用该模块创建表示正方形、矩形或非均匀网格的曲面。

网格类型

该图展示了 **Z Heights** 参数为 `[0 0 0.5 0.5; 0 0 0.5 0.5; 0 0 0 0; 0 0 0 0]` 的网格曲面示例。矩阵的列沿 *x-*axis 方向，矩阵的行沿 *y-*axis 方向。

网格参数

要使用 LiDAR 数据创建网格曲面，必须先在使用 Grid Surface 模块之前将散点数据转换为网格化数据。要转换数据，可以使用 `scatteredInterpolant` 对象，通过 LiDAR 数据的 *x*、*y* 和 *z* 值创建插值函数，创建表示网格域的 *x* 和 *y* 网格向量，然后将这些网格向量用作插值函数的查询点，以生成网格曲面的 *z* 值。生成的 *z* 值形成 `ndgrid` 格式的矩阵，可用于指定 **Z Heights** 参数。您也可以使用 `griddata` 函数为网格曲面生成 *z* 值，但需要将输出矩阵转置为 `ndgrid` 格式。

**注意**

为了获得最佳仿真性能，应使 *x* 和 *y* 网格向量中的间距尽可能大，同时又要足够小，以便以足够精度表示曲面。要更改网格向量的间距并计算相应的 *z* 值，请使用 `griddedInterpolant` 对象或 `interp2` 函数。

通常，在将 LiDAR 数据转换为网格化数据之前，需要清理 LiDAR 数据，例如去除离群值或 *NaN* 值。要清理数据，请使用 `isnan` 和 `isoutlier` 函数。
