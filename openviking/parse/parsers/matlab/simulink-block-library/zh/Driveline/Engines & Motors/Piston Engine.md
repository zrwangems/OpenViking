---
type: simulink-block
title: 'Piston Engine'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'pistonengine'
documentation_source_path: 'ref/pistonengine.html'
language: zh-CN
chinese_source: worker-translation
---

# Piston Engine

## 端口

### 输入

### **T** — 归一化发动机节气门开度，无量纲非负标量

发动机扭矩需求，表示为最大可能扭矩的分数。
### 输出

### **FC** — 燃油消耗率，kg/s 物理信号

发动机消耗的燃油。
### 守恒

### **B** — 与发动机模块机械旋转相关联的基座端口

与发动机模块相关联的旋转机械守恒端口。

### **F** — 发动机曲轴机械旋转

发动机的随动端口。曲轴传递燃烧过程产生的功率。通常，这是您连接离合器和变速器的地方。

## 参数

### 活塞

### **Number of pistons** — 总排量计算 `4`（默认）| 正标量

内燃机中的活塞数量。

### **Offset angle vector** — 每个活塞的上止点偏移 `[0, 180, 360, -180]`（默认）| 向量

活塞偏移角向量。偏移角指定活塞到达上止点时在发动机循环中的位置。发动机循环的角度范围为 -*S*\*180 到 +*S*\*180 度，其中 *S* 是每循环的冲程数。

向量大小必须与活塞数量相同。默认向量对应于四冲程四活塞发动机。

### **Cylinder bore** — 活塞气缸壁的内径 `.10` `m`（默认）| 正标量

活塞气缸壁的内径。该模块使用此测量值来计算扭矩表。您必须指定大于零的值。

### **Piston stroke** — 活塞平移行程的长度 `.06` `m`（默认）| 正标量

活塞从完全缩回位置到完全伸出位置的距离。该模块使用此测量值将活塞上的压力转换为扭矩值。您必须指定大于零的值。

### **Piston rod length** — 活塞到曲轴连杆的长度 `.1` `m`（默认）| 正标量

从活塞销孔中心到活塞杆中曲轴孔中心的距离。该模块使用此测量值将活塞上的压力转换为扭矩。您必须指定大于零的值。

### **Number of strokes per cycle** — 完成一个燃烧循环的活塞冲程数 `4`（默认）| 正偶标量

进气、压缩、燃烧和排气所需活塞阶段的数量。通常，发动机为两冲程或四冲程。您必须使用二的倍数。

### **Pressure parameterization** — 确定施加到活塞的压力 `By crank angle`（默认）| `By crank angle and throttle` | `By crank angle, throttle, and crank velocity`

您希望模块用于参数化压力数据的参数组。

### **Crank angle vector** — 不同的活塞曲柄角 `[-360, -90, -30, 10, 30, 90, 160, 360]` `deg`（默认）| 向量

活塞曲柄的角度，从大于或等于最小角度开始，到小于或等于最大角度结束。您可以通过将冲程数分别乘以 -90 度或 90 度来计算最小或最大角度。您必须指定至少两个值。

**Crank angle vector** 中的每个元素对应于 **Pressure vector (gauge)** 中的一个元素，或 **Pressure matrix (gauge)** 的 *M* 行，或每个 **Pressure 3D matrix (gauge)** 矩阵。

### **Throttle vector** — 不同的节气门位置 `[0, .3, .8, 1]`（默认）| 向量

与 **Pressure matrix (gauge)** 或 **Pressure 3D matrix (gauge)** 参数中的压力相对应的不同节气门位置。节气门位置必须保持在 [0,1] 范围内，其中 0 表示无节气门，1 表示全节气门。

**Throttle vector** 中的每个元素对应于 **Pressure matrix (gauge)** 的 *N* 列，或每个 **Pressure 3D matrix (gauge)** 矩阵。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle and throttle` 或 `By crank angle, throttle, and crank velocity`。

### **Crank velocity vector** — 不同的角速度 `[0, 1000, 6000]` `rpm`（默认）| 向量

与 **Pressure 3D matrix (gauge)** 中的压力相对应的不同曲柄速度。

**Crank velocity vector** 中的每个元素对应于 **Pressure 3D matrix (gauge)** 的一个 *O* 矩阵。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle, throttle, and crank velocity`。

### **Pressure vector (gauge)** — 曲柄角参数化压力 `[0, 3, 20, 50, 20, 10, 8, 0]` `bar`（默认）| 向量

与不同曲柄角位置相对应的压力值向量。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle`。

### **Pressure matrix (gauge)** — 曲柄角和节气门参数化压力 *M*×*N* 矩阵（默认）| 矩阵

与不同曲柄角和节气门组合相对应的压力值矩阵。默认值为 `[0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0]` `bar`。

**Crank angle vector** 的元素对应于 **Pressure matrix (gauge)** 中的 *M* 行。**Throttle vector** 的元素对应于 **Pressure matrix (gauge)** 中的 *N* 列。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle and throttle`。

### **Pressure 3D matrix (gauge)** — 曲柄角、节气门和曲柄速度参数化压力 *M*×*N*×*O* 矩阵（默认）| 三维矩阵

与各种曲柄角、节气门和曲柄速度组合相对应的压力值的拼接矩阵。默认值为 `cat(3, [0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0], [0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0], [0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0])` `bar`。

**Crank angle vector** 的元素对应于 *M* 行。**Throttle vector** 的元素对应于 *N* 列。**Crank velocity vector** 的元素对应于沿维度 *O* 拼接的矩阵。

默认情况下，*M* = 8，*N* = 4，*O* = 3。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle, throttle, and crank velocity`。

### 曲轴

### **Shaft dynamics** — 启用轴动力学建模参数 `No shaft dynamics - Suitable for HIL simulation`（默认）| `Specify shaft stiffness, damping, and inertia`

用于参数化轴动力学的选项。

### **Base and follower bearing viscous friction coefficients** — 表征系统摩擦 `[0, 0]` `deg`（默认）| 向量

基座轴承和随动轴承的粘性摩擦系数，按此顺序。

### **Initial crank angle** — 起始曲柄位置 `90` `deg`（默认）| 标量

相对于上止点位置在时间零点的曲柄角。发动机循环的角度范围为 -*S*\*180 到 +*S*\*180 度，其中 *S* 是每循环的冲程数。

### **Stiffness** — 抗变形能力 `1e6` `N*m/rad`（默认）| 正标量

发动机曲轴的平移弹簧刚度。弹簧刚度考虑了由于材料柔量导致的曲轴中的弹性能量存储。

发动机曲轴的刚度系数。此参数考虑了轴对变形的抗力。

#### 依赖关系

要启用此参数，请将 **Shaft dynamics** 设置为 `Specify shaft stiffness, damping, and inertia`。

### **Damping** — 从系统耗散能量的趋势 `1000` `N*m/(rad/s)`（默认）| 正标量

发动机曲轴的平移阻尼。阻尼考虑了由于材料柔量导致的曲轴中的能量耗散。

#### 依赖关系

要启用此参数，请将 **Shaft dynamics** 设置为 `Specify shaft stiffness, damping, and inertia`。

### **Inertia** — 抵抗运动变化的趋势 `.02` `kg*m^2`（默认）| 正标量

曲轴绕其旋转轴的转动惯量。此参数考虑了运动突然变化的抗力。

#### 依赖关系

要启用此参数，请将 **Shaft dynamics** 设置为 `Specify shaft stiffness, damping, and inertia`。

### **Initial angular deflection** — 角偏转初始化参数 `0` `deg`（默认）

在时间零点曲轴基座端和随动端之间的偏转角。偏转角测量由于扭转导致的曲轴角变形。

#### 依赖关系

要启用此参数，请将 **Shaft dynamics** 设置为 `Specify shaft stiffness, damping, and inertia`。

### **Initial angular velocity** — 角速度初始化参数 `0`（默认）| 标量

在时间零点曲轴的角速度。

#### 依赖关系

要启用此参数，请将 **Shaft dynamics** 设置为 `Specify shaft stiffness, damping, and inertia`。

### 燃油消耗

下表显示了 **Fuel consumption model** 参数的指定选项如何影响依赖参数的可用性。

**燃油消耗参数依赖关系**

| **Fuel Consumption** | | | | |
| --- | --- | --- | --- | --- |
| Fuel consumption model — 选择 `No fuel consumption`、`Constant per revolution`、`Fuel consumption by speed and torque`、`Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure` | | | | |
| **No fuel consumption** | **Constant per revolution** | **Fuel consumption by speed and torque** | **Brake specific fuel consumption by speed and torque** | **Brake specific fuel consumption by speed and brake mean effective pressure** |
| Fuel consumption per revolution |
| Speed vector | | |
| Torque vector | | Brake mean effective pressure vector |
| Fuel consumption table | Brake specific fuel consumption table | |
| Interpolation method — 选择 `Linear` 或 `Smooth` | | |

### **Fuel consumption model** — 启用燃油消耗建模参数 `No fuel consumption`（默认）| `Constant per revolution` | `Fuel consumption by speed and torque` | ...

基于可用数据的燃油消耗模型。选择用于计算发动机燃油消耗的模型。模型参数化与典型工业数据兼容。从以下选项中选择：

- `No fuel consumption` — 默认选项
- `Constant per revolution`
- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

如果您将 **Fuel consumption model** 保留为 `No fuel consumption`，即使 **FC** 端口连接到另一个模块，该模块也不会计算燃油消耗。选择此选项可提高仿真速度。

### **Fuel consumption per piston revolution** — 常数 `25` `mg/rev`（默认）| 正标量

作为曲轴转数函数的恒定燃油消耗率。输入一个曲轴转数中消耗的燃油体积。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Constant per revolution`。

### **Speed vector** — 发动机速度数据 `[1000, 2000, 3000, 4000, 5000, 6000]`（默认）| 向量

与燃油消耗查找表的 *M* 行相对应的发动机扭矩向量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque`、`Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Torque vector** — 发动机扭矩数据 `[0, 80, 160, 200, 240, 320, 360, 400]`（默认）| 向量

与燃油消耗查找表的 *N* 列相对应的发动机扭矩向量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and torque`。

### **Fuel consumption table** — 发动机燃油消耗数据 *M*×*N* 矩阵（默认）| 矩阵

输入与发动机速度和扭矩向量相对应的燃油消耗率矩阵。行数必须等于 **Speed vector** 中的元素数。列数必须等于 **Torque vector** 中的元素数。默认值为 `[.5, .9, 1.4, 1.6, 1.9, 2.7, 3.4, 4.4; 1, 1.7, 2.7, 3.1, 3.6, 5, 6, 7.4; 1.4, 2.7, 4, 4.8, 5.6, 7.5, 8.5, 10.5; 2, 3.6, 5.8, 6.7, 8, 10.4, 11.7, 13.3; 2.5, 4.8, 7.9, 9.4, 10.8, 14, 16.2, 18.6; 3.1, 6, 10.3, 11.9, 13.8, 18.4, 22, 26.5]` `g/s`。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque`。

### **Brake mean effective pressure vector** — 活塞压力数据 `[0, 250, 500, 625, 750, 1000, 1150, 1250]`（默认）| 向量

制动平均有效压力（BMEP）值向量。BMEP 满足以下表达式：

BMEP=T⋅(2π⋅ncVd)，

其中：

- *T* 是输出扭矩。
- *nc* 是每转的循环数。
- *Vd* 是气缸排量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Brake specific fuel consumption table** — 制动比油耗数据 *M*×*N* 矩阵（默认）| 矩阵

对于 `Brake specific fuel consumption by speed and torque` 燃油模型，输入与发动机速度和扭矩向量相对应的制动比油耗（BSFC）率矩阵。BSFC 是燃油消耗率与输出功率的比值。行数必须等于 **Speed vector** 中的元素数。列数必须等于 **Torque vector** 中的元素数。

对于 `Brake specific fuel consumption by speed and brake mean effective pressure` 燃油模型，输入与发动机速度和制动平均有效压力（BMEP）向量相对应的制动比油耗（BSFC）率矩阵。BSFC 是燃油消耗率与输出功率的比值。行数必须等于 **Speed vector** 中的元素数。列数必须等于 **Brake mean effective pressure vector** 中的元素数。

对于两种燃油消耗模型，默认值为 `[410, 380, 300, 280, 270, 290, 320, 380; 410, 370, 290, 270, 260, 270, 285, 320; 415, 380, 290, 275, 265, 270, 270, 300; 420, 390, 310, 290, 285, 280, 280, 285; 430, 410, 340, 320, 310, 300, 310, 320; 450, 430, 370, 340, 330, 330, 350, 380]` `g/hr/kW`。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Interpolation method** — 中间步骤行为 `Linear`（默认）| `Smooth`

用于计算中间速度和扭矩值处燃油消耗的插值方法。在数据范围之外，对于两种方法，燃油消耗保持为查找表中给出的最后一个值不变。

#### 依赖关系

要启用此参数，请将 **Fuel consumption** 设置为 `Fuel consumption by speed and torque`、`Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure`。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

可变活塞数量的往复式内燃机

Piston Engine 模块表示具有多个气缸的往复式内燃机。活塞模型考虑了传递到发动机驱动轴的瞬时扭矩。瞬时扭矩使您能够对由活塞旋转引起的传动系统振动进行建模。若要仅对燃烧发动机的活塞机构进行建模，请使用 Piston 模块。

端口 **B** 表示发动机缸体，端口 **F** 表示旋转曲轴。活塞力由气缸压力和横截面积得出。该模块从以曲柄转角为参数、并可选择以曲柄角速度和发动机节气门开度为参数的查找表中获取燃烧压力。

曲柄扭矩由活塞力、曲柄转角以及曲柄和连杆长度得出。根据这些输入，活塞力与曲柄扭矩之比为

TFFB=−c(sin(θ)+sin(2θ)2(rc)2−sin2(θ)),

其中：

- *FB* 是与 base 端口相关的瞬时活塞力。
- *TF* 是与 follower 端口相关的瞬时曲柄扭矩。
- *c* 是曲柄长度。
- *θ* 是瞬时曲柄转角。
- *r* 是连杆长度。

**活塞尺寸**

物理信号端口 T 允许您以 0 到 1 之间的分数指定发动机节气门开度。该分数对应于所产生的全功率的百分比。当模块属性检查器中的压力查找表仅以曲柄转角为参数时，该模块使用物理信号输入。
