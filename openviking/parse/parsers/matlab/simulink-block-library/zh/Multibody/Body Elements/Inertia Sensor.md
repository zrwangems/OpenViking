---
type: simulink-block
title: 'Inertia Sensor'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'inertiasensor'
documentation_source_path: 'ref/inertiasensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Inertia Sensor

## 端口
```yaml
ports:
- name: S
  summary: 传感器端口坐标系
  direction: input
- name: M
  summary: 自定义测量坐标系端口坐标系
  direction: input
- name: m
  summary: 质量标量
  direction: output
- name: com
  summary: 质心向量
  direction: output
- name: I
  summary: 惯性矩阵矩阵
  direction: output
- name: Ic
  summary: 中心惯性矩阵矩阵
  direction: output
- name: Ip
  summary: 主惯性矩阵矩阵
  direction: output
- name: R
  summary: 旋转矩阵矩阵
  direction: output
```

### 输入

### **S** — 传感器端口坐标系

用于连接到模型中坐标系的传感器端口。使用此端口可确定所测量的是哪个体组或机构。

### **M** — 自定义测量坐标系端口坐标系

当选择 `Custom` 时，Inertia Sensor 模块上会出现第二个端口 M。Inertia Sensor 模块测量相对于连接到 M 端口的坐标系的惯性属性。

#### 依赖关系

要启用此端口，请将 **Measurement Frame** 参数设置为 `Custom`。

### 输出

### **m** — 质量标量

体单元集合的总质量。

#### 依赖关系

要启用此端口，请选中 **Mass** 复选框。

### **com** — 质心向量

体单元集合的质心。

#### 依赖关系

要启用此端口，请选中 **Center of Mass** 复选框。

### **I** — 惯性矩阵矩阵

体单元集合的惯性矩阵。

#### 依赖关系

要启用此端口，请选中 **Inertia Matrix** 复选框。

### **Ic** — 中心惯性矩阵矩阵

体单元集合的中心惯性矩阵。

#### 依赖关系

要启用此端口，请选中 **Centered Inertia Matrix** 复选框。

### **Ip** — 主惯性矩阵矩阵

体单元集合的主惯性矩阵。

#### 依赖关系

要启用此端口，请选中 **Principal Inertia Matrix** 复选框。

### **R** — 旋转矩阵矩阵

主惯性坐标系相对于测量坐标系的姿态旋转矩阵。

#### 依赖关系

要启用此端口，请选中 **Rotation Matrix** 复选框。
## 参数
```yaml
parameters:
- name: Sensor Extent
  summary: 确定 Inertia Sensor 模块测量的范围 Body Group（默认）| Mechanism
  group: 传感器范围
- name: 'Sensor Extent: Span Weld Joints'
  summary: 在体组中包含通过焊接关节连接的体 cleared（默认）| 选中
  group: 传感器范围
- name: 'Sensor Extent: Exclude Grounded Bodies'
  summary: 不测量接地体的惯性属性 cleared（默认）| 选中
  group: 传感器范围
- name: Measurement Frame
  summary: 确定 Inertia Sensor 模块用于测量的坐标系 Attached（默认）| World | Custom
  group: 传感器范围
- name: Mass
  summary: 所测量体的总质量 cleared（默认）| 选中
  group: 传感器范围
- name: Center of Mass
  summary: 质心坐标 cleared（默认）| checked
  group: 传感器范围
- name: Inertia Matrix
  summary: 惯性张量的测量 cleared（默认）| checked
  group: 传感器范围
- name: Centered Inertia Matrix
  summary: 相对于中心坐标系的惯性张量的测量 cleared（默认）| checked
  group: 传感器范围
- name: Principal Inertia Matrix
  summary: 相对于主惯性坐标系的惯性张量的测量 cleared（默认）| checked
  group: 传感器范围
- name: Rotation Matrix
  summary: 主惯性坐标系的姿态 cleared（默认）| checked
  group: 传感器范围
- name: Type
  summary: 传感器可视化设置 Principal Inertia Frame（默认）| Equivalent Inertia Ellipsoid | None
  group: Graphic
- name: Size
  summary: 主惯性坐标系的显示大小 20 pixels（默认）| 正标量
  group: Graphic
- name: Visual Properties
  summary: 颜色和不透明度的参数化 Simple（默认）| Advanced
  group: Graphic
- name: 漫反射颜色
  summary: 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: 不透明度
  summary: 图形不透明度 1.0（默认）| 取值范围为 0 到 1 的标量
  group: Graphic
- name: 镜面反射颜色
  summary: 镜面反射产生的光的颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: 环境光颜色
  summary: 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: 自发光颜色
  summary: 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量
  group: Graphic
- name: Shininess
  summary: 高光锐度 75（默认）| 取值范围约束为 0–128 的标量
  group: Graphic
```

### 传感器范围

### **Sensor Extent** — 确定 Inertia Sensor 模块测量的范围 `Body Group`（默认）| `Mechanism`

Inertia Sensor 模块测量的范围，定义为 Body Group 或 Mechanism。

`Body Group`
:   当选择 `Body Group` 时，Inertia Sensor 模块测量彼此直接连接或通过刚性变换连接的体单元集合的惯性属性。这包括实体、惯性、变质量或柔性体。

`Mechanism`
:   当选择 `Mechanism` 时，Inertia Sensor 模块测量模型中所有已连接体单元的惯性属性。

### **Sensor Extent: Span Weld Joints** — 在体组中包含通过焊接关节连接的体 `cleared`（默认）| 选中

如果选中，此选项将使体组包含通过焊接关节连接的体单元。

#### 依赖关系

要启用此选项，请将 **Sensor Extent** 设置为 `Body Group`。

### **Sensor Extent: Exclude Grounded Bodies** — 不测量接地体的惯性属性 `cleared`（默认）| 选中

如果选中，此选项将使 Inertia Sensor 模块测量与 Inertia Sensor 模块连接到同一机构的体单元集合的惯性属性，但不包括任何接地体。

#### 依赖关系

要启用此选项，请将 **Sensor Extent** 设置为 `Mechanism`。

### **Measurement Frame** — 确定 Inertia Sensor 模块用于测量的坐标系 `Attached`（默认）| `World` | `Custom`

测量坐标系指定传感器用于测量质心、惯性矩阵和中心惯性矩阵的坐标系。

`Attached`
:   当选择 `Attached` 时，Inertia Sensor 模块测量相对于连接到 S 端口的同一坐标系的惯性属性。

`World`
:   当选择 `World` 时，Inertia Sensor 模块测量相对于 World Frame 的惯性属性。

`Custom`
:   当选择 `Custom` 时，M 端口会暴露出来。Inertia Sensor 模块测量相对于连接到 M 端口的坐标系的惯性属性。

### **Mass** — 所测量体的总质量 `cleared`（默认）| 选中

选中 **Mass** 复选框以测量体单元集合的质量。

### **Center of Mass** — 质心坐标 `cleared`（默认）| checked

选中 **Center of Mass** 复选框以测量体元素集合的质心，输出为相对于测量坐标系的 3×1 向量。如果被测体组或机构的质量为零，则质心未定义，并会发生运行时错误。

### **Inertia Matrix** — 惯性张量的测量 `cleared`（默认）| checked

选中 **Inertia Matrix** 复选框以测量体元素集合的惯性张量，输出为相对于测量坐标系的 3×3 矩阵。

### **Centered Inertia Matrix** — 相对于中心坐标系的惯性张量的测量 `cleared`（默认）| checked

选中 **Centered Inertia Matrix** 复选框以测量体元素集合的惯性张量，输出为相对于中心坐标系的 3×3 矩阵。中心坐标系是其原点与质心重合且其坐标轴与测量坐标系坐标轴对齐的坐标系。如果被测体组或机构的质量为零，则中心惯性矩阵未定义，并会发生运行时错误。

### **Principal Inertia Matrix** — 相对于主惯性坐标系的惯性张量的测量 `cleared`（默认）| checked

选中 **Principal Inertia Matrix** 复选框以测量体元素集合的惯性张量，输出为相对于主惯性坐标系的 3×3 矩阵。主惯性矩阵是对角矩阵。

主惯性坐标系是其原点与质心重合且其坐标轴与主惯性轴对齐的坐标系。如果被测体组或机构的质量为零，则主惯性矩阵未定义，并会发生运行时错误。

### **Rotation Matrix** — 主惯性坐标系的姿态 `cleared`（默认）| checked

选中 **Rotation Matrix** 复选框以测量主惯性轴相对于测量坐标系的姿态，输出为 3×3 矩阵。换言之，旋转矩阵将主惯性坐标系中的向量映射到测量坐标系中的向量。

如果被测体组或机构的质量为零，则旋转矩阵未定义，并会发生运行时错误。

### Graphic

### **Type** — 传感器可视化设置 `Principal Inertia Frame`（默认）| `Equivalent Inertia Ellipsoid` | `None`

所感测体元素集合的惯性属性的显示，指定为 `Principal Inertia Frame`、`Equivalent Inertia Ellipsoid` 或 `None`。

将参数设置为 `Principal Inertia Frame`，以将所感测的惯性属性表示为主惯性坐标系。主惯性坐标系是其原点与质心重合且其坐标轴与主惯性轴对齐的坐标系。

将参数设置为 `Equivalent Inertia Ellipsoid`，以将惯性属性表示为椭球体，该椭球体具有与被感测体组相同的质量、惯性矩和惯性积。

将参数设置为 `None`，以隐藏所感测惯性属性的可视化。

### **Size** — 主惯性坐标系的显示大小 20 `pixels`（默认）| 正标量

主惯性坐标系的显示大小，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Principal Inertia Frame`。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Principal Inertia Frame` 或 `Equivalent Inertia Ellipsoid`。

### **漫反射颜色** — 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

漫反射产生的光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

漫反射颜色反映图形的主色，并提供着色，使渲染对象呈现三维外观。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Principal Inertia Frame` 或 `Equivalent Inertia Ellipsoid`。

### **不透明度** — 图形不透明度 1.0（默认）| 取值范围为 0 到 1 的标量

图形不透明度，指定为取值范围为 0 到 1 的标量。标量为 0 对应完全透明，标量为 1 对应完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Principal Inertia Frame` 或 `Equivalent Inertia Ellipsoid`
2. **Visual Properties** 为 `Simple`

### **镜面反射颜色** — 镜面反射产生的光的颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

镜面反射产生的光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。此参数改变镜面高光的颜色，镜面高光是由于光源的光反射而在图形上形成的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Principal Inertia Frame` 或 `Equivalent Inertia Ellipsoid`
2. **Visual Properties** 为 `Advanced`

### **环境光颜色** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

环境光是指并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射以至于不再来自任何特定方向的光组成。您可以调整此参数以改变图形的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Principal Inertia Frame` 或 `Equivalent Inertia Ellipsoid`
2. **Visual Properties** 为 `Advanced`

### **自发光颜色** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

自发光颜色是不来自任何外部光源的颜色，因此看起来是由图形自身发出的。当图形具有自发光颜色时，即使没有外部光源，图形也可见。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Principal Inertia Frame` 或 `Equivalent Inertia Ellipsoid`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 取值范围约束为 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Principal Inertia
   Frame` 或 `Equivalent Inertia
   Ellipsoid`
2. **Visual Properties** 为
   `Advanced`
## 所属库

Simscape / Multibody / Body Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

用于测量体组或机构惯性特性的传感器

使用 Inertia Sensor 模块测量 Simscape Multibody 模型中体元素集合的惯性特性。Inertia Sensor 模块可以测量的参数包括：

- 质量
- 质心
- 惯性矩阵
- 中心惯性矩阵
- 主惯性矩阵
- 主惯性坐标系的方向

体组是直接相连或通过刚性变换相连的所有体元素的集合。体组可以包括固体模块、惯性模块、变质量模块或柔性体模块。默认情况下，通过关节模块连接的两个体元素不被视为同一体组的一部分。

机构是模型中所有相连体元素的集合。对于机构，您可以通过启用 **Exclude Grounded Bodies** 参数来选择排除接地体。接地体是任何刚性连接到 World Frame 模块的刚体。
