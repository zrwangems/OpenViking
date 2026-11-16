---
type: simulink-block
title: 'Vehicle Body 3DOF Longitudinal'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Vehicle Dynamics'
documentation_page: 'vehiclebody3doflongitudinal'
documentation_source_path: 'ref/vehiclebody3doflongitudinal.html'
language: zh-CN
chinese_source: worker-translation
---

# Vehicle Body 3DOF Longitudinal

## 端口

### 输入

### **FExt** — 车辆质心上的外部力 `array`

施加到车辆质心的外部力，
*Fxext*,
*Fyext*,
*Fzext*，在车辆固定坐标系中，单位为 N。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖项

要启用此端口，请选择 **External forces**。

### **MExt** — 车辆质心上的外部力矩 `array`

车辆质心上的外部力矩，
*Mx*,
*My*,
*Mz*，在车辆固定坐标系中，单位为 N·m。信号向量维度为
`[1x3]` 或 `[3x1]`。

#### 依赖项

要启用此端口，请选择 **External moments**。

### **FwF** — 前轴上的总纵向力 `scalar`

前轴上的纵向力，
*FwF*，沿车辆固定 *x* 轴，单位为 N。

### **FwR** — 后轴上的总纵向力 `scalar`

后轴上的纵向力，
*FwR*，沿车辆固定 *x* 轴，单位为 N。

### **Grade** — 道路坡度角 `scalar`

道路坡度角，γ，单位为 deg。

### **FsF** — 前轴每个车轮的悬架力 `vector`

前轴上的悬架力，
*FsF*，沿车辆固定 *z* 轴，单位为 N。

#### 依赖项

要启用此端口，对于 **Ground interaction type** 参数，请选择 `External suspension`。

### **FsR** — 后轴每个车轮的悬架力 `vector`

后轴上的悬架力，
*FsR*，沿车辆固定 *z* 轴，单位为 N。

#### 依赖项

要启用此端口，对于 **Ground interaction type** 参数，请选择 `External suspension`。

### **WindXYZ** — 风速 `array`

风速，*WX*,
*WY*,
*WZ*，沿地球固定 *X* 轴、*Y* 轴和 *Z* 轴，单位为 m/s。信号向量维度为
`[1x3]` 或 `[3x1]`。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，
*Tair*，单位为 K。如果您希望在运行期间改变温度，请考虑此选项。

#### 依赖项

要启用此端口，请选择 **Air temperature**。

### **zF,R** — 前轴和后轴位置 `vector`

沿车辆固定 *z* 轴的前轴和后轴位置，Z¯F,Z¯R，单位为 m。

#### 依赖项

要启用此端口，对于 **Ground interaction type** 参数，请选择 `Axle displacement, velocity`。

### **zdotF,R** — 前轴和后轴速度 `vector`

沿车辆固定 *z* 轴的前轴和后轴速度，Z¯˙F,Z¯˙R，单位为 m/s。

#### 依赖项

要启用此端口，对于 **Ground interaction type** 参数，请选择 `Axle displacement, velocity`。

### 输出

### **Info** — 总线信号 bus

包含这些模块值的总线信号。

| 信号 | | | | | 描述 | 值 | 单位 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `InertFrm` | `Cg` | `Disp` | `X` | | 车辆质心沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 车辆质心沿地球固定 *Y* 轴的位移 | `0` | m |
| `Z` | | 车辆质心沿地球固定 *Z* 轴的位移 | Computed | m |
| `Vel` | `Xdot` | | 车辆质心沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 车辆质心沿地球固定 *Y* 轴的速度 | `0` | m/s |
| `Zdot` | | 车辆质心沿地球固定 *Z* 轴的速度 | Computed | m/s |
| `Ang` | `phi` | | 车辆固定坐标系绕地球固定 *X* 轴的旋转（侧倾） | `0` | rad |
| `theta` | | 车辆固定坐标系绕地球固定 *Y* 轴的旋转（俯仰） | Computed | rad |
| `psi` | | 车辆固定坐标系绕地球固定 *Z* 轴的旋转（横摆） | `0` | rad |
| `FrntAxl` | `Disp` | `X` | | 前轴沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 前轴沿地球固定 *Y* 轴的位移 | `0` | m |
| `Z` | | 前轴沿地球固定 *Z* 轴的位移 | Computed | m |
| `Vel` | `Xdot` | | 前轴沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 前轴沿地球固定 *Y* 轴的速度 | `0` | m/s |
| `Zdot` | | 前轴沿地球固定 *Z* 轴的速度 | Computed | m/s |
| `RearAxl` | `Disp` | `X` | | 后轴沿地球固定 *X* 轴的位移 | Computed | m |
| `Y` | | 后轴沿地球固定 *Y* 轴的位移 | `0` | m |
| `Z` | | 后轴沿地球固定 *Z* 轴的位移 | Computed | m |
| `Vel` | `Xdot` | | 后轴沿地球固定 *X* 轴的速度 | Computed | m/s |
| `Ydot` | | 后轴沿地球固定 *Y* 轴的速度 | `0` | m/s |
| `Zdot` | | 后轴沿地球固定 *Z* 轴的速度 | Computed | m/s |
| `BdyFrm` | `Cg` | `Disp` | `x` | | 车辆质心沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 车辆质心沿车辆固定 *y* 轴的位移 | `0` | m |
| `z` | | 车辆质心沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 车辆质心沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 车辆质心沿车辆固定 *y* 轴的速度 | `0` | m/s |
| `zdot` | | 车辆质心沿车辆固定 *z* 轴的速度 | Computed | m/s |
| `AngVel` | `p` | | 车辆绕车辆固定 *x* 轴的角速度（侧倾速率） | `0` | rad/s |
| `q` | | 车辆绕车辆固定 y 轴的角速度（俯仰速率） | Computed | rad/s |
| `r` | | 车辆绕车辆固定 *z* 轴的角速度（横摆速率） | `0` | rad/s |
| `Accel` | `ax` | | 车辆质心沿车辆固定 *x* 轴的加速度 | Computed | gn |
| `ay` | | 车辆质心沿车辆固定 *y* 轴的加速度 | `0` | gn |
| `az` | | 车辆质心沿车辆固定 *z* 轴的加速度 | Computed | gn |
| `Forces` | `Body` | `Fx` | | 车辆质心沿车辆固定 *x* 轴的净力 | Computed | N |
| `Fy` | | 车辆质心沿车辆固定 *y* 轴的净力 | `0` | N |
| `Fz` | | 车辆质心沿车辆固定 *z* 轴的净力 | Computed | N |
| `Ext` | `Fx` | | 车辆质心沿车辆固定 *x* 轴的外部力 | `Computed` | N |
| `Fy` | | 车辆质心沿车辆固定 *y* 轴的外部力 | `Computed` | N |
| `Fz` | | 车辆质心沿车辆固定 *z* 轴的外部力 | `Computed` | N |
| `FrntAxl` | `Fx` | | 前轴沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 前轴沿车辆固定 *y* 轴的横向力 | `0` | N |
| `Fz` | | 前轴沿车辆固定 *z* 轴的法向力 | Computed | N |
| `RearAxl` | `Fx` | | 后轴沿车辆固定 *x* 轴的纵向力 | Computed | N |
| `Fy` | | 后轴沿车辆固定 *y* 轴的横向力 | `0` | N |
| `Fz` | | 后轴沿车辆固定 *z* 轴的法向力 | Computed | N |
| `Tires` | `FrntTire` | `Fx` | 前轮胎力，沿车辆固定 *x* 轴 | `0` | N |
| `Fy` | 前轮胎力，沿车辆固定 *y* 轴 | `0` | N |
| `Fz` | 前轮胎力，沿车辆固定 *z* 轴 | Computed | N |
| `RearTire` | `Fx` | 后轮胎力，沿车辆固定 *x* 轴 | `0` | N |
| `Fy` | 后轮胎力，沿车辆固定 *y* 轴 | `0` | N |
| `Fz` | 后轮胎力，沿车辆固定 *z* 轴 | Computed | N |
| `Drag` | `Fx` | | 车辆质心沿车辆固定 *x* 轴的阻力 | Computed | N |
| `Fy` | | 车辆质心沿车辆固定 *y* 轴的阻力 | Computed | N |
| `Fz` | | 车辆质心沿车辆固定 *z* 轴的阻力 | Computed | N |
| `Grvty` | `Fx` | | 车辆质心沿车辆固定 *x* 轴的重力 | Computed | N |
| `Fy` | | 车辆质心沿车辆固定 *y* 轴的重力 | `0` | N |
| `Fz` | | 车辆质心沿车辆固定 *z* 轴的重力 | Computed | N |
| `Moments` | `Body` | `Mx` | | 车辆质心绕车辆固定 *x* 轴的车身力矩 | `0` | N·m |
| `My` | | 车辆质心绕车辆固定 *y* 轴的车身力矩 | Computed | N·m |
| `Mz` | | 车辆质心绕车辆固定 *z* 轴的车身力矩 | `0` | N·m |
| `Drag` | `Mx` | | 车辆质心绕车辆固定 *x* 轴的阻力力矩 | `0` | N·m |
| `My` | | 车辆质心绕车辆固定 *y* 轴的阻力力矩 | Computed | N·m |
| `Mz` | | 车辆质心绕车辆固定 *z* 轴的阻力力矩 | `0` | N·m |
| `Ext` | `Fx` | | 车辆质心绕车辆固定 *x* 轴的外部力矩 | `Computed` | N·m |
| `Fy` | | 车辆质心绕车辆固定 *y* 轴的外部力矩 | `Computed` | N·m |
| `Fz` | | 车辆质心绕车辆固定 *z* 轴的外部力矩 | `Computed` | N·m |
| `FrntAxl` | `Disp` | `x` | | 前轴沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 前轴沿车辆固定 *y* 轴的位移 | `0` | m |
| `z` | | 前轴沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 前轴沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 前轴沿车辆固定 *y* 轴的速度 | `0` | m/s |
| `zdot` | | 前轴沿车辆固定 *z* 轴的速度 | Computed | m/s |
| `Steer` | `WhlAngFL` | | 前左车轮转向角 | Computed | rad |
| `WhlAngFR` | | 前右车轮转向角 | Computed | rad |
| `RearAxl` | `Disp` | `x` | | 后轴沿车辆固定 *x* 轴的位移 | Computed | m |
| `y` | | 后轴沿车辆固定 *y* 轴的位移 | `0` | m |
| `z` | | 后轴沿车辆固定 *z* 轴的位移 | Computed | m |
| `Vel` | `xdot` | | 后轴沿车辆固定 *x* 轴的速度 | Computed | m/s |
| `ydot` | | 后轴沿车辆固定 *y* 轴的速度 | `0` | m/s |
| `zdot` | | 后轴沿车辆固定 *z* 轴的速度 | Computed | m/s |
| `Steer` | `WhlAngRL` | | 后左车轮转向角 | Computed | rad |
| `WhlAngRR` | | 后右车轮转向角 | Computed | rad |
| `Pwr` | `PwrExt` | | | 施加的外部功率 | Computed | W |
| `Drag` | | | 阻力导致的功率损失 | Computed | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrFxExt` | | | 外部施加的纵向力功率 | Computed | W |
| `PwrFzExt` | | | 外部施加的纵向力功率 | Computed | W |
| `PwrMyExt` | | | 外部施加的俯仰力矩功率 | Computed | W |
| `PwrFwFx` | | | 施加在前轴上的纵向力 | Computed | W |
| `PwrFwRx` | | | 施加在后轴上的纵向力 | Computed | W |
| `PwrNotTrnsfrd` | `PwrFsF` | | | 前轴处悬架与车身之间传递的内部功率 | Computed | W |
| `PwrFsR` | | | 后轴处悬架与车身之间传递的内部功率 | Computed | W |
| `PwrFxDrag` | | | 纵向阻力功率 | Computed | W |
| `PwrFzDrag` | | | 垂向阻力功率 | Computed | W |
| `PwrMyDrag` | | | 阻力俯仰力矩功率 | Computed | W |
| `PwrFsb` | | | 总悬架阻尼功率 | Computed | W |
| `PwrStored` | `PwrStoredGrvty` | | | 重力势能变化率 | Computed | W |
| `PwrStoredxdot` | | | 纵向动能变化率 | Computed | W |
| `PwrStoredzdot` | | | 垂向动能变化率 | Computed | W |
| `PwrStoredq` | | | 俯仰转动动能变化率 | Computed | W |
| `PwrStoredFsFzSprng` | | | 前悬架存储的弹簧能量 | Computed | W |
| `PwrStoredFsRzSprng` | | | 后悬架存储的弹簧能量 | Computed | W |

### **xdot** — 车辆纵向速度 `scalar`

车辆质心沿车辆固定 *x* 轴的速度，单位为 m/s。

### **FzF** — 前轮法向力 `scalar`

前轮单个车轮的法向力，
*FzF*，沿车辆固定 *z* 轴，单位为 N。

### **FzR** — 后轮法向力 `scalar`

后轮单个车轮的法向力，
*FzR*，沿车辆固定 *z* 轴，单位为 N。

## 参数

#### 选项

### **Ground interaction type** — 车轴与车辆的连接 `Grade angle` (default) | `Axle displacement, velocity` | `External suspension`

指定车轴与车辆的连接类型：

- `Grade angle` — 从路面到车轴的垂向车轴位移保持恒定。模块使用表格化刚度和阻尼参数来建模作用在车身与车轴之间的悬架力。
- `Axle displacement, velocity` — 车轴具有相对于道路坡度的输入提供的垂向位移和速度。模块使用表格化刚度和阻尼参数来建模作用在车身与车轴之间的悬架力。
- `External suspension` — 车轴具有外部施加的力，用于将车身耦合到自定义悬架模型。

### **External forces** — `FExt` 输入端口 `off` (default) | `on`

指定以创建输入端口 `FExt`。

### **External moments** — `MExt` 输入端口 `off` (default) | `on`

指定以创建输入端口 `MExt`。

### **Air temperature** — `AirTemp` 输入端口 `off` (default) | `on`

指定以创建输入端口 `AirTemp`。

#### 纵向

### **Number of wheels on front axle, NF** — 前轮数量 `2` (default) | `scalar`

前轴上的车轮数量，
*NF*。该值无量纲。

### **Number of wheels on rear axle, NR** — 后轮数量 `2` (default) | `scalar`

后轴上的车轮数量，
*NR*。该值无量纲。

### **Mass, m** — 车辆质量 `1200` (default) | `scalar`

车辆质量，*m*，单位为 kg。

### **Horizontal distance from CG to front axle, a** — 前轴距离 `1.4` (default) | `scalar`

从车辆质心到前轮轴的水平距离 *a*，单位为 m。

### **Horizontal distance from CG to rear axle, b** — 后轴距离 `1.8` (default) | `scalar`

从车辆质心到后轮轴的水平距离 *b*，单位为 m。

### **CG height above axles, h** — 高度 `0.35` (default) | `scalar`

车辆质心高于车轴的高度，*h*，单位为 m。

### **Longitudinal drag coefficient, Cd** — 阻力 `.3` (default) | `scalar`

空气阻力系数，*Cd*。该值无量纲。

### **Frontal area, Af** — 面积 `2` (default) | `scalar`

用于计算车辆气动阻力的有效车辆横截面积，
*Af*，单位为 m^2。

### **Initial position, x\_o** — 位置 `0` (default) | `scalar`

车身沿地球固定 *x* 轴的纵向初始位置，
*xo*，单位为 m。

### **Initial velocity, xdot\_o** — 速度 `0` (default) | `scalar`

车身沿地球固定 *x* 轴的纵向初始速度，x˙0，单位为 m/s。

#### 垂向

### **Longitudinal lift coefficient, Cl** — 升力 `.1` (default) | `scalar`

升力系数，*Cl*。该值无量纲。

### **Initial vertical position, z\_o** — 位置 `-.35` (default) | `scalar`

沿车辆固定 *z* 轴的初始垂向质心位置，
*zo*，单位为 m。

### **Initial vertical velocity, zdot\_o** — 速度 `0` (default) | `scalar`

沿车辆固定 *z* 轴的初始垂向质心速度，
*zdoto*，单位为 m。

#### 俯仰

### **Inertia, Iyy** — 绕车身 `y` 轴 `3500` (default) | `scalar`

车身绕车身 *y* 轴的转动惯量。

### **Longitudinal drag pitch moment, Cpm** — 阻力系数 `.1` (default) | `scalar`

俯仰阻力矩系数。该值无量纲。

### **Initial pitch angle, theta\_o** — 俯仰 `0` (default) | `scalar`

绕车身 *y* 轴的初始俯仰角，单位为 rad。

### **Initial angular velocity, q\_o** — 俯仰速度 `0` (default) | `scalar`

绕车身 *y* 轴的初始车身角速度，单位为 rad/s。

#### 悬架

### **Front axle stiffness force data, FskF** — 力 `[-50, -1, 0, 2, 3, 52].*1.5e4` (default) | `vector`

前轴刚度力数据，
*FkF*，单位为 N。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

### **Front axle displacement data, dzsF** — 位移 `[-5e-3, -1e-4, 0, .2, .2001, .2051]` (default) | `vector`

前轴位移数据，单位为 m。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

### **Front axle damping force data, FsbF** — 阻尼力 `[-10000 -100 -10 0 10 100 10000]` (default) | `vector`

前轴阻尼力，单位为 N。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

### **Front axle velocity data, dzdotsF** — 速度 `[-10 -1 -.1 0 .1 1 10]` (default) | `vector`

前轴速度数据，单位为 m/s。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

### **Rear axle stiffness force data, FskR** — 力 `[-50, -1, 0, 2, 3, 52].*1e4` (default) | `vector`

后轴刚度力数据，单位为 N。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

### **Rear axle displacement data, dzsR** — 位移 `[-5e-3, -1e-4, 0, .2, .2001, .2051]` (default) | `vector`

后轴位移数据，单位为 m。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

### **Rear axle damping force data, FsbR** — 阻尼力 `[-10000 -100 -10 0 10 100 10000]` (default) | `vector`

后轴阻尼力，单位为 N。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

### **Rear axle velocity data, dzdotsR** — 速度 `[-10 -1 -.1 0 .1 1 10]` (default) | `vector`

后轴速度数据，单位为 m/s。

#### 依赖项

要启用此参数，对于 **Ground interaction type** 参数，请选择 `Grade angle` 或 `Axle displacement, velocity`。

#### 环境

### **Absolute air pressure, Pabs** — 压力 `101325` (default) | `scalar`

环境空气绝对压力，*Pabs*，单位为 Pa。

### **Air temperature, Tair** — 环境空气温度 `273` (default) | `scalar`

环境空气温度，*Tair*，单位为 K。

#### 依赖项

要启用此参数，请清除 **Air temperature**。

### **Gravitational acceleration, g** — 重力 `9.81` (default)

重力加速度，*g*，单位为 m/s2。

## 所属库

Powertrain Blockset / Vehicle Dynamics Vehicle Dynamics Blockset / Vehicle Body

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

3DOF 刚性车身，用于计算纵向、垂向和俯仰运动

Vehicle Body 3DOF Longitudinal 模块实现一个三自由度 (3DOF) 刚性车身模型，具有可配置的车轴刚度，用于计算纵向、垂向和俯仰运动。该模块考虑车身质量、气动阻力、道路倾角以及由于加速度和道路轮廓引起的前后轴之间的重量分布。

您可以指定车轴与车辆的连接类型：

- Grade angle — 从路面到车轴的垂向车轴位移保持恒定。模块使用表格化刚度和阻尼参数来建模作用在车身与车轴之间的悬架力。
- Axle displacement — 车轴具有相对于道路坡度的输入提供的垂向位移和速度。模块使用表格化刚度和阻尼参数来建模作用在车身与车轴之间的悬架力。
- External suspension — 车轴具有外部施加的力，用于将车身耦合到自定义悬架模型。

如果垂向和俯仰运动引起的重量转移不可忽略，请考虑使用此模块来表示动力总成和燃油经济性研究中的车辆运动。例如，在重度制动或加速，或道路轮廓包含较大垂向变化的研究中。

该模块使用刚体车辆运动、悬架系统力以及风力和阻力来计算前轴和后轴上的法向力。该模块在刚性车身坐标系上求解力分量和力矩：

Fx=FwF+FwR−Fd,x−Fsx,F−Fsx,R+Fg,xFz=Fd,z−Fsz,F−Fsz,R+Fg,zMy=aFsz,F−bFsz,R+h(FwF+FwR+Fsx,F+Fsx,R)−Md,y

倾斜车辆示意图

### 刚体车辆运动

车辆车轴平行并形成一个平面。纵向方向位于该平面内，并垂直于车轴。如果车辆在倾斜坡面上行驶，法向方向不平行于重力，但始终垂直于车轴-纵向平面。

该模块使用作用在其上的所有力和力矩的净效应来确定车辆运动。纵向轮胎力推动车辆前进或后退。车辆的重量通过其质心 (CG) 起作用。根据倾斜角，重量将车辆拉向地面，并向前或向后拉。无论车辆向前还是向后行驶，气动阻力都会使其减速。为简单起见，假设阻力通过质心作用。

Vehicle Body 3DOF Longitudinal 实现以下方程。

x¨=Fxm−qzz¨=Fzm−qxq˙=MyIyyθ˙=q

### 悬架系统力

如果将模块的 **Ground interaction type** 参数配置为 `Grade angle` 或 `Axle displacement, velocity`，则该模块使用非线性刚度和阻尼参数来建模悬架系统。

前轴和后轴悬架力由下式给出：

FsF=NF[FkF+FbF]FsR=NR[FkR+FbR]

该模块使用查找表来实现前悬架和后悬架刚度。为了考虑运动学和材料非线性，包括与限位块的碰撞，这些表是行程的函数。

FkF=f(dZF)FkR=f(dZR)

该模块使用查找表来实现前悬架和后悬架阻尼。为了考虑非线性、压缩和回弹，这些表是行程速率的函数。

FbF=f(dZ˙F)FbR=f(dZ˙R)

行程是车辆垂向位置与车轴位置之差。行程速率是垂向速度与车轴速度之差。

dZF=ZF−Z¯FdZR=ZR−Z¯RdZ˙F=Z˙F−Z¯˙FdZ˙R=Z˙R−Z¯˙R

当 **Ground interaction type** 参数为 `Grade angle` 时，车轴垂向位置 (Z¯F,Z¯R) 和速度 (Z¯˙F,Z¯˙R) 设置为 `0`。

### 风力和阻力

该模块从车辆速度分量中减去风速，以获得净相对空速。为了计算作用在车辆上的阻力和力矩，该模块使用净相对空速：

Fd,x=12TRCdAfPabs(x˙−wx)2Fd,z=12TRClAfPabs(x˙−wx)2Md,y=12TRCpmAfPabs(x˙−wx)2(a+b)

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrFxExt` | 外部施加的纵向力功率 | PFxExt=FxExtx˙ |
| `PwrFzExt` | 外部施加的纵向力功率 | PFzExt=FzExtz˙ |
| `PwrMyExt` | 外部施加的俯仰力矩功率 | PMzExt=MzExtθ˙ |
| `PwrFwFx` | 施加在前轴上的纵向力 | PFwFx=FwFx˙ |
| `PwrFwRx` | 施加在后轴上的纵向力 | PFwRx=FwRx˙ |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFsF` | 前轴处悬架与车身之间传递的内部功率 | PFs,F=−PFwFx+PFsbF+PFsk,F+FxFx˙F+FzFz˙F |
| `PwrFsR` | 后轴处悬架与车身之间传递的内部功率 | PFs,R=−PFwRx+PFsb,R+PFsk,R+FxFx˙F+FzFz˙F |
| `PwrFxDrag` | 纵向阻力功率 | Pd,x=Fd,xx˙ |
| `PwrFzDrag` | 垂向阻力功率 | Pd,z=Fd,zz˙ |
| `PwrMyDrag` | 阻力俯仰力矩功率 | Pd,My=Md,yθ˙ |
| `PwrFsb` | 总悬架阻尼功率 | PFsb=∑i=F,RFsb,iz˙i |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredGrvty` | 重力势能变化率 | Pg=−mgZ˙ |
| `PwrStoredxdot` | 纵向动能变化率 | Px˙=mx¨x˙ |
| `PwrStoredzdot` | 垂向动能变化率 | Pz˙=mz¨z˙ |
| `PwrStoredq` | 俯仰转动动能变化率 | Pθ˙=Iyyθ¨θ˙ |
| `PwrStoredFsFzSprng` | 前悬架存储的弹簧能量 | PFskF=Fsk,Fz˙F |
| `PwrStoredFsRzSprng` | 后悬架存储的弹簧能量 | PFskF=Fsk,Rz˙R |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Fx* | 车辆上的纵向力 |
| *Fz* | 车辆上的法向力 |
| *My* | 车辆绕车辆固定 *y* 轴的力矩 |
| *FwF*, *FwR* | 沿车辆固定 *x* 轴作用在前轴和后轴上的纵向力 |
| *Fd,x*, *Fd,z* | 车辆质心上的纵向阻力和法向阻力 |
| *Fsx,F*, *Fsx,R* | 前轴和后轴上的纵向悬架力 |
| *Fsz,F*, *Fsz,R* | 前轴和后轴上的法向悬架力 |
| *Fg,x*,*Fg,z* | 沿车辆固定坐标系作用在车辆上的纵向重力和法向重力 |
| *Md,y* | 车辆绕车辆固定 *y* 轴的阻力力矩 |
| *a*,*b* | 前轴和后轴分别距车辆质心在公共车轴平面上的法向投影点的距离 |
| *h* | 沿车辆固定 *z* 轴，车辆质心高于车轴平面的高度 |
| *FsF*, *FsR* | 沿车辆固定 *z* 轴的前轴和后轴悬架力 |
| *ZwF*, *ZwR* | 沿地球固定 *z* 轴的前后车辆法向位置 |
| *Θ* | 车辆绕车辆固定 *y* 轴的俯仰角 |
| *m* | 车身质量 |
| *NF*, *NR* | 前轮和后轮数量 |
| *Iyy* | 车身绕车辆固定 *y* 轴的转动惯量 |
| *x*, x˙, x¨ | 沿车辆固定 *x* 轴的车辆纵向位置、速度和加速度 |
| z, z˙, z¨ | 沿车辆固定 *z* 轴的车辆法向位置、速度和加速度 |
| *FkF*, *FkR* | 沿车辆固定 *z* 轴的前轮和后轮悬架刚度力 |
| *FbF*, *FbR* | 沿车辆固定 *z* 轴的前轮和后轮悬架阻尼力 |
| *ZF*, *ZR* | 沿地球固定 *Z* 轴的前后车辆垂向位置 |
| Z˙F,Z˙R | 沿车辆固定 *z* 轴的前后车辆垂向速度 |
| Z¯F,Z¯R | 沿车辆固定 *z* 轴的前后车轮车轴垂向位置 |
| Z¯˙F,Z¯˙R | 沿地球固定 *z* 轴的前后车轮车轴垂向速度 |
| *dZF*, *dZR* | 沿车辆固定 *z* 轴的前后轴悬架挠度 |
| dZ˙F,dZ˙R | 沿车辆固定 *z* 轴的前后轴悬架挠度率 |
| *Cd* | 沿车辆固定 *x* 轴作用的前部空气阻力系数 |
| *Cl* | 沿车辆固定 *z* 轴作用的侧向空气阻力系数 |
| *Cpm* | 作用在车辆俯仰平面内或绕车辆固定 *y* 轴的气动俯仰力矩系数 |
| *Af* | 前部面积 |
| *Pabs* | 环境绝对压力 |
| *R* | 大气比气体常数 |
| *T* | 环境空气温度 |
| *wx* | 沿车辆固定 *x* 轴的风速 |
