---
type: simulink-block
title: 'Spark Ignition Engine'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'sparkignitionengine'
documentation_source_path: 'ref/sparkignitionengine.html'
language: zh-CN
chinese_source: worker-translation
---

# Spark Ignition Engine

## 端口

### 输入

### **IgSw** — 点火器开关，二值物理信号

与点火器关联的物理信号输出，其中 `0` 关闭点火器，`1` 打开点火器。

#### 依赖

要启用此端口，请将 **Spark input type** 设置为 `Fixed` 或 `Spark angle`。

### **Pim** — 进气歧管压力输入，kPa 物理信号

与进气歧管关联的物理信号输入，单位为 kPa。当您清除 **Compute air intake dynamics** 时，您通过此端口提供进气歧管压力。您可以使用此端口作为向端口 **Thr** 提供节气门命令的替代方案。

#### 依赖

要启用此端口，请清除 **Compute air intake dynamics**。

### **Thr** — 节气门命令输入，无量纲物理信号

与归一化节气门命令关联的物理信号输入，其中 `0` 表示节气门完全关闭，`1` 表示节气门完全打开。该模块将此输入映射为 `0` 到 `90` 度之间的节气门打开角度。

#### 依赖

要启用此端口，请选择 **Compute air intake dynamics**。

### **InVT** — 进气可变气门正时输入，deg 物理信号

与移动进气门打开和关闭正时的角度关联的物理信号输入，单位为度。正值提前正时，负值延迟正时。

#### 依赖

要启用此端口，请选择 **Intake Variable Valve Timing**。

### **ExVT** — 排气可变气门正时输入，deg 物理信号

与移动排气门打开和关闭正时的角度关联的物理信号输入，单位为度。负值提前正时，正值延迟正时。

#### 依赖

要启用此端口，请设置 **Exhaust Variable Valve Timing**。

### **AfrCmd** — 空燃比命令输入，无量纲物理信号

与无量纲空燃比命令关联的物理信号输入。请注意，这与汽油的化学计量空燃比不同，该模块将其固定为 `14.6`。

#### 依赖

要启用此端口，请选择 **Input air-fuel ratio** 并清除 **Input injector pulse width**。

### **InjPw** — 喷油器脉冲宽度输入，ms 物理信号

与喷油器打开以喷射燃油的持续时间关联的物理信号输入，单位为 ms。该模块将此信号乘以 **Injector slope** 参数的值，以计算喷油器在一个脉冲期间释放的燃油量。

#### 依赖

要启用此端口，请选择 **Input air-fuel ratio** 和 **Input injector pulse width**。

### **SA** — 点火角输入，deg 物理信号

与上止点前点火角关联的物理信号输入，单位为 deg。

#### 依赖

要启用此端口，请将 **Spark input type** 设置为 `Spark angle`。

### **IgTrig** — 点火触发输入，无量纲物理信号

与点火触发器关联的物理信号输入。该模块将 `0` 到 `1` 的上升沿视为触发。输入必须返回到 `0`，模块才会接受另一次触发。

#### 依赖

要启用此端口，请将 **Spark input type** 设置为 `Spark trigger event`。

### **Pback** — 排气背压输入，kPa 物理信号

与排气背压关联的物理信号输入，单位为 kPa。

#### 依赖

要启用此端口，请选择 **Input back pressure**。
### 输出

### **AvrTrq** — 循环平均净指示扭矩输出，N\*m 物理信号

与循环平均净指示扭矩关联的物理信号输出，单位为 Nm。

#### 依赖

要启用此端口，请选择 **Cycle-average net indicated torque**。

### **AvrSpd** — 循环平均转速输出，rad/s 物理信号

与循环平均转速输出关联的物理信号输出，单位为 rad/s。

#### 依赖

要启用此端口，请选择 **Cycle-average speed**。

### **Pim** — 进气歧管压力输出，kPa 物理信号

与进气歧管压力关联的物理信号输出，单位为 kPa。

#### 依赖

要启用此端口，请选择 **Intake manifold pressure**。

### **crkpos** — 曲轴位置输出，deg 物理信号

与曲轴位置关联的物理信号输出，单位为度。

#### 依赖

要启用此端口，请选择 **Crank position**。

### **AirMassFlow** — 气缸空气质量流量输出，g/s 物理信号

与空气质量流量关联的物理信号输出，单位为 g/s。

#### 依赖

要启用此端口，请选择 **Cylinder air mass flow** 。

### **FuelMassFlow** — 气缸燃油质量流量输出，g/s 物理信号

与燃油质量流量关联的物理信号输出，单位为 g/s。

#### 依赖

要启用此端口，请选择 **Cylinder fuel mass flow**。

### **AFR** — 空燃比输出，无量纲物理信号

与该模块在运行期间达到的无量纲空燃比响应关联的物理信号输出。请注意，这与汽油的化学计量空燃比不同，该模块将其固定为 `14.6`。

#### 依赖

要启用此端口，请选择 **Air-fuel ratio**。

### **Vcyl** — 气缸容积输出，cm^3 物理信号

与气缸容积关联的物理信号输出，单位为 cm3。

#### 依赖

要启用此端口，请选择 **Cylinder volume**。

### **Pcyl** — 气缸压力输出，MPa 物理信号

与气缸压力关联的物理信号输出，单位为 MPa。

#### 依赖

要启用此端口，请选择 **Cylinder pressure**。

### **Tcyl** — 气缸温度输出，K 物理信号

与气缸温度关联的物理信号输出，单位为 K。

#### 依赖

要启用此端口，请选择 **Cylinder temperature**。
### 守恒

### **F** — 曲轴传动系连接机械旋转

与曲轴到传动系连接关联的机械旋转守恒端口。在此处包含摩擦和惯性以模拟发动机负载，或直接连接其他传动系元件。

## 参数

### 机械

### **Number of cylinders** — 气缸总数 `Single Cylinder`（默认）| `Two Cylinders` | `Three Cylinders` | `Four Cylinders`

火花点火气缸的数量。

### **Spark angle difference** — 双缸发动机点火角相位 `270` `deg`（默认）| 正标量

双缸发动机的点火角差值。

#### 依赖

要启用此参数，请将 **Number of cylinders** 设置为 `Two Cylinders`。

### **Firing order** — 四缸发动机的点火顺序 `1-3-4-2`（默认）| `1-3-2-4`

四缸发动机的点火顺序。点火顺序因发动机而异，但您对此参数的选择不会影响模块性能。控制器开发需要此信息。

#### 依赖

要启用此参数，请将 **Number of cylinders** 设置为 `Four Cylinders`。

### **Bore** — 气缸直径 `72.5` `mm`（默认）| 正标量

活塞气缸的直径。

### **Stroke** — 活塞行程距离 `80.5` `mm`（默认）| 正标量

活塞头在气缸内行进的距离。

### **Connecting-rod length** — 连杆长度 `141` `mm`（默认）| 正标量

活塞连杆从孔中心到孔中心的长度。

### **Compression ratio** — 静态压缩比 `11.0`（默认）| 正标量

最大气缸容积与最小气缸容积之比。

### 环境

### **Ambient pressure** — 参考空气压力 `101.325` `kPa`（默认）| 正标量

进入进气的空气压力。

### **Ambient temperature** — 参考温度 `298.15` `K`（默认）| 正标量

进入进气的空气温度。

### **Ambient air density** — 参考密度 `1.225` `mg/cm^3`（默认）| 正标量

进入进气的空气密度。

### **Specific gas constant of dry air** — 干空气比气体常数 `288.1965` `J/(K*kg)`（默认）| 正标量

干空气的比气体常数。

### 进气

### **Compute air intake dynamics** — 计算进气动态的选项 `on`（默认）| `off`

是否计算进气动态。选择此参数将启用以下参数：

- **Throttle response time constant**
- **Throttle rest angle**
- **Throttle plate diameter**
- **Throttle leakage area**
- **Intake manifold volume**

### **Throttle response time constant** — 节气门响应时间常数 `0.1` `s`（默认）| 正标量

与发动机对节气门命令的响应速率关联的时间常数。

#### 依赖

要启用此参数，请选择 **Compute air intake dynamics**。

### **Throttle rest angle** — 释放的节气门位置 `3` `deg`（默认）| 正标量

从静止节气门位置到 `0` 度的径向距离。

#### 依赖

要启用此参数，请选择 **Compute air intake dynamics**。

### **Throttle plate diameter** — 节气门板直径 `5` `cm`（默认）| 正标量

节气门体中蝶阀盘的直径。

#### 依赖

要启用此参数，请选择 **Compute air intake dynamics**。

### **Throttle leakage area** — 节气门泄漏面积 `1` `cm^2`（默认）| 非负标量

节气门泄漏的累计面积。

#### 依赖

要启用此参数，请选择 **Compute air intake dynamics**。

### **Intake manifold volume** — 进气歧管容积 `1000` `cm^3`（默认）| 正标量

进气歧管的容积容量。

#### 依赖

要启用此参数，请选择 **Compute air intake dynamics**。

### 气门

### **Discharge coefficient for intake valve** — 进气门流量系数 `0.9`（默认）| 正标量

进气门实际流量与理想流量之比。

### **Intake valve open before TDC** — IVO 曲轴位置 `15` `deg`（默认）| [-360,360] 范围内的标量

进气门打开时上止点前的曲轴位置。从上止点沿曲轴旋转相反方向测量到曲轴位置。

### **Intake valve close after BDC** — IVC 曲轴位置 `50` `deg`（默认）| [-360,360] 范围内的标量

进气门关闭时下止点后的曲轴位置。从下止点沿曲轴旋转相同方向测量到曲轴位置。

### **Exhaust valve open before BDC** — EVO 曲轴位置 `55` `deg`（默认）| [-360,360] 范围内的标量

排气门打开时下止点前的曲轴位置。从下止点沿曲轴旋转相反方向测量到曲轴位置。

### **Exhaust valve close after TDC** — EVC 曲轴位置 `10` `deg`（默认）| [-360,360] 范围内的标量

排气门关闭时上止点后的曲轴位置。从上止点沿曲轴旋转相同方向测量到曲轴位置。

### **Intake Variable Valve Timing** — 进气可变气门正时选项 `on`（默认）| `off`

是否控制进气门正时。选择此参数将启用 **InVT** 端口。

### **Exhaust Variable Valve Timing** — 排气可变气门正时选项 `on`（默认）| `off`

是否控制排气门正时。选择此端口将启用 **ExVT** 端口。

### 燃油

### **Lower heating value for gasoline** — 燃油净热值 `44.3` `MJ/kg`（默认）| 正标量

汽油的低热值。此值也称为燃油净热值。

### **Input air-fuel ratio** — 空燃比参数选项 `on`（默认）| `off`

是否通过 **Air-fuel ratio** 参数或 **AfrCmd** 端口指定空燃比。

### **Air-fuel ratio** — 空燃比 `14.6`（默认）| 正标量

空气与燃油的混合比。

#### 依赖

要启用此参数，请清除 **Input air-fuel ratio**。

### **Input injector pulse width** — 脉冲宽度参数化 `on`（默认）| `off`

是否指定喷油器脉冲宽度。

#### 依赖

要启用此参数，请选择 **Input air-fuel ratio**。

### **Injector slope** — 喷油器斜率 `6.5` `mg/ms`（默认）| 正标量

燃油喷油器质量流量的斜率。

#### 依赖

要启用此参数，请选择 **Input air-fuel ratio** 和 **Input injector pulse width**。

### 燃烧

### **Spark input type** — 点火输入类型 `Fixed`（默认）| `Spark angle` | `Spark trigger event`

是否使用固定值、点火角或点火触发事件来参数化点火输入。

### **Spark advance BTDC** — 上止点前点火提前角 `20` `deg`（默认）| 正标量

上止点前的点火提前角。

### **Combustion duration** — 燃烧持续时间 `50` `deg`（默认）| 正标量

燃烧持续时间占曲轴旋转的比例。

### **Cylinder pressure slow decay time constant** — 气缸压力缓慢衰减速率 `60` `s`（默认）| 正标量

气缸压力缓慢衰减的时间常数。

### **Cylinder temperature slow decay time constant** — 气缸温度缓慢衰减速率 `600` `s`（默认）| 正标量

气缸温度缓慢衰减的时间常数。

### 排气

### **Exhaust gas temperature decay time constant** — 排气温度衰减速率 `5` `ms`（默认）| 正标量

排气温度衰减的时间常数。

### **Input back pressure** — 背压输入选项 `on`（默认）| `off`

输入背压压力常数和转速常数的选项。

### **Back-pressure pressure constant** — 背压的压力常数 `50` `kPa`（默认）| 正标量

背压压力常数。

#### 依赖

要启用此参数，请清除 **Input back pressure**。

### **Back-pressure speed constant** — 背压的转速常数 `6000` `rpm`（默认）| 正标量

背压转速常数。

#### 依赖

要启用此参数，请清除 **Input back pressure**。

### **Compute exhaust manifold temperature** — 计算排气歧管温度的选项 `on`（默认）| `off`

模块是否计算排气歧管温度。选择此参数将启用以下参数：

- **Surface area of exhaust wall**
- **Mass of exhaust wall**
- **Heat capacity of exhaust wall**
- **Time constant of exhaust heat flow**
- **排气外侧的对流换热系数**
- **Radiation constant**
- **Stefan-Boltzmann constant**

### **Surface area of exhaust wall** — 排气壁表面积 `1` `m^2`（默认）| 正标量

排气壁的表面积。此壁仅为与排气接触的内壁的表面积。

#### 依赖

要启用此参数，请选择 **Compute exhaust manifold temperature**。

### **Mass of exhaust wall** — 排气壁总质量 `5` `kg`（默认）

排气壁的质量。

#### 依赖

要启用此参数，请选择 **Compute exhaust manifold temperature**。

### **Heat capacity of exhaust wall** — 排气壁热容量 `100` `J/(K*kg)`（默认）| 正标量

排气壁的热容量。

#### 依赖

要启用此参数，请选择 **Compute exhaust manifold temperature**。

### **Time constant of exhaust heat flow** — 排气热流时间常数 `10` `s`（默认）| 正标量

排气热流速率的时间常数。

#### 依赖

要启用此参数，请选择 **Compute exhaust manifold temperature**。

### **Convective heat transfer coefficient for the outer side of exhaust** — 排气外侧对流换热系数 `100` `W/(K*m^2)`（默认）| 正标量

排气外侧的对流换热系数。

#### 依赖

要启用此参数，请选择 **Compute exhaust manifold temperature**。

### **Radiation constant** — 排气辐射常数 `0.3`（默认）| 正标量

排气的辐射常数。

#### 依赖关系

要启用此参数，请选择 **Compute exhaust
manifold temperature**。

### **Stefan-Boltzmann constant** — 排气 Stefan-Boltzmann 常数 `5.7e-8` `W/(K^4*m^2)`（默认）| 正标量

总排气的 Stefan-Boltzmann 常数。

#### 依赖关系

要启用此参数，请选择 **Compute exhaust
manifold temperature**。

### 仿真

### **Initial intake manifold pressure** — 进气歧管内的初始压力 `101.325` `kPa`（默认）| 正标量

仿真开始时的进气歧管压力。

### **Initial crank position (0-720 CAdeg)** — 初始曲轴位置 `0` `deg`（默认）| 范围 [0,720] 内的标量

仿真开始时的曲轴位置。

### **Initial engine speed** — 初始发动机转速 `0` `rpm`（默认）| 非负标量

仿真开始时发动机的转速。

### **Engine speed simulation limit** — 最大发动机转速 `8500` `rpm`（默认）| 正标量

仿真期间允许的最大发动机转速。如果模块超过此值，将生成错误并停止仿真。

### 输出

### **Engine outlet gas energy flow** — 输出发动机出口气体能量流的选项 `off`（默认）| `on`

是否从物理信号端口 **Weo** 输出发动机出口气体能量流。

### **Cylinder volume** — 输出气缸容积的选项 `on`（默认）| `off`

是否从物理信号端口 **Vcyl** 输出气缸容积。

### **Cylinder pressure** — 输出气缸压力的选项 `on`（默认）| `off`

是否从物理信号端口 **Pcyl** 输出气缸压力。

### **Cylinder temperature** — 输出气缸温度的选项 `on`（默认）| `off`

是否从物理信号端口 **Tcyl** 输出气缸温度。

### **Input air/fuel ratio** — 输出空燃比的选项 `on`（默认）| `off`

是否从物理信号端口 **AFR** 输出空燃比。

### **Air mass flow** — 输出气缸空气质量流量的选项 `on`（默认）| `off`

是否从物理信号端口 **AirMassFlow** 输出进气歧管压力。

### **Fuel mass flow** — 输出燃料质量流量的选项 `on`（默认）| `off`

是否从物理信号端口 **FuelMassFlow** 输出燃料质量流量。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

### R2025a：枚举更新

这些参数现在使用复选框。

- **Air-fuel ratio**
- **Air mass flow**
- **Compute air intake dynamics**
- **Compute exhaust manifold temperature**
- **Crank position**
- **Cycle-average net indicated torque**
- **Cycle-average speed**
- **Cylinder air mass flow**
- **Cylinder fuel mass flow**
- **Cylinder pressure**
- **Cylinder temperature**
- **Cylinder volume**
- **Engine outlet gas energy flow**
- **Exhaust Variable Valve Timing**
- **Fuel mass flow**
- **Input air/fuel ratio**
- **Input back pressure**
- **Input injector pulse width**
- **Intake manifold pressure**
- **Intake Variable Valve Timing**

这些参数在之前的版本中使用下拉菜单。

### R2024b：仿真 Atkinson 循环

当您调整进气和排气门正时以与 Atkinson 循环对齐时，该模块会展示预期的发动机行为。

## 描述

火花点火发动机

Spark Ignition Engine 模块表示自然吸气式火花点火内燃机。该发动机可以是 1 到 4 个气缸的任意配置。此模块是一个复合模块，使用以下模块的子组件实现：

- SI Combustion Cylinder 模块表示单个火花点火燃烧气缸。Spark
  Ignition Engine 模块根据 **Number
  of cylinders** 参数的值控制在子组件实现中使用多少个
  SI Combustion Cylinder 模块。您可以调整气门正时，以适应传统汽油发动机应用以及混合动力电动和插电式混合动力电动车辆应用。
- Ignition Trigger 模块控制
  SI Combustion Cylinder 模块的点火器正时。
- Air Intake 模块向 SI Combustion
  Cylinder 模块提供进气歧管压力。要启用进气实现，请选择 **Compute air intake dynamics**。
- Crank Shaft 模块连接到每个
  SI Combustion Cylinder 模块，以报告曲轴转角分辨的瞬时扭矩。
- Exhaust Manifold Thermal 模块抽象排气歧管的热力学并报告排气歧管的温度。要计算排气歧管热效应，请选择 **Compute exhaust manifold
  temperature**。

许多 Spark Ignition Engine
参数与子组件模块中的参数相同，并且当该模块实现子组件模块时，它使用这些模块中的方程。您可以通过访问子组件模块的参考页来了解有关 Spark Ignition Engine 模块如何使用每个参数的更多信息。您可以查看源代码，使用此模块了解如何创建自己的子组件模块实现。

### 方程

该模块使用发动机组件各自与曲轴位置 *θ* 的关系来推导其性能信息，其中 0 度 ≤ *θ* < 720 度。该模块将曲轴起始位置定义为上止点处的进气冲程。对于四冲程发动机，每个气缸唯一对应一个曲轴位置，其中给定气缸 *i* 的曲轴位置为 *θi*。该模块从 *θ* 推导角速度，如下所示

ω=ddxθ。

无论您仿真多少个气缸，该模块都将第一个气缸 *θ1* =
*θ*。当您将 **Number of cylinders** 设置为 `Two
cylinders` 时，该模块计算
*θ2* 如下

θ2=θ1+Δ,

其中 *Δ* 是 **Spark angle
difference** 参数。

当您将 **Number of cylinders** 设置为 `Three
cylinders` 时，该模块假设气缸均匀定相，使得

θ2=θ1+(1⋅720°3)θ3=θ1+(2⋅720°3)

当您将 **Number of cylinders** 设置为 `Four
cylinders` 时，该模块假设火花角差为 180 度。您可以使用 **Firing
order** 参数选择点火顺序。

### 假设和限制

- 该模块忽略爆震和其他燃烧不稳定性。
- 该模块忽略内部和外部废气再循环。
