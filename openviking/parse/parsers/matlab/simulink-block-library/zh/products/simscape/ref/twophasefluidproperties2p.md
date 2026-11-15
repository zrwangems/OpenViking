---
type: simulink-block
title: 'Two-Phase Fluid Properties (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Utilities'
documentation_page: 'twophasefluidproperties2p'
documentation_source_path: 'ref/twophasefluidproperties2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Phase Fluid Properties (2P)

## 端口

### 守恒

### **A** — 两相流体连接端口

守恒端口，用于将模块连接到两相流体网络。您可以将其连接到框图中两相流体连接管线上的任意点。当您将 Two-Phase Fluid Properties (2P) 模块连接到连接管线时，软件会自动识别连接到特定回路的两相流体模块，并将属性传播到所有这些模块。

## 参数

### 参数

### **Minimum valid specific internal energy** — 允许的最低比内能 `0 kJ/kg`（默认）| nonnegative scalar

两相流体网络中允许的最低比内能。

### **Maximum valid specific internal energy** — 允许的最高比内能 `4000 kJ/kg`（默认）| nonnegative scalar

两相流体网络中允许的最高比内能。

### **Pressure vector** — 用于表查找的压力值向量 vector

长度为 *N* 的向量，包含与流体属性表的列对应的压力值。

默认向量是从 1e-3 到 100 MPa 的对数间隔 100 元素向量，涵盖流体的亚临界和超临界区域。

### **Critical pressure** — 液体和蒸气不再作为不同相存在的压力 `22.0640 MPa`（默认）| positive scalar

液体和蒸气不再作为不同相存在的压力。将此参数设置为 `inf`，以对始终为亚临界的流体建模。

### **Thermal transport properties near critical point** — 是否裁剪临界点附近热输运属性的峰值 `Clip peak values`（默认）| `Do not clip peak values`

选择是否裁剪临界点附近热输运属性的峰值：

- `Clip peak values` ― 如果峰值尖锐且大，则裁剪它们以避免仿真期间的数值问题。使用 **Fraction above and below Critical pressure for clipping** 参数指定裁剪区域的宽度。
- `Do not clip peak values` ― 保留热输运属性不变。

### **Fraction above and below Critical pressure for clipping** — 用于裁剪热输运属性峰值的压力范围 `0.12`（默认）| positive scalar

临界压力上方和下方的压力范围，以分数表示，用于裁剪热输运属性的峰值。

#### 依赖关系

要启用此参数，请将 **Thermal transport properties near critical point** 设置为 `Clip peak values`。

### **Atmospheric pressure** — 环境的绝对压力 `0.101325 MPa`（默认）| positive scalar

环境的绝对压力。

### **Pressure and specific internal energy outside valid range** — 是否在压力或比内能超出有效范围时通知 `Error`（默认）| `Warning` | `None`

选择仿真期间湿空气压力或温度超出有效范围时会发生什么：

- `None` ― 如果属性超出范围，模块不返回错误。
- `Warning` ― 模块发出警告，但继续仿真。
- `Error` ― 模块返回错误并停止仿真。

### **Dynamic pressure threshold for flow reversal** — 流动开始反向时的动态压力 `0.01 Pa`（默认）| positive scalar

端口处流动开始反向时的动态压力。动态压力是总压力与静态压力之差。将此参数视为平滑流动反向的一种方式。较大的值对应更平滑的反向，较小的值对应更急剧的反向。

两相流体域使用迎风格式，该格式从端口紧邻上游的值推导端口处的流量。在流动反向期间，流量值的来源会突然变化，流量可能会变得不连续。为防止不连续并提高仿真稳健性，流动反向会被平滑处理，动态压力阈值标记平滑过渡的开始。

### 液体属性

### **Normalized liquid internal energy vector** — 用于表查找的归一化液体内能值向量 vector

长度为 *M*L 的向量，包含与液体属性表的行对应的归一化内能值。该向量必须从 `-1` 开始，并以 `0` 结束（饱和液体状态）。

默认是均匀间隔的 25 元素向量。

### **Liquid specific volume table** — 用于表查找的液体比容值矩阵 matrix

*M*L × *N* 矩阵，包含与归一化液体内能向量和压力向量对应的液体比容值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Vapor specific volume table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Liquid specific entropy table** — 用于表查找的液体比熵值矩阵 matrix

*M*L × *N* 矩阵，包含与归一化液体内能向量和压力向量对应的液体比熵值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Vapor specific entropy table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Liquid temperature table** — 用于表查找的液体温度值矩阵 matrix

*M*L × *N* 矩阵，包含与归一化液体内能向量和压力向量对应的液体温度值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Vapor temperature table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Liquid kinematic viscosity table** — 用于表查找的液体运动黏度值矩阵 matrix

*M*L × *N* 矩阵，包含与归一化液体内能向量和压力向量对应的液体运动黏度值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Vapor kinematic viscosity table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Liquid thermal conductivity table** — 用于表查找的液体热导率值矩阵 matrix

*M*L × *N* 矩阵，包含与归一化液体内能向量和压力向量对应的液体热导率值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Vapor thermal conductivity table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Liquid Prandtl number table** — 用于表查找的液体 Prandtl 数值矩阵 matrix

*M*L × *N* 矩阵，包含与归一化液体内能向量和压力向量对应的液体 Prandtl 数值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Vapor Prandtl number table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Saturated liquid internal energy vector** — 用于表查找的饱和液体内能值向量 vector

长度为 *N* 的向量，包含与压力向量对应的饱和液体比内能值。处于或高于临界压力处的元素必须与其在 **Saturated vapor specific internal energy vector** 模块参数中的对应元素相等。

默认是水的 100 元素向量。

### 蒸气属性

### **Normalized vapor internal energy vector** — 用于表查找的归一化蒸气内能值向量 vector

长度为 *M*V 的向量，包含与蒸气属性表的行对应的归一化内能值。该向量必须从 `1` 开始（饱和蒸气状态），并以 `2` 结束。

默认是均匀间隔的 25 元素向量。

### **Vapor specific volume table** — 用于表查找的蒸气比容值矩阵 matrix

*M*V × *N* 矩阵，包含与归一化蒸气内能向量和压力向量对应的蒸气比容值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Liquid specific volume table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Vapor specific entropy table** — 用于表查找的蒸气比熵值矩阵 matrix

*M*V × *N* 矩阵，包含与归一化蒸气内能向量和压力向量对应的蒸气比熵值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Liquid specific entropy table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Vapor temperature table** — 用于表查找的蒸气温度值矩阵 matrix

*M*V × *N* 矩阵，包含与归一化蒸气内能向量和压力向量对应的蒸气温度值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Liquid temperature table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Vapor kinematic viscosity table** — 用于表查找的蒸气运动黏度值矩阵 matrix

*M*V × *N* 矩阵，包含与归一化蒸气内能向量和压力向量对应的蒸气运动黏度值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Liquid kinematic viscosity table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Vapor thermal conductivity table** — 用于表查找的蒸气热导率值矩阵 matrix

*M*V × *N* 矩阵，包含与归一化蒸气内能向量和压力向量对应的蒸气热导率值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Liquid thermal conductivity table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Vapor Prandtl number table** — 用于表查找的蒸气 Prandtl 数值矩阵 matrix

*M*V × *N* 矩阵，包含与归一化蒸气内能向量和压力向量对应的蒸气 Prandtl 数值。饱和边界处以及处于或高于临界压力处的元素必须与其在 **Liquid Prandtl number table** 参数中的对应元素相等。

默认矩阵是水的 25 × 100 表。

### **Saturated vapor internal energy vector** — 用于表查找的饱和蒸气内能值向量 vector

长度为 *N* 的向量，包含与压力向量对应的饱和蒸气比内能值。处于或高于临界压力处的元素必须与其在 **Saturated liquid specific internal energy vector** 模块参数中的对应元素相等。

默认是水的 100 元素向量。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2023a: 控制仿真期间流体属性超出范围时的模块行为

以前，如果流体属性在仿真期间超出有效范围，模块会返回错误。现在，您可以使用新的 **Pressure and specific internal energy outside valid range** 参数来控制流体属性在仿真期间超出范围时的模块行为。

## 描述

两相流体网络的流体属性

Two-Phase Fluid Properties (2P) 模块设置两相流体网络中流体的热物理属性。这些属性包括密度、黏度、比热等，可以延伸到流体的超临界区域（默认情况下为水，其超临界区域的压力最高可延伸到 `100 MPa`）。

这些属性适用于整个两相流体网络（连续连接的两相流体模块组）。一个网络只能有一种工作流体，因此只能有一个此模块实例。如果在没有此模块的情况下对网络建模，则流体设置为水，其属性从域定义中获取。

该模块根据压力和归一化内能（比内能的线性变换）来参数化流体属性。在过冷液体中，归一化内能定义为

u¯=u−uminusatL(p)−umin−1,umin≤u<uLsat(p),

其中：

- *u¯* 是流体的归一化内能。
- *u* 是流体的比内能。
- *u*min 是两相流体网络中允许的最低比内能。
- *u*Lsat 是饱和时液相的比内能。

在过热蒸气中，归一化内能定义为

u¯=u−umaxumax−usatV(p)+2,uVsat(p)<u≤umax,

其中：

- *u*max 是两相流体网络中允许的最高比内能。
- *u*Vsat 是饱和时蒸气相的比内能。

在两相混合物中，归一化内能定义为

u¯=u−usatL(p)usatV(p)−usatL(p),uLsat(p)≤u≤uVsat(p).

这些表达式对应于这样的归一化内能：在所有压力下，它在最小有效比内能处为 -1，在液体饱和边界处为 0，在蒸气饱和边界处为 +1，在最大有效比内能处为 +2。

在两相混合物中，归一化内能的值范围为 0 到 1，因此等效于蒸气干度——两相混合物中蒸气相的质量分数。在过冷液体和过热蒸气中，归一化内能表现为蒸气干度的扩展。

归一化内能相比比内能具有一个优势。它变换 *p*-*u* 相图，使过冷液体相和过热蒸气相占据不同的矩形区域。如图所示，这种变换使您能够在分开的矩形 *p*-*u¯* 网格上指定流体属性，每个相对应一个网格。

长度为 *N* 的压力向量和两个归一化内能向量（长度分别为 *M*L 和 *M*V）提供两个网格的 (*p*, *u¯*) 坐标。压力向量是两个网格共用的。过冷液体网格的大小为 *M*L × *N*，过热蒸气网格的大小为 *M*V × *N*。

双向查找表提供 (*p*, *u¯*) 网格上的流体属性值。表的行对应不同的归一化内能，表的列对应压力。*p*-*u¯* 连续体中的流体属性使用 *p*-*u¯* 数据点之间的线性插值计算。

**双向属性查找表**

饱和比内能向量提供 (*p*, *u¯*) 相图中的相边界。这些边界分隔相图的不同区域——过冷液体、两相混合物和过热蒸气。

与最小和最大有效比内能值一起，饱和比内能向量使 Two-Phase Fluid 模块能够将在此模块中指定的归一化内能转换为它们用于计算的比内能。

### 超临界流体

流体可以成为超临界流体。此时液体和蒸气不再作为独立的相存在。它们的饱和边界合并，形成所谓的拟临界线（在图中，从 *p*–*u* 相图的隆起处向上延伸的线段）。

拟临界线将流体分为类液相区域和类气相区域。然而，由于相不再有区别，区域之间的过渡是渐变的而非突变的。这意味着在拟临界线处，类液相流体和类气相流体必须具有相同的物理属性。

**属性表**

在该模块中，超临界区域的类液相部分被视为液相的延伸。类似地，类气相部分被视为气相的延伸。换句话说，超临界流体的属性被划分到模块的液体和蒸气属性表中。

然而，在超临界区域，相之间的区别是多余的。对于超过临界压力的断点，液体和蒸气属性表必须在饱和边界处一致（或者更准确地说，在拟临界线处一致）。此时表的超临界部分表现为一个连续整体。

以运动粘度表为例。**Liquid kinematic viscosity table** 参数的底行，由于它对应于归一化比内能 `1`，给出了饱和液体的数据。该行中对应压力等于或高于临界点的元素给出了拟临界线上的数据。

类似地，**Vapor kinematic viscosity table** 参数的顶行，由于它对应于归一化比内能 `1`，给出了饱和蒸气的数据。因此，该行中对应压力等于或高于临界点的元素给出了拟临界线上的数据。为了有效，该数据必须与液体表中拟临界线上的数据完全相同。

**拟临界线**

拟临界线被编码在液相和气相的饱和边界中。这些在模块中通过 **Saturated liquid specific internal energy vector** 和 **Saturated vapor internal energy vector** 参数指定。在低于临界点的压力下，一个向量中的值通常与另一个向量中的值不同；然而，在高于临界点时，一个必须始终等于另一个。

拟临界线可以呈现任何形状。对于简单近似，通常只需将临界点的比内能沿压力轴向上延伸即可。这意味着将饱和比内能向量的超临界部分设置为该临界值。如果已知拟临界线的精确形状，则可以改使用沿该线的比内能。

**热输运属性**

热输运属性的数据——比热、导热系数和普朗特数——通常会在临界点附近显示出很大的峰值。在某些情况下，峰值的尺度和大小可能会在仿真期间导致数值问题。为避免此类问题，模块允许裁剪峰值。该选项在 **Thermal transport properties near critical point** 模块参数中指定（通过将其设置为 `Clip peak values`）。

裁剪仅限于临界点周围的一小段压力范围。该范围指定为临界压力的一个分数（图中为 *f*），并从临界压力向两个方向延伸（延伸量相同）。在该范围内，每个热属性都限制为其两个端值中较大者所给定的最大值。图中显示了裁剪后水的普朗特数图。

### 数据可视化

该模块允许您将指定的两相流体属性绘制为压力和比内能的函数。绘制属性可让您在仿真模型之前可视化数据。

要绘制数据，请在模型中右键单击 Two-Phase Fluid Properties (2P) 模块，然后从上下文菜单中选择 **Foundation Library** > **Plot Fluid Properties (3D)** 或 **Foundation Library** > **Plot Fluid Properties (Contours)**。使用位于图顶部的下拉列表选择要可视化的属性。在模块参数更新后，单击 **Reload** 按钮重新生成图。

**流体属性（3D）图**

**流体属性（等值线）图**
