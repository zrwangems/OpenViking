---
type: simulink-block
title: 'Pipe (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'pipeil'
documentation_source_path: 'ref/pipeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

液体进入或退出端口。

### **B** — 液体端口 isothermal liquid

液体进入或退出端口。

### 输入

### **EL** — 高程物理信号

从端口 **A** 到端口 **B** 的可变高程，指定为物理信号。模块将 **EL** 处的信号值限制在 *-L* 和 *L* 之间，其中 *L* 是 **Pipe length** 参数的值。

#### 依赖关系

要启用此端口，请将 **Elevation gain specification** 设置为 `Variable`。

### **G** — 重力加速度物理信号

可变重力加速度，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Gravitational acceleration specification** 设置为 `Variable`。

## 参数

### 配置

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对由流体可压缩性引起的任何流体密度变化建模。当您选择 **Enable dynamic compressibility** 时，除了由压力变化引起的密度变化外，还会计算由进入模块的质量流量引起的密度变化。在 Isothermal Liquid Library 中，所有模块都将密度计算为压力的函数。

### **Enable fluid inertia** — 流体加速度 `off`（默认）| `on`

是否考虑由流体质量引起的对流率变化的阻力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Number of segments** — 管道分段数 `1`（默认）| 正整数

管道分段数。每个分段表示一个独立分段，针对该分段根据管道入口压力、流体可压缩性以及（如适用）管壁柔性计算压力。每个分段中的流体体积保持固定。

### **Pipe length** — 管道长度 `5 m`（默认）| 正标量

所有管道分段的总管道长度。

### **Cross-sectional geometry** — 管道几何形状 `Circular`（默认）| `Annular` | `Rectangular` | `Elliptical` | `Isosceles triangular` | `Custom`

管道横截面几何形状。根据横截面几何形状计算标称水力直径和标称横截面积。

### **Pipe diameter** — 管道直径 `0.1 m`（默认）| 正标量

圆形横截面管道的直径。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Circular`。

### **Pipe inner diameter** — 管道内径 `0.05 m`（默认）| 正标量

环形管道流动或两个同心管道之间流动的内径。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Annular`。

### **Pipe outer diameter** — 管道外径 `0.1 m`（默认）| 正标量

环形管道流动或两个同心管道之间流动的外径。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Annular`。

### **Pipe width** — 矩形管道宽度 `0.1 m`（默认）| 正标量

矩形管道的宽度。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Rectangular`。

### **Pipe height** — 矩形管道高度 `0.1 m`（默认）| 正标量

矩形管道的高度。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Rectangular`。

### **Pipe major axis** — 椭圆形管道长轴 `0.1 m`（默认）| 正标量

椭圆形管道的主轴。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Elliptical`。

### **Pipe minor axis** — 椭圆形管道短轴 `0.05 m`（默认）| 正标量

椭圆形管道的短轴。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Elliptical`。

### **Pipe side length** — 三角形管道边长 `0.1 m`（默认）| 正标量

等腰三角形管道的两条相等边的长度。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Isosceles triangular`。

### **Pipe vertex angle** — 三角形管道顶角 `30 deg`（默认）| 正标量

三角形管道的顶角。该值必须小于 180 度。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Isosceles triangular`。

### **Hydraulic diameter** — 水力直径 `0.1128 m`（默认）| 正标量

用于计算管道雷诺数的水力直径。对于非圆形管道，水力直径是管道中流体的有效直径。对于圆形管道，水力直径与管道直径相同。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Custom`。

### **Cross-sectional area** — 管道横截面积 `0.01 m^2`（默认）| 正标量

自定义管道几何形状的管道横截面积。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Custom`。

### **Elevation gain specification** — 管道高程规格 `Constant`（默认）| `Variable`

管道高程从端口 **A** 到 **B** 是保持恒定还是可变。

### **Elevation gain from port A to port B** — 恒定管道高程差 `0 m`（默认）| 标量

恒定高程管道的高程差。

#### 依赖关系

要启用此参数，请将 **Elevation gain specification** 设置为 `Constant`。

### **Gravitational acceleration specification** — 加速度规格 `Constant`（默认）| `Variable`

重力常量是恒定还是可变。

### **Gravitational acceleration** — 重力加速度 `9.81 m/s^2`（默认）| 标量

恒定重力加速度环境下的重力加速度。

#### 依赖关系

要启用此参数，请将 **Gravitational acceleration specification** 设置为 `Constant`。

### 粘性摩擦

### **Viscous friction parameterization** — 计算由壁面摩擦引起的压力损失的方法 `Haaland correlation`（默认）| `Nominal pressure drop vs. nominal mass flow rate` | `Tabulated data - Darcy friction factor vs. Reynolds number`

由壁面摩擦引起的压力损失的参数化。解析公式和表格公式均可用。

### **Local resistances specification** — 在 Haaland correlation 中量化压力损失的方法 `Aggregate equivalent length`（默认）| `Local loss coefficient`

量化由管道非均匀性引起的压力损失的方法。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`。

### **Total local loss coefficient** — 定义管道上的损失系数 `0.1`（默认）| 正标量

与每个管道非均匀性相关的损失系数。您可以输入单个损失系数或沿管道的所有损失系数之和。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`，并将 **Local resistance specifications** 设置为 `Local loss coefficient`。

### **Aggregate equivalent length of local resistances** — 管道几何形状对水力损失的贡献 `1 m`（默认）| 正标量

会产生与带有弯头、面积变化或其他非均匀属性的管道等效的水力损失的管道长度。管道的有效长度是 **Pipe length** 与 **Aggregate equivalent length of local resistances** 之和。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`，并将 **Local resistance specifications** 设置为 `Aggregate equivalent length`。

### **Surface roughness specification** — 用于粗糙度规格的管道材料 `Commercially smooth brass, lead, copper, or plastic pipe: 1.52 um`（默认）| `Steel and wrought iron : 46 um` | `Galvanized iron or steel : 152 um` | `Cast iron : 259 um` | `Custom`

基于管道材料的绝对表面粗糙度。提供的值是 ASHRAE 标准粗糙度值。您也可以通过将 **Surface roughness specification** 设置为 `Custom` 来输入自己的值。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`。

### **Internal surface absolute roughness** — 管壁粗糙度 `15e-6 m`（默认）| 正标量

管壁绝对粗糙度。此参数用于确定 Darcy 摩擦因子，该因子会造成管道中的压力损失。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`，并将 **Surface roughness specification** 设置为 `Custom`。

### **Laminar flow upper Reynolds number limit** — 层流上限阈值 `2000`（默认）| 正标量

层流的雷诺数上限。超过此数值后，流体流态为过渡流态，趋近湍流流态，并在 **Turbulent flow lower Reynolds number limit** 处变为完全湍流。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为以下之一：

- `Haaland correlation`
- `Tabulated data - Darcy friction factor vs. Reynolds number`

### **Turbulent flow lower Reynolds number limit** — 湍流下限阈值 `4000`（默认）| 正标量

湍流的雷诺数下限。低于此数值时，流态为过渡流态，趋近层流，并在 **Laminar flow upper Reynolds number limit** 处变为完全层流。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为以下之一：

- `Haaland correlation`
- `Tabulated data - Darcy friction factor vs. Reynolds number`

### **Nominal mass flow rate** — 用于计算损失系数的质量流量 `[.1, 1] kg/s`（默认）| 正标量 | 1-by-*n* 向量

用于计算刚性管道和柔性管道的压力损失系数的标称质量流量，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **Nominal pressure drop** 参数相同。当此参数以向量形式提供时，标量值 *K*loss 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **Nominal pressure drop** — 用于计算损失系数的压降 `[.001, .01] MPa`（默认）| 正标量 | 1-by-*n* 向量

用于计算刚性管道和柔性管道的压力损失系数的标称压降，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **Nominal mass flow rate** 参数相同。当此参数以向量形式提供时，标量值 *K*loss 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **Mass flow rate threshold for flow reversal** — 质量流量阈值 `1e-6 kg/s`（默认）| 正标量

反向流动的质量流量阈值。在质量流量阈值的正值和负值之间，围绕 0 kg/s 定义一个过渡区域。在该过渡区域内，对流动响应应用数值平滑。阈值必须大于 0。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **Reynolds number vector for turbulent Darcy friction factor** — 用于表格化参数化的雷诺数向量 [400, 1000, 1500, 3000, 4000, 6000, 10000, 20000, 40000, 60000, 100000, 100000000]（默认）| 1-by-*n* 向量

用于 Darcy 摩擦因子表格化参数化的雷诺数向量。向量元素与 **Darcy friction factor vector** 参数构成一个独立轴。向量元素必须按升序列出。正雷诺数对应于从端口 **A** 到端口 **B** 的流动。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — 用于表格化参数化的摩擦因子向量 `[.264, .112, .071, .0417, .0387, .0268, .025, .0232, .0226, .022, .0214, .0214]`（默认）| 1-by-*n* 向量

用于 Darcy 摩擦因子表格化参数化的 Darcy 摩擦因子向量。向量元素必须与 **Reynolds number vector for turbulent Darcy friction factor** 参数中的元素一一对应，并且必须唯一且大于或等于 0。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Laminar friction constant for Darcy friction factor** — 层流的摩擦常数 `64`（默认）| 正标量

层流的摩擦常数。Darcy 摩擦因子在压力损失计算中体现壁面摩擦的贡献。如果 **Cross-sectional geometry** 未设置为 `Custom`，则此参数在内部设置为 64。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为以下之一：

- `Haaland correlation`
- `Tabulated data - Darcy friction factor vs. Reynolds number`

并将 **Cross-sectional geometry** 设置为 `Custom`。

### 管壁

### **Pipe wall specification** — 指定管壁柔性 `Rigid`（默认）| `Flexible`

指定管壁柔性。此参数与管道横截面几何形状无关。`Flexible` 设置保留初始管道形状，并对横截面积施加均匀膨胀。对于高变形下的非圆形横截面几何形状，它可能不准确。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Volumetric expansion specification** — 线性膨胀相关性 `Cross-sectional area vs. pressure`（默认）| `Cross-sectional area vs. pressure - Tabulated` | `Hydraulic diameter vs. pressure` | `Based on material properties`

线性膨胀相关性。这些设置将新的横截面积或水力直径与管道压力相关联。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`。

### **Static gauge pressure to cross-sectional area gain** — 面积相关管道变形的系数 `1e-6 m^2/MPa`（默认）| 正标量

用于计算 `Cross-sectional area vs. pressure` 设置下管道变形的系数。该增益乘以分段压力与大气压力之间的压力差。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Cross-sectional area vs. pressure`。

### **Static gauge pressure vector** — 表压向量 `[.1,1] MPa`（默认）| 向量

包含表压的向量。模块在查表中使用此向量来计算管道横截面积。向量元素必须严格为正且单调递增，并且向量长度必须与 **Cross sectional area gain vector** 参数相同。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Cross-sectional area vs. pressure - Tabulated`。

### **Cross sectional area gain vector** — 管道横截面积的向量 `[1e-05, 1.1e-05] m^2`（默认）| vector

包含管道横截面积的向量。该模块使用此向量进行表查找，以计算其他压力下的管道横截面积。向量元素必须严格为正且单调递增，并且该向量必须与 **Static gauge pressure vector** 参数长度相同。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Cross-sectional area vs. pressure - Tabulated`。

### **Static gauge pressure to hydraulic diameter gain** — 与直径相关的管道变形的系数 `1e-6 m/MPa`（默认）| positive scalar

用于计算 `Hydraulic diameter vs. pressure` 设置下管道变形的系数。该增益乘以段压力与大气压力之间的压差。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Hydraulic diameter vs. pressure`。

### **Material behavior** — 用于指定材料行为的方法 `Linear Elastic`（默认）| `Multilinear Elastic`

该模块用于计算材料行为的方法。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`。

### **Pipe wall thickness** — 管壁厚度 `0.05 m`（默认）| positive scalar

管壁厚度。该模块使用此值计算应力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`。

### **Young's modulus** — 管壁材料的 Young's 模量 `69 GPa`（默认）| positive scalar

构成管壁的材料的 Young's 模量。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，并将 **Material behavior** 设置为 `Linear Elastic`。

### **Poisson's ratio** — 管壁材料的 Poisson's 比 `0.33`（默认）| positive scalar

构成管壁的材料的 Poisson's 比。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`。

### **Stress vector** — 管壁材料的应力向量 `[276, 310] MPa`（默认）| vector

包含构成管壁的材料的应力值的向量。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，并将 **Material behavior** 设置为 `Multilinear Elastic`。

### **Strain vector** — 管壁材料的应变向量 `[.004, .02]`（默认）| vector

包含构成管壁的材料的应变值的向量。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，并将 **Material behavior** 设置为 `Multilinear Elastic`。

### **Check if stress exceeds specified allowable level** — 当应力高于指定最大值时的通知 `None`（默认）| `Warning` | `Error`

当应力高于 **Maximum allowable stress** 参数指定的最大应力时，模块是不执行任何操作、生成警告还是生成错误。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，将 **Material behavior** 设置为 `Multilinear Elastic`，并将 **Check if stress exceeds specified allowable level** 设置为 `Warning` 或 `Error`。

### **Maximum allowable stress** — 管壁上允许的最大应力 `400 MPa`（默认）| positive scalar

模块允许的管壁最大应力。使用 **Check if stress exceeds specified allowable level** 参数控制当应力超过此值时模块的行为。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，将 **Material behavior** 设置为 `Multilinear Elastic`，并将 **Check if stress exceeds specified allowable level** 设置为 `Warning` 或 `Error`。

### **Volumetric expansion time constant** — 管道变形时间常数 `0.01 s`（默认）| positive scalar

管道变形后管壁达到稳态所需的时间。此参数影响管道体积的动态变化。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`。

### 初始条件

### **Initial liquid pressure** — 管道或管道段中的初始压力 `0.101325 MPa`（默认）| positive scalar | 1-by-*n* vector

初始液体压力，指定为标量或向量。长度为 *n* 个元素的向量定义 *n* 个管道段中每一段的液体压力。如果向量长度为两个元素，则沿管道的压力在两个元素值之间线性分布。如果向量长度为三个或更多元素，则第 *n* 段中的初始压力由向量的第 *n* 个元素设置。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Initial mass flow rate from port A to port B** — 用于惯性计算的初始质量流量 `0 kg/s`（默认）| scalar

模拟流体惯性的管道的初始质量流量。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility** 和 **Enable fluid inertia**。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023b: 对长度短于高程增益的管道建模

现在，当 **Elevation gain specification** 为 `Constant` 时，您可以对长度短于高程变化的管道建模。如果 **Elevation gain from port A to port B** 参数的值大于 **Pipe length** 参数的值，该模块会发出警告而不是错误。

### R2023a: 使用附加的柔性管道参数化

现在，当 **Pipe wall specification** 参数为 `Flexible` 时，您可以使用新的参数化方法。要使用新的参数化，请将 **Volumetric expansion specification** 参数设置为 `Cross-sectional area vs. pressure - Tabulated` 或 `Based on material properties`。

## 描述

等温液体网络中的管道段

Pipe (IL) 模块对刚性或柔性壁管道中的流动进行建模，并包含由管壁摩擦引起的损失。可以选择对动态可压缩性、流体惯性和管道高程的影响进行建模。可以定义多个管道段并为每个段设置液体压力。通过对管道进行分段并选择 **Enable fluid inertia**，可以对系统中的水锤等事件进行建模。

### 管道特性

可以使用 **Number of segments** 参数将管道模块划分为若干段。当管道由若干段组成时，每段中的压力基于入口压力以及（若适用）流体可压缩性和管壁柔性对段质量流量的影响来计算。每段中的流体体积保持固定。对于两段管道，压力相对于端口 **A** 和 **B** 处定义的压力线性演变。对于具有三个或更多段的管道，可以在 **Initial liquid pressure** 参数中以向量或标量形式指定每段中的流体压力。标量形式将在所有段上应用恒定值。

**柔性管壁**

可以为所有横截面几何形状对柔性管壁建模。当将 **Pipe wall specification** 设置为 `Flexible` 时，该模块假设沿所有方向均匀膨胀，并保留定义的横截面形状。对于承受相对于大气压力高压的非圆形横截面积，此设置可能不会产生物理上合理的结果。对柔性管壁建模时，可以使用 **Volumetric expansion specification** 参数控制指定管道横截面积体积膨胀的方法。

当 **Volumetric expansion specification** 参数为 `Cross-sectional area vs. pressure` 时，体积变化通过以下公式建模：

V˙=L(A−Sτ),

其中：

- A=SN+Kps(p−patm).
- *L* 是 **Pipe length** 参数。
- *SN* 是为每种形状定义的标称管道横截面积。
- *S* 是当前管道横截面积。
- *p* 是管道内部压力。
- *patm* 是大气压力。
- *K*ps 是 **Static gauge pressure to cross-sectional area gain** 参数。

  在假设薄壁开口圆柱管均匀弹性变形的情况下，要计算 *Kps*，请使用：

  Kps=ΔDΔp=πDN34tE,

  其中 *t* 是管壁厚度，*E* 是 Young's 模量。
- *τ* 是 **Volumetric expansion time constant**。

当 **Volumetric expansion specification** 参数为 `Cross-sectional area vs. pressure - Tabulated` 时，该模块使用与 `Cross-sectional area vs. pressure` 设置相同的 V˙ 方程。该模块使用表查找函数计算 *A*：

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear),

其中 *pps* 是 **Static gauge pressure vector** 参数，*Aps* 是 **Cross sectional area gain vector** 参数。

当 **Volumetric expansion specification** 参数为 `Hydraulic diameter vs. pressure` 时，体积变化通过以下公式建模：

V˙=π2DL(Dstatic−Dτ),

其中：

- Dstatic=DN+Kpd(p−patm).
- *DN* 是为每种形状定义的标称水力直径。
- *D* 是当前管道水力直径。
- *K*pd 是 **Static gauge pressure to hydraulic diameter gain** 参数。在假设薄壁开口圆柱管均匀弹性变形的情况下，要计算 *Kps*，请使用：

  Kpd=ΔDΔp=DN22tE.

当 **Volumetric expansion specification** 参数为 `Based on material properties` 时，该模块使用与 `Hydraulic diameter vs. pressure` 设置相同的 V˙ 方程，但根据 **Material behavior** 参数的值计算 *Dstatic*：

Dstatic=DN(1+ϵhoop).

此参数化假设为圆柱形薄壁压力容器，其中 σradial=0。

当 **Material behavior** 参数为 `Linear elastic` 时，

ϵhoop=1E[σhoop−vσlongitudinal],

其中：

- *E* 是 **Young's modulus** 参数的值。
- *v* 是 **Poisson's ratio** 参数的值。
- σhoop=pD2t，其中 *t* 是 **Pipe wall thickness** 参数的值。
- σlongitudinal=pD4t.

当 **Material behavior** 参数为 `Multilinear elastic` 时，该模块计算 von Mises 应力 *σv*，其简化为 σv=34pD2t，以确定等效应变。环向应变为

ϵhoop=ϵhoopelastic+ϵhoopplastic

ϵhoopelastic=1E[σhoop−vσlongitudinal]ϵhoopi,jplastic=32(1Es−1E)Si,j

其中：

- 该模块从 **Stress vector** 和 **Strain vector** 参数的第一个元素计算 Young's 模量 *E*。
- ES=σtotalϵtotal，其中 *σtotal* 和 *εtotal* 分别是等效总应力和等效总应变。该模块根据 von Mises 应力和应力-应变曲线计算等效总应变。
- Si,j=σi,j−[σhoop+σlongitudinal+σradial3]δi,j，其中 *σi,j* 是 Cauchy 应力张量的元素。

如果未对柔性管壁建模，则 *SN* = *S* 且 *DN* = *D*。

**Circular**

标称水力直径与 **Pipe diameter**（*d*circle）相同。管道横截面积为：SN=π4dcircle2。

**Annular**

标称水力直径 *D*h,nom 是 **Pipe outer diameter** 与 **Pipe inner diameter** 之差，*d*o – *d*i。管道横截面积为 SN=π4(do2−di2)。

**Rectangular**

标称水力直径为：

DN=2hwh+w,

其中：

- *h* 是 **Pipe height**。
- *w* 是 **Pipe width**。

管道横截面积为 SN=wh。

**Elliptical**

标称水力直径为：

DN=2amajbmin(64-16(amaj-bminamaj+bmin)2)(amaj+bmin)(64-3(amaj-bminamaj+bmin)4),

其中：

- *a*maj 是 **Pipe major axis**。
- *b*min 是 **Pipe minor axis**。

管道横截面积为 SN=π4amajbmin。

**Isosceles Triangular**

标称水力直径为：

DN=lsidesin(θ)1+sin(θ2)

其中：

- *l*side 是 **Pipe side length**。
- *θ* 是 **Pipe vertex angle**。

管道横截面积为 SN=lside22sin(θ)。

### Pressure Loss Due to Friction

**Haaland 关联式**

解析 Haaland 关联式通过 *总等效长度* 或 *局部损失系数* 对壁面摩擦导致的损失建模。前者将非均匀性引起的阻力视为增加一段直管长度，从而产生等效损失；后者直接对管道非均匀性应用损失系数。

当 **Local resistances specification** 参数设置为 `Aggregate equivalent length`，且管道中的流动低于 **Laminar flow upper Reynolds number limit** 时，所有管段上的压力损失为：

Δpf,A=υλ2D2SL+Ladd2m˙A,

Δpf,B=υλ2D2SL+Ladd2m˙B,

其中：

- *ν* 是流体运动粘度。
- *λ* 是 **Laminar friction constant for Darcy friction factor**，当 **Cross-sectional geometry** 设置为 `Custom` 时你可以定义该值，否则等于 64。
- *D* 是管道水力直径。
- *L*add 是 **Aggregate equivalent length of local resistances**。
- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

当雷诺数大于 **Turbulent flow lower Reynolds number limit** 时，管道中的压力损失为：

Δpf,A=f2ρIDS2L+Ladd2m˙A|m˙A|,

Δpf,B=f2ρIDS2L+Ladd2m˙B|m˙B|,

其中：

- *f* 是 Darcy 摩擦因子。它由经验 Haaland 方程近似，并基于 **Surface roughness specification**、*ε* 和管道水力直径：

  f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

  黄铜、铅、铜、塑料、钢、熟铁以及镀锌钢或铁的管道粗糙度按 ASHRAE 标准值提供。你还可以通过 `Custom` 设置提供自己的 **Internal surface absolute roughness**。
- *ρ*I 是内部流体密度。

当 **Local resistances specification** 参数设置为 `Local loss coefficient`，且管道中的流动低于 **Laminar flow upper Reynolds number limit** 时，所有管段上的压力损失为：

Δpf,A=υλ2D2SL2m˙A.

Δpf,B=υλ2D2SL2m˙B.

当雷诺数大于 **Turbulent flow lower Reynolds number limit** 时，管道中的压力损失为：

Δpf,A=(fL2D+Closs,total)12ρIS2m˙A|m˙A|,

Δpf,B=(fL2D+Closs,total)12ρIS2m˙B|m˙B|,

其中 *C*loss,total 是损失系数，可在 **Total local loss coefficient** 参数中定义为单个系数或沿管道所有损失系数之和。

**Nominal Pressure Drop vs. Nominal Mass Flow Rate**

**Nominal Pressure Drop vs. Nominal Mass Flow Rate** 参数化使用损失系数表征刚性或柔性壁的损失。当流体不可压缩时，由于壁面摩擦导致的整个管道压力损失为：

Δpf,A=Kpm˙Am˙A2+m˙th2,

其中 *K*p 为：

Kp=ΔpNm˙N2,

其中：

- *Δp*N 是 **Nominal pressure drop**，可定义为标量或向量。
- m˙N 是 **Nominal mass flow rate**，可定义为标量或向量。

当 **Nominal pressure drop** 和 **Nominal mass flow rate** 参数以向量形式提供时，标量值 *K*p 由向量元素的最小二乘拟合确定。

**Tabulated Data – Darcy Friction Factor vs. Reynolds Number**

由于粘性摩擦导致的压力损失也可由用户提供的 **Darcy friction factor vector** 和 **Reynolds number vector for turbulent Darcy friction factor** 参数的表格数据确定。数据点之间采用线性插值。

### 管道离散化

你可以将管道划分为多个管段。如果管道具有多个管段，则对每个管段计算质量流量和动量平衡方程。

如果你希望捕获应用中的特定现象，例如水锤，请选择能为瞬态提供足够分辨率的管段数。以下来自 Nyquist 采样定理的公式给出了将管道离散化为最少 *N* 个管段的经验法则：

N=2Lfc,

其中：

- *L* 是 **Pipe length**。
- *f* 是瞬态频率。
- *c* 是声速。

### 质量和动量平衡

当你清除 **Enable dynamic compressibility** 复选框时，流入管道的质量流量等于流出管道的质量流量

m˙A+m˙B=0.

当你选中 **Enable dynamic compressibility** 并将 **Pipe wall specification** 设置为 `Rigid` 时，流入和流出管道的质量流量之差取决于由可压缩性引起的流体密度变化，

m˙A+m˙B=p˙IdρIdpIV,

当你选中 **Enable dynamic compressibility** 并将 **Pipe wall specification** 设置为 `Flexible` 时，流入和流出管道的质量流量之差基于由可压缩性引起的流体密度变化，以及在新变形区域中积聚的流体量：

m˙A+m˙B=p˙IdρIdpIV+ρIV˙.

管道入口与出口之间的动量变化包括由管壁摩擦引起的压力变化，该摩擦根据 **Viscous friction parameterization** 和管道高程建模。

当你清除 **Enable fluid inertia** 复选框时，动量平衡为：

pA−pI=Δpf,A+ρIΔz2g,

pB−pI=Δpf,B−ρIΔz2g,

其中：

- *p*A 是端口 **A** 处的压力。
- *p*I 是流体体积内部压力。
- *p*B 是端口 **B** 处的压力。
- *Δp*f 是由于壁面摩擦导致的压力损失，根据相应端口由 **Viscous friction losses** 规范参数化。
- *Δz* 是管道高程。对于恒定高程管道，这是 **Elevation gain from port A to port B** 参数；否则，它作为物理信号在端口 **EL** 接收。
- *g* 是重力加速度。对于固定重力常数，这是 **Gravitational acceleration** 参数；否则，它作为物理信号在端口 **G** 接收。

当你选中 **Enable fluid inertia** 时，动量平衡为：

pA−pI=Δpf,A+ρIΔz2g+m¨AL2S,

pB−pI=Δpf,B−ρIΔz2g+m¨BL2S,

其中：

- m¨ 是在相应端口处的流体加速度。
- *S* 是管道横截面积。
