---
type: simulink-block
title: 'Variable Spherical Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Variable Mass'
documentation_page: 'variablesphericalsolid'
documentation_source_path: 'ref/variablesphericalsolid.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Spherical Solid

## 端口
```yaml
ports:
- name: R
  summary: 参考坐标系 frame
  direction: unspecified
- name: r
  summary: 球体半径 physical signal
  direction: unspecified
- name: m
  summary: 球体质量 physical signal
  direction: unspecified
- name: r
  summary: 球体半径 physical signal
  direction: unspecified
- name: m
  summary: 球体质量 physical signal
  direction: unspecified
- name: com
  summary: 球体质心坐标 physical signal
  direction: unspecified
- name: I
  summary: 球体惯性矩阵 physical signal
  direction: unspecified
```

### 坐标系

### **R** — 参考坐标系 frame

实体的局部参考坐标系。该坐标系相对于实体几何形状固定。坐标系原点位于几何中心。将此端口连接到坐标系实体——端口、线或节点——以在模型中解析坐标系的位置。有关详细信息，请参阅Working with Frames。
### 物理信号输入

### **r** — 球体半径 physical signal

球体半径的输入端口。

### **m** — 球体质量 physical signal

球体质量的输入端口。
### 物理信号输出

### **r** — 球体半径 physical signal

球体半径的输出端口。

### **m** — 球体质量 physical signal

球体质量的输出端口。

### **com** — 球体质心坐标 physical signal

球体质心的输出端口，以三元素向量形式报告，其笛卡尔坐标在实体的参考坐标系中解析。

### **I** — 球体惯性矩阵 physical signal

球体惯性矩阵的输出端口，以九元素矩阵形式报告，在实体的惯性解析坐标系中解析——惯性解析坐标系是参考坐标系的虚拟副本，其原点已移至质心。惯性解析坐标系的坐标轴与参考坐标系的坐标轴平行。矩阵的对角元素为惯性矩，非对角元素为惯性积。
## 参数
```yaml
parameters:
- name: Radius
  summary: 半径参数化方式 Calculate from Mass（默认）| Constant | Provided by Input
  group: ''
- name: 'Radius: Value'
  summary: 半径值 1 m（默认）| 带长度单位的标量
  group: ''
- name: Mass
  summary: 质量参数化方式 Provided by Input（默认）| Calculate from Geometry
  group: ''
- name: 'Mass: Density'
  summary: 材料单位体积质量 1000 kg/m^3（默认）| 以质量每单位体积为单位的标量
  group: ''
- name: Radius
  summary: 半径的传感选择 未选中（默认）| 已选中
  group: ''
- name: Mass
  summary: 总质量传感选择 清除（默认）| 选中
  group: ''
- name: Center of Mass
  summary: 质心坐标传感选择 清除（默认）| 选中
  group: ''
- name: Inertia Matrix
  summary: 惯性矩阵传感选项 清除（默认）| 选中
  group: ''
- name: Type
  summary: 用于可视化的图形 From Geometry（默认）| Marker | None
  group: Graphic
- name: Visual Properties
  summary: 颜色和不透明度的参数化 Simple（默认）| Advanced
  group: Graphic
- name: Shape
  summary: 用于表示固体的标记形状 Sphere（默认）| Cube | Frame
  group: Graphic
- name: Size
  summary: 标记的宽度（以像素为单位） 10 pixels（默认）| 标量
  group: Graphic
- name: Diffuse Color
  summary: 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量
  group: Graphic
- name: Opacity
  summary: 图形不透明度 1.0（默认）| 0 到 1 范围内的标量
  group: Graphic
- name: Specular Color
  summary: 镜面反射产生的光线颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: Ambient Color
  summary: 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: Emissive Color
  summary: 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量
  group: Graphic
- name: Shininess
  summary: 高光锐度 75（默认）| 取值范围约束为 0–128 的标量
  group: Graphic
```

#### 几何与惯性

### **Radius** — 半径参数化方式 `Calculate from Mass`（默认）| `Constant` | `Provided by Input`

实体半径的参数化方式。选择 `Constant` 以将固定值指定为模块参数。选择 `Provided by Input` 以将可变值指定为物理信号输入。使用默认设置（`Calculated from Mass`）从指定的实体密度和其余尺寸获取此参数。选择 `Provided by Input` 将显示一个新的物理信号输入端口，标记为 **r**，通过该端口指定可变值。

### **Radius: Value** — 半径值 `1 m`（默认）| 带长度单位的标量

实体的半径。实体的纵轴与局部参考坐标系的 *z* 轴对齐。当此模块参数激活时，*z* 维度为常量。

#### 参数依赖关系

当 **Radius** 参数设置为 `Constant` 时，此参数激活。

### **Mass** — 质量参数化方式 `Provided by Input`（默认）| `Calculate from Geometry`

实体质量的参数化方式。选择 `Calculate from Geometry` 从指定的实体密度和尺寸获取此参数。使用默认设置（`Provided by Input`）将此参数直接指定为时变物理信号。此选项将显示一个新的物理信号输入端口，标记为 **M**，通过该端口指定时变实体质量。

### **Mass: Density** — 材料单位体积质量 `1000 kg/m^3`（默认）| 以质量每单位体积为单位的标量

材料单位体积质量。质量密度可以取正值或负值。指定负质量密度以模拟实体中空洞或空腔的影响。默认值 `1000 kg/m^3` 是 ABS 塑料等聚合物的典型值。

#### 参数依赖关系

当 **Mass** 参数设置为 `Calculate from Geometry` 时，此参数激活。

#### 传感

### **Radius** — 半径的传感选择 未选中（默认）| 已选中

实体半径的传感选择。选中以显示一个新的物理信号输出端口，标记为 **r**，通过该端口输出半径的时变值。

### **Mass** — 总质量传感选择 清除（默认）| 选中

固体总质量的传感选择。选中以暴露一个新的物理信号输出端口，标记为 **m**，通过该端口输出固体质量随时间变化的值。

### **Center of Mass** — 质心坐标传感选择 清除（默认）| 选中

固体质心坐标的传感选择。选中以暴露一个新的物理信号输出端口，标记为 **com**，通过该端口输出随时间变化的坐标。输出是一个三元素向量，其笛卡尔坐标在固体的参考坐标系中解析。

### **Inertia Matrix** — 惯性矩阵传感选项 清除（默认）| 选中

固体惯性矩阵的传感选择。选中以暴露一个新的物理信号输出端口，标记为 **I**，通过该端口输出随时间变化的惯性矩阵。输出是一个九元素矩阵，对角线位置为惯性矩，非对角线位置为惯性积。惯性矩和惯性积在惯性解析坐标系中解析——该坐标系的轴与参考坐标系的轴平行，但原点位于质心。

### Graphic

### **Type** — 用于可视化的图形 `From Geometry`（默认）| `Marker` | `None`

固体的视觉表示类型，指定为 `From Geometry`、`Marker` 或 `None`。将参数设置为 `From Geometry` 以显示固体的视觉表示。将参数设置为 `Marker` 以将固体表示为标记。将参数设置为 `None` 以在模型可视化中隐藏固体。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Shape** — 用于表示固体的标记形状 `Sphere`（默认）| `Cube` | `Frame`

用于可视化固体的标记形状。标记的运动反映固体本身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记的宽度（以像素为单位） 10 `pixels`（默认）| 标量

标记的宽度（以像素为单位）。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，较高分辨率每单位长度包含更多像素，因此产生更小的图标。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Diffuse Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

漫反射光的颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

漫反射颜色反映渲染固体的主色，并提供着色，使渲染对象具有三维外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应完全透明，标量 1 对应完全不透明。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Simple`

### **Specular Color** — 镜面反射产生的光线颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

镜面反射产生的光线颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。此参数改变镜面高光的颜色，镜面高光是由于光源的光线反射而在渲染实体上出现的亮点。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

环境光是指并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射以至于不再来自任何特定方向的光组成。您可以调整此参数来改变渲染实体的阴影颜色。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

发射颜色是不来自任何外部光源的颜色，因此看起来是由实体自身发出的。当实体具有发射颜色时，即使没有外部光源，实体也能被看到。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Shininess** — 高光锐度 75（默认）| 取值范围约束为 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大光泽度值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`
## 所属库

Simscape / Multibody / Body Elements / Variable Mass

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

具有可变质量和尺寸的实心球体

Variable Spherical Solid 模块向所连接的坐标系中添加一个具有可变质量和尺寸的实心球体。球体的质量和半径可以各自为常量或随时间变化。可变物理量可以直接指定为物理信号，也可以作为其余物理量的函数进行计算。在仿真期间，只能计算质量或半径中的一个物理量。

参考坐标系编码了实体相对于模型中其他组件的位置和方向。该坐标系相对于实体几何体定义，使其原点位于球体中心。此关系在仿真期间保持不变。半径相对于坐标系原点在所有方向上对称增大。

**由质量计算半径的可变球体**

可视化是动态的。实体尺寸在 Multibody Explorer 的可视化窗格中随其变化而连续更新。实体的初始尺寸取决于您指定的参数和物理信号。可变尺寸可能以零值开始——例如，如果它派生自初始值也为零的物理信号。

密度本身可以是常量或变量。如果在仿真期间计算质量或半径中的任一个，则该物理量被指定为常量。如果质量和半径均被显式指定（无论是作为（常量）模块参数还是作为物理信号），则密度被计算为变量。与实体模块的情况一样，您可以指定负密度，例如，用于对复合体中的空隙进行建模。
