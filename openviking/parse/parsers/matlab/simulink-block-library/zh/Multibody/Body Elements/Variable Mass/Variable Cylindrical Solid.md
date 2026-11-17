---
type: simulink-block
title: 'Variable Cylindrical Solid'
family: 'body-elements'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Variable Mass'
documentation_page: 'variablecylindricalsolid'
documentation_source_path: 'ref/variablecylindricalsolid.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Cylindrical Solid

## 端口

### 坐标系

### **R** — 参考坐标系 frame

固体的局部参考坐标系。此坐标系相对于固体几何固定。坐标系原点位于 *xy* 平面上 *xy* 横截面的中心。*z* 轴与圆柱体的纵轴对齐。将此端口连接到 frame 实体——端口、线或节点——以解析模型中的 frame 放置。有关详细信息，请参阅 Working with Frames。

### 物理信号输入

### **len** — 圆柱长度 physical signal

圆柱长度的输入端口。

### **r** — 圆柱半径 physical signal

圆柱半径的输入端口。

### **m** — 圆柱质量 physical signal

圆柱质量的输入端口。

### 物理信号输出

### **len** — 圆柱长度 physical signal

圆柱长度的输出端口。

### **r** — 圆柱半径 physical signal

圆柱半径的输出端口。

### **m** — 圆柱质量 physical signal

圆柱质量的输出端口。

### **com** — 圆柱的质心坐标 physical signal

圆柱质心的输出端口，报告为三元素向量，其笛卡尔坐标在固体的参考坐标系中解析。

### **I** — 圆柱的惯性矩阵 physical signal

圆柱惯性矩阵的输出端口，报告为九元素矩阵，在模块的参考坐标系中解析。矩阵的对角元素是惯性矩。非对角元素是惯性积。

## 参数

#### 几何与惯性

### **Radius** — 半径参数化 `Calculate from Mass` (default) | `Constant` | `Provided by Input`

固体半径的参数化。选择 `Constant` 可将固定值指定为模块参数。选择 `Provided by Input` 可将可变值指定为 physical signal 输入。使用默认设置（`Calculated from Mass`）可根据指定的固体密度和剩余尺寸获取此参数。选择 `Provided by Input` 会显示一个新的 physical signal 输入端口，标记为 **r**，通过该端口指定可变值。

### **Radius: Value** — 半径的值 `1 m` (default) | scalar with units of length

固体的半径。固体的纵轴与局部参考坐标系的 *z* 轴对齐。当此模块参数处于活动状态时，*z* 尺寸为常量。

#### 参数依赖关系

当 **Radius** 参数设置为 `Constant` 时，此参数处于活动状态。

### **Length** — 长度参数化 `Calculate from Mass` (default) | `Constant` | `Provided by Input`

固体长度的参数化。选择 `Constant` 可将固定值指定为模块参数。选择 `Provided by Input` 可将可变值指定为 physical signal 输入。使用默认设置（`Calculated from Mass`）可根据指定的固体密度和剩余尺寸获取此参数。选择 `Provided by Input` 会显示一个新的 physical signal 输入端口，标记为 **len**，通过该端口指定可变值。

### **Length: Value** — 长度的值 `1 m` (default) | scalar with units of length

固体的长度。圆柱体的纵轴与局部参考坐标系的 *z* 轴对齐。当此模块参数处于活动状态时，*z* 尺寸为常量。

#### 参数依赖关系

当 **Length** 参数设置为 `Constant` 时，此参数处于活动状态。

### **Mass** — 质量参数化 `Provided by Input` (default) | `Calculate from Geometry`

固体质量的参数化。选择 `Calculate from Geometry` 可根据指定的固体密度和尺寸获取此参数。使用默认设置（`Provided by Input`）可直接将此参数指定为时变 physical signal。此选项会显示一个新的 physical signal 输入端口，标记为 **M**，通过该端口指定时变固体质量。

### **Mass: Density** — 材料的每单位体积质量 `1000 kg/m^3` (default) | scalar in units of mass per unit volume

材料的每单位体积质量。质量密度可采用正值或负值。指定负质量密度可对固体主体中的空隙或空腔效应进行建模。默认值 `1000 kg/m^3` 是聚合物（如 ABS 塑料）的典型值。

#### 参数依赖关系

当 **Mass** 参数设置为 `Calculate from Geometry` 时，此参数处于活动状态。

#### 感测

### **Radius** — 半径的感测选择 cleared (default) | checked

固体半径的感测选择。选中可显示一个新的 physical signal 输出端口，标记为 **r**，通过该端口输出半径的时变值。

### **Length** — 长度的感测选择 cleared (default) | checked

固体 *z* 尺寸的感测选择。选中可显示一个新的 physical signal 输出端口，标记为 **len**，通过该端口输出长度的时变值。

### **Mass** — 总质量的感测选择 cleared (default) | checked

固体总质量的感测选择。选中可显示一个新的 physical signal 输出端口，标记为 **m**，通过该端口输出固体质量的时变值。

### **Center of Mass** — 质心坐标的感测选择 cleared (default) | checked

固体质心坐标的感测选择。选中可显示一个新的 physical signal 输出端口，标记为 **com**，通过该端口输出时变坐标。输出是一个三元素向量，其中笛卡尔坐标在固体的参考坐标系中解析。

### **Inertia Matrix** — 惯性矩阵的感测选项 cleared (default) | checked

固体惯性矩阵的感测选择。选中可显示一个新的 physical signal 输出端口，标记为 **I**，通过该端口输出时变惯性矩阵。输出是一个九元素矩阵，对角线位置为惯性矩，非对角线位置为惯性积。惯性矩和惯性积在惯性解析坐标系中解析——该坐标系的轴与参考坐标系的轴平行，但原点位于质心。

### 图形

### **Type** — 用于可视化的图形 `From Geometry` (default) | `Marker` | `None`

固体的可视表示类型，指定为 `From Geometry`、`Marker` 或 `None`。将参数设置为 `From Geometry` 可显示固体的可视表示。将参数设置为 `Marker` 可将固体表示为标记。将参数设置为 `None` 可在模型可视化中隐藏固体。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple` (default) | `Advanced`

用于指定可视属性的参数化。选择 `Simple` 可指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 可指定更多可视属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Shape** — 用于表示固体的标记形状 `Sphere` (default) | `Cube` | `Frame`

用于可视化固体的标记形状。标记的运动反映固体本身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记的宽度（以像素为单位） 10 `pixels` (default) | scalar

标记的宽度（以像素为单位）。此宽度不随缩放级别缩放。请注意，标记的表观尺寸部分取决于屏幕分辨率，较高分辨率每单位长度包含更多像素，因此会产生更小的图标。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Diffuse Color** — 漫反射产生的光颜色 [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

漫反射产生的光颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，其值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

漫反射颜色反映渲染固体的主色，并提供阴影，使渲染对象具有三维外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Opacity** — 图形不透明度 1.0 (default) | scalar in the range of 0 to 1

图形不透明度，指定为 0 到 1 范围内的 scalar。scalar 0 对应完全透明，scalar 1 对应完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Specular Color** — 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

镜面反射产生的光颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，其值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数更改镜面高光的颜色，镜面高光是渲染固体上由于光源光线反射而产生的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

环境光颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，其值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光指并非直接来自光源的一般照明水平。环境光由已经反射和再反射多次、不再来自任何特定方向的光组成。您可以调整此参数以更改渲染固体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

由于自发光而产生的颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，其值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部源的颜色，因此似乎由固体本身发射。当固体具有发射颜色时，即使没有外部光源，也可以看到该固体。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75 (default) | scalar with value constrained to 0–128

镜面光反射的锐度，指定为 0–128 范围内的 scalar 数字。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

## 所属库

Simscape / Multibody / Body Elements / Variable Mass

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

可变质量和尺寸的实心圆柱体

Variable Cylindrical Solid 模块会向所连接的坐标系添加一个具有可变质量和尺寸的实心圆柱体。圆柱体的质量、半径和长度均可为常量或随时间变化。可变数量可直接指定为 physical signal，也可作为其余数量的函数计算。质量或圆柱体尺寸可在仿真期间计算，但不能同时计算两者。

参考坐标系编码模型中固体的位置和方向。该坐标系固定到固体，坐标系原点位于下表面的中心（按照 `Z up` 视图约定观察）。此放置在整个仿真过程中保持不变。长度相对于下表面沿 *z*-轴正方向非对称增加。

**长度由质量计算的可变圆柱体**

可视化是动态的。固体尺寸在其发生时连续更新，位于 Multibody Explorer 的可视化窗格中。固体的初始尺寸取决于您指定的参数和 physical signals。可变尺寸可能以零值开始——例如，如果它派生自初始值也为零的 physical signal。

密度本身可以是常量或变量。如果至少一个固体参数在仿真期间计算，则此数量指定为常量。如果所有固体参数都显式指定，作为（常量）模块参数或 physical signals，则它作为变量计算。与固体模块一样，您可以指定负密度，例如，用于对复合体中的空隙进行建模。
