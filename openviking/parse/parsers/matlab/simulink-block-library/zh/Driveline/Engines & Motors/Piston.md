---
type: simulink-block
title: 'Piston'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'piston'
documentation_source_path: 'ref/piston.html'
language: zh-CN
chinese_source: worker-translation
---

# Piston

## 端口
```yaml
ports:
- name: T
  summary: 归一化发动机节气门开度，无量纲物理信号
  direction: input
- name: FC
  summary: 燃油消耗，kg/s 物理信号
  direction: output
- name: B
  summary: 与活塞容器关联的基座端口，机械旋转
  direction: output
- name: F
  summary: 与曲轴扭矩关联的从动端口，机械旋转
  direction: output
```

### 输入

### **T** — 归一化发动机节气门开度，无量纲物理信号

物理信号输入端口，用于指定发动机节气门设置。
### 输出

### **FC** — 燃油消耗，kg/s 物理信号

物理信号输出端口，返回燃油消耗率。

#### 依赖关系

要启用此端口，请将 **Fuel consumption model** 设置为以下之一。

- `Constant per revolution`
- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`
### 守恒

### **B** — 与活塞容器关联的基座端口，机械旋转

与活塞容器关联的旋转机械守恒端口。

### **F** — 与曲轴扭矩关联的从动端口，机械旋转

连接到发动机曲轴的旋转机械守恒端口。
## 参数
```yaml
parameters:
- name: Cylinder bore
  summary: 活塞缸壁内径 .10 m（默认）| 正标量
  group: 主要
- name: Piston stroke
  summary: 活塞平移行程长度 .06 m（默认）| 正标量
  group: 主要
- name: Piston rod length
  summary: 活塞到曲轴连杆长度 .1 m（默认）| 正标量
  group: 主要
- name: Number of strokes per cycle
  summary: 完成一个燃烧循环的活塞行程数 4（默认）| 正偶标量
  group: 主要
- name: Pressure parameterization
  summary: 用于确定施加到活塞的压力的方法 By crank angle（默认）| By crank angle and throttle | By crank angle, throttle, and crank velocity
  group: 主要
- name: Crank angle vector
  summary: 不同的活塞曲轴转角 [-360, -90, -30, 10, 30, 90, 160, 360] deg（默认）| 向量
  group: 主要
- name: Throttle vector
  summary: 不同的节气门位置 [0, .3, .8, 1]（默认）| 向量
  group: 主要
- name: Crank velocity vector
  summary: 不同的角速度 [0, 1000, 6000] rpm（默认）| 向量
  group: 主要
- name: Pressure vector (gauge)
  summary: 曲轴转角参数化压力 [0, 3, 20, 50, 20, 10, 8, 0] bar（默认）| 向量
  group: 主要
- name: Pressure matrix (gauge)
  summary: 曲轴转角和节气门参数化压力 *M*×*N* 矩阵（默认）| 矩阵
  group: 主要
- name: Pressure 3D matrix (gauge)
  summary: 曲轴转角、节气门和曲轴速度参数化压力 *M*×*N*×*O* 矩阵（默认）| 三维矩阵
  group: 主要
- name: Bearing viscous friction coefficient
  summary: 主轴承和连杆轴承耗散功率的趋势 .001 N*m/(rad/s)（默认）| 正标量
  group: 主要
- name: Offset angle
  summary: 发动机循环中点与上止点之间的角度偏差 0 deg（默认）| 标量
  group: 主要
- name: Initial crank angle
  summary: 仿真开始时的曲轴转角 90 deg（默认）| 标量
  group: 主要
- name: Fuel consumption model
  summary: 燃油消耗的参数化 No fuel consumption（默认）| Constant per revolution | Fuel consumption by speed and torque | Brake specific
    fuel consumption by speed and torque | Brake specific fuel consumption by speed and brake mean effective pressure
  group: 燃油消耗
- name: Fuel consumption per revolution
  summary: 单次曲轴旋转期间消耗的燃油 25 mg/rev（默认）| 标量
  group: 燃油消耗
- name: Speed vector
  summary: 曲轴角速度 [1000, 2000, 3000, 4000, 5000, 6000] rpm（默认）| 向量
  group: 燃油消耗
- name: Torque vector
  summary: 给定速度下施加的扭矩 [0, 80, 160, 200, 240, 320, 360, 400] N*m（默认）| 向量
  group: 燃油消耗
- name: Fuel consumption table
  summary: 给定速度和扭矩组合下的燃油消耗率矩阵 *P*×*Q* 矩阵（默认）| 矩阵
  group: 燃油消耗
- name: Brake mean effective pressure vector
  summary: 产生给定扭矩所需的平均缸压 [0, 250, 500, 625, 750, 1000, 1150, 1250] kPa（默认）
  group: 燃油消耗
- name: Brake specific fuel consumption table
  summary: 制动比燃油消耗率的燃油效率 *P*×*Q* 矩阵（默认）| 矩阵
  group: 燃油消耗
- name: Interpolation method
  summary: 数据点之间的速度和扭矩行为 Linear（默认）| Smooth
  group: 燃油消耗
```

### 主要

### **Cylinder bore** — 活塞缸壁内径 `.10` `m`（默认）| 正标量

活塞缸壁的内径。Piston 模块使用此测量值来计算扭矩表。必须指定大于零的值。

### **Piston stroke** — 活塞平移行程长度 `.06` `m`（默认）| 正标量

活塞从完全缩回位置到完全伸出位置的距离。Piston 模块使用此测量值将活塞上的压力转换为扭矩值。必须指定大于零的值。

### **Piston rod length** — 活塞到曲轴连杆长度 `.1` `m`（默认）| 正标量

活塞销孔中心到活塞杆中曲轴孔中心的距离。该模块使用此测量值将活塞上的压力转换为扭矩。必须指定大于零的值。

### **Number of strokes per cycle** — 完成一个燃烧循环的活塞行程数 `4`（默认）| 正偶标量

进气、压缩、燃烧和排气燃烧气体所需的活塞阶段数。通常，发动机为二冲程或四冲程。必须使用二的倍数。

### **Pressure parameterization** — 用于确定施加到活塞的压力的方法 `By crank angle`（默认）| `By crank angle and throttle` | `By crank angle, throttle, and crank velocity`

希望模块用于参数化压力数据的参数组。

### **Crank angle vector** — 不同的活塞曲轴转角 `[-360, -90, -30, 10, 30, 90, 160, 360]` `deg`（默认）| 向量

活塞曲轴转角，从大于或等于最小角度开始，到小于或等于最大角度结束。可以通过将行程数分别乘以 -90 度或 90 度来计算最小或最大角度。必须指定至少两个值。

**Crank angle vector** 中的每个元素对应于 **Pressure vector (gauge)** 中的一个元素，或 **Pressure matrix (gauge)** 的 *M* 行，或每个 **Pressure 3D matrix (gauge)** 矩阵。

### **Throttle vector** — 不同的节气门位置 `[0, .3, .8, 1]`（默认）| 向量

与 **Pressure matrix (gauge)** 或 **Pressure 3D matrix (gauge)** 参数中的压力对应的不同节气门位置。节气门位置必须保持在 [0,1] 范围内，0 表示无节气门，1 表示全节气门。

**Throttle vector** 中的每个元素对应于 **Pressure matrix (gauge)** 的 *N* 列，或每个 **Pressure 3D matrix (gauge)** 矩阵。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle and throttle` 或 `By crank angle, throttle, and crank velocity`。

### **Crank velocity vector** — 不同的角速度 `[0, 1000, 6000]` `rpm`（默认）| 向量

与 **Pressure 3D matrix (gauge)** 中的压力对应的不同曲轴速度。

**Crank velocity vector** 中的每个元素对应于 **Pressure 3D matrix (gauge)** 的一个 *O* 矩阵。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle, throttle, and crank velocity`。

### **Pressure vector (gauge)** — 曲轴转角参数化压力 `[0, 3, 20, 50, 20, 10, 8, 0]` `bar`（默认）| 向量

对应于不同曲轴转角位置的压力值向量。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle`。

### **Pressure matrix (gauge)** — 曲轴转角和节气门参数化压力 *M*×*N* 矩阵（默认）| 矩阵

对应于不同曲轴转角和节气门组合的压力值矩阵。默认值为 `[0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0]` `bar`。

**Crank angle vector** 的元素对应于 **Pressure matrix (gauge)** 的 *M* 行。**Throttle vector** 的元素对应于 **Pressure matrix (gauge)** 的 *N* 列。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle and throttle`。

### **Pressure 3D matrix (gauge)** — 曲轴转角、节气门和曲轴速度参数化压力 *M*×*N*×*O* 矩阵（默认）| 三维矩阵

对应于各种曲轴转角、节气门和曲轴速度组合的压力值拼接矩阵。默认值为 `cat(3, [0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0], [0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0], [0, 0, 0, 0; 0, .9, 2.4, 3; 0, 6, 16, 20; 0, 15, 40, 50; 0, 6, 16, 20; 0, 3, 8, 10; 0, 2.4, 6.4, 8; 0, 0, 0, 0])` `bar`。

**Crank angle vector** 的元素对应于 *M* 行。**Throttle vector** 的元素对应于 *N* 列。**Crank velocity vector** 的元素对应于沿维度 *O* 拼接的矩阵。

默认情况下，*M* = 8，*N* = 4，*O* = 3。

#### 依赖关系

要启用此参数，请将 **Pressure parameterization** 设置为 `By crank angle, throttle, and crank velocity`。

### **Bearing viscous friction coefficient** — 主轴承和连杆轴承耗散功率的趋势 `.001` `N*m/(rad/s)`（默认）| 正标量

主轴承和连杆轴承的总粘性摩擦系数。该模块使用此参数来计算基座轴和从动轴之间的粘性功率损耗。

### **Offset angle** — 发动机循环中点与上止点之间的角度偏差 `0` `deg`（默认）| 标量

活塞到达上止点时发动机循环中的点。发动机循环的角度范围从 -*S*\*180 到 +*S*\*180 度，其中 *S* 是 **Number of strokes per cycle** 参数的值。

### **Initial crank angle** — 仿真开始时的曲轴转角 `90` `deg`（默认）| 标量

相对于上止点位置，时间零点的曲轴转角。

### 燃油消耗

### **Fuel consumption model** — 燃油消耗的参数化 `No fuel consumption`（默认）| `Constant per revolution` | `Fuel consumption by speed and torque` | `Brake specific fuel consumption by speed and torque` | `Brake specific fuel consumption by speed and brake mean effective pressure`

用于计算燃油消耗的模型。模型参数化与标准工业数据兼容。

选择除 `No fuel consumption` 以外的任何选项都会启用 **FC** 端口及相关参数。当将 **Fuel consumption model** 设置为 `No fuel consumption` 时，模块不计算燃油消耗。选择此选项可提高仿真速度。

### **Fuel consumption per revolution** — 单次曲轴旋转期间消耗的燃油 `25` `mg/rev`（默认）| 标量

一次曲轴旋转中消耗的燃油量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption model** 设置为 `Constant per revolution`。

### **Speed vector** — 曲轴角速度 `[1000, 2000, 3000, 4000, 5000, 6000]` `rpm`（默认）| 向量

用于查找表参数化的发动机速度向量。向量长度必须与 **Torque vector** 匹配。

#### 依赖关系

要启用此参数，请将 **Fuel consumption model** 设置为以下之一：

- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`

### **Torque vector** — 给定速度下施加的扭矩 `[0, 80, 160, 200, 240, 320, 360, 400]` `N*m`（默认）| 向量

用于查找表参数化的发动机扭矩向量。向量长度必须与 **Speed vector** 参数匹配。

#### 依赖关系

要启用此参数，请将 **Fuel consumption model** 设置为 `Fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and torque`。

### **Fuel consumption table** — 给定速度和扭矩组合下的燃油消耗率矩阵 *P*×*Q* 矩阵（默认）| 矩阵

对应于发动机速度和扭矩向量的燃油消耗率矩阵。行数 *P* 必须等于 **Speed vector** 参数中的元素数。列数 *Q* 必须等于 **Torque vector** 参数中的元素数。默认值为 `[.5, .9, 1.4, 1.6, 1.9, 2.7, 3.4, 4.4; 1, 1.7, 2.7, 3.1, 3.6, 5, 6, 7.4; 1.4, 2.7, 4, 4.8, 5.6, 7.5, 8.5, 10.5; 2, 3.6, 5.8, 6.7, 8, 10.4, 11.7, 13.3; 2.5, 4.8, 7.9, 9.4, 10.8, 14, 16.2, 18.6; 3.1, 6, 10.3, 11.9, 13.8, 18.4, 22, 26.5]` `g/s`。

#### 依赖关系

要启用此参数，请将 **Fuel consumption model** 设置为 `Fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and torque`。

### **Brake mean effective pressure vector** — 产生给定扭矩所需的平均缸压 `[0, 250, 500, 625, 750, 1000, 1150, 1250]` `kPa`（默认）

制动平均有效压力（BMEP）值向量。BMEP 满足以下表达式：

BMEP=T⋅(2π⋅ncVd)，

其中：

- *T* 是输出扭矩。
- *nc* 是每转的循环数。
- *Vd* 是气缸排量。

#### 依赖关系

要启用此参数，请将 **Fuel consumption model** 设置为 `Fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Brake specific fuel consumption table** — 制动比燃油消耗率的燃油效率 *P*×*Q* 矩阵（默认）| 矩阵

制动比燃油消耗率（BSFC）矩阵。BSFC 是燃油消耗率与输出功率的比值。行数 *P* 必须等于 **Speed vector** 参数中的元素数。列数 *Q* 必须等于 **Torque vector** 参数中的元素数。默认值为 `[410, 380, 300, 280, 270, 290, 320, 380; 410, 370, 290, 270, 260, 270, 285, 320; 415, 380, 290, 275, 265, 270, 270, 300; 420, 390, 310, 290, 285, 280, 280, 285; 430, 410, 340, 320, 310, 300, 310, 320; 450, 430, 370, 340, 330, 330, 350, 380]` `g/hr/kW`。

当将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and torque` 时，输入一个与发动机速度和扭矩向量对应的 BSFC 率矩阵。

当将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and brake mean effective pressure` 时，输入一个与发动机速度和制动平均有效压力（BMEP）向量对应的 BSFC 率矩阵。行数必须等于 **Speed vector** 参数中的元素数。列数必须等于 **Brake mean effective pressure vector** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **Fuel consumption model** 设置为 `Brake specific fuel consumption by speed and torque` 或 `Brake specific fuel consumption by speed and brake mean effective pressure`。

### **Interpolation method** — 数据点之间的速度和扭矩行为 `Linear`（默认）| `Smooth`

用于计算中间速度和扭矩值下燃油消耗的插值方法。在数据范围之外，两种方法的燃油消耗都保持在查找表中给出的最后一个值不变。

#### 依赖关系

要启用此参数，请将 **Fuel consumption model** 设置为以下之一：

- `Fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and torque`
- `Brake specific fuel consumption by speed and brake mean effective pressure`
## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

往复式内燃机的活塞机构

Piston 模块表示往复式内燃机的活塞机构。Piston 模块考虑了传递到发动机曲轴的瞬时扭矩，使您能够仿真由于活塞旋转引起的传动系统振动。要对多活塞发动机建模，请使用 Piston Engine 模块。

端口 **B** 表示活塞容器（如发动机缸体），端口 **F** 表示旋转曲轴。活塞力来自缸压和横截面积。该模块从以曲轴转角参数化的查找表获取燃烧压力，并可选地以曲轴角速度和发动机节气门开度参数化。

曲轴扭矩来自活塞力和曲轴转角、曲轴和连杆长度。根据这些输入，活塞力与曲轴扭矩的比值为

TFFB=−c(sin(θ)+sin(2θ)2(rc)2−sin2(θ))，

其中：

- *FB* 是与基座端口关联的瞬时活塞力。
- *TF* 是与从动端口关联的瞬时曲轴扭矩。
- *c* 是曲轴长度。
- *θ* 是瞬时曲轴转角。
- *r* 是连杆长度。

**活塞尺寸**

端口 **T** 允许您将发动机节气门开度指定为 0 到 1 之间的小数。该小数对应于产生的全功率百分比。当模块属性检查器中的压力查找表仅以曲轴转角参数化时，模块使用点 **T** 处的数据。
