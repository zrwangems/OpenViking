---
type: simulink-block
title: 'Vehicle Body'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'vehiclebody'
documentation_source_path: 'ref/vehiclebody.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body

## 端口

### 输入

### **W** — 逆风速度，m/s 物理信号

逆风速度的物理信号输入端口，单位为 m/s。

### **beta** — 道路倾斜角，rad 物理信号

道路倾斜角的物理信号输入端口，单位为 rad。

### **CG** — 重心，m 物理信号

外部定义质量的重心相对于车辆车身 CG 的物理信号输入端口，单位为 m。

#### 依赖关系

要启用此端口，请选择 **Externally-defined additional mass**。

### **M** — 质量，kg 物理信号

外部定义质量的物理信号输入端口，单位为 kg。

#### 依赖关系

要启用此端口，请选择 **Externally-defined additional mass**。

### **J** — 外部转动惯量，kg\*m^2 物理信号

外部定义质量的转动惯量的物理信号输入端口，单位为 kg\*m^2。

#### 依赖关系

要启用此端口，请选择 **Externally-defined additional mass** 和 **Pitch dynamics**。

### **CD** — 阻力系数，无单位物理信号

阻力系数的物理信号输入端口。

#### 依赖关系

要启用此端口，请选择 **Variable drag coefficient**。

### 输出

### **V** — 纵向速度，m/s 物理信号

车辆参考坐标系中车辆纵向速度的物理信号输出端口，单位为 m/s。

### **NF** — 前轴法向力，N 物理信号

前轴法向力的物理信号输出端口，单位为 N。如果车轮力向下作用，则视为正值。

### **NR** — 后轴法向力，N 物理信号

后轴法向力的物理信号输出端口，单位为 N。如果车轮力向下作用，则视为正值。

### 守恒

### **H** — 水平运动机械平移

与车辆车身水平运动关联的机械平移守恒端口。将轮胎牵引运动连接到此端口。

## 参数

### 主要

### **Mass** — 车辆质量 `1200` `kg`（默认）| 正标量

车辆的质量。

### **Number of wheels per axle** — 车轮数量 `2`（默认）| 正整数或二元素向量

前轴和后轴上的车轮数量。如果输入是标量数字，则假定前轴和后轴的车轮数量相同。例如，如果输入为 `2`，则假定前轴和后轴各有两轮。

如果输入是二元素数组，则第一个数字是前轴车轮数量，第二个数字是后轴车轮数量。例如，如果输入为数组 `[2,1]`，则假定前轴有两个车轮，后轴有一个车轮。

### **Horizontal distance from CG to front axle** — CG 到前轴距离 `1.4` `m`（默认）| 正标量

从车辆重心到前轮轴的水平距离，*a*。

### **Horizontal distance from CG to rear axle** — CG 到后轴距离 `1.6` `m`（默认）| 正标量

从车辆重心到后轮轴的水平距离，*b*。

### **CG height above ground** — CG 到地面距离 `0.5` `m`（默认）| 正标量

车辆重心与地面之间的距离，*h*。

### **Gravitational acceleration** — 重力加速度 `9.81` `m/s^2`（默认）| 非负标量

因重力作用在车辆重心处而产生的加速度。

### **Externally-defined additional mass** — 可变质量选项 `off`（默认）| `on`

用于将质量作为时间可变或事件可变项包含在内的选项，该项会影响车辆车身的质量和 CG。使用此选项来表示车辆乘员或非受限体。

### **Negative normal force warning** — 法向力警告 `off`（默认）| `on`

当法向力计算返回负值时，模块是否生成警告。由于方程假设车轮永不失去接触，模块可能会生成负力。

### 阻力

### **Frontal area** — 有效横截面积 `3` `m^2`（默认）| 正标量

车辆在纵向运动时呈现的有效横截面积，*A*。模块使用此值计算车辆受到的气动阻力。

### **Variable drag coefficient** — 可变阻力选项 `off`（默认）| `on`

阻力是否可变。使用端口 **CD** 控制阻力。

### **Drag coefficient** — 气动阻力系数 `0.4`（默认）| 非负标量

气动阻力系数，*C*d。模块使用此值计算车辆受到的气动阻力。

### **Air density** — 环境空气密度 `1.18` `kg/m^3`（默认）| 非负标量

车辆周围空气的密度。

### 俯仰

### **Pitch dynamics** — 俯仰动力学选项 `off`（默认）| `on`

是否对俯仰动力学建模。

### **Pitch moment of inertia** — 俯仰转动惯量 `4000` `kg/m^2`（默认）| 正标量

用于俯仰计算的转动惯量。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**。

### **Suspension model** — 悬架参数化方法 `Linear`（默认）| `By table lookup`

悬架建模的参数化方法。要使用标量值指定数据，请选择 `Linear`。要使用向量值指定数据，请选择 `By table lookup`。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**。

### **Front suspension stiffness** — 前悬架刚度 `1e4` `N/m`（默认）| 正标量

每个轴的前悬架刚度。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `Linear`。

### **Front suspension damping** — 前悬架阻尼 `1e4``N/(m/s)`（默认）| 正标量

每个轴的前悬架阻尼。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `Linear`。

### **Rear suspension stiffness** — 后悬架刚度 `1e4` `N/m`（默认）| 正标量

每个轴的后悬架刚度。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `Linear`。

### **Rear suspension damping** — 后悬架阻尼 `1e4` `N/(m/s)`（默认）| 正标量

每个轴的后悬架阻尼。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `Linear`。

### **Front suspension stiffness force vector** — 前悬架刚度力 `[-2000, -1000, 0, 1000, 2000]` `N`（默认）| 递增向量

前悬架的刚度力。将查找表的输出值指定为向量。输出向量中的元素数量必须与输入向量中的元素数量相同。输入向量参数是 **Front suspension deformation vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Front suspension deformation vector** — 前悬架变形 `[-.4, -.2, 0, .2, .4]` `m`（默认）| 递增向量

按位移指定的前悬架变形。将查找表的输入值指定为向量。向量中元素的值必须从左到右递增。向量中的最小元素数量取决于所选的插值方法。对于线性插值，请至少提供两个元素。对于平滑插值，请至少提供三个元素。输出向量参数是 **Front suspension stiffness force vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Front suspension damping force vector** — 前悬架阻尼力 `[-200, -100, 0, 100, 200]` `N`（默认）| 递增向量

前悬架的阻尼力。将查找表的输出值指定为向量。输出向量中的元素数量必须与输入向量中的元素数量相同。输入向量参数是 **Front suspension velocity vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Front suspension velocity vector** — 前悬架速度 `[-4, -2, 0, 2, 4]` `m/s`（默认）| 递增向量

前悬架的速度。将查找表的输入值指定为向量。向量中元素的值必须从左到右递增。向量中的最小元素数量取决于所选的插值方法。对于线性插值，请至少提供两个元素。对于平滑插值，请至少提供三个元素。输出向量参数是 **Front suspension damping force vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Rear suspension stiffness force vector** — 后悬架刚度力 `[-2000, -1000, 0, 1000, 2000]` `N`（默认）| 递增向量

后悬架的刚度力。将查找表的输出值指定为向量。输出向量中的元素数量必须与输入向量中的元素数量相同。输入向量参数是 **Rear suspension deformation vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Rear suspension deformation vector** — 后悬架变形 `[-.4, -.2, 0, .2, .4]` `m`（默认）| 递增向量

按位移指定的后悬架变形。将查找表的输入值指定为向量。向量中元素的值必须从左到右递增。向量中的最小元素数量取决于所选的插值方法。对于线性插值，请至少提供两个元素。对于平滑插值，请至少提供三个元素。输出向量参数是 **Rear suspension stiffness force vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Rear suspension damping force vector** — 后悬架阻尼力 `[-200, -100, 0, 100, 200]` `N`（默认）| 递增向量

后悬架的阻尼力。将查找表的输出值指定为向量。输出向量中的元素数量必须与输入向量中的元素数量相同。输入向量参数是 **Rear suspension velocity vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Rear suspension velocity vector** — 后悬架速度 `[-4, -2, 0, 2, 4]` `m/s`（默认）| 递增向量

后悬架的速度。将查找表的输入值指定为向量。向量中元素的值必须从左到右递增。向量中的最小元素数量取决于所选的插值方法。对于线性插值，请至少提供两个元素。对于平滑插值，请至少提供三个元素。输出向量参数是 **Rear suspension damping force vector** 参数。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法包括：

- `Linear` — 选择此默认选项以获得最佳性能。每个维度至少提供两个值。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。每个维度至少提供三个值。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Extrapolation method** — 外插方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外插方法包括：

- `Linear` — 在外插区域以及与插值区域的边界处生成具有连续一阶导数的曲线。
- `Nearest` — 生成不高于数据中最高点或不低于数据中最低点的外插。
- `Error` — 如果输入信号超出表的范围，则发出错误。当希望数据位于表范围内时，选择此选项以避免进入外插模式。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**，并将 **Suspension model** 设置为 `By table lookup`。

### **Hard stop** — 硬限位建模选项 `off`（默认）| `on`

用于对前悬架和后悬架硬限位建模的选项。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**。

### **Front upper bound** — 硬限位前悬架上界 `.25`（默认）| 正标量

前悬架硬限位的上界。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Front lower bound** — 车辆前下界 `-.25`（默认）| 负标量

前悬架硬限位的下界。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Front contact stiffness** — 车辆前接触刚度 `1e6`（默认）| 正标量

前悬架硬限位的接触刚度。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Front contact damping** — 车辆前接触阻尼 `150`（默认）| 正标量

前悬架硬限位的接触阻尼。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Rear upper bound** — 车辆后上界 `.25`（默认）| 正标量

后悬架硬限位的上界。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Rear lower bound** — 车辆后下界 `-.25`（默认）| 负标量

后悬架硬限位的下界。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Rear contact stiffness** — 车辆后接触刚度 `1e6`（默认）| 正标量

后悬架硬限位的接触刚度。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Rear contact damping** — 车辆后接触阻尼 `150`（默认）| 正标量

后悬架硬限位的接触阻尼。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics** 和 **Hard stop**。

### **Initial pitch** — 仿真开始时的俯仰角 `0` `rad`（默认）| 非负标量

仿真开始时的俯仰角。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**。

### **Initial pitch rate** — 仿真开始时的俯仰角速度 `0` `rad/s`（默认）| 非负标量

仿真开始时的俯仰角速度。

#### 依赖关系

要启用此参数，请选择 **Pitch dynamics**。

## 所属库

Simscape / Driveline / Tires & Vehicles

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2011a 中引入**

### R2024b：跟踪由空气动力阻力耗散的功率

该模块现在将 `power_dissipated` 记录到 `simlog` 工作区变量中，它表示由空气动力阻力耗散的功率。

### R2024b：使用物理信号控制阻力

要使用端口 **CD** 处的物理信号控制阻力系数，请选择 **Variable drag coefficient**。

## 描述

纵向运动的两轴车身

Vehicle Body 模块表示纵向运动的两轴车身。车辆可以在每个轴上具有相同或不同数量的车轮。例如，前轴有两个车轮，后轴有一个车轮。假设车辆车轮尺寸相同。车辆也可以具有位于或低于行驶平面的重心 (CG)。

该模块考虑车身质量、空气动力阻力、道路倾斜度以及由加速度和道路剖面引起的轴间重量分布。可选地包括俯仰和悬架动力学。车辆不会相对于地面垂直移动。

该模块提供了包含外部定义的质量和外部定义的惯性的选项。车身质量、惯性和重心可以在仿真过程中响应系统变化而变化。您还可以选择使用物理信号控制阻力系数。

### 模型

车辆各轴平行并形成一个平面。纵向 *x* 方向位于该平面内，并且垂直于各轴。如果车辆在坡道 *β* 上行驶，则法向 *z* 方向不平行于重力，但始终垂直于车轴-纵向平面。

此图和表定义了车辆运动模型变量。

**车辆动力学与运动**

倾斜车身示意图

**车辆模型变量**

| 符号 | 描述 |
| --- | --- |
| *g* | **Gravitational acceleration** 参数。 |
| *β* | 道路倾斜角，参数 **beta**。 |
| *m* | 车辆的质量，由 **Mass** 参数或端口 **M** 指定。 |
| *h* | 车辆重心 (CG) 高于地面的高度。 |
| *a*, *b* | 前轴和后轴分别距车辆 CG 在公共轴平面上的法向投影点的距离。 |
| *Vx* | 车辆的速度。当 *Vx* > 0 时，车辆向前运动。当 *Vx* < 0 时，车辆向后运动。 |
| *Vw* | 风速。当 *Vw* > 0 时，风为逆风。当 *Vw* < 0 时，风为顺风。 |
| *n* | **Number of wheels per axle** 参数。您可以使用整数或二元素向量，其中元素分别表示前轴和后轴。 |
| *Fxf*, *Fxr* | 分别作用在前、后接地点处每个车轮上的纵向力。 |
| *Fzf*, *Fzr* | 分别作用在前、后接地点处每个车轮上的法向载荷力。 |
| *A* | 有效的车辆正面横截面积。 |
| *Cd* | 空气动力阻力系数。 |
| *ρ* | 空气的质量密度。 |
| *Fd* | 空气动力阻力。 |

### 方程

**车辆动力学**

车辆运动是作用在其上的所有力和力矩净效应的结果。纵向轮胎力推动车辆向前或向后。车辆的重量 *mg* 通过其重心 (CG) 起作用。根据倾斜角，重量将车辆拉向地面，并将其向后或向前拉动。无论车辆向前还是向后行驶，空气动力阻力都会使其减速。为简单起见，假设阻力通过 CG 作用。

mV˙x=Fx−​ Fd−mg⋅sinβ

Integer nFx=n(Fxf+Fxr)Vector nFx=n(1)Fxf+n(2)Fxr

Fd=12CdρA(Vx+Vw)2⋅sgn(Vx+Vw)

零法向加速度和零俯仰力矩决定每个前轮和后轮上的法向力。

Integer nFzf=−h(Fd+mgsinβ+mV˙x)+b⋅mgcosβn(a+b)Vector nFzf=−h(Fd+mgsinβ+mV˙x)+b⋅mgcosβn(1)a+n(2)b

Integer nFzr=+h(Fd+mgsinβ+mV˙x)+a⋅mgcosβn(a+b)Vector nFzr=+h(Fd+mgsinβ+mV˙x)+a⋅mgcosβn(1)a+n(2)b

车轮法向力满足

Integer nFzf+Fzr=mgcosβnVector nn(1)Fzf+n(2)Fzr=mgcosβ

如果您包含外部定义的质量或惯性，则方程会按输入的加权值偏移。

**俯仰动力学**

俯仰加速度取决于三个力矩分量和车辆的惯性：

α=(f⋅h)+(Fzfa)−(Fzrb)J

其中：

- *ɑ* 是俯仰加速度。
- *f* 是纵向力。
- *h* 是沿 *z* 轴测量时的重心高度。
- *J* 是惯性。

如果您为悬架刚度和阻尼选择线性模型，则该模块使用小角度近似进行俯仰计算。如果您选择查表模型，则该模块使用您指定的向量来计算俯仰动力学。有关硬限位方程，请参阅 Translational Hard Stop。

**能量核算**

您可以跟踪由空气动力阻力耗散的功率。`simlog` 工作区变量包含 `power_dissipated` 变量。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。

### 限制与假设

Vehicle Body 模块只允许您对纵向动力学建模，即平行于地面并沿运动方向定向。假设车辆处于俯仰和法向平衡状态。该模块不考虑俯仰或垂直运动。因此，方程假设车轮从不失去接触。此约束可能导致负法向力。
