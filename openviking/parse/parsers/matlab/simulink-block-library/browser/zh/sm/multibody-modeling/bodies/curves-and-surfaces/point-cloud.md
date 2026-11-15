---
type: simulink-block
title: 'Point Cloud'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Curves and Surfaces'
documentation_page: 'pointcloud'
documentation_source_path: 'ref/pointcloud.html'
language: zh-CN
chinese_source: worker-translation
---

# Point Cloud

## 端口

### 坐标系

### **R** — 局部参考坐标系 frame

点云参考坐标系。要指定点云的位置和方向，请将此坐标系连接到另一个模块。

### 几何

### **G** — 几何坐标系 frame

表示由该模块定义的点集的几何坐标系。要对这些点建模接触，请将此端口连接到 Spatial Contact Force 或 Planar Contact Force 模块。

## 参数

### **Coordinates Matrix** — 点的坐标 [0 0 0 ] `m`（默认）| *N*-by-2 矩阵 | *N*-by-3 矩阵

点的坐标，指定为 *N*-by-2 或 *N*-by-3 矩阵。

- 要创建二维点云，请使用 *N*-by-2 矩阵，该矩阵指定每个点相对于局部参考坐标系的 *x* 和 *y* 笛卡尔坐标。
- 要创建三维点云，请使用 *N*-by-3 矩阵，该矩阵指定每个点相对于局部参考坐标系的 *x*、*y* 和 *z* 笛卡尔坐标。

对接触建模时，对二维点云使用 Planar Contact Force 模块，对三维点云使用 Spatial Contact Force 模块。

**数据类型：** `double`

### 图形

### **Type** — 用于点云可视化的图形 `Marker Cloud`（默认）| `None`

用于可视化点云的图形。要从模型可视化中消除点云，请将此参数设置为 `None`。

### **Sphere Radius** — 标记半径 1e-2 `m`（默认）| 正标量

点云中每个点的标记半径。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker Cloud`。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定漫反射颜色和不透明度。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker Cloud`。

### **Diffuse Color** — 图形颜色 [0.5 0.5 0.5]（默认）| 三元素向量 | 四元素向量

直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值为 1。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker Cloud`。

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应于完全透明，标量 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker Cloud`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 高光颜色 [0.5 0.5 0.5 1.0]（默认）| 三元素向量 | 四元素向量

镜面高光的颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker Cloud`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 阴影颜色 [0.15 0.15 0.15 1.0]（默认）| 三元素向量 | 四元素向量

漫反射环境光中阴影区域的颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等效于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker Cloud`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 三元素向量 | 四元素向量

由于自发光而产生的图形颜色，指定为 0–1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。可选的第四个元素 (A) 指定颜色不透明度。省略不透明度元素等效于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker Cloud`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 0 到 128 范围内的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值会产生更小但更锐利的高光。减小该值会产生更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Marker Cloud`
2. **Visual Properties** 为 `Advanced`

## 所属库

Simscape / Multibody / Curves and Surfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

点云几何

Point Cloud 模块在空间中创建一组点。每个点相对于 Point Cloud 模块的参考坐标系都有一个刚性偏移。您可以使用 Point Cloud 模块为接触近似一个几何体，例如具有凹形的物体。在对某些持续和分布式接触问题进行建模时，Spatial Contact Force 模块使用 Point Cloud 模块可能比使用几何体模块（例如 Brick Solid 或 File Solid）表现更好。此图演示如何使用点云近似机器人脚底。

Point Cloud 示例

对点云的接触进行建模时，Spatial Contact Force 和 Planar Contact Force 模块将点云视为 *N* 点几何体的聚合，并独立地对每个点施加接触力。每个接触力基于点云中单个点的穿透量和速度。

您可以使用 *N*-by-2 或 *N*-by-3 矩阵创建二维或三维点云。矩阵的每一行指定一个点相对于 Point Cloud 模块参考坐标系的笛卡尔坐标。如果矩阵有任何重复行，则会发生错误。

**提示**

您可以使用 `unique` 函数从输入矩阵中删除重复行。
