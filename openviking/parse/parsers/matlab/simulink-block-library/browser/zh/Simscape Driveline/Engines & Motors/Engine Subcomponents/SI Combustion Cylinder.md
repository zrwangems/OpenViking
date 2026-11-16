---
type: simulink-block
title: 'SI Combustion Cylinder'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'sicombustioncylinder'
documentation_source_path: 'ref/sicombustioncylinder.html'
language: zh-CN
chinese_source: worker-translation
---

# SI Combustion Cylinder

## 端口

### 输入

### **IgTrig** — 点火触发输入，unitless 物理信号

与点火触发器关联的物理信号输入。该模块将 `0` 到 `1` 的上升沿视为触发。输入必须返回到 `0`，模块才会接受另一个触发。

### **InjPw** — 喷油器脉冲宽度输入，ms 物理信号

与喷油器打开以喷射燃油的持续时间关联的物理信号输入，单位为毫秒。该模块将此信号乘以 **Injector slope** 参数的值，以计算喷油器在一个脉冲期间释放的燃油量。

#### 依赖关系

要启用此端口，请选择 **Input injector pulse width**。

### **AfrCmd** — 空燃比指令输入，unitless 物理信号

与无量纲空燃比指令关联的物理信号输入。注意，这与汽油的化学计量空燃比不同，该模块将其固定为 `14.6`。

#### 依赖关系

要启用此端口，请清除 **Input injector pulse width**。

### **Pim** — 进气歧管压力输入，kPa 物理信号

与进气歧管关联的物理信号输入，单位为 kPa。当您清除 **Compute air intake dynamics** 时，您通过此端口提供进气歧管压力。您可以使用此端口作为向端口 **Thr** 提供节气门指令的替代方案。

### **InVT** — 进气可变气门正时输入，deg 物理信号

与移动进气门打开和关闭正时的角度关联的物理信号输入，单位为度。正值使正时提前，负值使正时延迟。

#### 依赖关系

要启用此端口，请选择 **Intake Variable Valve Timing**。

### **ExVT** — 排气可变气门正时输入，deg 物理信号

与移动排气门打开和关闭正时的角度关联的物理信号输入，单位为度。负值使正时提前，正值使正时延迟。

#### 依赖关系

要启用此端口，请选择 **Exhaust Variable Valve Timing**。

### **Pback** — 排气背压输入，kPa 物理信号

与排气背压关联的物理信号输入，单位为 kPa。

#### 依赖关系

要启用此端口，请选择 **Input back pressure**。

### **CrkPos** — 曲轴位置，deg 物理信号

与曲轴位置关联的物理信号输入，单位为度。

### **Spd** — 发动机转速，rad/s 物理信号

与发动机转速关联的物理信号输入，单位为 rad/s。

### 输出

### **CylPwr** — 气缸功率，W 物理信号

与气缸功率关联的物理信号输出，单位为 W。

### **Weo** — 发动机出口气体能量流，W 物理信号

与发动机出口气体能量流关联的物理信号输出，单位为 W。

#### 依赖关系

要启用此端口，请选择 **Engine outlet gas energy flow**。

### **Vcyl** — 气缸容积输出，cm^3 物理信号

与气缸容积关联的物理信号输出，单位为 cm3。

#### 依赖关系

要启用此端口，请选择 **Cylinder volume**。

### **Pcyl** — 气缸压力输出，MPa 物理信号

与气缸压力关联的物理信号输出，单位为 MPa。

#### 依赖关系

要启用此端口，请选择 **Cylinder pressure**。

### **Tcyl** — 气缸温度输出，K 物理信号

与气缸温度关联的物理信号输出，单位为 K。

#### 依赖关系

要启用此端口，请选择 **Cylinder temperature**。

### **AFR** — 空燃比输出，unitless 物理信号

与模块在运行期间达到的无量纲空燃比响应关联的物理信号输出。注意，这与汽油的化学计量空燃比不同，该模块将其固定为 `14.6`。

#### 依赖关系

要启用此端口，请选择 **Air-fuel ratio**。

### **AirMassFlow** — 气缸空气质量流量输出，g/s 物理信号

与空气质量流量关联的物理信号输出，单位为 g/s。

#### 依赖关系

要启用此端口，请选择 **Air mass flow** 。

### **FuelMassFlow** — 气缸燃油质量流量输出，g/s 物理信号

与燃油质量流量关联的物理信号输出，单位为 g/s。

#### 依赖关系

要启用此端口，请选择 **Fuel mass flow**。

## 参数

### 机械

### **Number of cylinders as a system** — 串联的总燃烧气缸数 `1`（默认）| positive scalar

连接到单个 Crank Shaft 模块的总燃烧气缸数。此参数的值应与系统中的 SI Combustion Cylinder 模块数相同。

### **Cylinder number** — 气缸编号（串联）`1`（默认）| positive scalar

此 SI Combustion Cylinder 模块的分配编号。每个 SI Combustion Cylinder 模块必须为 **Cylinder number** 使用唯一值。

### **Bore** — 气缸直径 `75.0` `mm`（默认）| positive scalar

活塞气缸的直径。

### **Stroke** — 活塞行程 `84.7` `mm`（默认）| positive scalar

活塞头在气缸内行进的距离。

### **Connecting-rod length** — 连杆长度 `141` `mm`（默认）| positive scalar

活塞连杆从孔中心到孔中心的长度。

### **Compression ratio** — 静态压缩比 `11.0`（默认）| positive scalar

最大气缸容积与最小气缸容积之比。

### 环境

### **Ambient pressure** — 参考空气压力 `101.325` `kPa`（默认）| positive scalar

进入进气的空气压力。

### **Ambient temperature** — 参考温度 `(273.15 + 25)` `K`（默认）| positive scalar

进入进气的空气温度。

### **Ambient air density** — 参考密度 `1.225` `mg/cm^3`（默认）| positive scalar

进入进气的空气密度。

### **Specific gas constant of dry air** — 干空气的比气体常数 `288.1965` `J/(K*kg)`（默认）| positive scalar

干空气的比气体常数。

### 气门

### **Discharge coefficient for intake valve** — 进气门流量系数 `0.5`（默认）| positive scalar

进气门实际流量与理想流量之比。

### **Intake valve open before TDC** — 上止点前的 IVO 曲轴位置 `15` `deg`（默认）| scalar in the range [-360,360]

进气门打开时上止点前的曲轴位置。从上止点沿曲轴旋转相反方向测量到曲轴位置。

### **Intake valve close after BDC** — 下止点后的 IVC 曲轴位置 `50` `deg`（默认）| scalar in the range [-360,360]

进气门关闭时下止点后的曲轴位置。从下止点沿曲轴旋转相同方向测量到曲轴位置。

### **Exhaust valve open before BDC** — 下止点前的 EVO 曲轴位置 `55` `deg`（默认）| scalar in the range [-360,360]

排气门打开时下止点前的曲轴位置。从下止点沿曲轴旋转相反方向测量到曲轴位置。

### **Exhaust valve close after TDC** — 上止点后的 EVC 曲轴位置 `10` `deg`（默认）| scalar in the range [-360,360]

排气门关闭时上止点后的曲轴位置。从上止点沿曲轴旋转相同方向测量到曲轴位置。

### **Intake Variable Valve Timing** — 控制进气 VVT 的选项 `on`（默认）| `off`

控制进气门正时的选项。选择此参数将启用 **InVT** 端口。

### **Exhaust Variable Valve Timing** — 控制排气 VVT 的选项 `on`（默认）| `off`

控制排气门正时的选项。选择此参数将启用 **ExVT** 端口。

### 燃烧

### **Lower heating value for gasoline** — 燃油净热值 `44.3e+6` `J/kg`（默认）

汽油的低热值。此值也称为燃油净热值。

### **Input injector pulse width** — 输入喷油器脉冲宽度的选项 `on`（默认）| `off`

指定喷油器脉冲宽度的选项。选择此参数将启用 **InjPw** 端口。

### **Injector slope** — 喷油器斜率 `6.5` `mg/ms`（默认）| positive scalar

燃油喷油器质量流量的斜率。

#### 依赖关系

要启用此参数，请选择 **Input injector pulse width**。

### **Combustion duration** — 燃烧持续时间 `50` `deg`（默认）| positive scalar

作为曲轴旋转段的燃烧持续时间。

### **Cylinder pressure slow decay time constant** — 气缸压力缓慢衰减速率 `60` `s`（默认）| positive scalar

气缸压力缓慢衰减的时间常数。

### **Cylinder temperature slow decay time constant** — 气缸温度缓慢衰减速率 `600` `s`（默认）| positive scalar

气缸温度缓慢衰减的时间常数。

### 排气

### **Exhaust gas temperature decay time constant** — 排气温度衰减速率 `5` `ms`（默认）| positive scalar

用于指定排气温度衰减的时间常数。

### **Input back pressure** — 背压输入选项 `on`（默认）| `off`

用于输入背压压力常数和速度常数的选项。选择此参数将启用 **Pback** 端口。

### **Back-pressure pressure constant** — 背压的压力常数 `50` `kPa`（默认）| positive scalar

背压压力常数。

#### 依赖关系

要启用此参数，请清除 **Input back pressure**。

### **Back-pressure speed constant** — 背压的速度常数 `6000` `rpm`（默认）| positive scalar

背压速度常数。

#### 依赖关系

要启用此参数，请清除 **Input back pressure**。

### 仿真

### **Engine speed simulation limit** — 最大发动机转速 `8500` `rpm`（默认）| positive scalar

仿真期间允许的最大发动机转速。如果发动机转速超过此值，模块将阻止燃烧。

### **Initial crank position (0-720 deg)** — 初始曲轴位置 `0` `deg`（默认）| scalar in the range [0,720]

仿真开始时的曲轴位置。

### **Initial engine speed** — 初始发动机转速 `0` `rpm`（默认）| nonnegative scalar

仿真开始时发动机的转速。

### 输出

### **Engine outlet gas energy flow** — 输出发动机出口气体能量流的选项 `off`（默认）| `on`

是否从物理信号端口 **Weo** 输出发动机出口气体能量流。

### **Cylinder volume** — 输出气缸容积的选项 `on`（默认）| `off`

是否从物理信号端口 **Vcyl** 输出气缸容积。

### **Cylinder pressure** — 输出气缸压力的选项 `on`（默认）| `off`

是否从物理信号端口 **Pcyl** 输出气缸压力。

### **Cylinder temperature** — 输出气缸温度的选项 `on`（默认）| `off`

是否从物理信号端口 **Tcyl** 输出气缸温度。

### **Air/fuel ratio** — 输出空燃比的选项 `on`（默认）| `off`

是否从物理信号端口 **AFR** 输出空燃比。

### **Air mass flow** — 输出气缸空气质量流量的选项 `on`（默认）| `off`

是否从物理信号端口 **AirMassFlow** 输出进气歧管压力。

### **Fuel mass flow** — 输出燃油质量流量的选项 `on`（默认）| `off`

是否从物理信号端口 **FuelMassFlow** 输出燃油质量流量。

## 所属库

Simscape / Driveline / Engines & Motors / Engine Subcomponents

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
- **Cylinder pressure**
- **Cylinder temperature**
- **Cylinder volume**
- **Engine outlet gas energy flow**
- **Exhaust Variable Valve Timing**
- **Fuel mass flow**
- **Input back pressure**
- **Input injector pulse width**
- **Intake Variable Valve Timing**

这些参数在以前的版本中使用下拉菜单。

### R2024b：仿真 Atkinson 循环

当您调整进气和排气门正时以与 Atkinson 循环对齐时，模块会表现出预期的发动机行为。

## 描述

火花点火、四冲程内燃机气缸

SI Combustion Cylinder 模块表示火花点火、四冲程内燃机气缸的曲轴角解析瞬时压力产生动态。您可以将此模块用作复合内燃机模块（如 Spark Ignition Engine 模块）中的子组件。该模块计算瞬时气缸压力，还提供可选输出以收集附加信息。要获得瞬时扭矩，请将其中一个或多个此类模块与 Crankshaft 模块连接。本页使用以下常见的行业缩写：

- TDC — 上止点
- BDC — 下止点
- IVO — 进气门打开
- IVC — 进气门关闭
- EVO — 排气门打开
- EVC — 排气门关闭
- VVT — 可变气门正时

### 方程

该模块取决于曲轴的角位置 *θ*，其中 TDC 为 0°，曲轴位置可以在 0° 到 720° 范围内。根据此定义，0° 是进气 TDC，360° 是燃烧 TDC。该模块根据曲轴位置计算瞬时气缸容积，使得

V(θ)=Vcl+Vdispl⋅12(la+1−cosθ−(la)2−sin2θ),

其中：

- *Vcl* 是余隙容积。
- *Vdispl* 是排量容积，该模块从 **Bore** 和 **Stroke** 参数获取。
- *l* 是 **Connecting-rod length** 参数。
- *a* 是曲柄半径。

该模块按如下方式计算 *Vcl*

Vcl=Vdisplrc−1,

其中 *rc* 是 **Compression ratio** 参数。*V(θ)* 的时间导数对气缸产生的瞬时功率 *Q(θ)* 进行缩放，使得

Qcyl(θ)=(Pcyl(θ)−Pamb)⋅ddtV(θ),

其中 *Pcyl(θ)* 是作为曲轴位置函数的气缸压力，*Pamb* 是 **Ambient pressure** 参数。用于计算 *Pcyl(θ)* 的模块公式取决于气缸中当前处于冲程循环的哪一部分。

**气门正时与冲程循环**

这些图显示相对于曲轴位置的冲程状态。螺旋线表示曲轴旋转。螺旋线从 IVO 开始，到 EVC 结束。根据正时，可能存在进气门和排气门具有相同状态的重叠时间。当 IVO 发生在 EVC 之前时，发生正重叠。当 EVC 发生在 IVO 之前时，发生负重叠。根据此定义，取决于重叠发生在 TDC 之前、期间还是之后，可以有六种独特的模式。该模块对这些模式进行近似。

一个显示 25 degrees 正重叠的气门正时示例图

此图显示一个典型气门正时场景，其中 IVO 发生在 TDC 前 15 degrees，IVC 发生在 BDC 后 50 degrees。EVO 发生在 BDC 前 55 degrees，EVC 发生在 TDC 后 10 degrees。注意 25 degrees 的正重叠，其中进气门在排气门关闭之前打开。该表演示了六种气门重叠模式。

|  | Before TDC | During TDC | After TDC |
| --- | --- | --- | --- |
| Positive Overlap |  |  |  |
| Negative Overlap |  |  |  |

您可以调整 **Valves** 部分中的参数来表示 Otto cycle 或 Atkinson cycle。汽油发动机通常使用 Otto cycle，因为其在功率和效率之间取得平衡。混合动力发动机和一些现代汽油发动机使用 Atkinson cycle，通过牺牲功率输出来提高燃油效率。对 Spark Ignition Engine 或 SI Combustion Cylinder 模块使用 Atkinson cycle 正时会带来：

- 更小的有效压缩比和更大的膨胀比
- 改善的燃油效率
- 对于给定排量，扭矩和功率降低

该图显示了 Otto cycle 和 Atkinson cycle 的典型正时比较：

Otto cycle 和 Atkinson cycle 之间的气门正时示例。Otto cycle 具有 25 degree 重叠，而 Atkinson cycle 具有 -5 degree 重叠。

**气缸模式**

在正常运行期间，发动机气缸需要最低发动机转速来维持稳定燃烧。然而，在瞬态操作期间，例如使用起动机转动曲轴，气缸完成冲程循环但未达到稳定燃烧。该模块考虑这些低发动机转速相互作用，因此该模块考虑 18 种可能的模式。这些是慢速发动机运行模式：

1. Slow Intake
2. Slow Compression-Expansion
3. Slow Exhaust
4. Slow Positive Overlap Before TDC
5. Slow Positive Overlap During TDC
6. Slow Positive Overlap After TDC
7. Slow Negative Overlap Before TDC
8. Slow Negative Overlap During TDC
9. Slow Negative Overlap After TDC

这些是常规发动机运行模式：

10. Intake
11. Compression-Expansion
12. Exhaust
13. Positive Overlap Before TDC
14. Positive Overlap During TDC
15. Positive Overlap After TDC
16. Negative Overlap Before TDC
17. Negative Overlap During TDC
18. Negative Overlap After TDC

该模块通过使用模式图功能为每个离散模式提供转换约束。该表显示该模块允许哪些转换。

| 模式转换 | 允许的模式 |
| --- | --- |
| Slow ↣ Slow | - 1 ↣ 2 - 2 ↣ 3 - 3 ↣ 4, 5, 6, 7, 8, 9 - 4, 5, 6, 7, 8, 9 ↣ 1 |
| Slow ↣ Regular | - 4, 5, 6, 7, 8, 9 ↣ 10 |
| Regular ↣ Regular | - 10 ↣ 11 - 11 ↣ 12 - 12 ↣ 13, 14, 15, 16, 17, 18 - 13, 14, 15, 16, 17, 18 ↣ 10 |
| Regular ↣ Slow | - 10 ↣ 2 - 11 ↣ 3 - 12 ↣ 4, 5, 6, 7, 8, 9 - 13, 14, 15, 16, 17, 18 ↣ 1 |

该图中的流程图直观地描述了该模块如何在模式之间逐步转换。

**模式转换流程图**

说明表中步骤的转换流程图。

该模块捕获气门正时对有效压缩比的影响，并考虑 IVC 远晚于 BDC 的影响，这会减少充入燃烧气缸的空气量。但是，该模块忽略内部废气再循环。

### 假设和限制

- 该模块忽略爆震和其他燃烧不稳定性。
- 该模块忽略内部和外部废气再循环。
