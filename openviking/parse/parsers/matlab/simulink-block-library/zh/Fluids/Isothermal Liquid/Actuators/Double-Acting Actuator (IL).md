---
type: simulink-block
title: 'Double-Acting Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators'
documentation_page: 'doubleactingactuatoril'
documentation_source_path: 'ref/doubleactingactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Acting Actuator (IL)

## 端口
```yaml
ports:
- name: p
  summary: 活塞位置输入，m 物理信号
  direction: input
- name: p
  summary: 活塞位置输出，m 物理信号
  direction: output
- name: A
  summary: 腔室 A 的入口，等温液体
  direction: output
- name: B
  summary: 腔室 B 的入口，等温液体
  direction: output
- name: C
  summary: 执行器壳体，机械平移
  direction: output
- name: R
  summary: 执行器活塞，机械平移
  direction: output
```

### 输入

### **p** — 活塞位置输入，m 物理信号

与活塞位置关联的物理信号输入端口，该活塞位置由您使用 Simscape Multibody 模块指定。

#### 依赖

要显示此端口，请将 **Piston displacement from chamber A cap** 设置为 `Provide input signal from Multibody joint`。
### 输出

### **p** — 活塞位置输出，m 物理信号

与活塞位置关联的物理信号端口。

#### 依赖

要显示此端口，请将 **Piston displacement from chamber A cap** 设置为 `Calculate from velocity of port R relative to port C`。
### 守恒

### **A** — 腔室 A 的入口，等温液体

与腔室 A 入口关联的等温液体守恒端口。

### **B** — 腔室 B 的入口，等温液体

与腔室 B 入口关联的等温液体守恒端口。

### **C** — 执行器壳体，机械平移

与壳体关联的机械平移守恒端口。

### **R** — 执行器活塞，机械平移

与活塞关联的机械平移守恒端口。
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
- name: Environment pressure specification
  summary: 参考环境压力 Atmospheric pressure（默认）| Specified pressure
  group: 执行器
- name: Environment pressure
  summary: 用户定义的环境压力 0.101325 MPa（默认）| 正标量
  group: 执行器
- name: Breakaway to Coulomb friction force ratio
  summary: 分离力与库仑摩擦力之比 1.2（默认）| 正标量
  group: 执行器
- name: Breakaway friction velocity
  summary: 运动阈值 0.1 m/s（默认）| 正标量
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
  summary: 硬限位力模型的应用范围 0.1 mm（默认）| 正标量
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
- name: Cylinder A end cushioning
  summary: 是否建模活塞在最大伸出时的减速 off（默认）| on
  group: 转换器缓冲 A
- name: Cushion plunger cross-sectional area
  summary: 缸体缓冲柱塞面积 1e-4 m^2（默认）| 正标量
  group: 转换器缓冲 A
- name: Cushion plunger length
  summary: 缓冲柱塞长度 1e-3 m（默认）| 正标量
  group: 转换器缓冲 A
- name: Cushion orifice area
  summary: 缓冲腔室之间的节流孔面积 1e-6 m^2（默认）| 正标量
  group: 转换器缓冲 A
- name: Leakage area between plunger and cushion sleeve
  summary: 缓冲柱塞与套筒之间的间隙 1e-7 m^2（默认）| 正标量
  group: 转换器缓冲 A
- name: Check valve cracking pressure differential
  summary: 缓冲阈值压力 0.01 MPa（默认）| 正标量
  group: 转换器缓冲 A
- name: Check valve maximum pressure differential
  summary: 最大缓冲压差 0.1 MPa（默认）| 正标量
  group: 转换器缓冲 A
- name: Check valve maximum area
  summary: 完全打开的缓冲阀面积 1e-4 m^2（默认）| 正标量
  group: 转换器缓冲 A
- name: Check valve leakage area
  summary: 完全关闭位置时缓冲阀间隙面积 1e-10 m^2（默认）| 正标量
  group: 转换器缓冲 A
- name: Cylinder B end cushioning
  summary: 是否建模活塞在最大伸出时的减速 off（默认）| on
  group: 转换器缓冲 B
- name: Cushion plunger cross-sectional area
  summary: 缸体缓冲柱塞面积 1e-4 m^2（默认）| 正标量
  group: 转换器缓冲 B
- name: Cushion plunger length
  summary: 缓冲柱塞长度 1e-3 m（默认）| 正标量
  group: 转换器缓冲 B
- name: Cushion orifice area
  summary: 缓冲腔室之间的节流孔面积 1e-6 m^2（默认）| 正标量
  group: 转换器缓冲 B
- name: Leakage area between plunger and cushion sleeve
  summary: 缓冲柱塞与套筒之间的间隙 1e-7 m^2（默认）| 正标量
  group: 转换器缓冲 B
- name: Check valve cracking pressure differential
  summary: 缓冲阈值压力 0.01 MPa（默认）| 正标量
  group: 转换器缓冲 B
- name: Check valve maximum pressure differential
  summary: 最大缓冲压差 0.1 MPa（默认）| 正标量
  group: 转换器缓冲 B
- name: Check valve maximum area
  summary: 完全打开的缓冲阀面积 1e-4 m^2（默认）| 正标量
  group: 转换器缓冲 B
- name: Check valve leakage area
  summary: 完全关闭位置时缓冲阀间隙面积 1e-10 m^2（默认）| 正标量
  group: 转换器缓冲 B
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 正标量
  group: 转换器缓冲 B
- name: Cylinder friction effect
  summary: 是否建模阻碍活塞运动的摩擦 off（默认）| on
  group: 摩擦
- name: Breakaway to Coulomb friction force ratio
  summary: 分离力与库仑摩擦力之比 1.2（默认）| 正标量
  group: 摩擦
- name: Breakaway friction velocity
  summary: 运动阈值 0.1 m/s（默认）| 正标量
  group: 摩擦
- name: Preload force
  summary: 缸体上的初始力 20 N（默认）| 标量
  group: 摩擦
- name: Coulomb friction force coefficient
  summary: 库仑摩擦力系数 1e-6 N/Pa（默认）| 正标量
  group: 摩擦
- name: Viscous friction coefficient
  summary: 粘性摩擦系数 100 N/(m/s)（默认）| 正标量
  group: 摩擦
- name: Internal leakage
  summary: 是否建模环形泄漏 off（默认）| on
  group: 泄漏
- name: Piston-cylinder clearance
  summary: 径向间隙 1e-4 m（默认）| 正标量
  group: 泄漏
- name: Piston head length
  summary: 活塞安装的环形长度 0.01 m（默认）| 正标量
  group: 泄漏
- name: Piston displacement from chamber A cap
  summary: 确定活塞位置的方法 Calculate from velocity of port R relative to port C（默认）| Provide input signal from Multibody joint
  group: 初始条件
- name: Initial piston displacement from chamber A cap
  summary: 仿真开始时从腔室 A 端盖测量的活塞位置 0 m（默认）| 标量
  group: 初始条件
- name: Enable dynamic compressibility
  summary: 是否对流体可压缩性建模 on（默认）| off
  group: 初始条件
- name: Initial liquid pressure in chamber A
  summary: 腔室 A 中的起始液体压力 0.101325 MPa（默认）| 正标量
  group: 初始条件
- name: Initial liquid pressure in chamber B
  summary: 腔室 B 中的起始液体压力 0.101325 MPa（默认）| 正标量
  group: 初始条件
- name: Nominal liquid pressure in chamber A
  summary: 腔室 A 中额定工况下的压力 0.101325 MPa（默认）| 标量
  group: 初始条件
- name: Nominal liquid pressure in chamber B
  summary: 腔室 B 中额定工况下的压力 0.101325 MPa（默认）| 标量
  group: 初始条件
```

### 执行器

### **Same fluid on both sides** — 在两个腔室中建模相同流体的选项 `on`（默认）| `off`

是否在两个执行器腔室中建模相同的流体。如果选择此参数，执行器将通过两个腔室传播流体属性。清除此参数可将每个腔室建模为不同的流体，其中每个腔室连接到隔离的流体网络。

### **Mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

设置活塞位移方向。当您将此参数设置为：

- `Pressure at A causes positive displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为正。这对应于活塞杆伸出。
- `Pressure at A causes negative displacement of R relative to C` 时，当端口 **A** 处的液体体积膨胀时，活塞位移为负。这对应于活塞杆缩回。

### **Piston cross-sectional area in chamber A** — 腔室 A 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 A 侧活塞杆的横截面积。

### **Piston cross-sectional area in chamber B** — 腔室 B 活塞面积 `0.01 m^2`（默认）| 正标量

腔室 B 侧活塞杆的横截面积。

### **Piston stroke** — 最大活塞行程距离 `0.1 m`（默认）| 正标量

最大活塞行程距离。

### **Dead volume in chamber A** — 活塞完全缩回时腔室 A 的流体体积 `1e-5 m^3`（默认）| 正标量

腔室 A 中活塞位移为 `0` 时的液体体积。这是活塞紧靠执行器端盖时的液体体积。

### **Dead volume in chamber B** — 活塞完全缩回时腔室 B 的流体体积 `1e-5 m^3`（默认）| 正标量

腔室 B 中活塞位移为 `0` 时的液体体积。这是活塞紧靠执行器端盖时的液体体积。

### **Environment pressure specification** — 参考环境压力 `Atmospheric pressure`（默认）| `Specified pressure`

环境参考压力。`Atmospheric pressure` 选项将环境压力设置为 0.101325 MPa。

### **Environment pressure** — 用户定义的环境压力 `0.101325 MPa`（默认）| 正标量

用户定义的环境压力。

#### 依赖

要启用此参数，请将 **Environment pressure specification** 设置为 `Specified pressure`。

### **Breakaway to Coulomb friction force ratio** — 分离力与库仑摩擦力之比 `1.2`（默认）| 正标量

分离力与库仑摩擦力之比。

#### 依赖

要启用此参数，请在 **Friction** 选项卡中选择 **Cylinder friction effect**。

### **Breakaway friction velocity** — 运动阈值 `0.1 m/s`（默认）| 正标量

克服摩擦力开始运动的阈值速度。

#### 依赖

要启用此参数，请在 **Friction** 选项卡中选择 **Cylinder friction effect**。

### 硬限位

### **Hard stop model** — 选择硬限位模型 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | `Full stiffness and damping applied at bounds, damped rebound` | `Based on coefficient of restitution`

活塞在完全伸出或完全缩回时力的模型选择。有关更多信息，请参阅 Translational Hard Stop 模块。

### **Hard-stop stiffness coefficient** — 刚度系数 `1e10` `N/m`（默认）| 正标量

活塞刚度系数。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Hard-stop damping coefficient** — 阻尼系数 `150` `N*s/m`（默认）| 正标量

活塞阻尼系数。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

### **Transition region** — 硬限位力模型的应用范围 `0.1` `mm`（默认）| 正标量

硬限位力模型的应用范围。在活塞最大伸出量和活塞最大缩回量的此范围之外，不应用 **Hard stop model**，活塞上没有额外的力。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001 m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于 **Static contact speed threshold** 参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。要避免建模滑块与壳体之间的静态接触，请将此参数设置为 `0`。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001 N`（默认）| 正标量

将滑块从静态接触模式释放所需的最小力。

#### 依赖

要启用此参数，请将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### 转换器缓冲 A

### **Cylinder A end cushioning** — 是否建模活塞在最大伸出时的减速 `off`（默认）| `on`

是否建模活塞在最大伸出时的减速。有关更多信息，请参阅 Cylinder Cushion (IL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4 m^2`（默认）| 正标量

执行器缓冲元件内部柱塞的面积。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3 m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Cushion orifice area** — 缓冲腔室之间的节流孔面积 `1e-6 m^2`（默认）| 正标量

缓冲腔室之间节流孔的面积。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与套筒之间的间隙 `1e-7 m^2`（默认）| 正标量

缓冲柱塞与套筒之间的间隙面积。此值通过保持流动的连续性来贡献数值稳定性。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01 MPa`（默认）| 正标量

触发阀操作的阈值压力。当端口 **A** 与 *P*env 之间的压力差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve maximum pressure differential** — 最大缓冲压差 `0.1 MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持实际。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve maximum area** — 完全打开的缓冲阀面积 `1e-4 m^2`（默认）| 正标量

缓冲阀在完全打开位置的横截面积。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### **Check valve leakage area** — 完全关闭位置时缓冲阀间隙面积 `1e-10 m^2`（默认）| 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动的连续性来贡献数值稳定性。

#### 依赖

要启用此参数，请选择 **Cylinder A end cushioning**。

### 转换器缓冲 B

### **Cylinder B end cushioning** — 是否建模活塞在最大伸出时的减速 `off`（默认）| `on`

是否建模活塞在最大伸出时的减速。有关更多信息，请参阅 Cylinder Cushion (IL) 模块。

### **Cushion plunger cross-sectional area** — 缸体缓冲柱塞面积 `1e-4 m^2`（默认）| 正标量

执行器缓冲元件内部柱塞的面积。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Cushion plunger length** — 缓冲柱塞长度 `1e-3 m`（默认）| 正标量

缓冲柱塞的长度。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Cushion orifice area** — 缓冲腔室之间的节流孔面积 `1e-6 m^2`（默认）| 正标量

缓冲腔室之间节流孔的面积。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Leakage area between plunger and cushion sleeve** — 缓冲柱塞与套筒之间的间隙 `1e-7 m^2`（默认）| 正标量

缓冲柱塞与套筒之间的间隙面积。此值通过保持流动的连续性来贡献数值稳定性。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve cracking pressure differential** — 缓冲阈值压力 `0.01 MPa`（默认）| 正标量

触发阀操作的阈值压力。当端口 **A** 与 *P*env 之间的压力差达到或超过此参数的值时，缓冲阀开始打开。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve maximum pressure differential** — 最大缓冲压差 `0.1 MPa`（默认）| 正标量

最大缓冲阀压差。此参数为压力提供上限，以使系统压力保持实际。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve maximum area** — 完全打开的缓冲阀面积 `1e-4 m^2`（默认）| 正标量

缓冲阀在完全打开位置的横截面积。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Check valve leakage area** — 完全关闭位置时缓冲阀间隙面积 `1e-10 m^2`（默认）| 正标量

缓冲单向阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动的连续性来贡献数值稳定性。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当可变节流孔和单向阀处于接近打开或接近关闭位置时，为流动响应引入一层渐变。将此值设置为小于 1 的非零值，以提高在这些工况下仿真的稳定性。

#### 依赖

要启用此参数，请选择 **Cylinder B end cushioning**。

### 摩擦

### **Cylinder friction effect** — 是否建模阻碍活塞运动的摩擦 `off`（默认）| `on`

是否建模阻碍活塞运动的摩擦。该模块考虑库仑摩擦、Stribeck 摩擦和粘性摩擦。有关更多信息，请参阅 Cylinder Friction 模块。

### **Breakaway to Coulomb friction force ratio** — 分离力与库仑摩擦力之比 `1.2`（默认）| 正标量

分离力与库仑摩擦力之比。

#### 依赖

要启用此参数，请选择 **Cylinder friction**。

### **Breakaway friction velocity** — 运动阈值 `0.1` `m/s`（默认）| 正标量

克服摩擦力开始运动的阈值速度。

#### 依赖

要启用此参数，请选择 **Cylinder friction**。

### **Preload force** — 缸体上的初始力 `20 N`（默认）| 标量

缸体处于中立位置时施加在缸体上的力。

#### 依赖

要启用此参数，请选择 **Cylinder friction effect**。

### **Coulomb friction force coefficient** — 库仑摩擦力系数 `1e-6 N/Pa`（默认）| 正标量

库仑摩擦力系数。

#### 依赖

要启用此参数，请选择 **Cylinder friction effect**。

### **Viscous friction coefficient** — 粘性摩擦系数 `100 N/(m/s)`（默认）| 正标量

粘性摩擦系数。

#### 依赖

要启用此参数，请选择 **Cylinder friction effect**。

### 泄漏

### **Internal leakage** — 是否建模环形泄漏 `off`（默认）| `on`

是否建模参考环境条件下流体腔室与活塞储液器之间的环形泄漏。泄漏被视为层流。有关更多信息，请参阅 Laminar Leakage (IL) 模块。

#### 依赖

要启用此参数，请选择 **Same fluid on both sides**。

### **Piston-cylinder clearance** — 径向间隙 `1e-4 m`（默认）| 正标量

活塞杆与缸体壳体之间的径向距离。

#### 依赖

要启用此参数，请选择 **Same fluid on both sides** 和 **Internal leakage**。

### **Piston head length** — 活塞安装的环形长度 `0.01 m`（默认）| 正标量

活塞头的长度。

#### 依赖

要启用此参数，请选择 **Same fluid on both sides** 和 **Internal leakage**。

### 初始条件

### **Piston displacement from chamber A cap** — 确定活塞位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

确定活塞位置的方法。当设置为 `Provide input signal from
Multibody joint` 时，该模块可以从 Multibody 模块接收位置，或者
在内部计算位置并在端口 **p** 处报告位置。当机械方向为正时，位置
介于 `0` 和 **Piston stroke** 之间；当机械方向
为负时，位置介于 `0` 和
–**Piston stroke** 之间。

### **Initial piston displacement from chamber A cap** — 仿真开始时从腔室 A 端盖测量的活塞位置 `0 m`（默认）| 标量

仿真开始时相对于腔室 A 端盖的活塞位置。

#### 依赖关系

要启用此参数，请将 **Piston displacement from
chamber A cap** 设置为 `Calculate from velocity
of port R relative to port C`。

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `on`（默认）| `off`

是否对流体可压缩性引起的流体密度变化进行建模。当您选中 **Enable dynamic
compressibility** 时，除了压力变化引起的密度变化外，还会计算
流入模块的质量流量引起的密度变化。在 Isothermal Liquid 库中，所有模块
都将密度计算为压力的函数。

### **Initial liquid pressure in chamber A** — 腔室 A 中的起始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic
compressibility**。

### **Initial liquid pressure in chamber B** — 腔室 B 中的起始液体压力 `0.101325 MPa`（默认）| 正标量

可压缩流体的起始液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic
compressibility**。

### **Nominal liquid pressure in chamber A** — 腔室 A 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 A 中额定工况下的液体压力。当动态可压缩性
被禁用时，该模块使用此值来计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic
compressibility** 复选框。

### **Nominal liquid pressure in chamber B** — 腔室 B 中额定工况下的压力 `0.101325 MPa`（默认）| 标量

腔室 B 中额定工况下的液体压力。当动态可压缩性
被禁用时，该模块使用此值来计算质量守恒方程中使用的额定密度。

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

### R2024a：在执行器每一侧对不同的流体建模

清除新的 **Same fluid on both sides** 参数，以阻止
流体属性的传播，并将每个腔室建模为连接到其自身隔离流体网络的
不同流体。

### R2023a：新的硬限位参数化选项

该模块为 **Hard stop model** 参数提供了一个新选项。
此选项称为 `Based on coefficient of restitution`，
使用模式图对硬限位进行建模。

## 描述

等温液体系统中压力差到执行器动作的线性转换

Double-Acting Actuator (IL) 模块表示两个腔室之间的压力差到活塞运动的线性
转换。活塞动作由作用在分隔腔室的活塞板上的压力差控制。当活塞接近完全伸出或完全
缩回时，其运动受到四种硬限位模型之一的限制。两个活塞腔室中可选地
对流体可压缩性进行建模。

端口 **A** 和 **B** 是等温液体入口。端口
**C** 表示执行器壳体，而活塞速度在端口 **R** 处返回。当活塞位置在内部
计算时，它在端口 **p** 处报告；当位置由连接到 Simscape™
Multibody™ 关节设置时，它作为物理信号在端口
**p** 处接收。

您可以使用 **Mechanical
orientation** 参数定义活塞位移方向。如果机械方向设置为
`Pressure at A causes positive displacement of R relative to
C`，则当压力差
*p*A –
*p*B 为正时，活塞伸出。如果 **Mechanical
orientation** 设置为 `Pressure at A causes negative
displacement of R relative to C`，则当液体腔室和气体腔室之间的压力差为正时，
活塞缩回。

### 位移

活塞位移测量为端口 **R** 相对于端口 **C** 的位置。**Mechanical orientation**
标识活塞位移的方向。当腔室 A 体积等于腔室死区
体积时，活塞位移为中性，即 `0`。当位移作为输入接收时，请确保
位置的导数等于活塞速度。当输入从 Translational Multibody Interface 模块
连接到 Simscape Multibody 关节接收时，自动满足此条件。

### 硬限位模型

为避免执行器在完全伸出或完全缩回时发生机械损坏，执行器通常在活塞接近这些
限位时表现出非线性行为。Double-Acting Actuator (IL) 模块通过四种硬限位模型
来对此行为建模，这些模型通过弹簧-阻尼系统对材料柔度进行建模。硬限位模型包括：

- `Stiffness and damping applied smoothly through transition
  region, damped rebound`。
- `Full stiffness and damping applied at bounds, undamped
  rebound`。
- `Full stiffness and damping applied at bounds, damped
  rebound`。
- `Based on coefficient of restitution`

当活塞处于其上限或下限时，对硬限位力进行建模。边界区域位于
**Piston stroke** 或活塞初始位移的 **Transition region** 内。
在此区域之外，FHardStop=0。

有关这些设置的更多信息，请参阅 Translational Hard Stop 模块页面。

### 缓冲

该模块可以对活塞行程极限附近的缓冲进行建模。选中
**Cylinder end cushioning** 以在活塞接近由 **Piston stroke**
参数定义的最大伸出时减慢活塞运动。有关气缸缓冲功能的更多信息，请参阅
Cylinder Cushion (IL) 模块。

### 摩擦

该模块可以对阻碍活塞运动的摩擦进行建模。当您选中
**Cylinder friction** 时，产生的摩擦是 Stribeck、Coulomb 和粘性效应的
组合。该模块测量腔室压力与环境压力之间的压力
差。有关摩擦模型及其限制的更多信息，请参阅 Cylinder Friction
(IL) 模块。

### 泄漏

您可以选择性地对腔室 A 和腔室 B 之间的泄漏进行建模。当两个腔室中的流体
相同且您选中 **Internal leakage** 时，将在活塞和气缸之间对
Poiseuille 流进行建模。该模块使用
Simscape Foundation Library Laminar Leakage (IL) 模块。流量
计算如下：

m˙=π128(d04−di4−(d02−di2)2log(d0/di))υL(pA−pB),

其中：

- *ν* 是流体运动粘度。
- *L* 是活塞长度，**p** –
  *P*0。
- *p*A 是端口
  **A** 处的压力。
- *p*B 是端口
  **B** 处的压力。

气缸直径 *d*0
为 d0=di+2c，其中 *c* 是 **Piston-cylinder
clearance**，活塞直径
*d*i 为 di=4APπ，其中 *A*P 是
**Piston cross-sectional area in chamber A** 和
**Piston cross-sectional area in chamber B** 参数的平均值。

### 数值平滑的面积和压力

您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值
鲁棒性。如果 **Smoothing factor** 参数非零，该模块将平滑
缓冲 A 和 B 的孔口面积以及单向阀压力范围。孔口
面积在缓冲 A 和缓冲 B 的 **Leakage
area between plunger and cushion sleeve** 和 **Cushion
plunger cross-sectional area** 参数之间平滑饱和，而阀压力在
缓冲 A 和缓冲 B 的 **Check valve cracking
pressure differential** 和 **Check valve maximum pressure
differential** 参数之间饱和。有关更多信息，请参阅数值平滑。

### 模块原理图

Double-Acting Actuator (IL) 模块包含四个 Simscape Foundation 模块：

- Laminar Leakage (IL)
- Translational Mechanical Converter (IL)
- Translational Hard Stop
- Ideal Translational Motion Sensor

以及两个 Isothermal Liquid 库模块：

- Cylinder Cushion (IL)
- Cylinder Friction (IL)

### 动量平衡

执行器的动量守恒方程为

F= ε(SApA−SBpB−SRodpenv)

其中：

- *F* 是液体施加在转换器
  界面上的力。此力表达式不考虑硬限位、气缸缓冲或气缸
  摩擦子组件产生的力贡献。要查看这些力对
  转换器界面的贡献，请参阅这些子组件的文档页面。
- *ε* 取决于转换器的 **Mechanical
  orientation**。如果 **Mechanical
  orientation** 为 `Pressure at A causes
  positive displacement of R relative to C`，
  则 *ε* `= 1`。如果
  **Mechanical orientation** 为
  `Pressure at A causes negative displacement of R
  relative to C`，则 *ε* `=
  -1`。
- *SRod* 是活塞杆
  横截面积，其中SRod=SA−SB。
- *SA* 是
  **Piston cross-sectional area in chamber A**
  参数的值。
- *SB* 是
  **Piston cross-sectional area in chamber B**
  参数的值。
- *pA* 是腔室 A 内部的压力。
- *pB* 是腔室 B 内部的压力。
- *penv* 是环境
  压力。
