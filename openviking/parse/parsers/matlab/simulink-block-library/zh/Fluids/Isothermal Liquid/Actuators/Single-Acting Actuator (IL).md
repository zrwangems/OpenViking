---
type: simulink-block
title: 'Single-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'singleactingactuatoril'
documentation_source_path: 'ref/singleactingactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Single-Acting Actuator (IL)

## 端口
```yaml
ports:
- name: p
  summary: 多体活塞位置输入，m 物理信号
  direction: input
- name: p
  summary: 活塞位置，m 物理信号
  direction: output
- name: A
  summary: 液体端口 等温液体
  direction: output
- name: C
  summary: 执行器壳体 平移机械
  direction: output
- name: R
  summary: 执行器活塞 平移机械
  direction: output
```

### 输入

### **p** — 多体活塞位置输入，m 物理信号

与活塞位置相关联的物理信号输入端口，单位为 m。
将此端口连接到 Simscape
Multibody 模块。

#### 依赖关系

要启用此端口，请将 **Piston displacement**
设置为 `Provide input signal from Multibody
joint`。
### 输出

### **p** — 活塞位置，m 物理信号

活塞位置，单位为 m，以物理信号形式返回。

#### 依赖关系

要显示此端口，请将 **Piston displacement**
设置为 `Calculate from velocity of port R relative to port
C`。
### 守恒

### **A** — 液体端口 等温液体

与腔室 A 相关联的热液体守恒端口。

### **C** — 执行器壳体 平移机械

与执行器壳体相关联的平移机械守恒端口。

### **R** — 执行器活塞 平移机械

与执行器活塞相关联的平移机械守恒端口。
## 参数
```yaml
parameters:
- name: Mechanical orientation
  summary: 活塞位移方向 Pressure at A causes positive displacement of R relative to C（默认）| Pressure at A causes negative displacement
    of R relative to C
  group: 执行器
- name: Piston cross-sectional area
  summary: 活塞杆横截面积 0.01 m^2（默认）| 正标量
  group: 执行器
- name: Piston stroke
  summary: 最大活塞行程距离 0.1m（默认）| 正标量
  group: 执行器
- name: Dead volume
  summary: 活塞完全缩回时的流体体积 1e-5 m^3（默认）| 正标量
  group: 执行器
- name: Environment pressure specification
  summary: 参考环境压力 Atmospheric pressure（默认）| Specified pressure
  group: 执行器
- name: Environment pressure
  summary: 用户定义的环境压力 0.101325 MPa（默认）| 正标量
  group: 执行器
- name: Hard stop model
  summary: 选择硬限位模型 Stiffness and damping applied smoothly through transition region, damped rebound（默认）| Full stiffness and
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
  summary: 硬限位力模型的作用范围 0.1 mm（默认）| 正标量
  group: 硬限位
- name: Coefficient of restitution
  summary: 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 0.7（默认）| 0 到 1 之间的无单位值
  group: 硬限位
- name: Static contact speed threshold
  summary: 碰撞前滑块与限位之间的阈值相对速度 0.001 m/s（默认）| 非负标量
  group: 硬限位
- name: Static contact release force threshold
  summary: 从接触模式过渡到自由模式所需的阈值力 0.001 N（默认）| 正标量
  group: 硬限位
- name: Cylinder end cushioning
  summary: 是否对活塞在最大伸出时进行减速建模 off（默认）| on
  group: 缓冲
- name: Cushion plunger cross-sectional area
  summary: 缸体缓冲柱塞面积 1e-4 m^2（默认）| 正标量
  group: 缓冲
- name: Cushion plunger length
  summary: 缓冲柱塞长度 1e-3 m（默认）| 正标量
  group: 缓冲
- name: Cushion orifice area
  summary: 缓冲腔之间的节流孔面积 1e-6 m^2（默认）| 正标量
  group: 缓冲
- name: Leakage area between plunger and cushion sleeve
  summary: 缓冲柱塞与套筒之间的间隙 1e-7 m^2（默认）| 正标量
  group: 缓冲
- name: Check valve cracking pressure differential
  summary: 缓冲阈值压力 0.01 MPa（默认）| 正标量
  group: 缓冲
- name: Check valve maximum pressure differential
  summary: 缓冲压差最大值 0.1 MPa（默认）| 正标量
  group: 缓冲
- name: Check valve maximum area
  summary: 完全打开的缓冲阀面积 1e-4 m^2（默认）| 正标量
  group: 缓冲
- name: Check valve leakage area
  summary: 完全关闭位置时的缓冲阀间隙面积 1e-10 m^2（默认）| 正标量
  group: 缓冲
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 正标量
  group: 缓冲
- name: Cylinder friction
  summary: 是否对阻碍活塞运动的摩擦力建模 off（默认）| on
  group: 摩擦
- name: Breakaway to Coulomb friction force ratio
  summary: 启动力与库仑摩擦力之比 1.2（默认）| 正标量
  group: 摩擦
- name: Breakaway friction velocity
  summary: 运动阈值 0.1 m/s（默认）| 正标量
  group: 摩擦
- name: Preload force
  summary: 由密封组件引起的缸体初始力 20 N（默认）| 标量
  group: 摩擦
- name: Coulomb friction force coefficient
  summary: 库仑摩擦力系数 1e-6 N/Pa（默认）| 正标量
  group: 摩擦
- name: Viscous friction coefficient
  summary: 粘性摩擦系数 100 N*s/m（默认）| 正标量
  group: 摩擦
- name: Leakage
  summary: 是否对环形泄漏建模 off（默认）| on
  group: 泄漏
- name: Piston-cylinder clearance
  summary: 径向间隙 1e-4 m（默认）| 正标量
  group: 泄漏
- name: Piston head length
  summary: 活塞安装的环形长度 0.01 m（默认）| 正标量
  group: 泄漏
- name: Piston displacement
  summary: 确定活塞位置的方法 Calculate from velocity of port R relative to port C（默认）| Provide input signal from Multibody joint
  group: 初始条件
- name: Initial piston displacement
  summary: 仿真开始时的活塞位置 0 m（默认）| 标量
  group: 初始条件
- name: Enable dynamic compressibility
  summary: 是否对流体可压缩性建模 on（默认）| off
  group: 初始条件
- name: Initial liquid pressure
  summary: 可压缩流体的起始液体压力 0.101325 MPa（默认）| 正标量
  group: 初始条件
- name: Nominal liquid pressure
  summary: 标称工况下的压力 0.101325 MPa（默认）| 标量
  group: 初始条件
```

### 执行器

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

设置活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of
  R relative to C` 时，当端口
  **A** 处的液体体积膨胀时，活塞位移为正。这对应于
  活塞杆伸出。
- `Pressure at A causes negative displacement of
  R relative to C` 时，当端口
  **A** 处的液体体积膨胀时，活塞位移为负。这对应于
  活塞杆缩回。

### **Piston cross-sectional area** — 活塞杆横截面积 `0.01` `m^2`（默认）| 正标量

活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1``m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume** — 活塞完全缩回时的流体体积 `1e-5` `m^3`（默认）| 正标量

当活塞位移为 `0` 时的液体体积。这是
活塞紧靠执行器端盖时的液体体积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric
pressure` 选项将环境压力设置为
0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325` `MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖关系

要启用此参数，请将 **Environment pressure
specification** 设置为 `Specified
pressure`。

### 硬限位

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时所受力的模型选择。有关更多
信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Transition region** — 硬限位力模型的作用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的作用范围。在活塞最大伸出量和活塞最大缩回量的此范围
之外，不应用 **Hard stop model**，并且活塞上
没有额外的力。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹回后，滑块与限位之间的最终相对速度与初始相对速度
之比。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。
当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，
它们保持接触。否则，滑块弹回。为避免对滑块与壳体之间的静态
接触进行建模，请将此参数设置为
`0`。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请将 **Hard stop model**
设置为 `Based on coefficient of
restitution`。

### 缓冲

### **Cylinder end cushioning** — 是否对活塞在最大伸出时进行减速建模 `off`（默认）| `on`

是否对活塞在最大伸出时进行减速建模。有关更多信息，请参阅 Cylinder Cushion (IL)
模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4` `m^2`（默认）| 正标量

执行器缓冲元件内柱塞的面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3` `m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Cushion orifice area** — 缓冲腔之间的节流孔面积 `1e-6` `m^2`（默认）| 正标量

缓冲腔之间节流孔的面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与套筒之间的间隙 `1e-7` `m^2`（默认）| 正标量

缓冲柱塞与套筒之间的间隙面积。此值
通过保持流动的连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01` `MPa`（默认）| 正标量

触发阀操作的阈值压力。当端口 **A** 与
*P*env 之间的压差达到或超过
此参数的值时，缓冲阀开始打开。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Check valve maximum pressure differential** — 缓冲压差最大值 `0.1` `MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供
上限，以使系统压力保持
真实。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Check valve maximum area** — 完全打开的缓冲阀面积 `1e-4` `m^2`（默认）| 正标量

缓冲阀在完全打开位置的横截面积。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Check valve leakage area** — 完全关闭位置时的缓冲阀间隙面积 `1e-10` `m^2`（默认）| 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的
泄漏面积。此值通过保持流动的连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当可变节流孔和单向阀处于
接近打开或接近关闭位置时，为流动响应引入一层渐变
变化。将此值设置为小于 1 的非零值，以提高这些
工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请选中 **Cylinder end
cushioning**。

### 摩擦

### **Cylinder friction** — 是否对阻碍活塞运动的摩擦力建模 `off`（默认）| `on`

是否对阻碍活塞运动的摩擦力建模。该模块考虑库仑
摩擦、Stribeck 摩擦和粘性摩擦。有关更多
信息，请参阅 Cylinder Friction 模块。

### **Breakaway to Coulomb friction force ratio** — 启动力与库仑摩擦力之比 `1.2`（默认）| 正标量

启动力与库仑摩擦力之比。

#### 依赖关系

要启用此参数，请选中 **Cylinder friction**。

### **Breakaway friction velocity** — 运动阈值 `0.1` `m/s`（默认）| 正标量

开始克服摩擦力运动的速度阈值。

#### 依赖关系

要启用此参数，请选中 **Cylinder
friction**。

### **Preload force** — 由密封组件引起的缸体初始力 `20` `N`（默认）| 标量

由密封组件引起的缸体初始力。

#### 依赖关系

要启用此参数，请选中 **Cylinder
friction**。

### **Coulomb friction force coefficient** — 库仑摩擦力系数 `1e-6` `N/Pa`（默认）| 正标量

库仑摩擦力系数。

#### 依赖关系

要启用此参数，请选中 **Cylinder
friction**。

### **Viscous friction coefficient** — 粘性摩擦系数 `100` `N*s/m`（默认）| 正标量

粘性摩擦系数。

#### 依赖关系

要启用此参数，请选中 **Cylinder
friction**。

### 泄漏

### **Leakage** — 是否对环形泄漏建模 `off`（默认）| `on`

是否对参考环境条件下流体腔与活塞储液腔之间的环形泄漏
建模。该泄漏被视为层流。有关更多信息，请参阅 Laminar Leakage (IL)
模块。

### **Piston-cylinder clearance** — 径向间隙 `1e-4` `m`（默认）| 正标量

活塞杆与缸体壳体之间的径向距离。

#### 依赖关系

要启用此参数，请选中 **Leakage**。

### **Piston head length** — 活塞安装的环形长度 `0.01` `m`（默认）| 正标量

活塞头的长度。

#### 依赖关系

要启用此参数，请选中
**Leakage**。

### 初始条件

### **Piston displacement** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from
Multibody joint` 时，该模块可以从 Multibody 模块接收位置，或者在内部计算位置
并在端口 **p** 处报告位置。当机械方向为正时，位置
介于 `0` 与 **Piston stroke**
之间；当机械方向为负时，位置介于 `0` 与
–**Piston stroke** 之间。

### **Initial piston displacement** — 仿真开始时的活塞位置 `0` `m`（默认）| 标量

仿真开始时的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston
displacement** 设置为 `Calculate from velocity
of port R relative to port C`。

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对由流体可压缩性引起的任何流体密度变化建模。当您选中 **Enable dynamic
compressibility** 时，除了压力变化引起的密度变化外，还会计算
由流入模块的质量流量引起的变化。在 Isothermal Liquid Library 中，所有模块都根据压力计算
密度。

### **Initial liquid pressure** — 可压缩流体的起始液体压力 `0.101325` `MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic
compressibility**。

### **Nominal liquid pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的液体压力。当禁用
动态可压缩性时，该模块使用此值来计算质量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic
compressibility** 复选框。
## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数提供了一个新选项。
此选项称为 `Based on coefficient of restitution`，
使用模式图对硬限位进行建模。

## 描述

等温液体系统中的单作用线性执行器

Single-Acting Actuator (IL) 模块表示一种执行器，
它通过伸出-缩回活塞将端口 **A** 处的液体压力转换为端口 **R** 处的机械力
。活塞运动受到硬限位模型的限制。当活塞位置在内部计算时，它会在端口 **p** 处
报告；当位置通过连接到 Simscape™
Multibody™ 关节来设置时，它会作为物理信号在端口 **p** 处接收。

**Initial piston displacement**、**Enable dynamic
compressibility** 和参考环境压力可以修改。
流体惯性和机械惯性未建模。

### 位移

活塞位移以端口 **R** 相对于端口 **C** 的位置来测量。**Mechanical orientation**
标识活塞位移的方向。当腔室体积等于 **Dead
volume** 时，活塞位移为中性，
即 `0`。当位移作为输入接收时，请确保位置的
导数等于活塞速度。当输入从 Translational Multibody Interface 模块
与 Simscape Multibody 关节的连接接收时，会自动满足此条件。

### 硬限位模型

有四种模型可用于对执行器活塞的伸出限位建模。此模块
使用与 Translational Hard Stop 模块类似的公式，并在活塞行程两端对均匀
阻尼和刚度系数进行建模。有关硬限位模型选项的更多
信息，请参阅 Translational Hard Stop 模块。

当活塞处于其上限或下限时，对硬限位力进行建模。
边界区域位于 **Piston stroke** 或 **Piston initial
displacement** 的 **Transition region** 内。在此区域之外，FHardStop=0。

### Cushion

该模块可以对活塞行程两端的缓冲进行建模。选择 **Cylinder end cushioning** 以在活塞接近由 **Piston stroke** 参数定义的最大伸出量时减缓活塞运动。有关气缸缓冲功能的更多信息，请参阅 Cylinder Cushion (IL) 模块。

### Friction

该模块可以对阻碍活塞运动的摩擦力进行建模。当您选择 **Cylinder friction** 时，所产生的摩擦力是 Stribeck、Coulomb 和黏性效应的组合。该模块测量腔室压力与环境压力之间的压差。有关摩擦模型及其限制的更多信息，请参阅 Cylinder Friction (IL) 模块。

### Leakage

您可以选择性地对液体腔与活塞储液腔之间的泄漏进行建模。当您选择 **Leakage** 时，将在活塞与气缸之间建模 Poiseuille 流。该模块使用 Simscape Foundation Library 的 Laminar Leakage (IL) 模块。流量计算如下：

m˙=π128(d04−di4−(d02−di2)2log(d0/di))υL(pA−penv),

其中：

- *ν* 是流体运动黏度。
- *L* 是活塞长度，**p** – *P*0。
- *p*A 是端口 **A** 处的压力。
- *p*env 是环境压力，在 **Environment pressure specification** 参数中选择。

气缸直径 *d*0 为 d0=di+2c，其中 *c* 是 **Piston-cylinder clearance**，活塞直径 *d*i 为 di=4APπ，其中 *A*P 是 **Piston cross-sectional area**。

### Numerically-Smoothed Area and Pressure

您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，则该模块会对缓冲孔口面积和单向阀压力范围进行平滑处理。孔口面积在 **Leakage area between plunger and cushion sleeve** 与 **Cushion plunger cross-sectional area** 参数之间平滑饱和，而阀压力在 **Check valve cracking pressure differential** 与 **Check valve maximum pressure differential** 参数之间饱和。有关更多信息，请参阅 Numerical Smoothing。

### Block Sub-Components

Single-Acting Actuator (IL) 模块由四个 Simscape Foundation 模块和两个 Fluids Library 模块组成：

- Translational Hard Stop
- Laminar Leakage (IL)
- Translational Mechanical Converter (IL)
- Ideal Translational Motion Sensor
- Cylinder Cushion (IL)
- Cylinder Friction (IL)

**Actuator Structural Diagram**
