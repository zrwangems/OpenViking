---
type: simulink-block
title: 'Double-Acting Actuator (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Actuators'
documentation_page: 'doubleactingactuatorma'
documentation_source_path: 'ref/doubleactingactuatorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (MA)

## 端口
```yaml
ports:
- name: p
  summary: 活塞位置输入，m 物理信号
  direction: input
- name: p
  summary: 活塞位置，m 物理信号
  direction: output
- name: A
  summary: 液体端口 湿空气
  direction: output
- name: B
  summary: 液体端口 湿空气
  direction: output
- name: R
  summary: 执行器活塞 机械平移
  direction: output
- name: C
  summary: 执行器壳体 机械平移
  direction: output
- name: HA
  summary: 传热 热
  direction: output
- name: HB
  summary: 传热 热
  direction: output
```

### 输入

### **p** — 活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入，单位为 m。
将此端口连接到 Simscape
Multibody™ 网络，使用 Translational Multibody
Interface 模块。

#### 依赖

要启用此端口，请将 **Piston displacement from
chamber A cap** 设置为 `Provide input signal
from Multibody joint`。
### 输出

### **p** — 活塞位置，m 物理信号

与活塞位置关联的物理信号端口。

#### 依赖

要启用此端口，请将 **Piston displacement from
chamber A cap** 设置为 `Calculate from velocity
of port R relative to port C`。
### 守恒

### **A** — 液体端口 湿空气

与腔室 A 入口关联的湿空气守恒端口。

### **B** — 液体端口 湿空气

与腔室 B 入口关联的湿空气守恒端口。

### **R** — 执行器活塞 机械平移

与执行器活塞关联的机械平移守恒端口。

### **C** — 执行器壳体 机械平移

与执行器壳体关联的机械平移守恒端口。

### **HA** — 传热 热

与腔室 A 关联的热守恒端口。

### **HB** — 传热 热

与腔室 B 关联的热守恒端口。
## 参数
```yaml
parameters:
- name: Same fluid on both sides
  summary: 在两个腔室中建模相同流体的选项 on（默认）| off
  group: 执行器
- name: Mechanical orientation
  summary: 活塞位移方向 Pressure at A causes positive displacement of R relative to C（默认）| Pressure at A causes negative displacement
    of R relative to C
  group: 执行器
- name: Piston cross-sectional area in chamber A
  summary: 腔室 A 活塞面积 0.01 m^2（默认）| 正标量
  group: 执行器
- name: Piston cross-sectional area in chamber B
  summary: 腔室 B 活塞面积 0.01 m^2（默认）| 正标量
  group: 执行器
- name: Piston stroke
  summary: 最大活塞行程距离 0.1 m（默认）| 正标量
  group: 执行器
- name: Dead volume in chamber A
  summary: 活塞完全缩回时腔室 A 的流体体积 1e-5 m^3（默认）| 正标量
  group: 执行器
- name: Dead volume in chamber B
  summary: 活塞完全缩回时腔室 B 的流体体积 1e-5 m^3（默认）| 正标量
  group: 执行器
- name: Cross-sectional area at port A
  summary: 端口 A 处的面积 0.01 m^2（默认）| 正标量
  group: 执行器
- name: Cross-sectional area at port B
  summary: 端口 B 处的面积 0.01 m^2（默认）| 正标量
  group: 执行器
- name: Environment pressure specification
  summary: 参考环境压力 Atmospheric pressure（默认）| Specified pressure
  group: 执行器
- name: Environment pressure
  summary: 用户定义的环境压力 0.101325 MPa（默认）| 正标量
  group: 执行器
- name: Hard stop model
  summary: 硬限位模型 Stiffness and damping applied smoothly through transition region, damped rebound（默认）| Full stiffness and
    damping applied at bounds, undamped rebound | Full stiffness and damping applied at bounds, damped rebound | Based on
    coefficient of restitution
  group: 硬限位
- name: Hard-stop stiffness coefficient
  summary: 刚度系数 1e10 N/m（默认）| 正标量
  group: 硬限位
- name: Hard-stop damping coefficient
  summary: 阻尼系数 150 N*s/m（默认）| 正标量
  group: 硬限位
- name: Transition region
  summary: 硬限位力模型的应用范围 0.1 mm（默认）| 正标量
  group: 硬限位
- name: Coefficient of restitution
  summary: 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 0.7（默认）| 0 到 1 之间的无单位值
  group: 硬限位
- name: Static contact speed threshold
  summary: 碰撞前滑块与限位之间的阈值相对速度 0.001 m/s（默认）| 非负标量
  group: 硬限位
- name: Static contact release force threshold
  summary: 从接触模式过渡到自由模式所需的力 0.001 N（默认）| 正标量
  group: 硬限位
- name: Piston displacement from chamber A cap
  summary: 确定活塞位置的方法 Calculate from velocity of port R relative to port C（默认）| Provide input signal from Multibody joint
  group: 腔室 A 的初始条件
- name: Initial piston displacement from chamber A cap
  summary: 仿真开始时的活塞位移 0 m（默认）| 标量
  group: 腔室 A 的初始条件
- name: Initial moist air pressure in chamber A
  summary: 仿真开始时的湿空气压力 0.101325 MPa（默认）| 正标量
  group: 腔室 A 的初始条件
- name: Initial moist air temperature in chamber A
  summary: 仿真开始时的湿空气温度 293.15 K（默认）| 标量
  group: 腔室 A 的初始条件
- name: Initial humidity specification in chamber A
  summary: 用于描述初始湿度水平的量 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: 腔室 A 的初始条件
- name: Initial moist air relative humidity in chamber A
  summary: 仿真开始时的相对湿度 0.5（默认）| [0,1] 范围内的标量
  group: 腔室 A 的初始条件
- name: Initial moist air specific humidity in chamber A
  summary: 仿真开始时的比湿度 0.01（默认）| [0,1] 范围内的标量
  group: 腔室 A 的初始条件
- name: Initial moist air water vapor mole fraction in chamber A
  summary: 仿真开始时的水蒸气摩尔分数 0.01（默认）| [0,1] 范围内的标量
  group: 腔室 A 的初始条件
- name: Initial moist air humidity ratio in chamber A
  summary: 仿真开始时的湿度比 0.01（默认）| [0,1] 范围内的标量
  group: 腔室 A 的初始条件
- name: Initial moist air wet-bulb temperature in chamber A
  summary: 仿真开始时的湿球温度 287 K（默认）| 正标量
  group: 腔室 A 的初始条件
- name: Initial trace gas specification in chamber A
  summary: 用于描述初始痕量气体水平的量 Mass fraction（默认）| Mole fraction
  group: 腔室 A 的初始条件
- name: Initial trace gas mass fraction in chamber A
  summary: 仿真开始时痕量气体的质量分数 0.001（默认）| [0,1] 范围内的标量
  group: 腔室 A 的初始条件
- name: Initial trace gas mole fraction in chamber A
  summary: 仿真开始时痕量气体的摩尔分数 0.001（默认）| [0,1] 范围内的标量
  group: 腔室 A 的初始条件
- name: Initial mass ratio of water droplets to moist air in chamber A
  summary: 水滴与湿空气之比 0（默认）| 正标量
  group: 腔室 A 的初始条件
- name: Relative humidity at saturation in chamber A
  summary: 发生冷凝的相对湿度阈值 1（默认）| 正标量
  group: 腔室 A 的初始条件
- name: Water vapor condensation time constant in chamber A
  summary: 冷凝时间尺度 1e-3 s（默认）| 正标量
  group: 腔室 A 的初始条件
- name: Water droplets evaporation time constant in chamber A
  summary: 蒸发时间尺度 1e-3 s（默认）| 正标量
  group: 腔室 A 的初始条件
- name: Fraction of condensate entrained as water droplets in chamber A
  summary: 冷凝物中水滴的比例 1（默认）| [0,1] 范围内的标量
  group: 腔室 A 的初始条件
- name: Initial moist air pressure in chamber B
  summary: 仿真开始时的湿空气压力 0.101325 MPa（默认）| 正标量
  group: 腔室 B 的初始条件
- name: Initial moist air temperature in chamber B
  summary: 仿真开始时的湿空气温度 293.15 K（默认）| 标量
  group: 腔室 B 的初始条件
- name: Initial humidity specification in chamber B
  summary: 用于描述初始湿度水平的量 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: 腔室 B 的初始条件
- name: Initial moist air relative humidity in chamber B
  summary: 仿真开始时的相对湿度 0.5（默认）| [0,1] 范围内的标量
  group: 腔室 B 的初始条件
- name: Initial moist air specific humidity in chamber B
  summary: 仿真开始时的比湿度 0.01（默认）| [0,1] 范围内的标量
  group: 腔室 B 的初始条件
- name: Initial moist air water vapor mole fraction in chamber B
  summary: 仿真开始时的水蒸气摩尔分数 0.01（默认）| [0,1] 范围内的标量
  group: 腔室 B 的初始条件
- name: Initial moist air humidity ratio in chamber B
  summary: 仿真开始时的湿度比 0.01（默认）| [0,1] 范围内的标量
  group: 腔室 B 的初始条件
- name: Initial moist air wet-bulb temperature in chamber B
  summary: 仿真开始时的湿球温度 287 K（默认）| 正标量
  group: 腔室 B 的初始条件
- name: Initial trace gas specification in chamber B
  summary: 用于描述初始微量气体水平的量 Mass fraction（默认）| Mole fraction
  group: 腔室 B 的初始条件
- name: Initial trace gas mass fraction in chamber B
  summary: 仿真开始时微量气体的质量分数 0.001（默认）| [0,1] 范围内的标量
  group: 腔室 B 的初始条件
- name: Initial trace gas mole fraction in chamber B
  summary: 仿真开始时微量气体的摩尔分数 0.001（默认）| [0,1] 范围内的标量
  group: 腔室 B 的初始条件
- name: Initial mass ratio of water droplets to moist air in chamber B
  summary: 水滴与湿空气的质量比 0（默认）| 正标量
  group: 腔室 B 的初始条件
- name: Relative humidity at saturation in chamber B
  summary: 发生冷凝的相对湿度阈值 1（默认）| 正标量
  group: 腔室 B 的初始条件
- name: Water vapor condensation time constant in chamber B
  summary: 冷凝时间尺度 1e-3 s（默认）| 正标量
  group: 腔室 B 的初始条件
- name: Water droplets evaporation time constant in chamber B
  summary: 蒸发时间尺度 1e-3 s（默认）| 正标量
  group: 腔室 B 的初始条件
- name: Fraction of condensate entrained as water droplets in chamber B
  summary: 冷凝物中水滴的比例 1（默认）| [0,1] 范围内的标量
  group: 腔室 B 的初始条件
```

### 执行器

### **Same fluid on both sides** — 在两个腔室中建模相同流体的选项 `on`（默认）| `off`

是否在两个执行器腔室中建模相同的流体。如果选择此参数，执行器将通过两个腔室传播流体属性。清除此参数以将每个腔室建模为不同的流体，其中每个腔室连接到隔离的流体网络。

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C`，当端口
  **A** 处湿空气的体积膨胀时，活塞位移
  为正。此运动
  对应于杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C`，当端口
  **A** 处湿空气的体积膨胀时，活塞位移
  为负。此运动
  对应于杆缩回。

### **Piston cross-sectional area in chamber A** — 腔室 A 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 A 侧活塞杆的横截面积。

### **Piston cross-sectional area in chamber B** — 腔室 B 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 B 侧活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume in chamber A** — 活塞完全缩回时腔室 A 的流体体积 `1e-5 m^3`（默认）| 正标量

腔室 A 中活塞位移为
`0` 时的湿空气体积。此参数为活塞抵靠执行器端盖时的湿空气
体积。

### **Dead volume in chamber B** — 活塞完全缩回时腔室 B 的流体体积 `1e-5 m^3`（默认）| 正标量

腔室 B 中活塞位移为
`0` 时的湿空气体积。此参数为活塞抵靠执行器端盖时的湿空气
体积。

### **Cross-sectional area at port A** — 端口 A 处的面积 `0.01 m^2`（默认）| 正标量

端口 **A** 的横截面积。

### **Cross-sectional area at port B** — 端口 B 处的面积 `0.01 m^2`（默认）| 正标量

端口 **B** 的横截面积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。当您选择
`Atmospheric pressure` 时，模块假定压力为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖

要启用此参数，请将 **Environment pressure
specification** 设置为 `Specified
pressure`。

### 硬限位

### **Hard stop model** — 硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

当活塞处于完全伸出或完全缩回时使用的硬限位模型。有关更多信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为以下设置之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。当活塞的最大伸出或缩回超出此范围时，模块不应用硬限位模型。在这种情况下，活塞上没有额外的力。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹回后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹回。为避免建模滑块与壳体之间的静态接触，请将此参数设置为
`0`。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### 腔室 A 的初始条件

### **Piston displacement from chamber A cap** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input
signal from Multibody joint` 时，模块可以从 Multibody 模块接收位置，或者可以在内部计算位置并在端口
**p** 处报告位置。当机械方向为正时，位置在 `0`
和 **Piston stroke** 参数值之间；当机械方向为负时，位置在 `0`
和 **Piston stroke** 参数值的负值之间。

### **Initial piston displacement from chamber A cap** — 仿真开始时的活塞位移 `0` `m`（默认）| 标量

仿真开始时相对于腔室 A 端盖的活塞位置。

#### 依赖

要启用此参数，请将 **Piston
displacement** 设置为 `Calculate from velocity
of port R relative to port C`。

### **Initial moist air pressure in chamber A** — 仿真开始时的湿空气压力 `0.101325` `MPa`（默认）| 正标量

腔室 A 中仿真开始时的湿空气压力。

### **Initial moist air temperature in chamber A** — 仿真开始时的湿空气温度 `293.15` `K`（默认）| 标量

腔室 A 中仿真开始时的湿空气温度。

### **Initial humidity specification in chamber A** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述腔室 A 中的初始湿空气湿度水平。

### **Initial moist air relative humidity in chamber A** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

腔室 A 中仿真开始时的湿空气相对湿度。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber A** 设置为 `Relative
humidity`。

### **Initial moist air specific humidity in chamber A** — 仿真开始时的比湿度 `0.01`（默认）| [0,1] 范围内的标量

腔室 A 中仿真开始时湿空气的比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber A** 设置为 `Specific
humidity`。

### **Initial moist air water vapor mole fraction in chamber A** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

腔室 A 中仿真开始时湿空气混合物中水蒸气的摩尔分数。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber A** 设置为 `Mole
fraction`。

### **Initial moist air humidity ratio in chamber A** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的标量

腔室 A 中仿真开始时湿空气的湿度比，定义为水蒸气与干空气和痕量气体的质量比。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber A** 设置为 `Humidity
ratio`。

### **Initial moist air wet-bulb temperature in chamber A** — 仿真开始时的湿球温度 `287` `K`（默认）| 正标量

仿真开始时湿空气混合物的湿球温度。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber A** 设置为 `Wet-bulb
temperature`。

### **Initial trace gas specification in chamber A** — 用于描述初始痕量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数来描述仿真开始时腔室 A 中的痕量气体水平。

### **Initial trace gas mass fraction in chamber A** — 仿真开始时痕量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量

腔室 A 中仿真开始时湿空气混合物中痕量气体的质量分数。

#### 依赖

要启用此参数，请将 **Initial trace gas
specification** 设置为 `Mass
fraction`。

### **Initial trace gas mole fraction in chamber A** — 仿真开始时痕量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

腔室 A 中仿真开始时湿空气混合物中痕量气体的摩尔分数。

#### 依赖

要启用此参数，请将 **Initial trace gas
specification in chamber A** 设置为 `Mole
fraction`。

### **Initial mass ratio of water droplets to moist air in chamber A** — 水滴与湿空气之比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

### **Relative humidity at saturation in chamber A** — 发生冷凝的相对湿度阈值 `1`（默认）| 正标量

腔室 A 中发生冷凝的相对湿度阈值。

### **Water vapor condensation time constant in chamber A** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分回到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant in chamber A** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **Fraction of condensate entrained as water droplets in chamber A** — 冷凝物中水滴的比例 `1`（默认）| [0,1] 范围内的标量

湿空气中以水滴形式夹带的冷凝物比例。

### 腔室 B 的初始条件

### **Initial moist air pressure in chamber B** — 仿真开始时的湿空气压力 `0.101325` `MPa`（默认）| 正标量

腔室 B 中仿真开始时的湿空气压力。

### **Initial moist air temperature in chamber B** — 仿真开始时的湿空气温度 `293.15` `K`（默认）| 标量

腔室 B 中仿真开始时的湿空气温度。

### **Initial humidity specification in chamber B** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述腔室 B 中的初始湿空气湿度水平。

### **Initial moist air relative humidity in chamber B** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

腔室 B 中仿真开始时的湿空气相对湿度。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber B** 设置为 `Relative
humidity`。

### **Initial moist air specific humidity in chamber B** — 仿真开始时的比湿度 `0.01`（默认）| [0,1] 范围内的标量

腔室 B 中仿真开始时湿空气的比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber B** 设置为 `Specific
humidity`。

### **Initial moist air water vapor mole fraction in chamber B** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

腔室 B 中仿真开始时湿空气混合物中水蒸气的摩尔分数。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber B** 设置为 `Mole
fraction`。

### **Initial moist air humidity ratio in chamber B** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的标量

腔室 B 中仿真开始时湿空气的湿度比，定义为水蒸气与干空气和痕量气体的质量比。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber B** 设置为 `Humidity
ratio`。

### **Initial moist air wet-bulb temperature in chamber B** — 仿真开始时的湿球温度 `287` `K`（默认）| 正标量

仿真开始时湿空气混合物的湿球温度。

#### 依赖

要启用此参数，请将 **Initial humidity
specification in chamber B** 设置为 `Wet-bulb
temperature`。

### **Initial trace gas specification in chamber B** — 用于描述初始微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数来描述仿真开始时腔室 B 中的微量气体水平。

### **Initial trace gas mass fraction in chamber B** — 仿真开始时微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量

仿真开始时腔室 B 中湿空气混合物中微量气体的质量分数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial trace gas mole fraction in chamber B** — 仿真开始时微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

仿真开始时腔室 B 中湿空气混合物中微量气体的摩尔分数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification in chamber B** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air in chamber B** — 水滴与湿空气的质量比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

### **Relative humidity at saturation in chamber B** — 发生冷凝的相对湿度阈值 `1`（默认）| 正标量

腔室 B 中发生冷凝的相对湿度阈值。

### **Water vapor condensation time constant in chamber B** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分恢复到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant in chamber B** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **Fraction of condensate entrained as water droplets in chamber B** — 冷凝物中水滴的比例 `1`（默认）| [0,1] 范围内的标量

湿空气中以水滴形式夹带的冷凝物比例。
## 所属库

Simscape / Fluids / Moist Air / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的双作用线性执行器

Double-Acting Actuator (MA) 模块对由两个相对的湿空气腔室控制活塞的线性执行器进行建模。该执行器在伸出和缩回行程中产生力。所产生的力取决于两个腔室之间的压力差。

该图显示了执行器的关键组件。端口 **A** 和 **B** 表示湿空气腔室入口。端口 **R** 表示平移执行器活塞，端口 **C** 表示执行器壳体。端口 **HA** 和 **HB** 表示每个湿空气腔室与环境之间的热接口。移动活塞是绝热的。

双作用执行器示意图

### 位移

该模块将活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**Mechanical orientation** 参数确定活塞位移的方向。当腔室 A 的体积等于 **Dead volume in chamber A** 参数的值时，活塞位移为中性，即 `0`。当 **Piston displacement from chamber A cap** 参数为 `Provide input signal from Multibody joint` 时，您使用端口 **p** 输入活塞位移。确保位置信号的导数等于活塞速度。您可以通过使用 Translational Multibody Interface 模块提供活塞位移来确保位置信号的导数等于活塞速度。

活塞运动的方向取决于 **Mechanical orientation** 参数。如果机械方向为正，则当端口 **A** 处的表压为正时，活塞相对于执行器壳体的平移为正。当机械方向为负时，运动方向反转。

### 硬限位

一组硬限位限制活塞的运动范围。该模块使用 Translational Hard Stop 模块的实现，将硬限位视为弹簧-阻尼系统。弹簧刚度系数控制硬限位接触力的恢复分量，阻尼系数控制耗散分量。

硬限位位于活塞行程的远端。如果机械方向为正，则下限位在 *x* = 0 处，上限位在 *x* = +*stroke* 处。如果机械方向为负，则下限位在 *x* = -*stroke* 处，上限位在 *x* = 0 处。

### 模块组合

该模块是基于以下 Simscape™ Foundation 模块的复合组件：

- Translational Mechanical Converter (MA)
- Translational Hard Stop
- Ideal Translational Motion Sensor

构成该模块的元素图。
